# Bacterial thylakoid source and organism-context audit

- Review: 20261021T110749Z-bacterial-thylakoid-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T10:40:17Z
- Finished UTC: 2026-10-21T11:07:49Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact whole-thylakoid identity and coarse functional topology are supported. One major primary-source organism mismatch affects the canonical example and repeated localization notes.

## Scope And Provenance

Entire exact target including all components, taxa, example, functions, ten graph edges and both discussions.

Selection: Batch21 index5; entire exact maintained record at frozen main9c0446, reviewed individually.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0030075 | data/structures/membrane_organelle/bacterial_thylakoid.yaml | maintained | bacterial thylakoid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native verify | passed | True | GO:0030075 | Focused native check passed. |
| Focused native causal-graphs | passed | True | GO:0030075 | Focused native check passed. |
| Focused native schema | passed | True | GO:0030075 | Focused validator passed. |
| Focused native strict | passed | True | GO:0030075 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0030075 | 15 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Claim-level scientific review | passed | True | GO:0030075 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0030075 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0030075 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0030075 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0030075 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0030075 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Whole thylakoid identity and part boundaries

identity: supported. Targets: GO:0030075.

The exact GO identity, synonym, parent and four asserted parts are supported; OTHER follows the explicit GO comment that a thylakoid is not an organelle. The filesystem category does not redefine its kind. No local sibling record is used as scientific evidence.

### Collective bilayer and photosynthetic complex membership

evidence: supported. Targets: GO:0030075.

A membrane boundary is constitutional to this compartment, supporting ESSENTIAL at the collective bilayer level. The four known photosynthetic complexes are correctly represented by complex identifiers rather than forced single-protein families. Native authority and the primary assays establish broad membership; their incorrect organism attributions are separately addressed by F1.

### Individual molecular assembly requirements

evidence: unknown. Targets: GO:0030075.

The four complex rows correctly retain UNKNOWN. Membrane residence, photosynthetic function, changing abundance and the study of biogenesis do not alone establish which complex or individual lipid is necessary to form every bacterial thylakoid.

### Taxonomic distribution versus exact experimental model

scope: concern. Targets: GO:0030075.

Cyanobacterial COMMON presence with a named thylakoid-lacking exception is supported. Both source papers study Synechococcus elongatus PCC7942; the target transfers this work to Synechocystis PCC6803 and repeats Synechocystis in Casella evidence notes (F1). This is a source-organism mismatch, not evidence that Synechocystis lacks thylakoids.

### Both functions and all ten coarse graph edges

graph: supported. Targets: GO:0030075.

The membrane/lumen topology and PSII–quinone–b6f–PSI/ATP synthesis roles are supported at the declared NONMECHANISTIC scale. The b6f-to-PSI edge explicitly allows a downstream soluble carrier. No fixed stoichiometry, exhaustive respiratory inventory or direct b6f–PSI physical transfer is asserted. Correct the organism scope of the two Casella localization edges with F1.

### Ontology-derived attachment wording versus observed membrane development

evidence: unknown. Targets: GO:0030075.

The target reproduces current GO wording accurately. Huokko distinguishes proximity/thylapse-like contacts from direct membrane connection or fusion and leaves origin models unresolved. This review does not infer obligatory membrane continuity, universal plasma-membrane budding, or validated membrane tethers in every cyanobacterium from that wording.

### Evidence identity, discussion scope and bounded inventory

completeness: supported. Targets: GO:0030075.

All cited DOIs resolve to the intended works. The native ontology supports the resolved whole-compartment versus membrane and non-organelle decisions. The record has no image or protein-example assertions. Additional respiratory complexes, lipid species and detailed biogenesis machinery are not mandatory solely because the sources describe them. Historical notes remain historical.

## Findings

### F1: The cited primary thylakoid studies used Synechococcus PCC7942, not Synechocystis PCC6803

major / open / confirmed; issue key: bacterial_thylakoid-experimental-organism-mismatch.

