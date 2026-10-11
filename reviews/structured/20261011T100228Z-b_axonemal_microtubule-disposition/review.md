# B axonemal microtubule: finding disposition

- Review: 20261011T100228Z-b_axonemal_microtubule-disposition
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T09:53:45Z
- Finished UTC: 2026-10-11T10:02:28Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The exact predecessor finding is resolved by a bounded correction. Native scientific status and acknowledged unknowns remain unchanged.

## Scope And Provenance

Reassessment of the exact predecessor finding and preservation of surrounding native claims, not a new whole-record scientific review.

Selection: 20261011T094735Z-b_axonemal_microtubule-audit
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a6fb6adbe1e84c69b44974678e4f04ad1fdd2fbc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0097650 | data/structures/cytoskeleton/b_axonemal_microtubule.yaml | maintained | B axonemal microtubule |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0097650 | Actual post-curation deterministic check passed; namespace skips and empty snippet checks do not certify scientific evidence. |
| strict | passed | True | GO:0097650 | Actual post-curation deterministic check passed; namespace skips and empty snippet checks do not certify scientific evidence. |
| snippets | passed | True | GO:0097650 | Actual post-curation deterministic check passed; namespace skips and empty snippet checks do not certify scientific evidence. |
| history | passed | True | GO:0097650 | Actual post-curation deterministic check passed; namespace skips and empty snippet checks do not certify scientific evidence. |
| labels | passed | True | GO:0097650 | id↔label correspondence summary:<br>          OK_CANONICAL: 3544<br>            OK_SYNONYM: 50<br>          OK_EXCEPTION: 6<br>    SKIPPED_NO_ADAPTER: 603<br><br>✅ All id↔label pairs correspond. |
| traits | passed | True | GO:0097650 | Actual post-curation deterministic check passed; namespace skips and empty snippet checks do not certify scientific evidence. |
| curies | passed | True | GO:0097650 | resolver control: every resolver accepts a known id and rejects a fabricated one<br><br>identifier liveness summary:<br>  OK             4014<br>  SKIPPED         251<br><br>Every identifier resolves at its issuing authority. |
| regressions | passed | True | GO:0097650 | Actual post-curation deterministic check passed; namespace skips and empty snippet checks do not certify scientific evidence. |
| reviews | passed | True | GO:0097650 | Actual post-curation deterministic check passed; namespace skips and empty snippet checks do not certify scientific evidence. |
| diff | passed | True | GO:0097650 | Actual post-curation deterministic check passed; namespace skips and empty snippet checks do not certify scientific evidence. |
| focused | passed | True | GO:0097650 | ..............................                                           [100%]<br>30 passed in 59.22s |
| release-qc2 | passed | True | GO:0097650 | Full local QC passed: 846 passed, 3 skipped in 520.81s (0:08:40). Required remote PR and native merge-group checks remain separate publication gates. |

## Scientific And Domain Assessments

### Restore the original B-tubule discussion rationale

provenance: supported. Targets: GO:0097650.

The exact original B-tubule rationale and complete later inner-sheath rationale are retained with revision context. Current narrowed prompt, original author/date, OPEN status, graph attachment, child relation and all biological fields remain unchanged.

## Findings

### F1: Restore the original B-tubule discussion rationale

minor / resolved / confirmed; issue key: b-tubule-discussion-rationale-preservation.

The exact original B-tubule rationale and complete later inner-sheath rationale are retained with revision context. Current narrowed prompt, original author/date, OPEN status, graph attachment, child relation and all biological fields remain unchanged.

