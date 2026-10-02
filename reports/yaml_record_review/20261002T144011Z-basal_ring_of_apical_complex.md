# Basal ring of apical complex YAML review

- PR: https://github.com/CultureBotAI/CellStructureMech/pull/1917
- Record: `data/structures/cytoskeleton/basal_ring_of_apical_complex.yaml`
- Identifier: `GO:0020032`
- Review time: 2026-10-02T14:40:11Z

## Findings

No PR-blocking defects were found.

## Checks

- Confirmed the PR diff contains one new curated record, one new history record, the new rendered page, regenerated index/page artifacts, and regenerated embedding artifacts only.
- Ran an ignored/hidden-inclusive duplicate sweep for `basal ring of apical complex`, `lower polar ring of apical complex`, `posterior polar ring of apical complex`, `preconoidal ring of apical complex`, `GO:0020032`, and the Hu et al. 2006 PMID/DOI before adding the record. No existing `data/structures/**/*.yaml` record used that GO term or those exact labels.
- Repeated ignored/hidden-inclusive PR review searches for the basal-ring label, exact synonyms, `GO:0020032`, and subpellicular-microtubule phrasing after render. Matches were limited to the new source YAML, its generated page/index artifacts, the freshly refreshed `reports/curie_check.tsv`, and neighboring apical-complex context; no duplicate basal-ring record was found.
- Checked the new basal-ring boundary against the existing `GO:0020031` anterior polar-ring record, `GO:0020007` apical-complex record, and `GO:0033289` intraconoid-microtubule record. The new record carries an explicit resolved discussion separating the lower/posterior/preconoidal ring from the anterior polar ring instead of collapsing both rings under `GO:0020031`.
- Checked that no exact basal-ring protein constituents were asserted without exact source-neutral family grounding. The first record leaves basal-ring resident proteins as an open `CURATION_TODO` and avoids broad tubulin or generic cytoskeletal groundings.
- Confirmed identifier health and labels after the new GO term was introduced: `check_curies.py --check` resolved the new `GO:0020032` CURIE, and `validate_id_label_correspondence.py` accepted `basal ring of apical complex`.

## Validation Reviewed

- `linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/cytoskeleton/basal_ring_of_apical_complex.yaml`
- `uv run python scripts/validate_strict.py --quiet data/structures/cytoskeleton/basal_ring_of_apical_complex.yaml`
- `uv run python scripts/validate_strict.py --quiet`
- `just text-embeddings-refresh`
- `just text-map-check`
- `just render`
- `just render-check`
- `just docs-stats`
- `just docs-check`
- `just validate-history history/records/basal_ring_of_apical_complex`
- `just validate-history`
- `uv run python scripts/fetch_snippets.py --verify --check`
- `uv run python scripts/check_trait_links.py --check`
- `uv run python scripts/check_curies.py --check --report reports/curie_check.tsv`
- `uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `git diff --check`
- `git diff --cached --check`
- `just qc`
