# crescentin filament: whole-record scientific review

- Review: 20261011T185011Z-crescentin_filament-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T18:32:23Z
- Finished UTC: 2026-10-11T18:50:11Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Whole native record reviewed; concrete hierarchy and applicable evidence/provenance findings saved before curation.

## Scope And Provenance

Entire native YAML: identity, definition, synonyms, hierarchy/parthood, components and essentiality, taxa/examples, functions, every graph edge, evidence, discussions and both history surfaces.

Selection: One exact record of the 909-record goal; other records have separate coverage.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e6e0c667ee25463f158a36f5ba7484e88e4c7728.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:crescentin_filament | data/structures/cytoskeleton/crescentin_filament.yaml | maintained | crescentin filament |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | cellstructuremech:crescentin_filament | Actual deterministic check passed; scientific support assessed separately. |
| strict | passed | True | cellstructuremech:crescentin_filament | Actual deterministic check passed; scientific support assessed separately. |
| snippets | passed | True | cellstructuremech:crescentin_filament | No verbatim snippets; paraphrases assessed separately against inspected text. |
| history | passed | True | cellstructuremech:crescentin_filament | Actual deterministic check passed; scientific support assessed separately. |
| labels | passed | True | cellstructuremech:crescentin_filament | id↔label correspondence summary:<br>          OK_CANONICAL: 3544<br>            OK_SYNONYM: 50<br>          OK_EXCEPTION: 6<br>    SKIPPED_NO_ADAPTER: 603<br><br>✅ All id↔label pairs correspond. |
| traits | passed | True | cellstructuremech:crescentin_filament | Actual deterministic check passed; scientific support assessed separately. |
| curies | passed | True | cellstructuremech:crescentin_filament | [not exercised] BFO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] CHEBI: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] ComplexPortal: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] DOI: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] GO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] InterPro: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] NCBITaxon: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] PATO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] PMID: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] RO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] SO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] UO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] UniProtKB: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] DOI: DataCite was unreachable, so DOI:10.22002/D1.1355 was not exercised<br>resolver control: 14 resolver(s) could not be exercised because their authority was unreachable; the rest accept a known id and reject a fabricated one<br><br>identifier liveness summary:<br>  OK             4013<br>  SKIPPED         251<br><br>Every identifier resolves at its issuing authority. |
| reviews | passed | True | cellstructuremech:crescentin_filament | Actual deterministic check passed; scientific support assessed separately. |
| diff | passed | True | cellstructuremech:crescentin_filament | Actual deterministic check passed; scientific support assessed separately. |
| contract | passed | True | cellstructuremech:crescentin_filament | ....                                                                     [100%]<br>4 passed in 114.73s (0:01:54) |
| Exact-baseline native CI QC | passed | True | cellstructuremech:crescentin_filament | Exact-baseline full QC: 897 passed, 3 skipped. Not a new local full QC run. |

## Scientific And Domain Assessments

### Claim-by-claim biological scope

evidence: supported. Targets: cellstructuremech:crescentin_filament.

CreS constituent, Caulobacter species identity/example, concave-side localization, curvature function and all three NONMECHANISTIC graph edges are supported. Liu 2024 separates purified WT/SAT structures and cellular overexpression/truncation cryo-ET experiments; the record does not claim a native endogenous atomic reconstruction. Charbon 2009 abstract and the 2017 Woldemeskel/Goley review support assembly/localization and shape context. Prior #1260 species scope and replacement evidence remain preserved.

### Whole framework versus constituent fiber

grounding: concern. Targets: cellstructuremech:crescentin_filament.

Each record is an individual polymer, not the containing cytoskeleton.

### Unresolved identities and original curation

completeness: supported. Targets: cellstructuremech:crescentin_filament.

Label-only family groundings and optional empty fields are not defects. Essentiality describes the structural constituent rather than organism viability. Original discussions, prior issue rationale, dates and PROPOSED status must remain unchanged.

## Findings