Disposition: The exact original B-tubule rationale and complete later inner-sheath rationale are retained with revision context. Current narrowed prompt, original author/date, OPEN status, graph attachment, child relation and all biological fields remain unchanged. Verified by direct native diff, regression tests, source-based reassessment and full QC.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/b_axonemal_microtubule.yaml | context_only | Corrected native YAML reread and compared structurally against baseline; only the declared fields and appended curation event changed. |
| rules | docs/CURATION.md | context_only | parent_structures is is-a, part_of is containment; individual fibers are not cytoskeleton subclasses. Discussion rationale is append-only. |
| history | /private/tmp/csm-review-20261011T093443Z/b_axonemal_microtubule-discussion-history.json | context_only | Complete committed discussion and curation-event history inspected. |
| predecessors | /private/tmp/csm-review-20261011T093443Z/exact-target-predecessors.json | context_only | Ignored-inclusive canonical-review scan found no exact-target predecessor; legacy reports are historical context, not canonical lineage. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005575,GO:0005856,GO:0005879,GO:0032053,GO:0032991,GO:0036064,GO:0097545,GO:0097649,GO:0097650,GO:0110165,GO:0120280,GO:0140180,GO:0140535,GO:0160110,GO:0160112,GO:0160113,GO:0160114; Relevant GO definitions, aspect, obsolescence and typed reverse children | supports | B-tubule identity and axonemal parent/parthood are supported. GO:0005856 denotes the containing framework, not an is-a class for each basal-body subassembly. |
| taxa | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=285686%2C3055%2C5762%2C5888%2C5911%2C63628; Top-level NCBITaxon:3055 Chlamydomonas reinhardtii, rank species | supports | Resolves taxon identity, not biological prevalence. |
| adapter | /private/tmp/csm-review-20261011T093443Z/adapter.log | context_only | Live 28-dataset iModulonDB inventory has no Chlamydomonas dataset. Not applicable; lack of coverage is not negative biological evidence. |
| ma | DOI:10.1016/j.cell.2019.09.030; Primary introduction; Results MIP networks, tubule junctions and Figure 6; experimental model and specimen preparation | supports | Chlamydomonas doublets have 13-PF A and 10-PF B tubules; B01 joins A10/A11, B10 joins A01, and luminal MIP networks are distinct from the wall. |
| child | data/structures/cytoskeleton/axonemal_b_tubule_inner_sheath.yaml | context_only | Existing B-sheath child retains its OPEN molecular task and the already documented current GO A/B relationship discrepancy. B-lumen containment is primary-supported. |
| repository-history | history/records/b_axonemal_microtubule/2026-09-23T174334Z-claude-code-a53df0.yaml | context_only | Creation history read; original actor metadata retained. |
| predecessor | reviews/structured/20261011T094735Z-b_axonemal_microtubule-audit/review.yaml | context_only | Immutable original finding committed before curation. |
| preservation | /private/tmp/csm-review-20261011T093443Z/preservation.json | supports | 906 other native records and every previous review, history and legacy report remain byte-identical. |
| field-preservation | /private/tmp/csm-review-20261011T093443Z/adversarial-preservation.json | supports | Exact field comparisons confirm the three bounded edits, retained original rationales, unchanged molecular tasks and discussion lifecycle. |
| embeddings | /private/tmp/csm-review-20261011T093443Z/embedding-verification.json | supports | All 909 semantic inputs and vectors remain unchanged; parent relations are outside this repository semantic projection. |
| focused-tests | /private/tmp/csm-review-20261011T093443Z/focused-command.json | supports | Thirty focused and guarded-writer tests pass after correction. |
| red-tests | /private/tmp/csm-review-20261011T093443Z/regressions-red-command.json | supports | All three new regressions failed on the original native inputs. |
| final-baseline-replay | /private/tmp/csm-review-20261011T093443Z/final-baseline-replay.json | supports | All three final regression cases fail when the reader is pointed at original Git blobs, without mutating the working tree. |

## Limits And Additional Notes

- Same-agent scientific review, not independent human sign-off; all native records remain PROPOSED.
- No raw micrograph, reconstruction-map or experimental-data reanalysis. Unknown molecular composition and stoichiometry are not certified.
- Ma Europe PMC XML returned an error; official PMC HTML was inspected. Li 2012 ordinary browser page presented a challenge; public official PMC open-data JATS and original media were available and checksum verified.
- This disposition certifies only the exact predecessor finding; other batch records have separate completion accounting in the goal worklist.
- The first QC attempt stopped at a new-test line-length error; after formatting correction, full local QC passed. Original failed output remains in release-qc.log. Skipped label/identifier namespaces remain explicit and are not scientific certification.
- Exact disposition inputs retained by review-base/basal-body-boundaries-20261011. Remote PR and native merge-group checks are publication gates outside this observation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T100228Z-b_axonemal_microtubule-disposition
kind: record
repository: CultureBotAI/CellStructureMech
title: 'B axonemal microtubule: finding disposition'
started_at: '2026-10-11T09:53:45Z'
finished_at: '2026-10-11T10:02:28Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent correction and adversarial diff review, not independent
    human approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The exact predecessor finding is resolved by a bounded correction. Native
  scientific status and acknowledged unknowns remain unchanged.
