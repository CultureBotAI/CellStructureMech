"""Keep model-specific pilus mechanisms and append-only rationale explicit."""

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def record(slug):
    return yaml.safe_load((ROOT / f"data/structures/appendage/{slug}.yaml").read_text())


def test_tad_polar_retraction_is_model_scoped():
    doc = record("tad_pilus")
    assert "not asserted for every Tad system" in doc["definition"]
    graph = doc["causal_graphs"][0]
    assert "Caulobacter" in graph["scope_notes"]
    assert "unresolved" in graph["scope_notes"]
    motor_edges = [e for e in graph["edges"] if e["subject"] == "cpaf_motor"]
    assert len(motor_edges) == 1
    assert motor_edges[0]["predicate"] == "extends and retracts"
    assert "DOI:10.1126/sciadv.aay2591" in {
        e["reference"] for e in motor_edges[0]["evidence"]
    }
    endpoint = next(n for n in graph["nodes"] if n["node_id"] == "surface_colonization")
    assert endpoint["node_type"] == "BIOLOGICAL_PROCESS"


def test_type_i_inventory_is_not_universalized_to_salmonella():
    doc = record("type_i_pilus")
    assert "Escherichia coli model" in doc["definition"]
    assert "Salmonella" in doc["definition"]
    assert "Salmonella" in doc["taxonomic_distribution"][0]["note"]
    for component in doc["components"]:
        assert "Escherichia coli model" in component["role"]
    graph = doc["causal_graphs"][0]
    assert "without FimG" in graph["scope_notes"]
    expected = ["fimh_adhesin", "fimg_tip_adaptor", "fimf_tip_adaptor", "fima_major_pilin"]
    links = {(e["subject"], e["object"]) for e in graph["edges"]}
    assert set(zip(expected[:-1], expected[1:], strict=True)) <= links


def test_type_i_termination_function_cites_confirming_structure():
    function = record("type_i_pilus")["functions"][0]
    assert "Escherichia coli" in function["description"]
    assert "DOI:10.1038/s41467-025-60325-z" in {
        e["reference"] for e in function["evidence"]
    }


def test_type_iv_motors_are_external_to_filament_composition():
    doc = record("type_iv_pilus")
    components = {c["component_id"] for c in doc["components"]}
    assert "major_pilin" in components
    assert not {"extension_atpase", "retraction_atpase"} & components
    graph = doc["causal_graphs"][0]
    motors = [n for n in graph["nodes"] if n["node_id"] in {
        "extension_atpase", "retraction_atpase"
    }]
    assert len(motors) == 2
    assert all("component_ref" not in n for n in motors)
    assert "type IVa" in graph["scope_notes"]
    assert "not assert that every type IV subtype" in graph["scope_notes"]
    discussion = next(
        d for d in doc["discussions"] if d["discussion_id"] == "motor_machine_not_pilus_filament"
    )
    assert discussion["status"] == "RESOLVED"
    dataset = doc["datasets"][0]
    assert dataset["accession"] == "CryoETDataPortal:10155"
    assert "annotation 30707" in dataset["findings"]


def test_crossband_grounding_rationale_preserves_both_decisions():
    doc = record("stalk_crossband")
    discussion = next(d for d in doc["discussions"] if d["discussion_id"] == "stp_abcd_grounding")
    original = (
        "The first record uses a reviewed label for the StpABCD cohort until an "
        "exact protein-family or complex identifier is verified."
    )
    assert discussion["rationale"].startswith(original)
    assert "Reassessment on" in discussion["rationale"]
    assert "StpAB scaffold cohort from StpCD sealing constituents" in discussion["rationale"]
    assert discussion["posed_date"] == "2026-09-11"
    assert discussion["status"] == "OPEN"
