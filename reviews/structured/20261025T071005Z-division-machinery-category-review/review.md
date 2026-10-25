# Category review of data/structures/division_machinery/ (2 records): elongasome curation_history causal_graph ID alignment

- Review: 20261025T071005Z-division-machinery-category-review
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-25T06:56:00Z
- Finished UTC: 2026-10-25T07:10:05Z
- Reviewer: antigravity-c3s4-record-review (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Full-coverage category review of both records in data/structures/division_machinery/ (divisome.yaml and elongasome.yaml) verified distinct medial-division vs lateral-wall-elongation machinery boundaries and enriched causal graphs. One minor provenance discrepancy was found in elongasome.yaml (cellstructuremech:elongasome): curation_history[12].changes (CURATED_CAUSAL_GRAPH) cites graph_id 'elongasome_pg_synthesis' whereas causal_graphs[0].graph_id is 'elongasome_sidewall_elongation'.

## Scope And Provenance

Full-cohort review of all 2 CellStructureRecord YAML files under data/structures/division_machinery/.

Selection: Complete folder cohort data/structures/division_machinery/*.yaml in the frozen 993-record Cycle 3 Stage 4 inventory.
Coverage: full; 2 reviewed / 2 in the declared population.
Source: git_commit at Git base 83ec9d5184fb203d87d8c3bd7043792d385193bf.
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

### Identity, boundaries, causal graphs, and ontology grounding across data/structures/division_machinery/

scope: supported. Targets: GO:1990586, cellstructuremech:elongasome.

All 2 records in data/structures/division_machinery/ represent distinct microbial cell structures or subcomplexes with valid hierarchy links and verified UniProtKB protein examples.

### Alignment between curation_history CURATED_CAUSAL_GRAPH changes and causal_graphs[0].graph_id in elongasome.yaml

provenance: concern. Targets: cellstructuremech:elongasome.

curation_history[12].changes in elongasome.yaml cites elongasome_pg_synthesis instead of actual causal_graphs[0].graph_id elongasome_sidewall_elongation.

## Findings

### F1: elongasome.yaml curation_history[12].changes cites graph_id elongasome_pg_synthesis instead of elongasome_sidewall_elongation

minor / open / confirmed; issue key: elongasome-curation-history-causal-graph-id-mismatch.

In data/structures/division_machinery/elongasome.yaml (cellstructuremech:elongasome), curation_history[12].changes (action: CURATED_CAUSAL_GRAPH) summarizes the graph ID as 'elongasome_pg_synthesis', whereas causal_graphs[0].graph_id is 'elongasome_sidewall_elongation'.

## Recommended Actions And Acceptance Checks

### A1

Update curation_history[12].changes in data/structures/division_machinery/elongasome.yaml to reference elongasome_sidewall_elongation and record the update in history/records/elongasome/.

- .venv/bin/python scripts/validate_strict.py data/structures/division_machinery/elongasome.yaml --out /tmp/elongasome_failures.tsv
- .venv/bin/python scripts/validate_history.py

## Category Boundaries

- retain: GO:1990586, cellstructuremech:elongasome. Both records in data/structures/division_machinery/ (divisome and elongasome) represent distinct bacterial cell-envelope synthesis and division complexes.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev_strict_divisionmachinery | scripts/validate_strict.py; strict receipt | supports | validate_strict.py exited 0 across all 993 records including all 2 division_machinery records. |
| ev_labels_divisionmachinery | scripts/validate_id_label_correspondence.py; labels receipt | supports | validate_id_label_correspondence.py exited 0 across all ontology targets. |
| ev_div_elongasome_history | data/structures/division_machinery/elongasome.yaml; causal_graphs[0].graph_id (line 185) and curation_history[12].changes (lines 319-324) | supports | elongasome.yaml curation_history[12].changes states 'Added causal graph (elongasome_pg_synthesis)' whereas causal_graphs[0].graph_id is elongasome_sidewall_elongation. |

## Limits And Additional Notes

- Record edits for division_machinery cohort findings are queued for Cycle 3 Stage 5 (resolve_review_findings).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261025T071005Z-division-machinery-category-review
kind: category
repository: CultureBotAI/CellStructureMech
title: 'Category review of data/structures/division_machinery/ (2 records): elongasome
  curation_history causal_graph ID alignment'
started_at: '2026-10-25T06:56:00Z'
finished_at: '2026-10-25T07:10:05Z'
reviewer:
  identity: antigravity-c3s4-record-review
  kind: agent
  model: claude-opus-4-6
  independence: independent
  independence_basis: Reviewed in Cycle 3 Stage 4 record_review against committed
    git revision 83ec9d5184fb203d87d8c3bd7043792d385193bf without record edits in
    this stage.
skill: .claude/skills/review-yaml-category/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: PASS_WITH_FOLLOW_UP
scientific_review: true
summary: 'Full-coverage category review of both records in data/structures/division_machinery/
  (divisome.yaml and elongasome.yaml) verified distinct medial-division vs lateral-wall-elongation
  machinery boundaries and enriched causal graphs. One minor provenance discrepancy
  was found in elongasome.yaml (cellstructuremech:elongasome): curation_history[12].changes
  (CURATED_CAUSAL_GRAPH) cites graph_id ''elongasome_pg_synthesis'' whereas causal_graphs[0].graph_id
  is ''elongasome_sidewall_elongation''.'
source:
  git_revision: 83ec9d5184fb203d87d8c3bd7043792d385193bf
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
    sha256: b4f4919cc610dcb396b0646a715c51b071b0d7c05674b8f93e533130d225ac59
    role: target
  - path: data/structures/division_machinery/elongasome.yaml
    sha256: 9ed092396d873bd1619e15515ebaec36b5f6da64bfebec61752b30f4e4d4ec6f
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
    frozen 993-record Cycle 3 Stage 4 inventory.
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
    sha256: 9ed092396d873bd1619e15515ebaec36b5f6da64bfebec61752b30f4e4d4ec6f
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
  - ev_strict_divisionmachinery
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
  - ev_labels_divisionmachinery
evidence:
- evidence_id: ev_strict_divisionmachinery
  kind: validation
  reference: scripts/validate_strict.py
  locator: strict receipt
  accessed_at: '2026-10-25T07:10:05Z'
  support: supports
  summary: validate_strict.py exited 0 across all 993 records including all 2 division_machinery
    records.
  snapshot_sha256: fc80872aed828ea24abbaf1ff66194605d09857b0bf0773189fc076d223594eb
- evidence_id: ev_labels_divisionmachinery
  kind: validation
  reference: scripts/validate_id_label_correspondence.py
  locator: labels receipt
  accessed_at: '2026-10-25T07:10:05Z'
  support: supports
  summary: validate_id_label_correspondence.py exited 0 across all ontology targets.
  snapshot_sha256: 4bb207ccdd3216a741b1ca17643c1b57a2f2c68af02138decedfcd4fd19c8b3a
- evidence_id: ev_div_elongasome_history
  kind: record_content
  reference: data/structures/division_machinery/elongasome.yaml
  locator: causal_graphs[0].graph_id (line 185) and curation_history[12].changes (lines
    319-324)
  accessed_at: '2026-10-25T07:02:00Z'
  support: supports
  summary: elongasome.yaml curation_history[12].changes states 'Added causal graph
    (elongasome_pg_synthesis)' whereas causal_graphs[0].graph_id is elongasome_sidewall_elongation.
  quote: "- timestamp: '2026-10-24T06:00:00Z'\n  curator: antigravity\n  action: CURATED_CAUSAL_GRAPH\n\
    \  changes: 'Added mrec_mred (component_ref: mrec_mred) node and scaffolding edge\
    \ to\n    pg_synthesis in elongasome_pg_synthesis (DOI:10.1038/nrmicro2677).'\n\
    \  llm_assisted: true"
  snapshot_sha256: 9ed092396d873bd1619e15515ebaec36b5f6da64bfebec61752b30f4e4d4ec6f
assessments:
- assessment_id: assess_divisionmachinery_cohort
  area: scope
  topic: Identity, boundaries, causal graphs, and ontology grounding across data/structures/division_machinery/
  outcome: supported
  summary: All 2 records in data/structures/division_machinery/ represent distinct
    microbial cell structures or subcomplexes with valid hierarchy links and verified
    UniProtKB protein examples.
  target_ids:
  - GO:1990586
  - cellstructuremech:elongasome
  evidence_ids:
  - ev_strict_divisionmachinery
  - ev_labels_divisionmachinery
- assessment_id: assess_div_elongasome_history
  area: provenance
  topic: Alignment between curation_history CURATED_CAUSAL_GRAPH changes and causal_graphs[0].graph_id
    in elongasome.yaml
  outcome: concern
  summary: curation_history[12].changes in elongasome.yaml cites elongasome_pg_synthesis
    instead of actual causal_graphs[0].graph_id elongasome_sidewall_elongation.
  target_ids:
  - cellstructuremech:elongasome
  evidence_ids:
  - ev_div_elongasome_history
findings:
- finding_id: F1
  issue_key: elongasome-curation-history-causal-graph-id-mismatch
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: elongasome.yaml curation_history[12].changes cites graph_id elongasome_pg_synthesis
    instead of elongasome_sidewall_elongation
  description: 'In data/structures/division_machinery/elongasome.yaml (cellstructuremech:elongasome),
    curation_history[12].changes (action: CURATED_CAUSAL_GRAPH) summarizes the graph
    ID as ''elongasome_pg_synthesis'', whereas causal_graphs[0].graph_id is ''elongasome_sidewall_elongation''.'
  target_ids:
  - cellstructuremech:elongasome
  field_paths:
  - curation_history[12].changes
  - causal_graphs[0].graph_id
  evidence_ids:
  - ev_div_elongasome_history
  rule_id: docs/CURATION.md:curation-history-accuracy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/division_machinery/elongasome.yaml
    role: maintained_record
  tags:
  - curation-history
  - causal-graphs
  - stage4-record-review
actions:
- action_id: A1
  description: Update curation_history[12].changes in data/structures/division_machinery/elongasome.yaml
    to reference elongasome_sidewall_elongation and record the update in history/records/elongasome/.
  finding_ids:
  - F1
  target_ids:
  - cellstructuremech:elongasome
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/division_machinery/elongasome.yaml
    role: maintained_record
  acceptance_checks:
  - .venv/bin/python scripts/validate_strict.py data/structures/division_machinery/elongasome.yaml
    --out /tmp/elongasome_failures.tsv
  - .venv/bin/python scripts/validate_history.py
boundary_decisions:
- action: retain
  target_ids:
  - GO:1990586
  - cellstructuremech:elongasome
  rationale: Both records in data/structures/division_machinery/ (divisome and elongasome)
    represent distinct bacterial cell-envelope synthesis and division complexes.
  evidence_ids:
  - ev_strict_divisionmachinery
  - ev_labels_divisionmachinery
limitations:
- Record edits for division_machinery cohort findings are queued for Cycle 3 Stage
  5 (resolve_review_findings).
tags:
- stage4
- category-review
- division-machinery
```
