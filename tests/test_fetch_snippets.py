"""Offline tests for scripts/fetch_snippets.py — no network.

The mutation tests matter more than the positive ones. `normalise` was
deliberately loosened after the canary showed it rejecting a quotation that is
genuinely in the paper (PMC's tag-stripped XML writes "( Kruse et al., 2005 )"
for the printed "(Kruse et al., 2005)"). Loosening a comparison is how a gate
stops gating, so each mutation below is a fabrication the gate must still fail.
"""

from __future__ import annotations

import sys

from scripts import fetch_snippets as fs

# Real sentence from PMC5846203, as the tag stripper delivers it.
SOURCE = ("E. coli MreB forms membrane-bound, anti-parallel double protofilaments that are "
          "essential for rod-shape determination ( Van den Ent et al., 2014 ), MreB depletion "
          "results in loss of rod-like shape and rounding ( Kruse et al., 2005 ), and there are "
          "no E. coli mutants or growth conditions known to restore rod-like shape in the "
          "absence of MreB.")

# The quotation as a curator reads it off the published page.
QUOTED = ("MreB depletion results in loss of rod-like shape and rounding (Kruse et al., 2005), "
          "and there are no E. coli mutants or growth conditions known to restore rod-like "
          "shape in the absence of MreB.")


def _found(snippet: str, source: str = SOURCE) -> bool:
    """Verbatim: matched at the exact or despaced tier, not merely present."""
    return fs.match_tier(snippet, source) in (fs.EXACT, fs.DESPACED)


def test_a_real_quotation_is_found_despite_tag_stripping_artefacts():
    """The canary case: whitespace inside parentheses must not fail a true quote."""
    assert _found(QUOTED)


def test_an_exact_substring_matches_at_the_exact_tier():
    assert fs.match_tier("MreB depletion results in loss of rod-like shape", SOURCE) == fs.EXACT


# --- mutation tests: each is a way a snippet can be wrong, and must fail ---

def test_a_changed_word_is_caught():
    assert not _found(QUOTED.replace("loss of rod-like shape", "loss of spherical shape"))


def test_a_negation_flip_is_caught():
    """The defect this gate exists for: a quotation reworded to say the opposite."""
    assert not _found(QUOTED.replace("there are no E. coli mutants",
                                     "there are many E. coli mutants"))


def test_a_dropped_qualifier_is_caught():
    """Deleting 'no ... known to' silently strengthens the claim."""
    assert not _found("there are E. coli mutants or growth conditions that restore rod-like shape")


def test_a_fabricated_sentence_in_the_papers_own_vocabulary_is_caught():
    assert not _found("MreB depletion results in immediate cell lysis and loss of viability.")


def test_two_real_fragments_spliced_together_are_caught():
    """Both halves appear; the sentence they form does not."""
    assert not _found("MreB depletion results in loss of rod-shape determination")


def test_reordered_clauses_are_caught():
    assert not _found("Rounding and loss of rod-like shape results from MreB depletion")


# --- collection and readability ---

def test_evidence_items_carry_the_claim_they_are_attached_to():
    """A suggestion is only as good as the claim it is ranked against."""
    doc = {"label": "MreB filament", "associated_traits": [
        {"trait_label": "rod shaped", "evidence": [
            {"reference": "DOI:10.1016/j.cell.2018.02.050", "snippet": "x", "notes": "n"}]}]}
    items = fs.evidence_items([(fs.Path("mreb.yaml"), doc)])
    assert len(items) == 1
    assert items[0]["claim"] == "rod shaped"
    assert items[0]["path"] == "associated_traits[0].evidence[0]"
    assert items[0]["record"] == "mreb.yaml"


def test_evidence_is_collected_from_every_depth_not_a_fixed_list_of_fields():
    """Evidence hangs off components, images, traits, properties and more; a
    collector that enumerated known parents would silently skip new ones."""
    doc = {"label": "R", "components": [{"label": "c", "evidence": [{"reference": "PMID:1"}]}],
           "images": [{"evidence": [{"reference": "DOI:10.1/x"}]}],
           "physical_properties": {"nested": {"evidence": [{"reference": "PMID:2"}]}}}
    refs = {i["reference"] for i in fs.evidence_items([(fs.Path("r.yaml"), doc)])}
    assert refs == {"PMID:1", "DOI:10.1/x", "PMID:2"}


