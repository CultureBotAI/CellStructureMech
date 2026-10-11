"""Keep structural assembly, barrier function and nutrient capture distinct."""

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
BARRIER = "DOI:10.1016/j.cell.2012.10.046"
CAPTURE = "DOI:10.1073/pnas.0602047103"
COMPARISON = "DOI:10.1371/journal.pone.0184063"


def record(slug):
    return yaml.safe_load((ROOT / f"data/structures/appendage/{slug}.yaml").read_text())


def test_crossband_scaffold_and_sealing_have_distinct_structural_essentiality():
    doc = record("stalk_crossband")
    components = {c["component_id"]: c for c in doc["components"]}
    ab = components["stp_ab_crossband_scaffold"]
    cd = components["stp_cd_barrier_sealing_proteins"]
    assert ab["gene_symbols"] == ["stpA", "stpB"]
    assert cd["gene_symbols"] == ["stpC", "stpD"]
    assert ab["essentiality"] == "ESSENTIAL"
    assert cd["essentiality"] == "DISPENSABLE"
    assert "crossbands remain visible" in cd["role"]
    assert "leaky" in cd["role"]
    assert "does not mean normal barrier function is dispensable" in cd["role"]
    for component in components.values():
        assert component["component_role"] == "CONSTITUENT"
        assert BARRIER in {e["reference"] for e in component["evidence"]}
    graph = doc["causal_graphs"][0]
    component_nodes = [n for n in graph["nodes"] if n.get("component_ref")]
    assert {n["component_ref"] for n in component_nodes} == set(components)
    for node in component_nodes:
        assert node["label"] == components[node["component_ref"]]["label"]
    edges = {e["subject"]: e for e in graph["edges"] if e["subject"] in components}
    assert edges[ab["component_id"]]["predicate"] == "forms scaffold of"
    assert edges[cd["component_id"]]["predicate"] == "seals diffusion barrier of"
    discussion = next(d for d in doc["discussions"] if d["discussion_id"] == "stp_abcd_grounding")
    assert set(discussion["attaches_to"]) == {"components#" + c for c in components}


def test_prostheca_capture_does_not_assert_resolved_nutrient_delivery():
    doc = record("prostheca")
    assert "nutrient uptake" not in doc["definition"]
    function = next(f for f in doc["functions"] if f["function_id"] == "dilute_nutrient_scavenging")
    assert "fluorescein diphosphate" in function["description"]
    assert "Modeling predicts" in function["description"]
    assert "remain unresolved" in function["description"]
    assert {CAPTURE, BARRIER, COMPARISON} <= {e["reference"] for e in function["evidence"]}
    graph = doc["causal_graphs"][0]
    node = next(n for n in graph["nodes"] if n["node_id"] == "dilute_nutrient_scavenging")
    assert node["node_type"] == "BIOLOGICAL_PROCESS"
    assert "fluorescein diphosphate" in node["label"]
    edge = next(e for e in graph["edges"] if e["object"] == node["node_id"])
    assert "does not establish delivery" in edge["description"]
    assert {e["reference"] for e in edge["evidence"]} == {CAPTURE, BARRIER}
    discussion = next(d for d in doc["discussions"] if d["discussion_id"] == "stalk_capture_vs_cell_body_delivery")
    assert discussion["status"] == "OPEN"
    assert "hypotheses" in discussion["rationale"]


def test_na1000_example_stays_with_its_attached_stpx_source():
    doc = record("prostheca")
    example = doc["canonical_examples"][0]
    assert example["taxon_id"] == "NCBITaxon:565050"
    assert example["reference"] == "DOI:10.1073/pnas.0909119107"
    assert "StpX" in example["note"]
    assert "peptidoglycan" not in example["note"]
    edge = next(e for e in doc["causal_graphs"][0]["edges"] if e["subject"] == "stalk_wall_synthesis_machinery")
    assert "DOI:10.1371/journal.pgen.1007897" in {e["reference"] for e in edge["evidence"]}


def test_stalk_curation_retains_proposed_status_and_actual_agent_identity():
    for slug in ["prostheca", "stalk_crossband"]:
        doc = record(slug)
        assert doc["mapping_status"] == "PROPOSED"
        event = doc["curation_history"][-1]
        assert event["curator"] == "codex"
        assert event["llm_assisted"] is True
        assert event["action"] == "ADDRESS_SAVED_REVIEW"
