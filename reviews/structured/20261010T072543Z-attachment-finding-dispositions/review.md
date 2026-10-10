# Disposition of attachment record findings

- Review: 20261010T072543Z-attachment-finding-dispositions
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-10T07:25:41Z
- Finished UTC: 2026-10-10T07:25:43Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

All 1 prior findings are resolved within this scoped reassessment. This does not certify unreviewed claims or human scientific approval.

## Scope And Provenance

Re-read the corrected record and reassess exactly the predecessor findings against their inspected evidence and native rules.

Selection: All findings from 20261010T070627Z-attachment-assembly; no added corpus coverage.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f346ba56ced970ce94afed30ec349a61b3982c17.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0033099 | data/structures/appendage/attachment_organelle.yaml | maintained | attachment organelle |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Post-edit attachment-schema | passed | True | GO:0033099 | Documented validation completed on the corrected bytes before this successor bundle was added; review output is separately validated. |
| Post-edit attachment-strict | passed | True | GO:0033099 | Documented validation completed on the corrected bytes before this successor bundle was added; review output is separately validated. |
| Post-edit attachment-snippets | passed | True | GO:0033099 | Documented validation completed on the corrected bytes before this successor bundle was added; review output is separately validated. |
| Post-edit history | passed | True | GO:0033099 | Documented validation completed on the corrected bytes before this successor bundle was added; review output is separately validated. |
| Post-edit labels | passed | True | GO:0033099 | Documented validation completed on the corrected bytes before this successor bundle was added; review output is separately validated. |
| Post-edit traits | passed | True | GO:0033099 | Documented validation completed on the corrected bytes before this successor bundle was added; review output is separately validated. |
| Post-edit qc | passed | True | GO:0033099 | Documented validation completed on the corrected bytes before this successor bundle was added; review output is separately validated. |
| Remaining claim and identifier verification | skipped | True | GO:0033099 | Other components, protein examples, taxonomy, functions and full reference set have not been independently verified in this partial assessment. |

## Scientific And Domain Assessments

### Disposition of the exact saved findings

evidence: supported. Targets: GO:0033099.

The changed assertions now match their inspected evidence at the declared experimental or abstract-only level. Model-versus-measurement and assembly-versus-function distinctions are retained.

### Unreviewed content and incomplete full-text access

completeness: unknown. Targets: GO:0033099.

This successor resolves the named findings only. It does not expand the predecessor scientific coverage or remove its access limitations.

## Findings

### F1: Separate P1-complex assembly essentiality from adhesive function

major / resolved / confirmed; issue key: attachment-organelle-p1-complex-assembly-essentiality.

Changed P1/P40/P90 assembly essentiality to DISPENSABLE with class IV-22 imaging evidence; retained CONSTITUENT and explicitly excluded normal-function or cross-species generalization.

Disposition: Reassessed corrected bytes against the inspected sources and native rubric. Changed P1/P40/P90 assembly essentiality to DISPENSABLE with class IV-22 imaging evidence; retained CONSTITUENT and explicitly excluded normal-function or cross-species generalization.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/attachment_organelle.yaml; Entire corrected target; fields cited by resolved findings | supports | Re-read corrected claims, their citations and scope qualifiers; verified PROPOSED and appended curation history. |
| imaging | https://doi.org/10.1128/mBio.00243-16; Results: Surface structures; Figures 2 and 3B; Materials and Methods: strains | supports | Class IV-22 lacks P1/P40/P90 and surface nap but retains a membrane-bounded attachment organelle and internal core resembling wild type. This does not demonstrate normal cytadherence or gliding. This evidence now supports the corrected, bounded claim. |
| identity | https://www.ebi.ac.uk/QuickGO/term/GO:0033099; Nonobsolete cellular-component term and definition | supports | The exact term denotes the membrane extension with an internal core, rather than only its surface adhesin layer. |
| strain | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/272634; Scientific name, strain rank and synonyms | supports | The M129 named example agrees with the current Mycoplasmoides pneumoniae strain authority and historical Mycoplasma name. |
| rule | docs/CURATION.md; Components: essentiality is about structure formation; see schema EssentialityEnum | supports | A genuine constituent may be DISPENSABLE when the structure still forms defectively; essentiality is not normal functional performance. |
| prior | reviews/structured/20261010T070627Z-attachment-assembly/review.yaml; Exact finding IDs and stable issue keys | context_only | Immutable predecessor preserved; no finding is silently deleted. |
| curation | history/records/attachment_organelle/2026-10-10T070837Z-Codex-5596d4.yaml; Append-only EDIT event and issue links | supports | Records the guarded changes and scope without claiming premature downstream validation. |

