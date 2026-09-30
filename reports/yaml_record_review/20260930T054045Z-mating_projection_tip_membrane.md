# YAML Record Review: mating projection tip membrane

- PR: #1809
- Branch: `add-mating-projection-tip-membrane`
- Initial head: `ac6fe3a6b8fd042c6d05263eddf4f9ae55c04f31`
- Record: `data/structures/appendage/mating_projection_tip_membrane.yaml`
- History:
  - `history/records/mating_projection_tip_membrane/2026-09-30T050624Z-codex-3b6357.yaml`
  - `history/records/mating_projection_tip_membrane/2026-09-30T052738Z-codex-4dc264.yaml`

## Scope Reviewed

- Re-ran a hidden/ignored-inclusive duplicate search for `GO:0070867`, `mating projection tip membrane`, and `mating projection membrane` under `data/structures`.
- Compared the new membrane-domain topology against the existing mating projection and mating projection tip records.
- Checked that the curated lipid-bilayer component stayed `REVIEWED_LABEL_ONLY` instead of inventing a ChEBI, InterPro, Pfam, NCBIfam, UniProtKB, or Complex Portal grounding.
- Checked that the open `CURATION_TODO` attaches to the reviewed-label-only lipid component.
- Checked that the first PR commit included generated embedding JSON, README statistics, pages, and the dedicated rendered structure page.

## Findings

### #1810: Function row repeated the record identity

The initial `functions` row was labeled `mating projection tip membrane domain`, which restated the membrane record's identity instead of naming a functional role.

Resolution: rewrote the function row as `mating_projection_tip_polarized_growth` / `mating-projection tip polarized growth`, appended an `ADDRESSED_REVIEW` event to the record YAML, and added a second repository-level history record linked to PR #1809 and issue #1810.

## Validation Reviewed

- `uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/appendage/mating_projection_tip_membrane.yaml`
- `uv run python scripts/validate_strict.py --quiet data/structures/appendage/mating_projection_tip_membrane.yaml`
- `uv run python scripts/validate_history.py history/records/mating_projection_tip_membrane`
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
- Post-fix focused strict validation, focused history validation, generated-artifact checks, full strict/history validation, `git diff --check`, and `just qc`
