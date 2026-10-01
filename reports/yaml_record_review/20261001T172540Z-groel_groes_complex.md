# GroEL-GroES complex adversarial review

- **PR:** #1879
- **Branch:** `add-groel-groes-complex`
- **Record:** `data/structures/other/groel_groes_complex.yaml`
- **History:** `history/records/groel_groes_complex/2026-10-01T170413Z-codex-ff3d56.yaml`

## Scope Checks

- Ran hidden/ignored-inclusive duplicate searches for `GO:1990220`,
  `GroEL-GroES`, `GroEL/GroES`, `GroEL`, `GroES`, `Cpn60`, `Cpn10`,
  `IPR001844`, `IPR020818`, `P0A6F5`, `P0A6F9`, `PMID:9285585`,
  `DOI:10.1038/41944`, and `PDB:1AON` across `data/structures`,
  `history`, `reports`, `pages`, `README.md`, and `docs`. The
  pre-branch search, with ignored files included, found no existing
  exact `GO:1990220` or GroEL-GroES record; post-branch hits are confined
  to the new record, its history, regenerated pages, and the ignored
  CURIE-check report.
- Checked the only pre-existing chaperonin structure record,
  `GO:0005832` chaperonin-containing T-complex, and confirmed it is the
  eukaryotic TRiC/CCT complex rather than bacterial GroEL-GroES.
- Confirmed QuickGO reports `GO:1990220` as an unrestricted, non-obsolete
  cellular-component term named `GroEL-GroES complex`; its
  `bacterial chaperonin ATPase complex` and `bacterial chaperonin complex`
  synonyms are typed as related, matching the curated `RELATED_SYNONYM`
  rows.
- Checked QuickGO `GO:0016465` for the chaperonin ATPase complex parent
  and `GO:0006457` for protein folding function grounding.
- Verified RCSB `PDB:1AON` metadata:
  polymer entity 1 maps to fourteen GroEL chains and `UniProtKB:P0A6F5`;
  polymer entity 2 maps to seven GroES chains and `UniProtKB:P0A6F9`;
  assembly 1 contains 21 protein instances. The RCSB primary citation is
  Xu, Horwich and Sigler 1997, DOI `10.1038/41944`, PMID `9285585`.
- Verified the UniProt accessions directly through UniProt JSON:
  `P0A6F5` is reviewed E. coli K-12 Chaperonin GroEL with primary gene
  `groEL`, and `P0A6F9` is reviewed E. coli K-12 Co-chaperonin GroES
  with primary gene `groES`.
- Verified the InterPro accessions through the InterPro API:
  `IPR001844` is named `Chaperonin Cpn60/GroEL`, and `IPR020818` is
  named `GroES chaperonin family`.
- Confirmed with both `find` and `rg --no-ignore --hidden` that the
  temporary `scripts/enrich_groel_groes_complex.py` mutator was removed.
- Inspected `pages/structures/other/groel_groes_complex.html` and the
  embedding-map/search index entries generated from the new YAML.

## Findings

No concrete defects found. No GitHub issue was filed.

## Validation

- `.venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/groel_groes_complex.yaml`
- `.venv/bin/python scripts/validate_strict.py --quiet data/structures/other/groel_groes_complex.yaml`
- `.venv/bin/python scripts/validate_strict.py --quiet`
- `PATH=.venv/bin:$PATH .venv/bin/python scripts/validate_history.py history/records/groel_groes_complex/2026-10-01T170413Z-codex-ff3d56.yaml`
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

## Notes

- `scripts/check_curies.py` exercised resolver controls but could not reach
  all issuing authorities from this run; the new DOI, GO, InterPro, PMID,
  and UniProt identifiers were therefore reported as `UNREACHABLE`, which is
  treated as a transport failure rather than a curation defect.
- `scripts/fetch_snippets.py --verify --check` had no new verbatim snippets
  to verify for this record; all 31 existing corpus snippets were
  uncheckable because no route answered, not because any quote failed.
