# flagellum attachment zone: evidence and structure review

- Review: 20261011T233246Z-flagellum_attachment_zone-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T23:26:08Z
- Finished UTC: 2026-10-11T23:32:46Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Entire native record assessed; observed issue(s) saved before any scientific mutation.

## Scope And Provenance

Whole native YAML including identity, typed relations, every component/function/graph edge, taxon/example, discussions and both history surfaces. Source access limitations retained per paper.

Selection: One exact record within the active 909-record goal; no batch sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6b8e8880fd22415798fab889eacb8db10bddead2.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0120119 | data/structures/cytoskeleton/flagellum_attachment_zone.yaml | maintained | flagellum attachment zone |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0120119 | Actual deterministic check passed; scientific support assessed separately. |
| strict | passed | True | GO:0120119 | Actual deterministic check passed; scientific support assessed separately. |
| snippets | passed | True | GO:0120119 | No verbatim snippets; paraphrases assessed separately against inspected text. |
| history | passed | True | GO:0120119 | Actual deterministic check passed; scientific support assessed separately. |
| labels | passed | True | GO:0120119 | id↔label correspondence summary:<br>          OK_CANONICAL: 3545<br>            OK_SYNONYM: 50<br>          OK_EXCEPTION: 6<br>    SKIPPED_NO_ADAPTER: 603<br><br>✅ All id↔label pairs correspond. |
| traits | passed | True | GO:0120119 | Actual deterministic check passed; scientific support assessed separately. |
| curies | passed | True | GO:0120119 | [not exercised] BFO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] CHEBI: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] ComplexPortal: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] DOI: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] GO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] InterPro: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] NCBITaxon: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] PATO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] PMID: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] RO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] SO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] UO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] UniProtKB: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] DOI: DataCite was unreachable, so DOI:10.22002/D1.1355 was not exercised<br>resolver control: 14 resolver(s) could not be exercised because their authority was unreachable; the rest accept a known id and reject a fabricated one<br><br>identifier liveness summary:<br>  OK             4016<br>  SKIPPED         251<br><br>Every identifier resolves at its issuing authority. |
| reviews | passed | True | GO:0120119 | Actual deterministic check passed; scientific support assessed separately. |
| Exact-base native merge-group QC | passed | True | GO:0120119 | Exact 6b8e8880 baseline QC success verified from live run metadata and complete log. Not a fresh full local QC run. |

## Scientific And Domain Assessments

### Four components, gene identities, taxon/example, three functions and six edges

evidence: supported. Targets: GO:0120119.

FAZ1 Tb927.4.3740, FAZ2 Tb927.1.4310 and CC2D Tb927.4.2080 identities agree with primary text and review Table 1. Filament OTHER boundary, FAZ2-specific example and CC2D affinity-purification edge remain scoped. RNAi stability effects and proximal incorporation support coarse roles, not direct binding, exclusive localization, purified sufficiency or complete loss. FAZ1 normal-structure role remains valid despite the essentiality finding.

### Do not infer absolute FAZ assembly essentiality from FAZ1 knockdown

evidence: concern. Targets: GO:0120119.

FAZ1 is ESSENTIAL, which locally means the structure does not form without the component. Vaughan 2008 instead observes aberrant FAZ-like material and remaining filament markers after RNAi; normal attachment and cytokinesis are impaired. The authors explicitly allow knockdown degree to affect phenotype. This supports neither categorical failure of all assembly nor proven formation after complete protein loss. Use UNKNOWN for assembly essentiality while retaining the experimentally supported normal-structure role.

### Identity and structure relationships

grounding: supported. Targets: GO:0120119.

Exact GO structure identity, definition, category/kind and synonym evidence are supported. No single protein is substituted for a structure. The broad FAZ is correctly OTHER, not an individual protein or the FAZ filament alone. FAZ synonym type agrees with GO.

### Discussions, optional surfaces and status

completeness: supported. Targets: GO:0120119.

All original inline/repository history and open scope/grounding discussions read. Missing optional stoichiometry, physical measurements, images, datasets, protein examples and trait/pathway links are not defects. PROPOSED is retained. This is a bounded review of represented claims and consequential gaps, not an exhaustive discovery of every later protein or publication.

## Findings

### F1: Do not infer absolute FAZ assembly essentiality from FAZ1 knockdown

major / open / confirmed; issue key: faz1-assembly-essentiality-rnai-scope.

