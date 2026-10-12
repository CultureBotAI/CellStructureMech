# meiotic actomyosin contractile ring: scientific record review

- Review: 20261012T023600Z-meiotic_actomyosin_contractile_ring-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-12T02:28:09Z
- Finished UTC: 2026-10-12T02:36:00Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Whole native record assessed; one supported minor publication-identifier correction saved before curation.

## Scope And Provenance

Whole native YAML: identity, hierarchy, components, taxon/example/function where present, every graph edge, evidence, discussions and both history surfaces.

Selection: One exact record in the909-record review goal; no sampled verdict.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8da5e26473dd542f45e112a800bb0b62fcfc4c2b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0110086 | data/structures/cytoskeleton/meiotic_actomyosin_contractile_ring.yaml | maintained | meiotic actomyosin contractile ring |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0110086 | Actual deterministic check passed; scientific support assessed separately. |
| strict | passed | True | GO:0110086 | Actual deterministic check passed; scientific support assessed separately. |
| snippets | passed | True | GO:0110086 | No verbatim snippets; paraphrases assessed separately against inspected text. |
| history | passed | True | GO:0110086 | Actual deterministic check passed; scientific support assessed separately. |
| labels | passed | True | GO:0110086 | id↔label correspondence summary:<br>          OK_CANONICAL: 3545<br>            OK_SYNONYM: 50<br>          OK_EXCEPTION: 6<br>    SKIPPED_NO_ADAPTER: 603<br><br>✅ All id↔label pairs correspond. |
| traits | passed | True | GO:0110086 | Actual deterministic check passed; scientific support assessed separately. |
| curies | passed | True | GO:0110086 | resolver control: every resolver accepts a known id and rejects a fabricated one<br><br>identifier liveness summary:<br>  OK             4018<br>  SKIPPED         251<br><br>Every identifier resolves at its issuing authority. |
| reviews | passed | True | GO:0110086 | Actual deterministic check passed; scientific support assessed separately. |
| baseline-ci | passed | True | GO:0110086 | Actual deterministic check passed; scientific support assessed separately. |
| baseline-ci-full | passed | True | GO:0110086 | Actual deterministic check passed; scientific support assessed separately. |
| adapter | passed | True | GO:0110086 | Actual deterministic check passed; scientific support assessed separately. |
| typed-go | passed | True | GO:0110086 | Actual deterministic check passed; scientific support assessed separately. |
| Exact unchanged merged-baseline native QC | passed | True | GO:0110086 | Exact native merge-group8da5e264 passed979 tests,3 skips and4 contract tests;909 strict records and generated artifacts current. Fresh focused/global checks separate. Full QC not rerun locally before these no-edit observations. |

## Scientific And Domain Assessments

### Exact class, hierarchy and neighboring-ring boundaries

identity: supported. Targets: GO:0110086.

Exact GO cellular-component identity and direct is-a parent are supported. Prospore subtype, broad meiotic class, mitotic sibling and septin ring remain distinct. FILAMENT denotes a filamentous ring structure, not a single protein.

### Composition, present taxonomy/functions and all graph edges

evidence: supported. Targets: GO:0110086.

Broad actin/myosin membership and nonmechanistic topology edges are supported at the declared ontology tier. Meiotic record has a condition-qualified S.pombe example and observed expansion/closure; no explicit myosinII motor requirement or exact stoichiometry is asserted. Prospore record makes no taxonomic prevalence assertion. These claims do not determine assembly essentiality.

### Use the publisher-corrected MeiAR paper DOI

evidence: concern. Targets: GO:0110086.

All current paper references use DOI:10.1242/jcs.091561, the number corrected by the publisher erratum DOI:10.1242/jcs.113316. Both the article page and issuing Crossref object give DOI:10.1242/jcs.jcs091561. The old alias resolves, so this is a bounded provenance defect, not a wrong-paper or unreadability finding. Replace current reference values, preserve the inspected biological claims, and attach a short provenance note naming the correction. Do not rewrite historical events or reports.

