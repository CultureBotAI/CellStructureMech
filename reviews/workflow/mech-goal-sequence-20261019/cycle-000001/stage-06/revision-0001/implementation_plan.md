# Cycle 1 Stage 6 Infrastructure Implementation Plan

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `1`
- **Stage**: `6` (`infrastructure`)
- **Revision**: `1`
- **Repository**: `CultureBotAI/CellStructureMech` (`cellstructuremech`)
- **Base Revision (`main`)**: `0f5126a29f835e79c1eb25b3589ff57d94fc723b`
- **Scope Frozen At**: `2026-10-23T12:41:41Z`
- **Frozen Snapshot Artifact**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-06/revision-0001/infra_snapshot.md`
- **Frozen Snapshot SHA-256**: `d8ee261ed2d5eac92afc87e14ee9f8abdf042930f749afa72c5ecc97fd763f02`

## 1. Bounded Intake and Issue Mapping

At the Stage 6 cutoff (`2026-10-23T12:41:41Z`), `INFRA_TASKS.md` contained 4 pending infrastructure notes captured across Stages 1–4 of Cycle 1. Each task was deduplicated against existing open and closed issues in `CultureBotAI/CellStructureMech` and linked to a dedicated GitHub issue:

| Task ID | Originating Stage | GitHub Issue | Priority | Dependencies | Selected Action |
| --- | --- | --- | --- | --- | --- |
| `cellstructuremech-infra-0001` | Cycle 1, Stage 1 (`add_records`) | [#2407](https://github.com/CultureBotAI/CellStructureMech/issues/2407) | P2 | None | Implement in Stage 6 (`resolved`) |
| `cellstructuremech-infra-0002` | Cycle 1, Stage 2 (`causal_graphs`) | [#2408](https://github.com/CultureBotAI/CellStructureMech/issues/2408) | P2 | None | Implement in Stage 6 (`resolved`) |
| `cellstructuremech-infra-0003` | Cycle 1, Stage 3 (`protein_examples`) | [#2409](https://github.com/CultureBotAI/CellStructureMech/issues/2409) | P2 | None | Implement in Stage 6 (`resolved`) |
| `cellstructuremech-infra-0004` | Cycle 1, Stage 4 (`record_review`) | [#2410](https://github.com/CultureBotAI/CellStructureMech/issues/2410) | P2 | Shares `scripts/validate_history.py` with `0001` and `src/cellstructuremech/validation/validator.py` with `0002` | Implement in Stage 6 (`resolved`) |

## 2. Dependency Analysis and Execution Order

Although none of the four tasks has an external blocker, they share two target modules:
- `src/cellstructuremech/validation/validator.py` is created and wired into `src/cellstructuremech/validation/write_validated.py` and `scripts/validate_strict.py` by both `cellstructuremech-infra-0002` (#2408) and the `discussions` issue-link check of `cellstructuremech-infra-0004` (#2410).
- `scripts/validate_history.py` is updated by both `cellstructuremech-infra-0001` (#2407) and the 1:1 structure-to-history coverage check of `cellstructuremech-infra-0004` (#2410).

Execution is ordered into four phases:

### Phase 1: Semantic Record Validator (`#2408`, `#2410`)
- **Targets**:
  - `src/cellstructuremech/validation/validator.py`
  - `src/cellstructuremech/validation/write_validated.py`
  - `scripts/validate_strict.py`
- **Design**:
  1. Implement `validate_causal_graphs(record)`:
     - Check that every `CausalNode` in `causal_graphs[*].nodes` has at least one incident `CausalEdge` (`subject == node_id` or `object == node_id`).
     - Check that every `CausalEdge` in `causal_graphs[*].edges` carries a non-empty `description` string.
  2. Implement `validate_discussion_issue_links(record)`:
     - Scan `discussions[*]` prose fields (`prompt`, `rationale`, `resolution_note`, `notes`) for `#NNN` issue mentions (ignoring `attaches_to`-style `word#anchor` tokens) and verify that each referenced issue number has a corresponding `https://github.com/CultureBotAI/CellStructureMech/issues/NNN` entry in that discussion's `evidence[*].reference`.
  3. Expose `validate_record_semantics(record)` combining both checks and invoke it inside `validate_structure()` (`src/cellstructuremech/validation/write_validated.py`) and `validate_all()` (`scripts/validate_strict.py`).
