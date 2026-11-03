# Cyanelle thylakoid identity, topology and source review

- Review: 20261022T013526Z-cyanelle-thylakoid-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T00:57:22Z
- Finished UTC: 2026-10-22T01:35:26Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

No concrete curation defect established. Exact identity, hierarchy, membrane/lumen boundary, model occurrence and descriptive graph scope are supported within the inspected source limits.

## Scope And Provenance

Complete single maintained target: identity, category/kind, hierarchy, components and necessity where present, taxa, functions, all graph claims, evidence, discussions and history.

Selection: Batch26 index1; one exact maintained target selected in strict path order at fresh base f97b1abe. No neighboring record supplies scientific evidence for this review.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0009843 | data/structures/membrane_organelle/cyanelle_thylakoid.yaml | maintained | cyanelle thylakoid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Protein identity and causal gene nodes | not_applicable | False | GO:0009843 | The entire target contains no named protein examples, gene symbols or GENE_OR_PROTEIN nodes. A protein accession/member check is not applicable. |
| Expression-module applicability | not_applicable | False | GO:0009843 | No gene, regulator, stress, transcriptomic dataset or expression-module inference occurs in this structure/topology target. |
| Focused native schema | passed | True | GO:0009843 | Focused validator passed. |
| Focused native strict | passed | True | GO:0009843 | Focused validator passed. |
| Claim-level scientific review | passed | True | GO:0009843 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0009843 | 13 of 13 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0009843 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0009843 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0009843 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0009843 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0009843 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact structure, hierarchy and part boundaries

identity: supported. Targets: GO:0009843.

GO0009843 and SL0277 denote the internal cyanelle thylakoid system. Whole membrane-bounded structure, lumen and bounding membrane remain distinct. Both parent entries are valid is-a ancestors, cyanelle parthood and both exact parts are supported. The fresh new-base added membrane-to-thylakoid parthood edge agrees with the direct GO0009843 child relation.

### Exact constituent bilayer and unknown assembly necessity

grounding: supported. Targets: GO:0009843.

The LIPID row denotes the actual constituent cyanelle-thylakoid bilayer at GO0033115, not an arbitrary protein or the whole lumen. UNKNOWN essentiality avoids importing a specific molecular assembly requirement; no stoichiometry or exhaustive protein inventory is asserted.

### Glaucophyte identity and Cyanophora model context

scope: supported. Targets: GO:0009843.

Native taxonomy verifies the exact species and class labels. GO and nested SL cyanelle definitions establish characteristic glaucophyte anatomy; Giddings directly studies the named C. paradoxa model, with internal thylakoids in intact cells and isolated preparations. COMMON is supported as characteristic anatomy rather than a measured census. The publication does not establish identical numbers or molecular composition at every life stage.

### Every topology and functional-site edge

graph: supported. Targets: GO:0009843.

All three NONMECHANISTIC edges are supported: membrane bounds lumen, supports the light-reaction site, and is part of the thylakoid. The newly added parthood edge is source-backed in the fresh target. Descriptive site support is not presented as a full photosystem mechanism.

### Photosynthetic light-reaction site

evidence: supported. Targets: GO:0009843.

The exact function GO0019684 and native descriptions of photosynthetic internal membranes support the stated site role. Giddings microscopy corroborates architecture and phycobilisome association; it is not treated as a quantitative photosynthetic assay or proof of every light-reaction intermediate.

### Primary reading scope and native ownership

evidence: supported. Targets: GO:0009843.

The sole cited paper has exact native bibliographic identity and retained genuine published scans. Culture/preparation context and actual scanned-page extents remain explicit. All source claims are paraphrases; the target has no verbatim snippet, published image, quantitative physical-property value, named protein accession or trait link requiring additional verification. Historical curation/search claims are not re-certified.

### Bounded full-record audit

completeness: supported. Targets: GO:0009843.