### Open questions, histories and optional resources

completeness: supported. Targets: GO:0110086.

Unknown exact family/accessory boundaries remain legitimate open work. No optional image, property, dataset, trait or pathway is fabricated. Both original histories and prior reports are preserved; PROPOSED is unchanged.

## Findings

### F1: Use the publisher-corrected MeiAR paper DOI

minor / open / confirmed; issue key: meiotic-ring-corrected-publication-doi.

All current paper references use DOI:10.1242/jcs.091561, the number corrected by the publisher erratum DOI:10.1242/jcs.113316. Both the article page and issuing Crossref object give DOI:10.1242/jcs.jcs091561. The old alias resolves, so this is a bounded provenance defect, not a wrong-paper or unreadability finding. Replace current reference values, preserve the inspected biological claims, and attach a short provenance note naming the correction. Do not rewrite historical events or reports.

## Recommended Actions And Acceptance Checks

### A1

Use the publisher-corrected MeiAR paper DOI

- All current paper references use DOI:10.1242/jcs.091561, the number corrected by the publisher erratum DOI:10.1242/jcs.113316. Both the article page and issuing Crossref object give DOI:10.1242/jcs.jcs091561. The old alias resolves, so this is a bounded provenance defect, not a wrong-paper or unreadability finding. Replace current reference values, preserve the inspected biological claims, and attach a short provenance note naming the correction. Do not rewrite historical events or reports.
- Guarded writer; append actual Codex event and one EDIT history per changed record. Preserve all original histories, discussion rationale, graph content, taxonomic scope and PROPOSED status.
- Focused red/green regressions, regenerated pages, semantic-map drift check and full native QC. Save an exact-lineage successor disposition; pass PR and native merge-group gates before merge.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/meiotic_actomyosin_contractile_ring.yaml | context_only | Entire original native YAML read; captured bytes unchanged. |
| rules | docs/CURATION.md | context_only | Component membership and assembly necessity are distinct; scientific status is not promoted. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml | context_only | ESSENTIAL means the structure does not form without the component. |
| predecessors | /private/tmp/csm-review-20261012T023100Z/predecessors.json | context_only | Ignored-inclusive recursive canonical scan matched exact targetID OR path; no match. |
| reading | /private/tmp/csm-review-20261012T023100Z/reading-checkpoint.json | context_only | Actual reading scope and explicit source-access limits; source text, not search snippets. |
| typed-go | /private/tmp/csm-review-20261012T023100Z/typed-go.log | context_only | Exact OAK typed relations: prospore is_a meiotic ring; meiotic is_a generic actomyosin ring. |
| adapter | /private/tmp/csm-review-20261012T023100Z/adapter.log | context_only | Fresh28-dataset iModulonDB inventory has no matching S.pombe/Giardia coverage; not negative biological evidence. |
| history-0 | history/records/meiotic_actomyosin_contractile_ring/2026-09-29T224903Z-codex-3464bd.yaml | context_only | Whole append-only history read and preserved. |
| legacy | reports/yaml_record_review/20260929T231019Z-meiotic_actomyosin_contractile_ring.md | context_only | Whole historical PR review read; not substituted for fresh source assessment. |
| issues | /private/tmp/csm-review-20261012T023100Z/issues-2.log | context_only | All-state target searches include already-closed1767 parentage correction, still present. No related open finding in these bounded searches. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0097568%2CGO%3A0005856%2CGO%3A0005874%2CGO%3A0110086%2CGO%3A0032157%2CGO%3A0005826%2CGO%3A0110085%2CGO%3A0032169; Exact eight terms, current definitions/synonym types/typed children | supports | Both exact identities and direct is-a relations agree. Definitions assert composition and location, not component-depletion outcomes. |
| taxon | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896; ENA4896 species identity | supports | S.pombe verified; source experiments establish the occurrence, not the taxonomic resolver. |
| paper-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1242%2Fjcs.091561%22&amp;format=json&amp;resultType=core; PMID22526418 primary abstract and original DOI metadata | supports | MeiAR forms during meiosisII and coordinates forespore membranes; PubMed retains the original DOI. |
| corrected-doi | https://api.crossref.org/works/10.1242%2Fjcs.jcs091561; Issuing DOI metadata | supports | Canonical deposited DOI is10.1242/jcs.jcs091561. The original alias also resolves to this canonical object. |
| erratum-doi | https://api.crossref.org/works/10.1242%2Fjcs.113316; DOI10.1242/jcs.113316 metadata | supports | Publisher erratum identity verified. |
| erratum | DOI:10.1242/jcs.113316; Publisher full correction: https://journals.biologists.com/jcs/article/125/10/2544/32305/Meiotic-actin-rings-are-essential-for-proper | supports | The correction explicitly gives10.1242/jcs.jcs091561 as the correct paper DOI. It changes provenance, not experimental conclusions. |
| yan | DOI:10.1242/jcs.jcs091561; Publisher full main text and six captions at https://journals.biologists.com/jcs/article/125/6/1429/33273/Meiotic-actin-rings-are-essential-for-proper | supports | Fission-yeast actin ring expansion/closure and membrane coordination are observed. Myo1 and Rlc1 localize; individual myosinII mutants sporulate, and the double mutant was not testable. Ring closure is not demonstrated typeII-myosin force generation. |

