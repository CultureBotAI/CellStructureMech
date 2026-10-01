# DnaA-Dps complex adversarial review

- **PR:** #1873
- **Branch:** `add-dnaa-dps-complex`
- **Record:** `data/structures/other/dnaa_dps_complex.yaml`
- **History:**
  - `history/records/dnaa_dps_complex/2026-10-01T134250Z-codex-29d444.yaml`

## Scope Reviewed

- Ran ignored/hidden-inclusive duplicate searches with
  `rg --no-ignore --hidden` for `GO:1990084`, `DnaA-Dps complex`,
  `DnaA-Dps`, `PMID:18284581`, DOI
  `10.1111/j.1365-2958.2008.06127.x`, the Chodavarapu et al. title, adjacent
  `GO:1990082` DnaA-L2, and `GO:1990078` replication inhibiting complex
  across `data/structures`, `history/records`, `reports/yaml_record_review`,
  `pages`, `README.md`, and `.gitignore`. The pre-PR searches found no
  existing standalone `GO:1990084` or `GO:1990082` records.
- Checked QuickGO metadata for `GO:1990084`: the term is an unrestricted GO
  cellular component named `DnaA-Dps complex`, is not obsolete, and cites
  `PMID:18284581` from its GO definition.
- Checked OLS and QuickGO parentage for `GO:1990084` and confirmed it is a
  direct `is_a` child of `GO:1990078` replication inhibiting complex.
- Checked PubMed metadata for `PMID:18284581` and DOI
  `10.1111/j.1365-2958.2008.06127.x`; Chodavarapu, Gomez, Vicente and Kaguni
  2008 directly supports E. coli Dps/DnaA binding, Dps interference with DnaA
  function at the replication origin, and the E. coli taxonomic row.
- Checked the existing `GO:1990083` DnaA-Hda and `GO:1990085` Hda-beta clamp
  records to keep `GO:1990084` scoped to DnaA plus Dps rather than Hda, the
  beta clamp, or RIDA hydrolysis chemistry.
- Checked that DnaA and Dps remain `REVIEWED_LABEL_ONLY` components with no
  guessed InterPro, Pfam, NCBIfam, UniProtKB, or Complex Portal accessions.
- Checked that the graph remains `NONMECHANISTIC` and stops at GO-level
  DnaA-Dps composition supporting negative regulation of DNA replication
  initiation, without modeling Dps oligomer state, DnaA domain contacts,
  oxidative-stress signaling, or downstream adaptive mutation.

## Findings

No concrete defects found. No review issues were filed.

## Verification

- `uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/dnaa_dps_complex.yaml`
- `uv run python scripts/validate_strict.py --quiet data/structures/other/dnaa_dps_complex.yaml`
- `uv run python scripts/validate_history.py history/records/dnaa_dps_complex`
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
