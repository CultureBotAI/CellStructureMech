# YAML Record Review: formate hydrogenlyase complex

- **PR:** #1904
- **Record:** `data/structures/energy_complex/formate_hydrogenlyase_complex.yaml`
- **Reviewer:** codex
- **Review time:** 2026-10-02T06:35:31Z
- **Scope:** Adversarial review of the `cellstructuremech:formate_hydrogenlyase_complex` record, its history entry, and generated artifacts added in branch `add-formate-hydrogenlyase-complex`.

## Outcome

No concrete defects found.

## Checks Performed

- Re-read the submitted formate hydrogenlyase YAML and the append-only history record after opening PR #1904.
- Rechecked RCSB `PDB:7Z0T` as the E. coli K-12 formate hydrogenlyase structure:
  - source title `Structure of the Escherichia coli formate hydrogenlyase complex (aerobic preparation, composite structure)`
  - experimental method electron microscopy
  - seven polymer entities
  - primary citation PubMed identifier `36104349`
  - primary citation DOI `10.1038/s41467-022-32831-x`
- Rechecked RCSB 7Z0T polymer-entity mappings against the seven reviewed E. coli K-12 UniProtKB examples in the record:
  - entity 7 maps to `UniProtKB:P07658` / `fdhF` / `Formate dehydrogenase H`
  - entity 3 maps to `UniProtKB:P0AAK1` / `hycB` / `Formate hydrogenlyase subunit 2`
  - entity 1 maps to `UniProtKB:P16429` / `hycC` / `Formate hydrogenlyase subunit 3`
  - entity 6 maps to `UniProtKB:P16430` / `hycD` / `Formate hydrogenlyase subunit 4`
  - entity 2 maps to `UniProtKB:P16431` / `hycE` / `Formate hydrogenlyase subunit 5`
  - entity 5 maps to `UniProtKB:P16432` / `hycF` / `Formate hydrogenlyase subunit 6`
  - entity 4 maps to `UniProtKB:P16433` / `hycG` / `Formate hydrogenlyase subunit 7`
- Rechecked the cached reviewed E. coli K-12 UniProtKB response and confirmed that the seven declared protein examples are all reviewed Swiss-Prot records:
  - `P07658` / `fdhF` / `Formate dehydrogenase H`
  - `P0AAK1` / `hycB` / `Formate hydrogenlyase subunit 2`
  - `P16429` / `hycC` / `Formate hydrogenlyase subunit 3`
  - `P16430` / `hycD` / `Formate hydrogenlyase subunit 4`
  - `P16431` / `hycE` / `Formate hydrogenlyase subunit 5`
  - `P16432` / `hycF` / `Formate hydrogenlyase subunit 6`
  - `P16433` / `hycG` / `Formate hydrogenlyase subunit 7`
- Rechecked NCBI PubMed metadata:
  - `PMID:36104349` is Steinhilper et al. 2022, `Structure of the membrane-bound formate hydrogenlyase complex from Escherichia coli.`
  - the PubMed DOI article ID is `10.1038/s41467-022-32831-x`
  - the PubMed Central article ID is `PMC9474812`
- Rechecked active QuickGO `GO:1990204`:
  - aspect `cellular_component`
  - label `oxidoreductase complex`
  - definition `Any protein complex that possesses oxidoreductase activity.`
- Rechecked Complex Portal `CPX-8422` and confirmed it is an unrelated human `HAS1-HAS2 hyaluronan biosynthesis complex`, so no Complex Portal grounding was appropriate for this E. coli FHL record.
- Rechecked QuickGO search results for `formate hydrogenlyase` and confirmed they did not provide an exact cellular-component or molecular-function term for the seven-subunit FdhF/HycB-HycG complex.
- Ran a local YAML cross-check confirming:
  - the seven declared component gene symbols are exactly `fdhF`, `hycB`, `hycC`, `hycD`, `hycE`, `hycF`, and `hycG`
  - the seven declared UniProtKB examples are exactly `P07658`, `P0AAK1`, `P16429`, `P16430`, `P16431`, `P16432`, and `P16433`
  - every protein example is attached to `NCBITaxon:83333`
  - every causal-graph `component_ref` points at a declared component
  - every component has a reviewed-label-only grounding note and is attached to the `fhl_component_family_grounding` curation TODO
- Confirmed hidden and ignored files were included in duplicate searches for `formate_hydrogenlyase_complex`, `formate hydrogenlyase complex`, `FHL complex`, `PDB:7Z0T`, `PMID:36104349`, `DOI:10.1038/s41467-022-32831-x`, `fdhF`, `hycB`, `hycC`, `hycD`, `hycE`, `hycF`, `hycG`, and the seven UniProt accessions; matches were limited to the new maintained YAML, its generated artifacts, its history record, and build/report caches derived from the new record.
- Confirmed hidden and ignored files were included when checking `scripts/` for `curate_formate_hydrogenlyase_complex` and `formate_hydrogenlyase_complex`; no temporary mutator remains.
- Confirmed generated pages and embedding indexes reference the new `cellstructuremech:formate_hydrogenlyase_complex` identifier and page.

## Validation Reviewed

- `PATH=.venv/bin:$PATH linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/energy_complex/formate_hydrogenlyase_complex.yaml`
- `scripts/validate_strict.py --quiet data/structures/energy_complex/formate_hydrogenlyase_complex.yaml`
- local component/TODO consistency cross-check
- `scripts/build_text_embedding_map.py --refresh`
- `scripts/build_text_embedding_map.py --check`
- `scripts/render_pages.py`
- `scripts/check_docs.py --write`
- `scripts/render_pages.py --check`
- `scripts/check_docs.py --check`
- `scripts/validate_history.py history/records/formate_hydrogenlyase_complex/2026-10-02T062239Z-codex-574d2b.yaml`
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
