# Hyphal septin band YAML record review

PR: #1830
Record: `data/structures/cytoskeleton/hyphal_septin_band.yaml`
Review timestamp: 2026-09-30T15:13:03Z

## Scope

- Rechecked that `GO:0032163` is not already used as a top-level structure
  record, including hidden and ignored paths.
- Rechecked the OLS label and definition for `GO:0032163`.
- Rechecked the OLS graph for the direct `GO:0032158` septin-band parent and
  the absence of direct `part_of` or child edges.
- Compared the new record against the newly merged `GO:0032158` generic septin
  band and the neighboring germ-tube and hyphal septin-ring records.
- Inspected the rendered `pages/structures/cytoskeleton/hyphal_septin_band.html`
  artifact to verify the component, topology graph, evidence list, discussions,
  and curation history render as expected.

## Findings

No concrete defects found.

## Residual risk

- The record deliberately uses `grounding_status: REVIEWED_LABEL_ONLY` for the
  grouped septin-protein constituent rather than guessing an InterPro, Pfam, or
  NCBIfam accession for all hyphal-band-forming septins.
- The record stays GO-backed and does not add species-level distribution rows or
  canonical examples because no primary source was opened for those narrower
  claims in this PR.

## Validation reviewed

- `uv run --extra embeddings python scripts/build_text_embedding_map.py --check`
- `uv run python scripts/render_pages.py --check`
- `uv run python scripts/check_docs.py --check`
- `uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/cytoskeleton/hyphal_septin_band.yaml`
- `uv run python scripts/validate_strict.py --quiet data/structures/cytoskeleton/hyphal_septin_band.yaml`
- `uv run python scripts/validate_history.py history/records/hyphal_septin_band`
- `uv run python scripts/validate_strict.py --quiet`
- `uv run python scripts/validate_history.py`
- `uv run python scripts/fetch_snippets.py --verify --check`
- `uv run python scripts/check_trait_links.py --check`
- `uv run python scripts/check_curies.py --check --report reports/curie_check.tsv`
- `uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `git diff --check`
- `just qc`
