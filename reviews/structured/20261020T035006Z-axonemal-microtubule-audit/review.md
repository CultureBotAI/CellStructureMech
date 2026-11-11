# Axonemal microtubule hierarchy and assembly terminology

- Review: 20261020T035006Z-axonemal-microtubule-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-20T03:48:31Z
- Finished UTC: 2026-10-20T03:50:06Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact generic identity, nine topology edges and source-scoped scaffold role are supported. One minor wording inconsistency remains in discussion notes that call the doublet and central-pair assemblies subtypes.

## Scope And Provenance

Complete target, all nine graph edges and three cited primary studies; bounded related-record identity checks.

Selection: Fifth unreviewed path of batch3.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0005879 | data/structures/cytoskeleton/axonemal_microtubule.yaml | maintained | axonemal microtubule |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0005879 | Focused validator passed. |
| Focused native strict | passed | True | GO:0005879 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0005879 | All13 identifiers OK. |
| Expression-module applicability | not_applicable | False | GO:0005879 | No gene, locus or expression-module assertion is made; structural topology is assessed using ontology and primary microscopy sources. |
| Claim-level scientific review | passed | True | GO:0005879 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0005879 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0005879 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0005879 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0005879 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0005879 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Generic axonemal filament

identity: supported. Targets: GO:0005879.

Exact GO identity, definition and FILAMENT kind are appropriate. The source definition is used for this generic category, while the experimental scope is Chlamydomonas.

### All nine topology edges

graph: supported. Targets: GO:0005879.

Four is-a subtype edges, four membership edges and axoneme parthood exactly match GO. The geometry is expressly NONMECHANISTIC.

### Whole9+2 example

scope: supported. Targets: GO:0005879.

The original2006 source covers the whole scaffold;2019 doublet and2013 central-pair sources support their respective parts. Normal species anatomy supports qualitative COMMON without a numeric prevalence claim.

### Structural scaffold

evidence: supported. Targets: GO:0005879.

Formation of the axonemal scaffold is a supported structural role. The description remains bounded to A/B and C1/C2 architecture and asserts neither an untested regulatory mechanism nor a universal component inventory.

### Assembly versus subtype wording

consistency: concern. Targets: GO:0005879.

The resolved discussion correctly avoids duplicating component detail, but its two evidence notes mislabel containing assemblies as subtypes, contrary to both current GO ancestry and the graph.

### Native scope and optional surfaces

completeness: supported. Targets: GO:0005879.

The whole-scaffold citation correction is preserved in history. PROPOSED status remains appropriate. Component detail is intentionally distributed; no protein examples, images, quantitative property or trait claims require extra verification.

## Findings

### F1: Discussion notes call containing assemblies microtubule subtypes

minor / open / confirmed; issue key: axonemal-microtubule-assembly-subtype-wording.

The resolved discussion calls GO0097545 an outer-doublet subtype and GO0097540 a central-pair subtype. These are containing assemblies, not is_a descendants of GO0005879. The actual subtype members are A/B and C1/C2; the graph already represents their relations correctly.

## Recommended Actions And Acceptance Checks

### A1

Call the doublet and central pair containing assemblies in the discussion evidence notes; preserve the actual A/B/C1/C2 subtype and part-of graph.

