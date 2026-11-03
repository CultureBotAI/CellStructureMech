# Cycle 3 Stage 5 — Validation Summary

- **Remediation Commit:** `02e1550e1bcbb1b6d90762e1d83c9ac6ab5b1190`
- **Post-Remediation Structured Review Bundle:** `reviews/structured/20261025T122500Z-c3-stage5-remediation-verification/review.yaml` (`sha256: a135f495b6741cec26fd22368bab479d795150b6214e246d0431a0d6496418a1`)

## Validation Gates Executed

| Gate | Command | Result |
| --- | --- | --- |
| Strict corpus validation | `.venv/bin/python scripts/validate_strict.py` | **PASSED** (`files scanned: 993, files with ERROR: 0, total ERROR rows: 0`) |
| Ontology ID↔label correspondence | `.venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml` | **PASSED** (`OK_CANONICAL: 4064, OK_SYNONYM: 50, OK_EXCEPTION: 6, SKIPPED_NO_ADAPTER: 740 — All id↔label pairs correspond.`) |
| UniProtKB protein_examples & xrefs | `.venv/bin/python scripts/uniprot_genes.py --verify` | **PASSED** (`all UniProtKB protein_examples and causal_graphs xrefs verified ok`) |
| Offline CURIE liveness check | `.venv/bin/python scripts/check_curies.py --offline --check` | **PASSED** (`OK: 5776, SKIPPED: 252 — Every identifier resolves at its issuing authority.`) |
| History links & LinkML `HistoryRecord` schema | `.venv/bin/python scripts/validate_history.py` | **PASSED** (`history links: 2057 record(s), 0 invalid; 2057 history record(s) valid against src/cellstructuremech/schema/history.yaml`) |
| Static page synchronization | `.venv/bin/python scripts/render_pages.py --check` | **PASSED** (`pages/ is current`) |
| Vendored governance sync | `bash scripts/check_vendored_sync.sh` | **PASSED** (`OK: 22 governed artifacts match the pinned claw revision`) |
| Structured review bundle check | `.venv/bin/python scripts/record_review.py validate reviews/structured/20261025T122500Z-c3-stage5-remediation-verification/review.yaml && .venv/bin/python scripts/record_review.py check --require-reviews --base main` | **PASSED** (`294 review bundle(s) valid; all 36 modified records covered by post-remediation review`) |

## Immutability Verification of Stage 4 Review Artifacts

All 13 Stage 4 structured review bundles (`20261025T071001Z-static-microtubule-bundle-reference-attribution` through `20261025T071013Z-spore-category-review`) and `reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-04/revision-0001/evidence.yaml` (`sha256: 5c9d063bb0b141b352ef104a9e33ce39b7aa2ba418e55f76fe195e7d6fbae2d0`) remain byte-identical.