## Limits And Additional Notes

- Scoped agent reassessment, not a full-corpus review or human promotion of PROPOSED.
- Original full-text and unassessed-claim limitations remain; the 2020 anchor citation explicitly remains abstract-only where used.
- Local validation passed; remote PR and merge-queue status must be checked separately before merge.
- Terminology clarification for the predecessor assembly assessment: class IV-22 has an MPN141 frameshift and loss of P1/P40/P90, not a demonstrated gene-deletion construct. The original phrase deletion phenotype should be read as protein-loss phenotype; the imaging-supported finding and its disposition are unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T072543Z-attachment-finding-dispositions
kind: record
repository: CultureBotAI/CellStructureMech
title: Disposition of attachment record findings
started_at: '2026-10-10T07:25:41Z'
finished_at: '2026-10-10T07:25:43Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same Codex agent performed curation and this disposition. A
    separate AI adversarial reassessment is reported on the PR; neither constitutes
    human sign-off.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: pass_with_limitations
scientific_review: true
summary: All 1 prior findings are resolved within this scoped reassessment. This does
  not certify unreviewed claims or human scientific approval.
source:
  git_revision: f346ba56ced970ce94afed30ec349a61b3982c17
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
    role: context
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/appendage/attachment_organelle.yaml
    sha256: 84aa1125628ddc73b95ae788333569da468344c9beb1cf99793363e65c492164
    role: target
  - path: docs/CURATION.md
    sha256: c3e482fbf381edcf0238e579648b779c3a8803a1d888b89397ad6fc8808dd07d
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
  - path: history/README.md
    sha256: 1636df44f28547f440242afcb4a05ac293b9714b4d7b809cecc30b975e44a522
    role: context
  - path: history/records/attachment_organelle/2026-09-06T150543Z-claude-459ee1.yaml
    sha256: cd0da0beec435828bc3ff1e604c42af6bff609c6509c346f0dc280ba19550a25
    role: context
  - path: history/records/attachment_organelle/2026-09-06T152541Z-claude-c2f4d9.yaml
    sha256: e4eb2edc91e2032dbf94dab07b8846bedbd06e19349f85d234d11c4b76986a39
    role: context
  - path: history/records/attachment_organelle/2026-10-10T070837Z-Codex-5596d4.yaml
    sha256: da925b58cbea8dcb7438ba3fab90de6415acd3a50bd49611d86800d5e1973497
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reviews/structured/20261010T070627Z-attachment-assembly/review.yaml
    sha256: a975e4dd0b75cda1322a6e18d16c5e2dd84bdaf5528dd5ab1d50b20ff112b0b0
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: GO:0033099
  path: data/structures/appendage/attachment_organelle.yaml
  label: attachment organelle
  kind: maintained
  record_class: CellStructureRecord
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/attachment_organelle.yaml
    role: maintained scientific record
scope:
  description: Re-read the corrected record and reassess exactly the predecessor findings
    against their inspected evidence and native rules.
  selection: All findings from 20261010T070627Z-attachment-assembly; no added corpus
    coverage.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - GO:0033099
checks:
- check_id: post-attachment-schema
  name: Post-edit attachment-schema
  status: passed
  required: true
  target_ids:
  - GO:0033099
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/appendage/attachment_organelle.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Documented validation completed on the corrected bytes before this successor
    bundle was added; review output is separately validated.
  scope_note: 2026-10-10T07:12:44Z to 2026-10-10T07:12:47Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: post-attachment-strict
  name: Post-edit attachment-strict
  status: passed
  required: true
  target_ids:
  - GO:0033099
  command: .venv/bin/python scripts/validate_strict.py data/structures/appendage/attachment_organelle.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Documented validation completed on the corrected bytes before this successor
    bundle was added; review output is separately validated.
  scope_note: 2026-10-10T07:12:47Z to 2026-10-10T07:12:51Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: post-attachment-snippets
  name: Post-edit attachment-snippets
  status: passed
  required: true
  target_ids:
  - GO:0033099
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/appendage/attachment_organelle.yaml
    --report /private/tmp/csm-all-record-review-20261010T045734Z/attachment-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: Documented validation completed on the corrected bytes before this successor
    bundle was added; review output is separately validated.
  scope_note: 2026-10-10T07:12:51Z to 2026-10-10T07:13:12Z; log SHA-256 7115ae4b95b9a14b53c206b81cb145ce2536ea4e32296f471a47c40e230c8618