- The discussion distinguishes assemblies from constituent microtubule subtypes.
- No structured relation or correct graph edge is changed merely to match the old prose.
- After separately authorized curation, validate the record, history and generated pages.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| microtubule-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005879,GO:0005881,GO:0005930,GO:0097545,GO:0097649,GO:0097650,GO:0097540,GO:1990719,GO:1990720; Exact terms, definitions and all pertinent child relations | supports | Nine active terms match all labels. A/B/C1/C2 are is_a children of axonemal microtubule; A/B are parts of the doublet and C1/C2 parts of the central pair. Cytoplasmic-microtubule parentage and axoneme parthood are explicit. |
| microtubule-doublet-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097545/ancestors?relations=is_a; GO0097545 is_a ancestry | supports | The complete is_a ancestor response contains cellular anatomical entity and cellular component, not axonemal microtubule. |
| microtubule-pair-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097540/ancestors?relations=is_a; GO0097540 is_a ancestry | supports | The complete is_a ancestor response contains cellular anatomical entity and cellular component, not axonemal microtubule. |
| sheath-taxon | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=3055; Exact taxon identity | supports | NCBITaxon3055 identifies Chlamydomonas reinhardtii. |
| sheath-native-paper | https://pmc-oa-opendata.s3.amazonaws.com/PMC6936269.1/PMC6936269.1.xml; Doublet architecture Results and model-building Methods | supports | The primary model supports the A/B-tubule doublet walls and their distinction from luminal MIPs. |
| bridge-paper | https://pmc-oa-opendata.s3.amazonaws.com/PMC3914236.1/PMC3914236.1.xml; Central-pair Results and structural figures | supports | The primary source supports C1/C2 singlets, associated projections and their larger central-pair assembly. |
| dynein-doi | https://api.crossref.org/works/10.1126/science.1128618; Exact DOI/title and available PMID/PMCID joins | supports | Exact article identifiers and bibliographic metadata match the cited source. |
| dynein-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1126/science.1128618&amp;format=json&amp;resultType=core; Exact DOI/title and available PMID/PMCID joins | supports | Exact article identifiers and bibliographic metadata match the cited source. |
| sheath-doi | https://api.crossref.org/works/10.1016/j.cell.2019.09.030; Exact DOI/title and available PMID/PMCID joins | supports | Exact article identifiers and bibliographic metadata match the cited source. |
| sheath-native-meta | https://pmc-oa-opendata.s3.amazonaws.com/PMC6936269.1/PMC6936269.1.json; Exact DOI/title and available PMID/PMCID joins | supports | Exact article identifiers and bibliographic metadata match the cited source. |
| bridge-doi | https://api.crossref.org/works/10.1002/cm.21094; Exact DOI/title and available PMID/PMCID joins | supports | Exact article identifiers and bibliographic metadata match the cited source. |
| bridge-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1002/cm.21094&amp;format=json&amp;resultType=core; Exact DOI/title and available PMID/PMCID joins | supports | Exact article identifiers and bibliographic metadata match the cited source. |
| paper2006 | https://www.researchgate.net/publication/6871150_The_Molecular_Architecture_of_Axonemes_Revealed_by_Cryoelectron_Tomography; Author-uploaded primary Introduction, Chlamydomonas sections and Figures1/5 | supports | The cited primary text depicts the whole Chlamydomonas9+2 scaffold, supporting the species/example claim beyond outer doublets alone. |
| record | data/structures/cytoskeleton/axonemal_microtubule.yaml; Entire target, all nine edges, discussion and inline history | context_only | The graph separates subtype from part-of correctly. Two discussion evidence notes nevertheless call the doublet and central pair subtypes. Generic microtubule, doublet, central-pair and four individual-tubule records exist; no scientific review of those additional records is claimed. |
| schema-result | just validate data/structures/cytoskeleton/axonemal_microtubule.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/axonemal_microtubule.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/axonemal_microtubule.yaml --out /private/tmp/cellstructure-batch3-20261019-YKo4JU/axonemal_microtubule-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/axonemal_microtubule.yaml --out /private/tmp/cellstructure-batch3-20261019-YKo4JU/axonemal_microtubule-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch3-20261019-YKo4JU/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch3-20261019-YKo4JU/axonemal_microtubule-strict.tsv |
| target-curies | just check-curies-strict; data/structures/cytoskeleton/axonemal_microtubule.yaml; exact collect() scope | supports | All13 collected target identifiers returned OK at the unchanged base. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- This generic review does not certify the detailed composition of related records.
- COMMON is qualitative normal anatomy rather than measured population prevalence.
- The2006 primary text was read from an author upload; no browser-text byte hash is claimed.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Only the review bundle is saved. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T035006Z-axonemal-microtubule-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Axonemal microtubule hierarchy and assembly terminology
started_at: '2026-10-20T03:48:31Z'
finished_at: '2026-10-20T03:50:06Z'
reviewer:
  identity: Codex
  kind: agent
  independence: unknown
  independence_basis: Current source review does not establish independent historical
    authorship.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Exact generic identity, nine topology edges and source-scoped scaffold role
  are supported. One minor wording inconsistency remains in discussion notes that
  call the doublet and central-pair assemblies subtypes.
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
  - path: data/structures/cytoskeleton/a_axonemal_microtubule.yaml
    sha256: ce35e4855b506178485b229b515c89a717ddee0a5a9d26fff88ba991fac5b06b
    role: context
  - path: data/structures/cytoskeleton/axonemal_central_pair.yaml
    sha256: 5e6d9301edf395d718469728f33d6fd7aad90d01bea8bf84b31ba6a742e7cf75
    role: context
  - path: data/structures/cytoskeleton/axonemal_doublet_microtubule.yaml
    sha256: 8ca9df0aa3b658a662383c2f1b4489b029699d011828f35b4e2d82ecb2fa40b6
    role: context
  - path: data/structures/cytoskeleton/axonemal_microtubule.yaml
    sha256: 480cd29d1f2e87c07c19dd8d60e50768cdcce29223b28ce2df1d4c956dc46282
    role: target
  - path: data/structures/cytoskeleton/b_axonemal_microtubule.yaml
    sha256: 14dc7bee2d7f4dbaf766868cb49cb2e0145765a5de184a80452664871a7db50f
    role: context
  - path: data/structures/cytoskeleton/c1_axonemal_microtubule.yaml
    sha256: 2f4f420d4958d3133a60a7b072e517361d7c2c4908acb4e307bd2033095f18f4
    role: context
  - path: data/structures/cytoskeleton/c2_axonemal_microtubule.yaml
    sha256: 97c8666ddef318d146a2d902a225f8b0313468bcf54fa32d81d5f1d127798a44
    role: context
  - path: data/structures/cytoskeleton/microtubule.yaml
    sha256: 06773fdcef54b61e7ed2a8a4c1066dfed8ba71dce8050eb39a879fab702b7498
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
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: GO:0005879
  path: data/structures/cytoskeleton/axonemal_microtubule.yaml
  label: axonemal microtubule
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/axonemal_microtubule.yaml
    role: maintained scientific record
