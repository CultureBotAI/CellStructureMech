# Mating projection membrane identity, anatomy and evidence review

- Review: 20261020T032925Z-mating-projection-membrane-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-19T23:35:57Z
- Finished UTC: 2026-10-20T03:29:25Z
- Reviewer: Codex scientific review agent (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The entire maintained record was assessed. Exact identity, anatomical relations, lipid constituent, conditional yeast example and graph topology are supported. One minor representation issue remains: the sole function row repeats anatomical location and containment without describing a process or activity. No source-access or stable-identifier gap prevents assessment.

## Scope And Provenance

All maintained fields: identity and status, both history surfaces, parthood, component membership/role/essentiality/grounding, conditional distribution, canonical example, function, every evidence item, all three graph nodes and both edges, and the open grounding discussion. Three unique GO identifiers, the sole taxon and sole DOI were individually checked; plasma membrane and tip terms provided additional context.

Selection: First target in the second path-ordered group of previously unreviewed records: data/structures/appendage/mating_projection_membrane.yaml.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0070250 | data/structures/appendage/mating_projection_membrane.yaml | maintained | mating projection membrane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema validation | passed | True | GO:0070250 | Focused LinkML validation returned No issues found. |
| strict validation | passed | True | GO:0070250 | Focused strict validation scanned one file and reported zero ERROR rows. |
| All target identifiers and material claims | passed | True | GO:0070250 | All target GO identifiers, taxon and DOI resolve to the exact entities; full primary text and authority definitions were inspected. Internal graph node references and discussion attachment resolve within the target. Scientific field placement is assessed separately. |
| Verbatim snippet applicability | not_applicable | False | GO:0070250 | No snippet fields are present. |
| Expression and protein adapter applicability | not_applicable | False | GO:0070250 | The record has no UniProt accession or expression dataset. Spa2 is a cited localization marker, directly checked in the microscopy source; expression-module membership would not establish that claim. |
| Target identifier coverage and resolver residuals | passed | True | GO:0070250 | Exact collected identifiers are resolved by shared report and scoped authority/local receipts; remaining scientific correctness is assessed separately. |
| Full corpus QC | passed | True | GO:0070250 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0070250 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0070250 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0070250 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0070250 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Exact membrane identity and definition

identity: supported. Targets: GO:0070250.

The label, shortened definition, MEMBRANE kind and APPENDAGE category denote the same membrane region as the exact GO term. The record does not conflate the membrane with its enclosing whole projection.

### Projection parthood and tip membrane containment

grounding: supported. Targets: GO:0070250.

Both explicit mereological fields and the relevant sibling relationships match current GO children relations. Missing optional is-a or synonym fields are not a consequential gap.

### Constituent lipid bilayer and essentiality

completeness: supported. Targets: GO:0070250.

A lipid bilayer is constitutive of this plasma-membrane domain. ESSENTIAL is defensible as necessary composition, without implying a measured gene-deletion phenotype. No fixed lipid composition or stoichiometry is asserted.

### Label-only constituent and open discussion

grounding: supported. Targets: GO:0070250.

The record distinguishes the local bilayer constituent from the whole membrane GO term, gives the role and source, and records a specific open grounding task. The statement that no separate CURIE was verified is a bounded curation note, not proof that no such term exists.

### Conditional distribution and canonical example

scope: supported. Targets: GO:0070250.

The species identity and experimental context support VARIABLE presence and the yeast example. Spa2-positive tip wording remains a localization observation; it is not used to assign Spa2 as a membrane constituent.

### Anatomy represented as a function

representation: concern. Targets: GO:0070250.

The only function row repeats where the membrane lies and the tip domain it contains. Those statements are supported anatomy but do not describe a process or activity as the native function slot requires.

### Three nodes and two topological edges

graph: supported. Targets: GO:0070250.

Node identifiers, direction, surrounds and part-of predicates, descriptions and nearest evidence agree. NONMECHANISTIC scope explicitly avoids unsupported signaling, actin or secretion causality.

### Claim-level citations and source identity

evidence: supported. Targets: GO:0070250.

All cited references were checked in source-native material, and paper title/DOI match. GO supports the identity/topology claims while Read supports the stated cellular context. There are no uncited numerical measurements or source quotations.

### Properties, images, traits and datasets

completeness: not_applicable. Targets: GO:0070250.

No measurement, image, licence, dataset or trait link is asserted. Such optional fields and an exhaustive molecular inventory are not required to review this anatomically bounded record.

### Status, histories and ownership

provenance: supported. Targets: GO:0070250.

Both history surfaces identify this target; agent-authored mapping status remains PROPOSED. The maintained YAML owns any future scientific correction.

## Findings

### F1: The function row restates membrane anatomy

minor / open / confirmed; issue key: mating-projection-membrane-anatomy-as-function.

The function description says the membrane bounds the projection and contains the tip membrane. It does not identify a biological process or activity, as required by the native functions and StructureFunction descriptions. The same content is already represented by the definition, parthood fields and topology graph. Its cited anatomy is sound; the defect is semantic placement and redundancy.

## Recommended Actions And Acceptance Checks

### A1

In separately authorized curation, remove the redundant function row while retaining its anatomy in definition/parthood/graph, or replace it with a specifically sourced biological role of the membrane in the stated context. Do not infer a membrane mechanism from Spa2 localization.

- Every retained function describes a process or activity with evidence supporting that role, not only location or containment.
- For any scientific edit, use write_validated_structure, append the required curation and repository history, and run focused validate and validate-strict plus documented corpus gates.
- Regenerate pages with just render only as part of separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/mating_projection_membrane.yaml; Entire maintained YAML | context_only | The target contains one lipid constituent, one taxonomic row, one example, one function and a nonmechanistic three-node/two-edge graph. The discussion explicitly leaves constituent grounding label-only. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0070250%2CGO%3A0070867%2CGO%3A0005937%2CGO%3A0043332%2CGO%3A0005886; All five returned terms: id/name/aspect/isObsolete/definition, relevant children relations and synonyms | supports | All three target GO identifiers are current cellular components. GO distinguishes the projection, its membrane and its tip membrane, with the recorded parthood relations. The additional tip definition identifies the growth apex; the plasma membrane definition specifies a phospholipid bilayer with associated proteins. |
| taxonomy | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=4932; TaxaSet/Taxon TaxId, ScientificName and Rank | supports | NCBITaxon:4932 is the species Saccharomyces cerevisiae, matching both labels. |
| read-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1091/mbc.3.4.429&amp;format=json&amp;resultType=core; Core result DOI, title, authors, journal, year, PMID1498363 and PMC275593 | supports | The sole DOI resolves to the correctly named Read, Okamura and Drubin 1992 Molecular Biology of the Cell paper. Bibliographic identity was checked independently of source-body claims. |
| read-fulltext | https://europepmc.org/articles/PMC275593?pdf=render; DOI:10.1091/mbc.3.4.429; pp.429-432 Introduction/Table1/Methods/Results, p.436 Results, Figure7 and legend p.442; official PDF and extracted text | supports | Haploid Saccharomyces strains develop projections after pheromone stimulation. Methods distinguish arrest without projections from induction of outgrowth. The authors report Spa2p at the tip in 93% of scored wild-type projection-bearing cells; Figure7 compares localization in wild type and actin mutants. The local membrane identity is supplied by GO rather than a membrane-specific assay in this paper. |
| figure7 | https://europepmc.org/articles/PMC275593?pdf=render; Figure7 p.442; rendered official PDF page14 inspected visually | supports | The microscopy, bar-graph legend and caption match the source text and identify the phenotyped projection-bearing population. This supports the modest Spa2-positive-tip statement without generalizing localization to every cell state. |
| history | history/records/mating_projection_membrane/2026-09-30T055734Z-codex-00e17f.yaml; Entire CREATE event and target curation_history | context_only | History identifies this maintained target, its GO identity, topology and explicit label-only curation task. Mapping status remains PROPOSED. |
| siblings | data/structures/; Projection, tip membrane and tip records; exact paths and hashes in source.inputs | context_only | The related records distinguish whole projection, tip region, surrounding membrane and tip membrane. This context check does not review every assertion in those separate records. |
| function-schema | src/cellstructuremech/schema/cellstructuremech.yaml; CellStructureRecord.functions and StructureFunction descriptions | supports | The native schema defines function rows as biological processes or molecular functions carried out by the structure, and StructureFunction as a process or activity. A location/containment restatement does not supply that information. |
| schema-result | UV_CACHE_DIR=/private/tmp/cellstructure-record-reviews-UhRFh7/uv-cache just validate data/structures/appendage/mating_projection_membrane.yaml; External diagnostic log and actual process exit code 0 | supports | Focused LinkML validation returned No issues found. |
| strict-result | UV_CACHE_DIR=/private/tmp/cellstructure-record-reviews-UhRFh7/uv-cache just validate-strict data/structures/appendage/mating_projection_membrane.yaml --out /private/tmp/cellstructure-batch2-20261019-52rdp0/mating-projection-membrane/strict.tsv; External diagnostic log and actual process exit code 0 | supports | Focused strict validation scanned one file and reported zero ERROR rows. |
| target-resolver-coverage | just check-curies-strict; data/structures/appendage/mating_projection_membrane.yaml; scripts/check_curies.py collect(); shared reports/curie_check.tsv | supports | Exact target collection has 5 distinct CURIE-shaped scalars: {'OK': 5}. Every collected identifier is OK in the shared report. HTTP URLs and prose are outside collect(); separate source audit covers their claims. Identifier existence is distinct from biological correctness. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- The lipid-bilayer assignment is a constitutive membrane description, not a specific lipid composition, measured stoichiometry or mutant essentiality experiment. The acknowledged label-only grounding is retained as an explicit curation uncertainty.
- Read 1992 supports the pheromone-conditioned budding-yeast example and tip localization; GO supplies membrane identity and parthood. Neither source is used to assert an exhaustive membrane proteome or cross-fungal prevalence.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The user authorized a review bundle for every inspected target, including clean observations, overriding the repository issue-only persistence gate.
- No maintained scientific record, generated page, history or external shared content was changed. Parent coordination supplies actual shared native-check receipts before persistence.
- The official Europe PMC PDF was retrieved by a collaborating reviewer at 2026-10-19T07:44:14Z and locally reinspected for this review. No verbatim source quotations are reproduced.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T032925Z-mating-projection-membrane-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Mating projection membrane identity, anatomy and evidence review
started_at: '2026-10-19T23:35:57Z'
finished_at: '2026-10-20T03:29:25Z'
reviewer:
  identity: Codex scientific review agent
  kind: agent
  independence: unknown
  independence_basis: The review was performed by a separate agent, but historical
    authorship also names Codex; independence from that authorship is not asserted.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'The entire maintained record was assessed. Exact identity, anatomical relations,
  lipid constituent, conditional yeast example and graph topology are supported. One
  minor representation issue remains: the sole function row repeats anatomical location
  and containment without describing a process or activity. No source-access or stable-identifier
  gap prevents assessment.'
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
  - path: AGENTS.md
    sha256: ed0004703d4f76d2677e3fdf67aa39ef9a6c2c35ef2b51ec053fbaed9ba1ac86
    role: context
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: conf/record_review.yaml
    sha256: d3334a12b8a616a7638f1195748085d2b543fba7df67ad4ff8fcc0ac18f2d3ee
    role: context
  - path: data/structures/appendage/mating_projection.yaml
    sha256: bab39726b1ad7003dbf3f66e8d48d088365fac303dcbfeef0aae4009b26cc1b0
    role: context
  - path: data/structures/appendage/mating_projection_membrane.yaml
    sha256: d1ed93a7c920c648dbb7ae5967579738c66ac620fa3f16513d465d18d75fd473
    role: target
  - path: data/structures/appendage/mating_projection_tip_membrane.yaml
    sha256: 1159bcac347712f9a6a55778fe897892dfb90edb6affc5dc44cffbb348352286
    role: context
  - path: data/structures/other/mating_projection_tip.yaml
    sha256: ec2a7085e4d50080981c50bd9b523d8ffabf4de5739bbe1b696c382fddb7e1ad
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
  - path: history/records/mating_projection_membrane/2026-09-30T055734Z-codex-00e17f.yaml
    sha256: be88c5fbe86c7b1ff39738eeb2fb9bb20bb347697640acd01c86129f1f497353
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
- target_id: GO:0070250
  path: data/structures/appendage/mating_projection_membrane.yaml
  label: mating projection membrane
  record_class: CellStructureRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/mating_projection_membrane.yaml
    role: maintained scientific record
scope:
  description: 'All maintained fields: identity and status, both history surfaces,
    parthood, component membership/role/essentiality/grounding, conditional distribution,
    canonical example, function, every evidence item, all three graph nodes and both
    edges, and the open grounding discussion. Three unique GO identifiers, the sole
    taxon and sole DOI were individually checked; plasma membrane and tip terms provided
    additional context.'
  selection: 'First target in the second path-ordered group of previously unreviewed
    records: data/structures/appendage/mating_projection_membrane.yaml.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0070250
checks:
- check_id: schema
  name: schema validation
  status: passed
  required: true
  summary: Focused LinkML validation returned No issues found.
  target_ids:
  - GO:0070250
  command: UV_CACHE_DIR=/private/tmp/cellstructure-record-reviews-UhRFh7/uv-cache
    just validate data/structures/appendage/mating_projection_membrane.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - schema-result
- check_id: strict
  name: strict validation
  status: passed
  required: true
  summary: Focused strict validation scanned one file and reported zero ERROR rows.
  target_ids:
  - GO:0070250
  command: UV_CACHE_DIR=/private/tmp/cellstructure-record-reviews-UhRFh7/uv-cache
    just validate-strict data/structures/appendage/mating_projection_membrane.yaml
    --out /private/tmp/cellstructure-batch2-20261019-52rdp0/mating-projection-membrane/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - strict-result
- check_id: source-inspection
  name: All target identifiers and material claims
  status: passed
  required: true
  summary: All target GO identifiers, taxon and DOI resolve to the exact entities;
    full primary text and authority definitions were inspected. Internal graph node
    references and discussion attachment resolve within the target. Scientific field
    placement is assessed separately.
  target_ids:
  - GO:0070250
  evidence_ids:
  - record
  - go
  - taxonomy
  - read-metadata
  - read-fulltext
  - figure7
- check_id: snippet-audit
  name: Verbatim snippet applicability
  status: not_applicable
  required: false
  summary: No snippet fields are present.
  target_ids:
  - GO:0070250
  evidence_ids:
  - record
- check_id: expression-adapters
  name: Expression and protein adapter applicability
  status: not_applicable
  required: false
  summary: The record has no UniProt accession or expression dataset. Spa2 is a cited
    localization marker, directly checked in the microscopy source; expression-module
    membership would not establish that claim.
  target_ids:
  - GO:0070250
  evidence_ids:
  - record
  - read-fulltext
- check_id: target-resolver-coverage
  name: Target identifier coverage and resolver residuals
  status: passed
  required: true
  target_ids:
  - GO:0070250
  summary: Exact collected identifiers are resolved by shared report and scoped authority/local
    receipts; remaining scientific correctness is assessed separately.
  evidence_ids:
  - target-resolver-coverage
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0070250
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch2 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0070250
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch2 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0070250
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch2 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0070250
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch2 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0070250
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch2 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/appendage/mating_projection_membrane.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-19T23:37:42Z'
  support: context_only
  summary: The target contains one lipid constituent, one taxonomic row, one example,
    one function and a nonmechanistic three-node/two-edge graph. The discussion explicitly
    leaves constituent grounding label-only.
  snapshot_sha256: d1ed93a7c920c648dbb7ae5967579738c66ac620fa3f16513d465d18d75fd473
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0070250%2CGO%3A0070867%2CGO%3A0005937%2CGO%3A0043332%2CGO%3A0005886
  locator: 'All five returned terms: id/name/aspect/isObsolete/definition, relevant
    children relations and synonyms'
  accessed_at: '2026-10-19T23:37:13Z'
  support: supports
  summary: All three target GO identifiers are current cellular components. GO distinguishes
    the projection, its membrane and its tip membrane, with the recorded parthood
    relations. The additional tip definition identifies the growth apex; the plasma
    membrane definition specifies a phospholipid bilayer with associated proteins.
  snapshot_sha256: 553defa009fe0e96514164474837e8898231301a5303a350379afc7bc62e1d0f
- evidence_id: taxonomy
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=4932
  locator: TaxaSet/Taxon TaxId, ScientificName and Rank
  accessed_at: '2026-10-19T23:37:13Z'
  support: supports
  summary: NCBITaxon:4932 is the species Saccharomyces cerevisiae, matching both labels.
  snapshot_sha256: da089959ea98b54a0b26b43b88037705e7aed37e969e5c789267f92803002124
- evidence_id: read-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1091/mbc.3.4.429&format=json&resultType=core
  locator: Core result DOI, title, authors, journal, year, PMID1498363 and PMC275593
  accessed_at: '2026-10-19T23:37:13Z'
  support: supports
  summary: The sole DOI resolves to the correctly named Read, Okamura and Drubin 1992
    Molecular Biology of the Cell paper. Bibliographic identity was checked independently
    of source-body claims.
  snapshot_sha256: d1443582a49421da985aa245313d4519ee5505270f7e45e5d47fa365f24943bf
- evidence_id: read-fulltext
  kind: primary_source
  reference: https://europepmc.org/articles/PMC275593?pdf=render
  locator: DOI:10.1091/mbc.3.4.429; pp.429-432 Introduction/Table1/Methods/Results,
    p.436 Results, Figure7 and legend p.442; official PDF and extracted text
  accessed_at: '2026-10-19T23:37:42Z'
  support: supports
  summary: Haploid Saccharomyces strains develop projections after pheromone stimulation.
    Methods distinguish arrest without projections from induction of outgrowth. The
    authors report Spa2p at the tip in 93% of scored wild-type projection-bearing
    cells; Figure7 compares localization in wild type and actin mutants. The local
    membrane identity is supplied by GO rather than a membrane-specific assay in this
    paper.
  snapshot_sha256: 63d19679ef508f4c22b3a6a6428f2d78e1eefa32016310daac96f7753dc60377
- evidence_id: figure7
  kind: primary_source
  reference: https://europepmc.org/articles/PMC275593?pdf=render
  locator: Figure7 p.442; rendered official PDF page14 inspected visually
  accessed_at: '2026-10-19T23:37:42Z'
  support: supports
  summary: The microscopy, bar-graph legend and caption match the source text and
    identify the phenotyped projection-bearing population. This supports the modest
    Spa2-positive-tip statement without generalizing localization to every cell state.
  snapshot_sha256: fb4d1434d2cb69ff0cc08e2031b087d9fa2596b8b3cd6ec898e98374b5f6cb43
- evidence_id: history
  kind: record_content
  reference: history/records/mating_projection_membrane/2026-09-30T055734Z-codex-00e17f.yaml
  locator: Entire CREATE event and target curation_history
  accessed_at: '2026-10-19T23:37:42Z'
  support: context_only
  summary: History identifies this maintained target, its GO identity, topology and
    explicit label-only curation task. Mapping status remains PROPOSED.
- evidence_id: siblings
  kind: record_content
  reference: data/structures/
  locator: Projection, tip membrane and tip records; exact paths and hashes in source.inputs
  accessed_at: '2026-10-19T23:37:13Z'
  support: context_only
  summary: The related records distinguish whole projection, tip region, surrounding
    membrane and tip membrane. This context check does not review every assertion
    in those separate records.
- evidence_id: function-schema
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: CellStructureRecord.functions and StructureFunction descriptions
  accessed_at: '2026-10-19T23:37:25Z'
  support: supports
  summary: The native schema defines function rows as biological processes or molecular
    functions carried out by the structure, and StructureFunction as a process or
    activity. A location/containment restatement does not supply that information.
- evidence_id: schema-result
  kind: validation
  reference: UV_CACHE_DIR=/private/tmp/cellstructure-record-reviews-UhRFh7/uv-cache
    just validate data/structures/appendage/mating_projection_membrane.yaml
  locator: External diagnostic log and actual process exit code 0
  accessed_at: '2026-10-19T23:37:25Z'
  support: supports
  summary: Focused LinkML validation returned No issues found.
  snapshot_sha256: 969e8d652a028b460a24bc7c85c315eff0c2c396b55077afcf9df1dd5f79bbc6
- evidence_id: strict-result
  kind: validation
  reference: UV_CACHE_DIR=/private/tmp/cellstructure-record-reviews-UhRFh7/uv-cache
    just validate-strict data/structures/appendage/mating_projection_membrane.yaml
    --out /private/tmp/cellstructure-batch2-20261019-52rdp0/mating-projection-membrane/strict.tsv
  locator: External diagnostic log and actual process exit code 0
  accessed_at: '2026-10-19T23:37:25Z'
  support: supports
  summary: Focused strict validation scanned one file and reported zero ERROR rows.
  snapshot_sha256: 9d3595d91164b7ac11d457d55aab17f106adc1b514935c5af6fc28c3eee839ef
- evidence_id: target-resolver-coverage
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/appendage/mating_projection_membrane.yaml; scripts/check_curies.py
    collect(); shared reports/curie_check.tsv
  accessed_at: '2026-10-19T23:41:41.324461Z'
  support: supports
  snapshot_sha256: 68d64e4e86437df228658f43be4d47b41054fe882fedf357e660293691a0a061
  summary: 'Exact target collection has 5 distinct CURIE-shaped scalars: {''OK'':
    5}. Every collected identifier is OK in the shared report. HTTP URLs and prose
    are outside collect(); separate source audit covers their claims. Identifier existence
    is distinct from biological correctness.'
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
  topic: Exact membrane identity and definition
  outcome: supported
  summary: The label, shortened definition, MEMBRANE kind and APPENDAGE category denote
    the same membrane region as the exact GO term. The record does not conflate the
    membrane with its enclosing whole projection.
  target_ids:
  - GO:0070250
  evidence_ids:
  - record
  - go
