# YAML Record Review: central plaque of spindle pole body

- PR: #1770
- Branch: `add-central-plaque-of-spindle-pole-body`
- Head: `8d7f94588ed6235cd80d5b6796fc2c90a90efb28`
- Identifier: `GO:0005823`
- Record: `data/structures/cytoskeleton/central_plaque_of_spindle_pole_body.yaml`
- Review timestamp: 2026-09-29T07:51:19Z

## Scope

Reviewed the new GO-backed central-plaque record, its repository history entry,
and regenerated pages/embedding artifacts for boundary, grounding, evidence,
and generated-file drift defects.

## Checks Passed

- `GO:0005823` was verified in QuickGO as a non-obsolete, unrestricted cellular
  component labelled `central plaque of spindle pole body`.
- QuickGO reported the definition used in the record and the fungal
  `only_in_taxon` constraint for `GO:0005823`.
- The candidate duplicate search used `rg --no-ignore --hidden` and found no
  existing exact `GO:0005823`, central plaque, inner plaque, or half-bridge
  record.
- `part_of: GO:0005816` is the correct mereological relation from the central
  plaque to the whole spindle pole body.
- The `nuclear_envelope` causal node is correctly grounded to the canonical
  `GO:0005635` / `nuclear envelope` label.
- The scaffold and expansion curation events are present and `llm_assisted`.
- Local focused validation, generated-drift checks, full strict validation,
  full history validation, snippet verification, TraitMech link checking,
  CURIE liveness, id/label correspondence, and `just qc` passed before PR
  creation.

## Findings

### 1. Boundary discussion cites only the central plaque while asserting inner/outer plaque distinctions

- Location: `data/structures/cytoskeleton/central_plaque_of_spindle_pole_body.yaml:96`
- Severity: medium
- Concrete issue: `central_plaque_boundary` says the adjacent inner and outer
  plaques are separately named SPB laminates with different topology, but the
  discussion evidence lists only `GO:0005823`, which establishes the central
  plaque itself. The claim depends on the sibling GO terms for the inner and
  outer plaques: `GO:0005822` and `GO:0005824`.
- Required fix: add `GO:0005822` and `GO:0005824` as record-level evidence and
  cite them from the resolved boundary discussion, or narrow the discussion so
  it no longer asserts sibling plaque topology.

### 2. The component TODO leaks half-bridge scope into the central-plaque record

- Location: `data/structures/cytoskeleton/central_plaque_of_spindle_pole_body.yaml:115`
- Severity: medium
- Concrete issue: `resolve_central_plaque_components` is attached to the
  central-plaque record, but its rationale asks future curation to resolve
  groundings for "plaque and bridge proteins." The half-bridge is a separately
  named SPB substructure (`GO:0005825`) adjacent to the plaques, so this TODO
  blurs the component boundary the record is trying to establish.
- Required fix: narrow the TODO to central-plaque or SPB-core constituents and
  leave half-bridge proteins to a future half-bridge record/review.
