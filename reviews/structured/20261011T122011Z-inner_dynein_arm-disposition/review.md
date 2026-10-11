# inner dynein arm: composition finding disposition

- Review: 20261011T122011Z-inner_dynein_arm-disposition
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T12:06:41Z
- Finished UTC: 2026-10-11T12:20:11Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Exact predecessor minor finding resolved; original observation and PROPOSED status preserved.

## Scope And Provenance

Reassessment of the saved finding and surrounding-claim preservation, not another whole-record review.

Selection: 20261011T120358Z-inner_dynein_arm-audit
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7679d7440fbf356c46fa535bb1705ac9d543ab4c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0036156 | data/structures/cytoskeleton/inner_dynein_arm.yaml | maintained | inner dynein arm |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| inner_dynein_arm-schema | passed | True | GO:0036156 | Actual deterministic check passed; scientific support assessed separately. |
| inner_dynein_arm-strict | passed | True | GO:0036156 | Actual deterministic check passed; scientific support assessed separately. |
| inner_dynein_arm-snippets | passed | True | GO:0036156 | No verbatim snippets; paraphrases assessed separately against inspected text. |
| history | passed | True | GO:0036156 | Actual deterministic check passed; scientific support assessed separately. |
| labels | passed | True | GO:0036156 | id↔label correspondence summary:<br>          OK_CANONICAL: 3544<br>            OK_SYNONYM: 50<br>          OK_EXCEPTION: 6<br>    SKIPPED_NO_ADAPTER: 603<br><br>✅ All id↔label pairs correspond. |
| traits | passed | True | GO:0036156 | Actual deterministic check passed; scientific support assessed separately. |
| curies | passed | True | GO:0036156 | resolver control: every resolver accepts a known id and rejects a fabricated one<br><br>identifier liveness summary:<br>  OK             4014<br>  SKIPPED         251<br><br>Every identifier resolves at its issuing authority. |
| focused | passed | True | GO:0036156 | ............................                                             [100%]<br>28 passed in 54.92s |
| reviews | passed | True | GO:0036156 | Actual deterministic check passed; scientific support assessed separately. |
| diff | passed | True | GO:0036156 | Actual deterministic check passed; scientific support assessed separately. |
| release-qc | passed | True | GO:0036156 | Full local QC passed: 855 passed, 3 skipped in 616.64s (0:10:16). PR and native merge-group gates remain separate. |

## Scientific And Domain Assessments

### Align inner-arm description with the corrected parthood edge

evidence: supported. Targets: GO:0036156.

Graph description now calls heavy chains motor-chain constituents, agreeing with the existing parthood edge and preserving unresolved accessory-subunit scope.

## Findings

### F1: Align inner-arm description with the corrected parthood edge

minor / resolved / confirmed; issue key: inner-dynein-arm-residual-assembly-description.

Graph description now calls heavy chains motor-chain constituents, agreeing with the existing parthood edge and preserving unresolved accessory-subunit scope.

