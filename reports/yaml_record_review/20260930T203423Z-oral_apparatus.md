# Oral apparatus YAML record review

- PR: #1838
- Record: `data/structures/other/oral_apparatus.yaml`
- Identifier: `GO:0031912`
- Reviewer: codex
- Reviewed at: 2026-09-30T20:34:23Z

## Scope

Reviewed the PR #1838 diff and the newly curated `GO:0031912` oral apparatus
record for duplicate identity, exact GO grounding, parentage, child-part
modeling, ciliate taxonomic scope, Tetrahymena evidence, generated artifact
coverage, and append-only history coverage.

## Checks

- Confirmed the GitHub PR diff contains exactly the 14 expected initial files:
  the new source YAML, one append-only history record, regenerated README and
  embedding JSON, regenerated listing/data pages, and the rendered structure
  page.
- Re-ran an ignored-file-inclusive duplicate search for `GO:0031912`,
  `GO_0031912`, `oral apparatus`, `GO:0032123`, `GO_0032123`, `deep fiber`,
  and `deep fibre`. Matches were limited to the new oral-apparatus
  record/generated artifacts, the GO:0032123 child grounding introduced by this
  record, and the updated cache/report/history outputs.
- Re-read `data/structures/other/oral_apparatus.yaml` and verified that
  `GO:0031912` is curated as the whole ciliate feeding apparatus, not as the
  cytostome opening or its `GO:0032123` deep-fiber child.
- Re-read `history/records/oral_apparatus/2026-09-30T195024Z-codex-02ea1e.yaml`
  and confirmed it points at the new record and summarizes the CREATE event.
- Checked OLS-derived structure relations used by the record: `GO:0110165` as
  direct parent and `GO:0032123` as a direct child/part of the oral apparatus.
- Checked that `GO:0031912` carried no OLS synonyms, so no exact or related
  synonym was silently dropped from the YAML.
- Verified `NCBITaxon:5878` and `NCBITaxon:5911` labels through OLS before
  reviewing the Ciliophora and Tetrahymena rows.

## Findings

### 1. Generic food was modeled as a `CHEMICAL` graph node

- Issue: #1839
- Status: fixed on PR #1838
- Location: `causal_graphs#oral_apparatus_food_channeling`

The first graph represented a generic `food` node with `node_type: CHEMICAL`.
`GO:0031912` supports the statement that the oral apparatus collects food and
channels it to the cytostome, but it does not identify those particles as a
molecular chemical entity. Issue #1839 tracked the defect. The follow-up fix
removed the `food` node and its `oral_apparatus -> food` edge, retained the
GO-backed structural `oral_apparatus -> cytostome` edge, regenerated the
rendered oral-apparatus page, updated README graph-edge counts, and added
`history/records/oral_apparatus/2026-09-30T201418Z-codex-848c9e.yaml` linked
to PR #1838 and issue #1839.

No additional defects were found.
