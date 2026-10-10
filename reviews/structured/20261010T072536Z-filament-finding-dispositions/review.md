# Disposition of filament record findings

- Review: 20261010T072536Z-filament-finding-dispositions
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-10T07:25:34Z
- Finished UTC: 2026-10-10T07:25:36Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

All 1 prior findings are resolved within this scoped reassessment. This does not certify unreviewed claims or human scientific approval.

## Scope And Provenance

Re-read the corrected record and reassess exactly the predecessor findings against their inspected evidence and native rules.

Selection: All findings from 20261010T070621Z-archaellum-filament-scope; no added corpus coverage.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f346ba56ced970ce94afed30ec349a61b3982c17.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:archaeal_type_flagellum_filament | data/structures/appendage/archaeal_type_flagellum_filament.yaml | maintained | archaeal-type flagellum filament |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Post-edit filament-schema | passed | True | cellstructuremech:archaeal_type_flagellum_filament | Documented validation completed on the corrected bytes before this successor bundle was added; review output is separately validated. |
| Post-edit filament-strict | passed | True | cellstructuremech:archaeal_type_flagellum_filament | Documented validation completed on the corrected bytes before this successor bundle was added; review output is separately validated. |
| Post-edit filament-snippets | passed | True | cellstructuremech:archaeal_type_flagellum_filament | Documented validation completed on the corrected bytes before this successor bundle was added; review output is separately validated. |
| Post-edit history | passed | True | cellstructuremech:archaeal_type_flagellum_filament | Documented validation completed on the corrected bytes before this successor bundle was added; review output is separately validated. |
| Post-edit labels | passed | True | cellstructuremech:archaeal_type_flagellum_filament | Documented validation completed on the corrected bytes before this successor bundle was added; review output is separately validated. |
| Post-edit traits | passed | True | cellstructuremech:archaeal_type_flagellum_filament | Documented validation completed on the corrected bytes before this successor bundle was added; review output is separately validated. |
| Post-edit qc | passed | True | cellstructuremech:archaeal_type_flagellum_filament | Documented validation completed on the corrected bytes before this successor bundle was added; review output is separately validated. |
| Expression adapter applicability | not_applicable | False | cellstructuremech:archaeal_type_flagellum_filament | No dataset for the named M. villosus exemplar; unrelated Sulfolobus data are not transferred to this species. |

## Scientific And Domain Assessments

### Disposition of the exact saved findings

evidence: supported. Targets: cellstructuremech:archaeal_type_flagellum_filament.

The changed assertions now match their inspected evidence at the declared experimental or abstract-only level. Model-versus-measurement and assembly-versus-function distinctions are retained.

### Unreviewed content and incomplete full-text access

completeness: unknown. Targets: cellstructuremech:archaeal_type_flagellum_filament.

This successor resolves the named findings only. It does not expand the predecessor scientific coverage or remove its access limitations.

## Findings

### F1: Remove the blanket bacterial absence assertion

major / resolved / confirmed; issue key: archaellum-filament-bacterial-absence-2025.

Replaced ABSENT with bounded VARIABLE distribution cited to the 2025 study; reconciled identity/function wording where needed and retained archaeal-only mechanistic graph scope. The bacterial motor is not described as directly resolved.