FAZ1 is ESSENTIAL, which locally means the structure does not form without the component. Vaughan 2008 instead observes aberrant FAZ-like material and remaining filament markers after RNAi; normal attachment and cytokinesis are impaired. The authors explicitly allow knockdown degree to affect phenotype. This supports neither categorical failure of all assembly nor proven formation after complete protein loss. Use UNKNOWN for assembly essentiality while retaining the experimentally supported normal-structure role.

## Recommended Actions And Acceptance Checks

### A1

Do not infer absolute FAZ assembly essentiality from FAZ1 knockdown

- Set only FAZ1 assembly essentiality to UNKNOWN, not DISPENSABLE, since RNAi is not a demonstrated protein null.
- Add assertion-local notes on residual abnormal assembly and the depletion limit; preserve normal-structure role, graph and all FAZ2/CC2D evidence.
- Guarded writer; append only actual Codex curation and EDIT history; preserve PROPOSED, all original events/discussions and historical bundles.
- Regenerate target products, pass focused regressions and native gates; save an exact-lineage successor.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/flagellum_attachment_zone.yaml | context_only | Entire original native record read and unchanged captured bytes verified. |
| rules | docs/CURATION.md | context_only | Typed parthood, assertion-local evidence and assembly-only essentiality rules. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml | context_only | Essentiality concerns structure formation, possibly defectively; gene symbols are metadata, not component identity. |
| reading | /private/tmp/csm-review-20261011T232800Z/reading-checkpoint.json | context_only | Preserved source reading chronology and explicit abstract/full-text/visual limits. |
| predecessors | /private/tmp/csm-review-20261011T232800Z/predecessors.json | context_only | Ignored-inclusive canonical bundle scan; no exact-target predecessor. |
| go-relations | /private/tmp/csm-review-20261011T222903Z/next-go-relations.log | context_only | Source-native OAK typed relations inspected, independently consistent with QuickGO terms. |
| context | /private/tmp/csm-review-20261011T232800Z/context-search.log | context_only | Identifier/label/slug search includes ignored and hidden repository files, excluding Git internals and dependency trees. |
| adapter | /private/tmp/csm-review-20261011T222903Z/next-adapter.log | context_only | All 28 iModulonDB dataset rows inspected; no matching Trypanosoma dataset. Not negative biological evidence. |
| history-0 | history/records/flagellum_attachment_zone/2026-09-12T021349Z-codex-3c7249.yaml | context_only | Entire original append-only history read; preserve historical actors and resolved issue scope. |
| dedup-faz1-assembly-essentiality-rnai-scope | /private/tmp/csm-review-20261011T232800Z/dedup-faz1-assembly-essentiality-rnai-scope.log | context_only | All-state exact-key GitHub issue search checked before creation. Any earlier sandbox network failure remains in separate receipt. |
| paper-1 | https://wheelerlab.net/publications/17945531.pdf; DOI:10.1016/j.protis.2007.08.005; complete main text and all six captions; Figure 4 page 132 visually inspected | supports | Procyclic PTP-line FAZ1 RNAi leaves aberrant FAZ-like material and other filament markers despite attachment/cytokinesis defects. Knockdown degree is an explicit caveat; not a complete null experiment. |
| paper-2 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4827413/fullTextXML; DOI:10.1016/j.pt.2015.12.010; complete main text, Table 1 and four captions | supports | Review distinguishes FAZ zones, species/life-stage expression, gene IDs and a disorganized but retained FAZ after FAZ1 knockdown. Models of pulling, targeting and assembly hierarchy are not established native mechanisms. This is a literature review, not a new primary experiment. |
| paper-6 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1111%2Fj.1550-7408.1999.tb04592.x%22&amp;format=json&amp;resultType=core; DOI:10.1111/j.1550-7408.1999.tb04592.x; primary abstract and metadata only | supports | FAZ filament and PFR antibody localization and differing assembly timing/rates support the narrow record note. No claim that full methods or original figures were read. |
| paper-8 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1242%2Fjcs.087676%22&amp;format=json&amp;resultType=core; DOI:10.1242/jcs.087676; primary abstract and metadata only | supports | CC2D is reported at the filament, adjacent ER and basal bodies; RNAi yields a short FAZ stub and altered morphology. Not a protein-null or exclusive-localization claim. |
| paper-9 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4524107/; DOI:10.1242/jcs.168377; abstract, entire Results, Discussion, Methods and eight captions | supports | Procyclic 427/29-13 experiments identify FAZ2, retain old and short new FAZ after RNAi, destabilize other proteins, recover CC2D/KMP11 by affinity purification/co-IP and track proximal incorporation. Association is not purified direct binary binding. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0005856,GO%3A0020016,GO%3A0120119,GO%3A0120120,GO%3A0120269,GO%3A0140535,GO%3A1990900; Exact GO IDs, definitions, synonyms and child relation types | supports | Identity terms denote the requested structures; GO lexical synonymy is not an assertion that all historical protein cohorts are physically identical. |
| taxon | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5691; TaxId/name/rank | supports | T. brucei species identity verified; experiments remain limited to named laboratory forms/lines. |
| figure-4 | /private/tmp/csm-review-20261011T232800Z/faz1-page6.png | context_only | Actual original PDF page 132 visually inspected: Figure 4 TEM/IF panels show aberrant residual structure and patchy markers, with its complete caption. |

