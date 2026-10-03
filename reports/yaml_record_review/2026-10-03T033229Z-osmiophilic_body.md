# Adversarial YAML Record Review: osmiophilic body

- PR: https://github.com/CultureBotAI/CellStructureMech/pull/1964
- Record: `data/structures/membrane_organelle/osmiophilic_body.yaml`
- Identifier: `GO:0044310`
- Reviewer: `codex`
- Review timestamp: `2026-10-03T03:32:29Z`

## Scope

Reviewed the new `osmiophilic body` record added in PR #1964 after the initial
branch push.

## Duplicate And Identity Checks

- Before adding the record, searched hidden and ignored files with
  `rg --no-ignore --hidden` for `GO:0044310`, `osmiophilic body`,
  `osmiophilic bodies`, `Pfg377`, `pfg377`, `PFG377`, `PMID:18086189`,
  `10.1111/j.1365-2958.2007.06039`, `10.1074/mcp.M116.060681`, and related
  DOI spellings across curated records, history, reports, generated pages,
  docs, curation inputs, research, scripts, `.github`, build artifacts, pages,
  and embeddings.
- No pre-existing exact `GO:0044310`, top-level osmiophilic-body record, or
  osmiophilic-body synonym entry existed under `data/structures`. This exact
  duplicate search included hidden and ignored files via `rg --no-ignore
  --hidden`.
- After rendering, searched hidden and ignored source, data, history, and page
  files for the deleted temporary `expand_osmiophilic_body` mutator and found no
  remaining non-report references.

## Authority Checks

- Verified `GO:0044310` through QuickGO as a live cellular-component term named
  `osmiophilic body`, with the Plasmodium female-gametocyte vesicle definition
  used verbatim in the record and GO's source xref to `PMID:18086189`.
- Verified QuickGO lists `GO:0031410` cytoplasmic vesicle among the
  `GO:0044310` ancestors.
- Verified the QuickGO children endpoint for `GO:0044310` has no narrower child
  terms to model in this pass.
- Verified `DOI:10.1016/0166-6851(95)02491-3`,
  `DOI:10.1111/j.1365-2958.2007.06039.x`, and
  `DOI:10.1074/mcp.m116.060681` through Crossref before committing.
- Verified all newly referenced DOI and GO identifiers resolve through the
  repository CURIE liveness and id-label correspondence gates.

## Findings

No concrete defects were found that needed a GitHub issue or a follow-up YAML
edit.

The review specifically checked for these common failure modes:

- duplicate identity under a prior label, GO CURIE, plural label, Pfg377
  component thread, or primary osmiophilic-body DOI;
- a minted local identifier where exact GO identity existed;
- a guessed InterPro, Pfam, NCBIfam, or lipid CURIE for Pfg377 or the generic
  vesicle membrane;
- over-broad Apicomplexa or Eukaryota taxonomic distribution unsupported by the
  scoped osmiophilic-body evidence;
- a graph edge that turned GO's postulated osmiophilic-body content release
  into a supported causal mechanism.

The submitted record already used `GO:0044310`, limited the taxonomic row and
canonical example to `Plasmodium falciparum`, left Pfg377 and the
osmiophilic-body membrane as `REVIEWED_LABEL_ONLY`, and included a resolved
discussion that keeps the postulated release mechanism out of the graph.

## Validation

- `uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/membrane_organelle/osmiophilic_body.yaml`
- `uv run python scripts/validate_strict.py --quiet data/structures/membrane_organelle/osmiophilic_body.yaml`
- `just validate-history history/records/osmiophilic_body`
- `just text-embeddings-refresh`
- `just render`
- `just docs-stats`
- `just text-map-check`
- `just render-check`
- `just docs-check`
- `uv run python scripts/validate_strict.py --quiet`
- `just validate-history`
- `uv run python scripts/fetch_snippets.py --verify --check`
- `uv run python scripts/check_trait_links.py --check`
- `uv run python scripts/check_curies.py --check --report reports/curie_check.tsv`
- `uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `git diff --check`
- `just qc`

All checks passed.
