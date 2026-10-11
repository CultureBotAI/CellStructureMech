# MamK filament: finding dispositions

- Review: 20261011T191621Z-mamk_filament-disposition
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T19:15:52Z
- Finished UTC: 2026-10-11T19:16:21Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Exact saved findings resolved; original observations and surrounding biological scope preserved.

## Scope And Provenance

Exact findings and surrounding-claim preservation, not a repeated whole-record review.

Selection: 20261011T184954Z-mamk_filament-audit
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 829a2018bbe5e2dcb41b3f9f8d24fdea017addf8.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:mamk_filament | data/structures/cytoskeleton/mamk_filament.yaml | maintained | MamK filament |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| mamk_filament-schema | passed | True | cellstructuremech:mamk_filament | Actual deterministic check passed; scientific support assessed separately. |
| mamk_filament-strict | passed | True | cellstructuremech:mamk_filament | Actual deterministic check passed; scientific support assessed separately. |
| mamk_filament-snippets | passed | True | cellstructuremech:mamk_filament | No verbatim snippets; paraphrases assessed separately against inspected text. |
| history | passed | True | cellstructuremech:mamk_filament | Actual deterministic check passed; scientific support assessed separately. |
| labels | passed | True | cellstructuremech:mamk_filament | id↔label correspondence summary:<br>          OK_CANONICAL: 3544<br>            OK_SYNONYM: 50<br>          OK_EXCEPTION: 6<br>    SKIPPED_NO_ADAPTER: 603<br><br>✅ All id↔label pairs correspond. |
| traits | passed | True | cellstructuremech:mamk_filament | Actual deterministic check passed; scientific support assessed separately. |
| curies | passed | True | cellstructuremech:mamk_filament | resolver control: every resolver accepts a known id and rejects a fabricated one<br>resolving 2 DOI identifier(s)...<br><br>identifier liveness summary:<br>  OK             4015<br>  SKIPPED         251<br><br>Every identifier resolves at its issuing authority. |
| focused | passed | True | cellstructuremech:mamk_filament | ............................................                             [100%]<br>44 passed in 33.92s |
| reviews | passed | True | cellstructuremech:mamk_filament | Actual deterministic check passed; scientific support assessed separately. |
| diff | passed | True | cellstructuremech:mamk_filament | Actual deterministic check passed; scientific support assessed separately. |
| release-qc | passed | True | cellstructuremech:mamk_filament | Full local QC passed: 917 passed, 3 skipped in 495.64s (0:08:15). PR and native merge-group gates remain separate. |

## Scientific And Domain Assessments

### Correct cytoskeleton is-a versus parthood

evidence: supported. Targets: cellstructuremech:mamk_filament.

The individual filament now has GO:0099513 as broader parent and GO:0005856 as containing cytoskeleton part_of, with exact authority context.

## Findings

### F1: Correct cytoskeleton is-a versus parthood

major / resolved / confirmed; issue key: mamk-filament-cytoskeleton-is-a.

The individual filament now has GO:0099513 as broader parent and GO:0005856 as containing cytoskeleton part_of, with exact authority context.

