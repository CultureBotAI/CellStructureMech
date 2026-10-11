# septin band: finding disposition

- Review: 20261011T135744Z-septin_band-disposition
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T13:48:13Z
- Finished UTC: 2026-10-11T13:57:44Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Exact minor wording finding resolved; original observation and PROPOSED status preserved.

## Scope And Provenance

Reassessment of the exact saved finding and preservation, not another whole-record review.

Selection: 20261011T134159Z-septin_band-audit
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 2f27c8dc37863233d1e6c3f8ae966f275c361805.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0032158 | data/structures/cytoskeleton/septin_band.yaml | maintained | septin band |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| septin_band-schema | passed | True | GO:0032158 | Actual deterministic check passed; scientific support assessed separately. |
| septin_band-strict | passed | True | GO:0032158 | Actual deterministic check passed; scientific support assessed separately. |
| septin_band-snippets | passed | True | GO:0032158 | No verbatim snippets; paraphrases assessed separately against inspected text. |
| history | passed | True | GO:0032158 | Actual deterministic check passed; scientific support assessed separately. |
| labels | passed | True | GO:0032158 | id↔label correspondence summary:<br>          OK_CANONICAL: 3544<br>            OK_SYNONYM: 50<br>          OK_EXCEPTION: 6<br>    SKIPPED_NO_ADAPTER: 603<br><br>✅ All id↔label pairs correspond. |
| traits | passed | True | GO:0032158 | Actual deterministic check passed; scientific support assessed separately. |
| curies | passed | True | GO:0032158 | resolver control: every resolver accepts a known id and rejects a fabricated one<br><br>identifier liveness summary:<br>  OK             4014<br>  SKIPPED         251<br><br>Every identifier resolves at its issuing authority. |
| focused | passed | True | GO:0032158 | ...........................                                              [100%]<br>27 passed in 35.88s |
| reviews | passed | True | GO:0032158 | Actual deterministic check passed; scientific support assessed separately. |
| diff | passed | True | GO:0032158 | Actual deterministic check passed; scientific support assessed separately. |
| release-qc | passed | True | GO:0032158 | Full local QC passed: 861 passed, 3 skipped in 541.83s (0:09:01). PR and native merge-group gates remain separate. |

## Scientific And Domain Assessments

### Correct polarized grown to polarized growth

evidence: supported. Targets: GO:0032158.

Definition now uses polarized growth; all other definition words, GO source, topology and scope remain unchanged.

## Findings

### F1: Correct polarized grown to polarized growth

minor / resolved / confirmed; issue key: septin-band-polarized-growth-wording.

Definition now uses polarized growth; all other definition words, GO source, topology and scope remain unchanged.

Disposition: Definition now uses polarized growth; all other definition words, GO source, topology and scope remain unchanged. Verified against inspected source, bounded diff, red/green tests and full local QC.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/septin_band.yaml | context_only | Entire corrected native YAML reread; only finding field and appended curation event changed. |
| rules | docs/CURATION.md | context_only | Keep source support at the narrowest claim and preserve uncertainty. |
| history | /private/tmp/csm-review-20261011T133153Z/septin_band-discussion-history.json | context_only | Committed discussion and event versions inspected; existing rationale and dates retained. |
| append-history-0 | history/records/septin_band/2026-09-30T142319Z-codex-0a6cd1.yaml | context_only | Existing append-only history inspected, including legacy actor metadata; not rewritten. |
| predecessors | /private/tmp/csm-review-20261011T133153Z/exact-target-predecessors.json | context_only | Ignored-inclusive canonical scan found no exact-target predecessor. |
| issue-search | /private/tmp/csm-review-20261011T133153Z/septin-issues.log | context_only | All-state septin search inspected: 24 closed issues, including prior evidence changes. No existing issue for either exact new defect. |
| adapter | /private/tmp/csm-review-20261011T133153Z/adapter.log | context_only | Live 28-dataset inventory has no matching fungal dataset. Not negative biological evidence. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000144,GO:0005856,GO:0005938,GO:0005940,GO:0031105,GO:0032151,GO:0032152,GO:0032153,GO:0032156,GO:0032158,GO:0032159,GO:0032160,GO:0032161,GO:0032162,GO:0032163,GO:0032164,GO:0032165,GO:0032166,GO:0032168,GO:0032169,GO:0032170,GO:0032171,GO:0032172,GO:0032173,GO:0032174,GO:0032177,GO:0032991,GO:0036391,GO:0110165; Exact term definitions, labels, obsolescence and typed child relations for the septin cohort | supports | Identity and hierarchy are supported. GO:0032158 itself contains the grown typo; local prose can correct spelling without changing source identity. |
| legacy | reports/yaml_record_review/20260930T144307Z-septin_band.md | context_only | Earlier clean review checked GO correspondence; original review preserved. |
| predecessor | reviews/structured/20261011T134159Z-septin_band-audit/review.yaml | context_only | Immutable observation committed before scientific mutation. |
| preservation | /private/tmp/csm-review-20261011T133153Z/preservation.json | context_only | 907 other native records, 908 semantic vectors and all old review/history/legacy bytes preserved. |
| red | /private/tmp/csm-review-20261011T133153Z/regressions-red.log | context_only | Two focused regressions fail on original records; identity control passes. |
| green | /private/tmp/csm-review-20261011T133153Z/post-focused.log | context_only | Focused regressions and guarded-writer tests pass after correction. |
| edit-history | history/records/septin_band/2026-10-11T134319Z-codex-ed0221.yaml | context_only | Actual append-only Codex EDIT links the issue and saved finding. |

