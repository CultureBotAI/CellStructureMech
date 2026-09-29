# Adversarial review: prospore contractile ring

- PR: #1766
- Branch: `add-prospore-contractile-ring`
- Record: `data/structures/cytoskeleton/prospore_contractile_ring.yaml`
- Candidate: `GO:0032157` prospore contractile ring
- Reviewer: codex
- Timestamp: 2026-09-29T06:34:04Z

## Scope

Reviewed the PR diff for the new GO-grounded `prospore contractile ring` record,
its history record, and rendered output after local validation passed.

Local duplicate checks before the record was added included hidden and ignored
files via `rg --no-ignore --hidden` for `GO:0032157`, `prospore contractile ring`,
and `meiotic contractile ring`; no existing record or generated page used that
exact identifier or label.

## Findings

### 1. `parent_structures` skips the verified meiotic actomyosin-ring parent

- Severity: medium
- File: `data/structures/cytoskeleton/prospore_contractile_ring.yaml`
- Lines: 33-34, 69-73, 135-141

`GO:0032157` was curated as a GO-exact cellular-component record. QuickGO's
ancestor payload for `GO:0032157` includes `GO:0110086` (`meiotic actomyosin
contractile ring`) between the new prospore-localized record and the generic
`GO:0005826` (`actomyosin contractile ring`). The record even cites `GO:0110086`
as the broader meiotic class in evidence, but `parent_structures` points only to
the generic `GO:0005826` and the resolved boundary note says `GO:0005826` was
used as the is-a parent.

That flattens the new record's is-a edge past an already verified GO class. Use
`GO:0110086` as the `parent_structures` target and keep `GO:0005826` only as
ancestor/boundary evidence.

## Checks Reviewed

- `uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/cytoskeleton/prospore_contractile_ring.yaml`
- `uv run python scripts/validate_strict.py --quiet data/structures/cytoskeleton/prospore_contractile_ring.yaml`
- `uv run python scripts/validate_history.py history/records/prospore_contractile_ring/2026-09-29T062145Z-codex-1b6685.yaml`
- `uv run python scripts/validate_strict.py --quiet`
- `uv run python scripts/validate_history.py`
- `uv run python scripts/fetch_snippets.py --verify --check`
- `uv run python scripts/check_trait_links.py --check`
- `uv run python scripts/check_curies.py --check --report reports/curie_check.tsv`
- `uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `just qc`
- `git diff --check`