Disposition: Graph description now calls heavy chains motor-chain constituents, agreeing with the existing parthood edge and preserving unresolved accessory-subunit scope. Verified against exact GO definitions, primary structural context, bounded diff, red/green regressions and full local QC.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/inner_dynein_arm.yaml | context_only | Corrected entire native record reread; only graph semantics and appended event changed. |
| rules | docs/CURATION.md | context_only | Evidence must support the narrowest claim and graph relation; unknown component details need not be invented. |
| history | /private/tmp/csm-review-20261011T115516Z/inner_dynein_arm-discussion-history.json | context_only | All committed discussion and inline-event versions inspected; original rationale and dates retained. |
| append-history-0 | history/records/inner_dynein_arm/2026-09-23T104741Z-codex-0e0359.yaml | context_only | Original CREATE/review history and actor metadata inspected. |
| append-history-1 | history/records/inner_dynein_arm/2026-09-23T105609Z-codex-ca8b08.yaml | context_only | Original CREATE/review history and actor metadata inspected. |
| prior-issues | /private/tmp/csm-review-20261011T115516Z/inner-prior-issue.log | context_only | Closed issue 1385 corrected the inner-arm edge to static parthood; its description was not updated. This is context, not a canonical predecessor. |
| issue-search | /private/tmp/csm-review-20261011T115516Z/dynein-all-issues.log | context_only | All-state dynein issue search checked before creating findings. |
| predecessors | /private/tmp/csm-review-20261011T115516Z/exact-target-predecessors.json | context_only | Ignored-inclusive canonical scan found no exact-target predecessor. |
| adapter | /private/tmp/csm-review-20261011T115516Z/adapter.log | context_only | No Chlamydomonas coverage in the live 28-dataset iModulonDB inventory; not negative biological evidence. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005858,GO:0005879,GO:0005930,GO:0036156,GO:0036157,GO:0051012,GO:0097540,GO:1990717,GO:1990719,GO:1990720; Exact dynein-arm/axonemal-dynein definitions, typed is_a and part_of relations, microtubule-sliding identity | supports | The arm terms describe constituent chains and location. They do not supply an assembly pathway or establish individual chain cohorts as sufficient assembly inputs. |
| taxon | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055; TaxId 3055 scientificName and species rank | supports | Chlamydomonas reinhardtii identity verified; species prevalence is assessed from structural context, not taxonomy. |
| paper-id | DOI:10.1126/science.1128618; Exact DOI, PMID 16917055, title and primary abstract | supports | Nicastro et al. 2006 publication identity verified. |
| primary-text | DOI:10.1126/science.1128618; Author-uploaded full text: https://www.researchgate.net/publication/6871150_The_Molecular_Architecture_of_Axonemes_Revealed_by_Cryoelectron_Tomography ; introduction, specimen paragraph, dynein-position section, IDA organization section, Figures 1/3 captions | supports | Inspected actual article text supports Chlamydomonas arm location, motor-chain membership and sliding-force context. Structural observations and a motility model are not direct tests of how individual chain cohorts assemble a complete arm. |
| predecessor | reviews/structured/20261011T120358Z-inner_dynein_arm-audit/review.yaml | context_only | Immutable observation committed before scientific edits. |
| preservation | /private/tmp/csm-review-20261011T115516Z/preservation.json | context_only | All 907 other native records and old history/review/legacy bytes preserved; semantic embeddings unchanged. |
| red-tests | /private/tmp/csm-review-20261011T115516Z/regressions-red.log | context_only | Three new regressions failed on baseline; inner-arm parthood control passed. |
| green-tests | /private/tmp/csm-review-20261011T115516Z/post-focused.log | context_only | All focused regressions and guarded-writer tests pass. |
| edit-history | history/records/inner_dynein_arm/2026-10-11T120441Z-codex-ca9e0e.yaml | context_only | New append-only Codex EDIT links issue and original saved observation. |

## Limits And Additional Notes

- Same-agent disposition, not independent human approval or a repeated whole-record review.
- Static membership is not a new assembly mechanism; no protein identities, stoichiometry or raw experimental evidence inferred.
- Existing resolver/label namespace skips and three empty-parameter test skips remain explicit.
- Exact corrected source retained by review-base/dynein-composition-evidence-20261011; PR and native merge-group checks remain separate publication gates.
- Two C1/C2 records have separate clean coverage accounting and no review-output records.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T122011Z-inner_dynein_arm-disposition
kind: record
repository: CultureBotAI/CellStructureMech
title: 'inner dynein arm: composition finding disposition'
started_at: '2026-10-11T12:06:41Z'
finished_at: '2026-10-11T12:20:11Z'
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
summary: Exact predecessor minor finding resolved; original observation and PROPOSED
  status preserved.
