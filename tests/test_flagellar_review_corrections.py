"""Keep the reviewed claim boundaries explicit when these records are curated."""

from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "bacterial_type_flagellum"


def record(suffix=""):
    return yaml.safe_load(
        (ROOT / "data/structures/appendage" / f"{PREFIX}{suffix}.yaml").read_text()
    )


def named(items, key, value):
    return next(item for item in items if item[key] == value)


def test_length_has_no_unsourced_lower_bound():
    length = named(record()["physical_properties"], "property", "LENGTH")
    assert length["value"] == "up to 20"
    assert length["unit"] == "UO:0000017"
    assert length["reference"] == "DOI:10.3390/biom11020186"
    assert "not a universal maximum" in length["context"]


@pytest.mark.parametrize("suffix", ["", "_basal_body"])
def test_assembly_and_prevalence_remain_condition_bound(suffix):
    doc = record(suffix)
    ring = named(doc["components"], "component_id", "c_ring")
    assert ring["essentiality"] == "CONDITIONAL"
    assert "FliI overproduction" in ring["role"]
    assert "nonmotile" in ring["role"]
    assert any(e["reference"] == "DOI:10.1128/JB.00601-09" for e in ring["evidence"])
    bacteria = named(doc["taxonomic_distribution"], "taxon_id", "NCBITaxon:2")
    assert bacteria["presence"] == "VARIABLE"
    assert bacteria["reference"] == "DOI:10.1073/pnas.2512476122"
    assert "not direct observation" in bacteria["note"]


def test_sodium_input_is_not_routed_through_a_proton_only_node():
    graph = record()["causal_graphs"][0]
    edge = named(graph["edges"], "object", "stator")
    source = named(graph["nodes"], "node_id", edge["subject"])
    assert "ion motive force" in source["label"]
    assert "H+" in source["label"] and "Na+" in source["label"]


@pytest.mark.parametrize("suffix", ["", "_basal_body", "_basal_body_c_ring"])
def test_stator_trajectory_is_qualified_in_the_claim_itself(suffix):
    doc = record(suffix)
    if suffix == "_basal_body_c_ring":
        claim = named(doc["functions"], "function_id", "rotor_stator_torque_coupling")
    else:
        claim = named(doc["causal_graphs"][0]["edges"], "subject", "stator")
    assert "model" in claim["description"]
    assert "torque" in claim["description"]
    assert any(
        e["reference"] == "DOI:10.1038/s41564-020-0788-8"
        for e in claim["evidence"]
    )


def test_grounding_prompt_only_attaches_to_unresolved_components():
    doc = record()
    todo = named(doc["discussions"], "discussion_id", "component_groundings")
    assert todo["posed_date"] == "2026-08-29"
    assert todo["rationale"].startswith("Groundings were deliberately left blank")
    assert set(todo["attaches_to"]) == {
        f"components#{c['component_id']}" for c in doc["components"]
        if not c.get("grounding") and not c.get("grounding_status")
    }


def test_fliy_correction_preserves_history_and_family_region_scope():
    doc = record("_basal_body_c_ring")
    discussion = named(doc["discussions"], "discussion_id", "fliy_variant_boundary")
    assert discussion["posed_date"] == "2026-09-08"
    assert discussion["resolved_date"] == "2026-09-08"
    assert discussion["rationale"].startswith("Ward et al. 2019 support FliY")
    assert "that taxonomic restriction is incorrect" in discussion["rationale"]
    assert "corresponding region" in discussion["rationale"]
    assert named(doc["components"], "component_id", "flin")["grounding"] == "InterPro:IPR012826"


def test_partial_c_ring_bypass_does_not_extend_to_flig():
    components = record("_basal_body_c_ring")["components"]
    assert named(components, "component_id", "flig")["essentiality"] == "ESSENTIAL"
    for component_id in ("flim", "flin"):
        component = named(components, "component_id", component_id)
        assert component["essentiality"] == "CONDITIONAL"
        assert "FliI overproduction" in component["role"]
        assert "incomplete C ring" in component["role"]
        assert any(e["reference"] == "DOI:10.1128/JB.00601-09" for e in component["evidence"])


@pytest.mark.parametrize("part", ["distal_rod", "ms_ring", "proximal_rod", "rod"])
def test_rod_ring_prevalence_does_not_turn_genomic_markers_into_observed_anatomy(part):
    doc = record("_basal_body_" + part)
    bacteria = named(doc["taxonomic_distribution"], "taxon_id", "NCBITaxon:2")
    assert bacteria["presence"] == "VARIABLE"
    assert bacteria["reference"] == "DOI:10.1073/pnas.2512476122"
    assert "FliPQR" in bacteria["note"]
    assert "not direct observation" in bacteria["note"]
    assert "this particular rod/ring" in bacteria["note"]


@pytest.mark.parametrize("part", ["proximal_rod", "rod"])
def test_flie_grounding_supersedes_the_old_decision_without_guessing_flgf(part):
    components = record("_basal_body_" + part)["components"]
    flie = named(components, "component_id", "flie")
    assert flie["grounding"] == "InterPro:IPR001624"
    assert "grounding_status" not in flie
    assert flie["grounding_notes"].startswith("No exact integrated InterPro family was identified")
    assert "label-only decision is superseded" in flie["grounding_notes"]
    assert "UniProtKB:P26462" in flie["grounding_notes"]
    assert any(e["reference"] == "InterPro:IPR001624" for e in flie["evidence"])
    flgf = named(components, "component_id", "flgf")
    assert "grounding" not in flgf
    assert flgf["grounding_status"] == "REVIEWED_LABEL_ONLY"


def test_l_and_p_ring_synonym_scopes_are_checked_independently():
    l_ring = record("_basal_body_distal_rod_l_ring")
    p_ring = record("_basal_body_distal_rod_p_ring")
    assert l_ring["synonyms"][0]["synonym_type"] == "EXACT_SYNONYM"
    assert p_ring["synonyms"][0]["synonym_type"] == "RELATED_SYNONYM"


def test_p_ring_presence_is_independent_of_l_ring_but_not_of_flgi():
    doc = record("_basal_body_distal_rod_p_ring")
    bacteria = named(doc["taxonomic_distribution"], "taxon_id", "NCBITaxon:2")
    assert bacteria["presence"] == "VARIABLE"
    assert bacteria["reference"] == "DOI:10.1038/emboj.2011.186"
    assert "Borrelia burgdorferi" in bacteria["note"]
    assert "does not require an L ring" in bacteria["note"]
    flgi = named(doc["components"], "component_id", "flgi")
    assert flgi["essentiality"] == "ESSENTIAL"
    assert flgi["stoichiometry"] == "26 subunits in the Salmonella P ring"
    assert any(e["reference"] == "DOI:10.1128/JB.00340-09" for e in flgi["evidence"])
    assert "Salmonella" in flgi["role"]
    assert all("Salmonella" in f["description"] for f in doc["functions"])
    graph = doc["causal_graphs"][0]
    assert "Salmonella" in graph["description"]
    assert all("Salmonella" in edge["description"] for edge in graph["edges"])
