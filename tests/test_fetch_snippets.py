"""Offline tests for scripts/fetch_snippets.py — no network.

The mutation tests matter more than the positive ones. `normalise` was
deliberately loosened after the canary showed it rejecting a quotation that is
genuinely in the paper (PMC's tag-stripped XML writes "( Kruse et al., 2005 )"
for the printed "(Kruse et al., 2005)"). Loosening a comparison is how a gate
stops gating, so each mutation below is a fabrication the gate must still fail.
"""

from __future__ import annotations

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
    return fs.normalise(snippet) in fs.normalise(source)


def test_a_real_quotation_is_found_despite_tag_stripping_artefacts():
    """The canary case: whitespace inside parentheses must not fail a true quote."""
    assert _found(QUOTED)


def test_case_curly_quotes_and_dash_style_do_not_defeat_a_match():
    assert _found("MreB DEPLETION results in loss of rod–like shape")
    assert _found("MreB depletion results in loss of rod-like shape")


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
