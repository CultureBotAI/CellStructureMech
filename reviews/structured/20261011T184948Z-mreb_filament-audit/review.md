# MreB filament: whole-record scientific review

- Review: 20261011T184948Z-mreb_filament-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T18:32:10Z
- Finished UTC: 2026-10-11T18:49:48Z
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
| cellstructuremech:mreb_filament | data/structures/cytoskeleton/mreb_filament.yaml | maintained | MreB filament |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | cellstructuremech:mreb_filament | Actual deterministic check passed; scientific support assessed separately. |
| strict | passed | True | cellstructuremech:mreb_filament | Actual deterministic check passed; scientific support assessed separately. |
| snippets | passed | True | cellstructuremech:mreb_filament | Checker exited 0 but reported three NOT CHECKED network retrievals. This is not automated verbatim confirmation; a separate exact-text check against retrieved NCBI XML confirmed all three quotations. |
| history | passed | True | cellstructuremech:mreb_filament | Actual deterministic check passed; scientific support assessed separately. |
| labels | passed | True | cellstructuremech:mreb_filament | id↔label correspondence summary:<br>          OK_CANONICAL: 3544<br>            OK_SYNONYM: 50<br>          OK_EXCEPTION: 6<br>    SKIPPED_NO_ADAPTER: 603<br><br>✅ All id↔label pairs correspond. |
| traits | passed | True | cellstructuremech:mreb_filament | Actual deterministic check passed; scientific support assessed separately. |
| curies | passed | True | cellstructuremech:mreb_filament | [not exercised] BFO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] CHEBI: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] ComplexPortal: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] DOI: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] GO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] InterPro: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] NCBITaxon: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] PATO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] PMID: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] RO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] SO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] UO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] UniProtKB: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] DOI: DataCite was unreachable, so DOI:10.22002/D1.1355 was not exercised<br>resolver control: 14 resolver(s) could not be exercised because their authority was unreachable; the rest accept a known id and reject a fabricated one<br><br>identifier liveness summary:<br>  OK             4013<br>  SKIPPED         251<br><br>Every identifier resolves at its issuing authority. |
| reviews | passed | True | cellstructuremech:mreb_filament | Actual deterministic check passed; scientific support assessed separately. |
| diff | passed | True | cellstructuremech:mreb_filament | Actual deterministic check passed; scientific support assessed separately. |
| contract | passed | True | cellstructuremech:mreb_filament | ....                                                                     [100%]<br>4 passed in 114.73s (0:01:54) |
| Exact-baseline native CI QC | passed | True | cellstructuremech:mreb_filament | Exact-baseline full QC: 897 passed, 3 skipped. Not a new local full QC run. |

## Scientific And Domain Assessments

### Claim-by-claim biological scope

evidence: supported. Targets: cellstructuremech:mreb_filament.

Local filament identity, related actin synonym, MreB constituent and associated RodZ, conditional linkage, E. coli and B. subtilis examples, shape function, all five graph relations and bounded trait assertions are supported. RodZ is not made an obligatory constituent; MreC/D and the elongasome remain distinct. UniProt gene/taxon matches and cited localization abstracts support protein examples. All three trait quotations were independently matched verbatim against real full-text XML. Antiparallel double filaments are supported by van den Ent 2014. Citation placement and archaeal occurrence require the findings below.

### Whole framework versus constituent fiber

grounding: concern. Targets: cellstructuremech:mreb_filament.

Each record is an individual polymer, not the containing cytoskeleton.

### Unresolved identities and original curation

completeness: supported. Targets: cellstructuremech:mreb_filament.

Label-only family groundings and optional empty fields are not defects. Essentiality describes the structural constituent rather than organism viability. Original discussions, prior issue rationale, dates and PROPOSED status must remain unchanged.

## Findings

### F1: Correct cytoskeleton is-a versus parthood

major / open / confirmed; issue key: mreb-filament-cytoskeleton-is-a.

GO:0005856 is in parent_structures, asserting that this individual filament is a type of the entire cytoskeletal framework. Native rules and GO distinguish the fiber class from its containing framework.

### F2: Do not infer archaeal filament occurrence from actin-fold homology

major / open / confirmed; issue key: mreb-filament-archaeal-occurrence-evidence.