## Limits And Additional Notes

- Same-agent scientific review; no independent human sign-off or raw-data reanalysis.
- Yan2012 full scientific text/captions read via publisher web retrieval; local requests returned403. Figure pixels, movies and supplements not inspected. No quantitative or exact-myofibril-mechanism claim introduced.
- Myo2/Myp2 individual mutant sporulation is not a complete myosin-class deletion or a direct assembly assay. Current generic composition claims remain ontology-tier; force mechanism unresolved.
- Exact-baseline full QC/contract CI reused at unchanged8da5; fresh focused/global checks retain6 label exceptions,603 no-adapter cases,251 CURIE policy skips and3 baseline test skips.
- No matching adopted iModulonDB dataset; not negative evidence. Alias-bounded GitHub search and ignored-inclusive canonical scan have different scopes.
- Median body has separate whole-record coverage; no clean bundle or no-change history will be generated.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T023600Z-meiotic_actomyosin_contractile_ring-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'meiotic actomyosin contractile ring: scientific record review'
started_at: '2026-10-12T02:28:09Z'
finished_at: '2026-10-12T02:36:00Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent claim-by-claim scientific review, not independent
    human approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Whole native record assessed; one supported minor publication-identifier
  correction saved before curation.
source:
  git_revision: 8da5e26473dd542f45e112a800bb0b62fcfc4c2b
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/SKILL.md
    sha256: efb5aa79a0016ae7f1e53e40a9f5789930d152686ea6467aefce0928f7d1900f
    role: context
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
    role: context
  - path: .claude/skills/literature-evidence/SKILL.md
    sha256: f7c3c594b5fb2cd7d4d700844fce3b97c91cc382d4fdca8b2e2a96cf16abd41b
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
    role: context
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: conf/record_review.yaml
    sha256: d3334a12b8a616a7638f1195748085d2b543fba7df67ad4ff8fcc0ac18f2d3ee
    role: context
  - path: data/structures/cytoskeleton/actomyosin_contractile_ring.yaml
    sha256: 28a3e7b12391a9d3a16eb453974d6e0ed5ab92b925092e395e88f64fa6fe5ab0
    role: context
  - path: data/structures/cytoskeleton/ciliary_centrin_arm.yaml
    sha256: 483507c171218f013e0bfaaa4aa3c77c1cedb91cecb105d1b1a342bb3b914543
    role: context
  - path: data/structures/cytoskeleton/deep_fiber.yaml
    sha256: 7868013c7bf3ce1c327c9106136b716f305afebe4efe5d49412e69278d26d702
    role: context
  - path: data/structures/cytoskeleton/infraciliary_lattice.yaml
    sha256: 4c0d123ba0fcc1f65ea9ccf7d139013039bf1db51f987dec87b6df5286e5c00e
    role: context
  - path: data/structures/cytoskeleton/meiotic_actomyosin_contractile_ring.yaml
    sha256: a0c3dca4b15179b78b04e657aa274ba03dd5f8d9bd26c5f1534838081afe064e
    role: target
  - path: data/structures/cytoskeleton/mitotic_actomyosin_contractile_ring.yaml
    sha256: d90e4f93479d2774c995e54dcd260859b8a855a4c6c7241a7d46b76d6db352af
    role: context
  - path: data/structures/cytoskeleton/peritrich_body_myoneme_system.yaml
    sha256: 85563af4f17c846111f087a0c6bd31b6480a9b5fff05df9a3eff79e0b25418f9
    role: context
  - path: data/structures/cytoskeleton/prospore_contractile_ring.yaml
    sha256: 51f904a9bcc9ae19d4f7b75c05dc6b7e3f78dcaecf7d59c3607eec849238fd5e
    role: context
  - path: data/structures/cytoskeleton/spirostomum_myoneme_fishnet.yaml
    sha256: 23c2668330bc68a88153d7ed54feb0a5626a88d4ae53a8da6e250d2dda8d71af
    role: context
  - path: data/structures/cytoskeleton/stentor_myoneme_system.yaml
    sha256: 5d79ebc4d1396dc1a3e8d7e840a2aba6ed8dc37114846e4405df82c965b10b28
    role: context
  - path: data/structures/other/oral_apparatus.yaml
    sha256: 55dd7652482846930c83b0340be155e52c094dbdf9232427bc76580cbe65a372
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
  - path: history/README.md
    sha256: 1636df44f28547f440242afcb4a05ac293b9714b4d7b809cecc30b975e44a522
    role: context
  - path: history/records/meiotic_actomyosin_contractile_ring/2026-09-29T224903Z-codex-3464bd.yaml
    sha256: fbe266128475d2dfaff497a97fcce4e17dbb18cb6c8424f065504feb23bd997d
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reports/yaml_record_review/20260929T231019Z-meiotic_actomyosin_contractile_ring.md
    sha256: 5cae900c54d5d1d039e285de5fc39cfdeb9d8e4d2d433fe540f2c48644fb5c37
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
targets:
- target_id: GO:0110086
  path: data/structures/cytoskeleton/meiotic_actomyosin_contractile_ring.yaml
  label: meiotic actomyosin contractile ring
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/meiotic_actomyosin_contractile_ring.yaml
    role: maintained scientific record
