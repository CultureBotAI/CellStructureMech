# Prospore septin filament array YAML record review

PR: #1831
Record: `data/structures/cytoskeleton/prospore_septin_filament_array.yaml`
Review timestamp: 2026-09-30T15:48:55Z

## Scope

- Rechecked that `GO:0032165` is not already used as a top-level structure
  record, including hidden and ignored paths.
- Rechecked the OLS label and definition for `GO:0032165`.
- Rechecked the OLS graph for the direct `GO:0032160` septin-filament-array
  parent and the absence of a direct `part_of` edge.
- Compared the new record against the generic `GO:0032160` septin filament
  array, the `GO:0032166` chlamydospore septin filament array sibling, and the
  `GO:0032169` prospore septin ring.
- Inspected the rendered
  `pages/structures/cytoskeleton/prospore_septin_filament_array.html` artifact
  to verify the component, topology graph, evidence list, discussions, and
  curation history render as expected.

## Findings

No concrete defects found.

## Residual risk

- The record deliberately uses `grounding_status: REVIEWED_LABEL_ONLY` for the
  grouped septin-protein constituent rather than guessing an InterPro, Pfam, or
  NCBIfam accession for all prospore-array-forming septins.
- The record stays GO-backed and does not add species-level distribution rows or
  canonical examples because no primary source was opened for those narrower
  claims in this PR.

## Validation reviewed

- `uv run --extra embeddings python scripts/build_text_embedding_map.py --check`
- `uv run python scripts/render_pages.py --check`
- `uv run python scripts/check_docs.py --check`
- `uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/cytoskeleton/prospore_septin_filament_array.yaml`
- `uv run python scripts/validate_strict.py --quiet data/structures/cytoskeleton/prospore_septin_filament_array.yaml`
- `uv run python scripts/validate_history.py history/records/prospore_septin_filament_array`
- `uv run python scripts/validate_strict.py --quiet`
- `uv run python scripts/validate_history.py`
- `uv run python scripts/fetch_snippets.py --verify --check`
- `uv run python scripts/check_trait_links.py --check`
- `uv run python scripts/check_curies.py --check --report reports/curie_check.tsv`
- `uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `git diff --check`
- `just qc`