Every maintained field, graph edge, discussion and history entry was read. No concrete curation defect was established. Additional molecular inventories, kinetic properties or mechanisms are optional and must not be invented to fill slots. This review makes no exhaustive literature or ontology-absence claim.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/cyanelle_thylakoid.yaml; Entire maintained YAML, every evidence note, component, function, graph edge, discussion and history entry | context_only | The complete target was read after native inspection. No maintained scientific content, native status or history was changed. Historical correction claims are not recertified as independent evidence. |
| policy | docs/CURATION.md; Structure versus material identity, narrow claim evidence and assembly-necessity guidance | context_only | Constituent membership, function and necessity for formation are distinct. Optional inventories do not require adding unsupported molecular detail. |
| thylakoid-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009843,GO:0009842,GO:0009579,GO:0031976,GO:0033114,GO:0033115,GO:0031978,GO:0042651,GO:0055035,GO:0019684; Complete ten-term IDs, names, active flags, definitions, synonyms and direct child/relation fields | supports | All ten returned GO terms are active and match their exact IDs and definitions. Direct child edges establish cyanelle-thylakoid is-a plastid-thylakoid, plastid-thylakoid is-a thylakoid, cyanelle-thylakoid part-of cyanelle, and lumen/membrane part-of cyanelle-thylakoid. Plastid lumen/membrane parentage and the broader membrane parent are explicit. Broader two-step is-a ancestry is not misreported as a direct edge. The light-reaction term identifies the photosynthetic process, not an experiment performed in this source. |
| thylakoid-agent-SL-0277 | https://rest.uniprot.org/locations/SL-0277.json; Top-level exact ID/name/definition/GO cross-reference; isA and partOf entries and their relevant nested definitions | supports | Exact GO0009843 mapping, plastid-thylakoid isA and cyanelle partOf. The definition identifies internal interconnected photosynthetic membranes; nested cyanelle definition specifies glaucocystophyte algae. |
| thylakoid-agent-SL-0084 | https://rest.uniprot.org/locations/SL-0084.json; Top-level exact ID/name/definition/GO cross-reference; isA and partOf entries and their relevant nested definitions | supports | Exact GO0033114 mapping, plastid-thylakoid-lumen isA and cyanelle-thylakoid partOf. The definition identifies the compartment bounded by thylakoid membranes; it does not identify the bounding bilayer as lumen contents. |
| thylakoid-agent-SL-0085 | https://rest.uniprot.org/locations/SL-0085.json; Top-level exact ID/name/definition/GO cross-reference; isA and partOf entries and their relevant nested definitions | supports | Exact GO0033115 mapping, plastid-thylakoid-membrane isA and cyanelle-thylakoid partOf. The definition identifies a lipid bilayer within a glaucocystophyte cyanelle, distinct from lumen and whole thylakoid. |
| thylakoid-agent-tax2762 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2762; Exact taxId, scientificName, rank, lineage and otherNames; original batch25 receipt preserved | supports | Native ENA taxonomy identifies Cyanophora paradoxa as species2762 and places Glaucocystophyceae in its lineage. This taxon response alone does not measure structural frequency or identify an experimental stock. |
| thylakoid-agent-tax38254 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/38254; Exact taxId, scientificName, rank, lineage and otherNames; original batch25 receipt preserved | supports | Native ENA taxonomy identifies class38254 Glaucocystophyceae, with Glaucophyta and Glaucophyceae as synonyms. This class response alone does not measure structural frequency. |
| thylakoid-agent-doi-10.1104_pp.71.2.409 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1104/pp.71.2.409%22; Complete source MED bibliographic fields and indexed abstract; original batch25 receipt preserved | supports | Exact DOI10.1104/pp.71.2.409 and PMID16662839 identify Giddings, Wasmann and Staehelin1983, Structure of the Thylakoids and Envelope Membranes of the Cyanelles of Cyanophora paradoxa. Complete indexed abstract describes thylakoid/phycobilisome and envelope microscopy. Main-text reading is separately attached to original scans. |
| thylakoid-agent-giddings1983-page409 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/6ed041edd2c7/plntphys00558-0203.png; Original published page 409 PNG: Title, abstract, visible Introduction and first culture-method paragraph. Pixels directly viewed; original UTC/SHA preserved. | supports | The original page identifies the study and C. paradoxa UTEX LB555 culture at26C. The review does not generalize exact strain or preparation conditions into a species-wide experimental assertion. |
| thylakoid-agent-giddings1983-page410 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/8d99de19802c/plntphys00558-0204.png; Original published page 410 PNG: Fig1–3 original images and captions; visible preparation methods. Pixels directly viewed; original UTC/SHA preserved. | supports | Whole-cell and isolated-cyanelle/thylakoid images distinguish the internal thylakoid system from the envelope. Isolated preparations and intact-cell context are kept distinct; no independent image measurement is made. |
| thylakoid-agent-giddings1983-page411 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/e0e22d1a8212/plntphys00558-0205.png; Original published page 411 PNG: Fig4–5 original plots and captions; visible preparation/EM methods. Pixels directly viewed; original UTC/SHA preserved. | supports | Particle-size histograms and absorption spectra compare isolated thylakoids with attached or removed phycobiliproteins. These are structural/preparation observations; no numeric value or photosynthetic rate is imported into the record. |
| thylakoid-agent-giddings1983-page412 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/392b5bf89308/plntphys00558-0206.png; Original published page 412 PNG: Complete visible Results introduction and Thylakoids subsection; Fig6/caption and EM-method continuation. Pixels directly viewed; original UTC/SHA preserved. | supports | Intact-cell sections and isolated preparations support internal thylakoids. The body describes distinct thylakoid fracture faces and surface phycobilisomes in retained versus washed preparations. The record does not assert the paper's particle dimensions or a specific photosystem molecular assignment. |
| thylakoid-agent-giddings1983-page413 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/fa8191742d8c/plntphys00558-0207.png; Original published page 413 PNG: Original Fig7–10 image panels and complete captions. Pixels directly viewed; original UTC/SHA preserved. | supports | Thin-section and freeze-etch images/captions identify thylakoids with associated phycobilisomes and the changes following phycobiliprotein removal. This supports the structural context without reconstructing an electron-transfer mechanism. |
| thylakoid-agent-giddings1983-page416 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/c329334d81e0/plntphys00558-0210.png; Original published page 416 PNG: Visible Discussion thylakoid/phycobilisome paragraphs; envelope Results continuation and Fig15. Pixels directly viewed; original UTC/SHA preserved. | supports | Discussion compares cyanelle thylakoid organization with cyanobacterial/red-algal photosynthetic membranes. Structural resemblance is kept separate from proof of every molecular composition or activity claim. |
| thylakoid-agent-giddings1983-page417 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/7694ed6a7a74/plntphys00558-0211.png; Original published page 417 PNG: Visible Discussion continuation including Envelope Membranes; Fig16–18 captions. Pixels directly viewed; original UTC/SHA preserved. | supports | The inner envelope membrane is distinguished from internal thylakoids. Historical organelle/endosymbiont speculation is not used to override modern authority identity. |
| thylakoid-agent-giddings1983-page418 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/147bb64bab4f/plntphys00558-0212.png; Original published page 418 PNG: Fig19 schematic and complete caption; surrounding reference list not audited. Pixels directly viewed; original UTC/SHA preserved. | supports | The published interpretive thylakoid/phycobilisome model labels the membrane faces and surface complexes. It is an interpretation of the paper's structural observations, not an independent experimental mechanism or a modern complete subunit inventory. |
| schema-result | just validate data/structures/membrane_organelle/cyanelle_thylakoid.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/cyanelle_thylakoid.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/cyanelle_thylakoid.yaml --out /private/tmp/cellstructure-batch26-20261022-bheOrM1P/cyanelle_thylakoid-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/cyanelle_thylakoid.yaml --out /private/tmp/cellstructure-batch26-20261022-bheOrM1P/cyanelle_thylakoid-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch26-20261022-bheOrM1P/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch26-20261022-bheOrM1P/cyanelle_thylakoid-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/cyanelle_thylakoid.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 13 of 13 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Full coverage concerns one target, not a systematic census of glaucophytes or all membrane molecules. Model-specific UTEX LB555 microscopy is not a quantitative frequency survey.
- Giddings primary scans409,410,411,412,413,416,417,418 were directly viewed at stated locators. Page414 was also viewed previously for envelope context but is not separate evidence here; page419 was not read. Numeric plots and microscopy were not remeasured. Historical photosystem particle assignments and endosymbiont-status speculation are not adopted as modern mechanistic or identity evidence.
- Current GO/SL structure and process definitions support descriptive topology and functional-site classification; they are not new experimental assembly-necessity assays.
- No local neighboring record or previous review verdict supplies scientific evidence. External receipts retain their actual original URLs, UTC times and hashes.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; no old-base gate is applied.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The user explicitly authorized one review for every uncovered record, including clean reviews. No scientific record or immutable saved review is changed.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T013526Z-cyanelle-thylakoid-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Cyanelle thylakoid identity, topology and source review
started_at: '2026-10-22T00:57:22Z'
finished_at: '2026-10-22T01:35:26Z'
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
summary: No concrete curation defect established. Exact identity, hierarchy, membrane/lumen
  boundary, model occurrence and descriptive graph scope are supported within the
  inspected source limits.
