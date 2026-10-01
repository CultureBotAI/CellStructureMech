# FMN reductase complex record review

- PR: #1887
- Branch: `add-fmn-reductase-complex`
- Commit reviewed: `432679f75c956051ca4911725bbe523403d76a76`
- Record: `data/structures/other/fmn_reductase_complex.yaml`
- Identifier: `GO:1990202`
- Label: `FMN reductase complex`

## Scope

Adversarial review of the new `FMN reductase complex` CellStructureMech
record, its append-only history entry, and the regenerated README, embedding,
and static-page artifacts.

## Checks

- Re-ran an ignored/hidden-inclusive identity search across `data`, `history`,
  `reports`, and `pages` for `GO:1990202`, the exact `FMN reductase complex`
  label, the `SsuE complex` narrow synonym, and the FMN/flavin oxidoreductase
  synonym strings. Matches were limited to this new record, its generated
  artifacts, and the PR-local history entry; the prior `SsuD-SsuE complex`
  appeared only as an embedding neighbor.
- Re-ran an ignored/hidden-inclusive provenance search across `data/structures`
  for `PMID:10480865`, `DOI:10.1074/jbc.274.38.26639`,
  `UniProtKB:P80644`, and `InterPro:IPR020048`. The existing
  `SsuD-SsuE complex` shares those identifiers for its SsuE constituent, but
  its `GO:1990200` cellular component denotes a heteromeric SsuD/SsuE
  interaction complex rather than the SsuE homodimer named by `GO:1990202`.
- Checked the exact GO cellular-component identifier, the `GO:1990204`
  oxidoreductase-complex parent, and the `GO:0052873` molecular function for
  semantic fit against the curated record fields.
- Checked that the single protein component uses the exact reviewed
  `InterPro:IPR020048` SsuE family grounding and a reviewed E. coli K-12
  `UniProtKB:P80644` example rather than a broad flavoprotein or
  NAD(P)H-oxidoreductase family.
- Checked that the record asserts only an E. coli canonical example and the
  SsuE dimer subunit count stated by `GO:1990202`; no unsupported broad
  taxonomic-distribution row was added.
- Rebuilt and checked the embedding map, rendered pages, README corpus stats,
  strict record validation, full history validation, trait links, CURIE
  liveness, identifier/label correspondence, snippet verification, full QC,
  and `git diff --check`.
- Reviewed the PR file list and confirmed the diff contains one new semantic
  YAML record, one append-only history record, one generated HTML page, and
  generated README/index/embedding updates.

## Findings

No concrete defects found. No GitHub review issues were filed.
