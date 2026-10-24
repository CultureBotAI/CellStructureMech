# Dense granule membrane identity and boundary topology review

- Review: 20261021T104746Z-apicomplexan-dense-granule-membrane-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T10:27:16Z
- Finished UTC: 2026-10-21T10:47:46Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The dense-granule membrane identity, whole-organelle boundary, collective lipid material and explicitly nonmechanistic topology are supported. No corrective issue was established; literature-access and molecular-composition limits remain explicit.

## Scope And Provenance

Entire single target and whole-granule neighbor; own native GO/taxonomy/metadata and preserved review-tier body excerpts.

Selection: Ninth selected target in batch twenty, fixed maintained-path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0030668 | data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml | maintained | apicomplexan dense granule membrane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native UniProt verify | passed | False | GO:0030668 | Native command passed; scientific membership and graph scope assessed independently. |
| Native UniProt causal-graphs | passed | False | GO:0030668 | Native command passed; scientific membership and graph scope assessed independently. |
| Focused native schema | passed | True | GO:0030668 | Focused validator passed. |
| Focused native strict | passed | True | GO:0030668 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0030668 | 7 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Claim-level scientific review | passed | True | GO:0030668 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0030668 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0030668 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0030668 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0030668 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0030668 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Membrane distinct from the whole secretory organelle

identity: supported. Targets: GO:0030668.

The ontology definition, broader organelle-membrane parent and part_of dense-granule relation are supported. The record consistently represents the bounding membrane, not the stored lumen/cargo or the parasitophorous-vacuole membrane.

### Collective lipid matrix

grounding: supported. Targets: GO:0030668.

The generic lipid-bilayer row represents the constituting membrane material. GO0030668 identifies the whole membrane and is not an exact chemical-family identifier for its constituent lipids; label-only material grounding is justified. No universal lipid-species census is asserted.

### Individual formation requirements remain untested

evidence: unknown. Targets: GO:0030668.

ESSENTIAL denotes the collective constituting lipid bilayer. The cited synthesis and ontology do not identify which individual lipid species or proteins are necessary for membrane formation, and no such removal experiment is inferred from ordinary boundary identity.

### Cross-apicomplexan context and Toxoplasma example

scope: supported. Targets: GO:0030668.

The own taxonomy receipts attest Apicomplexa and Toxoplasma identities only. Cross-apicomplexan membrane-bounded dense-granule occurrence comes from review-tier Mercier context; the Toxoplasma trafficking/biogenesis example comes from Griffith. Neither establishes identical cargo inventories across all parasites.

### Explicit nonmechanistic topology

graph: supported. Targets: GO:0030668.

The boundary function and single part-of graph edge follow the native definition. NONMECHANISTIC accurately describes this topology; no cargo secretion mechanism or particular PVM permeability protein has been transferred onto the granule membrane.

### Bounded clean review

completeness: supported. Targets: GO:0030668.