source:
  git_revision: a6fb6adbe1e84c69b44974678e4f04ad1fdd2fbc
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
    sha256: 64862db2087298ae832b8a8410185349cc277151af31d88ce231e43201ab9440
    role: context
  - path: curation/source_queue.tsv
    sha256: 55d8fe79b5edd7d6b42bf4ca9168fe4878240417716e2f4ba423489144b89284
    role: context
  - path: data/structures/cytoskeleton/axonemal_b_tubule_inner_sheath.yaml
    sha256: d1b0e481219c8b248e22e069aaa333074857a9ef8cae74d159e9a9e1f33a733e
    role: context
  - path: data/structures/cytoskeleton/axonemal_doublet_microtubule.yaml
    sha256: deedf652ec4801ed3186c00789cb1c725e5c682f84c2934132489486535848b4
    role: context
  - path: data/structures/cytoskeleton/axonemal_microtubule.yaml
    sha256: 480cd29d1f2e87c07c19dd8d60e50768cdcce29223b28ce2df1d4c956dc46282
    role: context
  - path: data/structures/cytoskeleton/b_axonemal_microtubule.yaml
    sha256: 14dc7bee2d7f4dbaf766868cb49cb2e0145765a5de184a80452664871a7db50f
    role: target
  - path: data/structures/cytoskeleton/basal_body_a_b_inner_junction.yaml
    sha256: 818592b3a8a807ee94f6de26d50992ac0589c4bdcd261a0443df16dbc16edff9
    role: context
  - path: data/structures/cytoskeleton/basal_body_a_c_linker.yaml
    sha256: 0a7ea087c029443809ba73acf52e83c59170ffa490347c3f7ffed1f37f432b7b
    role: context
  - path: data/structures/cytoskeleton/basal_body_a_tusk.yaml
    sha256: f82923b0febf504980e0c7e006d03d72c9cfdd2b38e225b6ad82adaac4d754c1
    role: context
  - path: data/structures/cytoskeleton/basal_body_b_c_inner_junction.yaml
    sha256: 1fda2a9ff6bec4d4b314bdd8f5995a2a2e21a8f6d11286eed800057257e2028b
    role: context
  - path: data/structures/cytoskeleton/basal_body_c_tubule_hook.yaml
    sha256: 492ed1f70c96fec1ccf2f5eb0efbb7ed4950b46f69031242a1869c9c820ee383
    role: context
  - path: data/structures/cytoskeleton/basal_body_c_tubule_luminal_filament.yaml
    sha256: a7abec342419ed1f405caf67d4fbaf85d1ce7587db5391a73bfeb136509aa1b1
    role: context
  - path: data/structures/cytoskeleton/basal_body_cartwheel.yaml
    sha256: ad4e6fcf7639e0fffc00b553b0ab2e0e2a8eac5981b87ae9da1ee783ba942957
    role: context
  - path: data/structures/cytoskeleton/basal_body_cartwheel_inner_density.yaml
    sha256: cc7469f2607b02f62b092c115aac1669dd80865e82be6462c10e3dec866dfc00
    role: context
  - path: data/structures/cytoskeleton/basal_body_d2_rod.yaml
    sha256: acd457cb1d0121248e5d11bdebc1d70a815a42f240f31e02eaa556bc54e7bc27
    role: context
  - path: data/structures/cytoskeleton/basal_body_filamentous_cartwheel_inner_density.yaml
    sha256: 5fc268e1a3493fde87ab6856fae60c61025633bdbc9c7d29c08c794c5678d8df
    role: context
  - path: data/structures/cytoskeleton/basal_body_inner_scaffold.yaml
    sha256: b320c60ebc92c55021e2a673b4a4d696ad3a2d8dc8fae6a704cb972814ce2443
    role: context
  - path: data/structures/cytoskeleton/basal_body_pinhead.yaml
    sha256: ef3da1eee8d7e92150c0bf3ab1c6e2c67a410aa366416ab03454e3929e25bff2
    role: context
  - path: data/structures/cytoskeleton/basal_body_triplet_base.yaml
    sha256: c88a6c10f311bce934e37d5583f122fee6cae6f45950117728cb6d1a7905e6f8
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
  - path: history/records/b_axonemal_microtubule/2026-09-23T174334Z-claude-code-a53df0.yaml
    sha256: 75f3976a9633c450e1bed88a1fc8255122ff36eab3fda790e751bf9f423c329c
    role: context
  - path: history/records/b_axonemal_microtubule/2026-10-11T094831Z-codex-05f2ea.yaml
    sha256: 1e18a38ee2d2701ed9fa73204974322007437b87efc910ed6460b68ad48488ce
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reviews/structured/20261011T094735Z-b_axonemal_microtubule-audit/review.yaml
    sha256: 52463d38acaaa81a15216b572e600104e64e05bc9e7a43874a17f78bda882662
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: tests/test_basal_body_boundaries_review.py
    sha256: a3dea63d510fbb0c814ef2aee9b5a395c2f71fc23ec07f534150e12ebb98c363
    role: context
