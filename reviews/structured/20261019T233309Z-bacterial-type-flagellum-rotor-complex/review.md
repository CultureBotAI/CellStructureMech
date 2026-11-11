# Bacterial flagellar rotor: identity, evidence and experimental context

- Review: 20261019T233309Z-bacterial-type-flagellum-rotor-complex
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-19T07:29:58Z
- Finished UTC: 2026-10-19T23:33:09Z
- Reviewer: Codex (unknown)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The MS/C-ring rotor identity, composition and coarse functions are supported. One minor experimental-context wording issue remains. Exact full-body support in the Minamino review was not established; this is a partial scientific observation of one record.

## Scope And Provenance

Full target-file read and all-field audit; literature coverage is partial as explicitly recorded.

Selection: First path-sorted unreviewed record among 909 maintained YAML records. Validated record_review.py list inventory: 255 bundles cover 120 paths; 789 uncovered before this batch.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0120107 | data/structures/appendage/bacterial_type_flagellum_rotor_complex.yaml | maintained | bacterial-type flagellum rotor complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Open schema validation | passed | True | GO:0120107 | Exit 0; No issues found. |
| Closed schema validation | passed | True | GO:0120107 | Exit 0; one target scanned, zero errors. |
| Native literature access audit | passed | True | GO:0120107 | Exit 0; 14 references across 30 citations: 3 full text, 8 abstract, 3 database references, none unreadable/unchecked. Manual source retrieval subsequently improved coverage; this diagnostic is not scientific validation. |
| Full-text verification of Minamino 2015 nearest-source claims | unavailable | True | GO:0120107 | All material assertions assessed against accessible cited sources, but the full Minamino 2015 review remained unavailable. Two PNAS claims were checked against their explicit abstracts only. Retain partial completion; do not infer exact full-body support. |
| iModulonDB runner availability | unavailable | False | GO:0120107 | No kg-microbe-sources runner on PATH; ignored-inclusive pyproject search under /Users/marcin/Documents/VIMSS/ontology/Mechs found no culturebotai-claw runner there. Used live UniProt/NCBI/QuickGO structured authorities instead. No transcriptomic absence claim is made. |
| Target identifier coverage including resolver residuals | passed | True | GO:0120107 | All CURIE-shaped target values have issuing-authority or appropriate local/source-specific existence verification. Generic PMID HTTP414 failures and skipped namespaces were resolved by scoped receipts; biological mapping correctness is assessed separately. |
| Full corpus QC | passed | True | GO:0120107 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0120107 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0120107 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0120107 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0120107 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Exact structure identity, synonyms and parthood

identity: supported. Targets: GO:0120107.

GO:0120107 denotes the combined MS/C-ring rotor. It is a motor part, with stator, export apparatus and axial rod excluded as neighboring structures. Both related rotor synonyms occur in the cited literature; this is a structure-level record.

### Subcomplex composition and essentiality

representation: supported. Targets: GO:0120107.

Two constituent subcomplexes adequately represent this level. FliF MS ring and FliG/FliM/FliN C ring are essential to the defined complete MS/C rotor; this does not assert each is necessary for every residual basal-body subassembly. No universal copy number is asserted.

### Taxon-paired protein examples

grounding: supported. Targets: GO:0120107.

The four reviewed UniProt accessions, gene symbols, exact NCBI taxon pairing and declared single-entry searches match live authority data. Literature supplies membership independently of identifier lookup.

### Taxonomic distribution and canonical example

scope: supported. Targets: GO:0120107.

Bacterial VARIABLE occurrence and the distinction from archaeal archaella are supported at review-level scope. Salmonella is a valid exemplar; strain-specific structural preparations do not establish universal stoichiometry.

### Assembly, torque and switching claims

evidence: supported. Targets: GO:0120107.

Assembly is supported by Francis and Kawamoto; rod coupling by Tan; phospho-CheY switching by Welch and Lee at the stated coarse level. The inaccessible full Minamino body limits a nearest-source check but other inspected cited papers corroborate the biology.

### Biological support across all six edge assertions

graph: supported. Targets: GO:0120107.

Edges 0 and 2 are supported by Kawamoto; edge 1 by Paul at a mixed-species model level; edge 3 biology is corroborated by Kawamoto’s Introduction on FliG and MotA/MotB torque; edge 4 by Tan; edge 5 by Lee plus Welch. This is not a claim of full nearest-source verification for edge 3. No disputed detailed FliG geometry or numerical stoichiometry is encoded.

### Experimental context of Paul 2011

provenance: concern. Targets: GO:0120107.

Two evidence notes compress mixed-species structural and functional work into wording about Salmonella rotor architecture. Salmonella EM genuinely constrained the model; clarify the other experimental systems without treating the core membership claim as false.

### Optional source composition, properties, images, traits and datasets

completeness: not_applicable. Targets: GO:0120107.

This file asserts no organism-specific complex composition, measurements, images, trait links or datasets. Their absence is not a defect: no required feature or unsupported placeholder was found in those surfaces.

