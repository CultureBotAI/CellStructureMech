# Single-record review of potassium ion-transporting ATPase complex (GO:0031004): definition_source attribution and top-level PMID:41384914 evidence

- Review: 20261031T123502Z-potassium-ion-transporting-atpase-complex-review
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-31T12:30:30Z
- Finished UTC: 2026-10-31T12:35:02Z
- Reviewer: antigravity-c6s4-record-review (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Single-record audit of potassium_ion_transporting_atpase_complex.yaml (GO:0031004, potassium ion-transporting ATPase complex). Subunit composition (KdpF, KdpA, KdpB, KdpC with E. coli K-12 UniProtKB entries P36937, P03959, P03960, P03961) and causal graph are well-supported. Two minor curation issues were identified: (1) definition is a custom structural sentence while definition_source is set to GO:0031004 instead of quoting the official GO:0031004 definition verbatim; and (2) top-level evidence omits PMID:41384914, which is cited in taxonomic_distribution[0].reference, functions[1].evidence[1].reference, and causal_graphs[0].edges[5].evidence[0].reference.

## Scope And Provenance

Single-record review of data/structures/energy_complex/potassium_ion_transporting_atpase_complex.yaml (GO:0031004).

Selection: Targeted single-record audit of newly added Cycle 6 Stage 1 record potassium_ion_transporting_atpase_complex.yaml during Cycle 6 Stage 4 full-corpus inspection.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 9634411be0aeec8d8f4b9cb9158e3165db87c150.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0031004 | data/structures/energy_complex/potassium_ion_transporting_atpase_complex.yaml | maintained | potassium ion-transporting ATPase complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation covering potassium_ion_transporting_atpase_complex.yaml | passed | True | GO:0031004 | potassium_ion_transporting_atpase_complex.yaml passes current strict LinkML validation. |
| History ledger validation covering potassium_ion_transporting_atpase_complex.yaml | passed | True | GO:0031004 | History ledger records covering potassium_ion_transporting_atpase_complex.yaml validate cleanly. |

## Scientific And Domain Assessments

### GO cellular_component identity and KdpFABC subunit composition of GO:0031004

identity: supported. Targets: GO:0031004.

GO:0031004 accurately identifies the prokaryotic KdpFABC complex with verified E. coli K-12 UniProtKB protein_examples.

### Official GO:0031004 definition attribution and top-level PMID:41384914 evidence parity

evidence: concern. Targets: GO:0031004.

definition uses custom prose while setting definition_source: GO:0031004, and top-level evidence omits PMID:41384914 cited in three sub-sections.

## Findings

### F1: potassium_ion_transporting_atpase_complex.yaml attributes a custom definition to definition_source: GO:0031004

minor / open / confirmed; issue key: potassium-atpase-complex-definition-source-attribution.

In data/structures/energy_complex/potassium_ion_transporting_atpase_complex.yaml (GO:0031004, lines 5-9), definition is a custom structural sentence while definition_source is set to GO:0031004. The official GO:0031004 definition via OAK is: 'Protein complex that carries out the reaction: ATP + H2O + K+(out) = ADP + phosphate + K+(in). It is a high affinity potassium uptake system. The E. coli complex consists of 4 proteins: KdpA is the potassium ion translocase, KdpB is the ATPase, and KdpC and KdpF seem to be involved in assembly and stabilization of the complex.'

### F2: potassium_ion_transporting_atpase_complex.yaml omits sub-section-cited PMID:41384914 from top-level evidence

minor / open / confirmed; issue key: potassium-atpase-complex-missing-top-level-pmid-evidence.

In data/structures/energy_complex/potassium_ion_transporting_atpase_complex.yaml (GO:0031004), taxonomic_distribution[0].reference, functions[1].evidence[1].reference (potassium_ion_transport), and causal_graphs[0].edges[5].evidence[0].reference cite PMID:41384914, but top-level evidence (lines 212-231) lists only GO:0031004, ComplexPortal:CPX-3564, PMID:41259220, and PMID:34272288 without including PMID:41384914.

## Recommended Actions And Acceptance Checks

### A1

Set definition in data/structures/energy_complex/potassium_ion_transporting_atpase_complex.yaml to the official GO:0031004 definition text, preserve structural elaboration in description, and add PMID:41384914 to top-level evidence.

- .venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv
- .venv/bin/python scripts/validate_history.py

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev_strict_kdp | scripts/validate_strict.py; strict_all receipt | supports | validate_strict.py exited 0 across all 1,015 records. |
| ev_history_kdp | scripts/validate_history.py; history_all receipt | supports | validate_history.py exited 0 across all 2,192 history records. |
| ev_kdp_definition_and_evidence | data/structures/energy_complex/potassium_ion_transporting_atpase_complex.yaml; definition, definition_source, taxonomic_distribution[0].reference, functions[1].evidence[1].reference, evidence, causal_graphs[0].edges[5].evidence[0].reference (lines 5-9, 177, 207, 212-231, 336) | supports | potassium_ion_transporting_atpase_complex.yaml sets definition_source: GO:0031004 on a custom structural sentence and cites PMID:41384914 in taxonomic_distribution[0].reference, functions[1].evidence[1].reference, and causal_graphs[0].edges[5].evidence[0].reference while omitting PMID:41384914 from top-level evidence. |

## Limits And Additional Notes

- Record edits for potassium_ion_transporting_atpase_complex.yaml are queued for Cycle 6 Stage 5 (resolve_review_findings).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261031T123502Z-potassium-ion-transporting-atpase-complex-review
kind: record
repository: CultureBotAI/CellStructureMech
title: 'Single-record review of potassium ion-transporting ATPase complex (GO:0031004):
  definition_source attribution and top-level PMID:41384914 evidence'
started_at: '2026-10-31T12:30:30Z'
finished_at: '2026-10-31T12:35:02Z'
reviewer:
  identity: antigravity-c6s4-record-review
  kind: agent
  model: claude-opus-4-6
  independence: independent
  independence_basis: Reviewed in Cycle 6 Stage 4 record_review against committed
    git revision 9634411be0aeec8d8f4b9cb9158e3165db87c150 without record edits in
    this stage.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
native_verdict: NEEDS_CURATION
scientific_review: true
summary: 'Single-record audit of potassium_ion_transporting_atpase_complex.yaml (GO:0031004,
  potassium ion-transporting ATPase complex). Subunit composition (KdpF, KdpA, KdpB,
  KdpC with E. coli K-12 UniProtKB entries P36937, P03959, P03960, P03961) and causal
  graph are well-supported. Two minor curation issues were identified: (1) definition
  is a custom structural sentence while definition_source is set to GO:0031004 instead
  of quoting the official GO:0031004 definition verbatim; and (2) top-level evidence
  omits PMID:41384914, which is cited in taxonomic_distribution[0].reference, functions[1].evidence[1].reference,
  and causal_graphs[0].edges[5].evidence[0].reference.'
