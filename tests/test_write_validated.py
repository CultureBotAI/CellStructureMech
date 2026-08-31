"""The write gate, and the round-trip property that makes bulk edits reviewable."""

from __future__ import annotations

import pytest
import yaml

from cellstructuremech.validation.write_validated import (
    ValidationFailedError,
    emit_structure_yaml,
    validate_structure,
    write_validated_structure,
)

MINIMAL = {
    "identifier": "GO:0005840",
    "label": "ribosome",
    "definition": "A ribonucleoprotein complex that translates messenger RNA.",
    "definition_source": "GO:0005840",
    "structure_category": "RIBONUCLEOPROTEIN",
    "structure_kind": "RIBONUCLEOPROTEIN_COMPLEX",
    "mapping_status": "PROPOSED",
}


def test_valid_record_passes():
    assert validate_structure(MINIMAL) == []


def test_missing_required_field_is_rejected():
    doc = {k: v for k, v in MINIMAL.items() if k != "structure_category"}
    assert validate_structure(doc)


def test_unknown_field_is_rejected():
    """Closed-mode validation is the point of this helper."""
    doc = dict(MINIMAL, structure_catgory="ENVELOPE")
    assert validate_structure(doc)


def test_bad_enum_value_is_rejected():
    assert validate_structure(dict(MINIMAL, structure_category="BLOBS"))


def test_bad_identifier_pattern_is_rejected():
    assert validate_structure(dict(MINIMAL, identifier="not a curie"))


def test_unstructured_provenance_reference_is_rejected():
    assert validate_structure(dict(MINIMAL, definition_source="a paper somewhere"))


def test_causal_edge_without_evidence_is_rejected():
    """Mechanism claims are curator-asserted, so the schema requires edge-level evidence."""
    doc = dict(
        MINIMAL,
        causal_graphs=[
            {
                "graph_id": "g1",
                "graph_kind": "FUNCTION",
                "scope_status": "MECHANISTIC",
                "nodes": [
                    {"node_id": "a", "label": "ribosome", "node_type": "STRUCTURE"},
                    {"node_id": "b", "label": "translation", "node_type": "BIOLOGICAL_PROCESS"},
                ],
                "edges": [{"subject": "a", "predicate": "carries out", "object": "b"}],
            }
        ],
    )
    assert validate_structure(doc)


def test_function_without_evidence_is_rejected():
    doc = dict(MINIMAL, functions=[{"function_id": "f1", "label": "translation"}])
    assert validate_structure(doc)


def test_trait_link_without_evidence_is_rejected():
    doc = dict(
        MINIMAL,
        associated_traits=[{
            "trait_id": "METPO:1000702",
            "trait_label": "motile",
            "relation": "CONFERS",
        }],
    )
    assert validate_structure(doc)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("components", [{
            "component_id": "protein",
            "label": "example protein",
            "component_type": "PROTEIN",
        }]),
        ("taxonomic_distribution", [{
            "taxon_id": "NCBITaxon:2",
            "taxon_label": "Bacteria",
            "presence": "COMMON",
        }]),
        ("canonical_examples", [{
            "taxon_id": "NCBITaxon:562",
            "taxon_label": "Escherichia coli",
        }]),
        ("physical_properties", [{
            "property": "DIAMETER",
            "value": "20",
            "unit": "UO:0000018",
        }]),
    ],
)
def test_claim_bearing_entries_without_provenance_are_rejected(field, value):
    assert validate_structure(dict(MINIMAL, **{field: value}))


def test_invalid_record_is_not_written(tmp_path):
    path = tmp_path / "bad.yaml"
    with pytest.raises(ValidationFailedError):
        write_validated_structure({"identifier": "GO:1"}, path)
    assert not path.exists(), "an invalid record must not reach disk"


def test_valid_record_is_written(tmp_path):
    path = tmp_path / "nested" / "good.yaml"
    write_validated_structure(dict(MINIMAL), path)
    assert path.exists()
    assert yaml.safe_load(path.read_text())["identifier"] == MINIMAL["identifier"]


def test_emit_is_stable_across_calls():
    assert emit_structure_yaml(MINIMAL) == emit_structure_yaml(MINIMAL)


def test_every_record_round_trips_byte_identically(records):
    """Re-emitting the corpus through the helper must change nothing."""
    drifted = []
    for path, doc in records:
        if emit_structure_yaml(doc) != path.read_text(encoding="utf-8"):
            drifted.append(str(path))
    assert not drifted, (
        f"{len(drifted)} record(s) are not what emit_structure_yaml would write, "
        f"e.g. {drifted[:5]}. Reformat them through the helper rather than loosening this test."
    )


@pytest.mark.parametrize("placeholder", ["TODO:add_citation", "FIXME:later", "XXX:none", "TBD:unknown"])
def test_a_placeholder_does_not_satisfy_required_provenance(placeholder):
    """definition_source is required, so a placeholder that validates would turn
    missing provenance (countable) into fake provenance (invisible) — #70. A
    prefix that merely starts with those letters is still a real prefix."""
    assert validate_structure(dict(MINIMAL, definition_source=placeholder))
    assert validate_structure(dict(MINIMAL, definition_source="TODOS:real_prefix")) == []


def test_component_without_a_role_is_rejected():
    """component_role is required: the constituent/machinery distinction is not
    recoverable from essentiality, which only says whether the structure
    assembles without the component (#77)."""
    doc = dict(MINIMAL, components=[{
        "component_id": "c", "label": "x", "component_type": "PROTEIN",
        "evidence": [{"reference": "GO:0005840", "notes": "n"}],
    }])
    assert validate_structure(doc)


def test_component_with_an_unknown_role_is_rejected():
    doc = dict(MINIMAL, components=[{
        "component_id": "c", "label": "x", "component_type": "PROTEIN",
        "component_role": "SIDEKICK",
        "evidence": [{"reference": "GO:0005840", "notes": "n"}],
    }])
    assert validate_structure(doc)
