# SsuD-SsuE complex record review

## Scope

- PR: https://github.com/CultureBotAI/CellStructureMech/pull/1880
- Record: `data/structures/other/ssud_ssue_complex.yaml`
- Identifier: `GO:1990200`
- Label: `SsuD-SsuE complex`

## Checks

- Re-ran a hidden/ignored-inclusive duplicate search for `GO:1990200`, the
  `SsuD-SsuE complex` label, the GO related synonym, GO-cited PMIDs/DOIs, and
  the E. coli K-12 SsuD/SsuE UniProt accessions; no prior record or review report
  already covered this exact structure.
- Checked QuickGO and OLS metadata for `GO:1990200`; the term is active,
  cellular-component-scoped, named `SsuD-SsuE complex`, and carries the related
  `two-component alkanesulfonate monooxygenase system` synonym used in the record.
- Checked QuickGO parentage for `GO:1990200`; `GO:0032991`
  `protein-containing complex` is a direct `is_a` parent.
- Checked QuickGO `GO:0008726`; the function label
  `alkanesulfonate monooxygenase activity` is active and matches the curated
  function grounding.
- Checked InterPro `IPR020048`; it is a family entry for
  `NADPH-dependent FMN reductase, SsuE`, matching the SsuE component grounding.
- Checked InterPro `IPR050172`; it is the broader `SsuD/RutA monooxygenase`
  family and is therefore correctly cited only as a declined exact grounding for
  SsuD.
- Checked UniProtKB `P80645` and `P80644`; both are reviewed E. coli K-12
  entries for `ssuD` and `ssuE`, respectively.
- Checked PubMed metadata for `PMID:10480865` and `PMID:16997955`; the former
  characterizes the E. coli SsuD/SsuE two-component monooxygenase and the latter
  reports direct SsuD/SsuE interaction evidence.
- Confirmed the first record does not overclaim an assembled six-subunit count:
  the record leaves stoichiometry unset and records the isolated-oligomer versus
  proposed interaction-stoichiometry boundary decision.
- Confirmed regenerated embedding, README, and page artifacts contain the new
  record and no unrelated hand-authored changes.

## Local Validation

- `linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/ssud_ssue_complex.yaml`
- `python scripts/validate_strict.py --quiet data/structures/other/ssud_ssue_complex.yaml`
- `python scripts/validate_strict.py --quiet`
- `python scripts/validate_history.py history/records/ssud_ssue_complex/2026-10-01T174630Z-codex-cfa1b6.yaml`
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