scope:
  description: Complete target, all nine graph edges and three cited primary studies;
    bounded related-record identity checks.
  selection: Fifth unreviewed path of batch3.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0005879
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0005879
  command: just validate data/structures/cytoskeleton/axonemal_microtubule.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0005879
  command: just validate-strict data/structures/cytoskeleton/axonemal_microtubule.yaml
    --out /private/tmp/cellstructure-batch3-20261019-YKo4JU/axonemal_microtubule-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0005879
  summary: All13 identifiers OK.
  evidence_ids:
  - target-curies
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0005879
  summary: No gene, locus or expression-module assertion is made; structural topology
    is assessed using ontology and primary microscopy sources.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0005879
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - microtubule-go
  - microtubule-doublet-ancestors
  - microtubule-pair-ancestors
  - sheath-taxon
  - sheath-native-paper
  - bridge-paper
  - dynein-doi
  - dynein-epmc
  - sheath-doi
  - sheath-native-meta
  - bridge-doi
  - bridge-epmc
  - paper2006
  - record
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0005879
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch3 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0005879
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch3 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0005879
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch3 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0005879
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch3 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0005879
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch3 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: microtubule-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005879,GO:0005881,GO:0005930,GO:0097545,GO:0097649,GO:0097650,GO:0097540,GO:1990719,GO:1990720
  locator: Exact terms, definitions and all pertinent child relations
  accessed_at: '2026-10-20T03:48:50.414698Z'
  support: supports
  summary: Nine active terms match all labels. A/B/C1/C2 are is_a children of axonemal
    microtubule; A/B are parts of the doublet and C1/C2 parts of the central pair.
    Cytoplasmic-microtubule parentage and axoneme parthood are explicit.
  snapshot_sha256: 7bd301f0f9e2eac89c21c76ffe88fcb1e52571d016adf64d4c162dbf273d0dad