The Archaea RARE occurrence row is justified only by actin-fold proteins while its own note identifies the MreB-elongasome arrangement as bacterial. Broad fold homology and Ta0583 polymerization do not establish occurrence or frequency of the specific bacterial system defined here. This is an unsupported affirmative row, not evidence of archaeal absence.

### F3: Attach evidence that supports the chronology of the MreB claims

minor / open / confirmed; issue key: mreb-filament-claim-local-citation-chronology.

The definition cites a 2010 review for short circumferentially moving filaments characterized in 2011 and later. The RodA/PBP2 synthase-pair graph claim cites only a 2011 review, preceding the 2016 SEDS polymerase experiments. The biological claims are supported by later inspected sources but the claim-local citation assignments are not adequate.

## Recommended Actions And Acceptance Checks

### A1

Correct cytoskeleton is-a versus parthood

- Use GO:0099513 as broader parent and GO:0005856 as part_of. Preserve the exact local filament identity and add precise authority evidence.
- Use guarded writer, append actual Codex EDIT history, preserve original discussions/history and PROPOSED status, and pass focused tests plus native QC.

### A2

Do not infer archaeal filament occurrence from actin-fold homology

- Remove the unsupported affirmative row and append the uncertainty/scope rationale without claiming absence or erasing prior history.
- Use guarded writer, append actual Codex EDIT history, preserve original discussions/history and PROPOSED status, and pass focused tests plus native QC.

### A3

Attach evidence that supports the chronology of the MreB claims

