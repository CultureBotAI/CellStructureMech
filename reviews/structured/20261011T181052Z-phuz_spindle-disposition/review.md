# PhuZ spindle: finding dispositions

- Review: 20261011T181052Z-phuz_spindle-disposition
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T18:10:22Z
- Finished UTC: 2026-10-11T18:10:52Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Saved findings resolved through bounded evidence-backed corrections; original observations retained.

## Scope And Provenance

Exact saved findings and preservation of surrounding claims; not a second whole-record review.

Selection: 20261011T175546Z-phuz_spindle-audit
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 2157c7bca99e2814d9a816a49299034bd190e671.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:phuz_spindle | data/structures/cytoskeleton/phuz_spindle.yaml | maintained | PhuZ spindle |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| phuz_spindle-schema | passed | True | cellstructuremech:phuz_spindle | Actual deterministic check passed; scientific support assessed separately. |
| phuz_spindle-strict | passed | True | cellstructuremech:phuz_spindle | Actual deterministic check passed; scientific support assessed separately. |
| phuz_spindle-snippets | passed | True | cellstructuremech:phuz_spindle | No verbatim snippets; paraphrases assessed separately against inspected text. |
| history | passed | True | cellstructuremech:phuz_spindle | Actual deterministic check passed; scientific support assessed separately. |
| labels | passed | True | cellstructuremech:phuz_spindle | id↔label correspondence summary:<br>          OK_CANONICAL: 3544<br>            OK_SYNONYM: 50<br>          OK_EXCEPTION: 6<br>    SKIPPED_NO_ADAPTER: 603<br><br>✅ All id↔label pairs correspond. |
| traits | passed | True | cellstructuremech:phuz_spindle | Actual deterministic check passed; scientific support assessed separately. |
| curies | passed | True | cellstructuremech:phuz_spindle | [not exercised] BFO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] CHEBI: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] ComplexPortal: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] DOI: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] GO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] InterPro: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] NCBITaxon: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] PATO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] PMID: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] RO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] SO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] UO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] UniProtKB: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] DOI: DataCite was unreachable, so DOI:10.22002/D1.1355 was not exercised<br>resolver control: 14 resolver(s) could not be exercised because their authority was unreachable; the rest accept a known id and reject a fabricated one<br><br>identifier liveness summary:<br>  OK             4013<br>  SKIPPED         251<br><br>Every identifier resolves at its issuing authority. |
| focused | passed | True | cellstructuremech:phuz_spindle | ......................................                                   [100%]<br>38 passed in 44.21s |
| reviews | passed | True | cellstructuremech:phuz_spindle | Actual deterministic check passed; scientific support assessed separately. |
| diff | passed | True | cellstructuremech:phuz_spindle | Actual deterministic check passed; scientific support assessed separately. |
| release-qc | passed | True | cellstructuremech:phuz_spindle | Full local QC passed: 897 passed, 3 skipped in 509.54s (0:08:29). PR and native merge-group gates remain separate. |

## Scientific And Domain Assessments

### Correct cytoskeleton is-a versus parthood

evidence: supported. Targets: cellstructuremech:phuz_spindle.

GO:0005856 is now part_of; individual polymers use GO:0099513 as their fiber parent. The multi-filament spindle is not forced into a single-fiber identity.

### Separate the Goslar vortex from the PhuZ spindle

evidence: supported. Targets: cellstructuremech:phuz_spindle.

Active occurrence/examples and component/function claims now describe the spindle. Goslar vortex evidence remains in an explicit contrasting discussion. Rotation is retained with Science 2017 spindle evidence; the positioning graph and original history remain unchanged.

## Findings

### F1: Correct cytoskeleton is-a versus parthood

major / resolved / confirmed; issue key: phuz-spindle-cytoskeleton-is-a.

GO:0005856 is now part_of; individual polymers use GO:0099513 as their fiber parent. The multi-filament spindle is not forced into a single-fiber identity.