source:
  git_revision: f97b1abe2d78971b6f66b9083087d7a94cf3c0cc
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
  - path: data/structures/membrane_organelle/cyanelle_thylakoid.yaml
    sha256: 19838578792948bb527b33a0dd61374b6ee7a688eb2ee0406426c2e95639c7e3
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
- target_id: GO:0009843
  path: data/structures/membrane_organelle/cyanelle_thylakoid.yaml
  label: cyanelle thylakoid
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cyanelle_thylakoid.yaml
    role: maintained scientific record
scope:
  description: 'Complete single maintained target: identity, category/kind, hierarchy,
    components and necessity where present, taxa, functions, all graph claims, evidence,
    discussions and history.'
  selection: Batch26 index1; one exact maintained target selected in strict path order
    at fresh base f97b1abe. No neighboring record supplies scientific evidence for
    this review.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0009843
checks:
- check_id: protein-examples
  name: Protein identity and causal gene nodes
  status: not_applicable
  required: false
  target_ids:
  - GO:0009843
  summary: The entire target contains no named protein examples, gene symbols or GENE_OR_PROTEIN
    nodes. A protein accession/member check is not applicable.
  evidence_ids:
  - record
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0009843
  summary: No gene, regulator, stress, transcriptomic dataset or expression-module
    inference occurs in this structure/topology target.
  evidence_ids:
  - record
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0009843
  command: just validate data/structures/membrane_organelle/cyanelle_thylakoid.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0009843
  command: just validate-strict data/structures/membrane_organelle/cyanelle_thylakoid.yaml
    --out /private/tmp/cellstructure-batch26-20261022-bheOrM1P/cyanelle_thylakoid-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0009843
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - thylakoid-agent-go
  - thylakoid-agent-SL-0277
  - thylakoid-agent-SL-0084
  - thylakoid-agent-SL-0085
  - thylakoid-agent-tax2762
  - thylakoid-agent-tax38254
  - thylakoid-agent-doi-10.1104_pp.71.2.409
  - thylakoid-agent-giddings1983-page409
  - thylakoid-agent-giddings1983-page410
  - thylakoid-agent-giddings1983-page411
  - thylakoid-agent-giddings1983-page412
  - thylakoid-agent-giddings1983-page413
  - thylakoid-agent-giddings1983-page416
  - thylakoid-agent-giddings1983-page417
  - thylakoid-agent-giddings1983-page418
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0009843
  summary: 13 of 13 collected target identifiers returned OK. No residuals. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.
  evidence_ids:
  - target-curies
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0009843
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in this fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input. It is not a scientific review
    of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0009843
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in this fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input. It is not a scientific review
    of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0009843
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in this fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input. It is not a scientific review
    of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0009843
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in this fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input. It is not a scientific review
    of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0009843
  command: just check-curies-strict
  exit_code: 0
  summary: 'Exit0. Native resolver control: every resolver accepts a known id and
    rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE.
    Transport failures and skipped prefixes are not proof of identifier resolution;
    exact target residuals are assessed separately.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:34Z to
    2026-10-22T01:34:04Z in this fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input. It is not a scientific review
    of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/cyanelle_thylakoid.yaml
  locator: Entire maintained YAML, every evidence note, component, function, graph
    edge, discussion and history entry
  accessed_at: '2026-10-22T01:04:57Z'
  support: context_only
  summary: The complete target was read after native inspection. No maintained scientific
    content, native status or history was changed. Historical correction claims are
    not recertified as independent evidence.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Structure versus material identity, narrow claim evidence and assembly-necessity
    guidance
  accessed_at: '2026-10-22T01:04:57Z'
  support: context_only
  summary: Constituent membership, function and necessity for formation are distinct.
    Optional inventories do not require adding unsupported molecular detail.