def test_candidate_sentences_rank_by_overlap_with_the_claim():
    text = ("The ribosome translates messenger RNA. MreB depletion results in loss of rod-like "
            "shape and rounding of the cell. Buffers were prepared as described.")
    got = fs.candidate_sentences(text, "rod shaped", "cell shape depends on MreB")
    assert "rod-like" in got[0]


def test_candidate_sentences_return_nothing_rather_than_noise():
    """No overlap must yield no suggestion — a ranked list of irrelevant
    sentences invites a curator to quote one."""
    assert fs.candidate_sentences("Buffers were prepared as described. Gels were run.",
                                  "flagellar rotation", "") == []


def test_plain_text_keeps_sentence_boundaries():
    assert fs.plain("<p>One thing.</p><p>Another thing.</p>") == "One thing. Another thing."
    assert "alert" not in fs.plain("<script>alert(1)</script><p>Text.</p>")


def test_readability_levels_are_ordered_worst_to_best():
    """The audit counts these; a renamed level must not silently vanish."""
    assert (fs.UNREADABLE, fs.ABSTRACT, fs.FULL_TEXT) == ("unreadable", "abstract", "full_text")


# --- literature vs database record ---

def test_urls_and_ontology_curies_are_not_treated_as_papers():
    """SubtiWiki gene pages and GO terms are records; counting them among
    unreadable papers inflated the audit's headline number from 3 to 21."""
    for reference in ("https://www.subtiwiki.uni-goettingen.de/v5/gene/hag",
                      "GO:0030257", "UniProtKB:P0A6A9"):
        assert not fs.is_literature_shape(reference)


def test_dois_and_pmids_are_treated_as_papers():
    for reference in ("DOI:10.1016/j.cell.2018.02.050", "PMID:21047262"):
        assert fs.is_literature_shape(reference)


def test_literature_types_include_book_chapters():
    """The corpus's one genuinely unreadable paper is an ASM book chapter; if
    'book-chapter' were not literature it would be excused rather than counted."""
    assert "book-chapter" in fs.LITERATURE_TYPES
    assert "journal-article" in fs.LITERATURE_TYPES
    assert "dataset" not in fs.LITERATURE_TYPES


# --- what counts as a sentence, and as text at all ---

def test_a_genus_initial_does_not_end_a_sentence():
    """'E. coli' split a real sentence into a fragment that --verify would still
    pass, because the fragment is a literal substring of the source."""
    got = fs.split_sentences("MreB is essential. E. coli MreB forms filaments. B. subtilis differs.")
    assert got == ["MreB is essential.", "E. coli MreB forms filaments.", "B. subtilis differs."]


def test_common_abbreviations_do_not_end_a_sentence():
    assert fs.split_sentences("It is essential (Kruse et al., 2005). Fig. 2 shows this.") == \
        ["It is essential (Kruse et al., 2005).", "Fig. 2 shows this."]


def test_real_sentence_ends_still_split():
    """The guard must not swallow genuine boundaries."""
    assert len(fs.split_sentences("One thing happened. Another thing followed. A third did too.")) == 3


def test_journal_front_matter_is_not_offered_as_a_quotation():
    """The ranker offered 'Cell Cell 319 nihpa 0413066 ... Article How to build a
    bacterial cell' — journal metadata, not a claim anyone made."""
    text = fs.plain("<article><front>Cell Cell 319 nihpa 0413066 0092-8674</front>"
                    "<body><p>MreB rotates around the cell circumference.</p></body>"
                    "<back><ref-list>Kruse T, 2005</ref-list></back></article>")
    assert text == "MreB rotates around the cell circumference."


def test_the_bibliography_is_not_quotable():
    """A sentence from the reference list is not evidence for anything."""
    assert "Kruse" not in fs.plain("<body><p>Real claim.</p></body><ref-list>Kruse T, 2005</ref-list>")