### Status, curation history and boundary discussion

provenance: supported. Targets: GO:0120107.

PROPOSED status is appropriate for an agent-authored record. Target creation/review changes and later shared protein enrichment have repository history. The resolved discussion consistently excludes nonrotor neighboring parts. This audit does not promote status or append curation events.

### Minamino 2015 nearest-source support

evidence: unknown. Targets: GO:0120107.

Exact full-body support for definition_source, the torque function and graph edge 3 remains unverified. The abstract and preview support only part of their wording. Kawamoto and other inspected cited papers corroborate the coarse biology, but do not establish what this nearest citation says.

## Findings

### F1: Paul 2011 experimental context is compressed into Salmonella wording

minor / open / confirmed; issue key: rotor-paul2011-experimental-context.

The C-ring component and its graph-edge evidence notes describe Paul et al. as mapping the Salmonella rotor. The paper combines Thermotoga domain structures and E. coli experiments with earlier Salmonella EM. Clarify that provenance so a reader does not interpret this as a native Salmonella determination. Membership and coarse switching biology remain supported.

## Recommended Actions And Acceptance Checks

### A1

Clarify both Paul 2011 evidence notes to distinguish source proteins, cellular experiments and inherited EM context; retain the supported C-ring membership. Any future scientific edit must use the guarded writer and both history surfaces, followed by rendering.