- check_id: post-history
  name: Post-edit history
  status: passed
  required: true
  target_ids:
  - GO:0033099
  command: .venv/bin/python scripts/validate_history.py history
  exit_code: 0
  expected_exit_code: 0
  summary: Documented validation completed on the corrected bytes before this successor
    bundle was added; review output is separately validated.
  scope_note: 2026-10-10T07:13:12Z to 2026-10-10T07:13:25Z; log SHA-256 93b3169f8b92ab2b60919adcac2994723dd741de791680ffe216e57579cc44ea
- check_id: post-labels
  name: Post-edit labels
  status: passed
  required: true
  target_ids:
  - GO:0033099
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Documented validation completed on the corrected bytes before this successor
    bundle was added; review output is separately validated.
  scope_note: 2026-10-10T07:13:25Z to 2026-10-10T07:14:49Z; log SHA-256 553dd4c9f88c8a5289a33f588649f4677e541cc9da09ecd6c78c0e9f3cae8917
- check_id: post-traits
  name: Post-edit traits
  status: passed
  required: true
  target_ids:
  - GO:0033099
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Documented validation completed on the corrected bytes before this successor
    bundle was added; review output is separately validated.
  scope_note: 2026-10-10T07:14:49Z to 2026-10-10T07:15:09Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: post-qc
  name: Post-edit qc
  status: passed
  required: true
  target_ids:
  - GO:0033099
  command: .venv/bin/python scripts/run_qc.py
  exit_code: 0
  expected_exit_code: 0
  summary: Documented validation completed on the corrected bytes before this successor
    bundle was added; review output is separately validated.
  scope_note: 2026-10-10T07:15:09Z to 2026-10-10T07:25:08Z; log SHA-256 5d6dae8832a7bbe86a0779ba5b25367480370feb8c5f53667d1aa87c17e5b7af
- check_id: remaining-science
  name: Remaining claim and identifier verification
  status: skipped
  required: true
  target_ids:
  - GO:0033099
  summary: Other components, protein examples, taxonomy, functions and full reference
    set have not been independently verified in this partial assessment.
  scope_note: Retained access or scope limitation from the predecessor; not a newly
    repeated command.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/appendage/attachment_organelle.yaml
  locator: Entire corrected target; fields cited by resolved findings
  accessed_at: '2026-10-10T07:25:43Z'
  snapshot_sha256: 84aa1125628ddc73b95ae788333569da468344c9beb1cf99793363e65c492164
  support: supports
  summary: Re-read corrected claims, their citations and scope qualifiers; verified
    PROPOSED and appended curation history.
- evidence_id: imaging
  kind: primary_source
  reference: https://doi.org/10.1128/mBio.00243-16
  locator: 'Results: Surface structures; Figures 2 and 3B; Materials and Methods:
    strains'
  summary: Class IV-22 lacks P1/P40/P90 and surface nap but retains a membrane-bounded
    attachment organelle and internal core resembling wild type. This does not demonstrate
    normal cytadherence or gliding. This evidence now supports the corrected, bounded
    claim.
  support: supports
  accessed_at: '2026-10-10T07:01:02Z'
  snapshot_sha256: 7d579ad7ba828670d16c6e9e9a73c4a692a56d52366b08be6e97b59e0249f793
- evidence_id: identity
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/term/GO:0033099
  locator: Nonobsolete cellular-component term and definition
  summary: The exact term denotes the membrane extension with an internal core, rather
    than only its surface adhesin layer.
  support: supports
  accessed_at: '2026-10-10T07:01:03Z'
  snapshot_sha256: 7386b48d2989ab4eb1369b50a8f4fb75cc4fd7f1685e63842bacf75d5de52251
