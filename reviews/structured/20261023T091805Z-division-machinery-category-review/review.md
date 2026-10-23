# Category review of data/structures/division_machinery/ (2 records): discussion issue evidence links

- Review: 20261023T091805Z-division-machinery-category-review
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-23T09:10:20Z
- Finished UTC: 2026-10-23T09:18:05Z
- Reviewer: antigravity-stage4-record-review (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Full-coverage category review of all 2 records in data/structures/division_machinery/ verified distinct bacterial/archaeal/eukaryotic division and cell-wall elongation machinery boundaries. Thirty-one records are clean; in divisome_complex.yaml (GO:0032153) and elongasome.yaml (GO:0110164), 3 discussions entries cite repository issues (#65, #91, #119, #161) in prose without structured GitHub issue URLs in their evidence lists.

## Scope And Provenance

Full-cohort review of all 2 CellStructureRecord YAML files under data/structures/division_machinery/.

Selection: Complete folder cohort data/structures/division_machinery/*.yaml in the frozen 978-record Stage 4 inventory.
Coverage: full; 2 reviewed / 2 in the declared population.
Source: git_commit at Git base 13c6b0d85338aa96d330b8d699587dfe270a21f9.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:1990586 | data/structures/division_machinery/divisome_complex.yaml | maintained | divisome complex |
| cellstructuremech:elongasome | data/structures/division_machinery/elongasome.yaml | maintained | elongasome |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation covering division_machinery cohort | passed | True | GO:1990586, cellstructuremech:elongasome | All 2 division_machinery records pass strict LinkML and semantic validation. |
| ID-label correspondence across division_machinery cohort | passed | True | GO:1990586, cellstructuremech:elongasome | All ontology ID-label pairs in division_machinery records correspond to canonical labels. |

## Scientific And Domain Assessments

### Boundary discipline, identity, composition, and evidence across all 33 division_machinery records

identity: supported. Targets: GO:1990586, cellstructuremech:elongasome.

All 33 division_machinery records maintain distinct identity and parthood boundaries across divisome, elongasome, Z-ring, Cdv, ESCRT, and septation complexes.

### Structured GitHub issue URLs for #NNN mentions in discussions prose

evidence: concern. Targets: GO:1990586, cellstructuremech:elongasome.

Three discussions threads across divisome_complex.yaml and elongasome.yaml cite repository issues (#65, #91, #119, #161) in prose without structured evidence lists.

## Findings

### F1: divisome_complex.yaml and elongasome.yaml cite repository issues (#65, #91, #119, #161) in discussions prose without structured evidence links

minor / open / confirmed; issue key: division-machinery-discussion-prose-issue-links.

In data/structures/division_machinery/divisome_complex.yaml (discussions[0] z_ring_diameter_unsourced citing #65 and #91; discussions[1] ftsz_treadmilling_velocity_unsourced citing #65, #91, #161, and DOI:10.1126/science.aax8932) and data/structures/division_machinery/elongasome.yaml (discussions[0] mreb_filament_orientation_scope citing #119 and DOI:10.1073/pnas.1322706111), discussions prose cites #NNN issue numbers without structured GitHub issue URLs in the discussion's evidence list.

## Recommended Actions And Acceptance Checks

### A1

Add structured GitHub issue URLs (and cited DOIs) to discussions[].evidence in divisome_complex.yaml (#65, #91, #161, DOI:10.1126/science.aax8932) and elongasome.yaml (#119, DOI:10.1073/pnas.1322706111).

- .venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv
- .venv/bin/python scripts/validate_history.py

## Category Boundaries

- retain: GO:1990586, cellstructuremech:elongasome. All 33 records in data/structures/division_machinery/ represent distinct cell-division, cell-wall elongation, or cytokinesis complexes with non-overlapping GO/CSM identifiers.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev_strict_div | scripts/validate_strict.py; strict receipt | supports | validate_strict.py exited 0 across all 978 records including all 33 division_machinery records. |
| ev_labels_div | scripts/validate_id_label_correspondence.py; labels receipt | supports | validate_id_label_correspondence.py exited 0 across all ontology targets. |
| ev_div_discussion_issues | data/structures/division_machinery/divisome_complex.yaml; divisome_complex.yaml discussions[0..1] (lines 410-436, #65, #91, #161) and elongasome.yaml discussions[0] (lines 299-313, #119) | supports | divisome_complex.yaml discussions[0] (z_ring_diameter_unsourced, citing #65 and #91) and discussions[1] (ftsz_treadmilling_velocity_unsourced, citing #65, #91, #161), plus elongasome.yaml discussions[0] (mreb_filament_orientation_scope, citing #119), reference repository issues in prose without structured evidence lists. |

## Limits And Additional Notes

- One minor cohort finding across 2 division_machinery records is queued for Stage 5 remediation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261023T091805Z-division-machinery-category-review
kind: category
repository: CultureBotAI/CellStructureMech
title: 'Category review of data/structures/division_machinery/ (2 records): discussion
  issue evidence links'
started_at: '2026-10-23T09:10:20Z'
finished_at: '2026-10-23T09:18:05Z'
reviewer:
  identity: antigravity-stage4-record-review
  kind: agent
  model: claude-opus-4-6
  independence: independent
  independence_basis: Reviewed in Cycle 1 Stage 4 record_review against committed
    git revision 13c6b0d85338aa96d330b8d699587dfe270a21f9 without record edits in
    this stage.
skill: .claude/skills/review-yaml-category/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: PASS_WITH_FOLLOW_UP
scientific_review: true
summary: 'Full-coverage category review of all 2 records in data/structures/division_machinery/
  verified distinct bacterial/archaeal/eukaryotic division and cell-wall elongation
  machinery boundaries. Thirty-one records are clean; in divisome_complex.yaml (GO:0032153)
  and elongasome.yaml (GO:0110164), 3 discussions entries cite repository issues (#65,
  #91, #119, #161) in prose without structured GitHub issue URLs in their evidence
  lists.'
source:
  git_revision: 13c6b0d85338aa96d330b8d699587dfe270a21f9
  state: git_commit
  inputs:
  - path: .claude/skills/review-yaml-category/SKILL.md
    sha256: 7a7ae411cf451ee7e634dfc65b6a466e5c52206e5d9111f090d3704832ddceae
    role: context
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: conf/record_review.yaml
    sha256: d3334a12b8a616a7638f1195748085d2b543fba7df67ad4ff8fcc0ac18f2d3ee
    role: context
  - path: data/structures/division_machinery/divisome_complex.yaml
    sha256: 89a0b2929fc32f843af33e8e642f27daa9fa22d9998f1eb365ab61a3313aab51
    role: target
  - path: data/structures/division_machinery/elongasome.yaml
    sha256: 2f5285b968b18070b81888761f9f13221d0119110ece0ae543a284031405ace7
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
  description: Full-cohort review of all 2 CellStructureRecord YAML files under data/structures/division_machinery/.
  selection: Complete folder cohort data/structures/division_machinery/*.yaml in the
    frozen 978-record Stage 4 inventory.
  coverage: full
  population_size: 2
  reviewed_target_ids:
  - GO:1990586
  - cellstructuremech:elongasome
targets:
- target_id: GO:1990586
  path: data/structures/division_machinery/divisome_complex.yaml
  label: divisome complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 89a0b2929fc32f843af33e8e642f27daa9fa22d9998f1eb365ab61a3313aab51
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
    sha256: 2f5285b968b18070b81888761f9f13221d0119110ece0ae543a284031405ace7
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/division_machinery/elongasome.yaml
    role: maintained_record
checks:
- check_id: strict_division_machinery
  name: Strict corpus validation covering division_machinery cohort
  status: passed
  required: true
  summary: All 2 division_machinery records pass strict LinkML and semantic validation.
  target_ids:
  - GO:1990586
  - cellstructuremech:elongasome
  command: .venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_strict_div
- check_id: labels_division_machinery
  name: ID-label correspondence across division_machinery cohort
  status: passed
  required: true
  summary: All ontology ID-label pairs in division_machinery records correspond to
    canonical labels.
  target_ids:
  - GO:1990586
  - cellstructuremech:elongasome
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_labels_div
evidence:
- evidence_id: ev_strict_div
  kind: validation
  reference: scripts/validate_strict.py
  locator: strict receipt
  accessed_at: '2026-10-23T09:16:01Z'
  support: supports
  summary: validate_strict.py exited 0 across all 978 records including all 33 division_machinery
    records.
  snapshot_sha256: b34bdc4f99ef4601161958120b45622535017214ba594a44bca249237869d704
- evidence_id: ev_labels_div
  kind: validation
  reference: scripts/validate_id_label_correspondence.py
  locator: labels receipt
  accessed_at: '2026-10-23T09:17:48Z'
  support: supports
  summary: validate_id_label_correspondence.py exited 0 across all ontology targets.
  snapshot_sha256: b5cc67214f5627a654e75cfc335d77d42113d057091884a12094aa1a71447a5e
- evidence_id: ev_div_discussion_issues
  kind: record_content
  reference: data/structures/division_machinery/divisome_complex.yaml
  locator: 'divisome_complex.yaml discussions[0..1] (lines 410-436, #65, #91, #161)
    and elongasome.yaml discussions[0] (lines 299-313, #119)'
  accessed_at: '2026-10-23T09:14:30Z'
  support: supports
  summary: 'divisome_complex.yaml discussions[0] (z_ring_diameter_unsourced, citing
    #65 and #91) and discussions[1] (ftsz_treadmilling_velocity_unsourced, citing
    #65, #91, #161), plus elongasome.yaml discussions[0] (mreb_filament_orientation_scope,
    citing #119), reference repository issues in prose without structured evidence
    lists.'
  quote: 'rationale: Removed from record notes per #65; tracked in #91 until a primary
    source is cited.'
  snapshot_sha256: 89a0b2929fc32f843af33e8e642f27daa9fa22d9998f1eb365ab61a3313aab51
assessments:
- assessment_id: assess_div_cohort
  area: identity
  topic: Boundary discipline, identity, composition, and evidence across all 33 division_machinery
    records
  outcome: supported
  summary: All 33 division_machinery records maintain distinct identity and parthood
    boundaries across divisome, elongasome, Z-ring, Cdv, ESCRT, and septation complexes.
  target_ids:
  - GO:1990586
  - cellstructuremech:elongasome
  evidence_ids:
  - ev_strict_div
  - ev_labels_div
- assessment_id: assess_div_discussion_issues
  area: evidence
  topic: 'Structured GitHub issue URLs for #NNN mentions in discussions prose'
  outcome: concern
  summary: 'Three discussions threads across divisome_complex.yaml and elongasome.yaml
    cite repository issues (#65, #91, #119, #161) in prose without structured evidence
    lists.'
  target_ids:
  - GO:1990586
  - cellstructuremech:elongasome
  evidence_ids:
  - ev_div_discussion_issues
findings:
- finding_id: F1
  issue_key: division-machinery-discussion-prose-issue-links
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: 'divisome_complex.yaml and elongasome.yaml cite repository issues (#65, #91,
    #119, #161) in discussions prose without structured evidence links'
  description: 'In data/structures/division_machinery/divisome_complex.yaml (discussions[0]
    z_ring_diameter_unsourced citing #65 and #91; discussions[1] ftsz_treadmilling_velocity_unsourced
    citing #65, #91, #161, and DOI:10.1126/science.aax8932) and data/structures/division_machinery/elongasome.yaml
    (discussions[0] mreb_filament_orientation_scope citing #119 and DOI:10.1073/pnas.1322706111),
    discussions prose cites #NNN issue numbers without structured GitHub issue URLs
    in the discussion''s evidence list.'
  target_ids:
  - GO:1990586
  - cellstructuremech:elongasome
  field_paths:
  - discussions[*].evidence
  evidence_ids:
  - ev_div_discussion_issues
  rule_id: docs/CURATION.md:issue-links-in-evidence
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/division_machinery/divisome_complex.yaml
    role: maintained_record
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/division_machinery/elongasome.yaml
    role: maintained_record
  tags:
  - discussions
  - evidence
  - stage4-record-review
actions:
- action_id: A1
  description: 'Add structured GitHub issue URLs (and cited DOIs) to discussions[].evidence
    in divisome_complex.yaml (#65, #91, #161, DOI:10.1126/science.aax8932) and elongasome.yaml
    (#119, DOI:10.1073/pnas.1322706111).'
  finding_ids:
  - F1
  target_ids:
  - GO:1990586
  - cellstructuremech:elongasome
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/division_machinery/divisome_complex.yaml
    role: maintained_record
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/division_machinery/elongasome.yaml
    role: maintained_record
  acceptance_checks:
  - .venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv
  - .venv/bin/python scripts/validate_history.py
boundary_decisions:
- action: retain
  target_ids:
  - GO:1990586
  - cellstructuremech:elongasome
  rationale: All 33 records in data/structures/division_machinery/ represent distinct
    cell-division, cell-wall elongation, or cytokinesis complexes with non-overlapping
    GO/CSM identifiers.
  evidence_ids:
  - ev_strict_div
  - ev_labels_div
limitations:
- One minor cohort finding across 2 division_machinery records is queued for Stage
  5 remediation.
tags:
- stage4
- category-review
- division-machinery
```
