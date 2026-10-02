# Adversarial YAML Record Review: dinoflagellate epicone

- PR: https://github.com/CultureBotAI/CellStructureMech/pull/1930
- Record: `data/structures/other/dinoflagellate_epicone.yaml`
- Identifier: `GO:0097613`
- Reviewer: `codex`
- Review timestamp: `2026-10-02T18:34:10Z`

## Scope

Reviewed the new `dinoflagellate epicone` record added in PR #1930 after the
initial branch push.

## Duplicate And Identity Checks

- Before adding the record, searched hidden and ignored files with
  `rg --no-ignore --hidden` for `GO:0097613`, `GO_0097613`,
  `dinoflagellate epicone`, `epicone`, `episome`, and `epitheca` across
  curated records, history, reports, generated pages, docs, curation inputs,
  research, scripts, `.github`, build artifacts, and embeddings.
- The broad word search for `epicone` and exact `GO:0097613` included ignored
  and hidden files and found only the existing apical-groove record, history,
  rendered page, and review report that used the epicone as adjacent topology,
  plus liveness/report caches.
- No pre-existing exact `GO:0097613`, top-level dinoflagellate-epicone record,
  or epicone/episome/epitheca synonym entry existed under `data/structures`
  before the new YAML and derived artifacts were created.

## Authority Checks

- Verified `GO:0097613` through QuickGO as a live cellular-component term named
  `dinoflagellate epicone`, with broad synonym `epicone`, related synonyms
  `episome` and `epitheca`, and a definition that describes it as the part of a
  dinoflagellate cell above the cingulum and separated from the hypocone by the
  cingulum.
- Verified the QuickGO ancestor payload places `GO:0097613` under `GO:0110165`
  cellular anatomical structure.
- Verified QuickGO lists `GO:0097683` dinoflagellate apex and `GO:0097685`
  dinoflagellate apical groove as `part_of` children of `GO:0097613`.
- Verified `GO:0097614` is a live cellular-component sibling term for
  `dinoflagellate hypocone`, the posterior counterpart separated from the
  epicone by the cingulum.
- Verified `GO:0097683`, `GO:0097614`, and all other newly referenced GO terms
  resolve through the repository CURIE liveness and id-label gates.

## Findings

### 1. Hypocone boundary was undocumented

- Issue: https://github.com/CultureBotAI/CellStructureMech/issues/1931
- Severity: medium
- Status: fixed in commit `96205fe4`

The record cited `GO:0097614` dinoflagellate hypocone because the
`GO:0097613` epicone definition names the hypocone, but it only documented the
dinoflagellate apex as a narrower boundary. `GO:0097614` is the posterior
counterpart separated from the epicone by the cingulum, not a synonym or a part
of the epicone.

Fix: added a resolved `hypocone_is_sibling` interpretation explaining that
`GO:0097614` should remain separate from the anterior `GO:0097613` epicone
record and be left for future posterior hypocone curation.

### 2. Missing cingulum/hypocone topology edges

- Issue: https://github.com/CultureBotAI/CellStructureMech/issues/1932
- Severity: medium
- Status: fixed in commit `96205fe4`

The initial `epicone_topology` graph included the GO is-a edge and the
apex/apical-groove part edges, but it omitted the cingulum and hypocone even
though the record-level evidence cited both and the `GO:0097613` definition
says the cingulum separates the epicone from the hypocone. That left the
definition's strongest boundary claim out of the graph layer.

Fix: added `dinoflagellate_cingulum` and `dinoflagellate_hypocone` STRUCTURE
nodes and two `GO:0097613`-supported boundary edges that record the epicone as
separated from the hypocone and the cingulum as the separating boundary.

## Post-Fix Validation

- `uv run python scripts/validate_strict.py --quiet data/structures/other/dinoflagellate_epicone.yaml`
- `just validate-history history/records/dinoflagellate_epicone`
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