- Use the inspected 2018 review for the definition and add Cho 2016 primary evidence locally to the synthesis edge. Preserve older contextual bibliography, all graph relations and exact trait quotations.
- Use guarded writer, append actual Codex EDIT history, preserve original discussions/history and PROPOSED status, and pass focused tests plus native QC.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/mreb_filament.yaml | context_only | Entire native YAML inspected before judgment. |
| rules | docs/CURATION.md | context_only | Fiber is-a versus containing cytoskeleton part_of; narrow claim-local evidence. |
| schema | docs/SCHEMA.md | context_only | Hierarchy and parthood field contracts. |
| history | /private/tmp/csm-review-20261011T183112Z/mreb_filament-discussion-history.json | context_only | All committed discussion/inline-history versions inspected. |
| predecessors | /private/tmp/csm-review-20261011T183112Z/exact-target-predecessors.json | context_only | Ignored-inclusive canonical search: no exact-target predecessor. |
| identity | /private/tmp/csm-review-20261011T183112Z/identity-matches.json | context_only | Ignored-inclusive identity enumeration; separate elongasome/magnetosome identities retained. |
| issues | /private/tmp/csm-review-20261011T183112Z/mreb-all-issues.log | context_only | All-state slug/label issue searches and relevant earlier issues inspected. |
| adapter | /private/tmp/csm-review-20261011T183112Z/adapter.log | context_only | Inventory checked; absent coverage is not biological absence. |
| history-0 | history/records/mreb_filament/2026-09-04T010327Z-codex-4abcd4.yaml | context_only | Original append-only event inspected. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005856,GO:0099513,GO:0008360,GO:0009252,GO:0110143; GO:0005856 and GO:0099513 definitions and typed parthood | supports | The framework contains polymeric cytoskeletal fibers; a fiber is not the whole framework. |
| paper-1 | DOI:10.1016/j.cell.2018.02.050; Relevant Results/Discussion, methods and figure captions | supports | Inspected secondary review context, not a new primary experiment. Full text inspected for native claims. |
| paper-7 | DOI:10.1038/nrmicro2677; Relevant Results/Discussion, methods and figure captions | supports | Inspected secondary review context, not a new primary experiment. Full text inspected for native claims. |
| paper-16 | DOI:10.1146/annurev-genet-102108-134845; Exact DOI/PMID metadata and complete abstract only | supports | Inspected secondary review context, not a new primary experiment. Full text was not obtained; abstract-level support only. |
| paper-17 | PMID:15612918; Exact DOI/PMID metadata and complete abstract only | supports | Inspected primary experimental evidence. Full text was not obtained; abstract-level support only. |
| paper-18 | PMID:19008860; Exact DOI/PMID metadata and complete abstract only | supports | Inspected primary experimental evidence. Full text was not obtained; abstract-level support only. |
| taxon-2 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2; TaxId, scientificName, rank and aliases | supports | Exact taxon identity verified; taxonomy is not proof of structural occurrence. |
| taxon-2157 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2157; TaxId, scientificName, rank and aliases | supports | Exact taxon identity verified; taxonomy is not proof of structural occurrence. |
| taxon-83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; TaxId, scientificName, rank and aliases | supports | Exact taxon identity verified; taxonomy is not proof of structural occurrence. |
| taxon-1423 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1423; TaxId, scientificName, rank and aliases | supports | Exact taxon identity verified; taxonomy is not proof of structural occurrence. |
| protein-P0A9X4 | https://rest.uniprot.org/uniprotkb/P0A9X4.json; Reviewed accession, gene, organism and localization provenance | supports | Identifier/source matches verified; localization is not alone filament membership proof. |
| protein-P27434 | https://rest.uniprot.org/uniprotkb/P27434.json; Reviewed accession, gene, organism and localization provenance | supports | Identifier/source matches verified; localization is not alone filament membership proof. |
| modern-structure | DOI:10.7554/eLife.02634; Relevant primary Results/Discussion | supports | Primary antiparallel filament/membrane experiments and chronology of circumferential movement. |
| synthase | DOI:10.1038/nmicrobiol.2016.172; Relevant primary Results/Discussion | supports | Primary E. coli RodA/PBP2/SEDS synthesis experiments support the modern synthase-pair claim. |
| archaeal-actin | DOI:10.1128/JB.01454-06; Exact DOI/PMID and abstract | supports | Abstract only: Ta0583 actin-like polymerization is not a demonstrated bacterial MreB-elongasome filament; no archaeal absence inferred. |
| manual-snippets | /private/tmp/csm-review-20261011T183112Z/manual-snippets.json | context_only | All three quotations exactly present after whitespace normalization in inspected real NCBI XML. |
| protein-seed-history | history/mappings/protein-example-accessions/2026-09-08T064823Z-claude-f9b0cf.yaml | context_only | Original mapping event inspected; seeded accessions do not replace source evidence. |
| expression-e_coli-mreB | /private/tmp/csm-review-20261011T183112Z/adapter-e_coli-mreB.log | context_only | Actual source query; matched genes but zero modules, not negative structural evidence. |
| expression-e_coli-rodZ | /private/tmp/csm-review-20261011T183112Z/adapter-e_coli-rodZ.log | context_only | Actual source query; matched genes but zero modules, not negative structural evidence. |
| expression-b_subtilis-mreB | /private/tmp/csm-review-20261011T183112Z/adapter-b_subtilis-mreB.log | context_only | Actual source query; matched genes but zero modules, not negative structural evidence. |

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
review_id: 20261011T184948Z-mreb_filament-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'MreB filament: whole-record scientific review'
started_at: '2026-10-11T18:32:10Z'
finished_at: '2026-10-11T18:49:48Z'
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
    role: context
  - path: data/structures/cytoskeleton/mamk_filament.yaml
    sha256: e42eeee29c4e227048b2881bcbbc073a67f6f1ae133a8464c76257693c6812f7
    role: context
  - path: data/structures/cytoskeleton/mreb_filament.yaml
    sha256: 2d03a06bf7c994d73d3371701a00fe87ec9107d327d5bede0d53debda85f9d64
    role: target
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
  - path: history/records/mreb_filament/2026-09-04T010327Z-codex-4abcd4.yaml
    sha256: c87b0454903ba2109ccf961fe7b3035b219432ba9117f4c26304346723843a95
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
- target_id: cellstructuremech:mreb_filament
  path: data/structures/cytoskeleton/mreb_filament.yaml
  label: MreB filament
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/mreb_filament.yaml
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
  - cellstructuremech:mreb_filament
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mreb_filament
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/mreb_filament.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T18:31:48Z to 2026-10-11T18:31:51Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mreb_filament
  command: .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/mreb_filament.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T18:31:51Z to 2026-10-11T18:31:57Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mreb_filament
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/cytoskeleton/mreb_filament.yaml
    --report /private/tmp/csm-review-20261011T183112Z/mreb_filament-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: Checker exited 0 but reported three NOT CHECKED network retrievals. This
    is not automated verbatim confirmation; a separate exact-text check against retrieved
    NCBI XML confirmed all three quotations.
  scope_note: 2026-10-11T18:31:57Z to 2026-10-11T18:32:43Z; log SHA-256 c65d0d31420b132b945f7a8a4c04016f9225e7a29200d8d456950c7c61a4fc0a
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mreb_filament
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
  - cellstructuremech:mreb_filament
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
  - cellstructuremech:mreb_filament
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
  - cellstructuremech:mreb_filament
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
  - cellstructuremech:mreb_filament
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
  - cellstructuremech:mreb_filament
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
  - cellstructuremech:mreb_filament
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
  - cellstructuremech:mreb_filament
  command: gh run view 38163493641 --repo CultureBotAI/CellStructureMech --log
  exit_code: 0
  expected_exit_code: 0
  summary: 'Exact-baseline full QC: 897 passed, 3 skipped. Not a new local full QC
    run.'
  scope_note: https://github.com/CultureBotAI/CellStructureMech/actions/runs/38163493641
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/mreb_filament.yaml
  accessed_at: '2026-10-11T18:49:48Z'
  snapshot_sha256: 2d03a06bf7c994d73d3371701a00fe87ec9107d327d5bede0d53debda85f9d64
  support: context_only
  summary: Entire native YAML inspected before judgment.
