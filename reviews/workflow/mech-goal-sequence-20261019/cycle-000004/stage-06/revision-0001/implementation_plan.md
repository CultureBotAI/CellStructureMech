# Cycle 4 Stage 6 Infrastructure Implementation Plan

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `4`
- **Stage**: `6` (`infrastructure`)
- **Revision**: `1`
- **Repository**: `CultureBotAI/CellStructureMech` (`cellstructuremech`)
- **Base Revision (`main`)**: `6ba79ee3d9f23d0d754a91a9e558ef748a906c07`
- **Scope Frozen At**: `2026-10-30T13:29:08Z`
- **Frozen Snapshot Artifact**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-06/revision-0001/infra_snapshot.md`
- **Frozen Snapshot SHA-256**: `de7077b2c974fe53133e47b07b7be9bbb43e3045d20f7dfa8a90d3c597286f8d`

## 1. Bounded Intake and Issue Mapping

At the Stage 6 cutoff (`2026-10-30T13:29:08Z`), `INFRA_TASKS.md` contained 7 infrastructure tasks in its machine-readable inventory: 6 tasks resolved in Cycles 1–3 (`cellstructuremech-infra-0001` through `cellstructuremech-infra-0006`) and 1 open task (`cellstructuremech-infra-0007`) captured during Cycle 4 Stage 4 (`record_review`) and linked to a real GitHub issue in `CultureBotAI/CellStructureMech`:

| Task ID | Originating Stage | GitHub Issue | Priority | Dependencies | Selected Action |
| --- | --- | --- | --- | --- | --- |
| `cellstructuremech-infra-0007` | Cycle 4, Stage 4 (`record_review`) | [#2457](https://github.com/CultureBotAI/CellStructureMech/issues/2457) | P2 | Builds on `src/cellstructuremech/validation/validator.py` (`#2408`, `#2410`, `#2417`, `#2428`) | Implement in Stage 6 (`resolved`) |

## 2. Dependency Analysis and Execution Plan

`cellstructuremech-infra-0007` (#2457) has no external blockers. It extends the repository's semantic record validator (`src/cellstructuremech/validation/validator.py`) to prevent two classes of curation drift identified during the Cycle 4 Stage 4 whole-corpus audit of all 1,001 structure records and remediated in Cycle 4 Stage 5 (`PR #2464`):

### Phase 1: Hierarchy, Parthood, and Constituent Relation Disjointness Check (`#2457`)
- **Targets**:
  - `src/cellstructuremech/validation/validator.py` (`validate_hierarchy_relations`, `validate_record_semantics`)
- **Design**:
  1. Implement `validate_hierarchy_relations(doc)` and wire it into `validate_record_semantics(doc)`.
  2. Flag any record where the same CURIE appears in more than one of `parent_structures` (is-a), `part_of` (parthood), and `has_part`.
  3. Flag any `components[]` entry with `component_role == "CONSTITUENT"` whose `grounding` CURIE also appears in `parent_structures` or `part_of` on the same record.
- **Acceptance Criteria**:
  - `validate_hierarchy_relations()` and `write_validated_structure()` reject records with overlapping `parent_structures`, `part_of`, `has_part`, or `CONSTITUENT` `components[].grounding` CURIEs.
  - All 1,001 corpus records under `data/structures/` pass `validate_hierarchy_relations()` with 0 errors.

### Phase 2: `CausalNode` `component_ref` Grounding and Type Consistency Check (`#2457`)
- **Targets**:
  - `src/cellstructuremech/validation/validator.py` (`validate_causal_graphs`)
- **Design**:
  1. In `validate_causal_graphs(doc)`, inspect every `CausalNode` carrying a `component_ref` that resolves to a declared component in `doc["components"]`.
  2. Flag `CausalNode` entries with `node_type == "STRUCTURE"` when the referenced component has `component_type == "PROTEIN"`.
  3. Flag `CausalNode` entries with `component_ref` where both `node.grounding` and `referenced_component.grounding` are present and `node.grounding != referenced_component.grounding`.
- **Acceptance Criteria**:
  - `validate_causal_graphs()` and `write_validated_structure()` reject `CausalNode` items with `component_ref` that conflict with `referenced_component.grounding` or use `node_type: STRUCTURE` for a `PROTEIN` component.
  - All 1,001 corpus records under `data/structures/` pass `validate_causal_graphs()` with 0 errors.

### Phase 3: Unit & Corpus Integrity Tests and Ledger Update
- **Targets**:
  - `tests/test_validator.py`
  - `tests/test_corpus_integrity.py`
  - `INFRA_TASKS.md`
  - `reviews/workflow/latest.yaml`
- **Acceptance Criteria**:
  - Unit tests in `tests/test_validator.py` cover hierarchy/component relation disjointness (`test_hierarchy_relation_disjointness`) and `CausalNode` `component_ref` grounding and type consistency (`test_causal_node_component_ref_grounding_and_type_consistency`).
  - Corpus-integrity test `test_hierarchy_and_component_relations_are_disjoint` (alongside existing `test_causal_graphs_have_no_isolated_nodes_or_undescribed_edges`) in `tests/test_corpus_integrity.py` passes across all 1,001 records.
  - All 10 quality gates in `scripts/run_qc.py` pass with 0 errors.
  - `INFRA_TASKS.md` marks `cellstructuremech-infra-0007` as `resolved` with its disposition, and `reviews/workflow/latest.yaml` is updated from `verified-evidence-index.json` to include Cycle 4 Stage 5.

## 3. Carry-Forward and Deferred Tasks

- **Deferred / Blocked Tasks**: None (`0` tasks deferred or blocked; `cellstructuremech-infra-0007`, the sole open task in the frozen Stage 6 scope, is resolved in this goal).
