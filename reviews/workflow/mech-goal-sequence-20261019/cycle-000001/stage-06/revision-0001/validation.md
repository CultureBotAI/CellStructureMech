# Cycle 1 Stage 6 Infrastructure Validation Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `1`
- **Stage**: `6` (`infrastructure`)
- **Revision**: `1`
- **Repository**: `CultureBotAI/CellStructureMech` (`cellstructuremech`)
- **Scope Frozen At**: `2026-10-23T12:41:41Z`
- **Frozen Snapshot**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-06/revision-0001/infra_snapshot.md` (`d8ee261ed2d5eac92afc87e14ee9f8abdf042930f749afa72c5ecc97fd763f02`)

## 1. Per-Task Implementation and Unit Test Verification

| Task ID | GitHub Issue | Implemented Modules | Unit & Corpus Tests | Outcome |
| --- | --- | --- | --- | --- |
| `cellstructuremech-infra-0001` | [#2407](https://github.com/CultureBotAI/CellStructureMech/issues/2407) | `scripts/validate_history.py` (`resolve_linkml_validate`, `run_linkml_validate`) | `tests/test_new_history_record.py` (`test_resolve_linkml_validate_prefers_sibling_of_sys_executable`, `test_resolve_linkml_validate_falls_back_to_shutil_which`) + direct `.venv/bin/python scripts/run_qc.py` execution without `.venv/bin` on `PATH` | **Pass** |
| `cellstructuremech-infra-0002` | [#2408](https://github.com/CultureBotAI/CellStructureMech/issues/2408) | `src/cellstructuremech/validation/validator.py` (`validate_causal_graphs`, `validate_record_semantics`), `src/cellstructuremech/validation/write_validated.py`, `scripts/validate_strict.py` | `tests/test_validator.py` (`test_connected_graph_with_edge_descriptions_passes`, `test_isolated_causal_node_is_flagged_and_blocks_write`, `test_causal_edge_missing_or_blank_description_is_flagged`), `tests/test_corpus_integrity.py` (`test_causal_graphs_have_no_isolated_nodes_and_all_edges_have_descriptions`) | **Pass** (0 isolated nodes, 0 description-less edges across 947 causal graphs and 4,190 edges in 978 records) |
| `cellstructuremech-infra-0003` | [#2409](https://github.com/CultureBotAI/CellStructureMech/issues/2409) | `scripts/uniprot_genes.py` (`_component_in_scope`, `NON_PROTEIN_COMPONENT_TYPES`, `candidates`, `gap_report`, `cmd_gaps`, `plan_record`, `seed_records`, `--include-non-protein`) | `tests/test_uniprot_genes.py` (`TestComponentInScopeAndSeedRecords`: 6 unit tests covering `OTHER` components with `gene_symbols`, `--include-complexes`, `--include-non-protein`, and `seed_records` preserving `component_type`) | **Pass** |
| `cellstructuremech-infra-0004` | [#2410](https://github.com/CultureBotAI/CellStructureMech/issues/2410) | `scripts/validate_history.py` (`check_structure_history_coverage`, `LEGACY_BATCH_HISTORY_SLUGS`), `src/cellstructuremech/validation/validator.py` (`validate_discussion_issue_links`, `validate_record_semantics`) | `tests/test_new_history_record.py` (`test_structure_history_1_to_1_coverage_check`), `tests/test_validator.py` (`test_discussion_referencing_issue_in_prose_requires_structured_issue_evidence`), `tests/test_corpus_integrity.py` (`test_discussions_referencing_issues_in_prose_have_structured_issue_links`, `test_every_structure_record_has_history_ledger`) | **Pass** (all 978 structure records covered 1:1 in `history/records/<slug>/`; 0 unlinked `#NNN` discussion prose mentions) |

## 2. Full Authoritative Quality Gate Suite (`.venv/bin/python scripts/run_qc.py`)

Executed `.venv/bin/python scripts/run_qc.py` directly without `.venv/bin` prepended to `PATH`:

1. **`lint`** (`.venv/bin/python -m ruff check .`): `All checks passed!`
2. **`documentation`** (`.venv/bin/python scripts/check_docs.py --check`): `README.md corpus block is current`
3. **`source queue`** (`.venv/bin/python scripts/check_source_queue.py`): `source queue OK: 26 sources — 17 adopted, 1 blocked, 5 candidate, 3 rejected`
4. **`pathway links`** (`.venv/bin/python scripts/check_pathway_links.py`): `OK: 6 pathway links match the pinned target snapshot`
5. **`text embedding map`** (`.venv/bin/python scripts/build_text_embedding_map.py --check`): `text embedding map is current: 978 records, 384 dimensions, sentence-transformers/all-MiniLM-L6-v2`
6. **`tests`** (`.venv/bin/python -m pytest -q`): `1065 passed, 3 skipped in 617.16s`
7. **`history records`** (`.venv/bin/python scripts/validate_history.py`): `history links: 1921 record(s), 0 invalid; No issues found; 1921 history record(s) valid against src/cellstructuremech/schema/history.yaml`
8. **`schema validation`** (`.venv/bin/python scripts/validate_strict.py --quiet`): `files scanned: 978, files with ERROR: 0, total ERROR rows: 0`
9. **`generated site`** (`.venv/bin/python scripts/render_pages.py --check`): `pages/ is current`
10. **`corpus report`** (`.venv/bin/python scripts/corpus_report.py`): `978 structure records (829 GO, 149 CSM; 804 with components, 784 with functions, 947 with causal graphs / 4,190 edges)`

Result: `All CellStructureMech quality gates passed.` (exit code `0`).
