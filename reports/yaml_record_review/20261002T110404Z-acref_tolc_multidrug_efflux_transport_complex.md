# YAML Record Review: AcrEF-TolC multidrug efflux transport complex

Review timestamp: 2026-10-02T11:04:04Z

Pull request: #1911

Reviewed head:
`3d702955ff7baddc36a810ac13e5df9e7d9071ef`

## Scope

- Re-read the submitted AcrEF-TolC YAML and append-only history record after
  opening PR #1911.
- Confirmed the GitHub PR head SHA matched the reviewed local commit.
- Confirmed the PR diff contains only the new AcrEF-TolC record, its history
  record, refreshed embedding artifacts, refreshed README corpus statistics, and
  regenerated pages.
- Rechecked hidden and ignored files for duplicate candidates matching `AcrEF`,
  `AcrE`, `AcrF`, `acrE`, `acrF`, `CPX-4265`, `P24180`, `P24181`,
  `PMID:30880703`, and `DOI:10.4103/ijmm.IJMM_18_308`.
  The sweep found only the expected new record, generated pages, generated
  embeddings, the new history record, and transient rows in
  `reports/curie_check.tsv`; no pre-existing maintained AcrEF-TolC record or
  CPX-4265 evidence use was present.
- Rechecked hidden and ignored files under `scripts/` with both `find` and `rg`;
  no temporary AcrEF mutator remained.

## Authority Checks

- Resolved `ComplexPortal:CPX-4265` through
  `https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-4265` and rechecked:
  - primary accession `CPX-4265`
  - source label `AcrEF-TolC multidrug efflux transport complex`
  - systematic name `acrE:acrF:3xtolC`
  - source species `Escherichia coli (strain K12); 83333`
  - evidence `ECO:0005547`
  - participants:
    - `P24180` / `acrE` / `Multidrug export protein AcrE`
    - `P24181` / `acrF` / `Multidrug export protein AcrF`
    - `P02930` / `tolC` / `Outer membrane protein TolC` with stoichiometry
      `minValue: 3, maxValue: 3`
  - cross-references to `GO:1990281`, `GO:0042910`, `GO:0140330`,
    `PMID:30880703`, and `PMID:26113845`
- Rechecked QuickGO:
  - `AcrEF` search returned no exact AcrEF-TolC cellular-component term.
  - `AcrEF-TolC` search returned only `GO:1990196` MacAB-TolC complex and its
    broader macrolide-transporter parent, not an exact AcrEF-TolC term.
  - `GO:1990281` is the cellular-component term `efflux pump complex`, a
    broader parent for this minted AcrEF-TolC record.
  - `GO:0042910` is `xenobiotic transmembrane transporter activity`.
  - `GO:0140330` is `xenobiotic detoxification by transmembrane export across
    the cell outer membrane`.
- Rechecked reviewed UniProtKB records:
  - `P24180` / `ACRE_ECOLI` / `acrE` / `Multidrug export protein AcrE`,
    taxon `83333`, cross-referenced to `ComplexPortal:CPX-4265`
  - `P24181` / `ACRF_ECOLI` / `acrF` / `Multidrug export protein AcrF`,
    taxon `83333`, cross-referenced to `ComplexPortal:CPX-4265`
  - `P02930` / `TOLC_ECOLI` / `tolC` / `Outer membrane protein TolC`,
    taxon `83333`, cross-referenced to `ComplexPortal:CPX-4265`
- Rechecked InterPro `IPR058622`; it resolves to the exact
  `Outer membrane channel protein TolC` family.
- Rechecked PubMed:
  - `PMID:30880703` has DOI `10.4103/ijmm.IJMM_18_308` and title
    `Transcriptional response of AcrEF-TolC against fluoroquinolone and
    carbapenem in Escherichia coli of clinical origin.`
  - `PMID:26113845` has DOI `10.3389/fmicb.2015.00587` and title
    `The ins and outs of RND efflux pumps in Escherichia coli.`
- Ran a structured assertion pass comparing the YAML against the CPX-4265,
  UniProtKB, QuickGO, InterPro, and PubMed authority payloads; all assertions
  passed.

## Boundary Review

- `cellstructuremech:acref_tolc_multidrug_efflux_transport_complex` is minted
  correctly: GO has a broad efflux-pump term but no exact AcrEF-TolC cellular
  component.
- The three component rows match the three Complex Portal participants.
- AcrE and AcrF remain `REVIEWED_LABEL_ONLY` because their UniProt records have
  broader or domain-level InterPro/Pfam entries, but no exact source-neutral
  AcrE or AcrF family was verified.
- TolC is grounded to the exact `InterPro:IPR058622` family.
- Only TolC has asserted stoichiometry because CPX-4265 supplies a copy number
  for TolC but not for AcrE or AcrF.
- The `complex_compositions` entry preserves the exact source accession, source
  interactor IDs, taxon, and participant copy numbers supplied by CPX-4265.
- The function graph stays at nonmechanistic whole-complex scope and does not
  claim unverified AcrF transport states, substrate-binding sites, or TolC
  opening mechanics.
- The history record points at the new YAML target and is append-only.

## Validation Re-run

- Single-record LinkML validation passed.
- Single-record strict validation passed.
- Single-record history validation passed.
- Full strict validation passed for 800 structure records.
- Full history validation passed for 1,434 history records.
- Snippet verification reported 31 unchecked snippets because no fetch route
  answered and 0 verbatim mismatches.
- TraitMech link verification passed: 10 links resolved with matching labels.
- CURIE liveness passed for every reachable identifier.
- id-label correspondence passed.
- `git diff --check` passed.
- `scripts/run_qc.py` passed: 567 tests passed, 3 skipped, 2 dependency
  warnings, and all local CellStructureMech quality gates passed.

## Findings

No concrete defects were found. No GitHub issues were filed.
