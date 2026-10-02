# Adversarial YAML Record Review: dinoflagellate apex

- PR: https://github.com/CultureBotAI/CellStructureMech/pull/1936
- Record: `data/structures/other/dinoflagellate_apex.yaml`
- Identifier: `GO:0097683`
- Reviewer: `codex`
- Review timestamp: `2026-10-02T19:59:43Z`

## Scope

Reviewed the new `dinoflagellate apex` record added in PR #1936 after the
initial branch push.

## Duplicate And Identity Checks

- Before adding the record, searched hidden and ignored files with
  `rg --no-ignore --hidden` for `dinoflagellate apex`, `GO:0097683`,
  `GO_0097683`, `apex`, `apical pore`, `GO:0097686`, and `GO_0097686` across
  curated records, history, reports, generated pages, docs, curation inputs,
  research, scripts, `.github`, build artifacts, pages, and embeddings.
- The broad search found `GO:0097683` only as adjacent topology evidence in the
  already-merged epicone record, generated pages, the CURIE cache, and earlier
  review reports before the new apex YAML and derived artifacts were created.
- No pre-existing exact `GO:0097683`, top-level dinoflagellate-apex record, or
  `apex` synonym entry existed under `data/structures`; this exact duplicate
  search included hidden and ignored files via `rg --no-ignore --hidden`.

## Authority Checks

- Verified `GO:0097683` through QuickGO as a live cellular-component term named
  `dinoflagellate apex`, with broad synonym `apex`, a definition placing it at
  the anterior-most point of a dinoflagellate epicone, and ancestor coverage
  under `GO:0097613` dinoflagellate epicone and `GO:0110165` cellular
  anatomical structure.
- Verified QuickGO lists `GO:0097686` dinoflagellate apical horn as an `is_a`
  child of `GO:0097683`.
- Verified the adjacent `GO:0097685` dinoflagellate apical groove record is
  still the appropriate evidence for modeling the apical groove as a
  cell-surface furrow found on the dinoflagellate apex.
- Verified all newly referenced GO terms resolve through the repository CURIE
  liveness and id-label correspondence gates.

## Findings

### 1. Apex-epicone edge under-cited the GO:0097613 child assertion

- Issue: https://github.com/CultureBotAI/CellStructureMech/issues/1937
- Severity: medium
- Status: fixed in commit `4a237077`

The initial `dinoflagellate_apex is part of dinoflagellate_epicone` edge cited
only `GO:0097683`, but its evidence note said both that QuickGO lists
`GO:0097613` as an ancestor of `GO:0097683` and that the `GO:0097613` payload
lists `GO:0097683` as a `part_of` child. The second assertion is evidence from
the `GO:0097613` child listing, so a reviewer following only `GO:0097683` would
not see every statement made by the note.

Fix: split the evidence into a `GO:0097683` ancestor note and a direct
`GO:0097613` child-endpoint note for the `part_of` child assertion.

### 2. Apical-horn boundary dropped the thecate qualifier

- Issue: https://github.com/CultureBotAI/CellStructureMech/issues/1938
- Severity: medium
- Status: fixed in commit `4a237077`

The initial record used `GO:0097686` as the narrower apical-horn class but only
described it as an `is_a` child or specialized apex. GO defines that term as a
horn-shaped dinoflagellate apex found in thecate species, and leaving out those
qualifiers could blur the boundary between a general `GO:0097683` apex and the
narrower apical horn.

Fix: retained the horn-shaped thecate qualifier in the `GO:0097686`
record-level evidence, graph edge, second edge evidence item, graph summary,
and resolved `apical_horn_is_narrower_than_apex` interpretation.

## Post-Fix Validation

- `uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/dinoflagellate_apex.yaml`
- `uv run python scripts/validate_strict.py --quiet data/structures/other/dinoflagellate_apex.yaml`
- `uv run python scripts/validate_history.py history/records/dinoflagellate_apex`
- `uv run python scripts/build_text_embedding_map.py --refresh`
- `uv run python scripts/build_text_embedding_map.py --check`
- `uv run python scripts/render_pages.py`
- `uv run python scripts/check_docs.py --write`
- `uv run python scripts/render_pages.py --check`
- `uv run python scripts/check_docs.py --check`
- `uv run python scripts/validate_strict.py --quiet`
- `uv run python scripts/validate_history.py`
- `uv run python scripts/fetch_snippets.py --verify --check`
- `uv run python scripts/check_trait_links.py --check`
- `uv run python scripts/check_curies.py --check --report reports/curie_check.tsv`
- `uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `uv run python scripts/run_qc.py`
- `git diff --check`

All post-fix checks passed.