Disposition: Reassessed corrected bytes against the inspected sources and native rubric. Replaced ABSENT with bounded VARIABLE distribution cited to the 2025 study; reconciled identity/function wording where needed and retained archaeal-only mechanistic graph scope. The bacterial motor is not described as directly resolved.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/archaeal_type_flagellum_filament.yaml; Entire corrected target; fields cited by resolved findings | supports | Re-read corrected claims, their citations and scope qualifiers; verified PROPOSED and appended curation history. |
| bacterial | https://doi.org/10.1038/s41564-025-02110-8; Results: L. aerophila, an archaellated bacterium; filament cryoEM; motor predictions; Methods: growth and motility plates; Figs 3-5 | supports | Litorilinea aerophila has experimentally identified archaellum filaments and swimming motility. Motor architecture is supported partly by predicted structures, not a resolved bacterial motor. This evidence now supports the corrected, bounded claim. |
| synthesis | https://doi.org/10.3389/fmicb.2015.00023; Source-native secondary review; processing, assembly machinery, rotation, glycosylation and distribution sections | partial | Inspected as a secondary synthesis, not a new primary experiment. Supports the historical model but predates the bacterial exception. |
| arlb | https://doi.org/10.1038/s41467-022-28337-1; Results: The M. villosus archaellum consists of the subunits ArlB1 and ArlB2; Figs 1-4; Discussion; culture and filament methods | supports | The species-specific alternating ArlB1/ArlB2 filament is supported; the record does not universalize its stoichiometry or hypothetical dimer-assembly mechanism. |
| go-whole | https://www.ebi.ac.uk/QuickGO/term/GO:0097589; Current term ID, name, definition, synonyms, aspect and obsolete status | supports | The term denotes the whole archaellum, not a filament-only or motor-only entity. |
| go-motility | https://www.ebi.ac.uk/QuickGO/term/GO:0097590; Current name, definition and biological_process aspect | supports | The motility grounding is specific to the archaellum. |
| go-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=archaellum&amp;limit=100; QuickGO query archaellum, complete one-result response; separate broad name searches inspected only their first page | context_only | The exact archaellum query returns the whole-structure term. Neither that term nor bacterial motor/filament terms are exact replacements for the local subassemblies. |
| taxon-2 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2; taxId, scientificName, rank and available lineage/synonyms | supports | The identifier and label agree; taxon identity does not validate the associated presence assertion. |
| taxon-2157 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2157; taxId, scientificName, rank and available lineage/synonyms | supports | The identifier and label agree; taxon identity does not validate the associated presence assertion. |
| taxon-667126 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/667126; taxId, scientificName, rank and available lineage/synonyms | supports | The identifier and label agree; taxon identity does not validate the associated presence assertion. |
| parent | https://www.ebi.ac.uk/QuickGO/term/GO:0042995; Current definition, aspect and obsolete status | supports | The broader parent is appropriate; it is not asserted as exact identity. |
| prior | reviews/structured/20261010T070621Z-archaellum-filament-scope/review.yaml; Exact finding IDs and stable issue keys | context_only | Immutable predecessor preserved; no finding is silently deleted. |
| curation | history/records/archaeal_type_flagellum_filament/2026-10-10T070830Z-Codex-980dc6.yaml; Append-only EDIT event and issue links | supports | Records the guarded changes and scope without claiming premature downstream validation. |

## Limits And Additional Notes

- Scoped agent reassessment, not a full-corpus review or human promotion of PROPOSED.
- Original full-text and unassessed-claim limitations remain; the 2020 anchor citation explicitly remains abstract-only where used.
- Local validation passed; remote PR and merge-queue status must be checked separately before merge.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T072536Z-filament-finding-dispositions
kind: record
repository: CultureBotAI/CellStructureMech
title: Disposition of filament record findings
started_at: '2026-10-10T07:25:34Z'
finished_at: '2026-10-10T07:25:36Z'
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
  - path: data/structures/appendage/archaeal_type_flagellum_filament.yaml
    sha256: a42d6314be9fa818283455e0d0cd55b22729a9d6d85f4bca9cb87eab42e0e27c
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
  - path: history/records/archaeal_type_flagellum_filament/2026-09-23T045457Z-codex-9349a2.yaml
    sha256: 042dccb4f4022f86c4f4731c955be94f54c0f6daf87220d4fa6492249ebe054f
    role: context
  - path: history/records/archaeal_type_flagellum_filament/2026-09-23T050528Z-codex-821c8c.yaml
    sha256: d2639f3cca885b355e8350592c67a12b54161e8a2afba82f0ce7188b72fc06ad
    role: context
  - path: history/records/archaeal_type_flagellum_filament/2026-10-10T070830Z-Codex-980dc6.yaml
    sha256: 41364b90eb6c2292b82e3bc40169e075b8e85960a46e49999abb9faacea04060
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reviews/structured/20261010T070621Z-archaellum-filament-scope/review.yaml
    sha256: 22f06171cde413eeca090623c7119ed41b9b849f3fa40b7633f825f3a51a2c40
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: cellstructuremech:archaeal_type_flagellum_filament
  path: data/structures/appendage/archaeal_type_flagellum_filament.yaml
  label: archaeal-type flagellum filament
  kind: maintained
  record_class: CellStructureRecord
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/archaeal_type_flagellum_filament.yaml
    role: maintained scientific record
