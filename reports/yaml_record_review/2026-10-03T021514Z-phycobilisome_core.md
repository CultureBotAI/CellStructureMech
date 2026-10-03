# YAML Record Review: phycobilisome_core

- **Record:** `data/structures/energy_complex/phycobilisome_core.yaml`
- **PR:** https://github.com/CultureBotAI/CellStructureMech/pull/1960
- **Initial commit:** `dc6c781a`
- **Review-fix commit:** `6e312874`
- **Reviewer:** codex
- **Timestamp:** 2026-10-03T02:15:14Z

## Scope

Adversarial review of the new minted `cellstructuremech:phycobilisome_core`
record added in PR #1960. The review covered identity, de-duplication against
the existing `GO:0030089` `phycobilisome` parent record, GO and minted
parentage, DOI/PMID evidence, NCBI Taxonomy labels, component grounding
decisions, canonical examples, the energy-transfer causal graph, generated site
output, and append-only history.

## Findings

### #1961: Sauer 2021 taxon attribution used an unsupported Synechocystis example

The initial record cited `DOI:10.1038/s41467-021-25813-y` as evidence that the
`Synechocystis sp. PCC 6803` phycobilisome core was resolved by cryo-EM. Sauer
2021 instead resolves phycobilisomes from PCC 7002 and PCC 7120; Synechocystis
was not the directly solved canonical example for the core.

- Filed: https://github.com/CultureBotAI/CellStructureMech/issues/1961
- Fixed in: `6e312874`
- Fix: replaced the canonical example with NCBI-verified
  `NCBITaxon:32049` / `Picosynechococcus sp. PCC 7002`; rewrote Sauer-specific
  component, function, and causal-graph evidence notes to refer to directly
  supported PCC 7002/PCC 7120 phycobilisome cores or cyanobacterial cores
  generically; added a linked append-only history record.

## Post-Fix Checks

- `uv run python scripts/validate_strict.py --quiet data/structures/energy_complex/phycobilisome_core.yaml`
- `uv run python scripts/validate_history.py history/records/phycobilisome_core`
- `just text-map-check`
- `just render-check`
- `just docs-check`
- `git diff --check`
- `uv run python scripts/fetch_snippets.py --verify --check`
- `uv run python scripts/check_trait_links.py --check`
- `uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `uv run python scripts/check_curies.py --check --report reports/curie_check.tsv`
- `just qc`

## Residual Scope

The review did not modify the older `GO:0030089` `phycobilisome` record, which
contains pre-existing Sauer/Synechocystis wording outside the new child record's
diff. That should be handled in a separate edit/review workflow if the parent
record is selected for cleanup.
