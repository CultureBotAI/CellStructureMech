# DnaA-HU complex adversarial review

- **PR:** #1867
- **Branch:** `add-dnaa-hu-complex`
- **Record:** `data/structures/other/dnaa_hu_complex.yaml`
- **History:**
  - `history/records/dnaa_hu_complex/2026-10-01T105354Z-codex-db5dfa.yaml`
  - `history/records/dnaa_hu_complex/2026-10-01T110835Z-codex-6776c2.yaml`

## Review

- Ran an ignored/hidden-inclusive duplicate search for `GO:1990103`,
  `DnaA-HU`, `DnaA HU`, `DnaA-HU-DNA`, `HU-DnaA`, and adjacent DnaA/HU
  phrases across `data/structures`, `history/records`,
  `reports/yaml_record_review`, `pages`, `README.md`, and `.gitignore`.
  The search found no existing `GO:1990103` or `DnaA-HU complex` record; the
  only pre-existing hits were incidental references to Chodavarapu et al. 2008
  in adjacent rendered DnaA/pre-primosome material.
- Checked QuickGO metadata for `GO:1990103`: the term is an unrestricted
  cellular-component `DnaA-HU complex`, carries exact synonym `DnaA-HU-DNA
  complex`, is an is-a child of `GO:1990077` primosome complex, and cites
  `PMID:18179598`.
- Checked that `GO:1990077` lists `GO:1990103` as a primosome-complex child
  alongside the already curated `GO:1990101` DnaA-oriC and `GO:1990102`
  DnaA-DiaA siblings.
- Checked PubMed metadata for `PMID:18179598` and DOI
  `10.1111/j.1365-2958.2007.06094.x`; the paper title directly scopes the
  E. coli canonical example and taxonomic row to DnaA/HU at the E. coli
  replication origin.
- Checked that DnaA, HU, and oriC are left as `REVIEWED_LABEL_ONLY`
  components with no guessed InterPro, Pfam, NCBIfam, UniProtKB, or SO
  accessions.
- Checked that the graph remains `NONMECHANISTIC` and stops at the GO-level
  DnaA/HU/oriC complex supporting replication initiation instead of expanding
  into adjacent DiaA, DnaA oligomerization, or DnaB-DnaC helicase loading
  mechanisms.

## Issues

### Fixed: unsupported DNA-bending mechanism in graph scope

The first PR revision mentioned `DNA bending` in `causal_graphs[].scope_notes`.
The curated record only cited `GO:1990103` plus Chodavarapu et al. PubMed/DOI
metadata, which support the DnaA-HU-DNA complex boundary and replication
initiation scope but do not directly establish HU DNA bending as a mechanism
inside the record.

Filed #1868 and fixed it by removing the DNA-bending phrase from the
nonmechanistic graph scope while preserving the supported DnaA-HU-DNA boundary
and adjacent-complex exclusions.

## Verification

- `uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/dnaa_hu_complex.yaml`
- `uv run python scripts/validate_strict.py --quiet data/structures/other/dnaa_hu_complex.yaml`
- `uv run python scripts/validate_history.py history/records/dnaa_hu_complex`
- `uv run python scripts/build_text_embedding_map.py --check`
- `uv run python scripts/render_pages.py --check`
- `uv run python scripts/check_docs.py --check`
- `uv run pytest tests/test_corpus_integrity.py::test_discussion_anchors_resolve`
- `uv run python scripts/validate_strict.py --quiet`
- `uv run python scripts/validate_history.py`
- `uv run python scripts/fetch_snippets.py --verify --check`
- `uv run python scripts/check_trait_links.py --check`
- `uv run python scripts/check_curies.py --check --report reports/curie_check.tsv`
- `uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `git diff --check`
- `just qc`