Huokko2021 explicitly performs light-regulated thylakoid biogenesis experiments in Synechococcus elongatus PCC7942, whereas canonical_examples[0] assigns that experiment to tax1148 Synechocystis PCC6803. Casella2017 likewise performs its native membrane organization and mobility experiments in PCC7942, but four maintained component/graph source notes call the assayed organism Synechocystis. Both papers discuss earlier Synechocystis work, which is not a substitute for their own Methods. Reconcile the exemplar taxon, label, note and reference together, and correct the repeated Casella organism attributions. The evidence does not imply that Synechocystis lacks thylakoids.

## Recommended Actions And Acceptance Checks

### A1

Align the canonical experimental example and all Casella source notes with the actually assayed strain, or provide a separate direct source for the retained Synechocystis claim.

- Huokko2021 is assigned to Synechococcus elongatus PCC7942 with a native-verified taxon identifier, or the Synechocystis example receives an appropriate direct study.
- All four Casella membrane-localization notes identify PCC7942 rather than transferring its observations to PCC6803.
- Keep light-adaptation context and source uncertainty; do not rewrite historical curation entries or infer absence of thylakoids in either organism.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/bacterial_thylakoid.yaml; Entire YAML, including all10 graph edges and both resolved discussions | context_only | The whole bacterial-thylakoid record is distinct from its membrane and lumen parts. All fields, sources and historical entries were inspected; no historical entry was rewritten. |
| graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; NONMECHANISTIC and source-scope rubric | context_only | A coarse topology/function graph need not claim a complete molecular mechanism or direct interventions. |
| policy | docs/CURATION.md; Composition and assembly essentiality; claim-level evidence scope | context_only | Localization and catalytic activity differ from necessity for structure formation. Sources must retain their organism and experimental context. |
| thylakoid-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030075,GO:0009579,GO:0031676,GO:0031979,GO:0030094,GO:0030096,GO:0009512,GO:0045259,GO:0009767,GO:0042651; Complete results identity/definition/synonym/comment fields and relevant children relations | supports | All ten native GO terms are active with the stated labels and aspects. GO0009579 lists bacterial thylakoid as an is_a child and explicitly excludes organelle status. GO0030075 lists the asserted membrane, lumen and photosystems as part_of children; native definitions support their topology and complex functions. The retained plasma-membrane-derived wording is an ontology definition, not direct proof of universal fusion or a resolved biogenesis pathway. |
| thylakoid-agent-tax-1117 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1117; taxId/scientificName/rank/lineage/otherNames | supports | Native taxonomy identifies Cyanobacteriota phylum. Taxon identity alone does not establish occurrence or the experimental organism used by a paper. |
| thylakoid-agent-tax-1148 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1148; taxId/scientificName/rank/lineage/otherNames | supports | Native taxonomy identifies Synechocystis sp. PCC6803 strain. Taxon identity alone does not establish occurrence or the experimental organism used by a paper. |
| thylakoid-agent-tax-1140 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1140; taxId/scientificName/rank/lineage/otherNames | supports | Native taxonomy identifies Synechococcus elongatus PCC7942 = FACHB-805 strain, including the historical Syn7942 names. Taxon identity alone does not establish occurrence or the experimental organism used by a paper. |
| thylakoid-agent-perez2024-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1146%2Fannurev-cellbio-120823-022747&amp;format=json&amp;resultType=core; resultList.result[0] complete citation and abstractText | supports | Exact native metadata identifies Evolution of Thylakoid Structural Diversity. PMID38950450, DOI10.1146/annurev-cellbio-120823-022747; author/year and complete abstract inspected. This is bibliographic and abstract scope for a secondary review.  |
| thylakoid-agent-casella2017-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fj.molp.2017.09.019&amp;format=json&amp;resultType=core; resultList.result[0] complete citation and abstractText | supports | Exact native metadata identifies Dissecting the Native Architecture and Dynamics of Cyanobacterial Photosynthetic Machinery. PMID29017828, DOI10.1016/j.molp.2017.09.019; author/year and complete abstract inspected. The abstract explicitly identifies Synechococcus elongatus PCC7942.  |
| thylakoid-agent-huokko2021-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fs41467-021-23680-1&amp;format=json&amp;resultType=core; resultList.result[0] complete citation and abstractText | supports | Exact native metadata identifies Probing the biogenesis pathway and dynamics of thylakoid membranes. PMID34108457, DOI10.1038/s41467-021-23680-1; author/year and complete abstract inspected. The abstract explicitly identifies Synechococcus elongatus PCC7942.  |
| thylakoid-agent-jats-PMC5683893 | https://pmc-oa-opendata.s3.amazonaws.com/PMC5683893.1/PMC5683893.1.xml; Introduction; all Results sec2.1–sec2.4 and embedded Table1/Fig1–8 captions; Methods sec4.1 strains and sec4.8 FRAP. Discussion selected comparison/limitations paragraphs. No figure pixels, supplements or raw data reanalysis. | supports | The primary experiments use Synechococcus elongatus PCC7942. Detergent-free membrane AFM, separately tagged photosynthetic complexes, live-cell microscopy and FRAP establish localization and condition-dependent mobility. Cyt b6f identification by AFM alone is tentative; tagged-cell localization provides distinct support. References to Synechocystis in the Introduction compare prior studies and do not change the assayed strain. |
| thylakoid-agent-jats-PMC8190092 | https://pmc-oa-opendata.s3.amazonaws.com/PMC8190092.1/PMC8190092.1.xml; Introduction Sec1; all Results Sec3–Sec6; Discussion Sec7; Methods Sec9 strains/culture, Sec12 TEM and Sec13 cryo-ET; embedded figure captions. No microscopy pixels, supplements or raw proteomics independently reanalyzed. | supports | The primary biogenesis experiment uses Synechococcus elongatus PCC7942 after14 days of high light and subsequent low-light recovery. Microscopy, proteomics and tagged complexes resolve membrane redevelopment and sequential complex accumulation. It finds no apparent direct plasma/thylakoid fusion or connection in the observed cells, while tips approach the plasma membrane and biogenic mechanisms remain debated. Synechocystis PCC6803 is background comparison, not this experimental model. |
| thylakoid-agent-perez2024-browser-search | https://doi.org/10.1146%2Fannurev-cellbio-120823-022747; Preserved original batch14 browser artifact: publisher Electron Transport Chain Complexes subsection. Mixed output contains unrelated search results, which are not evidence here. | supports | The inspected review passage describes the PSII–plastoquinol–b6f–soluble-carrier–PSI route, ferredoxin reduction, lumenal proton accumulation and ATP synthase. It also distinguishes cyanobacterial respiratory machinery. This is secondary synthesis captured through a browser, not native HTTP200 or a full review audit. |
| thylakoid-agent-perez2024-browser-introduction | https://doi.org/10.1146%2Fannurev-cellbio-120823-022747; Current browser artifact: publisher Introduction paragraphs and selected Architecture contact-site paragraphs; mixed search/open output, unrelated hits not relied on. Capture timestamp is not a native request timestamp. | supports | The publisher Introduction describes thylakoids across oxygenic phototrophs and the Gloeobacter exception. Selected Architecture paragraphs distinguish membrane contacts and protein tethers from continuity. These passages support the bounded COMMON distribution and caution against treating an ontology label as a universal fusion mechanism. |
| native-verify | /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/bacterial_thylakoid.yaml --verify; Complete focused native output | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/bacterial_thylakoid.yaml --causal-graphs; Complete focused native output | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/membrane_organelle/bacterial_thylakoid.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/bacterial_thylakoid.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/bacterial_thylakoid.yaml --out /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/bacterial_thylakoid-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/bacterial_thylakoid.yaml --out /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/bacterial_thylakoid-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch21-20261021-jc4u1a6u/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/bacterial_thylakoid-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/bacterial_thylakoid.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 15 of15 collected target identifiers returned OK in this fresh base resolver run. Residuals: none. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Casella2017 and Huokko2021 were read in genuine JATS bodies at the declared sections. No figure pixels, raw microscopy, raw proteomics, supplements or complete Methods audits were performed.
- Perez-Boerema2024 native publisher routes returned403. Actual publisher Introduction and Electron Transport Chain Complexes passages were read through preserved browser captures; these are secondary review evidence, not a complete full-text audit or native HTTP200.
- Native GO retains plasma-membrane-derived/attached language. The primary biogenesis study does not establish universal fusion or a single origin mechanism; proximity, membrane contacts and continuity remain distinct.
- Assembly necessity of individual complexes/lipids and an exhaustive inventory are not established. No exact single-protein mapping is required for the represented whole-complex rows.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T110749Z-bacterial-thylakoid-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Bacterial thylakoid source and organism-context audit
started_at: '2026-10-21T10:40:17Z'
finished_at: '2026-10-21T11:07:49Z'
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
summary: Exact whole-thylakoid identity and coarse functional topology are supported.
  One major primary-source organism mismatch affects the canonical example and repeated
  localization notes.
