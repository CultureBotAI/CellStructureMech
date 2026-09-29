# YAML record review: cytoplasmic_microtubule

- PR: https://github.com/CultureBotAI/CellStructureMech/pull/1783
- Record: `data/structures/cytoskeleton/cytoplasmic_microtubule.yaml`
- Identifier: `GO:0005881`
- Label: `cytoplasmic microtubule`
- Review timestamp: `2026-09-29T13:19:18Z`
- Reviewer: `codex`

## Findings

No concrete defects found.

## Adversarial checks

- Rechecked identity and duplicate risk with a hidden/ignored-inclusive search for
  `GO:0005881`, `cytoplasmic microtubule`, `non-spindle-associated astral microtubule`,
  and `DOI:10.1146/annurev.cellbio.20.022003.114106` across `data/structures`,
  `history`, and `reports`. Existing hits are the new record, prior SPB and
  axonemal references to the same GO term, and prior review/history provenance;
  no pre-existing exact structure record was present.
- Checked the candidate boundary against `microtubule`, `axonemal microtubule`,
  `spindle microtubule`, and `outer plaque of spindle pole body`. The new record
  uses the exact GO cellular-component identifier for the cytoplasmic subtype,
  keeps `GO:0005874` as its broader microtubule parent, keeps `GO:0005879`
  axonemal microtubules as descendants, and uses `GO:0005824` only as an
  adjacent budding-yeast organizer in a nonmechanistic graph.
- Checked evidence shape. Non-GO Saccharomyces scope and the outer-plaque
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
- `uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/cytoskeleton/cytoplasmic_microtubule.yaml`
- `just validate-strict data/structures/cytoskeleton/cytoplasmic_microtubule.yaml`
- `just validate-history history/records/cytoplasmic_microtubule`
- `just validate-strict`
- `just validate-history`
- `uv run python scripts/fetch_snippets.py --verify --check`
- `just check-trait-links --check`
- `just check-curies-strict`
- `just validate-products`
- `just qc`
- `git diff --check`
