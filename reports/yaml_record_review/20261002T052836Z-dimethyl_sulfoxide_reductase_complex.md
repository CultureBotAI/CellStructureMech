# YAML Record Review: dimethyl sulfoxide reductase complex

- **PR:** #1902
- **Record:** `data/structures/energy_complex/dimethyl_sulfoxide_reductase_complex.yaml`
- **Reviewer:** codex
- **Review time:** 2026-10-02T05:28:36Z
- **Scope:** Adversarial review of the GO:0009390 dimethyl sulfoxide reductase complex record, its history entry, and generated artifacts added in branch `add-dmso-reductase-complex`.

## Outcome

No concrete defects found.

## Checks Performed

- Re-read the submitted dimethyl sulfoxide reductase complex YAML and history record after opening PR #1902.
- Rechecked the record boundary against active GO terms:
  - `GO:0009390` is the exact dimethyl sulfoxide reductase complex cellular-component term.
  - `GO:0009389` is the exact dimethyl sulfoxide reductase activity molecular-function term.
  - `GO:0032991` is the direct generic GO parent for protein-containing complexes.
  - `GO:0009390` carries exact synonym `dimethyl sulphoxide reductase complex`.
- Rechecked Complex Portal `CPX-320` as the E. coli K-12 DMSO reductase complex entry:
  - primary accession `CPX-320`
  - source label `DmaABC DMSO reductase complex`, preserved only in `complex_compositions`
  - species `Escherichia coli (strain K12); 83333`
  - assembly `Heterotrimer`
  - evidence code `ECO:0000353`
  - participants `P18776`/DmsB, `P18777`/DmsC, `P18775`/DmsA, `CHEBI:60539`, and `CHEBI:49883` with copied stoichiometries
- Confirmed the source label typo-like `DmaABC` spelling was not promoted into the record label or synonyms.
- Rechecked reviewed E. coli K-12 UniProtKB examples:
  - `P18775` / `dmsA` / `Dimethyl sulfoxide reductase DmsA`
  - `P18776` / `dmsB` / `Anaerobic dimethyl sulfoxide reductase chain B`
  - `P18777` / `dmsC` / `Anaerobic dimethyl sulfoxide reductase chain C`
- Rechecked source-neutral InterPro family groundings:
  - `InterPro:IPR011888` for the DmsA/YnfE anaerobic dimethyl sulphoxide reductase subunit A family
  - `InterPro:IPR014297` for dimethylsulphoxide reductase chain B
  - `InterPro:IPR007059` for the DMSO reductase anchor subunit DmsC family
- Rechecked PubMed metadata for the literature support:
  - `PMID:21357619` / `DOI:10.1074/jbc.M110.213306`
  - `PMID:3280546` / `DOI:10.1128/jb.170.4.1505-1510.1988`
- Ran a local YAML cross-check confirming every causal-graph `component_ref` points at a declared component and the CPX-320 protein participants match the reviewed UniProt examples.
- Confirmed hidden and ignored files were included in duplicate searches for `GO:0009390`, the DMSO reductase labels, `DmsABC`, `dmsA`, `dmsB`, `dmsC`, `CPX-320`, the DmsA/DmsB/DmsC UniProt accessions and InterPro IDs, and the primary PMID/DOI values; only the new record matched after curation.
- Confirmed hidden and ignored files were included when checking that the temporary DMSO reductase mutator was removed from `scripts/`.
- Confirmed generated pages and embedding indexes reference `GO:0009390`, `CPX-320`, and the new `dimethyl_sulfoxide_reductase_complex` page.

## Validation Reviewed

- `linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/energy_complex/dimethyl_sulfoxide_reductase_complex.yaml`
- `scripts/validate_strict.py --quiet data/structures/energy_complex/dimethyl_sulfoxide_reductase_complex.yaml`
- `scripts/build_text_embedding_map.py --refresh`
- `scripts/build_text_embedding_map.py --check`
- `scripts/render_pages.py`
- `scripts/check_docs.py --write`
- `scripts/render_pages.py --check`
- `scripts/check_docs.py --check`
- `scripts/validate_history.py history/records/dimethyl_sulfoxide_reductase_complex`
- `scripts/validate_history.py`
- `scripts/validate_strict.py --quiet`
- `scripts/fetch_snippets.py --verify --check`
- `scripts/check_trait_links.py --check`
- `scripts/check_curies.py --check --report reports/curie_check.tsv`
- `scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `scripts/run_qc.py`
- `git diff --check`

## Issues Filed

None.
