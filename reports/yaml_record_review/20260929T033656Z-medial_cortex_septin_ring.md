# YAML Record Review: medial_cortex_septin_ring

- PR: #1758
- Issue: #1759
- Record: `data/structures/cytoskeleton/medial_cortex_septin_ring.yaml`
- Reviewed at: 2026-09-29T03:36:56Z
- Result: changes requested

## Scope

Adversarial review of the new `GO:0036391` medial cortex septin ring record, its
append-only history entry, and regenerated CellStructureMech pages, docs, and
embedding artifacts in PR #1758.

The review compared the new record with existing localized septin-ring subtype
records, including bud-neck, split bud-neck, prospore, hyphal, germ-tube,
pseudohyphal, and mating-projection septin rings.

## Findings

### #1759: Boundary discussion omits the mating projection septin ring

Severity: medium

The new `medial_cortex_septin_ring_boundary` discussion separates `GO:0036391`
from bud-neck, bud-neck split-ring, prospore, hyphal, germ-tube, and
pseudohyphal septin-ring states, but it does not explicitly separate the medial
cortex ring from the already curated `GO:0032175` mating projection septin
ring.

The boundary discussion claims to keep the medial cortex septin ring distinct
from other localized septin-ring states, so it should name the shmoo-neck
mating-projection septin ring alongside the other localized GO siblings.

## Non-Findings

- The PR file list on GitHub matched the expected 14-file local change set.
- `GO:0036391` is an exact cellular-component identifier for the new record.
- The topology graph is `NONMECHANISTIC` and only records GO-backed composition
  and medial-cortex localization.
- The reviewed-label-only `septin_proteins` component has an open TODO for exact
  source-neutral septin and septin-associated-protein boundaries, avoiding
  unsupported Pfam, InterPro, NCBIfam, or associated-protein groundings.
