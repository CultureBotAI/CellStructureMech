# EmrE multidrug transporter complex YAML review

- PR: #1884
- Branch: `add-emre-multidrug-transporter-complex`
- Head reviewed: `34214316ed241ec0f4c0732c71f3f51b63cdb9ff`
- Record: `data/structures/other/emre_multidrug_transporter_complex.yaml`
- History: `history/records/emre_multidrug_transporter_complex/2026-10-01T195637Z-codex-59b3e3.yaml`
- Reviewer: Codex
- Date: 2026-10-01

## Candidate And Duplicate Check

The pre-addition duplicate search used `rg --no-ignore --hidden` across
`data`, `history`, `reports`, and `pages` for `GO:1990207`, `EmrE`, `emrE`,
`P23895`, `PDB:3B5D`, `PMID:18024586`, `DOI:10.1073/pnas.0709387104`, and
EmrE-related InterPro accessions. It found no existing EmrE multidrug
transporter complex record or exact identifier/accession collision.

The post-PR review rechecked `data`, `history`, and `reports` with
`rg --no-ignore --hidden` for the same exact GO, PDB, PMID, DOI, UniProt, and
InterPro strings and found only the new record, its history, and regenerated
embedding references. The temporary `scripts/expand_emre_complex.py` mutator
was absent under both `find` and an ignored/hidden-inclusive `rg` search.

## Authority Checks

- QuickGO reports `GO:1990207` as an active cellular-component term named
  `EmrE multidrug transporter complex`, with narrow synonym `EmrE complex`, a
  definition backed by `PMID:18024586`, and text defining the E. coli complex
  as a homodimeric bacterial transporter of positively charged hydrophobic
  drugs.
- QuickGO reports `GO:1902495` as the active cellular-component term
  `transmembrane transporter complex`, with `GO:1990207` as an `is_a` child.
- QuickGO reports `GO:0042910` as the active molecular-function term
  `xenobiotic transmembrane transporter activity`.
- UniProt REST reports `P23895` as the reviewed E. coli K-12 `emrE` entry
  named `Multidrug transporter EmrE`; it cross-references `PDB:3B5D` and the
  InterPro entries `IPR037185`, `IPR000390`, and `IPR045324`.
- InterPro reports `IPR000390`, `IPR037185`, and `IPR045324` against
  `UniProtKB:P23895`; these denote the broader small drug/metabolite
  transporter family, the EmrE homologous superfamily, and the small multidrug
  resistance protein family, so the component is deliberately left
  `REVIEWED_LABEL_ONLY`.
- InterPro also exposes NCBIFam/PANTHER member signatures for `P23895`.
  Because a hidden/ignored-inclusive search of `data/structures`, `history`,
  `reports`, `pages`, `conf`, and `scripts` found no existing use of an
  `NCBIfam:` component grounding, the open exact-grounding `CURATION_TODO`
  remains the conservative curation choice for the initial record.
- RCSB reports `PDB:3B5D` as `EmrE multidrug transporter in complex with TPP,
  C2 crystal form`; polymer entity 1 is protein entity `Multidrug transporter
  emrE`, maps to `UniProtKB:P23895`, and appears twice in biological assembly
  1.
- RCSB reports biological assembly `3B5D-1` as an author-defined dimeric
  homomeric protein assembly with polymer entity count 1 and polymer entity
  instance count 2.
- RCSB and PubMed both link `PDB:3B5D` / `PMID:18024586` to
  `DOI:10.1073/pnas.0709387104` and the primary citation `X-ray structure of
  EmrE supports dual topology model.`

## Review Findings

No concrete defects were found.

The review specifically checked:

- the new record identifier is the exact GO cellular-component term for the
  EmrE complex, not only the broader `GO:1902495` transporter-complex parent;
- the GO narrow synonym, definition, and Bacteria-scoped distribution row are
  represented without broadening the record to all SMR multidrug transporters;
- `GO:0042910` is molecular-function evidence for xenobiotic transport and is
  kept under `functions` rather than used as the structure identity;
- the single EmrE component is modeled as a source-neutral protein constituent
  with a reviewed E. coli K-12 UniProt example, while exact family grounding is
  left open instead of overmapping to broad InterPro/Pfam families;
- `PDB:3B5D` assembly 1 supports both the canonical E. coli example and the
  homodimeric `SUBUNIT_COUNT` value of 2;
- PubMed, RCSB, and GO converge on `PMID:18024586` for the PDB:3B5D X-ray
  structure evidence;
- the history record targets the new YAML path and summarizes the GO, UniProt,
  PDB, DOI/PMID, taxonomy, function, component, and grounding-discussion
  additions;
- rendered `pages/`, README statistics, and text embedding artifacts are
  regenerated from the new corpus state.

## Issues Filed

None.

## Local Verification

- `.venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/emre_multidrug_transporter_complex.yaml`
- `.venv/bin/python scripts/validate_strict.py --quiet data/structures/other/emre_multidrug_transporter_complex.yaml`
- `PATH=.venv/bin:$PATH .venv/bin/python scripts/validate_history.py history/records/emre_multidrug_transporter_complex/2026-10-01T195637Z-codex-59b3e3.yaml`
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
