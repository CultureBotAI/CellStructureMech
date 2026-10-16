# Phycobilisome source attribution and architecture-scope review

- Review: 20261012T092129Z-phycobilisome-source-architecture
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-12T09:10:35Z
- Finished UTC: 2026-10-12T09:21:29Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Two confirmed major findings: conflated state-specific structural citations and an unqualified core requirement despite documented coreless alternatives. Native identity, hierarchy and eleven protein identities are supported. Review remains partial because the Sui2021 photoprotection attribution could not be verified.

## Scope And Provenance

One entire native record read; all component/example/graph fields assessed within stated source limits. One claim-level citation attribution remains unassessed; no sampling.

Selection: data/structures/energy_complex/phycobilisome.yaml
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e74d0c3e33df7e44348afbba1695b61c23262ab0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0030089 | data/structures/energy_complex/phycobilisome.yaml | maintained | phycobilisome |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0030089 | Fresh target check. Actual run: 2026-10-12T09:10:38Z to 2026-10-12T09:10:41Z. |
| strict | passed | True | GO:0030089 | Fresh target check. Actual run: 2026-10-12T09:10:41Z to 2026-10-12T09:10:47Z. |
| snippets | passed | True | GO:0030089 | Fresh target check. Zero of36 citations carries snippets; not full-text verification. Actual run: 2026-10-12T09:10:47Z to 2026-10-12T09:11:04Z. |
| reused-release-qc | passed | True | GO:0030089 | Verified unchanged-input reuse, not fresh execution. QC987passed/3skipped; labels603 no-adapter skips; cached trait index. Actual run: 2026-10-12T06:33:07Z to 2026-10-12T06:45:16Z. |
| reused-release-labels | passed | True | GO:0030089 | Verified unchanged-input reuse, not fresh execution. QC987passed/3skipped; labels603 no-adapter skips; cached trait index. Actual run: 2026-10-12T06:45:16Z to 2026-10-12T06:47:16Z. |
| reused-release-traits | passed | True | GO:0030089 | Verified unchanged-input reuse, not fresh execution. QC987passed/3skipped; labels603 no-adapter skips; cached trait index. Actual run: 2026-10-12T06:48:15Z to 2026-10-12T06:48:52Z. |
| reused-curies-live | passed | True | GO:0030089 | Log/input hash-verified reuse: live CURIE4023OK/251skips, archive203valid, contract4passed. Fresh post-save checks follow. Actual run: 2026-10-12T07:05:41Z to 2026-10-12T07:10:58Z. |
| reused-post-save-archive | passed | True | GO:0030089 | Log/input hash-verified reuse: live CURIE4023OK/251skips, archive203valid, contract4passed. Fresh post-save checks follow. Actual run: 2026-10-12T08:59:03Z to 2026-10-12T09:01:34Z. |
| reused-post-save-contract | passed | True | GO:0030089 | Log/input hash-verified reuse: live CURIE4023OK/251skips, archive203valid, contract4passed. Fresh post-save checks follow. Actual run: 2026-10-12T09:01:34Z to 2026-10-12T09:04:22Z. |
| adapter-datasets | passed | False | GO:0030089 | Fresh complete dataset inventory; exact target organism queries not applicable. Actual run: 2026-10-12T09:10:52Z to 2026-10-12T09:10:53Z. |
| Local author-hosted Sui PDF retrieval | failed | False | GO:0030089 | Executed local retrieval returned HTTP403 HTML and exited1; the unsuccessful response and actual UTC request times are retained in source-access.jsonl. It was not parsed as PDF or used as source text. |
| Sui review photoprotection attribution | unavailable | True | GO:0030089 | Manual claim-level verification incomplete: first review sections only were readable; later PDF requests timed out. The failed local PDF retrieval returned403 and exited1. This is not evidence that the subject is absent from the review. |
| Initial draft validation | failed | False | GO:0030089 | Draft used a string instead of the required target/reason object in scope.exclusions. Corrected without changing scientific findings. Actual run: 2026-10-12T09:21:00Z to 2026-10-12T09:21:03Z. |

## Scientific And Domain Assessments

### Generic structure, synonym and hierarchy

identity: supported. Targets: GO:0030089.

Active phycobilisome identity, PBS related synonym, light-harvesting-complex parent and thylakoid parthood are appropriate. The structure is not a single phycobiliprotein or photosystem. Preserve generic identity while resolving architecture scope.

### Core requirement and light-harvesting route

scope: concern. Targets: GO:0030089.

Conventional core-bearing composition is supported, but the native unqualified definition, essential allophycocyanin group and core-mediated function omit the coreless alternatives explicitly documented by two native citations. The GO definition is also conventional; do not silently pretend it already captures the literature distinction.

### Three reviewed-label-only protein classes and pigment group

grounding: supported. Targets: GO:0030089.

Grouped rod proteins, core proteins and heterogeneous linkers do not have one demonstrated universal exact family. Their deferred grounding is defensible. The mixed phycobilin group should not be forced to a single chemical ID; no universal subunit stoichiometry is asserted.

### All eleven identity-only examples

provenance: supported. Targets: GO:0030089.

All eleven reviewed gene/accession/taxon identities and current uniqueness queries agree. Membership caveats are explicit. P07123 and P73093 PMID/ECO localization notes match UniProt; do not replace the CpcG1 example with CpcG2 merely because the cited paper compares both.

### Two qualitative distributions

scope: supported. Targets: GO:0030089.

COMMON cyanobacterial and red-algal occurrence is supported within a qualitative, non-universal interpretation. No measured prevalence or experimentally established absence is asserted; an omitted optional lineage is not itself a defect.

### Three organism examples and DOI provenance

evidence: concern. Targets: GO:0030089.

T.vulcanus core/rod and PCC7120 PBS-PSII examples agree with their inspected sources and current taxonomy. PCC6803 occurs biologically, but its state-resolved cryo-EM example and several related notes conflate two different papers.

### Photoprotection claim versus nearest cited review

evidence: unknown. Targets: GO:0030089.

The bounded cyanobacterial OCP/quenching function is independently supported by the inspected2022 primary abstract. Whether Sui2021 actually discusses this subject, as the native evidence note claims, was not established from the accessible portions. No third finding is inferred from access failure.

### All seven rod/core graph edges

graph: concern. Targets: GO:0030089.

Pigment binding, rod assembly, core formation, linker organization and excitation transfer are supported for conventional core-bearing PBS at the stated coarse level. Scope must not imply a mandatory allophycocyanin path in coreless forms, and source notes need correction. Structural transfer predictions are not direct recordings of excitation trajectories.

### Optional fields and grounding discussion

completeness: supported. Targets: GO:0030089.

The family-grounding TODO is relevant to the grouped components. No required quantity, image, trait or expression dataset gap was established. Lack of exact adapter coverage is not a negative phenotype or composition result.

### Deterministic gates and stable identifiers

schema: supported. Targets: GO:0030089.

All native stable IDs and citation identities resolve in source-native metadata. Target gates pass; broader gates are verified reuse, not fresh execution. Citation resolution alone does not establish support for the attached taxon/state claim.

### History and read-only boundary

ownership: supported. Targets: GO:0030089.

