"""Preserve corrected publication provenance and bounded ring assembly evidence."""

from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
RECORDS = ROOT / "data/structures/cytoskeleton"
CORRECTED = "DOI:10.1242/jcs.jcs091561"
ORIGINAL = "DOI:10.1242/jcs.091561"


def record(slug):
    return yaml.safe_load((RECORDS / f"{slug}.yaml").read_text())


def references(value):
    if isinstance(value, dict):
        for key, child in value.items():
            if key == "reference":
                yield child
            elif key != "curation_history":
                yield from references(child)
    elif isinstance(value, list):
        for child in value:
            yield from references(child)


def test_meiar_claims_use_the_publisher_corrected_doi():
    refs = list(references(record("meiotic_actomyosin_contractile_ring")))
    assert ORIGINAL not in refs
    assert refs.count(CORRECTED) == 6


def test_meiar_correction_has_local_provenance():
    evidence = record("meiotic_actomyosin_contractile_ring")["evidence"]
    correction = next((e for e in evidence if e["reference"] == "DOI:10.1242/jcs.113316"), None)
    assert correction is not None
    assert "10.1242/jcs.jcs091561" in correction["notes"]
    assert "biological" in correction["notes"]


@pytest.mark.parametrize("component_id", ["actin_filaments", "myosin_proteins"])
def test_prospore_composition_does_not_assert_assembly_essentiality(component_id):
    components = record("prospore_contractile_ring")["components"]
    component = next(c for c in components if c["component_id"] == component_id)
    assert component["essentiality"] == "UNKNOWN"
    assert component["component_role"] == "CONSTITUENT"
    assert component["grounding_status"] == "REVIEWED_LABEL_ONLY"


@pytest.mark.parametrize("component_id", ["actin_filaments", "myosin_proteins"])
def test_prospore_component_note_explains_the_evidence_limit(component_id):
    component = next(
        c for c in record("prospore_contractile_ring")["components"] if c["component_id"] == component_id
    )
    note = next(e["notes"] for e in component["evidence"] if e["reference"] == "GO:0032157")
    assert "composition" in note
    assert "assembly" in note
    assert "UNKNOWN" in note


@pytest.mark.parametrize(
    ("slug", "identifier", "parent"),
    [
        ("meiotic_actomyosin_contractile_ring", "GO:0110086", "GO:0005826"),
        ("prospore_contractile_ring", "GO:0032157", "GO:0110086"),
    ],
)
def test_ring_identity_hierarchy_and_graph_scope_are_preserved(slug, identifier, parent):
    data = record(slug)
    assert data["identifier"] == identifier
    assert data["parent_structures"] == [parent]
    assert data["mapping_status"] == "PROPOSED"
    assert data["causal_graphs"][0]["scope_status"] == "NONMECHANISTIC"
