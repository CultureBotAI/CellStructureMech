# Adversarial YAML Record Review: dinoflagellate apical horn

- PR: https://github.com/CultureBotAI/CellStructureMech/pull/1939
- Record: `data/structures/other/dinoflagellate_apical_horn.yaml`
- Identifier: `GO:0097686`
- Reviewer: `codex`
- Review timestamp: `2026-10-02T20:38:49Z`

## Scope

Reviewed the new `dinoflagellate apical horn` record added in PR #1939 after
the initial branch push.

## Duplicate And Identity Checks

- Before adding the record, searched hidden and ignored files with
  `rg --no-ignore --hidden` for `dinoflagellate apical horn`, `GO:0097686`,
  `GO_0097686`, `apical horn`, `horn-shaped dinoflagellate apex`, and `thecate`
  across curated records, history, reports, generated pages, docs, curation
  inputs, research, scripts, `.github`, build artifacts, pages, and embeddings.
- The broad search found `GO:0097686` only as adjacent topology evidence in the
  already-merged apex record, generated pages, the CURIE cache, and the apex
  review report/history before the new apical-horn YAML and derived artifacts
  were created.
- No pre-existing exact `GO:0097686`, top-level dinoflagellate-apical-horn
  record, or `apical horn` synonym entry existed under `data/structures`; this
  exact duplicate search included hidden and ignored files via
  `rg --no-ignore --hidden`.

## Authority Checks

- Verified `GO:0097686` through QuickGO as a live cellular-component term named
  `dinoflagellate apical horn`, with a definition for a horn-shaped
  dinoflagellate apex found in thecate species, xref `PMID:7002229`, and
  `only_in_taxon` constraint `NCBITaxon:2864` Dinophyceae.
- Verified QuickGO records an `is_a` relation from `GO:0097686` to
  `GO:0097683` dinoflagellate apex and lists `GO:0097613` dinoflagellate
  epicone and `GO:0110165` cellular anatomical structure among `GO:0097686`
  ancestors.
- Verified the QuickGO children endpoint for `GO:0097686` has no narrower child
  terms to model in this pass.
- Verified all newly referenced GO terms resolve through the repository CURIE
  liveness and id-label correspondence gates.

## Findings

### 1. Epicone parthood was only implicit

- Issue: https://github.com/CultureBotAI/CellStructureMech/issues/1940
- Severity: medium
- Status: fixed in commit `72188860`

The initial record modeled `GO:0097686` as an exact child of `GO:0097683`, and
its graph placed the parent apex in the dinoflagellate epicone. The
apical-horn record itself did not carry `part_of: GO:0097613`, and the graph
omitted an explicit `dinoflagellate_apical_horn is part of
dinoflagellate_epicone` edge, so consumers had to infer apical-horn location
through the intermediate apex node.

Fix: added record-level `part_of: GO:0097613` and a graph edge materializing
the inherited apical-horn-to-epicone topology with `GO:0097686` and
`GO:0097683` evidence.

### 2. The graph flattened the GO ancestor path

- Issue: https://github.com/CultureBotAI/CellStructureMech/issues/1941
- Severity: medium
- Status: fixed in commit `72188860`

The initial `apical_horn_apex_topology` graph included both the immediate
`dinoflagellate_apical_horn is a dinoflagellate_apex` edge and an additional
`dinoflagellate_apical_horn is a cellular_anatomical_structure` edge supported
only by the transitive `GO:0110165` ancestor payload. That made the broad
cellular-anatomical-structure ancestor look like peer topology beside the exact
`GO:0097683` parent.

Fix: kept `GO:0110165` as record-level ancestor evidence but removed the
`cellular_anatomical_structure` graph node and transitive `is a` edge, leaving
the graph focused on exact apical-horn, apex, and epicone topology.

## Post-Fix Validation

- `uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/dinoflagellate_apical_horn.yaml`
- `uv run python scripts/validate_strict.py --quiet data/structures/other/dinoflagellate_apical_horn.yaml`
- `uv run python scripts/validate_history.py history/records/dinoflagellate_apical_horn`
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