scope:
  description: Re-read the corrected record and reassess exactly the predecessor findings
    against their inspected evidence and native rules.
  selection: All findings from 20261010T070621Z-archaellum-filament-scope; no added
    corpus coverage.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:archaeal_type_flagellum_filament
checks:
- check_id: post-filament-schema
  name: Post-edit filament-schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:archaeal_type_flagellum_filament
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/appendage/archaeal_type_flagellum_filament.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Documented validation completed on the corrected bytes before this successor
    bundle was added; review output is separately validated.
  scope_note: 2026-10-10T07:11:25Z to 2026-10-10T07:11:27Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: post-filament-strict
  name: Post-edit filament-strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:archaeal_type_flagellum_filament
  command: .venv/bin/python scripts/validate_strict.py data/structures/appendage/archaeal_type_flagellum_filament.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Documented validation completed on the corrected bytes before this successor
    bundle was added; review output is separately validated.
  scope_note: 2026-10-10T07:11:27Z to 2026-10-10T07:11:31Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: post-filament-snippets
  name: Post-edit filament-snippets
  status: passed
  required: true
  target_ids:
  - cellstructuremech:archaeal_type_flagellum_filament
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/appendage/archaeal_type_flagellum_filament.yaml
    --report /private/tmp/csm-all-record-review-20261010T045734Z/filament-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: Documented validation completed on the corrected bytes before this successor
    bundle was added; review output is separately validated.
  scope_note: 2026-10-10T07:11:31Z to 2026-10-10T07:11:51Z; log SHA-256 adb46945b6c51e82af1d8f615eb370d5dd3b626d13cf0ea3c0647b1fc529d49c
- check_id: post-history
  name: Post-edit history
  status: passed
  required: true
  target_ids:
  - cellstructuremech:archaeal_type_flagellum_filament
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
  - cellstructuremech:archaeal_type_flagellum_filament
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
  - cellstructuremech:archaeal_type_flagellum_filament
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
  - cellstructuremech:archaeal_type_flagellum_filament
  command: .venv/bin/python scripts/run_qc.py
  exit_code: 0
  expected_exit_code: 0
  summary: Documented validation completed on the corrected bytes before this successor
    bundle was added; review output is separately validated.
  scope_note: 2026-10-10T07:15:09Z to 2026-10-10T07:25:08Z; log SHA-256 5d6dae8832a7bbe86a0779ba5b25367480370feb8c5f53667d1aa87c17e5b7af
- check_id: expression-applicability
  name: Expression adapter applicability
  status: not_applicable
  required: false
  target_ids:
  - cellstructuremech:archaeal_type_flagellum_filament
  summary: No dataset for the named M. villosus exemplar; unrelated Sulfolobus data
    are not transferred to this species.
  scope_note: Retained access or scope limitation from the predecessor; not a newly
    repeated command.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/appendage/archaeal_type_flagellum_filament.yaml
  locator: Entire corrected target; fields cited by resolved findings
  accessed_at: '2026-10-10T07:25:36Z'
  support: supports
  snapshot_sha256: a42d6314be9fa818283455e0d0cd55b22729a9d6d85f4bca9cb87eab42e0e27c
  summary: Re-read corrected claims, their citations and scope qualifiers; verified
    PROPOSED and appended curation history.