source:
  git_revision: 9c0446c4c0dd4b458787c43a499e4ceab5e179a6
  state: working_tree
  inputs:
  - path: .claude/skills/curate-causal-graphs/SKILL.md
    sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
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
  - path: data/structures/membrane_organelle/bacterial_thylakoid.yaml
    sha256: a134c6cf6fd6069f0a0ddc37f1e99ded9a32994b3b1fa16d2f9938e3e46b8c40
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
- target_id: GO:0030075
  path: data/structures/membrane_organelle/bacterial_thylakoid.yaml
  label: bacterial thylakoid
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/bacterial_thylakoid.yaml
    role: maintained scientific record
scope:
  description: Entire exact target including all components, taxa, example, functions,
    ten graph edges and both discussions.
  selection: Batch21 index5; entire exact maintained record at frozen main9c0446,
    reviewed individually.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0030075
checks:
- check_id: native-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - GO:0030075
  command: /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/bacterial_thylakoid.yaml
    --verify
  exit_code: 0
  summary: Focused native check passed.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0030075
  command: /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/bacterial_thylakoid.yaml
    --causal-graphs
  exit_code: 0
  summary: Focused native check passed.
  evidence_ids:
  - native-causal-graphs
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0030075
  command: just validate data/structures/membrane_organelle/bacterial_thylakoid.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0030075
  command: just validate-strict data/structures/membrane_organelle/bacterial_thylakoid.yaml
    --out /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/bacterial_thylakoid-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0030075
  summary: 15 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0030075
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - graph-policy
  - policy
  - thylakoid-agent-go
  - thylakoid-agent-tax-1117
  - thylakoid-agent-tax-1148
  - thylakoid-agent-tax-1140
  - thylakoid-agent-perez2024-meta
  - thylakoid-agent-casella2017-meta
  - thylakoid-agent-huokko2021-meta
  - thylakoid-agent-jats-PMC5683893
  - thylakoid-agent-jats-PMC8190092
  - thylakoid-agent-perez2024-browser-search
  - thylakoid-agent-perez2024-browser-introduction
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0030075
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
  - GO:0030075
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
  - GO:0030075
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
  - GO:0030075
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
  - GO:0030075
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
  reference: data/structures/membrane_organelle/bacterial_thylakoid.yaml
  locator: Entire YAML, including all10 graph edges and both resolved discussions
  accessed_at: '2026-10-21T10:53:31Z'
  support: context_only
  summary: The whole bacterial-thylakoid record is distinct from its membrane and
    lumen parts. All fields, sources and historical entries were inspected; no historical
    entry was rewritten.
