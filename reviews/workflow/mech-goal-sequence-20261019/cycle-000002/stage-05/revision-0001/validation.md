# Cycle 2 Stage 5 — Validation Summary

- **Remediation Commit:** `99e590eb7afb0e8251f6e81183e59ca1119987b9`
- **Post-Remediation Structured Review Bundle:** `reviews/structured/20261024T004000Z-c2-stage5-remediation-verification/review.yaml`

## Validation Gates Executed

| Gate | Command | Result |
| --- | --- | --- |
| Strict corpus validation | `.venv/bin/python scripts/validate_strict.py` | **PASSED** (`files scanned: 985, files with ERROR: 0, total ERROR rows: 0`) |
| Ontology ID↔label correspondence | `.venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml` | **PASSED** (`OK_CANONICAL: 4023, OK_SYNONYM: 50, OK_EXCEPTION: 6, SKIPPED_NO_ADAPTER: 685 — All id↔label pairs correspond.`) |
| UniProtKB protein_examples & xrefs | `.venv/bin/python scripts/uniprot_genes.py --verify` | **PASSED** (`all UniProtKB protein_examples and causal_graphs xrefs verified ok`) |
| History links & LinkML `HistoryRecord` schema | `.venv/bin/python scripts/validate_history.py` | **PASSED** (`history links: 1991 record(s), 0 invalid; 1991 history record(s) valid against src/cellstructuremech/schema/history.yaml`) |
| Static page synchronization | `.venv/bin/python scripts/render_pages.py --check` | **PASSED** (`pages/ is current`) |
| Structured review bundle check | `.venv/bin/python scripts/record_review.py validate reviews/structured/20261024T004000Z-c2-stage5-remediation-verification/review.yaml && .venv/bin/python scripts/record_review.py check` | **PASSED** (`ok: 270 review bundle(s) valid`) |
| Pytest suite | `.venv/bin/python -m pytest -q` | **PASSED** (`1065 passed, 3 skipped`) |

## Immutability Verification of Stage 4 Review Artifacts

All 6 Stage 4 structured review bundles (`20261023T230501Z-clathrin-coat-ap2-causal-node-type` through `20261023T230506Z-microcompartment-category-review`) and `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-04/revision-0001/evidence.yaml` (`sha256: d82e8d95fbabf37450deff6a3de9169f52b4e6b6af66536d101b5abf3673f945`) remain byte-identical.