Disposition: The individual filament now has GO:0099513 as broader parent and GO:0005856 as containing cytoskeleton part_of, with exact authority context. Verified by source inspection, bounded diff, red/green regressions and local full QC.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/mamk_filament.yaml | context_only | Corrected entire native YAML reinspected against source and original. |
| rules | docs/CURATION.md | context_only | Fiber is-a versus containing cytoskeleton part_of; narrow claim-local evidence. |
| schema | docs/SCHEMA.md | context_only | Hierarchy and parthood field contracts. |
| history | /private/tmp/csm-review-20261011T183112Z/mamk_filament-discussion-history.json | context_only | All committed discussion/inline-history versions inspected. |
| predecessors | /private/tmp/csm-review-20261011T183112Z/exact-target-predecessors.json | context_only | Ignored-inclusive canonical search: no exact-target predecessor. |
| identity | /private/tmp/csm-review-20261011T183112Z/identity-matches.json | context_only | Ignored-inclusive identity enumeration; separate elongasome/magnetosome identities retained. |
| issues | /private/tmp/csm-review-20261011T183112Z/mamk-all-issues.log | context_only | All-state slug/label issue searches and relevant earlier issues inspected. |
| adapter | /private/tmp/csm-review-20261011T183112Z/adapter.log | context_only | Inventory checked; absent coverage is not biological absence. |
| history-0 | history/records/mamk_filament/2026-09-13T081610Z-codex-9427ac.yaml | context_only | Original append-only event inspected. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005856,GO:0099513,GO:0008360,GO:0009252,GO:0110143; GO:0005856 and GO:0099513 definitions and typed parthood | supports | The framework contains polymeric cytoskeletal fibers; a fiber is not the whole framework. |
| paper-0 | DOI:10.1002/pro.2979; Exact DOI/PMID metadata and complete abstract only | supports | Inspected primary experimental evidence. Full text was not obtained; abstract-level support only. |
| paper-5 | DOI:10.1038/nrmicro.2016.99; Exact DOI/PMID metadata and complete abstract only | supports | Inspected secondary review context, not a new primary experiment. Full text was not obtained; abstract-level support only. |
| paper-14 | DOI:10.1126/science.1123231; Exact DOI/PMID metadata and complete abstract only | supports | Inspected primary experimental evidence. Full text was not obtained; abstract-level support only. |
| paper-19 | PMID:20487281; Exact DOI/PMID metadata and complete abstract only | supports | Inspected primary experimental evidence. Full text was not obtained; abstract-level support only. |
| taxon-342108 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/342108; TaxId, scientificName, rank and aliases | supports | Exact taxon identity verified; taxonomy is not proof of structural occurrence. |
| taxon-431944 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/431944; TaxId, scientificName, rank and aliases | supports | Exact taxon identity verified; taxonomy is not proof of structural occurrence. |
| protein-Q2W8Q6 | https://rest.uniprot.org/uniprotkb/Q2W8Q6.json; Reviewed accession, gene, organism and localization provenance | supports | Identifier/source matches verified; localization is not alone filament membership proof. |
| protein-Q6NE59 | https://rest.uniprot.org/uniprotkb/Q6NE59.json; Reviewed accession, gene, organism and localization provenance | supports | Identifier/source matches verified; localization is not alone filament membership proof. |
| mamk-regulation | DOI:10.1111/j.1365-2958.2011.07815.x; Results: MamJ/LimJ single/double mutants and dynamics | supports | Correct Draper 2011 source supports redundant regulation and explicitly bounded physical-interaction evidence. |
| pdb | https://data.rcsb.org/rest/v1/core/entry/5JYG; Structure accession, citation, experimental organism and protein cross-references | supports | Verified AMB-1 MamK structural context; no universal copy-number inference. |
| pdb-entity | https://data.rcsb.org/rest/v1/core/polymer_entity/5JYG/1; Structure accession, citation, experimental organism and protein cross-references | supports | Verified AMB-1 MamK structural context; no universal copy-number inference. |
| emdb | https://www.ebi.ac.uk/emdb/api/entry/EMD-8180; Structure accession, citation, experimental organism and protein cross-references | supports | Verified AMB-1 MamK structural context; no universal copy-number inference. |
| predecessor | reviews/structured/20261011T184954Z-mamk_filament-audit/review.yaml | context_only | Immutable pre-edit finding. |
| preservation | /private/tmp/csm-review-20261011T183112Z/preservation.json | context_only | Other native records/vectors and all prior history/review/legacy bytes preserved. |
| red | /private/tmp/csm-review-20261011T183112Z/regressions-red.log | context_only | Baseline tests expose saved defects. |
| green | /private/tmp/csm-review-20261011T183112Z/post-focused.log | context_only | Focused regressions and guarded-writer tests pass. |
| edit-history | history/records/mamk_filament/2026-10-11T185219Z-codex-cf9d24.yaml | context_only | Actual Codex EDIT links original observation and exact issues. |