- evidence_id: rules
  kind: record_content
  reference: docs/CURATION.md
  accessed_at: '2026-10-11T18:49:48Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  support: context_only
  summary: Fiber is-a versus containing cytoskeleton part_of; narrow claim-local evidence.
- evidence_id: schema
  kind: record_content
  reference: docs/SCHEMA.md
  accessed_at: '2026-10-11T18:49:48Z'
  snapshot_sha256: 07b8f936a553a45cc6e8dba924c21e6af48c81b3866725efeb00c8183f0c75a2
  support: context_only
  summary: Hierarchy and parthood field contracts.
- evidence_id: history
  kind: record_content
  reference: /private/tmp/csm-review-20261011T183112Z/mreb_filament-discussion-history.json
  accessed_at: '2026-10-11T18:49:48Z'
  snapshot_sha256: 199493965cd268c0e198d327d328661d2951f8d7da05d1a319d0fef68549dea5
  support: context_only
  summary: All committed discussion/inline-history versions inspected.
- evidence_id: predecessors
  kind: validation
  reference: /private/tmp/csm-review-20261011T183112Z/exact-target-predecessors.json
  accessed_at: '2026-10-11T18:49:48Z'
  snapshot_sha256: f7bb865579cd8ac8088b01d712760c8b12268a7fb70bc59b6af68f5cf9d7cc19
  support: context_only
  summary: 'Ignored-inclusive canonical search: no exact-target predecessor.'
- evidence_id: identity
  kind: validation
  reference: /private/tmp/csm-review-20261011T183112Z/identity-matches.json
  accessed_at: '2026-10-11T18:49:48Z'
  snapshot_sha256: 2b7b7369dae8179ab0188eb431905ef8360ea1f16d25c67c9c95567de7ce3006
  support: context_only
  summary: Ignored-inclusive identity enumeration; separate elongasome/magnetosome
    identities retained.
- evidence_id: issues
  kind: validation
  reference: /private/tmp/csm-review-20261011T183112Z/mreb-all-issues.log
  accessed_at: '2026-10-11T18:49:48Z'
  snapshot_sha256: fb5188a18a426da3b08b306a5194ed83f1c103d927af46090eb3b6188fd5c59f
  support: context_only
  summary: All-state slug/label issue searches and relevant earlier issues inspected.
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/csm-review-20261011T183112Z/adapter.log
  accessed_at: '2026-10-11T18:49:48Z'
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
  support: context_only
  summary: Inventory checked; absent coverage is not biological absence.