## Limits And Additional Notes

- Same-agent scoped disposition, not independent human approval.
- Original scientific scope, component unknowns, citations, discussions, history and PROPOSED status preserved.
- PR and separate native merge-group gates remain publication requirements; corrected source retained by review-base/septin-evidence-20261011.
- The predecessor audit included a generic limitation about stoichiometry in this cohort. That sentence concerns the companion septin_complex review, not this band finding, which is solely a grammatical correction; no septin-band copy-number claim was assessed or changed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T135744Z-septin_band-disposition
kind: record
repository: CultureBotAI/CellStructureMech
title: 'septin band: finding disposition'
started_at: '2026-10-11T13:48:13Z'
finished_at: '2026-10-11T13:57:44Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent source and native-record review, not independent
    human approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Exact minor wording finding resolved; original observation and PROPOSED status
  preserved.
source:
  git_revision: 2f27c8dc37863233d1e6c3f8ae966f275c361805
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
  - path: README.md
    sha256: 7354ab3cdd2e80719041752e623b51c95369a7f1463ce3cf615d196448b156ce
    role: context
  - path: curation/source_queue.tsv
    sha256: 55d8fe79b5edd7d6b42bf4ca9168fe4878240417716e2f4ba423489144b89284
    role: context
  - path: data/structures/cytoskeleton/cleavage_apparatus_septin_structure.yaml
    sha256: 07dd82a0f5ad6f6a473e9305c85bf0de6ca336f573878668664e2ee44dbc90e1
    role: context
  - path: data/structures/cytoskeleton/meiotic_septin_complex.yaml
    sha256: 4f10be6c6b32a3c71f43f28570d1eefac729c757657a1a28d29ff41f890aebe9
    role: context
  - path: data/structures/cytoskeleton/mitotic_septin_complex.yaml
    sha256: 99bf85740532379d8f9d88a2f07563cf9853a42e00a367fc5453d598ad308d1e
    role: context
  - path: data/structures/cytoskeleton/prospore_septin_filament_array.yaml
    sha256: 39df294524bcae01b5a3c70410172ac4d19c6fb936a7bf970fda23a043220bfa
    role: context
  - path: data/structures/cytoskeleton/prospore_septin_ring.yaml
    sha256: 56b764eb06dde6d49e5ad5135ab577218f765b63791ffe0483147d4186498da5
    role: context
  - path: data/structures/cytoskeleton/septin_band.yaml
    sha256: 41d269f0b9bd3a3814d8fd2bb5e3e26e933763e1b06c42a30e8b13e20f2865da
    role: target
  - path: data/structures/cytoskeleton/septin_cap.yaml
    sha256: e1da0541d20bb06900ac45fc5af0f71b067add0b7eb153ed277f5e5f05660054
    role: context
  - path: data/structures/cytoskeleton/septin_complex.yaml
    sha256: f78b610e98d1c7ca7e32d91c1aee3505ff4d35026cc6eaf9bd03bd60369a0523
    role: context
  - path: data/structures/cytoskeleton/septin_filament_array.yaml
    sha256: 67445ee5e4546ac3791a3e58c43f1968d3944593039a001be2445f6713fba27e
    role: context
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
  - path: history/records/septin_band/2026-09-30T142319Z-codex-0a6cd1.yaml
    sha256: 4be1b76a4885419ff4717265f3604d9b7ba9c47446410a74bbd87fa42f75a4d7
    role: context
  - path: history/records/septin_band/2026-10-11T134319Z-codex-ed0221.yaml
    sha256: 6e2785a626e8cdb5bd1893f851c0cf0915d7229f69f2539d8bb1555fa4581846
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reports/yaml_record_review/20260930T144307Z-septin_band.md
    sha256: 0513d54587ab9ac182f68679ded22504dcbfbe89c84b6740efbc16d07111f4aa
    role: context
  - path: reports/yaml_record_review/20260930T151303Z-hyphal_septin_band.md
    sha256: ec2af965f78d0e83abe139fb547137890ec639f444739a85bf9be353e27fb84d
    role: context
  - path: reviews/structured/20261011T134159Z-septin_band-audit/review.yaml
    sha256: 8b957e3f43273b8f8ef1df845a789191d11e2e00e598fbe07021e836417184df
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: tests/test_septin_evidence_qualifications.py
    sha256: 349fb7a7b664ecd6064a5bc2a38f1e8b96ff7981205b8236e894d60c8cebc070
    role: context