- Compare revised wording directly with Paul 2011 Results, Figure 1A and Methods; do not label the work a native Salmonella complex determination.
- Run just validate and just validate-strict for the target, then just render and just qc after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/bacterial_type_flagellum_rotor_complex.yaml; Entire file; components, functions, taxonomic_distribution, causal_graphs, discussions, curation_history | supports | Read the complete maintained record. It defines an MS/C-ring rotor; two constituent subcomplexes, four LT2 protein examples, two distribution assertions, one Salmonella exemplar, three functions, six graph edges, and a resolved boundary discussion. Scientific status is PROPOSED. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0120107,GO:0120100,GO:0009431,GO:0009433,GO:0120101,GO:0030694; results[].id/name/isObsolete/aspect/definition/children | supports | Six exact nonobsolete cellular-component identities match. Motor explicitly has rotor and stator part_of children. Rotor definition describes membrane-anchored ring plus motor switch; MS/C membership is supported by the papers, not an explicit QuickGO rotor relation. |
| uniprot | https://rest.uniprot.org/uniprotkb/search?query=(gene_exact:fliF%20OR%20gene_exact:fliG%20OR%20gene_exact:fliM%20OR%20gene_exact:fliN)%20AND%20organism_id:99287%20AND%20reviewed:true&amp;format=tsv&amp;fields=accession,id,gene_names,organism_id,reviewed; All four results; separately inspected accession JSON including P0A1J9 localization evidence | supports | Exactly one reviewed LT2 entry per gene: P15928/fliF, P0A1J9/fliG, P26418/fliM, P26419/fliN. Labels match. P0A1J9 cites ECO:0000269 and PMID:1631122 for its inner-membrane localization. Identity evidence is correctly distinguished from structural membership. |
| taxa | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=2,2157,90371,99287&amp;retmode=xml; TaxaSet/Taxon scientific names, ranks and lineage | supports | All four NCBI names match; 99287 is the LT2 strain within serovar 90371, while 2 and 2157 are domains. |
| kawamoto | https://www.nature.com/articles/s41467-021-24507-9; Introduction; Results: CryoEM structural analysis of the basal body; Mutation analysis of FliF; Figure 1; XML inspected through NCBI EFetch db=pmc&amp;id=PMC8270960&amp;retmode=xml | supports | Salmonella basal-body cryoEM and FliF analyses support membrane MS ring, attached C ring, templating, and rotor coupling. FliF mutagenesis separates MS/C assembly from export defects. Native rings and heterologously expressed FliF are distinct preparations. |
| tan | https://gwern.net/doc/biology/2021-tan.pdf; DOI:10.1016/j.cell.2021.03.057; article pp. 2, 12–13; MS ring–rod interactions and torque transmission; Limitations | supports | CryoEM of Salmonella LT2-derived motor–hook particles supports FliF contacts with FliE/FlgB and proximal rod, and the proposed torque-transmission interface. C ring and stator were absent from this preparation; it does not directly validate their interface. The record cites it for the rod-coupling claim only. |
| paul | https://pmc.ncbi.nlm.nih.gov/articles/PMC3160249/?pdf=1; DOI:10.1038/emboj.2011.188; Results: Structure of a FliGM:FliMM complex; Figure 1A; Methods: Protein preparation and Strains | partial | FliG/FliM/FliN membership and switch architecture are supported. Thermotoga maritima domains supplied crystal structures; E. coli supplied biochemical/genetic tests; prior Salmonella EM constrained the model. The record obscures this mixed experimental provenance. |
| lee | https://pmc.ncbi.nlm.nih.gov/articles/PMC3159035/?pdf=1; DOI:10.1038/nature09300; opening paragraph; Figure 4; EM docking; Methods Summary | supports | Aquifex FliG structures and comparison/docking support a proposed switching model; this was not an intact FliG/FliM/FliN structure determination. Paul disputes detailed domain geometry, which this record does not encode. General switching remains supported. |
| thomas | https://journals.asm.org/doi/10.1128/jb.00552-06; Abstract; Sample preparation; Figure 4; Discussion: The C ring | supports | Rotor terminology and the Salmonella Typhimurium example are supported by cryoEM of CW-locked SJW2811-derived NRF2811 hook–basal bodies. The canonical note also mentions later native MS-ring and architecture studies, whose sources occur elsewhere in the record. |
| francis | https://pmc.ncbi.nlm.nih.gov/articles/PMC49489/?pdf=1; DOI:10.1073/pnas.89.14.6304 / PMID:1631122; bibliographic header and abstract | supports | The abstract supports FliG on the cytoplasmic M-ring face in Salmonella using fusion mutants, immunoblotting, EM and antibody decoration. DOI and PMID identify the same paper. Full scanned body was not inspected. |
| welch | https://pmc.ncbi.nlm.nih.gov/articles/PMC47445/?pdf=1; DOI:10.1073/pnas.90.19.8787; abstract | supports | The abstract supports phosphorylation-dependent CheY binding to the switch with FliM as primary docking site. It supports the narrowly worded evidence note, not all downstream conformational details. Full scanned body was not inspected. |
| minamino | https://pubmed.ncbi.nlm.nih.gov/25613993/; DOI:10.1016/j.tim.2014.12.011; PubMed abstract via NCBI EFetch and publisher abstract/section preview | partial | Bibliographic identity and conserved MS/C motor core are verified. Full review body was not accessible through the inspected routes; its exact support for the definition and stator-to-FliG wording remains partial. The same coarse biology is corroborated by Kawamoto and Paul. |
| chevance | https://pmc.ncbi.nlm.nih.gov/articles/PMC5963726/?pdf=1; DOI:10.1038/nrmicro1887; Introduction, Box 1, closing discussion | supports | The cited review describes bacterial flagellar diversity, regulated transitions between flagellated and nonflagellated states, and MS/C-ring coupling. VARIABLE is a qualitative occurrence claim, not a prevalence estimate; no numerical prevalence is asserted. |
| archaella | https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2015.00023/full; Abstract; Similarities of archaeal flagella and type IV pili: further structural and genetic evidence | supports | The review distinguishes archaella from bacterial flagella, including type-IV-pilus-related machinery and surveyed archaeal genomes lacking bacterial rod/hook/ring genes. This supports the scoped absence note about the bacterial rotor, not absence of archaeal motility. |
| internal | repository working tree; Target identifier, label, slug and related GO structural IDs; history/records/bacterial_type_flagellum_rotor_complex | supports | Maintained motor, MS ring, C ring, stator and rod references resolve. Three record history files and the shared 2026-10-18 UniProt enrichment history explain the local events. |
| target-resolver-coverage | just check-curies-strict; data/structures/appendage/bacterial_type_flagellum_rotor_complex.yaml; exact scripts/check_curies.py collect() scope; reports/curie_check.tsv | supports | This target contains 25 distinct CURIE-shaped scalar values: 24 OK, 1 transport-unreachable and 0 skipped in the global report. The attached scoped receipts resolve each non-OK identifier. HTTP URLs and prose are outside collect(); their content was inspected separately. Existence is not proof of correct biological mapping. |
| liveness-pmid-1631122 | https://pmc.ncbi.nlm.nih.gov/articles/PMC49489/?pdf=1; DOI:10.1073/pnas.89.14.6304 / PMID:1631122; bibliographic header and abstract | supports | PMID:1631122 resolves through the scoped source inspection. This receipt reuses the existing reviewer inspection; it does not claim a fresh PubMed request or full-body reading. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Full text of DOI:10.1016/j.tim.2014.12.011 was not obtained; its abstract and publisher preview were inspected and relevant biology corroborated in other cited papers.
- Francis 1992 and Welch 1993 were assessed from their explicit abstracts, not their scanned full-body pages.
- Mechanistic papers use particular strains, preparations and inferred models; this review does not universalize precise copy numbers or resolve disputed FliG domain geometry.
- iModulonDB runner was unavailable within the bounded local search; no expression-module claim was inferred.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Only a review bundle is saved. No scientific record, status, generated page or history event was changed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T233309Z-bacterial-type-flagellum-rotor-complex
kind: record
repository: CultureBotAI/CellStructureMech
title: 'Bacterial flagellar rotor: identity, evidence and experimental context'
started_at: '2026-10-19T07:29:58Z'
finished_at: '2026-10-19T23:33:09Z'
reviewer:
  identity: Codex
  kind: agent
  independence: unknown
  independence_basis: Fresh source review with delegated source and authority checks.
    Historical agent curation is not treated as independent human review.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The MS/C-ring rotor identity, composition and coarse functions are supported.
  One minor experimental-context wording issue remains. Exact full-body support in
  the Minamino review was not established; this is a partial scientific observation
  of one record.
