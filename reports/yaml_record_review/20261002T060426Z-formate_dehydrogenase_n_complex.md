# YAML Record Review: formate dehydrogenase N complex

- **PR:** #1903
- **Record:** `data/structures/energy_complex/formate_dehydrogenase_n_complex.yaml`
- **Reviewer:** codex
- **Review time:** 2026-10-02T06:04:26Z
- **Scope:** Adversarial review of the `cellstructuremech:formate_dehydrogenase_n_complex` record, its history entry, and generated artifacts added in branch `add-formate-dehydrogenase-n-complex`.

## Outcome

No concrete defects found.

## Checks Performed

- Re-read the submitted formate dehydrogenase N YAML and the append-only history record after opening PR #1903.
- Rechecked Complex Portal `CPX-1975` as the E. coli K-12 formate dehydrogenase N complex entry:
  - primary accession `CPX-1975`
  - source label `Formate dehydrogenase N complex`
  - species `Escherichia coli (strain K12); 83333`
  - systematic name `3xfdnG:3xfdnH:3xfdnI`
  - assembly `Heterononamer`
  - evidence code `ECO:0000353`
  - participants `P0AEK7`/`fdnI` x3, `CHEBI:60539` x3, `CHEBI:16374` x1, `P24183`/`fdnG` x3, `P0AAJ3`/`fdnH` x3, `CHEBI:30413` x6, and `CHEBI:33725` x15
- Rechecked active QuickGO terms:
  - `GO:0009326` is the cellular-component term `formate dehydrogenase complex`, a broader parent for this nitrate-inducible FdnGHI record.
  - `GO:0098803` is the cellular-component term `respiratory chain complex`.
  - `GO:0036397` is the molecular-function term `formate dehydrogenase (quinone) activity` with the reaction formate + quinone = CO2 + quinol.
- Rechecked reviewed E. coli UniProtKB examples from the cached UniProt response:
  - `P24183` / `FDNG_ECOLI` / `fdnG` / `Formate dehydrogenase, nitrate-inducible, major subunit`
  - `P0AAJ3` / `FDNH_ECOLI` / `fdnH` / `Formate dehydrogenase, nitrate-inducible, iron-sulfur subunit`
  - `P0AEK7` / `FDNI_ECOLI` / `fdnI` / `Formate dehydrogenase, nitrate-inducible, cytochrome b556(Fdn) subunit`
  - all three entries cross-reference `ComplexPortal:CPX-1975` and `GO:0009326`
- Rechecked source-native ChEBI labels through OLS:
  - `CHEBI:60539` resolves to `Mo(=O)-bis(molybdopterin guanine dinucleotide)(4-)`
  - `CHEBI:16374` resolves to `menaquinone`
  - `CHEBI:30413` resolves to `heme`
  - `CHEBI:33725` resolves to `tetra-mu3-sulfido-tetrairon(0)`, while the record preserves Complex Portal's participant label `tetra-mu3-sulfido-tetrairon`
- Rechecked the structural accessions through RCSB:
  - `PDB:1KQF` is `FORMATE DEHYDROGENASE N FROM E. COLI`
  - `PDB:1KQG` is `FORMATE DEHYDROGENASE N FROM E. COLI`
- Rechecked NCBI PubMed metadata:
  - `PMID:11884747` is Jormakka et al. 2002, `Molecular basis of proton motive force generation: structure of formate dehydrogenase-N.`
  - the PubMed DOI article ID is `10.1126/science.1068186`
- Ran a local YAML cross-check confirming:
  - the three declared component gene symbols are exactly `fdnG`, `fdnH`, and `fdnI`
  - the CPX-1975 protein participants are exactly `fdnG`, `fdnH`, and `fdnI`
  - all protein stoichiometries copied into `complex_compositions` are `3`
  - every causal-graph `component_ref` points at a declared component
- Confirmed hidden and ignored files were included in duplicate searches for `formate_dehydrogenase_n_complex`, `formate dehydrogenase N complex`, CPX-1975 labels and synonyms, the three UniProt accessions, the PDB accessions, `PMID:11884747`, and `DOI:10.1126/science.1068186`; matches were limited to the new maintained YAML, its generated artifacts, its history record, and build/report caches derived from the new record.
- Confirmed hidden and ignored files were included when checking `scripts/` for `curate_formate_dehydrogenase_n_complex` and `formate_dehydrogenase_n_complex`; no temporary mutator remains.
- Confirmed generated pages and embedding indexes reference the new `cellstructuremech:formate_dehydrogenase_n_complex` identifier and page.
- Corrected the PR body to list the actual validation commands run for this repository.

## Validation Reviewed

- `PATH=.venv/bin:$PATH linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/energy_complex/formate_dehydrogenase_n_complex.yaml`
- `scripts/validate_strict.py --quiet data/structures/energy_complex/formate_dehydrogenase_n_complex.yaml`
- `scripts/build_text_embedding_map.py --refresh`
- `scripts/build_text_embedding_map.py --check`
- `scripts/render_pages.py`
- `scripts/check_docs.py --write`
- `scripts/render_pages.py --check`
- `scripts/check_docs.py --check`
- `scripts/validate_history.py history/records/formate_dehydrogenase_n_complex/2026-10-02T054708Z-claude-code-e62c49.yaml`
- `scripts/validate_history.py`
- `scripts/validate_strict.py --quiet`
- `scripts/fetch_snippets.py --verify --check`
- `scripts/check_trait_links.py --check`
- `scripts/check_curies.py --check --report reports/curie_check.tsv`
- `scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `git diff --check`
- `PATH=.venv/bin:$PATH .venv/bin/python scripts/run_qc.py`

## Issues Filed

None.
