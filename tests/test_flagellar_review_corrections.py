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


@pytest.mark.parametrize("part", ["filament", "hook"])
def test_axial_prevalence_distinguishes_marker_survey_from_anatomy(part):
    bacteria = named(record("_" + part)["taxonomic_distribution"], "taxon_id", "NCBITaxon:2")
    assert bacteria["presence"] == "VARIABLE"
    assert bacteria["reference"] == "DOI:10.1073/pnas.2512476122"
    assert "FliPQR" in bacteria["note"]
    assert "not direct observation" in bacteria["note"]
    assert "does not establish this particular structure" in bacteria["note"]


def test_filament_definition_does_not_mistake_thickness_for_length():
    doc = record("_filament")
    assert doc["identifier"] == "GO:0009420"
    assert "20 nm" not in doc["definition"]
    assert "external" in doc["definition"]
    assert "flagellin" in doc["definition"]
    assert doc["definition_source"] == "DOI:10.1038/nrmicro1887"
    assert any("#230" in event["changes"] for event in doc["curation_history"])


def test_filament_author_corrections_do_not_rewrite_historical_events():
    doc = record("_filament")
    by_doi = {
        "DOI:10.3390/biom11020186": ("Halte and Erhardt", "Minamino and Namba"),
        "DOI:10.1038/s41598-019-51440-1": ("Blum", "Yonekura"),
        "DOI:10.1038/s41467-026-71203-7": ("Qin", "Zhu"),
    }
    entries = doc["evidence"] + doc["components"][0]["evidence"]
    entries += [e for edge in doc["causal_graphs"][0]["edges"] for e in edge["evidence"]]
    for entry in entries:
        if entry["reference"] in by_doi:
            author, former_author = by_doi[entry["reference"]]
            assert author in entry["notes"]
            assert former_author not in entry["notes"]
    assert any("Zhu et al. 2026" in event["changes"] for event in doc["curation_history"])


def test_cap_model_is_not_recast_as_direct_growth_imaging():
    edge = named(record("_filament_cap")["causal_graphs"][0]["edges"], "predicate", "incorporates below")
    note = named(edge["evidence"], "reference", "DOI:10.1073/pnas.2534343100")["notes"]
    assert "isolated-cap cryo-EM" in note
    assert "structural modeling" in note
    assert "not a directly imaged growth sequence" in note


def test_junction_assembled_contacts_are_not_solution_binding_claims():
    doc = record("_hook_filament_junction")
    flgl = named(doc["components"], "component_id", "flgl_hap3")
    modern = named(flgl["evidence"], "reference", "DOI:10.1038/s41564-025-02037-0")
    assert "assembled" in modern["notes"]
    for edge in doc["causal_graphs"][0]["edges"]:
        if edge["predicate"] == "contacts":
            assert all(e["reference"] != "DOI:10.1016/S0022-2836(02)00139-0" for e in edge["evidence"])
    bounding = named(doc["evidence"], "reference", "DOI:10.1016/S0022-2836(02)00139-0")
    assert "not FlgK-FlgL solution binding" in bounding["notes"]


def test_junction_historical_precision_does_not_replace_native_stoichiometry():
    doc = record("_hook_filament_junction")
    for component_id, count in (("flgk_hap1", "10-20"), ("flgl_hap3", "10-40")):
        component = named(doc["components"], "component_id", component_id)
        old = named(component["evidence"], "reference", "DOI:10.1128/jb.169.3.1168-1173.1987")
        assert count in old["notes"]
        assert "fine localization within the junction was not determined" in old["notes"]
        assert component["stoichiometry"].startswith("11 ")
    for edge in doc["causal_graphs"][0]["edges"][:2]:
        assert edge["evidence"][0]["reference"] == "DOI:10.1038/s41564-025-02037-0"
    assert doc["physical_properties"][0]["value"] == "22"
    old = doc["functions"][0]["evidence"][0]
    assert "filamentless" in old["notes"] and "mature HAP3" in old["notes"]


