# PhuZ spindle: whole-record scientific review

- Review: 20261011T175546Z-phuz_spindle-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T17:47:37Z
- Finished UTC: 2026-10-11T17:55:46Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Whole record reviewed; concrete hierarchy and, for PhuZ, structure-boundary findings saved before curation.

## Scope And Provenance

Entire native YAML: identity, definition, synonym scope, mereology, component roles and essentiality, taxa/examples, functions, every graph edge, sources, discussions and both history surfaces.

Selection: One exact member of the five-record tubulin-family cohort in the 909-record goal.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a8bab45f6868c61fad49550ea05bc10167c27689.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:phuz_spindle | data/structures/cytoskeleton/phuz_spindle.yaml | maintained | PhuZ spindle |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | cellstructuremech:phuz_spindle | Actual deterministic check passed; scientific support assessed separately. |
| strict | passed | True | cellstructuremech:phuz_spindle | Actual deterministic check passed; scientific support assessed separately. |
| snippets | passed | True | cellstructuremech:phuz_spindle | No verbatim snippets; paraphrases assessed separately against inspected text. |
| history | passed | True | cellstructuremech:phuz_spindle | Actual deterministic check passed; scientific support assessed separately. |
| labels | passed | True | cellstructuremech:phuz_spindle | id↔label correspondence summary:<br>          OK_CANONICAL: 3544<br>            OK_SYNONYM: 50<br>          OK_EXCEPTION: 6<br>    SKIPPED_NO_ADAPTER: 603<br><br>✅ All id↔label pairs correspond. |
| traits | passed | True | cellstructuremech:phuz_spindle | Actual deterministic check passed; scientific support assessed separately. |
| curies | passed | True | cellstructuremech:phuz_spindle | [not exercised] BFO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] CHEBI: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] ComplexPortal: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] DOI: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] GO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] InterPro: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] NCBITaxon: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] PATO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] PMID: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] RO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] SO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] UO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] UniProtKB: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] DOI: DataCite was unreachable, so DOI:10.22002/D1.1355 was not exercised<br>resolver control: 14 resolver(s) could not be exercised because their authority was unreachable; the rest accept a known id and reject a fabricated one<br><br>identifier liveness summary:<br>  OK             4014<br>  SKIPPED         251<br><br>Every identifier resolves at its issuing authority. |
| reviews | passed | True | cellstructuremech:phuz_spindle | Actual deterministic check passed; scientific support assessed separately. |
| diff | passed | True | cellstructuremech:phuz_spindle | Actual deterministic check passed; scientific support assessed separately. |
| contract | passed | True | cellstructuremech:phuz_spindle | ....                                                                     [100%]<br>4 passed in 84.17s (0:01:24) |
| Exact-baseline native CI QC | passed | True | cellstructuremech:phuz_spindle | Exact baseline merge-group full QC passed: 883 passed, 3 skipped. Not a new local full QC run. |

## Scientific And Domain Assessments

### Retained identity, component, taxon and graph scope

evidence: supported. Targets: cellstructuremech:phuz_spindle.

Erb 2014 and Chaikeeratisak 2017 support phage-encoded PhuZ polymerization, bipolar spindle organization and nucleus positioning. PhuZ is an essential spindle constituent, not asserted essential for phage viability. Chimallin shell and nucleus are distinct cargo, not tubulin constituents. All three positioning graph edges remain supported in Pseudomonas phage experiments; the Goslar vortex is outside this spindle identity.

### Whole framework versus constituent system

grounding: concern. Targets: cellstructuremech:phuz_spindle.

The record places GO:0005856 cytoskeleton in parent_structures, asserting that this filament system is a type of the whole cellular framework. The native schema and CURATION rules distinguish is-a from part_of; GO:0099513 likewise describes a polymeric fiber as a component of the cytoskeleton. This is a semantic hierarchy error, even though all identifiers resolve.

### Spindle versus vortex

evidence: concern. Targets: cellstructuremech:phuz_spindle.

The spindle definition and positioning graph retain a bipolar nucleus-positioning identity, but Goslar taxonomic/example rows, component role and rotation function include a distinct vortex. Birkholz 2022 explicitly contrasts this array with a bipolar spindle and finds no midcell-positioning role. Earlier #481/#482 aligned Goslar evidence with the component but did not resolve the record identity mismatch. Preserve that history while narrowing the active spindle claims.

### Unresolved molecular details and provenance

completeness: supported. Targets: cellstructuremech:phuz_spindle.

No exact protein accession, universal copy number, quantitative property, image, trait or pathway assertion is invented. Label-only grounding tasks and optional empty fields are not defects. Prior discussions and curation events remain provenance, not authorization to promote PROPOSED.

## Findings