targets:
- target_id: GO:0097650
  path: data/structures/cytoskeleton/b_axonemal_microtubule.yaml
  label: B axonemal microtubule
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/b_axonemal_microtubule.yaml
    role: maintained scientific record
scope:
  description: Reassessment of the exact predecessor finding and preservation of surrounding
    native claims, not a new whole-record scientific review.
  selection: 20261011T094735Z-b_axonemal_microtubule-audit
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - GO:0097650
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - GO:0097650
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/b_axonemal_microtubule.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation deterministic check passed; namespace skips and empty
    snippet checks do not certify scientific evidence.
  scope_note: 2026-10-11T09:48:41Z to 2026-10-11T09:48:44Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - GO:0097650
  command: .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/b_axonemal_microtubule.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation deterministic check passed; namespace skips and empty
    snippet checks do not certify scientific evidence.
  scope_note: 2026-10-11T09:48:44Z to 2026-10-11T09:48:49Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - GO:0097650
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/cytoskeleton/b_axonemal_microtubule.yaml
    --report /private/tmp/csm-review-20261011T093443Z/b_axonemal_microtubule-post-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation deterministic check passed; namespace skips and empty
    snippet checks do not certify scientific evidence.
  scope_note: 2026-10-11T09:48:49Z to 2026-10-11T09:49:21Z; log SHA-256 08e7608d0335fe274a4dbfc3f88fd0ce8b255edb4ecd2053cef3ebf6fc1f1f13
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:0097650
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation deterministic check passed; namespace skips and empty
    snippet checks do not certify scientific evidence.
  scope_note: 2026-10-11T09:50:41Z to 2026-10-11T09:50:58Z; log SHA-256 492e83d5895ef12ed7c8fdaa79e2e4c4df62e5689ad61364be05c4fa6d39efee
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - GO:0097650
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: "id↔label correspondence summary:\n          OK_CANONICAL: 3544\n     \
    \       OK_SYNONYM: 50\n          OK_EXCEPTION: 6\n    SKIPPED_NO_ADAPTER: 603\n\
    \n✅ All id↔label pairs correspond."
  scope_note: 2026-10-11T09:50:58Z to 2026-10-11T09:52:28Z; log SHA-256 d423103555a6a5b538a7c811a73a29c24ed0e5a2eae00d1bb94715295f23f7cb
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - GO:0097650
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation deterministic check passed; namespace skips and empty
    snippet checks do not certify scientific evidence.
  scope_note: 2026-10-11T09:52:28Z to 2026-10-11T09:52:48Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - GO:0097650
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: "resolver control: every resolver accepts a known id and rejects a fabricated\
    \ one\n\nidentifier liveness summary:\n  OK             4014\n  SKIPPED      \
    \   251\n\nEvery identifier resolves at its issuing authority."
  scope_note: 2026-10-11T09:52:48Z to 2026-10-11T09:53:32Z; log SHA-256 ee1c5f2e78a2d29fcb6781a8ecd722934376595042d2cc261b4465b361d19b79
