# Cycle 4 Stage 5 — Validation Summary

- **Remediation Commit:** `31fd33d9556ea5627b36d50ab608ccb9464f9353`
- **Post-Remediation Structured Review Bundle:** `reviews/structured/20261030T122500Z-c4-stage5-remediation-verification/review.yaml` (`sha256: 92b533c9903987b0e70e1d7ebbe188fe7880d52cfa63b4379c7310a8cb29aa4f`)

## Validation Gates Executed

| Gate | Command | Result |
| --- | --- | --- |
| Strict corpus validation | `.venv/bin/python scripts/validate_strict.py` | **PASSED** (`files scanned: 1001, files with ERROR: 0, total ERROR rows: 0`) |
| Ontology ID↔label correspondence | `.venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml` | **PASSED** (`OK_CANONICAL: 4103, OK_SYNONYM: 50, OK_EXCEPTION: 6, SKIPPED_NO_ADAPTER: 792 — All id↔label pairs correspond.`) |
| UniProtKB protein_examples & xrefs | `.venv/bin/python scripts/uniprot_genes.py --verify` | **PASSED** (`all UniProtKB protein_examples and causal_graphs xrefs verified ok`) |
| Offline CURIE liveness check | `.venv/bin/python scripts/check_curies.py --offline --check` | **PASSED** (`OK: 5858, SKIPPED: 252 — Every identifier resolves at its issuing authority.`) |
| History links & LinkML `HistoryRecord` schema | `.venv/bin/python scripts/validate_history.py` | **PASSED** (`history links: 2101 record(s), 0 invalid; 2101 history record(s) valid against src/cellstructuremech/schema/history.yaml`) |
| Static page synchronization | `.venv/bin/python scripts/render_pages.py --check` | **PASSED** (`pages/ is current`) |
| README statistics block | `.venv/bin/python scripts/check_docs.py --check` | **PASSED** (`README.md corpus block is current`) |
| Text embedding map | `.venv/bin/python scripts/build_text_embedding_map.py --check` | **PASSED** (`text embedding map is current: 1001 records, 384 dimensions`) |
| Vendored governance sync | `bash scripts/check_vendored_sync.sh` | **PASSED** (`OK: 22 governed artifacts match the pinned claw revision`) |
| Structured review bundle check | `.venv/bin/python scripts/record_review.py validate reviews/structured/20261030T122500Z-c4-stage5-remediation-verification/review.yaml && .venv/bin/python scripts/record_review.py check --require-reviews --base main` | **PASSED** (`314 review bundle(s) valid; all 19 modified records covered by post-remediation review`) |

## Immutability Verification of Stage 4 Review Artifacts

All 11 Stage 4 structured review bundles (`20261030T082001Z-ftsqbl-complex-parent-partof-duplication` through `20261030T082011Z-secretion-system-category-review`) and `reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-04/revision-0001/evidence.yaml` (`sha256: 898a10c8ecaef3546e1c415c2f64dbb2a33cc62161793db073d6866f7f1ca5aa`) remain byte-identical.