Disposition: GO:0005856 is now part_of; individual polymers use GO:0099513 as their fiber parent. The multi-filament spindle is not forced into a single-fiber identity. Verified by scoped diff, inspected sources, red/green tests and full local QC.

### F2: Separate the Goslar vortex from the PhuZ spindle

major / resolved / confirmed; issue key: phuz-spindle-goslar-vortex-boundary.

Active occurrence/examples and component/function claims now describe the spindle. Goslar vortex evidence remains in an explicit contrasting discussion. Rotation is retained with Science 2017 spindle evidence; the positioning graph and original history remain unchanged.

Disposition: Active occurrence/examples and component/function claims now describe the spindle. Goslar vortex evidence remains in an explicit contrasting discussion. Rotation is retained with Science 2017 spindle evidence; the positioning graph and original history remain unchanged. Verified by scoped diff, inspected sources, red/green tests and full local QC.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/phuz_spindle.yaml | context_only | Corrected full record reread and compared with original and sources. |
| rules | docs/CURATION.md | context_only | Explicitly separates cytoskeletal fiber is-a from containing cytoskeleton part_of. |
| schema | docs/SCHEMA.md | context_only | parent_structures is-a; part_of is parthood. |
| history | /private/tmp/csm-review-20261011T174605Z/phuz_spindle-discussion-history.json | context_only | All committed discussion/inline-history versions inspected; prior rationale retained. |
| history-0 | history/records/phuz_spindle/2026-09-11T124312Z-codex-8c515a.yaml | context_only | Original CREATE and correction events inspected. |
| history-1 | history/records/phuz_spindle/2026-09-11T125034Z-codex-0a6ca0.yaml | context_only | Original CREATE and correction events inspected. |
| predecessors | /private/tmp/csm-review-20261011T174605Z/exact-target-predecessors.json | context_only | Ignored-inclusive canonical scan found no exact target predecessor. |
| identity-search | /private/tmp/csm-review-20261011T174605Z/identity-matches.json | context_only | Ignored-inclusive native identity enumeration: retain distinct tubulin-family structures; do not equate generic microtubule, division ring, phage nucleus or vortex with the spindle. |
| issues | /private/tmp/csm-review-20261011T174605Z/phuz-all-issues.log | context_only | All-state issue search inspected, including earlier component/scope fixes; no existing open issue resolves these findings. |
| adapter | /private/tmp/csm-review-20261011T174605Z/adapter.log | context_only | No matching source-organism dataset for these encoded structural proteins; host E. coli/Pseudomonas expression modules do not establish phage-encoded PhuZ structure. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005856,GO:0005874,GO:0099513,GO:0015630; GO:0005856 definition; GO:0099513 definition and part_of relation | supports | Cytoskeleton is the containing framework; polymeric fibers are components, not types of that entire framework. |
| taxon-198110 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/198110; taxId, scientificName, rank and aliases | supports | Exact taxon identifier/label verified; presence claims evaluated from papers, not taxonomic rank. |
| taxon-2502409 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2502409; taxId, scientificName, rank and aliases | supports | Exact taxon identifier/label verified; presence claims evaluated from papers, not taxonomic rank. |
| paper-0 | DOI:10.1016/j.celrep.2017.07.064; Relevant Results, Discussion, methods and figure captions for native claims | supports | Inspected primary source text for structure, component and experimental scope. |
| paper-1 | DOI:10.1016/j.celrep.2022.111179; Relevant Results, Discussion, methods and figure captions for native claims | supports | Inspected primary source text for structure, component and experimental scope. |
| paper-11 | DOI:10.1126/science.aal2130; Relevant Results, Discussion, methods and figure captions for native claims | supports | Inspected primary source text for structure, component and experimental scope. |
| paper-18 | DOI:10.7554/eLife.03197; Relevant Results, Discussion, methods and figure captions for native claims | supports | Inspected primary source text for structure, component and experimental scope. |
| predecessor | reviews/structured/20261011T175546Z-phuz_spindle-audit/review.yaml | context_only | Immutable pre-edit finding. |
| preservation | /private/tmp/csm-review-20261011T174605Z/preservation.json | context_only | Untouched native records, vectors and prior history/review/legacy files preserved. |
| red | /private/tmp/csm-review-20261011T174605Z/regressions-red.log | context_only | Baseline failures demonstrate the defects. |
| green | /private/tmp/csm-review-20261011T174605Z/post-focused.log | context_only | Focused tests and guarded-writer tests passed. |
| edit-history | history/records/phuz_spindle/2026-10-11T175640Z-codex-e6ed72.yaml | context_only | Actual Codex EDIT links original observation and issues. |