Entire target and retained append-only CREATE event read. All native data, histories and prior bundle bytes remain unchanged. Future corrections belong to guarded maintained-YAML curation; this review neither promotes PROPOSED nor resolves any prior finding.

## Findings

### F1: Separate the PCC6803 state-resolved structure from the Zheng2021 paper

major / open / confirmed; issue key: phycobilisome-pcc6803-state-source-conflation.

The native PCC6803 light-harvesting/photoprotected example cites DOI10.1038/s41467-021-25813-y, and multiple core-related notes call it Sauer2021. The inspected paper is Zheng2021 and its new structures concern PCC7002/PCC7120. The stated state-resolved PCC6803 experiment is reported by Dominguez-Martin, Sauer and colleagues2022 under DOI10.1038/s41586-022-05156-4. Correct claim-level attribution without denying the2021 secondary PCC6803 array comparison.

### F2: Qualify the core requirement and core-mediated transfer route

major / open / confirmed; issue key: phycobilisome-coreless-architecture-scope.

The generic record requires an allophycocyanin core and describes light harvesting through it without a conventional-architecture boundary. Two native primary references document functional coreless PBS alternatives in the named cyanobacterial models. Qualify the definition, constituent requirement, function and graph to distinguish conventional core-bearing complexes from those alternatives. Retain the GO identity and explicitly acknowledge its core-centric definition; do not infer that conventional complexes lack a core or replace CpcG1 with CpcG2.

## Recommended Actions And Acceptance Checks

### A1

Correct the PCC6803 claim-level source and author/year notes. Retain the2021 citation only where its actual specimens, architecture or bounded array comparison support the attached claim; do not blindly replace every occurrence.

- Each organism/state claim matches an inspected primary source.
- Bibliographic attribution agrees across example, component and graph evidence notes.
- Record remains PROPOSED; guarded edit/history, target gates and lineage-linked successor disposition are required.

### A2

Introduce a supported conventional/coreless architecture distinction in the maintained record and constrain the existing core-transfer graph to the architecture it represents.

- No universal allophycocyanin-core requirement is implied for documented coreless alternatives.
- The conventional core/rod model remains supported and the GO definition limitation stays explicit.
- CpcG1 and CpcG2 gene/accession identities are not conflated.
- Validate guarded native changes and save a successor retaining this stable issue key.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/structures/energy_complex/phycobilisome.yaml; Entire native YAML and one append-only history event | supports | Generic phycobilisome identity; four constituent groups, eleven explicitly identity-only protein examples, three organism examples, two functions and seven graph edges. Core architecture and an essential allophycocyanin constituent are unqualified. Several notes misattribute the 2021 DOI to Sauer and to a newly resolved Synechocystis structure. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030089,GO:0030076,GO:0042651; All three active terms, complete definitions and parent relations | supports | The generic structure ID, light-harvesting-complex parent and thylakoid-membrane part_of agree. The GO definition itself describes the conventional core-to-PSII route; this limitation must be distinguished from primary reports of alternative coreless phycobilisomes. |
| zheng | https://doi.org/10.1038/s41467-021-25813-y; Complete abstract/authors; selected overall/core structure, bilin environment and strain-method sections; Fig.4 array-model paragraph | partial | Zheng et al.2021 solved PCC7002 and PCC7120 preparations and explicitly observed no OCP. PCC6803 appears in a secondary array-model comparison, not as a newly resolved photoprotected specimen. Conventional core architecture and terminal emitters are supported. |
| dominguez | https://doi.org/10.1038/s41586-022-05156-4; Complete PMID36045294 primary abstract and authors/DOI metadata, not full article | supports | Dominguez-Martin, Sauer and colleagues2022 report Synechocystis PCC6803 PBS structures with and without OCP. This supports the native state-specific example under a different citation and independently supports the bounded photoprotection function. |
| kawakami | https://doi.org/10.1038/s41467-022-30962-9; Complete abstract; subunit composition, core purification/refinement, PC-rod structure/transfer and PBS preparation sections | supports | The T.vulcanus NIES2134 study resolves isolated core and rod structures, with covalent bilins and internal linkers. It retains uncertain isoform assignments and predicts transfer routes from structure. No whole moving energy trajectory was directly observed. |
| chang | https://doi.org/10.1038/cr.2015.59; Complete primary abstract, authors and bibliographic metadata; no full-body inference | supports | Chang et al.2015 report intact PBS and PBS-PSII assemblies from Anabaena PCC7120 using single-particle EM and biochemical/molecular analyses. This supports the bounded native example and association edge. |
| watanabe | https://pubmed.ncbi.nlm.nih.gov/24550276/; Complete PubMed abstract; PMC abstract, Significance and Introduction also inspected before later access challenge | refutes | Watanabe et al.2014 isolated a PCC7120 CpcL-PBS/PSI supercomplex. The antenna contains phycocyanin and CpcL without allophycocyanin or conventional CpcG linkers; fluorescence excitation supports functional transfer to PSI. EM-based docking remains a model. |
| kondo | https://pubmed.ncbi.nlm.nih.gov/17468217/; Complete PubMed abstract, title and authors; full body inaccessible | refutes | Kondo et al.2007 compare conventional CpcG1-PBS with coreless CpcG2-PBS in PCC6803, using fluorescence, mutants and membrane association. The native P73093 example is CpcG1; the paper comparison does not make that accession CpcG2. |
| sui | https://doi.org/10.1146/annurev-biophys-062920-063657; Complete secondary-review abstract and author PDF pages0-2/initial composition text only | partial | Sui2021 summarizes red-algal PBS, phycobiliproteins, linkers and energy transfer; initial text also recognizes uncommon rod-shaped forms. Later review sections were not read. The native attribution of cyanobacterial quenching to this review remains unverified, not disproved. |
| eco | http://purl.obolibrary.org/obo/ECO_0000269; Current label and definition | supports | ECO0000269 denotes experimental evidence used in manual assertion. The two native PMID notes explicitly describe UniProt localization annotations, not independent reanalysis of every localization experiment. |
| adapter | https://imodulondb.org/; Fresh complete28-dataset inventory | supports | No exact native Synechocystis, Nostoc PCC7120 or T.vulcanus dataset is listed. Synechococcus elongatus is not a substitute. No applicable gene query or biological absence inference. |
| validation | /private/tmp/csm-review-20261012T091010Z-pbs/baseline-verification.json; Fresh target checks and checksum-verified unchanged-input broader results | supports | Schema and strict checks pass; zero of36 citations carries a snippet. Reused QC987passed/3skipped, cached labels/trait checks, live CURIE4023OK/251skips and203-bundle archive/four contract tests retain their original limitations. Fresh post-save checks follow. |
| access | /private/tmp/csm-review-20261012T091010Z-pbs/source-access.jsonl; All46 local HTTP receipts, including unsuccessful requests; browser reading limits separately stated | supports | Forty-two HTTP200 responses, three HTTP500 XML responses and one HTTP403 HTML response at a PDF URL were retained with timestamps and hashes. Failed responses were not parsed as articles. The local Sui fetch exited1; browser initially exposed only the first PDF sections and subsequent opens/finds failed. |
| predecessors | reviews/structured/; Ignored-inclusive canonical scan and rg -uu over review/report/history/research/curation roots | supports | No exact target predecessor among203 canonical bundles and no existing occurrence of either new issue key. The broad light-harvesting record has a related source-conflation finding, but it is a different target and is not a predecessor or disposition here. |
| tax-1117 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1117; Complete taxonomy record including current name and equivalents | supports | Native taxon label and identifier agree; historical publication names are retained as synonyms where applicable. |
| tax-2763 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2763; Complete taxonomy record including current name and equivalents | supports | Native taxon label and identifier agree; historical publication names are retained as synonyms where applicable. |
| tax-1148 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1148; Complete taxonomy record including current name and equivalents | supports | Native taxon label and identifier agree; historical publication names are retained as synonyms where applicable. |
| tax-32053 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/32053; Complete taxonomy record including current name and equivalents | supports | Native taxon label and identifier agree; historical publication names are retained as synonyms where applicable. |
| tax-103690 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/103690; Complete taxonomy record including current name and equivalents | supports | Native taxon label and identifier agree; historical publication names are retained as synonyms where applicable. |
| tax-1111708 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1111708; Complete taxonomy record including current name and equivalents | supports | Native taxon label and identifier agree; historical publication names are retained as synonyms where applicable. |
| protein-Q54715 | https://rest.uniprot.org/uniprotkb/Q54715.json; Entry identity plus exact reviewed gene/taxon search; reference and localization annotations for P07123/P73093 | supports | Reviewed accession, gene, taxon and protein label agree. Fresh exact reviewed gene/taxon search returned only this accession. This verifies current identity, not historical query reconstruction or independent membership proof. |
| protein-Q54714 | https://rest.uniprot.org/uniprotkb/Q54714.json; Entry identity plus exact reviewed gene/taxon search; reference and localization annotations for P07123/P73093 | supports | Reviewed accession, gene, taxon and protein label agree. Fresh exact reviewed gene/taxon search returned only this accession. This verifies current identity, not historical query reconstruction or independent membership proof. |
| protein-Q01951 | https://rest.uniprot.org/uniprotkb/Q01951.json; Entry identity plus exact reviewed gene/taxon search; reference and localization annotations for P07123/P73093 | supports | Reviewed accession, gene, taxon and protein label agree. Fresh exact reviewed gene/taxon search returned only this accession. This verifies current identity, not historical query reconstruction or independent membership proof. |
| protein-Q01952 | https://rest.uniprot.org/uniprotkb/Q01952.json; Entry identity plus exact reviewed gene/taxon search; reference and localization annotations for P07123/P73093 | supports | Reviewed accession, gene, taxon and protein label agree. Fresh exact reviewed gene/taxon search returned only this accession. This verifies current identity, not historical query reconstruction or independent membership proof. |
| protein-P72870 | https://rest.uniprot.org/uniprotkb/P72870.json; Entry identity plus exact reviewed gene/taxon search; reference and localization annotations for P07123/P73093 | supports | Reviewed accession, gene, taxon and protein label agree. Fresh exact reviewed gene/taxon search returned only this accession. This verifies current identity, not historical query reconstruction or independent membership proof. |
| protein-P74551 | https://rest.uniprot.org/uniprotkb/P74551.json; Entry identity plus exact reviewed gene/taxon search; reference and localization annotations for P07123/P73093 | supports | Reviewed accession, gene, taxon and protein label agree. Fresh exact reviewed gene/taxon search returned only this accession. This verifies current identity, not historical query reconstruction or independent membership proof. |
| protein-P07123 | https://rest.uniprot.org/uniprotkb/P07123.json; Entry identity plus exact reviewed gene/taxon search; reference and localization annotations for P07123/P73093 | supports | Reviewed accession, gene, taxon and protein label agree. Fresh exact reviewed gene/taxon search returned only this accession. This verifies current identity, not historical query reconstruction or independent membership proof. The native PMID and ECO0000269 thylakoid annotation are present in the entry references and localization evidence. |
| protein-P73202 | https://rest.uniprot.org/uniprotkb/P73202.json; Entry identity plus exact reviewed gene/taxon search; reference and localization annotations for P07123/P73093 | supports | Reviewed accession, gene, taxon and protein label agree. Fresh exact reviewed gene/taxon search returned only this accession. This verifies current identity, not historical query reconstruction or independent membership proof. |
| protein-P73093 | https://rest.uniprot.org/uniprotkb/P73093.json; Entry identity plus exact reviewed gene/taxon search; reference and localization annotations for P07123/P73093 | supports | Reviewed accession, gene, taxon and protein label agree. Fresh exact reviewed gene/taxon search returned only this accession. This verifies current identity, not historical query reconstruction or independent membership proof. The native PMID and ECO0000269 thylakoid annotation are present in the entry references and localization evidence. |
| protein-Q01950 | https://rest.uniprot.org/uniprotkb/Q01950.json; Entry identity plus exact reviewed gene/taxon search; reference and localization annotations for P07123/P73093 | supports | Reviewed accession, gene, taxon and protein label agree. Fresh exact reviewed gene/taxon search returned only this accession. This verifies current identity, not historical query reconstruction or independent membership proof. |
| protein-Q55544 | https://rest.uniprot.org/uniprotkb/Q55544.json; Entry identity plus exact reviewed gene/taxon search; reference and localization annotations for P07123/P73093 | supports | Reviewed accession, gene, taxon and protein label agree. Fresh exact reviewed gene/taxon search returned only this accession. This verifies current identity, not historical query reconstruction or independent membership proof. |