- **Acceptance Criteria**:
  - `write_validated_structure()` refuses to write records with isolated `CausalNode` entries, `CausalEdge` items lacking `description`, or `discussions` prose `#NNN` mentions without structured issue URLs in `evidence`.
  - All 978 corpus records under `data/structures/` pass `validate_record_semantics()` with 0 errors.

### Phase 2: History Validator Executable Resolution and 1:1 Coverage (`#2407`, `#2410`)
- **Targets**:
  - `scripts/validate_history.py`
- **Design**:
  1. Implement `resolve_linkml_validate()` in `scripts/validate_history.py`:
     - Prefer `Path(sys.executable).with_name("linkml-validate")` when present and executable, falling back to `shutil.which("linkml-validate")` and `"linkml-validate"`.
     - Replace bare `"linkml-validate"` in `run_linkml_validate()` with `resolve_linkml_validate()` so `.venv/bin/python scripts/run_qc.py` succeeds without `.venv/bin` on `PATH`.
  2. Implement `check_structure_history_coverage(structures_root, history_root)` in `scripts/validate_history.py`:
     - Verify that every `data/structures/<category>/<slug>.yaml` file has at least one `history/records/<slug>/*.yaml` ledger whose `target.path` resolves to that structure YAML.
     - Verify that every `history/records/<slug>/*.yaml` record has `target.kind == "record"`, `target.slug == <slug>`, and `target.path` resolving to an existing structure YAML under `data/structures/`.
     - Exempt the 6 pre-existing append-only legacy batch/hyphenated history directories (`divisome-injectisome-discussions`, `mreb-filament`, `records-tranche-1`, `records-tranche-2`, `records-tranche-3`, `uniprot-evidence-titles`) from the directory-name slug match while still requiring their `target.path` targets to exist.
- **Acceptance Criteria**:
  - `.venv/bin/python scripts/validate_history.py` and `.venv/bin/python scripts/run_qc.py` succeed when invoked with a minimal `PATH` lacking `.venv/bin`.
  - Missing `history/records/<slug>/` directories, empty history directories, mismatched `target.slug`, and broken `target.path` pointers fail validation with actionable error messages.

### Phase 3: UniProt Component Seeding Scope (`#2409`)
- **Targets**:
  - `scripts/uniprot_genes.py`
- **Design**:
  1. Add `_component_in_scope(component, include_complexes=False, include_non_protein=False)` and `NON_PROTEIN_COMPONENT_TYPES`.
  2. When `include_complexes=True` (`--include-complexes`), include `PROTEIN`, `PROTEIN_COMPLEX`, and any composite protein-bearing component type (such as `OTHER`) that declares non-empty `gene_symbols`, while excluding explicitly non-protein molecule types (`LIPID`, `POLYSACCHARIDE`, `PEPTIDOGLYCAN`, `RNA`, `DNA`, `INORGANIC`, `METABOLITE`) unless `include_non_protein=True` (`--include-non-protein`) is passed.
  3. Wire `include_non_protein` through `candidates()`, `gap_report()`, `cmd_gaps()`, `plan_record()`, `seed_records()`, and the CLI parser (`--include-non-protein`), preserving `component_type` on all seeded components.
- **Acceptance Criteria**:
  - `candidates(doc, include_complexes=True)` and `seed_records(..., include_complexes=True)` inspect `OTHER` components with declared `gene_symbols` (such as `centromeric_cse4_nucleosome` in `kinetochore.yaml` and `eif3_40s_translation_initiation_cohort` in `cytoplasmic_stress_granule.yaml`) while preserving their `component_type`.
  - Default mode (`include_complexes=False, include_non_protein=False`) remains restricted to `PROTEIN` components.

### Phase 4: Unit & Corpus Integrity Tests and Ledger Update
- **Targets**:
  - `tests/test_validator.py`
  - `tests/test_corpus_integrity.py`
  - `tests/test_new_history_record.py`
  - `tests/test_uniprot_genes.py`
  - `INFRA_TASKS.md`
- **Acceptance Criteria**:
  - All unit and corpus-wide tests pass (`pytest -q`), `ruff check .` reports 0 warnings, and all 10 quality gates in `scripts/run_qc.py` pass.
  - `INFRA_TASKS.md` records `status: resolved`, `issue_url`, and dispositions for all 4 frozen tasks.

## 3. Carry-Forward and Deferred Tasks

- **Deferred / Blocked Tasks**: None (`0` tasks deferred or blocked; all 4 tasks in the frozen Stage 6 scope are resolved in this goal).