scope:
  description: 'Whole native YAML: identity, hierarchy, components, taxon/example/function
    where present, every graph edge, evidence, discussions and both history surfaces.'
  selection: One exact record in the909-record review goal; no sampled verdict.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0110086
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - GO:0110086
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/meiotic_actomyosin_contractile_ring.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-12T02:28:47Z to 2026-10-12T02:28:50Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - GO:0110086
  command: .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/meiotic_actomyosin_contractile_ring.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-12T02:28:50Z to 2026-10-12T02:28:54Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - GO:0110086
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/cytoskeleton/meiotic_actomyosin_contractile_ring.yaml
    --report /private/tmp/csm-review-20261012T023100Z/meiotic_actomyosin_contractile_ring-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: No verbatim snippets; paraphrases assessed separately against inspected
    text.
  scope_note: 2026-10-12T02:28:54Z to 2026-10-12T02:29:18Z; log SHA-256 2ec08b67f30e2c8e9749d3452814664dd824d228b1e37e2d799b6b14f06b211d
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:0110086
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-12T02:29:47Z to 2026-10-12T02:29:59Z; log SHA-256 18ccd1252becfd50c7b7b60bac6a12cbe7a48c66582a4bf9e60fd29e20d3a3ba
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - GO:0110086
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: "id↔label correspondence summary:\n          OK_CANONICAL: 3545\n     \
    \       OK_SYNONYM: 50\n          OK_EXCEPTION: 6\n    SKIPPED_NO_ADAPTER: 603\n\
    \n✅ All id↔label pairs correspond."
  scope_note: 2026-10-12T02:29:59Z to 2026-10-12T02:31:26Z; log SHA-256 459523b233cf29c593d6ebe49a38d5ed4484b1f98496dc47ea4fdc17be729286
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - GO:0110086
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-12T02:31:26Z to 2026-10-12T02:31:49Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - GO:0110086
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: "resolver control: every resolver accepts a known id and rejects a fabricated\
    \ one\n\nidentifier liveness summary:\n  OK             4018\n  SKIPPED      \
    \   251\n\nEvery identifier resolves at its issuing authority."
  scope_note: 2026-10-12T02:31:49Z to 2026-10-12T02:32:54Z; log SHA-256 e23813ddcc5db74cba9775b414dcfa6b02508de21416034936676ba9948d0a3a