- evidence_id: thylakoid-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009843,GO:0009842,GO:0009579,GO:0031976,GO:0033114,GO:0033115,GO:0031978,GO:0042651,GO:0055035,GO:0019684
  locator: Complete ten-term IDs, names, active flags, definitions, synonyms and direct
    child/relation fields
  accessed_at: '2026-10-22T01:03:48.873190Z'
  support: supports
  summary: All ten returned GO terms are active and match their exact IDs and definitions.
    Direct child edges establish cyanelle-thylakoid is-a plastid-thylakoid, plastid-thylakoid
    is-a thylakoid, cyanelle-thylakoid part-of cyanelle, and lumen/membrane part-of
    cyanelle-thylakoid. Plastid lumen/membrane parentage and the broader membrane
    parent are explicit. Broader two-step is-a ancestry is not misreported as a direct
    edge. The light-reaction term identifies the photosynthetic process, not an experiment
    performed in this source.
  snapshot_sha256: 80a3716fe3cbefb29f0605ef8c411af5924fd206d86f2c0d0df65861ac476fbb
- evidence_id: thylakoid-agent-SL-0277
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0277.json
  locator: Top-level exact ID/name/definition/GO cross-reference; isA and partOf entries
    and their relevant nested definitions
  accessed_at: '2026-10-22T01:03:48.872376Z'
  support: supports
  summary: Exact GO0009843 mapping, plastid-thylakoid isA and cyanelle partOf. The
    definition identifies internal interconnected photosynthetic membranes; nested
    cyanelle definition specifies glaucocystophyte algae.
  snapshot_sha256: df24a25f56576fb322f032647d7a00c7e40087a5631bc78579f0392d613a66cf
