# Attachment organelle: assembly versus adhesion essentiality

- Review: 20261010T070627Z-attachment-assembly
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-10T06:58:35Z
- Finished UTC: 2026-10-10T07:06:27Z
- Reviewer: Codex (unknown)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One confirmed assembly-essentiality defect; this is not a complete review of the record.

## Scope And Provenance

Full target read; scientific assessment limited to exact identity and P1/P40/P90 assembly essentiality.

Selection: Exact attachment_organelle.yaml target, not a corpus sample.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f346ba56ced970ce94afed30ec349a61b3982c17.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0033099 | data/structures/appendage/attachment_organelle.yaml | maintained | attachment organelle |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| history | passed | True | GO:0033099 | Full-corpus deterministic gate passed; not scientific sign-off. |
| labels | passed | True | GO:0033099 | Full-corpus deterministic gate passed; not scientific sign-off. |
| traits | passed | True | GO:0033099 | Full-corpus deterministic gate passed; not scientific sign-off. |
| qc | passed | True | GO:0033099 | Full-corpus deterministic gate passed; not scientific sign-off. |
| Focused schema | passed | True | GO:0033099 | Executed during this audit; no issues reported. |
| Focused strict | passed | True | GO:0033099 | Executed during this audit; no issues reported. |
| Remaining claim and identifier verification | skipped | True | GO:0033099 | Other components, protein examples, taxonomy, functions and full reference set have not been independently verified in this partial assessment. |

## Scientific And Domain Assessments

### Exact structure identity

identity: supported. Targets: GO:0033099.

The record denotes the attachment organelle including its internal core, not only the P1 surface layer.

### P1 surface-complex essentiality

evidence: concern. Targets: GO:0033099.

The deletion phenotype contradicts ESSENTIAL for assembly under the native definition; functional requirement must remain separate.

### Other scientific claims

completeness: unknown. Targets: GO:0033099.

Unassessed material remains; no findings are inferred from optional empty slots or lack of review.

## Findings

### F1: Separate P1-complex assembly essentiality from adhesive function

major / open / confirmed; issue key: attachment-organelle-p1-complex-assembly-essentiality.

components[0].essentiality is ESSENTIAL although the cited 2016 study shows an attachment organelle and internal core without P1/P40/P90. DISPENSABLE allows defective assembly; retain CONSTITUENT and the adhesive role.

## Recommended Actions And Acceptance Checks

### A1

Correct P1/P40/P90 assembly essentiality through the guarded writer and attach the mutant-imaging citation with its functional limit.

- DISPENSABLE applies to assembly, not normal adherence or gliding.
- The component remains a CONSTITUENT; no claims about other components are silently changed.
- Append both curation histories, preserve PROPOSED, and pass native gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/attachment_organelle.yaml; Entire YAML read; finding at components[0].essentiality | context_only | P1/P40/P90 is a constituent and classified ESSENTIAL for structure assembly. |
| imaging | https://doi.org/10.1128/mBio.00243-16; Results: Surface structures; Figures 2 and 3B; Materials and Methods: strains | refutes | Class IV-22 lacks P1/P40/P90 and surface nap but retains a membrane-bounded attachment organelle and internal core resembling wild type. This does not demonstrate normal cytadherence or gliding. |
| identity | https://www.ebi.ac.uk/QuickGO/term/GO:0033099; Nonobsolete cellular-component term and definition | supports | The exact term denotes the membrane extension with an internal core, rather than only its surface adhesin layer. |
| strain | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/272634; Scientific name, strain rank and synonyms | supports | The M129 named example agrees with the current Mycoplasmoides pneumoniae strain authority and historical Mycoplasma name. |
| rule | docs/CURATION.md; Components: essentiality is about structure formation; see schema EssentialityEnum | supports | A genuine constituent may be DISPENSABLE when the structure still forms defectively; essentiality is not normal functional performance. |

## Limits And Additional Notes

- Only identity and P1-complex assembly essentiality were scientifically assessed; the remaining identifiers and claims are unassessed.
- Ignored and hidden review/history files were included in the prior-finding search; no earlier matching P1 assembly finding was found in those directories.
- No structure or history was changed during this observation. Subsequent curation and GitHub publication require separate authorization.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T070627Z-attachment-assembly
kind: record
repository: CultureBotAI/CellStructureMech
title: 'Attachment organelle: assembly versus adhesion essentiality'
started_at: '2026-10-10T06:58:35Z'
finished_at: '2026-10-10T07:06:27Z'
reviewer:
  identity: Codex
  kind: agent
  independence: unknown
  independence_basis: Independence from historical agent authorship is not established.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: One confirmed assembly-essentiality defect; this is not a complete review
  of the record.
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
    sha256: b95cba4687283e9350fda6aacee5913f18a608e59648f77d78160afe5edc62d4
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
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
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
  description: Full target read; scientific assessment limited to exact identity and
    P1/P40/P90 assembly essentiality.
  selection: Exact attachment_organelle.yaml target, not a corpus sample.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - GO:0033099