source:
  git_revision: 7679d7440fbf356c46fa535bb1705ac9d543ab4c
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
  - path: data/structures/cytoskeleton/axonemal_dynein_complex.yaml
    sha256: 9158b3b827892de2d3f14320353af5fbd6ef8ef3cfae114687b9e6725f7ce44e
    role: context
  - path: data/structures/cytoskeleton/axoneme.yaml
    sha256: 0b91b4cd41d1a34bdc3883d988f31009effc74347b881cdc5c9b66014704e223
    role: context
  - path: data/structures/cytoskeleton/c1_axonemal_microtubule.yaml
    sha256: 2f4f420d4958d3133a60a7b072e517361d7c2c4908acb4e307bd2033095f18f4
    role: context
  - path: data/structures/cytoskeleton/c2_axonemal_microtubule.yaml
    sha256: 97c8666ddef318d146a2d902a225f8b0313468bcf54fa32d81d5f1d127798a44
    role: context
  - path: data/structures/cytoskeleton/inner_dynein_arm.yaml
    sha256: 53971a43a2eb2cd74132e0a1f8fee55699f20cff7ea8a4280cda3c50ccf4fbb2
    role: target
  - path: data/structures/cytoskeleton/outer_dynein_arm.yaml
    sha256: 2cd61e50ae013bea6061a72163ca507e7d97c7b497ef261fbbc15f90a7c66541
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
  - path: history/records/inner_dynein_arm/2026-09-23T104741Z-codex-0e0359.yaml
    sha256: 9fa6825759452885f392d9409c918f68740dcbd1e95cffe62e4dd9f42b255956
    role: context
  - path: history/records/inner_dynein_arm/2026-09-23T105609Z-codex-ca8b08.yaml
    sha256: c30f8a85356b86c6f66f2276c6b60d48d2da178f8a21811aeb509e7e2c954e4c
    role: context
  - path: history/records/inner_dynein_arm/2026-10-11T120441Z-codex-ca9e0e.yaml
    sha256: 066a5904ea448258d066e40c4ec030d1f9767fd22f19c60a9a57df96c88308dc
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reviews/structured/20261011T120358Z-inner_dynein_arm-audit/review.yaml
    sha256: 576a4a85a5585364c984555bd46643f9fe40b4fe2d8da066d5e184bbf255207b
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: tests/test_dynein_composition_scope.py
    sha256: 8311ede7a84b028dbf11c7829dfdd8464573fa0de653baf6755ea7d50e800415
    role: context
targets:
- target_id: GO:0036156
  path: data/structures/cytoskeleton/inner_dynein_arm.yaml
  label: inner dynein arm
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/inner_dynein_arm.yaml
    role: maintained scientific record
scope:
  description: Reassessment of the saved finding and surrounding-claim preservation,
    not another whole-record review.
  selection: 20261011T120358Z-inner_dynein_arm-audit
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - GO:0036156
checks:
- check_id: inner_dynein_arm-schema
  name: inner_dynein_arm-schema
  status: passed
  required: true
  target_ids:
  - GO:0036156
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/inner_dynein_arm.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T12:04:57Z to 2026-10-11T12:04:59Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: inner_dynein_arm-strict
  name: inner_dynein_arm-strict
  status: passed
  required: true
  target_ids:
  - GO:0036156
  command: .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/inner_dynein_arm.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T12:04:59Z to 2026-10-11T12:05:03Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: inner_dynein_arm-snippets
  name: inner_dynein_arm-snippets
  status: passed
  required: true
  target_ids:
  - GO:0036156
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/cytoskeleton/inner_dynein_arm.yaml
    --report /private/tmp/csm-review-20261011T115516Z/inner_dynein_arm-post-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: No verbatim snippets; paraphrases assessed separately against inspected
    text.
  scope_note: 2026-10-11T12:05:03Z to 2026-10-11T12:05:24Z; log SHA-256 76a62fd5ec31e6ba130825b4a29c72af0af9ccf523b06b12b351759481bf488c
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:0036156
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T12:05:55Z to 2026-10-11T12:06:11Z; log SHA-256 e002f7ee670d93f9ac79e90f87c45b6741dfd42a7e96f25c08bbe5bdf4bebe56
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - GO:0036156
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: "id↔label correspondence summary:\n          OK_CANONICAL: 3544\n     \
    \       OK_SYNONYM: 50\n          OK_EXCEPTION: 6\n    SKIPPED_NO_ADAPTER: 603\n\
    \n✅ All id↔label pairs correspond."
  scope_note: 2026-10-11T12:06:11Z to 2026-10-11T12:08:33Z; log SHA-256 d423103555a6a5b538a7c811a73a29c24ed0e5a2eae00d1bb94715295f23f7cb
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - GO:0036156
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T12:08:33Z to 2026-10-11T12:09:03Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - GO:0036156
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: "resolver control: every resolver accepts a known id and rejects a fabricated\
    \ one\n\nidentifier liveness summary:\n  OK             4014\n  SKIPPED      \
    \   251\n\nEvery identifier resolves at its issuing authority."
  scope_note: 2026-10-11T12:09:03Z to 2026-10-11T12:10:03Z; log SHA-256 ee1c5f2e78a2d29fcb6781a8ecd722934376595042d2cc261b4465b361d19b79
