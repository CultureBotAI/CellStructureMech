# Organellar chromatophore thylakoid scientific review

- Review: 20261022T030053Z-organellar-chromatophore-thylakoid-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T02:42:17Z
- Finished UTC: 2026-10-22T03:00:53Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact thylakoid identity, topology and photosynthetic context are supported. One major finding corrects whole-membrane LIPID typing; one minor finding corrects the GO light-complex attribution.

## Scope And Provenance

Entire single record: exact identity, all hierarchy/parts, components, taxonomic scope, function, every graph edge, source notes, history and discussions.

Selection: Target 5 of batch36 in strict uncovered path order from fresh origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0070116 | data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml | maintained | organellar chromatophore thylakoid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0070116 | Focused validator passed. |
| Focused native strict | passed | True | GO:0070116 | Focused validator passed. |
| Native graph protein-reference check | passed | True | GO:0070116 | Native focused graph check passed; graph assertions reviewed separately. |
| Expression-module applicability | not_applicable | False | GO:0070116 | No named expression-module or regulator inference is asserted; no structured individual protein instance or gene-symbol field requires verification. |
| Claim-level scientific review | passed | True | GO:0070116 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0070116 | 9 of 9 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0070116 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0070116 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0070116 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0070116 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0070116 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact thylakoid and parts

identity: supported. Targets: GO:0070116.

GO0070116 exactly denotes the thylakoid within the chromatophore. Native is_a supports GO0009579, while relation-labelled children separately support lumen/membrane parthood. The target is a membrane-bounded compartment in the repository category that explicitly includes thylakoids.

### Whole membrane misclassified as lipid

grounding: concern. Targets: GO:0070116.

The single component labels and grounds the whole thylakoid membrane GO0070118 while assigning LIPID. Its structural graph node joins this row. This is a material type/identity error; accurate membrane parthood and function do not identify a chemical lipid.

### Photosynthetic site and citation placement

evidence: concern. Targets: GO:0070116.

SL0354 directly supports the light-reaction-complex function, with independent primary thylakoid/PSI evidence. The component and one edge instead attribute this phrase to GO0070118, which supplies only the bilayer definition; the biology is supported but this precise attribution is overstated.

### Species and culture context

scope: supported. Targets: GO:0070116.

The maintained P.chromatophora example and qualitative COMMON note are consistent with the primary CCAC0185 observations and secondary species description. This is not a census of all isolates or an assertion that all Paulinella species carry chromatophores.

### Three descriptive topology/function edges

graph: supported. Targets: GO:0070116.

The membrane bounds the lumen and is part of the thylakoid; its photosynthetic role is supported at the descriptive level. The NONMECHANISTIC graph does not assert complete photosystem composition or assembly machinery. Its component join and source note need the two bounded corrections already identified.

### Entire bounded target

completeness: supported. Targets: GO:0070116.

All current fields, history and any discussions were read. The target has no maintained image, protein accession, exact stoichiometry or quantitative physical measurement; no optional inventory is invented.

## Findings

### F1: Separate whole membrane identity from lipid material

major / open / confirmed; issue key: chromatophore-thylakoid-whole-membrane-lipid.

The LIPID component is labelled and grounded to the entire organellar chromatophore thylakoid membrane GO0070118. The graph structural node carries a component_ref to this row. GO identifies a whole anatomical membrane, not a lipid entity.

### F2: Use the source that establishes the light-complex claim

minor / open / confirmed; issue key: chromatophore-thylakoid-go-light-complex-attribution.

The component and photosynthesis edge say GO0070118 defines a membrane carrying light-reaction complexes. Its native definition identifies only the bilayer compartment. SL0354 already cited by the function, and the independently inspected Nowack2012 primary study, support the biological statement.

## Recommended Actions And Acceptance Checks

### A1

Preserve supported membrane topology. Retain a whole structural constituent with an appropriate type, or describe supported lipid material separately with exact chemical grounding or justified reviewed-label-only status; align the component_ref accordingly.

- Verify each amended type and source note against the exact native definition or primary passage.
- After separately authorized curation, run focused schema, strict, graph and label validation.

### A2