source:
  git_revision: 99692a3d5f16a7dcd6db7e3811344c299a977b81
  state: working_tree
  inputs:
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
  - path: data/structures/appendage/bacterial_type_flagellum_basal_body_c_ring.yaml
    sha256: 2700a13f9ed340978e2ff87c12d8c8533df7e68a676ee28998a1b8992b32fff2
    role: context
  - path: data/structures/appendage/bacterial_type_flagellum_basal_body_ms_ring.yaml
    sha256: 3dff5bf1515fcc88eb92baba769644b3132deebfb84bd81aca6503211cf2bb4f
    role: context
  - path: data/structures/appendage/bacterial_type_flagellum_basal_body_rod.yaml
    sha256: 4bc0fd676e9105d51d591cd6808eba7b15881e5a599334eb13d2fa12c857a3ae
    role: context
  - path: data/structures/appendage/bacterial_type_flagellum_motor.yaml
    sha256: 5e44c59ab01fe438525f8536391b09d400702fbf63b0be48e7f3e91fed9b9fd2
    role: context
  - path: data/structures/appendage/bacterial_type_flagellum_rotor_complex.yaml
    sha256: ee2dbb7c9e548096ea0890cf21c6a7126fd2a5536b3a208764e7024fe42616f3
    role: target
  - path: data/structures/appendage/bacterial_type_flagellum_stator_complex.yaml
    sha256: a3fa0c560f6f73e3c1d0be77b423926c56d658c94746e28dcb38ac4aae63f40a
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
  - path: history/infrastructure/uniprot-protein-examples/2026-10-18T053500Z-claude-code-1d4cdb.yaml
    sha256: 72f669bcf4fd3ecb68dc4bd592c937858602f7415ebba38d870cc7e73c8a7d1d
    role: context
  - path: history/records/bacterial_type_flagellum_rotor_complex/2026-09-08T160631Z-claude-b62592.yaml
    sha256: 648ce93efe63e98783cd554876808afa4feeb92822e37394bb399d56f63a145b
    role: context
  - path: history/records/bacterial_type_flagellum_rotor_complex/2026-09-08T202822Z-claude-96031f.yaml
    sha256: cbeab2c4ad78e66bf15f81b2d26a53fc481977d5b6f7b7d9c5feed7eeaec2a55
    role: context
  - path: history/records/bacterial_type_flagellum_rotor_complex/2026-09-08T214414Z-claude-8d0bc6.yaml
    sha256: 53a593420ac5700bab2d667a1c074377757243f88e6d2cb7480341f4e90b5177
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: GO:0120107
  path: data/structures/appendage/bacterial_type_flagellum_rotor_complex.yaml
  label: bacterial-type flagellum rotor complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_rotor_complex.yaml
    role: maintained scientific record
scope:
  description: Full target-file read and all-field audit; literature coverage is partial
    as explicitly recorded.
  selection: 'First path-sorted unreviewed record among 909 maintained YAML records.
    Validated record_review.py list inventory: 255 bundles cover 120 paths; 789 uncovered
    before this batch.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0120107
  exclusions:
  - target: Other 908 maintained records
    reason: Outside this single-record scientific observation; global deterministic
      checks do not imply their scientific coverage.
checks:
- check_id: schema
  name: Open schema validation
  status: passed
  required: true
  target_ids:
  - GO:0120107
  command: just validate data/structures/appendage/bacterial_type_flagellum_rotor_complex.yaml
  exit_code: 0
  summary: Exit 0; No issues found.
- check_id: strict
  name: Closed schema validation
  status: passed
  required: true
  target_ids:
  - GO:0120107
  command: just validate-strict data/structures/appendage/bacterial_type_flagellum_rotor_complex.yaml
    --out /private/tmp/cellstructure-record-reviews-UhRFh7/rotor-strict.tsv
  exit_code: 0
  summary: Exit 0; one target scanned, zero errors.
- check_id: readability
  name: Native literature access audit
  status: passed
  required: true
  target_ids:
  - GO:0120107
  command: just evidence-audit --record data/structures/appendage/bacterial_type_flagellum_rotor_complex.yaml
  exit_code: 0
  summary: 'Exit 0; 14 references across 30 citations: 3 full text, 8 abstract, 3
    database references, none unreadable/unchecked. Manual source retrieval subsequently
    improved coverage; this diagnostic is not scientific validation.'
- check_id: primary-source-coverage
  name: Full-text verification of Minamino 2015 nearest-source claims
  status: unavailable
  required: true
  target_ids:
  - GO:0120107
  summary: All material assertions assessed against accessible cited sources, but
    the full Minamino 2015 review remained unavailable. Two PNAS claims were checked
    against their explicit abstracts only. Retain partial completion; do not infer
    exact full-body support.
  evidence_ids:
  - minamino
  - francis
  - welch
  - kawamoto
  - paul
  - lee
  - tan
  - thomas
  - chevance
  - archaella
