---
name: literature-evidence
description: Read the papers this corpus cites and hold its evidence to them — audit what is readable, propose verbatim snippets for a curator to choose, and verify that every existing snippet is really in its source. Use when adding or checking evidence, when a claim needs a snippet and DOI, or when asked whether a record's assertions can be checked.
---

# Ground a claim in the paper that supports it

Every claim-bearing field in this corpus carries `evidence`, and every evidence
item names a `reference`. Until this skill existed, nothing read those
references: `check_curies.py` asks whether a DOI or PMID *resolves*, never what
it says. That is how the corpus reached 341 evidence items with 3 verbatim
snippets (#133), and how one record cited a review for the opposite of what the
review reports.

`scripts/fetch_snippets.py` is the tool. This skill is the judgement around it.

## The distinction the schema makes

- **`snippet`** is a **verbatim quotation** from the source. Nothing else may go
  here. It is the only field a machine can check, and `--verify` checks it.
- **`notes`** is the curator's paraphrase, gloss, or reason for citing. Anything
  that is not a literal quotation belongs here.

Moving a paraphrase into `snippet` to satisfy a gate is the worst thing this
skill can lead to. An honest `notes` with an empty `snippet` is fine; a
`snippet` that is not in the paper is a fabricated quotation.

## The three modes

```bash
just evidence-audit                      # what is readable, corpus-wide
uv run python scripts/fetch_snippets.py --suggest --record data/structures/<cat>/<rec>.yaml
just evidence-verify                     # every snippet occurs in its source
```

**`--audit`** classifies every reference: `full_text`, `abstract`, `unreadable`,
`not_literature`, or `unchecked`. It writes `reports/evidence_readability.tsv`
and prints the one number that matters — claims citing a paper with no reachable
text *and* no quotation, which nobody can check.

`unchecked` means no route answered — a network fault, not a fact about the
paper. It is excluded from that count and never fails `--verify`, because a
question we failed to ask is not an answer. Identities resolved during an outage
are not cached, so the next run retries them.

Two populations are counted and named apart: **citations** (every field carrying
a `reference`, including taxon notes, canonical examples, causal-graph edges and
images) and **evidence items** (entries in an `evidence` list, the population
#133 counts). Both are checked; only the labels differ.

**`--suggest`** prints candidate sentences ranked against the claim. **It never
picks.** Choosing which sentence supports a claim is the judgement the evidence
field exists to record; a tool that picked would be generating the appearance of
grounding. Read the candidates, read enough of the paper around the one you
choose to know it means what it appears to mean, then paste it verbatim.

**`--verify`** is the anti-fabrication gate. Run it before every commit that
touches a snippet. It grades what it finds, because "copied imprecisely" and
"not in the paper" need different responses:

| verdict | meaning | action |
|---|---|---|
| verbatim | matches exactly, or differs only in whitespace | none |
| **not verbatim** | the text is in the paper; the record's copy differs in case, quote or dash style | re-copy the exact characters |
| **ABSENT** | not in the source at any tier | the quotation is fabricated or reworded — fix it |
| not checked | no route answered | re-run when the network is back |

Only ABSENT fails the run; add `--strict` to fail on *not verbatim* too, when
finishing a record. The report names which of case, quote or dash style actually
differs, not all three. Whitespace differences pass silently: stripping
`<xref>` tags renders "(Kruse et al., 2005)" with spaces inside the parentheses,
and that is an extraction artefact, not a difference in the text. Hyphens stay
significant — "rod-like" and "rodlike" are different words.

## Rules

1. **Quote the claim, not the topic.** A sentence containing the same words is
   not support. The MreB record cited a review for "MreB is required for rod
   shape"; the quotation that survived says depletion causes rounding *and* that
   no mutant restores shape without it — the second clause is what makes it
   `REQUIRED_FOR` rather than `MODULATES`.
2. **Read around the sentence.** `--suggest` returns sentences stripped of
   context, and papers contain sentences stating what the authors go on to
   refute. Full text is fetched to `build/literature/`; read it.
3. **An abstract is a weak source for a specific number.** Physical properties,
   subunit counts and rates need the methods or results, not the summary. Four
   such properties were removed in #91 for resting on titles alone.
4. **Unreadable is a finding, not a dead end.** Say so in `notes` and leave
   `snippet` empty rather than paraphrasing a title into something that reads
   like knowledge of the paper's contents. `unchecked` is *not* that finding —
   re-run it when the network is back before concluding anything.
5. **A quotation contradicting the record outranks the record.** File it; do not
   quietly pick a different sentence.

## Establishing readability

**Probe; never trust a flag.** NCBI's ID converter knows only PMC, so a paper
absent from PMC looks absent from PubMed too — that is how PMID 21047262 was
recorded as "no PubMed record" in #133 and the citation removed on a false
premise. Europe PMC's `inEPMC: Y` is no better: it says so for PMC5433867, whose
`fullTextXML` returns 404. The script therefore tries NCBI's converter, Europe
PMC search, `efetch db=pmc`, Europe PMC full text, then `efetch db=pubmed`, and
reports what actually came back.

If you assert a reference is unreadable, name the routes tried.

**A 200 is not text.** Publisher text-mining endpoints answer 200 with an
entitlement stub: Crossref's `text-mining` links for three Elsevier papers each
returned ~1.8 KB of metadata — title, journal, `openaccess: false`, no body
(#142). Adding that route would have registered them as full text and then
reported their correct quotations as fabricated. Any new full-text route must be
shown to contain body prose, not merely to return 200 — the same rule that
retired Europe PMC's `inEPMC` flag and Semantic Scholar's `isOpenAccess`.

## Not every reference is a paper

SubtiWiki gene pages, GO terms and deposited datasets are `not_literature`:
"what does it say" is the wrong question, and `check_curies.py` already answers
the right one. Counting them among unreadable papers inflated the headline from
3 to 21. `--verify` refuses a `snippet` on one of these outright.

## Before committing evidence

```bash
just evidence-verify   # bare; a pipe hides the exit code (PR #39)
just qc
```

`--verify` needs the network. It is not part of `just qc`, which runs offline —
so it is a discipline, not a gate that will catch you. Run it.

## Related

- `scripts/check_curies.py` — does the identifier resolve (not what it says).
- `docs/CURATION.md` — the verbatim-snippet rule and the evidence contract.
- `source-queue` — whether to adopt a source at all.
