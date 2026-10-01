# Dxr protein complex record review

## Scope

- PR: https://github.com/CultureBotAI/CellStructureMech/pull/1881
- Record: `data/structures/other/dxr_protein_complex.yaml`
- Identifier: `GO:1990065`
- Label: `Dxr protein complex`

## Checks

- Re-ran a hidden/ignored-inclusive duplicate search for `GO:1990065`, the
  `Dxr protein complex` label, the GO exact synonym, the GO definition PMID, the
  primary Dxr structural PMID/DOI/PDB accessions, and Dxr/IspC names; no prior
  record or review report already covered this exact structure.
- Checked Gene Ontology metadata for `GO:1990065`; the term is active,
  cellular-component-scoped, named `Dxr protein complex`, and carries the exact
  `1-deoxy-D-xylulose 5-phosphate reductoisomerase complex` synonym used in the
  record.
- Checked Gene Ontology parentage for `GO:1990065`; `GO:0032991`
  `protein-containing complex` is an ancestor and is the narrowest existing
  CellStructureMech parent used by the new record.
- Checked `GO:0030604`; it is the active molecular-function term for
  `1-deoxy-D-xylulose-5-phosphate reductoisomerase activity`, matching the
  curated Dxr function.
- Checked InterPro `IPR003821`; it is the whole-family entry for
  `1-deoxy-D-xylulose 5-phosphate reductoisomerase`, matching the constituent
  Dxr reductoisomerase grounding.
- Checked UniProtKB `P45568`; it is the reviewed E. coli K-12 entry for
  Dxr/IspC and matches the accession used in the protein example.
- Checked RCSB PDB `1Q0Q`; the entry is an E. coli homomeric Dxr structure, has
  two deposited protein chains, and maps its only polymer entity to
  UniProtKB:P45568.
- Checked PubMed metadata for `PMID:15567415`; it is Mac Sweeney et al. 2005,
  the Journal of Molecular Biology E. coli Dxr structural paper cited by
  PDB:1Q0Q.
- Confirmed the record does not overfit a catalytic protein as a single-protein
  structure: GO represents `GO:1990065` as a cellular-component complex, and
  the PDB-backed canonical example and `SUBUNIT_COUNT` capture a homodimeric
  E. coli Dxr instance.
- Confirmed regenerated embedding, README, and page artifacts contain the new
  record and no unrelated hand-authored changes.

## Local Validation

- `linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/dxr_protein_complex.yaml`
- `python scripts/validate_strict.py --quiet data/structures/other/dxr_protein_complex.yaml`
- `python scripts/validate_strict.py --quiet`
- `python scripts/validate_history.py history/records/dxr_protein_complex/2026-10-01T181839Z-codex-358387.yaml`
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
