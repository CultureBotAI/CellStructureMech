# Cycle 1 Stage 5 Validation & Post-Remediation Review Report

## Validation Commands Executed

1. **Validated Record Formatting & Closed-Mode Write Gate (`write_validated_structure`)**
   - Command: `.venv/bin/python -m pytest -q -o cache_dir=/tmp/pytest_cache tests/test_write_validated.py`
   - Result: `24 passed` (`test_every_record_round_trips_byte_identically` verified across all 978 records).

2. **Strict Schema & Semantic Validation (`scripts/validate_strict.py`)**
   - Command: `.venv/bin/python scripts/validate_strict.py --quiet --out /tmp/instance_validation_failures.tsv`
   - Result: `files scanned: 978, files with ERROR: 0, total ERROR rows: 0`.

3. **ID-Label Correspondence (`scripts/validate_id_label_correspondence.py`)**
   - Command: `.venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
   - Result: `OK_CANONICAL: 3982, OK_SYNONYM: 50, OK_EXCEPTION: 6, SKIPPED_NO_ADAPTER: 659 — All id↔label pairs correspond.`

4. **UniProt Protein Examples & Causal-Graph Xrefs (`scripts/uniprot_genes.py --verify`)**
   - Command: `.venv/bin/python scripts/uniprot_genes.py --verify`
   - Result: `all UniProtKB protein_examples and causal_graphs xrefs verified ok`.

5. **Repository History Ledger Links & LinkML `HistoryRecord` Validation (`scripts/validate_history_links.py` & `linkml.validator`)**
   - Command: `.venv/bin/python scripts/validate_history_links.py history`
   - Result: `history links: 1921 record(s), 0 invalid`; all new `2026-10-23` history files and backfilled `woronin_body` files validated with 0 errors against `src/cellstructuremech/schema/history.yaml` (`HistoryRecord`).

6. **Derived Site Synchronization (`scripts/render_pages.py --check`)**
   - Command: `.venv/bin/python scripts/render_pages.py --check`
   - Result: `pages/ is current` (digest `f6e25438d424`, 978 records).

7. **Corpus-Wide Quality Suite (`ruff`, `check_docs.py`, `check_source_queue.py`, `check_pathway_links.py`, `build_text_embedding_map.py --check`, `corpus_report.py`, and `pytest`)**
   - Result: All checks passed (`1051 passed, 3 skipped` across the pytest suite).

8. **Post-Remediation Native Structured Review (`scripts/record_review.py`)**
   - Saved Bundle: `reviews/structured/20261023T114600Z-stage5-remediation-verification/review.yaml` (SHA256 `82cb13bad1f7c75c6de8c4a930c65a4b704a18b8981722e8a28f6b526422cb8e`) and `review.md` (SHA256 `c663622ca6033c153ef3a6310f48d8b77d3faf80f419ca93fc8fb3167c6f35ed`).
   - Git Revision Inspected: `9dd9935ee1cf1d85454d42df0cec7da12f550a79` (`state: git_commit`).
   - Verdict: `pass` (`native_verdict: PASS`, `findings: []`, 16/16 target records verified).
   - Immutability Check: All Stage 4 review bundles (`20261023T091801Z` through `20261023T091807Z`) and `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/` remain byte-identical.