- check_id: focused
  name: focused
  status: passed
  required: true
  target_ids:
  - GO:0036156
  command: .venv/bin/python -m pytest -q tests/test_dynein_composition_scope.py tests/test_write_validated.py
  exit_code: 0
  expected_exit_code: 0
  summary: '............................                                             [100%]

    28 passed in 54.92s'
  scope_note: 2026-10-11T12:10:03Z to 2026-10-11T12:10:59Z; log SHA-256 0e8b8d3f16727ebf26d56191240e57039a027e466180ac7a5b071575d34e99fa
- check_id: reviews
  name: reviews
  status: passed
  required: true
  target_ids:
  - GO:0036156
  command: .venv/bin/python scripts/record_review.py check --base b8492a0b5913cd3301bb30b1c261a9d3f3759574
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T12:10:59Z to 2026-10-11T12:12:56Z; log SHA-256 a24375f0ce722d8a505ea8f41c36ca1df1845750ceb725dd4b057aee502ad6f7
- check_id: diff
  name: diff
  status: passed
  required: true
  target_ids:
  - GO:0036156
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T12:12:56Z to 2026-10-11T12:12:56Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- check_id: release-qc
  name: release-qc
  status: passed
  required: true
  target_ids:
  - GO:0036156
  command: .venv/bin/python scripts/run_qc.py
  exit_code: 0
  expected_exit_code: 0
  summary: 'Full local QC passed: 855 passed, 3 skipped in 616.64s (0:10:16). PR and
    native merge-group gates remain separate.'
  scope_note: 2026-10-11T12:06:12Z to 2026-10-11T12:19:55Z; log SHA-256 f98135646a1433a18027a34be9e8a2de6b6a26828f8aa5760c8ef5725c526d6f
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/inner_dynein_arm.yaml
  accessed_at: '2026-10-11T12:20:11Z'
  snapshot_sha256: 53971a43a2eb2cd74132e0a1f8fee55699f20cff7ea8a4280cda3c50ccf4fbb2
  support: context_only
  summary: Corrected entire native record reread; only graph semantics and appended
    event changed.
- evidence_id: rules
  kind: record_content
  reference: docs/CURATION.md
  accessed_at: '2026-10-11T12:03:58Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  support: context_only
  summary: Evidence must support the narrowest claim and graph relation; unknown component
    details need not be invented.
- evidence_id: history
  kind: record_content
  reference: /private/tmp/csm-review-20261011T115516Z/inner_dynein_arm-discussion-history.json
  accessed_at: '2026-10-11T12:03:58Z'
  snapshot_sha256: 3a8b058818f3e60bd80b64dc2c553529adeb368052a0d875a50a97cd44c23a33
  support: context_only
  summary: All committed discussion and inline-event versions inspected; original
    rationale and dates retained.
- evidence_id: append-history-0
  kind: record_content
  reference: history/records/inner_dynein_arm/2026-09-23T104741Z-codex-0e0359.yaml
  accessed_at: '2026-10-11T12:03:58Z'
  snapshot_sha256: 9fa6825759452885f392d9409c918f68740dcbd1e95cffe62e4dd9f42b255956
  support: context_only
  summary: Original CREATE/review history and actor metadata inspected.
- evidence_id: append-history-1
  kind: record_content
  reference: history/records/inner_dynein_arm/2026-09-23T105609Z-codex-ca8b08.yaml
  accessed_at: '2026-10-11T12:03:58Z'
  snapshot_sha256: c30f8a85356b86c6f66f2276c6b60d48d2da178f8a21811aeb509e7e2c954e4c
  support: context_only
  summary: Original CREATE/review history and actor metadata inspected.