## Limits And Additional Notes

- Same-agent scoped disposition, not independent human sign-off.
- Original primary snapshots remain the evidence basis; no raw-data reanalysis. Protein groundings and experimental scope remain bounded.
- Native PR and separate merge-group gates remain required; existing resolver/test skips retained. Corrected source retained by review-base/tubulin-family-boundaries-20261011.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T181052Z-phuz_spindle-disposition
kind: record
repository: CultureBotAI/CellStructureMech
title: 'PhuZ spindle: finding dispositions'
started_at: '2026-10-11T18:10:22Z'
finished_at: '2026-10-11T18:10:52Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent review; not independent human scientific approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Saved findings resolved through bounded evidence-backed corrections; original
  observations retained.
source:
  git_revision: 2157c7bca99e2814d9a816a49299034bd190e671
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
  - path: data/structures/cytoskeleton/btubab_bacterial_microtubule.yaml
    sha256: 9dad1b4ea650b206b4d5005f63805f2f8ec586b4c942c0663da3df94b9367284
    role: context
  - path: data/structures/cytoskeleton/cetz_filament.yaml
    sha256: fd116102dcb2f7c9dc89aa074142d8224fd910b8199ddf816881716f6116ede9
    role: context
  - path: data/structures/cytoskeleton/microtubule.yaml
    sha256: 29404191864964cf5b86c3894c7b942d63b83fc4bb1b6b461d7677baad6af305
    role: context
  - path: data/structures/cytoskeleton/phuz_spindle.yaml
    sha256: 4a319827b4a744aadeb7827c470defa533270bbc990afef9ec024ec5365e8459
    role: target
  - path: data/structures/cytoskeleton/tubz_filament.yaml
    sha256: 32bd17ec65c8b2d36716dd3df603beebe144d34ea4af986b0c041d8cc49b5f8d
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
  - path: history/records/phuz_spindle/2026-09-11T124312Z-codex-8c515a.yaml
    sha256: f39e3afbb92658c1efeaa24fd200ef008d4dfa474977e7d6147c6a381c436eee
    role: context
  - path: history/records/phuz_spindle/2026-09-11T125034Z-codex-0a6ca0.yaml
    sha256: f79b3af7a92c83d0bd8b688dacee0d341905597a4012cbd2233cb7f910f519a5
    role: context
  - path: history/records/phuz_spindle/2026-10-11T175640Z-codex-e6ed72.yaml
    sha256: 2f5ee29b570c7515446787434ee7d830dc1c06bcb8f73b4c95fe87b55896a874
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reviews/structured/20261011T175546Z-phuz_spindle-audit/review.yaml
    sha256: 13d570484e2fd6723d90b47d30eb41484d2b0d915bc4999f60fc92f0ce53882e
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: tests/test_tubulin_family_boundaries.py
    sha256: 81a2a97813e7e4b75b28a5f06779d4ead81b36c7a27d7cb2e040bdb00bf1bbd3
    role: context
targets:
- target_id: cellstructuremech:phuz_spindle
  path: data/structures/cytoskeleton/phuz_spindle.yaml
  label: PhuZ spindle
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/phuz_spindle.yaml
    role: maintained scientific record
