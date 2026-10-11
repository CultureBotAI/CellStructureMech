"""Keep ventral-disc source conflicts and ontology synonym scopes explicit."""

from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1] / "data/structures/cytoskeleton"
SCHWARTZ = "DOI:10.1371/journal.pone.0043783"
HAGEN = "DOI:10.1371/journal.pntd.0001442"


def record(slug):
    return yaml.safe_load((ROOT / f"{slug}.yaml").read_text())


def test_disc_definition_does_not_assert_classical_contractile_machinery():
    doc = record("ventral_disc")
    assert doc["definition_source"] == SCHWARTZ
    assert "myosin" not in doc["definition"].lower()
    assert "attachment" in doc["definition"].lower()
    conflict = next(
        d for d in doc["discussions"] if d["discussion_id"] == "ventral_disc_contractile_source_conflict"
    )
    assert conflict["status"] == "RESOLVED"
    assert {e["reference"] for e in conflict["evidence"]} >= {
        HAGEN,
        "DOI:10.1091/mbc.E23-12-0515",
        "GO:0097597",
    }


@pytest.mark.parametrize("text", ["adhesive disc", "ventral disk"])
def test_related_disc_synonyms_are_not_exact(text):
    synonym = next(s for s in record("ventral_disc")["synonyms"] if s["synonym_text"] == text)
    assert synonym["synonym_type"] == "RELATED_SYNONYM"
    assert synonym["source"] == "GO:0097597"


def test_tubulin_labels_are_source_neutral_with_stable_references():
    doc = record("ventral_disc")
    component = next(c for c in doc["components"] if c["component_id"] == "ventral_disc_tubulins")
    node = next(n for n in doc["causal_graphs"][0]["nodes"] if n["node_id"] == "ventral_disc_tubulins")
    assert component["label"] == node["label"] == "alpha- and beta-tubulins"
    assert node["component_ref"] == component["component_id"]
    assert component["essentiality"] == "UNKNOWN"


def test_supernumerary_orientation_is_study_bounded_and_preserves_conflict():
    doc = record("ventral_disc_supernumerary_microtubule_array")
    assert doc["definition_source"] == SCHWARTZ
    assert "Schwartz" in doc["definition"] and "right-handed" in doc["definition"]
    graph = doc["causal_graphs"][0]
    edge = graph["edges"][0]
    assert edge["predicate"] == "lies ventral to"
    assert "Schwartz" in edge["description"] and "2012" in edge["description"]
    assert any(e["reference"] == SCHWARTZ for e in edge["evidence"])
    assert "Hagen" in graph["scope_notes"] and "left-handed" in graph["scope_notes"]
    conflict = next(
        d for d in doc["discussions"] if d["discussion_id"] == "supernumerary_array_orientation_conflict"
    )
    assert {e["reference"] for e in conflict["evidence"]} >= {HAGEN, SCHWARTZ, "GO:0097596"}


@pytest.mark.parametrize(
    "slug,identifier",
    [("ventral_disc", "GO:0097597"), ("ventral_disc_supernumerary_microtubule_array", "GO:0097596")],
)
def test_disc_identity_status_and_unknowns_remain_bounded(slug, identifier):
    doc = record(slug)
    assert doc["identifier"] == identifier
    assert doc["mapping_status"] == "PROPOSED"
    assert doc["taxonomic_distribution"][0]["taxon_id"] == "NCBITaxon:5741"
    assert any(d["kind"] == "CURATION_TODO" and d["status"] == "OPEN" for d in doc["discussions"])
    assert doc["causal_graphs"][0]["scope_status"] == "NONMECHANISTIC"
    if slug.endswith("supernumerary_microtubule_array"):
        assert not doc.get("functions")
        assert doc["part_of"] == ["GO:0097597"]
        assert doc["has_part"] == ["GO:0005874"]