- evidence_id: thylakoid-agent-SL-0084
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0084.json
  locator: Top-level exact ID/name/definition/GO cross-reference; isA and partOf entries
    and their relevant nested definitions
  accessed_at: '2026-10-22T01:03:48.873945Z'
  support: supports
  summary: Exact GO0033114 mapping, plastid-thylakoid-lumen isA and cyanelle-thylakoid
    partOf. The definition identifies the compartment bounded by thylakoid membranes;
    it does not identify the bounding bilayer as lumen contents.
  snapshot_sha256: 1d9d5a21592a2b0e9cc7199aeabcf70e6d0740dd5f390522ed6881f8c24a00f3
- evidence_id: thylakoid-agent-SL-0085
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0085.json
  locator: Top-level exact ID/name/definition/GO cross-reference; isA and partOf entries
    and their relevant nested definitions
  accessed_at: '2026-10-22T01:03:48.874286Z'
  support: supports
  summary: Exact GO0033115 mapping, plastid-thylakoid-membrane isA and cyanelle-thylakoid
    partOf. The definition identifies a lipid bilayer within a glaucocystophyte cyanelle,
    distinct from lumen and whole thylakoid.
  snapshot_sha256: 521b00e6f6978134d8516bb2234fc24c1ccc8e96da88735660076a3ef99ce4e4
- evidence_id: thylakoid-agent-tax2762
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2762
  locator: Exact taxId, scientificName, rank, lineage and otherNames; original batch25
    receipt preserved
  accessed_at: '2026-10-21T11:21:45.924999Z'
  support: supports
  summary: Native ENA taxonomy identifies Cyanophora paradoxa as species2762 and places
    Glaucocystophyceae in its lineage. This taxon response alone does not measure
    structural frequency or identify an experimental stock.
  snapshot_sha256: 285d213ba479ce1d232bf54aac3efda6f16d45546b5ce13284818fc16482408a
- evidence_id: thylakoid-agent-tax38254
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/38254
  locator: Exact taxId, scientificName, rank, lineage and otherNames; original batch25
    receipt preserved
  accessed_at: '2026-10-21T11:21:46.530610Z'
  support: supports
  summary: Native ENA taxonomy identifies class38254 Glaucocystophyceae, with Glaucophyta
    and Glaucophyceae as synonyms. This class response alone does not measure structural
    frequency.
  snapshot_sha256: 4b487eb0e34bcb4941fbb315aae5214c96ea6f60255d71a2aca172cd35844009
- evidence_id: thylakoid-agent-doi-10.1104_pp.71.2.409
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1104/pp.71.2.409%22
  locator: Complete source MED bibliographic fields and indexed abstract; original
    batch25 receipt preserved
  accessed_at: '2026-10-21T11:21:14.649813Z'
  support: supports
  summary: Exact DOI10.1104/pp.71.2.409 and PMID16662839 identify Giddings, Wasmann
    and Staehelin1983, Structure of the Thylakoids and Envelope Membranes of the Cyanelles
    of Cyanophora paradoxa. Complete indexed abstract describes thylakoid/phycobilisome
    and envelope microscopy. Main-text reading is separately attached to original
    scans.
  snapshot_sha256: 63e06e7891bc1f0bf83152a34ce823faa160c98bf984757e546f4acb00f202dc
- evidence_id: thylakoid-agent-giddings1983-page409
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/6ed041edd2c7/plntphys00558-0203.png
  locator: 'Original published page 409 PNG: Title, abstract, visible Introduction
    and first culture-method paragraph. Pixels directly viewed; original UTC/SHA preserved.'
  accessed_at: '2026-10-22T00:53:33.924113Z'
  support: supports
  summary: The original page identifies the study and C. paradoxa UTEX LB555 culture
    at26C. The review does not generalize exact strain or preparation conditions into
    a species-wide experimental assertion.
  snapshot_sha256: c0184058c66810b2544be1af57fac9acc2bbbfcdf71ee1186aade8232e5c9f61
- evidence_id: thylakoid-agent-giddings1983-page410
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/8d99de19802c/plntphys00558-0204.png
  locator: 'Original published page 410 PNG: Fig1–3 original images and captions;
    visible preparation methods. Pixels directly viewed; original UTC/SHA preserved.'
  accessed_at: '2026-10-22T00:53:33.924991Z'
  support: supports
  summary: Whole-cell and isolated-cyanelle/thylakoid images distinguish the internal
    thylakoid system from the envelope. Isolated preparations and intact-cell context
    are kept distinct; no independent image measurement is made.
  snapshot_sha256: ba0bd01ef58d44879c8f7b2689f79f5066039cef904b15a32330a611681812c0
