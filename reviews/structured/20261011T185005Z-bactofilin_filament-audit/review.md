# bactofilin filament: whole-record scientific review

- Review: 20261011T185005Z-bactofilin_filament-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T18:32:19Z
- Finished UTC: 2026-10-11T18:50:05Z
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
| cellstructuremech:bactofilin_filament | data/structures/cytoskeleton/bactofilin_filament.yaml | maintained | bactofilin filament |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | cellstructuremech:bactofilin_filament | Actual deterministic check passed; scientific support assessed separately. |
| strict | passed | True | cellstructuremech:bactofilin_filament | Actual deterministic check passed; scientific support assessed separately. |
| snippets | passed | True | cellstructuremech:bactofilin_filament | No verbatim snippets; paraphrases assessed separately against inspected text. |
| history | passed | True | cellstructuremech:bactofilin_filament | Actual deterministic check passed; scientific support assessed separately. |
| labels | passed | True | cellstructuremech:bactofilin_filament | id↔label correspondence summary:<br>          OK_CANONICAL: 3544<br>            OK_SYNONYM: 50<br>          OK_EXCEPTION: 6<br>    SKIPPED_NO_ADAPTER: 603<br><br>✅ All id↔label pairs correspond. |
| traits | passed | True | cellstructuremech:bactofilin_filament | Actual deterministic check passed; scientific support assessed separately. |
| curies | passed | True | cellstructuremech:bactofilin_filament | [not exercised] BFO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] CHEBI: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] ComplexPortal: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] DOI: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] GO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] InterPro: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] NCBITaxon: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] PATO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] PMID: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] RO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] SO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] UO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] UniProtKB: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] DOI: DataCite was unreachable, so DOI:10.22002/D1.1355 was not exercised<br>resolver control: 14 resolver(s) could not be exercised because their authority was unreachable; the rest accept a known id and reject a fabricated one<br><br>identifier liveness summary:<br>  OK             4013<br>  SKIPPED         251<br><br>Every identifier resolves at its issuing authority. |
| reviews | passed | True | cellstructuremech:bactofilin_filament | Actual deterministic check passed; scientific support assessed separately. |
| diff | passed | True | cellstructuremech:bactofilin_filament | Actual deterministic check passed; scientific support assessed separately. |
| contract | passed | True | cellstructuremech:bactofilin_filament | ....                                                                     [100%]<br>4 passed in 114.73s (0:01:54) |
| Exact-baseline native CI QC | passed | True | cellstructuremech:bactofilin_filament | Exact-baseline full QC: 897 passed, 3 skipped. Not a new local full QC run. |

## Scientific And Domain Assessments

### Claim-by-claim biological scope

evidence: supported. Targets: cellstructuremech:bactofilin_filament.

Bactofilin polymer and beta-helical architecture are supported. Caulobacter BacA/BacB, NA1000 example and all four polar-scaffold/PbpC/stalk graph edges are supported by Kuhn 2010 Results and Methods. The double deletion disrupts PbpC localization; this collective claim is not changed into individual BacA/BacB indispensability. PiBac in vitro polymerization refutes bacteria-specific family wording but does not establish native oomycete function or archaeal polymerization.

### Whole framework versus constituent fiber

grounding: concern. Targets: cellstructuremech:bactofilin_filament.

Each record is an individual polymer, not the containing cytoskeleton.

### Unresolved identities and original curation

completeness: supported. Targets: cellstructuremech:bactofilin_filament.

Label-only family groundings and optional empty fields are not defects. Essentiality describes the structural constituent rather than organism viability. Original discussions, prior issue rationale, dates and PROPOSED status must remain unchanged.

## Findings

### F1: Correct cytoskeleton is-a versus parthood

major / open / confirmed; issue key: bactofilin-filament-cytoskeleton-is-a.

GO:0005856 is in parent_structures, asserting that this individual filament is a type of the entire cytoskeletal framework. Native rules and GO distinguish the fiber class from its containing framework.

### F2: Remove bacteria-specific bactofilin family exclusivity

major / open / confirmed; issue key: bactofilin-filament-bacterial-exclusivity.