## Limits And Additional Notes

- Partial scientific review: entire target read and all rubric areas considered, but the Sui2021 photoprotection attribution is unassessed. Independent support for the biological function does not verify that specific citation note. This access limitation is not a third finding.
- Same-agent review, not independent human sign-off, exhaustive literature/retraction search or new experimental analysis.
- Zheng and Kawakami selected main-text sections were inspected as identified in Evidence, not all figures, supplementary files or raw maps. Candidate energy-transfer pathways and uncertain linker assignments remain interpretations.
- Chang and Dominguez-Martin assessed from complete primary abstracts and bibliographic identities, not full articles. Watanabe abstract/Significance/Introduction and Kondo complete abstract support the bounded coreless examples; no unread Methods or Results are represented as inspected.
- Forty-six local captures include42 HTTP200, three HTTP500 XML failures and one HTTP403 HTML response at the Sui PDF URL. The Sui local-fetch process exited1. Browser access initially exposed PDF pages0-2 only; subsequent opens/finds timed out or failed. PMC challenges were not bypassed. Search snippets are not evidence.
- All eleven exact UniProt searches verify present reviewed identity/uniqueness only, not reconstruction of the2026-09-08 retrieval. The two cited ECO annotations were inspected as UniProt assertions; no automatic conversion into universal structure membership.
- Fresh target checks are distinguished from checksum-verified broader-check reuse with original cache/no-adapter/test skips. No exact iModulonDB dataset applies. No target trait links exist; cached wider trait-source limitations remain.
- No native scientific edits, product regeneration, history/status changes, GitHub issue/PR creation, CI, push or merge. External-publication approval remains unanswered and is not bypassed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T092129Z-phycobilisome-source-architecture
kind: record
repository: CultureBotAI/CellStructureMech
title: Phycobilisome source attribution and architecture-scope review
started_at: '2026-10-12T09:10:35Z'
finished_at: '2026-10-12T09:21:29Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Same coding-agent context; no independent reviewer or human
    sign-off.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'Two confirmed major findings: conflated state-specific structural citations
  and an unqualified core requirement despite documented coreless alternatives. Native
  identity, hierarchy and eleven protein identities are supported. Review remains
  partial because the Sui2021 photoprotection attribution could not be verified.'
