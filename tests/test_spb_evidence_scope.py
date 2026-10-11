"""Retain the scope and provenance established by the SPB record review."""

from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1] / "data/structures/cytoskeleton"
GRALLERT = "DOI:10.1101/gad.296204"
NICKAS = "DOI:10.1128/EC.2.3.431-445.2003"


def record(slug):
    return yaml.safe_load((ROOT / f"{slug}.yaml").read_text())


def test_old_spb_definition_preserves_stage_and_species_scope():
    doc = record("old_mitotic_spindle_pole_body")
    assert doc["definition_source"] == GRALLERT
    assert "Schizosaccharomyces pombe" in doc["definition"]
    assert "late anaphase B" in doc["definition"]
    assert "both poles earlier" in doc["definition"]
    assert "segregates to the daughter cell" not in doc["definition"]


def test_old_spb_example_distinguishes_early_and_late_signaling():
    example = record("old_mitotic_spindle_pole_body")["canonical_examples"][0]
    assert example["taxon_id"] == "NCBITaxon:4896"
    assert example["reference"] == GRALLERT
    assert "both poles in early anaphase B" in example["note"]
    assert "late anaphase B" in example["note"]
    assert "not constitutively absent" in example["note"]


def test_old_spb_source_conflict_clarifies_without_erasing_prior_discussions():
    doc = record("old_mitotic_spindle_pole_body")
    discussions = {d["discussion_id"]: d for d in doc["discussions"]}
    assert discussions["old_mitotic_spb_boundary"]["posed_date"] == "2026-09-29"
    assert discussions["resolve_old_mitotic_spb_signaling_exclusions"]["status"] == "OPEN"
    clarification = discussions["old_mitotic_spb_signaling_scope_clarification"]
    assert clarification["status"] == "RESOLVED"
    assert {e["reference"] for e in clarification["evidence"]} == {GRALLERT, "GO:0071957"}
    assert "supersedes" in clarification["resolution_note"]
    assert "Saccharomyces cerevisiae" in clarification["rationale"]
    evidence = next(e for e in doc["evidence"] if e["reference"] == GRALLERT)
    assert "Figure 5" in evidence["notes"]
    assert "Figure 6" in evidence["notes"]


def test_meiotic_outer_plaque_uses_the_actual_nickas_article_title():
    doc = record("meiotic_outer_plaque")
    evidence = next(e for e in doc["evidence"] if e["reference"] == NICKAS)
    assert "Growth of the Prospore Membrane" in evidence["notes"]
    assert "Growth of the Spores" not in evidence["notes"]


@pytest.mark.parametrize(
    "slug,identifier,parent",
    [
        ("old_mitotic_spindle_pole_body", "GO:0071957", "GO:0044732"),
        ("meiotic_outer_plaque", "cellstructuremech:meiotic_outer_plaque", "GO:0005824"),
    ],
)
def test_scope_fixes_do_not_promote_or_reidentify_records(slug, identifier, parent):
    doc = record(slug)
    assert doc["identifier"] == identifier
    assert doc["parent_structures"] == [parent]
    assert doc["mapping_status"] == "PROPOSED"
