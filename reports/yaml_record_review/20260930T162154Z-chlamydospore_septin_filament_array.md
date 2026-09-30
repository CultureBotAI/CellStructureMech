# Chlamydospore septin filament array YAML record review

PR: #1832
Record: `data/structures/cytoskeleton/chlamydospore_septin_filament_array.yaml`
Review timestamp: 2026-09-30T16:21:54Z

## Scope

- Rechecked that `GO:0032166` is not already used as a top-level structure
  record, including hidden and ignored paths.
- Rechecked the OLS label and definition for `GO:0032166`.
- Rechecked the OLS graph for the direct `GO:0032160` septin-filament-array
  parent, its `BFO:0000050` edge to the `CL:0000726` chlamydospore cell type,
  and its fungal `in_taxon` constraint.
- Compared the new record against the generic `GO:0032160` septin filament
  array, the newly curated `GO:0032165` prospore septin filament array sibling,
  and the broader septin ring, collar, and cap records.
- Inspected the rendered
  `pages/structures/cytoskeleton/chlamydospore_septin_filament_array.html`
  artifact to verify the component, topology graph, evidence list, discussions,
  and curation history render as expected.

## Findings

No concrete defects found.

## Residual risk

- The record deliberately uses `grounding_status: REVIEWED_LABEL_ONLY` for the
  grouped septin-protein constituent rather than guessing an InterPro, Pfam, or
  NCBIfam accession for all chlamydospore-array-forming septins.
- The OLS graph reports `GO:0032166` as part of `CL:0000726` chlamydospore, but
  the record does not add that cell-type term to `part_of` because
  CellStructureMech uses structural or GO cellular-component targets there.
- The record stays GO-backed and does not add species-level distribution rows or
  canonical examples because no primary source was opened for those narrower
  claims in this PR.

## Validation reviewed

- `uv run --extra embeddings python scripts/build_text_embedding_map.py --check`
- `uv run python scripts/render_pages.py --check`
- `uv run python scripts/check_docs.py --check`
- `uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/cytoskeleton/chlamydospore_septin_filament_array.yaml`
- `uv run python scripts/validate_strict.py --quiet data/structures/cytoskeleton/chlamydospore_septin_filament_array.yaml`
- `uv run python scripts/validate_history.py history/records/chlamydospore_septin_filament_array`
- `uv run python scripts/validate_strict.py --quiet`
- `uv run python scripts/validate_history.py`
- `uv run python scripts/fetch_snippets.py --verify --check`
- `uv run python scripts/check_trait_links.py --check`
- `uv run python scripts/check_curies.py --check --report reports/curie_check.tsv`
- `uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `git diff --check`
- `just qc`
