"""Preserve the reviewed distinction between linker identity and molecular inventory."""

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def zone():
    path = ROOT / "data/structures/appendage/ciliary_transition_zone.yaml"
    return yaml.safe_load(path.read_text())


def test_y_link_identity_matches_its_graph_node_without_promoting_the_zone():
    doc = zone()
    assert doc["identifier"] == "GO:0035869"
    assert doc["mapping_status"] == "PROPOSED"
    link = next(c for c in doc["components"] if c["component_id"] == "transition_zone_y_linkers")
    assert link["grounding"] == "GO:0097537"
    assert link["label"] == "Y-shaped link"
    assert link["component_type"] == "PROTEIN_COMPLEX"
    assert "grounding_status" not in link
    assert link["essentiality"] == "UNKNOWN"
    assert "stoichiometry" not in link
    assert any(e["reference"] == link["grounding"] for e in link["evidence"])
    graph = doc["causal_graphs"][0]
    node = next(n for n in graph["nodes"] if n.get("component_ref") == link["component_id"])
    assert (node["grounding"], node["label"]) == (link["grounding"], link["label"])
    assert graph["scope_status"] == "NONMECHANISTIC"


def test_exact_linker_identity_does_not_resolve_its_molecular_inventory():
    doc = zone()
    link, segment, network = doc["components"]
    assert link["grounding_notes"].startswith("GO:0035869 defines Y-shaped linkers")
    assert "earlier label-only decision is superseded" in link["grounding_notes"]
    for component in (segment, network):
        assert "grounding" not in component
        assert component["grounding_status"] == "REVIEWED_LABEL_ONLY"
        assert component["essentiality"] == "UNKNOWN"
    discussion = doc["discussions"][0]
    assert discussion["status"] == "OPEN"
    assert discussion["posed_date"] == "2026-09-15"
    assert "molecular constituents" in discussion["prompt"]
    assert discussion["rationale"].startswith("CEP290, MKS, NPHP and TCTN proteins")
    assert "does not resolve its molecular constituents" in discussion["rationale"]
    assert set(discussion["attaches_to"]) == {
        "components#" + c["component_id"] for c in doc["components"]
    }
