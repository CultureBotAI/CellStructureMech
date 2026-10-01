# DnaA-oriC complex adversarial review

- **PR:** #1857
- **Branch:** `add-dnaa-oric-complex`
- **Record:** `data/structures/other/dnaa_oric_complex.yaml`
- **Initial history:** `history/records/dnaa_oric_complex/2026-10-01T062311Z-claude-code-cdd913.yaml`
- **Review-fix history:** `history/records/dnaa_oric_complex/2026-10-01T065917Z-claude-code-18d432.yaml`
- **Reviewer:** codex
- **Timestamp:** 2026-10-01T07:00:05Z
- **Outcome:** one concrete defect found and fixed

## Scope Reviewed

- Confirmed the candidate was novel before curation by searching with
  `rg --no-ignore --hidden` for `GO:1990101`, `DnaA-oriC`, `DnaA-DNA complex`,
  PMID `19833870`, and adjacent DnaA initiation-complex identifiers across
  tracked curation/data outputs and ignored files.
- Reviewed the GO:1990101 identity choice, GO:1990077 primosome-complex
  parentage, GO:1990102 DnaA-DiaA boundary, and GO:1990100 DnaB-DnaC boundary
  against Gene Ontology and the newly added DnaB-DnaC family of records.
- Checked that DnaA and oriC origin DNA are not assigned guessed InterPro,
  Pfam, NCBIfam, UniProtKB, or SO identifiers and that the record carries a
  `CURATION_TODO` for exact source-neutral component grounding.
- Checked that the Escherichia coli `taxonomic_distribution` and
  `canonical_examples` assertions cite PMID:19833870 directly, not GO, and do
  not overgeneralize from GO's only-in-taxon Prokaryota axiom.
- Checked that the causal graph remained nonmechanistic and used coarse,
  directly supported nodes for DnaA binding, oriC recognition, and DNA
  replication initiation.
- Checked generated fan-out in README statistics, embedding JSON, rendered
  index/category pages, the GO-grounded page, and the new rendered record page.
- Confirmed all temporary guarded DnaA-oriC mutators were deleted with `find`
  and an ignored-file-inclusive `rg --no-ignore --hidden` search.

## Findings

### Unsupported HU/IHF/Fis boundary names

- **Issue:** #1858
- **Severity:** medium
- **Status:** fixed by `176a1005`

The first revision named HU, IHF, and Fis in `causal_graphs[].scope_notes`,
`discussions[].prompt`, and `discussions[].resolution_note` even though the
record only carried direct GO/PubMed evidence for GO:1990101 itself plus the
separate GO:1990102 DnaA-DiaA and GO:1990100 DnaB-DnaC boundary calls.

The fix narrowed the text to exclude only DiaA and DnaB-DnaC. It left
ATP-DnaA oligomerization and origin unwinding as out-of-scope mechanistic
detail because those are process steps rather than named HU/IHF/Fis factors.

## Issues

- https://github.com/CultureBotAI/CellStructureMech/issues/1858

## Local Validation

- `uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/dnaa_oric_complex.yaml`
- `uv run python scripts/validate_strict.py --quiet data/structures/other/dnaa_oric_complex.yaml`
- `uv run python scripts/validate_history.py history/records/dnaa_oric_complex`
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
