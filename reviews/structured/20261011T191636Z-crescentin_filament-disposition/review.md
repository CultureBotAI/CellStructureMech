# crescentin filament: finding dispositions

- Review: 20261011T191636Z-crescentin_filament-disposition
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T19:15:57Z
- Finished UTC: 2026-10-11T19:16:36Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Exact saved findings resolved; original observations and surrounding biological scope preserved.

## Scope And Provenance

Exact findings and surrounding-claim preservation, not a repeated whole-record review.

Selection: 20261011T185011Z-crescentin_filament-audit
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 829a2018bbe5e2dcb41b3f9f8d24fdea017addf8.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:crescentin_filament | data/structures/cytoskeleton/crescentin_filament.yaml | maintained | crescentin filament |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| crescentin_filament-schema | passed | True | cellstructuremech:crescentin_filament | Actual deterministic check passed; scientific support assessed separately. |
| crescentin_filament-strict | passed | True | cellstructuremech:crescentin_filament | Actual deterministic check passed; scientific support assessed separately. |
| crescentin_filament-snippets | passed | True | cellstructuremech:crescentin_filament | No verbatim snippets; paraphrases assessed separately against inspected text. |
| history | passed | True | cellstructuremech:crescentin_filament | Actual deterministic check passed; scientific support assessed separately. |
| labels | passed | True | cellstructuremech:crescentin_filament | id↔label correspondence summary:<br>          OK_CANONICAL: 3544<br>            OK_SYNONYM: 50<br>          OK_EXCEPTION: 6<br>    SKIPPED_NO_ADAPTER: 603<br><br>✅ All id↔label pairs correspond. |
| traits | passed | True | cellstructuremech:crescentin_filament | Actual deterministic check passed; scientific support assessed separately. |
| curies | passed | True | cellstructuremech:crescentin_filament | resolver control: every resolver accepts a known id and rejects a fabricated one<br>resolving 2 DOI identifier(s)...<br><br>identifier liveness summary:<br>  OK             4015<br>  SKIPPED         251<br><br>Every identifier resolves at its issuing authority. |
| focused | passed | True | cellstructuremech:crescentin_filament | ............................................                             [100%]<br>44 passed in 33.92s |
| reviews | passed | True | cellstructuremech:crescentin_filament | Actual deterministic check passed; scientific support assessed separately. |
| diff | passed | True | cellstructuremech:crescentin_filament | Actual deterministic check passed; scientific support assessed separately. |
| release-qc | passed | True | cellstructuremech:crescentin_filament | Full local QC passed: 917 passed, 3 skipped in 495.64s (0:08:15). PR and native merge-group gates remain separate. |

## Scientific And Domain Assessments

### Correct cytoskeleton is-a versus parthood

evidence: supported. Targets: cellstructuremech:crescentin_filament.

The individual filament now has GO:0099513 as broader parent and GO:0005856 as containing cytoskeleton part_of, with exact authority context.

### Correct the Woldemeskel and Goley publication year

evidence: supported. Targets: cellstructuremech:crescentin_filament.

Corrected four active evidence notes to 2017 and appended an explicit correction discussion. Original #1260 curation history, DOI, biology and graph relations are preserved.

## Findings

### F1: Correct cytoskeleton is-a versus parthood

major / resolved / confirmed; issue key: crescentin-filament-cytoskeleton-is-a.

The individual filament now has GO:0099513 as broader parent and GO:0005856 as containing cytoskeleton part_of, with exact authority context.

Disposition: The individual filament now has GO:0099513 as broader parent and GO:0005856 as containing cytoskeleton part_of, with exact authority context. Verified by source inspection, bounded diff, red/green regressions and local full QC.

### F2: Correct the Woldemeskel and Goley publication year

minor / resolved / confirmed; issue key: crescentin-filament-woldemeskel-publication-year.

Corrected four active evidence notes to 2017 and appended an explicit correction discussion. Original #1260 curation history, DOI, biology and graph relations are preserved.

