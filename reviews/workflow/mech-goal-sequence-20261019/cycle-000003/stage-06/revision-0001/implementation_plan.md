# Cycle 3 Stage 6 Infrastructure Implementation Plan

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `3`
- **Stage**: `6` (`infrastructure`)
- **Revision**: `1`
- **Repository**: `CultureBotAI/CellStructureMech` (`cellstructuremech`)
- **Base Revision (`main`)**: `08473198b32bffce4520313807aea4527a788a7e`
- **Scope Frozen At**: `2026-10-25T13:48:26Z`
- **Frozen Snapshot Artifact**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-06/revision-0001/infra_snapshot.md`
- **Frozen Snapshot SHA-256**: `d9f903712f75f1a27d026d55a6216ad1bcaaef01560d26b1b2a843f2c44638e2`

## 1. Bounded Intake and Issue Mapping

At the Stage 6 cutoff (`2026-10-25T13:48:26Z`), `INFRA_TASKS.md` contained 6 infrastructure tasks in its machine-readable inventory: 5 tasks resolved in Cycles 1 and 2 (`cellstructuremech-infra-0001` through `cellstructuremech-infra-0005`) and 1 open task (`cellstructuremech-infra-0006`) captured during Cycle 3 Stage 4 (`record_review`) and linked to a real GitHub issue in `CultureBotAI/CellStructureMech`:

| Task ID | Originating Stage | GitHub Issue | Priority | Dependencies | Selected Action |
| --- | --- | --- | --- | --- | --- |
| `cellstructuremech-infra-0006` | Cycle 3, Stage 4 (`record_review`) | [#2428](https://github.com/CultureBotAI/CellStructureMech/issues/2428) | P2 | Builds on `src/cellstructuremech/validation/validator.py` (`#2408`, `#2410`, `#2417`) | Implement in Stage 6 (`resolved`) |

## 2. Dependency Analysis and Execution Plan

`cellstructuremech-infra-0006` (#2428) has no external blockers. It extends the repository's semantic record validator (`src/cellstructuremech/validation/validator.py`) to prevent three classes of curation drift identified during the Cycle 3 Stage 4 whole-corpus audit of all 993 structure records and remediated in Cycle 3 Stage 5 (`PR #2433`):

### Phase 1: Causal-Graph `component_ref` Grounding Propagation Check (`#2428`)
- **Targets**:
  - `src/cellstructuremech/validation/validator.py` (`validate_causal_graphs`)
- **Design**:
  1. In `validate_causal_graphs(doc)`, inspect every `CausalNode` carrying a `component_ref` that resolves to a declared component in `doc["components"]`.
  2. When the referenced component carries a non-empty `grounding` and the `CausalNode` omits `grounding` (unless the node's `description` explicitly discloses that it represents a sub-region carrying no grounding of its own, as in `ribosome.yaml`'s `23S rRNA peptidyl transferase centre`), emit a semantic validation error identifying the graph, node, `component_ref`, and missing grounding CURIE.
- **Acceptance Criteria**:
  - `validate_causal_graphs()` and `write_validated_structure()` reject `CausalNode` items with `component_ref` that omit `grounding` from a grounded target component.
  - All 993 corpus records under `data/structures/` pass `validate_causal_graphs()` with 0 errors.

### Phase 2: `CURATED_CAUSAL_GRAPH` `curation_history` Target `graph_id` Check (`#2428`)
- **Targets**:
  - `src/cellstructuremech/validation/validator.py` (`validate_curation_history`, `validate_record_semantics`)
- **Design**:
  1. Implement `validate_curation_history(doc)` and wire it into `validate_record_semantics(doc)`.
  2. For every entry in `doc["curation_history"]` with `action == "CURATED_CAUSAL_GRAPH"`, verify that the record declares at least one `causal_graphs` item and that any target causal-graph slug named in `changes` (`in <slug>`, `Enriched <slug>`, `causal graph <slug>`, or `causal_graphs (<slug>)`) resolves to a declared `causal_graphs[].graph_id` on the record.
- **Acceptance Criteria**:
  - `validate_curation_history()` and `write_validated_structure()` reject `CURATED_CAUSAL_GRAPH` history entries whose target `graph_id` does not match any `causal_graphs[].graph_id` on the record.
  - All 993 corpus records under `data/structures/` pass `validate_curation_history()` with 0 errors.

### Phase 3: `discussions` Prose `DOI` and `PMID` Citation Evidence Check (`#2428`)
- **Targets**:
  - `src/cellstructuremech/validation/validator.py` (`validate_discussion_issue_links`)
- **Design**:
  1. Extend `validate_discussion_issue_links(doc)` to include `notes` alongside `prompt`, `rationale`, `resolution_note`, and `text` when scanning discussion prose.
  2. Check that every `DOI` (`10.\d{4,9}/...`) or `PMID:\d+` citation mentioned in discussion prose is backed by a matching `reference` in that discussion's `evidence` list.
- **Acceptance Criteria**:
  - `validate_discussion_issue_links()` and `write_validated_structure()` reject `discussions` entries that cite a `DOI` or `PMID` in prose without a matching entry in `discussion.evidence`.
  - All 993 corpus records under `data/structures/` pass `validate_discussion_issue_links()` with 0 errors.

### Phase 4: Unit & Corpus Integrity Tests and Ledger Update
- **Targets**:
  - `tests/test_validator.py`
  - `tests/test_corpus_integrity.py`
  - `INFRA_TASKS.md`
  - `reviews/workflow/latest.yaml`
- **Acceptance Criteria**:
  - Unit tests in `tests/test_validator.py` cover `CausalNode` `component_ref` grounding propagation (`test_causal_node_component_ref_requires_grounding_propagation`), `CURATED_CAUSAL_GRAPH` target `graph_id` matching (`test_curated_causal_graph_history_target_must_match_record_graph_id`), and `discussions` prose `DOI`/`PMID` citation evidence (`test_discussion_referencing_doi_or_pmid_requires_structured_evidence`).
  - Corpus-integrity test `test_curated_causal_graph_history_targets_match_record_graphs` (alongside existing `test_causal_graphs_have_no_isolated_nodes_or_undescribed_edges` and `test_discussions_referencing_issues_carry_structured_issue_links`) in `tests/test_corpus_integrity.py` passes across all 993 records.
  - All 10 quality gates in `scripts/run_qc.py` pass with 0 errors.
  - `INFRA_TASKS.md` marks `cellstructuremech-infra-0006` as `resolved` with its disposition, and `reviews/workflow/latest.yaml` is updated from `verified-evidence-index.json` to include Cycle 3 Stage 5.

## 3. Carry-Forward and Deferred Tasks

- **Deferred / Blocked Tasks**: None (`0` tasks deferred or blocked; `cellstructuremech-infra-0006`, the sole open task in the frozen Stage 6 scope, is resolved in this goal).