- check_id: regressions
  name: regressions
  status: passed
  required: true
  target_ids:
  - GO:0097650
  command: .venv/bin/python -m pytest -q tests/test_cytoskeleton_evidence_review.py
    tests/test_write_validated.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation deterministic check passed; namespace skips and empty
    snippet checks do not certify scientific evidence.
  scope_note: 2026-10-11T09:53:32Z to 2026-10-11T09:54:06Z; log SHA-256 fb66f73f55125a46fae4687eaa2f1c00098fd1d3e3984d7f90463ad44037e7d7
- check_id: reviews
  name: reviews
  status: passed
  required: true
  target_ids:
  - GO:0097650
  command: .venv/bin/python scripts/record_review.py check --base 51cbd8eb58e2082cbb54d629d3a9516c716a249c
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation deterministic check passed; namespace skips and empty
    snippet checks do not certify scientific evidence.
  scope_note: 2026-10-11T09:54:06Z to 2026-10-11T09:55:12Z; log SHA-256 4221e8213cb0304efc5b3996205aae44293a0476ba011f2644acb31d99c0b842
- check_id: diff
  name: diff
  status: passed
  required: true
  target_ids:
  - GO:0097650
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation deterministic check passed; namespace skips and empty
    snippet checks do not certify scientific evidence.
  scope_note: 2026-10-11T09:55:12Z to 2026-10-11T09:55:12Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- check_id: focused
  name: focused
  status: passed
  required: true
  target_ids:
  - GO:0097650
  command: .venv/bin/pytest -q tests/test_basal_body_boundaries_review.py tests/test_axonemal_architecture_review.py
    tests/test_write_validated.py
  exit_code: 0
  expected_exit_code: 0
  summary: '..............................                                           [100%]

    30 passed in 59.22s'
  scope_note: 2026-10-11T09:48:43Z to 2026-10-11T09:49:43Z; log SHA-256 08eb3be61d8ca3c54a766f22eb2afeb674606e16d3cffa7bc16e43c2625ef0a8
- check_id: release-qc2
  name: release-qc2
  status: passed
  required: true
  target_ids:
  - GO:0097650
  command: .venv/bin/python scripts/run_qc.py
  exit_code: 0
  expected_exit_code: 0
  summary: 'Full local QC passed: 846 passed, 3 skipped in 520.81s (0:08:40). Required
    remote PR and native merge-group checks remain separate publication gates.'
  scope_note: 2026-10-11T09:50:51Z to 2026-10-11T10:02:23Z; log SHA-256 98907a8f31807aad4117dd0c2c2ecd339314f46856176fa1065211b13ac5cdd7
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/b_axonemal_microtubule.yaml
  accessed_at: '2026-10-11T10:02:28Z'
  snapshot_sha256: 14dc7bee2d7f4dbaf766868cb49cb2e0145765a5de184a80452664871a7db50f
  support: context_only
  summary: Corrected native YAML reread and compared structurally against baseline;
    only the declared fields and appended curation event changed.
- evidence_id: rules
  kind: record_content
  reference: docs/CURATION.md
  accessed_at: '2026-10-11T09:47:35Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  support: context_only
  summary: parent_structures is is-a, part_of is containment; individual fibers are
    not cytoskeleton subclasses. Discussion rationale is append-only.
- evidence_id: history
  kind: record_content
  reference: /private/tmp/csm-review-20261011T093443Z/b_axonemal_microtubule-discussion-history.json
  accessed_at: '2026-10-11T09:47:35Z'
  snapshot_sha256: bd5bb8fd945ddc93098e4833a4049fae9cb2969b07397b4990ff74fec6302136
  support: context_only
  summary: Complete committed discussion and curation-event history inspected.
- evidence_id: predecessors
  kind: validation
  reference: /private/tmp/csm-review-20261011T093443Z/exact-target-predecessors.json
  accessed_at: '2026-10-11T09:47:35Z'
  snapshot_sha256: b8cb7a2be3d74d5e013507af93d561be33a033653302a0851f787235026ead84
  support: context_only
  summary: Ignored-inclusive canonical-review scan found no exact-target predecessor;
    legacy reports are historical context, not canonical lineage.
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005575,GO:0005856,GO:0005879,GO:0032053,GO:0032991,GO:0036064,GO:0097545,GO:0097649,GO:0097650,GO:0110165,GO:0120280,GO:0140180,GO:0140535,GO:0160110,GO:0160112,GO:0160113,GO:0160114
  locator: Relevant GO definitions, aspect, obsolescence and typed reverse children
  accessed_at: '2026-10-11T09:44:12Z'
  snapshot_sha256: 55218f64ea9ce115bdafbfb9b583c1799457662afcd378d4d01d29704fdc8d09
  support: supports
  summary: B-tubule identity and axonemal parent/parthood are supported. GO:0005856
    denotes the containing framework, not an is-a class for each basal-body subassembly.