No corrective issue was established. The open generic-lipid grounding question is not an error, and optional resident-membrane-protein inventories are not required to make this topology record valid. The whole-granule neighbor supplies context only.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml; Entire maintained YAML including definition, components, functions, hierarchy, examples, graph edges, discussions, image metadata and history | context_only | All fields were read after fresh native inspection; the maintained target and PROPOSED state are unchanged. |
| policy | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, CausalNode and source-specific ComplexComposition contracts; essentiality definition; docs/CURATION.md assembly-versus-function guidance and review checklist | context_only | Component family identity, concrete protein identity and source-specific assembly membership are separate. Essentiality asks whether the structure forms without the component; membership and activity do not establish it. Optional fields are not mandatory. CausalNode permits protein complexes; its xrefs contract does not inherit the top-level record equivalence restriction. |
| granule-membrane-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0020026,GO:0030668,GO:0031090; Complete definitions, synonyms and relevant relations of all three native terms | supports | GO0030668 identifies the lipid bilayer surrounding an apicomplexan dense granule. GO0031090 is the broader organelle-membrane class; GO0020026 identifies the bounded secretory organelle. |
| granule-membrane-agent-tax-5794 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5794; Complete taxId, scientificName, rank, lineage and relevant synonyms | supports | Native ENA taxonomy identifies Apicomplexa, phylum. This receipt attests that identity and rank only, not occurrence or the experimental strain. |
| granule-membrane-agent-tax-5811 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5811; Complete taxId, scientificName, rank, lineage and relevant synonyms | supports | Native ENA taxonomy identifies Toxoplasma gondii, species. This receipt attests that identity and rank only, not occurrence or the experimental strain. |
| granule-membrane-agent-doi-10.1111_jeu.12904 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1111/jeu.12904; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Dense granule biogenesis, secretion, and function in Toxoplasma gondii. Authors: Griffith MB, Pearce CS, Heaslip AT.; PMID 35302693; DOI 10.1111/jeu.12904. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| granule-membrane-agent-doi-10.1016_j.ijpara.2005.03.011 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.ijpara.2005.03.011; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Dense granules: are they key organelles to help understand the parasitophorous vacuole of all apicomplexa parasites? Authors: Mercier C, Adjogble KD, Däubener W, Delauw MF.; PMID 15978597; DOI 10.1016/j.ijpara.2005.03.011. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| granule-membrane-agent-jats-PMC9482668 | https://pmc-oa-opendata.s3.amazonaws.com/PMC9482668.1/PMC9482668.1.xml; Introduction paragraphs1-3; S2 cargo processing, S3 granule formation, S4 transport, S5-S7 secretion, S8 function opening, S10 intravacuolar network, S13 diffusion, S18 exported effectors, S20-S21 cell cycle; no comprehensive audit of remaining sections or supplementary tables. | supports | Griffith2022 is review-tier synthesis. It describes membrane-enclosed dense granules, cargo processing/aggregation, post-Golgi biogenesis, secretion and later cargo functions. Stored transmembrane cargo is distinguished from resident granule-membrane proteins. It does not supply a universal lipid species list or establish every GRA as necessary for granule formation. |
| granule-membrane-agent-mercier2005-search | https://www.sciencedirect.com/science/article/abs/pii/S0020751905001414; Publisher abstract, Introduction and discontinuous opening of Dense-granule biogenesis; indexed body extract only, with status null rather than a native HTTP200 claim. | supports | This review-tier indexed publisher extract describes dense bodies/dense granules across invasive apicomplexan stages, their bounding membrane, and taxon-specific variation. It supports qualitative broad occurrence, not a measured prevalence across all Apicomplexa. Native full publisher body was not obtained. |
| boundary-0 | data/structures/membrane_organelle/apicomplexan_dense_granule.yaml; Identifier, label, definition/source, synonyms, hierarchy/parthood and all discussions; frozen additional inspection input | context_only | These maintained fields were read to verify the stated identity boundary. This is contextual corpus evidence, not an independent full scientific review of the neighboring record. |
| native-verify | /private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml --verify; Captured focused native verify log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml --causal-graphs; Captured focused native causal-graphs log | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml --out /private/tmp/cellstructure-batch20-20261021-guyhe4k8/apicomplexan_dense_granule_membrane-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml --out /private/tmp/cellstructure-batch20-20261021-guyhe4k8/apicomplexan_dense_granule_membrane-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch20-20261021-guyhe4k8/apicomplexan_dense_granule_membrane-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 7 of7 collected target identifiers returned OK in this fresh base resolver run. Residuals: none. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Griffith2022 is a review and was read at the named biogenesis/secretion/function sections, not every supplemental table or underlying primary experiment.
- Mercier2005 evidence is limited to native metadata/abstract and indexed publisher Introduction/biogenesis excerpts. Qualitative COMMON occurrence is not a quantitative prevalence estimate.
- No universal lipid species inventory or individual lipid/protein assembly requirement is established. The whole granule was read as the explicit boundary neighbor; it is not conflated with this membrane target.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T104746Z-apicomplexan-dense-granule-membrane-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Dense granule membrane identity and boundary topology review
started_at: '2026-10-21T10:27:16Z'
finished_at: '2026-10-21T10:47:46Z'
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
summary: The dense-granule membrane identity, whole-organelle boundary, collective
  lipid material and explicitly nonmechanistic topology are supported. No corrective
  issue was established; literature-access and molecular-composition limits remain
  explicit.
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
  - path: .claude/skills/uniprot-protein-examples/SKILL.md
    sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
    role: context
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/membrane_organelle/apicomplexan_dense_granule.yaml
    sha256: 49d7347778d1dd9a80bf5ab53049d35eeefad4aee5581cb2c493dab7bb1c0bb2
    role: context
  - path: data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml
    sha256: bd48fa3c1773cf7be7066602608acdd61ba386a9fbc5fc3fd19ddaa25dcab51b
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
- target_id: GO:0030668
  path: data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml
  label: apicomplexan dense granule membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml
    role: maintained scientific record