Restrict the GO note to its membrane definition and attach the light-complex claim to SL0354 and/or the relevant primary thylakoid photosystem evidence.

- Verify each amended type and source note against the exact native definition or primary passage.
- After separately authorized curation, run focused schema, strict, graph and label validation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml; Entire maintained target, all history, components, every graph edge and discussions | context_only | Complete target read, retaining boundary distinctions and historical context; no scientific content changed. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, ComponentTypeEnum, EssentialityEnum, StructureCategoryEnum and StructureKindEnum | context_only | A structural membrane identity is distinct from a molecular lipid identity. Constitutive material necessity is distinct from individual lipid/protein depletion. Repository MEMBRANE_ORGANELLE category expressly includes thylakoids. |
| root36-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070116,GO:0070117,GO:0070118,GO:0009579,GO:0070111,GO:0019684,GO:0031978,GO:0042651,GO:0055035,GO:0070112; Complete results GO0070116/17/18,0009579,0070111,0019684,0031978,0042651,0055035,0070112 | supports | All ten active native term entries read, including definitions, exact synonym scopes, comments and relation-labelled children. Thylakoid, enclosed lumen and whole bilayer membrane are distinct identities. GO0070118 defines the membrane compartment without the light-reaction-complex phrase. |
| root36-sources-GO0070116-isa | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070116/ancestors?relations=is_a; Complete results requested with relations=is_a | supports | The complete is_a-only ancestry for GO0070116 includes GO0009579 thylakoid. This single-term response supports the maintained generic thylakoid parent; containment is assessed separately. |
| root36-sources-SL0354 | https://rest.uniprot.org/locations/SL-0354.json; Complete native JSON, including nested isA and partOf entries | supports | Exact native location ID, name, definition, GO mapping and all nested isA/partOf entries were read. The source explicitly supplies the plastid-thylakoid classification and Paulinella context; protein statistics are not a constituent inventory or prevalence count. |
| root36-sources-tax39717 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/39717; Complete native taxId, scientificName, rank, lineage and names | supports | Native ENA confirms taxId39717 as the species Paulinella chromatophora. Taxonomic identity alone does not establish occurrence frequency. |
| root36-shared-nowack2014-crossref | https://api.crossref.org/works/10.5586/asbp.2014.049; message.DOI/title/author/published/link; bibliographic metadata only | supports | Crossref verifies the exact 2014 DOI/title, Eva C.M.Nowack and publisher PDF locator. Bibliographic identity is checked independently of article readability. |
| root36-shared-nowack2012-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1073/pnas.1118800109; Complete native bibliographic identity and abstractText | supports | Exact native MED identity, title, DOI10.1073/pnas.1118800109, PMID22371600, authors and complete abstract verified. |
| root36-shared-nowack2012-pmc | https://pmc.ncbi.nlm.nih.gov/articles/3325729/; Verified article title/DOI; complete Results sec2/3/4 including Fig1/2/3 captions, Methods sec14/16/19. Remaining sections, figure pixels and supplements not certified read here | supports | In P.chromatophora CCAC0185, immunogold localization places PsaE over thylakoids; PSI isolation identifies PsaE/PsaK subunits, and inhibitor/radiolabel experiments support cytoplasmic synthesis and import. These directly support thylakoid photosystem context without proving a complete import pathway. |
| root36-shared-gabr2020-pmc | https://pmc.ncbi.nlm.nih.gov/articles/7734844/; Verified title/DOI; complete S2 The Paulinella Model with Fig1 caption. Remaining sections, figure pixels and supplements not certified read here | supports | This secondary review describes the photosynthetic P.chromatophora species and distinguishes other photosynthetic Paulinella from heterotrophic relatives. It supports bounded taxonomic context, not a numerical species prevalence. |
| schema-result | just validate data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml --out /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/organellar_chromatophore_thylakoid-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml --out /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/organellar_chromatophore_thylakoid-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch36-20261022-i5iwb5rr/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/organellar_chromatophore_thylakoid-strict.tsv |
| native-causal | /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml; Complete native focused graph protein-reference log; zero GENE_OR_PROTEIN nodes | supports | <br>causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes<br> |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 9 of 9 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- No individual lipid species, protein requirement, stoichiometry, quantitative occurrence estimate, raw image or omics reanalysis is established. Optional molecular inventory is not fabricated.
- Nowack2014 was verified bibliographically. Native publisher routes returned empty HTTP500 and the retained public mirror returned401. A transient browser extraction exposed opening text but could not be retained/retrieved consistently; it is not used as reviewed full-body evidence here. The stated species/thylakoid context was independently checked against the retained 2012 primary body and 2020 secondary review.
- GO0009579 comments that thylakoids are not organelles, while GO0070116 ancestry includes a non-membrane-bounded-organelle class and the repository MEMBRANE_ORGANELLE category explicitly includes thylakoids. This terminology conflict is retained as a classification limitation, not treated as proof that the physically membrane-bounded target has the wrong identity.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The user explicitly authorizes a bundle for every uncovered record, including honest zero-finding observations.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T030053Z-organellar-chromatophore-thylakoid-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Organellar chromatophore thylakoid scientific review
started_at: '2026-10-22T02:42:17Z'
finished_at: '2026-10-22T03:00:53Z'
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
summary: Exact thylakoid identity, topology and photosynthetic context are supported.
  One major finding corrects whole-membrane LIPID typing; one minor finding corrects
  the GO light-complex attribution.
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
  - path: data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml
    sha256: 6ce01ac746d2a475719c41e8eea903b510d96648cff04a1338248feb3558731a
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
- target_id: GO:0070116
  path: data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml
  label: organellar chromatophore thylakoid
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml
    role: maintained scientific record
