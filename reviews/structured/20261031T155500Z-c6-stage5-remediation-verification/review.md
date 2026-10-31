# Post-remediation verification review of all 12 CellStructureRecord files remediated in Cycle 6 Stage 5 (#2489, #2490)

- Review: 20261031T155500Z-c6-stage5-remediation-verification
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-31T15:53:00Z
- Finished UTC: 2026-10-31T15:55:00Z
- Reviewer: antigravity-c6-stage5-remediation-review (self_review)
- Completion: completed
- Verdict: pass
- Scientific review: true

## Summary

Fresh post-remediation review of all 12 CellStructureRecord YAML files modified in Cycle 6 Stage 5 (commit c0423878c9544a29b0db748b5f228b081d978f92) resolving all 10 open findings carried forward from Cycle 6 Stage 4 across issues #2489 (aligning top-level definition fields on 7 Cycle 6 Stage 1 protein-complex records [sid2_mob1_complex.yaml, potassium_ion_transporting_atpase_complex.yaml, atg12_atg5_atg16_complex.yaml, cobalamin_transport_complex.yaml, ekc_keops_complex.yaml, hsluv_protease_complex.yaml, and maltose_transport_complex.yaml] to their official GO IAO:0000115 definitions verified via OAK sqlite:obo:go and mirroring function/causal-graph edge PMID citations into top-level evidence) and #2490 (adding reciprocal has_part links on prostheca.yaml, basal_body_cartwheel.yaml, infraciliary_lattice.yaml, and reservosome.yaml; grounding components#reservosome_membrane to GO:0106126 on reservosome.yaml; and aligning reservosome_membrane.yaml to official GO:0106126 definition text, adding a life-stage note for presence: VARIABLE on Trypanosoma cruzi NCBITaxon:5693, and marking its 2-node parthood graph as graph_kind: FUNCTION and scope_status: NONMECHANISTIC). All 12 records pass strict validation, ID-label correspondence, CURIE liveness check, history ledger validation, text embedding map check, and page regeneration checks with zero open findings.

## Scope And Provenance

Complete cohort of all 12 CellStructureRecord YAML files remediated in Cycle 6 Stage 5 to resolve the 10 carried-forward Stage 4 findings.

Selection: All 12 records modified in commit c0423878c9544a29b0db748b5f228b081d978f92 for issues #2489 and #2490.
Coverage: full; 12 reviewed / 12 in the declared population.
Source: git_commit at Git base c0423878c9544a29b0db748b5f228b081d978f92.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:prostheca | data/structures/appendage/prostheca.yaml | maintained | prostheca |
| cellstructuremech:basal_body_cartwheel | data/structures/cytoskeleton/basal_body_cartwheel.yaml | maintained | basal body cartwheel |
| cellstructuremech:infraciliary_lattice | data/structures/cytoskeleton/infraciliary_lattice.yaml | maintained | infraciliary lattice |
| GO:0034973 | data/structures/division_machinery/sid2_mob1_complex.yaml | maintained | Sid2-Mob1 complex |
| GO:0031004 | data/structures/energy_complex/potassium_ion_transporting_atpase_complex.yaml | maintained | potassium ion-transporting ATPase complex |
| cellstructuremech:reservosome | data/structures/membrane_organelle/reservosome.yaml | maintained | reservosome |
| GO:0106126 | data/structures/membrane_organelle/reservosome_membrane.yaml | maintained | reservosome membrane |
| GO:0034274 | data/structures/other/atg12_atg5_atg16_complex.yaml | maintained | Atg12-Atg5-Atg16 complex |
| GO:1990191 | data/structures/other/cobalamin_transport_complex.yaml | maintained | cobalamin transport complex |
| GO:0000408 | data/structures/other/ekc_keops_complex.yaml | maintained | EKC/KEOPS complex |
| GO:0009376 | data/structures/other/hsluv_protease_complex.yaml | maintained | HslUV protease complex |
| GO:1990060 | data/structures/other/maltose_transport_complex.yaml | maintained | maltose transport complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation covering all 12 remediated records | passed | True | cellstructuremech:prostheca, cellstructuremech:basal_body_cartwheel, cellstructuremech:infraciliary_lattice, GO:0034973, GO:0031004, cellstructuremech:reservosome, GO:0106126, GO:0034274, GO:1990191, GO:0000408, GO:0009376, GO:1990060 | All 1015 corpus records including the 12 remediated records pass strict LinkML and semantic validation with 0 errors. |
| ID-label correspondence across corpus and generated products | passed | True | cellstructuremech:prostheca, cellstructuremech:basal_body_cartwheel, cellstructuremech:infraciliary_lattice, GO:0034973, GO:0031004, cellstructuremech:reservosome, GO:0106126, GO:0034274, GO:1990191, GO:0000408, GO:0009376, GO:1990060 | All ontology ID-label pairs across the corpus (4182 canonical, 50 synonym, 9 exception) correspond to authoritative ontology labels via OAK. |
| Strict CURIE liveness check across corpus | passed | True | cellstructuremech:prostheca, cellstructuremech:basal_body_cartwheel, cellstructuremech:infraciliary_lattice, GO:0034973, GO:0031004, cellstructuremech:reservosome, GO:0106126, GO:0034274, GO:1990191, GO:0000408, GO:0009376, GO:1990060 | All 6068 resolved CURIEs across the corpus pass liveness verification at their issuing authorities (254 skipped). |
| Repository history link and LinkML HistoryRecord validation | passed | True | cellstructuremech:prostheca, cellstructuremech:basal_body_cartwheel, cellstructuremech:infraciliary_lattice, GO:0034973, GO:0031004, cellstructuremech:reservosome, GO:0106126, GO:0034274, GO:1990191, GO:0000408, GO:0009376, GO:1990060 | All 2204 repository history files (including the 12 newly added Cycle 6 Stage 5 history ledger records) pass link and LinkML HistoryRecord schema validation. |
| Full CellStructureMech quality gate (lint, docs, source-queue, pathway-links, embeddings, pytest, history, strict, pages, report) | passed | True | cellstructuremech:prostheca, cellstructuremech:basal_body_cartwheel, cellstructuremech:infraciliary_lattice, GO:0034973, GO:0031004, cellstructuremech:reservosome, GO:0106126, GO:0034274, GO:1990191, GO:0000408, GO:0009376, GO:1990060 | scripts/run_qc.py passed all 10 gates including 1079 pytest tests, text embedding map check, and generated site check. |

