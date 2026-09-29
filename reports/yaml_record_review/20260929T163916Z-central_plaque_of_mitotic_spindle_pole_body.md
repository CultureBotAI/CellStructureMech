# YAML Record Review: central plaque of mitotic spindle pole body

PR: #1789
Issue: #1790
Record: `data/structures/cytoskeleton/central_plaque_of_mitotic_spindle_pole_body.yaml`
Identifier: `GO:0061493`
Review timestamp: `2026-09-29T16:39:16Z`

## Scope

Reviewed the opened PR diff for the new GO-backed mitotic spindle-pole-body
central plaque record, its append-only history entry, regenerated corpus
documentation, text embedding JSON, and static page artifacts.

## Duplicate and Boundary Checks

- Before creating the record, checked the `GO:0061493` identifier, the exact
  `central plaque of mitotic spindle pole body` label, the
  `central_plaque_of_mitotic_spindle_pole_body` slug, and `mitotic central
  plaque` with hidden/ignored-inclusive `rg --no-ignore --hidden`.
- Checked for an existing central-plaque mitotic SPB file under
  `data/structures` with `find`, which is independent of `.gitignore`.
- Compared the new record against:
  - `GO:0005823` `central plaque of spindle pole body`
  - `GO:0061497` `inner plaque of mitotic spindle pole body`
  - `GO:0061499` `outer plaque of mitotic spindle pole body`
  - `GO:0044732` `mitotic spindle pole body`

The exact GO:0061493 identifier and label are unused locally, but GO:0061493's
current definition text describes the inner plaque rather than the central
plaque. The record correctly uses literature as the local definition source and
captures the GO wording mismatch in a resolved discussion.

## Findings

### 1. Boundary discussion omits mitotic inner/outer plaque sibling evidence

Issue: #1790

The record says the GO:0061493 definition currently describes the inner plaque,
but it cites only GO:0061493, the general central-plaque term, the mitotic SPB
term, and SPB literature in the boundary discussion. To make the corrected
boundary locally auditable, the record should cite the exact mitotic sibling
terms `GO:0061497` and `GO:0061499`, mirroring the already-reviewed general
central-plaque record's explicit sibling evidence.

## Local Gates Reviewed

- `linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/cytoskeleton/central_plaque_of_mitotic_spindle_pole_body.yaml`
- `just validate-strict data/structures/cytoskeleton/central_plaque_of_mitotic_spindle_pole_body.yaml`
- `just validate-history history/records/central_plaque_of_mitotic_spindle_pole_body`
- `just text-embeddings-refresh`
- `just text-map-check`
- `just render`
- `just docs-stats`
- `just render-check`
- `just docs-check`
- `just validate-strict`
- `just validate-history`
- `uv run python scripts/fetch_snippets.py --verify --check`
- `just check-trait-links --check`
- `just check-curies-strict`
- `just validate-products`
- `just qc`
- `git diff --check`
