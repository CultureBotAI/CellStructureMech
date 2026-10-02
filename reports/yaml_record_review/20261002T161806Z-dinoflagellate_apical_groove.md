# Adversarial YAML Record Review: dinoflagellate apical groove

- PR: https://github.com/CultureBotAI/CellStructureMech/pull/1921
- Record: `data/structures/other/dinoflagellate_apical_groove.yaml`
- Identifier: `GO:0097685`
- Reviewer: `codex`
- Review timestamp: `2026-10-02T16:18:06Z`

## Scope

Reviewed the new `dinoflagellate apical groove` record added in PR #1921 after
the initial branch push.

## Duplicate And Identity Checks

- Before adding the record, searched hidden and ignored files with
  `rg --no-ignore --hidden` for `GO:0097685`, `GO_0097685`,
  `dinoflagellate apical groove`, `apical groove`, `cingulum`, `sulcus`, and
  `apical furrow` across curated records, history, reports, generated pages,
  docs, curation inputs, research, scripts, `.github`, and build artifacts.
- After adding the record, searched hidden and ignored files for the exact GO
  term, label, synonym, `Margalefidinium polykrikoides`,
  `Cochlodinium polykrikoides`, `PMID:20561119`,
  `DOI:10.1111/j.1550-7408.2010.00491.x`, and
  `DOI:10.1016/j.hal.2017.01.008`.
- No pre-existing exact `GO:0097685` or dinoflagellate-apical-groove record was
  found before the new YAML and derived artifacts were created.

## Authority Checks

- Verified `GO:0097685` in QuickGO as a live cellular-component term named
  `dinoflagellate apical groove`, with definition source `PMID:20561119`.
- Verified the OLS GO graph places `GO:0097685` under `GO:0097610` cell
  surface furrow, `part_of GO:0097613` dinoflagellate epicone, and `in_taxon`
  `NCBITaxon:2864` Dinophyceae.
- Verified `PMID:20561119` and
  `DOI:10.1111/j.1550-7408.2010.00491.x` for Iwataki et al. 2010 in
  Europe PMC/Crossref.
- Verified `DOI:10.1016/j.hal.2017.01.008` for the 2017 Harmful Algae paper
  that established `Margalefidinium` for `Cochlodinium polykrikoides` and allied
  species.
- Verified `NCBITaxon:77300` resolves to active species
  `Margalefidinium polykrikoides` with NCBI ESummary and the repository CURIE
  liveness gate.

## Findings

### 1. Taxonomic row mixed two papers

- Issue: https://github.com/CultureBotAI/CellStructureMech/issues/1922
- Severity: medium
- Status: fixed in commit `6b1b18a8`

The `NCBITaxon:77300` distribution note said the species was later transferred
to `Margalefidinium`, but the row cited only the 2010 ultrastructure DOI. That
paper supports the apical-groove observation in the organism studied as
`Cochlodinium polykrikoides`; it cannot support a nomenclatural transfer
published later.

Fix: removed the transfer clause from the taxonomic-distribution row and kept
the 2017 `Margalefidinium` paper as record-level evidence only.

### 2. `GO:0097613` evidence overclaimed

- Issue: https://github.com/CultureBotAI/CellStructureMech/issues/1923
- Severity: medium
- Status: fixed in commit `6b1b18a8`

The standalone `GO:0097613` evidence note described it as the epicone term that
carried the apical groove. `GO:0097613` defines the epicone; the
apical-groove-to-epicone `part_of` edge comes from the `GO:0097685` graph.

Fix: narrowed the record-level `GO:0097613` note to identify only the
dinoflagellate epicone term.

## Post-Fix Validation

- `uv run python scripts/validate_strict.py --quiet data/structures/other/dinoflagellate_apical_groove.yaml`
- `just text-embeddings-refresh`
- `just render`
- `just validate-history history/records/dinoflagellate_apical_groove`
- `just text-map-check`
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