def test_an_abstract_without_a_body_element_still_yields_text():
    """PubMed abstracts are not JATS articles; requiring <body> would blank them."""
    assert fs.plain("<AbstractText>Bacteria employ cytoskeletal elements.</AbstractText>") == \
        "Bacteria employ cytoskeletal elements."


def test_the_jats_abstract_is_quotable_even_though_it_sits_in_front_matter():
    """Keeping only <body> made every abstract sentence unquotable; --verify
    caught it on a real snippet from this corpus."""
    text = fs.plain("<article><front><journal-meta>Cell 0092-8674</journal-meta>"
                    "<abstract><p>MreB both senses and changes cell shape.</p></abstract></front>"
                    "<body><p>Rotation was measured.</p></body></article>")
    assert "MreB both senses and changes cell shape." in text
    assert "0092-8674" not in text
    assert "Rotation was measured." in text


# --- a failure to ask is not an answer (#146) ---

class _Transport:
    """Stand-in for _get: replays a scripted status per URL substring."""

    def __init__(self, script):
        self.script = script
        self.calls = []

    def __call__(self, url, timeout=45.0):
        self.calls.append(url)
        for fragment, result in self.script.items():
            if fragment in url:
                return result
        return (fs.TRANSPORT_FAILURE, "")


def test_a_transport_failure_is_not_the_verdict_unreadable(monkeypatch):
    """A dead socket says nothing about the paper. Reporting `unreadable` would
    indict the corpus for a local network fault -- demonstrated against
    PMC5846203, whose full text is known good."""
    monkeypatch.setattr(fs, "_get", _Transport({}))
    identity = {"pmid": "29522748", "pmcid": "PMC5846203", "unanswered": False}
    readability, source, text = fs.fetch_text(identity)
    assert readability == fs.UNCHECKED
    assert (source, text) == ("", "")


def test_a_real_404_still_means_unreadable(monkeypatch):
    """The server answered. That is a verdict and must not be softened."""
    monkeypatch.setattr(fs, "_get", _Transport({"efetch": (404, ""), "fullTextXML": (404, "")}))
    assert fs.fetch_text({"pmid": "1", "pmcid": "PMC1"})[0] == fs.UNREADABLE


def test_an_unanswered_identity_is_never_cached(monkeypatch):
    """Caching a failed resolution leaves the paper permanently unreadable with
    nothing to say why -- it survives until someone deletes build/ by hand."""
    monkeypatch.setattr(fs, "_get", _Transport({}))
    monkeypatch.setattr(fs.time, "sleep", lambda *_: None)
    cache = {}
    fs._load_texts(["DOI:10.1016/j.cell.2018.02.050"], cache)
    assert cache == {}


def test_an_answered_identity_is_cached(monkeypatch):
    """The guard must not disable caching altogether."""
    monkeypatch.setattr(fs, "_get", _Transport({
        "idconv": (200, '{"records":[{"pmid":"29522748","pmcid":"PMC5846203"}]}'),
        "efetch.fcgi?db=pmc": (200, "<body><p>" + "x" * 5000 + "</p></body>"),
    }))
    monkeypatch.setattr(fs.time, "sleep", lambda *_: None)
    cache = {}
    fs._load_texts(["DOI:10.1016/j.cell.2018.02.050"], cache)
    assert cache["DOI:10.1016/j.cell.2018.02.050"]["pmcid"] == "PMC5846203"


def test_transport_failures_are_retried_before_giving_up(monkeypatch):
    calls = {"n": 0}

    def flaky(url, timeout=45.0):
        calls["n"] += 1
        raise OSError("connection refused")

    monkeypatch.setattr(fs.urllib.request, "urlopen", flaky)
    monkeypatch.setattr(fs.time, "sleep", lambda *_: None)
    assert fs._get("https://example.invalid/x") == (fs.TRANSPORT_FAILURE, "")
    assert calls["n"] == fs.RETRIES


def test_an_http_error_is_not_retried(monkeypatch):
    """The server already answered; retrying wastes a request and a rate limit."""
    calls = {"n": 0}

    def refused(url, timeout=45.0):
        calls["n"] += 1
        raise fs.urllib.error.HTTPError(url, 404, "Not Found", {}, None)

    monkeypatch.setattr(fs.urllib.request, "urlopen", refused)
    assert fs._get("https://example.invalid/x") == (404, "")
    assert calls["n"] == 1


