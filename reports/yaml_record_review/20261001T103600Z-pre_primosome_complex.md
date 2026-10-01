# pre-primosome complex adversarial review

- **PR:** #1865
- **Branch:** `add-pre-primosome-complex`
- **Record:** `data/structures/other/pre_primosome_complex.yaml`
- **History:**
  - `history/records/pre_primosome_complex/2026-10-01T101103Z-codex-cca84e.yaml`
  - `history/records/pre_primosome_complex/2026-10-01T102351Z-codex-7542e3.yaml`
- **Review issue:** #1866

## Scope reviewed

- Re-ran ignored-and-hidden duplicate checks with `rg --no-ignore --hidden` for
  `GO:1990099`, `pre-primosome complex`, exact GO synonyms, `PMID:18179598`,
  and `10.1111/j.1365-2958.2007.06094.x` across `data`, `history`,
  `reports`, `pages`, `README.md`, and `.gitignore`; no standalone
  `GO:1990099` or `pre-primosome complex` record existed before this PR.
- Checked the GO:1990099 definition, exact/related synonymy, and is-a children
  reported by QuickGO against the curated identity, synonym list, and
  no-`has_part` boundary.
- Checked that QuickGO reports GO:1990099 as an is-a child of GO:1990077
  `primosome complex`.
- Checked that the generic GO:1990099 record stays primase-free while
  documenting the narrower DnaA-DnaB-DnaC and replication-restart
  preprimosomes as children, not as parts of every generic pre-primosome.
- Checked PubMed metadata for the GO-cited papers and DOI pairs used in the
  top-level evidence list.
- Checked the generated page, `pages/index.json`, GO-grounded listing, README
  statistics, and embedding artifacts were regenerated from the YAML.

## Findings

### Fixed: GO-backed E. coli taxonomic row

The first PR revision cited `GO:1990099` on the `NCBITaxon:562` taxonomic row.
GO:1990099 defines the generic pre-primosome class and its synonymy but does
not directly establish an E. coli species-level taxonomic claim.

Filed #1866 and fixed it by replacing the GO-backed row with direct
`PMID:8663105` Ng and Marians PhiX174-type E. coli preprimosome evidence. The
fix appended an in-record `FIX_REVIEW_ISSUE` curation event, added a second
issue-linked repository history record, rerendered the structure page, and
passed the full gate set again.

## Validation

- `uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/pre_primosome_complex.yaml`
- `uv run python scripts/validate_strict.py --quiet data/structures/other/pre_primosome_complex.yaml`
- `uv run python scripts/validate_history.py history/records/pre_primosome_complex`
- `uv run python scripts/build_text_embedding_map.py --refresh`
- `uv run python scripts/build_text_embedding_map.py --check`
- `uv run python scripts/render_pages.py`
- `uv run python scripts/check_docs.py --write`
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

## Result

- #1866 was the only concrete review finding and is fixed in PR #1865.
- All post-fix local gates passed.