### F1: Correct cytoskeleton is-a versus parthood

major / open / confirmed; issue key: phuz-spindle-cytoskeleton-is-a.

The record places GO:0005856 cytoskeleton in parent_structures, asserting that this filament system is a type of the whole cellular framework. The native schema and CURATION rules distinguish is-a from part_of; GO:0099513 likewise describes a polymeric fiber as a component of the cytoskeleton. This is a semantic hierarchy error, even though all identifiers resolve.

### F2: Separate the Goslar vortex from the PhuZ spindle

major / open / confirmed; issue key: phuz-spindle-goslar-vortex-boundary.

The spindle definition and positioning graph retain a bipolar nucleus-positioning identity, but Goslar taxonomic/example rows, component role and rotation function include a distinct vortex. Birkholz 2022 explicitly contrasts this array with a bipolar spindle and finds no midcell-positioning role. Earlier #481/#482 aligned Goslar evidence with the component but did not resolve the record identity mismatch. Preserve that history while narrowing the active spindle claims.

## Recommended Actions And Acceptance Checks

### A1

Correct cytoskeleton is-a versus parthood

- Move GO:0005856 to part_of. For the BtubAB, CetZ and TubZ polymer records use GO:0099513 as the broader fiber parent; for the multi-filament PhuZ spindle retain parthood without forcing it into a single-fiber class. Preserve local identities and cite the precise ontology scope.
- Guarded writer, actual Codex EDIT history, original discussion/history preservation, PROPOSED status, focused regressions, generated artifacts and native QC.

### A2

Separate the Goslar vortex from the PhuZ spindle

- Retain the spindle identifier/label and positioning graph. Remove Goslar as a spindle occurrence/example and vortex-specific component/function claims. Preserve Birkholz evidence in a new explicit boundary discussion; retain rotation only with primary spindle evidence, such as Chaikeeratisak Science 2017 Figure 1. Do not claim every phage nucleus needs a spindle or that rotation is unique to vortices.
- Guarded writer, actual Codex EDIT history, original discussion/history preservation, PROPOSED status, focused regressions, generated artifacts and native QC.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/phuz_spindle.yaml | context_only | Entire native YAML inspected before judgement. |
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

## Limits And Additional Notes

- Same-agent whole-native-record review, not independent approval or raw-data reanalysis.
- Europe PMC fullTextXML returned HTTP 500 for several papers; complete official PMC HTML was retrieved instead. Source metadata alone and web interstitials were not used as full text.
- Exact-baseline CI supplies full QC; actual local schema/strict/snippet/global/contract checks ran separately. Existing resolver namespaces and three test skips remain explicit.
- The generic microtubule record is assessed separately in operational goal coverage; no clean review bundle is created. Experimental models, species versus strain scope, and unresolved exact protein groundings remain bounded.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T175546Z-phuz_spindle-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'PhuZ spindle: whole-record scientific review'
started_at: '2026-10-11T17:47:37Z'
finished_at: '2026-10-11T17:55:46Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent review; not independent human scientific approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Whole record reviewed; concrete hierarchy and, for PhuZ, structure-boundary
  findings saved before curation.
source:
  git_revision: a8bab45f6868c61fad49550ea05bc10167c27689
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
    sha256: a92bfffd5e2ac9594d505cdbe5f67999861ea8fa85c00a602b6ff8be3e30864a
    role: context
  - path: data/structures/cytoskeleton/cetz_filament.yaml
    sha256: 5c86011dc09b711a9b4006aca1035e43905d852a2b4f04a9de0b6cf440244ec7
    role: context
  - path: data/structures/cytoskeleton/microtubule.yaml
    sha256: 29404191864964cf5b86c3894c7b942d63b83fc4bb1b6b461d7677baad6af305
    role: context
  - path: data/structures/cytoskeleton/phuz_spindle.yaml
    sha256: a0cd618df5afacc0504bdee6fdaea6eda424b16b3246319de49e93da1970b910
    role: target
  - path: data/structures/cytoskeleton/tubz_filament.yaml
    sha256: 0663d5846cde80b8afd93d07909b3c472ea093dec17c4f9754e9c3f0d790904f
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
- target_id: cellstructuremech:phuz_spindle
  path: data/structures/cytoskeleton/phuz_spindle.yaml
  label: PhuZ spindle
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/phuz_spindle.yaml
    role: maintained scientific record
