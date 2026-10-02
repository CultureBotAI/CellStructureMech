# MdtABC-TolC multidrug efflux transport complex YAML review

## Scope

- **PR:** #1912
- **Reviewed head:** `15224915fd0e7bc5acc03da6385c1d791664f9e7`
- **Reviewed record:** `data/structures/other/mdtabc_tolc_multidrug_efflux_transport_complex.yaml`
- **History record:** `history/records/mdtabc_tolc_multidrug_efflux_transport_complex/2026-10-02T112319Z-codex-80284d.yaml`
- **Complex Portal source:** `ComplexPortal:CPX-2119`

## Duplicate and Residue Checks

Before creation, a hidden/ignored-inclusive sweep across `data`, `history`,
`pages`, `reports`, `scripts`, `docs`, `src`, `curation`, `research`, and
`.github` for `MdtABC`, `MdtABC-TolC`, `MdtA`, `MdtB`, `MdtC`, `mdtA`,
`mdtB`, `mdtC`, `CPX-2119`, `P76397`, `P76398`, `P76399`, and the MdtABC
component labels found the existing `GO:1990203` MdtBC subcomplex and its
generated review artifacts but no exact preexisting MdtABC-TolC or CPX-2119
record.

The post-PR hidden/ignored-inclusive sweep found the expected new
MdtABC-TolC record, rendered page, embedding/index rows, and history record
alongside the existing MdtBC subcomplex. A hidden/ignored-inclusive
`scripts/` sweep for `curate_mdtabc`, `mdtabc_tolc`, and `CPX-2119` found no
temporary mutator residue.

## Authority Rechecks

- `gh pr diff 1912 --name-only` reported the expected 13 files: the new YAML
  record, its history record, the new rendered detail page, regenerated
  browse/index/category pages, README statistics, and the committed embedding
  JSON mirrors.
- The GitHub REST PR metadata reported head
  `15224915fd0e7bc5acc03da6385c1d791664f9e7`, matching the local commit
  reviewed here.
- QuickGO search for `MdtABC` returned zero hits. QuickGO search for
  `MdtABC-TolC` returned fuzzy `MacAB-TolC`/macrolide hits only, not an exact
  MdtABC or MdtABC-TolC cellular-component term. Minting
  `cellstructuremech:mdtabc_tolc_multidrug_efflux_transport_complex` under
  `GO:1990281` is therefore scoped correctly.
- QuickGO resolved active terms:
  - `GO:1990281` `efflux pump complex`
  - `GO:0042910` `xenobiotic transmembrane transporter activity`
  - `GO:0140330` `xenobiotic detoxification by transmembrane export across the cell outer membrane`
- `ComplexPortal:CPX-2119` resolved through
  `https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-2119` and rechecked:
  - primary accession `CPX-2119`
  - label `MdtABC-TolC multidrug efflux transport complex`
  - systematic name `mdtA:2xmdtB:mdtC:3xtolC`
  - source taxon `Escherichia coli (strain K12); 83333`
  - evidence code `ECO:0005547`
  - GO cross-references `GO:1990281`, `GO:0042910`, `GO:0140330`, and `GO:0098567`
  - participants `P76399/mdtC` with stoichiometry 1, `P76397/mdtA` with no
    asserted stoichiometry, `P76398/mdtB` with stoichiometry 2, and
    `P02930/tolC` with stoichiometry 3
  - literature cross-references `PMID:12107133`, `PMID:20038594`, and
    `PMID:26113845`
- UniProtKB REST reported reviewed E. coli K-12 entries:
  - `P76397` / `MDTA_ECOLI` / `mdtA` / `Multidrug resistance protein MdtA`,
    cross-referenced to `ComplexPortal:CPX-2119` and `InterPro:IPR022824`
  - `P76398` / `MDTB_ECOLI` / `mdtB` / `Multidrug resistance protein MdtB`,
    cross-referenced to `ComplexPortal:CPX-2119` and `InterPro:IPR022831`
  - `P76399` / `MDTC_ECOLI` / `mdtC` / `Multidrug resistance protein MdtC`,
    cross-referenced to `ComplexPortal:CPX-2119` and `InterPro:IPR023931`
  - `P02930` / `TOLC_ECOLI` / `tolC` / `Outer membrane protein TolC`,
    cross-referenced to `ComplexPortal:CPX-2119` and `InterPro:IPR058622`
