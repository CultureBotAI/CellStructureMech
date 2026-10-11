"""Keep historical GO ring identities distinct from modern whole-APR evidence."""

from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
IDENTITIES = {
    "basal_ring_of_apical_complex": "GO:0020032",
    "polar_ring_of_apical_complex": "GO:0020031",
    "conoid": "GO:0020010",
    "intraconoid_microtubule": "GO:0033289",
    "subpellicular_microtubule": "GO:0020025",
}


def record(slug):
    return yaml.safe_load(
        (ROOT / "data" / "structures" / "cytoskeleton" / f"{slug}.yaml").read_text()
    )


def discussion(data, identifier):
    return next(d for d in data["discussions"] if d["discussion_id"] == identifier)


@pytest.mark.parametrize("slug,identifier", IDENTITIES.items())
def test_exact_native_identity_and_proposed_status_remain(slug, identifier):
    data = record(slug)
    assert data["identifier"] == identifier
    assert data["mapping_status"] == "PROPOSED"
    assert "GO:0020007" in data["part_of"]


def test_basal_ring_does_not_equate_preconoidal_rings():
    data = record("basal_ring_of_apical_complex")
    assert not any("preconoidal" in s["synonym_text"] for s in data["synonyms"])
    assert "preconoidal" not in data["taxonomic_distribution"][0]["note"]
    assert "posterior preconoidal" not in data["functions"][0]["description"]
    note = discussion(data, "basal_preconoidal_source_conflict")
    assert {e["reference"] for e in note["evidence"]} >= {
        "GO:0020032", "DOI:10.1371/journal.ppat.0020013"
    }


def test_basal_relative_position_is_extrusion_qualified():
    graph = record("basal_ring_of_apical_complex")["causal_graphs"][0]
    edge = next(e for e in graph["edges"] if e["predicate"] == "is posterior to")
    assert "extruded" in edge["description"]
    assert "retracted" in graph["scope_notes"]


def test_anterior_ring_is_not_the_whole_multilayer_apr():
    data = record("polar_ring_of_apical_complex")
    assert "conoid fibers originate" in data["definition"]
    assert not data.get("components")
    assert "apical polar ring" not in {s["synonym_text"] for s in data["synonyms"]}
    graph = data["causal_graphs"][0]
    assert graph["scope_status"] == "NONMECHANISTIC"
    assert ("conoid_fibers", "originate from", "polar_ring_of_apical_complex") in {
        (e["subject"], e["predicate"], e["object"]) for e in graph["edges"]
    }
    assert data["canonical_examples"][0]["reference"] == "DOI:10.1371/journal.ppat.0020013"
    note = discussion(data, "separate_modern_multilayer_apr")
    assert {e["reference"] for e in note["evidence"]} >= {
        "DOI:10.1073/pnas.2416602121", "DOI:10.1002/cm.20469"
    }


def test_retained_apr2_context_uses_the_resolved_middle_layer():
    data = record("polar_ring_of_apical_complex")
    note = discussion(data, "separate_modern_multilayer_apr")
    assert "APR2 in the middle layer" in note["resolution_note"]
    assert "upper-APR" in note["resolution_note"]
    assert "assembly" in note["resolution_note"]


def test_whole_conoid_complex_cohort_is_not_a_body_constituent():
    data = record("conoid")
    assert "conserved_conoid_complex_proteins" not in {
        c["component_id"] for c in data["components"]
    }
    assert "conserved_conoid_complex_proteins" not in {
        n["node_id"] for n in data["causal_graphs"][0]["nodes"]
    }
    assert discussion(data, "conoid_body_versus_complex_scope")


def test_conoid_fibers_and_protofilaments_are_assemblies():
    data = record("conoid")
    fiber = next(c for c in data["components"] if c["component_id"] == "conoid_tubulin_fibers")
    assert fiber["component_type"] == "PROTEIN_COMPLEX"
    nodes = {n["node_id"]: n for n in data["causal_graphs"][0]["nodes"]}
    assert nodes["conoid_tubulin_fibers"]["node_type"] == "STRUCTURE"
    assert nodes["tubulin_protofilaments"]["node_type"] == "STRUCTURE"


def test_spiral_conoid_occurrence_is_not_whole_complex_conservation():
    data = record("conoid")
    assert not any(
        d["taxon_id"] == "NCBITaxon:5794" and d["presence"] == "COMMON"
        for d in data["taxonomic_distribution"]
    )
    assert any(d["taxon_id"] == "NCBITaxon:5811" for d in data["taxonomic_distribution"])
    note = discussion(data, "conoid_body_versus_complex_scope")
    assert "Plasmodium" in note["resolution_note"]
    assert "absence" in note["resolution_note"]


def test_intraconoid_topology_does_not_infer_anterior_ring_projection():
    data = record("intraconoid_microtubule")
    graph = data["causal_graphs"][0]
    assert "projects through" not in {e["predicate"] for e in graph["edges"]}
    assert "GO:0020031" not in {n.get("grounding") for n in graph["nodes"]}
    assert any(e["predicate"] == "threads through" for e in graph["edges"])
    assert data["definition_source"] == "GO:0033289"
    note = discussion(data, "intraconoid_ring_projection_scope")
    assert "DOI:10.1002/advs.202206595" in {e["reference"] for e in note["evidence"]}


def test_subpellicular_attachment_uses_basal_go_ring():
    data = record("subpellicular_microtubule")
    graph = data["causal_graphs"][0]
    nodes = {n["node_id"]: n for n in graph["nodes"]}
    edge = next(e for e in graph["edges"] if e["predicate"] == "attaches to")
    assert nodes[edge["object"]]["grounding"] == "GO:0020032"
    assert "GO:0020031" not in {n.get("grounding") for n in graph["nodes"]}


def test_myoh_and_lattice_evidence_boundaries_remain():
    conoid = record("conoid")
    motor = next(c for c in conoid["components"] if c["component_id"] == "myoh_motor")
    assert (motor["component_role"], motor["essentiality"]) == ("ASSOCIATED_MACHINERY", "UNKNOWN")
    data = record("subpellicular_microtubule")
    edge = data["causal_graphs"][0]["edges"][-1]
    assert edge["predicate"] == "associates with"
    assert "32 nm" in edge["description"]
    assert data["canonical_examples"][0]["reference"] == "DOI:10.1242/jcs.110.1.35"
    note = discussion(data, "exclude_kinetoplastid_subpellicular_arrays")
    assert "DOI:10.1155/2014/893272" in {e["reference"] for e in note["evidence"]}
