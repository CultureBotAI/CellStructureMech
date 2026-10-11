"""Keep coarse dynein composition distinct from an assembly mechanism."""

from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1] / "data/structures/cytoskeleton"
SLUGS = ["inner_dynein_arm", "outer_dynein_arm"]


@pytest.mark.parametrize("slug", SLUGS)
def test_dynein_constituent_edges_are_static_parthood(slug):
    record = yaml.safe_load((ROOT / f"{slug}.yaml").read_text())
    graph = record["causal_graphs"][0]
    components = {component["component_id"] for component in record["components"]}
    nodes = {node["node_id"]: node for node in graph["nodes"]}
    edges = [edge for edge in graph["edges"] if edge["subject"] in components]
    assert {edge["subject"] for edge in edges} == components
    for edge in edges:
        assert edge["predicate"] == "are part of"
        assert edge["object"] == slug
        assert nodes[edge["subject"]]["component_ref"] == edge["subject"]
        assert any(e["reference"] == record["identifier"] for e in edge["evidence"])
    assert graph["graph_kind"] == "FUNCTION"
    assert graph["scope_status"] == "NONMECHANISTIC"
    assert any(
        edge["subject"] == slug
        and edge["predicate"] == "projects from"
        and edge["object"] == "outer_doublet_microtubules"
        for edge in graph["edges"]
    )
    assert any(
        edge["subject"] == slug
        and edge["predicate"] == "drives"
        and edge["object"] == "microtubule_sliding"
        for edge in graph["edges"]
    )


@pytest.mark.parametrize("slug", SLUGS)
def test_dynein_description_agrees_with_constituent_scope(slug):
    record = yaml.safe_load((ROOT / f"{slug}.yaml").read_text())
    graph = record["causal_graphs"][0]
    assert "assemble into" not in graph["description"]
    assert "constituent" in graph["description"]
    assert "Chlamydomonas" in graph["description"]
    assert "sliding force" in graph["description"]
    assert record["mapping_status"] == "PROPOSED"
    assert record["discussions"][0]["status"] == "OPEN"
    assert "unresolved" in graph["scope_notes"]
