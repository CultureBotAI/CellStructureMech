# core primosome complex adversarial review

- **PR:** #1863
- **Branch:** `add-core-primosome-complex`
- **Record:** `data/structures/other/core_primosome_complex.yaml`
- **History:**
  - `history/records/core_primosome_complex/2026-10-01T092010Z-codex-b44004.yaml`
  - `history/records/core_primosome_complex/2026-10-01T094245Z-codex-ba2201.yaml`
- **Reviewer:** codex
- **Timestamp:** 2026-10-01T09:55:27Z
- **Outcome:** fixed one concrete defect

## Scope Reviewed

- Confirmed the candidate was novel before curation by searching with
  `rg --no-ignore --hidden` for `GO:1990098`, `core primosome`,
  `PMID:21856207`, `21856207`, `10.1016/j.cbpa.2011.07.016`, and
  `PMC3189269` across tracked curation/data outputs and ignored files.
- Reviewed the GO:1990098 identity choice and exact `core primosome` synonym
  against QuickGO.
- Checked that QuickGO reports GO:1990098 as an is-a descendant of GO:1990077
  `primosome complex`.
- Checked that GO:1990098 is broader than the species-specific GO:1990156
  `DnaB-DnaG complex` and that the final generic record does not assert
  GO:1990156 under `has_part`.
- Checked the GO:1990099 `pre-primosome complex` boundary so
  primase-lacking DnaB-DnaC preprimosomes remain outside this core-primosome
  record.
- Checked that the generic helicase, primase, and template-DNA components are
  not assigned guessed InterPro, Pfam, NCBIfam, UniProtKB, or SO identifiers
  and that the record carries a `CURATION_TODO` for exact source-neutral
  groundings.
- Checked the E. coli `taxonomic_distribution` and `canonical_examples`
  assertions against the open Kaguni 2011 PMC review cited by GO:1990098.
- Checked that the causal graph remained nonmechanistic and used coarse,
  directly supported nodes for the DNA helicase, primase, template DNA,
  GO:1990098 core primosome, and GO:0006269 primer synthesis.
- Checked generated fan-out in README statistics, embedding JSON, rendered
  index/category pages, the GO-grounded page, and the new rendered record page.
- Confirmed both temporary guarded mutators were deleted with `find` and an
  ignored-file-inclusive `rg --no-ignore --hidden` search.

## Findings

### Fixed: generic core primosome over-modeled DnaB-DnaG parthood

The first PR revision asserted `has_part: GO:1990156` and carried a
`DnaB-DnaG complex -> core primosome complex` graph edge on the generic
GO:1990098 record. QuickGO's relation supports the existing narrow
GO:1990156 DnaB-DnaG protein complex being part of a core primosome, but it
does not make that E. coli-specific protein subcomplex an obligatory part of
every GO:1990098 core primosome.

Filed #1864 and fixed it by removing `GO:1990156` from `has_part`, removing
the DnaB-DnaG graph node and edge, dropping the now-unneeded Mitkova/Khopde/
Biswas top-level references, narrowing the boundary discussion, and adding a
second history record linked to PR #1863 and issue #1864.

## Issues

- #1864 — GO:1990098 core primosome overstates DnaB-DnaG parthood

## Local Validation

- `uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/core_primosome_complex.yaml`
- `uv run python scripts/validate_strict.py --quiet data/structures/other/core_primosome_complex.yaml`
- `uv run python scripts/validate_history.py history/records/core_primosome_complex`
- `uv run pytest tests/test_corpus_integrity.py::test_discussion_anchors_resolve`
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