- evidence_id: thylakoid-agent-giddings1983-page411
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/e0e22d1a8212/plntphys00558-0205.png
  locator: 'Original published page 411 PNG: Fig4–5 original plots and captions; visible
    preparation/EM methods. Pixels directly viewed; original UTC/SHA preserved.'
  accessed_at: '2026-10-22T00:53:33.926010Z'
  support: supports
  summary: Particle-size histograms and absorption spectra compare isolated thylakoids
    with attached or removed phycobiliproteins. These are structural/preparation observations;
    no numeric value or photosynthetic rate is imported into the record.
  snapshot_sha256: 04c8112a5bdb0baf084cf2bbe18bdab02f401d99b64e56123a9408dcac13afc5
- evidence_id: thylakoid-agent-giddings1983-page412
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/392b5bf89308/plntphys00558-0206.png
  locator: 'Original published page 412 PNG: Complete visible Results introduction
    and Thylakoids subsection; Fig6/caption and EM-method continuation. Pixels directly
    viewed; original UTC/SHA preserved.'
  accessed_at: '2026-10-22T00:53:33.926387Z'
  support: supports
  summary: Intact-cell sections and isolated preparations support internal thylakoids.
    The body describes distinct thylakoid fracture faces and surface phycobilisomes
    in retained versus washed preparations. The record does not assert the paper's
    particle dimensions or a specific photosystem molecular assignment.
  snapshot_sha256: 9c033e4b190ed1cd62006b88fa8961e80608056e79e1ec0fc45040e3bb19f47f
- evidence_id: thylakoid-agent-giddings1983-page413
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/fa8191742d8c/plntphys00558-0207.png
  locator: 'Original published page 413 PNG: Original Fig7–10 image panels and complete
    captions. Pixels directly viewed; original UTC/SHA preserved.'
  accessed_at: '2026-10-22T00:53:33.926810Z'
  support: supports
  summary: Thin-section and freeze-etch images/captions identify thylakoids with associated
    phycobilisomes and the changes following phycobiliprotein removal. This supports
    the structural context without reconstructing an electron-transfer mechanism.
  snapshot_sha256: 304f4c6eeb11b196e20f2e557df93393f410b032f1a7c1c5f62cf699ca9430d5
- evidence_id: thylakoid-agent-giddings1983-page416
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/c329334d81e0/plntphys00558-0210.png
  locator: 'Original published page 416 PNG: Visible Discussion thylakoid/phycobilisome
    paragraphs; envelope Results continuation and Fig15. Pixels directly viewed; original
    UTC/SHA preserved.'
  accessed_at: '2026-10-22T00:53:34.247595Z'
  support: supports
  summary: Discussion compares cyanelle thylakoid organization with cyanobacterial/red-algal
    photosynthetic membranes. Structural resemblance is kept separate from proof of
    every molecular composition or activity claim.
  snapshot_sha256: 41f820c6bde6abc4318ac32baa45293634543bb4aceb0dc5129c3d25414e91ef
- evidence_id: thylakoid-agent-giddings1983-page417
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/7694ed6a7a74/plntphys00558-0211.png
  locator: 'Original published page 417 PNG: Visible Discussion continuation including
    Envelope Membranes; Fig16–18 captions. Pixels directly viewed; original UTC/SHA
    preserved.'
  accessed_at: '2026-10-22T00:53:34.248245Z'
  support: supports
  summary: The inner envelope membrane is distinguished from internal thylakoids.
    Historical organelle/endosymbiont speculation is not used to override modern authority
    identity.
  snapshot_sha256: 276c1cb60d1a909200199f8e24495840d2caa5f5131c8a896d3f97d70e5bcf6f
- evidence_id: thylakoid-agent-giddings1983-page418
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/147bb64bab4f/plntphys00558-0212.png
  locator: 'Original published page 418 PNG: Fig19 schematic and complete caption;
    surrounding reference list not audited. Pixels directly viewed; original UTC/SHA
    preserved.'
  accessed_at: '2026-10-22T00:53:34.263940Z'
  support: supports
  summary: The published interpretive thylakoid/phycobilisome model labels the membrane
    faces and surface complexes. It is an interpretation of the paper's structural
    observations, not an independent experimental mechanism or a modern complete subunit
    inventory.
  snapshot_sha256: 53bb97a831bd4188d8c67250adbeae16a40c0df97c26f61c6417debe30e83e53
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/cyanelle_thylakoid.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T00:57:25Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/cyanelle_thylakoid.yaml'
  snapshot_sha256: 93deb71161ffe5d5c9b82a0683e6a08097282e92863b006cdd17e262f941fa89
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/cyanelle_thylakoid.yaml
    --out /private/tmp/cellstructure-batch26-20261022-bheOrM1P/cyanelle_thylakoid-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T00:57:27Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/cyanelle_thylakoid.yaml\
    \ --out /private/tmp/cellstructure-batch26-20261022-bheOrM1P/cyanelle_thylakoid-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch26-20261022-bheOrM1P/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch26-20261022-bheOrM1P/cyanelle_thylakoid-strict.tsv"
  snapshot_sha256: 5550bc91c8c134a665d368f40fd7da4087cfbd23e3fb4a0ef03e9a209f96436e
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/cyanelle_thylakoid.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 13 of 13 collected target identifiers returned OK. No residuals. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.
  snapshot_sha256: 173c367ec1621e2a96027e149b5cad9f4db0a86f0a3c916455ce192a9aa5f428