Disposition: Corrected four active evidence notes to 2017 and appended an explicit correction discussion. Original #1260 curation history, DOI, biology and graph relations are preserved. Verified by source inspection, bounded diff, red/green regressions and local full QC.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/crescentin_filament.yaml | context_only | Corrected entire native YAML reinspected against source and original. |
| rules | docs/CURATION.md | context_only | Fiber is-a versus containing cytoskeleton part_of; narrow claim-local evidence. |
| schema | docs/SCHEMA.md | context_only | Hierarchy and parthood field contracts. |
| history | /private/tmp/csm-review-20261011T183112Z/crescentin_filament-discussion-history.json | context_only | All committed discussion/inline-history versions inspected. |
| predecessors | /private/tmp/csm-review-20261011T183112Z/exact-target-predecessors.json | context_only | Ignored-inclusive canonical search: no exact-target predecessor. |
| identity | /private/tmp/csm-review-20261011T183112Z/identity-matches.json | context_only | Ignored-inclusive identity enumeration; separate elongasome/magnetosome identities retained. |
| issues | /private/tmp/csm-review-20261011T183112Z/crescentin-all-issues.log | context_only | All-state slug/label issue searches and relevant earlier issues inspected. |
| adapter | /private/tmp/csm-review-20261011T183112Z/adapter.log | context_only | Inventory checked; absent coverage is not biological absence. |
| history-0 | history/records/crescentin_filament/2026-09-11T095221Z-codex-cb614e.yaml | context_only | Original append-only event inspected. |
| history-1 | history/records/crescentin_filament/2026-09-11T100218Z-codex-3bdebf.yaml | context_only | Original append-only event inspected. |
| history-2 | history/records/crescentin_filament/2026-09-21T191603Z-claude-code-8a7d7a.yaml | context_only | Original append-only event inspected. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005856,GO:0099513,GO:0008360,GO:0009252,GO:0110143; GO:0005856 and GO:0099513 definitions and typed parthood | supports | The framework contains polymeric cytoskeletal fibers; a fiber is not the whole framework. |
| paper-2 | DOI:10.1016/j.tim.2017.03.006; Relevant Results/Discussion, methods and figure captions | supports | Inspected secondary review context, not a new primary experiment. Full text inspected for native claims. |
| paper-10 | DOI:10.1073/pnas.2309984121; Relevant Results/Discussion, methods and figure captions | supports | Inspected primary experimental evidence. Full text inspected for native claims. |
| paper-12 | DOI:10.1101/gad.1795509; Exact DOI/PMID metadata and complete abstract only | supports | Inspected primary experimental evidence. Full text was not obtained; abstract-level support only. |
| taxon-155892 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/155892; TaxId, scientificName, rank and aliases | supports | Exact taxon identity verified; taxonomy is not proof of structural occurrence. |
| predecessor | reviews/structured/20261011T185011Z-crescentin_filament-audit/review.yaml | context_only | Immutable pre-edit finding. |
| preservation | /private/tmp/csm-review-20261011T183112Z/preservation.json | context_only | Other native records/vectors and all prior history/review/legacy bytes preserved. |
| red | /private/tmp/csm-review-20261011T183112Z/regressions-red.log | context_only | Baseline tests expose saved defects. |
| green | /private/tmp/csm-review-20261011T183112Z/post-focused.log | context_only | Focused regressions and guarded-writer tests pass. |
| edit-history | history/records/crescentin_filament/2026-10-11T185227Z-codex-67d17a.yaml | context_only | Actual Codex EDIT links original observation and exact issues. |

## Limits And Additional Notes