- evidence_id: microtubule-doublet-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097545/ancestors?relations=is_a
  locator: GO0097545 is_a ancestry
  accessed_at: '2026-10-20T03:48:50.557567Z'
  support: supports
  summary: The complete is_a ancestor response contains cellular anatomical entity
    and cellular component, not axonemal microtubule.
  snapshot_sha256: 77fc2b2d7301353cfcf2f6f1e3cfc087f429494f6c6d93f89d98efb0b4b0e055
- evidence_id: microtubule-pair-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097540/ancestors?relations=is_a
  locator: GO0097540 is_a ancestry
  accessed_at: '2026-10-20T03:48:50.386228Z'
  support: supports
  summary: The complete is_a ancestor response contains cellular anatomical entity
    and cellular component, not axonemal microtubule.
  snapshot_sha256: 9db33924a80fc2576fbe069bc15170bafe920e8c4a572ad040faef3ad8a3c8b1
- evidence_id: sheath-taxon
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=3055
  locator: Exact taxon identity
  accessed_at: '2026-10-20T03:38:20.199537Z'
  support: supports
  summary: NCBITaxon3055 identifies Chlamydomonas reinhardtii.
  snapshot_sha256: a17bc1c97fea9112288574ef15727ed7e37c42787a430ef074ae5fc654547e6b
- evidence_id: sheath-native-paper
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6936269.1/PMC6936269.1.xml
  locator: Doublet architecture Results and model-building Methods
  accessed_at: '2026-10-20T03:39:02.896527Z'
  support: supports
  summary: The primary model supports the A/B-tubule doublet walls and their distinction
    from luminal MIPs.
  snapshot_sha256: 0876ca7aaca5f9242bcead773c38bd14befec9d32ada12bb647428f60f79594e
- evidence_id: bridge-paper
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3914236.1/PMC3914236.1.xml
  locator: Central-pair Results and structural figures
  accessed_at: '2026-10-20T03:42:14.888078Z'
  support: supports
  summary: The primary source supports C1/C2 singlets, associated projections and
    their larger central-pair assembly.
  snapshot_sha256: 8ea6c2f20d7cecc7a071669f91afd2d6b2d2aa8681eefb5b001ef22c6b82a7d0
- evidence_id: dynein-doi
  kind: database
  reference: https://api.crossref.org/works/10.1126/science.1128618
  locator: Exact DOI/title and available PMID/PMCID joins
  accessed_at: '2026-10-20T03:46:21.364103Z'
  support: supports
  summary: Exact article identifiers and bibliographic metadata match the cited source.
  snapshot_sha256: 47d6b3ba693d41e04a97d329936eae46d6b1e4b18ca20b3c9734a213c83ff94a
- evidence_id: dynein-epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1126/science.1128618&format=json&resultType=core
  locator: Exact DOI/title and available PMID/PMCID joins
  accessed_at: '2026-10-20T03:46:21.748213Z'
  support: supports
  summary: Exact article identifiers and bibliographic metadata match the cited source.
  snapshot_sha256: e7f2749f2c3a6b39317f088a33e4528ad8fa85ca46821689867ae812b89ad36f
- evidence_id: sheath-doi
  kind: database
  reference: https://api.crossref.org/works/10.1016/j.cell.2019.09.030
  locator: Exact DOI/title and available PMID/PMCID joins
  accessed_at: '2026-10-20T03:38:20.146648Z'
  support: supports
  summary: Exact article identifiers and bibliographic metadata match the cited source.
  snapshot_sha256: a3e49957a48d0ff0d685a5bc8982695c74b53673cbe9d10fbc706024ab787e50
