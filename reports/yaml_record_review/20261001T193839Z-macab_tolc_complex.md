# MacAB-TolC complex YAML review

- PR: #1883
- Branch: `add-macab-tolc-complex`
- Head reviewed: `1f1dd3e5e47d9be76442afbdcf848cb183247bcb`
- Record: `data/structures/other/macab_tolc_complex.yaml`
- History: `history/records/macab_tolc_complex/2026-10-01T192412Z-codex-e17b33.yaml`
- Reviewer: Codex
- Date: 2026-10-01

## Candidate And Duplicate Check

The pre-addition duplicate search used `rg --no-ignore --hidden` across
`data`, `history`, `reports`, and `pages` for `GO:1990196`, `MacAB-TolC`,
MacA/MacB/TolC accessions and exact InterPro families, `PDB:5NIK`,
`PMID:28504659`, `PMID:18955484`, and `DOI:10.1038/nmicrobiol.2017.70`.
It found only generic TolC-family references in the existing type I secretion
system record and no existing MacAB-TolC structure record.

## Authority Checks

- QuickGO reports `GO:1990196` as an active cellular-component term named
  `MacAB-TolC complex` with exact synonym `macrolide transporter MacAB-TolC
  complex` and an `is_a` parent of `GO:1990195`.
- QuickGO reports `GO:1990195` as the active cellular-component term
  `macrolide transmembrane transporter complex`.
- QuickGO reports `GO:0008559` as the active molecular-function term
  `ABC-type xenobiotic transporter activity`.
- UniProt REST reports reviewed E. coli K-12 entries `P75830` for MacA,
  `P75831` for MacB, and `P02930` for TolC, all cross-referenced to
  `GO:1990196`.
- InterPro reports exact family entries `IPR058623` for Macrolide export
  protein MacA, `IPR050250` for Macrolide Exporter MacB, and `IPR058622`
  for Outer membrane channel protein TolC.
- RCSB reports `PDB:5NIK` as the E. coli MacAB-TolC tripartite pump; assembly
  1 contains three TolC chains mapped to `P02930`, six MacA chains mapped to
  `P75830`, and two MacB chains mapped to `P75831`.
- RCSB and PubMed both link `PDB:5NIK` to `PMID:28504659` and
  `DOI:10.1038/nmicrobiol.2017.70`.
- PubMed reports `PMID:18955484` as the 2009 MacB/MacA ATPase and
  macrolide-binding paper cited for the MacB function evidence.

## Review Findings

No concrete defects were found.

The review specifically checked:

- the new identifier is the exact GO cellular-component term rather than a
  broader macrolide-transporter parent;
- the pre-existing type I secretion TolC-family component is not a duplicate
  MacAB-TolC record;
- every InterPro grounding is an exact component-family term, not a broad ABC
  transporter or outer-membrane efflux family;
- every UniProtKB example is reviewed, from E. coli K-12, and maps to the
  matching `PDB:5NIK` polymer entity;
- the 6:2:3 component stoichiometry and total `SUBUNIT_COUNT` 11 match
  `PDB:5NIK` biological assembly 1;
- the taxonomic distribution stays variable within Bacteria instead of
  overclaiming universality;
- `GO:0008559` is a molecular-function term appropriate for ATP-dependent
  xenobiotic export by a MacB ABC transporter;
- the history record targets the new YAML path and summarizes the record
  addition;
- rendered `pages/`, README statistics, and text embedding artifacts are
  regenerated from the new corpus state.

## Issues Filed

None.

## Local Verification

- `.venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/macab_tolc_complex.yaml`
- `.venv/bin/python scripts/validate_strict.py --quiet data/structures/other/macab_tolc_complex.yaml`
- `PATH=.venv/bin:$PATH .venv/bin/python scripts/validate_history.py history/records/macab_tolc_complex/2026-10-01T192412Z-codex-e17b33.yaml`
- `.venv/bin/python scripts/validate_strict.py --quiet`
- `PATH=.venv/bin:$PATH .venv/bin/python scripts/validate_history.py`
- `.venv/bin/python scripts/fetch_snippets.py --verify --check`
- `.venv/bin/python scripts/check_trait_links.py --check`
- `.venv/bin/python scripts/check_curies.py --check --report reports/curie_check.tsv`
- `.venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `.venv/bin/python scripts/build_text_embedding_map.py --check`
- `.venv/bin/python scripts/render_pages.py --check`
- `.venv/bin/python scripts/check_docs.py --check`
- `PATH=.venv/bin:$PATH .venv/bin/python scripts/run_qc.py`
- `git diff --check`
