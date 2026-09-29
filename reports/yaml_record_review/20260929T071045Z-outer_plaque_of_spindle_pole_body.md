# YAML Record Review: outer plaque of spindle pole body

- PR: #1768
- Record: `data/structures/cytoskeleton/outer_plaque_of_spindle_pole_body.yaml`
- Identifier: `GO:0005824`
- Review timestamp: `2026-09-29T07:10:45Z`

## Findings

### 1. Ground the cytoplasmic-microtubule graph node

- Severity: medium
- Location: `data/structures/cytoskeleton/outer_plaque_of_spindle_pole_body.yaml`
- Anchor: `causal_graphs#outer_plaque_topology`

The topology graph introduces an ungrounded `cytoplasmic_microtubules` structure
node with the plural label `cytoplasmic microtubules`. QuickGO has an exact,
current cellular-component term for that structure, `GO:0005881 cytoplasmic
microtubule`; the same CURIE is already locally resolved and used as the
cytoplasmic-microtubule parent of `data/structures/cytoskeleton/axonemal_microtubule.yaml`.

Leaving the node ungrounded weakens the graph and hides the label mismatch from
the id-to-label correspondence gate. Add `grounding: GO:0005881`, use GO's
canonical singular label `cytoplasmic microtubule`, and cite `GO:0005881` in the
record evidence.

## Non-Findings

- `GO:0005824` was verified in QuickGO as a non-obsolete, unrestricted cellular
  component whose ancestor payload includes `GO:0005816` spindle pole body.
- `part_of: GO:0005816` is the correct mereological relation for the plaque to
  the whole spindle pole body.
- The duplicate search included hidden and ignored files via
  `rg --no-ignore --hidden` and found no existing exact `GO:0005824` record.
