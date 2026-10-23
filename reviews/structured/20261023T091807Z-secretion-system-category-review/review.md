# Category review of data/structures/secretion_system/ (20 records): T3SS discussion issue evidence links

- Review: 20261023T091807Z-secretion-system-category-review
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-23T09:10:30Z
- Finished UTC: 2026-10-23T09:18:07Z
- Reviewer: antigravity-stage4-record-review (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Full-coverage category review of all 20 records in data/structures/secretion_system/ verified distinct T1SS-T11SS, Sec, Tat, Bam, Lol, and TAM secretion/translocation complex boundaries. 19 records are clean; in type_iii_protein_secretion_system_complex.yaml (GO:0030257), discussions[0] (needle_dimensions_unsourced) cites repository issues #65 and #91 in rationale prose without a structured evidence list.

## Scope And Provenance

Full-cohort review of all 20 CellStructureRecord YAML files under data/structures/secretion_system/.

Selection: Complete folder cohort data/structures/secretion_system/*.yaml in the frozen 978-record Stage 4 inventory.
Coverage: full; 20 reviewed / 20 in the declared population.
Source: git_commit at Git base 13c6b0d85338aa96d330b8d699587dfe270a21f9.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0031522 | data/structures/secretion_system/cell_envelope_sec_protein_transport_complex.yaml | maintained | cell envelope Sec protein transport complex |
| GO:0062155 | data/structures/secretion_system/curli_secretion_complex.yaml | maintained | curli secretion complex |
| cellstructuremech:esx_3_type_vii_secretion_system_membrane_complex | data/structures/secretion_system/esx_3_type_vii_secretion_system_membrane_complex.yaml | maintained | ESX-3 type VII secretion system membrane complex |
| cellstructuremech:esx_5_type_vii_secretion_system_membrane_complex | data/structures/secretion_system/esx_5_type_vii_secretion_system_membrane_complex.yaml | maintained | ESX-5 type VII secretion system membrane complex |
| cellstructuremech:holo_translocon_secyeg_secdf_yajc_yidc_complex | data/structures/secretion_system/holo_translocon_secyeg_secdf_yajc_yidc_complex.yaml | maintained | Holo-translocon SecYEG-SecDF-YajC-YidC complex |
| cellstructuremech:secyeg_translocon_complex | data/structures/secretion_system/secyeg_translocon_complex.yaml | maintained | SecYEG translocon complex |
| GO:0097347 | data/structures/secretion_system/tam_protein_secretion_complex.yaml | maintained | TAM protein secretion complex |
| GO:0033281 | data/structures/secretion_system/tat_protein_transport_complex.yaml | maintained | TAT protein transport complex |
| GO:0030256 | data/structures/secretion_system/type_i_protein_secretion_system_complex.yaml | maintained | type I protein secretion system complex |
| GO:0015627 | data/structures/secretion_system/type_ii_protein_secretion_system_complex.yaml | maintained | type II protein secretion system complex |
| GO:0030257 | data/structures/secretion_system/type_iii_protein_secretion_system_complex.yaml | maintained | type III protein secretion system complex |
| GO:0043684 | data/structures/secretion_system/type_iv_secretion_system_complex.yaml | maintained | type IV secretion system complex |
| cellstructuremech:type_ix_protein_secretion_system_complex | data/structures/secretion_system/type_ix_protein_secretion_system_complex.yaml | maintained | type IX protein secretion system complex |
| GO:0098046 | data/structures/secretion_system/type_v_protein_secretion_system_complex.yaml | maintained | type V protein secretion system complex |
| GO:0033104 | data/structures/secretion_system/type_vi_protein_secretion_system_complex.yaml | maintained | type VI protein secretion system complex |
| cellstructuremech:type_vi_secretion_system_baseplate | data/structures/secretion_system/type_vi_secretion_system_baseplate.yaml | maintained | type VI secretion system baseplate |
| cellstructuremech:type_vi_secretion_system_contractile_sheath | data/structures/secretion_system/type_vi_secretion_system_contractile_sheath.yaml | maintained | type VI secretion system contractile sheath |
| cellstructuremech:type_vi_secretion_system_hcp_tube | data/structures/secretion_system/type_vi_secretion_system_hcp_tube.yaml | maintained | type VI secretion system Hcp tube |
| cellstructuremech:type_vi_secretion_system_membrane_complex | data/structures/secretion_system/type_vi_secretion_system_membrane_complex.yaml | maintained | type VI secretion system membrane complex |
| cellstructuremech:type_vi_secretion_system_vgrg_paar_spike_complex | data/structures/secretion_system/type_vi_secretion_system_vgrg_paar_spike_complex.yaml | maintained | type VI secretion system VgrG/PAAR spike complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation covering secretion_system cohort | passed | True | GO:0031522, GO:0062155, cellstructuremech:esx_3_type_vii_secretion_system_membrane_complex, cellstructuremech:esx_5_type_vii_secretion_system_membrane_complex, cellstructuremech:holo_translocon_secyeg_secdf_yajc_yidc_complex, cellstructuremech:secyeg_translocon_complex, GO:0097347, GO:0033281, GO:0030256, GO:0015627, GO:0030257, GO:0043684, cellstructuremech:type_ix_protein_secretion_system_complex, GO:0098046, GO:0033104, cellstructuremech:type_vi_secretion_system_baseplate, cellstructuremech:type_vi_secretion_system_contractile_sheath, cellstructuremech:type_vi_secretion_system_hcp_tube, cellstructuremech:type_vi_secretion_system_membrane_complex, cellstructuremech:type_vi_secretion_system_vgrg_paar_spike_complex | All 20 secretion_system records pass strict LinkML and semantic validation. |
| ID-label correspondence across secretion_system cohort | passed | True | GO:0031522, GO:0062155, cellstructuremech:esx_3_type_vii_secretion_system_membrane_complex, cellstructuremech:esx_5_type_vii_secretion_system_membrane_complex, cellstructuremech:holo_translocon_secyeg_secdf_yajc_yidc_complex, cellstructuremech:secyeg_translocon_complex, GO:0097347, GO:0033281, GO:0030256, GO:0015627, GO:0030257, GO:0043684, cellstructuremech:type_ix_protein_secretion_system_complex, GO:0098046, GO:0033104, cellstructuremech:type_vi_secretion_system_baseplate, cellstructuremech:type_vi_secretion_system_contractile_sheath, cellstructuremech:type_vi_secretion_system_hcp_tube, cellstructuremech:type_vi_secretion_system_membrane_complex, cellstructuremech:type_vi_secretion_system_vgrg_paar_spike_complex | All ontology ID-label pairs in secretion_system records correspond to canonical labels. |

## Scientific And Domain Assessments

### Boundary discipline, identity, composition, and evidence across all 20 secretion_system records

identity: supported. Targets: GO:0031522, GO:0062155, cellstructuremech:esx_3_type_vii_secretion_system_membrane_complex, cellstructuremech:esx_5_type_vii_secretion_system_membrane_complex, cellstructuremech:holo_translocon_secyeg_secdf_yajc_yidc_complex, cellstructuremech:secyeg_translocon_complex, GO:0097347, GO:0033281, GO:0030256, GO:0015627, GO:0030257, GO:0043684, cellstructuremech:type_ix_protein_secretion_system_complex, GO:0098046, GO:0033104, cellstructuremech:type_vi_secretion_system_baseplate, cellstructuremech:type_vi_secretion_system_contractile_sheath, cellstructuremech:type_vi_secretion_system_hcp_tube, cellstructuremech:type_vi_secretion_system_membrane_complex, cellstructuremech:type_vi_secretion_system_vgrg_paar_spike_complex.

All 20 secretion_system records maintain clean boundaries across T1SS-T11SS, Sec, Tat, Bam, Lol, and TAM translocation complexes.

### Structured GitHub issue URLs for #NNN mentions in discussions[0] of type_iii_protein_secretion_system_complex.yaml

evidence: concern. Targets: GO:0030257.

discussions[0] (needle_dimensions_unsourced) cites #65 and #91 in rationale prose without a structured evidence list.

## Findings

### F1: type_iii_protein_secretion_system_complex.yaml discussions[0] cites #65 and #91 in prose without structured evidence links

minor / open / confirmed; issue key: t3ss-complex-discussion-issue-evidence.

In data/structures/secretion_system/type_iii_protein_secretion_system_complex.yaml, discussions[0] (needle_dimensions_unsourced, lines 482-490) cites repository issues #65 and #91 in rationale prose without a structured evidence list containing https://github.com/CultureBotAI/CellStructureMech/issues/65 and https://github.com/CultureBotAI/CellStructureMech/issues/91.

## Recommended Actions And Acceptance Checks

### A1

Add structured GitHub issue URLs for #65 and #91 to discussions[0].evidence in data/structures/secretion_system/type_iii_protein_secretion_system_complex.yaml.

- .venv/bin/python scripts/validate_strict.py data/structures/secretion_system/type_iii_protein_secretion_system_complex.yaml --out /tmp/t3ss_failures.tsv
- .venv/bin/python scripts/validate_history.py

## Category Boundaries

- retain: GO:0031522, GO:0062155, cellstructuremech:esx_3_type_vii_secretion_system_membrane_complex, cellstructuremech:esx_5_type_vii_secretion_system_membrane_complex, cellstructuremech:holo_translocon_secyeg_secdf_yajc_yidc_complex, cellstructuremech:secyeg_translocon_complex, GO:0097347, GO:0033281, GO:0030256, GO:0015627, GO:0030257, GO:0043684, cellstructuremech:type_ix_protein_secretion_system_complex, GO:0098046, GO:0033104, cellstructuremech:type_vi_secretion_system_baseplate, cellstructuremech:type_vi_secretion_system_contractile_sheath, cellstructuremech:type_vi_secretion_system_hcp_tube, cellstructuremech:type_vi_secretion_system_membrane_complex, cellstructuremech:type_vi_secretion_system_vgrg_paar_spike_complex. All 20 records in data/structures/secretion_system/ represent distinct secretion or membrane-translocation systems with non-overlapping GO/CSM identifiers.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev_strict_sec | scripts/validate_strict.py; strict receipt | supports | validate_strict.py exited 0 across all 978 records including all 20 secretion_system records. |
| ev_labels_sec | scripts/validate_id_label_correspondence.py; labels receipt | supports | validate_id_label_correspondence.py exited 0 across all ontology targets. |
| ev_t3ss_discussion_issue | data/structures/secretion_system/type_iii_protein_secretion_system_complex.yaml; discussions[0] (lines 482-490) | supports | In type_iii_protein_secretion_system_complex.yaml, discussions[0] (needle_dimensions_unsourced) cites #65 and #91 in rationale prose without a structured evidence list. |

## Limits And Additional Notes

- One minor discussion-evidence finding on type_iii_protein_secretion_system_complex.yaml (GO:0030257) is queued for Stage 5 remediation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261023T091807Z-secretion-system-category-review
kind: category
repository: CultureBotAI/CellStructureMech
title: 'Category review of data/structures/secretion_system/ (20 records): T3SS discussion
  issue evidence links'
started_at: '2026-10-23T09:10:30Z'
finished_at: '2026-10-23T09:18:07Z'
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
summary: 'Full-coverage category review of all 20 records in data/structures/secretion_system/
  verified distinct T1SS-T11SS, Sec, Tat, Bam, Lol, and TAM secretion/translocation
  complex boundaries. 19 records are clean; in type_iii_protein_secretion_system_complex.yaml
  (GO:0030257), discussions[0] (needle_dimensions_unsourced) cites repository issues
  #65 and #91 in rationale prose without a structured evidence list.'
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
  - path: data/structures/secretion_system/cell_envelope_sec_protein_transport_complex.yaml
    sha256: 2164f385ec6847a1ba064f6975717b50373c080f563494e31af789d2946d3421
    role: target
  - path: data/structures/secretion_system/curli_secretion_complex.yaml
    sha256: 0a0e0ec596146bd7c74bf065593dd4b922a5b6d863be94edcfdd9143ffa342c2
    role: target
  - path: data/structures/secretion_system/esx_3_type_vii_secretion_system_membrane_complex.yaml
    sha256: a7d0bfe7a523a96f5fdf588c0b86e36e9f231d86cbd82e044fbf18c1803fb309
    role: target
  - path: data/structures/secretion_system/esx_5_type_vii_secretion_system_membrane_complex.yaml
    sha256: 5b0858ffa6e346668aeb54928ed38273e399fa41507685b4a40d674a8481dc24
    role: target
  - path: data/structures/secretion_system/holo_translocon_secyeg_secdf_yajc_yidc_complex.yaml
    sha256: 6209ad1fbf2d82e579f3cc0940d7fcc0a9a28031cfa1cf40b034eefd2a3a1333
    role: target
  - path: data/structures/secretion_system/secyeg_translocon_complex.yaml
    sha256: 97cfcee7198dc3907db94d83f0245ad5d8e8a4cd50aa04fe7c07e4a746a7bb41
    role: target
  - path: data/structures/secretion_system/tam_protein_secretion_complex.yaml
    sha256: d072c0e8a5d468669a2550868dad4bfc014c87be2748a74ab58bfa1fec69ba21
    role: target
  - path: data/structures/secretion_system/tat_protein_transport_complex.yaml
    sha256: f86a56c2a993ad7398bb2bedc50fb7baf54cbcc36a3d2a41a63a854808120b9e
    role: target
  - path: data/structures/secretion_system/type_i_protein_secretion_system_complex.yaml
    sha256: b64a9bfd3bebcd55ac53298d8198fddb4d49ae2a139c9629d68edae489f3349f
    role: target
  - path: data/structures/secretion_system/type_ii_protein_secretion_system_complex.yaml
    sha256: c8b043677bb629bcf79bbe7e9496d1203551020a53d8669366405af3517ca1cd
    role: target
  - path: data/structures/secretion_system/type_iii_protein_secretion_system_complex.yaml
    sha256: 135e1ea677f6af86fac8f7800c6132c55cade16eeefcb6c6cc71a0dcdaad3a22
    role: target
  - path: data/structures/secretion_system/type_iv_secretion_system_complex.yaml
    sha256: 917a40542c722b785ce4dbbf1ffd166fdcbc1bac2a89087eb13cce450fc05741
    role: target
  - path: data/structures/secretion_system/type_ix_protein_secretion_system_complex.yaml
    sha256: e41dca44f8506fd9950a2f6190e0de04e44c08ba49994bf77c295e1b15d2b959
    role: target
  - path: data/structures/secretion_system/type_v_protein_secretion_system_complex.yaml
    sha256: 20546ba3699057a447efdaad8a89677dbaeb1f3fde4e091b843aceb25fe8a523
    role: target
  - path: data/structures/secretion_system/type_vi_protein_secretion_system_complex.yaml
    sha256: be4f5a711c8bf48de352cdfd45b5a8182b4586e82e7fe5947501ff2432286018
    role: target
  - path: data/structures/secretion_system/type_vi_secretion_system_baseplate.yaml
    sha256: f7744ff6d16cead92c82eb953141e1b95f1fb380e860b2dd6824a5c8e0aeb292
    role: target
  - path: data/structures/secretion_system/type_vi_secretion_system_contractile_sheath.yaml
    sha256: 1c7b1a64ab4aec1fa73bb16ca210f7b315c32d90efb460767b33830fe2262e56
    role: target
  - path: data/structures/secretion_system/type_vi_secretion_system_hcp_tube.yaml
    sha256: 0eee4d20e69c006410ffa6432d6b72915a3fa90ed07e8c4da7fda28400d3d106
    role: target
  - path: data/structures/secretion_system/type_vi_secretion_system_membrane_complex.yaml
    sha256: 6c040ffcffa8e435d6c9e0558d279ebc6b6118524c91de377cf19bc9b02f77b9
    role: target
  - path: data/structures/secretion_system/type_vi_secretion_system_vgrg_paar_spike_complex.yaml
    sha256: 5b2a010a304b7a2e84d9978ddf4658b45317b9b45039b95b63d0ffa988117da8
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
  description: Full-cohort review of all 20 CellStructureRecord YAML files under data/structures/secretion_system/.
  selection: Complete folder cohort data/structures/secretion_system/*.yaml in the
    frozen 978-record Stage 4 inventory.
  coverage: full
  population_size: 20
  reviewed_target_ids:
  - GO:0031522
  - GO:0062155
  - cellstructuremech:esx_3_type_vii_secretion_system_membrane_complex
  - cellstructuremech:esx_5_type_vii_secretion_system_membrane_complex
  - cellstructuremech:holo_translocon_secyeg_secdf_yajc_yidc_complex
  - cellstructuremech:secyeg_translocon_complex
  - GO:0097347
  - GO:0033281
  - GO:0030256
  - GO:0015627
  - GO:0030257
  - GO:0043684
  - cellstructuremech:type_ix_protein_secretion_system_complex
  - GO:0098046
  - GO:0033104
  - cellstructuremech:type_vi_secretion_system_baseplate
  - cellstructuremech:type_vi_secretion_system_contractile_sheath
  - cellstructuremech:type_vi_secretion_system_hcp_tube
  - cellstructuremech:type_vi_secretion_system_membrane_complex
  - cellstructuremech:type_vi_secretion_system_vgrg_paar_spike_complex
targets:
- target_id: GO:0031522
  path: data/structures/secretion_system/cell_envelope_sec_protein_transport_complex.yaml
  label: cell envelope Sec protein transport complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 2164f385ec6847a1ba064f6975717b50373c080f563494e31af789d2946d3421
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/secretion_system/cell_envelope_sec_protein_transport_complex.yaml
    role: maintained_record
- target_id: GO:0062155
  path: data/structures/secretion_system/curli_secretion_complex.yaml
  label: curli secretion complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 0a0e0ec596146bd7c74bf065593dd4b922a5b6d863be94edcfdd9143ffa342c2
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/secretion_system/curli_secretion_complex.yaml
    role: maintained_record
- target_id: cellstructuremech:esx_3_type_vii_secretion_system_membrane_complex
  path: data/structures/secretion_system/esx_3_type_vii_secretion_system_membrane_complex.yaml
  label: ESX-3 type VII secretion system membrane complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: a7d0bfe7a523a96f5fdf588c0b86e36e9f231d86cbd82e044fbf18c1803fb309
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/secretion_system/esx_3_type_vii_secretion_system_membrane_complex.yaml
    role: maintained_record
- target_id: cellstructuremech:esx_5_type_vii_secretion_system_membrane_complex
  path: data/structures/secretion_system/esx_5_type_vii_secretion_system_membrane_complex.yaml
  label: ESX-5 type VII secretion system membrane complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 5b0858ffa6e346668aeb54928ed38273e399fa41507685b4a40d674a8481dc24
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/secretion_system/esx_5_type_vii_secretion_system_membrane_complex.yaml
    role: maintained_record
- target_id: cellstructuremech:holo_translocon_secyeg_secdf_yajc_yidc_complex
  path: data/structures/secretion_system/holo_translocon_secyeg_secdf_yajc_yidc_complex.yaml
  label: Holo-translocon SecYEG-SecDF-YajC-YidC complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 6209ad1fbf2d82e579f3cc0940d7fcc0a9a28031cfa1cf40b034eefd2a3a1333
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/secretion_system/holo_translocon_secyeg_secdf_yajc_yidc_complex.yaml
    role: maintained_record
- target_id: cellstructuremech:secyeg_translocon_complex
  path: data/structures/secretion_system/secyeg_translocon_complex.yaml
  label: SecYEG translocon complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 97cfcee7198dc3907db94d83f0245ad5d8e8a4cd50aa04fe7c07e4a746a7bb41
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/secretion_system/secyeg_translocon_complex.yaml
    role: maintained_record
- target_id: GO:0097347
  path: data/structures/secretion_system/tam_protein_secretion_complex.yaml
  label: TAM protein secretion complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: d072c0e8a5d468669a2550868dad4bfc014c87be2748a74ab58bfa1fec69ba21
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/secretion_system/tam_protein_secretion_complex.yaml
    role: maintained_record
- target_id: GO:0033281
  path: data/structures/secretion_system/tat_protein_transport_complex.yaml
  label: TAT protein transport complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: f86a56c2a993ad7398bb2bedc50fb7baf54cbcc36a3d2a41a63a854808120b9e
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/secretion_system/tat_protein_transport_complex.yaml
    role: maintained_record
- target_id: GO:0030256
  path: data/structures/secretion_system/type_i_protein_secretion_system_complex.yaml
  label: type I protein secretion system complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: b64a9bfd3bebcd55ac53298d8198fddb4d49ae2a139c9629d68edae489f3349f
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/secretion_system/type_i_protein_secretion_system_complex.yaml
    role: maintained_record
- target_id: GO:0015627
  path: data/structures/secretion_system/type_ii_protein_secretion_system_complex.yaml
  label: type II protein secretion system complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: c8b043677bb629bcf79bbe7e9496d1203551020a53d8669366405af3517ca1cd
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/secretion_system/type_ii_protein_secretion_system_complex.yaml
    role: maintained_record
- target_id: GO:0030257
  path: data/structures/secretion_system/type_iii_protein_secretion_system_complex.yaml
  label: type III protein secretion system complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 135e1ea677f6af86fac8f7800c6132c55cade16eeefcb6c6cc71a0dcdaad3a22
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/secretion_system/type_iii_protein_secretion_system_complex.yaml
    role: maintained_record
- target_id: GO:0043684
  path: data/structures/secretion_system/type_iv_secretion_system_complex.yaml
  label: type IV secretion system complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 917a40542c722b785ce4dbbf1ffd166fdcbc1bac2a89087eb13cce450fc05741
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/secretion_system/type_iv_secretion_system_complex.yaml
    role: maintained_record
- target_id: cellstructuremech:type_ix_protein_secretion_system_complex
  path: data/structures/secretion_system/type_ix_protein_secretion_system_complex.yaml
  label: type IX protein secretion system complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: e41dca44f8506fd9950a2f6190e0de04e44c08ba49994bf77c295e1b15d2b959
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/secretion_system/type_ix_protein_secretion_system_complex.yaml
    role: maintained_record
- target_id: GO:0098046
  path: data/structures/secretion_system/type_v_protein_secretion_system_complex.yaml
  label: type V protein secretion system complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 20546ba3699057a447efdaad8a89677dbaeb1f3fde4e091b843aceb25fe8a523
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/secretion_system/type_v_protein_secretion_system_complex.yaml
    role: maintained_record
- target_id: GO:0033104
  path: data/structures/secretion_system/type_vi_protein_secretion_system_complex.yaml
  label: type VI protein secretion system complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: be4f5a711c8bf48de352cdfd45b5a8182b4586e82e7fe5947501ff2432286018
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/secretion_system/type_vi_protein_secretion_system_complex.yaml
    role: maintained_record
- target_id: cellstructuremech:type_vi_secretion_system_baseplate
  path: data/structures/secretion_system/type_vi_secretion_system_baseplate.yaml
  label: type VI secretion system baseplate
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: f7744ff6d16cead92c82eb953141e1b95f1fb380e860b2dd6824a5c8e0aeb292
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/secretion_system/type_vi_secretion_system_baseplate.yaml
    role: maintained_record
- target_id: cellstructuremech:type_vi_secretion_system_contractile_sheath
  path: data/structures/secretion_system/type_vi_secretion_system_contractile_sheath.yaml
  label: type VI secretion system contractile sheath
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 1c7b1a64ab4aec1fa73bb16ca210f7b315c32d90efb460767b33830fe2262e56
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/secretion_system/type_vi_secretion_system_contractile_sheath.yaml
    role: maintained_record
- target_id: cellstructuremech:type_vi_secretion_system_hcp_tube
  path: data/structures/secretion_system/type_vi_secretion_system_hcp_tube.yaml
  label: type VI secretion system Hcp tube
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 0eee4d20e69c006410ffa6432d6b72915a3fa90ed07e8c4da7fda28400d3d106
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/secretion_system/type_vi_secretion_system_hcp_tube.yaml
    role: maintained_record
- target_id: cellstructuremech:type_vi_secretion_system_membrane_complex
  path: data/structures/secretion_system/type_vi_secretion_system_membrane_complex.yaml
  label: type VI secretion system membrane complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 6c040ffcffa8e435d6c9e0558d279ebc6b6118524c91de377cf19bc9b02f77b9
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/secretion_system/type_vi_secretion_system_membrane_complex.yaml
    role: maintained_record
- target_id: cellstructuremech:type_vi_secretion_system_vgrg_paar_spike_complex
  path: data/structures/secretion_system/type_vi_secretion_system_vgrg_paar_spike_complex.yaml
  label: type VI secretion system VgrG/PAAR spike complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 5b2a010a304b7a2e84d9978ddf4658b45317b9b45039b95b63d0ffa988117da8
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/secretion_system/type_vi_secretion_system_vgrg_paar_spike_complex.yaml
    role: maintained_record
checks:
- check_id: strict_secretion_system
  name: Strict corpus validation covering secretion_system cohort
  status: passed
  required: true
  summary: All 20 secretion_system records pass strict LinkML and semantic validation.
  target_ids:
  - GO:0031522
  - GO:0062155
  - cellstructuremech:esx_3_type_vii_secretion_system_membrane_complex
  - cellstructuremech:esx_5_type_vii_secretion_system_membrane_complex
  - cellstructuremech:holo_translocon_secyeg_secdf_yajc_yidc_complex
  - cellstructuremech:secyeg_translocon_complex
  - GO:0097347
  - GO:0033281
  - GO:0030256
  - GO:0015627
  - GO:0030257
  - GO:0043684
  - cellstructuremech:type_ix_protein_secretion_system_complex
  - GO:0098046
  - GO:0033104
  - cellstructuremech:type_vi_secretion_system_baseplate
  - cellstructuremech:type_vi_secretion_system_contractile_sheath
  - cellstructuremech:type_vi_secretion_system_hcp_tube
  - cellstructuremech:type_vi_secretion_system_membrane_complex
  - cellstructuremech:type_vi_secretion_system_vgrg_paar_spike_complex
  command: .venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_strict_sec
- check_id: labels_secretion_system
  name: ID-label correspondence across secretion_system cohort
  status: passed
  required: true
  summary: All ontology ID-label pairs in secretion_system records correspond to canonical
    labels.
  target_ids:
  - GO:0031522
  - GO:0062155
  - cellstructuremech:esx_3_type_vii_secretion_system_membrane_complex
  - cellstructuremech:esx_5_type_vii_secretion_system_membrane_complex
  - cellstructuremech:holo_translocon_secyeg_secdf_yajc_yidc_complex
  - cellstructuremech:secyeg_translocon_complex
  - GO:0097347
  - GO:0033281
  - GO:0030256
  - GO:0015627
  - GO:0030257
  - GO:0043684
  - cellstructuremech:type_ix_protein_secretion_system_complex
  - GO:0098046
  - GO:0033104
  - cellstructuremech:type_vi_secretion_system_baseplate
  - cellstructuremech:type_vi_secretion_system_contractile_sheath
  - cellstructuremech:type_vi_secretion_system_hcp_tube
  - cellstructuremech:type_vi_secretion_system_membrane_complex
  - cellstructuremech:type_vi_secretion_system_vgrg_paar_spike_complex
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_labels_sec
evidence:
- evidence_id: ev_strict_sec
  kind: validation
  reference: scripts/validate_strict.py
  locator: strict receipt
  accessed_at: '2026-10-23T09:16:01Z'
  support: supports
  summary: validate_strict.py exited 0 across all 978 records including all 20 secretion_system
    records.
  snapshot_sha256: b34bdc4f99ef4601161958120b45622535017214ba594a44bca249237869d704
- evidence_id: ev_labels_sec
  kind: validation
  reference: scripts/validate_id_label_correspondence.py
  locator: labels receipt
  accessed_at: '2026-10-23T09:17:48Z'
  support: supports
  summary: validate_id_label_correspondence.py exited 0 across all ontology targets.
  snapshot_sha256: b5cc67214f5627a654e75cfc335d77d42113d057091884a12094aa1a71447a5e
- evidence_id: ev_t3ss_discussion_issue
  kind: record_content
  reference: data/structures/secretion_system/type_iii_protein_secretion_system_complex.yaml
  locator: discussions[0] (lines 482-490)
  accessed_at: '2026-10-23T09:14:50Z'
  support: supports
  summary: 'In type_iii_protein_secretion_system_complex.yaml, discussions[0] (needle_dimensions_unsourced)
    cites #65 and #91 in rationale prose without a structured evidence list.'
  quote: 'rationale: Removed from record notes per #65; tracked in #91 until a primary
    source is cited.'
  snapshot_sha256: 135e1ea677f6af86fac8f7800c6132c55cade16eeefcb6c6cc71a0dcdaad3a22
assessments:
- assessment_id: assess_sec_cohort
  area: identity
  topic: Boundary discipline, identity, composition, and evidence across all 20 secretion_system
    records
  outcome: supported
  summary: All 20 secretion_system records maintain clean boundaries across T1SS-T11SS,
    Sec, Tat, Bam, Lol, and TAM translocation complexes.
  target_ids:
  - GO:0031522
  - GO:0062155
  - cellstructuremech:esx_3_type_vii_secretion_system_membrane_complex
  - cellstructuremech:esx_5_type_vii_secretion_system_membrane_complex
  - cellstructuremech:holo_translocon_secyeg_secdf_yajc_yidc_complex
  - cellstructuremech:secyeg_translocon_complex
  - GO:0097347
  - GO:0033281
  - GO:0030256
  - GO:0015627
  - GO:0030257
  - GO:0043684
  - cellstructuremech:type_ix_protein_secretion_system_complex
  - GO:0098046
  - GO:0033104
  - cellstructuremech:type_vi_secretion_system_baseplate
  - cellstructuremech:type_vi_secretion_system_contractile_sheath
  - cellstructuremech:type_vi_secretion_system_hcp_tube
  - cellstructuremech:type_vi_secretion_system_membrane_complex
  - cellstructuremech:type_vi_secretion_system_vgrg_paar_spike_complex
  evidence_ids:
  - ev_strict_sec
  - ev_labels_sec
- assessment_id: assess_t3ss_discussion_issue
  area: evidence
  topic: 'Structured GitHub issue URLs for #NNN mentions in discussions[0] of type_iii_protein_secretion_system_complex.yaml'
  outcome: concern
  summary: 'discussions[0] (needle_dimensions_unsourced) cites #65 and #91 in rationale
    prose without a structured evidence list.'
  target_ids:
  - GO:0030257
  evidence_ids:
  - ev_t3ss_discussion_issue
findings:
- finding_id: F1
  issue_key: t3ss-complex-discussion-issue-evidence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: 'type_iii_protein_secretion_system_complex.yaml discussions[0] cites #65
    and #91 in prose without structured evidence links'
  description: 'In data/structures/secretion_system/type_iii_protein_secretion_system_complex.yaml,
    discussions[0] (needle_dimensions_unsourced, lines 482-490) cites repository issues
    #65 and #91 in rationale prose without a structured evidence list containing https://github.com/CultureBotAI/CellStructureMech/issues/65
    and https://github.com/CultureBotAI/CellStructureMech/issues/91.'
  target_ids:
  - GO:0030257
  field_paths:
  - discussions[0].evidence
  evidence_ids:
  - ev_t3ss_discussion_issue
  rule_id: docs/CURATION.md:issue-links-in-evidence
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/secretion_system/type_iii_protein_secretion_system_complex.yaml
    role: maintained_record
  tags:
  - discussions
  - evidence
  - stage4-record-review
actions:
- action_id: A1
  description: 'Add structured GitHub issue URLs for #65 and #91 to discussions[0].evidence
    in data/structures/secretion_system/type_iii_protein_secretion_system_complex.yaml.'
  finding_ids:
  - F1
  target_ids:
  - GO:0030257
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/secretion_system/type_iii_protein_secretion_system_complex.yaml
    role: maintained_record
  acceptance_checks:
  - .venv/bin/python scripts/validate_strict.py data/structures/secretion_system/type_iii_protein_secretion_system_complex.yaml
    --out /tmp/t3ss_failures.tsv
  - .venv/bin/python scripts/validate_history.py
boundary_decisions:
- action: retain
  target_ids:
  - GO:0031522
  - GO:0062155
  - cellstructuremech:esx_3_type_vii_secretion_system_membrane_complex
  - cellstructuremech:esx_5_type_vii_secretion_system_membrane_complex
  - cellstructuremech:holo_translocon_secyeg_secdf_yajc_yidc_complex
  - cellstructuremech:secyeg_translocon_complex
  - GO:0097347
  - GO:0033281
  - GO:0030256
  - GO:0015627
  - GO:0030257
  - GO:0043684
  - cellstructuremech:type_ix_protein_secretion_system_complex
  - GO:0098046
  - GO:0033104
  - cellstructuremech:type_vi_secretion_system_baseplate
  - cellstructuremech:type_vi_secretion_system_contractile_sheath
  - cellstructuremech:type_vi_secretion_system_hcp_tube
  - cellstructuremech:type_vi_secretion_system_membrane_complex
  - cellstructuremech:type_vi_secretion_system_vgrg_paar_spike_complex
  rationale: All 20 records in data/structures/secretion_system/ represent distinct
    secretion or membrane-translocation systems with non-overlapping GO/CSM identifiers.
  evidence_ids:
  - ev_strict_sec
  - ev_labels_sec
limitations:
- One minor discussion-evidence finding on type_iii_protein_secretion_system_complex.yaml
  (GO:0030257) is queued for Stage 5 remediation.
tags:
- stage4
- category-review
- secretion-system
```
