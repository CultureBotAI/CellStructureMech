"""Preserve relation types and experimental limits in trypanosome structures."""

from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]


def record(slug):
    return yaml.safe_load(
        (ROOT / "data/structures/cytoskeleton" / f"{slug}.yaml").read_text()
    )


def test_bilobe_cytoskeleton_link_is_parthood():
    doc = record("bilobe_structure")
    assert doc["identifier"] == "GO:0120120"
    assert "GO:0005856" not in doc.get("parent_structures", [])
    assert "GO:0005856" in doc.get("part_of", [])
    assert doc["causal_graphs"][0]["scope_status"] == "NONMECHANISTIC"


@pytest.mark.parametrize("owner", ["component", "function"])
def test_centrin_arm_source_notes_distinguish_hook_terminology(owner):
    doc = record("ciliary_centrin_arm")
    entry = doc["components"][0] if owner == "component" else doc["functions"][0]
    note = next(
        e["notes"] for e in entry["evidence"]
        if e["reference"] == "DOI:10.3390/cells4040726"
    )
    assert "Centrin4-positive centrin arm" in note
    assert "MORN1-positive hook complex" in note
    assert "historical" in note
    assert doc["components"][0]["essentiality"] == "UNKNOWN"


def test_centrin_arm_occurrence_is_not_identity_with_hook():
    note = record("ciliary_centrin_arm")["taxonomic_distribution"][0]["note"]
    assert "alongside the trypanosome hook complex" in note
    assert "arm of the trypanosome hook complex" not in note


def test_three_collar_proteins_have_the_later_primary_citation():
    taxon = record("ciliary_pocket_collar")["taxonomic_distribution"][0]
    assert taxon["taxon_id"] == "NCBITaxon:5691"
    assert taxon["reference"] == "DOI:10.1371/journal.ppat.1009329"
    assert all(name in taxon["note"] for name in ("BILBO1", "FPC4", "BILBO2"))


def test_fpc4_native_link_is_proposed_but_binding_is_supported():
    doc = record("ciliary_pocket_collar")
    fpc4 = next(c for c in doc["components"] if c["component_id"] == "fpc4")
    assert "proposed to link" in fpc4["role"]
    edges = doc["causal_graphs"][0]["edges"]
    edge = next(e for e in edges if e["subject"] == "fpc4" and e["object"] == "microtubules")
    assert edge["predicate"] == "binds"
    assert "in vitro" in edge["description"]
    assert "possible proximal" in edge["evidence"][0]["notes"]


def test_faz1_rnai_does_not_establish_null_assembly_essentiality():
    doc = record("flagellum_attachment_zone")
    components = {c["component_id"]: c for c in doc["components"]}
    assert components["faz1"]["essentiality"] == "UNKNOWN"
    note = next(
        e["notes"] for e in components["faz1"]["evidence"]
        if e["reference"] == "DOI:10.1016/j.protis.2007.08.005"
    )
    assert "RNAi left aberrant FAZ-like structures" in note
    assert "does not establish complete protein absence" in note
    assert "not an absolute block of FAZ formation" in note
    assert "required for normal" in components["faz1"]["role"]
    assert components["faz2"]["essentiality"] == components["cc2d"]["essentiality"] == "UNKNOWN"
    assert components["faz_filament"]["component_type"] == "OTHER"


@pytest.mark.parametrize(
    "slug",
    ["bilobe_structure", "ciliary_centrin_arm", "ciliary_pocket_collar", "flagellum_attachment_zone"],
)
def test_scientific_status_and_open_boundary_discussions_are_retained(slug):
    doc = record(slug)
    assert doc["mapping_status"] == "PROPOSED"
    assert all(d["status"] == "OPEN" for d in doc["discussions"])
