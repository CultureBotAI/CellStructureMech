# Adversarial YAML Record Review: dinoflagellate sulcus

- PR: https://github.com/CultureBotAI/CellStructureMech/pull/1927
- Record: `data/structures/other/dinoflagellate_sulcus.yaml`
- Identifier: `GO:0097612`
- Reviewer: `codex`
- Review timestamp: `2026-10-02T17:50:24Z`

## Scope

Reviewed the new `dinoflagellate sulcus` record added in PR #1927 after the
initial branch push.

## Duplicate And Identity Checks

- Before adding the record, searched hidden and ignored files with
  `rg --no-ignore --hidden` for `GO:0097612`, `GO_0097612`,
  `dinoflagellate sulcus`, `longitudinal groove`, `PMID:7002229`, and
  `DOI:10.1016/0303-2647(80)90006-4` across curated records, history, reports,
  generated pages, docs, curation inputs, research, scripts, `.github`, build
  artifacts, and embeddings.
- The broad word search for `sulcus` included ignored and hidden files and
  found only the previous apical-groove review report that named `sulcus` as an
  adjacent absent GO child, plus the newly added sulcus record after creation.
- No pre-existing exact `GO:0097612`, dinoflagellate-sulcus record, or
  sulcus/longitudinal-furrow/longitudinal-groove synonym entry existed under
  `data/structures` before the new YAML and derived artifacts were created.

## Authority Checks

- Verified `GO:0097612` through OLS as a live cellular-component term named
  `dinoflagellate sulcus`, with broad synonym `sulcus`, related synonyms
  `longitudinal furrow` and `longitudinal groove`, and a definition that places
  it on the ventral side of a dinoflagellate cell, says it partially houses the
  longitudinal flagellum, and says it intersects the cingulum.
- Verified the OLS GO graph places `GO:0097612` under `GO:0097610` cell surface
  furrow and exposes narrower child terms.
- Verified OLS returns `GO:0097618` as the narrower `dinoflagellate sulcal
  notch` child of `GO:0097612`, not as an exact duplicate of the general sulcus.
- Verified `NCBITaxon:2864` is the active `Dinophyceae` class taxon with NCBI
  ESummary and the repository CURIE liveness gate.
- Verified `PMID:7002229` and `DOI:10.1016/0303-2647(80)90006-4` resolve as
  Taylor 1980, "On dinoflagellate evolution", in EuropePMC/Crossref metadata.

## Findings

### 1. Missing evidence for cingulum graph node

- Issue: https://github.com/CultureBotAI/CellStructureMech/issues/1928
- Severity: medium
- Status: fixed in commit `d38df9ff`

The `sulcus_cingulum_topology` graph used a `dinoflagellate_cingulum` STRUCTURE
node grounded to `GO:0097611`, but the record-level evidence list cited only the
sulcus, the parent cell-surface-furrow term, and Taylor 1980 metadata. That
left a graph node grounded to a GO class with no explicit authority entry at
record scope.

Fix: added `GO:0097611` to record-level evidence and scoped the note to the
dinoflagellate cingulum term named by the `GO:0097612` definition.

### 2. Sulcal notch boundary was undocumented

- Issue: https://github.com/CultureBotAI/CellStructureMech/issues/1929
- Severity: medium
- Status: fixed in commit `d38df9ff`

The source search for sulcus also returned `GO:0097618` `dinoflagellate sulcal
notch`, a narrower child of `GO:0097612`. The initial record did not document
whether that term was an exact duplicate, a synonym, or a child that should be
curated separately.

Fix: added a resolved `sulcal_notch_is_narrower` interpretation explaining that
`GO:0097618` is a narrower posterior sulcus class and should not be folded into
the general `GO:0097612` record.

## Post-Fix Validation

- `uv run python scripts/validate_strict.py --quiet data/structures/other/dinoflagellate_sulcus.yaml`
- `just validate-history history/records/dinoflagellate_sulcus`
- `just text-embeddings-refresh`
- `just text-map-check`
- `just render`
- `just docs-stats`
- `just render-check`
- `just docs-check`
- `just validate-strict --quiet`
- `just validate-history`
- `just evidence-verify`
- `just check-trait-links --check`
- `just check-curies --check --report reports/curie_check.tsv`
- `just validate-products`
- `just qc`
- `git diff --check`

All post-fix checks passed.