- Same-agent scoped disposition, not independent approval.
- Original source-access and experimental-scope limits remain; no raw-data reanalysis or new universal taxon claim.
- Initial MreB automated snippet fetch was NOT CHECKED; all three were independently verified against retrieved XML. The post-change checker successfully found all three unchanged quotations verbatim. Existing resolver and test skips retained.
- Corrected source retained by review-base/bacterial-filament-evidence-20261011. Four PR gates and separate native merge-group gates remain required.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T191636Z-crescentin_filament-disposition
kind: record
repository: CultureBotAI/CellStructureMech
title: 'crescentin filament: finding dispositions'
started_at: '2026-10-11T19:15:57Z'
finished_at: '2026-10-11T19:16:36Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent review, not independent human scientific approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Exact saved findings resolved; original observations and surrounding biological
  scope preserved.
source:
  git_revision: 829a2018bbe5e2dcb41b3f9f8d24fdea017addf8
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
  - path: data/structures/cytoskeleton/bactofilin_filament.yaml
    sha256: 3523c9e8fb7e30222f094001ba56a1a5e4bbbc5fa2ed82257086ba3743a583a1
    role: context
  - path: data/structures/cytoskeleton/crescentin_filament.yaml
    sha256: 221a3e850e66a310205cefa75742cb7026d0fe14d6b7f783ef0e66d182efe131
    role: target
  - path: data/structures/cytoskeleton/mamk_filament.yaml
    sha256: fb273942dd11b99a71c61834f5ca331829a340b6a271e0f73e050c1b0128ca64
    role: context
  - path: data/structures/cytoskeleton/mreb_filament.yaml
    sha256: b27d315ff07c11f2aa9eb1f1c1f4c65203ba62509fe6999c7804397e76ab9711
    role: context
  - path: data/structures/cytoskeleton/parm_filament.yaml
    sha256: 576cae9c1768f57e204ad51bb925a87f9fdb55f63def731eb709160678b9aab7
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
  - path: history/records/crescentin_filament/2026-09-11T095221Z-codex-cb614e.yaml
    sha256: b0e7649d4db0adbe1f4484ce65ff5a2c2b17133bd0c0a9d37e77d108daf5835a
    role: context
  - path: history/records/crescentin_filament/2026-09-11T100218Z-codex-3bdebf.yaml
    sha256: fd318cdeaffd19992c5ea6c2c4b5abe9694227775df8af39e744aae6a2c2ec45
    role: context
  - path: history/records/crescentin_filament/2026-09-21T191603Z-claude-code-8a7d7a.yaml
    sha256: 214b0a36d81516c169b7a2864326be6ab23f5f89c9f8dde5e3990381721f91fe
    role: context
  - path: history/records/crescentin_filament/2026-10-11T185227Z-codex-67d17a.yaml
    sha256: 0a6b019f0ac7b12a1806790035c6dc8be70de63d106fd44bc545274232ea9410
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reviews/structured/20261011T185011Z-crescentin_filament-audit/review.yaml
    sha256: 0860cccd51c3f2126cee804474d30c77bc2472f9cfdf653d419a09c18a7c0d2f
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: tests/test_bacterial_filament_evidence.py
    sha256: 60f57f5184e9646ed3a18bdae6b38a5622d159e56d7d2e8672f4d8771b55b983
    role: context
targets:
- target_id: cellstructuremech:crescentin_filament
  path: data/structures/cytoskeleton/crescentin_filament.yaml
  label: crescentin filament
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/crescentin_filament.yaml
    role: maintained scientific record
