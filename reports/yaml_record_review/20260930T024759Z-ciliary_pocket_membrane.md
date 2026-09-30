# Adversarial review: ciliary pocket membrane

- PR: #1805
- Branch: `add-ciliary-pocket-membrane`
- Record: `data/structures/membrane_organelle/ciliary_pocket_membrane.yaml`
- History: `history/records/ciliary_pocket_membrane/2026-09-30T022510Z-codex-69f5ef.yaml`
- Review time: 2026-09-30T02:47:59Z

## Scope

Reviewed the new `GO:0020018` ciliary pocket membrane record, its append-only
history record, and the generated embedding, page, and README artifacts in the
PR diff.

The candidate duplicate search was run with ignored and hidden files included.
It searched `GO:0020018`, `ciliary pocket membrane`,
`cilial pocket membrane`, `cilium pocket membrane`, and
`flagellar pocket membrane`. The only hits were the existing component inside
the parent flagellar-pocket record, generated pages for that component, and
GO/CURIE cache entries; no top-level `identifier: GO:0020018` existed.

## Findings

No concrete defects found.

## Checks

- `GO:0020018` resolves as `ciliary pocket membrane` in
  `reports/curie_check.tsv`.
- `GO:0060170`, `GO:0020016`, and `GO:1990900` resolve as `ciliary membrane`,
  `ciliary pocket`, and `ciliary pocket collar`.
- `NCBITaxon:5691` resolves as `Trypanosoma brucei`.
- `DOI:10.1038/nrmicro2221`, `DOI:10.1073/pnas.0909289106`,
  `DOI:10.1242/jcs.045740`, and `DOI:10.1016/j.pt.2020.11.005` resolve in
  the current CURIE report.
- The record keeps the membrane lipid bilayer as a `REVIEWED_LABEL_ONLY`
  aggregate and carries an open `CURATION_TODO` instead of guessing exact ChEBI
  lipids or membrane-protein family accessions.
- The boundary discussion distinguishes `GO:0020018` from the complete
  ciliary/flagellar pocket and from the cytoskeletal ciliary pocket collar.
- Focused LinkML, focused strict validation, focused history validation, full
  strict validation, full history validation, snippet verification, TraitMech
  link checking, CURIE liveness, id/label correspondence, generated artifact
  checks, `just qc`, and `git diff --check` all passed locally before the PR was
  opened.
