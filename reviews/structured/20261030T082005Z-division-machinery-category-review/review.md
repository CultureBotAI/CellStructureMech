# Category review of data/structures/division_machinery/ (4 records)

- Review: 20261030T082005Z-division-machinery-category-review
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-30T08:09:00Z
- Finished UTC: 2026-10-30T08:20:05Z
- Reviewer: antigravity-c4s4-record-review (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Full cohort audit of all 4 DIVISION_MACHINERY records in data/structures/division_machinery/ (divisome_complex, elongasome, ftsbl_complex, ftsqbl_complex). Three records are clean; ftsqbl_complex.yaml (GO:1990587) duplicates GO:1990586 (divisome complex) across parent_structures and part_of (shared issue_key ftsqbl-complex-parent-partof-duplication).

## Scope And Provenance

Full-cohort review of all 4 CellStructureRecord YAML files under data/structures/division_machinery/.

Selection: Complete folder cohort data/structures/division_machinery/*.yaml in the frozen 1,001-record Cycle 4 Stage 4 inventory.
Coverage: full; 4 reviewed / 4 in the declared population.
Source: git_commit at Git base 5c642e4080ef3a0f026845843c559d3b46de8871.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:1990586 | data/structures/division_machinery/divisome_complex.yaml | maintained | divisome complex |
| cellstructuremech:elongasome | data/structures/division_machinery/elongasome.yaml | maintained | elongasome |
| GO:1990588 | data/structures/division_machinery/ftsbl_complex.yaml | maintained | FtsBL complex |
| GO:1990587 | data/structures/division_machinery/ftsqbl_complex.yaml | maintained | FtsQBL complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation covering division_machinery cohort | passed | True | GO:1990586, cellstructuremech:elongasome, GO:1990588, GO:1990587 | All 4 division_machinery records pass strict LinkML and semantic validation. |
| History ledger validation covering division_machinery cohort | passed | True | GO:1990586, cellstructuremech:elongasome, GO:1990588, GO:1990587 | All history ledger records covering division_machinery validate cleanly. |

## Scientific And Domain Assessments

### Identity, boundaries, causal graphs, and ontology grounding across data/structures/division_machinery/

scope: supported. Targets: GO:1990586, cellstructuremech:elongasome, GO:1990588, GO:1990587.

All 4 records in data/structures/division_machinery/ represent distinct microbial cell structures or subcomplexes with valid schema and history provenance.

### Divisome complex (GO:1990586) hierarchy consistency between ftsqbl_complex and ftsbl_complex

representation: concern. Targets: GO:1990587.

ftsbl_complex.yaml (GO:1990588) places GO:1990586 only in parent_structures and GO:1990587 in part_of, whereas ftsqbl_complex.yaml places GO:1990586 in both parent_structures and part_of.

## Findings

### F1: ftsqbl_complex.yaml lists GO:1990586 (divisome complex) in both parent_structures and part_of

major / open / confirmed; issue key: ftsqbl-complex-parent-partof-duplication.

In data/structures/division_machinery/ftsqbl_complex.yaml (GO:1990587), GO:1990586 (divisome complex) appears in both parent_structures and part_of. In GO, GO:1990587 is an is_a child of GO:1990586 with no part_of edge.

## Recommended Actions And Acceptance Checks

### A1

Remove part_of: [GO:1990586] from data/structures/division_machinery/ftsqbl_complex.yaml.

- .venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv
- .venv/bin/python scripts/validate_history.py

## Category Boundaries

- retain: GO:1990586, cellstructuremech:elongasome, GO:1990588, GO:1990587. All 4 division_machinery records represent distinct prokaryotic division or elongation assemblies.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev_strict_division_machinery | scripts/validate_strict.py; strict_all receipt | supports | validate_strict.py exited 0 across all 1,001 records including all 4 division_machinery records. |
| ev_history_division_machinery | scripts/validate_history.py; history_all receipt | supports | validate_history.py exited 0 across all 2,082 history records covering division_machinery. |
| ev_divmach_ftsqbl | data/structures/division_machinery/ftsqbl_complex.yaml; parent_structures and part_of (lines 12-16) | supports | ftsqbl_complex.yaml lists GO:1990586 in both parent_structures and part_of. |

## Limits And Additional Notes

- Record edits for division_machinery cohort findings are queued for Cycle 4 Stage 5 (resolve_review_findings).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261030T082005Z-division-machinery-category-review
kind: category
repository: CultureBotAI/CellStructureMech
title: Category review of data/structures/division_machinery/ (4 records)
started_at: '2026-10-30T08:09:00Z'
finished_at: '2026-10-30T08:20:05Z'
reviewer:
  identity: antigravity-c4s4-record-review
  kind: agent
  model: claude-opus-4-6
  independence: independent
  independence_basis: Reviewed in Cycle 4 Stage 4 record_review against committed
    git revision 5c642e4080ef3a0f026845843c559d3b46de8871 without record edits in
    this stage.
skill: .claude/skills/review-yaml-category/SKILL.md
completion: completed
verdict: needs_curation
native_verdict: NEEDS_CURATION
scientific_review: true
summary: Full cohort audit of all 4 DIVISION_MACHINERY records in data/structures/division_machinery/
  (divisome_complex, elongasome, ftsbl_complex, ftsqbl_complex). Three records are
  clean; ftsqbl_complex.yaml (GO:1990587) duplicates GO:1990586 (divisome complex)
  across parent_structures and part_of (shared issue_key ftsqbl-complex-parent-partof-duplication).
source:
  git_revision: 5c642e4080ef3a0f026845843c559d3b46de8871
  state: git_commit
  inputs:
  - path: .claude/skills/review-yaml-category/SKILL.md
    sha256: 7a7ae411cf451ee7e634dfc65b6a466e5c52206e5d9111f090d3704832ddceae
    role: context
  - path: AGENTS.md
    sha256: ef74a980161b55cd24f1851e38d1c0b2e004fcf8837f1bc70da1874e4e8380f0
    role: context
  - path: conf/record_review.yaml
    sha256: d3334a12b8a616a7638f1195748085d2b543fba7df67ad4ff8fcc0ac18f2d3ee
    role: context
  - path: data/structures/division_machinery/divisome_complex.yaml
    sha256: b4f4919cc610dcb396b0646a715c51b071b0d7c05674b8f93e533130d225ac59
    role: target
  - path: data/structures/division_machinery/elongasome.yaml
    sha256: 17ec224fdda023f226646f624729b1e0f84fe4be24fe5976407d4d9c7f69221b
    role: target
  - path: data/structures/division_machinery/ftsbl_complex.yaml
    sha256: dde89c1c0094b667c97e5d226c447bcbf6882b307809ea5bc6996f42ea882c0f
    role: target
  - path: data/structures/division_machinery/ftsqbl_complex.yaml
    sha256: c6563e47cef93b8807aaebfdd48e746d54d985e1b42f35b1ff42f0eab32e296a
    role: target
  - path: docs/CURATION.md
    sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
    role: context
  - path: docs/SCHEMA.md
    sha256: 07b8f936a553a45cc6e8dba924c21e6af48c81b3866725efeb00c8183f0c75a2
    role: context
  - path: docs/record-review-profile.md
    sha256: 6a49c8d35f0a94082a9ad0b8bd8c6a929d85de8339141955f3779bd7ab0eb7e4
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
scope:
  description: Full-cohort review of all 4 CellStructureRecord YAML files under data/structures/division_machinery/.
  selection: Complete folder cohort data/structures/division_machinery/*.yaml in the
    frozen 1,001-record Cycle 4 Stage 4 inventory.
  coverage: full
  population_size: 4
  reviewed_target_ids:
  - GO:1990586
  - cellstructuremech:elongasome
  - GO:1990588
  - GO:1990587
targets:
- target_id: GO:1990586
  path: data/structures/division_machinery/divisome_complex.yaml
  label: divisome complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: b4f4919cc610dcb396b0646a715c51b071b0d7c05674b8f93e533130d225ac59
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/division_machinery/divisome_complex.yaml
    role: maintained_record
- target_id: cellstructuremech:elongasome
  path: data/structures/division_machinery/elongasome.yaml
  label: elongasome
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 17ec224fdda023f226646f624729b1e0f84fe4be24fe5976407d4d9c7f69221b
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/division_machinery/elongasome.yaml
    role: maintained_record
- target_id: GO:1990588
  path: data/structures/division_machinery/ftsbl_complex.yaml
  label: FtsBL complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: dde89c1c0094b667c97e5d226c447bcbf6882b307809ea5bc6996f42ea882c0f
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/division_machinery/ftsbl_complex.yaml
    role: maintained_record
- target_id: GO:1990587
  path: data/structures/division_machinery/ftsqbl_complex.yaml
  label: FtsQBL complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: c6563e47cef93b8807aaebfdd48e746d54d985e1b42f35b1ff42f0eab32e296a
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/division_machinery/ftsqbl_complex.yaml
    role: maintained_record
checks:
- check_id: strict_division_machinery
  name: Strict corpus validation covering division_machinery cohort
  status: passed
  required: true
  summary: All 4 division_machinery records pass strict LinkML and semantic validation.
  target_ids:
  - GO:1990586
  - cellstructuremech:elongasome
  - GO:1990588
  - GO:1990587
  command: .venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_strict_division_machinery
- check_id: history_division_machinery
  name: History ledger validation covering division_machinery cohort
  status: passed
  required: true
  summary: All history ledger records covering division_machinery validate cleanly.
  target_ids:
  - GO:1990586
  - cellstructuremech:elongasome
  - GO:1990588
  - GO:1990587
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_history_division_machinery
evidence:
- evidence_id: ev_strict_division_machinery
  kind: validation
  reference: scripts/validate_strict.py
  locator: strict_all receipt
  accessed_at: '2026-10-30T08:20:05Z'
  support: supports
  summary: validate_strict.py exited 0 across all 1,001 records including all 4 division_machinery
    records.
  snapshot_sha256: 1ebf6e7daebc19797861570fcac0d3cf8b06c18f7f40abf3277d35ef5867f442
- evidence_id: ev_history_division_machinery
  kind: validation
  reference: scripts/validate_history.py
  locator: history_all receipt
  accessed_at: '2026-10-30T08:20:05Z'
  support: supports
  summary: validate_history.py exited 0 across all 2,082 history records covering
    division_machinery.
  snapshot_sha256: 8bcb91b216ec775bac08188426f9ef860888b78f91561be1e471ea4a2159ad3b
- evidence_id: ev_divmach_ftsqbl
  kind: record_content
  reference: data/structures/division_machinery/ftsqbl_complex.yaml
  locator: parent_structures and part_of (lines 12-16)
  accessed_at: '2026-10-30T08:14:00Z'
  support: supports
  summary: ftsqbl_complex.yaml lists GO:1990586 in both parent_structures and part_of.
  quote: 'parent_structures:

    - GO:1990586

    - GO:0098797

    part_of:

    - GO:1990586

    has_part:

    - GO:1990588'
  snapshot_sha256: c6563e47cef93b8807aaebfdd48e746d54d985e1b42f35b1ff42f0eab32e296a
assessments:
- assessment_id: assess_division_machinery_cohort
  area: scope
  topic: Identity, boundaries, causal graphs, and ontology grounding across data/structures/division_machinery/
  outcome: supported
  summary: All 4 records in data/structures/division_machinery/ represent distinct
    microbial cell structures or subcomplexes with valid schema and history provenance.
  target_ids:
  - GO:1990586
  - cellstructuremech:elongasome
  - GO:1990588
  - GO:1990587
  evidence_ids:
  - ev_strict_division_machinery
  - ev_history_division_machinery
- assessment_id: assess_divmach_ftsqbl_hierarchy
  area: representation
  topic: Divisome complex (GO:1990586) hierarchy consistency between ftsqbl_complex
    and ftsbl_complex
  outcome: concern
  summary: ftsbl_complex.yaml (GO:1990588) places GO:1990586 only in parent_structures
    and GO:1990587 in part_of, whereas ftsqbl_complex.yaml places GO:1990586 in both
    parent_structures and part_of.
  target_ids:
  - GO:1990587
  evidence_ids:
  - ev_divmach_ftsqbl
findings:
- finding_id: F1
  issue_key: ftsqbl-complex-parent-partof-duplication
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: ftsqbl_complex.yaml lists GO:1990586 (divisome complex) in both parent_structures
    and part_of
  description: In data/structures/division_machinery/ftsqbl_complex.yaml (GO:1990587),
    GO:1990586 (divisome complex) appears in both parent_structures and part_of. In
    GO, GO:1990587 is an is_a child of GO:1990586 with no part_of edge.
  target_ids:
  - GO:1990587
  field_paths:
  - parent_structures
  - part_of
  evidence_ids:
  - ev_divmach_ftsqbl
  rule_id: docs/CURATION.md:parent_structures-vs-part_of
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/division_machinery/ftsqbl_complex.yaml
    role: maintained_record
  tags:
  - division-machinery
  - hierarchy
  - stage4-record-review
actions:
- action_id: A1
  description: 'Remove part_of: [GO:1990586] from data/structures/division_machinery/ftsqbl_complex.yaml.'
  finding_ids:
  - F1
  target_ids:
  - GO:1990587
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/division_machinery/ftsqbl_complex.yaml
    role: maintained_record
  acceptance_checks:
  - .venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv
  - .venv/bin/python scripts/validate_history.py
boundary_decisions:
- action: retain
  target_ids:
  - GO:1990586
  - cellstructuremech:elongasome
  - GO:1990588
  - GO:1990587
  rationale: All 4 division_machinery records represent distinct prokaryotic division
    or elongation assemblies.
  evidence_ids:
  - ev_strict_division_machinery
  - ev_history_division_machinery
limitations:
- Record edits for division_machinery cohort findings are queued for Cycle 4 Stage
  5 (resolve_review_findings).
tags:
- stage4
- category-review
- division-machinery
```