- check_id: reviews
  name: reviews
  status: passed
  required: true
  target_ids:
  - GO:0110086
  command: .venv/bin/python scripts/record_review.py check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-12T02:32:54Z to 2026-10-12T02:35:12Z; log SHA-256 44da58b21cfa0337a9d7b73f5a8591a5d90d9766fef897041724365308467508
- check_id: baseline-ci
  name: baseline-ci
  status: passed
  required: true
  target_ids:
  - GO:0110086
  command: gh run view 38194005432 --repo CultureBotAI/CellStructureMech --json status,conclusion,headSha,event,name,url,jobs
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-12T02:35:12Z to 2026-10-12T02:35:13Z; log SHA-256 5c75f24a435f9d0bc44c7d83f136cbb31aa65294bd885abf75d3c5cf1f4f45b5
- check_id: baseline-ci-full
  name: baseline-ci-full
  status: passed
  required: true
  target_ids:
  - GO:0110086
  command: gh run view 38194005432 --repo CultureBotAI/CellStructureMech --log
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-12T02:35:13Z to 2026-10-12T02:35:15Z; log SHA-256 99fae9afbe5251016944a7d753357df4398cee2fe1c7fb5d703a0c3aee0a2698
- check_id: adapter
  name: adapter
  status: passed
  required: true
  target_ids:
  - GO:0110086
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-12T02:35:15Z to 2026-10-12T02:35:15Z; log SHA-256 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- check_id: typed-go
  name: typed-go
  status: passed
  required: true
  target_ids:
  - GO:0110086
  command: .venv/bin/python -c 'from oaklib import get_adapter; import json; a=get_adapter('"'"'sqlite:obo:go'"'"');
    print(json.dumps(list(a.relationships(['"'"'GO:0097568'"'"','"'"'GO:0032157'"'"','"'"'GO:0110086'"'"']))))'
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-12T02:35:07Z to 2026-10-12T02:35:22Z; log SHA-256 c6bc0bac9dfb120a6b52beafa6233c2a28238a3a6c963591efa963822ad78d7d
- check_id: qc
  name: Exact unchanged merged-baseline native QC
  status: passed
  required: true
  target_ids:
  - GO:0110086
  command: gh run view 38194005432 --repo CultureBotAI/CellStructureMech --log
  exit_code: 0
  summary: Exact native merge-group8da5e264 passed979 tests,3 skips and4 contract
    tests;909 strict records and generated artifacts current. Fresh focused/global
    checks separate. Full QC not rerun locally before these no-edit observations.
  scope_note: https://github.com/CultureBotAI/CellStructureMech/actions/runs/38194005432
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/meiotic_actomyosin_contractile_ring.yaml
  accessed_at: '2026-10-12T02:36:00Z'
  snapshot_sha256: a0c3dca4b15179b78b04e657aa274ba03dd5f8d9bd26c5f1534838081afe064e
  support: context_only
  summary: Entire original native YAML read; captured bytes unchanged.
- evidence_id: rules
  kind: record_content
  reference: docs/CURATION.md
  accessed_at: '2026-10-12T02:36:00Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  support: context_only
  summary: Component membership and assembly necessity are distinct; scientific status
    is not promoted.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  accessed_at: '2026-10-12T02:36:00Z'
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
  support: context_only
  summary: ESSENTIAL means the structure does not form without the component.
