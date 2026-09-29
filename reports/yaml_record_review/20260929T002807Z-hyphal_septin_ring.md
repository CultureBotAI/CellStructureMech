# Adversarial review: hyphal septin ring

- PR: https://github.com/CultureBotAI/CellStructureMech/pull/1749
- Branch: add-hyphal-septin-ring
- Head: 4a1deacda345d022ddbe26ad7f714dbd913d1eb5
- Record: `data/structures/cytoskeleton/hyphal_septin_ring.yaml`
- Reviewed: 2026-09-29T00:28:07Z

## Scope

Reviewed the new `GO:0032168` record, its generated artifacts, and the local
evidence/modeling choices made in PR #1749:

- live QuickGO identity for `GO:0032168`
- hidden/ignored-inclusive de-duplication searches for `GO:0032168`, the exact
  label, the file slug, and hyphal septin-ring synonyms
- the neighboring broad `GO:0005940` septin-ring record
- parentage against live QuickGO responses for `GO:0032168` and `GO:0005940`
- reviewed-label-only septin component scope
- topology graph and discussion evidence notes
- generated README/site/search artifacts and the repository history record

## Finding

| Severity | Finding | File |
|---|---|---|
| Major | The `hyphal_septation_site_ring` entry is a cellular localization/topology claim rather than a biological process or molecular function. `GO:0032168` is a cellular-component term that says the ring forms in the division plane within hyphae where a septum will form; the current record already captures that under the nonmechanistic topology graph. Until a direct source is curated for a septation-site scaffold or cytokinesis activity, this should not be duplicated under `functions`. | `data/structures/cytoskeleton/hyphal_septin_ring.yaml` |

## Required fix

- Remove the location-only `functions` entry.
- Keep the GO-backed future-septation-site claim in
  `causal_graphs#hyphal_septin_ring_topology`.
- Append an `ADDRESSED_REVIEW` in-record curation event and a linked repository
  history entry.
- Regenerate embeddings, pages, and docs.
- Re-run focused LinkML/strict/history checks, the full strict/history/snippet/
  trait/CURIE/id-label gates, `just qc`, and `git diff --check`.

## Validation already green before review

- `uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/cytoskeleton/hyphal_septin_ring.yaml`
- `uv run python scripts/validate_strict.py --quiet data/structures/cytoskeleton/hyphal_septin_ring.yaml`
- `uv run python scripts/validate_history.py history/records/hyphal_septin_ring`
- `uv run python scripts/build_text_embedding_map.py --check`
- `uv run python scripts/render_pages.py --check`
- `uv run python scripts/check_docs.py --check`
- `uv run python scripts/validate_strict.py --quiet`
- `uv run python scripts/validate_history.py`
- `uv run python scripts/fetch_snippets.py --verify --check`
- `uv run python scripts/check_trait_links.py --check`
- `uv run python scripts/check_curies.py --check --report reports/curie_check.tsv`
- `uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `just qc`
- `git diff --check`
