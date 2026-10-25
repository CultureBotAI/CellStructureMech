# Category review of data/structures/inclusion/ (20 records): proteasome_storage_granule.yaml discussions DOI evidence link

- Review: 20261025T071008Z-inclusion-category-review
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-25T06:56:00Z
- Finished UTC: 2026-10-25T07:10:08Z
- Reviewer: antigravity-c3s4-record-review (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Full-coverage category review of all 20 records in data/structures/inclusion/ verified distinct microbial storage-granule and crystalline-inclusion boundaries. One minor discussion-evidence gap was identified in proteasome_storage_granule.yaml (GO:0034515): discussions[0] (discussion_id: retracted_evidence) mentions DOI 10.7554/eLife.34532 in discussions[0].notes without a corresponding structured EvidenceItem in discussions[0].evidence.

## Scope And Provenance

Full-cohort review of all 20 CellStructureRecord YAML files under data/structures/inclusion/.

Selection: Complete folder cohort data/structures/inclusion/*.yaml in the frozen 993-record Cycle 3 Stage 4 inventory.
Coverage: full; 20 reviewed / 20 in the declared population.
Source: git_commit at Git base 83ec9d5184fb203d87d8c3bd7043792d385193bf.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:age_associated_protein_deposit | data/structures/inclusion/age_associated_protein_deposit.yaml | maintained | age-associated protein deposit |
| cellstructuremech:bacterial_aggresome | data/structures/inclusion/bacterial_aggresome.yaml | maintained | bacterial aggresome |
| cellstructuremech:cyanophycin_granule | data/structures/inclusion/cyanophycin_granule.yaml | maintained | cyanophycin granule |
| GO:0031411 | data/structures/inclusion/gas_vesicle.yaml | maintained | gas vesicle |
| GO:0033172 | data/structures/inclusion/gas_vesicle_shell.yaml | maintained | gas vesicle shell |
| cellstructuremech:glycogen_granule | data/structures/inclusion/glycogen_granule.yaml | maintained | glycogen granule |
| cellstructuremech:insoluble_protein_deposit | data/structures/inclusion/insoluble_protein_deposit.yaml | maintained | insoluble protein deposit |
| cellstructuremech:intranuclear_quality_control_compartment | data/structures/inclusion/intranuclear_quality_control_compartment.yaml | maintained | intranuclear quality control compartment |
| cellstructuremech:juxtanuclear_quality_control_compartment | data/structures/inclusion/juxtanuclear_quality_control_compartment.yaml | maintained | juxtanuclear quality control compartment |
| GO:0005811 | data/structures/inclusion/lipid_droplet.yaml | maintained | lipid droplet |
| cellstructuremech:mitostore | data/structures/inclusion/mitostore.yaml | maintained | MitoStore |
| GO:0034430 | data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml | maintained | monolayer-surrounded lipid storage body outer lipid monolayer |
| GO:0140602 | data/structures/inclusion/nucleolar_peripheral_inclusion_body.yaml | maintained | nucleolar peripheral inclusion body |
| cellstructuremech:parasporal_crystal | data/structures/inclusion/parasporal_crystal.yaml | maintained | parasporal crystal |
| GO:0010287 | data/structures/inclusion/plastoglobule.yaml | maintained | plastoglobule |
| GO:0070088 | data/structures/inclusion/polyhydroxyalkanoate_granule.yaml | maintained | polyhydroxyalkanoate granule |
| GO:0034515 | data/structures/inclusion/proteasome_storage_granule.yaml | maintained | proteasome storage granule |
| GO:0140453 | data/structures/inclusion/protein_aggregate_center.yaml | maintained | protein aggregate center |
| cellstructuremech:r_body | data/structures/inclusion/r_body.yaml | maintained | R-body |
| cellstructuremech:sulfur_globule | data/structures/inclusion/sulfur_globule.yaml | maintained | sulfur globule |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation covering inclusion cohort | passed | True | cellstructuremech:age_associated_protein_deposit, cellstructuremech:bacterial_aggresome, cellstructuremech:cyanophycin_granule, GO:0031411, GO:0033172, cellstructuremech:glycogen_granule, cellstructuremech:insoluble_protein_deposit, cellstructuremech:intranuclear_quality_control_compartment, cellstructuremech:juxtanuclear_quality_control_compartment, GO:0005811, cellstructuremech:mitostore, GO:0034430, GO:0140602, cellstructuremech:parasporal_crystal, GO:0010287, GO:0070088, GO:0034515, GO:0140453, cellstructuremech:r_body, cellstructuremech:sulfur_globule | All 20 inclusion records pass strict LinkML and semantic validation. |
| ID-label correspondence across inclusion cohort | passed | True | cellstructuremech:age_associated_protein_deposit, cellstructuremech:bacterial_aggresome, cellstructuremech:cyanophycin_granule, GO:0031411, GO:0033172, cellstructuremech:glycogen_granule, cellstructuremech:insoluble_protein_deposit, cellstructuremech:intranuclear_quality_control_compartment, cellstructuremech:juxtanuclear_quality_control_compartment, GO:0005811, cellstructuremech:mitostore, GO:0034430, GO:0140602, cellstructuremech:parasporal_crystal, GO:0010287, GO:0070088, GO:0034515, GO:0140453, cellstructuremech:r_body, cellstructuremech:sulfur_globule | All ontology ID-label pairs in inclusion records correspond to canonical labels. |

## Scientific And Domain Assessments

### Identity, boundaries, causal graphs, and ontology grounding across data/structures/inclusion/

scope: supported. Targets: cellstructuremech:age_associated_protein_deposit, cellstructuremech:bacterial_aggresome, cellstructuremech:cyanophycin_granule, GO:0031411, GO:0033172, cellstructuremech:glycogen_granule, cellstructuremech:insoluble_protein_deposit, cellstructuremech:intranuclear_quality_control_compartment, cellstructuremech:juxtanuclear_quality_control_compartment, GO:0005811, cellstructuremech:mitostore, GO:0034430, GO:0140602, cellstructuremech:parasporal_crystal, GO:0010287, GO:0070088, GO:0034515, GO:0140453, cellstructuremech:r_body, cellstructuremech:sulfur_globule.

All 20 records in data/structures/inclusion/ represent distinct microbial cell structures or subcomplexes with valid hierarchy links and verified UniProtKB protein examples.

### Structured evidence backing for DOI citation in discussions[0] (retracted_evidence) of proteasome_storage_granule.yaml

evidence: concern. Targets: GO:0034515.

discussions[0].notes in proteasome_storage_granule.yaml mentions DOI 10.7554/eLife.34532 without a matching structured EvidenceItem in discussions[0].evidence.

## Findings

### F1: proteasome_storage_granule.yaml discussions[0].notes mentions DOI 10.7554/eLife.34532 without a structured discussions[0].evidence entry

minor / open / confirmed; issue key: inclusion-psg-discussions-unlinked-doi.

In data/structures/inclusion/proteasome_storage_granule.yaml (GO:0034515), discussions[0] (discussion_id: retracted_evidence, lines 249-265) mentions DOI 10.7554/eLife.34532 in discussions[0].notes while discussions[0].evidence only lists DOI:10.7554/eLife.82988 and PMID:30204036.

## Recommended Actions And Acceptance Checks

### A1

Add a structured EvidenceItem for DOI:10.7554/eLife.34532 (supports: REFUTE) to discussions[0].evidence in data/structures/inclusion/proteasome_storage_granule.yaml and record the update in history/records/proteasome_storage_granule/.

- .venv/bin/python scripts/validate_strict.py data/structures/inclusion/proteasome_storage_granule.yaml --out /tmp/psg_failures.tsv
- .venv/bin/python scripts/validate_history.py

## Category Boundaries

- retain: cellstructuremech:age_associated_protein_deposit, cellstructuremech:bacterial_aggresome, cellstructuremech:cyanophycin_granule, GO:0031411, GO:0033172, cellstructuremech:glycogen_granule, cellstructuremech:insoluble_protein_deposit, cellstructuremech:intranuclear_quality_control_compartment, cellstructuremech:juxtanuclear_quality_control_compartment, GO:0005811, cellstructuremech:mitostore, GO:0034430, GO:0140602, cellstructuremech:parasporal_crystal, GO:0010287, GO:0070088, GO:0034515, GO:0140453, cellstructuremech:r_body, cellstructuremech:sulfur_globule. All 20 records in data/structures/inclusion/ represent distinct microbial storage granules, bodies, or crystalline inclusions.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev_strict_inclusion | scripts/validate_strict.py; strict receipt | supports | validate_strict.py exited 0 across all 993 records including all 20 inclusion records. |
| ev_labels_inclusion | scripts/validate_id_label_correspondence.py; labels receipt | supports | validate_id_label_correspondence.py exited 0 across all ontology targets. |
| ev_inc_psg_discussion | data/structures/inclusion/proteasome_storage_granule.yaml; discussions[0] (lines 249-265) | supports | proteasome_storage_granule.yaml discussions[0] (retracted_evidence) mentions DOI 10.7554/eLife.34532 in discussions[0].notes while discussions[0].evidence only lists DOI:10.7554/eLife.82988 and PMID:30204036. |

## Limits And Additional Notes

- Record edits for inclusion cohort findings are queued for Cycle 3 Stage 5 (resolve_review_findings).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261025T071008Z-inclusion-category-review
kind: category
repository: CultureBotAI/CellStructureMech
title: 'Category review of data/structures/inclusion/ (20 records): proteasome_storage_granule.yaml
  discussions DOI evidence link'
started_at: '2026-10-25T06:56:00Z'
finished_at: '2026-10-25T07:10:08Z'
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
summary: 'Full-coverage category review of all 20 records in data/structures/inclusion/
  verified distinct microbial storage-granule and crystalline-inclusion boundaries.
  One minor discussion-evidence gap was identified in proteasome_storage_granule.yaml
  (GO:0034515): discussions[0] (discussion_id: retracted_evidence) mentions DOI 10.7554/eLife.34532
  in discussions[0].notes without a corresponding structured EvidenceItem in discussions[0].evidence.'
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
  - path: data/structures/inclusion/age_associated_protein_deposit.yaml
    sha256: f782fddfb8eb004a13ce40857c05527e29272b04da88e010cec04250ca867c30
    role: target
  - path: data/structures/inclusion/bacterial_aggresome.yaml
    sha256: 8f6d6cf20835c5114b8c13bc929767a750bbb7b0db778799d7d1e1be387f8636
    role: target
  - path: data/structures/inclusion/cyanophycin_granule.yaml
    sha256: 3838d566884d37b7a5bedd818de97e1880a15d469f5145d27a710defdf1a9260
    role: target
  - path: data/structures/inclusion/gas_vesicle.yaml
    sha256: 7bafef7a0ce0bc91ac7189ed216f4d2cdfc786cebbd47eeb5645c5408267f7cb
    role: target
  - path: data/structures/inclusion/gas_vesicle_shell.yaml
    sha256: 06f0f2aa709e62b9e46e2e38d2ce26692fc0d8e0fe16a78d998aa7a51b1e0ae6
    role: target
  - path: data/structures/inclusion/glycogen_granule.yaml
    sha256: 5474a36cc242751386b08cc597d8ec1f1649f10550d19005b7b75cfb9bf58894
    role: target
  - path: data/structures/inclusion/insoluble_protein_deposit.yaml
    sha256: 8bf3ffb3c2ce2ee5448d00f88d4d0de7911e3ee135e409e174a40f5c890e5f8a
    role: target
  - path: data/structures/inclusion/intranuclear_quality_control_compartment.yaml
    sha256: 7e6cc3b1915d2093b6712f349dea34cad79831f2d4b93f0eaff29351b37f3c36
    role: target
  - path: data/structures/inclusion/juxtanuclear_quality_control_compartment.yaml
    sha256: c3fbd426fe95ef931039579f467743997b83a889fa00c53442b36f46ccd95545
    role: target
  - path: data/structures/inclusion/lipid_droplet.yaml
    sha256: 379b5b516486c6bc55055e3289a565c7854b3088a5c13ebe6f614df5c1688a7a
    role: target
  - path: data/structures/inclusion/mitostore.yaml
    sha256: c932945c5ae1c4501b217b75333c4ae85551096cd4630bdae07f3ef84b0a7dd4
    role: target
  - path: data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml
    sha256: d72e9789b2d49d4fe380c06834e31dfe9eaf46fb6a412ddecdc9c8e1742b7a87
    role: target
  - path: data/structures/inclusion/nucleolar_peripheral_inclusion_body.yaml
    sha256: 0882138e885027304adbb077da65d773ad7a2197cd6cb5d7ab3688a49f9c35cc
    role: target
  - path: data/structures/inclusion/parasporal_crystal.yaml
    sha256: 59163a5ec708789816078e74a74e62fd9d3dbd38b580c40103a658e711274052
    role: target
  - path: data/structures/inclusion/plastoglobule.yaml
    sha256: ba5f8ac9dd4b54fefc917e1d6ed8587fdabdb2cf6152f1e331511bfc8ee38027
    role: target
  - path: data/structures/inclusion/polyhydroxyalkanoate_granule.yaml
    sha256: eea68c83cb758dcd5c7fe3a909af4628f405811f47941f2b4ab6b0faec7582d1
    role: target
  - path: data/structures/inclusion/proteasome_storage_granule.yaml
    sha256: 4e9730ed25a0a5a14b8c758073d590597c4f7c4638395e54897ec6fa1f12ff2e
    role: target
  - path: data/structures/inclusion/protein_aggregate_center.yaml
    sha256: c598bb2eae3dd31eb4ca363ddbea3b61ccdb85dd71ae8fc56385abd867ff4c9b
    role: target
  - path: data/structures/inclusion/r_body.yaml
    sha256: 1654ed4e95053883ebe6ca2f25f33b5a02b3dd778601afebd054698d0a86ba87
    role: target
  - path: data/structures/inclusion/sulfur_globule.yaml
    sha256: d4e16c6f94b832d3430d2aee0a0fa9cb0f6d75bf471768cb26c7e5b9f3100527
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
  description: Full-cohort review of all 20 CellStructureRecord YAML files under data/structures/inclusion/.
  selection: Complete folder cohort data/structures/inclusion/*.yaml in the frozen
    993-record Cycle 3 Stage 4 inventory.
  coverage: full
  population_size: 20
  reviewed_target_ids:
  - cellstructuremech:age_associated_protein_deposit
  - cellstructuremech:bacterial_aggresome
  - cellstructuremech:cyanophycin_granule
  - GO:0031411
  - GO:0033172
  - cellstructuremech:glycogen_granule
  - cellstructuremech:insoluble_protein_deposit
  - cellstructuremech:intranuclear_quality_control_compartment
  - cellstructuremech:juxtanuclear_quality_control_compartment
  - GO:0005811
  - cellstructuremech:mitostore
  - GO:0034430
  - GO:0140602
  - cellstructuremech:parasporal_crystal
  - GO:0010287
  - GO:0070088
  - GO:0034515
  - GO:0140453
  - cellstructuremech:r_body
  - cellstructuremech:sulfur_globule
targets:
- target_id: cellstructuremech:age_associated_protein_deposit
  path: data/structures/inclusion/age_associated_protein_deposit.yaml
  label: age-associated protein deposit
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: f782fddfb8eb004a13ce40857c05527e29272b04da88e010cec04250ca867c30
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/age_associated_protein_deposit.yaml
    role: maintained_record
- target_id: cellstructuremech:bacterial_aggresome
  path: data/structures/inclusion/bacterial_aggresome.yaml
  label: bacterial aggresome
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 8f6d6cf20835c5114b8c13bc929767a750bbb7b0db778799d7d1e1be387f8636
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/bacterial_aggresome.yaml
    role: maintained_record
- target_id: cellstructuremech:cyanophycin_granule
  path: data/structures/inclusion/cyanophycin_granule.yaml
  label: cyanophycin granule
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 3838d566884d37b7a5bedd818de97e1880a15d469f5145d27a710defdf1a9260
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/cyanophycin_granule.yaml
    role: maintained_record
- target_id: GO:0031411
  path: data/structures/inclusion/gas_vesicle.yaml
  label: gas vesicle
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 7bafef7a0ce0bc91ac7189ed216f4d2cdfc786cebbd47eeb5645c5408267f7cb
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/gas_vesicle.yaml
    role: maintained_record
- target_id: GO:0033172
  path: data/structures/inclusion/gas_vesicle_shell.yaml
  label: gas vesicle shell
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 06f0f2aa709e62b9e46e2e38d2ce26692fc0d8e0fe16a78d998aa7a51b1e0ae6
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/gas_vesicle_shell.yaml
    role: maintained_record
- target_id: cellstructuremech:glycogen_granule
  path: data/structures/inclusion/glycogen_granule.yaml
  label: glycogen granule
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 5474a36cc242751386b08cc597d8ec1f1649f10550d19005b7b75cfb9bf58894
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/glycogen_granule.yaml
    role: maintained_record
- target_id: cellstructuremech:insoluble_protein_deposit
  path: data/structures/inclusion/insoluble_protein_deposit.yaml
  label: insoluble protein deposit
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 8bf3ffb3c2ce2ee5448d00f88d4d0de7911e3ee135e409e174a40f5c890e5f8a
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/insoluble_protein_deposit.yaml
    role: maintained_record
- target_id: cellstructuremech:intranuclear_quality_control_compartment
  path: data/structures/inclusion/intranuclear_quality_control_compartment.yaml
  label: intranuclear quality control compartment
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 7e6cc3b1915d2093b6712f349dea34cad79831f2d4b93f0eaff29351b37f3c36
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/intranuclear_quality_control_compartment.yaml
    role: maintained_record
- target_id: cellstructuremech:juxtanuclear_quality_control_compartment
  path: data/structures/inclusion/juxtanuclear_quality_control_compartment.yaml
  label: juxtanuclear quality control compartment
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: c3fbd426fe95ef931039579f467743997b83a889fa00c53442b36f46ccd95545
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/juxtanuclear_quality_control_compartment.yaml
    role: maintained_record
- target_id: GO:0005811
  path: data/structures/inclusion/lipid_droplet.yaml
  label: lipid droplet
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 379b5b516486c6bc55055e3289a565c7854b3088a5c13ebe6f614df5c1688a7a
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/lipid_droplet.yaml
    role: maintained_record
- target_id: cellstructuremech:mitostore
  path: data/structures/inclusion/mitostore.yaml
  label: MitoStore
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: c932945c5ae1c4501b217b75333c4ae85551096cd4630bdae07f3ef84b0a7dd4
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/mitostore.yaml
    role: maintained_record
- target_id: GO:0034430
  path: data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml
  label: monolayer-surrounded lipid storage body outer lipid monolayer
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: d72e9789b2d49d4fe380c06834e31dfe9eaf46fb6a412ddecdc9c8e1742b7a87
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml
    role: maintained_record
- target_id: GO:0140602
  path: data/structures/inclusion/nucleolar_peripheral_inclusion_body.yaml
  label: nucleolar peripheral inclusion body
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 0882138e885027304adbb077da65d773ad7a2197cd6cb5d7ab3688a49f9c35cc
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/nucleolar_peripheral_inclusion_body.yaml
    role: maintained_record
- target_id: cellstructuremech:parasporal_crystal
  path: data/structures/inclusion/parasporal_crystal.yaml
  label: parasporal crystal
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 59163a5ec708789816078e74a74e62fd9d3dbd38b580c40103a658e711274052
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/parasporal_crystal.yaml
    role: maintained_record
- target_id: GO:0010287
  path: data/structures/inclusion/plastoglobule.yaml
  label: plastoglobule
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: ba5f8ac9dd4b54fefc917e1d6ed8587fdabdb2cf6152f1e331511bfc8ee38027
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/plastoglobule.yaml
    role: maintained_record
- target_id: GO:0070088
  path: data/structures/inclusion/polyhydroxyalkanoate_granule.yaml
  label: polyhydroxyalkanoate granule
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: eea68c83cb758dcd5c7fe3a909af4628f405811f47941f2b4ab6b0faec7582d1
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/polyhydroxyalkanoate_granule.yaml
    role: maintained_record
- target_id: GO:0034515
  path: data/structures/inclusion/proteasome_storage_granule.yaml
  label: proteasome storage granule
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 4e9730ed25a0a5a14b8c758073d590597c4f7c4638395e54897ec6fa1f12ff2e
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/proteasome_storage_granule.yaml
    role: maintained_record
- target_id: GO:0140453
  path: data/structures/inclusion/protein_aggregate_center.yaml
  label: protein aggregate center
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: c598bb2eae3dd31eb4ca363ddbea3b61ccdb85dd71ae8fc56385abd867ff4c9b
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/protein_aggregate_center.yaml
    role: maintained_record
- target_id: cellstructuremech:r_body
  path: data/structures/inclusion/r_body.yaml
  label: R-body
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 1654ed4e95053883ebe6ca2f25f33b5a02b3dd778601afebd054698d0a86ba87
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/r_body.yaml
    role: maintained_record
- target_id: cellstructuremech:sulfur_globule
  path: data/structures/inclusion/sulfur_globule.yaml
  label: sulfur globule
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: d4e16c6f94b832d3430d2aee0a0fa9cb0f6d75bf471768cb26c7e5b9f3100527
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/sulfur_globule.yaml
    role: maintained_record
checks:
- check_id: strict_inclusion
  name: Strict corpus validation covering inclusion cohort
  status: passed
  required: true
  summary: All 20 inclusion records pass strict LinkML and semantic validation.
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  - cellstructuremech:bacterial_aggresome
  - cellstructuremech:cyanophycin_granule
  - GO:0031411
  - GO:0033172
  - cellstructuremech:glycogen_granule
  - cellstructuremech:insoluble_protein_deposit
  - cellstructuremech:intranuclear_quality_control_compartment
  - cellstructuremech:juxtanuclear_quality_control_compartment
  - GO:0005811
  - cellstructuremech:mitostore
  - GO:0034430
  - GO:0140602
  - cellstructuremech:parasporal_crystal
  - GO:0010287
  - GO:0070088
  - GO:0034515
  - GO:0140453
  - cellstructuremech:r_body
  - cellstructuremech:sulfur_globule
  command: .venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_strict_inclusion
- check_id: labels_inclusion
  name: ID-label correspondence across inclusion cohort
  status: passed
  required: true
  summary: All ontology ID-label pairs in inclusion records correspond to canonical
    labels.
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  - cellstructuremech:bacterial_aggresome
  - cellstructuremech:cyanophycin_granule
  - GO:0031411
  - GO:0033172
  - cellstructuremech:glycogen_granule
  - cellstructuremech:insoluble_protein_deposit
  - cellstructuremech:intranuclear_quality_control_compartment
  - cellstructuremech:juxtanuclear_quality_control_compartment
  - GO:0005811
  - cellstructuremech:mitostore
  - GO:0034430
  - GO:0140602
  - cellstructuremech:parasporal_crystal
  - GO:0010287
  - GO:0070088
  - GO:0034515
  - GO:0140453
  - cellstructuremech:r_body
  - cellstructuremech:sulfur_globule
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_labels_inclusion
evidence:
- evidence_id: ev_strict_inclusion
  kind: validation
  reference: scripts/validate_strict.py
  locator: strict receipt
  accessed_at: '2026-10-25T07:10:08Z'
  support: supports
  summary: validate_strict.py exited 0 across all 993 records including all 20 inclusion
    records.
  snapshot_sha256: fc80872aed828ea24abbaf1ff66194605d09857b0bf0773189fc076d223594eb
- evidence_id: ev_labels_inclusion
  kind: validation
  reference: scripts/validate_id_label_correspondence.py
  locator: labels receipt
  accessed_at: '2026-10-25T07:10:08Z'
  support: supports
  summary: validate_id_label_correspondence.py exited 0 across all ontology targets.
  snapshot_sha256: 4bb207ccdd3216a741b1ca17643c1b57a2f2c68af02138decedfcd4fd19c8b3a
- evidence_id: ev_inc_psg_discussion
  kind: record_content
  reference: data/structures/inclusion/proteasome_storage_granule.yaml
  locator: discussions[0] (lines 249-265)
  accessed_at: '2026-10-25T07:03:20Z'
  support: supports
  summary: proteasome_storage_granule.yaml discussions[0] (retracted_evidence) mentions
    DOI 10.7554/eLife.34532 in discussions[0].notes while discussions[0].evidence
    only lists DOI:10.7554/eLife.82988 and PMID:30204036.
  quote: "- discussion_id: retracted_evidence\n  kind: INTERPRETATION\n  status: RESOLVED\n\
    \  prompt: Exclude the retracted 2018 study and derivative commentary from positive\n\
    \    support.\n  rationale: Ontology citation chains can retain secondary accounts\
    \ of withdrawn work.\n  notes: DOI 10.7554/eLife.34532 was retracted by DOI 10.7554/eLife.82988\
    \ following\n    reported western-blot irregularities and misplaced confocal images.\
    \ GO's definition\n    also cites PMID 30204036, a commentary on that study, which\
    \ is not independent\n    support. No proteaphagy-protection or Arabidopsis PSG\
    \ claim is imported from either.\n    Independent 2008 and 2017 primary evidence\
    \ supports this record's yeast scope.\n  evidence:\n  - reference: DOI:10.7554/eLife.82988\n\
    \    notes: Official retraction notice read; used only for exclusion provenance.\n\
    \  - reference: PMID:30204036\n    notes: Native PubMed identifies this as a comment\
    \ on the retracted study.\n  posed_by: codex"
  snapshot_sha256: 4e9730ed25a0a5a14b8c758073d590597c4f7c4638395e54897ec6fa1f12ff2e
assessments:
- assessment_id: assess_inclusion_cohort
  area: scope
  topic: Identity, boundaries, causal graphs, and ontology grounding across data/structures/inclusion/
  outcome: supported
  summary: All 20 records in data/structures/inclusion/ represent distinct microbial
    cell structures or subcomplexes with valid hierarchy links and verified UniProtKB
    protein examples.
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  - cellstructuremech:bacterial_aggresome
  - cellstructuremech:cyanophycin_granule
  - GO:0031411
  - GO:0033172
  - cellstructuremech:glycogen_granule
  - cellstructuremech:insoluble_protein_deposit
  - cellstructuremech:intranuclear_quality_control_compartment
  - cellstructuremech:juxtanuclear_quality_control_compartment
  - GO:0005811
  - cellstructuremech:mitostore
  - GO:0034430
  - GO:0140602
  - cellstructuremech:parasporal_crystal
  - GO:0010287
  - GO:0070088
  - GO:0034515
  - GO:0140453
  - cellstructuremech:r_body
  - cellstructuremech:sulfur_globule
  evidence_ids:
  - ev_strict_inclusion
  - ev_labels_inclusion
- assessment_id: assess_inc_psg_discussion
  area: evidence
  topic: Structured evidence backing for DOI citation in discussions[0] (retracted_evidence)
    of proteasome_storage_granule.yaml
  outcome: concern
  summary: discussions[0].notes in proteasome_storage_granule.yaml mentions DOI 10.7554/eLife.34532
    without a matching structured EvidenceItem in discussions[0].evidence.
  target_ids:
  - GO:0034515
  evidence_ids:
  - ev_inc_psg_discussion
findings:
- finding_id: F1
  issue_key: inclusion-psg-discussions-unlinked-doi
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: proteasome_storage_granule.yaml discussions[0].notes mentions DOI 10.7554/eLife.34532
    without a structured discussions[0].evidence entry
  description: 'In data/structures/inclusion/proteasome_storage_granule.yaml (GO:0034515),
    discussions[0] (discussion_id: retracted_evidence, lines 249-265) mentions DOI
    10.7554/eLife.34532 in discussions[0].notes while discussions[0].evidence only
    lists DOI:10.7554/eLife.82988 and PMID:30204036.'
  target_ids:
  - GO:0034515
  field_paths:
  - discussions[0].notes
  - discussions[0].evidence
  evidence_ids:
  - ev_inc_psg_discussion
  rule_id: docs/CURATION.md:discussion-evidence-links
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/proteasome_storage_granule.yaml
    role: maintained_record
  tags:
  - discussions
  - evidence
  - stage4-record-review
actions:
- action_id: A1
  description: 'Add a structured EvidenceItem for DOI:10.7554/eLife.34532 (supports:
    REFUTE) to discussions[0].evidence in data/structures/inclusion/proteasome_storage_granule.yaml
    and record the update in history/records/proteasome_storage_granule/.'
  finding_ids:
  - F1
  target_ids:
  - GO:0034515
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/proteasome_storage_granule.yaml
    role: maintained_record
  acceptance_checks:
  - .venv/bin/python scripts/validate_strict.py data/structures/inclusion/proteasome_storage_granule.yaml
    --out /tmp/psg_failures.tsv
  - .venv/bin/python scripts/validate_history.py
boundary_decisions:
- action: retain
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  - cellstructuremech:bacterial_aggresome
  - cellstructuremech:cyanophycin_granule
  - GO:0031411
  - GO:0033172
  - cellstructuremech:glycogen_granule
  - cellstructuremech:insoluble_protein_deposit
  - cellstructuremech:intranuclear_quality_control_compartment
  - cellstructuremech:juxtanuclear_quality_control_compartment
  - GO:0005811
  - cellstructuremech:mitostore
  - GO:0034430
  - GO:0140602
  - cellstructuremech:parasporal_crystal
  - GO:0010287
  - GO:0070088
  - GO:0034515
  - GO:0140453
  - cellstructuremech:r_body
  - cellstructuremech:sulfur_globule
  rationale: All 20 records in data/structures/inclusion/ represent distinct microbial
    storage granules, bodies, or crystalline inclusions.
  evidence_ids:
  - ev_strict_inclusion
  - ev_labels_inclusion
limitations:
- Record edits for inclusion cohort findings are queued for Cycle 3 Stage 5 (resolve_review_findings).
tags:
- stage4
- category-review
- inclusion
```
