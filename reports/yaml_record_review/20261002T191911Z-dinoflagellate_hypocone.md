# Adversarial YAML Record Review: dinoflagellate hypocone

- PR: https://github.com/CultureBotAI/CellStructureMech/pull/1933
- Record: `data/structures/other/dinoflagellate_hypocone.yaml`
- Identifier: `GO:0097614`
- Reviewer: `codex`
- Review timestamp: `2026-10-02T19:19:11Z`

## Scope

Reviewed the new `dinoflagellate hypocone` record added in PR #1933 after the
initial branch push.

## Duplicate And Identity Checks

- Before adding the record, searched hidden and ignored files with
  `rg --no-ignore --hidden` for `GO:0097614`, `GO_0097614`,
  `dinoflagellate hypocone`, `hypocone`, `hyposome`, `hypotheca`, and nearby
  `GO:009761*` and `GO:009768*` dinoflagellate terms across curated records,
  history, reports, generated pages, docs, curation inputs, research, scripts,
  `.github`, build artifacts, and embeddings.
- The broad search found `GO:0097614` only as adjacent topology evidence in the
  already-merged epicone record and in generated/report caches before the new
  hypocone YAML and derived artifacts were created.
- No pre-existing exact `GO:0097614`, top-level dinoflagellate-hypocone
  record, or hypocone/hyposome/hypotheca synonym entry existed under
  `data/structures`; this exact duplicate search included hidden and ignored
  files via `rg --no-ignore --hidden`.

## Authority Checks

- Verified `GO:0097614` through QuickGO as a live cellular-component term named
  `dinoflagellate hypocone`, with broad synonym `hypocone`, related synonyms
  `hyposome` and `hypotheca`, and a definition that describes it as the part
  of a dinoflagellate cell below the cingulum and separated from the epicone by
  the cingulum.
- Verified the QuickGO ancestor payload places `GO:0097614` under
  `GO:0110165` cellular anatomical structure.
- Verified QuickGO lists `GO:0097684` dinoflagellate antapex as a `part_of`
  child of `GO:0097614`.
- Verified `GO:0097618` through QuickGO as a live cellular-component term named
  `dinoflagellate sulcal notch`, with a definition linking an antapex-reaching
  sulcus to bilobed hypocone morphology and ancestors placing it under
  `GO:0097612` dinoflagellate sulcus.
- Verified all newly referenced GO terms resolve through the repository CURIE
  liveness and id-label correspondence gates.

## Findings

### 1. Cingulum boundary was one-sided

- Issue: https://github.com/CultureBotAI/CellStructureMech/issues/1934
- Severity: medium
- Status: fixed in commit `40ae1125`

The initial `hypocone_topology` graph included a `dinoflagellate_cingulum`
STRUCTURE node and a cingulum-to-hypocone edge, but it omitted the reciprocal
cingulum-to-epicone boundary even though the `GO:0097614` definition says the
cingulum separates the hypocone from the epicone. Traversing cingulum boundary
edges would therefore see only the posterior structure.

Fix: added a `dinoflagellate_cingulum` to `dinoflagellate_epicone` `separates`
edge with `GO:0097614` evidence, making the cingulum boundary two-sided in the
hypocone graph.

### 2. Sulcal-notch morphology was omitted

- Issue: https://github.com/CultureBotAI/CellStructureMech/issues/1935
- Severity: medium
- Status: fixed in commit `40ae1125`

The initial record followed the direct `GO:0097684` antapex child of
`GO:0097614`, but it did not document `GO:0097618` dinoflagellate sulcal
notch. GO defines the sulcal notch as a `GO:0097612` sulcus subclass that
extends to the posterior antapex and can make the hypocone appear bilobed, so
future curation needed an explicit split keeping that adjacent sulcus
morphology out of the whole hypocone record.

Fix: added `GO:0097618` and `GO:0097612` evidence, sulcus and sulcal-notch
STRUCTURE nodes, GO-backed sulcal-notch topology edges, and a resolved
`sulcal_notch_is_sulcus_subclass` interpretation.

## Post-Fix Validation

- `uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/dinoflagellate_hypocone.yaml`
- `uv run python scripts/validate_strict.py --quiet data/structures/other/dinoflagellate_hypocone.yaml`
- `uv run python scripts/validate_history.py history/records/dinoflagellate_hypocone`
- `just text-embeddings-refresh`
- `just text-map-check`
- `just render`
- `just docs-stats`
- `just render-check`
- `just docs-check`
- `uv run python scripts/validate_strict.py --quiet`
- `uv run python scripts/validate_history.py`
- `just evidence-verify`
- `just check-trait-links --check`
- `just check-curies`
- `just validate-products`
- `git diff --check`
- `just qc`

All post-fix checks passed.