scope:
  description: Exact saved findings and preservation of surrounding claims; not a
    second whole-record review.
  selection: 20261011T175546Z-phuz_spindle-audit
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:phuz_spindle
checks:
- check_id: phuz_spindle-schema
  name: phuz_spindle-schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:phuz_spindle
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/phuz_spindle.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T17:58:47Z to 2026-10-11T17:58:50Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: phuz_spindle-strict
  name: phuz_spindle-strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:phuz_spindle
  command: .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/phuz_spindle.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T17:58:50Z to 2026-10-11T17:58:56Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: phuz_spindle-snippets
  name: phuz_spindle-snippets
  status: passed
  required: true
  target_ids:
  - cellstructuremech:phuz_spindle
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/cytoskeleton/phuz_spindle.yaml
    --report /private/tmp/csm-review-20261011T174605Z/post-phuz_spindle-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: No verbatim snippets; paraphrases assessed separately against inspected
    text.
  scope_note: 2026-10-11T17:58:56Z to 2026-10-11T17:59:23Z; log SHA-256 dcaf5b9dfacf71de98bb95ec16cf870fbad4758354ffcad0ef4d5903fd2ac10e
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - cellstructuremech:phuz_spindle
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T17:59:23Z to 2026-10-11T17:59:42Z; log SHA-256 4f6b05d12a24e704b5b087418a3dec5d72f923f73be7080e8103d2b0be9094e0
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - cellstructuremech:phuz_spindle
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: "id↔label correspondence summary:\n          OK_CANONICAL: 3544\n     \
    \       OK_SYNONYM: 50\n          OK_EXCEPTION: 6\n    SKIPPED_NO_ADAPTER: 603\n\
    \n✅ All id↔label pairs correspond."
  scope_note: 2026-10-11T17:59:42Z to 2026-10-11T18:01:09Z; log SHA-256 d423103555a6a5b538a7c811a73a29c24ed0e5a2eae00d1bb94715295f23f7cb
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - cellstructuremech:phuz_spindle
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T18:01:09Z to 2026-10-11T18:01:32Z; log SHA-256 553832e049eb99562adc0d8260a3f74f18342e6aa8261c4cbc33b824c4f6332c
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - cellstructuremech:phuz_spindle
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: "[not exercised] BFO: the issuing authority was unreachable after 1 attempts,\
    \ so this resolver was not exercised\n  [not exercised] CHEBI: the issuing authority\
    \ was unreachable after 1 attempts, so this resolver was not exercised\n  [not\
    \ exercised] ComplexPortal: the issuing authority was unreachable after 1 attempts,\
    \ so this resolver was not exercised\n  [not exercised] DOI: the issuing authority\
    \ was unreachable after 1 attempts, so this resolver was not exercised\n  [not\
    \ exercised] GO: the issuing authority was unreachable after 1 attempts, so this\
    \ resolver was not exercised\n  [not exercised] InterPro: the issuing authority\
    \ was unreachable after 1 attempts, so this resolver was not exercised\n  [not\
    \ exercised] NCBITaxon: the issuing authority was unreachable after 1 attempts,\
    \ so this resolver was not exercised\n  [not exercised] PATO: the issuing authority\
    \ was unreachable after 1 attempts, so this resolver was not exercised\n  [not\
    \ exercised] PMID: the issuing authority was unreachable after 1 attempts, so\
    \ this resolver was not exercised\n  [not exercised] RO: the issuing authority\
    \ was unreachable after 1 attempts, so this resolver was not exercised\n  [not\
    \ exercised] SO: the issuing authority was unreachable after 1 attempts, so this\
    \ resolver was not exercised\n  [not exercised] UO: the issuing authority was\
    \ unreachable after 1 attempts, so this resolver was not exercised\n  [not exercised]\
    \ UniProtKB: the issuing authority was unreachable after 1 attempts, so this resolver\
    \ was not exercised\n  [not exercised] DOI: DataCite was unreachable, so DOI:10.22002/D1.1355\
    \ was not exercised\nresolver control: 14 resolver(s) could not be exercised because\
    \ their authority was unreachable; the rest accept a known id and reject a fabricated\
    \ one\n\nidentifier liveness summary:\n  OK             4013\n  SKIPPED      \
    \   251\n\nEvery identifier resolves at its issuing authority."
  scope_note: 2026-10-11T18:01:32Z to 2026-10-11T18:01:57Z; log SHA-256 800d5c4ef6c7964ccbd1a80a4be5c5f7e04774af577c1544c94abaa18c2326b3