The component calls bactofilins bacteria-specific and the generic definition is bacterial-only. The already cited Deng 2019 paper experimentally polymerizes recombinant Phytophthora infestans PiBac. It also reports archaeal domain hits, which are not themselves polymerization evidence. Family exclusivity contradicts the inspected experiment.

## Recommended Actions And Acceptance Checks

### A1

Correct cytoskeleton is-a versus parthood

- Use GO:0099513 as broader parent and GO:0005856 as part_of. Preserve the exact local filament identity and add precise authority evidence.
- Use guarded writer, append actual Codex EDIT history, preserve original discussions/history and PROPOSED status, and pass focused tests plus native QC.

### A2

Remove bacteria-specific bactofilin family exclusivity

- Remove exclusive family wording, cite the 2019 architecture study and append a boundary discussion. Retain demonstrated bacterial occurrence and Caulobacter function; do not add unverified native oomycete or archaeal occurrences.
- Use guarded writer, append actual Codex EDIT history, preserve original discussions/history and PROPOSED status, and pass focused tests plus native QC.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/bactofilin_filament.yaml | context_only | Entire native YAML inspected before judgment. |
| rules | docs/CURATION.md | context_only | Fiber is-a versus containing cytoskeleton part_of; narrow claim-local evidence. |
| schema | docs/SCHEMA.md | context_only | Hierarchy and parthood field contracts. |
| history | /private/tmp/csm-review-20261011T183112Z/bactofilin_filament-discussion-history.json | context_only | All committed discussion/inline-history versions inspected. |
| predecessors | /private/tmp/csm-review-20261011T183112Z/exact-target-predecessors.json | context_only | Ignored-inclusive canonical search: no exact-target predecessor. |
| identity | /private/tmp/csm-review-20261011T183112Z/identity-matches.json | context_only | Ignored-inclusive identity enumeration; separate elongasome/magnetosome identities retained. |
| issues | /private/tmp/csm-review-20261011T183112Z/bactofilin-all-issues.log | context_only | All-state slug/label issue searches and relevant earlier issues inspected. |
| adapter | /private/tmp/csm-review-20261011T183112Z/adapter.log | context_only | Inventory checked; absent coverage is not biological absence. |
| history-0 | history/records/bactofilin_filament/2026-09-11T101347Z-codex-4f3727.yaml | context_only | Original append-only event inspected. |
| history-1 | history/records/bactofilin_filament/2026-09-11T102158Z-claude-code-cba182.yaml | context_only | Original append-only event inspected. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005856,GO:0099513,GO:0008360,GO:0009252,GO:0110143; GO:0005856 and GO:0099513 definitions and typed parthood | supports | The framework contains polymeric cytoskeletal fibers; a fiber is not the whole framework. |
| paper-3 | DOI:10.1038/emboj.2009.358; Relevant Results/Discussion, methods and figure captions | supports | Inspected primary experimental evidence. Full text inspected for native claims. |
| paper-8 | DOI:10.1038/s41564-019-0544-0; Relevant Results/Discussion, methods and figure captions | supports | Inspected primary experimental evidence. Full text inspected for native claims. |
| paper-9 | DOI:10.1073/pnas.1418450112; Exact DOI/PMID metadata and complete abstract only | supports | Inspected primary experimental evidence. Full text was not obtained; abstract-level support only. |
| taxon-2 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2; TaxId, scientificName, rank and aliases | supports | Exact taxon identity verified; taxonomy is not proof of structural occurrence. |
| taxon-155892 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/155892; TaxId, scientificName, rank and aliases | supports | Exact taxon identity verified; taxonomy is not proof of structural occurrence. |
| taxon-565050 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/565050; TaxId, scientificName, rank and aliases | supports | Exact taxon identity verified; taxonomy is not proof of structural occurrence. |

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
review_id: 20261011T185005Z-bactofilin_filament-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'bactofilin filament: whole-record scientific review'
started_at: '2026-10-11T18:32:19Z'
finished_at: '2026-10-11T18:50:05Z'
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
    role: target
  - path: data/structures/cytoskeleton/crescentin_filament.yaml
    sha256: 97605fef83a99a796c40fc2f423a8816cf9f5a79be34f59710efe3e02d96937d
    role: context
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
  - path: history/records/bactofilin_filament/2026-09-11T101347Z-codex-4f3727.yaml
    sha256: 3fec9611e094c5fc2587efd5c49e1e43c9595959999df0fcc7e5bfc84ff86963
    role: context
  - path: history/records/bactofilin_filament/2026-09-11T102158Z-claude-code-cba182.yaml
    sha256: fef1f52b752ad1289622447195bc1748e39387f591572031c61f60893bb9bf83
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
- target_id: cellstructuremech:bactofilin_filament
  path: data/structures/cytoskeleton/bactofilin_filament.yaml
  label: bactofilin filament
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/bactofilin_filament.yaml
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
  - cellstructuremech:bactofilin_filament
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:bactofilin_filament
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/bactofilin_filament.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T18:34:52Z to 2026-10-11T18:34:55Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:bactofilin_filament
  command: .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/bactofilin_filament.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T18:34:55Z to 2026-10-11T18:34:59Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - cellstructuremech:bactofilin_filament
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/cytoskeleton/bactofilin_filament.yaml
    --report /private/tmp/csm-review-20261011T183112Z/bactofilin_filament-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: No verbatim snippets; paraphrases assessed separately against inspected
    text.
  scope_note: 2026-10-11T18:34:59Z to 2026-10-11T18:35:28Z; log SHA-256 d6f225b4d128d32d69af0f0dcf2a64afd9da9b41fabcafb7713c341de51cf125
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - cellstructuremech:bactofilin_filament
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
  - cellstructuremech:bactofilin_filament
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
  - cellstructuremech:bactofilin_filament
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
  - cellstructuremech:bactofilin_filament
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
  - cellstructuremech:bactofilin_filament
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
  - cellstructuremech:bactofilin_filament
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
  - cellstructuremech:bactofilin_filament
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
  - cellstructuremech:bactofilin_filament
  command: gh run view 38163493641 --repo CultureBotAI/CellStructureMech --log
  exit_code: 0
  expected_exit_code: 0
  summary: 'Exact-baseline full QC: 897 passed, 3 skipped. Not a new local full QC
    run.'
  scope_note: https://github.com/CultureBotAI/CellStructureMech/actions/runs/38163493641
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/bactofilin_filament.yaml
  accessed_at: '2026-10-11T18:50:05Z'
  snapshot_sha256: 3dfa27495f59921dcffeeec704de58007abdc046ba94880f04f1716b0055474a
  support: context_only
  summary: Entire native YAML inspected before judgment.
