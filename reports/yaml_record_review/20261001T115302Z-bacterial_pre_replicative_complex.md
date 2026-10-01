# bacterial pre-replicative complex adversarial review

- **PR:** #1869
- **Branch:** `add-bacterial-pre-replicative-complex`
- **Record:** `data/structures/other/bacterial_pre_replicative_complex.yaml`
- **History:**
  - `history/records/bacterial_pre_replicative_complex/2026-10-01T113934Z-codex-e61af7.yaml`

## Scope Reviewed

- Ran an ignored/hidden-inclusive duplicate search with
  `rg --no-ignore --hidden` for `GO:0036389`, `bacterial pre-replicative
  complex`, `bacterial pre-RC`, and `pre-replicative complex` across
  `data/structures`, `history/records`, `reports/yaml_record_review`, `pages`,
  `README.md`, and `.gitignore`. The search found no pre-existing standalone
  `GO:0036389` or `bacterial pre-replicative complex` record; the only
  pre-existing structure hit was the narrower `GO:1990101` DnaA-oriC complex
  record that explicitly seeds bacterial pre-RC assembly.
- Checked the OLS record for `GO:0036389`: the term is the unrestricted GO
  cellular component `bacterial pre-replicative complex`, carries the exact
  `bacterial pre-RC` synonym, and cites `PMID:19833870` and `PMID:21035377`
  from the GO definition.
- Checked QuickGO metadata for `GO:0036387` and confirmed that
  `GO:0036389` is an `is_a` child of `GO:0036387` pre-replicative complex.
- Checked the GO scopes of `GO:1990101` DnaA-oriC, `GO:1990102` DnaA-DiaA,
  `GO:1990103` DnaA-HU, and `GO:1990100` DnaB-DnaC against the boundary
  discussion; the first is the high-affinity DnaA-oriC subcomplex and the
  others are named adjacent DiaA, HU, or helicase-loading states, not required
  parts of every generic bacterial pre-RC.
- Checked PubMed metadata for `PMID:19833870` and DOI
  `10.1073/pnas.0909472106`; the Miller et al. 2009 abstract directly supports
  the E. coli DnaA/oriC pre-RC assembly claim used for the species row and
  canonical example.
- Checked PubMed metadata for `PMID:21035377` and DOI
  `10.1016/j.mib.2010.10.001`; the Leonard and Grimwade 2010 review directly
  supports the broad DnaA-complex assembly context.
- Checked that DnaA and oriC remain `REVIEWED_LABEL_ONLY` components with no
  guessed InterPro, Pfam, NCBIfam, UniProtKB, or SO accessions.
- Checked that the graph remains `NONMECHANISTIC` and only records DnaA/oriC
  bacterial pre-RC formation, leaving DnaA oligomerization, DiaA/HU-containing
  substates, and DnaB-DnaC helicase loading out of graph edges and `has_part`.
- Checked that the PR adds one append-only history file for the new structure
  and only touches regenerated embedding, page, and documentation artifacts.

## Findings

No concrete defects found. No review issues were filed.

## Verification

- `uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/bacterial_pre_replicative_complex.yaml`
- `uv run python scripts/validate_strict.py --quiet data/structures/other/bacterial_pre_replicative_complex.yaml`
- `uv run python scripts/validate_history.py history/records/bacterial_pre_replicative_complex`
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