- check_id: focused
  name: focused
  status: passed
  required: true
  target_ids:
  - cellstructuremech:phuz_spindle
  command: .venv/bin/python -m pytest -q tests/test_tubulin_family_boundaries.py tests/test_write_validated.py
  exit_code: 0
  expected_exit_code: 0
  summary: '......................................                                   [100%]

    38 passed in 44.21s'
  scope_note: 2026-10-11T18:01:57Z to 2026-10-11T18:02:42Z; log SHA-256 6e640f1ba6ef4107aa281f81192503e0aadd3f41192157c8c14b163a4981b234
- check_id: reviews
  name: reviews
  status: passed
  required: true
  target_ids:
  - cellstructuremech:phuz_spindle
  command: .venv/bin/python scripts/record_review.py check --base a8bab45f6868c61fad49550ea05bc10167c27689
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T18:02:42Z to 2026-10-11T18:04:05Z; log SHA-256 ea3f8b4b85974547f68746fef4b708ef2f67e6082b0712bbdddae6b46a591d97
- check_id: diff
  name: diff
  status: passed
  required: true
  target_ids:
  - cellstructuremech:phuz_spindle
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T18:04:05Z to 2026-10-11T18:04:06Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- check_id: release-qc
  name: release-qc
  status: passed
  required: true
  target_ids:
  - cellstructuremech:phuz_spindle
  command: .venv/bin/python scripts/run_qc.py
  exit_code: 0
  expected_exit_code: 0
  summary: 'Full local QC passed: 897 passed, 3 skipped in 509.54s (0:08:29). PR and
    native merge-group gates remain separate.'
  scope_note: 2026-10-11T17:58:49Z to 2026-10-11T18:10:01Z; log SHA-256 505b68a7863a797e081efe5832e9cdeaaa90b33eb3ec8042e434cd2fdcae782f
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/phuz_spindle.yaml
  accessed_at: '2026-10-11T18:10:52Z'
  snapshot_sha256: 4a319827b4a744aadeb7827c470defa533270bbc990afef9ec024ec5365e8459
  support: context_only
  summary: Corrected full record reread and compared with original and sources.
- evidence_id: rules
  kind: record_content
  reference: docs/CURATION.md
  accessed_at: '2026-10-11T17:55:46Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  support: context_only
  summary: Explicitly separates cytoskeletal fiber is-a from containing cytoskeleton
    part_of.
- evidence_id: schema
  kind: record_content
  reference: docs/SCHEMA.md
  accessed_at: '2026-10-11T17:55:46Z'
  snapshot_sha256: 07b8f936a553a45cc6e8dba924c21e6af48c81b3866725efeb00c8183f0c75a2
  support: context_only
  summary: parent_structures is-a; part_of is parthood.
- evidence_id: history
  kind: record_content
  reference: /private/tmp/csm-review-20261011T174605Z/phuz_spindle-discussion-history.json
  accessed_at: '2026-10-11T17:55:46Z'
  snapshot_sha256: 5d328ff43c385069b5ec76212c4ff07ef2e3974488168781ffa3c05d9ce3a700
  support: context_only
  summary: All committed discussion/inline-history versions inspected; prior rationale
    retained.