- evidence_id: rules
  kind: record_content
  reference: docs/CURATION.md
  accessed_at: '2026-10-11T18:50:05Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  support: context_only
  summary: Fiber is-a versus containing cytoskeleton part_of; narrow claim-local evidence.
- evidence_id: schema
  kind: record_content
  reference: docs/SCHEMA.md
  accessed_at: '2026-10-11T18:50:05Z'
  snapshot_sha256: 07b8f936a553a45cc6e8dba924c21e6af48c81b3866725efeb00c8183f0c75a2
  support: context_only
  summary: Hierarchy and parthood field contracts.
- evidence_id: history
  kind: record_content
  reference: /private/tmp/csm-review-20261011T183112Z/bactofilin_filament-discussion-history.json
  accessed_at: '2026-10-11T18:50:05Z'
  snapshot_sha256: 404f02fc4ed8128b62461cbb54edd4ed7e7cad3781886d1bca46461ff159f6f7
  support: context_only
  summary: All committed discussion/inline-history versions inspected.
- evidence_id: predecessors
  kind: validation
  reference: /private/tmp/csm-review-20261011T183112Z/exact-target-predecessors.json
  accessed_at: '2026-10-11T18:50:05Z'
  snapshot_sha256: f7bb865579cd8ac8088b01d712760c8b12268a7fb70bc59b6af68f5cf9d7cc19
  support: context_only
  summary: 'Ignored-inclusive canonical search: no exact-target predecessor.'