source:
  git_revision: e74d0c3e33df7e44348afbba1695b61c23262ab0
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
  - path: data/structures/energy_complex/phycobilisome.yaml
    sha256: 26e458fabb972c35a3ddfdf903ef287ce4c33e1687cf5cba12a98ba9f2ccd504
    role: target
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
  - path: history/records/phycobilisome/2026-09-04T183819Z-claude-1865d0.yaml
    sha256: a1cd8c47ca3b1c09111bba40937b4d3408c766629c64b35a2d3096b14238c6a3
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
targets:
- target_id: GO:0030089
  path: data/structures/energy_complex/phycobilisome.yaml
  label: phycobilisome
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/phycobilisome.yaml
    role: maintained scientific record
scope:
  description: One entire native record read; all component/example/graph fields assessed
    within stated source limits. One claim-level citation attribution remains unassessed;
    no sampling.
  selection: data/structures/energy_complex/phycobilisome.yaml
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - GO:0030089
  exclusions:
  - target: functions[photoprotection].evidence[DOI:10.1146/annurev-biophys-062920-063657].notes
    reason: Later Sui2021 sections needed to verify this attribution remained inaccessible;
      the biological function has independent primary support.
checks:
- check_id: schema
  name: schema
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/energy_complex/phycobilisome.yaml
  exit_code: 0
  status: passed
  required: true
  summary: 'Fresh target check. Actual run: 2026-10-12T09:10:38Z to 2026-10-12T09:10:41Z.'
  target_ids:
  - GO:0030089
  evidence_ids:
  - validation
- check_id: strict
  name: strict
  command: .venv/bin/python scripts/validate_strict.py data/structures/energy_complex/phycobilisome.yaml
  exit_code: 0
  status: passed
  required: true
  summary: 'Fresh target check. Actual run: 2026-10-12T09:10:41Z to 2026-10-12T09:10:47Z.'
  target_ids:
  - GO:0030089
  evidence_ids:
  - validation
- check_id: snippets
  name: snippets
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/energy_complex/phycobilisome.yaml
    --report /private/tmp/csm-review-20261012T091010Z-pbs/snippets.md
  exit_code: 0
  status: passed
  required: true
  summary: 'Fresh target check. Zero of36 citations carries snippets; not full-text
    verification. Actual run: 2026-10-12T09:10:47Z to 2026-10-12T09:11:04Z.'
  target_ids:
  - GO:0030089
  evidence_ids:
  - validation
- check_id: reused-release-qc
  name: reused-release-qc
  command: .venv/bin/python scripts/run_qc.py
  exit_code: 0
  status: passed
  required: true
  summary: 'Verified unchanged-input reuse, not fresh execution. QC987passed/3skipped;
    labels603 no-adapter skips; cached trait index. Actual run: 2026-10-12T06:33:07Z
    to 2026-10-12T06:45:16Z.'
  target_ids:
  - GO:0030089
  evidence_ids:
  - validation
- check_id: reused-release-labels
  name: reused-release-labels
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  status: passed
  required: true
  summary: 'Verified unchanged-input reuse, not fresh execution. QC987passed/3skipped;
    labels603 no-adapter skips; cached trait index. Actual run: 2026-10-12T06:45:16Z
    to 2026-10-12T06:47:16Z.'
  target_ids:
  - GO:0030089
  evidence_ids:
  - validation
- check_id: reused-release-traits
  name: reused-release-traits
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  status: passed
  required: true
  summary: 'Verified unchanged-input reuse, not fresh execution. QC987passed/3skipped;
    labels603 no-adapter skips; cached trait index. Actual run: 2026-10-12T06:48:15Z
    to 2026-10-12T06:48:52Z.'
  target_ids:
  - GO:0030089
  evidence_ids:
  - validation
- check_id: reused-curies-live
  name: reused-curies-live
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  status: passed
  required: true
  summary: 'Log/input hash-verified reuse: live CURIE4023OK/251skips, archive203valid,
    contract4passed. Fresh post-save checks follow. Actual run: 2026-10-12T07:05:41Z
    to 2026-10-12T07:10:58Z.'
  target_ids:
  - GO:0030089
  evidence_ids:
  - validation
- check_id: reused-post-save-archive
  name: reused-post-save-archive
  command: .venv/bin/python scripts/record_review.py check
  exit_code: 0
  status: passed
  required: true
  summary: 'Log/input hash-verified reuse: live CURIE4023OK/251skips, archive203valid,
    contract4passed. Fresh post-save checks follow. Actual run: 2026-10-12T08:59:03Z
    to 2026-10-12T09:01:34Z.'
  target_ids:
  - GO:0030089
  evidence_ids:
  - validation
- check_id: reused-post-save-contract
  name: reused-post-save-contract
  command: .venv/bin/python -m pytest -q tests/test_record_review_contract.py
  exit_code: 0
  status: passed
  required: true
  summary: 'Log/input hash-verified reuse: live CURIE4023OK/251skips, archive203valid,
    contract4passed. Fresh post-save checks follow. Actual run: 2026-10-12T09:01:34Z
    to 2026-10-12T09:04:22Z.'
  target_ids:
  - GO:0030089
  evidence_ids:
  - validation
- check_id: adapter-datasets
  name: adapter-datasets
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  exit_code: 0
  status: passed
  required: false
  summary: 'Fresh complete dataset inventory; exact target organism queries not applicable.
    Actual run: 2026-10-12T09:10:52Z to 2026-10-12T09:10:53Z.'
  target_ids:
  - GO:0030089
  evidence_ids:
  - adapter
- check_id: sui-local-pdf-fetch
  name: Local author-hosted Sui PDF retrieval
  status: failed
  exit_code: 1
  required: false
  summary: Executed local retrieval returned HTTP403 HTML and exited1; the unsuccessful
    response and actual UTC request times are retained in source-access.jsonl. It
    was not parsed as PDF or used as source text.
  target_ids:
  - GO:0030089
  evidence_ids:
  - access
- check_id: photoprotection-citation-support
  name: Sui review photoprotection attribution
  status: unavailable
  required: true
  summary: 'Manual claim-level verification incomplete: first review sections only
    were readable; later PDF requests timed out. The failed local PDF retrieval returned403
    and exited1. This is not evidence that the subject is absent from the review.'
  target_ids:
  - GO:0030089
  evidence_ids:
  - sui
  - access
- check_id: draft-contract-corrected
  name: Initial draft validation
  command: .venv/bin/python scripts/record_review.py validate /private/tmp/csm-review-20261012T091010Z-pbs/observation.yaml
  exit_code: 1
  status: failed
  required: false
  summary: 'Draft used a string instead of the required target/reason object in scope.exclusions.
    Corrected without changing scientific findings. Actual run: 2026-10-12T09:21:00Z
    to 2026-10-12T09:21:03Z.'
  target_ids:
  - GO:0030089
  evidence_ids:
  - validation