## Limits And Additional Notes

- Same-agent scoped disposition, not independent approval.
- Original source-access and experimental-scope limits remain; no raw-data reanalysis or new universal taxon claim.
- Initial MreB automated snippet fetch was NOT CHECKED; all three were independently verified against retrieved XML. The post-change checker successfully found all three unchanged quotations verbatim. Existing resolver and test skips retained.
- Corrected source retained by review-base/bacterial-filament-evidence-20261011. Four PR gates and separate native merge-group gates remain required.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T191621Z-mamk_filament-disposition
kind: record
repository: CultureBotAI/CellStructureMech
title: 'MamK filament: finding dispositions'
started_at: '2026-10-11T19:15:52Z'
finished_at: '2026-10-11T19:16:21Z'
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
    role: context
  - path: data/structures/cytoskeleton/mamk_filament.yaml
    sha256: fb273942dd11b99a71c61834f5ca331829a340b6a271e0f73e050c1b0128ca64
    role: target
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
  - path: history/records/mamk_filament/2026-09-13T081610Z-codex-9427ac.yaml
    sha256: dce0f5ccfda22f671c95cb0c4ce3f4b7b572189ab01d24dd6978cc158085491f
    role: context
  - path: history/records/mamk_filament/2026-10-11T185219Z-codex-cf9d24.yaml
    sha256: 8c1cfd58d76efbd8ee20a9f830e44c7c9254cbceceab3d6152509ee23950a76e
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reviews/structured/20261011T184954Z-mamk_filament-audit/review.yaml
    sha256: 603067e348107b9e39adb309cdf47dbb43e97871e21b1497893e700dc290688f
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
- target_id: cellstructuremech:mamk_filament
  path: data/structures/cytoskeleton/mamk_filament.yaml
  label: MamK filament
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/mamk_filament.yaml
    role: maintained scientific record
scope:
  description: Exact findings and surrounding-claim preservation, not a repeated whole-record
    review.
  selection: 20261011T184954Z-mamk_filament-audit
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:mamk_filament
checks:
- check_id: mamk_filament-schema
  name: mamk_filament-schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mamk_filament
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/mamk_filament.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T18:55:44Z to 2026-10-11T18:55:47Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: mamk_filament-strict
  name: mamk_filament-strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mamk_filament
  command: .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/mamk_filament.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T18:55:47Z to 2026-10-11T18:55:54Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: mamk_filament-snippets
  name: mamk_filament-snippets
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mamk_filament
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/cytoskeleton/mamk_filament.yaml
    --report /private/tmp/csm-review-20261011T183112Z/post-mamk_filament-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: No verbatim snippets; paraphrases assessed separately against inspected
    text.
  scope_note: 2026-10-11T18:55:54Z to 2026-10-11T18:56:25Z; log SHA-256 474e0a9301abb992e24f80b238f8b519692cfe989a846e70797ac9c3524c7e86
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mamk_filament
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
  - cellstructuremech:mamk_filament
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
  - cellstructuremech:mamk_filament
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
  - cellstructuremech:mamk_filament
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
  - cellstructuremech:mamk_filament
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
  - cellstructuremech:mamk_filament
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
  - cellstructuremech:mamk_filament
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
  - cellstructuremech:mamk_filament
  command: .venv/bin/python scripts/run_qc.py
  exit_code: 0
  expected_exit_code: 0
  summary: 'Full local QC passed: 917 passed, 3 skipped in 495.64s (0:08:15). PR and
    native merge-group gates remain separate.'
  scope_note: 2026-10-11T19:05:00Z to 2026-10-11T19:15:35Z; log SHA-256 5480a33277350ae7917a9ca358aa849c480d233aed5f054193e030e1ca3e0275
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/mamk_filament.yaml
  accessed_at: '2026-10-11T19:16:21Z'
  snapshot_sha256: fb273942dd11b99a71c61834f5ca331829a340b6a271e0f73e050c1b0128ca64
  support: context_only
  summary: Corrected entire native YAML reinspected against source and original.