### F1: Correct cytoskeleton is-a versus parthood

major / open / confirmed; issue key: crescentin-filament-cytoskeleton-is-a.

GO:0005856 is in parent_structures, asserting that this individual filament is a type of the entire cytoskeletal framework. Native rules and GO distinguish the fiber class from its containing framework.

### F2: Correct the Woldemeskel and Goley publication year

minor / open / confirmed; issue key: crescentin-filament-woldemeskel-publication-year.

Four active evidence notes describe the review as 2018. The exact DOI/PMID metadata and article front matter give electronic publication 27 March 2017 and print publication August 2017, volume 25 issue 8. The DOI and scientific claims are otherwise correct; the old #1260 event must remain append-only.

## Recommended Actions And Acceptance Checks

### A1

Correct cytoskeleton is-a versus parthood

- Use GO:0099513 as broader parent and GO:0005856 as part_of. Preserve the exact local filament identity and add precise authority evidence.
- Use guarded writer, append actual Codex EDIT history, preserve original discussions/history and PROPOSED status, and pass focused tests plus native QC.

### A2

Correct the Woldemeskel and Goley publication year

- Correct the four active notes to 2017 and append a clarification of the retained historical 2018 typo. Preserve original history and all biology.
- Use guarded writer, append actual Codex EDIT history, preserve original discussions/history and PROPOSED status, and pass focused tests plus native QC.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/crescentin_filament.yaml | context_only | Entire native YAML inspected before judgment. |
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

## Limits And Additional Notes

- Same-agent whole-native-record review, not independent human approval or raw-data reanalysis.
- Each evidence entry distinguishes full-text inspection from abstract-only support. PMC browser pages and the ParM supplemental document returned interstitials; empty/rate-limited responses were not scientific evidence. Secondary reviews remain secondary.
- A guessed MamK DOI resolved to a MamB/MamM paper and was rejected; the correct PMID/DOI was retrieved before use. No optional source-access gap alone is a finding.
- Exact-baseline full QC and actual scoped/global/contract checks completed; known resolver namespaces and three test skips retained. MreB automated snippet retrieval was NOT CHECKED, with three independently verified exact-text matches.
- No universal taxon prevalence, native stoichiometry or complete molecular mechanism is inferred from a model structure, heterologous expression, database match or domain homology.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T185011Z-crescentin_filament-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'crescentin filament: whole-record scientific review'
started_at: '2026-10-11T18:32:23Z'
finished_at: '2026-10-11T18:50:11Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent review, not independent human scientific approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Whole native record reviewed; concrete hierarchy and applicable evidence/provenance
  findings saved before curation.