- evidence_id: graph-policy
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: NONMECHANISTIC and source-scope rubric
  accessed_at: '2026-10-21T10:53:31Z'
  support: context_only
  summary: A coarse topology/function graph need not claim a complete molecular mechanism
    or direct interventions.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Composition and assembly essentiality; claim-level evidence scope
  accessed_at: '2026-10-21T10:53:31Z'
  support: context_only
  summary: Localization and catalytic activity differ from necessity for structure
    formation. Sources must retain their organism and experimental context.
- evidence_id: thylakoid-agent-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030075,GO:0009579,GO:0031676,GO:0031979,GO:0030094,GO:0030096,GO:0009512,GO:0045259,GO:0009767,GO:0042651
  locator: Complete results identity/definition/synonym/comment fields and relevant
    children relations
  accessed_at: '2026-10-21T10:44:32.317729Z'
  support: supports
  summary: All ten native GO terms are active with the stated labels and aspects.
    GO0009579 lists bacterial thylakoid as an is_a child and explicitly excludes organelle
    status. GO0030075 lists the asserted membrane, lumen and photosystems as part_of
    children; native definitions support their topology and complex functions. The
    retained plasma-membrane-derived wording is an ontology definition, not direct
    proof of universal fusion or a resolved biogenesis pathway.
  snapshot_sha256: a318cc333a4ce72ef86dbc2671fef779dc2ad9fc744e8d3404ca11b9911e9954