- evidence_id: history-0
  kind: record_content
  reference: history/records/mreb_filament/2026-09-04T010327Z-codex-4abcd4.yaml
  accessed_at: '2026-10-11T18:49:48Z'
  snapshot_sha256: c87b0454903ba2109ccf961fe7b3035b219432ba9117f4c26304346723843a95
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
- evidence_id: paper-1
  kind: primary_source
  reference: DOI:10.1016/j.cell.2018.02.050
  locator: Relevant Results/Discussion, methods and figure captions
  accessed_at: '2026-10-11T18:36:28Z'
  snapshot_sha256: 85461821236439e38067b63c72a9d974ee718cf73430bf07acd76995eb3c0d4a
  support: supports
  summary: Inspected secondary review context, not a new primary experiment. Full
    text inspected for native claims.
- evidence_id: paper-7
  kind: primary_source
  reference: DOI:10.1038/nrmicro2677
  locator: Relevant Results/Discussion, methods and figure captions
  accessed_at: '2026-10-11T18:36:45Z'
  snapshot_sha256: 5d58623346677d6ecd21e26fff4f0e373028b6d0a679e7a041981805380810f1
  support: supports
  summary: Inspected secondary review context, not a new primary experiment. Full
    text inspected for native claims.
- evidence_id: paper-16
  kind: primary_source
  reference: DOI:10.1146/annurev-genet-102108-134845
  locator: Exact DOI/PMID metadata and complete abstract only
  accessed_at: '2026-10-11T18:32:20Z'
  snapshot_sha256: 18d205a2a42159ec22765571de00840ddb78f481f042be4d839970ab7a31a60a
  support: supports
  summary: Inspected secondary review context, not a new primary experiment. Full
    text was not obtained; abstract-level support only.
- evidence_id: paper-17
  kind: primary_source
  reference: PMID:15612918
  locator: Exact DOI/PMID metadata and complete abstract only
  accessed_at: '2026-10-11T18:32:21Z'
  snapshot_sha256: ac312650bca07602938695a4218d42736b4f94b15277c2d8b28b19a52d2b6997
  support: supports
  summary: Inspected primary experimental evidence. Full text was not obtained; abstract-level
    support only.
- evidence_id: paper-18
  kind: primary_source
  reference: PMID:19008860
  locator: Exact DOI/PMID metadata and complete abstract only
  accessed_at: '2026-10-11T18:32:22Z'
  snapshot_sha256: 9aa2eaa73b4625b859b3fd961242b7845cef9c05d3103a10fcc9f6cdd49f2acc
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
- evidence_id: taxon-2157
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2157
  locator: TaxId, scientificName, rank and aliases
  accessed_at: '2026-10-11T18:34:22Z'
  snapshot_sha256: c6e652011b95e43e933983bf5f3f5cec9508c1925adae00dc55e46cd4e816b19
  support: supports
  summary: Exact taxon identity verified; taxonomy is not proof of structural occurrence.
- evidence_id: taxon-83333
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: TaxId, scientificName, rank and aliases
  accessed_at: '2026-10-11T18:34:23Z'
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
  support: supports
  summary: Exact taxon identity verified; taxonomy is not proof of structural occurrence.
- evidence_id: taxon-1423
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1423
  locator: TaxId, scientificName, rank and aliases
  accessed_at: '2026-10-11T18:34:24Z'
  snapshot_sha256: cba62f34e18147fc64dac9d0b13c66a25f60ac516c43a451187d6787e3c7a07b
  support: supports
  summary: Exact taxon identity verified; taxonomy is not proof of structural occurrence.
- evidence_id: protein-P0A9X4
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0A9X4.json
  locator: Reviewed accession, gene, organism and localization provenance
  accessed_at: '2026-10-11T18:34:31Z'
  snapshot_sha256: d993238876d75bb9d1189c96641de8c767a44b179cb0fbd6f9ec4b6e44f21ad8
  support: supports
  summary: Identifier/source matches verified; localization is not alone filament
    membership proof.
- evidence_id: protein-P27434
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P27434.json
  locator: Reviewed accession, gene, organism and localization provenance
  accessed_at: '2026-10-11T18:34:31Z'
  snapshot_sha256: c7f625d134c7a45fbc08770f5ac5edadb94e593b081e5502c4726e14d22130ad
  support: supports
  summary: Identifier/source matches verified; localization is not alone filament
    membership proof.