- check_id: structured-adapter
  name: iModulonDB runner availability
  status: unavailable
  required: false
  target_ids:
  - GO:0120107
  summary: No kg-microbe-sources runner on PATH; ignored-inclusive pyproject search
    under /Users/marcin/Documents/VIMSS/ontology/Mechs found no culturebotai-claw
    runner there. Used live UniProt/NCBI/QuickGO structured authorities instead. No
    transcriptomic absence claim is made.
  scope_note: Bounded local runner search; not a claim that no installation exists
    elsewhere. Expression-module evidence would not establish physical rotor membership.
- check_id: target-identifier-coverage
  name: Target identifier coverage including resolver residuals
  status: passed
  required: true
  target_ids:
  - GO:0120107
  summary: All CURIE-shaped target values have issuing-authority or appropriate local/source-specific
    existence verification. Generic PMID HTTP414 failures and skipped namespaces were
    resolved by scoped receipts; biological mapping correctness is assessed separately.
  evidence_ids:
  - target-resolver-coverage
  - liveness-pmid-1631122
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0120107
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused across
    the batch because maintained scientific inputs are unchanged. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0120107
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused across
    the batch because maintained scientific inputs are unchanged. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0120107
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused across
    the batch because maintained scientific inputs are unchanged. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0120107
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused across
    the batch because maintained scientific inputs are unchanged. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0120107
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused across
    the batch because maintained scientific inputs are unchanged. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/appendage/bacterial_type_flagellum_rotor_complex.yaml
  locator: Entire file; components, functions, taxonomic_distribution, causal_graphs,
    discussions, curation_history
  accessed_at: '2026-10-19T07:29:58Z'
  support: supports
  summary: Read the complete maintained record. It defines an MS/C-ring rotor; two
    constituent subcomplexes, four LT2 protein examples, two distribution assertions,
    one Salmonella exemplar, three functions, six graph edges, and a resolved boundary
    discussion. Scientific status is PROPOSED.
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0120107,GO:0120100,GO:0009431,GO:0009433,GO:0120101,GO:0030694
  locator: results[].id/name/isObsolete/aspect/definition/children
  accessed_at: '2026-10-19T07:30:56Z'
  support: supports
  summary: Six exact nonobsolete cellular-component identities match. Motor explicitly
    has rotor and stator part_of children. Rotor definition describes membrane-anchored
    ring plus motor switch; MS/C membership is supported by the papers, not an explicit
    QuickGO rotor relation.
- evidence_id: uniprot
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?query=(gene_exact:fliF%20OR%20gene_exact:fliG%20OR%20gene_exact:fliM%20OR%20gene_exact:fliN)%20AND%20organism_id:99287%20AND%20reviewed:true&format=tsv&fields=accession,id,gene_names,organism_id,reviewed
  locator: All four results; separately inspected accession JSON including P0A1J9
    localization evidence
  accessed_at: '2026-10-19T07:31:10Z'
  support: supports
  summary: 'Exactly one reviewed LT2 entry per gene: P15928/fliF, P0A1J9/fliG, P26418/fliM,
    P26419/fliN. Labels match. P0A1J9 cites ECO:0000269 and PMID:1631122 for its inner-membrane
    localization. Identity evidence is correctly distinguished from structural membership.'
- evidence_id: taxa
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=2,2157,90371,99287&retmode=xml
  locator: TaxaSet/Taxon scientific names, ranks and lineage
  accessed_at: '2026-10-19T07:30:56Z'
  support: supports
  summary: All four NCBI names match; 99287 is the LT2 strain within serovar 90371,
    while 2 and 2157 are domains.
- evidence_id: kawamoto
  kind: primary_source
  reference: https://www.nature.com/articles/s41467-021-24507-9
  locator: 'Introduction; Results: CryoEM structural analysis of the basal body; Mutation
    analysis of FliF; Figure 1; XML inspected through NCBI EFetch db=pmc&id=PMC8270960&retmode=xml'
  accessed_at: '2026-10-19T07:35:51Z'
  support: supports
  summary: Salmonella basal-body cryoEM and FliF analyses support membrane MS ring,
    attached C ring, templating, and rotor coupling. FliF mutagenesis separates MS/C
    assembly from export defects. Native rings and heterologously expressed FliF are
    distinct preparations.
- evidence_id: tan
  kind: primary_source
  reference: https://gwern.net/doc/biology/2021-tan.pdf
  locator: DOI:10.1016/j.cell.2021.03.057; article pp. 2, 12–13; MS ring–rod interactions
    and torque transmission; Limitations
  accessed_at: '2026-10-19T07:34:30Z'
  support: supports
  summary: CryoEM of Salmonella LT2-derived motor–hook particles supports FliF contacts
    with FliE/FlgB and proximal rod, and the proposed torque-transmission interface.
    C ring and stator were absent from this preparation; it does not directly validate
    their interface. The record cites it for the rod-coupling claim only.