scope:
  description: 'Entire single record: exact identity, all hierarchy/parts, components,
    taxonomic scope, function, every graph edge, source notes, history and discussions.'
  selection: Target 5 of batch36 in strict uncovered path order from fresh origin/main
    f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0070116
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0070116
  command: just validate data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0070116
  command: just validate-strict data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml
    --out /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/organellar_chromatophore_thylakoid-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal
  name: Native graph protein-reference check
  status: passed
  required: true
  target_ids:
  - GO:0070116
  command: /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml
  exit_code: 0
  summary: Native focused graph check passed; graph assertions reviewed separately.
  evidence_ids:
  - native-causal
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0070116
  summary: No named expression-module or regulator inference is asserted; no structured
    individual protein instance or gene-symbol field requires verification.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0070116
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - root36-sources-go
  - root36-sources-GO0070116-isa
  - root36-sources-SL0354
  - root36-sources-tax39717
  - root36-shared-nowack2014-crossref
  - root36-shared-nowack2012-meta
  - root36-shared-nowack2012-pmc
  - root36-shared-gabr2020-pmc
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0070116
  summary: 9 of 9 collected target identifiers returned OK. No residuals. Native source
    checks are separately scoped; skipped or unreachable identifiers are not silently
    counted as resolved.
  evidence_ids:
  - target-curies
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0070116
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch36 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0070116
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch36 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0070116
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch36 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0070116
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch36 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0070116
  command: just check-curies-strict
  exit_code: 0
  summary: 'Exit0. Native resolver control: every resolver accepts a known id and
    rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE.
    Transport failures and skipped prefixes are not proof of identifier resolution;
    exact target residuals are assessed separately.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:34Z to
    2026-10-22T01:34:04Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch36 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml
  locator: Entire maintained target, all history, components, every graph edge and
    discussions
  accessed_at: '2026-10-22T02:53:27Z'
  support: context_only
  summary: Complete target read, retaining boundary distinctions and historical context;
    no scientific content changed.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, ComponentTypeEnum, EssentialityEnum, StructureCategoryEnum
    and StructureKindEnum
  accessed_at: '2026-10-22T02:53:27Z'
  support: context_only
  summary: A structural membrane identity is distinct from a molecular lipid identity.
    Constitutive material necessity is distinct from individual lipid/protein depletion.
    Repository MEMBRANE_ORGANELLE category expressly includes thylakoids.
