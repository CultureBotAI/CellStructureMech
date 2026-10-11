"""Keep orthology, lineage scope and motility evidence distinct."""

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
NOMENCLATURE = "DOI:10.1016/j.molbiopara.2004.03.006"
SKELETAL_STUDY = "DOI:10.1073/pnas.200221797"
MOTILITY_REVIEW = "DOI:10.3390/biom10040550"


def record(slug):
    return yaml.safe_load((ROOT / f"data/structures/appendage/{slug}.yaml").read_text())


def test_pfr_families_follow_cross_species_nomenclature_not_uniprot_mnemonics():
    doc = record("paraflagellar_rod")
    components = {c["component_id"]: c for c in doc["components"]}
    for key, genes, accession, label in [
        ("pfr1", {"PFR1", "PFRC", "PFRD"}, "UniProtKB:Q26789", "73 kDa"),
        ("pfr2", {"PFR2", "PFRA", "PFRB"}, "UniProtKB:P22225", "69 kDa"),
    ]:
        component = components[key]
        assert set(component["gene_symbols"]) == genes
        example = component["protein_examples"][0]
        assert example["uniprot_id"] == accession
        assert label in example["protein_label"]
        assert example["gene_symbol"] in genes
        assert NOMENCLATURE in {e["reference"] for e in example["evidence"]}
        assert NOMENCLATURE in {e["reference"] for e in component["evidence"]}
    graph = doc["causal_graphs"][0]
    for node in graph["nodes"]:
        if node.get("component_ref") in components:
            assert node["label"] == components[node["component_ref"]]["label"]
    tracked_edges = [
        e for e in graph["edges"]
        if "DOI:10.1128/MCB.19.12.8191" in {v["reference"] for v in e["evidence"]}
    ]
    assert len(tracked_edges) == 1
    assert tracked_edges[0]["subject"] == "pfr2"


def test_pfr2_requirement_does_not_exclude_reduced_rods():
    doc = record("paraflagellar_rod")
    pfr2 = next(c for c in doc["components"] if c["component_id"] == "pfr2")
    assert pfr2["essentiality"] == "CONDITIONAL"
    assert "full native" in pfr2["role"]
    assert "Crithidia deanei" in pfr2["role"]
    assert "detection limitations" in pfr2["role"]
    assert "DOI:10.1128/EC.4.3.516-525.2005" in {
        e["reference"] for e in pfr2["evidence"]
    }
    graph = doc["causal_graphs"][0]
    assert "reduced rods" in graph["description"]
    edge = next(e for e in graph["edges"] if e["subject"] == "pfr2")
    assert "not a universal requirement" in edge["description"]


def test_flaa_membership_is_not_a_universal_sheath_claim():
    doc = record("periplasmic_flagellum")
    component = next(c for c in doc["components"] if c["component_id"] == "flaA_sheath")
    assert component["essentiality"] == "UNKNOWN"
    assert component["protein_examples"][0]["uniprot_id"] == "UniProtKB:P70856"
    assert "Brachyspira hyodysenteriae" in component["role"]
    assert "unresolved precise localization" in component["role"]
    assert "Leptospira sheath formation does not require FlaA" in component["role"]
    graph = doc["causal_graphs"][0]
    filament = next(n for n in graph["nodes"] if n["node_id"] == "filament")
    assert "sheathed" not in filament["label"]
    edge = next(e for e in graph["edges"] if e["subject"] == "flaA_sheath")
    assert edge["predicate"] == "associates with"
    assert "lineage-specific" in edge["description"]
    assert {e["reference"] for e in edge["evidence"]} == {
        "DOI:10.1128/JB.180.9.2418-2425.1998", MOTILITY_REVIEW,
    }


def test_rotation_pathway_distinguishes_swimming_from_resting_skeletal_shape():
    doc = record("periplasmic_flagellum")
    graph = doc["causal_graphs"][0]
    state = next(n for n in graph["nodes"] if n["node_id"] == "cell_deformation")
    assert "during swimming" in state["label"]
    edges = {(e["subject"], e["object"]): e for e in graph["edges"]}
    assert ("basal_body_motor", "flagellar_rotation") in edges
    assert ("flagellar_rotation", "filament") in edges
    edge = edges[("flagellar_rotation", "cell_deformation")]
    evidence = {e["reference"]: e["notes"] for e in edge["evidence"]}
    assert "wave propagation" in evidence[MOTILITY_REVIEW]
    assert "not proof of this active edge" in evidence[SKELETAL_STUDY]
    assert "CCCP-paralyzed" in evidence[SKELETAL_STUDY]
    assert "does not require rotation" in evidence[SKELETAL_STUDY]
    assert ("cell_deformation", "motility") in edges
    assert len(graph["edges"]) == 7
    assert doc["mapping_status"] == "PROPOSED"