source:
  git_revision: e6e0c667ee25463f158a36f5ba7484e88e4c7728
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
    sha256: 3dfa27495f59921dcffeeec704de58007abdc046ba94880f04f1716b0055474a
    role: context
  - path: data/structures/cytoskeleton/crescentin_filament.yaml
    sha256: 97605fef83a99a796c40fc2f423a8816cf9f5a79be34f59710efe3e02d96937d
    role: target
  - path: data/structures/cytoskeleton/mamk_filament.yaml
    sha256: e42eeee29c4e227048b2881bcbbc073a67f6f1ae133a8464c76257693c6812f7
    role: context
  - path: data/structures/cytoskeleton/mreb_filament.yaml
    sha256: 2d03a06bf7c994d73d3371701a00fe87ec9107d327d5bede0d53debda85f9d64
    role: context
  - path: data/structures/cytoskeleton/parm_filament.yaml
    sha256: 2fcfa9960498109111ebcf7579f906f8b0bc1d2206d2fabf64678ea399d31bd3
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
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
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
  description: 'Entire native YAML: identity, definition, synonyms, hierarchy/parthood,
    components and essentiality, taxa/examples, functions, every graph edge, evidence,
    discussions and both history surfaces.'
  selection: One exact record of the 909-record goal; other records have separate
    coverage.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:crescentin_filament
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:crescentin_filament
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/crescentin_filament.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T18:35:28Z to 2026-10-11T18:35:32Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:crescentin_filament
  command: .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/crescentin_filament.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T18:35:32Z to 2026-10-11T18:35:38Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - cellstructuremech:crescentin_filament
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/cytoskeleton/crescentin_filament.yaml
    --report /private/tmp/csm-review-20261011T183112Z/crescentin_filament-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: No verbatim snippets; paraphrases assessed separately against inspected
    text.
  scope_note: 2026-10-11T18:35:38Z to 2026-10-11T18:36:15Z; log SHA-256 08e7608d0335fe274a4dbfc3f88fd0ce8b255edb4ecd2053cef3ebf6fc1f1f13
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
  scope_note: 2026-10-11T18:36:15Z to 2026-10-11T18:36:36Z; log SHA-256 4f6b05d12a24e704b5b087418a3dec5d72f923f73be7080e8103d2b0be9094e0
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
  scope_note: 2026-10-11T18:36:36Z to 2026-10-11T18:38:40Z; log SHA-256 d423103555a6a5b538a7c811a73a29c24ed0e5a2eae00d1bb94715295f23f7cb
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
  scope_note: 2026-10-11T18:38:40Z to 2026-10-11T18:39:07Z; log SHA-256 553832e049eb99562adc0d8260a3f74f18342e6aa8261c4cbc33b824c4f6332c
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - cellstructuremech:crescentin_filament
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
  scope_note: 2026-10-11T18:39:07Z to 2026-10-11T18:39:50Z; log SHA-256 800d5c4ef6c7964ccbd1a80a4be5c5f7e04774af577c1544c94abaa18c2326b3
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
  scope_note: 2026-10-11T18:39:50Z to 2026-10-11T18:41:47Z; log SHA-256 9a9180e4d728d328eec8b0e9e54706b0561c680d2acb5e3b58cdf018e994d5f2
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
  scope_note: 2026-10-11T18:41:47Z to 2026-10-11T18:41:47Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- check_id: contract
  name: contract
  status: passed
  required: true
  target_ids:
  - cellstructuremech:crescentin_filament
  command: .venv/bin/python -m pytest -q tests/test_record_review_contract.py
  exit_code: 0
  expected_exit_code: 0
  summary: '....                                                                     [100%]

    4 passed in 114.73s (0:01:54)'
  scope_note: 2026-10-11T18:31:40Z to 2026-10-11T18:33:36Z; log SHA-256 f01416e078e46993bc47de3e252581e4c1a09a9d5eab8c3291ee0c0e2268ad87
- check_id: qc
  name: Exact-baseline native CI QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:crescentin_filament
  command: gh run view 38163493641 --repo CultureBotAI/CellStructureMech --log
  exit_code: 0
  expected_exit_code: 0
  summary: 'Exact-baseline full QC: 897 passed, 3 skipped. Not a new local full QC
    run.'
  scope_note: https://github.com/CultureBotAI/CellStructureMech/actions/runs/38163493641
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/crescentin_filament.yaml
  accessed_at: '2026-10-11T18:50:11Z'
  snapshot_sha256: 97605fef83a99a796c40fc2f423a8816cf9f5a79be34f59710efe3e02d96937d
  support: context_only
  summary: Entire native YAML inspected before judgment.
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
assessments:
- assessment_id: biology
  area: evidence
  topic: Claim-by-claim biological scope
  outcome: supported
  target_ids:
  - cellstructuremech:crescentin_filament
  evidence_ids:
  - record
  - paper-2
  - paper-10
  - paper-12
  summary: 'CreS constituent, Caulobacter species identity/example, concave-side localization,
    curvature function and all three NONMECHANISTIC graph edges are supported. Liu
    2024 separates purified WT/SAT structures and cellular overexpression/truncation
    cryo-ET experiments; the record does not claim a native endogenous atomic reconstruction.
    Charbon 2009 abstract and the 2017 Woldemeskel/Goley review support assembly/localization
    and shape context. Prior #1260 species scope and replacement evidence remain preserved.'