- evidence_id: paul
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3160249/?pdf=1
  locator: 'DOI:10.1038/emboj.2011.188; Results: Structure of a FliGM:FliMM complex;
    Figure 1A; Methods: Protein preparation and Strains'
  accessed_at: '2026-10-19T07:31:10Z'
  support: partial
  summary: FliG/FliM/FliN membership and switch architecture are supported. Thermotoga
    maritima domains supplied crystal structures; E. coli supplied biochemical/genetic
    tests; prior Salmonella EM constrained the model. The record obscures this mixed
    experimental provenance.
- evidence_id: lee
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3159035/?pdf=1
  locator: DOI:10.1038/nature09300; opening paragraph; Figure 4; EM docking; Methods
    Summary
  accessed_at: '2026-10-19T07:31:10Z'
  support: supports
  summary: Aquifex FliG structures and comparison/docking support a proposed switching
    model; this was not an intact FliG/FliM/FliN structure determination. Paul disputes
    detailed domain geometry, which this record does not encode. General switching
    remains supported.
- evidence_id: thomas
  kind: primary_source
  reference: https://journals.asm.org/doi/10.1128/jb.00552-06
  locator: 'Abstract; Sample preparation; Figure 4; Discussion: The C ring'
  accessed_at: '2026-10-19T07:30:18Z'
  support: supports
  summary: Rotor terminology and the Salmonella Typhimurium example are supported
    by cryoEM of CW-locked SJW2811-derived NRF2811 hook–basal bodies. The canonical
    note also mentions later native MS-ring and architecture studies, whose sources
    occur elsewhere in the record.
- evidence_id: francis
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC49489/?pdf=1
  locator: DOI:10.1073/pnas.89.14.6304 / PMID:1631122; bibliographic header and abstract
  accessed_at: '2026-10-19T07:31:28Z'
  support: supports
  summary: The abstract supports FliG on the cytoplasmic M-ring face in Salmonella
    using fusion mutants, immunoblotting, EM and antibody decoration. DOI and PMID
    identify the same paper. Full scanned body was not inspected.
- evidence_id: welch
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC47445/?pdf=1
  locator: DOI:10.1073/pnas.90.19.8787; abstract
  accessed_at: '2026-10-19T07:31:28Z'
  support: supports
  summary: The abstract supports phosphorylation-dependent CheY binding to the switch
    with FliM as primary docking site. It supports the narrowly worded evidence note,
    not all downstream conformational details. Full scanned body was not inspected.
- evidence_id: minamino
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/25613993/
  locator: DOI:10.1016/j.tim.2014.12.011; PubMed abstract via NCBI EFetch and publisher
    abstract/section preview
  accessed_at: '2026-10-19T07:32:01Z'
  support: partial
  summary: Bibliographic identity and conserved MS/C motor core are verified. Full
    review body was not accessible through the inspected routes; its exact support
    for the definition and stator-to-FliG wording remains partial. The same coarse
    biology is corroborated by Kawamoto and Paul.
- evidence_id: chevance
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC5963726/?pdf=1
  locator: DOI:10.1038/nrmicro1887; Introduction, Box 1, closing discussion
  accessed_at: '2026-10-19T07:31:28Z'
  support: supports
  summary: The cited review describes bacterial flagellar diversity, regulated transitions
    between flagellated and nonflagellated states, and MS/C-ring coupling. VARIABLE
    is a qualitative occurrence claim, not a prevalence estimate; no numerical prevalence
    is asserted.
- evidence_id: archaella
  kind: primary_source
  reference: https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2015.00023/full
  locator: 'Abstract; Similarities of archaeal flagella and type IV pili: further
    structural and genetic evidence'
  accessed_at: '2026-10-19T07:31:29Z'
  support: supports
  summary: The review distinguishes archaella from bacterial flagella, including type-IV-pilus-related
    machinery and surveyed archaeal genomes lacking bacterial rod/hook/ring genes.
    This supports the scoped absence note about the bacterial rotor, not absence of
    archaeal motility.
- evidence_id: internal
  kind: search
  reference: repository working tree
  locator: Target identifier, label, slug and related GO structural IDs; history/records/bacterial_type_flagellum_rotor_complex
  accessed_at: '2026-10-19T07:31:10Z'
  support: supports
  summary: Maintained motor, MS ring, C ring, stator and rod references resolve. Three
    record history files and the shared 2026-10-18 UniProt enrichment history explain
    the local events.
  search_scope: rg --no-ignore --hidden across the isolated clone; includes ignored
    files, excludes .git and .venv internals. Queried GO:0120107, bacterial-type flagellum
    rotor complex, bacterial_type_flagellum_rotor_complex, and the five related structural
    identifiers. This establishes reference/owner locations, not absence from external
    literature.
