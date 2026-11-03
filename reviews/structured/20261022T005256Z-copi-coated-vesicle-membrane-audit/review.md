# COPI structure identity, boundaries and source review

- Review: 20261022T005256Z-copi-coated-vesicle-membrane-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T11:11:23Z
- Finished UTC: 2026-10-22T00:52:56Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The maintained COPI membrane identity, collective bilayer and descriptive topology are supported within the declared source scopes. No concrete curation finding was established.

## Scope And Provenance

Entire single maintained record with exact identity, source-native taxonomy, primary claim support, hierarchy, material/formation boundaries and every graph edge.

Selection: Target 8 in batch twenty-four, selected by native uncovered path order at frozen fresh-main revision.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0030663 | data/structures/membrane_organelle/copi_coated_vesicle_membrane.yaml | maintained | COPI-coated vesicle membrane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0030663 | Focused validator passed. |
| Focused native strict | passed | True | GO:0030663 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0030663 | 9 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Protein-identifier verification applicability | not_applicable | False | GO:0030663 | The target has no UniProt protein examples, declared gene symbols or GENE_OR_PROTEIN graph nodes. Neighbor protein identities were not promoted to target assertions. |
| Expression-module applicability | not_applicable | False | GO:0030663 | No expression-module, regulator or transcriptomic assertion is made by this structural record review. |
| Claim-level scientific review | passed | True | GO:0030663 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0030663 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0030663 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0030663 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0030663 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0030663 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Whole-vesicle, membrane and lumen boundaries

identity: supported. Targets: GO:0030663.

The maintained target denotes the stated cellular structure or region, distinct from a coatomer protein complex. Its parent/parthood relationships preserve the whole-versus-part distinction. Generic GO descriptions are used only at the level they denote. The heterogeneous cargos and lower-level coat constituents are not relabeled as this target.

### Yeast occurrence and model context

scope: supported. Targets: GO:0030663.

The maintained Saccharomyces scope and canonical example are supported by the inspected Sandmann yeast mutant, binding and vesicle-assay contexts. COMMON is treated as qualitative occurrence, not a numerical cell prevalence. The canonical statement is broad early-secretory/COPI context; it does not assign a particular strain, purification or quantitative result not given in the record. Lumen/membrane occurrence is the structural implication of these membrane-bounded COPI vesicles together with their native location definitions, not a separately measured organelle frequency.

### Collective bilayer constituent

grounding: supported. Targets: GO:0030663.

GO0030663 denotes the whole membrane and directly defines it as the surrounding lipid bilayer. The direct LIPID row denotes that collective material; its label-only grounding avoids treating a location term as a molecular lipid species. The graph component_ref is appropriate for the membrane defined as this bilayer. Coat proteins remain represented on the coat/whole-vesicle records; no molecular inventory is demanded here.

### Specific lipid requirements remain untested

grounding: unknown. Targets: GO:0030663.

The ESSENTIAL row applies to collective bilayer material constituting this membrane. The record does not name individual lipid species whose deletion or replacement necessity could be inferred; neither the ontology definition nor the inspected vesicle assays establish those individual formation requirements. This distinction supplies an uncertainty boundary, not a finding against the collective material statement.

### Descriptive topology at the maintained scope

graph: supported. Targets: GO:0030663.

The three NONMECHANISTIC edges express membrane parthood/boundary and donation from Golgi membrane. GO0030663 and GO0035964 directly support these topological/process descriptions. The graph does not elevate the coat to a lipid species or claim a complete assembly mechanism.

### Bounded whole-record coverage

completeness: supported. Targets: GO:0030663.