- evidence_id: sheath-native-meta
  kind: database
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6936269.1/PMC6936269.1.json
  locator: Exact DOI/title and available PMID/PMCID joins
  accessed_at: '2026-10-20T03:39:02.669848Z'
  support: supports
  summary: Exact article identifiers and bibliographic metadata match the cited source.
  snapshot_sha256: 3c4ec5e8504f645ea0d0a4d43925a26045c4b84322cff24f4c6119e55c151723
- evidence_id: bridge-doi
  kind: database
  reference: https://api.crossref.org/works/10.1002/cm.21094
  locator: Exact DOI/title and available PMID/PMCID joins
  accessed_at: '2026-10-20T03:41:58.394317Z'
  support: supports
  summary: Exact article identifiers and bibliographic metadata match the cited source.
  snapshot_sha256: 702d09d0f5a5caa853a9c926637db2260447908ab1e6fdfa12ff48c69b370248
- evidence_id: bridge-epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1002/cm.21094&format=json&resultType=core
  locator: Exact DOI/title and available PMID/PMCID joins
  accessed_at: '2026-10-20T03:41:58.165073Z'
  support: supports
  summary: Exact article identifiers and bibliographic metadata match the cited source.
  snapshot_sha256: 99899baa950adcfa150e85483fd760d4addfbe5ff43e56e0aa5eb30f428dafd1
- evidence_id: paper2006
  kind: primary_source
  reference: https://www.researchgate.net/publication/6871150_The_Molecular_Architecture_of_Axonemes_Revealed_by_Cryoelectron_Tomography
  locator: Author-uploaded primary Introduction, Chlamydomonas sections and Figures1/5
  accessed_at: '2026-10-20T03:47:41.783874Z'
  support: supports
  summary: The cited primary text depicts the whole Chlamydomonas9+2 scaffold, supporting
    the species/example claim beyond outer doublets alone.
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/axonemal_microtubule.yaml
  locator: Entire target, all nine edges, discussion and inline history
  accessed_at: '2026-10-20T03:50:06Z'
  support: context_only
  summary: The graph separates subtype from part-of correctly. Two discussion evidence
    notes nevertheless call the doublet and central pair subtypes. Generic microtubule,
    doublet, central-pair and four individual-tubule records exist; no scientific
    review of those additional records is claimed.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/axonemal_microtubule.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-20T03:48:32Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/axonemal_microtubule.yaml'
  snapshot_sha256: 6f4228cd50dbedf75d6a482f87c93cdbf1e224f5eac5e847b6f6f208dd1a002f
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/axonemal_microtubule.yaml
    --out /private/tmp/cellstructure-batch3-20261019-YKo4JU/axonemal_microtubule-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-20T03:48:33Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/axonemal_microtubule.yaml\
    \ --out /private/tmp/cellstructure-batch3-20261019-YKo4JU/axonemal_microtubule-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch3-20261019-YKo4JU/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch3-20261019-YKo4JU/axonemal_microtubule-strict.tsv"
  snapshot_sha256: aa3331a3e26e7de615a898024ea7aa992403eb8afea2008969537d5f32759d1c
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/axonemal_microtubule.yaml; exact collect()
    scope
  accessed_at: '2026-10-20T03:50:06Z'
  support: supports
  summary: All13 collected target identifiers returned OK at the unchanged base. Source-native
    identity checked separately.
  snapshot_sha256: 68d64e4e86437df228658f43be4d47b41054fe882fedf357e660293691a0a061
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
  topic: Generic axonemal filament
  outcome: supported
  target_ids:
  - GO:0005879
  summary: Exact GO identity, definition and FILAMENT kind are appropriate. The source
    definition is used for this generic category, while the experimental scope is
    Chlamydomonas.
  evidence_ids:
  - microtubule-go
  - record