## Limits And Additional Notes

- Same-agent scientific review, not independent human approval or raw-data reanalysis.
- Original source access dates/hashes are retained from the read-ahead phase. Actual reading scope is recorded per source; separate supplements, movies and raw experiments were not reviewed.
- 2009 MORN1, 1999 FAZ assembly and 2011 CC2D remain primary-abstract-only for narrow supported claims; full-text inaccessibility is not asserted globally. Other material sources have the inspected main-text scope stated in evidence.
- The 2008 FAZ1 Figure 4 is visually inspected only for the FAZ review; other main figures were read as captions, not certified pixel-level reanalyses. No source media adopted.
- Exact baseline full QC is verified CI; fresh local schema/strict/history/label/reference/trait/review checks are separate. Existing identifier-policy/no-adapter and test skips remain explicit.
- No exact whole-family accession is invented and no absence from iModulonDB is biological evidence. Neighboring flagellar pocket and newer-publication leads are not counted as completed reviews.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T233246Z-flagellum_attachment_zone-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'flagellum attachment zone: evidence and structure review'
started_at: '2026-10-11T23:26:08Z'
finished_at: '2026-10-11T23:32:46Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent whole-record and primary-source assessment, not independent
    human approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Entire native record assessed; observed issue(s) saved before any scientific
  mutation.
source:
  git_revision: 6b8e8880fd22415798fab889eacb8db10bddead2
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
    sha256: 3acb13884094f40c840ed3452a6209ee9a38b479ae16e4c0bca390c3c290828a
    role: context
  - path: curation/source_queue.tsv
    sha256: 55d8fe79b5edd7d6b42bf4ca9168fe4878240417716e2f4ba423489144b89284
    role: context
  - path: data/structures/cytoskeleton/bilobe_structure.yaml
    sha256: 19e9083dd8c398e9ab49a74949bb53d0e0c0c16058d800c87619da78ebd0885f
    role: context
  - path: data/structures/cytoskeleton/ciliary_centrin_arm.yaml
    sha256: 076a14eebce9d80acada8668f1ff0c82f7d2949a7ce0a0ae76a5478fca4a1a96
    role: context
  - path: data/structures/cytoskeleton/ciliary_pocket_collar.yaml
    sha256: abefa0652c7dfae6a06cd962f7c0805dd526c230f87180b35c408e076bd6a9b4
    role: context
  - path: data/structures/cytoskeleton/flagellum_attachment_zone.yaml
    sha256: a3c88e9e9a6b27327238a732a4d6cdc4740ba50f26c581d251bfb5ad12f7dc0c
    role: target
  - path: data/structures/membrane_organelle/flagellar_pocket.yaml
    sha256: d67c465d104f21905f63ea994b6f4f526a51502cefccf79e9e732698f4971fa8
    role: context
  - path: docs/CURATION.md
    sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
    role: context
  - path: docs/SCHEMA.md
    sha256: 07b8f936a553a45cc6e8dba924c21e6af48c81b3866725efeb00c8183f0c75a2
    role: context
  - path: docs/SOURCE_QUEUE.md
    sha256: 793e9a16435684b90b0d64b7be4bdfeffbba5ab6ac0ca99eadf25c8548e22729
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
  - path: history/records/flagellum_attachment_zone/2026-09-12T021349Z-codex-3c7249.yaml
    sha256: 428a3afaa3d407d620cb07027273f1bfe65a45deaee9012da96b90da500b28ff
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: pages/structures/cytoskeleton/flagellum_attachment_zone.html
    sha256: 3ac6964adb6c6cc5cdbff0717be944deb71659b31d672dc6712aaefd4ea89dd5
    role: context
  - path: scripts/render_pages.py
    sha256: b5be74a8a3a0f7190b63da47a86cd8b48cbce4bb955ea0896f29d24f214a9b22
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: src/cellstructuremech/templates/structure.html
    sha256: 417b020a6eda677a1e40ecd3d849bfd5063d83291d7496e1c52a1a3a321f35ed
    role: context
