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
    status: resolved
    issue_url: https://github.com/CultureBotAI/CellStructureMech/issues/2407
    disposition: Implemented resolve_linkml_validate() in scripts/validate_history.py (preferring Path(sys.executable).with_name('linkml-validate') before shutil.which('linkml-validate')) and covered with unit tests in tests/test_new_history_record.py.
  - task_id: cellstructuremech-infra-0002
    summary: Add causal-graph completeness checks in src/cellstructuremech/validation/validator.py for isolated CausalNode entries with zero incident edges and CausalEdge items lacking description
    status: resolved
    issue_url: https://github.com/CultureBotAI/CellStructureMech/issues/2408
    disposition: Created src/cellstructuremech/validation/validator.py (validate_causal_graphs) and wired validate_record_semantics into write_validated_structure and scripts/validate_strict.py; verified 0 isolated nodes and 0 description-less edges across all 978 records and added unit tests in tests/test_validator.py and tests/test_corpus_integrity.py.
  - task_id: cellstructuremech-infra-0003
    summary: Allow scripts/uniprot_genes.py seeding mode to inspect components of any component_type that declare gene_symbols when --include-complexes is passed
    status: resolved
    issue_url: https://github.com/CultureBotAI/CellStructureMech/issues/2409
    disposition: Added _component_in_scope(), --include-non-protein, and seed_records() in scripts/uniprot_genes.py so --include-complexes inspects composite protein-bearing components (e.g. OTHER) declaring gene_symbols while preserving component_type; covered in tests/test_uniprot_genes.py.
  - task_id: cellstructuremech-infra-0004
    summary: Extend scripts/validate_history.py to enforce 1:1 record-to-history coverage and extend src/cellstructuremech/validation/validator.py to enforce structured issue links on discussions prose mentions
    status: resolved
    issue_url: https://github.com/CultureBotAI/CellStructureMech/issues/2410
    disposition: Added check_structure_history_coverage() in scripts/validate_history.py (enforcing 1:1 coverage across all 978 structure records and history/records/<slug>/) and validate_discussion_issue_links() in src/cellstructuremech/validation/validator.py; covered in tests/test_new_history_record.py, tests/test_validator.py, and tests/test_corpus_integrity.py.
  - task_id: cellstructuremech-infra-0005
    summary: Extend src/cellstructuremech/validation/validator.py to check GO/complex CausalNode node_type and component gene_symbols vs protein_examples consistency
    status: resolved
    issue_url: https://github.com/CultureBotAI/CellStructureMech/issues/2417
    disposition: Extended validate_causal_graphs() and added validate_component_protein_examples() in src/cellstructuremech/validation/validator.py (wired into validate_record_semantics, write_validated_structure, and scripts/validate_strict.py); verified 0 errors across all 985 structure records and added unit and corpus-integrity tests in tests/test_validator.py and tests/test_corpus_integrity.py.
  - task_id: cellstructuremech-infra-0006
    summary: Extend src/cellstructuremech/validation/validator.py to check causal_graphs component_ref grounding propagation, CURATED_CAUSAL_GRAPH id targets, and discussions prose citation evidence
    status: open
    issue_url: https://github.com/CultureBotAI/CellStructureMech/issues/2428