scope:
  description: Entire single target and whole-granule neighbor; own native GO/taxonomy/metadata
    and preserved review-tier body excerpts.
  selection: Ninth selected target in batch twenty, fixed maintained-path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0030668
checks:
- check_id: native-verify
  name: Native UniProt verify
  status: passed
  required: false
  target_ids:
  - GO:0030668
  command: /private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml
    --verify
  exit_code: 0
  summary: Native command passed; scientific membership and graph scope assessed independently.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Native UniProt causal-graphs
  status: passed
  required: false
  target_ids:
  - GO:0030668
  command: /private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Native command passed; scientific membership and graph scope assessed independently.
  evidence_ids:
  - native-causal-graphs
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0030668
  command: just validate data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0030668
  command: just validate-strict data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml
    --out /private/tmp/cellstructure-batch20-20261021-guyhe4k8/apicomplexan_dense_granule_membrane-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0030668
  summary: 7 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0030668
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - granule-membrane-agent-go
  - granule-membrane-agent-tax-5794
  - granule-membrane-agent-tax-5811
  - granule-membrane-agent-doi-10.1111_jeu.12904
  - granule-membrane-agent-doi-10.1016_j.ijpara.2005.03.011
  - granule-membrane-agent-jats-PMC9482668
  - granule-membrane-agent-mercier2005-search
  - boundary-0
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0030668
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
  - GO:0030668
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
  - GO:0030668
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
  - GO:0030668
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
  - GO:0030668
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
  reference: data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml
  locator: Entire maintained YAML including definition, components, functions, hierarchy,
    examples, graph edges, discussions, image metadata and history
  accessed_at: '2026-10-21T10:46:04Z'
  support: context_only
  summary: All fields were read after fresh native inspection; the maintained target
    and PROPOSED state are unchanged.
- evidence_id: policy
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, CausalNode and source-specific ComplexComposition
    contracts; essentiality definition; docs/CURATION.md assembly-versus-function
    guidance and review checklist
  accessed_at: '2026-10-21T10:46:04Z'
  support: context_only
  summary: Component family identity, concrete protein identity and source-specific
    assembly membership are separate. Essentiality asks whether the structure forms
    without the component; membership and activity do not establish it. Optional fields
    are not mandatory. CausalNode permits protein complexes; its xrefs contract does
    not inherit the top-level record equivalence restriction.
- evidence_id: granule-membrane-agent-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0020026,GO:0030668,GO:0031090
  locator: Complete definitions, synonyms and relevant relations of all three native
    terms
  accessed_at: '2026-10-21T10:32:33.022420Z'
  support: supports
  summary: GO0030668 identifies the lipid bilayer surrounding an apicomplexan dense
    granule. GO0031090 is the broader organelle-membrane class; GO0020026 identifies
    the bounded secretory organelle.
  snapshot_sha256: d93916e4ebfb03cc1f9d6c567264d2af79d565945eeb574a85c7a792d8c7fb5f
- evidence_id: granule-membrane-agent-tax-5794
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5794
  locator: Complete taxId, scientificName, rank, lineage and relevant synonyms
  accessed_at: '2026-10-21T10:32:33.237557Z'
  support: supports
  summary: Native ENA taxonomy identifies Apicomplexa, phylum. This receipt attests
    that identity and rank only, not occurrence or the experimental strain.
  snapshot_sha256: 71f50f7adf0b7ad8670573c6c6ac0e6df37a9cf467fdec2ab20d612db477bc53
- evidence_id: granule-membrane-agent-tax-5811
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5811
  locator: Complete taxId, scientificName, rank, lineage and relevant synonyms
  accessed_at: '2026-10-21T10:32:33.426619Z'
  support: supports
  summary: Native ENA taxonomy identifies Toxoplasma gondii, species. This receipt
    attests that identity and rank only, not occurrence or the experimental strain.
  snapshot_sha256: 11679825fa4d00b18d5848862450ab6b3770aaa47ad6676d1196d9df61124b16
