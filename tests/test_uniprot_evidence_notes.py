"""Offline tests for the #41 evidence-note enrichment — no network."""

from __future__ import annotations

from cellstructuremech.ingest import _short_citation
from scripts.uniprot_sl import boilerplate_note, evidence_note, refresh_evidence_notes

SUMMARY = {
    "title": "Structural determinants of the outer shell of beta-carboxysomes.",
    "authors": [{"name": "Rae BD"}, {"name": "Long BM"}],
    "pubdate": "2012 Aug 20",
    "source": "PLoS One",
}


def test_a_citation_names_author_year_title_and_journal():
    assert _short_citation(SUMMARY) == (
        "Rae BD et al. 2012, ‘Structural determinants of the outer shell of "
        "beta-carboxysomes’, PLoS One."
    )


def test_a_single_author_is_not_given_et_al():
    assert _short_citation({**SUMMARY, "authors": [{"name": "Rae BD"}]}).startswith("Rae BD 2012,")


def test_a_summary_without_a_title_yields_no_citation():
    """A reference the reader still cannot identify is better left as it was than
    dressed up with a half-citation."""
    assert _short_citation({**SUMMARY, "title": ""}) is None
    assert _short_citation({}) is None


def test_an_enriched_note_keeps_the_provenance_it_had():
    """The ECO code and the 'as cited by UniProt' attribution are the claim; the
    citation is added in front of them, not instead of them."""
    note = evidence_note("carboxysome", "Q03511", "Rae BD et al. 2012, ‘T’, PLoS One.")
    assert note.startswith("Rae BD et al. 2012,")
    assert boilerplate_note("carboxysome", "Q03511") in note


def test_a_note_stays_as_it_was_when_no_citation_could_be_fetched():
    assert evidence_note("carboxysome", "Q03511", None) == boilerplate_note("carboxysome", "Q03511")


def _doc(notes: str) -> dict:
    return {"label": "carboxysome", "components": [{"label": "shell", "protein_examples": [
        {"uniprot_id": "UniProtKB:Q03511",
         "evidence": [{"reference": "PMID:17675289", "notes": notes}]}]}]}


def test_backfill_rewrites_only_the_boilerplate_it_wrote(monkeypatch):
    import scripts.uniprot_sl as mod
    monkeypatch.setattr(mod, "pubmed_citations", lambda pmids: {"17675289": "Long BM et al. 2007."})
    doc = _doc(boilerplate_note("carboxysome", "Q03511"))
    assert refresh_evidence_notes(doc) == ["PMID:17675289 on Q03511"]
    assert doc["components"][0]["protein_examples"][0]["evidence"][0]["notes"].startswith("Long BM")


def test_backfill_never_overwrites_a_curator_written_note(monkeypatch):
    """The difference between filling a gap and destroying someone's work."""
    import scripts.uniprot_sl as mod
    monkeypatch.setattr(mod, "pubmed_citations", lambda pmids: {"17675289": "Long BM et al. 2007."})
    doc = _doc("Curator: this paper shows the shell is permeable to bicarbonate.")
    assert refresh_evidence_notes(doc) == []
    assert doc["components"][0]["protein_examples"][0]["evidence"][0]["notes"].startswith("Curator:")


def test_backfill_is_idempotent(monkeypatch):
    """Re-emitting an unchanged record must be byte-identical, so a second run
    must find nothing to do."""
    import scripts.uniprot_sl as mod
    monkeypatch.setattr(mod, "pubmed_citations", lambda pmids: {"17675289": "Long BM et al. 2007."})
    doc = _doc(boilerplate_note("carboxysome", "Q03511"))
    assert refresh_evidence_notes(doc)
    assert refresh_evidence_notes(doc) == []


def test_backfill_ignores_references_that_are_not_pubmed(monkeypatch):
    import scripts.uniprot_sl as mod
    monkeypatch.setattr(mod, "pubmed_citations", lambda pmids: {})
    doc = _doc(boilerplate_note("carboxysome", "Q03511"))
    doc["components"][0]["protein_examples"][0]["evidence"][0]["reference"] = "DOI:10.1/x"
    assert refresh_evidence_notes(doc) == []