source:
  git_revision: 9634411be0aeec8d8f4b9cb9158e3165db87c150
  state: git_commit
  inputs:
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
    role: context
  - path: AGENTS.md
    sha256: ef74a980161b55cd24f1851e38d1c0b2e004fcf8837f1bc70da1874e4e8380f0
    role: context
  - path: conf/record_review.yaml
    sha256: d3334a12b8a616a7638f1195748085d2b543fba7df67ad4ff8fcc0ac18f2d3ee
    role: context
  - path: data/structures/energy_complex/potassium_ion_transporting_atpase_complex.yaml
    sha256: 2302fc637ad2db57b258080172b9f4d4a53721fd13c60e7450758acc111ffded
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
  description: Single-record review of data/structures/energy_complex/potassium_ion_transporting_atpase_complex.yaml
    (GO:0031004).
  selection: Targeted single-record audit of newly added Cycle 6 Stage 1 record potassium_ion_transporting_atpase_complex.yaml
    during Cycle 6 Stage 4 full-corpus inspection.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0031004
targets:
- target_id: GO:0031004
  path: data/structures/energy_complex/potassium_ion_transporting_atpase_complex.yaml
  label: potassium ion-transporting ATPase complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 2302fc637ad2db57b258080172b9f4d4a53721fd13c60e7450758acc111ffded
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/potassium_ion_transporting_atpase_complex.yaml
    role: maintained_record
checks:
- check_id: strict_potassium_atpase_complex
  name: Strict corpus validation covering potassium_ion_transporting_atpase_complex.yaml
  status: passed
  required: true
  summary: potassium_ion_transporting_atpase_complex.yaml passes current strict LinkML
    validation.
  target_ids:
  - GO:0031004
  command: .venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_strict_kdp
- check_id: history_potassium_atpase_complex
  name: History ledger validation covering potassium_ion_transporting_atpase_complex.yaml
  status: passed
  required: true
  summary: History ledger records covering potassium_ion_transporting_atpase_complex.yaml
    validate cleanly.
  target_ids:
  - GO:0031004
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_history_kdp
evidence:
- evidence_id: ev_strict_kdp
  kind: validation
  reference: scripts/validate_strict.py
  locator: strict_all receipt
  accessed_at: '2026-10-31T12:31:00Z'
  support: supports
  summary: validate_strict.py exited 0 across all 1,015 records.
  snapshot_sha256: dac1304f2a7feba26c94eee3835f43b0d766af8799cf4ef6f24109717d585fbd
- evidence_id: ev_history_kdp
  kind: validation
  reference: scripts/validate_history.py
  locator: history_all receipt
  accessed_at: '2026-10-31T12:31:00Z'
  support: supports
  summary: validate_history.py exited 0 across all 2,192 history records.
  snapshot_sha256: 4f1459e8514fab4d9a4196c25cc7c27a6ec862b50ae111521446eb44924ae9db
