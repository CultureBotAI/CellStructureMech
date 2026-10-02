# YAML Record Review: EmrKY-TolC multidrug efflux transport complex

- **PR:** #1913
- **Record:** `data/structures/other/emrky_tolc_multidrug_efflux_transport_complex.yaml`
- **Reviewed head:** `fa22b4c9cf3783f2807bb9c8b1c1c3200920ee30`
- **Base:** `82eb79264b5056394a8f51b763f3389eb37e9cd4`
- **Result:** no concrete defects found
- **Issues filed:** none

## Scope

PR #1913 adds one proposed `cellstructuremech:` record for the E. coli K-12
EmrKY-TolC multidrug efflux transport complex, one repository-level history
record, refreshed text-embedding artifacts, regenerated pages, and refreshed
README corpus statistics.

The GitHub PR metadata reported exactly 13 changed files at reviewed head
`fa22b4c9cf3783f2807bb9c8b1c1c3200920ee30`, matching the local commit that
passed QC.

## Duplicate and Residue Checks

Hidden and ignored files were included in the duplicate/residue checks.

- `rg --no-ignore --hidden` over `data/structures/**/*.yaml` for `EmrKY`,
  `emrKY`, `CPX-4273`, `P52599`, and `P52600` found matches only in the new
  `emrky_tolc_multidrug_efflux_transport_complex.yaml` record.
- `rg --no-ignore --hidden` over `history`, `reports`, `scripts`, `docs`,
  `src`, `curation`, `research`, and `.github` for `EmrKY`, `CPX-4273`,
  `P52599`, `P52600`, `19721076`, and `10.1128/AAC.00454-09` found the new
  history record and transient local `reports/curie_check.tsv` rows, but no
  preexisting history/review entry and no leftover temporary mutator under
  `scripts/`.
- `find scripts -maxdepth 1 -type f -name '*emrky*' -print` found no
  temporary script.
- `rg --no-ignore --hidden -n 'curate_emrky|emrky_tolc|CPX-4273' scripts`
  found no temporary script content, including in hidden or ignored files.

## Authority Checks

The review rechecked the source payloads against the YAML model:

- Complex Portal `CPX-4273` resolves to `EmrKY-TolC multidrug efflux transport
  system` in `Escherichia coli (strain K12); 83333`.
- CPX-4273 lists participants P52599/EmrK, P52600/EmrY, and P02930/TolC in
  that source order, with source interactors `EBI-21418869`, `EBI-21407650`,
  and `EBI-21419977`.
- CPX-4273 carries null source stoichiometry for EmrK and EmrY and
  `minValue: 3, maxValue: 3` for TolC; the YAML correctly omits EmrK/EmrY
  participant copy numbers and preserves TolC stoichiometry as `3`.
- CPX-4273 cross-references `GO:1990281`, `GO:0042910`, `GO:0140330`, and
  `PMID:19721076`, which are represented in the record evidence.
- QuickGO exact-name checks found no exact `EmrKY` term; the only
  `EmrKY-TolC` fuzzy cellular-component hits were `GO:1990196`
  MacAB-TolC complex and `GO:1990195` macrolide transmembrane transporter
  complex, so the minted identifier under `GO:1990281` is justified.
- UniProtKB P52599 and P52600 are reviewed E. coli K-12 entries for `emrK`
  and `emrY` and both cross-reference `ComplexPortal:CPX-4273`.
- UniProtKB P02930 is the reviewed E. coli K-12 TolC entry, cross-references
  `ComplexPortal:CPX-4273`, and cross-references the exact TolC InterPro
  family `IPR058622`.
- EmrK and EmrY were left at `REVIEWED_LABEL_ONLY` because the available
  InterPro cross-references are broader membrane-fusion or MFS/EmrB-like
  families rather than exact source-neutral EmrK/EmrY families.
- PubMed `19721076` resolves to May et al. 2009 with DOI
  `10.1128/AAC.00454-09`.

## Validation Reviewed

The following local gates passed before the PR was opened:

- `linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/emrky_tolc_multidrug_efflux_transport_complex.yaml`
- `scripts/validate_strict.py --quiet data/structures/other/emrky_tolc_multidrug_efflux_transport_complex.yaml`
- `scripts/validate_history.py history/records/emrky_tolc_multidrug_efflux_transport_complex`
- `scripts/build_text_embedding_map.py --check`
- `scripts/render_pages.py --check`
- `scripts/check_docs.py --check`
- `scripts/validate_strict.py --quiet`
- `scripts/validate_history.py`
- `scripts/fetch_snippets.py --verify --check`
- `scripts/check_trait_links.py --check`
- `scripts/check_curies.py --check --report reports/curie_check.tsv`
- `scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `scripts/run_qc.py`
- `git diff --check`

`scripts/run_qc.py` passed with 567 tests passing, 3 skipped tests, 802
structure records, 1,436 valid history records, zero strict-validation errors,
and current generated pages.