- evidence_id: prior-issues
  kind: prior_review
  reference: /private/tmp/csm-review-20261011T115516Z/inner-prior-issue.log
  accessed_at: '2026-10-11T12:03:58Z'
  snapshot_sha256: db61b08dd2957e419bca1afd1698aca12a135b994ec840bb70bbbd1c31af21b5
  support: context_only
  summary: Closed issue 1385 corrected the inner-arm edge to static parthood; its
    description was not updated. This is context, not a canonical predecessor.
- evidence_id: issue-search
  kind: validation
  reference: /private/tmp/csm-review-20261011T115516Z/dynein-all-issues.log
  accessed_at: '2026-10-11T12:03:58Z'
  snapshot_sha256: e7c74f0c2811a0f7bbae786e748b462cfeb45735ccd20135723acad6c51e55dd
  support: context_only
  summary: All-state dynein issue search checked before creating findings.
- evidence_id: predecessors
  kind: validation
  reference: /private/tmp/csm-review-20261011T115516Z/exact-target-predecessors.json
  accessed_at: '2026-10-11T12:03:58Z'
  snapshot_sha256: 186da3531c676cf51472a73accb334683dda8283ac5f1e6c4ff62145aa1955d6
  support: context_only
  summary: Ignored-inclusive canonical scan found no exact-target predecessor.
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/csm-review-20261011T115516Z/adapter.log
  accessed_at: '2026-10-11T12:03:58Z'
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
  support: context_only
  summary: No Chlamydomonas coverage in the live 28-dataset iModulonDB inventory;
    not negative biological evidence.
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005858,GO:0005879,GO:0005930,GO:0036156,GO:0036157,GO:0051012,GO:0097540,GO:1990717,GO:1990719,GO:1990720
  locator: Exact dynein-arm/axonemal-dynein definitions, typed is_a and part_of relations,
    microtubule-sliding identity
  accessed_at: '2026-10-11T11:56:47Z'
  snapshot_sha256: 46cf9606bf3ed226a1d3d55b65c11f8b510cd14b644607267d1e4b898b802baa
  support: supports
  summary: The arm terms describe constituent chains and location. They do not supply
    an assembly pathway or establish individual chain cohorts as sufficient assembly
    inputs.
- evidence_id: taxon
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055
  locator: TaxId 3055 scientificName and species rank
  accessed_at: '2026-10-11T11:56:48Z'
  snapshot_sha256: e3861fe6706cefe2e079e15c0178a65e95efaad3890f548f25e721553eaa93a0
  support: supports
  summary: Chlamydomonas reinhardtii identity verified; species prevalence is assessed
    from structural context, not taxonomy.
- evidence_id: paper-id
  kind: primary_source
  reference: DOI:10.1126/science.1128618
  locator: Exact DOI, PMID 16917055, title and primary abstract
  accessed_at: '2026-10-11T11:56:20Z'
  snapshot_sha256: d770ed57ab44095ac4a836cb572e8c5f510cbe41ea00f2237bda26bfe6e7b991
  support: supports
  summary: Nicastro et al. 2006 publication identity verified.
- evidence_id: primary-text
  kind: primary_source
  reference: DOI:10.1126/science.1128618
  locator: 'Author-uploaded full text: https://www.researchgate.net/publication/6871150_The_Molecular_Architecture_of_Axonemes_Revealed_by_Cryoelectron_Tomography
    ; introduction, specimen paragraph, dynein-position section, IDA organization
    section, Figures 1/3 captions'
  accessed_at: '2026-10-11T12:03:58Z'
  support: supports
  summary: Inspected actual article text supports Chlamydomonas arm location, motor-chain
    membership and sliding-force context. Structural observations and a motility model
    are not direct tests of how individual chain cohorts assemble a complete arm.
- evidence_id: predecessor
  kind: prior_review
  reference: reviews/structured/20261011T120358Z-inner_dynein_arm-audit/review.yaml
  accessed_at: '2026-10-11T12:20:11Z'
  snapshot_sha256: 576a4a85a5585364c984555bd46643f9fe40b4fe2d8da066d5e184bbf255207b
  support: context_only
  summary: Immutable observation committed before scientific edits.