- evidence_id: granule-membrane-agent-doi-10.1111_jeu.12904
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1111/jeu.12904
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T10:32:33.600335Z'
  support: supports
  summary: 'Native metadata identifies Dense granule biogenesis, secretion, and function
    in Toxoplasma gondii. Authors: Griffith MB, Pearce CS, Heaslip AT.; PMID 35302693;
    DOI 10.1111/jeu.12904. Bibliographic identity and available abstract only; not
    a substitute for inspected article body.'
  snapshot_sha256: deab13eca62c55b1cdbdff5590b100d2be74786a62b86faca60ae5aefcb396c6
- evidence_id: granule-membrane-agent-doi-10.1016_j.ijpara.2005.03.011
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.ijpara.2005.03.011
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T10:32:33.579611Z'
  support: supports
  summary: 'Native metadata identifies Dense granules: are they key organelles to
    help understand the parasitophorous vacuole of all apicomplexa parasites? Authors:
    Mercier C, Adjogble KD, Däubener W, Delauw MF.; PMID 15978597; DOI 10.1016/j.ijpara.2005.03.011.
    Bibliographic identity and available abstract only; not a substitute for inspected
    article body.'
  snapshot_sha256: 676306a8292b4688db4432a0bf7274977650407a19d0812ebe6be47b78d1718a
- evidence_id: granule-membrane-agent-jats-PMC9482668
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC9482668.1/PMC9482668.1.xml
  locator: Introduction paragraphs1-3; S2 cargo processing, S3 granule formation,
    S4 transport, S5-S7 secretion, S8 function opening, S10 intravacuolar network,
    S13 diffusion, S18 exported effectors, S20-S21 cell cycle; no comprehensive audit
    of remaining sections or supplementary tables.
  accessed_at: '2026-10-21T10:33:24.005355Z'
  support: supports
  summary: Griffith2022 is review-tier synthesis. It describes membrane-enclosed dense
    granules, cargo processing/aggregation, post-Golgi biogenesis, secretion and later
    cargo functions. Stored transmembrane cargo is distinguished from resident granule-membrane
    proteins. It does not supply a universal lipid species list or establish every
    GRA as necessary for granule formation.
  snapshot_sha256: c299f0194d8df4f3f95ed870283b1cc9212a3b8f7a39bfab4328c318d08a1b8c
- evidence_id: granule-membrane-agent-mercier2005-search
  kind: authority
  reference: https://www.sciencedirect.com/science/article/abs/pii/S0020751905001414
  locator: Publisher abstract, Introduction and discontinuous opening of Dense-granule
    biogenesis; indexed body extract only, with status null rather than a native HTTP200
    claim.
  accessed_at: '2026-10-21T10:35:00.260Z'
  support: supports
  summary: This review-tier indexed publisher extract describes dense bodies/dense
    granules across invasive apicomplexan stages, their bounding membrane, and taxon-specific
    variation. It supports qualitative broad occurrence, not a measured prevalence
    across all Apicomplexa. Native full publisher body was not obtained.
  snapshot_sha256: cc62d73c79c01ec94ed5baa90427143c95f4c1f88f7c96c147365807de86d565
- evidence_id: boundary-0
  kind: record_content
  reference: data/structures/membrane_organelle/apicomplexan_dense_granule.yaml
  locator: Identifier, label, definition/source, synonyms, hierarchy/parthood and
    all discussions; frozen additional inspection input
  accessed_at: '2026-10-21T10:46:04Z'
  support: context_only
  summary: These maintained fields were read to verify the stated identity boundary.
    This is contextual corpus evidence, not an independent full scientific review
    of the neighboring record.
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml
    --verify
  locator: Captured focused native verify log
  accessed_at: '2026-10-21T10:32:35.592035Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml
    --causal-graphs
  locator: Captured focused native causal-graphs log
  accessed_at: '2026-10-21T10:32:36.067909Z'
  support: supports
  summary: "causal_graphs GENE_OR_PROTEIN node summary:\n     0  COVERED         \
    \          component_ref target holds protein_examples covering all declared symbols\n\
    \     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     0\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:27:18Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml'
  snapshot_sha256: 568a15314d8c3787631c05cc75d45926805f4695e585711f278ca0b83f9acdd5
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml
    --out /private/tmp/cellstructure-batch20-20261021-guyhe4k8/apicomplexan_dense_granule_membrane-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:27:20Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml\
    \ --out /private/tmp/cellstructure-batch20-20261021-guyhe4k8/apicomplexan_dense_granule_membrane-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch20-20261021-guyhe4k8/apicomplexan_dense_granule_membrane-strict.tsv"
  snapshot_sha256: e8778c782533b7ef8ce76b9f745584320a4f74df9ca1a2d47376e6b6040e85dc
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml;
    exact collect() scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T10:46:05Z'
  support: supports
  summary: '7 of7 collected target identifiers returned OK in this fresh base resolver
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
  topic: Membrane distinct from the whole secretory organelle
  outcome: supported
  target_ids:
  - GO:0030668
  summary: The ontology definition, broader organelle-membrane parent and part_of
    dense-granule relation are supported. The record consistently represents the bounding
    membrane, not the stored lumen/cargo or the parasitophorous-vacuole membrane.
  evidence_ids:
  - granule-membrane-agent-go
  - boundary-0
  - granule-membrane-agent-jats-PMC9482668
  - record