- evidence_id: target-resolver-coverage
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/appendage/bacterial_type_flagellum_rotor_complex.yaml;
    exact scripts/check_curies.py collect() scope; reports/curie_check.tsv
  accessed_at: '2026-10-19T23:32:25.400320Z'
  support: supports
  snapshot_sha256: 68d64e4e86437df228658f43be4d47b41054fe882fedf357e660293691a0a061
  summary: 'This target contains 25 distinct CURIE-shaped scalar values: 24 OK, 1
    transport-unreachable and 0 skipped in the global report. The attached scoped
    receipts resolve each non-OK identifier. HTTP URLs and prose are outside collect();
    their content was inspected separately. Existence is not proof of correct biological
    mapping.'
- evidence_id: liveness-pmid-1631122
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC49489/?pdf=1
  locator: DOI:10.1073/pnas.89.14.6304 / PMID:1631122; bibliographic header and abstract
  accessed_at: '2026-10-19T07:31:28Z'
  support: supports
  summary: PMID:1631122 resolves through the scoped source inspection. This receipt
    reuses the existing reviewer inspection; it does not claim a fresh PubMed request
    or full-body reading.
  snapshot_sha256: f612b849dd5b8cdc957c64e7867274d9309439f2d1d25876aeae3ed033f984ae
- evidence_id: global-qc-result
  kind: validation
  reference: just qc
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec
  accessed_at: '2026-10-19T07:38:12Z'
  support: supports
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  snapshot_sha256: 7b6165ba8532d080a336f7a5a4c29b456fdf7182dd596410b700dfe60af61a06
- evidence_id: global-history-result
  kind: validation
  reference: just validate-history
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0
  accessed_at: '2026-10-19T07:29:37Z'
  support: supports
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  snapshot_sha256: b98e3eecd58a81fa46033e6baca6977811a439f119b943fd5d9931964adb2680
- evidence_id: global-products-result
  kind: validation
  reference: just validate-products
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad
  accessed_at: '2026-10-19T07:32:39Z'
  support: supports
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  snapshot_sha256: 2a1330c26aac5bd248a2fd3a3a7b9c882d2b3bb202365c555e5d6415d1c2203d
- evidence_id: global-traits-result
  kind: validation
  reference: just check-trait-links --check
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad
  accessed_at: '2026-10-19T07:29:45Z'
  support: supports
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  snapshot_sha256: 6eab64b59433928ec8e0df9b0046dbccf479c84bb0911c315feebc344d536007
- evidence_id: global-curies-result
  kind: validation
  reference: just check-curies-strict
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4
  accessed_at: '2026-10-19T08:04:01Z'
  support: supports
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  snapshot_sha256: 7cb413edccc92ee6ce79a32cd2b96a59bc4da37f2cb7b326eaca51a64f723cfb
assessments:
- assessment_id: identity
  area: identity
  topic: Exact structure identity, synonyms and parthood
  outcome: supported
  summary: GO:0120107 denotes the combined MS/C-ring rotor. It is a motor part, with
    stator, export apparatus and axial rod excluded as neighboring structures. Both
    related rotor synonyms occur in the cited literature; this is a structure-level
    record.
  target_ids:
  - GO:0120107
  evidence_ids:
  - record
  - go
  - kawamoto
  - thomas
  - paul
- assessment_id: components
  area: representation
  topic: Subcomplex composition and essentiality
  outcome: supported
  summary: Two constituent subcomplexes adequately represent this level. FliF MS ring
    and FliG/FliM/FliN C ring are essential to the defined complete MS/C rotor; this
    does not assert each is necessary for every residual basal-body subassembly. No
    universal copy number is asserted.
  target_ids:
  - GO:0120107
  evidence_ids:
  - record
  - kawamoto
  - paul
  - go
- assessment_id: examples
  area: grounding
  topic: Taxon-paired protein examples
  outcome: supported
  summary: The four reviewed UniProt accessions, gene symbols, exact NCBI taxon pairing
    and declared single-entry searches match live authority data. Literature supplies
    membership independently of identifier lookup.
  target_ids:
  - GO:0120107
  evidence_ids:
  - uniprot
  - taxa
  - francis
  - record
- assessment_id: scope
  area: scope
  topic: Taxonomic distribution and canonical example
  outcome: supported
  summary: Bacterial VARIABLE occurrence and the distinction from archaeal archaella
    are supported at review-level scope. Salmonella is a valid exemplar; strain-specific
    structural preparations do not establish universal stoichiometry.
  target_ids:
  - GO:0120107
  evidence_ids:
  - chevance
  - archaella
  - taxa
  - thomas
  dimensions:
  - name: experimental_context
    value: Salmonella mutant basal-body preparations; Thermotoga and Aquifex domains;
      E. coli functional tests
    definition: Organisms and experimental systems supplying mechanistic support;
      not interchangeable strain claims.
    evidence_ids:
    - thomas
    - paul
    - lee
    - kawamoto
