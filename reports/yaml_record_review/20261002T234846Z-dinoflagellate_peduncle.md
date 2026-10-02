# Adversarial YAML Record Review: dinoflagellate peduncle

- PR: https://github.com/CultureBotAI/CellStructureMech/pull/1951
- Record: `data/structures/appendage/dinoflagellate_peduncle.yaml`
- Identifier: `GO:1990905`
- Reviewer: `codex`
- Review timestamp: `2026-10-02T23:48:46Z`

## Scope

Reviewed the new `dinoflagellate peduncle` record added in PR #1951 after
the initial branch push.

## Duplicate And Identity Checks

- Before adding the record, searched hidden and ignored files with
  `rg --no-ignore --hidden` for `dinoflagellate peduncle`, `GO:1990905`,
  `GO_1990905`, and peduncle synonym/candidate forms across curated records,
  history, reports, generated pages, docs, curation inputs, research, scripts,
  `.github`, build artifacts, pages, and embeddings.
- After scaffolding and expansion, hidden/ignored-inclusive duplicate searches
  found `GO:1990905` and `dinoflagellate peduncle` only in the new YAML record
  and its intentionally generated or manually curated artifacts.
- No pre-existing exact `GO:1990905`, top-level `dinoflagellate peduncle`
  record, or peduncle synonym entry existed under `data/structures`; this exact
  duplicate search included hidden and ignored files via
  `rg --no-ignore --hidden`.

## Authority Checks

- Verified `GO:1990905` through QuickGO and OLS as a live cellular-component
  term named `dinoflagellate peduncle`.
- Verified the current direct `GO:1990905` `is a` parent as `GO:0120025`
  `plasma membrane bounded cell projection`.
- Verified QuickGO lists `GO:0110165` cellular anatomical structure,
  `GO:0120025` plasma membrane bounded cell projection, `GO:0032991` protein-
  containing complex, and `GO:0005575` cellular component in the `GO:1990905`
  ancestor closure.
- Verified `GO:1990905` records Lee and Kugrens 1992 as an authority through
  `PMID:1480107`.
- Verified `PMID:1480107`, `PMCID:PMC372886`, and
  `DOI:10.1128/mr.56.4.529-542.1992` identify the Lee and Kugrens 1992
  _Microbiological Reviews_ article cited by `GO:1990905`; PMC exposed article
  metadata and HTML, but no peduncle-specific searchable body text was available
  in this pass.
- Verified `DOI:10.3390/microorganisms2010073` and `PMID:27694777` identify
  Okamoto and Keeling 2014, an open-access review of dinoflagellate, perkinsid,
  and colpodellid flagellar-apparatus ultrastructure that discusses the
  dinoflagellate peduncle, the microtubular strand or basket, and apical-complex
  homology hypotheses.
- Verified `DOI:10.1038/s41467-022-28867-8`, `PMID:35288549`, and
  `PMCID:PMC8921327` identify Larsson et al. 2022, the open-access primary
  study that observed Australian `Prorocentrum cf. balticum` strains feeding on
  `Rhodomonas salina` through a short tubular peduncle.
- Verified `DOI:10.1111/jeu.70017` and `PMID:40448289` identify Larsson et al.
  2025, the morphological and phylogenetic characterization naming
  `Prorocentrum insidiosum` sp. nov. for the Australian strains originally
  reported as `Prorocentrum cf. balticum`.
- Verified all newly referenced GO, DOI, PMID, and NCBITaxon identifiers resolve
  through the repository CURIE liveness and id-label correspondence gates.

## Findings

### 1. Okamoto/Keeling peduncle evidence needed a narrower claim

- Issue: https://github.com/CultureBotAI/CellStructureMech/issues/1952
- Severity: medium
- Status: fixed in commit `cd83c15e`

The initial Okamoto and Keeling 2014 evidence note risked overgeneralizing from
the reviewed microtubular-strand literature and did not make the distinction
between a microtubular strand or basket near the flagellar apparatus and
confirmed extension of that strand into a peduncle in a specific lineage
explicit enough.

Fix: narrowed the Okamoto and Keeling 2014 evidence to state that the authors
distinguished the widespread microtubular strand or basket near the flagellar
apparatus from confirmed peduncle membership in specific lineages, including
their note that the analogous gonyaulacoid strand had not been shown to extend
into the peduncle.

### 2. Prorocentrum peduncular feeding needed the 2022 primary source

- Issue: https://github.com/CultureBotAI/CellStructureMech/issues/1953
- Severity: medium
- Status: fixed in commit `cd83c15e`

The initial record cited Larsson et al. 2025 for `Prorocentrum insidiosum`
taxonomy and feeding biology, but the primary observation of the Australian
strains feeding through a short tubular peduncle came from Larsson et al. 2022.

Fix: added `DOI:10.1038/s41467-022-28867-8` and `PMID:35288549` evidence for
Larsson et al. 2022, used those rows for the primary peduncular-feeding
observation, and narrowed the Larsson et al. 2025 evidence row to
`Prorocentrum insidiosum` taxonomy and strain naming.

## Post-Fix Validation

- `uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/appendage/dinoflagellate_peduncle.yaml`
- `just validate-strict --quiet data/structures/appendage/dinoflagellate_peduncle.yaml`
- `just validate-history history/records/dinoflagellate_peduncle/2026-10-02T232926Z-codex-41b398.yaml`
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