- evidence_id: predecessors
  kind: validation
  reference: /private/tmp/csm-review-20261012T023100Z/predecessors.json
  accessed_at: '2026-10-12T02:36:00Z'
  snapshot_sha256: a0aa0a6697475908e7fed115e5756d08d4c28993782bdd89d5b34afe3696d08f
  support: context_only
  summary: Ignored-inclusive recursive canonical scan matched exact targetID OR path;
    no match.
- evidence_id: reading
  kind: validation
  reference: /private/tmp/csm-review-20261012T023100Z/reading-checkpoint.json
  accessed_at: '2026-10-12T02:36:00Z'
  snapshot_sha256: 08399c7b74512de2df5c4023b7127ce5e544ce30b52b3cc0f00c6863e9422c74
  support: context_only
  summary: Actual reading scope and explicit source-access limits; source text, not
    search snippets.
- evidence_id: typed-go
  kind: authority
  reference: /private/tmp/csm-review-20261012T023100Z/typed-go.log
  accessed_at: '2026-10-12T02:36:00Z'
  snapshot_sha256: c6bc0bac9dfb120a6b52beafa6233c2a28238a3a6c963591efa963822ad78d7d
  support: context_only
  summary: 'Exact OAK typed relations: prospore is_a meiotic ring; meiotic is_a generic
    actomyosin ring.'
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/csm-review-20261012T023100Z/adapter.log
  accessed_at: '2026-10-12T02:36:00Z'
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
  support: context_only
  summary: Fresh28-dataset iModulonDB inventory has no matching S.pombe/Giardia coverage;
    not negative biological evidence.
- evidence_id: history-0
  kind: record_content
  reference: history/records/meiotic_actomyosin_contractile_ring/2026-09-29T224903Z-codex-3464bd.yaml
  accessed_at: '2026-10-12T02:36:00Z'
  snapshot_sha256: fbe266128475d2dfaff497a97fcce4e17dbb18cb6c8424f065504feb23bd997d
  support: context_only
  summary: Whole append-only history read and preserved.
- evidence_id: legacy
  kind: prior_review
  reference: reports/yaml_record_review/20260929T231019Z-meiotic_actomyosin_contractile_ring.md
  accessed_at: '2026-10-12T02:36:00Z'
  snapshot_sha256: 5cae900c54d5d1d039e285de5fc39cfdeb9d8e4d2d433fe540f2c48644fb5c37
  support: context_only
  summary: Whole historical PR review read; not substituted for fresh source assessment.
- evidence_id: issues
  kind: validation
  reference: /private/tmp/csm-review-20261012T023100Z/issues-2.log
  accessed_at: '2026-10-12T02:36:00Z'
  snapshot_sha256: 6b413d54db0fe0ccf201a9177a2bdef7b8dfad7729b1980c96bbb0adfca90005
  support: context_only
  summary: All-state target searches include already-closed1767 parentage correction,
    still present. No related open finding in these bounded searches.
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0097568%2CGO%3A0005856%2CGO%3A0005874%2CGO%3A0110086%2CGO%3A0032157%2CGO%3A0005826%2CGO%3A0110085%2CGO%3A0032169
  locator: Exact eight terms, current definitions/synonym types/typed children
  accessed_at: '2026-10-12T02:28:49Z'
  snapshot_sha256: aca4fbd868bfa4d9ff3630394b6d07d493b8cad1e353f87a985ded4fcc13cc31
  support: supports
  summary: Both exact identities and direct is-a relations agree. Definitions assert
    composition and location, not component-depletion outcomes.
- evidence_id: taxon
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896
  locator: ENA4896 species identity
  accessed_at: '2026-10-12T02:28:50Z'
  snapshot_sha256: cdb53b3f4ab5e6bb4476de3bf0db333ae647e307a9fa8f98108827f98fe7f4d3
  support: supports
  summary: S.pombe verified; source experiments establish the occurrence, not the
    taxonomic resolver.
