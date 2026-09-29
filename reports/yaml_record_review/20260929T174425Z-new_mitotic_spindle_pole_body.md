# Adversarial YAML review: new mitotic spindle pole body

- PR: https://github.com/CultureBotAI/CellStructureMech/pull/1791
- Commit reviewed: `0a58cea2`
- Record: `data/structures/cytoskeleton/new_mitotic_spindle_pole_body.yaml`
- History: `history/records/new_mitotic_spindle_pole_body/2026-09-29T172834Z-codex-27006c.yaml`
- Review timestamp: `2026-09-29T17:44:25Z`

## Verdict

No concrete defects found.

## Checks

- Confirmed `GO:0071958` is current, unrestricted, and in the cellular-component
  aspect.
- Confirmed `GO:0071958` has label `new mitotic spindle pole body`, exact
  synonym `new SPB`, definition provenance `PMID:15132994`, an
  `only_in_taxon` constraint to `NCBITaxon:4751` Fungi, and `GO:0044732`
  `mitotic spindle pole body` as a current ancestor.
- Confirmed `parent_structures: [GO:0044732]` is narrower than the existing
  `GO:0005816` general spindle-pole-body record and matches the GO hierarchy.
- Confirmed the `GO:0071957` old-mitotic-SPB sibling is cited only as boundary
  context, not as an asserted parent or local component.
- Confirmed the only pre-existing `new SPB` / `old SPB` mentions are the generic
  duplication placeholders on broad budding-yeast SPB records; they are not
  exact duplicates of the fission-yeast GO:0071958 age/asymmetry term.
- Confirmed the fission-yeast taxon row is species-scoped to
  `NCBITaxon:4896` and does not overstate GO's fungal taxon constraint as a
  literature-backed broad distribution assertion.
- Confirmed transient SIN/NIMA signaling proteins are left out of
  `components`, with a `CURATION_TODO` for exact source-neutral grounding work
  instead of guessed InterPro, Pfam, NCBIfam, UniProtKB, or Complex Portal IDs.
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