- evidence_id: history-0
  kind: record_content
  reference: history/records/phuz_spindle/2026-09-11T124312Z-codex-8c515a.yaml
  accessed_at: '2026-10-11T17:55:46Z'
  snapshot_sha256: f39e3afbb92658c1efeaa24fd200ef008d4dfa474977e7d6147c6a381c436eee
  support: context_only
  summary: Original CREATE and correction events inspected.
- evidence_id: history-1
  kind: record_content
  reference: history/records/phuz_spindle/2026-09-11T125034Z-codex-0a6ca0.yaml
  accessed_at: '2026-10-11T17:55:46Z'
  snapshot_sha256: f79b3af7a92c83d0bd8b688dacee0d341905597a4012cbd2233cb7f910f519a5
  support: context_only
  summary: Original CREATE and correction events inspected.
- evidence_id: predecessors
  kind: validation
  reference: /private/tmp/csm-review-20261011T174605Z/exact-target-predecessors.json
  accessed_at: '2026-10-11T17:55:46Z'
  snapshot_sha256: b58274921260ac2318a673d931246261d1b7ea598c7a3d2eb5013f3ff36dfbbc
  support: context_only
  summary: Ignored-inclusive canonical scan found no exact target predecessor.
- evidence_id: identity-search
  kind: validation
  reference: /private/tmp/csm-review-20261011T174605Z/identity-matches.json
  accessed_at: '2026-10-11T17:55:46Z'
  snapshot_sha256: c026bdc56a293d9fc1419efd2f0798c6ec25e7c3f9b51a44a4bae7e231256ab2
  support: context_only
  summary: 'Ignored-inclusive native identity enumeration: retain distinct tubulin-family
    structures; do not equate generic microtubule, division ring, phage nucleus or
    vortex with the spindle.'
- evidence_id: issues
  kind: validation
  reference: /private/tmp/csm-review-20261011T174605Z/phuz-all-issues.log
  accessed_at: '2026-10-11T17:55:46Z'
  snapshot_sha256: db9cb03d507e473c8ac842c3a02bc2ca7e260a2de0eddda46b4c16736cfecd41
  support: context_only
  summary: All-state issue search inspected, including earlier component/scope fixes;
    no existing open issue resolves these findings.
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/csm-review-20261011T174605Z/adapter.log
  accessed_at: '2026-10-11T17:55:46Z'
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
  support: context_only
  summary: No matching source-organism dataset for these encoded structural proteins;
    host E. coli/Pseudomonas expression modules do not establish phage-encoded PhuZ
    structure.
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005856,GO:0005874,GO:0099513,GO:0015630
  locator: GO:0005856 definition; GO:0099513 definition and part_of relation
  accessed_at: '2026-10-11T17:50:36Z'
  snapshot_sha256: 3f5a3dd27abf49ffd043baef1f9e0730ddd2274ecad7b0cc2f5a52aea7516850
  support: supports
  summary: Cytoskeleton is the containing framework; polymeric fibers are components,
    not types of that entire framework.
- evidence_id: taxon-198110
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/198110
  locator: taxId, scientificName, rank and aliases
  accessed_at: '2026-10-11T17:50:41Z'
  snapshot_sha256: 05582eae738417bf2943ad2780dad7e3e1fd8e94e5e3d8da834b2d6a78b95752
  support: supports
  summary: Exact taxon identifier/label verified; presence claims evaluated from papers,
    not taxonomic rank.
- evidence_id: taxon-2502409
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2502409
  locator: taxId, scientificName, rank and aliases
  accessed_at: '2026-10-11T17:50:42Z'
  snapshot_sha256: 87c3dd5062888416f7217bb3da804d04c5e2521c6e69ceb4333d5fa3e04109c7
  support: supports
  summary: Exact taxon identifier/label verified; presence claims evaluated from papers,
    not taxonomic rank.
