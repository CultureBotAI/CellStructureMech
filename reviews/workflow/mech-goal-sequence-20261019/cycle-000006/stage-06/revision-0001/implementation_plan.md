# Cycle 6 Stage 6 Infrastructure Implementation Plan

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `6`
- **Stage**: `6` (`infrastructure`)
- **Revision**: `1`
- **Repository**: `CultureBotAI/CellStructureMech` (`cellstructuremech`)
- **Base Revision (`main`)**: `6b1e9f0aec2b18ce38f6e48e83a8464a2c0e172a`
- **Scope Frozen At**: `2026-10-31T16:42:06Z`
- **Frozen Snapshot Artifact**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000006/stage-06/revision-0001/infra_snapshot.md`
- **Frozen Snapshot SHA-256**: `eff06ec8760db8b15ca0b7bd2f3afd18e1d35b3d0870f464c05b492c8ce1cc0a`

## 1. Bounded Intake and Issue Mapping

At the Stage 6 cutoff (`2026-10-31T16:42:06Z`), `INFRA_TASKS.md` contained 9 infrastructure tasks in its machine-readable inventory: 8 tasks resolved in Cycles 1–5 (`cellstructuremech-infra-0001` through `cellstructuremech-infra-0008`) and 1 open task (`cellstructuremech-infra-0009`) captured during Cycle 6 Stage 4 (`record_review`) and linked to a real GitHub issue in `CultureBotAI/CellStructureMech`:

| Task ID | Originating Stage | GitHub Issue | Priority | Dependencies | Selected Action |
| --- | --- | --- | --- | --- | --- |
| `cellstructuremech-infra-0009` | Cycle 6, Stage 4 (`record_review`) | [#2486](https://github.com/CultureBotAI/CellStructureMech/issues/2486) | P2 | Builds on `src/cellstructuremech/validation/validator.py` (`#2408`, `#2410`, `#2417`, `#2428`, `#2457`, `#2472`) | Implement in Stage 6 (`resolved`) |

## 2. Dependency Analysis and Execution Plan

`cellstructuremech-infra-0009` ([#2486](https://github.com/CultureBotAI/CellStructureMech/issues/2486)) has no external blockers. It extends the repository's semantic record validator (`src/cellstructuremech/validation/validator.py`) to prevent two classes of curation drift identified during the Cycle 6 Stage 4 whole-corpus audit of all 1,015 structure records and remediated in Cycle 6 Stage 5 (`PR #2491`):

### Phase 1: Top-Level `PMID:` Evidence Parity Check (`#2486`)
- **Targets**:
  - `src/cellstructuremech/validation/validator.py` (`validate_top_level_pmid_parity`, `validate_record_semantics`)
- **Design**:
  1. Add `validate_top_level_pmid_parity(doc)` and wire it into `validate_record_semantics(doc)`.
  2. When a record's top-level `evidence` cites primary literature `PMID:` references (`len(top_dois) <= len(top_pmids)` and not a legacy `CHEBI:` cofactor-enumeration top-level evidence list), collect all `PMID:` references present in top-level `evidence` or `components[].protein_examples[].evidence`.
  3. Inspect `components[].evidence`, `taxonomic_distribution[].reference`, `functions[].evidence`, and `causal_graphs[].edges[].evidence` (outside `discussions` and `curation_history`), and flag any primary `PMID:` reference omitted from top-level `evidence` (allowing secondary companion citations with inline `DOI:10.` in `notes` when a sibling `PMID:` in the same `evidence` list is covered).
- **Acceptance Criteria**:
  - `validate_top_level_pmid_parity()` and `write_validated_structure()` reject records whose top-level `evidence` cites `PMID:` references while omitting primary `PMID:` references cited in `components`, `taxonomic_distribution`, `functions`, or `causal_graphs` (such as `sid2_mob1_complex.yaml` `PMID:11069087`, `potassium_ion_transporting_atpase_complex.yaml` `PMID:4241429`, `atg12_atg5_atg16_complex.yaml` `PMID:10611963`, and `cobalamin_transport_complex.yaml` `PMID:12000972` prior to `#2491`).
  - All 1,015 corpus records under `data/structures/` pass `validate_top_level_pmid_parity()` with 0 errors.

### Phase 2: 2-Node, 1-Edge Parthood-Only `STRUCTURE` `CausalGraph` `scope_status` Check (`#2486`)
- **Targets**:
  - `src/cellstructuremech/validation/validator.py` (`validate_causal_graphs`)
- **Design**:
  1. In `validate_causal_graphs(doc)`, inspect each `CausalGraph` on non-`SUBCELLULAR_REGION` records (`doc.get("structure_kind") != "SUBCELLULAR_REGION"`).
  2. When `scope_status == "MECHANISTIC"`, `len(nodes) == 2`, `len(edges) == 1`, both nodes have `node_type == "STRUCTURE"`, and the sole edge `predicate` is in `{"is part of", "part_of", "BFO:0000050"}`, emit an error requiring `scope_status` to be `'NONMECHANISTIC'` or `'INCOMPLETE'`.
- **Acceptance Criteria**:
  - `validate_causal_graphs()` and `write_validated_structure()` reject 2-node, 1-edge `STRUCTURE` graphs whose sole edge is `"is part of"` / `part_of` when marked `scope_status: MECHANISTIC` (such as `reservosome_membrane.yaml` `reservosome_membrane_parthood` prior to `#2491`).
  - All 1,015 corpus records under `data/structures/` pass `validate_causal_graphs()` with 0 errors.

### Phase 3: Unit & Corpus Integrity Tests and Ledger Update
- **Targets**:
  - `tests/test_validator.py`
  - `tests/test_corpus_integrity.py`
  - `INFRA_TASKS.md`
  - `reviews/workflow/latest.yaml`
- **Acceptance Criteria**:
  - Unit tests in `tests/test_validator.py` cover top-level `PMID:` evidence parity (`test_top_level_pmid_evidence_parity_is_enforced`) and 2-node parthood-only `STRUCTURE` causal graphs (`test_two_node_parthood_only_structure_causal_graph_marked_mechanistic_is_flagged`).
  - Corpus-integrity tests `test_top_level_pmid_evidence_parity` and `test_causal_graphs_have_no_isolated_nodes_or_undescribed_edges` in `tests/test_corpus_integrity.py` pass across all 1,015 records.
  - All 10 quality gates in `scripts/run_qc.py` pass with 0 errors.
  - `INFRA_TASKS.md` marks `cellstructuremech-infra-0009` as `resolved` with its disposition, and `reviews/workflow/latest.yaml` is updated from `verified-evidence-index.json` to include Cycle 6 Stage 5.

## 3. Carry-Forward and Deferred Tasks

- **Deferred / Blocked Tasks**: None (`0` tasks deferred or blocked; `cellstructuremech-infra-0009`, the sole open task in the frozen Stage 6 scope, is resolved in this goal).