- evidence_id: modern-structure
  kind: primary_source
  reference: DOI:10.7554/eLife.02634
  locator: Relevant primary Results/Discussion
  accessed_at: '2026-10-11T18:43:23Z'
  snapshot_sha256: 5b69cd7e6ed8be42e405407aca99a95aa0646b9460e583bb0ead7507c2275f5f
  support: supports
  summary: Primary antiparallel filament/membrane experiments and chronology of circumferential
    movement.
- evidence_id: synthase
  kind: primary_source
  reference: DOI:10.1038/nmicrobiol.2016.172
  locator: Relevant primary Results/Discussion
  accessed_at: '2026-10-11T18:43:25Z'
  snapshot_sha256: 394ddc19e2663964c0e03c8c88ad29b40f702a4f2e46ec76f8c160b2d82db050
  support: supports
  summary: Primary E. coli RodA/PBP2/SEDS synthesis experiments support the modern
    synthase-pair claim.
- evidence_id: archaeal-actin
  kind: primary_source
  reference: DOI:10.1128/JB.01454-06
  locator: Exact DOI/PMID and abstract
  accessed_at: '2026-10-11T18:43:25Z'
  snapshot_sha256: aaf0446ce7b6a72c6e275db4623d6a2fa8b19009c818060154a92a6525b77eb6
  support: supports
  summary: 'Abstract only: Ta0583 actin-like polymerization is not a demonstrated
    bacterial MreB-elongasome filament; no archaeal absence inferred.'
- evidence_id: manual-snippets
  kind: validation
  reference: /private/tmp/csm-review-20261011T183112Z/manual-snippets.json
  accessed_at: '2026-10-11T18:49:48Z'
  snapshot_sha256: 19a8aafdfc6088c9773509abb595b235635988c8569f2e304ad9384f8bc97309
  support: context_only
  summary: All three quotations exactly present after whitespace normalization in
    inspected real NCBI XML.
- evidence_id: protein-seed-history
  kind: record_content
  reference: history/mappings/protein-example-accessions/2026-09-08T064823Z-claude-f9b0cf.yaml
  accessed_at: '2026-10-11T18:49:48Z'
  snapshot_sha256: 7dd6983d5d623dde8367fd767ef38395247a824dd8520090685ace010e30f29c
  support: context_only
  summary: Original mapping event inspected; seeded accessions do not replace source
    evidence.
- evidence_id: expression-e_coli-mreB
  kind: validation
  reference: /private/tmp/csm-review-20261011T183112Z/adapter-e_coli-mreB.log
  accessed_at: '2026-10-11T18:49:48Z'
  snapshot_sha256: 9172854f4ca45302248e62b20358a16aea6a135a781bc0b8d8fbeebae82113af
  support: context_only
  summary: Actual source query; matched genes but zero modules, not negative structural
    evidence.
- evidence_id: expression-e_coli-rodZ
  kind: validation
  reference: /private/tmp/csm-review-20261011T183112Z/adapter-e_coli-rodZ.log
  accessed_at: '2026-10-11T18:49:48Z'
  snapshot_sha256: 7ce21dc0169c9185636070c8da53998754937568b81ecfe3ae5012d947d16506
  support: context_only
  summary: Actual source query; matched genes but zero modules, not negative structural
    evidence.
- evidence_id: expression-b_subtilis-mreB
  kind: validation
  reference: /private/tmp/csm-review-20261011T183112Z/adapter-b_subtilis-mreB.log
  accessed_at: '2026-10-11T18:49:48Z'
  snapshot_sha256: f02c35ae63063c499008a4094637a869d55ab13034a1c52fb38c09cec07bf1ee
  support: context_only
  summary: Actual source query; matched genes but zero modules, not negative structural
    evidence.
assessments:
- assessment_id: biology
  area: evidence
  topic: Claim-by-claim biological scope
  outcome: supported
  target_ids:
  - cellstructuremech:mreb_filament
  evidence_ids:
  - record
  - paper-1
  - paper-7
  - paper-16
  - paper-17
  - paper-18
  summary: Local filament identity, related actin synonym, MreB constituent and associated
    RodZ, conditional linkage, E. coli and B. subtilis examples, shape function, all
    five graph relations and bounded trait assertions are supported. RodZ is not made
    an obligatory constituent; MreC/D and the elongasome remain distinct. UniProt
    gene/taxon matches and cited localization abstracts support protein examples.
    All three trait quotations were independently matched verbatim against real full-text
    XML. Antiparallel double filaments are supported by van den Ent 2014. Citation
    placement and archaeal occurrence require the findings below.
