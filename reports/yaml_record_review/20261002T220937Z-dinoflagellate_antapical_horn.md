# Adversarial YAML Record Review: dinoflagellate antapical horn

- PR: https://github.com/CultureBotAI/CellStructureMech/pull/1945
- Record: `data/structures/other/dinoflagellate_antapical_horn.yaml`
- Identifier: `GO:0097687`
- Reviewer: `codex`
- Review timestamp: `2026-10-02T22:09:37Z`

## Scope

Reviewed the new `dinoflagellate antapical horn` record added in PR #1945
after the initial branch push.

## Duplicate And Identity Checks

- Before adding the record, searched hidden and ignored files with
  `rg --no-ignore --hidden` for `dinoflagellate antapical horn`,
  `GO:0097687`, `GO_0097687`, and `antapical horn` across curated records,
  history, reports, generated pages, docs, curation inputs, research, scripts,
  `.github`, build artifacts, pages, and embeddings.
- The broad hidden/ignored-inclusive search found `GO:0097687` only as adjacent
  topology evidence in the already-merged antapex record, generated pages,
  CURIE report/cache files, and the antapex review/history before the new
  antapical-horn YAML and derived artifacts were created.
- No pre-existing exact `GO:0097687`, top-level
  `dinoflagellate antapical horn` record, or `antapical horn` synonym entry
  existed under `data/structures`; this exact duplicate search included hidden
  and ignored files via `rg --no-ignore --hidden`.

## Authority Checks

- Verified `GO:0097687` through QuickGO and OLS as a live cellular-component
  term named `dinoflagellate antapical horn`, with definition
  `A horn-shaped dinoflagellate antapex found in thecate species.` and
  definition xref `PMID:7002229`.
- Verified the QuickGO `GO:0097687` history records a direct
  `is a GO:0097684 (dinoflagellate antapex)` relation.
- Verified QuickGO lists `GO:0097684` dinoflagellate antapex,
  `GO:0097614` dinoflagellate hypocone, `GO:0110165` cellular anatomical
  structure, and `GO:0005575` cellular component in the `GO:0097687` ancestor
  closure.
- Verified the QuickGO `GO:0097684` history records direct
  `part of GO:0097614 (dinoflagellate hypocone)` topology and lists
  `GO:0097687` as an `is_a` child.
- Verified the QuickGO `GO:0097614` children endpoint lists `GO:0097684` as a
  `part_of` child.
- Verified Crossref and Europe PMC identify `PMID:7002229` as Taylor 1980,
  _Biosystems_, DOI `10.1016/0303-2647(80)90006-4`, pages 65-108, and that
  Europe PMC reports no PMC, open-access, full-text, or PDF route.
- Verified the Crossref Elsevier text-mining URL exposed in DOI metadata did
  not yield readable article-body text in this pass.
- Verified all newly referenced GO terms resolve through the repository CURIE
  liveness and id-label correspondence gates.

## Findings

### 1. The antapical-horn parent edge cited ancestor closure

- Issue: https://github.com/CultureBotAI/CellStructureMech/issues/1946
- Severity: medium
- Status: fixed in commit `e4906393`

The initial `dinoflagellate_antapical_horn -> dinoflagellate_antapex`
`is a` edge cited the QuickGO `GO:0097687` ancestors endpoint. That endpoint
establishes `GO:0097684` is in the closure, but QuickGO history has the more
specific direct relation for the child term.

Fix: changed the record-level `GO:0097684` evidence and the graph-level
`GO:0097687` evidence to cite the direct `GO:0097687 is_a GO:0097684` history
relation.

### 2. Inherited hypocone parthood was not explicit enough

- Issue: https://github.com/CultureBotAI/CellStructureMech/issues/1947
- Severity: medium
- Status: fixed in commit `e4906393`

The initial `dinoflagellate_antapical_horn is part of
dinoflagellate_hypocone` edge materialized parthood inherited through
`GO:0097684`, but the graph scope note described exact GO topology and the
`GO:0097687` evidence row attributed the inherited path to a flat ancestors
response.

Fix: rewrote the graph scope note, the antapical-horn to hypocone edge
description, and the `GO:0097687` evidence note so the edge is explicitly
identified as inherited via `GO:0097687 is_a GO:0097684` plus
`GO:0097684 part_of GO:0097614`.

## Post-Fix Validation

- `uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/dinoflagellate_antapical_horn.yaml`
- `just validate-strict --quiet data/structures/other/dinoflagellate_antapical_horn.yaml`
- `just validate-history history/records/dinoflagellate_antapical_horn/2026-10-02T215653Z-codex-b4e26f.yaml`
- `just text-embeddings-refresh`
- `just text-map-check`
- `just render`
- `just docs-stats`
- `just render-check`
- `just docs-check`
- `just validate-strict --quiet`
- `just validate-history`
- `just evidence-verify --check`
- `just check-trait-links --check`
- `just check-curies-strict`
- `just validate-products`
- `git diff --check`
- `just qc`

All post-fix checks passed.
