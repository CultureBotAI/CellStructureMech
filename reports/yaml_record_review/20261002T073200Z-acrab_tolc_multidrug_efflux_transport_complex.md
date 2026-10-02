# YAML Record Review: AcrAB-TolC multidrug efflux transport complex

- **PR:** #1905
- **Record:** `data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml`
- **Reviewer:** codex
- **Review time:** 2026-10-02T07:32:00Z
- **Scope:** Adversarial review of the `cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex` record, its history entries, and generated artifacts added in branch `add-acrab-tolc-complex`.

## Outcome

One concrete defect was found, filed as issue #1906, and fixed in follow-up commit `12878a78`.

## Checks Performed

- Re-read the submitted AcrAB-TolC YAML and both append-only history records after opening PR #1905.
- Rechecked hidden and ignored files for duplicate candidates matching `AcrAB-TolC`, `AcrAB`, `ComplexPortal:CPX-4263`, and `PDB:5V5S`; no existing maintained AcrAB-TolC record or prior CPX-4263/PDB:5V5S use was found.
- Rechecked exact Complex Portal `CPX-4263`:
  - source label `AcrAB-TolC multidrug efflux transport complex`
  - species `Escherichia coli (strain K12); 83333`
  - systematic name `6xacrA:3xacrB:3xtolC`
  - assembly `Heterododecamer`
  - evidence code `ECO:0000353`
  - participants `P31224` / `acrB` x3, `P0AE06` / `acrA` x6, and `P02930` / `tolC` x3
  - cross-references `GO:1990281`, `GO:0042910`, `PDB:5V5S`, `EMD-8636`, `PMID:28355133`, `PMID:26113845`, and `PMID:12426336`
- Rechecked active QuickGO terms:
  - `GO:1990281` is the cellular-component term `efflux pump complex`, a broader parent for this AcrAB-TolC-specific record.
  - `GO:0042910` is the molecular-function term `xenobiotic transmembrane transporter activity`.
- Rechecked RCSB `PDB:5V5S` as a three-protein AcrAB-TolC cryo-EM structure:
  - source title `multi-drug efflux; membrane transport; RND superfamily; Drug resistance`
  - experimental method electron microscopy
  - primary DOI `10.7554/eLife.24905`
  - primary PubMed identifier `28355133`
  - exactly three protein polymer entities
- Rechecked RCSB PDB:5V5S polymer-entity mappings:
  - `P02930` / TolC
  - `P0AE06` / AcrA
  - `P31224` / AcrB
- Rechecked reviewed E. coli K-12 UniProtKB examples from the cached UniProt response:
  - `P0AE06` / `ACRA_ECOLI` / `acrA` / `Multidrug efflux pump subunit AcrA`, cross-referenced to `ComplexPortal:CPX-4263`
  - `P31224` / `ACRB_ECOLI` / `acrB` / `Multidrug efflux pump subunit AcrB`, cross-referenced to `ComplexPortal:CPX-4263`
  - `P02930` / `TOLC_ECOLI` / `tolC` / `Outer membrane protein TolC`, cross-referenced to `ComplexPortal:CPX-4263`
- Rechecked NCBI PubMed metadata:
  - `PMID:28355133` is Wang et al. 2017, `An allosteric transport mechanism for the AcrAB-TolC multidrug efflux pump.`
  - the PubMed DOI article ID is `10.7554/eLife.24905`
  - the PubMed Central article ID is `PMC5404916`
  - `PMID:26113845` is a 2015 review, `The ins and outs of RND efflux pumps in Escherichia coli.`
- Rechecked the existing MacAB-TolC record and found that TolC had already been verified to the exact family `InterPro:IPR058622`, `Outer membrane channel protein TolC`.
- Ran a local YAML cross-check confirming:
  - the declared component gene symbols are exactly `acrA`, `acrB`, and `tolC`
  - the declared UniProtKB examples are exactly `P0AE06`, `P31224`, and `P02930`
  - the Complex Portal participants and stoichiometries are exactly `acrA` x6, `acrB` x3, and `tolC` x3
  - every causal-graph `component_ref` points at a declared component
  - after issue #1906 was fixed, TolC is grounded to `InterPro:IPR058622`
  - after issue #1906 was fixed, only the AcrA and AcrB components remain `REVIEWED_LABEL_ONLY` and attached to the open component-family grounding TODO
- Confirmed hidden and ignored files were included when checking `scripts/` for `curate_acrab_tolc_multidrug_efflux_transport_complex` and `acrab_tolc_multidrug_efflux_transport_complex`; no temporary mutator remains.
- Confirmed generated pages and embedding indexes reference the new `cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex` identifier and page.

## Validation Reviewed

- `PATH=.venv/bin:$PATH linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml`
- `scripts/validate_strict.py --quiet data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml`
- local component/Complex Portal/TODO consistency cross-checks
- `scripts/build_text_embedding_map.py --refresh`
- `scripts/build_text_embedding_map.py --check`
- `scripts/render_pages.py`
- `scripts/check_docs.py --write`
- `scripts/render_pages.py --check`
- `scripts/check_docs.py --check`
- `scripts/validate_history.py history/records/acrab_tolc_multidrug_efflux_transport_complex/2026-10-02T065622Z-codex-229e8a.yaml`
- `scripts/validate_history.py history/records/acrab_tolc_multidrug_efflux_transport_complex/2026-10-02T070954Z-codex-5547ae.yaml`
- `scripts/validate_history.py`
- `scripts/validate_strict.py --quiet`
- `scripts/fetch_snippets.py --verify --check`
- `scripts/check_trait_links.py --check`
- `scripts/check_curies.py --check --report reports/curie_check.tsv`
- `scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `git diff --check`
- `PATH=.venv/bin:$PATH .venv/bin/python scripts/run_qc.py`

## Issues Filed

- #1906 — Ground AcrAB-TolC TolC component to InterPro IPR058622