```
<!-- mech-infra-tasks:end -->

## Tasks

### `cellstructuremech-infra-0001` — Resolve `linkml-validate` relative to `sys.executable` in `scripts/validate_history.py`

- **Origin**: `mech-goal-sequence-20261019`, Cycle 1, Stage 1 (`add_records`)
- **Issue**: https://github.com/CultureBotAI/CellStructureMech/issues/2407
- **Status**: `resolved` (Cycle 1, Stage 6)
- **Priority**: P2
- **Dependencies**: None
- **Observation**: `scripts/run_qc.py` invokes `[sys.executable, "scripts/validate_history.py"]`, which in turn shells out to bare `["linkml-validate", ...]` (`scripts/validate_history.py` line 48). When `.venv/bin/python scripts/run_qc.py` is run without `.venv/bin` prepended to `PATH`, `linkml-validate` resolves to a global `pyenv` shim and fails with `pyenv: version '3.13' is not installed`.
- **Desired outcome**: Resolve `Path(sys.executable).with_name("linkml-validate")` (falling back to `shutil.which("linkml-validate")`) in `scripts/validate_history.py` so `scripts/run_qc.py` is self-contained when invoked via `.venv/bin/python`.
- **Resolution**: Added `resolve_linkml_validate()` in `scripts/validate_history.py` to prefer the sibling `linkml-validate` executable beside `sys.executable` before falling back to `shutil.which("linkml-validate")`, and added unit tests in `tests/test_new_history_record.py`.
- **Evidence paths**: `scripts/run_qc.py`, `scripts/validate_history.py`, `tests/test_new_history_record.py`

### `cellstructuremech-infra-0002` — Add causal-graph completeness checks in `src/cellstructuremech/validation/validator.py` for isolated `CausalNode` entries and `CausalEdge` items lacking `description`

- **Origin**: `mech-goal-sequence-20261019`, Cycle 1, Stage 2 (`causal_graphs`)
- **Issue**: https://github.com/CultureBotAI/CellStructureMech/issues/2408
- **Status**: `resolved` (Cycle 1, Stage 6)
- **Priority**: P2
- **Dependencies**: None
- **Observation**: `src/cellstructuremech/validation/validator.py` (`validate_causal_graphs`) validates `CausalEdge.subject`/`object` node references, `component_ref`, and `attaches_to` anchors, but does not check whether a declared `CausalNode` has zero incident `CausalEdge` items or whether a `CausalEdge` omits `description`. During the Stage 2 whole-corpus audit across 978 records, 17 records contained isolated `CausalNode` entries and 9 records contained 44 `CausalEdge` items lacking `description` despite passing `scripts/validate_strict.py` and `write_validated_structure`.
- **Desired outcome**: Add validation checks in `src/cellstructuremech/validation/validator.py` (`validate_causal_graphs`) to flag isolated `CausalNode` entries (zero incident edges in `edges`) and `CausalEdge` entries with missing/blank `description`.
- **Resolution**: Created `src/cellstructuremech/validation/validator.py` with `validate_causal_graphs()` and `validate_record_semantics()`, integrated into `src/cellstructuremech/validation/write_validated.py` and `scripts/validate_strict.py`, and added unit and corpus-integrity tests in `tests/test_validator.py` and `tests/test_corpus_integrity.py`.
- **Evidence paths**: `src/cellstructuremech/validation/validator.py`, `src/cellstructuremech/validation/write_validated.py`, `scripts/validate_strict.py`, `tests/test_validator.py`, `tests/test_corpus_integrity.py`

### `cellstructuremech-infra-0003` — Allow `scripts/uniprot_genes.py` seeding mode to inspect components of any `component_type` that declare `gene_symbols` when `--include-complexes` is passed

- **Origin**: `mech-goal-sequence-20261019`, Cycle 1, Stage 3 (`protein_examples`)
- **Issue**: https://github.com/CultureBotAI/CellStructureMech/issues/2409
- **Status**: `resolved` (Cycle 1, Stage 6)
- **Priority**: P2
- **Dependencies**: None
- **Observation**: In `scripts/uniprot_genes.py`, `verify_records` checks `protein_examples` across all components regardless of `component_type`, whereas `seed_records` restricts seeding to `allowed_types = {"PROTEIN", "PROTEIN_COMPLEX"} if include_complexes else {"PROTEIN"}` (`scripts/uniprot_genes.py` line 675). Consequently, composite nucleoprotein or ribonucleoprotein components typed `OTHER` that legitimately declare `gene_symbols` and are referenced by `GENE_OR_PROTEIN` causal-graph nodes (`centromeric_cse4_nucleosome` with `CSE4` in `data/structures/other/kinetochore.yaml` and `eif3_40s_translation_initiation_cohort` with `TIF32` in `data/structures/ribonucleoprotein/cytoplasmic_stress_granule.yaml`) are silently skipped by `scripts/uniprot_genes.py --include-complexes`.
- **Desired outcome**: Allow `scripts/uniprot_genes.py` (`seed_records`) to seed `protein_examples` on any component with non-empty `gene_symbols` when `--include-complexes` (or an explicit `--include-non-protein` flag) is passed, while preserving `component_type`.
- **Resolution**: Added `_component_in_scope()`, `--include-non-protein`, and `seed_records()` in `scripts/uniprot_genes.py` so `--include-complexes` inspects protein-bearing composite components (e.g. `OTHER`) declaring `gene_symbols` while excluding explicitly non-protein molecule types unless `--include-non-protein` is passed, and preserving `component_type`; covered in `tests/test_uniprot_genes.py`.
- **Evidence paths**: `scripts/uniprot_genes.py`, `tests/test_uniprot_genes.py`, `data/structures/other/kinetochore.yaml`, `data/structures/ribonucleoprotein/cytoplasmic_stress_granule.yaml`

### `cellstructuremech-infra-0004` — Extend `scripts/validate_history.py` to enforce 1:1 record-to-history coverage and extend `src/cellstructuremech/validation/validator.py` to enforce structured issue links on `discussions` prose mentions

- **Origin**: `mech-goal-sequence-20261019`, Cycle 1, Stage 4 (`record_review`)
- **Issue**: https://github.com/CultureBotAI/CellStructureMech/issues/2410
- **Status**: `resolved` (Cycle 1, Stage 6)
- **Priority**: P2
- **Dependencies**: None
- **Observation**: During the Stage 4 whole-corpus audit of all 978 records: (1) `scripts/validate_history.py` checks that every existing `history/records/<stem>/*.yaml` file points to a valid `data/structures/` record, but does not check the inverse direction (whether every `data/structures/**/*.yaml` record has at least one `history/records/<stem>/*.yaml` ledger), allowing `data/structures/membrane_organelle/woronin_body.yaml` to lack a `history/records/woronin_body/` directory silently; and (2) `src/cellstructuremech/validation/validator.py` does not verify the `docs/CURATION.md` rule that every `#NNN` issue mention in `discussions` prose (`prompt`, `rationale`, `resolution_note`) is backed by a full GitHub issue URL in that discussion's `evidence` list (affecting 7 records across `other`, `cytoskeleton`, `division_machinery`, and `secretion_system`).
- **Desired outcome**: Extend `scripts/validate_history.py` to verify that every `data/structures/**/*.yaml` record has at least one valid `history/records/<stem>/*.yaml` file, and add a check in `src/cellstructuremech/validation/validator.py` flagging `#NNN` issue mentions in `discussions` prose that lack a matching GitHub issue URL in `discussion.evidence`.
- **Resolution**: Added `check_structure_history_coverage()` in `scripts/validate_history.py` and `validate_discussion_issue_links()` in `src/cellstructuremech/validation/validator.py`, wired into `write_validated_structure` and `scripts/validate_strict.py`, and added unit and corpus-integrity tests in `tests/test_new_history_record.py`, `tests/test_validator.py`, and `tests/test_corpus_integrity.py`.
- **Evidence paths**: `scripts/validate_history.py`, `src/cellstructuremech/validation/validator.py`, `tests/test_new_history_record.py`, `tests/test_validator.py`, `tests/test_corpus_integrity.py`, `reviews/structured/20261023T091801Z-woronin-body-missing-history/review.yaml`, `reviews/structured/20261023T091804Z-cytoskeleton-category-review/review.yaml`

### `cellstructuremech-infra-0005` — Extend `src/cellstructuremech/validation/validator.py` to check GO/complex `CausalNode` `node_type` and component `gene_symbols` vs `protein_examples` consistency

- **Origin**: `mech-goal-sequence-20261019`, Cycle 2, Stage 4 (`record_review`)
- **Issue**: https://github.com/CultureBotAI/CellStructureMech/issues/2417
- **Status**: `resolved` (Cycle 2, Stage 6)
- **Priority**: P2
- **Dependencies**: None
- **Observation**: During the Cycle 2 Stage 4 whole-corpus audit of all 985 records: (1) `src/cellstructuremech/validation/validator.py` (`validate_causal_graphs`) does not check whether a `CausalNode` carrying a `GO:` or `cellstructuremech:` cellular-component/complex `grounding` (or referencing a `PROTEIN_COMPLEX` component) is typed `GENE_OR_PROTEIN` instead of `STRUCTURE`, allowing 5 records (`clathrin_coat_of_endocytic_vesicle.yaml`, `mitochondrial_crista_junction.yaml`, `mitochondrial_outer_membrane.yaml`, `chlorosome.yaml`, `chlorosome_envelope.yaml`) to use `GENE_OR_PROTEIN` for multiprotein complexes; and (2) `validator.py` does not check whether every `components[].protein_examples[].gene_symbol` is included in a non-empty parent `components[].gene_symbols` list or explicitly disclosed as an organism-specific synonym/locus in `protein_examples[].role`, allowing 6 records across `appendage`, `cytoskeleton`, and `microcompartment` to omit verified `protein_examples` gene symbols (`hag`, `fliY`, `nda2`, `ccmK3`, `ccmK4`) from `components[].gene_symbols`.
- **Desired outcome**: Extend `src/cellstructuremech/validation/validator.py` (`validate_record_semantics` / `validate_causal_graphs`) to flag `CausalNode` items grounded to `GO:` / `cellstructuremech:` (or referencing `PROTEIN_COMPLEX` components) that use `node_type: GENE_OR_PROTEIN`, and flag `components[].protein_examples` entries whose `gene_symbol` is neither in a non-empty parent `components[].gene_symbols` list nor disclosed in `protein_examples[].role`.
- **Resolution**: Extended `validate_causal_graphs()` and added `validate_component_protein_examples()` in `src/cellstructuremech/validation/validator.py` (wired into `validate_record_semantics()`, `write_validated_structure()`, and `scripts/validate_strict.py`), verified 0 errors across all 985 corpus records, and added unit and corpus-integrity tests in `tests/test_validator.py` and `tests/test_corpus_integrity.py`.
- **Evidence paths**: `src/cellstructuremech/validation/validator.py`, `tests/test_validator.py`, `tests/test_corpus_integrity.py`, `reviews/structured/20261023T230501Z-clathrin-coat-ap2-causal-node-type/review.yaml`, `reviews/structured/20261023T230502Z-appendage-category-review/review.yaml`, `reviews/structured/20261023T230503Z-cytoskeleton-category-review/review.yaml`, `reviews/structured/20261023T230505Z-membrane-organelle-category-review/review.yaml`, `reviews/structured/20261023T230506Z-microcompartment-category-review/review.yaml`

### `cellstructuremech-infra-0006` — Extend `src/cellstructuremech/validation/validator.py` to check `causal_graphs` `component_ref` grounding propagation, `CURATED_CAUSAL_GRAPH` `id` targets, and `discussions` prose citation evidence

- **Origin**: `mech-goal-sequence-20261019`, Cycle 3, Stage 4 (`record_review`)
- **Issue**: https://github.com/CultureBotAI/CellStructureMech/issues/2428
- **Status**: `open`
- **Priority**: P2
- **Dependencies**: None
- **Observation**: During the Cycle 3 Stage 4 whole-corpus audit of all 993 records: (1) `src/cellstructuremech/validation/validator.py` (`validate_causal_graphs`) does not check whether a `CausalNode` carrying a `component_ref` omits `grounding` when the referenced `components[]` item carries a verified ontology `grounding` (affecting 39 nodes across 21 records in `appendage`, `energy_complex`, `envelope`, `membrane_organelle`, `other`, `ribonucleoprotein`, `secretion_system`, and `spore`); (2) `validator.py` does not check whether `curation_history` entries with `action: CURATED_CAUSAL_GRAPH` reference a `causal_graphs` slug (`graph_id`) in `summary`/`notes` that no longer matches any `causal_graphs[].id` in the record (affecting 9 records across `cytoskeleton`, `division_machinery`, `energy_complex`, `other`, and `ribonucleoprotein`); and (3) `validator.py` (`validate_discussion_issue_links`) checks `#NNN` issue mentions in `discussions` prose against `discussion.evidence`, but does not check whether `DOI:` or `PMID:` citations in `discussions` prose (`prompt`, `rationale`, `resolution_note`) are backed by matching structured `discussion.evidence` items (affecting 3 records: `basal_body_cartwheel.yaml`, `basal_body_cartwheel_inner_density.yaml`, and `proteasome_storage_granule.yaml`).
- **Desired outcome**: Extend `src/cellstructuremech/validation/validator.py` (`validate_record_semantics` / `validate_causal_graphs` / `validate_discussion_issue_links`) to flag `CausalNode` items with `component_ref` lacking `grounding` when the referenced component has `grounding`, `CURATED_CAUSAL_GRAPH` `curation_history` summaries/notes referencing nonexistent `causal_graphs[].id` slugs, and `DOI:`/`PMID:` citations in `discussions` prose lacking matching structured `discussion.evidence` entries.
- **Evidence paths**: `src/cellstructuremech/validation/validator.py`, `reviews/structured/20261025T071001Z-static-microtubule-bundle-reference-attribution/review.yaml`, `reviews/structured/20261025T071002Z-primosome-complex-pmid-citation-misattribution/review.yaml`, `reviews/structured/20261025T071003Z-appendage-category-review/review.yaml`, `reviews/structured/20261025T071004Z-cytoskeleton-category-review/review.yaml`, `reviews/structured/20261025T071005Z-division-machinery-category-review/review.yaml`, `reviews/structured/20261025T071006Z-energy-complex-category-review/review.yaml`, `reviews/structured/20261025T071007Z-envelope-category-review/review.yaml`, `reviews/structured/20261025T071008Z-inclusion-category-review/review.yaml`, `reviews/structured/20261025T071009Z-membrane-organelle-category-review/review.yaml`, `reviews/structured/20261025T071010Z-other-category-review/review.yaml`, `reviews/structured/20261025T071011Z-ribonucleoprotein-category-review/review.yaml`, `reviews/structured/20261025T071012Z-secretion-system-category-review/review.yaml`, `reviews/structured/20261025T071013Z-spore-category-review/review.yaml`




