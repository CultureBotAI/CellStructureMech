# YAML Record Review: prospore_septin_ring

- PR: #1756
- Issue: #1757
- Record: `data/structures/cytoskeleton/prospore_septin_ring.yaml`
- Reviewed at: 2026-09-29T02:52:33Z
- Result: changes requested

## Scope

Adversarial review of the new `GO:0032169` prospore septin ring record, its
append-only history entry, and regenerated CellStructureMech pages, docs, and
embedding artifacts in PR #1756.

The review compared the new record with localized fungal septin-ring subtype
records, including `GO:0032172` germ tube septin ring, `GO:0032168` hyphal
septin ring, `GO:0032170` pseudohyphal septin ring, `GO:0032177` cellular bud
neck split septin rings, and `GO:0032175` mating projection septin ring.

## Findings

### #1757: Boundary discussion omits cytokinetic bud-neck split rings

Severity: medium

The new `prospore_septin_ring_boundary` discussion separates `GO:0032169` from
germ-tube, hyphal, and pseudohyphal septin rings, but it does not explicitly
separate the prospore ring from `GO:0032177` cellular bud neck split septin
rings.

That leaves the prospore ring distinct from three localized sibling rings but
not from the already-curated budding-cell cytokinetic split-ring pair formed
from the bud-neck septin collar. The boundary discussion should name
`GO:0032177` so future cytokinesis-site curation does not collapse a single
prospore septin ring with the two-ring bud-neck split state.

## Non-Findings

- The PR file list on GitHub matched the expected 14-file local change set.
- `GO:0032169` is an exact cellular-component identifier for the new record.
- The new record deliberately omits a function because the GO definition only
  supplies composition and localization for the first curation pass.
- The reviewed-label-only `septin_proteins` component has an open TODO for exact
  source-neutral septin and septin-associated-protein boundaries, avoiding
  unsupported Pfam, InterPro, NCBIfam, or associated-protein groundings.