- evidence_id: bacterial
  kind: primary_source
  reference: https://doi.org/10.1038/s41564-025-02110-8
  locator: 'Results: L. aerophila, an archaellated bacterium; filament cryoEM; motor
    predictions; Methods: growth and motility plates; Figs 3-5'
  accessed_at: '2026-10-10T06:51:21Z'
  snapshot_sha256: e3f6b0250391b28747f24fcf3f2621d85db8f9a4b6a96866ad566af095f96afe
  summary: Litorilinea aerophila has experimentally identified archaellum filaments
    and swimming motility. Motor architecture is supported partly by predicted structures,
    not a resolved bacterial motor. This evidence now supports the corrected, bounded
    claim.
  support: supports
- evidence_id: synthesis
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2015.00023
  locator: Source-native secondary review; processing, assembly machinery, rotation,
    glycosylation and distribution sections
  accessed_at: '2026-10-10T05:03:52Z'
  snapshot_sha256: c2cec0461a17865f7242ef36df178bfc68d00c1f1e292b75f9682a6ba5461464
  summary: Inspected as a secondary synthesis, not a new primary experiment. Supports
    the historical model but predates the bacterial exception.
  support: partial
- evidence_id: arlb
  kind: primary_source
  reference: https://doi.org/10.1038/s41467-022-28337-1
  locator: 'Results: The M. villosus archaellum consists of the subunits ArlB1 and
    ArlB2; Figs 1-4; Discussion; culture and filament methods'
  accessed_at: '2026-10-10T05:03:54Z'
  snapshot_sha256: def26a9b9abd602bf1d23d61ce02a180a603d91852544f5d76b4bc32825f8ae1
  summary: The species-specific alternating ArlB1/ArlB2 filament is supported; the
    record does not universalize its stoichiometry or hypothetical dimer-assembly
    mechanism.
  support: supports
- evidence_id: go-whole
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/term/GO:0097589
  locator: Current term ID, name, definition, synonyms, aspect and obsolete status
  accessed_at: '2026-10-10T05:04:03Z'
  snapshot_sha256: 136977fcd947e027684e55ebfdd698cf4f17470777c56a3693ccc858ca104ce1
  summary: The term denotes the whole archaellum, not a filament-only or motor-only
    entity.
  support: supports
- evidence_id: go-motility
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/term/GO:0097590
  locator: Current name, definition and biological_process aspect
  accessed_at: '2026-10-10T05:04:04Z'
  snapshot_sha256: fef853d9ce6a36042c99450a6a8a5cdb7373120539d157e459b393864c6e6ddc
  summary: The motility grounding is specific to the archaellum.
  support: supports
- evidence_id: go-search
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=archaellum&limit=100
  locator: QuickGO query archaellum, complete one-result response; separate broad
    name searches inspected only their first page
  accessed_at: '2026-10-10T06:49:17Z'
  snapshot_sha256: be2922ae316517bc6802975dc8726012799d214d3c577c24a9d4cea5e29d7235
  summary: The exact archaellum query returns the whole-structure term. Neither that
    term nor bacterial motor/filament terms are exact replacements for the local subassemblies.
  support: context_only
  search_scope: QuickGO archaellum query complete at one hit. Broad multiword motor/filament
    queries returned more than one page; only first-page candidates were inspected.
    No exhaustive ontology-absence claim.
- evidence_id: taxon-2
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2
  locator: taxId, scientificName, rank and available lineage/synonyms
  accessed_at: '2026-10-10T05:04:05Z'
  snapshot_sha256: 314bd7723b8dea04f1840809fb74e06c514664fba9c6a0619e8f12e2a6dceef1
  summary: The identifier and label agree; taxon identity does not validate the associated
    presence assertion.
  support: supports
- evidence_id: taxon-2157
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2157
  locator: taxId, scientificName, rank and available lineage/synonyms
  accessed_at: '2026-10-10T05:04:05Z'
  snapshot_sha256: c6e652011b95e43e933983bf5f3f5cec9508c1925adae00dc55e46cd4e816b19
  summary: The identifier and label agree; taxon identity does not validate the associated
    presence assertion.
  support: supports
