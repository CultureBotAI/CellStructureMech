# Cycle 2 Stage 6 Infrastructure Implementation Plan

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `2`
- **Stage**: `6` (`infrastructure`)
- **Revision**: `1`
- **Repository**: `CultureBotAI/CellStructureMech` (`cellstructuremech`)
- **Base Revision (`main`)**: `ef2bb4d5c3ec8f83b02376510569b2186a2522d6`
- **Scope Frozen At**: `2026-10-24T01:33:57Z`
- **Frozen Snapshot Artifact**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-06/revision-0001/infra_snapshot.md`
- **Frozen Snapshot SHA-256**: `ad2c3350ee2e7036ee1774b2f1ba620acab11a9b336898fefae3bbb71bba7d52`

## 1. Bounded Intake and Issue Mapping

At the Stage 6 cutoff (`2026-10-24T01:33:57Z`), `INFRA_TASKS.md` contained 5 infrastructure tasks in its machine-readable inventory: 4 tasks resolved in Cycle 1 Stage 6 (`cellstructuremech-infra-0001` through `cellstructuremech-infra-0004`) and 1 open task (`cellstructuremech-infra-0005`) captured during Cycle 2 Stage 4 (`record_review`) and linked to a real GitHub issue in `CultureBotAI/CellStructureMech`:

| Task ID | Originating Stage | GitHub Issue | Priority | Dependencies | Selected Action |
| --- | --- | --- | --- | --- | --- |
| `cellstructuremech-infra-0005` | Cycle 2, Stage 4 (`record_review`) | [#2417](https://github.com/CultureBotAI/CellStructureMech/issues/2417) | P2 | Builds on `src/cellstructuremech/validation/validator.py` (`#2408`, `#2410`) | Implement in Stage 6 (`resolved`) |

## 2. Dependency Analysis and Execution Plan

`cellstructuremech-infra-0005` (#2417) has no external blockers. It extends the repository's semantic record validator (`src/cellstructuremech/validation/validator.py`) to prevent two recurring classes of curation drift identified during the Cycle 2 Stage 4 whole-corpus audit of all 985 structure records and remediated in Cycle 2 Stage 5 (`PR #2422`):

### Phase 1: Causal-Graph `CausalNode` `node_type` vs Grounding / `PROTEIN_COMPLEX` Check (`#2417`)
- **Targets**:
  - `src/cellstructuremech/validation/validator.py` (`validate_causal_graphs`)
- **Design**:
  1. In `validate_causal_graphs(doc)`, inspect every `CausalNode` with `node_type == "GENE_OR_PROTEIN"`.
  2. Flag any `GENE_OR_PROTEIN` node whose `grounding` starts with `GO:` or `cellstructuremech:` (cellular-component/structure CURIEs require `node_type: STRUCTURE`).
  3. Flag any `GENE_OR_PROTEIN` node whose `component_ref` resolves to a component with `component_type == "PROTEIN_COMPLEX"` that itself carries a `grounding` starting with `GO:` or `cellstructuremech:` (representing a distinct structure-level complex rather than an ungrounded subunit cohort).
- **Acceptance Criteria**:
  - `validate_causal_graphs()` and `write_validated_structure()` reject `GENE_OR_PROTEIN` nodes carrying `GO:` / `cellstructuremech:` groundings or referencing structure-grounded `PROTEIN_COMPLEX` components.
  - All 985 corpus records under `data/structures/` pass `validate_causal_graphs()` with 0 errors.

### Phase 2: Component `gene_symbols` vs `protein_examples` Consistency Check (`#2417`)
- **Targets**:
  - `src/cellstructuremech/validation/validator.py` (`validate_component_protein_examples`, `validate_record_semantics`)
- **Design**:
  1. Implement `validate_component_protein_examples(doc)` and wire it into `validate_record_semantics(doc)`.
  2. For every component in `doc["components"]` that declares a non-empty `gene_symbols` list, inspect each entry in `protein_examples`.
  3. Verify that `protein_examples[].gene_symbol` either matches an entry in `component.gene_symbols` (case-insensitively) or is explicitly disclosed as an organism-specific synonym/locus tag in `protein_examples[].role` (matching `scripts/uniprot_genes.py`'s `_SYNONYM_ROLE_RE` and `_ALSO_SYNONYM_RE` conventions).
- **Acceptance Criteria**:
  - `validate_component_protein_examples()` and `write_validated_structure()` reject `protein_examples` entries whose `gene_symbol` is missing from a non-empty parent `component.gene_symbols` list without synonym disclosure in `role`.
  - All 985 corpus records under `data/structures/` pass `validate_component_protein_examples()` with 0 errors.

### Phase 3: Unit & Corpus Integrity Tests and Ledger Update
- **Targets**:
  - `tests/test_validator.py`
  - `tests/test_corpus_integrity.py`
  - `INFRA_TASKS.md`
  - `reviews/workflow/latest.yaml`
- **Acceptance Criteria**:
  - Unit tests in `tests/test_validator.py` cover `GO:` and `cellstructuremech:` groundings on `GENE_OR_PROTEIN` nodes, `GENE_OR_PROTEIN` nodes referencing grounded `PROTEIN_COMPLEX` components, and `protein_examples[].gene_symbol` drift vs synonym disclosure.
  - Corpus-integrity test `test_component_protein_examples_match_declared_gene_symbols` in `tests/test_corpus_integrity.py` passes across all 985 records.
  - All 10 quality gates in `scripts/run_qc.py` pass with 0 errors.
  - `INFRA_TASKS.md` marks `cellstructuremech-infra-0005` as `resolved` with its disposition, and `reviews/workflow/latest.yaml` is updated from `verified-evidence-index.json` to include Cycle 2 Stage 5.

## 3. Carry-Forward and Deferred Tasks

- **Deferred / Blocked Tasks**: None (`0` tasks deferred or blocked; `cellstructuremech-infra-0005`, the sole open task in the frozen Stage 6 scope, is resolved in this goal).
