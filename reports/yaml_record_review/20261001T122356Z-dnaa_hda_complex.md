# DnaA-Hda complex adversarial review

- **PR:** #1870
- **Branch:** `add-dnaa-hda-complex`
- **Record:** `data/structures/other/dnaa_hda_complex.yaml`
- **History:**
  - `history/records/dnaa_hda_complex/2026-10-01T121016Z-codex-eaa96f.yaml`

## Scope Reviewed

- Ran ignored/hidden-inclusive duplicate searches with
  `rg --no-ignore --hidden` for `GO:1990083`, `DnaA-Hda`, adjacent
  DnaA-L2/DnaA-Dps candidates, `GO:1990085` Hda-beta clamp, and
  `GO:1990078` replication inhibiting complex across `data/structures`,
  `history/records`, `reports/yaml_record_review`, `pages`, `README.md`, and
  `.gitignore`. The pre-PR searches found no existing standalone
  `GO:1990083`, `GO:1990085`, or `GO:1990078` records.
- Checked OLS metadata for `GO:1990083`: the term is an unrestricted GO
  cellular component named `DnaA-Hda complex`, is not obsolete, and cites
  `PMID:21708944` from its GO definition.
- Checked the OLS parent graph for `GO:1990083` and confirmed that
  `GO:1990078` replication inhibiting complex is its direct `is_a` parent.
- Checked OLS and QuickGO metadata for `GO:1990085` Hda-beta clamp complex;
  the term is separately scoped to Hda plus the DnaN beta clamp and cites
  `PMID:15150238`, so the beta clamp should remain out of `GO:1990083`
  components and graph edges.
- Checked PubMed metadata for `PMID:21708944` and DOI
  `10.1074/jbc.M111.233403`; the Keyamura and Katayama 2011 abstract directly
  supports the E. coli DnaA-Hda interaction and RIDA framing used for the
  component evidence, taxonomic row, canonical example, and regulatory graph.
- Checked PubMed metadata for `PMID:15150238` and DOI
  `10.1128/JB.186.11.3508-3515.2004`; Kurz et al. 2004 directly supports the
  neighboring Hda-beta clamp boundary in the resolved discussion.
- Checked that DnaA and Hda are left as `REVIEWED_LABEL_ONLY` components with
  no guessed InterPro, Pfam, NCBIfam, UniProtKB, or Complex Portal accessions.
- Checked that the graph remains `NONMECHANISTIC` and stops at GO-level
  DnaA-Hda composition supporting negative regulation of DNA replication
  initiation, without modeling DNA-loaded clamp binding or DnaA-ATP hydrolysis
  chemistry.

## Findings

No concrete defects found. No review issues were filed.

## Verification

- `uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/dnaa_hda_complex.yaml`
- `uv run python scripts/validate_strict.py --quiet data/structures/other/dnaa_hda_complex.yaml`
- `uv run python scripts/validate_history.py history/records/dnaa_hda_complex`
- `uv run python scripts/build_text_embedding_map.py --check`
- `uv run python scripts/render_pages.py --check`
- `uv run python scripts/check_docs.py --check`
- `uv run pytest tests/test_corpus_integrity.py::test_discussion_anchors_resolve`
- `uv run python scripts/validate_strict.py --quiet`
- `uv run python scripts/validate_history.py`
- `uv run python scripts/fetch_snippets.py --verify --check`
- `uv run python scripts/check_trait_links.py --check`
- `uv run python scripts/check_curies.py --check --report reports/curie_check.tsv`
- `uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `git diff --check`
- `just qc`