evidence:
- evidence_id: native
  kind: record_content
  reference: data/structures/energy_complex/phycobilisome.yaml
  locator: Entire native YAML and one append-only history event
  summary: Generic phycobilisome identity; four constituent groups, eleven explicitly
    identity-only protein examples, three organism examples, two functions and seven
    graph edges. Core architecture and an essential allophycocyanin constituent are
    unqualified. Several notes misattribute the 2021 DOI to Sauer and to a newly resolved
    Synechocystis structure.
  support: supports
  accessed_at: '2026-10-12T09:21:00Z'
  snapshot_sha256: 26e458fabb972c35a3ddfdf903ef287ce4c33e1687cf5cba12a98ba9f2ccd504
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030089,GO:0030076,GO:0042651
  locator: All three active terms, complete definitions and parent relations
  summary: The generic structure ID, light-harvesting-complex parent and thylakoid-membrane
    part_of agree. The GO definition itself describes the conventional core-to-PSII
    route; this limitation must be distinguished from primary reports of alternative
    coreless phycobilisomes.
  support: supports
  accessed_at: '2026-10-12T09:10:39Z'
  snapshot_sha256: aef3df28cc07464072044ed5335d4cb10dfedbbeeef0b1cf8db13708b625e33c
- evidence_id: zheng
  kind: primary_source
  reference: https://doi.org/10.1038/s41467-021-25813-y
  locator: Complete abstract/authors; selected overall/core structure, bilin environment
    and strain-method sections; Fig.4 array-model paragraph
  summary: Zheng et al.2021 solved PCC7002 and PCC7120 preparations and explicitly
    observed no OCP. PCC6803 appears in a secondary array-model comparison, not as
    a newly resolved photoprotected specimen. Conventional core architecture and terminal
    emitters are supported.
  support: partial
  accessed_at: '2026-10-12T09:11:28Z'
  snapshot_sha256: 1726fe18d49fc2e19a9fe0846a7d6879eb72b486b58cf84cd033d33794251ef1
- evidence_id: dominguez
  kind: primary_source
  reference: https://doi.org/10.1038/s41586-022-05156-4
  locator: Complete PMID36045294 primary abstract and authors/DOI metadata, not full
    article
  summary: Dominguez-Martin, Sauer and colleagues2022 report Synechocystis PCC6803
    PBS structures with and without OCP. This supports the native state-specific example
    under a different citation and independently supports the bounded photoprotection
    function.
  support: supports
  accessed_at: '2026-10-12T09:12:47Z'
  snapshot_sha256: 696f29a263077163125a90176897afe0cc5b3e95b636b07eec7516b472272b31
- evidence_id: kawakami
  kind: primary_source
  reference: https://doi.org/10.1038/s41467-022-30962-9
  locator: Complete abstract; subunit composition, core purification/refinement, PC-rod
    structure/transfer and PBS preparation sections
  summary: The T.vulcanus NIES2134 study resolves isolated core and rod structures,
    with covalent bilins and internal linkers. It retains uncertain isoform assignments
    and predicts transfer routes from structure. No whole moving energy trajectory
    was directly observed.
  support: supports
  accessed_at: '2026-10-12T09:11:29Z'
  snapshot_sha256: d428f0c1cc2ccea5b0e4e343d5841355b892f65e6cb694481ee1ff13c9087713
- evidence_id: chang
  kind: primary_source
  reference: https://doi.org/10.1038/cr.2015.59
  locator: Complete primary abstract, authors and bibliographic metadata; no full-body
    inference
  summary: Chang et al.2015 report intact PBS and PBS-PSII assemblies from Anabaena
    PCC7120 using single-particle EM and biochemical/molecular analyses. This supports
    the bounded native example and association edge.
  support: supports
  accessed_at: '2026-10-12T09:10:55Z'
  snapshot_sha256: fabc7b865b1d6a098a899cd7f0096736a4d629b96ff03226d7947b7d3a4eb60e
- evidence_id: watanabe
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/24550276/
  locator: Complete PubMed abstract; PMC abstract, Significance and Introduction also
    inspected before later access challenge
  summary: Watanabe et al.2014 isolated a PCC7120 CpcL-PBS/PSI supercomplex. The antenna
    contains phycocyanin and CpcL without allophycocyanin or conventional CpcG linkers;
    fluorescence excitation supports functional transfer to PSI. EM-based docking
    remains a model.
  support: refutes
  accessed_at: '2026-10-12T09:10:39Z'
  snapshot_sha256: d4195d13ae13030eb8c291e8bf59e0b20517093b898f83aa79acfd283ad587f9
- evidence_id: kondo
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/17468217/
  locator: Complete PubMed abstract, title and authors; full body inaccessible
  summary: Kondo et al.2007 compare conventional CpcG1-PBS with coreless CpcG2-PBS
    in PCC6803, using fluorescence, mutants and membrane association. The native P73093
    example is CpcG1; the paper comparison does not make that accession CpcG2.
  support: refutes
  accessed_at: '2026-10-12T09:10:39Z'
  snapshot_sha256: d4195d13ae13030eb8c291e8bf59e0b20517093b898f83aa79acfd283ad587f9
- evidence_id: sui
  kind: authority
  reference: https://doi.org/10.1146/annurev-biophys-062920-063657
  locator: Complete secondary-review abstract and author PDF pages0-2/initial composition
    text only
  summary: Sui2021 summarizes red-algal PBS, phycobiliproteins, linkers and energy
    transfer; initial text also recognizes uncommon rod-shaped forms. Later review
    sections were not read. The native attribution of cyanobacterial quenching to
    this review remains unverified, not disproved.
  support: partial
  accessed_at: '2026-10-12T09:10:52Z'
  snapshot_sha256: fdddeb666d015fb4772777d39ef582864bbeb10d98e56a298c7ce08d1141b00b
- evidence_id: eco
  kind: authority
  reference: http://purl.obolibrary.org/obo/ECO_0000269
  locator: Current label and definition
  summary: ECO0000269 denotes experimental evidence used in manual assertion. The
    two native PMID notes explicitly describe UniProt localization annotations, not
    independent reanalysis of every localization experiment.
  support: supports
  accessed_at: '2026-10-12T09:12:46Z'
  snapshot_sha256: 93e3084215699f536b15652e236a64f0ff6e1a8d3dd283e744bef108924ccd12
- evidence_id: adapter
  kind: database
  reference: https://imodulondb.org/
  locator: Fresh complete28-dataset inventory
  summary: No exact native Synechocystis, Nostoc PCC7120 or T.vulcanus dataset is
    listed. Synechococcus elongatus is not a substitute. No applicable gene query
    or biological absence inference.
  support: supports
  accessed_at: '2026-10-12T09:21:00Z'
- evidence_id: validation
  kind: validation
  reference: /private/tmp/csm-review-20261012T091010Z-pbs/baseline-verification.json
  locator: Fresh target checks and checksum-verified unchanged-input broader results
  summary: Schema and strict checks pass; zero of36 citations carries a snippet. Reused
    QC987passed/3skipped, cached labels/trait checks, live CURIE4023OK/251skips and203-bundle
    archive/four contract tests retain their original limitations. Fresh post-save
    checks follow.
  support: supports
  accessed_at: '2026-10-12T09:21:00Z'