- evidence_id: taxa
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=285686%2C3055%2C5762%2C5888%2C5911%2C63628
  locator: Top-level NCBITaxon:3055 Chlamydomonas reinhardtii, rank species
  accessed_at: '2026-10-11T09:36:27Z'
  snapshot_sha256: dc9bf03533798607ae6a53c723c8b6f9c70991fc4b14d36a48a152a3c938d348
  support: supports
  summary: Resolves taxon identity, not biological prevalence.
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/csm-review-20261011T093443Z/adapter.log
  accessed_at: '2026-10-11T09:47:35Z'
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
  support: context_only
  summary: Live 28-dataset iModulonDB inventory has no Chlamydomonas dataset. Not
    applicable; lack of coverage is not negative biological evidence.
- evidence_id: ma
  kind: primary_source
  reference: DOI:10.1016/j.cell.2019.09.030
  locator: Primary introduction; Results MIP networks, tubule junctions and Figure
    6; experimental model and specimen preparation
  accessed_at: '2026-10-11T09:38:39Z'
  snapshot_sha256: d2509facbaa0004a0963bc4722cda3b68d9e3eba7f8c1700f7c3f060440b9b90
  support: supports
  summary: Chlamydomonas doublets have 13-PF A and 10-PF B tubules; B01 joins A10/A11,
    B10 joins A01, and luminal MIP networks are distinct from the wall.
- evidence_id: child
  kind: record_content
  reference: data/structures/cytoskeleton/axonemal_b_tubule_inner_sheath.yaml
  accessed_at: '2026-10-11T09:47:35Z'
  snapshot_sha256: d1b0e481219c8b248e22e069aaa333074857a9ef8cae74d159e9a9e1f33a733e
  support: context_only
  summary: Existing B-sheath child retains its OPEN molecular task and the already
    documented current GO A/B relationship discrepancy. B-lumen containment is primary-supported.
- evidence_id: repository-history
  kind: record_content
  reference: history/records/b_axonemal_microtubule/2026-09-23T174334Z-claude-code-a53df0.yaml
  accessed_at: '2026-10-11T09:47:35Z'
  snapshot_sha256: 75f3976a9633c450e1bed88a1fc8255122ff36eab3fda790e751bf9f423c329c
  support: context_only
  summary: Creation history read; original actor metadata retained.
- evidence_id: predecessor
  kind: prior_review
  reference: reviews/structured/20261011T094735Z-b_axonemal_microtubule-audit/review.yaml
  accessed_at: '2026-10-11T10:02:28Z'
  snapshot_sha256: 52463d38acaaa81a15216b572e600104e64e05bc9e7a43874a17f78bda882662
  support: context_only
  summary: Immutable original finding committed before curation.
- evidence_id: preservation
  kind: validation
  reference: /private/tmp/csm-review-20261011T093443Z/preservation.json
  accessed_at: '2026-10-11T10:02:28Z'
  snapshot_sha256: cf23f2d0d4be1647125805b967727d9b1749fbf5fd40c48352bb173cbce9edd1
  support: supports
  summary: 906 other native records and every previous review, history and legacy
    report remain byte-identical.
- evidence_id: field-preservation
  kind: validation
  reference: /private/tmp/csm-review-20261011T093443Z/adversarial-preservation.json
  accessed_at: '2026-10-11T10:02:28Z'
  snapshot_sha256: e606931851c7d3579145e694eabf22e4dce644f9df132514dadd30d968227c7d
  support: supports
  summary: Exact field comparisons confirm the three bounded edits, retained original
    rationales, unchanged molecular tasks and discussion lifecycle.
