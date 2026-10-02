# YAML Record Review: PotABCD spermidine ABC transporter complex

- **PR:** #1907
- **Record:** `data/structures/other/potabcd_spermidine_abc_transporter_complex.yaml`
- **Reviewer:** codex
- **Review time:** 2026-10-02T08:48:07Z
- **Scope:** Adversarial review of the `cellstructuremech:potabcd_spermidine_abc_transporter_complex` record, its append-only history entry, and generated artifacts added in branch `add-potabcd-spermidine-abc-transporter`.

## Outcome

No concrete defects were found. No GitHub issues were filed.

## Checks Performed

- Re-read the submitted PotABCD YAML and append-only history record after opening PR #1907.
- Rechecked hidden and ignored files for duplicate candidates matching `spermidine ABC transporter`, `Spermidine ABC transporter`, `Spermidine-preferential ABC transporter`, `potABCD`, `PotABCD`, `CPX-4383`, `P0AFK9`, `P69874`, `P0AFK4`, `P0AFK6`, `PMID:11421274`, `PMID:18634750`, `DOI:10.1016/j.bbamem.2008.06.009`, and `DOI:10.1016/s0923-2508(01)01198-6`; no existing maintained PotABCD record or prior CPX-4383 use was found before this PR.
- Rechecked exact Complex Portal `CPX-4383`:
  - source label `Spermidine ABC transporter complex`
  - species `Escherichia coli (strain K12); 83333`
  - systematic name `2xpotA:potB:potC:potD`
  - assembly `Heteropentamer`
  - evidence code `ECO:0005547`
  - synonyms `Spermidine-preferential ABC transporter complex` and `potABCD complex`
  - ligands `Spermidine (CHEBI:16610)` and `Putrescine (CHEBI:17148)`
  - participants `P0AFK9` / `potD` x1, `P69874` / `potA` x2, `P0AFK4` / `potB` x1, and `P0AFK6` / `potC` x1
  - cross-references `GO:0015594`, `GO:0015417`, `PMID:18634750`, and `PMID:11421274`
- Rechecked active QuickGO terms:
  - `GO:0055052` is the cellular-component term `ATP-binding cassette (ABC) transporter complex, substrate-binding subunit-containing`, a broader parent for this PotABCD-specific record.
  - `GO:0015417` is the molecular-function term `ABC-type polyamine transporter activity`.
  - `GO:0015594` is the molecular-function term `ABC-type putrescine transporter activity`.
- Rechecked reviewed E. coli K-12 UniProtKB examples from the cached UniProt response:
  - `P69874` / `POTA_ECOLI` / `potA` / `Spermidine/putrescine import ATP-binding protein PotA`, cross-referenced to `ComplexPortal:CPX-4383`
  - `P0AFK4` / `POTB_ECOLI` / `potB` / `Spermidine/putrescine transport system permease protein PotB`, cross-referenced to `ComplexPortal:CPX-4383`
  - `P0AFK6` / `POTC_ECOLI` / `potC` / `Spermidine/putrescine transport system permease protein PotC`, cross-referenced to `ComplexPortal:CPX-4383`
  - `P0AFK9` / `POTD_ECOLI` / `potD` / `Spermidine/putrescine-binding periplasmic protein`, cross-referenced to `ComplexPortal:CPX-4383`
- Rechecked NCBI PubMed metadata:
  - `PMID:18634750` is Moussatova et al. 2008, `ATP-binding cassette transporters in Escherichia coli.`
  - the PubMed DOI article ID for `PMID:18634750` is `10.1016/j.bbamem.2008.06.009`
  - `PMID:11421274` is Igarashi and Kashiwagi 2001, `Polyamine uptake systems in Escherichia coli.`
  - the PubMed DOI article ID for `PMID:11421274` is `10.1016/s0923-2508(01)01198-6`
- Ran a local YAML cross-check confirming:
  - the declared component gene symbols are exactly `potA`, `potB`, `potC`, and `potD`
  - the declared UniProtKB examples are exactly `P69874`, `P0AFK4`, `P0AFK6`, and `P0AFK9`
  - the Complex Portal participants and stoichiometries are exactly `potA` x2, `potB` x1, `potC` x1, and `potD` x1
  - the Complex Portal source composition sums to 5 subunits
  - every causal-graph `component_ref` points at a declared component
  - every causal-graph edge subject and object points at a declared graph node
  - all four protein components remain `REVIEWED_LABEL_ONLY` and are attached to the open component-family grounding TODO
- Confirmed hidden and ignored files were included when checking `scripts/` for `curate_potabcd`, `potabcd_spermidine`, and `CPX-4383`; no temporary mutator remains.
- Confirmed generated pages and embedding indexes reference the new `cellstructuremech:potabcd_spermidine_abc_transporter_complex` identifier and page.
- Confirmed the PR changed exactly the new record, the new history file, generated embedding JSON, generated static site files, and the README corpus summary.

## Validation Reviewed

- `PATH=.venv/bin:$PATH linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/potabcd_spermidine_abc_transporter_complex.yaml`
- `scripts/validate_strict.py --quiet data/structures/other/potabcd_spermidine_abc_transporter_complex.yaml`
- local component/Complex Portal/graph consistency cross-checks
- `scripts/build_text_embedding_map.py --refresh`
- `scripts/build_text_embedding_map.py --check`
- `scripts/render_pages.py`
- `scripts/check_docs.py --write`
- `scripts/render_pages.py --check`
- `scripts/check_docs.py --check`
- `scripts/validate_history.py history/records/potabcd_spermidine_abc_transporter_complex`
- `scripts/validate_history.py`
- `scripts/validate_strict.py --quiet`
- `scripts/fetch_snippets.py --verify --check`
- `scripts/check_trait_links.py --check`
- `scripts/check_curies.py --check --report reports/curie_check.tsv`
- `scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `PATH=.venv/bin:$PATH .venv/bin/python scripts/run_qc.py`
- `git diff --check`

## Issues Filed

None.