- evidence_id: access
  kind: validation
  reference: /private/tmp/csm-review-20261012T091010Z-pbs/source-access.jsonl
  locator: All46 local HTTP receipts, including unsuccessful requests; browser reading
    limits separately stated
  summary: Forty-two HTTP200 responses, three HTTP500 XML responses and one HTTP403
    HTML response at a PDF URL were retained with timestamps and hashes. Failed responses
    were not parsed as articles. The local Sui fetch exited1; browser initially exposed
    only the first PDF sections and subsequent opens/finds failed.
  support: supports
  accessed_at: '2026-10-12T09:21:00Z'
- evidence_id: predecessors
  kind: search
  reference: reviews/structured/
  locator: Ignored-inclusive canonical scan and rg -uu over review/report/history/research/curation
    roots
  summary: No exact target predecessor among203 canonical bundles and no existing
    occurrence of either new issue key. The broad light-harvesting record has a related
    source-conflation finding, but it is a different target and is not a predecessor
    or disposition here.
  support: supports
  accessed_at: '2026-10-12T09:21:00Z'
  search_scope: Path.rglob included hidden/ignored bundles; rg -uu included ignored
    files and searched target slug, label, GO ID, source DOI and both new issue keys
    in reviews, reports/yaml_record_review, history, research and curation. No remote
    issue-absence claim.
- evidence_id: tax-1117
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1117
  locator: Complete taxonomy record including current name and equivalents
  summary: Native taxon label and identifier agree; historical publication names are
    retained as synonyms where applicable.
  support: supports
  accessed_at: '2026-10-12T09:10:40Z'
  snapshot_sha256: 5f4919ad6f362a82291b587d27134147f277ffc5fa593f6076f1983a704cd985
- evidence_id: tax-2763
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2763
  locator: Complete taxonomy record including current name and equivalents
  summary: Native taxon label and identifier agree; historical publication names are
    retained as synonyms where applicable.
  support: supports
  accessed_at: '2026-10-12T09:10:40Z'
  snapshot_sha256: 73c5fb9f4e663ee9f81162bbef7158f567879f7e39c91ee4823564289385434b
- evidence_id: tax-1148
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1148
  locator: Complete taxonomy record including current name and equivalents
  summary: Native taxon label and identifier agree; historical publication names are
    retained as synonyms where applicable.
  support: supports
  accessed_at: '2026-10-12T09:10:41Z'
  snapshot_sha256: 84c0a354189f6b736c57eb3886dc08090cd6edba80c6e35c1b92909c26f35ab4
- evidence_id: tax-32053
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/32053
  locator: Complete taxonomy record including current name and equivalents
  summary: Native taxon label and identifier agree; historical publication names are
    retained as synonyms where applicable.
  support: supports
  accessed_at: '2026-10-12T09:10:42Z'
  snapshot_sha256: 22e01d3cfa17a447e15eeb62ce0bc9e9f698799dc9e5e2586e3408b075a1829e
- evidence_id: tax-103690
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/103690
  locator: Complete taxonomy record including current name and equivalents
  summary: Native taxon label and identifier agree; historical publication names are
    retained as synonyms where applicable.
  support: supports
  accessed_at: '2026-10-12T09:10:42Z'
  snapshot_sha256: 7fc96669520f8a094b5b0b4a5d68f95194ff1e0468875dc63a80f0361da2ef19
- evidence_id: tax-1111708
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1111708
  locator: Complete taxonomy record including current name and equivalents
  summary: Native taxon label and identifier agree; historical publication names are
    retained as synonyms where applicable.
  support: supports
  accessed_at: '2026-10-12T09:10:43Z'
  snapshot_sha256: a059d5c8b13212e336d88e33ebf02c638ad3840710b5228abfff6fa8d5c065a0
- evidence_id: protein-Q54715
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q54715.json
  locator: Entry identity plus exact reviewed gene/taxon search; reference and localization
    annotations for P07123/P73093
  summary: Reviewed accession, gene, taxon and protein label agree. Fresh exact reviewed
    gene/taxon search returned only this accession. This verifies current identity,
    not historical query reconstruction or independent membership proof.
  support: supports
  accessed_at: '2026-10-12T09:10:44Z'
  snapshot_sha256: 60aa54ea320d5d42410b6899250ab676b177ccdaad73f88168b79491affcbf3f
- evidence_id: protein-Q54714
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q54714.json
  locator: Entry identity plus exact reviewed gene/taxon search; reference and localization
    annotations for P07123/P73093
  summary: Reviewed accession, gene, taxon and protein label agree. Fresh exact reviewed
    gene/taxon search returned only this accession. This verifies current identity,
    not historical query reconstruction or independent membership proof.
  support: supports
  accessed_at: '2026-10-12T09:10:45Z'
  snapshot_sha256: 2d20e895e2a54210bd225c535fe24572cbe05a204657fa12344d0f2f113b3896
- evidence_id: protein-Q01951
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q01951.json
  locator: Entry identity plus exact reviewed gene/taxon search; reference and localization
    annotations for P07123/P73093
  summary: Reviewed accession, gene, taxon and protein label agree. Fresh exact reviewed
    gene/taxon search returned only this accession. This verifies current identity,
    not historical query reconstruction or independent membership proof.
  support: supports
  accessed_at: '2026-10-12T09:10:45Z'
  snapshot_sha256: e1fea67561c176d463155426734a2153aeae798557a565929976f20c66b912e8
- evidence_id: protein-Q01952
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q01952.json
  locator: Entry identity plus exact reviewed gene/taxon search; reference and localization
    annotations for P07123/P73093
  summary: Reviewed accession, gene, taxon and protein label agree. Fresh exact reviewed
    gene/taxon search returned only this accession. This verifies current identity,
    not historical query reconstruction or independent membership proof.
  support: supports
  accessed_at: '2026-10-12T09:10:46Z'
  snapshot_sha256: 679ac80a381bc7a6a4a0be13e299055450fa6f6032f11e554f532adcf7bc6fb9
- evidence_id: protein-P72870
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P72870.json
  locator: Entry identity plus exact reviewed gene/taxon search; reference and localization
    annotations for P07123/P73093
  summary: Reviewed accession, gene, taxon and protein label agree. Fresh exact reviewed
    gene/taxon search returned only this accession. This verifies current identity,
    not historical query reconstruction or independent membership proof.
  support: supports
  accessed_at: '2026-10-12T09:10:47Z'
  snapshot_sha256: fa4c446c646513fb5c3859d356c11736939b1a18e1386f636efb08097535a0b7
- evidence_id: protein-P74551
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P74551.json
  locator: Entry identity plus exact reviewed gene/taxon search; reference and localization
    annotations for P07123/P73093
  summary: Reviewed accession, gene, taxon and protein label agree. Fresh exact reviewed
    gene/taxon search returned only this accession. This verifies current identity,
    not historical query reconstruction or independent membership proof.
  support: supports
  accessed_at: '2026-10-12T09:10:47Z'
  snapshot_sha256: 07ed2493a009e0620d9d8bc83a32fa61d9042ec077fc5997ac67260b687a5705
