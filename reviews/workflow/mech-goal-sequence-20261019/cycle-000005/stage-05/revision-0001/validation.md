# Cycle 5 Stage 5 — Validation Summary

- **Remediation Commit:** `c4a8f347c314b5601cad86c334497d5aca756640`
- **Post-Remediation Structured Review Bundle:** `reviews/structured/20261031T012000Z-c5-stage5-remediation-verification/review.yaml` (`sha256: 7058ca363b7d34269f3bd0993273db04445ed3369109a6cbe1d312d90dc04de9`)

## Validation Gates Executed

| Gate | Command | Result |
| --- | --- | --- |
| Strict corpus validation | `.venv/bin/python scripts/validate_strict.py` | **PASSED** (`files scanned: 1008, files with ERROR: 0, total ERROR rows: 0`) |
| Ontology ID↔label correspondence | `.venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml` | **PASSED** (`OK_CANONICAL: 4139, OK_SYNONYM: 50, OK_EXCEPTION: 6, SKIPPED_NO_ADAPTER: 838 — All id↔label pairs correspond.`) |
| UniProtKB protein_examples & xrefs (remediated cohort) | `.venv/bin/python scripts/uniprot_genes.py --verify --record <path>` | **PASSED** (`0 issues across all 10 remediated records`) |
| Offline CURIE liveness check | `.venv/bin/python scripts/check_curies.py --offline --check` | **PASSED** (`OK: 5952, SKIPPED: 254 — Every identifier resolves at its issuing authority.`) |
| History links & LinkML `HistoryRecord` schema | `.venv/bin/python scripts/validate_history.py history` | **PASSED** (`history links: 2153 record(s), 0 invalid; 2153 history record(s) valid against src/cellstructuremech/schema/history.yaml`) |
| Static page synchronization | `.venv/bin/python scripts/render_pages.py --check` | **PASSED** (`pages/ is current`) |
| README statistics block | `.venv/bin/python scripts/check_docs.py --check` | **PASSED** (`README.md corpus block is current`) |
| Text embedding map | `.venv/bin/python scripts/build_text_embedding_map.py --check` | **PASSED** (`text embedding map is current: 1008 records, 384 dimensions`) |
| Vendored governance sync | `bash scripts/check_vendored_sync.sh` | **PASSED** (`OK: 22 governed artifacts match the pinned claw revision`) |
| Structured review bundle check | `.venv/bin/python scripts/record_review.py validate reviews/structured/20261031T012000Z-c5-stage5-remediation-verification/review.yaml && .venv/bin/python scripts/record_review.py check --require-reviews --base main` | **PASSED** (`320 review bundle(s) valid; all 10 modified records covered by post-remediation review`) |

## Immutability Verification of Stage 4 Review Artifacts

All 5 Stage 4 structured review bundles (`20261031T003001Z-post-anaphase-microtubule-array-emtoc-gene-symbols` through `20261031T003005Z-other-category-review`) and `reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-04/revision-0001/evidence.yaml` (`sha256: 008cce72cea1a120bfef359392a32f3930ae39fa3af2b47ef9f79bda7608df12`) remain byte-identical.
