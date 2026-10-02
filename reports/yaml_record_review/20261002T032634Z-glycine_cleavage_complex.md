# Adversarial YAML Record Review: glycine cleavage complex

- PR: #1897
- Branch: `add-glycine-cleavage-complex`
- Commit reviewed: `6b3496e4dc7a0fa930e42c23016fd7a0a04d3d3a`
- Record: `data/structures/other/glycine_cleavage_complex.yaml`
- Identifier: `GO:0005960`

## Scope

Reviewed the PR diff adding the GO-backed glycine cleavage complex record, one append-only history record, regenerated embedding artifacts, regenerated HTML pages, regenerated page JSON, and the refreshed README corpus block.

## Evidence And Grounding

- `GO:0005960` exactly denotes the glycine cleavage complex and supplies the exact synonyms used in the record.
- `GO:1990204` and `GO:1990234` are direct GO parents for `GO:0005960`, so the oxidoreductase- and transferase-complex parentage is not inferred from reaction chemistry alone.
- `InterPro:IPR020581`, `InterPro:IPR017453`, and `InterPro:IPR006223` were used only for the P, H, and T constituents whose InterPro family labels exactly match glycine-cleavage roles.
- The shared L constituent was not forced onto broad dihydrolipoamide-dehydrogenase signatures; it remains `REVIEWED_LABEL_ONLY` with the open `resolve_l_protein_grounding` TODO.
- The reviewed UniProt examples are strain-scoped to `NCBITaxon:83333` and are cited separately from the taxon-agnostic component grounding.
- `GO:0004375` is scoped in the function description to the P-protein constituent, avoiding an overclaim that the single molecular-function term captures the full L/P/H/T multistep complex.

## Duplicate Search

Ran hidden/ignored-inclusive `rg --no-ignore --hidden` searches for the exact GO identifier, exact label, GO synonyms, gcv genes, exact InterPro families, exact UniProt examples, primary PMIDs, and DOIs across `data`, `history`, `pages`, `reports`, `scripts`, `docs`, `src`, `curation`, `research`, and `.github`.

The only post-generation matches for glycine-cleavage-specific terms were the new record, its generated pages/embedding artifacts, the new append-only history record, and this review report. Pre-existing hits for `GO:1990204` and `GO:1990234` were shared parent references in older complex records.

## Generated Artifacts

- `data/embeddings/structure_text_embeddings.json`
- `data/embeddings/structure_text_map.json`
- `data/embeddings/structure_text_neighbors.json`
- `pages/data/structure_text_map.json`
- `pages/data/structure_text_neighbors.json`
- `pages/structures/other/glycine_cleavage_complex.html`
- Browse, category, grounded, index, and README corpus-stat outputs

The rendered page includes all four constituents, all organism-specific protein examples, the E. coli K-12 canonical example, the P-protein function, the open L-protein grounding TODO, and all top-level DOI/PMID/database evidence.

## Local Gates

- `linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/glycine_cleavage_complex.yaml`
- `scripts/validate_strict.py --quiet data/structures/other/glycine_cleavage_complex.yaml`
- `scripts/build_text_embedding_map.py --refresh`
- `scripts/build_text_embedding_map.py --check`
- `scripts/render_pages.py`
- `scripts/check_docs.py --write`
- `scripts/render_pages.py --check`
- `scripts/check_docs.py --check`
- `scripts/validate_history.py history/records/glycine_cleavage_complex/2026-10-02T031439Z-codex-a56ef2.yaml`
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