- evidence_id: protein-P07123
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P07123.json
  locator: Entry identity plus exact reviewed gene/taxon search; reference and localization
    annotations for P07123/P73093
  summary: Reviewed accession, gene, taxon and protein label agree. Fresh exact reviewed
    gene/taxon search returned only this accession. This verifies current identity,
    not historical query reconstruction or independent membership proof. The native
    PMID and ECO0000269 thylakoid annotation are present in the entry references and
    localization evidence.
  support: supports
  accessed_at: '2026-10-12T09:10:48Z'
  snapshot_sha256: a9bdb3da53ed546247b490e702223047b173bc9d84596d6195e00e8a493908f7
- evidence_id: protein-P73202
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P73202.json
  locator: Entry identity plus exact reviewed gene/taxon search; reference and localization
    annotations for P07123/P73093
  summary: Reviewed accession, gene, taxon and protein label agree. Fresh exact reviewed
    gene/taxon search returned only this accession. This verifies current identity,
    not historical query reconstruction or independent membership proof.
  support: supports
  accessed_at: '2026-10-12T09:10:49Z'
  snapshot_sha256: de55ea67c626896fa93a034fe7b51cfd23674bf4f7c8565f50ea692fd7530c7a
- evidence_id: protein-P73093
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P73093.json
  locator: Entry identity plus exact reviewed gene/taxon search; reference and localization
    annotations for P07123/P73093
  summary: Reviewed accession, gene, taxon and protein label agree. Fresh exact reviewed
    gene/taxon search returned only this accession. This verifies current identity,
    not historical query reconstruction or independent membership proof. The native
    PMID and ECO0000269 thylakoid annotation are present in the entry references and
    localization evidence.
  support: supports
  accessed_at: '2026-10-12T09:10:50Z'
  snapshot_sha256: e7f8648eaa9ebdad0f10f57e20d1f0ec5e96205b8d4af4f76dcf6b0fc2aaa87f
- evidence_id: protein-Q01950
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q01950.json
  locator: Entry identity plus exact reviewed gene/taxon search; reference and localization
    annotations for P07123/P73093
  summary: Reviewed accession, gene, taxon and protein label agree. Fresh exact reviewed
    gene/taxon search returned only this accession. This verifies current identity,
    not historical query reconstruction or independent membership proof.
  support: supports
  accessed_at: '2026-10-12T09:10:50Z'
  snapshot_sha256: 29415828e812e915b4770216678a1d5977a2db66da4d75abb8f3cb2c4e4e9ee4
- evidence_id: protein-Q55544
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q55544.json
  locator: Entry identity plus exact reviewed gene/taxon search; reference and localization
    annotations for P07123/P73093
  summary: Reviewed accession, gene, taxon and protein label agree. Fresh exact reviewed
    gene/taxon search returned only this accession. This verifies current identity,
    not historical query reconstruction or independent membership proof.
  support: supports
  accessed_at: '2026-10-12T09:10:51Z'
  snapshot_sha256: fc7a4be9ee0f9c48b450fe5b95b7e469bdeb114d99ef52f1e8b110fadfa1304d
assessments:
- assessment_id: identity
  area: identity
  topic: Generic structure, synonym and hierarchy
  outcome: supported
  summary: Active phycobilisome identity, PBS related synonym, light-harvesting-complex
    parent and thylakoid parthood are appropriate. The structure is not a single phycobiliprotein
    or photosystem. Preserve generic identity while resolving architecture scope.
  target_ids:
  - GO:0030089
  evidence_ids:
  - native
  - go
  - sui
- assessment_id: architecture
  area: scope
  topic: Core requirement and light-harvesting route
  outcome: concern
  summary: Conventional core-bearing composition is supported, but the native unqualified
    definition, essential allophycocyanin group and core-mediated function omit the
    coreless alternatives explicitly documented by two native citations. The GO definition
    is also conventional; do not silently pretend it already captures the literature
    distinction.
  target_ids:
  - GO:0030089
  evidence_ids:
  - native
  - go
  - kawakami
  - watanabe
  - kondo
  dimensions:
  - name: conventional_architecture
    value: Core-bearing PBS with rods and allophycocyanin
    definition: Supported architecture, but not silently universal across the literature
      class.
    evidence_ids:
    - kawakami
    - zheng
  - name: counterexample_scope
    value: PCC7120 CpcL-PBS and PCC6803 CpcG2-PBS
    definition: Primary experimentally functional coreless examples; not a claim that
      conventional CpcG1 complexes lack a core.
    evidence_ids:
    - watanabe
    - kondo
- assessment_id: grounding
  area: grounding
  topic: Three reviewed-label-only protein classes and pigment group
  outcome: supported
  summary: Grouped rod proteins, core proteins and heterogeneous linkers do not have
    one demonstrated universal exact family. Their deferred grounding is defensible.
    The mixed phycobilin group should not be forced to a single chemical ID; no universal
    subunit stoichiometry is asserted.
  target_ids:
  - GO:0030089
  evidence_ids:
  - native
  - sui
  - kawakami
- assessment_id: proteins
  area: provenance
  topic: All eleven identity-only examples
  outcome: supported
  summary: All eleven reviewed gene/accession/taxon identities and current uniqueness
    queries agree. Membership caveats are explicit. P07123 and P73093 PMID/ECO localization
    notes match UniProt; do not replace the CpcG1 example with CpcG2 merely because
    the cited paper compares both.
  target_ids:
  - GO:0030089
  evidence_ids:
  - native
  - eco
  - protein-Q54715
  - protein-Q54714
  - protein-Q01951
  - protein-Q01952
  - protein-P72870
  - protein-P74551
  - protein-P07123
  - protein-P73202
  - protein-P73093
  - protein-Q01950
  - protein-Q55544
- assessment_id: distribution
  area: scope
  topic: Two qualitative distributions
  outcome: supported
  summary: COMMON cyanobacterial and red-algal occurrence is supported within a qualitative,
    non-universal interpretation. No measured prevalence or experimentally established
    absence is asserted; an omitted optional lineage is not itself a defect.
  target_ids:
  - GO:0030089
  evidence_ids:
  - native
  - sui
  - tax-1117
  - tax-2763
- assessment_id: examples
  area: evidence
  topic: Three organism examples and DOI provenance
  outcome: concern
  summary: T.vulcanus core/rod and PCC7120 PBS-PSII examples agree with their inspected
    sources and current taxonomy. PCC6803 occurs biologically, but its state-resolved
    cryo-EM example and several related notes conflate two different papers.
  target_ids:
  - GO:0030089
  evidence_ids:
  - native
  - zheng
  - dominguez
  - kawakami
  - chang
  - tax-1148
  - tax-32053
  - tax-103690
- assessment_id: photoprotection
  area: evidence
  topic: Photoprotection claim versus nearest cited review
  outcome: unknown
  summary: The bounded cyanobacterial OCP/quenching function is independently supported
    by the inspected2022 primary abstract. Whether Sui2021 actually discusses this
    subject, as the native evidence note claims, was not established from the accessible
    portions. No third finding is inferred from access failure.
  target_ids:
  - GO:0030089
  evidence_ids:
  - native
  - dominguez
  - sui
  - access
- assessment_id: graph
  area: graph
  topic: All seven rod/core graph edges
  outcome: concern
  summary: Pigment binding, rod assembly, core formation, linker organization and
    excitation transfer are supported for conventional core-bearing PBS at the stated
    coarse level. Scope must not imply a mandatory allophycocyanin path in coreless
    forms, and source notes need correction. Structural transfer predictions are not
    direct recordings of excitation trajectories.
  target_ids:
  - GO:0030089
  evidence_ids:
  - native
  - sui
  - zheng
  - kawakami
  - chang
  - watanabe
  - kondo
