"""Preserve the experimentally bounded SIN inhibitory configuration."""

from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1] / "data/structures/cytoskeleton"
JOHNSON = "DOI:10.1038/emboj.2010.317"
GRALLERT = "DOI:10.1038/ncb2514"


def record(slug):
    return yaml.safe_load((ROOT / f"{slug}.yaml").read_text())


def test_interphase_sin_distinguishes_spg1_from_its_gap():
    doc = record("interphase_sin_signaling_complex")
    assert doc["definition_source"] == JOHNSON
    assert "Byr4-Cdc16 GAP" in doc["definition"]
    assert "Spg1 GTPase" in doc["definition"]
    assert "GTPase activator (Spg1" not in doc["definition"]


def test_interphase_sin_inhibition_preserves_stage_and_checkpoint_scope():
    doc = record("interphase_sin_signaling_complex")
    function = doc["functions"][0]
    assert "G2" in function["description"]
    assert "mitotic checkpoint arrest" in function["description"]
    assert "inactive before anaphase" not in function["description"]
    assert "Byr4-Cdc16" in doc["canonical_examples"][0]["note"]
    evidence = next(e for e in function["evidence"] if e["reference"] == JOHNSON)
    assert "metaphase" in evidence["notes"]


def test_interphase_sin_clarification_preserves_prior_discussions():
    doc = record("interphase_sin_signaling_complex")
    discussions = {d["discussion_id"]: d for d in doc["discussions"]}
    assert discussions["interphase_sin_complex_boundary"]["posed_date"] == "2026-09-29"
    assert discussions["resolve_interphase_sin_component_groundings"]["status"] == "OPEN"
    clarification = discussions["interphase_sin_inhibitory_scope_clarification"]
    assert clarification["status"] == "RESOLVED"
    assert "Spg1" in clarification["rationale"]
    assert "metaphase" in clarification["resolution_note"]
    assert {e["reference"] for e in clarification["evidence"]} >= {
        JOHNSON,
        "GO:0160066",
    }


def test_sid2_fin1_evidence_preserves_sin_independent_g2_context():
    doc = record("sin_men_signaling_complex")
    evidence = next(e for e in doc["evidence"] if e["reference"] == GRALLERT)
    assert "cytoplasmic" in evidence["notes"]
    assert "outside the SIN" in evidence["notes"]
    assert "SIN-ablation" in evidence["notes"]
    assert "links the SIN pathway to mitotic commitment" not in evidence["notes"]


@pytest.mark.parametrize(
    "slug,identifier,parent",
    [
        ("interphase_sin_signaling_complex", "GO:0160066", "GO:0160065"),
        ("sin_men_signaling_complex", "GO:0160065", "GO:0032991"),
    ],
)
def test_sin_scope_fixes_preserve_identity_and_proposed_status(slug, identifier, parent):
    doc = record(slug)
    assert doc["identifier"] == identifier
    assert doc["parent_structures"] == [parent]
    assert doc["mapping_status"] == "PROPOSED"