scope:
  description: Exact findings and surrounding-claim preservation, not a repeated whole-record
    review.
  selection: 20261011T185011Z-crescentin_filament-audit
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:crescentin_filament
checks:
- check_id: crescentin_filament-schema
  name: crescentin_filament-schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:crescentin_filament
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/crescentin_filament.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T18:57:34Z to 2026-10-11T18:57:37Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: crescentin_filament-strict
  name: crescentin_filament-strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:crescentin_filament
  command: .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/crescentin_filament.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T18:57:37Z to 2026-10-11T18:57:42Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: crescentin_filament-snippets
  name: crescentin_filament-snippets
  status: passed
  required: true
  target_ids:
  - cellstructuremech:crescentin_filament
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/cytoskeleton/crescentin_filament.yaml
    --report /private/tmp/csm-review-20261011T183112Z/post-crescentin_filament-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: No verbatim snippets; paraphrases assessed separately against inspected
    text.
  scope_note: 2026-10-11T18:57:42Z to 2026-10-11T18:58:18Z; log SHA-256 4a688dfe5311e8e53e6b6d3107d7e4367146d2bfdef0635b78df791ed6ec924a
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - cellstructuremech:crescentin_filament
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T18:58:18Z to 2026-10-11T18:58:41Z; log SHA-256 c3d705502a321602dac206664f3c14d2b2e226b4b934ebd4bef80256c3249095
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - cellstructuremech:crescentin_filament
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: "id↔label correspondence summary:\n          OK_CANONICAL: 3544\n     \
    \       OK_SYNONYM: 50\n          OK_EXCEPTION: 6\n    SKIPPED_NO_ADAPTER: 603\n\
    \n✅ All id↔label pairs correspond."
  scope_note: 2026-10-11T18:58:41Z to 2026-10-11T19:00:47Z; log SHA-256 d423103555a6a5b538a7c811a73a29c24ed0e5a2eae00d1bb94715295f23f7cb
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - cellstructuremech:crescentin_filament
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T19:00:47Z to 2026-10-11T19:01:04Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - cellstructuremech:crescentin_filament
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: "resolver control: every resolver accepts a known id and rejects a fabricated\
    \ one\nresolving 2 DOI identifier(s)...\n\nidentifier liveness summary:\n  OK\
    \             4015\n  SKIPPED         251\n\nEvery identifier resolves at its\
    \ issuing authority."
  scope_note: 2026-10-11T19:01:04Z to 2026-10-11T19:01:53Z; log SHA-256 ca743f73ab0b56d0cf83f0cb589c71dd629de18cca1bed3127fab794ef121059
- check_id: focused
  name: focused
  status: passed
  required: true
  target_ids:
  - cellstructuremech:crescentin_filament
  command: .venv/bin/python -m pytest -q tests/test_bacterial_filament_evidence.py
    tests/test_write_validated.py
  exit_code: 0
  expected_exit_code: 0
  summary: '............................................                             [100%]

    44 passed in 33.92s'
  scope_note: 2026-10-11T19:01:53Z to 2026-10-11T19:02:28Z; log SHA-256 1c60fe6f497b95ae8afc2ec35e6e4c271eafe08bf67d03e07f68ac9fb7b2861b
- check_id: reviews
  name: reviews
  status: passed
  required: true
  target_ids:
  - cellstructuremech:crescentin_filament
  command: .venv/bin/python scripts/record_review.py check --base e6e0c667ee25463f158a36f5ba7484e88e4c7728
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T19:02:28Z to 2026-10-11T19:04:04Z; log SHA-256 7ad6c07ef025f1ae80ea676f8d3d4c29262bfe88412a46c454cd916457f0a445
- check_id: diff
  name: diff
  status: passed
  required: true
  target_ids:
  - cellstructuremech:crescentin_filament
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T19:04:04Z to 2026-10-11T19:04:05Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- check_id: release-qc
  name: release-qc
  status: passed
  required: true
  target_ids:
  - cellstructuremech:crescentin_filament
  command: .venv/bin/python scripts/run_qc.py
  exit_code: 0
  expected_exit_code: 0
  summary: 'Full local QC passed: 917 passed, 3 skipped in 495.64s (0:08:15). PR and
    native merge-group gates remain separate.'
  scope_note: 2026-10-11T19:05:00Z to 2026-10-11T19:15:35Z; log SHA-256 5480a33277350ae7917a9ca358aa849c480d233aed5f054193e030e1ca3e0275
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/crescentin_filament.yaml
  accessed_at: '2026-10-11T19:16:36Z'
  snapshot_sha256: 221a3e850e66a310205cefa75742cb7026d0fe14d6b7f783ef0e66d182efe131
  support: context_only
  summary: Corrected entire native YAML reinspected against source and original.