- evidence_id: taxon-667126
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/667126
  locator: taxId, scientificName, rank and available lineage/synonyms
  accessed_at: '2026-10-10T05:04:06Z'
  snapshot_sha256: 3c462a758dc7ee73cdf47f2edaa17ab951cfeba44ec50ff42b3236a1f4bacc77
  summary: The identifier and label agree; taxon identity does not validate the associated
    presence assertion.
  support: supports
- evidence_id: parent
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/term/GO:0042995
  locator: Current definition, aspect and obsolete status
  accessed_at: '2026-10-10T05:00:15Z'
  snapshot_sha256: b7bc936645b14ccf7b8d96f309e7ff4b3965e82c0b305cc6e5d3c2ae03005bd5
  summary: The broader parent is appropriate; it is not asserted as exact identity.
  support: supports
- evidence_id: prior
  kind: prior_review
  reference: reviews/structured/20261010T070621Z-archaellum-filament-scope/review.yaml
  locator: Exact finding IDs and stable issue keys
  accessed_at: '2026-10-10T07:25:36Z'
  snapshot_sha256: 22f06171cde413eeca090623c7119ed41b9b849f3fa40b7633f825f3a51a2c40
  support: context_only
  summary: Immutable predecessor preserved; no finding is silently deleted.
- evidence_id: curation
  kind: record_content
  reference: history/records/archaeal_type_flagellum_filament/2026-10-10T070830Z-Codex-980dc6.yaml
  locator: Append-only EDIT event and issue links
  accessed_at: '2026-10-10T07:25:36Z'
  snapshot_sha256: 41364b90eb6c2292b82e3bc40169e075b8e85960a46e49999abb9faacea04060
  support: supports
  summary: Records the guarded changes and scope without claiming premature downstream
    validation.
assessments:
- assessment_id: resolution
  area: evidence
  topic: Disposition of the exact saved findings
  outcome: supported
  target_ids:
  - cellstructuremech:archaeal_type_flagellum_filament
  evidence_ids:
  - record
  - bacterial
  - synthesis
  - arlb
  - go-whole
  - go-motility
  - taxon-2
  - taxon-2157
  - taxon-667126
  - parent
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
  - cellstructuremech:archaeal_type_flagellum_filament
  evidence_ids:
  - record
  - prior
  summary: This successor resolves the named findings only. It does not expand the
    predecessor scientific coverage or remove its access limitations.
findings:
- finding_id: F1
  issue_key: archaellum-filament-bacterial-absence-2025
  category: scope
  severity: major
  status: resolved
  certainty: confirmed
  title: Remove the blanket bacterial absence assertion
  description: Replaced ABSENT with bounded VARIABLE distribution cited to the 2025
    study; reconciled identity/function wording where needed and retained archaeal-only
    mechanistic graph scope. The bacterial motor is not described as directly resolved.
  target_ids:
  - cellstructuremech:archaeal_type_flagellum_filament
  field_paths:
  - taxonomic_distribution[1].presence
  - taxonomic_distribution[1].note
  evidence_ids:
  - record
  - bacterial
  - taxon-2
  - prior
  - curation
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/archaeal_type_flagellum_filament.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#evidence
  native_severity: major
  normalization_reason: A false domain-wide taxonomic exclusion, not merely a missing
    optional exemplar.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261010T070621Z-archaellum-filament-scope
    finding_id: F1
  disposition_reason: Reassessed corrected bytes against the inspected sources and
    native rubric. Replaced ABSENT with bounded VARIABLE distribution cited to the
    2025 study; reconciled identity/function wording where needed and retained archaeal-only
    mechanistic graph scope. The bacterial motor is not described as directly resolved.
actions: []
limitations:
- Scoped agent reassessment, not a full-corpus review or human promotion of PROPOSED.
- Original full-text and unassessed-claim limitations remain; the 2020 anchor citation
  explicitly remains abstract-only where used.
- Local validation passed; remote PR and merge-queue status must be checked separately
  before merge.
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261010T070621Z-archaellum-filament-scope
  relationship: Resolves exactly the predecessor findings; other earlier dispositions
    remain unchanged.
links:
- https://github.com/CultureBotAI/CellStructureMech/issues/2115
```