def test_exact_flgk_family_does_not_force_a_broad_flge_grounding():
    flgk = named(record("_hook_filament_junction")["components"], "component_id", "flgk_hap1")
    assert flgk["grounding"] == "InterPro:IPR002371"
    assert "grounding_status" not in flgk
    assert "label-only decision is superseded" in flgk["grounding_notes"]
    assert "UniProtKB:P0A1J5" in flgk["grounding_notes"]
    flge = record("_hook")["components"][0]
    assert "grounding" not in flge
    assert flge["grounding_status"] == "REVIEWED_LABEL_ONLY"


@pytest.mark.parametrize("part", ["motor", "stator_complex"])
def test_stator_dynamics_keep_source_and_organism_context(part):
    doc = record("_" + part)
    edges = doc["causal_graphs"][0]["edges"]
    edge = named(edges, "subject", "ion_flux")
    assert "model" in edge["description"]
    assert "Escherichia coli" in edge["description"]
    direct = named(edge["evidence"], "reference", "DOI:10.1073/pnas.2515291122")
    assert "not the direction" in direct["notes"]
    assert "not test all Mot/Pom" in direct["notes"]
    exchange = doc["functions"][1]
    assert "Escherichia coli" in exchange["description"]
    assert any(e["reference"] == "DOI:10.1038/nature05135" for e in exchange["evidence"])


def test_stator_a_family_grounding_does_not_overground_b_subunit():
    a, b = record("_stator_complex")["components"]
    assert a["grounding"] == "InterPro:IPR047055"
    assert a["label"] == "Motility protein A-like"
    assert "grounding_status" not in a
    assert "former label-only decision is superseded" in a["grounding_notes"]
    assert a["gene_symbols"] == ["motA", "pomA"]
    assert "grounding" not in b
    assert b["grounding_status"] == "REVIEWED_LABEL_ONLY"


def test_export_core_counts_keep_the_correct_source_and_organism():
    doc = record("_secretion_apparatus")
    for component_id, count in (("flip", "5"), ("fliq", "4"), ("flir", "1")):
        component = named(doc["components"], "component_id", component_id)
        assert component["stoichiometry"].startswith(count + " ")
        assert "Salmonella" in component["stoichiometry"]
        assert component["evidence"][0]["reference"] == "DOI:10.1038/s41594-018-0086-9"
    flhb = named(doc["components"], "component_id", "flhb")
    assert "Vibrio mimicus" in flhb["stoichiometry"]
    assert flhb["evidence"][0]["reference"] == "DOI:10.1038/s41467-020-15071-9"
    assert "wrapping around the base" in flhb["role"]
    assert doc["canonical_examples"][0]["reference"] == "DOI:10.1038/s41594-018-0086-9"
    edges = doc["causal_graphs"][0]["edges"]
    assert named(edges, "subject", "flhb")["predicate"] == "contacts"
    assert "static structure" in edges[0]["description"]
    assert "does not by itself establish assembly order" in edges[0]["description"]
    assert "not a FliP5-FliQ4-FliR1-FlhB1 reconstruction" in doc["discussions"][0]["rationale"]


def test_export_atpase_model_is_not_a_resolved_complete_complex():
    doc = record("_secretion_apparatus")
    for component_id in ("flih", "flii", "flij"):
        component = named(doc["components"], "component_id", component_id)
        assert "modeled" in component["stoichiometry"]
        note = named(component["evidence"], "reference", "DOI:10.1073/pnas.1524025113")["notes"]
        assert "FliH C-terminal dimer-FliI heterotrimer" in note
        assert "not a direct reconstruction" in note
    edge = named(doc["causal_graphs"][0]["edges"], "subject", "flii")
    assert "In the structural model" in edge["description"]


def test_export_sodium_coupling_is_not_assigned_to_intact_atpase_state():
    doc = record("_secretion_apparatus")
    function = named(doc["functions"], "function_id", "energy_coupled_export")
    assert "Salmonella" in function["description"]
    assert "compromised ATPase system" in function["description"]
    assert "intact ATPase-assisted system showed no sodium dependence" in function["description"]
    edge = named(doc["causal_graphs"][0]["edges"], "subject", "ion_motive_force")
    assert "not with the intact FliH/FliI/FliJ system" in edge["description"]
    assert edge["evidence"][0]["reference"] == "DOI:10.1371/journal.ppat.1005495"