- assessment_id: hierarchy
  area: grounding
  topic: Projection parthood and tip membrane containment
  outcome: supported
  summary: Both explicit mereological fields and the relevant sibling relationships
    match current GO children relations. Missing optional is-a or synonym fields are
    not a consequential gap.
  target_ids:
  - GO:0070250
  evidence_ids:
  - record
  - go
  - siblings
- assessment_id: component
  area: completeness
  topic: Constituent lipid bilayer and essentiality
  outcome: supported
  summary: A lipid bilayer is constitutive of this plasma-membrane domain. ESSENTIAL
    is defensible as necessary composition, without implying a measured gene-deletion
    phenotype. No fixed lipid composition or stoichiometry is asserted.
  target_ids:
  - GO:0070250
  evidence_ids:
  - record
  - go
- assessment_id: component-grounding
  area: grounding
  topic: Label-only constituent and open discussion
  outcome: supported
  summary: The record distinguishes the local bilayer constituent from the whole membrane
    GO term, gives the role and source, and records a specific open grounding task.
    The statement that no separate CURIE was verified is a bounded curation note,
    not proof that no such term exists.
  target_ids:
  - GO:0070250
  evidence_ids:
  - record
  - go
- assessment_id: scope
  area: scope
  topic: Conditional distribution and canonical example
  outcome: supported
  summary: The species identity and experimental context support VARIABLE presence
    and the yeast example. Spa2-positive tip wording remains a localization observation;
    it is not used to assign Spa2 as a membrane constituent.
  target_ids:
  - GO:0070250
  evidence_ids:
  - taxonomy
  - read-fulltext
  - figure7
  - go
  dimensions:
  - name: organism_and_state
    value: Saccharomyces cerevisiae; haploid, pheromone-induced projection-bearing
      cells
    definition: Conditions of the cited example rather than an all-state or all-fungal
      frequency estimate.
    evidence_ids:
    - taxonomy
    - read-fulltext
  - name: evidence_scale
    value: Authority anatomy with experimental morphology and immunofluorescence
    definition: Ontology definitions supply membrane identity; the source study supplies
      the conditional cellular example.
    evidence_ids:
    - go
    - read-fulltext
    - figure7