- assessment_id: composition
  area: grounding
  topic: Collective lipid matrix
  outcome: supported
  target_ids:
  - GO:0030668
  summary: The generic lipid-bilayer row represents the constituting membrane material.
    GO0030668 identifies the whole membrane and is not an exact chemical-family identifier
    for its constituent lipids; label-only material grounding is justified. No universal
    lipid-species census is asserted.
  evidence_ids:
  - granule-membrane-agent-go
  - granule-membrane-agent-jats-PMC9482668
  - record
  - policy
- assessment_id: necessity
  area: evidence
  topic: Individual formation requirements remain untested
  outcome: unknown
  target_ids:
  - GO:0030668
  summary: ESSENTIAL denotes the collective constituting lipid bilayer. The cited
    synthesis and ontology do not identify which individual lipid species or proteins
    are necessary for membrane formation, and no such removal experiment is inferred
    from ordinary boundary identity.
  evidence_ids:
  - granule-membrane-agent-go
  - granule-membrane-agent-jats-PMC9482668
  - record
  - policy
- assessment_id: scope
  area: scope
  topic: Cross-apicomplexan context and Toxoplasma example
  outcome: supported
  target_ids:
  - GO:0030668
  summary: The own taxonomy receipts attest Apicomplexa and Toxoplasma identities
    only. Cross-apicomplexan membrane-bounded dense-granule occurrence comes from
    review-tier Mercier context; the Toxoplasma trafficking/biogenesis example comes
    from Griffith. Neither establishes identical cargo inventories across all parasites.
  evidence_ids:
  - granule-membrane-agent-tax-5794
  - granule-membrane-agent-tax-5811
  - granule-membrane-agent-doi-10.1111_jeu.12904
  - granule-membrane-agent-doi-10.1016_j.ijpara.2005.03.011
  - granule-membrane-agent-mercier2005-search
  - granule-membrane-agent-jats-PMC9482668
  - record
- assessment_id: function-graph
  area: graph
  topic: Explicit nonmechanistic topology
  outcome: supported
  target_ids:
  - GO:0030668
  summary: The boundary function and single part-of graph edge follow the native definition.
    NONMECHANISTIC accurately describes this topology; no cargo secretion mechanism
    or particular PVM permeability protein has been transferred onto the granule membrane.
  evidence_ids:
  - granule-membrane-agent-go
  - granule-membrane-agent-jats-PMC9482668
  - record
- assessment_id: coverage
  area: completeness
  topic: Bounded clean review
  outcome: supported
  target_ids:
  - GO:0030668
  summary: No corrective issue was established. The open generic-lipid grounding question
    is not an error, and optional resident-membrane-protein inventories are not required
    to make this topology record valid. The whole-granule neighbor supplies context
    only.
  evidence_ids:
  - granule-membrane-agent-go
  - granule-membrane-agent-jats-PMC9482668
  - boundary-0
  - record
  - policy
findings: []
actions: []
limitations:
- Griffith2022 is a review and was read at the named biogenesis/secretion/function
  sections, not every supplemental table or underlying primary experiment.
- Mercier2005 evidence is limited to native metadata/abstract and indexed publisher
  Introduction/biogenesis excerpts. Qualitative COMMON occurrence is not a quantitative
  prevalence estimate.
- No universal lipid species inventory or individual lipid/protein assembly requirement
  is established. The whole granule was read as the explicit boundary neighbor; it
  is not conflated with this membrane target.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