- assessment_id: hierarchy
  area: grounding
  topic: Whole framework versus constituent fiber
  outcome: concern
  target_ids:
  - cellstructuremech:crescentin_filament
  evidence_ids:
  - record
  - go
  - rules
  summary: Each record is an individual polymer, not the containing cytoskeleton.
- assessment_id: provenance
  area: completeness
  topic: Unresolved identities and original curation
  outcome: supported
  target_ids:
  - cellstructuremech:crescentin_filament
  evidence_ids:
  - record
  - history
  summary: Label-only family groundings and optional empty fields are not defects.
    Essentiality describes the structural constituent rather than organism viability.
    Original discussions, prior issue rationale, dates and PROPOSED status must remain
    unchanged.
findings:
- finding_id: F1
  issue_key: crescentin-filament-cytoskeleton-is-a
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Correct cytoskeleton is-a versus parthood
  description: GO:0005856 is in parent_structures, asserting that this individual
    filament is a type of the entire cytoskeletal framework. Native rules and GO distinguish
    the fiber class from its containing framework.
  target_ids:
  - cellstructuremech:crescentin_filament
  field_paths:
  - parent_structures
  evidence_ids:
  - record
  - go
  - rules
  - schema
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/crescentin_filament.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: major
  normalization_reason: Incorrect scientific hierarchy or scope.
- finding_id: F2
  issue_key: crescentin-filament-woldemeskel-publication-year
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the Woldemeskel and Goley publication year
  description: 'Four active evidence notes describe the review as 2018. The exact
    DOI/PMID metadata and article front matter give electronic publication 27 March
    2017 and print publication August 2017, volume 25 issue 8. The DOI and scientific
    claims are otherwise correct; the old #1260 event must remain append-only.'
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
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/crescentin_filament.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: minor
  normalization_reason: Bounded citation/provenance defect; underlying biology is
    supported.
actions:
- action_id: A1
  description: Correct cytoskeleton is-a versus parthood
  finding_ids:
  - F1
  target_ids:
  - cellstructuremech:crescentin_filament
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/crescentin_filament.yaml
    role: maintained scientific record
  acceptance_checks:
  - Use GO:0099513 as broader parent and GO:0005856 as part_of. Preserve the exact
    local filament identity and add precise authority evidence.
  - Use guarded writer, append actual Codex EDIT history, preserve original discussions/history
    and PROPOSED status, and pass focused tests plus native QC.
- action_id: A2
  description: Correct the Woldemeskel and Goley publication year
  finding_ids:
  - F2
  target_ids:
  - cellstructuremech:crescentin_filament
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/crescentin_filament.yaml
    role: maintained scientific record
  acceptance_checks:
  - Correct the four active notes to 2017 and append a clarification of the retained
    historical 2018 typo. Preserve original history and all biology.
  - Use guarded writer, append actual Codex EDIT history, preserve original discussions/history
    and PROPOSED status, and pass focused tests plus native QC.
limitations:
- Same-agent whole-native-record review, not independent human approval or raw-data
  reanalysis.
- Each evidence entry distinguishes full-text inspection from abstract-only support.
  PMC browser pages and the ParM supplemental document returned interstitials; empty/rate-limited
  responses were not scientific evidence. Secondary reviews remain secondary.
- A guessed MamK DOI resolved to a MamB/MamM paper and was rejected; the correct PMID/DOI
  was retrieved before use. No optional source-access gap alone is a finding.
- Exact-baseline full QC and actual scoped/global/contract checks completed; known
  resolver namespaces and three test skips retained. MreB automated snippet retrieval
  was NOT CHECKED, with three independently verified exact-text matches.
- No universal taxon prevalence, native stoichiometry or complete molecular mechanism
  is inferred from a model structure, heterologous expression, database match or domain
  homology.
```