All maintained fields, assertions, evidence notes and graph edges were read; cited sources were assessed at the precise scopes recorded. Empty optional function, trait, image, property or molecular-inventory slots do not establish defects. No snippet is present to repair, and no historical search or status promotion is certified.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/copi_coated_vesicle_membrane.yaml; Entire maintained YAML including every definition, history, claim, citation, graph edge and discussion | context_only | All maintained fields were read before assessment. No status promotion or scientific edit is made. |
| policy | docs/CURATION.md; Identifiers and exact definition matching; evidence at claim scope; component grounding | context_only | Exact identity depends on definitions, not labels alone. A structural part, molecular constituent and experimental formation requirement are distinct. |
| neighbor-copi_coated_vesicle | data/structures/membrane_organelle/copi_coated_vesicle.yaml; Entire neighboring COPI record | context_only | Boundary-only context confirms the distinction between whole vesicle, structural coat, lipid membrane and enclosed lumen. Other claims in this neighbor are not an additional review target. |
| neighbor-copi_coated_vesicle_lumen | data/structures/membrane_organelle/copi_coated_vesicle_lumen.yaml; Entire neighboring COPI record | context_only | Boundary-only context confirms the distinction between whole vesicle, structural coat, lipid membrane and enclosed lumen. Other claims in this neighbor are not an additional review target. |
| neighbor-copi_vesicle_coat | data/structures/other/copi_vesicle_coat.yaml; Identifier, definition, parent/parthood and constituent labels/roles only | context_only | Boundary-only context confirms the distinction between whole vesicle, structural coat, lipid membrane and enclosed lumen. Other claims in this neighbor are not an additional review target. |
| copi-membrane-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030137,GO:0005798,GO:0030135,GO:0030126,GO:0030663,GO:0006890,GO:0035964,GO:0000139,GO:0005783,GO:0060205,GO:0030660,GO:0030662; All twelve returned terms: identifiers, names, definitions, active status, synonyms and relevant is_a/part_of children | supports | The twelve returned active GO terms were read. Their exact definitions and explicit parent-child relations support the declared whole-vesicle, membrane, coat, Golgi, ER and transport boundaries. Coatomer is only related to the whole vesicle but exact for the coat; GO0030663 has the exact unhyphenated membrane synonym. GO0060205 denotes enclosed volume. The newly observed GO0106172 candidate is evaluated separately for the lumen. |
| copi-membrane-agent-NCBITaxon-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Exact taxId, scientificName, rank and lineage | supports | ENA identifies NCBITaxon4932 as Saccharomyces cerevisiae at species rank. This row attests only that species identity, not experimental strain or prevalence. |
| copi-membrane-agent-sandmann2003-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1091%2Fmbc.e02-11-0736; Exact bibliographic fields and complete returned abstract | supports | Native MED identifies Suppression of coatomer mutants by a new protein family with COPI and COPII binding motifs in Saccharomyces cerevisiae. (Sandmann T, Herrmann JM, Dengjel J, Schwarz H, Spang A., 2003), PMID12925749, DOI10.1091/mbc.e02-11-0736. Exact citation and complete abstract were read; body access and reading are described separately. |
| copi-membrane-agent-sandmann2003-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC181553/; Complete Introduction sec1; Methods sec3 including Table1, sec7 protein-binding assay and sec14 budding assay; complete Results sec16 and sec20–23 including Figures1 and5–7 captions; complete Discussion sec25. Other Results/Methods, image pixels and raw data were not reanalysed. | supports | The primary yeast study reports sec21/alpha-COP mutant suppression, KKXX-dependent coatomer binding, and vesicle production from semi-intact cells and enriched Golgi membranes. It distinguishes mixed-cytosol assays that cannot separate COPI/COPII from purified-coat assays and explicitly qualifies mechanistic interpretations. The strain table identifies yeast experimental backgrounds; no population frequency or universal formation requirement is inferred. |
| copi-membrane-agent-sandmann2003-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC181553/fullTextXML; Actual failed XML access response only | context_only | This XML route returned HTTP500 and supplied no scientific body. The separately recovered genuine PMC HTML supplied the readable primary sections. |
| copi-membrane-agent-sandmann2003-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC181553.1/PMC181553.1.xml; Actual failed XML access response only | context_only | This XML route returned HTTP404 and supplied no scientific body. The separately recovered genuine PMC HTML supplied the readable primary sections. |
| schema-result | just validate data/structures/membrane_organelle/copi_coated_vesicle_membrane.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/copi_coated_vesicle_membrane.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/copi_coated_vesicle_membrane.yaml --out /private/tmp/cellstructure-batch24-20261021-qayobm82/copi_coated_vesicle_membrane-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/copi_coated_vesicle_membrane.yaml --out /private/tmp/cellstructure-batch24-20261021-qayobm82/copi_coated_vesicle_membrane-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch24-20261021-qayobm82/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch24-20261021-qayobm82/copi_coated_vesicle_membrane-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/copi_coated_vesicle_membrane.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 9 of9 collected target identifiers returned OK in this fresh base resolver run. Residuals: none. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Sandmann was read in the explicitly named primary sections, not the entire paper or image pixels; neither raw microscopy nor vesicle-assay data were reanalysed. Yeast experimental contexts do not establish quantitative population prevalence.
- Neighbor records are boundary context only; their other claims are not additional review targets. No exhaustive molecular-family or chemical ontology absence is asserted.
- Global checks from the unchanged fresh base are integrated by the parent at finalization; deterministic success does not independently establish scientific support.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The explicit user goal authorizes an honest review bundle for each uncovered target, including clean reviews; no finding is invented to satisfy the local issue-only gate.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T005256Z-copi-coated-vesicle-membrane-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: COPI structure identity, boundaries and source review
started_at: '2026-10-21T11:11:23Z'
finished_at: '2026-10-22T00:52:56Z'
reviewer:
  identity: Codex
  kind: agent
  independence: unknown
  independence_basis: Current source review does not establish independent historical
    authorship.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The maintained COPI membrane identity, collective bilayer and descriptive
  topology are supported within the declared source scopes. No concrete curation finding
  was established.
