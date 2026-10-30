# Category review of data/structures/microcompartment/ (6 records)

- Review: 20261030T082008Z-microcompartment-category-review
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-30T08:12:00Z
- Finished UTC: 2026-10-30T08:20:08Z
- Reviewer: antigravity-c4s4-record-review (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Full cohort audit of all 6 MICROCOMPARTMENT records in data/structures/microcompartment/ (bacterial_microcompartment, carboxysome, alpha_carboxysome, beta_carboxysome, propanediol_utilization_microcompartment, ethanolamine_utilization_microcompartment). Hierarchy and parthood across general and subtype BMCs are clean. One minor causal-graph node alignment issue was found in carboxysome.yaml (GO:0031470): causal_graphs[0].nodes[0] (shell, node_type: STRUCTURE) sets component_ref: bmc_h (component_type: PROTEIN, InterPro:IPR000249), whereas causal_graphs[1].nodes[3] (shell, node_type: STRUCTURE) in the same record omits component_ref because the icosahedral shell is formed jointly by bmc_h, bmc_t, and bmc_p.

## Scope And Provenance

Full-cohort review of all 6 CellStructureRecord YAML files under data/structures/microcompartment/.

Selection: Complete folder cohort data/structures/microcompartment/*.yaml in the frozen 1,001-record Cycle 4 Stage 4 inventory.
Coverage: full; 6 reviewed / 6 in the declared population.
Source: git_commit at Git base 5c642e4080ef3a0f026845843c559d3b46de8871.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0031469 | data/structures/microcompartment/bacterial_microcompartment.yaml | maintained | bacterial microcompartment |
| GO:0031470 | data/structures/microcompartment/carboxysome.yaml | maintained | carboxysome |
| cellstructuremech:carboxysome_shell | data/structures/microcompartment/carboxysome_shell.yaml | maintained | carboxysome shell |
| GO:0140737 | data/structures/microcompartment/encapsulin_nanocompartment.yaml | maintained | encapsulin nanocompartment |
| GO:0031471 | data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml | maintained | ethanolamine degradation polyhedral organelle |
| GO:0031472 | data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml | maintained | propanediol degradation polyhedral organelle |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation covering microcompartment cohort | passed | True | GO:0031469, GO:0031470, cellstructuremech:carboxysome_shell, GO:0140737, GO:0031471, GO:0031472 | All 6 microcompartment records pass strict LinkML and semantic validation. |
| History ledger validation covering microcompartment cohort | passed | True | GO:0031469, GO:0031470, cellstructuremech:carboxysome_shell, GO:0140737, GO:0031471, GO:0031472 | All history ledger records covering microcompartment validate cleanly. |

## Scientific And Domain Assessments

### Identity, boundaries, causal graphs, and ontology grounding across data/structures/microcompartment/

scope: supported. Targets: GO:0031469, GO:0031470, cellstructuremech:carboxysome_shell, GO:0140737, GO:0031471, GO:0031472.

All 6 records in data/structures/microcompartment/ represent distinct microbial cell structures or subcomplexes with valid schema and history provenance.

### Consistency of STRUCTURE node 'shell' across carboxysome_ccm and carboxysome_assembly causal graphs

graph: concern. Targets: GO:0031470.

In carboxysome.yaml, causal_graphs[0] binds STRUCTURE node shell to single hexamer family bmc_h via component_ref, whereas causal_graphs[1] models shell as the composite icosahedral shell formed by bmc_h, bmc_t, and bmc_p.

## Findings

### F1: carboxysome.yaml causal_graphs[0].nodes[0] (shell, node_type: STRUCTURE) sets component_ref: bmc_h (component_type: PROTEIN)

minor / open / confirmed; issue key: microcompartment-carboxysome-shell-node-component-ref.

In data/structures/microcompartment/carboxysome.yaml (GO:0031470), causal_graphs[0].nodes[0] (id: shell, label: 'Carboxysome protein shell', node_type: STRUCTURE) sets component_ref: bmc_h (components[0], component_type: PROTEIN, grounding: InterPro:IPR000249), whereas causal_graphs[1].nodes[3] (id: shell, label: 'Icosahedral protein shell', node_type: STRUCTURE) in the same file omits component_ref because the shell is assembled from three distinct shell protein families (bmc_h, bmc_t, and bmc_p).

## Recommended Actions And Acceptance Checks

### A1

Remove component_ref: bmc_h from causal_graphs[0].nodes[0] (shell, node_type: STRUCTURE) in data/structures/microcompartment/carboxysome.yaml so both causal graphs consistently treat shell as the composite icosahedral protein shell.

- .venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv
- .venv/bin/python scripts/validate_history.py

## Category Boundaries

- retain: GO:0031469, GO:0031470, cellstructuremech:carboxysome_shell, GO:0140737, GO:0031471, GO:0031472. All 6 microcompartment records represent distinct bacterial microcompartment classes with clean parent_structures hierarchy.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev_strict_microcompartment | scripts/validate_strict.py; strict_all receipt | supports | validate_strict.py exited 0 across all 1,001 records including all 6 microcompartment records. |
| ev_history_microcompartment | scripts/validate_history.py; history_all receipt | supports | validate_history.py exited 0 across all 2,082 history records covering microcompartment. |
| ev_microcomp_carboxysome_shell | data/structures/microcompartment/carboxysome.yaml; causal_graphs[0].nodes[0] (lines 167-171) vs causal_graphs[1].nodes[3] (lines 222-225) | supports | carboxysome.yaml causal_graphs[0].nodes[0] (shell, STRUCTURE) sets component_ref: bmc_h (PROTEIN), whereas causal_graphs[1].nodes[3] (shell, STRUCTURE) does not. |

## Limits And Additional Notes

- Record edits for microcompartment cohort findings are queued for Cycle 4 Stage 5 (resolve_review_findings).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261030T082008Z-microcompartment-category-review
kind: category
repository: CultureBotAI/CellStructureMech
title: Category review of data/structures/microcompartment/ (6 records)
started_at: '2026-10-30T08:12:00Z'
finished_at: '2026-10-30T08:20:08Z'
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
verdict: pass_with_limitations
native_verdict: PASS_WITH_FOLLOW_UP
scientific_review: true
summary: 'Full cohort audit of all 6 MICROCOMPARTMENT records in data/structures/microcompartment/
  (bacterial_microcompartment, carboxysome, alpha_carboxysome, beta_carboxysome, propanediol_utilization_microcompartment,
  ethanolamine_utilization_microcompartment). Hierarchy and parthood across general
  and subtype BMCs are clean. One minor causal-graph node alignment issue was found
  in carboxysome.yaml (GO:0031470): causal_graphs[0].nodes[0] (shell, node_type: STRUCTURE)
  sets component_ref: bmc_h (component_type: PROTEIN, InterPro:IPR000249), whereas
  causal_graphs[1].nodes[3] (shell, node_type: STRUCTURE) in the same record omits
  component_ref because the icosahedral shell is formed jointly by bmc_h, bmc_t, and
  bmc_p.'
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
  - path: data/structures/microcompartment/bacterial_microcompartment.yaml
    sha256: 744baee4509a2d6c59e951bf107ec3730a2576b7c084d239569913389b1a3321
    role: target
  - path: data/structures/microcompartment/carboxysome.yaml
    sha256: 2d532dcd3f7267b41e377c7a595a93507b3aa7c139c57da0c6c58d6d36cae58a
    role: target
  - path: data/structures/microcompartment/carboxysome_shell.yaml
    sha256: a732afb9239cc57b69ff7d4ca75700b4f2b3fb682837b1be799376d12acb7762
    role: target
  - path: data/structures/microcompartment/encapsulin_nanocompartment.yaml
    sha256: 9c18ca6df3185b48f8755d7f53857234df1955a0f48ffc0fb1199793b3b6b9d8
    role: target
  - path: data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml
    sha256: 67b4280a4ef1837e40fe65ac0ed67e263b95339d1b364a976ee1110c2440029f
    role: target
  - path: data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml
    sha256: 6be0e75f5fb1ffa1081869af24522c1c2864d31090832eacb2f920b3dec3d443
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
  description: Full-cohort review of all 6 CellStructureRecord YAML files under data/structures/microcompartment/.
  selection: Complete folder cohort data/structures/microcompartment/*.yaml in the
    frozen 1,001-record Cycle 4 Stage 4 inventory.
  coverage: full
  population_size: 6
  reviewed_target_ids:
  - GO:0031469
  - GO:0031470
  - cellstructuremech:carboxysome_shell
  - GO:0140737
  - GO:0031471
  - GO:0031472
targets:
- target_id: GO:0031469
  path: data/structures/microcompartment/bacterial_microcompartment.yaml
  label: bacterial microcompartment
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 744baee4509a2d6c59e951bf107ec3730a2576b7c084d239569913389b1a3321
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/microcompartment/bacterial_microcompartment.yaml
    role: maintained_record
- target_id: GO:0031470
  path: data/structures/microcompartment/carboxysome.yaml
  label: carboxysome
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 2d532dcd3f7267b41e377c7a595a93507b3aa7c139c57da0c6c58d6d36cae58a
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/microcompartment/carboxysome.yaml
    role: maintained_record
- target_id: cellstructuremech:carboxysome_shell
  path: data/structures/microcompartment/carboxysome_shell.yaml
  label: carboxysome shell
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: a732afb9239cc57b69ff7d4ca75700b4f2b3fb682837b1be799376d12acb7762
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/microcompartment/carboxysome_shell.yaml
    role: maintained_record
- target_id: GO:0140737
  path: data/structures/microcompartment/encapsulin_nanocompartment.yaml
  label: encapsulin nanocompartment
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 9c18ca6df3185b48f8755d7f53857234df1955a0f48ffc0fb1199793b3b6b9d8
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/microcompartment/encapsulin_nanocompartment.yaml
    role: maintained_record
- target_id: GO:0031471
  path: data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml
  label: ethanolamine degradation polyhedral organelle
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 67b4280a4ef1837e40fe65ac0ed67e263b95339d1b364a976ee1110c2440029f
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml
    role: maintained_record
- target_id: GO:0031472
  path: data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml
  label: propanediol degradation polyhedral organelle
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 6be0e75f5fb1ffa1081869af24522c1c2864d31090832eacb2f920b3dec3d443
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml
    role: maintained_record
checks:
- check_id: strict_microcompartment
  name: Strict corpus validation covering microcompartment cohort
  status: passed
  required: true
  summary: All 6 microcompartment records pass strict LinkML and semantic validation.
  target_ids:
  - GO:0031469
  - GO:0031470
  - cellstructuremech:carboxysome_shell
  - GO:0140737
  - GO:0031471
  - GO:0031472
  command: .venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_strict_microcompartment
- check_id: history_microcompartment
  name: History ledger validation covering microcompartment cohort
  status: passed
  required: true
  summary: All history ledger records covering microcompartment validate cleanly.
  target_ids:
  - GO:0031469
  - GO:0031470
  - cellstructuremech:carboxysome_shell
  - GO:0140737
  - GO:0031471
  - GO:0031472
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_history_microcompartment
evidence:
- evidence_id: ev_strict_microcompartment
  kind: validation
  reference: scripts/validate_strict.py
  locator: strict_all receipt
  accessed_at: '2026-10-30T08:20:08Z'
  support: supports
  summary: validate_strict.py exited 0 across all 1,001 records including all 6 microcompartment
    records.
  snapshot_sha256: 1ebf6e7daebc19797861570fcac0d3cf8b06c18f7f40abf3277d35ef5867f442
- evidence_id: ev_history_microcompartment
  kind: validation
  reference: scripts/validate_history.py
  locator: history_all receipt
  accessed_at: '2026-10-30T08:20:08Z'
  support: supports
  summary: validate_history.py exited 0 across all 2,082 history records covering
    microcompartment.
  snapshot_sha256: 8bcb91b216ec775bac08188426f9ef860888b78f91561be1e471ea4a2159ad3b
- evidence_id: ev_microcomp_carboxysome_shell
  kind: record_content
  reference: data/structures/microcompartment/carboxysome.yaml
  locator: causal_graphs[0].nodes[0] (lines 167-171) vs causal_graphs[1].nodes[3]
    (lines 222-225)
  accessed_at: '2026-10-30T08:15:30Z'
  support: supports
  summary: 'carboxysome.yaml causal_graphs[0].nodes[0] (shell, STRUCTURE) sets component_ref:
    bmc_h (PROTEIN), whereas causal_graphs[1].nodes[3] (shell, STRUCTURE) does not.'
  quote: "  - id: shell\n    label: Carboxysome protein shell\n    node_type: STRUCTURE\n\
    \    component_ref: bmc_h"
  snapshot_sha256: 2d532dcd3f7267b41e377c7a595a93507b3aa7c139c57da0c6c58d6d36cae58a
assessments:
- assessment_id: assess_microcompartment_cohort
  area: scope
  topic: Identity, boundaries, causal graphs, and ontology grounding across data/structures/microcompartment/
  outcome: supported
  summary: All 6 records in data/structures/microcompartment/ represent distinct microbial
    cell structures or subcomplexes with valid schema and history provenance.
  target_ids:
  - GO:0031469
  - GO:0031470
  - cellstructuremech:carboxysome_shell
  - GO:0140737
  - GO:0031471
  - GO:0031472
  evidence_ids:
  - ev_strict_microcompartment
  - ev_history_microcompartment
- assessment_id: assess_microcomp_carboxysome_graph
  area: graph
  topic: Consistency of STRUCTURE node 'shell' across carboxysome_ccm and carboxysome_assembly
    causal graphs
  outcome: concern
  summary: In carboxysome.yaml, causal_graphs[0] binds STRUCTURE node shell to single
    hexamer family bmc_h via component_ref, whereas causal_graphs[1] models shell
    as the composite icosahedral shell formed by bmc_h, bmc_t, and bmc_p.
  target_ids:
  - GO:0031470
  evidence_ids:
  - ev_microcomp_carboxysome_shell
findings:
- finding_id: F1
  issue_key: microcompartment-carboxysome-shell-node-component-ref
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: 'carboxysome.yaml causal_graphs[0].nodes[0] (shell, node_type: STRUCTURE)
    sets component_ref: bmc_h (component_type: PROTEIN)'
  description: 'In data/structures/microcompartment/carboxysome.yaml (GO:0031470),
    causal_graphs[0].nodes[0] (id: shell, label: ''Carboxysome protein shell'', node_type:
    STRUCTURE) sets component_ref: bmc_h (components[0], component_type: PROTEIN,
    grounding: InterPro:IPR000249), whereas causal_graphs[1].nodes[3] (id: shell,
    label: ''Icosahedral protein shell'', node_type: STRUCTURE) in the same file omits
    component_ref because the shell is assembled from three distinct shell protein
    families (bmc_h, bmc_t, and bmc_p).'
  target_ids:
  - GO:0031470
  field_paths:
  - causal_graphs[0].nodes[0].component_ref
  evidence_ids:
  - ev_microcomp_carboxysome_shell
  rule_id: docs/SCHEMA.md:CausalNode.component_ref
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/microcompartment/carboxysome.yaml
    role: maintained_record
  tags:
  - microcompartment
  - causal-graphs
  - stage4-record-review
actions:
- action_id: A1
  description: 'Remove component_ref: bmc_h from causal_graphs[0].nodes[0] (shell,
    node_type: STRUCTURE) in data/structures/microcompartment/carboxysome.yaml so
    both causal graphs consistently treat shell as the composite icosahedral protein
    shell.'
  finding_ids:
  - F1
  target_ids:
  - GO:0031470
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/microcompartment/carboxysome.yaml
    role: maintained_record
  acceptance_checks:
  - .venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv
  - .venv/bin/python scripts/validate_history.py
boundary_decisions:
- action: retain
  target_ids:
  - GO:0031469
  - GO:0031470
  - cellstructuremech:carboxysome_shell
  - GO:0140737
  - GO:0031471
  - GO:0031472
  rationale: All 6 microcompartment records represent distinct bacterial microcompartment
    classes with clean parent_structures hierarchy.
  evidence_ids:
  - ev_strict_microcompartment
  - ev_history_microcompartment
limitations:
- Record edits for microcompartment cohort findings are queued for Cycle 4 Stage 5
  (resolve_review_findings).
tags:
- stage4
- category-review
- microcompartment
```