- evidence_id: paper-metadata
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1242%2Fjcs.091561%22&format=json&resultType=core
  locator: PMID22526418 primary abstract and original DOI metadata
  accessed_at: '2026-10-12T02:28:48Z'
  snapshot_sha256: 28f45a9d4240feb58fb29234f538e81e982a87423044d465dbf7360a0e03b506
  support: supports
  summary: MeiAR forms during meiosisII and coordinates forespore membranes; PubMed
    retains the original DOI.
- evidence_id: corrected-doi
  kind: authority
  reference: https://api.crossref.org/works/10.1242%2Fjcs.jcs091561
  locator: Issuing DOI metadata
  accessed_at: '2026-10-12T02:31:46Z'
  snapshot_sha256: 70798c15f31460a5370d28c26d9a45ad415b377d052010c778858ad68e62f965
  support: supports
  summary: Canonical deposited DOI is10.1242/jcs.jcs091561. The original alias also
    resolves to this canonical object.
- evidence_id: erratum-doi
  kind: authority
  reference: https://api.crossref.org/works/10.1242%2Fjcs.113316
  locator: DOI10.1242/jcs.113316 metadata
  accessed_at: '2026-10-12T02:31:47Z'
  snapshot_sha256: e4a6e6996974ec8be2a88eb0625ce31899852cf8e4f2a7e3d37a2c22c792cf0b
  support: supports
  summary: Publisher erratum identity verified.
- evidence_id: erratum
  kind: primary_source
  reference: DOI:10.1242/jcs.113316
  locator: 'Publisher full correction: https://journals.biologists.com/jcs/article/125/10/2544/32305/Meiotic-actin-rings-are-essential-for-proper'
  accessed_at: '2026-10-12T02:36:00Z'
  support: supports
  summary: The correction explicitly gives10.1242/jcs.jcs091561 as the correct paper
    DOI. It changes provenance, not experimental conclusions.
- evidence_id: yan
  kind: primary_source
  reference: DOI:10.1242/jcs.jcs091561
  locator: Publisher full main text and six captions at https://journals.biologists.com/jcs/article/125/6/1429/33273/Meiotic-actin-rings-are-essential-for-proper
  accessed_at: '2026-10-12T02:36:00Z'
  support: supports
  summary: Fission-yeast actin ring expansion/closure and membrane coordination are
    observed. Myo1 and Rlc1 localize; individual myosinII mutants sporulate, and the
    double mutant was not testable. Ring closure is not demonstrated typeII-myosin
    force generation.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact class, hierarchy and neighboring-ring boundaries
  outcome: supported
  target_ids:
  - GO:0110086
  evidence_ids:
  - record
  - go
  - typed-go
  summary: Exact GO cellular-component identity and direct is-a parent are supported.
    Prospore subtype, broad meiotic class, mitotic sibling and septin ring remain
    distinct. FILAMENT denotes a filamentous ring structure, not a single protein.
- assessment_id: retained-biology
  area: evidence
  topic: Composition, present taxonomy/functions and all graph edges
  outcome: supported
  target_ids:
  - GO:0110086
  evidence_ids:
  - record
  - go
  - yan
  - taxon
  summary: Broad actin/myosin membership and nonmechanistic topology edges are supported
    at the declared ontology tier. Meiotic record has a condition-qualified S.pombe
    example and observed expansion/closure; no explicit myosinII motor requirement
    or exact stoichiometry is asserted. Prospore record makes no taxonomic prevalence
    assertion. These claims do not determine assembly essentiality.