- evidence_id: identity
  kind: validation
  reference: /private/tmp/csm-review-20261011T183112Z/identity-matches.json
  accessed_at: '2026-10-11T18:50:05Z'
  snapshot_sha256: 2b7b7369dae8179ab0188eb431905ef8360ea1f16d25c67c9c95567de7ce3006
  support: context_only
  summary: Ignored-inclusive identity enumeration; separate elongasome/magnetosome
    identities retained.
- evidence_id: issues
  kind: validation
  reference: /private/tmp/csm-review-20261011T183112Z/bactofilin-all-issues.log
  accessed_at: '2026-10-11T18:50:05Z'
  snapshot_sha256: c3ed0b6e0007099cbc662ae954ebfbb2a0bb14e10e3fe932a128980976bb593f
  support: context_only
  summary: All-state slug/label issue searches and relevant earlier issues inspected.
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/csm-review-20261011T183112Z/adapter.log
  accessed_at: '2026-10-11T18:50:05Z'
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
  support: context_only
  summary: Inventory checked; absent coverage is not biological absence.
- evidence_id: history-0
  kind: record_content
  reference: history/records/bactofilin_filament/2026-09-11T101347Z-codex-4f3727.yaml
  accessed_at: '2026-10-11T18:50:05Z'
  snapshot_sha256: 3fec9611e094c5fc2587efd5c49e1e43c9595959999df0fcc7e5bfc84ff86963
  support: context_only
  summary: Original append-only event inspected.
- evidence_id: history-1
  kind: record_content
  reference: history/records/bactofilin_filament/2026-09-11T102158Z-claude-code-cba182.yaml
  accessed_at: '2026-10-11T18:50:05Z'
  snapshot_sha256: fef1f52b752ad1289622447195bc1748e39387f591572031c61f60893bb9bf83
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
- evidence_id: paper-3
  kind: primary_source
  reference: DOI:10.1038/emboj.2009.358
  locator: Relevant Results/Discussion, methods and figure captions
  accessed_at: '2026-10-11T18:39:48Z'
  snapshot_sha256: 88dd4a98f1ec644334a77bb75acb9c3d284ef31c5a751f1e6955bec429106cf1
  support: supports
  summary: Inspected primary experimental evidence. Full text inspected for native
    claims.
- evidence_id: paper-8
  kind: primary_source
  reference: DOI:10.1038/s41564-019-0544-0
  locator: Relevant Results/Discussion, methods and figure captions
  accessed_at: '2026-10-11T18:36:46Z'
  snapshot_sha256: 5b808304d6eec3f7fb8e7c9ef6735b94e660f8e13d2f4aa94162bbcbfe8b5cb4
  support: supports
  summary: Inspected primary experimental evidence. Full text inspected for native
    claims.
- evidence_id: paper-9
  kind: primary_source
  reference: DOI:10.1073/pnas.1418450112
  locator: Exact DOI/PMID metadata and complete abstract only
  accessed_at: '2026-10-11T18:32:07Z'
  snapshot_sha256: 3965258c4d5fa9db5fe886c98be06fb48e97c3040ffd79d4ab7ebf731133438e
  support: supports
  summary: Inspected primary experimental evidence. Full text was not obtained; abstract-level
    support only.
- evidence_id: taxon-2
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2
  locator: TaxId, scientificName, rank and aliases
  accessed_at: '2026-10-11T18:34:22Z'
  snapshot_sha256: 314bd7723b8dea04f1840809fb74e06c514664fba9c6a0619e8f12e2a6dceef1
  support: supports
  summary: Exact taxon identity verified; taxonomy is not proof of structural occurrence.
- evidence_id: taxon-155892
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/155892
  locator: TaxId, scientificName, rank and aliases
  accessed_at: '2026-10-11T18:34:29Z'
  snapshot_sha256: 5e0fd272e1c0461a6f0dc3a10151587eb27de65a6ebebe95bf9adb62d57e215e
  support: supports
  summary: Exact taxon identity verified; taxonomy is not proof of structural occurrence.