- evidence_id: rules
  kind: record_content
  reference: docs/CURATION.md
  accessed_at: '2026-10-11T18:49:54Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  support: context_only
  summary: Fiber is-a versus containing cytoskeleton part_of; narrow claim-local evidence.
- evidence_id: schema
  kind: record_content
  reference: docs/SCHEMA.md
  accessed_at: '2026-10-11T18:49:54Z'
  snapshot_sha256: 07b8f936a553a45cc6e8dba924c21e6af48c81b3866725efeb00c8183f0c75a2
  support: context_only
  summary: Hierarchy and parthood field contracts.
- evidence_id: history
  kind: record_content
  reference: /private/tmp/csm-review-20261011T183112Z/mamk_filament-discussion-history.json
  accessed_at: '2026-10-11T18:49:54Z'
  snapshot_sha256: 880788895b05bb391cd74b457c8a6d8514b9bc0f3c71a90fb6377bb8a1cd1cfc
  support: context_only
  summary: All committed discussion/inline-history versions inspected.
- evidence_id: predecessors
  kind: validation
  reference: /private/tmp/csm-review-20261011T183112Z/exact-target-predecessors.json
  accessed_at: '2026-10-11T18:49:54Z'
  snapshot_sha256: f7bb865579cd8ac8088b01d712760c8b12268a7fb70bc59b6af68f5cf9d7cc19
  support: context_only
  summary: 'Ignored-inclusive canonical search: no exact-target predecessor.'
- evidence_id: identity
  kind: validation
  reference: /private/tmp/csm-review-20261011T183112Z/identity-matches.json
  accessed_at: '2026-10-11T18:49:54Z'
  snapshot_sha256: 2b7b7369dae8179ab0188eb431905ef8360ea1f16d25c67c9c95567de7ce3006
  support: context_only
  summary: Ignored-inclusive identity enumeration; separate elongasome/magnetosome
    identities retained.
- evidence_id: issues
  kind: validation
  reference: /private/tmp/csm-review-20261011T183112Z/mamk-all-issues.log
  accessed_at: '2026-10-11T18:49:54Z'
  snapshot_sha256: f5abb655f1ae2a65d5ed477ad387031619eb824f20df6ca40b35bf71108829c1
  support: context_only
  summary: All-state slug/label issue searches and relevant earlier issues inspected.
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/csm-review-20261011T183112Z/adapter.log
  accessed_at: '2026-10-11T18:49:54Z'
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
  support: context_only
  summary: Inventory checked; absent coverage is not biological absence.
- evidence_id: history-0
  kind: record_content
  reference: history/records/mamk_filament/2026-09-13T081610Z-codex-9427ac.yaml
  accessed_at: '2026-10-11T18:49:54Z'
  snapshot_sha256: dce0f5ccfda22f671c95cb0c4ce3f4b7b572189ab01d24dd6978cc158085491f
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
- evidence_id: paper-0
  kind: primary_source
  reference: DOI:10.1002/pro.2979
  locator: Exact DOI/PMID metadata and complete abstract only
  accessed_at: '2026-10-11T18:31:53Z'
  snapshot_sha256: 2c926af54adae80ae8fee51f579d04a6f8f5262f3aff12e68968ccb9493d4510
  support: supports
  summary: Inspected primary experimental evidence. Full text was not obtained; abstract-level
    support only.