def test_classify_doi_reports_unchecked_rather_than_guessing(monkeypatch):
    """Silence from Crossref and DataCite must not become 'literature'."""
    monkeypatch.setattr(fs, "_get", _Transport({}))
    assert fs.classify_doi("10.1/x") == fs.UNCHECKED


# --- the two populations are named apart (#147) ---

def test_evidence_items_are_distinguished_from_bare_citations():
    """#133 counts entries in `evidence` lists; this tool also sees a bare
    `reference` on a taxon note or image. Reporting one number for both made a
    changed definition look like a changed count."""
    doc = {"label": "R",
           "associated_traits": [{"trait_label": "t", "evidence": [{"reference": "PMID:1"}]}],
           "taxonomic_distribution": [{"taxon_label": "Bacteria", "reference": "PMID:2"}]}
    items = {i["reference"]: i["in_evidence"] for i in fs.evidence_items([(fs.Path("r.yaml"), doc)])}
    assert items == {"PMID:1": True, "PMID:2": False}


# --- graded comparison: imprecise is not the same as fabricated (#143) ---

def test_the_canary_case_still_passes_as_verbatim():
    """Whitespace injected by tag stripping is an extraction artefact."""
    assert fs.match_tier(QUOTED, SOURCE) == fs.DESPACED


def test_curly_quotes_are_reported_as_not_verbatim_rather_than_absent():
    """The text IS in the paper; the record's copy of it is not exact. Passing
    this silently would let `snippet` claim verbatim while holding something else."""
    source = 'He wrote “MreB senses shape” in the review.'
    assert fs.match_tier('"MreB senses shape"', source) == fs.LOOSE


def test_an_en_dash_swapped_for_a_hyphen_is_not_verbatim():
    assert fs.match_tier("rod–like shape", "the rod-like shape of cells") == fs.LOOSE


def test_a_case_difference_is_not_verbatim():
    assert fs.match_tier("MREB DEPLETION RESULTS", "MreB depletion results in rounding") == fs.LOOSE


def test_hyphens_stay_significant_unlike_the_pdf_equivalent():
    """A PDF line-break hyphen is indistinguishable from a compound hyphen, so the
    tool this is modelled on drops hyphens. JATS has no line breaks, so 'rodlike'
    and 'rod-like' are genuinely different words and must not match."""
    assert fs.match_tier("rodlike shape", "the rod-like shape of cells") == fs.ABSENT


def test_every_fabrication_mutation_is_still_absent_at_every_tier():
    """The loosening must not have reached the errors. Same six cases as above."""
    for mutation in (
        QUOTED.replace("loss of rod-like shape", "loss of spherical shape"),
        QUOTED.replace("there are no E. coli mutants", "there are many E. coli mutants"),
        "there are E. coli mutants or growth conditions that restore rod-like shape",
        "MreB depletion results in immediate cell lysis and loss of viability.",
        "MreB depletion results in loss of rod-shape determination",
        "Rounding and loss of rod-like shape results from MreB depletion",
    ):
        assert fs.match_tier(mutation, SOURCE) == fs.ABSENT


def test_an_empty_snippet_is_absent_not_trivially_present():
    """"" is a substring of everything; it must never read as verified."""
    assert fs.match_tier("   ", SOURCE) == fs.ABSENT


# --- the report must be machine-readable (#151) ---

def test_the_report_round_trips_through_csv_dictreader(tmp_path, monkeypatch):
    """A '# scope:' comment line made DictReader take it as the header and
    misparse every row -- silently, which is the worst shape for a report whose
    job is to be counted."""
    import csv

    report = tmp_path / "readability.tsv"
    monkeypatch.setattr(fs, "_load_texts",
                        lambda refs, cache: {r: (fs.ABSTRACT, "PubMed/1", "text") for r in refs})
    monkeypatch.setattr(fs, "load_records", lambda: [
        (fs.Path("r.yaml"), {"label": "R", "components": [
            {"label": "c", "evidence": [{"reference": "PMID:1"}]}]})])
    monkeypatch.setattr(sys, "argv", ["fetch_snippets", "--audit", "--report", str(report)])
    assert fs.main() == 0

    rows = list(csv.DictReader(report.open(), delimiter="\t"))
    assert [r["reference"] for r in rows] == ["PMID:1"]
    assert rows[0]["scope"] == "whole corpus"
    assert rows[0]["readability"] == "abstract"


