# YAML Record Review: NarGHI complex

- **PR:** #1900
- **Record:** `data/structures/energy_complex/narghi_complex.yaml`
- **Reviewer:** codex
- **Review time:** 2026-10-02T04:33:08Z
- **Scope:** Adversarial review of the GO:0044799 NarGHI complex record, its history entry, and generated artifacts added in branch `add-narghi-complex`.

## Outcome

No concrete defects found.

## Checks Performed

- Re-read the staged NarGHI YAML and history diff after opening PR #1900.
- Rechecked the record boundary against active GO terms:
  - `GO:0009325` is the broader nitrate reductase complex.
  - `GO:0044799` is the active, exact NarGHI complex child term.
  - `GO:0044799` carries exact synonyms `cytoplasmic membrane-bound quinol-nitrate oxidoreductase` and `nitrate reductase A`.
- Rechecked `GO:0160182` as the active molecular-function term for nitrate reductase (quinone) activity.
- Rechecked Complex Portal `CPX-1974` directly through `https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-1974`:
  - primary accession `CPX-1974`
  - label `Nitrate reductase A complex`
  - species `Escherichia coli (strain K12); 83333`
  - assembly `Heterohexamer`
  - evidence code `ECO:0000353`
  - participants and stoichiometries copied into `complex_compositions`
- Rechecked reviewed UniProtKB entries:
  - `P09152` / `narG` / `Respiratory nitrate reductase 1 alpha chain`
  - `P11349` / `narH` / `Respiratory nitrate reductase 1 beta chain`
  - `P11350` / `narI` / `Respiratory nitrate reductase 1 gamma chain`
- Rechecked source-neutral family groundings:
  - `InterPro:IPR006468` for NarG
  - `InterPro:IPR006547` for NarH
  - `NCBIfam:TIGR00351` for NarI
- Confirmed the broader `InterPro:IPR003816` NarI-adjacent family was not used because its InterPro hierarchy already includes a non-NarI DsrM child family.
- Rechecked PubMed metadata for the three GO definition xrefs:
  - `PMID:11289299` / `DOI:10.1007/PL00000845`
  - `PMID:12910261` / `DOI:10.1038/nsb969`
  - `PMID:17964535` / `DOI:10.1016/j.bbamem.2007.09.002`
- Ran a local Python authority cross-check comparing the record to the cached QuickGO, Complex Portal, UniProtKB, and NCBIfam API payloads for transcribed labels, cross-references, and stoichiometries.
- Confirmed hidden and ignored files were included in duplicate searches for `GO:0044799`, `GO:0160182`, `ComplexPortal:CPX-1974`, the NarG/NarH/NarI UniProt accessions, NarG/NarH/NarI family IDs, exact synonyms, gene symbols, and primary PMID/DOI values; only the new record matched after curation.
- Confirmed the temporary NarGHI mutator was removed and that a hidden/ignored-inclusive search under `scripts/` found no remaining mutator identifiers.

## Validation Reviewed

- `linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/energy_complex/narghi_complex.yaml`
- `scripts/validate_strict.py --quiet data/structures/energy_complex/narghi_complex.yaml`
- `scripts/build_text_embedding_map.py --refresh`
- `scripts/build_text_embedding_map.py --check`
- `scripts/render_pages.py`
- `scripts/check_docs.py --write`
- `scripts/render_pages.py --check`
- `scripts/check_docs.py --check`
- `scripts/validate_history.py history/records/narghi_complex`
- `scripts/validate_strict.py --quiet`
- `scripts/validate_history.py`
- `scripts/fetch_snippets.py --verify --check`
- `scripts/check_trait_links.py --check`
- `scripts/check_curies.py --check --report reports/curie_check.tsv`
- `scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `scripts/run_qc.py`
- `git diff --check`

## Issues Filed

None.