- evidence_id: embeddings
  kind: validation
  reference: /private/tmp/csm-review-20261011T093443Z/embedding-verification.json
  accessed_at: '2026-10-11T10:02:28Z'
  snapshot_sha256: 857edd7a986ddbb5fb952b8aa1726fbd3fc8c03d86714bea68d96a90851fe6ef
  support: supports
  summary: All 909 semantic inputs and vectors remain unchanged; parent relations
    are outside this repository semantic projection.
- evidence_id: focused-tests
  kind: validation
  reference: /private/tmp/csm-review-20261011T093443Z/focused-command.json
  accessed_at: '2026-10-11T10:02:28Z'
  snapshot_sha256: b873d5d52fc390f466a8af73430d19a5d9a63f3257cdf7c5384fbdf1bc5acc2d
  support: supports
  summary: Thirty focused and guarded-writer tests pass after correction.
- evidence_id: red-tests
  kind: validation
  reference: /private/tmp/csm-review-20261011T093443Z/regressions-red-command.json
  accessed_at: '2026-10-11T10:02:28Z'
  snapshot_sha256: c887c81a2ad9bb29765dcd07c7ae82eb2c6e0bcb8bda2335283a5397838250aa
  support: supports
  summary: All three new regressions failed on the original native inputs.
- evidence_id: final-baseline-replay
  kind: validation
  reference: /private/tmp/csm-review-20261011T093443Z/final-baseline-replay.json
  accessed_at: '2026-10-11T10:02:28Z'
  snapshot_sha256: 57b6858ffdfd688cb5413a358ff1a77e3623ff5933154aad4463d66fb062051a
  support: supports
  summary: All three final regression cases fail when the reader is pointed at original
    Git blobs, without mutating the working tree.
assessments:
- assessment_id: resolved-f1
  area: provenance
  topic: Restore the original B-tubule discussion rationale
  outcome: supported
  target_ids:
  - GO:0097650
  evidence_ids:
  - record
  - rules
  - history
  - predecessor
  - field-preservation
  - focused-tests
  summary: The exact original B-tubule rationale and complete later inner-sheath rationale
    are retained with revision context. Current narrowed prompt, original author/date,
    OPEN status, graph attachment, child relation and all biological fields remain
    unchanged.
findings:
- finding_id: F1
  issue_key: b-tubule-discussion-rationale-preservation
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  title: Restore the original B-tubule discussion rationale
  description: The exact original B-tubule rationale and complete later inner-sheath
    rationale are retained with revision context. Current narrowed prompt, original
    author/date, OPEN status, graph attachment, child relation and all biological
    fields remain unchanged.
  target_ids:
  - GO:0097650
  field_paths:
  - discussions[0].rationale
  evidence_ids:
  - record
  - rules
  - history
  - predecessor
  - field-preservation
  - focused-tests
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/b_axonemal_microtubule.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: minor
  normalization_reason: A bounded source-attribution or discussion-provenance defect;
    the biological identity and structure boundaries remain supported.
  disposition_reason: The exact original B-tubule rationale and complete later inner-sheath
    rationale are retained with revision context. Current narrowed prompt, original
    author/date, OPEN status, graph attachment, child relation and all biological
    fields remain unchanged. Verified by direct native diff, regression tests, source-based
    reassessment and full QC.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261011T094735Z-b_axonemal_microtubule-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2202
actions: []
limitations:
- Same-agent scientific review, not independent human sign-off; all native records
  remain PROPOSED.
- No raw micrograph, reconstruction-map or experimental-data reanalysis. Unknown molecular
  composition and stoichiometry are not certified.
- Ma Europe PMC XML returned an error; official PMC HTML was inspected. Li 2012 ordinary
  browser page presented a challenge; public official PMC open-data JATS and original
  media were available and checksum verified.
- This disposition certifies only the exact predecessor finding; other batch records
  have separate completion accounting in the goal worklist.
- The first QC attempt stopped at a new-test line-length error; after formatting correction,
  full local QC passed. Original failed output remains in release-qc.log. Skipped
  label/identifier namespaces remain explicit and are not scientific certification.
- Exact disposition inputs retained by review-base/basal-body-boundaries-20261011.
  Remote PR and native merge-group checks are publication gates outside this observation.
links:
- https://github.com/CultureBotAI/CellStructureMech/issues/2202
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261011T094735Z-b_axonemal_microtubule-audit
  relationship: Resolves the exact predecessor finding without rewriting the original
    observation.
```