- evidence_id: paper-5
  kind: primary_source
  reference: DOI:10.1038/nrmicro.2016.99
  locator: Exact DOI/PMID metadata and complete abstract only
  accessed_at: '2026-10-11T18:32:03Z'
  snapshot_sha256: bf54bba5cb5e9466b90b162cb7ee317ec91032a15937b2d17ef3b4de38fc737e
  support: supports
  summary: Inspected secondary review context, not a new primary experiment. Full
    text was not obtained; abstract-level support only.
- evidence_id: paper-14
  kind: primary_source
  reference: DOI:10.1126/science.1123231
  locator: Exact DOI/PMID metadata and complete abstract only
  accessed_at: '2026-10-11T18:32:17Z'
  snapshot_sha256: 705c49bca2b6fa6acd03761609c5b491ca118b56d1eb520c65fe423a9e20f611
  support: supports
  summary: Inspected primary experimental evidence. Full text was not obtained; abstract-level
    support only.
- evidence_id: paper-19
  kind: primary_source
  reference: PMID:20487281
  locator: Exact DOI/PMID metadata and complete abstract only
  accessed_at: '2026-10-11T18:32:24Z'
  snapshot_sha256: f15d4ab2fc6c7372a35c856caf7b46695986dfa107b3ff9ef76e7839e08163c0
  support: supports
  summary: Inspected primary experimental evidence. Full text was not obtained; abstract-level
    support only.
- evidence_id: taxon-342108
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/342108
  locator: TaxId, scientificName, rank and aliases
  accessed_at: '2026-10-11T18:34:24Z'
  snapshot_sha256: 23ab2a141de441b18fc4edcd456c3cf95d789c0c017cd9e58cb8bda73a5ae365
  support: supports
  summary: Exact taxon identity verified; taxonomy is not proof of structural occurrence.
- evidence_id: taxon-431944
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/431944
  locator: TaxId, scientificName, rank and aliases
  accessed_at: '2026-10-11T18:34:25Z'
  snapshot_sha256: 8e6916672afb4c32a2a99e2dcc07f5a14b4ba7b0969243ce89646042ce60476d
  support: supports
  summary: Exact taxon identity verified; taxonomy is not proof of structural occurrence.
- evidence_id: protein-Q2W8Q6
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q2W8Q6.json
  locator: Reviewed accession, gene, organism and localization provenance
  accessed_at: '2026-10-11T18:34:32Z'
  snapshot_sha256: 7601fb1d103bdd527f7c86bfdd80179cc4ce3a535a8b35948bc9dbbc22ab34cb
  support: supports
  summary: Identifier/source matches verified; localization is not alone filament
    membership proof.
- evidence_id: protein-Q6NE59
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q6NE59.json
  locator: Reviewed accession, gene, organism and localization provenance
  accessed_at: '2026-10-11T18:34:33Z'
  snapshot_sha256: 12f0f9719e4395404b26dee6039de9834b8d17f6019884b8430479d69502a40c
  support: supports
  summary: Identifier/source matches verified; localization is not alone filament
    membership proof.
- evidence_id: mamk-regulation
  kind: primary_source
  reference: DOI:10.1111/j.1365-2958.2011.07815.x
  locator: 'Results: MamJ/LimJ single/double mutants and dynamics'
  accessed_at: '2026-10-11T18:43:43Z'
  snapshot_sha256: 85b2188211537155bfebeeb92b4e0c2ceeaa621aaf95a3793d2d84a6f75459ed
  support: supports
  summary: Correct Draper 2011 source supports redundant regulation and explicitly
    bounded physical-interaction evidence.
- evidence_id: pdb
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/entry/5JYG
  locator: Structure accession, citation, experimental organism and protein cross-references
  accessed_at: '2026-10-11T18:34:35Z'
  snapshot_sha256: 77952202023ada2d37bd5c1637bdcf9947483720df741a87e94e5ecd4f61cf12
  support: supports
  summary: Verified AMB-1 MamK structural context; no universal copy-number inference.
