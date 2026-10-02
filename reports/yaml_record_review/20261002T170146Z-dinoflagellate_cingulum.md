# Adversarial YAML Record Review: dinoflagellate cingulum

- PR: https://github.com/CultureBotAI/CellStructureMech/pull/1924
- Record: `data/structures/other/dinoflagellate_cingulum.yaml`
- Identifier: `GO:0097611`
- Reviewer: `codex`
- Review timestamp: `2026-10-02T17:01:46Z`

## Scope

Reviewed the new `dinoflagellate cingulum` record added in PR #1924 after the
initial branch push.

## Duplicate And Identity Checks

- Before adding the record, searched hidden and ignored files with
  `rg --no-ignore --hidden` for `GO:0097611`, `GO_0097611`,
  `dinoflagellate cingulum`, `cingulum`, `girdle`, `transverse groove`,
  `PMID:7002229`, and `DOI:10.1016/0303-2647(80)90006-4` across curated
  records, history, reports, generated pages, docs, curation inputs, research,
  scripts, `.github`, build artifacts, and embeddings.
- The broad word search for `cingulum` / `girdle` included ignored and hidden
  files and found only the previous apical-groove review report that named
  `cingulum` as an adjacent absent GO child, plus the newly added cingulum
  record after creation.
- No pre-existing exact `GO:0097611`, dinoflagellate-cingulum record, or
  cingulum/girdle/transverse-groove synonym entry existed under
  `data/structures` before the new YAML and derived artifacts were created.

## Authority Checks

- Verified `GO:0097611` through OLS as a live cellular-component term named
  `dinoflagellate cingulum`, with broad synonym `cingulum`, related synonyms
  `girdle` and `transverse groove`, and definition "A cell surface furrow that
  wraps around a dinoflagellate cell; the transverse flagellum lies in it."
- Verified the OLS GO graph places `GO:0097611` under `GO:0097610` cell surface
  furrow.
- Verified `NCBITaxon:2864` is the active `Dinophyceae` class taxon with NCBI
  ESummary and the repository CURIE liveness gate.
- Verified `PMID:7002229` and `DOI:10.1016/0303-2647(80)90006-4` resolve as
  Taylor 1980, "On dinoflagellate evolution", in EuropePMC/Crossref metadata.

## Findings

### 1. Missing graph-layer topology

- Issue: https://github.com/CultureBotAI/CellStructureMech/issues/1925
- Severity: medium
- Status: fixed in commit `7fb2d4bd`

The record added `parent_structures: [GO:0097610]`, but did not carry a
`causal_graphs` entry to preserve the evidence-backed GO `is_a` edge in the
graph layer. That left the only cingulum topology edge outside the explicit
edge model.

Fix: added a `cingulum_cell_surface_furrow_topology` NONMECHANISTIC graph with
`dinoflagellate_cingulum` and `cell_surface_furrow` STRUCTURE nodes and a
GO-backed `is a` edge from `GO:0097611` to `GO:0097610`.

### 2. Taylor 1980 readability was implicit

- Issue: https://github.com/CultureBotAI/CellStructureMech/issues/1926
- Severity: medium
- Status: fixed in commit `7fb2d4bd`

The Taylor 1980 PMID/DOI evidence notes cited a subscription Elsevier review
through GO/metadata routes, but they did not say no full text was reachable.
The curation contract treats unreadability as a finding and expects the record
to make that boundary explicit when a cited paper cannot be opened.

Fix: tightened the `PMID:7002229` and `DOI:10.1016/0303-2647(80)90006-4`
evidence notes so they say EuropePMC/Crossref metadata were checked and that no
PMC, open-access, full-text, article-body, or PDF route was reachable.

## Post-Fix Validation

- `uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/dinoflagellate_cingulum.yaml`
- `uv run python scripts/validate_strict.py --quiet data/structures/other/dinoflagellate_cingulum.yaml`
- `uv run python scripts/validate_strict.py --quiet`
- `uv run python scripts/validate_history.py history/records/dinoflagellate_cingulum`
- `uv run python scripts/validate_history.py`
- `just text-embeddings-refresh`
- `just text-map-check`
- `just render`
- `just render-check`
- `just docs-stats`
- `just docs-check`
- `just evidence-verify`
- `just check-trait-links --check`
- `just check-curies --check --report reports/curie_check.tsv`
- `just validate-products`
- `just qc`
- `git diff --check`

All post-fix checks passed.