- evidence_id: thylakoid-agent-tax-1117
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1117
  locator: taxId/scientificName/rank/lineage/otherNames
  accessed_at: '2026-10-21T10:44:32.373938Z'
  support: supports
  summary: Native taxonomy identifies Cyanobacteriota phylum. Taxon identity alone
    does not establish occurrence or the experimental organism used by a paper.
  snapshot_sha256: 0462d61ee879faf0de43deb3472da6e0fe29fdf63cc068591b0ca652eb921c4d
- evidence_id: thylakoid-agent-tax-1148
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1148
  locator: taxId/scientificName/rank/lineage/otherNames
  accessed_at: '2026-10-21T10:44:32.392061Z'
  support: supports
  summary: Native taxonomy identifies Synechocystis sp. PCC6803 strain. Taxon identity
    alone does not establish occurrence or the experimental organism used by a paper.
  snapshot_sha256: 84c0a354189f6b736c57eb3886dc08090cd6edba80c6e35c1b92909c26f35ab4
- evidence_id: thylakoid-agent-tax-1140
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1140
  locator: taxId/scientificName/rank/lineage/otherNames
  accessed_at: '2026-10-21T10:45:06.746047Z'
  support: supports
  summary: Native taxonomy identifies Synechococcus elongatus PCC7942 = FACHB-805
    strain, including the historical Syn7942 names. Taxon identity alone does not
    establish occurrence or the experimental organism used by a paper.
  snapshot_sha256: 70bf02b8ca783e9afbd060d6c098a79cec71954ea2d64a270fc130481a63cb2b
- evidence_id: thylakoid-agent-perez2024-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1146%2Fannurev-cellbio-120823-022747&format=json&resultType=core
  locator: resultList.result[0] complete citation and abstractText
  accessed_at: '2026-10-21T10:44:30.997805Z'
  support: supports
  summary: 'Exact native metadata identifies Evolution of Thylakoid Structural Diversity.
    PMID38950450, DOI10.1146/annurev-cellbio-120823-022747; author/year and complete
    abstract inspected. This is bibliographic and abstract scope for a secondary review. '
  snapshot_sha256: f9df3427bb3b35764922628c9e89cc9378fa7875a4a103bde71a75b130d54926
- evidence_id: thylakoid-agent-casella2017-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fj.molp.2017.09.019&format=json&resultType=core
  locator: resultList.result[0] complete citation and abstractText
  accessed_at: '2026-10-21T10:44:30.998767Z'
  support: supports
  summary: 'Exact native metadata identifies Dissecting the Native Architecture and
    Dynamics of Cyanobacterial Photosynthetic Machinery. PMID29017828, DOI10.1016/j.molp.2017.09.019;
    author/year and complete abstract inspected. The abstract explicitly identifies
    Synechococcus elongatus PCC7942. '
  snapshot_sha256: 1c47c2e672d5f9c2bc828bcd7f7112bfa00418cb7a683c5677e18e365e6acdf4
- evidence_id: thylakoid-agent-huokko2021-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fs41467-021-23680-1&format=json&resultType=core
  locator: resultList.result[0] complete citation and abstractText
  accessed_at: '2026-10-21T10:44:30.999142Z'
  support: supports
  summary: 'Exact native metadata identifies Probing the biogenesis pathway and dynamics
    of thylakoid membranes. PMID34108457, DOI10.1038/s41467-021-23680-1; author/year
    and complete abstract inspected. The abstract explicitly identifies Synechococcus
    elongatus PCC7942. '
  snapshot_sha256: af3189fba6c317b70a180f0f879e06319c38aa25d407906fa3a9c9e4628f1ab5
