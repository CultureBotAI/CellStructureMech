"""Keep cytoskeletal substructures distinct from their containing framework."""

from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]


def record(slug):
    return yaml.safe_load(
        (ROOT / "data/structures/cytoskeleton" / f"{slug}.yaml").read_text()
    )


@pytest.mark.parametrize("slug", ["deep_fiber", "funis"])
def test_cytoskeleton_link_is_parthood(slug):
    doc = record(slug)
    assert "GO:0005856" not in doc.get("parent_structures", [])
    assert doc.get("part_of", []).count("GO:0005856") == 1


def test_deep_fiber_keeps_oral_apparatus_parthood():
    doc = record("deep_fiber")
    assert doc["identifier"] == "GO:0032123"
    assert doc["part_of"].count("GO:0031912") == 1
    assert len(doc["causal_graphs"][0]["edges"]) == 2


def test_deep_fiber_evidence_names_the_typed_relation():
    note = next(
        e["notes"] for e in record("deep_fiber")["evidence"]
        if e["reference"] == "GO:0005856"
    )
    assert "part_of" in note
    assert "direct GO:0032123 parent" not in note


def test_funis_keeps_broad_class_and_microtubule_parts():
    doc = record("funis")
    assert doc["identifier"] == "cellstructuremech:funis"
    assert doc["parent_structures"] == ["GO:0005622"]
    assert doc["has_part"] == ["GO:0005874"]
    assert doc["components"][0]["essentiality"] == "UNKNOWN"


def test_funis_tail_flexion_remains_a_proposed_model():
    graph = record("funis")["causal_graphs"][0]
    edge = next(e for e in graph["edges"] if e["object"] == "tail_flexion")
    assert edge["predicate"] == "is proposed to support"
    assert len(graph["edges"]) == 5
    assert graph["scope_status"] == "NONMECHANISTIC"


@pytest.mark.parametrize("slug", ["deep_fiber", "funis"])
def test_status_and_open_component_uncertainty_remain(slug):
    doc = record(slug)
    assert doc["mapping_status"] == "PROPOSED"
    assert any(d["kind"] == "CURATION_TODO" and d["status"] == "OPEN" for d in doc["discussions"])