checks:
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:0033099
  command: .venv/bin/python scripts/validate_history.py history
  exit_code: 0
  expected_exit_code: 0
  summary: Full-corpus deterministic gate passed; not scientific sign-off.
  scope_note: 2026-10-10T06:49:30Z to 2026-10-10T06:50:19Z; log SHA-256 86e440ae4c54ba14bc23c67108fe3a209b94444c27774b1b0b3b3535704719e6
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - GO:0033099
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Full-corpus deterministic gate passed; not scientific sign-off.
  scope_note: 2026-10-10T06:50:19Z to 2026-10-10T06:52:30Z; log SHA-256 553dd4c9f88c8a5289a33f588649f4677e541cc9da09ecd6c78c0e9f3cae8917
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - GO:0033099
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Full-corpus deterministic gate passed; not scientific sign-off.
  scope_note: 2026-10-10T06:52:30Z to 2026-10-10T06:52:59Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: qc
  name: qc
  status: passed
  required: true
  target_ids:
  - GO:0033099
  command: .venv/bin/python scripts/run_qc.py
  exit_code: 0
  expected_exit_code: 0
  summary: Full-corpus deterministic gate passed; not scientific sign-off.
  scope_note: 2026-10-10T06:52:59Z to 2026-10-10T07:06:08Z; log SHA-256 d2d47649ec6fd19e1d4b6fbeffe19366cc12c86cff12053c9bcb04ebea9d4ce5
- check_id: schema
  name: Focused schema
  status: passed
  required: true
  target_ids:
  - GO:0033099
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/appendage/attachment_organelle.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Executed during this audit; no issues reported.
- check_id: strict
  name: Focused strict
  status: passed
  required: true
  target_ids:
  - GO:0033099
  command: .venv/bin/python scripts/validate_strict.py data/structures/appendage/attachment_organelle.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Executed during this audit; no issues reported.
- check_id: remaining-science
  name: Remaining claim and identifier verification
  status: skipped
  required: true
  target_ids:
  - GO:0033099
  summary: Other components, protein examples, taxonomy, functions and full reference
    set have not been independently verified in this partial assessment.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/appendage/attachment_organelle.yaml
  locator: Entire YAML read; finding at components[0].essentiality
  accessed_at: '2026-10-10T07:06:27Z'
  snapshot_sha256: b95cba4687283e9350fda6aacee5913f18a608e59648f77d78160afe5edc62d4
  support: context_only
  summary: P1/P40/P90 is a constituent and classified ESSENTIAL for structure assembly.
- evidence_id: imaging
  kind: primary_source
  reference: https://doi.org/10.1128/mBio.00243-16
  locator: 'Results: Surface structures; Figures 2 and 3B; Materials and Methods:
    strains'
  summary: Class IV-22 lacks P1/P40/P90 and surface nap but retains a membrane-bounded
    attachment organelle and internal core resembling wild type. This does not demonstrate
    normal cytadherence or gliding.
  support: refutes
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
assessments:
- assessment_id: identity
  area: identity
  topic: Exact structure identity
  outcome: supported
  target_ids:
  - GO:0033099
  evidence_ids:
  - record
  - identity
  - strain
  summary: The record denotes the attachment organelle including its internal core,
    not only the P1 surface layer.
- assessment_id: assembly
  area: evidence
  topic: P1 surface-complex essentiality
  outcome: concern
  target_ids:
  - GO:0033099
  evidence_ids:
  - record
  - imaging
  - rule
  summary: The deletion phenotype contradicts ESSENTIAL for assembly under the native
    definition; functional requirement must remain separate.
  dimensions:
  - name: experimental-context
    value: M. pneumoniae M129 and class IV-22 mutant; ECT and immuno-EM; Aluotto medium
      at 37 C
    definition: Observed organism, mutant, methods and growth context, not a universal
      phenotype for all homologues
    evidence_ids:
    - imaging
- assessment_id: remaining
  area: completeness
  topic: Other scientific claims
  outcome: unknown
  target_ids:
  - GO:0033099
  evidence_ids:
  - record
  summary: Unassessed material remains; no findings are inferred from optional empty
    slots or lack of review.
findings:
- finding_id: F1
  issue_key: attachment-organelle-p1-complex-assembly-essentiality
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Separate P1-complex assembly essentiality from adhesive function
  description: components[0].essentiality is ESSENTIAL although the cited 2016 study
    shows an attachment organelle and internal core without P1/P40/P90. DISPENSABLE
    allows defective assembly; retain CONSTITUENT and the adhesive role.
  target_ids:
  - GO:0033099
  field_paths:
  - components[0].essentiality
  - components[0].evidence
  evidence_ids:
  - record
  - imaging
  - rule
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/attachment_organelle.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#components
  native_severity: major
  normalization_reason: The assembly enum asserts absence of the structure despite
    direct mutant imaging.
actions:
- action_id: A1
  description: Correct P1/P40/P90 assembly essentiality through the guarded writer
    and attach the mutant-imaging citation with its functional limit.
  finding_ids:
  - F1
  target_ids:
  - GO:0033099
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/attachment_organelle.yaml
    role: maintained scientific record
  generator: just render
  acceptance_checks:
  - DISPENSABLE applies to assembly, not normal adherence or gliding.
  - The component remains a CONSTITUENT; no claims about other components are silently
    changed.
  - Append both curation histories, preserve PROPOSED, and pass native gates.
limitations:
- Only identity and P1-complex assembly essentiality were scientifically assessed;
  the remaining identifiers and claims are unassessed.
- Ignored and hidden review/history files were included in the prior-finding search;
  no earlier matching P1 assembly finding was found in those directories.
- No structure or history was changed during this observation. Subsequent curation
  and GitHub publication require separate authorization.
```