## Scientific And Domain Assessments

### Official GO IAO:0000115 definition alignment and top-level PMID evidence completeness across 7 Cycle 6 Stage 1 protein-complex records (#2489)

evidence: supported. Targets: GO:0034973, GO:0031004, GO:0034274, GO:1990191, GO:0000408, GO:0009376, GO:1990060.

All 7 Cycle 6 Stage 1 protein-complex records in Group 1 (#2489) resolve their GO definition source-attribution and top-level evidence findings: sid2_mob1_complex.yaml (GO:0034973), potassium_ion_transporting_atpase_complex.yaml (GO:0031004), atg12_atg5_atg16_complex.yaml (GO:0034274), cobalamin_transport_complex.yaml (GO:1990191), ekc_keops_complex.yaml (GO:0000408), hsluv_protease_complex.yaml (GO:0009376), and maltose_transport_complex.yaml (GO:1990060) now carry the exact official GO IAO:0000115 definition strings verified via OAK sqlite:obo:go while preserving mechanistic summaries in causal_graphs[0].description; and sid2_mob1_complex.yaml (PMID:29813053, PMID:35011608), potassium_ion_transporting_atpase_complex.yaml (PMID:41384914), atg12_atg5_atg16_complex.yaml (PMID:41457424), and cobalamin_transport_complex.yaml (PMID:27457716, PMID:29084999) now mirror their function and causal-graph edge PMID citations and verbatim snippets in top-level evidence.

### Reciprocal has_part parthood links and reservosome / reservosome_membrane curation (#2490)

representation: supported. Targets: cellstructuremech:prostheca, cellstructuremech:basal_body_cartwheel, cellstructuremech:infraciliary_lattice, cellstructuremech:reservosome, GO:0106126.

All 5 records in Group 2 (#2490) resolve their parthood reciprocity, component grounding, definition, taxonomic note, and causal-graph metadata findings: prostheca.yaml adds cellstructuremech:stalk_crossband to has_part; basal_body_cartwheel.yaml adds has_part: [cellstructuremech:basal_body_cartwheel_inner_density, cellstructuremech:basal_body_d2_rod, cellstructuremech:basal_body_filamentous_cartwheel_inner_density]; infraciliary_lattice.yaml adds has_part: [cellstructuremech:cytostomal_cord]; reservosome.yaml grounds components#reservosome_membrane to GO:0106126 with GO:0106126 evidence and adds has_part: [GO:0106124, GO:0106125, GO:0106126]; and reservosome_membrane.yaml aligns definition to official GO:0106126 text ('The lipid bilayer surrounding a reservosome.'), adds an epimastigote vs amastigote/trypomastigote life-stage note on taxonomic_distribution[0] (NCBITaxon:5693, presence: VARIABLE), and marks its 2-node parthood graph reservosome_membrane_mechanism as graph_kind: FUNCTION and scope_status: NONMECHANISTIC.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: cellstructuremech:prostheca, cellstructuremech:basal_body_cartwheel, cellstructuremech:infraciliary_lattice, GO:0034973, GO:0031004, cellstructuremech:reservosome, GO:0106126, GO:0034274, GO:1990191, GO:0000408, GO:0009376, GO:1990060. All 12 remediated records preserve their existing structure boundaries and canonical GO/cellstructuremech identifiers while resolving all 10 Cycle 6 Stage 4 review findings.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev_strict_c6_stage5 | scripts/validate_strict.py; strict validation summary | supports | validate_strict.py scanned 1015 files with 0 ERROR rows. |
| ev_labels_c6_stage5 | scripts/validate_id_label_correspondence.py; id-label correspondence summary | supports | validate_id_label_correspondence.py verified 4182 canonical, 50 synonym, and 9 exception pairs with 0 mismatches. |
| ev_curies_c6_stage5 | scripts/check_curies.py; check_curies --check summary | supports | check_curies.py --check verified 6068 OK and 254 SKIPPED identifiers. |
| ev_history_c6_stage5 | scripts/validate_history.py; history link and schema validation | supports | 2204 history records validated with 0 invalid links and 0 HistoryRecord schema errors. |
| ev_qc_c6_stage5 | scripts/run_qc.py; run_qc summary | supports | All CellStructureMech quality gates passed (1015 records, 1079 passed tests). |

## Limits And Additional Notes


## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261031T155500Z-c6-stage5-remediation-verification
kind: category
repository: CultureBotAI/CellStructureMech
title: 'Post-remediation verification review of all 12 CellStructureRecord files remediated
  in Cycle 6 Stage 5 (#2489, #2490)'
started_at: '2026-10-31T15:53:00Z'
finished_at: '2026-10-31T15:55:00Z'
reviewer:
  identity: antigravity-c6-stage5-remediation-review
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: 'Post-remediation verification review against committed git
    revision c0423878c9544a29b0db748b5f228b081d978f92 covering all 12 records modified
    to resolve the 10 Cycle 6 Stage 4 review findings across GitHub issues #2489 and
    #2490.'
skill: .claude/skills/review-yaml-category/SKILL.md
completion: completed
verdict: pass
native_verdict: PASS
scientific_review: true
summary: 'Fresh post-remediation review of all 12 CellStructureRecord YAML files modified
  in Cycle 6 Stage 5 (commit c0423878c9544a29b0db748b5f228b081d978f92) resolving all
  10 open findings carried forward from Cycle 6 Stage 4 across issues #2489 (aligning
  top-level definition fields on 7 Cycle 6 Stage 1 protein-complex records [sid2_mob1_complex.yaml,
  potassium_ion_transporting_atpase_complex.yaml, atg12_atg5_atg16_complex.yaml, cobalamin_transport_complex.yaml,
  ekc_keops_complex.yaml, hsluv_protease_complex.yaml, and maltose_transport_complex.yaml]
  to their official GO IAO:0000115 definitions verified via OAK sqlite:obo:go and
  mirroring function/causal-graph edge PMID citations into top-level evidence) and
  #2490 (adding reciprocal has_part links on prostheca.yaml, basal_body_cartwheel.yaml,
  infraciliary_lattice.yaml, and reservosome.yaml; grounding components#reservosome_membrane
  to GO:0106126 on reservosome.yaml; and aligning reservosome_membrane.yaml to official
  GO:0106126 definition text, adding a life-stage note for presence: VARIABLE on Trypanosoma
  cruzi NCBITaxon:5693, and marking its 2-node parthood graph as graph_kind: FUNCTION
  and scope_status: NONMECHANISTIC). All 12 records pass strict validation, ID-label
  correspondence, CURIE liveness check, history ledger validation, text embedding
  map check, and page regeneration checks with zero open findings.'
source:
  git_revision: c0423878c9544a29b0db748b5f228b081d978f92
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
  - path: data/structures/appendage/prostheca.yaml
    sha256: ca294fdb8b89868f52e36f7ccd6cce9d9c6e31215be47a43d9610d797aa26bd8
    role: target
  - path: data/structures/cytoskeleton/basal_body_cartwheel.yaml
    sha256: 5b5a30ce3eef6e9113b4e308da82f2346d941f30930ad45c0d2e54b48c21f2cb
    role: target
  - path: data/structures/cytoskeleton/infraciliary_lattice.yaml
    sha256: d479a82edbd5420bb6fdfd3be27671537d19e4661694cc53af523d7090175058
    role: target
  - path: data/structures/division_machinery/sid2_mob1_complex.yaml
    sha256: d0248ff0e1d8a23193932050f980d2914ae03369cd5137fa448c9fe45d8e5fcd
    role: target
  - path: data/structures/energy_complex/potassium_ion_transporting_atpase_complex.yaml
    sha256: a163466245755fc7ce6ab43be29c935a8902ed7bcaa1849d734b542f633a8def
    role: target
  - path: data/structures/membrane_organelle/reservosome.yaml
    sha256: c15fb660484e37324ce3dca77fb7a9cf6c65c04bce70252d8bbb69d29ec99133
    role: target
  - path: data/structures/membrane_organelle/reservosome_membrane.yaml
    sha256: 224f7dcba21303a545d8bb7a009b661386a865c10b1b092efc7da3025e698a93
    role: target
  - path: data/structures/other/atg12_atg5_atg16_complex.yaml
    sha256: 3ba182028d65120424500dde4a0fb91ea7145e3c6c22243783a1156053f77357
    role: target
  - path: data/structures/other/cobalamin_transport_complex.yaml
    sha256: 07e97a1cedb5b9f2d917045de1c1a70d9e4c456a3f8bf26bc161b8fe405c04e5
    role: target
  - path: data/structures/other/ekc_keops_complex.yaml
    sha256: 05b319fdc13a0e7e3313f3819588380d680906df5e5cf82048d99a80026be08d
    role: target
  - path: data/structures/other/hsluv_protease_complex.yaml
    sha256: da7f008af805ac3ea632e49cc2d5da6b2bb30abf4b51e5e71be247ebab574361
    role: target
  - path: data/structures/other/maltose_transport_complex.yaml
    sha256: a9e3f890c572d93e8d5996fe05a4562201cacb9e5d541004491c398ce533e494
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
  description: Complete cohort of all 12 CellStructureRecord YAML files remediated
    in Cycle 6 Stage 5 to resolve the 10 carried-forward Stage 4 findings.
  selection: 'All 12 records modified in commit c0423878c9544a29b0db748b5f228b081d978f92
    for issues #2489 and #2490.'
  coverage: full
  population_size: 12
  reviewed_target_ids:
  - cellstructuremech:prostheca
  - cellstructuremech:basal_body_cartwheel
  - cellstructuremech:infraciliary_lattice
  - GO:0034973
  - GO:0031004
  - cellstructuremech:reservosome
  - GO:0106126
  - GO:0034274
  - GO:1990191
  - GO:0000408
  - GO:0009376
  - GO:1990060
targets:
- target_id: cellstructuremech:prostheca
  path: data/structures/appendage/prostheca.yaml
  label: prostheca
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: ca294fdb8b89868f52e36f7ccd6cce9d9c6e31215be47a43d9610d797aa26bd8
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/prostheca.yaml
    role: maintained_record
- target_id: cellstructuremech:basal_body_cartwheel
  path: data/structures/cytoskeleton/basal_body_cartwheel.yaml
  label: basal body cartwheel
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 5b5a30ce3eef6e9113b4e308da82f2346d941f30930ad45c0d2e54b48c21f2cb
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/basal_body_cartwheel.yaml
    role: maintained_record
- target_id: cellstructuremech:infraciliary_lattice
  path: data/structures/cytoskeleton/infraciliary_lattice.yaml
  label: infraciliary lattice
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: d479a82edbd5420bb6fdfd3be27671537d19e4661694cc53af523d7090175058
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/infraciliary_lattice.yaml
    role: maintained_record
- target_id: GO:0034973
  path: data/structures/division_machinery/sid2_mob1_complex.yaml
  label: Sid2-Mob1 complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: d0248ff0e1d8a23193932050f980d2914ae03369cd5137fa448c9fe45d8e5fcd
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/division_machinery/sid2_mob1_complex.yaml
    role: maintained_record
- target_id: GO:0031004
  path: data/structures/energy_complex/potassium_ion_transporting_atpase_complex.yaml
  label: potassium ion-transporting ATPase complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: a163466245755fc7ce6ab43be29c935a8902ed7bcaa1849d734b542f633a8def
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/potassium_ion_transporting_atpase_complex.yaml
    role: maintained_record
- target_id: cellstructuremech:reservosome
  path: data/structures/membrane_organelle/reservosome.yaml
  label: reservosome
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: c15fb660484e37324ce3dca77fb7a9cf6c65c04bce70252d8bbb69d29ec99133
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/reservosome.yaml
    role: maintained_record
- target_id: GO:0106126
  path: data/structures/membrane_organelle/reservosome_membrane.yaml
  label: reservosome membrane
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 224f7dcba21303a545d8bb7a009b661386a865c10b1b092efc7da3025e698a93
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/reservosome_membrane.yaml
    role: maintained_record
- target_id: GO:0034274
  path: data/structures/other/atg12_atg5_atg16_complex.yaml
  label: Atg12-Atg5-Atg16 complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 3ba182028d65120424500dde4a0fb91ea7145e3c6c22243783a1156053f77357
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/atg12_atg5_atg16_complex.yaml
    role: maintained_record
- target_id: GO:1990191
  path: data/structures/other/cobalamin_transport_complex.yaml
  label: cobalamin transport complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 07e97a1cedb5b9f2d917045de1c1a70d9e4c456a3f8bf26bc161b8fe405c04e5
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/cobalamin_transport_complex.yaml
    role: maintained_record
- target_id: GO:0000408
  path: data/structures/other/ekc_keops_complex.yaml
  label: EKC/KEOPS complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 05b319fdc13a0e7e3313f3819588380d680906df5e5cf82048d99a80026be08d
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ekc_keops_complex.yaml
    role: maintained_record
- target_id: GO:0009376
  path: data/structures/other/hsluv_protease_complex.yaml
  label: HslUV protease complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: da7f008af805ac3ea632e49cc2d5da6b2bb30abf4b51e5e71be247ebab574361
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/hsluv_protease_complex.yaml
    role: maintained_record
- target_id: GO:1990060
  path: data/structures/other/maltose_transport_complex.yaml
  label: maltose transport complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: a9e3f890c572d93e8d5996fe05a4562201cacb9e5d541004491c398ce533e494
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/maltose_transport_complex.yaml
    role: maintained_record
checks:
- check_id: strict_remediated_cohort
  name: Strict corpus validation covering all 12 remediated records
  status: passed
  required: true
  summary: All 1015 corpus records including the 12 remediated records pass strict
    LinkML and semantic validation with 0 errors.
  target_ids:
  - cellstructuremech:prostheca
  - cellstructuremech:basal_body_cartwheel
  - cellstructuremech:infraciliary_lattice
  - GO:0034973
  - GO:0031004
  - cellstructuremech:reservosome
  - GO:0106126
  - GO:0034274
  - GO:1990191
  - GO:0000408
  - GO:0009376
  - GO:1990060
  command: .venv/bin/python scripts/validate_strict.py --quiet
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_strict_c6_stage5
- check_id: labels_remediated_cohort
  name: ID-label correspondence across corpus and generated products
  status: passed
  required: true
  summary: All ontology ID-label pairs across the corpus (4182 canonical, 50 synonym,
    9 exception) correspond to authoritative ontology labels via OAK.
  target_ids:
  - cellstructuremech:prostheca
  - cellstructuremech:basal_body_cartwheel
  - cellstructuremech:infraciliary_lattice
  - GO:0034973
  - GO:0031004
  - cellstructuremech:reservosome
  - GO:0106126
  - GO:0034274
  - GO:1990191
  - GO:0000408
  - GO:0009376
  - GO:1990060
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_labels_c6_stage5
- check_id: curies_remediated_cohort
  name: Strict CURIE liveness check across corpus
  status: passed
  required: true
  summary: All 6068 resolved CURIEs across the corpus pass liveness verification at
    their issuing authorities (254 skipped).
  target_ids:
  - cellstructuremech:prostheca
  - cellstructuremech:basal_body_cartwheel
  - cellstructuremech:infraciliary_lattice
  - GO:0034973
  - GO:0031004
  - cellstructuremech:reservosome
  - GO:0106126
  - GO:0034274
  - GO:1990191
  - GO:0000408
  - GO:0009376
  - GO:1990060
  command: .venv/bin/python scripts/check_curies.py --check --report reports/curie_check.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_curies_c6_stage5
- check_id: history_remediated_cohort
  name: Repository history link and LinkML HistoryRecord validation
  status: passed
  required: true
  summary: All 2204 repository history files (including the 12 newly added Cycle 6
    Stage 5 history ledger records) pass link and LinkML HistoryRecord schema validation.
  target_ids:
  - cellstructuremech:prostheca
  - cellstructuremech:basal_body_cartwheel
  - cellstructuremech:infraciliary_lattice
  - GO:0034973
  - GO:0031004
  - cellstructuremech:reservosome
  - GO:0106126
  - GO:0034274
  - GO:1990191
  - GO:0000408
  - GO:0009376
  - GO:1990060
  command: .venv/bin/python scripts/validate_history.py history
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_history_c6_stage5
- check_id: qc_remediated_cohort
  name: Full CellStructureMech quality gate (lint, docs, source-queue, pathway-links,
    embeddings, pytest, history, strict, pages, report)
  status: passed
  required: true
  summary: scripts/run_qc.py passed all 10 gates including 1079 pytest tests, text
    embedding map check, and generated site check.
  target_ids:
  - cellstructuremech:prostheca
  - cellstructuremech:basal_body_cartwheel
  - cellstructuremech:infraciliary_lattice
  - GO:0034973
  - GO:0031004
  - cellstructuremech:reservosome
  - GO:0106126
  - GO:0034274
  - GO:1990191
  - GO:0000408
  - GO:0009376
  - GO:1990060
  command: .venv/bin/python scripts/run_qc.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_qc_c6_stage5
evidence:
- evidence_id: ev_strict_c6_stage5
  kind: validation
  reference: scripts/validate_strict.py
  locator: strict validation summary
  accessed_at: '2026-10-31T15:53:30Z'
  support: supports
  summary: validate_strict.py scanned 1015 files with 0 ERROR rows.
  snapshot_sha256: 9bd48d5966d4a124f5841e9a10619da7f14b7aa020a2f9b9c45cce26dadd699e
- evidence_id: ev_labels_c6_stage5
  kind: validation
  reference: scripts/validate_id_label_correspondence.py
  locator: id-label correspondence summary
  accessed_at: '2026-10-31T15:53:45Z'
  support: supports
  summary: validate_id_label_correspondence.py verified 4182 canonical, 50 synonym,
    and 9 exception pairs with 0 mismatches.
  snapshot_sha256: 07337cdad127562713b7ad614bc03b5050ebdcb2f862eacbfb9b663f5de3a0f5
- evidence_id: ev_curies_c6_stage5
  kind: validation
  reference: scripts/check_curies.py
  locator: check_curies --check summary
  accessed_at: '2026-10-31T15:54:00Z'
  support: supports
  summary: check_curies.py --check verified 6068 OK and 254 SKIPPED identifiers.
  snapshot_sha256: 92a451e8ef168171f4f29cfb7979eba3138dc47361abc397a27cbff95f0b96c8
- evidence_id: ev_history_c6_stage5
  kind: validation
  reference: scripts/validate_history.py
  locator: history link and schema validation
  accessed_at: '2026-10-31T15:54:15Z'
  support: supports
  summary: 2204 history records validated with 0 invalid links and 0 HistoryRecord
    schema errors.
  snapshot_sha256: c01634a73b9a644bcab76c1adbea2086d3c17e08856ee18801edfacc0f74f5d1
- evidence_id: ev_qc_c6_stage5
  kind: validation
  reference: scripts/run_qc.py
  locator: run_qc summary
  accessed_at: '2026-10-31T15:54:30Z'
  support: supports
  summary: All CellStructureMech quality gates passed (1015 records, 1079 passed tests).
  snapshot_sha256: 2b56119a66efb5f20a5fde1c8f8aec5b9e3247ce6681bf8643abe38d0d83f2b2
assessments:
- assessment_id: assess_group1_go_definitions_and_top_level_evidence
  area: evidence
  topic: Official GO IAO:0000115 definition alignment and top-level PMID evidence
    completeness across 7 Cycle 6 Stage 1 protein-complex records (#2489)
  outcome: supported
  summary: 'All 7 Cycle 6 Stage 1 protein-complex records in Group 1 (#2489) resolve
    their GO definition source-attribution and top-level evidence findings: sid2_mob1_complex.yaml
    (GO:0034973), potassium_ion_transporting_atpase_complex.yaml (GO:0031004), atg12_atg5_atg16_complex.yaml
    (GO:0034274), cobalamin_transport_complex.yaml (GO:1990191), ekc_keops_complex.yaml
    (GO:0000408), hsluv_protease_complex.yaml (GO:0009376), and maltose_transport_complex.yaml
    (GO:1990060) now carry the exact official GO IAO:0000115 definition strings verified
    via OAK sqlite:obo:go while preserving mechanistic summaries in causal_graphs[0].description;
    and sid2_mob1_complex.yaml (PMID:29813053, PMID:35011608), potassium_ion_transporting_atpase_complex.yaml
    (PMID:41384914), atg12_atg5_atg16_complex.yaml (PMID:41457424), and cobalamin_transport_complex.yaml
    (PMID:27457716, PMID:29084999) now mirror their function and causal-graph edge
    PMID citations and verbatim snippets in top-level evidence.'
  target_ids:
  - GO:0034973
  - GO:0031004
  - GO:0034274
  - GO:1990191
  - GO:0000408
  - GO:0009376
  - GO:1990060
  evidence_ids:
  - ev_strict_c6_stage5
  - ev_labels_c6_stage5
  - ev_curies_c6_stage5
  - ev_history_c6_stage5
  - ev_qc_c6_stage5
- assessment_id: assess_group2_reciprocal_has_part_and_reservosome_curation
  area: representation
  topic: Reciprocal has_part parthood links and reservosome / reservosome_membrane
    curation (#2490)
  outcome: supported
  summary: 'All 5 records in Group 2 (#2490) resolve their parthood reciprocity, component
    grounding, definition, taxonomic note, and causal-graph metadata findings: prostheca.yaml
    adds cellstructuremech:stalk_crossband to has_part; basal_body_cartwheel.yaml
    adds has_part: [cellstructuremech:basal_body_cartwheel_inner_density, cellstructuremech:basal_body_d2_rod,
    cellstructuremech:basal_body_filamentous_cartwheel_inner_density]; infraciliary_lattice.yaml
    adds has_part: [cellstructuremech:cytostomal_cord]; reservosome.yaml grounds components#reservosome_membrane
    to GO:0106126 with GO:0106126 evidence and adds has_part: [GO:0106124, GO:0106125,
    GO:0106126]; and reservosome_membrane.yaml aligns definition to official GO:0106126
    text (''The lipid bilayer surrounding a reservosome.''), adds an epimastigote
    vs amastigote/trypomastigote life-stage note on taxonomic_distribution[0] (NCBITaxon:5693,
    presence: VARIABLE), and marks its 2-node parthood graph reservosome_membrane_mechanism
    as graph_kind: FUNCTION and scope_status: NONMECHANISTIC.'
  target_ids:
  - cellstructuremech:prostheca
  - cellstructuremech:basal_body_cartwheel
  - cellstructuremech:infraciliary_lattice
  - cellstructuremech:reservosome
  - GO:0106126
  evidence_ids:
  - ev_strict_c6_stage5
  - ev_labels_c6_stage5
  - ev_curies_c6_stage5
  - ev_history_c6_stage5
  - ev_qc_c6_stage5
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - cellstructuremech:prostheca
  - cellstructuremech:basal_body_cartwheel
  - cellstructuremech:infraciliary_lattice
  - GO:0034973
  - GO:0031004
  - cellstructuremech:reservosome
  - GO:0106126
  - GO:0034274
  - GO:1990191
  - GO:0000408
  - GO:0009376
  - GO:1990060
  rationale: All 12 remediated records preserve their existing structure boundaries
    and canonical GO/cellstructuremech identifiers while resolving all 10 Cycle 6
    Stage 4 review findings.
  evidence_ids:
  - ev_strict_c6_stage5
  - ev_labels_c6_stage5
  - ev_curies_c6_stage5
  - ev_history_c6_stage5
  - ev_qc_c6_stage5
limitations: []
tags:
- stage5
- cycle6
- post-remediation
- verification-review
```