- evidence_id: pdb-entity
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/5JYG/1
  locator: Structure accession, citation, experimental organism and protein cross-references
  accessed_at: '2026-10-11T18:34:35Z'
  snapshot_sha256: 13a5b92fd1c62e3e125c5c760af1e61bc2eadf681bf68872dd51c94101b8125f
  support: supports
  summary: Verified AMB-1 MamK structural context; no universal copy-number inference.
- evidence_id: emdb
  kind: database
  reference: https://www.ebi.ac.uk/emdb/api/entry/EMD-8180
  locator: Structure accession, citation, experimental organism and protein cross-references
  accessed_at: '2026-10-11T18:34:36Z'
  snapshot_sha256: 45f0d90faec842ea7f5bc14094bb504a8286381cbd39feae5d2a2133a19f15ea
  support: supports
  summary: Verified AMB-1 MamK structural context; no universal copy-number inference.
- evidence_id: predecessor
  kind: prior_review
  reference: reviews/structured/20261011T184954Z-mamk_filament-audit/review.yaml
  accessed_at: '2026-10-11T19:16:21Z'
  snapshot_sha256: 603067e348107b9e39adb309cdf47dbb43e97871e21b1497893e700dc290688f
  support: context_only
  summary: Immutable pre-edit finding.
- evidence_id: preservation
  kind: validation
  reference: /private/tmp/csm-review-20261011T183112Z/preservation.json
  accessed_at: '2026-10-11T19:16:21Z'
  snapshot_sha256: dcecfdef06b599719f9653cbd04f06a233bb4f6b667614ea9903362c6cb90665
  support: context_only
  summary: Other native records/vectors and all prior history/review/legacy bytes
    preserved.
- evidence_id: red
  kind: validation
  reference: /private/tmp/csm-review-20261011T183112Z/regressions-red.log
  accessed_at: '2026-10-11T19:16:21Z'
  snapshot_sha256: 680bd2d0a3f966a6144db02cb7ae9b4bb355bab57a3ff1dca99bf13e43ba7a7c
  support: context_only
  summary: Baseline tests expose saved defects.
- evidence_id: green
  kind: validation
  reference: /private/tmp/csm-review-20261011T183112Z/post-focused.log
  accessed_at: '2026-10-11T19:16:21Z'
  snapshot_sha256: 1c60fe6f497b95ae8afc2ec35e6e4c271eafe08bf67d03e07f68ac9fb7b2861b
  support: context_only
  summary: Focused regressions and guarded-writer tests pass.
- evidence_id: edit-history
  kind: record_content
  reference: history/records/mamk_filament/2026-10-11T185219Z-codex-cf9d24.yaml
  accessed_at: '2026-10-11T19:16:21Z'
  snapshot_sha256: 8c1cfd58d76efbd8ee20a9f830e44c7c9254cbceceab3d6152509ee23950a76e
  support: context_only
  summary: Actual Codex EDIT links original observation and exact issues.
assessments:
- assessment_id: resolved-F1
  area: evidence
  topic: Correct cytoskeleton is-a versus parthood
  outcome: supported
  target_ids:
  - cellstructuremech:mamk_filament
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
findings:
- finding_id: F1
  issue_key: mamk-filament-cytoskeleton-is-a
  category: evidence
  severity: major
  status: resolved
  certainty: confirmed
  title: Correct cytoskeleton is-a versus parthood
  description: The individual filament now has GO:0099513 as broader parent and GO:0005856
    as containing cytoskeleton part_of, with exact authority context.
  target_ids:
  - cellstructuremech:mamk_filament
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
    path: data/structures/cytoskeleton/mamk_filament.yaml
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
    review_id: 20261011T184954Z-mamk_filament-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2240
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
- https://github.com/CultureBotAI/CellStructureMech/issues/2240
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261011T184954Z-mamk_filament-audit
  relationship: Resolves exact predecessor without replacing the original observation.
```