- InterPro resolved exact family entries:
  - `IPR022824` `Multidrug resistance protein MdtA`
  - `IPR022831` `Multidrug resistance protein MdtB`
  - `IPR023931` `Multidrug resistance protein MdtC`
  - `IPR058622` `Outer membrane channel protein TolC`
- PubMed ESummary verified:
  - `PMID:12107133`, DOI `10.1128/JB.184.15.4161-4167.2002`, title
    `The putative response regulator BaeR stimulates multidrug resistance of Escherichia coli via a novel multidrug exporter system, MdtABC.`
  - `PMID:20038594`, DOI `10.1128/JB.01448-09`, title
    `Multidrug efflux pump MdtBC of Escherichia coli is active only as a B2C heterotrimer.`
  - `PMID:26113845`, DOI `10.3389/fmicb.2015.00587`, title
    `The ins and outs of RND efflux pumps in Escherichia coli.`
- A structured assertion pass compared the YAML against the CPX-2119,
  UniProtKB, QuickGO, InterPro, and PubMed authority payloads; all assertions
  passed.

## Record Review

- The record mints a local `cellstructuremech:` identifier because QuickGO has
  no exact MdtABC-TolC cellular-component term and uses the broader
  `GO:1990281` efflux-pump cellular-component term as `parent_structures`.
- The whole CPX-2119 pump is modeled separately from the existing `GO:1990203`
  MdtBC inner-membrane subcomplex.
- The curated component rows use exact source-neutral InterPro family
  groundings for MdtA, MdtB, MdtC, and TolC; no reviewed-label-only fallback or
  grounding TODO was required.
- The `complex_compositions` row preserves the CPX-2119 participant order,
  participant accessions, interactor IDs, source taxon, evidence code, and
  asserted copy numbers.
- MdtA intentionally has no curated stoichiometry in either `components` or
  `complex_compositions` because the CPX-2119 participant record itself omits
  a `stochiometry` value.
- The definition and function text keep the CPX-2119 zinc substrate in the
  substrate list without representing zinc as a xenobiotic.
- The compact function graph keeps the MdtABC-TolC boundary and outer-membrane
  export function evidence-backed without pretending to resolve RND conformer
  cycling or TolC gate opening.

## Validation

Local validation before review passed:

- `linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/mdtabc_tolc_multidrug_efflux_transport_complex.yaml`
- `scripts/validate_strict.py --quiet data/structures/other/mdtabc_tolc_multidrug_efflux_transport_complex.yaml`: 1 file, 0 errors
- `scripts/validate_strict.py --quiet`: 801 files, 0 errors
- `scripts/validate_history.py history/records/mdtabc_tolc_multidrug_efflux_transport_complex`: 1 history record valid
- `scripts/validate_history.py`: 1435 history records, 0 invalid
- `scripts/build_text_embedding_map.py --refresh`
- `scripts/build_text_embedding_map.py --check`: 801 records, 384 dimensions
- `scripts/render_pages.py --check`: current
- `scripts/check_docs.py --check`: current
- `scripts/fetch_snippets.py --verify --check`: 31 snippets not checked because no route answered; 0 failures
- `scripts/check_trait_links.py --check`: 10 resolve with a matching label
- `scripts/check_curies.py --check --report reports/curie_check.tsv`: OK 3097, UNREACHABLE 278, SKIPPED 145
- `scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`: OK_CANONICAL 3309, OK_SYNONYM 48, OK_EXCEPTION 8, SKIPPED_NO_ADAPTER 370
- `git diff --check`
- `scripts/run_qc.py`: 567 passed, 3 skipped, 2 warnings; all quality gates passed

The substrate wording refinement was followed by record validation,
embedding/page/docs regeneration, check-mode artifact validation, `git diff
--check`, and a second full `scripts/run_qc.py`, which again passed all
quality gates.

## Issues

No concrete defects were found, so no GitHub issues were filed.