- evidence_id: rules
  kind: record_content
  reference: docs/CURATION.md
  accessed_at: '2026-10-11T18:50:11Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  support: context_only
  summary: Fiber is-a versus containing cytoskeleton part_of; narrow claim-local evidence.
- evidence_id: schema
  kind: record_content
  reference: docs/SCHEMA.md
  accessed_at: '2026-10-11T18:50:11Z'
  snapshot_sha256: 07b8f936a553a45cc6e8dba924c21e6af48c81b3866725efeb00c8183f0c75a2
  support: context_only
  summary: Hierarchy and parthood field contracts.
- evidence_id: history
  kind: record_content
  reference: /private/tmp/csm-review-20261011T183112Z/crescentin_filament-discussion-history.json
  accessed_at: '2026-10-11T18:50:11Z'
  snapshot_sha256: f76a13d2542c370f218c224ad7b7a31f780db6454d8810c1fddcacda3e5041cf
  support: context_only
  summary: All committed discussion/inline-history versions inspected.
- evidence_id: predecessors
  kind: validation
  reference: /private/tmp/csm-review-20261011T183112Z/exact-target-predecessors.json
  accessed_at: '2026-10-11T18:50:11Z'
  snapshot_sha256: f7bb865579cd8ac8088b01d712760c8b12268a7fb70bc59b6af68f5cf9d7cc19
  support: context_only
  summary: 'Ignored-inclusive canonical search: no exact-target predecessor.'
- evidence_id: identity
  kind: validation
  reference: /private/tmp/csm-review-20261011T183112Z/identity-matches.json
  accessed_at: '2026-10-11T18:50:11Z'
  snapshot_sha256: 2b7b7369dae8179ab0188eb431905ef8360ea1f16d25c67c9c95567de7ce3006
  support: context_only
  summary: Ignored-inclusive identity enumeration; separate elongasome/magnetosome
    identities retained.
- evidence_id: issues
  kind: validation
  reference: /private/tmp/csm-review-20261011T183112Z/crescentin-all-issues.log
  accessed_at: '2026-10-11T18:50:11Z'
  snapshot_sha256: a9451318297c274057e2a38a1f4e55db66c44af7a04ac82fe58fa2d58941f2a0
  support: context_only
  summary: All-state slug/label issue searches and relevant earlier issues inspected.
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/csm-review-20261011T183112Z/adapter.log
  accessed_at: '2026-10-11T18:50:11Z'
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
  support: context_only
  summary: Inventory checked; absent coverage is not biological absence.
- evidence_id: history-0
  kind: record_content
  reference: history/records/crescentin_filament/2026-09-11T095221Z-codex-cb614e.yaml
  accessed_at: '2026-10-11T18:50:11Z'
  snapshot_sha256: b0e7649d4db0adbe1f4484ce65ff5a2c2b17133bd0c0a9d37e77d108daf5835a
  support: context_only
  summary: Original append-only event inspected.
- evidence_id: history-1
  kind: record_content
  reference: history/records/crescentin_filament/2026-09-11T100218Z-codex-3bdebf.yaml
  accessed_at: '2026-10-11T18:50:11Z'
  snapshot_sha256: fd318cdeaffd19992c5ea6c2c4b5abe9694227775df8af39e744aae6a2c2ec45
  support: context_only
  summary: Original append-only event inspected.
- evidence_id: history-2
  kind: record_content
  reference: history/records/crescentin_filament/2026-09-21T191603Z-claude-code-8a7d7a.yaml
  accessed_at: '2026-10-11T18:50:11Z'
  snapshot_sha256: 214b0a36d81516c169b7a2864326be6ab23f5f89c9f8dde5e3990381721f91fe
  support: context_only
  summary: Original append-only event inspected.
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005856,GO:0099513,GO:0008360,GO:0009252,GO:0110143
  locator: GO:0005856 and GO:0099513 definitions and typed parthood
  accessed_at: '2026-10-11T18:34:21Z'
  snapshot_sha256: 6a239b16f131ac9ca47f663e2cc29ffe96b7dcbc1b3815cb9139317e44c1272f
  support: supports
  summary: The framework contains polymeric cytoskeletal fibers; a fiber is not the
    whole framework.