- assessment_id: graph
  area: graph
  topic: All nine topology edges
  outcome: supported
  target_ids:
  - GO:0005879
  summary: Four is-a subtype edges, four membership edges and axoneme parthood exactly
    match GO. The geometry is expressly NONMECHANISTIC.
  evidence_ids:
  - microtubule-go
  - record
- assessment_id: scope
  area: scope
  topic: Whole9+2 example
  outcome: supported
  target_ids:
  - GO:0005879
  summary: The original2006 source covers the whole scaffold;2019 doublet and2013
    central-pair sources support their respective parts. Normal species anatomy supports
    qualitative COMMON without a numeric prevalence claim.
  evidence_ids:
  - paper2006
  - sheath-native-paper
  - bridge-paper
  - sheath-taxon
  - record
- assessment_id: function
  area: evidence
  topic: Structural scaffold
  outcome: supported
  target_ids:
  - GO:0005879
  summary: Formation of the axonemal scaffold is a supported structural role. The
    description remains bounded to A/B and C1/C2 architecture and asserts neither
    an untested regulatory mechanism nor a universal component inventory.
  evidence_ids:
  - sheath-native-paper
  - bridge-paper
  - microtubule-go
  - record
- assessment_id: discussion
  area: consistency
  topic: Assembly versus subtype wording
  outcome: concern
  target_ids:
  - GO:0005879
  summary: The resolved discussion correctly avoids duplicating component detail,
    but its two evidence notes mislabel containing assemblies as subtypes, contrary
    to both current GO ancestry and the graph.
  evidence_ids:
  - microtubule-doublet-ancestors
  - microtubule-pair-ancestors
  - microtubule-go
  - record
- assessment_id: status
  area: completeness
  topic: Native scope and optional surfaces
  outcome: supported
  target_ids:
  - GO:0005879
  summary: The whole-scaffold citation correction is preserved in history. PROPOSED
    status remains appropriate. Component detail is intentionally distributed; no
    protein examples, images, quantitative property or trait claims require extra
    verification.
  evidence_ids:
  - record
findings:
- finding_id: F1
  issue_key: axonemal-microtubule-assembly-subtype-wording
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  title: Discussion notes call containing assemblies microtubule subtypes
  description: The resolved discussion calls GO0097545 an outer-doublet subtype and
    GO0097540 a central-pair subtype. These are containing assemblies, not is_a descendants
    of GO0005879. The actual subtype members are A/B and C1/C2; the graph already
    represents their relations correctly.
  target_ids:
  - GO:0005879
  field_paths:
  - discussions[discussion_id=axonemal_microtubule_child_boundary].evidence[1].notes
  - discussions[discussion_id=axonemal_microtubule_child_boundary].evidence[2].notes
  evidence_ids:
  - microtubule-doublet-ancestors
  - microtubule-pair-ancestors
  - microtubule-go
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/axonemal_microtubule.yaml
    role: maintained scientific record
  rule_id: CURATION:parent_structures is-a versus part_of
  native_severity: minor
  normalization_reason: Misleading prose only; structured relations and exact record
    identity are correct.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0005879
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/axonemal_microtubule.yaml
    role: maintained scientific record
  description: Call the doublet and central pair containing assemblies in the discussion
    evidence notes; preserve the actual A/B/C1/C2 subtype and part-of graph.
  acceptance_checks:
  - The discussion distinguishes assemblies from constituent microtubule subtypes.
  - No structured relation or correct graph edge is changed merely to match the old
    prose.
  - After separately authorized curation, validate the record, history and generated
    pages.
  generator: Maintained YAML owns the prose; just render derives pages.
limitations:
- This generic review does not certify the detailed composition of related records.
- COMMON is qualitative normal anatomy rather than measured population prevalence.
- The2006 primary text was read from an author upload; no browser-text byte hash is
  claimed.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- Only the review bundle is saved. Maintained scientific content, native status, history
  and generated pages remain unchanged.
```
