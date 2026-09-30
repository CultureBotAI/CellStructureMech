# Adversarial review: radial spoke neck

- PR: #1804
- Branch: `add-radial-spoke-neck`
- Record: `data/structures/cytoskeleton/radial_spoke_neck.yaml`
- History: `history/records/radial_spoke_neck/2026-09-30T014627Z-codex-344df8.yaml`
- Review time: 2026-09-30T02:07:21Z

## Scope

Reviewed the new `GO:0120343` radial spoke neck record, its append-only
history record, and the generated embedding, page, and README artifacts in the
PR diff.

The candidate duplicate search was run with ignored and hidden files included.
It found `GO:0120343` and `radial spoke neck` only as a component/reference in
the existing whole radial spoke and as adjacent-boundary context in the radial
spoke head and stalk records; no top-level `identifier: GO:0120343` existed.

## Findings

No concrete defects found.

## Checks

- `GO:0120343` resolves as `radial spoke neck` in `reports/curie_check.tsv`.
- `GO:0032991` resolves as `protein-containing complex`.
- `GO:0001534`, `GO:0001535`, and `GO:0001536` resolve as the complete radial
  spoke and the adjacent head and stalk subcomplexes.
- `NCBITaxon:3055` resolves as `Chlamydomonas reinhardtii`.
- `DOI:10.1242/jcs.245233` and `DOI:10.1126/science.1128618` resolve in the
  current CURIE report.
- The record keeps individual RSP protein families as a
  `REVIEWED_LABEL_ONLY` aggregate and carries an open `CURATION_TODO` instead
  of guessing InterPro, Pfam, NCBIfam, or UniProtKB accessions.
- The neck boundary discussion distinguishes the exact neck subcomplex from
  the whole radial spoke and the adjacent head and stalk subcomplexes.
- Focused LinkML, focused strict validation, focused history validation, full
  strict validation, full history validation, snippet verification, TraitMech
  link checking, CURIE liveness, id/label correspondence, generated artifact
  checks, `just qc`, and `git diff --check` all passed locally before the PR was
  opened.
