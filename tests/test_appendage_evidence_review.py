"""Preserve assay boundaries in haptonema and mastigoneme evidence."""

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def record(slug):
    return yaml.safe_load((ROOT / f"data/structures/appendage/{slug}.yaml").read_text())


def test_haptonema_calcium_note_reports_shape_not_influx_measurement():
    doc = record("haptonema")
    graph = doc["causal_graphs"][0]
    edge = next(e for e in graph["edges"] if e["subject"] == "calcium_signal")
    assert graph["scope_status"] == "NONMECHANISTIC"
    assert edge["object"] == "haptonemal_singlet_microtubules"
    evidence = edge["evidence"][0]
    assert evidence["reference"] == "DOI:10.1242/bio.036590"
    assert "taxol blocked rapid haptonemal coiling" in evidence["notes"]
    assert "calcium-free conditions" in evidence["notes"]
    assert "planar bend" in evidence["notes"]
    assert "not a direct measurement" in evidence["notes"]
    assert "without preventing Ca2+ influx" not in evidence["notes"]


def test_mastigoneme_function_keeps_conflicting_strain_specific_results():
    doc = record("mastigoneme")
    function = next(
        f for f in doc["functions"] if f["function_id"] == "ciliary_surface_motility_modulation"
    )
    assert "context-dependent" in function["label"]
    assert "general hydrodynamic contribution is therefore not established" in function["description"]
    evidence = {e["reference"]: e["notes"] for e in function["evidence"]}
    liu = evidence["DOI:10.1083/jcb.202001122"]
    amador = evidence["DOI:10.1016/j.bpj.2020.05.003"]
    assert "LMJ.RY0402.052413" in liu and "15% slower" in liu
    assert "LMJ.RY0402.136134" in amador
    assert "did not show significant enhancement" in amador
    assert "Increased turning" in amador
    assert "not evidence that all motility phenotypes are absent" in amador


def test_mastigoneme_conflict_stays_open_without_changing_assembly_boundary():
    doc = record("mastigoneme")
    discussions = {d["discussion_id"]: d for d in doc["discussions"]}
    conflict = discussions["resolve_mastigoneme_swimming_conflict"]
    assert conflict["status"] == "OPEN"
    assert conflict["attaches_to"] == ["functions#ciliary_surface_motility_modulation"]
    assert {e["reference"] for e in conflict["evidence"]} == {
        "DOI:10.1083/jcb.202001122",
        "DOI:10.1016/j.bpj.2020.05.003",
        "DOI:10.1016/j.cell.2024.03.005",
    }
    assert discussions["ground_mastigoneme_protein_families"]["status"] == "OPEN"
    assert discussions["curate_stramenopile_and_cryptophyte_scope"]["status"] == "OPEN"
    roles = {c["component_id"]: c["component_role"] for c in doc["components"]}
    assert roles == {
        "mst1_hrgp": "CONSTITUENT",
        "mst3_hrgp": "CONSTITUENT",
        "pkd2_anchor": "ASSOCIATED_MACHINERY",
    }
    assert doc["causal_graphs"][0]["scope_status"] == "MECHANISTIC"
    assert len(doc["causal_graphs"][0]["edges"]) == 3
