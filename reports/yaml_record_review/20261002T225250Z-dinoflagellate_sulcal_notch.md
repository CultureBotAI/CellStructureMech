# Adversarial YAML Record Review: dinoflagellate sulcal notch

- PR: https://github.com/CultureBotAI/CellStructureMech/pull/1948
- Record: `data/structures/other/dinoflagellate_sulcal_notch.yaml`
- Identifier: `GO:0097618`
- Reviewer: `codex`
- Review timestamp: `2026-10-02T22:52:50Z`

## Scope

Reviewed the new `dinoflagellate sulcal notch` record added in PR #1948 after
the initial branch push.

## Duplicate And Identity Checks

- Before adding the record, searched hidden and ignored files with
  `rg --no-ignore --hidden` for `dinoflagellate sulcal notch`,
  `GO:0097618`, `GO_0097618`, and `sulcal notch` across curated records,
  history, reports, generated pages, docs, curation inputs, research, scripts,
  `.github`, build artifacts, pages, and embeddings.
- The broad hidden/ignored-inclusive search found `GO:0097618` only as
  adjacent topology evidence in already-merged sulcus, hypocone, and antapex
  records, generated pages, CURIE report/cache files, and prior
  dinoflagellate review/history artifacts before the new sulcal-notch YAML and
  derived artifacts were created.
- No pre-existing exact `GO:0097618`, top-level
  `dinoflagellate sulcal notch` record, or `sulcal notch` synonym entry
  existed under `data/structures`; this exact duplicate search included hidden
  and ignored files via `rg --no-ignore --hidden`.

## Authority Checks

- Verified `GO:0097618` through QuickGO and OLS as a live cellular-component
  term named `dinoflagellate sulcal notch`.
- Verified the QuickGO and OLS payloads carry the exact synonym
  `dinoflagellate sulcus notch` and the related synonym `sulcal notch`.
- Verified the QuickGO `GO:0097618` history records a direct
  `is a GO:0097612 (dinoflagellate sulcus)` relation.
- Verified QuickGO lists `GO:0097612` dinoflagellate sulcus,
  `GO:0097610` cell surface furrow, `GO:0110165` cellular anatomical
  structure, `GO:0009986` cell surface, and `GO:0005575` cellular component in
  the `GO:0097618` ancestor closure.
- Verified the QuickGO `GO:0097618` children endpoint returned no narrower
  child terms.
- Verified Crossref and Europe PMC identify `PMID:7002229` as Taylor 1980,
  _Biosystems_, DOI `10.1016/0303-2647(80)90006-4`, pages 65-108, and that
  Europe PMC reports no PMC, open-access, full-text, or PDF route.
- Verified the Crossref Elsevier text-mining URL exposed in DOI metadata did
  not yield readable article-body text in this pass.
- Verified all newly referenced GO terms resolve through the repository CURIE
  liveness and id-label correspondence gates.

## Findings

### 1. Antapex and hypocone graph objects were under-grounded

- Issue: https://github.com/CultureBotAI/CellStructureMech/issues/1949
- Severity: medium
- Status: fixed in commit `4fc2da3f`

The initial sulcal-notch graph introduced `dinoflagellate_antapex` and
`dinoflagellate_hypocone` nodes grounded to `GO:0097684` and `GO:0097614`,
but the `extends to` and `gives bilobed appearance to` edges only cited
`GO:0097618`.

Fix: added edge-level `GO:0097684` evidence to the antapex extension edge and
edge-level `GO:0097614` evidence to the bilobed-hypocone edge.

### 2. Antapex and hypocone boundary decisions were implicit

- Issue: https://github.com/CultureBotAI/CellStructureMech/issues/1950
- Severity: medium
- Status: fixed in commit `4fc2da3f`

The initial record resolved the sulcal-notch versus sulcus boundary, but its
graph also touched the antapex and hypocone without explicitly documenting
that those links are morphology edges rather than subclass relations.

Fix: added a resolved interpretation explaining that `GO:0097618` remains
under `GO:0097612` and connects to the antapex and hypocone by morphology
only.

## Post-Fix Validation

- `uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/dinoflagellate_sulcal_notch.yaml`
- `just validate-strict --quiet data/structures/other/dinoflagellate_sulcal_notch.yaml`
- `just validate-history history/records/dinoflagellate_sulcal_notch/2026-10-02T223906Z-codex-15785b.yaml`
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
