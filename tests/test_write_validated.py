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
    "structure_category": "RIBONUCLEOPROTEIN",
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


def test_causal_edge_without_evidence_is_rejected():
    """Mechanism claims are curator-asserted, so the schema requires edge-level evidence."""
    doc = dict(
        MINIMAL,
        causal_graphs=[
            {
                "graph_id": "g1",
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
