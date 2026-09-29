# YAML Record Review: outer plaque of mitotic spindle pole body

PR: #1788
Record: `data/structures/cytoskeleton/outer_plaque_of_mitotic_spindle_pole_body.yaml`
Identifier: `GO:0061499`
Review timestamp: `2026-09-29T16:00:41Z`

## Scope

Reviewed the opened PR diff for the new GO-backed mitotic spindle-pole-body outer
plaque record, its append-only history entry, the regenerated README, text
embedding JSON, and static page artifacts.

## Duplicate and Boundary Checks

- Rechecked the new `GO:0061499` identifier and label against local `data/`,
  `history/`, `pages/`, `reports/`, and `README.md` references with
  hidden/ignored-inclusive `rg --no-ignore --hidden`.
- Rechecked the exact new slug and any pre-existing outer-plaque files under
  `data/structures` with `find`, which is independent of `.gitignore`.
- Compared the new record against:
  - `GO:0005824` `outer plaque of spindle pole body`
  - `cellstructuremech:meiotic_outer_plaque`
  - `GO:0044732` `mitotic spindle pole body`
  - `GO:0005881` `cytoplasmic microtubule`

The new record stays narrower than the general SPB outer plaque, stays distinct
from the sporulation-specific meiotic outer plaque, and uses the existing
mitotic SPB and cytoplasmic microtubule records only for parthood and topology
context.

## Evidence Checks

- `GO:0061499` is used as the exact identifier and definition source for the
  outer plaque of the mitotic spindle pole body.
- `GO:0005824` and `GO:0044732` support the parent and `part_of` assertions.
- `GO:0005881` is only used to ground the cytoplasmic microtubule node that is
  organized by the outer plaque.
- The `Saccharomyces cerevisiae` distribution, canonical example, and
  cytoplasmic microtubule organization function are scoped to the reviewed
  budding-yeast SPB literature rather than generalized across fungi.
- No verbatim snippets were added, so there are no source-quote transcription
  risks in the new YAML.

## Findings

No concrete curation defects found.

## Issues Filed

None.

## Local Gates Reviewed

- `linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/cytoskeleton/outer_plaque_of_mitotic_spindle_pole_body.yaml`
- `just validate-strict data/structures/cytoskeleton/outer_plaque_of_mitotic_spindle_pole_body.yaml`
- `just validate-history history/records/outer_plaque_of_mitotic_spindle_pole_body`
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
