# CellStructureMech infrastructure tasks

This versioned ledger collects repository requirements and upgrades discovered
during every goal. The workflow profile and its parent govern intake, stage 6
implementation, closure and cycle restart.

## Intake protocol

- Give each actionable task a stable ID such as `cellstructuremech-infra-0001` and retain it
  across cycles. Record the originating run, cycle and goal, observation,
  desired outcome, evidence paths, priority, dependencies and status.
- Link each task to an actual issue in https://github.com/CultureBotAI/CellStructureMech/issues.
  Search existing open and closed issues before creating one. If access fails,
  retain an explicit pending-link blocker; never invent an issue number or URL.
- Preserve resolved and deferred entries with their issue, implementation PR,
  validation and disposition. Do not overwrite previous cycle evidence.
- At stage 6, freeze a bounded snapshot, write a dependency-aware plan and
  acceptance criteria, implement selected work, validate, and complete the
  commit sequence, write the closure receipt and stop; only the supervisor
  dispatches another goal. New arrivals after the cutoff enter the next cycle;
  never expand the frozen task-ID scope. A new blocking prerequisite requires
  an explicit deferred disposition for the selected task. Carry unfinished work
  forward explicitly.

## Machine-readable task inventory

This fenced mapping is the inventory stage 6 freezes and reconciles. Each task
uses `task_id`, `summary`, `status` (`note`, `open`, `deferred`, or `resolved`),
optional `issue_url`, and optional `disposition`. Status `note` may have a
pending issue link; all other statuses require a real issue URL. Keep richer
notes below keyed by the same stable task ID.

<!-- mech-infra-tasks:start -->
```yaml
schema_version: '1.0.0'
tasks:
  - task_id: cellstructuremech-infra-0001
    summary: Resolve linkml-validate relative to sys.executable in scripts/validate_history.py so scripts/run_qc.py succeeds under direct .venv/bin/python invocation
    status: note
    disposition: Discovered during Cycle 1 Stage 1 (add_records) QC gate execution; queued for Stage 6 infrastructure implementation.
  - task_id: cellstructuremech-infra-0002
    summary: Add causal-graph completeness checks in src/cellstructuremech/validation/validator.py for isolated CausalNode entries with zero incident edges and CausalEdge items lacking description
    status: note
    disposition: Discovered during Cycle 1 Stage 2 (causal_graphs) whole-corpus audit (17 records with isolated nodes, 9 records with 44 description-less edges); queued for Stage 6 infrastructure implementation.
  - task_id: cellstructuremech-infra-0003
    summary: Allow scripts/uniprot_genes.py seeding mode to inspect components of any component_type that declare gene_symbols when --include-complexes is passed
    status: note
    disposition: Discovered during Cycle 1 Stage 3 (protein_examples) audit where OTHER components with declared gene_symbols referenced by GENE_OR_PROTEIN causal-graph nodes (centromeric_cse4_nucleosome in kinetochore.yaml and eif3_40s_translation_initiation_cohort in cytoplasmic_stress_granule.yaml) were skipped by seed_records; queued for Stage 6 infrastructure implementation.
```
<!-- mech-infra-tasks:end -->

## Tasks

### `cellstructuremech-infra-0001` — Resolve `linkml-validate` relative to `sys.executable` in `scripts/validate_history.py`

- **Origin**: `mech-goal-sequence-20261019`, Cycle 1, Stage 1 (`add_records`)
- **Status**: `note` (pending issue creation/triage in Stage 6)
- **Priority**: P2
- **Dependencies**: None
- **Observation**: `scripts/run_qc.py` invokes `[sys.executable, "scripts/validate_history.py"]`, which in turn shells out to bare `["linkml-validate", ...]` (`scripts/validate_history.py` line 48). When `.venv/bin/python scripts/run_qc.py` is run without `.venv/bin` prepended to `PATH`, `linkml-validate` resolves to a global `pyenv` shim and fails with `pyenv: version '3.13' is not installed`.
- **Desired outcome**: Resolve `Path(sys.executable).with_name("linkml-validate")` (falling back to `shutil.which("linkml-validate")`) in `scripts/validate_history.py` so `scripts/run_qc.py` is self-contained when invoked via `.venv/bin/python`.
- **Evidence paths**: `scripts/run_qc.py`, `scripts/validate_history.py`

### `cellstructuremech-infra-0002` — Add causal-graph completeness checks in `src/cellstructuremech/validation/validator.py` for isolated `CausalNode` entries and `CausalEdge` items lacking `description`

- **Origin**: `mech-goal-sequence-20261019`, Cycle 1, Stage 2 (`causal_graphs`)
- **Status**: `note` (pending issue creation/triage in Stage 6)
- **Priority**: P2
- **Dependencies**: None
- **Observation**: `src/cellstructuremech/validation/validator.py` (`validate_causal_graphs`) validates `CausalEdge.subject`/`object` node references, `component_ref`, and `attaches_to` anchors, but does not check whether a declared `CausalNode` has zero incident `CausalEdge` items or whether a `CausalEdge` omits `description`. During the Stage 2 whole-corpus audit across 978 records, 17 records contained isolated `CausalNode` entries and 9 records contained 44 `CausalEdge` items lacking `description` despite passing `scripts/validate_strict.py` and `write_validated_structure`.
- **Desired outcome**: Add validation checks in `src/cellstructuremech/validation/validator.py` (`validate_causal_graphs`) to flag isolated `CausalNode` entries (zero incident edges in `edges`) and `CausalEdge` entries with missing/blank `description`.
- **Evidence paths**: `src/cellstructuremech/validation/validator.py`, `scripts/validate_structures.py`

### `cellstructuremech-infra-0003` — Allow `scripts/uniprot_genes.py` seeding mode to inspect components of any `component_type` that declare `gene_symbols` when `--include-complexes` is passed

- **Origin**: `mech-goal-sequence-20261019`, Cycle 1, Stage 3 (`protein_examples`)
- **Status**: `note` (pending issue creation/triage in Stage 6)
- **Priority**: P2
- **Dependencies**: None
- **Observation**: In `scripts/uniprot_genes.py`, `verify_records` checks `protein_examples` across all components regardless of `component_type`, whereas `seed_records` restricts seeding to `allowed_types = {"PROTEIN", "PROTEIN_COMPLEX"} if include_complexes else {"PROTEIN"}` (`scripts/uniprot_genes.py` line 675). Consequently, composite nucleoprotein or ribonucleoprotein components typed `OTHER` that legitimately declare `gene_symbols` and are referenced by `GENE_OR_PROTEIN` causal-graph nodes (`centromeric_cse4_nucleosome` with `CSE4` in `data/structures/other/kinetochore.yaml` and `eif3_40s_translation_initiation_cohort` with `TIF32` in `data/structures/ribonucleoprotein/cytoplasmic_stress_granule.yaml`) are silently skipped by `scripts/uniprot_genes.py --include-complexes`.
- **Desired outcome**: Allow `scripts/uniprot_genes.py` (`seed_records`) to seed `protein_examples` on any component with non-empty `gene_symbols` when `--include-complexes` (or an explicit `--include-non-protein` flag) is passed, while preserving `component_type`.
- **Evidence paths**: `scripts/uniprot_genes.py`, `data/structures/other/kinetochore.yaml`, `data/structures/ribonucleoprotein/cytoplasmic_stress_granule.yaml`