targets:
- target_id: GO:0032158
  path: data/structures/cytoskeleton/septin_band.yaml
  label: septin band
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_band.yaml
    role: maintained scientific record
scope:
  description: Reassessment of the exact saved finding and preservation, not another
    whole-record review.
  selection: 20261011T134159Z-septin_band-audit
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - GO:0032158
checks:
- check_id: septin_band-schema
  name: septin_band-schema
  status: passed
  required: true
  target_ids:
  - GO:0032158
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/septin_band.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T13:44:18Z to 2026-10-11T13:44:21Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: septin_band-strict
  name: septin_band-strict
  status: passed
  required: true
  target_ids:
  - GO:0032158
  command: .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/septin_band.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T13:44:21Z to 2026-10-11T13:44:28Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: septin_band-snippets
  name: septin_band-snippets
  status: passed
  required: true
  target_ids:
  - GO:0032158
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/cytoskeleton/septin_band.yaml
    --report /private/tmp/csm-review-20261011T133153Z/post-septin_band-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: No verbatim snippets; paraphrases assessed separately against inspected
    text.
  scope_note: 2026-10-11T13:44:28Z to 2026-10-11T13:44:59Z; log SHA-256 25c9d2bb38f6e0db4bdc10d284edd84f3f3cc116a11dbc083f03b5469f0a3885
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:0032158
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T13:44:59Z to 2026-10-11T13:45:18Z; log SHA-256 87f6e0276531bc60d78359853ebfda8bb817f50c271e400d5e94bbdbeb93e2cd
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - GO:0032158
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: "id↔label correspondence summary:\n          OK_CANONICAL: 3544\n     \
    \       OK_SYNONYM: 50\n          OK_EXCEPTION: 6\n    SKIPPED_NO_ADAPTER: 603\n\
    \n✅ All id↔label pairs correspond."
  scope_note: 2026-10-11T13:45:18Z to 2026-10-11T13:46:54Z; log SHA-256 d423103555a6a5b538a7c811a73a29c24ed0e5a2eae00d1bb94715295f23f7cb
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - GO:0032158
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T13:46:54Z to 2026-10-11T13:47:15Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - GO:0032158
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: "resolver control: every resolver accepts a known id and rejects a fabricated\
    \ one\n\nidentifier liveness summary:\n  OK             4014\n  SKIPPED      \
    \   251\n\nEvery identifier resolves at its issuing authority."
  scope_note: 2026-10-11T13:47:15Z to 2026-10-11T13:48:02Z; log SHA-256 ee1c5f2e78a2d29fcb6781a8ecd722934376595042d2cc261b4465b361d19b79
- check_id: focused
  name: focused
  status: passed
  required: true
  target_ids:
  - GO:0032158
  command: .venv/bin/python -m pytest -q tests/test_septin_evidence_qualifications.py
    tests/test_write_validated.py
  exit_code: 0
  expected_exit_code: 0
  summary: '...........................                                              [100%]

    27 passed in 35.88s'
  scope_note: 2026-10-11T13:48:02Z to 2026-10-11T13:48:39Z; log SHA-256 0081c64b573a881cc1b0c645cd72feb2fc7506b9e1d3604ee16df1a2b2f7edc1