- evidence_id: paper-2
  kind: primary_source
  reference: DOI:10.1016/j.tim.2017.03.006
  locator: Relevant Results/Discussion, methods and figure captions
  accessed_at: '2026-10-11T18:36:45Z'
  snapshot_sha256: 9580c45d77709114509193e7f0fce6ea39ea3dac3f380393ffc0a7538c9d21df
  support: supports
  summary: Inspected secondary review context, not a new primary experiment. Full
    text inspected for native claims.
- evidence_id: paper-10
  kind: primary_source
  reference: DOI:10.1073/pnas.2309984121
  locator: Relevant Results/Discussion, methods and figure captions
  accessed_at: '2026-10-11T18:32:11Z'
  snapshot_sha256: 8cb50cbc0203beef46d47b203d8961872ec5d9032a6d81682ace643f0376f63e
  support: supports
  summary: Inspected primary experimental evidence. Full text inspected for native
    claims.
- evidence_id: paper-12
  kind: primary_source
  reference: DOI:10.1101/gad.1795509
  locator: Exact DOI/PMID metadata and complete abstract only
  accessed_at: '2026-10-11T18:32:14Z'
  snapshot_sha256: 4ee6eb49b5123b035acd2daa3e105aaadcbc4ed08008d26de60575b80db0bab5
  support: supports
  summary: Inspected primary experimental evidence. Full text was not obtained; abstract-level
    support only.
- evidence_id: taxon-155892
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/155892
  locator: TaxId, scientificName, rank and aliases
  accessed_at: '2026-10-11T18:34:29Z'
  snapshot_sha256: 5e0fd272e1c0461a6f0dc3a10151587eb27de65a6ebebe95bf9adb62d57e215e
  support: supports
  summary: Exact taxon identity verified; taxonomy is not proof of structural occurrence.
- evidence_id: predecessor
  kind: prior_review
  reference: reviews/structured/20261011T185011Z-crescentin_filament-audit/review.yaml
  accessed_at: '2026-10-11T19:16:36Z'
  snapshot_sha256: 0860cccd51c3f2126cee804474d30c77bc2472f9cfdf653d419a09c18a7c0d2f
  support: context_only
  summary: Immutable pre-edit finding.
- evidence_id: preservation
  kind: validation
  reference: /private/tmp/csm-review-20261011T183112Z/preservation.json
  accessed_at: '2026-10-11T19:16:36Z'
  snapshot_sha256: dcecfdef06b599719f9653cbd04f06a233bb4f6b667614ea9903362c6cb90665
  support: context_only
  summary: Other native records/vectors and all prior history/review/legacy bytes
    preserved.
- evidence_id: red
  kind: validation
  reference: /private/tmp/csm-review-20261011T183112Z/regressions-red.log
  accessed_at: '2026-10-11T19:16:36Z'
  snapshot_sha256: 680bd2d0a3f966a6144db02cb7ae9b4bb355bab57a3ff1dca99bf13e43ba7a7c
  support: context_only
  summary: Baseline tests expose saved defects.
- evidence_id: green
  kind: validation
  reference: /private/tmp/csm-review-20261011T183112Z/post-focused.log
  accessed_at: '2026-10-11T19:16:36Z'
  snapshot_sha256: 1c60fe6f497b95ae8afc2ec35e6e4c271eafe08bf67d03e07f68ac9fb7b2861b
  support: context_only
  summary: Focused regressions and guarded-writer tests pass.
- evidence_id: edit-history
  kind: record_content
  reference: history/records/crescentin_filament/2026-10-11T185227Z-codex-67d17a.yaml
  accessed_at: '2026-10-11T19:16:36Z'
  snapshot_sha256: 0a6b019f0ac7b12a1806790035c6dc8be70de63d106fd44bc545274232ea9410
  support: context_only
  summary: Actual Codex EDIT links original observation and exact issues.