- assessment_id: functions
  area: evidence
  topic: Assembly, torque and switching claims
  outcome: supported
  summary: Assembly is supported by Francis and Kawamoto; rod coupling by Tan; phospho-CheY
    switching by Welch and Lee at the stated coarse level. The inaccessible full Minamino
    body limits a nearest-source check but other inspected cited papers corroborate
    the biology.
  target_ids:
  - GO:0120107
  evidence_ids:
  - francis
  - kawamoto
  - tan
  - welch
  - lee
  - minamino
- assessment_id: graph
  area: graph
  topic: Biological support across all six edge assertions
  outcome: supported
  summary: Edges 0 and 2 are supported by Kawamoto; edge 1 by Paul at a mixed-species
    model level; edge 3 biology is corroborated by Kawamoto’s Introduction on FliG
    and MotA/MotB torque; edge 4 by Tan; edge 5 by Lee plus Welch. This is not a claim
    of full nearest-source verification for edge 3. No disputed detailed FliG geometry
    or numerical stoichiometry is encoded.
  target_ids:
  - GO:0120107
  evidence_ids:
  - kawamoto
  - paul
  - minamino
  - tan
  - lee
  - welch
- assessment_id: provenance
  area: provenance
  topic: Experimental context of Paul 2011
  outcome: concern
  summary: Two evidence notes compress mixed-species structural and functional work
    into wording about Salmonella rotor architecture. Salmonella EM genuinely constrained
    the model; clarify the other experimental systems without treating the core membership
    claim as false.
  target_ids:
  - GO:0120107
  evidence_ids:
  - record
  - paul
- assessment_id: completeness
  area: completeness
  topic: Optional source composition, properties, images, traits and datasets
  outcome: not_applicable
  summary: 'This file asserts no organism-specific complex composition, measurements,
    images, trait links or datasets. Their absence is not a defect: no required feature
    or unsupported placeholder was found in those surfaces.'
  target_ids:
  - GO:0120107
  evidence_ids:
  - record
- assessment_id: history
  area: provenance
  topic: Status, curation history and boundary discussion
  outcome: supported
  summary: PROPOSED status is appropriate for an agent-authored record. Target creation/review
    changes and later shared protein enrichment have repository history. The resolved
    discussion consistently excludes nonrotor neighboring parts. This audit does not
    promote status or append curation events.
  target_ids:
  - GO:0120107
  evidence_ids:
  - record
  - internal
  - go
- assessment_id: nearest-minamino
  area: evidence
  topic: Minamino 2015 nearest-source support
  outcome: unknown
  summary: Exact full-body support for definition_source, the torque function and
    graph edge 3 remains unverified. The abstract and preview support only part of
    their wording. Kawamoto and other inspected cited papers corroborate the coarse
    biology, but do not establish what this nearest citation says.
  target_ids:
  - GO:0120107
  evidence_ids:
  - minamino
  - kawamoto
findings:
- finding_id: F1
  issue_key: rotor-paul2011-experimental-context
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Paul 2011 experimental context is compressed into Salmonella wording
  description: The C-ring component and its graph-edge evidence notes describe Paul
    et al. as mapping the Salmonella rotor. The paper combines Thermotoga domain structures
    and E. coli experiments with earlier Salmonella EM. Clarify that provenance so
    a reader does not interpret this as a native Salmonella determination. Membership
    and coarse switching biology remain supported.
  target_ids:
  - GO:0120107
  field_paths:
  - components[component_id=c_ring].evidence[0].notes
  - causal_graphs[graph_id=ms_c_ring_rotor_function].edges[1].evidence[0].notes
  evidence_ids:
  - record
  - paul
  rule_id: 'review-checklist: experimental context and source version'
  native_severity: minor
  normalization_reason: Bounded provenance wording, without wrong structure identity
    or an unsupported core membership claim.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_rotor_complex.yaml
    role: maintained scientific record
actions:
- action_id: A1
  description: Clarify both Paul 2011 evidence notes to distinguish source proteins,
    cellular experiments and inherited EM context; retain the supported C-ring membership.
    Any future scientific edit must use the guarded writer and both history surfaces,
    followed by rendering.
  finding_ids:
  - F1
  target_ids:
  - GO:0120107
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_rotor_complex.yaml
    role: maintained scientific record
  acceptance_checks:
  - Compare revised wording directly with Paul 2011 Results, Figure 1A and Methods;
    do not label the work a native Salmonella complex determination.
  - Run just validate and just validate-strict for the target, then just render and
    just qc after separately authorized curation.
limitations:
- Full text of DOI:10.1016/j.tim.2014.12.011 was not obtained; its abstract and publisher
  preview were inspected and relevant biology corroborated in other cited papers.
- Francis 1992 and Welch 1993 were assessed from their explicit abstracts, not their
  scanned full-body pages.
- Mechanistic papers use particular strains, preparations and inferred models; this
  review does not universalize precise copy numbers or resolve disputed FliG domain
  geometry.
- iModulonDB runner was unavailable within the bounded local search; no expression-module
  claim was inferred.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- Only a review bundle is saved. No scientific record, status, generated page or history
  event was changed.
```
