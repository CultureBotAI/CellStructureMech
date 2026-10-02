# Adversarial YAML Record Review: glutamate synthase complex (NADPH)

- PR: #1898
- Branch: `add-glutamate-synthase-complex`
- Commit reviewed: `b2586962`
- Record: `data/structures/other/glutamate_synthase_complex_nadph.yaml`
- Identifier: `GO:0009342`

## Scope

Reviewed the PR diff adding the GO-backed NADPH glutamate synthase complex record, one append-only history record, regenerated embedding artifacts, regenerated HTML pages, regenerated page JSON, and the refreshed README corpus block.

## Evidence And Grounding

- `GO:0009342` exactly scopes the record to the NADPH glutamate synthase complex rather than the broader `GO:0031026` generic glutamate synthase complex.
- `GO:0031026` is the sole direct GO parent reported by OLS4 for `GO:0009342`.
- `GO:0004355` exactly denotes glutamate synthase (NADPH) activity and QuickGO links `GO:0009342` to it through `capable_of`.
- `UniProtKB:P09831` and `UniProtKB:P09832` are reviewed E. coli K-12 GltB and GltD accessions.
- `ComplexPortal:CPX-5041` is the E. coli K-12 Glutamate synthase [NADPH] complex and lists `P09831`, `P09832`, and one `CHEBI:49883` 4Fe-4S cofactor participant.
- Both GltB and GltD remain `REVIEWED_LABEL_ONLY`; `InterPro:IPR006006` was reviewed but not used as exact grounding because it also covers AegA/UacF relatives.

## Duplicate Search

Ran hidden/ignored-inclusive `rg --no-ignore --hidden` searches for `GO:0009342`, `GO:0031026`, the exact label, Complex Portal synonyms, GOGAT aliases, `CPX-5041`, Glt gene symbols, reviewed UniProt examples, the 4Fe-4S ChEBI identifier, primary PMIDs, and DOI values across `data`, `history`, `pages`, `reports`, `scripts`, `docs`, `src`, `curation`, `research`, and `.github`.

The only post-generation matches for glutamate-synthase-specific terms were the new record, its generated pages/embedding artifacts, the new append-only history record, and this review report.

## Generated Artifacts

- `data/embeddings/structure_text_embeddings.json`
- `data/embeddings/structure_text_map.json`
- `data/embeddings/structure_text_neighbors.json`
- `pages/data/structure_text_map.json`
- `pages/data/structure_text_neighbors.json`
- `pages/structures/other/glutamate_synthase_complex_nadph.html`
- Browse, category, grounded, index, and README corpus-stat outputs

The rendered page includes both reviewed-label-only constituents, both organism-specific UniProt examples, the CPX-5041 source-composition table, the E. coli K-12 canonical example, the NADPH activity, the open GltB/GltD grounding TODO, and all top-level DOI/PMID/database evidence.

## Local Gates

- `linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/glutamate_synthase_complex_nadph.yaml`
- `scripts/validate_strict.py --quiet data/structures/other/glutamate_synthase_complex_nadph.yaml`
- `scripts/build_text_embedding_map.py --refresh`
- `scripts/build_text_embedding_map.py --check`
- `scripts/render_pages.py`
- `scripts/check_docs.py --write`
- `scripts/render_pages.py --check`
- `scripts/check_docs.py --check`
- `scripts/validate_history.py history/records/glutamate_synthase_complex_nadph/2026-10-02T034627Z-codex-7a82df.yaml`
- `scripts/validate_strict.py --quiet`
- `scripts/validate_history.py`
- `scripts/fetch_snippets.py --verify --check`
- `scripts/check_trait_links.py --check`
- `scripts/check_curies.py --check --report reports/curie_check.tsv`
- `scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `scripts/run_qc.py`
- `git diff --check`

## Findings

No concrete defects found.