- evidence_id: paper-0
  kind: primary_source
  reference: DOI:10.1016/j.celrep.2017.07.064
  locator: Relevant Results, Discussion, methods and figure captions for native claims
  accessed_at: '2026-10-11T17:49:43Z'
  snapshot_sha256: 9812d6859d4714ed77676e35dc26d846c47b7793f20395d36ca590caa69e00a9
  support: supports
  summary: Inspected primary source text for structure, component and experimental
    scope.
- evidence_id: paper-1
  kind: primary_source
  reference: DOI:10.1016/j.celrep.2022.111179
  locator: Relevant Results, Discussion, methods and figure captions for native claims
  accessed_at: '2026-10-11T17:49:43Z'
  snapshot_sha256: 732e4542caa34c1a2d0c370f3d39d1c88377eea0f8e4e656adcf0c6cc0e5f36c
  support: supports
  summary: Inspected primary source text for structure, component and experimental
    scope.
- evidence_id: paper-11
  kind: primary_source
  reference: DOI:10.1126/science.aal2130
  locator: Relevant Results, Discussion, methods and figure captions for native claims
  accessed_at: '2026-10-11T17:49:45Z'
  snapshot_sha256: 4ccb39d224cfb78f54a5948a8e3b04aae8f964acd1eda601727eef7f6393eb92
  support: supports
  summary: Inspected primary source text for structure, component and experimental
    scope.
- evidence_id: paper-18
  kind: primary_source
  reference: DOI:10.7554/eLife.03197
  locator: Relevant Results, Discussion, methods and figure captions for native claims
  accessed_at: '2026-10-11T17:47:39Z'
  snapshot_sha256: 5654fbc48edb1740282321290a118152595c040c10c5ec0564a591549f8f0ac5
  support: supports
  summary: Inspected primary source text for structure, component and experimental
    scope.
- evidence_id: predecessor
  kind: prior_review
  reference: reviews/structured/20261011T175546Z-phuz_spindle-audit/review.yaml
  accessed_at: '2026-10-11T18:10:52Z'
  snapshot_sha256: 13d570484e2fd6723d90b47d30eb41484d2b0d915bc4999f60fc92f0ce53882e
  support: context_only
  summary: Immutable pre-edit finding.
- evidence_id: preservation
  kind: validation
  reference: /private/tmp/csm-review-20261011T174605Z/preservation.json
  accessed_at: '2026-10-11T18:10:52Z'
  snapshot_sha256: 788bec1b0614a7621d6c344299aa8012f139a1683eb41c3742730f6fed024cba
  support: context_only
  summary: Untouched native records, vectors and prior history/review/legacy files
    preserved.
- evidence_id: red
  kind: validation
  reference: /private/tmp/csm-review-20261011T174605Z/regressions-red.log
  accessed_at: '2026-10-11T18:10:52Z'
  snapshot_sha256: c69b7206201befb5d17cc4d2384edaa5b2def9885eaefcc05f0a51cec3c427a1
  support: context_only
  summary: Baseline failures demonstrate the defects.
- evidence_id: green
  kind: validation
  reference: /private/tmp/csm-review-20261011T174605Z/post-focused.log
  accessed_at: '2026-10-11T18:10:52Z'
  snapshot_sha256: 6e640f1ba6ef4107aa281f81192503e0aadd3f41192157c8c14b163a4981b234
  support: context_only
  summary: Focused tests and guarded-writer tests passed.
- evidence_id: edit-history
  kind: record_content
  reference: history/records/phuz_spindle/2026-10-11T175640Z-codex-e6ed72.yaml
  accessed_at: '2026-10-11T18:10:52Z'
  snapshot_sha256: 2f5ee29b570c7515446787434ee7d830dc1c06bcb8f73b4c95fe87b55896a874
  support: context_only
  summary: Actual Codex EDIT links original observation and issues.