- evidence_id: root36-sources-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070116,GO:0070117,GO:0070118,GO:0009579,GO:0070111,GO:0019684,GO:0031978,GO:0042651,GO:0055035,GO:0070112
  locator: Complete results GO0070116/17/18,0009579,0070111,0019684,0031978,0042651,0055035,0070112
  accessed_at: '2026-10-22T02:44:35.510156Z'
  support: supports
  summary: All ten active native term entries read, including definitions, exact synonym
    scopes, comments and relation-labelled children. Thylakoid, enclosed lumen and
    whole bilayer membrane are distinct identities. GO0070118 defines the membrane
    compartment without the light-reaction-complex phrase.
  snapshot_sha256: 642f9e6750fd0be63dd96aa3dc1623f673a56abbce933097292a33b051b42443
- evidence_id: root36-sources-GO0070116-isa
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070116/ancestors?relations=is_a
  locator: Complete results requested with relations=is_a
  accessed_at: '2026-10-22T02:44:35.511204Z'
  support: supports
  summary: The complete is_a-only ancestry for GO0070116 includes GO0009579 thylakoid.
    This single-term response supports the maintained generic thylakoid parent; containment
    is assessed separately.
  snapshot_sha256: 2a2f77cbbdf186428226847de78ed299545c690fbf53f5cb7d42e2eddbe9f08d
- evidence_id: root36-sources-SL0354
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0354.json
  locator: Complete native JSON, including nested isA and partOf entries
  accessed_at: '2026-10-22T02:44:35.511844Z'
  support: supports
  summary: Exact native location ID, name, definition, GO mapping and all nested isA/partOf
    entries were read. The source explicitly supplies the plastid-thylakoid classification
    and Paulinella context; protein statistics are not a constituent inventory or
    prevalence count.
  snapshot_sha256: a4810ddcc1c8f3cbb0e2162c5b38ab395c056ca74c7774f1ec075ede165e3903
- evidence_id: root36-sources-tax39717
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/39717
  locator: Complete native taxId, scientificName, rank, lineage and names
  accessed_at: '2026-10-22T02:44:36.289679Z'
  support: supports
  summary: Native ENA confirms taxId39717 as the species Paulinella chromatophora.
    Taxonomic identity alone does not establish occurrence frequency.
  snapshot_sha256: 11763b1d5106d7c4445bbe97d3755f012b4a6ddb4d806de48dfbbcec488f56f3
- evidence_id: root36-shared-nowack2014-crossref
  kind: database
  reference: https://api.crossref.org/works/10.5586/asbp.2014.049
  locator: message.DOI/title/author/published/link; bibliographic metadata only
  accessed_at: '2026-10-22T02:41:59.235726Z'
  support: supports
  summary: Crossref verifies the exact 2014 DOI/title, Eva C.M.Nowack and publisher
    PDF locator. Bibliographic identity is checked independently of article readability.
  snapshot_sha256: 7a5635c186a67f8d0f6b1eebbe0d69651d31f4f794592f79583b8106e2e2e16d
- evidence_id: root36-shared-nowack2012-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1073/pnas.1118800109
  locator: Complete native bibliographic identity and abstractText
  accessed_at: '2026-10-22T02:37:48.587487Z'
  support: supports
  summary: Exact native MED identity, title, DOI10.1073/pnas.1118800109, PMID22371600,
    authors and complete abstract verified.
  snapshot_sha256: 8f62b9fd80b8ca0fc14ec7ba0953bc2fb5becd33876f6d27bd7f6cd5198d364b
- evidence_id: root36-shared-nowack2012-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/3325729/
  locator: Verified article title/DOI; complete Results sec2/3/4 including Fig1/2/3
    captions, Methods sec14/16/19. Remaining sections, figure pixels and supplements
    not certified read here
  accessed_at: '2026-10-22T02:39:41.676639Z'
  support: supports
  summary: In P.chromatophora CCAC0185, immunogold localization places PsaE over thylakoids;
    PSI isolation identifies PsaE/PsaK subunits, and inhibitor/radiolabel experiments
    support cytoplasmic synthesis and import. These directly support thylakoid photosystem
    context without proving a complete import pathway.
  snapshot_sha256: df4b05048ab13ce50055bc6357bdc95ef2a5195af3269700d7b791f514864c94