source:
  git_revision: 9c0446c4c0dd4b458787c43a499e4ceab5e179a6
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
  - path: data/structures/membrane_organelle/copi_coated_vesicle.yaml
    sha256: c8cf402aeadf4fea155d4735ed1df973e319b23d46664cd7ec286ba385c1a250
    role: context
  - path: data/structures/membrane_organelle/copi_coated_vesicle_lumen.yaml
    sha256: f4da3395ba3aa5bfa65d859069e5b2f5d15303f81d7da6048291813188d9bcfa
    role: context
  - path: data/structures/membrane_organelle/copi_coated_vesicle_membrane.yaml
    sha256: 70dbc868044797a3911de45524d13ccbedb5bf9cc671824b0dcade909ab4922f
    role: target
  - path: data/structures/other/copi_vesicle_coat.yaml
    sha256: 1b264ad3800f2c5c8c78d327f63a32bdc73888a003e3be3fcad778bb9f993195
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
- target_id: GO:0030663
  path: data/structures/membrane_organelle/copi_coated_vesicle_membrane.yaml
  label: COPI-coated vesicle membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/copi_coated_vesicle_membrane.yaml
    role: maintained scientific record
scope:
  description: Entire single maintained record with exact identity, source-native
    taxonomy, primary claim support, hierarchy, material/formation boundaries and
    every graph edge.
  selection: Target 8 in batch twenty-four, selected by native uncovered path order
    at frozen fresh-main revision.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0030663
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0030663
  command: just validate data/structures/membrane_organelle/copi_coated_vesicle_membrane.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0030663
  command: just validate-strict data/structures/membrane_organelle/copi_coated_vesicle_membrane.yaml
    --out /private/tmp/cellstructure-batch24-20261021-qayobm82/copi_coated_vesicle_membrane-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0030663
  summary: 9 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: protein-identifiers
  name: Protein-identifier verification applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0030663
  summary: The target has no UniProt protein examples, declared gene symbols or GENE_OR_PROTEIN
    graph nodes. Neighbor protein identities were not promoted to target assertions.
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0030663
  summary: No expression-module, regulator or transcriptomic assertion is made by
    this structural record review.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0030663
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - neighbor-copi_coated_vesicle
  - neighbor-copi_coated_vesicle_lumen
  - neighbor-copi_vesicle_coat
  - copi-membrane-agent-go
  - copi-membrane-agent-NCBITaxon-4932
  - copi-membrane-agent-sandmann2003-meta
  - copi-membrane-agent-sandmann2003-pmc
  - copi-membrane-agent-sandmann2003-jats
  - copi-membrane-agent-sandmann2003-s3
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0030663
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:53Z to
    2026-10-21T09:12:21Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0030663
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1828 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:53Z to
    2026-10-21T09:05:00Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0030663
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:57Z to
    2026-10-21T09:05:46Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0030663
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:57Z to
    2026-10-21T09:05:06Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0030663
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE.
    Transport failures and skipped prefixes are not evidence of resolution. Exact
    target identifiers are assessed separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:57Z to
    2026-10-21T09:45:43Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/copi_coated_vesicle_membrane.yaml
  locator: Entire maintained YAML including every definition, history, claim, citation,
    graph edge and discussion
  accessed_at: '2026-10-21T11:16:02Z'
  support: context_only
  summary: All maintained fields were read before assessment. No status promotion
    or scientific edit is made.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Identifiers and exact definition matching; evidence at claim scope; component
    grounding
  accessed_at: '2026-10-21T11:16:02Z'
  support: context_only
  summary: Exact identity depends on definitions, not labels alone. A structural part,
    molecular constituent and experimental formation requirement are distinct.