- assessment_id: function
  area: representation
  topic: Anatomy represented as a function
  outcome: concern
  summary: The only function row repeats where the membrane lies and the tip domain
    it contains. Those statements are supported anatomy but do not describe a process
    or activity as the native function slot requires.
  target_ids:
  - GO:0070250
  evidence_ids:
  - record
  - go
  - function-schema
- assessment_id: graph
  area: graph
  topic: Three nodes and two topological edges
  outcome: supported
  summary: Node identifiers, direction, surrounds and part-of predicates, descriptions
    and nearest evidence agree. NONMECHANISTIC scope explicitly avoids unsupported
    signaling, actin or secretion causality.
  target_ids:
  - GO:0070250
  evidence_ids:
  - record
  - go
- assessment_id: evidence
  area: evidence
  topic: Claim-level citations and source identity
  outcome: supported
  summary: All cited references were checked in source-native material, and paper
    title/DOI match. GO supports the identity/topology claims while Read supports
    the stated cellular context. There are no uncited numerical measurements or source
    quotations.
  target_ids:
  - GO:0070250
  evidence_ids:
  - record
  - go
  - read-metadata
  - read-fulltext
- assessment_id: optional
  area: completeness
  topic: Properties, images, traits and datasets
  outcome: not_applicable
  summary: No measurement, image, licence, dataset or trait link is asserted. Such
    optional fields and an exhaustive molecular inventory are not required to review
    this anatomically bounded record.
  target_ids:
  - GO:0070250
  evidence_ids:
  - record