- assessment_id: completeness
  area: completeness
  topic: Optional fields and grounding discussion
  outcome: supported
  summary: The family-grounding TODO is relevant to the grouped components. No required
    quantity, image, trait or expression dataset gap was established. Lack of exact
    adapter coverage is not a negative phenotype or composition result.
  target_ids:
  - GO:0030089
  evidence_ids:
  - native
  - adapter
  - kawakami
- assessment_id: checks
  area: schema
  topic: Deterministic gates and stable identifiers
  outcome: supported
  summary: All native stable IDs and citation identities resolve in source-native
    metadata. Target gates pass; broader gates are verified reuse, not fresh execution.
    Citation resolution alone does not establish support for the attached taxon/state
    claim.
  target_ids:
  - GO:0030089
  evidence_ids:
  - validation
  - go
  - eco
  - zheng
- assessment_id: ownership
  area: ownership
  topic: History and read-only boundary
  outcome: supported
  summary: Entire target and retained append-only CREATE event read. All native data,
    histories and prior bundle bytes remain unchanged. Future corrections belong to
    guarded maintained-YAML curation; this review neither promotes PROPOSED nor resolves
    any prior finding.
  target_ids:
  - GO:0030089
  evidence_ids:
  - native
  - predecessors
findings:
- finding_id: F1
  issue_key: phycobilisome-pcc6803-state-source-conflation
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Separate the PCC6803 state-resolved structure from the Zheng2021 paper
  description: The native PCC6803 light-harvesting/photoprotected example cites DOI10.1038/s41467-021-25813-y,
    and multiple core-related notes call it Sauer2021. The inspected paper is Zheng2021
    and its new structures concern PCC7002/PCC7120. The stated state-resolved PCC6803
    experiment is reported by Dominguez-Martin, Sauer and colleagues2022 under DOI10.1038/s41586-022-05156-4.
    Correct claim-level attribution without denying the2021 secondary PCC6803 array
    comparison.
  target_ids:
  - GO:0030089
  field_paths:
  - canonical_examples[taxon_id=NCBITaxon:1148].reference
  - canonical_examples[taxon_id=NCBITaxon:1148].note
  - components[allophycocyanin_core].evidence
  - evidence[reference=DOI:10.1038/s41467-021-25813-y].notes
  - causal_graphs[rod_core_energy_funnel].edges[subject=core].evidence
  evidence_ids:
  - native
  - zheng
  - dominguez
  rule_id: review-checklist:exact-source-and-experimental-scope
  native_severity: major
  normalization_reason: Wrong experimental study and organism/state scope on a material
    structural example, not just citation formatting. Generic structure identity remains
    valid.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/phycobilisome.yaml
    role: maintained scientific record
- finding_id: F2
  issue_key: phycobilisome-coreless-architecture-scope
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Qualify the core requirement and core-mediated transfer route
  description: The generic record requires an allophycocyanin core and describes light
    harvesting through it without a conventional-architecture boundary. Two native
    primary references document functional coreless PBS alternatives in the named
    cyanobacterial models. Qualify the definition, constituent requirement, function
    and graph to distinguish conventional core-bearing complexes from those alternatives.
    Retain the GO identity and explicitly acknowledge its core-centric definition;
    do not infer that conventional complexes lack a core or replace CpcG1 with CpcG2.
  target_ids:
  - GO:0030089
  field_paths:
  - definition
  - components[allophycocyanin_core].essentiality
  - components[allophycocyanin_core].role
  - functions[photosynthetic_light_harvesting].description
  - causal_graphs[rod_core_energy_funnel].description
  evidence_ids:
  - native
  - go
  - watanabe
  - kondo
  - kawakami
  rule_id: review-checklist:composition-and-organism-scope
  native_severity: major
  normalization_reason: An unqualified required constituent and transfer route exclude
    experimentally established members of the literature class. This requires an explicit
    architecture boundary, not merely an optional new example.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/phycobilisome.yaml
    role: maintained scientific record
actions:
- action_id: A1
  description: Correct the PCC6803 claim-level source and author/year notes. Retain
    the2021 citation only where its actual specimens, architecture or bounded array
    comparison support the attached claim; do not blindly replace every occurrence.
  finding_ids:
  - F1
  target_ids:
  - GO:0030089
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/phycobilisome.yaml
    role: maintained scientific record
  generator: Native guarded writer and documented product workflow only during separately
    authorized curation.
  acceptance_checks:
  - Each organism/state claim matches an inspected primary source.
  - Bibliographic attribution agrees across example, component and graph evidence
    notes.
  - Record remains PROPOSED; guarded edit/history, target gates and lineage-linked
    successor disposition are required.
- action_id: A2
  description: Introduce a supported conventional/coreless architecture distinction
    in the maintained record and constrain the existing core-transfer graph to the
    architecture it represents.
  finding_ids:
  - F2
  target_ids:
  - GO:0030089
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/phycobilisome.yaml
    role: maintained scientific record
  acceptance_checks:
  - No universal allophycocyanin-core requirement is implied for documented coreless
    alternatives.
  - The conventional core/rod model remains supported and the GO definition limitation
    stays explicit.
  - CpcG1 and CpcG2 gene/accession identities are not conflated.
  - Validate guarded native changes and save a successor retaining this stable issue
    key.
limitations:
- 'Partial scientific review: entire target read and all rubric areas considered,
  but the Sui2021 photoprotection attribution is unassessed. Independent support for
  the biological function does not verify that specific citation note. This access
  limitation is not a third finding.'
- Same-agent review, not independent human sign-off, exhaustive literature/retraction
  search or new experimental analysis.
- Zheng and Kawakami selected main-text sections were inspected as identified in Evidence,
  not all figures, supplementary files or raw maps. Candidate energy-transfer pathways
  and uncertain linker assignments remain interpretations.
- Chang and Dominguez-Martin assessed from complete primary abstracts and bibliographic
  identities, not full articles. Watanabe abstract/Significance/Introduction and Kondo
  complete abstract support the bounded coreless examples; no unread Methods or Results
  are represented as inspected.
- Forty-six local captures include42 HTTP200, three HTTP500 XML failures and one HTTP403
  HTML response at the Sui PDF URL. The Sui local-fetch process exited1. Browser access
  initially exposed PDF pages0-2 only; subsequent opens/finds timed out or failed.
  PMC challenges were not bypassed. Search snippets are not evidence.
- All eleven exact UniProt searches verify present reviewed identity/uniqueness only,
  not reconstruction of the2026-09-08 retrieval. The two cited ECO annotations were
  inspected as UniProt assertions; no automatic conversion into universal structure
  membership.
- Fresh target checks are distinguished from checksum-verified broader-check reuse
  with original cache/no-adapter/test skips. No exact iModulonDB dataset applies.
  No target trait links exist; cached wider trait-source limitations remain.
- No native scientific edits, product regeneration, history/status changes, GitHub
  issue/PR creation, CI, push or merge. External-publication approval remains unanswered
  and is not bypassed.
tags:
- scientific-review
- energy-complex
- source-scope
- architecture-scope
- partial
```
