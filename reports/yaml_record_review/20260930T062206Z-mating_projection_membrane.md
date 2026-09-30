# YAML Record Review: mating projection membrane

- PR: #1811
- Branch: `add-mating-projection-membrane`
- Head: `749026dc408ca4a8b22e844d5e1439778545b370`
- Record: `data/structures/appendage/mating_projection_membrane.yaml`
- History: `history/records/mating_projection_membrane/2026-09-30T055734Z-codex-00e17f.yaml`

## Scope Reviewed

- Re-ran a hidden/ignored-inclusive duplicate search for `GO:0070250` and `mating projection membrane` under `data/structures`.
- Compared the new projection-membrane topology against the existing mating projection and mating projection tip membrane records.
- Checked that `GO:0070250` is curated as the broader projection membrane and `GO:0070867` remains the narrower tip membrane subdomain.
- Checked that the curated lipid-bilayer component stayed `REVIEWED_LABEL_ONLY` instead of inventing a ChEBI, InterPro, Pfam, NCBIfam, UniProtKB, or Complex Portal grounding.
- Checked that the open `CURATION_TODO` attaches to the reviewed-label-only lipid component.
- Confirmed generated embedding JSON, README statistics, pages, and the dedicated rendered structure page were included in the initial commit.

## Findings

No concrete defects found.

## Validation Reviewed

- `uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/appendage/mating_projection_membrane.yaml`
- `uv run python scripts/validate_strict.py --quiet data/structures/appendage/mating_projection_membrane.yaml`
- `uv run python scripts/validate_history.py history/records/mating_projection_membrane`
- `uv run --extra embeddings python scripts/build_text_embedding_map.py --check`
- `uv run python scripts/render_pages.py --check`
- `uv run python scripts/check_docs.py --check`
- `uv run python scripts/validate_strict.py --quiet`
- `uv run python scripts/validate_history.py`
- `uv run python scripts/fetch_snippets.py --verify --check`
- `uv run python scripts/check_trait_links.py --check`
- `uv run python scripts/check_curies.py --check --report reports/curie_check.tsv`
- `uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `git diff --check`
- `just qc`