- evidence_id: root36-shared-gabr2020-pmc
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/7734844/
  locator: Verified title/DOI; complete S2 The Paulinella Model with Fig1 caption.
    Remaining sections, figure pixels and supplements not certified read here
  accessed_at: '2026-10-22T02:39:41.678213Z'
  support: supports
  summary: This secondary review describes the photosynthetic P.chromatophora species
    and distinguishes other photosynthetic Paulinella from heterotrophic relatives.
    It supports bounded taxonomic context, not a numerical species prevalence.
  snapshot_sha256: 4cb5e9956e00937ea3f62ff80af921075a27b1cd6951c7d460b530c200993396
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:42:18Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml'
  snapshot_sha256: 30cb8e3b1851b89327899789f73e3b449dd058c4eacda1b813c73e43a59dd9f2
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml
    --out /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/organellar_chromatophore_thylakoid-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:42:19Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml\
    \ --out /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/organellar_chromatophore_thylakoid-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch36-20261022-i5iwb5rr/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/organellar_chromatophore_thylakoid-strict.tsv"
  snapshot_sha256: 353eeaecff5df8317709153f84ebd56055170b5695571fbf762c3fec4d1b255d
- evidence_id: native-causal
  kind: validation
  reference: /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml
  locator: Complete native focused graph protein-reference log; zero GENE_OR_PROTEIN
    nodes
  accessed_at: '2026-10-22T02:52:21.382232Z'
  support: supports
  summary: "\ncausal_graphs GENE_OR_PROTEIN node summary:\n     0  COVERED       \
    \            component_ref target holds protein_examples covering all declared\
    \ symbols\n     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     0\
    \  total GENE_OR_PROTEIN causal nodes\n"
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml;
    native collect() exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 9 of 9 collected target identifiers returned OK. No residuals. Native source
    checks are separately scoped; skipped or unreachable identifiers are not silently
    counted as resolved.
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
  topic: Exact thylakoid and parts
  outcome: supported
  target_ids:
  - GO:0070116
  summary: GO0070116 exactly denotes the thylakoid within the chromatophore. Native
    is_a supports GO0009579, while relation-labelled children separately support lumen/membrane
    parthood. The target is a membrane-bounded compartment in the repository category
    that explicitly includes thylakoids.
  evidence_ids:
  - record
  - schema
  - root36-sources-go
  - root36-sources-GO0070116-isa
  - root36-sources-SL0354
- assessment_id: component
  area: grounding
  topic: Whole membrane misclassified as lipid
  outcome: concern
  target_ids:
  - GO:0070116
  summary: The single component labels and grounds the whole thylakoid membrane GO0070118
    while assigning LIPID. Its structural graph node joins this row. This is a material
    type/identity error; accurate membrane parthood and function do not identify a
    chemical lipid.
  evidence_ids:
  - record
  - schema
  - root36-sources-go
- assessment_id: function
  area: evidence
  topic: Photosynthetic site and citation placement
  outcome: concern
  target_ids:
  - GO:0070116
  summary: SL0354 directly supports the light-reaction-complex function, with independent
    primary thylakoid/PSI evidence. The component and one edge instead attribute this
    phrase to GO0070118, which supplies only the bilayer definition; the biology is
    supported but this precise attribution is overstated.
  evidence_ids:
  - record
  - root36-sources-go
  - root36-sources-SL0354
  - root36-shared-nowack2012-pmc
- assessment_id: scope
  area: scope
  topic: Species and culture context
  outcome: supported
  target_ids:
  - GO:0070116
  summary: The maintained P.chromatophora example and qualitative COMMON note are
    consistent with the primary CCAC0185 observations and secondary species description.
    This is not a census of all isolates or an assertion that all Paulinella species
    carry chromatophores.
  evidence_ids:
  - record
  - root36-sources-tax39717
  - root36-shared-nowack2012-pmc
  - root36-shared-gabr2020-pmc
  - root36-shared-nowack2014-crossref
  - root36-shared-nowack2012-meta