- evidence_id: neighbor-copi_coated_vesicle
  kind: record_content
  reference: data/structures/membrane_organelle/copi_coated_vesicle.yaml
  locator: Entire neighboring COPI record
  accessed_at: '2026-10-21T11:16:02Z'
  support: context_only
  summary: Boundary-only context confirms the distinction between whole vesicle, structural
    coat, lipid membrane and enclosed lumen. Other claims in this neighbor are not
    an additional review target.
- evidence_id: neighbor-copi_coated_vesicle_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/copi_coated_vesicle_lumen.yaml
  locator: Entire neighboring COPI record
  accessed_at: '2026-10-21T11:16:02Z'
  support: context_only
  summary: Boundary-only context confirms the distinction between whole vesicle, structural
    coat, lipid membrane and enclosed lumen. Other claims in this neighbor are not
    an additional review target.
- evidence_id: neighbor-copi_vesicle_coat
  kind: record_content
  reference: data/structures/other/copi_vesicle_coat.yaml
  locator: Identifier, definition, parent/parthood and constituent labels/roles only
  accessed_at: '2026-10-21T11:16:02Z'
  support: context_only
  summary: Boundary-only context confirms the distinction between whole vesicle, structural
    coat, lipid membrane and enclosed lumen. Other claims in this neighbor are not
    an additional review target.
- evidence_id: copi-membrane-agent-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030137,GO:0005798,GO:0030135,GO:0030126,GO:0030663,GO:0006890,GO:0035964,GO:0000139,GO:0005783,GO:0060205,GO:0030660,GO:0030662
  locator: 'All twelve returned terms: identifiers, names, definitions, active status,
    synonyms and relevant is_a/part_of children'
  accessed_at: '2026-10-21T11:12:18.648633Z'
  support: supports
  summary: The twelve returned active GO terms were read. Their exact definitions
    and explicit parent-child relations support the declared whole-vesicle, membrane,
    coat, Golgi, ER and transport boundaries. Coatomer is only related to the whole
    vesicle but exact for the coat; GO0030663 has the exact unhyphenated membrane
    synonym. GO0060205 denotes enclosed volume. The newly observed GO0106172 candidate
    is evaluated separately for the lumen.
  snapshot_sha256: 149510128ef185f304cc1354d54bd22114e3f298d694298cb6be161bd9da0bba
- evidence_id: copi-membrane-agent-NCBITaxon-4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Exact taxId, scientificName, rank and lineage
  accessed_at: '2026-10-21T10:57:49.116059Z'
  support: supports
  summary: ENA identifies NCBITaxon4932 as Saccharomyces cerevisiae at species rank.
    This row attests only that species identity, not experimental strain or prevalence.
  snapshot_sha256: be57b95543b586448f6bd2889db42e91038e90ae2d12e8f654050c92af5b9087
- evidence_id: copi-membrane-agent-sandmann2003-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1091%2Fmbc.e02-11-0736
  locator: Exact bibliographic fields and complete returned abstract
  accessed_at: '2026-10-21T11:12:18.649055Z'
  support: supports
  summary: Native MED identifies Suppression of coatomer mutants by a new protein
    family with COPI and COPII binding motifs in Saccharomyces cerevisiae. (Sandmann
    T, Herrmann JM, Dengjel J, Schwarz H, Spang A., 2003), PMID12925749, DOI10.1091/mbc.e02-11-0736.
    Exact citation and complete abstract were read; body access and reading are described
    separately.
  snapshot_sha256: 022eedace493fd025dfedbc5584f496bf17c339d8c252d617e82628790b24a76
- evidence_id: copi-membrane-agent-sandmann2003-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC181553/
  locator: Complete Introduction sec1; Methods sec3 including Table1, sec7 protein-binding
    assay and sec14 budding assay; complete Results sec16 and sec20–23 including Figures1
    and5–7 captions; complete Discussion sec25. Other Results/Methods, image pixels
    and raw data were not reanalysed.
  accessed_at: '2026-10-21T11:12:53.605970Z'
  support: supports
  summary: The primary yeast study reports sec21/alpha-COP mutant suppression, KKXX-dependent
    coatomer binding, and vesicle production from semi-intact cells and enriched Golgi
    membranes. It distinguishes mixed-cytosol assays that cannot separate COPI/COPII
    from purified-coat assays and explicitly qualifies mechanistic interpretations.
    The strain table identifies yeast experimental backgrounds; no population frequency
    or universal formation requirement is inferred.
  snapshot_sha256: cffe4575f5abb83724d453c57de119c644e3608b33e4ca827c6f2338d0d26d7d
