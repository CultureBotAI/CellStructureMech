# YAML Record Review: EmrAB-TolC multidrug efflux transport complex

## Scope

- Reviewed PR #1910 after it was opened.
- Confirmed the PR head is `99a028922ba5425e8590e25c0128ff19c8e60e84` on
  `add-emrab-tolc-multidrug-efflux-transport`.
- Confirmed `gh pr diff 1910 --name-only` contains exactly the expected 13
  files: the new YAML record, one append-only history record, README statistics,
  three text-embedding artifacts, and six rendered page/index artifacts plus
  the new structure page.

## Duplicate And Residue Checks

- Re-ran a hidden- and ignored-inclusive sweep for `EmrAB`, `EmrA`, `EmrB`,
  `emrA`, `emrB`, `CPX-4268`, `P27303`, `P0AEJ0`, `8ZAL`, `PMID:33065135`,
  `PMID:41839863`, `DOI:10.1016/j.bbamem.2020.183488`, and
  `DOI:10.1038/s41467-026-70500-5` under `data`, `history`, `pages`, `reports`,
  `scripts`, `docs`, `src`, `curation`, `research`, and `.github`.
- The duplicate sweep found only the expected new EmrAB-TolC record, history
  record, rendered page/index/embedding entries, and the transient
  `reports/curie_check.tsv` rows emitted by CURIE validation.
- Re-ran a hidden- and ignored-inclusive `scripts/` sweep for `curate_emrab`,
  `emrab_tolc`, and `CPX-4268`; no temporary mutator remains.

## Source Cross-Checks

- Rechecked exact Complex Portal `CPX-4268`:
  - source label `EmrAB-TolC multidrug efflux transport system`
  - species `Escherichia coli (strain K12); 83333`
  - assembly `Heterodecamer`
  - participants `P27303` / `emrA` / `Multidrug export protein EmrA` at 6 copies
    with source interactor `EBI-21407298`
  - participants `P0AEJ0` / `emrB` / `Multidrug export protein EmrB` at 1 copy
    with source interactor `EBI-21407257`
  - participants `P02930` / `tolC` / `Outer membrane protein TolC` at 3 copies
    with source interactor `EBI-21407260`
  - cross-referenced `GO:1990281`, `GO:0042910`, and `GO:0140330`
- Rechecked QuickGO for `EmrAB-TolC`; no exact EmrAB-TolC cellular-component
  term was returned, so the minted identifier under broader `GO:1990281` is
  appropriate.
- Rechecked UniProt:
  - `P27303` is reviewed `EMRA_ECOLI`, gene `emrA`, in taxon `83333`, and
    cross-references `CPX-4268` and `PDB:8ZAL`
  - `P0AEJ0` is reviewed `EMRB_ECOLI`, gene `emrB`, in taxon `83333`, and
    cross-references `CPX-4268` and `PDB:8ZAL`
  - `P02930` is reviewed `TOLC_ECOLI`, gene `tolC`, in taxon `83333`, and
    cross-references `CPX-4268` and `PDB:8ZAL`
- Rechecked InterPro:
  - `IPR004638` is the family `Drug resistance transporter EmrB-like`
  - `IPR058622` is the family `Outer membrane channel protein TolC`
  - broader EmrA/FarA domain or membrane-fusion entries remain intentionally
    unused, with EmrA left `REVIEWED_LABEL_ONLY`
- Rechecked RCSB `PDB:8ZAL` as a released electron-microscopy entry titled
  `EmrAB-TolC MFS-type tripartite multidrug efflux pump EA`, with 10 deposited
  protein-chain instances and primary citation `PMID:41839863` /
  `DOI:10.1038/s41467-026-70500-5`.
- Rechecked PubMed titles and DOIs for `PMID:33065135`, `PMID:12482849`, and
  `PMID:41839863`; they match the evidence notes committed in the YAML.

## Validation

- Local `scripts/run_qc.py` passed before the first PR commit.
- The targeted single-record LinkML and strict validators passed.
- All 799 records passed closed-schema validation.
- All 1433 history records passed history validation.
- README, rendered pages, and the text-embedding map all passed drift checks.
- `git diff --check` passed.

## Findings

No concrete record defects were found. No GitHub issues were filed.