- assessment_id: graph
  area: graph
  topic: Three descriptive topology/function edges
  outcome: supported
  target_ids:
  - GO:0070116
  summary: The membrane bounds the lumen and is part of the thylakoid; its photosynthetic
    role is supported at the descriptive level. The NONMECHANISTIC graph does not
    assert complete photosystem composition or assembly machinery. Its component join
    and source note need the two bounded corrections already identified.
  evidence_ids:
  - record
  - root36-sources-go
  - root36-sources-SL0354
  - root36-shared-nowack2012-pmc
- assessment_id: coverage
  area: completeness
  topic: Entire bounded target
  outcome: supported
  target_ids:
  - GO:0070116
  summary: All current fields, history and any discussions were read. The target has
    no maintained image, protein accession, exact stoichiometry or quantitative physical
    measurement; no optional inventory is invented.
  evidence_ids:
  - record
  - schema
  - root36-sources-go
  - root36-sources-SL0354
findings:
- finding_id: F1
  issue_key: chromatophore-thylakoid-whole-membrane-lipid
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Separate whole membrane identity from lipid material
  description: The LIPID component is labelled and grounded to the entire organellar
    chromatophore thylakoid membrane GO0070118. The graph structural node carries
    a component_ref to this row. GO identifies a whole anatomical membrane, not a
    lipid entity.
  target_ids:
  - GO:0070116
  field_paths:
  - components[0].component_type
  - components[0].grounding
  - causal_graphs[0].nodes[1].component_ref
  evidence_ids:
  - record
  - schema
  - root36-sources-go
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:components and narrow evidence placement
  native_severity: major
  normalization_reason: Major whole-structure versus molecular-type mismatch.
- finding_id: F2
  issue_key: chromatophore-thylakoid-go-light-complex-attribution
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Use the source that establishes the light-complex claim
  description: The component and photosynthesis edge say GO0070118 defines a membrane
    carrying light-reaction complexes. Its native definition identifies only the bilayer
    compartment. SL0354 already cited by the function, and the independently inspected
    Nowack2012 primary study, support the biological statement.
  target_ids:
  - GO:0070116
  field_paths:
  - components[0].evidence[0].notes
  - causal_graphs[0].edges[1].evidence[0].notes
  evidence_ids:
  - record
  - root36-sources-go
  - root36-sources-SL0354
  - root36-shared-nowack2012-pmc
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:components and narrow evidence placement
  native_severity: minor
  normalization_reason: Minor bounded source-attribution error; photosynthetic biology
    itself has positive support.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0070116
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml
    role: maintained scientific record
  description: Preserve supported membrane topology. Retain a whole structural constituent
    with an appropriate type, or describe supported lipid material separately with
    exact chemical grounding or justified reviewed-label-only status; align the component_ref
    accordingly.
  acceptance_checks:
  - Verify each amended type and source note against the exact native definition or
    primary passage.
  - After separately authorized curation, run focused schema, strict, graph and label
    validation.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0070116
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml
    role: maintained scientific record
  description: Restrict the GO note to its membrane definition and attach the light-complex
    claim to SL0354 and/or the relevant primary thylakoid photosystem evidence.
  acceptance_checks:
  - Verify each amended type and source note against the exact native definition or
    primary passage.
  - After separately authorized curation, run focused schema, strict, graph and label
    validation.
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- No individual lipid species, protein requirement, stoichiometry, quantitative occurrence
  estimate, raw image or omics reanalysis is established. Optional molecular inventory
  is not fabricated.
- Nowack2014 was verified bibliographically. Native publisher routes returned empty
  HTTP500 and the retained public mirror returned401. A transient browser extraction
  exposed opening text but could not be retained/retrieved consistently; it is not
  used as reviewed full-body evidence here. The stated species/thylakoid context was
  independently checked against the retained 2012 primary body and 2020 secondary
  review.
- GO0009579 comments that thylakoids are not organelles, while GO0070116 ancestry
  includes a non-membrane-bounded-organelle class and the repository MEMBRANE_ORGANELLE
  category explicitly includes thylakoids. This terminology conflict is retained as
  a classification limitation, not treated as proof that the physically membrane-bounded
  target has the wrong identity.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The user explicitly authorizes a bundle for every uncovered record, including honest
  zero-finding observations.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
