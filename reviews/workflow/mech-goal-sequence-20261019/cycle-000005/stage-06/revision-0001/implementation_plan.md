# Cycle 5 Stage 6 Infrastructure Implementation Plan

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `5`
- **Stage**: `6` (`infrastructure`)
- **Revision**: `1`
- **Repository**: `CultureBotAI/CellStructureMech` (`cellstructuremech`)
- **Base Revision (`main`)**: `ecd788f5a2090d23dddea6a1c8757ed55f7ddf68`
- **Scope Frozen At**: `2026-10-31T02:45:18Z`
- **Frozen Snapshot Artifact**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-06/revision-0001/infra_snapshot.md`
- **Frozen Snapshot SHA-256**: `581fae595ba5b8ea81028969e1da5cf5bfd0b939bfb9ca5d89259e7f9fe672f7`

## 1. Bounded Intake and Issue Mapping

At the Stage 6 cutoff (`2026-10-31T02:45:18Z`), `INFRA_TASKS.md` contained 8 infrastructure tasks in its machine-readable inventory: 7 tasks resolved in Cycles 1–4 (`cellstructuremech-infra-0001` through `cellstructuremech-infra-0007`) and 1 open task (`cellstructuremech-infra-0008`) captured during Cycle 5 Stage 4 (`record_review`) and linked to a real GitHub issue in `CultureBotAI/CellStructureMech`:

| Task ID | Originating Stage | GitHub Issue | Priority | Dependencies | Selected Action |
| --- | --- | --- | --- | --- | --- |
| `cellstructuremech-infra-0008` | Cycle 5, Stage 4 (`record_review`) | [#2472](https://github.com/CultureBotAI/CellStructureMech/issues/2472) | P2 | Builds on `src/cellstructuremech/validation/validator.py` (`#2408`, `#2410`, `#2417`, `#2428`, `#2457`) | Implement in Stage 6 (`resolved`) |

## 2. Dependency Analysis and Execution Plan

`cellstructuremech-infra-0008` ([#2472](https://github.com/CultureBotAI/CellStructureMech/issues/2472)) has no external blockers. It extends the repository's semantic record validator (`src/cellstructuremech/validation/validator.py`) to prevent three classes of curation drift identified during the Cycle 5 Stage 4 whole-corpus audit of all 1,008 structure records and remediated in Cycle 5 Stage 5 (`PR #2477`):

### Phase 1: Empty-`gene_symbols` Component `protein_examples` Check (`#2472`)
- **Targets**:
  - `src/cellstructuremech/validation/validator.py` (`validate_component_protein_examples`)
- **Design**:
  1. In `validate_component_protein_examples(doc)`, replace the early `if not gs: continue` skip with an explicit check over `comp.get("protein_examples") or []` when `component.gene_symbols` is empty.
  2. Flag any `protein_examples[]` entry that declares a non-empty `gene_symbol` on a component with empty `gene_symbols` unless `role` omits `"declared gene symbol"` and explicitly discloses a UniProt primary-name or synonym/locus exception matching `_SYNONYM_ROLE_RE` or `_ALSO_SYNONYM_RE`.
- **Acceptance Criteria**:
  - `validate_component_protein_examples()` and `write_validated_structure()` reject components that omit `gene_symbols` while declaring `protein_examples[].gene_symbol` (such as `post_anaphase_microtubule_array.yaml` `components#emtoc` prior to `#2475`).
  - All 1,008 corpus records under `data/structures/` pass `validate_component_protein_examples()` with 0 errors.

### Phase 2: `functions[]` and `CausalNode` GO Aspect and Grounding Consistency Check (`#2472`)
- **Targets**:
  - `src/cellstructuremech/validation/validator.py` (`validate_causal_graphs`)
- **Design**:
  1. In `validate_causal_graphs(doc)`, inspect every `CausalNode` against `doc["functions"]` entries that match by `function_id == node_id`, case-insensitive `label`, or `grounding`.
  2. When a `CausalNode` and a `functions[]` entry match by `function_id == node_id` or `label`, flag any `functions[]` entry that omits `grounding` when the matching `CausalNode` carries a `GO:` `grounding` (and vice versa), or where the two groundings conflict.
  3. When a `CausalNode` and a `functions[]` entry match by ID, label, or `grounding`, inspect the GO aspect documented in `functions[].evidence`, record-level `evidence`, and incident `edges[].evidence` for that `GO:` term, and flag `CausalNode` items typed `BIOLOGICAL_PROCESS` when the term is documented as a `molecular_function` (or typed `MOLECULAR_FUNCTION` when documented as a `biological_process`).
- **Acceptance Criteria**:
  - `validate_causal_graphs()` and `write_validated_structure()` reject `CausalNode` items whose `node_type` contradicts the GO aspect documented on the matching `functions[]` entry (such as `origin_recognition_complex.yaml` `dna_replication_origin_binding` `GO:0003688` prior to `#2476`) and `functions[]` entries that omit `GO:` `grounding` present on a matching `CausalNode` (such as `autophagosome.yaml` `functions#macroautophagy` `GO:0016236` prior to `#2476`).
  - All 1,008 corpus records under `data/structures/` pass `validate_causal_graphs()` with 0 errors.

### Phase 3: Unit & Corpus Integrity Tests and Ledger Update
- **Targets**:
  - `tests/test_validator.py`
  - `tests/test_corpus_integrity.py`
  - `INFRA_TASKS.md`
  - `reviews/workflow/latest.yaml`
- **Acceptance Criteria**:
  - Unit tests in `tests/test_validator.py` cover empty-`gene_symbols` component `protein_examples` (`test_component_with_empty_gene_symbols_and_protein_example_is_flagged`) and function/`CausalNode` GO aspect and grounding consistency (`test_function_and_causal_node_go_grounding_and_aspect_consistency`).
  - Corpus-integrity tests `test_causal_graphs_have_no_isolated_nodes_or_undescribed_edges` and `test_component_protein_examples_match_declared_gene_symbols` in `tests/test_corpus_integrity.py` pass across all 1,008 records.
  - All 10 quality gates in `scripts/run_qc.py` pass with 0 errors.
  - `INFRA_TASKS.md` marks `cellstructuremech-infra-0008` as `resolved` with its disposition, and `reviews/workflow/latest.yaml` is updated from `verified-evidence-index.json` to include Cycle 5 Stage 5.

## 3. Carry-Forward and Deferred Tasks

- **Deferred / Blocked Tasks**: None (`0` tasks deferred or blocked; `cellstructuremech-infra-0008`, the sole open task in the frozen Stage 6 scope, is resolved in this goal).
