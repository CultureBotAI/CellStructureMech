# YAML Record Review: starch utilization system complex

- Record: `data/structures/other/starch_utilization_system_complex.yaml`
- PR: #1875
- Reviewed at: `2026-10-01T15:34:37Z`
- Outcome: 1 defect found, filed as #1876, and fixed before merge.

## Findings

### #1876 - SusE and SusF essentiality overstated assembly evidence

- Status: fixed in `0937b79b`
- Affected rows:
  - `components#suse_starch_binding_lipoprotein`
  - `components#susf_starch_binding_lipoprotein`
- Problem: the initial record set both components to `essentiality: DISPENSABLE`.
  The cited Sus literature supports SusE as an accessory starch-binding factor and
  SusF as a surface-exposed lipoprotein associated with bound starch, but it does
  not directly show that the starch utilization system complex assembles without
  either component. In CellStructureMech, `essentiality` is about whether the
  structure forms, not whether starch utilization or growth persists.
- Fix: changed both `essentiality` values to `UNKNOWN`, appended an
  `ADDRESS_REVIEW` curation event, rerendered the generated page, and added a
  second repository history entry linked to PR #1875 and issue #1876.

## Verification After Fix

- `uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/starch_utilization_system_complex.yaml`
- `uv run python scripts/validate_strict.py --quiet data/structures/other/starch_utilization_system_complex.yaml`
- `uv run python scripts/validate_history.py history/records/starch_utilization_system_complex/2026-10-01T152437Z-codex-854389.yaml`
- `uv run python scripts/validate_history.py`
- `uv run python scripts/build_text_embedding_map.py --check`
- `uv run python scripts/render_pages.py --check`
- `uv run python scripts/check_docs.py --check`
- `uv run python scripts/run_qc.py`
- `git diff --check`