- evidence_id: copi-membrane-agent-sandmann2003-jats
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC181553/fullTextXML
  locator: Actual failed XML access response only
  accessed_at: '2026-10-21T11:12:39.864541Z'
  support: context_only
  summary: This XML route returned HTTP500 and supplied no scientific body. The separately
    recovered genuine PMC HTML supplied the readable primary sections.
  snapshot_sha256: 815d5d8e97853f158325ad3766a76c9a12da88493546ae654aeff9ffd68159e2
- evidence_id: copi-membrane-agent-sandmann2003-s3
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC181553.1/PMC181553.1.xml
  locator: Actual failed XML access response only
  accessed_at: '2026-10-21T11:12:39.864861Z'
  support: context_only
  summary: This XML route returned HTTP404 and supplied no scientific body. The separately
    recovered genuine PMC HTML supplied the readable primary sections.
  snapshot_sha256: 7eac4b813fabf74e10158bea55b77d9b23c7940f73cfb489f767742fefdc6898
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/copi_coated_vesicle_membrane.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T11:11:24Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/copi_coated_vesicle_membrane.yaml'
  snapshot_sha256: d2b73f13939335f9a5650b7cb8702c45a3213a99e620e3e559b6ce0f2b4f3fcf
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/copi_coated_vesicle_membrane.yaml
    --out /private/tmp/cellstructure-batch24-20261021-qayobm82/copi_coated_vesicle_membrane-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T11:11:25Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/copi_coated_vesicle_membrane.yaml\
    \ --out /private/tmp/cellstructure-batch24-20261021-qayobm82/copi_coated_vesicle_membrane-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch24-20261021-qayobm82/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch24-20261021-qayobm82/copi_coated_vesicle_membrane-strict.tsv"
  snapshot_sha256: 2f67e59b33fb21d4660be710c74aee6d015cdf0f57e3c06a8c5b84116aa0e415
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/copi_coated_vesicle_membrane.yaml; exact
    collect() scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T11:16:02Z'
  support: supports
  summary: '9 of9 collected target identifiers returned OK in this fresh base resolver
    run. Residuals: none. Source-native identity checked separately.'
  snapshot_sha256: d428d95fd13ac608f3786bcf74a032c768ac80e494b9673013e1e4d27de9ad66
- evidence_id: global-qc-result
  kind: validation
  reference: just qc
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82
  accessed_at: '2026-10-21T09:12:21Z'
  support: supports
  summary: 'Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  snapshot_sha256: 2cf77f0998cf42f98e103ee00a0f23cd610d5fcfd4814d7438d3e76bc9ef3d6d
- evidence_id: global-history-result
  kind: validation
  reference: just validate-history
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0
  accessed_at: '2026-10-21T09:05:00Z'
  support: supports
  summary: Exit 0. All 1828 history records validated; URI precheck reported zero
    invalid references.
  snapshot_sha256: 793664cc55dee807ad6725ace8cbdeb817e07c968f017af7ab0b5183a67b3df0
- evidence_id: global-products-result
  kind: validation
  reference: just validate-products
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26
  accessed_at: '2026-10-21T09:05:46Z'
  support: supports
  summary: 'Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  snapshot_sha256: dd07915effbb88aa88c56f6c102542b3cea4d9c70f381d943a664796a79c6917
- evidence_id: global-traits-result
  kind: validation
  reference: just check-trait-links --check
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad
  accessed_at: '2026-10-21T09:05:06Z'
  support: supports
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  snapshot_sha256: 6eab64b59433928ec8e0df9b0046dbccf479c84bb0911c315feebc344d536007
- evidence_id: global-curies-result
  kind: validation
  reference: just check-curies-strict
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d
  accessed_at: '2026-10-21T09:45:43Z'
  support: supports
  summary: Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE.
    Transport failures and skipped prefixes are not evidence of resolution. Exact
    target identifiers are assessed separately in this review.
  snapshot_sha256: 4b17ccc07b33ceab3eeb8631b1cf075f5f750c5a6f4820455b1930e3aa165286
