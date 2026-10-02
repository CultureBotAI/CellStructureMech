# YAML Record Review: AcrAD-TolC multidrug efflux transport complex

- **PR:** #1909
- **Record:** `data/structures/other/acrad_tolc_multidrug_efflux_transport_complex.yaml`
- **Reviewer:** codex
- **Review time:** 2026-10-02T09:56:14Z
- **Scope:** Adversarial review of the `cellstructuremech:acrad_tolc_multidrug_efflux_transport_complex` record, its append-only history entry, and generated artifacts added in branch `add-acrad-tolc-multidrug-efflux-transport`.

## Outcome

No concrete defects were found. No GitHub issues were filed.

## Checks Performed

- Re-read the submitted AcrAD-TolC YAML and append-only history record after opening PR #1909.
- Rechecked hidden and ignored files for duplicate candidates matching `AcrAD`, `AcrD`, `acrD`, `CPX-4264`, `P24177`, `PMID:15743938`, and `DOI:10.1128/JB.187.6.1923-1929.2005`; no existing maintained AcrAD-TolC record or prior `CPX-4264` use was found outside this PR.
- Rechecked exact Complex Portal `CPX-4264`:
  - source label `AcrAD-TolC multidrug efflux transport complex`
  - species `Escherichia coli (strain K12); 83333`
  - systematic name `6xacrA:3xacrD:3xtolC`
  - assembly `Heterododecamer`
  - evidence code `ECO:0005547`
  - participants `P0AE06` / `acrA` x6, `P24177` / `acrD` x3, and `P02930` / `tolC` x3
  - cross-references `GO:1990281`, `GO:0042910`, `GO:0140330`, `PMID:15743938`, and `PMID:26113845`
- Rechecked active QuickGO terms:
  - `GO:1990281` is the cellular-component term `efflux pump complex`, a broader parent for this AcrAD-TolC-specific record.
  - `GO:0042910` is the molecular-function term `xenobiotic transmembrane transporter activity`.
  - `GO:0140330` is the biological-process term `xenobiotic detoxification by transmembrane export across the cell outer membrane`.
- Rechecked reviewed E. coli K-12 UniProtKB examples from exact accession JSON:
  - `P0AE06` / `ACRA_ECOLI` / `acrA` / `Multidrug efflux pump subunit AcrA`, cross-referenced to `ComplexPortal:CPX-4264`
  - `P24177` / `ACRD_ECOLI` / `acrD` / `Probable aminoglycoside efflux pump`, cross-referenced to `ComplexPortal:CPX-4264`
  - `P02930` / `TOLC_ECOLI` / `tolC` / `Outer membrane protein TolC`, cross-referenced to `ComplexPortal:CPX-4264`
- Rechecked exact InterPro `IPR058622`, which resolves to the `Outer membrane channel protein TolC` family.
- Rechecked NCBI PubMed metadata:
  - `PMID:15743938` is Murakami et al. 2005, `Aminoglycosides are captured from both periplasm and cytoplasm by the AcrD multidrug efflux transporter of Escherichia coli.`
  - the PubMed DOI article ID for `PMID:15743938` is `10.1128/JB.187.6.1923-1929.2005`
  - `PMID:26113845` is Zwama and Pos 2015, `The ins and outs of RND efflux pumps in Escherichia coli.`
  - the PubMed DOI article ID for `PMID:26113845` is `10.3389/fmicb.2015.00587`
- Ran a local YAML/source cross-check confirming:
  - the declared component gene symbols are exactly `acrA`, `acrD`, and `tolC`
  - the declared UniProtKB examples are exactly `P0AE06`, `P24177`, and `P02930`
  - the Complex Portal participants and stoichiometries are exactly `acrA` x6, `acrD` x3, and `tolC` x3
  - the Complex Portal source composition sums to 12 subunits
  - every causal-graph `component_ref` points at a declared component
  - every causal-graph edge subject and object points at a declared graph node
  - AcrA and AcrD remain `REVIEWED_LABEL_ONLY`, TolC is grounded to `InterPro:IPR058622`, and the open component-family grounding TODO is attached only to AcrA and AcrD
- Confirmed hidden and ignored files were included when checking `scripts/` for `curate_acrad`, `acrad_tolc`, and `CPX-4264`; no temporary mutator remains.
- Confirmed generated pages and embedding indexes reference the new `cellstructuremech:acrad_tolc_multidrug_efflux_transport_complex` identifier and page.
- Confirmed the PR changed exactly the new record, the new history file, generated embedding JSON, generated static site files, and the README corpus summary before this review report was added.

## Validation Reviewed

- `PATH=.venv/bin:$PATH linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/acrad_tolc_multidrug_efflux_transport_complex.yaml`
- `scripts/validate_strict.py --quiet data/structures/other/acrad_tolc_multidrug_efflux_transport_complex.yaml`
- `scripts/validate_history.py history/records/acrad_tolc_multidrug_efflux_transport_complex/2026-10-02T093931Z-codex-cdb670.yaml`
- local component/Complex Portal/UniProt/QuickGO/InterPro/PubMed/graph consistency cross-checks
- `scripts/build_text_embedding_map.py --refresh`
- `scripts/render_pages.py`
- `PATH=.venv/bin:$PATH .venv/bin/python scripts/run_qc.py`
- `git diff --check`

## Issues Filed

None.