- evidence_id: thylakoid-agent-jats-PMC5683893
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5683893.1/PMC5683893.1.xml
  locator: Introduction; all Results sec2.1–sec2.4 and embedded Table1/Fig1–8 captions;
    Methods sec4.1 strains and sec4.8 FRAP. Discussion selected comparison/limitations
    paragraphs. No figure pixels, supplements or raw data reanalysis.
  accessed_at: '2026-10-21T10:45:06.271696Z'
  support: supports
  summary: The primary experiments use Synechococcus elongatus PCC7942. Detergent-free
    membrane AFM, separately tagged photosynthetic complexes, live-cell microscopy
    and FRAP establish localization and condition-dependent mobility. Cyt b6f identification
    by AFM alone is tentative; tagged-cell localization provides distinct support.
    References to Synechocystis in the Introduction compare prior studies and do not
    change the assayed strain.
  snapshot_sha256: 6e3c04f52b15e4ce163579c9c0c3a44b1946bded6fe47e1299e3ef6dc2ce18d7
- evidence_id: thylakoid-agent-jats-PMC8190092
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC8190092.1/PMC8190092.1.xml
  locator: Introduction Sec1; all Results Sec3–Sec6; Discussion Sec7; Methods Sec9
    strains/culture, Sec12 TEM and Sec13 cryo-ET; embedded figure captions. No microscopy
    pixels, supplements or raw proteomics independently reanalyzed.
  accessed_at: '2026-10-21T10:45:06.271226Z'
  support: supports
  summary: The primary biogenesis experiment uses Synechococcus elongatus PCC7942
    after14 days of high light and subsequent low-light recovery. Microscopy, proteomics
    and tagged complexes resolve membrane redevelopment and sequential complex accumulation.
    It finds no apparent direct plasma/thylakoid fusion or connection in the observed
    cells, while tips approach the plasma membrane and biogenic mechanisms remain
    debated. Synechocystis PCC6803 is background comparison, not this experimental
    model.
  snapshot_sha256: 0140e3b1a9fbb1fe170d186f153c24e08fb32c4cc91754a49facf09cdc67ff21
- evidence_id: thylakoid-agent-perez2024-browser-search
  kind: authority
  reference: https://doi.org/10.1146%2Fannurev-cellbio-120823-022747
  locator: 'Preserved original batch14 browser artifact: publisher Electron Transport
    Chain Complexes subsection. Mixed output contains unrelated search results, which
    are not evidence here.'
  accessed_at: '2026-10-21T08:46:38.912004Z'
  support: supports
  summary: The inspected review passage describes the PSII–plastoquinol–b6f–soluble-carrier–PSI
    route, ferredoxin reduction, lumenal proton accumulation and ATP synthase. It
    also distinguishes cyanobacterial respiratory machinery. This is secondary synthesis
    captured through a browser, not native HTTP200 or a full review audit.
  snapshot_sha256: 1e2a20aee1043d6a8c9b511e909b825174d51fe9374f438c494e924d20992a0e
- evidence_id: thylakoid-agent-perez2024-browser-introduction
  kind: authority
  reference: https://doi.org/10.1146%2Fannurev-cellbio-120823-022747
  locator: 'Current browser artifact: publisher Introduction paragraphs and selected
    Architecture contact-site paragraphs; mixed search/open output, unrelated hits
    not relied on. Capture timestamp is not a native request timestamp.'
  accessed_at: '2026-10-21T10:46:36.113233Z'
  support: supports
  summary: The publisher Introduction describes thylakoids across oxygenic phototrophs
    and the Gloeobacter exception. Selected Architecture paragraphs distinguish membrane
    contacts and protein tethers from continuity. These passages support the bounded
    COMMON distribution and caution against treating an ontology label as a universal
    fusion mechanism.
  snapshot_sha256: 634c866a9cd76eae27d4820d7734d7e25ef595d42781bf95f8b816821065e9ba
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/bacterial_thylakoid.yaml
    --verify
  locator: Complete focused native output
  accessed_at: '2026-10-21T10:46:55.342680Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/bacterial_thylakoid.yaml
    --causal-graphs
  locator: Complete focused native output
  accessed_at: '2026-10-21T10:46:56.004173Z'
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
  reference: just validate data/structures/membrane_organelle/bacterial_thylakoid.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:40:19Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/bacterial_thylakoid.yaml'
  snapshot_sha256: ed9da953ba3bf01d293a7674e9a7c0ac2e0ba28c9a2a60154b702b36a7c25466
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/bacterial_thylakoid.yaml
    --out /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/bacterial_thylakoid-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:40:22Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/bacterial_thylakoid.yaml\
    \ --out /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/bacterial_thylakoid-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch21-20261021-jc4u1a6u/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/bacterial_thylakoid-strict.tsv"
  snapshot_sha256: 73ff0bb598641a19771b087f210834c82c0c855d67c28f06dbcfb6ac6c99711d
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/bacterial_thylakoid.yaml; exact collect()
    scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T10:53:31Z'
  support: supports
  summary: '15 of15 collected target identifiers returned OK in this fresh base resolver
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
  topic: Whole thylakoid identity and part boundaries
  outcome: supported
  target_ids:
  - GO:0030075
  summary: The exact GO identity, synonym, parent and four asserted parts are supported;
    OTHER follows the explicit GO comment that a thylakoid is not an organelle. The
    filesystem category does not redefine its kind. No local sibling record is used
    as scientific evidence.
  evidence_ids:
  - record
  - thylakoid-agent-go