targets:
- target_id: GO:0120119
  path: data/structures/cytoskeleton/flagellum_attachment_zone.yaml
  label: flagellum attachment zone
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/flagellum_attachment_zone.yaml
    role: maintained scientific record
scope:
  description: Whole native YAML including identity, typed relations, every component/function/graph
    edge, taxon/example, discussions and both history surfaces. Source access limitations
    retained per paper.
  selection: One exact record within the active 909-record goal; no batch sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0120119
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - GO:0120119
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/flagellum_attachment_zone.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T23:27:21Z to 2026-10-11T23:27:23Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - GO:0120119
  command: .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/flagellum_attachment_zone.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T23:27:23Z to 2026-10-11T23:27:26Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - GO:0120119
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/cytoskeleton/flagellum_attachment_zone.yaml
    --report /private/tmp/csm-review-20261011T232800Z/flagellum_attachment_zone-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: No verbatim snippets; paraphrases assessed separately against inspected
    text.
  scope_note: 2026-10-11T23:27:26Z to 2026-10-11T23:27:44Z; log SHA-256 ce3f8b903c129e79d003c3769d89f364c4afeb3dcf52c486d926dbc4ede9f157
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:0120119
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T23:27:44Z to 2026-10-11T23:27:58Z; log SHA-256 e2ce523e6e88c9e5ea99c23750f1c095bb4476f6573aead8b46a1d5d8ff2e754
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - GO:0120119
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: "id↔label correspondence summary:\n          OK_CANONICAL: 3545\n     \
    \       OK_SYNONYM: 50\n          OK_EXCEPTION: 6\n    SKIPPED_NO_ADAPTER: 603\n\
    \n✅ All id↔label pairs correspond."
  scope_note: 2026-10-11T23:27:58Z to 2026-10-11T23:29:17Z; log SHA-256 459523b233cf29c593d6ebe49a38d5ed4484b1f98496dc47ea4fdc17be729286
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - GO:0120119
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T23:32:04Z to 2026-10-11T23:32:30Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - GO:0120119
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
    \ one\n\nidentifier liveness summary:\n  OK             4016\n  SKIPPED      \
    \   251\n\nEvery identifier resolves at its issuing authority."
  scope_note: 2026-10-11T23:29:34Z to 2026-10-11T23:29:57Z; log SHA-256 fea3297b8556f2bc1f9b7053d2e57fa238f7e27121b7eab5396a9b3b27ec0c80
- check_id: reviews
  name: reviews
  status: passed
  required: true
  target_ids:
  - GO:0120119
  command: .venv/bin/python scripts/record_review.py check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T23:29:57Z to 2026-10-11T23:31:27Z; log SHA-256 45a25fc1072d38a21fae9e79615ac64cf2ae2b52e40088ef081e2c6581728997
- check_id: baseline-qc
  name: Exact-base native merge-group QC
  status: passed
  required: true
  target_ids:
  - GO:0120119
  command: gh run view 38183517588 --repo CultureBotAI/CellStructureMech --log
  exit_code: 0
  summary: Exact 6b8e8880 baseline QC success verified from live run metadata and
    complete log. Not a fresh full local QC run.
  scope_note: https://github.com/CultureBotAI/CellStructureMech/actions/runs/38183517588;
    SHA-256 525a55d17a881a4c84dad779082212e22f4340030d6a86859c0b1702d026b789
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/flagellum_attachment_zone.yaml
  accessed_at: '2026-10-11T23:32:46Z'
  snapshot_sha256: a3c88e9e9a6b27327238a732a4d6cdc4740ba50f26c581d251bfb5ad12f7dc0c
  support: context_only
  summary: Entire original native record read and unchanged captured bytes verified.