assessments:
- assessment_id: resolved-F1
  area: evidence
  topic: Correct cytoskeleton is-a versus parthood
  outcome: supported
  target_ids:
  - cellstructuremech:phuz_spindle
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
  summary: GO:0005856 is now part_of; individual polymers use GO:0099513 as their
    fiber parent. The multi-filament spindle is not forced into a single-fiber identity.
- assessment_id: resolved-F2
  area: evidence
  topic: Separate the Goslar vortex from the PhuZ spindle
  outcome: supported
  target_ids:
  - cellstructuremech:phuz_spindle
  evidence_ids:
  - record
  - paper-0
  - paper-1
  - paper-11
  - issues
  - rules
  - predecessor
  - preservation
  - red
  - green
  - edit-history
  summary: Active occurrence/examples and component/function claims now describe the
    spindle. Goslar vortex evidence remains in an explicit contrasting discussion.
    Rotation is retained with Science 2017 spindle evidence; the positioning graph
    and original history remain unchanged.
findings:
- finding_id: F1
  issue_key: phuz-spindle-cytoskeleton-is-a
  category: evidence
  severity: major
  status: resolved
  certainty: confirmed
  title: Correct cytoskeleton is-a versus parthood
  description: GO:0005856 is now part_of; individual polymers use GO:0099513 as their
    fiber parent. The multi-filament spindle is not forced into a single-fiber identity.
  target_ids:
  - cellstructuremech:phuz_spindle
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
    path: data/structures/cytoskeleton/phuz_spindle.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: major
  normalization_reason: Material hierarchy or structure-scope assertion, not an optional
    completeness suggestion.
  disposition_reason: GO:0005856 is now part_of; individual polymers use GO:0099513
    as their fiber parent. The multi-filament spindle is not forced into a single-fiber
    identity. Verified by scoped diff, inspected sources, red/green tests and full
    local QC.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261011T175546Z-phuz_spindle-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2234
- finding_id: F2
  issue_key: phuz-spindle-goslar-vortex-boundary
  category: evidence
  severity: major
  status: resolved
  certainty: confirmed
  title: Separate the Goslar vortex from the PhuZ spindle
  description: Active occurrence/examples and component/function claims now describe
    the spindle. Goslar vortex evidence remains in an explicit contrasting discussion.
    Rotation is retained with Science 2017 spindle evidence; the positioning graph
    and original history remain unchanged.
  target_ids:
  - cellstructuremech:phuz_spindle
  field_paths:
  - components
  - taxonomic_distribution
  - canonical_examples
  - functions
  - discussions
  evidence_ids:
  - record
  - paper-0
  - paper-1
  - paper-11
  - issues
  - rules
  - predecessor
  - preservation
  - red
  - green
  - edit-history
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/phuz_spindle.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: major
  normalization_reason: Material hierarchy or structure-scope assertion, not an optional
    completeness suggestion.
  disposition_reason: Active occurrence/examples and component/function claims now
    describe the spindle. Goslar vortex evidence remains in an explicit contrasting
    discussion. Rotation is retained with Science 2017 spindle evidence; the positioning
    graph and original history remain unchanged. Verified by scoped diff, inspected
    sources, red/green tests and full local QC.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261011T175546Z-phuz_spindle-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2235
actions: []
limitations:
- Same-agent scoped disposition, not independent human sign-off.
- Original primary snapshots remain the evidence basis; no raw-data reanalysis. Protein
  groundings and experimental scope remain bounded.
- Native PR and separate merge-group gates remain required; existing resolver/test
  skips retained. Corrected source retained by review-base/tubulin-family-boundaries-20261011.
links:
- https://github.com/CultureBotAI/CellStructureMech/issues/2234
- https://github.com/CultureBotAI/CellStructureMech/issues/2235
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261011T175546Z-phuz_spindle-audit
  relationship: Resolves exact predecessor findings without replacing the observation.
```
