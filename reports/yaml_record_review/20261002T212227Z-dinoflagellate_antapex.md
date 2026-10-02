# Adversarial YAML Record Review: dinoflagellate antapex

- PR: https://github.com/CultureBotAI/CellStructureMech/pull/1942
- Record: `data/structures/other/dinoflagellate_antapex.yaml`
- Identifier: `GO:0097684`
- Reviewer: `codex`
- Review timestamp: `2026-10-02T21:22:27Z`

## Scope

Reviewed the new `dinoflagellate antapex` record added in PR #1942 after the
initial branch push.

## Duplicate And Identity Checks

- Before adding the record, searched hidden and ignored files with
  `rg --no-ignore --hidden` for `dinoflagellate antapex`, `GO:0097684`,
  `GO_0097684`, and `antapex` across curated records, history, reports,
  generated pages, docs, curation inputs, research, scripts, `.github`, build
  artifacts, pages, and embeddings.
- The broad search found `GO:0097684` only as adjacent topology evidence in the
  already-merged hypocone record, generated pages, CURIE report/cache files,
  and hypocone review/history before the new antapex YAML and derived artifacts
  were created.
- No pre-existing exact `GO:0097684`, top-level dinoflagellate-antapex record,
  or `antapex` synonym entry existed under `data/structures`; this exact
  duplicate search included hidden and ignored files via
  `rg --no-ignore --hidden`.

## Authority Checks

- Verified `GO:0097684` through QuickGO as a live cellular-component term named
  `dinoflagellate antapex`, with broad synonym `antapex`, an
  `only_in_taxon` constraint for `NCBITaxon:2864` Dinophyceae, and an explicit
  `part of GO:0097614 (dinoflagellate hypocone)` relation in its history.
- Verified QuickGO lists `GO:0097614` dinoflagellate hypocone,
  `GO:0110165` cellular anatomical structure, and `GO:0005575` cellular
  component among the `GO:0097684` ancestors.
- Verified the QuickGO `GO:0097684` children endpoint lists `GO:0097687`
  `dinoflagellate antapical horn` as an `is_a` child.
- Verified the `GO:0097687` ancestors endpoint returns a live
  cellular-component term for the horn-shaped thecate dinoflagellate antapical
  horn, with `GO:0097684`, `GO:0097614`, `GO:0110165`, and `GO:0005575` in its
  ancestor closure.
- Verified all newly referenced GO terms resolve through the repository CURIE
  liveness and id-label correspondence gates.

## Findings

### 1. The antapex-hypocone edge cited ancestor closure as if it were direct

- Issue: https://github.com/CultureBotAI/CellStructureMech/issues/1943
- Severity: medium
- Status: fixed in commit `c9ae6c44`

The initial `dinoflagellate_antapex -> dinoflagellate_hypocone` graph edge
claimed that QuickGO lists `GO:0097614` among the `GO:0097684` ancestors
through part-of topology. The `/ancestors` response establishes that the
hypocone is in the ancestor closure, but not the relation label on the
intermediate edge.

Fix: changed the GO:0097684 evidence note to cite the QuickGO GO:0097684
history entry that directly records a `part_of` relation to GO:0097614.

### 2. Sulcal-notch sulcus parentage was left implicit

- Issue: https://github.com/CultureBotAI/CellStructureMech/issues/1944
- Severity: medium
- Status: fixed in commit `c9ae6c44`

The initial antapex topology graph used `dinoflagellate_sulcal_notch` for the
`extends to dinoflagellate_antapex` edge and cited `GO:0097612` at record level
as the parent of GO:0097618, but it omitted the `dinoflagellate_sulcus` node and
the GO-backed `dinoflagellate_sulcal_notch is a dinoflagellate_sulcus` edge.

Fix: added the GO:0097612 sulcus node and materialized the GO:0097618 subclass
edge before the `extends to` edge in the graph.

## Post-Fix Validation

- `uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/dinoflagellate_antapex.yaml`
- `uv run python scripts/validate_strict.py --quiet data/structures/other/dinoflagellate_antapex.yaml`
- `uv run python scripts/validate_history.py history/records/dinoflagellate_antapex/2026-10-02T211309Z-codex-e0fbb3.yaml`
- `uv run --extra embeddings python scripts/build_text_embedding_map.py --refresh`
- `uv run python scripts/build_text_embedding_map.py --check`
- `uv run python scripts/render_pages.py`
- `uv run python scripts/check_docs.py --write`
- `uv run python scripts/render_pages.py --check`
- `uv run python scripts/check_docs.py --check`
- `uv run python scripts/validate_strict.py --quiet`
- `uv run python scripts/validate_history.py`
- `uv run python scripts/fetch_snippets.py --verify --check`
- `uv run python scripts/check_trait_links.py --check`
- `uv run python scripts/check_curies.py --check --report reports/curie_check.tsv`
- `uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `uv run python scripts/run_qc.py`
- `git diff --check`

All post-fix checks passed.