- evidence_id: rules
  kind: record_content
  reference: docs/CURATION.md
  accessed_at: '2026-10-11T23:32:46Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  support: context_only
  summary: Typed parthood, assertion-local evidence and assembly-only essentiality
    rules.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  accessed_at: '2026-10-11T23:32:46Z'
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
  support: context_only
  summary: Essentiality concerns structure formation, possibly defectively; gene symbols
    are metadata, not component identity.
- evidence_id: reading
  kind: validation
  reference: /private/tmp/csm-review-20261011T232800Z/reading-checkpoint.json
  accessed_at: '2026-10-11T23:32:46Z'
  snapshot_sha256: eacec47a4ec83f7aea2dc57abf00b895a6e216bf1d1c76ee2f5c9855606301c6
  support: context_only
  summary: Preserved source reading chronology and explicit abstract/full-text/visual
    limits.
- evidence_id: predecessors
  kind: validation
  reference: /private/tmp/csm-review-20261011T232800Z/predecessors.json
  accessed_at: '2026-10-11T23:32:46Z'
  snapshot_sha256: 4f1c46b912fe671dcc64a5d99949cef6f94e3090587c5806a3ba5a876602b212
  support: context_only
  summary: Ignored-inclusive canonical bundle scan; no exact-target predecessor.
- evidence_id: go-relations
  kind: authority
  reference: /private/tmp/csm-review-20261011T222903Z/next-go-relations.log
  accessed_at: '2026-10-11T23:32:46Z'
  snapshot_sha256: a262339b1fbbc4277e13ac20c44b1875fd6042cc5209596e64eed932c6413396
  support: context_only
  summary: Source-native OAK typed relations inspected, independently consistent with
    QuickGO terms.
- evidence_id: context
  kind: validation
  reference: /private/tmp/csm-review-20261011T232800Z/context-search.log
  accessed_at: '2026-10-11T23:32:46Z'
  snapshot_sha256: 1ba49870de1404b7f4c562c367b0563ca9ce248e3d0349886dd8ae944b8a267a
  support: context_only
  summary: Identifier/label/slug search includes ignored and hidden repository files,
    excluding Git internals and dependency trees.
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/csm-review-20261011T222903Z/next-adapter.log
  accessed_at: '2026-10-11T23:32:46Z'
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
  support: context_only
  summary: All 28 iModulonDB dataset rows inspected; no matching Trypanosoma dataset.
    Not negative biological evidence.
- evidence_id: history-0
  kind: record_content
  reference: history/records/flagellum_attachment_zone/2026-09-12T021349Z-codex-3c7249.yaml
  accessed_at: '2026-10-11T23:32:46Z'
  snapshot_sha256: 428a3afaa3d407d620cb07027273f1bfe65a45deaee9012da96b90da500b28ff
  support: context_only
  summary: Entire original append-only history read; preserve historical actors and
    resolved issue scope.
- evidence_id: dedup-faz1-assembly-essentiality-rnai-scope
  kind: validation
  reference: /private/tmp/csm-review-20261011T232800Z/dedup-faz1-assembly-essentiality-rnai-scope.log
  accessed_at: '2026-10-11T23:32:46Z'
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
  support: context_only
  summary: All-state exact-key GitHub issue search checked before creation. Any earlier
    sandbox network failure remains in separate receipt.
- evidence_id: paper-1
  kind: primary_source
  reference: https://wheelerlab.net/publications/17945531.pdf
  locator: DOI:10.1016/j.protis.2007.08.005; complete main text and all six captions;
    Figure 4 page 132 visually inspected
  accessed_at: '2026-10-11T23:21:28Z'
  snapshot_sha256: b396a9805e20bbf2b0fe72c148fb1217dda4589e0d9a6ed265d16c712c451ac6
  support: supports
  summary: Procyclic PTP-line FAZ1 RNAi leaves aberrant FAZ-like material and other
    filament markers despite attachment/cytokinesis defects. Knockdown degree is an
    explicit caveat; not a complete null experiment.
- evidence_id: paper-2
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4827413/fullTextXML
  locator: DOI:10.1016/j.pt.2015.12.010; complete main text, Table 1 and four captions
  accessed_at: '2026-10-11T22:54:07Z'
  snapshot_sha256: 616b6f43ba776fdf150e6a39c41fe056779efa6f9a3a540a372167dd70c1e67f
  support: supports
  summary: Review distinguishes FAZ zones, species/life-stage expression, gene IDs
    and a disorganized but retained FAZ after FAZ1 knockdown. Models of pulling, targeting
    and assembly hierarchy are not established native mechanisms. This is a literature
    review, not a new primary experiment.
