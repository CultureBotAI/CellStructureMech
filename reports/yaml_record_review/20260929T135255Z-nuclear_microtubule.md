# YAML record review: nuclear_microtubule

- PR: https://github.com/CultureBotAI/CellStructureMech/pull/1784
- Record: `data/structures/cytoskeleton/nuclear_microtubule.yaml`
- Identifier: `GO:0005880`
- Label: `nuclear microtubule`
- Review timestamp: `2026-09-29T13:52:55Z`
- Reviewer: `codex`

## Findings

No concrete defects found.

## Adversarial checks

- Rechecked identity and duplicate risk with a hidden/ignored-inclusive search for
  `GO:0005880`, `nuclear microtubule`, and `DOI:10.1146/annurev.cellbio.20.022003.114106`
  across `data/structures`, `history`, and `reports`. Existing hits are the new
  record, prior SPB references to the same DOI, the inner-plaque graph node grounded
  to `GO:0005880`, and prior review/history provenance; no pre-existing exact
  structure record was present.
- Checked the GO hierarchy for `GO:0005880`; the term is the exact
  nuclear-microtubule cellular component, has `GO:0005874` microtubule as its
  broader parent, has `GO:0005634` nucleus as a `part_of` target, and lists no
  synonyms that the record omitted.
- Checked the candidate boundary against `nucleus`, `cytoplasmic microtubule`,
  `spindle microtubule`, and `inner plaque of spindle pole body`. The new record
  stays at the GO:0005880 spatial subtype level, distinguishes itself from
  cytoplasmic microtubules and array-specific spindle microtubules, and uses
  `GO:0005822` only as an adjacent budding-yeast organizer in a nonmechanistic
  graph.
- Checked evidence shape. Non-GO Saccharomyces scope and the inner-plaque
  organization edge cite `DOI:10.1146/annurev.cellbio.20.022003.114106`; GO
  structural relationships cite GO cellular-component terms; no unverifiable
  snippet text was introduced.
- Checked generated artifacts. The rendered structure page, browse index,
  cytoskeleton category, grounded index, JSON search index, README counts, and
  semantic text-map artifacts were regenerated from the YAML and passed drift
  checks.

## Validation

- `just text-embeddings-refresh`
- `just text-map-check`
- `just render`
- `just docs-stats`
- `just render-check`
- `just docs-check`
- `uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/cytoskeleton/nuclear_microtubule.yaml`
- `just validate-strict data/structures/cytoskeleton/nuclear_microtubule.yaml`
- `just validate-history history/records/nuclear_microtubule`
- `just validate-strict`
- `just validate-history`
- `uv run python scripts/fetch_snippets.py --verify --check`
- `just check-trait-links --check`
- `just check-curies-strict`
- `just validate-products`
- `just qc`
- `git diff --check`