- assessment_id: hierarchy
  area: grounding
  topic: Whole framework versus constituent fiber
  outcome: concern
  target_ids:
  - cellstructuremech:mreb_filament
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
  - cellstructuremech:mreb_filament
  evidence_ids:
  - record
  - history
  summary: Label-only family groundings and optional empty fields are not defects.
    Essentiality describes the structural constituent rather than organism viability.
    Original discussions, prior issue rationale, dates and PROPOSED status must remain
    unchanged.
findings:
- finding_id: F1
  issue_key: mreb-filament-cytoskeleton-is-a
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Correct cytoskeleton is-a versus parthood
  description: GO:0005856 is in parent_structures, asserting that this individual
    filament is a type of the entire cytoskeletal framework. Native rules and GO distinguish
    the fiber class from its containing framework.
  target_ids:
  - cellstructuremech:mreb_filament
  field_paths:
  - parent_structures
  evidence_ids:
  - record
  - go
  - rules
  - schema
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/mreb_filament.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: major
  normalization_reason: Incorrect scientific hierarchy or scope.
- finding_id: F2
  issue_key: mreb-filament-archaeal-occurrence-evidence
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Do not infer archaeal filament occurrence from actin-fold homology
  description: The Archaea RARE occurrence row is justified only by actin-fold proteins
    while its own note identifies the MreB-elongasome arrangement as bacterial. Broad
    fold homology and Ta0583 polymerization do not establish occurrence or frequency
    of the specific bacterial system defined here. This is an unsupported affirmative
    row, not evidence of archaeal absence.
  target_ids:
  - cellstructuremech:mreb_filament
  field_paths:
  - taxonomic_distribution
  evidence_ids:
  - record
  - paper-1
  - archaeal-actin
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/mreb_filament.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: major
  normalization_reason: Incorrect scientific hierarchy or scope.
- finding_id: F3
  issue_key: mreb-filament-claim-local-citation-chronology
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Attach evidence that supports the chronology of the MreB claims
  description: The definition cites a 2010 review for short circumferentially moving
    filaments characterized in 2011 and later. The RodA/PBP2 synthase-pair graph claim
    cites only a 2011 review, preceding the 2016 SEDS polymerase experiments. The
    biological claims are supported by later inspected sources but the claim-local
    citation assignments are not adequate.
  target_ids:
  - cellstructuremech:mreb_filament
  field_paths:
  - definition_source
  - causal_graphs[0].edges[3].evidence
  evidence_ids:
  - record
  - paper-1
  - paper-7
  - modern-structure
  - synthase
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/mreb_filament.yaml
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
  - cellstructuremech:mreb_filament
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/mreb_filament.yaml
    role: maintained scientific record
  acceptance_checks:
  - Use GO:0099513 as broader parent and GO:0005856 as part_of. Preserve the exact
    local filament identity and add precise authority evidence.
  - Use guarded writer, append actual Codex EDIT history, preserve original discussions/history
    and PROPOSED status, and pass focused tests plus native QC.
- action_id: A2
  description: Do not infer archaeal filament occurrence from actin-fold homology
  finding_ids:
  - F2
  target_ids:
  - cellstructuremech:mreb_filament
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/mreb_filament.yaml
    role: maintained scientific record
  acceptance_checks:
  - Remove the unsupported affirmative row and append the uncertainty/scope rationale
    without claiming absence or erasing prior history.
  - Use guarded writer, append actual Codex EDIT history, preserve original discussions/history
    and PROPOSED status, and pass focused tests plus native QC.
- action_id: A3
  description: Attach evidence that supports the chronology of the MreB claims
  finding_ids:
  - F3
  target_ids:
  - cellstructuremech:mreb_filament
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/mreb_filament.yaml
    role: maintained scientific record
  acceptance_checks:
  - Use the inspected 2018 review for the definition and add Cho 2016 primary evidence
    locally to the synthesis edge. Preserve older contextual bibliography, all graph
    relations and exact trait quotations.
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