- evidence_id: strain
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/272634
  locator: Scientific name, strain rank and synonyms
  summary: The M129 named example agrees with the current Mycoplasmoides pneumoniae
    strain authority and historical Mycoplasma name.
  support: supports
  accessed_at: '2026-10-10T07:01:04Z'
  snapshot_sha256: 8d9655c50a16daf386bf566a6d2559d9cfa092a9e862d4eeba09dbd474a8f7f2
- evidence_id: rule
  kind: authority
  reference: docs/CURATION.md
  locator: 'Components: essentiality is about structure formation; see schema EssentialityEnum'
  accessed_at: '2026-10-10T07:06:27Z'
  support: supports
  summary: A genuine constituent may be DISPENSABLE when the structure still forms
    defectively; essentiality is not normal functional performance.
- evidence_id: prior
  kind: prior_review
  reference: reviews/structured/20261010T070627Z-attachment-assembly/review.yaml
  locator: Exact finding IDs and stable issue keys
  accessed_at: '2026-10-10T07:25:43Z'
  snapshot_sha256: a975e4dd0b75cda1322a6e18d16c5e2dd84bdaf5528dd5ab1d50b20ff112b0b0
  support: context_only
  summary: Immutable predecessor preserved; no finding is silently deleted.
- evidence_id: curation
  kind: record_content
  reference: history/records/attachment_organelle/2026-10-10T070837Z-Codex-5596d4.yaml
  locator: Append-only EDIT event and issue links
  accessed_at: '2026-10-10T07:25:43Z'
  snapshot_sha256: da925b58cbea8dcb7438ba3fab90de6415acd3a50bd49611d86800d5e1973497
  support: supports
  summary: Records the guarded changes and scope without claiming premature downstream
    validation.
assessments:
- assessment_id: resolution
  area: evidence
  topic: Disposition of the exact saved findings
  outcome: supported
  target_ids:
  - GO:0033099
  evidence_ids:
  - record
  - imaging
  - identity
  - strain
  - rule
  - prior
  - curation
  summary: The changed assertions now match their inspected evidence at the declared
    experimental or abstract-only level. Model-versus-measurement and assembly-versus-function
    distinctions are retained.
- assessment_id: limits
  area: completeness
  topic: Unreviewed content and incomplete full-text access
  outcome: unknown
  target_ids:
  - GO:0033099
  evidence_ids:
  - record
  - prior
  summary: This successor resolves the named findings only. It does not expand the
    predecessor scientific coverage or remove its access limitations.
findings:
- finding_id: F1
  issue_key: attachment-organelle-p1-complex-assembly-essentiality
  category: evidence
  severity: major
  status: resolved
  certainty: confirmed
  title: Separate P1-complex assembly essentiality from adhesive function
  description: Changed P1/P40/P90 assembly essentiality to DISPENSABLE with class
    IV-22 imaging evidence; retained CONSTITUENT and explicitly excluded normal-function
    or cross-species generalization.
  target_ids:
  - GO:0033099
  field_paths:
  - components[0].essentiality
  - components[0].evidence
  evidence_ids:
  - record
  - imaging
  - rule
  - prior
  - curation
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/attachment_organelle.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#components
  native_severity: major
  normalization_reason: The assembly enum asserts absence of the structure despite
    direct mutant imaging.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261010T070627Z-attachment-assembly
    finding_id: F1
  disposition_reason: Reassessed corrected bytes against the inspected sources and
    native rubric. Changed P1/P40/P90 assembly essentiality to DISPENSABLE with class
    IV-22 imaging evidence; retained CONSTITUENT and explicitly excluded normal-function
    or cross-species generalization.
actions: []
limitations:
- Scoped agent reassessment, not a full-corpus review or human promotion of PROPOSED.
- Original full-text and unassessed-claim limitations remain; the 2020 anchor citation
  explicitly remains abstract-only where used.
- Local validation passed; remote PR and merge-queue status must be checked separately
  before merge.
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261010T070627Z-attachment-assembly
  relationship: Resolves exactly the predecessor findings; other earlier dispositions
    remain unchanged.
links:
- https://github.com/CultureBotAI/CellStructureMech/issues/2118
notes:
- 'Terminology clarification for the predecessor assembly assessment: class IV-22
  has an MPN141 frameshift and loss of P1/P40/P90, not a demonstrated gene-deletion
  construct. The original phrase deletion phenotype should be read as protein-loss
  phenotype; the imaging-supported finding and its disposition are unchanged.'
```
