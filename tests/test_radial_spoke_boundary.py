"""Keep the exact stalk grounding separate from the microtubule-binding base."""

from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1] / "data/structures/cytoskeleton"


@pytest.mark.parametrize("slug", ["radial_spoke", "radial_spoke_stalk"])
def test_stalk_has_separate_base_and_neck_endpoints(slug):
    record = yaml.safe_load((ROOT / f"{slug}.yaml").read_text())
    graph = record["causal_graphs"][0]
    nodes = {node["node_id"]: node for node in graph["nodes"]}
    assert nodes["radial_spoke_stalk"]["grounding"] == "GO:0001536"
    assert nodes["radial_spoke_base"]["node_type"] == "STRUCTURE"
    assert nodes["radial_spoke_neck"]["grounding"] == "GO:0120343"
    edges = graph["edges"]
    assert any(
        edge["subject"] == "radial_spoke_stalk"
        and edge["object"] == "radial_spoke_base"
        and edge["predicate"] == "connects to"
        and any(e["reference"] == "GO:0001536" for e in edge["evidence"])
        for edge in edges
    )
    assert any(
        {edge["subject"], edge["object"]}
        == {"radial_spoke_stalk", "radial_spoke_neck"}
        and edge["predicate"] == "connects to"
        for edge in edges
    )
    assert not any(
        edge["subject"] == "radial_spoke_stalk"
        and edge["object"] == "outer_doublet_microtubule"
        for edge in edges
    )


def test_whole_spoke_preserves_base_attachment_without_widening_stalk():
    record = yaml.safe_load((ROOT / "radial_spoke.yaml").read_text())
    stalk = next(c for c in record["components"] if c["component_id"] == "radial_spoke_stalk")
    assert "base" in stalk["role"] and "neck" in stalk["role"]
    graph = record["causal_graphs"][0]
    edge = next(e for e in graph["edges"] if e["subject"] == "radial_spoke_base")
    assert edge["object"] == "outer_doublet_microtubule"
    assert edge["predicate"] == "binds to"
    assert "A-tubule" in edge["description"]
    assert any(e["reference"] == "GO:0001536" for e in edge["evidence"])
    assert graph["scope_status"] == "NONMECHANISTIC"