- assessment_id: finding
  area: evidence
  topic: Use the publisher-corrected MeiAR paper DOI
  outcome: concern
  target_ids:
  - GO:0110086
  evidence_ids:
  - record
  - rules
  - schema
  - go
  - yan
  - corrected-doi
  - erratum
  summary: All current paper references use DOI:10.1242/jcs.091561, the number corrected
    by the publisher erratum DOI:10.1242/jcs.113316. Both the article page and issuing
    Crossref object give DOI:10.1242/jcs.jcs091561. The old alias resolves, so this
    is a bounded provenance defect, not a wrong-paper or unreadability finding. Replace
    current reference values, preserve the inspected biological claims, and attach
    a short provenance note naming the correction. Do not rewrite historical events
    or reports.
- assessment_id: provenance
  area: completeness
  topic: Open questions, histories and optional resources
  outcome: supported
  target_ids:
  - GO:0110086
  evidence_ids:
  - record
  - rules
  - reading
  summary: Unknown exact family/accessory boundaries remain legitimate open work.
    No optional image, property, dataset, trait or pathway is fabricated. Both original
    histories and prior reports are preserved; PROPOSED is unchanged.
findings:
- finding_id: F1
  issue_key: meiotic-ring-corrected-publication-doi
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Use the publisher-corrected MeiAR paper DOI
  description: All current paper references use DOI:10.1242/jcs.091561, the number
    corrected by the publisher erratum DOI:10.1242/jcs.113316. Both the article page
    and issuing Crossref object give DOI:10.1242/jcs.jcs091561. The old alias resolves,
    so this is a bounded provenance defect, not a wrong-paper or unreadability finding.
    Replace current reference values, preserve the inspected biological claims, and
    attach a short provenance note naming the correction. Do not rewrite historical
    events or reports.
  target_ids:
  - GO:0110086
  field_paths:
  - evidence
  - components[0].evidence
  - taxonomic_distribution[0].reference
  - canonical_examples[0].reference
  - functions[0].evidence
  - discussions[1].evidence
  evidence_ids:
  - record
  - rules
  - schema
  - go
  - yan
  - corrected-doi
  - erratum
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/meiotic_actomyosin_contractile_ring.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#evidence
  native_severity: minor
  normalization_reason: Corrected resolving alias is nonblocking provenance; unsupported
    categorical assembly requirements change structured scientific meaning.
actions:
- action_id: A1
  description: Use the publisher-corrected MeiAR paper DOI
  finding_ids:
  - F1
  target_ids:
  - GO:0110086
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/meiotic_actomyosin_contractile_ring.yaml
    role: maintained scientific record
  acceptance_checks:
  - All current paper references use DOI:10.1242/jcs.091561, the number corrected
    by the publisher erratum DOI:10.1242/jcs.113316. Both the article page and issuing
    Crossref object give DOI:10.1242/jcs.jcs091561. The old alias resolves, so this
    is a bounded provenance defect, not a wrong-paper or unreadability finding. Replace
    current reference values, preserve the inspected biological claims, and attach
    a short provenance note naming the correction. Do not rewrite historical events
    or reports.
  - Guarded writer; append actual Codex event and one EDIT history per changed record.
    Preserve all original histories, discussion rationale, graph content, taxonomic
    scope and PROPOSED status.
  - Focused red/green regressions, regenerated pages, semantic-map drift check and
    full native QC. Save an exact-lineage successor disposition; pass PR and native
    merge-group gates before merge.
limitations:
- Same-agent scientific review; no independent human sign-off or raw-data reanalysis.
- Yan2012 full scientific text/captions read via publisher web retrieval; local requests
  returned403. Figure pixels, movies and supplements not inspected. No quantitative
  or exact-myofibril-mechanism claim introduced.
- Myo2/Myp2 individual mutant sporulation is not a complete myosin-class deletion
  or a direct assembly assay. Current generic composition claims remain ontology-tier;
  force mechanism unresolved.
- Exact-baseline full QC/contract CI reused at unchanged8da5; fresh focused/global
  checks retain6 label exceptions,603 no-adapter cases,251 CURIE policy skips and3
  baseline test skips.
- No matching adopted iModulonDB dataset; not negative evidence. Alias-bounded GitHub
  search and ignored-inclusive canonical scan have different scopes.
- Median body has separate whole-record coverage; no clean bundle or no-change history
  will be generated.
```