assessments:
- assessment_id: resolved-F1
  area: evidence
  topic: Correct cytoskeleton is-a versus parthood
  outcome: supported
  target_ids:
  - cellstructuremech:crescentin_filament
  evidence_ids:
  - record
  - go
  - rules
  - schema
  - predecessor
  - preservation
  - red
  - green
  - edit-history
  summary: The individual filament now has GO:0099513 as broader parent and GO:0005856
    as containing cytoskeleton part_of, with exact authority context.
- assessment_id: resolved-F2
  area: evidence
  topic: Correct the Woldemeskel and Goley publication year
  outcome: supported
  target_ids:
  - cellstructuremech:crescentin_filament
  evidence_ids:
  - record
  - paper-2
  - history
  - predecessor
  - preservation
  - red
  - green
  - edit-history
  summary: 'Corrected four active evidence notes to 2017 and appended an explicit
    correction discussion. Original #1260 curation history, DOI, biology and graph
    relations are preserved.'
findings:
- finding_id: F1
  issue_key: crescentin-filament-cytoskeleton-is-a
  category: evidence
  severity: major
  status: resolved
  certainty: confirmed
  title: Correct cytoskeleton is-a versus parthood
  description: The individual filament now has GO:0099513 as broader parent and GO:0005856
    as containing cytoskeleton part_of, with exact authority context.
  target_ids:
  - cellstructuremech:crescentin_filament
  field_paths:
  - parent_structures
  evidence_ids:
  - record
  - go
  - rules
  - schema
  - predecessor
  - preservation
  - red
  - green
  - edit-history
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/crescentin_filament.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: major
  normalization_reason: Incorrect scientific hierarchy or scope.
  disposition_reason: The individual filament now has GO:0099513 as broader parent
    and GO:0005856 as containing cytoskeleton part_of, with exact authority context.
    Verified by source inspection, bounded diff, red/green regressions and local full
    QC.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261011T185011Z-crescentin_filament-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2244
- finding_id: F2
  issue_key: crescentin-filament-woldemeskel-publication-year
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: Correct the Woldemeskel and Goley publication year
  description: 'Corrected four active evidence notes to 2017 and appended an explicit
    correction discussion. Original #1260 curation history, DOI, biology and graph
    relations are preserved.'
  target_ids:
  - cellstructuremech:crescentin_filament
  field_paths:
  - components[0].evidence[0].notes
  - functions[0].evidence[0].notes
  - evidence[0].notes
  - causal_graphs[0].edges[2].evidence[0].notes
  evidence_ids:
  - record
  - paper-2
  - history
  - predecessor
  - preservation
  - red
  - green
  - edit-history
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/crescentin_filament.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: minor
  normalization_reason: Bounded citation/provenance defect; underlying biology is
    supported.
  disposition_reason: 'Corrected four active evidence notes to 2017 and appended an
    explicit correction discussion. Original #1260 curation history, DOI, biology
    and graph relations are preserved. Verified by source inspection, bounded diff,
    red/green regressions and local full QC.'
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261011T185011Z-crescentin_filament-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2245
actions: []
limitations:
- Same-agent scoped disposition, not independent approval.
- Original source-access and experimental-scope limits remain; no raw-data reanalysis
  or new universal taxon claim.
- Initial MreB automated snippet fetch was NOT CHECKED; all three were independently
  verified against retrieved XML. The post-change checker successfully found all three
  unchanged quotations verbatim. Existing resolver and test skips retained.
- Corrected source retained by review-base/bacterial-filament-evidence-20261011. Four
  PR gates and separate native merge-group gates remain required.
links:
- https://github.com/CultureBotAI/CellStructureMech/issues/2244
- https://github.com/CultureBotAI/CellStructureMech/issues/2245
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261011T185011Z-crescentin_filament-audit
  relationship: Resolves exact predecessor without replacing the original observation.
```