- evidence_id: ev_kdp_definition_and_evidence
  kind: record_content
  reference: data/structures/energy_complex/potassium_ion_transporting_atpase_complex.yaml
  locator: definition, definition_source, taxonomic_distribution[0].reference, functions[1].evidence[1].reference,
    evidence, causal_graphs[0].edges[5].evidence[0].reference (lines 5-9, 177, 207,
    212-231, 336)
  accessed_at: '2026-10-31T12:31:00Z'
  support: supports
  summary: 'potassium_ion_transporting_atpase_complex.yaml sets definition_source:
    GO:0031004 on a custom structural sentence and cites PMID:41384914 in taxonomic_distribution[0].reference,
    functions[1].evidence[1].reference, and causal_graphs[0].edges[5].evidence[0].reference
    while omitting PMID:41384914 from top-level evidence.'
  quote: "definition: A heterotetrameric P-type ATPase complex (KdpFABC) in the prokaryotic\n\
    \  plasma membrane that couples ATP hydrolysis in the KdpB P-type ATPase subunit\
    \ to\n  high-affinity potassium ion import through the channel-like KdpA selectivity\
    \ filter\n  and inter-subunit intramembrane tunnel, stabilized by KdpC and KdpF.\n\
    definition_source: GO:0031004"
  snapshot_sha256: 2302fc637ad2db57b258080172b9f4d4a53721fd13c60e7450758acc111ffded
assessments:
- assessment_id: assess_kdp_identity_and_components
  area: identity
  topic: GO cellular_component identity and KdpFABC subunit composition of GO:0031004
  outcome: supported
  summary: GO:0031004 accurately identifies the prokaryotic KdpFABC complex with verified
    E. coli K-12 UniProtKB protein_examples.
  target_ids:
  - GO:0031004
  evidence_ids:
  - ev_strict_kdp
  - ev_history_kdp
- assessment_id: assess_kdp_definition_and_top_level_evidence
  area: evidence
  topic: Official GO:0031004 definition attribution and top-level PMID:41384914 evidence
    parity
  outcome: concern
  summary: 'definition uses custom prose while setting definition_source: GO:0031004,
    and top-level evidence omits PMID:41384914 cited in three sub-sections.'
  target_ids:
  - GO:0031004
  evidence_ids:
  - ev_kdp_definition_and_evidence
findings:
- finding_id: F1
  issue_key: potassium-atpase-complex-definition-source-attribution
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: 'potassium_ion_transporting_atpase_complex.yaml attributes a custom definition
    to definition_source: GO:0031004'
  description: 'In data/structures/energy_complex/potassium_ion_transporting_atpase_complex.yaml
    (GO:0031004, lines 5-9), definition is a custom structural sentence while definition_source
    is set to GO:0031004. The official GO:0031004 definition via OAK is: ''Protein
    complex that carries out the reaction: ATP + H2O + K+(out) = ADP + phosphate +
    K+(in). It is a high affinity potassium uptake system. The E. coli complex consists
    of 4 proteins: KdpA is the potassium ion translocase, KdpB is the ATPase, and
    KdpC and KdpF seem to be involved in assembly and stabilization of the complex.'''
  target_ids:
  - GO:0031004
  field_paths:
  - definition
  - definition_source
  - description
  evidence_ids:
  - ev_kdp_definition_and_evidence
  rule_id: docs/SCHEMA.md:CellStructureRecord.definition_source
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/potassium_ion_transporting_atpase_complex.yaml
    role: maintained_record
  tags:
  - energy_complex
  - definition-source
  - stage4-record-review
- finding_id: F2
  issue_key: potassium-atpase-complex-missing-top-level-pmid-evidence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: potassium_ion_transporting_atpase_complex.yaml omits sub-section-cited PMID:41384914
    from top-level evidence
  description: In data/structures/energy_complex/potassium_ion_transporting_atpase_complex.yaml
    (GO:0031004), taxonomic_distribution[0].reference, functions[1].evidence[1].reference
    (potassium_ion_transport), and causal_graphs[0].edges[5].evidence[0].reference
    cite PMID:41384914, but top-level evidence (lines 212-231) lists only GO:0031004,
    ComplexPortal:CPX-3564, PMID:41259220, and PMID:34272288 without including PMID:41384914.
  target_ids:
  - GO:0031004
  field_paths:
  - evidence
  evidence_ids:
  - ev_kdp_definition_and_evidence
  rule_id: .claude/skills/curate-yaml-record/SKILL.md:top-level-evidence
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/potassium_ion_transporting_atpase_complex.yaml
    role: maintained_record
  tags:
  - energy_complex
  - evidence
  - stage4-record-review
actions:
- action_id: A1
  description: Set definition in data/structures/energy_complex/potassium_ion_transporting_atpase_complex.yaml
    to the official GO:0031004 definition text, preserve structural elaboration in
    description, and add PMID:41384914 to top-level evidence.
  finding_ids:
  - F1
  - F2
  target_ids:
  - GO:0031004
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/potassium_ion_transporting_atpase_complex.yaml
    role: maintained_record
  acceptance_checks:
  - .venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv
  - .venv/bin/python scripts/validate_history.py
limitations:
- Record edits for potassium_ion_transporting_atpase_complex.yaml are queued for Cycle
  6 Stage 5 (resolve_review_findings).
tags:
- stage4
- record-review
- energy_complex
```