- check_id: reviews
  name: reviews
  status: passed
  required: true
  target_ids:
  - GO:0032158
  command: .venv/bin/python scripts/record_review.py check --base 739bbe42dc53bc9473099554ddcf6f34e0a9c283
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T13:48:39Z to 2026-10-11T13:50:02Z; log SHA-256 42258e07e083ddb0b7b113f9152a7318323794f0706db3b3f93c85c4750a9916
- check_id: diff
  name: diff
  status: passed
  required: true
  target_ids:
  - GO:0032158
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T13:50:02Z to 2026-10-11T13:50:02Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- check_id: release-qc
  name: release-qc
  status: passed
  required: true
  target_ids:
  - GO:0032158
  command: .venv/bin/python scripts/run_qc.py
  exit_code: 0
  expected_exit_code: 0
  summary: 'Full local QC passed: 861 passed, 3 skipped in 541.83s (0:09:01). PR and
    native merge-group gates remain separate.'
  scope_note: 2026-10-11T13:45:51Z to 2026-10-11T13:57:32Z; log SHA-256 77d0e58929e44f121737c7e2fea5cca649bd9e94aee479877ac09ab13b50a6dc
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/septin_band.yaml
  accessed_at: '2026-10-11T13:57:44Z'
  snapshot_sha256: 41d269f0b9bd3a3814d8fd2bb5e3e26e933763e1b06c42a30e8b13e20f2865da
  support: context_only
  summary: Entire corrected native YAML reread; only finding field and appended curation
    event changed.
- evidence_id: rules
  kind: record_content
  reference: docs/CURATION.md
  accessed_at: '2026-10-11T13:41:59Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  support: context_only
  summary: Keep source support at the narrowest claim and preserve uncertainty.
- evidence_id: history
  kind: record_content
  reference: /private/tmp/csm-review-20261011T133153Z/septin_band-discussion-history.json
  accessed_at: '2026-10-11T13:41:59Z'
  snapshot_sha256: 78c1bf7e47fb24f793cdbfeafe77a1bd35a6668c90fdb9013e1cb666cb6eacb9
  support: context_only
  summary: Committed discussion and event versions inspected; existing rationale and
    dates retained.
- evidence_id: append-history-0
  kind: record_content
  reference: history/records/septin_band/2026-09-30T142319Z-codex-0a6cd1.yaml
  accessed_at: '2026-10-11T13:41:59Z'
  snapshot_sha256: 4be1b76a4885419ff4717265f3604d9b7ba9c47446410a74bbd87fa42f75a4d7
  support: context_only
  summary: Existing append-only history inspected, including legacy actor metadata;
    not rewritten.
- evidence_id: predecessors
  kind: validation
  reference: /private/tmp/csm-review-20261011T133153Z/exact-target-predecessors.json
  accessed_at: '2026-10-11T13:41:59Z'
  snapshot_sha256: 21185dfdca86c41ba34542d206b58c0eca5fc7947f33b0d528236b7e0661201b
  support: context_only
  summary: Ignored-inclusive canonical scan found no exact-target predecessor.
- evidence_id: issue-search
  kind: validation
  reference: /private/tmp/csm-review-20261011T133153Z/septin-issues.log
  accessed_at: '2026-10-11T13:41:59Z'
  snapshot_sha256: 73c4d8f6bf30349a992e3c7230a996a3309e844b6870c97a98e33221161545ac
  support: context_only
  summary: 'All-state septin search inspected: 24 closed issues, including prior evidence
    changes. No existing issue for either exact new defect.'
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/csm-review-20261011T133153Z/adapter.log
  accessed_at: '2026-10-11T13:41:59Z'
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
  support: context_only
  summary: Live 28-dataset inventory has no matching fungal dataset. Not negative
    biological evidence.
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000144,GO:0005856,GO:0005938,GO:0005940,GO:0031105,GO:0032151,GO:0032152,GO:0032153,GO:0032156,GO:0032158,GO:0032159,GO:0032160,GO:0032161,GO:0032162,GO:0032163,GO:0032164,GO:0032165,GO:0032166,GO:0032168,GO:0032169,GO:0032170,GO:0032171,GO:0032172,GO:0032173,GO:0032174,GO:0032177,GO:0032991,GO:0036391,GO:0110165
  locator: Exact term definitions, labels, obsolescence and typed child relations
    for the septin cohort
  accessed_at: '2026-10-11T13:34:39Z'
  snapshot_sha256: 6abfcd4ea6461b228555d26f22ba40c28e0f3e68800bd57d3eb6dc5fb1a8b8b4
  support: supports
  summary: Identity and hierarchy are supported. GO:0032158 itself contains the grown
    typo; local prose can correct spelling without changing source identity.