- assessment_id: composition
  area: evidence
  topic: Collective bilayer and photosynthetic complex membership
  outcome: supported
  target_ids:
  - GO:0030075
  summary: A membrane boundary is constitutional to this compartment, supporting ESSENTIAL
    at the collective bilayer level. The four known photosynthetic complexes are correctly
    represented by complex identifiers rather than forced single-protein families.
    Native authority and the primary assays establish broad membership; their incorrect
    organism attributions are separately addressed by F1.
  evidence_ids:
  - record
  - thylakoid-agent-go
  - thylakoid-agent-jats-PMC5683893
  - thylakoid-agent-jats-PMC8190092
- assessment_id: necessity
  area: evidence
  topic: Individual molecular assembly requirements
  outcome: unknown
  target_ids:
  - GO:0030075
  summary: The four complex rows correctly retain UNKNOWN. Membrane residence, photosynthetic
    function, changing abundance and the study of biogenesis do not alone establish
    which complex or individual lipid is necessary to form every bacterial thylakoid.
  evidence_ids:
  - record
  - policy
  - thylakoid-agent-jats-PMC5683893
  - thylakoid-agent-jats-PMC8190092
- assessment_id: taxon-example
  area: scope
  topic: Taxonomic distribution versus exact experimental model
  outcome: concern
  target_ids:
  - GO:0030075
  summary: Cyanobacterial COMMON presence with a named thylakoid-lacking exception
    is supported. Both source papers study Synechococcus elongatus PCC7942; the target
    transfers this work to Synechocystis PCC6803 and repeats Synechocystis in Casella
    evidence notes (F1). This is a source-organism mismatch, not evidence that Synechocystis
    lacks thylakoids.
  evidence_ids:
  - record
  - thylakoid-agent-perez2024-browser-introduction
  - thylakoid-agent-jats-PMC5683893
  - thylakoid-agent-jats-PMC8190092
  - thylakoid-agent-tax-1117
  - thylakoid-agent-tax-1148
  - thylakoid-agent-tax-1140
- assessment_id: functions-graph
  area: graph
  topic: Both functions and all ten coarse graph edges
  outcome: supported
  target_ids:
  - GO:0030075
  summary: The membrane/lumen topology and PSII–quinone–b6f–PSI/ATP synthesis roles
    are supported at the declared NONMECHANISTIC scale. The b6f-to-PSI edge explicitly
    allows a downstream soluble carrier. No fixed stoichiometry, exhaustive respiratory
    inventory or direct b6f–PSI physical transfer is asserted. Correct the organism
    scope of the two Casella localization edges with F1.
  evidence_ids:
  - record
  - graph-policy
  - thylakoid-agent-go
  - thylakoid-agent-perez2024-browser-search
  - thylakoid-agent-jats-PMC5683893
- assessment_id: biogenesis-limit
  area: evidence
  topic: Ontology-derived attachment wording versus observed membrane development
  outcome: unknown
  target_ids:
  - GO:0030075
  summary: The target reproduces current GO wording accurately. Huokko distinguishes
    proximity/thylapse-like contacts from direct membrane connection or fusion and
    leaves origin models unresolved. This review does not infer obligatory membrane
    continuity, universal plasma-membrane budding, or validated membrane tethers in
    every cyanobacterium from that wording.
  evidence_ids:
  - record
  - thylakoid-agent-go
  - thylakoid-agent-jats-PMC8190092
  - thylakoid-agent-perez2024-browser-introduction
