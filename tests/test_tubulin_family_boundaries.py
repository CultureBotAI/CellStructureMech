"""Preserve filament partonomy and distinguish the PhuZ spindle from a vortex."""

from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1] / "data/structures/cytoskeleton"
FIBERS = ("btubab_bacterial_microtubule", "cetz_filament", "tubz_filament")
SYSTEMS = (*FIBERS, "phuz_spindle")


def record(slug):
    return yaml.safe_load((ROOT / f"{slug}.yaml").read_text())


@pytest.mark.parametrize("slug", SYSTEMS)
def test_cytoskeleton_is_containing_framework(slug):
    data = record(slug)
    assert "GO:0005856" not in data.get("parent_structures", [])
    assert "GO:0005856" in data["part_of"]
    assert any(e["reference"] == "GO:0005856" for e in data["evidence"])


@pytest.mark.parametrize("slug", FIBERS)
def test_individual_polymers_keep_broader_fiber_parent(slug):
    data = record(slug)
    assert data["parent_structures"] == ["GO:0099513"]
    assert any(e["reference"] == "GO:0099513" for e in data["evidence"])


def test_phuz_spindle_does_not_claim_goslar_vortex_occurrence():
    data = record("phuz_spindle")
    for field in ("taxonomic_distribution", "canonical_examples"):
        assert {row["taxon_id"] for row in data[field]} == {"NCBITaxon:198110"}
    assert "vortex" not in data["components"][0]["role"].lower()
    discussion = next(
        d for d in data["discussions"]
        if d["discussion_id"] == "phuz_spindle_excludes_goslar_vortex"
    )
    assert discussion["status"] == "RESOLVED"
    assert any(
        e["reference"] == "DOI:10.1016/j.celrep.2022.111179"
        for e in discussion["evidence"]
    )


def test_spindle_rotation_has_spindle_specific_primary_evidence():
    data = record("phuz_spindle")
    function = next(f for f in data["functions"] if f["function_id"] == "phage_nucleus_rotation")
    assert "201phi2-1" in function["description"]
    assert "vortex" not in function["description"].lower()
    assert {e["reference"] for e in function["evidence"]} == {"DOI:10.1126/science.aal2130"}


def test_phuz_spindle_preserves_positioning_graph_and_uncertain_grounding():
    data = record("phuz_spindle")
    graph = data["causal_graphs"][0]
    assert graph["scope_status"] == "NONMECHANISTIC"
    assert [e["predicate"] for e in graph["edges"]] == ["polymerizes into", "positions", "supports"]
    assert data["components"][0]["grounding_status"] == "REVIEWED_LABEL_ONLY"
    assert "grounding" not in data["components"][0]


@pytest.mark.parametrize("slug", SYSTEMS)
def test_specific_identities_remain_proposed(slug):
    data = record(slug)
    assert data["identifier"] == f"cellstructuremech:{slug}"
    assert data["mapping_status"] == "PROPOSED"