- evidence_id: global-qc-result
  kind: validation
  reference: just qc
  locator: Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02
  accessed_at: '2026-10-22T01:05:35Z'
  support: supports
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  snapshot_sha256: 8696c0d603149cee93ac200eaa3ed26c84320204285cd22cca542eb1ae7ba572
- evidence_id: global-history-result
  kind: validation
  reference: just validate-history
  locator: Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02
  accessed_at: '2026-10-22T00:58:37Z'
  support: supports
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  snapshot_sha256: 98a7952c42add0416633f4dee73ff64331e5c6c4c4c8d707e98a152f04fc5b6d
- evidence_id: global-products-result
  kind: validation
  reference: just validate-products
  locator: Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02
  accessed_at: '2026-10-22T00:59:14Z'
  support: supports
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  snapshot_sha256: b5cc67214f5627a654e75cfc335d77d42113d057091884a12094aa1a71447a5e
- evidence_id: global-traits-result
  kind: validation
  reference: just check-trait-links --check
  locator: Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02
  accessed_at: '2026-10-22T00:58:40Z'
  support: supports
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  snapshot_sha256: 6eab64b59433928ec8e0df9b0046dbccf479c84bb0911c315feebc344d536007
- evidence_id: global-curies-result
  kind: validation
  reference: just check-curies-strict
  locator: Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 'Exit0. Native resolver control: every resolver accepts a known id and
    rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE.
    Transport failures and skipped prefixes are not proof of identifier resolution;
    exact target residuals are assessed separately.'
  snapshot_sha256: 00cc5664a9143235d28fb9885fc5c43a8a78c9a9c9f47603b1232e1eddddeac1
assessments:
- assessment_id: identity
  area: identity
  topic: Exact structure, hierarchy and part boundaries
  outcome: supported
  target_ids:
  - GO:0009843
  summary: GO0009843 and SL0277 denote the internal cyanelle thylakoid system. Whole
    membrane-bounded structure, lumen and bounding membrane remain distinct. Both
    parent entries are valid is-a ancestors, cyanelle parthood and both exact parts
    are supported. The fresh new-base added membrane-to-thylakoid parthood edge agrees
    with the direct GO0009843 child relation.
  evidence_ids:
  - thylakoid-agent-go
  - thylakoid-agent-SL-0277
  - thylakoid-agent-SL-0084
  - thylakoid-agent-SL-0085
  - record
- assessment_id: component
  area: grounding
  topic: Exact constituent bilayer and unknown assembly necessity
  outcome: supported
  target_ids:
  - GO:0009843
  summary: The LIPID row denotes the actual constituent cyanelle-thylakoid bilayer
    at GO0033115, not an arbitrary protein or the whole lumen. UNKNOWN essentiality
    avoids importing a specific molecular assembly requirement; no stoichiometry or
    exhaustive protein inventory is asserted.
  evidence_ids:
  - thylakoid-agent-go
  - thylakoid-agent-SL-0085
  - record
  - policy
- assessment_id: taxa
  area: scope
  topic: Glaucophyte identity and Cyanophora model context
  outcome: supported
  target_ids:
  - GO:0009843
  summary: Native taxonomy verifies the exact species and class labels. GO and nested
    SL cyanelle definitions establish characteristic glaucophyte anatomy; Giddings
    directly studies the named C. paradoxa model, with internal thylakoids in intact
    cells and isolated preparations. COMMON is supported as characteristic anatomy
    rather than a measured census. The publication does not establish identical numbers
    or molecular composition at every life stage.
  evidence_ids:
  - thylakoid-agent-go
  - thylakoid-agent-SL-0277
  - thylakoid-agent-SL-0084
  - thylakoid-agent-SL-0085
  - thylakoid-agent-tax2762
  - thylakoid-agent-tax38254
  - thylakoid-agent-doi-10.1104_pp.71.2.409
  - thylakoid-agent-giddings1983-page409
  - thylakoid-agent-giddings1983-page410
  - thylakoid-agent-giddings1983-page411
  - thylakoid-agent-giddings1983-page412
  - thylakoid-agent-giddings1983-page413
  - thylakoid-agent-giddings1983-page416
  - thylakoid-agent-giddings1983-page417
  - thylakoid-agent-giddings1983-page418
