# Ammonium transmembrane transporter complex record review

## Scope

- PR: https://github.com/CultureBotAI/CellStructureMech/pull/1882
- Record: `data/structures/other/ammonium_transmembrane_transporter_complex.yaml`
- Identifier: `GO:0110067`
- Label: `ammonium transmembrane transporter complex`

## Checks

- Re-ran a hidden/ignored-inclusive duplicate search for `GO:0110067`, the
  `ammonium transmembrane transporter complex` label, the `AMT1 complex` GO
  narrow synonym, AmtB/ammonia-channel names, `PDB:1U7G`, `PMID:15361618`,
  and `DOI:10.1126/science.1101952`; no prior record or review report already
  covered this exact ammonium-transporter complex.
- Checked QuickGO metadata for `GO:0110067`; the term is active,
  cellular-component-scoped, named `ammonium transmembrane transporter
  complex`, and carries the narrow `AMT1 complex` synonym used in the record.
- Checked QuickGO `GO:1902495`; it is an active cellular-component
  `transmembrane transporter complex` term and lists `GO:0110067` as an
  `is_a` child.
- Checked QuickGO `GO:0008519`; it is the active molecular-function term for
  `ammonium channel activity`, and QuickGO lists it as the capable-of target
  for `GO:0110067`.
- Checked QuickGO `GO:0072488`; it is the active biological-process term for
  `ammonium transmembrane transport`, and QuickGO lists it as the
  capable-of-part-of target for `GO:0110067`.
- Checked InterPro `IPR001905`; it is the reviewed `Ammonium transporter`
  family entry, excludes the Rhesus subgroup, and lists PDB `1u7g` as its
  representative structure.
- Checked UniProtKB `P69681`; it is the reviewed E. coli K-12 entry for
  ammonium transporter AmtB and includes the `amtB` gene symbol used in the
  protein example.
- Checked RCSB PDB `1U7G`; the entry is an E. coli AmtB ammonia-channel
  crystal structure, its polymer entity maps to UniProtKB:P69681 by SIFTS, and
  biological assembly 1 is a homotrimer with three protein instances.
- Checked PubMed metadata for `PMID:15361618`; it is Khademi et al. 2004, the
  Science E. coli AmtB structure paper cited by PDB:1U7G.
- Confirmed the record does not overstate the deposited asymmetric unit: the
  three-subunit physical property is scoped to RCSB biological assembly 1, not
  the single deposited polymer instance.
- Confirmed regenerated embedding, README, and page artifacts contain the new
  record and no unrelated hand-authored changes.

## Local Validation

- `linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/ammonium_transmembrane_transporter_complex.yaml`
- `python scripts/validate_strict.py --quiet data/structures/other/ammonium_transmembrane_transporter_complex.yaml`
- `python scripts/validate_strict.py --quiet`
- `python scripts/validate_history.py history/records/ammonium_transmembrane_transporter_complex/2026-10-01T184859Z-codex-30430e.yaml`
- `python scripts/validate_history.py`
- `python scripts/fetch_snippets.py --verify --check`
- `python scripts/check_trait_links.py --check`
- `python scripts/check_curies.py --check --report reports/curie_check.tsv`
- `python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `python scripts/build_text_embedding_map.py --check`
- `python scripts/render_pages.py --check`
- `python scripts/check_docs.py --check`
- `python scripts/run_qc.py`
- `git diff --check`

## Findings

No concrete defects found. No GitHub issues were filed.