scope:
  description: 'Entire native YAML: identity, definition, synonym scope, mereology,
    component roles and essentiality, taxa/examples, functions, every graph edge,
    sources, discussions and both history surfaces.'
  selection: One exact member of the five-record tubulin-family cohort in the 909-record
    goal.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:phuz_spindle
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:phuz_spindle
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/phuz_spindle.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T17:50:22Z to 2026-10-11T17:50:25Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:phuz_spindle
  command: .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/phuz_spindle.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T17:50:25Z to 2026-10-11T17:50:29Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - cellstructuremech:phuz_spindle
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/cytoskeleton/phuz_spindle.yaml
    --report /private/tmp/csm-review-20261011T174605Z/phuz_spindle-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: No verbatim snippets; paraphrases assessed separately against inspected
    text.
  scope_note: 2026-10-11T17:50:29Z to 2026-10-11T17:50:54Z; log SHA-256 5d285691367d6e71d96725abf83a48d0a11d8199572fcb8455e27b6ef3c4c4be
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
  scope_note: 2026-10-11T17:50:54Z to 2026-10-11T17:51:10Z; log SHA-256 a454941f6e4cdaf7e2a2bef570001bfff59209562b91d4bfa67737b7f11fbf47
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
  scope_note: 2026-10-11T17:51:10Z to 2026-10-11T17:52:44Z; log SHA-256 d423103555a6a5b538a7c811a73a29c24ed0e5a2eae00d1bb94715295f23f7cb
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
  scope_note: 2026-10-11T17:52:44Z to 2026-10-11T17:53:08Z; log SHA-256 553832e049eb99562adc0d8260a3f74f18342e6aa8261c4cbc33b824c4f6332c
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
    \ one\n\nidentifier liveness summary:\n  OK             4014\n  SKIPPED      \
    \   251\n\nEvery identifier resolves at its issuing authority."
  scope_note: 2026-10-11T17:53:08Z to 2026-10-11T17:53:35Z; log SHA-256 65fa87dd6c59c0cf9ee029739b96f5fbea1c050c8475a3a461f9503646604183
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
  scope_note: 2026-10-11T17:53:35Z to 2026-10-11T17:55:02Z; log SHA-256 c24b0d38ae591be95bfaf2343fc38afa87f41a7b6b113b29cdbb4d32784f9e79
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
  scope_note: 2026-10-11T17:55:02Z to 2026-10-11T17:55:02Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- check_id: contract
  name: contract
  status: passed
  required: true
  target_ids:
  - cellstructuremech:phuz_spindle
  command: .venv/bin/python -m pytest -q tests/test_record_review_contract.py
  exit_code: 0
  expected_exit_code: 0
  summary: '....                                                                     [100%]

    4 passed in 84.17s (0:01:24)'
  scope_note: 2026-10-11T17:47:02Z to 2026-10-11T17:48:27Z; log SHA-256 95cd3e5e3af25a23d0d553eac0fae420249f5d090cb99535ef8f07366ce149b0
- check_id: qc
  name: Exact-baseline native CI QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:phuz_spindle
  command: gh run view 38160393937 --repo CultureBotAI/CellStructureMech --log
  exit_code: 0
  expected_exit_code: 0
  summary: 'Exact baseline merge-group full QC passed: 883 passed, 3 skipped. Not
    a new local full QC run.'
  scope_note: https://github.com/CultureBotAI/CellStructureMech/actions/runs/38160393937
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/phuz_spindle.yaml
  accessed_at: '2026-10-11T17:55:46Z'
  snapshot_sha256: a0cd618df5afacc0504bdee6fdaea6eda424b16b3246319de49e93da1970b910
  support: context_only
  summary: Entire native YAML inspected before judgement.
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
assessments:
- assessment_id: biology
  area: evidence
  topic: Retained identity, component, taxon and graph scope
  outcome: supported
  target_ids:
  - cellstructuremech:phuz_spindle
  evidence_ids:
  - record
  - paper-0
  - paper-1
  - paper-11
  - paper-18
  summary: Erb 2014 and Chaikeeratisak 2017 support phage-encoded PhuZ polymerization,
    bipolar spindle organization and nucleus positioning. PhuZ is an essential spindle
    constituent, not asserted essential for phage viability. Chimallin shell and nucleus
    are distinct cargo, not tubulin constituents. All three positioning graph edges
    remain supported in Pseudomonas phage experiments; the Goslar vortex is outside
    this spindle identity.
- assessment_id: hierarchy
  area: grounding
  topic: Whole framework versus constituent system
  outcome: concern
  target_ids:
  - cellstructuremech:phuz_spindle
  evidence_ids:
  - record
  - go
  - rules
  - schema
  summary: The record places GO:0005856 cytoskeleton in parent_structures, asserting
    that this filament system is a type of the whole cellular framework. The native
    schema and CURATION rules distinguish is-a from part_of; GO:0099513 likewise describes
    a polymeric fiber as a component of the cytoskeleton. This is a semantic hierarchy
    error, even though all identifiers resolve.