- evidence_id: taxon-565050
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/565050
  locator: TaxId, scientificName, rank and aliases
  accessed_at: '2026-10-11T18:34:30Z'
  snapshot_sha256: d3c932efaddd17db870d54241a8c2441cc71fa808cad435ef9bfd60976641685
  support: supports
  summary: Exact taxon identity verified; taxonomy is not proof of structural occurrence.
assessments:
- assessment_id: biology
  area: evidence
  topic: Claim-by-claim biological scope
  outcome: supported
  target_ids:
  - cellstructuremech:bactofilin_filament
  evidence_ids:
  - record
  - paper-3
  - paper-8
  - paper-9
  summary: Bactofilin polymer and beta-helical architecture are supported. Caulobacter
    BacA/BacB, NA1000 example and all four polar-scaffold/PbpC/stalk graph edges are
    supported by Kuhn 2010 Results and Methods. The double deletion disrupts PbpC
    localization; this collective claim is not changed into individual BacA/BacB indispensability.
    PiBac in vitro polymerization refutes bacteria-specific family wording but does
    not establish native oomycete function or archaeal polymerization.
- assessment_id: hierarchy
  area: grounding
  topic: Whole framework versus constituent fiber
  outcome: concern
  target_ids:
  - cellstructuremech:bactofilin_filament
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
  - cellstructuremech:bactofilin_filament
  evidence_ids:
  - record
  - history
  summary: Label-only family groundings and optional empty fields are not defects.
    Essentiality describes the structural constituent rather than organism viability.
    Original discussions, prior issue rationale, dates and PROPOSED status must remain
    unchanged.
findings:
- finding_id: F1
  issue_key: bactofilin-filament-cytoskeleton-is-a
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Correct cytoskeleton is-a versus parthood
  description: GO:0005856 is in parent_structures, asserting that this individual
    filament is a type of the entire cytoskeletal framework. Native rules and GO distinguish
    the fiber class from its containing framework.
  target_ids:
  - cellstructuremech:bactofilin_filament
  field_paths:
  - parent_structures
  evidence_ids:
  - record
  - go
  - rules
  - schema
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/bactofilin_filament.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: major
  normalization_reason: Incorrect scientific hierarchy or scope.
- finding_id: F2
  issue_key: bactofilin-filament-bacterial-exclusivity
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Remove bacteria-specific bactofilin family exclusivity
  description: The component calls bactofilins bacteria-specific and the generic definition
    is bacterial-only. The already cited Deng 2019 paper experimentally polymerizes
    recombinant Phytophthora infestans PiBac. It also reports archaeal domain hits,
    which are not themselves polymerization evidence. Family exclusivity contradicts
    the inspected experiment.
  target_ids:
  - cellstructuremech:bactofilin_filament
  field_paths:
  - definition
  - definition_source
  - components[0].role
  evidence_ids:
  - record
  - paper-3
  - paper-8
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/bactofilin_filament.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: major
  normalization_reason: Incorrect scientific hierarchy or scope.
actions:
- action_id: A1
  description: Correct cytoskeleton is-a versus parthood
  finding_ids:
  - F1
  target_ids:
  - cellstructuremech:bactofilin_filament
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/bactofilin_filament.yaml
    role: maintained scientific record
  acceptance_checks:
  - Use GO:0099513 as broader parent and GO:0005856 as part_of. Preserve the exact
    local filament identity and add precise authority evidence.
  - Use guarded writer, append actual Codex EDIT history, preserve original discussions/history
    and PROPOSED status, and pass focused tests plus native QC.
- action_id: A2
  description: Remove bacteria-specific bactofilin family exclusivity
  finding_ids:
  - F2
  target_ids:
  - cellstructuremech:bactofilin_filament
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/bactofilin_filament.yaml
    role: maintained scientific record
  acceptance_checks:
  - Remove exclusive family wording, cite the 2019 architecture study and append a
    boundary discussion. Retain demonstrated bacterial occurrence and Caulobacter
    function; do not add unverified native oomycete or archaeal occurrences.
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