# --- naming the actual difference, and gating on it (#153, #154) ---

def test_the_reported_difference_names_only_what_actually_differs():
    """_loose unifies case, quotes and dashes together, so reporting all three
    every time sends the curator looking for two things that are not there."""
    assert fs.describe_difference("rod–like", "rod-like shape") == "dash style"
    assert fs.describe_difference('"MreB"', '“MreB” in the text') == "quote style"
    assert fs.describe_difference("MREB DEPLETION", "MreB depletion follows") == "letter case"


def test_strict_fails_on_a_snippet_that_is_present_but_not_verbatim(tmp_path, monkeypatch, capsys):
    """Default --check passes it; --strict is the way to enforce verbatim."""
    doc = {"label": "R", "components": [{"label": "c", "evidence": [
        {"reference": "PMID:1", "snippet": "rod–like shape"}]}]}
    monkeypatch.setattr(fs, "load_records", lambda *a, **k: [(fs.Path("r.yaml"), doc)])
    monkeypatch.setattr(fs, "_load_texts",
                        lambda refs, cache: {r: (fs.ABSTRACT, "PubMed/1", "the rod-like shape here")
                                             for r in refs})
    monkeypatch.setattr(fs, "IDMAP_PATH", tmp_path / "idmap.json")

    monkeypatch.setattr(sys, "argv", ["fetch_snippets", "--verify", "--check"])
    assert fs.main() == 0
    assert "not verbatim" in capsys.readouterr().err

    monkeypatch.setattr(sys, "argv", ["fetch_snippets", "--verify", "--check", "--strict"])
    assert fs.main() == 1


def test_strict_does_not_change_what_counts_as_fabricated(tmp_path, monkeypatch):
    """A quotation genuinely absent must fail with or without --strict."""
    doc = {"label": "R", "components": [{"label": "c", "evidence": [
        {"reference": "PMID:1", "snippet": "MreB causes immediate lysis"}]}]}
    monkeypatch.setattr(fs, "load_records", lambda *a, **k: [(fs.Path("r.yaml"), doc)])
    monkeypatch.setattr(fs, "_load_texts",
                        lambda refs, cache: {r: (fs.ABSTRACT, "PubMed/1", "the rod-like shape here")
                                             for r in refs})
    monkeypatch.setattr(fs, "IDMAP_PATH", tmp_path / "idmap.json")
    monkeypatch.setattr(sys, "argv", ["fetch_snippets", "--verify", "--check"])
    assert fs.main() == 1


def test_the_snippet_count_line_names_what_each_number_counts(tmp_path, monkeypatch, capsys):
    """'(10 of them evidence items)' read as qualifying the 3 quoted snippets
    when it was computed over all 14 citations."""
    doc = {"label": "R",
           "components": [{"label": "c", "evidence": [
               {"reference": "PMID:1", "snippet": "rod-like shape"}]}],
           "taxonomic_distribution": [{"taxon_label": "Bacteria", "reference": "PMID:1"}]}
    monkeypatch.setattr(fs, "load_records", lambda *a, **k: [(fs.Path("r.yaml"), doc)])
    monkeypatch.setattr(fs, "_load_texts",
                        lambda refs, cache: {r: (fs.ABSTRACT, "PubMed/1", "the rod-like shape here")
                                             for r in refs})
    monkeypatch.setattr(fs, "IDMAP_PATH", tmp_path / "idmap.json")
    monkeypatch.setattr(sys, "argv", ["fetch_snippets", "--verify"])
    fs.main()
    err = capsys.readouterr().err
    assert "1 of 2 citations carry a snippet; 1 of those are evidence items" in err
    assert "2 citations = 1 evidence items + 1 bare references" in err