- assessment_id: provenance-completeness
  area: completeness
  topic: Evidence identity, discussion scope and bounded inventory
  outcome: supported
  target_ids:
  - GO:0030075
  summary: All cited DOIs resolve to the intended works. The native ontology supports
    the resolved whole-compartment versus membrane and non-organelle decisions. The
    record has no image or protein-example assertions. Additional respiratory complexes,
    lipid species and detailed biogenesis machinery are not mandatory solely because
    the sources describe them. Historical notes remain historical.
  evidence_ids:
  - record
  - thylakoid-agent-go
  - thylakoid-agent-perez2024-meta
  - thylakoid-agent-casella2017-meta
  - thylakoid-agent-huokko2021-meta
findings:
- finding_id: F1
  issue_key: bacterial_thylakoid-experimental-organism-mismatch
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: The cited primary thylakoid studies used Synechococcus PCC7942, not Synechocystis
    PCC6803
  description: Huokko2021 explicitly performs light-regulated thylakoid biogenesis
    experiments in Synechococcus elongatus PCC7942, whereas canonical_examples[0]
    assigns that experiment to tax1148 Synechocystis PCC6803. Casella2017 likewise
    performs its native membrane organization and mobility experiments in PCC7942,
    but four maintained component/graph source notes call the assayed organism Synechocystis.
    Both papers discuss earlier Synechocystis work, which is not a substitute for
    their own Methods. Reconcile the exemplar taxon, label, note and reference together,
    and correct the repeated Casella organism attributions. The evidence does not
    imply that Synechocystis lacks thylakoids.
  target_ids:
  - GO:0030075
  field_paths:
  - canonical_examples[0]
  - components[0].evidence[1].notes
  - components[3].evidence[1].notes
  - causal_graphs[0].edges[2].evidence[0].notes
  - causal_graphs[0].edges[3].evidence[0].notes
  evidence_ids:
  - record
  - thylakoid-agent-jats-PMC5683893
  - thylakoid-agent-jats-PMC8190092
  - thylakoid-agent-tax-1117
  - thylakoid-agent-tax-1148
  - thylakoid-agent-tax-1140
  normalization_reason: Major because the only canonical experimental example and
    repeated source-specific localization claims transfer evidence between distinct
    genera and strains; the general thylakoid identity remains correct.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/bacterial_thylakoid.yaml
    role: maintained scientific record
actions:
- action_id: A1
  description: Align the canonical experimental example and all Casella source notes
    with the actually assayed strain, or provide a separate direct source for the
    retained Synechocystis claim.
  finding_ids:
  - F1
  target_ids:
  - GO:0030075
  acceptance_checks:
  - Huokko2021 is assigned to Synechococcus elongatus PCC7942 with a native-verified
    taxon identifier, or the Synechocystis example receives an appropriate direct
    study.
  - All four Casella membrane-localization notes identify PCC7942 rather than transferring
    its observations to PCC6803.
  - Keep light-adaptation context and source uncertainty; do not rewrite historical
    curation entries or infer absence of thylakoids in either organism.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/bacterial_thylakoid.yaml
    role: maintained scientific record
limitations:
- Casella2017 and Huokko2021 were read in genuine JATS bodies at the declared sections.
  No figure pixels, raw microscopy, raw proteomics, supplements or complete Methods
  audits were performed.
- Perez-Boerema2024 native publisher routes returned403. Actual publisher Introduction
  and Electron Transport Chain Complexes passages were read through preserved browser
  captures; these are secondary review evidence, not a complete full-text audit or
  native HTTP200.
- Native GO retains plasma-membrane-derived/attached language. The primary biogenesis
  study does not establish universal fusion or a single origin mechanism; proximity,
  membrane contacts and continuity remain distinct.
- Assembly necessity of individual complexes/lipids and an exhaustive inventory are
  not established. No exact single-protein mapping is required for the represented
  whole-complex rows.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
