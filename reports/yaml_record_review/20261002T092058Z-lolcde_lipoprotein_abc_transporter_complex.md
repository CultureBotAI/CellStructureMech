# YAML Record Review: LolCDE lipoprotein ABC transporter complex

- **PR:** #1908
- **Record:** `data/structures/other/lolcde_lipoprotein_abc_transporter_complex.yaml`
- **Reviewer:** codex
- **Review time:** 2026-10-02T09:20:58Z
- **Scope:** Adversarial review of the `cellstructuremech:lolcde_lipoprotein_abc_transporter_complex` record, its append-only history entry, and generated artifacts added in branch `add-lolcde-lipoprotein-abc-transporter`.

## Outcome

No concrete defects were found. No GitHub issues were filed.

## Checks Performed

- Re-read the submitted LolCDE YAML and append-only history record after opening PR #1908.
- Rechecked hidden and ignored files for duplicate candidates matching `LolCDE`, `lipoprotein ABC transporter`, `lipoprotein-releasing`, `CPX-4262`, `P75958`, `P0ADC3`, `P75957`, `lolC`, `lolD`, `lolE`, `PMID:10783239`, `PMID:18634750`, `DOI:10.1038/35008635`, and `DOI:10.1016/j.bbamem.2008.06.009`; no existing maintained LolCDE record or prior `CPX-4262` use was found outside this PR.
- Rechecked exact Complex Portal `CPX-4262`:
  - source label `LolCDE lipoprotein ABC transporter complex`
  - species `Escherichia coli (strain K12); 83333`
  - systematic name `lolC:2xlolD:lolE`
  - assembly `Heterotetramer`
  - evidence code `ECO:0000353`
  - participants `P0ADC3` / `lolC` x1, `P75957` / `lolD` x2, and `P75958` / `lolE` x1
  - cross-references `GO:0043190`, `GO:0042626`, `GO:0016887`, `GO:0005524`, `GO:0044874`, `PDB:7MDY`, and `PMID:18634750`
- Rechecked active QuickGO terms:
  - `GO:0043190` is the cellular-component term `ATP-binding cassette (ABC) transporter complex`, a broader parent for the LolCDE-specific CPX-4262 record.
  - `GO:0140306` is the molecular-function term `lipoprotein releasing activity`.
  - `GO:0044874` is the biological-process term `lipoprotein localization to outer membrane`.
- Rechecked reviewed E. coli K-12 UniProtKB examples from exact accession JSON:
  - `P0ADC3` / `LOLC_ECOLI` / `lolC` / `Lipoprotein-releasing system transmembrane protein LolC`, cross-referenced to `ComplexPortal:CPX-4262` and `PDB:7MDY`
  - `P75957` / `LOLD_ECOLI` / `lolD` / `Lipoprotein-releasing system ATP-binding protein LolD`, cross-referenced to `ComplexPortal:CPX-4262` and `PDB:7MDY`
  - `P75958` / `LOLE_ECOLI` / `lolE` / `Lipoprotein-releasing system transmembrane protein LolE`, cross-referenced to `ComplexPortal:CPX-4262` and `PDB:7MDY`
- Rechecked RCSB PDB metadata:
  - `PDB:7MDY` is the released electron-microscopy entry `LolCDE nucleotide-bound`
  - the primary citation DOI is `10.1038/s41467-021-24965-1`
  - the primary citation year is 2021
- Rechecked NCBI PubMed metadata:
  - `PMID:10783239` is Yakushi et al. 2000, `A new ABC transporter mediating the detachment of lipid-modified proteins from membranes.`
  - the PubMed DOI article ID for `PMID:10783239` is `10.1038/35008635`
  - `PMID:18634750` is Moussatova et al. 2008, `ATP-binding cassette transporters in Escherichia coli.`
  - the PubMed DOI article ID for `PMID:18634750` is `10.1016/j.bbamem.2008.06.009`
- Ran a local YAML/source cross-check confirming:
  - the declared component gene symbols are exactly `lolC`, `lolD`, and `lolE`
  - the declared UniProtKB examples are exactly `P0ADC3`, `P75957`, and `P75958`
  - the Complex Portal participants and stoichiometries are exactly `lolC` x1, `lolD` x2, and `lolE` x1
  - the Complex Portal source composition sums to 4 subunits
  - every causal-graph `component_ref` points at a declared component
  - every causal-graph edge subject and object points at a declared graph node
  - all three protein components remain `REVIEWED_LABEL_ONLY` and are attached to the open component-family grounding TODO
- Confirmed hidden and ignored files were included when checking `scripts/` for `curate_lolcde`, `lolcde_lipoprotein`, and `CPX-4262`; no temporary mutator remains.
- Confirmed generated pages and embedding indexes reference the new `cellstructuremech:lolcde_lipoprotein_abc_transporter_complex` identifier and page.
- Confirmed the PR changed exactly the new record, the new history file, generated embedding JSON, generated static site files, and the README corpus summary before this review report was added.

## Validation Reviewed

- `PATH=.venv/bin:$PATH linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/lolcde_lipoprotein_abc_transporter_complex.yaml`
- `scripts/validate_strict.py --quiet data/structures/other/lolcde_lipoprotein_abc_transporter_complex.yaml`
- `scripts/validate_history.py history/records/lolcde_lipoprotein_abc_transporter_complex/2026-10-02T090608Z-codex-09ebd3.yaml`
- local component/Complex Portal/UniProt/QuickGO/RCSB/PubMed/graph consistency cross-checks
- `scripts/build_text_embedding_map.py --refresh`
- `scripts/render_pages.py`
- `PATH=.venv/bin:$PATH .venv/bin/python scripts/run_qc.py`
- `git diff --check`

## Issues Filed

None.
