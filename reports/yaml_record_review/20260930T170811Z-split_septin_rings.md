# Adversarial review: split septin rings

## Scope

- PR: #1833
- Record: `data/structures/cytoskeleton/split_septin_rings.yaml`
- History: `history/records/split_septin_rings/2026-09-30T163754Z-codex-8f2667.yaml`

## Checks

- Re-read the GO:0032176 YAML and compared it to `GO:0032177` cellular bud neck split septin rings.
- Confirmed the PR file list contains only the new record, one history entry, one generated structure page, and regenerated README/site/embedding artifacts.
- Re-ran a hidden/ignored-inclusive search for `GO:0032176`, `GO_0032176`, `split septin rings`, and `split_septin_rings` across `data/structures`, `history`, `pages`, `reports`, and `README.md`.
- Checked the generic GO:0032176 boundary against the narrower bud-neck GO:0032177 record so the new record does not inherit bud-neck-specific localization, parthood, or taxon claims.
- Checked that the cytokinetic function preserves GO's "thought to" uncertainty rather than asserting an experimentally resolved trapping mechanism.
- Checked that no species-specific canonical examples or exact InterPro, Pfam, NCBIfam, or UniProt component groundings were guessed from the GO label or definition.
- Re-ran `just qc`; it passed on 738 structure records.

## Findings

| Severity | Finding | File |
| --- | --- | --- |
| Minor | The `cell_division_site` topology node has the exact label of `GO:0032153` but is left ungrounded. `GO:0032153` is already used as the exact grounding for the same cell-division-site location in the cleavage-apparatus septin-structure topology graph, so leaving this node label-only drops a resolvable source CURIE from an otherwise GO-backed split-ring topology. | `data/structures/cytoskeleton/split_septin_rings.yaml` |

## Non-findings

- `GO:0032177` remains the bud-neck-localized child; `GO:0032176` is curated as the generic split-ring pair.
- The top-level `part_of` relation stops at `GO:0005856` cytoskeleton and does not overstate a direct GO parthood to the bud neck.
- The function text says the double-ring structure is "thought to" trap cytokinesis, membrane, or cell-wall proteins, preserving the GO definition's uncertainty.
- The composite `septin ring or collar` graph node is intentionally ungrounded because the GO definition allows either precursor structure and there is no single exact source-neutral class for that disjunction.

## Validation

- `uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/cytoskeleton/split_septin_rings.yaml`
- `uv run python scripts/validate_strict.py --quiet data/structures/cytoskeleton/split_septin_rings.yaml`
- `uv run python scripts/validate_history.py history/records/split_septin_rings`
- `uv run python scripts/validate_strict.py --quiet`
- `uv run python scripts/validate_history.py`
- `uv run python scripts/fetch_snippets.py --verify --check`
- `uv run python scripts/check_trait_links.py --check`
- `uv run python scripts/check_curies.py --check --report reports/curie_check.tsv`
- `uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `just qc`
- `git diff --check`