- assessment_id: graph
  area: graph
  topic: Every topology and functional-site edge
  outcome: supported
  target_ids:
  - GO:0009843
  summary: 'All three NONMECHANISTIC edges are supported: membrane bounds lumen, supports
    the light-reaction site, and is part of the thylakoid. The newly added parthood
    edge is source-backed in the fresh target. Descriptive site support is not presented
    as a full photosystem mechanism.'
  evidence_ids:
  - thylakoid-agent-go
  - thylakoid-agent-SL-0277
  - thylakoid-agent-SL-0084
  - thylakoid-agent-SL-0085
  - record
- assessment_id: function
  area: evidence
  topic: Photosynthetic light-reaction site
  outcome: supported
  target_ids:
  - GO:0009843
  summary: The exact function GO0019684 and native descriptions of photosynthetic
    internal membranes support the stated site role. Giddings microscopy corroborates
    architecture and phycobilisome association; it is not treated as a quantitative
    photosynthetic assay or proof of every light-reaction intermediate.
  evidence_ids:
  - thylakoid-agent-go
  - thylakoid-agent-SL-0277
  - thylakoid-agent-doi-10.1104_pp.71.2.409
  - thylakoid-agent-giddings1983-page409
  - thylakoid-agent-giddings1983-page410
  - thylakoid-agent-giddings1983-page411
  - thylakoid-agent-giddings1983-page412
  - thylakoid-agent-giddings1983-page413
  - thylakoid-agent-giddings1983-page416
  - thylakoid-agent-giddings1983-page417
  - thylakoid-agent-giddings1983-page418
  - record
- assessment_id: sources
  area: evidence
  topic: Primary reading scope and native ownership
  outcome: supported
  target_ids:
  - GO:0009843
  summary: The sole cited paper has exact native bibliographic identity and retained
    genuine published scans. Culture/preparation context and actual scanned-page extents
    remain explicit. All source claims are paraphrases; the target has no verbatim
    snippet, published image, quantitative physical-property value, named protein
    accession or trait link requiring additional verification. Historical curation/search
    claims are not re-certified.
  evidence_ids:
  - thylakoid-agent-doi-10.1104_pp.71.2.409
  - thylakoid-agent-giddings1983-page409
  - thylakoid-agent-giddings1983-page410
  - thylakoid-agent-giddings1983-page411
  - thylakoid-agent-giddings1983-page412
  - thylakoid-agent-giddings1983-page413
  - thylakoid-agent-giddings1983-page416
  - thylakoid-agent-giddings1983-page417
  - thylakoid-agent-giddings1983-page418
  - record
- assessment_id: completeness
  area: completeness
  topic: Bounded full-record audit
  outcome: supported
  target_ids:
  - GO:0009843
  summary: Every maintained field, graph edge, discussion and history entry was read.
    No concrete curation defect was established. Additional molecular inventories,
    kinetic properties or mechanisms are optional and must not be invented to fill
    slots. This review makes no exhaustive literature or ontology-absence claim.
  evidence_ids:
  - thylakoid-agent-go
  - thylakoid-agent-SL-0277
  - thylakoid-agent-SL-0084
  - thylakoid-agent-SL-0085
  - thylakoid-agent-doi-10.1104_pp.71.2.409
  - thylakoid-agent-giddings1983-page409
  - thylakoid-agent-giddings1983-page410
  - thylakoid-agent-giddings1983-page411
  - thylakoid-agent-giddings1983-page412
  - thylakoid-agent-giddings1983-page413
  - thylakoid-agent-giddings1983-page416
  - thylakoid-agent-giddings1983-page417
  - thylakoid-agent-giddings1983-page418
  - record
  - policy
findings: []
actions: []
limitations:
- Full coverage concerns one target, not a systematic census of glaucophytes or all
  membrane molecules. Model-specific UTEX LB555 microscopy is not a quantitative frequency
  survey.
- Giddings primary scans409,410,411,412,413,416,417,418 were directly viewed at stated
  locators. Page414 was also viewed previously for envelope context but is not separate
  evidence here; page419 was not read. Numeric plots and microscopy were not remeasured.
  Historical photosystem particle assignments and endosymbiont-status speculation
  are not adopted as modern mechanistic or identity evidence.
- Current GO/SL structure and process definitions support descriptive topology and
  functional-site classification; they are not new experimental assembly-necessity
  assays.
- No local neighboring record or previous review verdict supplies scientific evidence.
  External receipts retain their actual original URLs, UTC times and hashes.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; no old-base gate is applied.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The user explicitly authorized one review for every uncovered record, including
  clean reviews. No scientific record or immutable saved review is changed.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
