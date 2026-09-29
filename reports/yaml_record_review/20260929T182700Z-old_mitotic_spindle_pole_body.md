# Adversarial YAML review: old mitotic spindle pole body

- PR: https://github.com/CultureBotAI/CellStructureMech/pull/1792
- Commit reviewed: `10269ce0`
- Record: `data/structures/cytoskeleton/old_mitotic_spindle_pole_body.yaml`
- History: `history/records/old_mitotic_spindle_pole_body/2026-09-29T181148Z-codex-331120.yaml`
- Review timestamp: `2026-09-29T18:27:00Z`

## Verdict

No concrete defects found.

## Checks

- Confirmed `GO:0071957` is current, unrestricted, and in the cellular-component
  aspect.
- Confirmed `GO:0071957` has label `old mitotic spindle pole body`, exact
  synonym `old SPB`, definition provenance `PMID:15132994`, an
  `only_in_taxon` constraint to `NCBITaxon:4751` Fungi, and `GO:0044732`
  `mitotic spindle pole body` as a current ancestor.
- Confirmed `parent_structures: [GO:0044732]` follows the GO hierarchy and
  keeps this age/asymmetry term narrower than the broader mitotic SPB.
- Confirmed `GO:0071958` is cited only as the new-mitotic-SPB sibling, not as
  an asserted parent or part.
- Confirmed the pre-existing `old SPB` and `new SPB` mentions are generic
  duplication placeholders on broad budding-yeast SPB records or boundary notes
  on the GO:0071958 sibling; they are not exact duplicates of GO:0071957.
- Confirmed the taxonomic row is limited to directly evidenced
  `NCBITaxon:4896` rather than broadening GO's fungal taxon constraint into an
  unsupported clade-level literature assertion.
- Confirmed no SIN/NIMA signaling proteins were added as components from a
  negative localization claim; the unresolved exact groundings and exclusions
  are preserved as a `CURATION_TODO`.
- Confirmed the generated page renders the synonym, taxon row, canonical
  example, discussions, and record-level evidence.
- Confirmed local validation passed:
  - focused LinkML validation
  - focused strict validation
  - focused history validation
  - full strict validation
  - full history validation
  - snippet verification
  - TraitMech link check
  - CURIE liveness check
  - id/label correspondence check
  - `just qc`
  - `git diff --check`

## Issues

No GitHub issues were filed because this review found no actionable defects.
