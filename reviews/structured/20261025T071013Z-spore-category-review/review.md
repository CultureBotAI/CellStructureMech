# Category review of data/structures/spore/ (23 records): ascospore_wall.yaml chitosan_outer_layer causal-node grounding propagation

- Review: 20261025T071013Z-spore-category-review
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-25T06:56:00Z
- Finished UTC: 2026-10-25T07:10:13Z
- Reviewer: antigravity-c3s4-record-review (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Full-coverage category review of all 23 records in data/structures/spore/ verified distinct bacterial endospore, fungal ascospore/prospore, and microsporidian spore apparatus boundaries. One minor causal-graph grounding gap was identified in ascospore_wall.yaml (GO:0005619): causal_graphs[0].nodes[3] (node_id: chitosan_outer_layer, component_ref: chitosan_outer_layer) omits grounding: CHEBI:16261 declared on components#chitosan_outer_layer.

## Scope And Provenance

Full-cohort review of all 23 CellStructureRecord YAML files under data/structures/spore/.

Selection: Complete folder cohort data/structures/spore/*.yaml in the frozen 993-record Cycle 3 Stage 4 inventory.
Coverage: full; 23 reviewed / 23 in the declared population.
Source: git_commit at Git base 83ec9d5184fb203d87d8c3bd7043792d385193bf.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0042764 | data/structures/spore/ascospore_type_prospore.yaml | maintained | ascospore-type prospore |
| GO:1905754 | data/structures/spore/ascospore_type_prospore_nucleus.yaml | maintained | ascospore-type prospore nucleus |
| GO:0005619 | data/structures/spore/ascospore_wall.yaml | maintained | ascospore wall |
| GO:0005631 | data/structures/spore/chitosan_layer_of_spore_wall.yaml | maintained | chitosan layer of spore wall |
| GO:0005630 | data/structures/spore/dityrosine_layer_of_spore_wall.yaml | maintained | dityrosine layer of spore wall |
| GO:0043593 | data/structures/spore/endospore_coat.yaml | maintained | endospore coat |
| GO:0070477 | data/structures/spore/endospore_core.yaml | maintained | endospore core |
| GO:0043595 | data/structures/spore/endospore_cortex.yaml | maintained | endospore cortex |
| GO:0043591 | data/structures/spore/endospore_external_encapsulating_structure.yaml | maintained | endospore external encapsulating structure |
| GO:0042601 | data/structures/spore/endospore_forming_forespore.yaml | maintained | endospore-forming forespore |
| GO:0043592 | data/structures/spore/exosporium.yaml | maintained | exosporium |
| GO:0005632 | data/structures/spore/inner_layer_of_spore_wall.yaml | maintained | inner layer of spore wall |
| GO:1990916 | data/structures/spore/isp3_layer_of_spore_wall.yaml | maintained | Isp3 layer of spore wall |
| GO:0090641 | data/structures/spore/microsporidian_type_endospore.yaml | maintained | microsporidian-type endospore |
| GO:0090642 | data/structures/spore/microsporidian_type_exospore.yaml | maintained | microsporidian-type exospore |
| GO:0043594 | data/structures/spore/outer_endospore_membrane.yaml | maintained | outer endospore membrane |
| GO:0044099 | data/structures/spore/polar_tube.yaml | maintained | polar tube |
| GO:0160202 | data/structures/spore/polar_tube_anchoring_disc.yaml | maintained | polar tube anchoring disc |
| GO:0005628 | data/structures/spore/prospore_membrane.yaml | maintained | prospore membrane |
| GO:0070056 | data/structures/spore/prospore_membrane_leading_edge.yaml | maintained | prospore membrane leading edge |
| GO:0070057 | data/structures/spore/prospore_membrane_spindle_pole_body_attachment_site.yaml | maintained | prospore membrane spindle pole body attachment site |
| GO:0140549 | data/structures/spore/spore_inner_membrane.yaml | maintained | spore inner membrane |
| GO:0031160 | data/structures/spore/spore_wall.yaml | maintained | spore wall |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation covering spore cohort | passed | True | GO:0042764, GO:1905754, GO:0005619, GO:0005631, GO:0005630, GO:0043593, GO:0070477, GO:0043595, GO:0043591, GO:0042601, GO:0043592, GO:0005632, GO:1990916, GO:0090641, GO:0090642, GO:0043594, GO:0044099, GO:0160202, GO:0005628, GO:0070056, GO:0070057, GO:0140549, GO:0031160 | All 23 spore records pass strict LinkML and semantic validation. |
| ID-label correspondence across spore cohort | passed | True | GO:0042764, GO:1905754, GO:0005619, GO:0005631, GO:0005630, GO:0043593, GO:0070477, GO:0043595, GO:0043591, GO:0042601, GO:0043592, GO:0005632, GO:1990916, GO:0090641, GO:0090642, GO:0043594, GO:0044099, GO:0160202, GO:0005628, GO:0070056, GO:0070057, GO:0140549, GO:0031160 | All ontology ID-label pairs in spore records correspond to canonical labels. |

## Scientific And Domain Assessments

### Identity, boundaries, causal graphs, and ontology grounding across data/structures/spore/

scope: supported. Targets: GO:0042764, GO:1905754, GO:0005619, GO:0005631, GO:0005630, GO:0043593, GO:0070477, GO:0043595, GO:0043591, GO:0042601, GO:0043592, GO:0005632, GO:1990916, GO:0090641, GO:0090642, GO:0043594, GO:0044099, GO:0160202, GO:0005628, GO:0070056, GO:0070057, GO:0140549, GO:0031160.

All 23 records in data/structures/spore/ represent distinct microbial cell structures or subcomplexes with valid hierarchy links and verified UniProtKB protein examples.

### Causal-graph component_ref grounding propagation in ascospore_wall.yaml

graph: concern. Targets: GO:0005619.

causal_graphs[0].nodes[3] (chitosan_outer_layer) in ascospore_wall.yaml omits CHEBI:16261 from components#chitosan_outer_layer.

## Findings

### F1: ascospore_wall.yaml causal_graphs[0].nodes[3] (chitosan_outer_layer) omits verified CHEBI:16261 grounding from components#chitosan_outer_layer

minor / open / confirmed; issue key: spore-ascospore-wall-causal-node-component-ref-grounding.

In data/structures/spore/ascospore_wall.yaml (GO:0005619), components#chitosan_outer_layer declares grounding: CHEBI:16261 (chitosan), whereas causal_graphs[0].nodes[3] (node_id: chitosan_outer_layer, component_ref: chitosan_outer_layer) omits grounding.

## Recommended Actions And Acceptance Checks

### A1

Propagate grounding: CHEBI:16261 (grounding_label: chitosan) to causal_graphs[0].nodes[3] (chitosan_outer_layer) in data/structures/spore/ascospore_wall.yaml and record the update in history/records/ascospore_wall/.

- .venv/bin/python scripts/validate_strict.py data/structures/spore/ascospore_wall.yaml --out /tmp/ascospore_failures.tsv
- .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml

## Category Boundaries

- retain: GO:0042764, GO:1905754, GO:0005619, GO:0005631, GO:0005630, GO:0043593, GO:0070477, GO:0043595, GO:0043591, GO:0042601, GO:0043592, GO:0005632, GO:1990916, GO:0090641, GO:0090642, GO:0043594, GO:0044099, GO:0160202, GO:0005628, GO:0070056, GO:0070057, GO:0140549, GO:0031160. All 23 records in data/structures/spore/ represent distinct bacterial endospore, fungal ascospore/prospore, or microsporidian spore structures.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev_strict_spore | scripts/validate_strict.py; strict receipt | supports | validate_strict.py exited 0 across all 993 records including all 23 spore records. |
| ev_labels_spore | scripts/validate_id_label_correspondence.py; labels receipt | supports | validate_id_label_correspondence.py exited 0 across all ontology targets. |
| ev_sp_ascospore_grounding | data/structures/spore/ascospore_wall.yaml; components#chitosan_outer_layer vs causal_graphs[0].nodes[3] (lines 220-223) | supports | ascospore_wall.yaml components#chitosan_outer_layer declares grounding: CHEBI:16261 whereas causal_graphs[0].nodes[3] (chitosan_outer_layer) omits grounding. |

## Limits And Additional Notes

- Record edits for spore cohort findings are queued for Cycle 3 Stage 5 (resolve_review_findings).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261025T071013Z-spore-category-review
kind: category
repository: CultureBotAI/CellStructureMech
title: 'Category review of data/structures/spore/ (23 records): ascospore_wall.yaml
  chitosan_outer_layer causal-node grounding propagation'
started_at: '2026-10-25T06:56:00Z'
finished_at: '2026-10-25T07:10:13Z'
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
summary: 'Full-coverage category review of all 23 records in data/structures/spore/
  verified distinct bacterial endospore, fungal ascospore/prospore, and microsporidian
  spore apparatus boundaries. One minor causal-graph grounding gap was identified
  in ascospore_wall.yaml (GO:0005619): causal_graphs[0].nodes[3] (node_id: chitosan_outer_layer,
  component_ref: chitosan_outer_layer) omits grounding: CHEBI:16261 declared on components#chitosan_outer_layer.'
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
  - path: data/structures/spore/ascospore_type_prospore.yaml
    sha256: ecde9752e75feafaafe127df75de5db61d4d2ca17825f238f56f02b05cfeed48
    role: target
  - path: data/structures/spore/ascospore_type_prospore_nucleus.yaml
    sha256: 6f96984824c5928cf017034f900c6fc5d686a227107a04c63c2dd9b9fa51750a
    role: target
  - path: data/structures/spore/ascospore_wall.yaml
    sha256: 97c1d9a7123cc5f0e5209c1e4bb6ba15d7ddebe89f5e001363c564938cfbacc7
    role: target
  - path: data/structures/spore/chitosan_layer_of_spore_wall.yaml
    sha256: 0aeb88c94d483c44abea9e6be8de3cb337cc1508b14452b124842f54ffc361a4
    role: target
  - path: data/structures/spore/dityrosine_layer_of_spore_wall.yaml
    sha256: 86c3468857e2f15a3e742faffab939c75c6e45556e0c2286a5e736d740ceda6f
    role: target
  - path: data/structures/spore/endospore_coat.yaml
    sha256: 704dbd6d4e07e904a9ab545eaff6ff5b08295d7537cd462a215900f8102098e4
    role: target
  - path: data/structures/spore/endospore_core.yaml
    sha256: 92d80935979f700d5dc019121c3092df535805c5f91d6da65c18b6f29724a9b3
    role: target
  - path: data/structures/spore/endospore_cortex.yaml
    sha256: 10fbc9261dad43bfc378cd30a8d4ccd4338cccc110a309ae323636415e3f806e
    role: target
  - path: data/structures/spore/endospore_external_encapsulating_structure.yaml
    sha256: ac2cd0c35e2cb6ecd67b518c8be628e33594fbe8081c93e851589c5ce03f37ff
    role: target
  - path: data/structures/spore/endospore_forming_forespore.yaml
    sha256: 9a8fcd588f0f9043c35d8bb5fde36a7141c89a61494798752bae860789d9f537
    role: target
  - path: data/structures/spore/exosporium.yaml
    sha256: c855d90bdd0a47bccc1384875e86326c1383fcfe2e0b6c8e045e06fecec09999
    role: target
  - path: data/structures/spore/inner_layer_of_spore_wall.yaml
    sha256: 0e164d5b4d572b2ffc76af4fdbb1e11316cbfdf7b02b095c37c5f0149739bda9
    role: target
  - path: data/structures/spore/isp3_layer_of_spore_wall.yaml
    sha256: f876af63f561fd1a3f5ee4d5fe33b359cee3f502ea90954bea8f8acac9db2681
    role: target
  - path: data/structures/spore/microsporidian_type_endospore.yaml
    sha256: 580021ae9fb36187c9f8f1500a28f24093a89f8e68cd2331593c01751f08b4cf
    role: target
  - path: data/structures/spore/microsporidian_type_exospore.yaml
    sha256: 8783e96f7961e1d98fdcea0a04365d7113a97e09263cd59cf81e04659017e134
    role: target
  - path: data/structures/spore/outer_endospore_membrane.yaml
    sha256: 0d2b281f27e33d2c52681ac84d8de04ff367979fae90f15af416e1ae09e915cc
    role: target
  - path: data/structures/spore/polar_tube.yaml
    sha256: 89ea679592718479c4ee008135d1aca2fcf19d85f50b837ee23e39943f591623
    role: target
  - path: data/structures/spore/polar_tube_anchoring_disc.yaml
    sha256: 49662b4addd0691548cef8fb96628ac5046330119cc993afbe58719d97622389
    role: target
  - path: data/structures/spore/prospore_membrane.yaml
    sha256: 3ef165721ce16d797936a9881b4e2594ddd24b771ed0f4d0940f773381f55c9b
    role: target
  - path: data/structures/spore/prospore_membrane_leading_edge.yaml
    sha256: 1d5e8efe8ceb3ce24f7f816ffd6653fe3897bae4d10e2dbad4243c390fa5b5d6
    role: target
  - path: data/structures/spore/prospore_membrane_spindle_pole_body_attachment_site.yaml
    sha256: 7349483b810c10d202f0288406bd16468b713c8688c61238d3ce6d6d94222396
    role: target
  - path: data/structures/spore/spore_inner_membrane.yaml
    sha256: 62d3c15151fb7d0d4e1845f38cdb2e729413698c09dc27e14d7112d9afe26d2b
    role: target
  - path: data/structures/spore/spore_wall.yaml
    sha256: 50dea23f2bb94c38c0d0c8ed90fdabc3368d6d20ae4d69bb1ed4218c098d97ab
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
  description: Full-cohort review of all 23 CellStructureRecord YAML files under data/structures/spore/.
  selection: Complete folder cohort data/structures/spore/*.yaml in the frozen 993-record
    Cycle 3 Stage 4 inventory.
  coverage: full
  population_size: 23
  reviewed_target_ids:
  - GO:0042764
  - GO:1905754
  - GO:0005619
  - GO:0005631
  - GO:0005630
  - GO:0043593
  - GO:0070477
  - GO:0043595
  - GO:0043591
  - GO:0042601
  - GO:0043592
  - GO:0005632
  - GO:1990916
  - GO:0090641
  - GO:0090642
  - GO:0043594
  - GO:0044099
  - GO:0160202
  - GO:0005628
  - GO:0070056
  - GO:0070057
  - GO:0140549
  - GO:0031160
targets:
- target_id: GO:0042764
  path: data/structures/spore/ascospore_type_prospore.yaml
  label: ascospore-type prospore
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: ecde9752e75feafaafe127df75de5db61d4d2ca17825f238f56f02b05cfeed48
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/spore/ascospore_type_prospore.yaml
    role: maintained_record
- target_id: GO:1905754
  path: data/structures/spore/ascospore_type_prospore_nucleus.yaml
  label: ascospore-type prospore nucleus
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 6f96984824c5928cf017034f900c6fc5d686a227107a04c63c2dd9b9fa51750a
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/spore/ascospore_type_prospore_nucleus.yaml
    role: maintained_record
- target_id: GO:0005619
  path: data/structures/spore/ascospore_wall.yaml
  label: ascospore wall
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 97c1d9a7123cc5f0e5209c1e4bb6ba15d7ddebe89f5e001363c564938cfbacc7
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/spore/ascospore_wall.yaml
    role: maintained_record
- target_id: GO:0005631
  path: data/structures/spore/chitosan_layer_of_spore_wall.yaml
  label: chitosan layer of spore wall
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 0aeb88c94d483c44abea9e6be8de3cb337cc1508b14452b124842f54ffc361a4
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/spore/chitosan_layer_of_spore_wall.yaml
    role: maintained_record
- target_id: GO:0005630
  path: data/structures/spore/dityrosine_layer_of_spore_wall.yaml
  label: dityrosine layer of spore wall
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 86c3468857e2f15a3e742faffab939c75c6e45556e0c2286a5e736d740ceda6f
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/spore/dityrosine_layer_of_spore_wall.yaml
    role: maintained_record
- target_id: GO:0043593
  path: data/structures/spore/endospore_coat.yaml
  label: endospore coat
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 704dbd6d4e07e904a9ab545eaff6ff5b08295d7537cd462a215900f8102098e4
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/spore/endospore_coat.yaml
    role: maintained_record
- target_id: GO:0070477
  path: data/structures/spore/endospore_core.yaml
  label: endospore core
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 92d80935979f700d5dc019121c3092df535805c5f91d6da65c18b6f29724a9b3
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/spore/endospore_core.yaml
    role: maintained_record
- target_id: GO:0043595
  path: data/structures/spore/endospore_cortex.yaml
  label: endospore cortex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 10fbc9261dad43bfc378cd30a8d4ccd4338cccc110a309ae323636415e3f806e
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/spore/endospore_cortex.yaml
    role: maintained_record
- target_id: GO:0043591
  path: data/structures/spore/endospore_external_encapsulating_structure.yaml
  label: endospore external encapsulating structure
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: ac2cd0c35e2cb6ecd67b518c8be628e33594fbe8081c93e851589c5ce03f37ff
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/spore/endospore_external_encapsulating_structure.yaml
    role: maintained_record
- target_id: GO:0042601
  path: data/structures/spore/endospore_forming_forespore.yaml
  label: endospore-forming forespore
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 9a8fcd588f0f9043c35d8bb5fde36a7141c89a61494798752bae860789d9f537
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/spore/endospore_forming_forespore.yaml
    role: maintained_record
- target_id: GO:0043592
  path: data/structures/spore/exosporium.yaml
  label: exosporium
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: c855d90bdd0a47bccc1384875e86326c1383fcfe2e0b6c8e045e06fecec09999
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/spore/exosporium.yaml
    role: maintained_record
- target_id: GO:0005632
  path: data/structures/spore/inner_layer_of_spore_wall.yaml
  label: inner layer of spore wall
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 0e164d5b4d572b2ffc76af4fdbb1e11316cbfdf7b02b095c37c5f0149739bda9
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/spore/inner_layer_of_spore_wall.yaml
    role: maintained_record
- target_id: GO:1990916
  path: data/structures/spore/isp3_layer_of_spore_wall.yaml
  label: Isp3 layer of spore wall
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: f876af63f561fd1a3f5ee4d5fe33b359cee3f502ea90954bea8f8acac9db2681
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/spore/isp3_layer_of_spore_wall.yaml
    role: maintained_record
- target_id: GO:0090641
  path: data/structures/spore/microsporidian_type_endospore.yaml
  label: microsporidian-type endospore
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 580021ae9fb36187c9f8f1500a28f24093a89f8e68cd2331593c01751f08b4cf
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/spore/microsporidian_type_endospore.yaml
    role: maintained_record
- target_id: GO:0090642
  path: data/structures/spore/microsporidian_type_exospore.yaml
  label: microsporidian-type exospore
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 8783e96f7961e1d98fdcea0a04365d7113a97e09263cd59cf81e04659017e134
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/spore/microsporidian_type_exospore.yaml
    role: maintained_record
- target_id: GO:0043594
  path: data/structures/spore/outer_endospore_membrane.yaml
  label: outer endospore membrane
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 0d2b281f27e33d2c52681ac84d8de04ff367979fae90f15af416e1ae09e915cc
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/spore/outer_endospore_membrane.yaml
    role: maintained_record
- target_id: GO:0044099
  path: data/structures/spore/polar_tube.yaml
  label: polar tube
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 89ea679592718479c4ee008135d1aca2fcf19d85f50b837ee23e39943f591623
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/spore/polar_tube.yaml
    role: maintained_record
- target_id: GO:0160202
  path: data/structures/spore/polar_tube_anchoring_disc.yaml
  label: polar tube anchoring disc
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 49662b4addd0691548cef8fb96628ac5046330119cc993afbe58719d97622389
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/spore/polar_tube_anchoring_disc.yaml
    role: maintained_record
- target_id: GO:0005628
  path: data/structures/spore/prospore_membrane.yaml
  label: prospore membrane
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 3ef165721ce16d797936a9881b4e2594ddd24b771ed0f4d0940f773381f55c9b
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/spore/prospore_membrane.yaml
    role: maintained_record
- target_id: GO:0070056
  path: data/structures/spore/prospore_membrane_leading_edge.yaml
  label: prospore membrane leading edge
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 1d5e8efe8ceb3ce24f7f816ffd6653fe3897bae4d10e2dbad4243c390fa5b5d6
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/spore/prospore_membrane_leading_edge.yaml
    role: maintained_record
- target_id: GO:0070057
  path: data/structures/spore/prospore_membrane_spindle_pole_body_attachment_site.yaml
  label: prospore membrane spindle pole body attachment site
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 7349483b810c10d202f0288406bd16468b713c8688c61238d3ce6d6d94222396
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/spore/prospore_membrane_spindle_pole_body_attachment_site.yaml
    role: maintained_record
- target_id: GO:0140549
  path: data/structures/spore/spore_inner_membrane.yaml
  label: spore inner membrane
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 62d3c15151fb7d0d4e1845f38cdb2e729413698c09dc27e14d7112d9afe26d2b
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/spore/spore_inner_membrane.yaml
    role: maintained_record
- target_id: GO:0031160
  path: data/structures/spore/spore_wall.yaml
  label: spore wall
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 50dea23f2bb94c38c0d0c8ed90fdabc3368d6d20ae4d69bb1ed4218c098d97ab
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/spore/spore_wall.yaml
    role: maintained_record
checks:
- check_id: strict_spore
  name: Strict corpus validation covering spore cohort
  status: passed
  required: true
  summary: All 23 spore records pass strict LinkML and semantic validation.
  target_ids:
  - GO:0042764
  - GO:1905754
  - GO:0005619
  - GO:0005631
  - GO:0005630
  - GO:0043593
  - GO:0070477
  - GO:0043595
  - GO:0043591
  - GO:0042601
  - GO:0043592
  - GO:0005632
  - GO:1990916
  - GO:0090641
  - GO:0090642
  - GO:0043594
  - GO:0044099
  - GO:0160202
  - GO:0005628
  - GO:0070056
  - GO:0070057
  - GO:0140549
  - GO:0031160
  command: .venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_strict_spore
- check_id: labels_spore
  name: ID-label correspondence across spore cohort
  status: passed
  required: true
  summary: All ontology ID-label pairs in spore records correspond to canonical labels.
  target_ids:
  - GO:0042764
  - GO:1905754
  - GO:0005619
  - GO:0005631
  - GO:0005630
  - GO:0043593
  - GO:0070477
  - GO:0043595
  - GO:0043591
  - GO:0042601
  - GO:0043592
  - GO:0005632
  - GO:1990916
  - GO:0090641
  - GO:0090642
  - GO:0043594
  - GO:0044099
  - GO:0160202
  - GO:0005628
  - GO:0070056
  - GO:0070057
  - GO:0140549
  - GO:0031160
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_labels_spore
evidence:
- evidence_id: ev_strict_spore
  kind: validation
  reference: scripts/validate_strict.py
  locator: strict receipt
  accessed_at: '2026-10-25T07:10:13Z'
  support: supports
  summary: validate_strict.py exited 0 across all 993 records including all 23 spore
    records.
  snapshot_sha256: fc80872aed828ea24abbaf1ff66194605d09857b0bf0773189fc076d223594eb
- evidence_id: ev_labels_spore
  kind: validation
  reference: scripts/validate_id_label_correspondence.py
  locator: labels receipt
  accessed_at: '2026-10-25T07:10:13Z'
  support: supports
  summary: validate_id_label_correspondence.py exited 0 across all ontology targets.
  snapshot_sha256: 4bb207ccdd3216a741b1ca17643c1b57a2f2c68af02138decedfcd4fd19c8b3a
- evidence_id: ev_sp_ascospore_grounding
  kind: record_content
  reference: data/structures/spore/ascospore_wall.yaml
  locator: components#chitosan_outer_layer vs causal_graphs[0].nodes[3] (lines 220-223)
  accessed_at: '2026-10-25T07:05:40Z'
  support: supports
  summary: 'ascospore_wall.yaml components#chitosan_outer_layer declares grounding:
    CHEBI:16261 whereas causal_graphs[0].nodes[3] (chitosan_outer_layer) omits grounding.'
  quote: "  - node_id: chitosan_outer_layer\n    label: chitosan\n    node_type: CHEMICAL\n\
    \    component_ref: chitosan_outer_layer"
  snapshot_sha256: 97c1d9a7123cc5f0e5209c1e4bb6ba15d7ddebe89f5e001363c564938cfbacc7
assessments:
- assessment_id: assess_spore_cohort
  area: scope
  topic: Identity, boundaries, causal graphs, and ontology grounding across data/structures/spore/
  outcome: supported
  summary: All 23 records in data/structures/spore/ represent distinct microbial cell
    structures or subcomplexes with valid hierarchy links and verified UniProtKB protein
    examples.
  target_ids:
  - GO:0042764
  - GO:1905754
  - GO:0005619
  - GO:0005631
  - GO:0005630
  - GO:0043593
  - GO:0070477
  - GO:0043595
  - GO:0043591
  - GO:0042601
  - GO:0043592
  - GO:0005632
  - GO:1990916
  - GO:0090641
  - GO:0090642
  - GO:0043594
  - GO:0044099
  - GO:0160202
  - GO:0005628
  - GO:0070056
  - GO:0070057
  - GO:0140549
  - GO:0031160
  evidence_ids:
  - ev_strict_spore
  - ev_labels_spore
- assessment_id: assess_sp_ascospore_grounding
  area: graph
  topic: Causal-graph component_ref grounding propagation in ascospore_wall.yaml
  outcome: concern
  summary: causal_graphs[0].nodes[3] (chitosan_outer_layer) in ascospore_wall.yaml
    omits CHEBI:16261 from components#chitosan_outer_layer.
  target_ids:
  - GO:0005619
  evidence_ids:
  - ev_sp_ascospore_grounding
findings:
- finding_id: F1
  issue_key: spore-ascospore-wall-causal-node-component-ref-grounding
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: ascospore_wall.yaml causal_graphs[0].nodes[3] (chitosan_outer_layer) omits
    verified CHEBI:16261 grounding from components#chitosan_outer_layer
  description: 'In data/structures/spore/ascospore_wall.yaml (GO:0005619), components#chitosan_outer_layer
    declares grounding: CHEBI:16261 (chitosan), whereas causal_graphs[0].nodes[3]
    (node_id: chitosan_outer_layer, component_ref: chitosan_outer_layer) omits grounding.'
  target_ids:
  - GO:0005619
  field_paths:
  - causal_graphs[0].nodes[3].grounding
  evidence_ids:
  - ev_sp_ascospore_grounding
  rule_id: docs/SCHEMA.md:CausalNode-grounding
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/spore/ascospore_wall.yaml
    role: maintained_record
  tags:
  - causal-graphs
  - grounding
  - component-ref
  - stage4-record-review
actions:
- action_id: A1
  description: 'Propagate grounding: CHEBI:16261 (grounding_label: chitosan) to causal_graphs[0].nodes[3]
    (chitosan_outer_layer) in data/structures/spore/ascospore_wall.yaml and record
    the update in history/records/ascospore_wall/.'
  finding_ids:
  - F1
  target_ids:
  - GO:0005619
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/spore/ascospore_wall.yaml
    role: maintained_record
  acceptance_checks:
  - .venv/bin/python scripts/validate_strict.py data/structures/spore/ascospore_wall.yaml
    --out /tmp/ascospore_failures.tsv
  - .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
boundary_decisions:
- action: retain
  target_ids:
  - GO:0042764
  - GO:1905754
  - GO:0005619
  - GO:0005631
  - GO:0005630
  - GO:0043593
  - GO:0070477
  - GO:0043595
  - GO:0043591
  - GO:0042601
  - GO:0043592
  - GO:0005632
  - GO:1990916
  - GO:0090641
  - GO:0090642
  - GO:0043594
  - GO:0044099
  - GO:0160202
  - GO:0005628
  - GO:0070056
  - GO:0070057
  - GO:0140549
  - GO:0031160
  rationale: All 23 records in data/structures/spore/ represent distinct bacterial
    endospore, fungal ascospore/prospore, or microsporidian spore structures.
  evidence_ids:
  - ev_strict_spore
  - ev_labels_spore
limitations:
- Record edits for spore cohort findings are queued for Cycle 3 Stage 5 (resolve_review_findings).
tags:
- stage4
- category-review
- spore
```