- evidence_id: legacy
  kind: prior_review
  reference: reports/yaml_record_review/20260930T144307Z-septin_band.md
  accessed_at: '2026-10-11T13:41:59Z'
  snapshot_sha256: 0513d54587ab9ac182f68679ded22504dcbfbe89c84b6740efbc16d07111f4aa
  support: context_only
  summary: Earlier clean review checked GO correspondence; original review preserved.
- evidence_id: predecessor
  kind: prior_review
  reference: reviews/structured/20261011T134159Z-septin_band-audit/review.yaml
  accessed_at: '2026-10-11T13:57:44Z'
  snapshot_sha256: 8b957e3f43273b8f8ef1df845a789191d11e2e00e598fbe07021e836417184df
  support: context_only
  summary: Immutable observation committed before scientific mutation.
- evidence_id: preservation
  kind: validation
  reference: /private/tmp/csm-review-20261011T133153Z/preservation.json
  accessed_at: '2026-10-11T13:57:44Z'
  snapshot_sha256: 95153d4cbf01733b652745a68461282f631af06d012dbeaafcfe1f1cf5cbd76f
  support: context_only
  summary: 907 other native records, 908 semantic vectors and all old review/history/legacy
    bytes preserved.
- evidence_id: red
  kind: validation
  reference: /private/tmp/csm-review-20261011T133153Z/regressions-red.log
  accessed_at: '2026-10-11T13:57:44Z'
  snapshot_sha256: 088f4a4ce352e2a42edcfc2af6f8791bb109b25578faa754689250c1cd1e10e5
  support: context_only
  summary: Two focused regressions fail on original records; identity control passes.
- evidence_id: green
  kind: validation
  reference: /private/tmp/csm-review-20261011T133153Z/post-focused.log
  accessed_at: '2026-10-11T13:57:44Z'
  snapshot_sha256: 0081c64b573a881cc1b0c645cd72feb2fc7506b9e1d3604ee16df1a2b2f7edc1
  support: context_only
  summary: Focused regressions and guarded-writer tests pass after correction.
- evidence_id: edit-history
  kind: record_content
  reference: history/records/septin_band/2026-10-11T134319Z-codex-ed0221.yaml
  accessed_at: '2026-10-11T13:57:44Z'
  snapshot_sha256: 6e2785a626e8cdb5bd1893f851c0cf0915d7229f69f2539d8bb1555fa4581846
  support: context_only
  summary: Actual append-only Codex EDIT links the issue and saved finding.
assessments:
- assessment_id: resolved
  area: evidence
  topic: Correct polarized grown to polarized growth
  outcome: supported
  target_ids:
  - GO:0032158
  evidence_ids:
  - record
  - go
  - rules
  - predecessor
  - preservation
  - red
  - green
  - edit-history
  summary: Definition now uses polarized growth; all other definition words, GO source,
    topology and scope remain unchanged.
findings:
- finding_id: F1
  issue_key: septin-band-polarized-growth-wording
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: Correct polarized grown to polarized growth
  description: Definition now uses polarized growth; all other definition words, GO
    source, topology and scope remain unchanged.
  target_ids:
  - GO:0032158
  field_paths:
  - definition
  evidence_ids:
  - record
  - go
  - rules
  - predecessor
  - preservation
  - red
  - green
  - edit-history
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_band.yaml
    role: maintained scientific record
  rule_id: docs/record-reviews.md#verdict-and-severity
  native_severity: minor
  normalization_reason: Bounded wording correction. The proposed stoichiometry remains
    plausible and identity is sound; the grammar defect does not alter biological
    scope.
  disposition_reason: Definition now uses polarized growth; all other definition words,
    GO source, topology and scope remain unchanged. Verified against inspected source,
    bounded diff, red/green tests and full local QC.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261011T134159Z-septin_band-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2216
actions: []
limitations:
- Same-agent scoped disposition, not independent human approval.
- Original scientific scope, component unknowns, citations, discussions, history and
  PROPOSED status preserved.
- PR and separate native merge-group gates remain publication requirements; corrected
  source retained by review-base/septin-evidence-20261011.
- The predecessor audit included a generic limitation about stoichiometry in this
  cohort. That sentence concerns the companion septin_complex review, not this band
  finding, which is solely a grammatical correction; no septin-band copy-number claim
  was assessed or changed.
links:
- https://github.com/CultureBotAI/CellStructureMech/issues/2216
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261011T134159Z-septin_band-audit
  relationship: Resolves exact predecessor without replacing it.
```