- evidence_id: paper-6
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1111%2Fj.1550-7408.1999.tb04592.x%22&format=json&resultType=core
  locator: DOI:10.1111/j.1550-7408.1999.tb04592.x; primary abstract and metadata only
  accessed_at: '2026-10-11T22:54:12Z'
  snapshot_sha256: 505a42a6e88acc382a5595a6648e621a228689d30601de45f92b7e0a83d2949b
  support: supports
  summary: FAZ filament and PFR antibody localization and differing assembly timing/rates
    support the narrow record note. No claim that full methods or original figures
    were read.
- evidence_id: paper-8
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1242%2Fjcs.087676%22&format=json&resultType=core
  locator: DOI:10.1242/jcs.087676; primary abstract and metadata only
  accessed_at: '2026-10-11T22:54:14Z'
  snapshot_sha256: 5ca9f8602a88065868f02ea09b1753a8708a001adbe0b4db527da6fd31f718ba
  support: supports
  summary: CC2D is reported at the filament, adjacent ER and basal bodies; RNAi yields
    a short FAZ stub and altered morphology. Not a protein-null or exclusive-localization
    claim.
- evidence_id: paper-9
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4524107/
  locator: DOI:10.1242/jcs.168377; abstract, entire Results, Discussion, Methods and
    eight captions
  accessed_at: '2026-10-11T22:54:50Z'
  snapshot_sha256: 09cf00b49c01059a1b81c5912c994204218addefdd5f2cd24344a1a9d2fccd32
  support: supports
  summary: Procyclic 427/29-13 experiments identify FAZ2, retain old and short new
    FAZ after RNAi, destabilize other proteins, recover CC2D/KMP11 by affinity purification/co-IP
    and track proximal incorporation. Association is not purified direct binary binding.
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0005856,GO%3A0020016,GO%3A0120119,GO%3A0120120,GO%3A0120269,GO%3A0140535,GO%3A1990900
  locator: Exact GO IDs, definitions, synonyms and child relation types
  accessed_at: '2026-10-11T22:57:55Z'
  snapshot_sha256: 2193158f92fafcc78c308b1ae6dcbcb7483113522fe12b201f3665c879e99c2e
  support: supports
  summary: Identity terms denote the requested structures; GO lexical synonymy is
    not an assertion that all historical protein cohorts are physically identical.
- evidence_id: taxon
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5691
  locator: TaxId/name/rank
  accessed_at: '2026-10-11T22:57:55Z'
  snapshot_sha256: ba78ff6fe5de62b2654b61e249c2c87b239dca0208950b0e4ecf3ef2d81c99be
  support: supports
  summary: T. brucei species identity verified; experiments remain limited to named
    laboratory forms/lines.
- evidence_id: figure-4
  kind: primary_source
  reference: /private/tmp/csm-review-20261011T232800Z/faz1-page6.png
  accessed_at: '2026-10-11T23:32:46Z'
  snapshot_sha256: a88175bae6e04cb95df8c34e83f10a872548ac740824b1af0a66f5c9734ea9ae
  support: context_only
  summary: 'Actual original PDF page 132 visually inspected: Figure 4 TEM/IF panels
    show aberrant residual structure and patchy markers, with its complete caption.'
assessments:
- assessment_id: biology
  area: evidence
  topic: Four components, gene identities, taxon/example, three functions and six
    edges
  outcome: supported
  target_ids:
  - GO:0120119
  evidence_ids:
  - record
  - paper-1
  - paper-2
  - paper-6
  - paper-8
  - paper-9
  - go
  summary: FAZ1 Tb927.4.3740, FAZ2 Tb927.1.4310 and CC2D Tb927.4.2080 identities agree
    with primary text and review Table 1. Filament OTHER boundary, FAZ2-specific example
    and CC2D affinity-purification edge remain scoped. RNAi stability effects and
    proximal incorporation support coarse roles, not direct binding, exclusive localization,
    purified sufficiency or complete loss. FAZ1 normal-structure role remains valid
    despite the essentiality finding.
