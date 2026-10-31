# Cycle 6 Stage 5 — Validation Summary

- **Remediation Commit:** `c0423878c9544a29b0db748b5f228b081d978f92`
- **Post-Remediation Structured Review Bundle:** `reviews/structured/20261031T155500Z-c6-stage5-remediation-verification/review.yaml` (`sha256: a5cf3b7885d640f7d73bc97d69b539fa7af788362e7439c0be95688d29afa83f`)

## Validation Gates Executed

| Gate | Command | Result |
| --- | --- | --- |
| Full quality gate (`just qc`) | `.venv/bin/python scripts/run_qc.py` | **PASSED** (`lint`, `documentation`, `source queue`, `pathway links`, `text embedding map`, `tests` [1079 passed, 3 skipped], `history records` [2204 valid], `schema validation` [1015 files, 0 ERROR], `generated site` [`pages/ is current`], `corpus report`) |
| Strict corpus validation | `.venv/bin/python scripts/validate_strict.py --quiet` | **PASSED** (`files scanned: 1015, files with ERROR: 0, total ERROR rows: 0`) |
| Ontology ID↔label correspondence | `.venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml` | **PASSED** (`OK_CANONICAL: 4182, OK_SYNONYM: 50, OK_EXCEPTION: 9, SKIPPED_NO_ADAPTER: 887 — All id↔label pairs correspond.`) |
| Strict CURIE liveness check | `.venv/bin/python scripts/check_curies.py --check --report reports/curie_check.tsv` | **PASSED** (`OK: 6068, SKIPPED: 254 — Every identifier resolves at its issuing authority.`) |
| TraitMech link check | `.venv/bin/python scripts/check_trait_links.py --check` | **PASSED** (`10 trait link(s): 10 resolve with a matching label, 0 missing, 0 mislabelled`) |
| History links & LinkML `HistoryRecord` schema | `.venv/bin/python scripts/validate_history.py history` | **PASSED** (`history links: 2204 record(s), 0 invalid; 2204 history record(s) valid against src/cellstructuremech/schema/history.yaml`) |
| Static page synchronization | `.venv/bin/python scripts/render_pages.py --check` | **PASSED** (`pages/ is current`) |
| README statistics block | `.venv/bin/python scripts/check_docs.py --check` | **PASSED** (`README.md corpus block is current`) |
| Text embedding map | `.venv/bin/python scripts/build_text_embedding_map.py --check` | **PASSED** (`text embedding map is current: 1015 records, 384 dimensions`) |
| Vendored governance sync | `bash scripts/check_vendored_sync.sh` | **PASSED** (`OK: 22 governed artifacts match the pinned claw revision`) |
| Structured review bundle check | `.venv/bin/python scripts/record_review.py validate reviews/structured/20261031T155500Z-c6-stage5-remediation-verification/review.yaml && .venv/bin/python scripts/record_review.py check --require-reviews --base main` | **PASSED** (`all retained review bundles valid; all 12 modified records covered by post-remediation review`) |

## Immutability Verification of Stage 4 Review Artifacts

All 6 Stage 4 structured review bundles (`20261031T123501Z-sid2-mob1-complex-review` through `20261031T123506Z-other-category-review`) and `reviews/workflow/mech-goal-sequence-20261019/cycle-000006/stage-04/revision-0001/evidence.yaml` (`sha256: ba3e8d38c2d0d9f8f3376bf70cae924a97685b4fa7c3cbc959613dd70c5992a5`) remain byte-identical.