assessments:
- assessment_id: identity
  area: identity
  topic: Whole-vesicle, membrane and lumen boundaries
  outcome: supported
  target_ids:
  - GO:0030663
  summary: The maintained target denotes the stated cellular structure or region,
    distinct from a coatomer protein complex. Its parent/parthood relationships preserve
    the whole-versus-part distinction. Generic GO descriptions are used only at the
    level they denote. The heterogeneous cargos and lower-level coat constituents
    are not relabeled as this target.
  evidence_ids:
  - record
  - policy
  - copi-membrane-agent-go
- assessment_id: scope
  area: scope
  topic: Yeast occurrence and model context
  outcome: supported
  target_ids:
  - GO:0030663
  summary: The maintained Saccharomyces scope and canonical example are supported
    by the inspected Sandmann yeast mutant, binding and vesicle-assay contexts. COMMON
    is treated as qualitative occurrence, not a numerical cell prevalence. The canonical
    statement is broad early-secretory/COPI context; it does not assign a particular
    strain, purification or quantitative result not given in the record. Lumen/membrane
    occurrence is the structural implication of these membrane-bounded COPI vesicles
    together with their native location definitions, not a separately measured organelle
    frequency.
  evidence_ids:
  - record
  - copi-membrane-agent-NCBITaxon-4932
  - copi-membrane-agent-sandmann2003-meta
  - copi-membrane-agent-sandmann2003-pmc
  - copi-membrane-agent-go
- assessment_id: material
  area: grounding
  topic: Collective bilayer constituent
  outcome: supported
  target_ids:
  - GO:0030663
  summary: GO0030663 denotes the whole membrane and directly defines it as the surrounding
    lipid bilayer. The direct LIPID row denotes that collective material; its label-only
    grounding avoids treating a location term as a molecular lipid species. The graph
    component_ref is appropriate for the membrane defined as this bilayer. Coat proteins
    remain represented on the coat/whole-vesicle records; no molecular inventory is
    demanded here.
  evidence_ids:
  - record
  - policy
  - copi-membrane-agent-go
  - neighbor-copi_vesicle_coat
- assessment_id: formation-necessity
  area: grounding
  topic: Specific lipid requirements remain untested
  outcome: unknown
  target_ids:
  - GO:0030663
  summary: The ESSENTIAL row applies to collective bilayer material constituting this
    membrane. The record does not name individual lipid species whose deletion or
    replacement necessity could be inferred; neither the ontology definition nor the
    inspected vesicle assays establish those individual formation requirements. This
    distinction supplies an uncertainty boundary, not a finding against the collective
    material statement.
  evidence_ids:
  - record
  - policy
  - copi-membrane-agent-go
  - copi-membrane-agent-sandmann2003-pmc
- assessment_id: graph
  area: graph
  topic: Descriptive topology at the maintained scope
  outcome: supported
  target_ids:
  - GO:0030663
  summary: The three NONMECHANISTIC edges express membrane parthood/boundary and donation
    from Golgi membrane. GO0030663 and GO0035964 directly support these topological/process
    descriptions. The graph does not elevate the coat to a lipid species or claim
    a complete assembly mechanism.
  evidence_ids:
  - record
  - copi-membrane-agent-go
- assessment_id: coverage
  area: completeness
  topic: Bounded whole-record coverage
  outcome: supported
  target_ids:
  - GO:0030663
  summary: All maintained fields, assertions, evidence notes and graph edges were
    read; cited sources were assessed at the precise scopes recorded. Empty optional
    function, trait, image, property or molecular-inventory slots do not establish
    defects. No snippet is present to repair, and no historical search or status promotion
    is certified.
  evidence_ids:
  - record
  - policy
  - copi-membrane-agent-go
  - copi-membrane-agent-sandmann2003-pmc
findings: []
actions: []
limitations:
- Sandmann was read in the explicitly named primary sections, not the entire paper
  or image pixels; neither raw microscopy nor vesicle-assay data were reanalysed.
  Yeast experimental contexts do not establish quantitative population prevalence.
- Neighbor records are boundary context only; their other claims are not additional
  review targets. No exhaustive molecular-family or chemical ontology absence is asserted.
- Global checks from the unchanged fresh base are integrated by the parent at finalization;
  deterministic success does not independently establish scientific support.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- The explicit user goal authorizes an honest review bundle for each uncovered target,
  including clean reviews; no finding is invented to satisfy the local issue-only
  gate.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