- assessment_id: provenance
  area: provenance
  topic: Status, histories and ownership
  outcome: supported
  summary: Both history surfaces identify this target; agent-authored mapping status
    remains PROPOSED. The maintained YAML owns any future scientific correction.
  target_ids:
  - GO:0070250
  evidence_ids:
  - record
  - history
findings:
- finding_id: F1
  issue_key: mating-projection-membrane-anatomy-as-function
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: The function row restates membrane anatomy
  description: The function description says the membrane bounds the projection and
    contains the tip membrane. It does not identify a biological process or activity,
    as required by the native functions and StructureFunction descriptions. The same
    content is already represented by the definition, parthood fields and topology
    graph. Its cited anatomy is sound; the defect is semantic placement and redundancy.
  target_ids:
  - GO:0070250
  field_paths:
  - functions[function_id=mating_projection_membrane_boundary]
  evidence_ids:
  - record
  - go
  - function-schema
  rule_id: cellstructuremech-schema/StructureFunction+review-checklist/functions-traits
  native_severity: minor
  normalization_reason: This is a nonblocking field-semantics and redundancy issue.
    It does not change the structure identity or invalidate the supported anatomical
    relationships.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/mating_projection_membrane.yaml
    role: maintained scientific record
actions:
- action_id: A1
  description: In separately authorized curation, remove the redundant function row
    while retaining its anatomy in definition/parthood/graph, or replace it with a
    specifically sourced biological role of the membrane in the stated context. Do
    not infer a membrane mechanism from Spa2 localization.
  finding_ids:
  - F1
  target_ids:
  - GO:0070250
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/mating_projection_membrane.yaml
    role: maintained scientific record
  acceptance_checks:
  - Every retained function describes a process or activity with evidence supporting
    that role, not only location or containment.
  - For any scientific edit, use write_validated_structure, append the required curation
    and repository history, and run focused validate and validate-strict plus documented
    corpus gates.
  - Regenerate pages with just render only as part of separately authorized curation.
  generator: The maintained YAML owns the scientific assertion; generated pages are
    derived by just render.
limitations:
- The lipid-bilayer assignment is a constitutive membrane description, not a specific
  lipid composition, measured stoichiometry or mutant essentiality experiment. The
  acknowledged label-only grounding is retained as an explicit curation uncertainty.
- Read 1992 supports the pheromone-conditioned budding-yeast example and tip localization;
  GO supplies membrane identity and parthood. Neither source is used to assert an
  exhaustive membrane proteome or cross-fungal prevalence.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- The user authorized a review bundle for every inspected target, including clean
  observations, overriding the repository issue-only persistence gate.
- No maintained scientific record, generated page, history or external shared content
  was changed. Parent coordination supplies actual shared native-check receipts before
  persistence.
- The official Europe PMC PDF was retrieved by a collaborating reviewer at 2026-10-19T07:44:14Z
  and locally reinspected for this review. No verbatim source quotations are reproduced.
```
