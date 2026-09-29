# YAML Record Review: inner plaque of spindle pole body

- PR: #1773
- Branch: `add-inner-plaque-of-spindle-pole-body`
- Head: `d12868a7cd6847324ebe7386a9c30e796cd66c6d`
- Identifier: `GO:0005822`
- Record: `data/structures/cytoskeleton/inner_plaque_of_spindle_pole_body.yaml`
- Review timestamp: 2026-09-29T08:29:28Z

## Scope

Reviewed the new GO-backed inner-plaque record, its repository history entry,
and regenerated pages/embedding artifacts for boundary, grounding, evidence,
and generated-file drift defects.

## Checks Passed

- `GO:0005822` was verified in QuickGO as a non-obsolete, unrestricted cellular
  component labelled `inner plaque of spindle pole body`.
- QuickGO reported the definition used in the record and the fungal
  `only_in_taxon` constraint for `GO:0005822`.
- The candidate duplicate search used `rg --no-ignore --hidden` and found no
  existing exact `GO:0005822`, inner plaque, half-bridge, or mitotic child
  plaque record.
- `part_of: GO:0005816` is the correct mereological relation from the inner
  plaque to the whole spindle pole body.
- The `nuclear_microtubule` causal node is correctly grounded to the canonical
  `GO:0005880` / `nuclear microtubule` label.
- The inner/central/outer plaque boundary discussion cites the sibling GO terms
  it relies on: `GO:0005823` and `GO:0005824`.
- The scaffold and expansion curation events are present and `llm_assisted`.
- Local focused validation, generated-drift checks, full strict validation,
  full history validation, snippet verification, TraitMech link checking,
  CURIE liveness, id/label correspondence, and `just qc` passed before PR
  creation.

## Findings

No concrete findings.