- evidence_id: preservation
  kind: validation
  reference: /private/tmp/csm-review-20261011T115516Z/preservation.json
  accessed_at: '2026-10-11T12:20:11Z'
  snapshot_sha256: 69ea6c5df73c81c097cfb67fc4f4a6869376b28c301497fcd96203917ad9fb77
  support: context_only
  summary: All 907 other native records and old history/review/legacy bytes preserved;
    semantic embeddings unchanged.
- evidence_id: red-tests
  kind: validation
  reference: /private/tmp/csm-review-20261011T115516Z/regressions-red.log
  accessed_at: '2026-10-11T12:20:11Z'
  snapshot_sha256: ede926ecd6fc13c2504b64e6982ba254b0dae701cc859f4ab0e8264699f98750
  support: context_only
  summary: Three new regressions failed on baseline; inner-arm parthood control passed.
- evidence_id: green-tests
  kind: validation
  reference: /private/tmp/csm-review-20261011T115516Z/post-focused.log
  accessed_at: '2026-10-11T12:20:11Z'
  snapshot_sha256: 0e8b8d3f16727ebf26d56191240e57039a027e466180ac7a5b071575d34e99fa
  support: context_only
  summary: All focused regressions and guarded-writer tests pass.
- evidence_id: edit-history
  kind: record_content
  reference: history/records/inner_dynein_arm/2026-10-11T120441Z-codex-ca9e0e.yaml
  accessed_at: '2026-10-11T12:20:11Z'
  snapshot_sha256: 066a5904ea448258d066e40c4ec030d1f9767fd22f19c60a9a57df96c88308dc
  support: context_only
  summary: New append-only Codex EDIT links issue and original saved observation.
assessments:
- assessment_id: resolved
  area: evidence
  topic: Align inner-arm description with the corrected parthood edge
  outcome: supported
  target_ids:
  - GO:0036156
  evidence_ids:
  - record
  - go
  - primary-text
  - prior-issues
  - rules
  - predecessor
  - preservation
  - red-tests
  - green-tests
  - edit-history
  summary: Graph description now calls heavy chains motor-chain constituents, agreeing
    with the existing parthood edge and preserving unresolved accessory-subunit scope.
findings:
- finding_id: F1
  issue_key: inner-dynein-arm-residual-assembly-description
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: Align inner-arm description with the corrected parthood edge
  description: Graph description now calls heavy chains motor-chain constituents,
    agreeing with the existing parthood edge and preserving unresolved accessory-subunit
    scope.
  target_ids:
  - GO:0036156
  field_paths:
  - causal_graphs[0].description
  evidence_ids:
  - record
  - go
  - primary-text
  - prior-issues
  - rules
  - predecessor
  - preservation
  - red-tests
  - green-tests
  - edit-history
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/inner_dynein_arm.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: minor
  normalization_reason: Bounded predicate/description overstatement in a coarse nonmechanistic
    graph. Identity, constituent membership and motor function remain supported; no
    false protein identity or universal mechanism is established.
  disposition_reason: Graph description now calls heavy chains motor-chain constituents,
    agreeing with the existing parthood edge and preserving unresolved accessory-subunit
    scope. Verified against exact GO definitions, primary structural context, bounded
    diff, red/green regressions and full local QC.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261011T120358Z-inner_dynein_arm-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2210
actions: []
limitations:
- Same-agent disposition, not independent human approval or a repeated whole-record
  review.
- Static membership is not a new assembly mechanism; no protein identities, stoichiometry
  or raw experimental evidence inferred.
- Existing resolver/label namespace skips and three empty-parameter test skips remain
  explicit.
- Exact corrected source retained by review-base/dynein-composition-evidence-20261011;
  PR and native merge-group checks remain separate publication gates.
- Two C1/C2 records have separate clean coverage accounting and no review-output records.
links:
- https://github.com/CultureBotAI/CellStructureMech/issues/2210
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261011T120358Z-inner_dynein_arm-audit
  relationship: Resolves exact predecessor without replacing it.
```
