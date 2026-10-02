# Review: MlaFEDB lipid transport complex

- **PR:** #1914
- **Record:** `data/structures/other/mlafedb_lipid_transport_complex.yaml`
- **Identifier:** `cellstructuremech:mlafedb_lipid_transport_complex`
- **Review timestamp:** 2026-10-02T13:15:57Z
- **Reviewer:** codex

## Scope

Adversarial review of the newly added proposed `MlaFEDB lipid transport complex`
record, its `ComplexPortal:CPX-3464` source composition, generated site and
embedding artifacts, and the append-only history record.

## Authority Checks

- Hidden/ignored-inclusive duplicate checks over `data/structures` and
  `history/records` found no pre-existing MlaFEDB, MlaFEDBCA, `CPX-3464`,
  `P64606`, `P63386`, `P64604`, or `P64602` record.
- QuickGO searches for `MlaFEDB`, `MlaFEDBCA`, and `Mla` returned zero exact
  cellular-component hits, so a local `cellstructuremech:` identifier is
  appropriate.
- QuickGO `GO:1990531` resolves to `phospholipid-translocating ATPase complex`,
  defined for P-type ATPases; the record correctly uses the broader ABC
  transporter parent `GO:0043190` instead.
- ComplexPortal `CPX-3464` resolves to `MlaFEDB lipid transport complex` for
  *Escherichia coli* K-12 and lists MlaE, MlaF, MlaD, and MlaB participants.
- The ComplexPortal source asserts six copies only for MlaD; the MlaE, MlaF,
  and MlaB stoichiometries in curated `components` are separately backed by
  RCSB PDB `7CGE`.
- RCSB PDB `7CGE` assembly 1 is an author-defined dodecameric MlaFEDB assembly
  with two MlaE chains, two MlaF chains, two MlaB chains, and six MlaD chains.
- UniProt searches for the E. coli K-12 `mlaE`, `mlaF`, `mlaD`, and `mlaB`
  genes resolve to reviewed Swiss-Prot entries `P64606`, `P63386`, `P64604`,
  and `P64602`; each cross-references `CPX-3464`.
- InterPro entries `IPR053408`, `IPR030970`, and `IPR049743` exactly denote
  MlaE, MlaD, and MlaB families. MlaF is correctly left
  `REVIEWED_LABEL_ONLY` because its UniProt InterPro cross-references are
  broad ABC/P-loop ATPase entries.
- PubMed `32884137`, DOI `10.1038/s41422-020-00404-6`, and RCSB all agree on
  the primary 2020 MlaFEDB structural paper.

## Findings

No concrete defects found in the opened PR diff.

## Validation Reviewed

- `linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/mlafedb_lipid_transport_complex.yaml`
- `.venv/bin/python scripts/validate_strict.py --quiet data/structures/other/mlafedb_lipid_transport_complex.yaml`
- `env PATH=.venv/bin:$PATH .venv/bin/python scripts/validate_history.py history/records/mlafedb_lipid_transport_complex/2026-10-02T125446Z-codex-8f8867.yaml`
- `.venv/bin/python scripts/build_text_embedding_map.py --check`
- `.venv/bin/python scripts/render_pages.py --check`
- `.venv/bin/python scripts/check_docs.py --check`
- `.venv/bin/python scripts/validate_strict.py --quiet`
- `env PATH=.venv/bin:$PATH .venv/bin/python scripts/validate_history.py`
- `.venv/bin/python scripts/fetch_snippets.py --verify --check`
- `.venv/bin/python scripts/check_trait_links.py --check`
- `.venv/bin/python scripts/check_curies.py --check --report reports/curie_check.tsv`
- `.venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `env PATH=.venv/bin:$PATH .venv/bin/python scripts/run_qc.py`
- `git diff --check`