- assessment_id: boundary
  area: evidence
  topic: Spindle versus vortex
  outcome: concern
  target_ids:
  - cellstructuremech:phuz_spindle
  evidence_ids:
  - record
  - paper-1
  - paper-11
  summary: 'The spindle definition and positioning graph retain a bipolar nucleus-positioning
    identity, but Goslar taxonomic/example rows, component role and rotation function
    include a distinct vortex. Birkholz 2022 explicitly contrasts this array with
    a bipolar spindle and finds no midcell-positioning role. Earlier #481/#482 aligned
    Goslar evidence with the component but did not resolve the record identity mismatch.
    Preserve that history while narrowing the active spindle claims.'
- assessment_id: optional
  area: completeness
  topic: Unresolved molecular details and provenance
  outcome: supported
  target_ids:
  - cellstructuremech:phuz_spindle
  evidence_ids:
  - record
  - history
  summary: No exact protein accession, universal copy number, quantitative property,
    image, trait or pathway assertion is invented. Label-only grounding tasks and
    optional empty fields are not defects. Prior discussions and curation events remain
    provenance, not authorization to promote PROPOSED.
findings:
- finding_id: F1
  issue_key: phuz-spindle-cytoskeleton-is-a
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Correct cytoskeleton is-a versus parthood
  description: The record places GO:0005856 cytoskeleton in parent_structures, asserting
    that this filament system is a type of the whole cellular framework. The native
    schema and CURATION rules distinguish is-a from part_of; GO:0099513 likewise describes
    a polymeric fiber as a component of the cytoskeleton. This is a semantic hierarchy
    error, even though all identifiers resolve.
  target_ids:
  - cellstructuremech:phuz_spindle
  field_paths:
  - parent_structures
  evidence_ids:
  - record
  - go
  - rules
  - schema
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/phuz_spindle.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: major
  normalization_reason: Material hierarchy or structure-scope assertion, not an optional
    completeness suggestion.
- finding_id: F2
  issue_key: phuz-spindle-goslar-vortex-boundary
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Separate the Goslar vortex from the PhuZ spindle
  description: 'The spindle definition and positioning graph retain a bipolar nucleus-positioning
    identity, but Goslar taxonomic/example rows, component role and rotation function
    include a distinct vortex. Birkholz 2022 explicitly contrasts this array with
    a bipolar spindle and finds no midcell-positioning role. Earlier #481/#482 aligned
    Goslar evidence with the component but did not resolve the record identity mismatch.
    Preserve that history while narrowing the active spindle claims.'
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
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/phuz_spindle.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: major
  normalization_reason: Material hierarchy or structure-scope assertion, not an optional
    completeness suggestion.
actions:
- action_id: A1
  description: Correct cytoskeleton is-a versus parthood
  finding_ids:
  - F1
  target_ids:
  - cellstructuremech:phuz_spindle
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/phuz_spindle.yaml
    role: maintained scientific record
  acceptance_checks:
  - Move GO:0005856 to part_of. For the BtubAB, CetZ and TubZ polymer records use
    GO:0099513 as the broader fiber parent; for the multi-filament PhuZ spindle retain
    parthood without forcing it into a single-fiber class. Preserve local identities
    and cite the precise ontology scope.
  - Guarded writer, actual Codex EDIT history, original discussion/history preservation,
    PROPOSED status, focused regressions, generated artifacts and native QC.
- action_id: A2
  description: Separate the Goslar vortex from the PhuZ spindle
  finding_ids:
  - F2
  target_ids:
  - cellstructuremech:phuz_spindle
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/phuz_spindle.yaml
    role: maintained scientific record
  acceptance_checks:
  - Retain the spindle identifier/label and positioning graph. Remove Goslar as a
    spindle occurrence/example and vortex-specific component/function claims. Preserve
    Birkholz evidence in a new explicit boundary discussion; retain rotation only
    with primary spindle evidence, such as Chaikeeratisak Science 2017 Figure 1. Do
    not claim every phage nucleus needs a spindle or that rotation is unique to vortices.
  - Guarded writer, actual Codex EDIT history, original discussion/history preservation,
    PROPOSED status, focused regressions, generated artifacts and native QC.
limitations:
- Same-agent whole-native-record review, not independent approval or raw-data reanalysis.
- Europe PMC fullTextXML returned HTTP 500 for several papers; complete official PMC
  HTML was retrieved instead. Source metadata alone and web interstitials were not
  used as full text.
- Exact-baseline CI supplies full QC; actual local schema/strict/snippet/global/contract
  checks ran separately. Existing resolver namespaces and three test skips remain
  explicit.
- The generic microtubule record is assessed separately in operational goal coverage;
  no clean review bundle is created. Experimental models, species versus strain scope,
  and unresolved exact protein groundings remain bounded.
```
