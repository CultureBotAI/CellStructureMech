# DnaB-DnaC-Rep-PriC complex adversarial review

- **PR:** #1862
- **Branch:** `add-dnab-dnac-rep-pric-complex`
- **Record:** `data/structures/other/dnab_dnac_rep_pric_complex.yaml`
- **History:** `history/records/dnab_dnac_rep_pric_complex/2026-10-01T084756Z-codex-f773a2.yaml`
- **Reviewer:** codex
- **Timestamp:** 2026-10-01T09:01:42Z
- **Outcome:** no blocking defects found

## Scope Reviewed

- Confirmed the candidate was novel before curation by searching with
  `rg --no-ignore --hidden` for `GO:1990160`,
  `DnaB-DnaC-Rep-PriC`, `Rep-PriC`, and `Rep and PriC` across tracked
  curation/data outputs and ignored files.
- Reviewed the GO:1990160 identity choice, exact
  `DnaB-DnaC-Rep-PriC preprimosome` synonym, and related
  `phi-X174-type preprimosome` synonym against QuickGO.
- Checked that QuickGO reports GO:1990160 as an is-a child of GO:1990099
  `pre-primosome complex`.
- Checked that the GO:1990160 definition names DnaB-DnaC, Rep, PriC, and
  associated DNA, matching the curated constituents and the GO:1990100
  `has_part` assertion.
- Checked the GO:1990158 and GO:1990159 sibling boundaries so PriA, PriB, DnaT,
  and DnaG stay out of this Rep/PriC-scoped record.
- Checked that Rep, PriC, and primosome assembly site DNA are not assigned
  guessed InterPro, Pfam, NCBIfam, UniProtKB, or SO identifiers and that the
  record carries a `CURATION_TODO` for exact source-neutral groundings.
- Checked the E. coli `taxonomic_distribution` and `canonical_examples`
  assertions against Guy et al. 2009 and the GO:1990160 evidence pattern.
- Checked that the causal graph remained nonmechanistic and used coarse,
  directly supported nodes for the DnaB-DnaC subcomplex, Rep, PriC,
  primosome assembly site DNA, the GO:1990160 complex, and primosome assembly.
- Checked generated fan-out in README statistics, embedding JSON, rendered
  index/category pages, the GO-grounded page, and the new rendered record page.
- Confirmed the temporary guarded mutator was deleted with `find` and an
  ignored-file-inclusive `rg --no-ignore --hidden` search.

## Findings

No concrete defects found.

## Issues

No GitHub issues were filed from this review.

## Local Validation

- `uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/dnab_dnac_rep_pric_complex.yaml`
- `uv run python scripts/validate_strict.py --quiet data/structures/other/dnab_dnac_rep_pric_complex.yaml`
- `uv run python scripts/validate_history.py history/records/dnab_dnac_rep_pric_complex`
- `uv run python scripts/build_text_embedding_map.py --refresh`
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
- `git diff --check`
- `just qc`