- assessment_id: faz1-assembly-essentiality-rnai-scope
  area: evidence
  topic: Do not infer absolute FAZ assembly essentiality from FAZ1 knockdown
  outcome: concern
  target_ids:
  - GO:0120119
  evidence_ids:
  - record
  - rules
  - schema
  - paper-1
  - paper-2
  - figure-4
  summary: FAZ1 is ESSENTIAL, which locally means the structure does not form without
    the component. Vaughan 2008 instead observes aberrant FAZ-like material and remaining
    filament markers after RNAi; normal attachment and cytokinesis are impaired. The
    authors explicitly allow knockdown degree to affect phenotype. This supports neither
    categorical failure of all assembly nor proven formation after complete protein
    loss. Use UNKNOWN for assembly essentiality while retaining the experimentally
    supported normal-structure role.
- assessment_id: identity
  area: grounding
  topic: Identity and structure relationships
  outcome: supported
  target_ids:
  - GO:0120119
  evidence_ids:
  - record
  - go
  - go-relations
  summary: Exact GO structure identity, definition, category/kind and synonym evidence
    are supported. No single protein is substituted for a structure. The broad FAZ
    is correctly OTHER, not an individual protein or the FAZ filament alone. FAZ synonym
    type agrees with GO.
- assessment_id: provenance
  area: completeness
  topic: Discussions, optional surfaces and status
  outcome: supported
  target_ids:
  - GO:0120119
  evidence_ids:
  - record
  - rules
  - reading
  - context
  summary: All original inline/repository history and open scope/grounding discussions
    read. Missing optional stoichiometry, physical measurements, images, datasets,
    protein examples and trait/pathway links are not defects. PROPOSED is retained.
    This is a bounded review of represented claims and consequential gaps, not an
    exhaustive discovery of every later protein or publication.
findings:
- finding_id: F1
  issue_key: faz1-assembly-essentiality-rnai-scope
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Do not infer absolute FAZ assembly essentiality from FAZ1 knockdown
  description: FAZ1 is ESSENTIAL, which locally means the structure does not form
    without the component. Vaughan 2008 instead observes aberrant FAZ-like material
    and remaining filament markers after RNAi; normal attachment and cytokinesis are
    impaired. The authors explicitly allow knockdown degree to affect phenotype. This
    supports neither categorical failure of all assembly nor proven formation after
    complete protein loss. Use UNKNOWN for assembly essentiality while retaining the
    experimentally supported normal-structure role.
  target_ids:
  - GO:0120119
  field_paths:
  - components[1].essentiality
  - components[1].evidence[0].notes
  evidence_ids:
  - record
  - rules
  - schema
  - paper-1
  - paper-2
  - figure-4
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/flagellum_attachment_zone.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: major
  normalization_reason: Wrong typed ontology relation or unsupported assembly-essentiality
    classification affects structured biological interpretation.
actions:
- action_id: A1
  description: Do not infer absolute FAZ assembly essentiality from FAZ1 knockdown
  finding_ids:
  - F1
  target_ids:
  - GO:0120119
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/flagellum_attachment_zone.yaml
    role: maintained scientific record
  acceptance_checks:
  - Set only FAZ1 assembly essentiality to UNKNOWN, not DISPENSABLE, since RNAi is
    not a demonstrated protein null.
  - Add assertion-local notes on residual abnormal assembly and the depletion limit;
    preserve normal-structure role, graph and all FAZ2/CC2D evidence.
  - Guarded writer; append only actual Codex curation and EDIT history; preserve PROPOSED,
    all original events/discussions and historical bundles.
  - Regenerate target products, pass focused regressions and native gates; save an
    exact-lineage successor.
limitations:
- Same-agent scientific review, not independent human approval or raw-data reanalysis.
- Original source access dates/hashes are retained from the read-ahead phase. Actual
  reading scope is recorded per source; separate supplements, movies and raw experiments
  were not reviewed.
- 2009 MORN1, 1999 FAZ assembly and 2011 CC2D remain primary-abstract-only for narrow
  supported claims; full-text inaccessibility is not asserted globally. Other material
  sources have the inspected main-text scope stated in evidence.
- The 2008 FAZ1 Figure 4 is visually inspected only for the FAZ review; other main
  figures were read as captions, not certified pixel-level reanalyses. No source media
  adopted.
- Exact baseline full QC is verified CI; fresh local schema/strict/history/label/reference/trait/review
  checks are separate. Existing identifier-policy/no-adapter and test skips remain
  explicit.
- No exact whole-family accession is invented and no absence from iModulonDB is biological
  evidence. Neighboring flagellar pocket and newer-publication leads are not counted
  as completed reviews.
```
