# taurine dioxygenase complex record review

- Date: 2026-10-01
- PR: #1890
- Record: `data/structures/other/taurine_dioxygenase_complex.yaml`
- Identifier: `GO:1990205`
- Label: `taurine dioxygenase complex`
- Branch head reviewed: `93d121b147f8f25ed231d60d1a59a1066be6b7b3`

## Authority checks

- QuickGO resolves `GO:1990205` as an active cellular-component term named
  `taurine dioxygenase complex`, with exact synonyms
  `2-aminoethanesulfonate dioxygenase complex` and
  `alpha-ketoglutarate-dependent taurine dioxygenase complex`, narrow synonym
  `TauD complex`, and definition xref `PMID:12741810`.
- QuickGO resolves `GO:0000908` as the active molecular-function term
  `taurine dioxygenase activity`.
- UniProtKB resolves `P37610` as reviewed E. coli K-12 `TAUD_ECOLI`, primary
  gene `tauD`, with GO xrefs including `GO:1990205` and `GO:0000908`, PDB xrefs
  including `1OS7`, and InterPro xrefs `IPR051323`, `IPR042098`, and
  `IPR003819`.
- InterPro maps reviewed UniProt `P37610` to broad entries
  `IPR051323` alpha-ketoglutarate-dependent sulfate ester dioxygenase-like,
  `IPR003819` TauD/TfdA-like domain, and `IPR042098` Glutarate 2-hydroxylase
  superfamily. None was exact for TauD alone, so the component stays
  `REVIEWED_LABEL_ONLY`.
- RCSB resolves `PDB:1OS7` as an E. coli TauD structure whose primary
  citation is O'Brien et al. 2003, `PMID:12741810`,
  `DOI:10.1021/bi0341096`; assemblies 1 and 2 are both homodimeric.
- PubMed and Crossref resolve the E. coli TauD characterization paper as
  Eichhorn et al. 1997, `PMID:9287300`,
  `DOI:10.1074/jbc.272.37.23031`.
- PubMed resolves van der Ploeg et al. 1996,
  `PMID:8808933`, `DOI:10.1128/jb.178.18.5438-5446.1996`, as the E. coli
  `tauABCD` taurine-utilization gene-cluster paper. That citation was checked
  as background and was not needed in the final record.

## Duplicate and boundary checks

- Before addition, `rg --no-ignore --hidden` found no existing matches for
  `GO:1990205`, `taurine dioxygenase complex`, the GO exact/narrow synonyms,
  `UniProtKB:P37610`, `PDB:1OS7`, `PMID:9287300`, `PMID:12741810`,
  `DOI:10.1074/jbc.272.37.23031`, `DOI:10.1021/bi0341096`, or `tauD`.
- After generation, the same hidden/ignored-inclusive duplicate scan found only
  the new source record, the new history records, regenerated pages and
  embedding JSON, and ignored validator outputs under `reports/curie_check.tsv`
  and `build/curie_cache.json`.
- The record models the homo-oligomeric TauD complex, not the single TauD
  polypeptide. That matches the repository boundary already used for
  homomeric complexes such as the `SsuE` FMN reductase complex.
- `GO:1990201` alkanesulfonate monooxygenase complex was deliberately skipped
  in this iteration because it overlaps the already-curated SsuD/SsuE evidence
  cluster and its open exact-SsuD-grounding TODO.

## Findings

### Fixed: over-broad TauD grounding review wording

- Issue: #1891
- Fixed in commit: `93d121b1`
- Finding: the initial `grounding_notes` named `Pfam:PF02668` and `NCBIfam`
  while the reviewed evidence only supported the two broad InterPro entries
  mapped to `UniProtKB:P37610`. That overstated the exact grounding search.
- Resolution: narrowed `grounding_notes` to `InterPro:IPR051323` and
  `InterPro:IPR003819`, preserved `REVIEWED_LABEL_ONLY`, and added a
  follow-up repository history record linked to issue #1891 and PR #1890.

No other concrete defects were found in the final `93d121b1` PR diff.

## Local validation

Initial addition:

- `.venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/taurine_dioxygenase_complex.yaml`
- `.venv/bin/python scripts/validate_strict.py --quiet data/structures/other/taurine_dioxygenase_complex.yaml`
- `PATH=.venv/bin:$PATH .venv/bin/python scripts/validate_history.py history/records/taurine_dioxygenase_complex/2026-10-01T232121Z-codex-5bbaab.yaml`
- `.venv/bin/python scripts/build_text_embedding_map.py --check`
- `.venv/bin/python scripts/render_pages.py --check`
- `.venv/bin/python scripts/check_docs.py --check`
- `.venv/bin/python scripts/validate_strict.py --quiet`
- `PATH=.venv/bin:$PATH .venv/bin/python scripts/validate_history.py`
- `.venv/bin/python scripts/fetch_snippets.py --verify --check`
- `.venv/bin/python scripts/check_trait_links.py --check`
- `.venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `.venv/bin/python scripts/check_curies.py --check --report reports/curie_check.tsv`
- `PATH=.venv/bin:$PATH .venv/bin/python scripts/run_qc.py`
- `git diff --check`

Review fix for #1891:

- `.venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/taurine_dioxygenase_complex.yaml`
- `.venv/bin/python scripts/validate_strict.py --quiet data/structures/other/taurine_dioxygenase_complex.yaml`
- `PATH=.venv/bin:$PATH .venv/bin/python scripts/validate_history.py history/records/taurine_dioxygenase_complex/2026-10-01T233719Z-codex-12e418.yaml`
- `.venv/bin/python scripts/build_text_embedding_map.py --check`
- `.venv/bin/python scripts/render_pages.py --check`
- `.venv/bin/python scripts/check_docs.py --check`
- `.venv/bin/python scripts/validate_strict.py --quiet`
- `PATH=.venv/bin:$PATH .venv/bin/python scripts/validate_history.py`
- `PATH=.venv/bin:$PATH .venv/bin/python scripts/run_qc.py`
- `git diff --check`

