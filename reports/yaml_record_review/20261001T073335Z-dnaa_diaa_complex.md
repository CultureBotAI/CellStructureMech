# DnaA-DiaA complex adversarial review

- **PR:** #1859
- **Branch:** `add-dnaa-diaa-complex`
- **Record:** `data/structures/other/dnaa_diaa_complex.yaml`
- **History:** `history/records/dnaa_diaa_complex/2026-10-01T071950Z-claude-code-d7af08.yaml`
- **Reviewer:** codex
- **Timestamp:** 2026-10-01T07:33:35Z
- **Outcome:** no blocking defects found

## Scope Reviewed

- Confirmed the candidate was novel before curation by searching with
  `rg --no-ignore --hidden` for `GO:1990102`, `DnaA-DiaA`, `DnaA DiaA`,
  `DnaA.*DiaA`, `DiaA.*DnaA`, `GO:1990125`, `DiaA complex`, and
  `DiaA homotetramer` across tracked curation/data outputs and ignored files.
- Reviewed the GO:1990102 identity choice, exact DnaA-DiaA-DNA synonym, and
  GO:1990077 primosome-complex parentage against QuickGO and OLS.
- Checked the GO:1990102 relation graph and confirmed that `GO:1990101`
  DnaA-oriC complex and `GO:1990125` DiaA complex are outgoing `has part`
  targets rather than reversed relations.
- Checked that DiaA, DnaA, and oriC DNA are not assigned guessed InterPro,
  Pfam, NCBIfam, UniProtKB, or SO identifiers and that the record carries a
  `CURATION_TODO` for exact source-neutral primitive-component grounding.
- Checked the E. coli `taxonomic_distribution` and `canonical_examples`
  assertions against Keyamura et al. 2007 and confirmed the record does not
  overgeneralize from GO's only-in-taxon Prokaryota axiom.
- Checked that the GO:1990102 DnaA-DiaA scope is distinct from GO:1990101
  DnaA-oriC, GO:1990125 DiaA homotetramer, and GO:1990100 DnaB-DnaC
  helicase-loading scopes.
- Checked that the causal graph remained nonmechanistic and used coarse,
  directly supported nodes for DiaA, DnaA, oriC DNA, the DnaA-DiaA structure,
  and DNA replication initiation.
- Checked generated fan-out in README statistics, embedding JSON, rendered
  index/category pages, the GO-grounded page, and the new rendered record page.
- Confirmed the temporary guarded mutators were deleted with `find` and an
  ignored-file-inclusive `rg --no-ignore --hidden` search.

## Findings

No concrete defects found.

## Issues

No GitHub issues were filed from this review.

## Local Validation

- `uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/dnaa_diaa_complex.yaml`
- `uv run python scripts/validate_strict.py --quiet data/structures/other/dnaa_diaa_complex.yaml`
- `uv run python scripts/validate_history.py history/records/dnaa_diaa_complex`
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
