# Organellar chromatophore thylakoid membrane scientific review

- Review: 20261022T030055Z-organellar-chromatophore-thylakoid-membrane-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T02:42:21Z
- Finished UTC: 2026-10-22T03:00:55Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

No concrete defect observed in the exact thylakoid-membrane identity, supported parentage, label-only lipid material and source-qualified photosynthetic topology.

## Scope And Provenance

Entire single record: exact identity, all hierarchy/parts, components, taxonomic scope, function, every graph edge, source notes, history and discussions.

Selection: Target 7 of batch36 in strict uncovered path order from fresh origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0070118 | data/structures/membrane_organelle/organellar_chromatophore_thylakoid_membrane.yaml | maintained | organellar chromatophore thylakoid membrane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0070118 | Focused validator passed. |
| Focused native strict | passed | True | GO:0070118 | Focused validator passed. |
| Native graph protein-reference check | passed | True | GO:0070118 | Native focused graph check passed; graph assertions reviewed separately. |
| Expression-module applicability | not_applicable | False | GO:0070118 | No named expression-module or regulator inference is asserted; no structured individual protein instance or gene-symbol field requires verification. |
| Claim-level scientific review | passed | True | GO:0070118 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0070118 | 9 of 9 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0070118 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0070118 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0070118 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0070118 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0070118 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact whole membrane

identity: supported. Targets: GO:0070118.

GO0070118 and its exact synonym identify the lipid-bilayer membrane of the chromatophore thylakoid. Membrane parthood and enclosed lumen identity remain distinct.

### Explicit native classifications

grounding: supported. Targets: GO:0070118.

GO is_a ancestry supplies generic thylakoid membrane and organellar chromatophore membrane; SL0356 additionally supplies plastid-thylakoid-membrane isA SL0216/GO0055035. This supports all maintained parent classes without inventing a missing GO relation.

### Label-only lipid constituent

grounding: supported. Targets: GO:0070118.

The LIPID row describes the collective lipid bilayer material and explicitly separates it from the whole-membrane GO/SL identity. No whole-membrane CURIE is used as chemical grounding. ESSENTIAL expresses the constitutive bilayer requirement of this bilayer-defined structure, not necessity of every individual lipid or protein species.

### Source-backed photosynthetic site

evidence: supported. Targets: GO:0070118.

The function and corresponding graph edge cite SL0356 for light-reaction complexes. GO0070118 is restricted to the membrane definition. This is a positive example of appropriate source separation for the same biological context.

### Two descriptive edges

graph: supported. Targets: GO:0070118.

Membrane bounds the lumen and supports light-reaction complexes; both statements have exact current source support. NONMECHANISTIC scope does not imply a complete photosystem or electron-transport inventory.

### Bounded genus context

scope: supported. Targets: GO:0070118.

The verified genus and explicit VARIABLE note preserve photosynthetic-lineage limits without implying all Paulinella carry this membrane.

### Entire bounded target

completeness: supported. Targets: GO:0070118.

All current fields, history and any discussions were read. The target has no maintained image, protein accession, exact stoichiometry or quantitative physical measurement; no optional inventory is invented.

### Experimental necessity of individual molecules

evidence: unknown. Targets: GO:0070118.

The collective bilayer is constitutive of this bilayer-defined membrane. The retained sources do not establish experimentally that an individual lipid or protein species is necessary for membrane formation; no individual depletion or reconstitution result is inferred.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/organellar_chromatophore_thylakoid_membrane.yaml; Entire maintained target, all history, components, every graph edge and discussions | context_only | Complete target read, retaining boundary distinctions and historical context; no scientific content changed. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, ComponentTypeEnum, EssentialityEnum, StructureCategoryEnum and StructureKindEnum | context_only | A structural membrane identity is distinct from a molecular lipid identity. Constitutive material necessity is distinct from individual lipid/protein depletion. Repository MEMBRANE_ORGANELLE category expressly includes thylakoids. |
| root36-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070116,GO:0070117,GO:0070118,GO:0009579,GO:0070111,GO:0019684,GO:0031978,GO:0042651,GO:0055035,GO:0070112; Complete results GO0070116/17/18,0009579,0070111,0019684,0031978,0042651,0055035,0070112 | supports | All ten active native term entries read, including definitions, exact synonym scopes, comments and relation-labelled children. Thylakoid, enclosed lumen and whole bilayer membrane are distinct identities. GO0070118 defines the membrane compartment without the light-reaction-complex phrase. |
| root36-sources-GO0070118-isa | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070118/ancestors?relations=is_a; Complete results requested with relations=is_a | supports | The complete is_a-only ancestry for GO0070118 includes GO0042651 thylakoid membrane and GO0070112 organellar chromatophore membrane, and lacks GO0055035 plastid thylakoid membrane. The plastid-specific classification is assessed separately against the positive SL0356 hierarchy. |
| root36-sources-SL0356 | https://rest.uniprot.org/locations/SL-0356.json; Complete native JSON, including nested isA and partOf entries | supports | Exact native location ID, name, definition, GO mapping and all nested isA/partOf entries were read. The source explicitly supplies the plastid-thylakoid classification and Paulinella context; protein statistics are not a constituent inventory or prevalence count. |
| root36-sources-tax39716 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/39716; Complete native taxId, scientificName, rank, lineage and names | supports | Native ENA confirms taxId39716 as the genus Paulinella. Taxonomic identity alone does not establish occurrence frequency. |
| schema-result | just validate data/structures/membrane_organelle/organellar_chromatophore_thylakoid_membrane.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/organellar_chromatophore_thylakoid_membrane.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/organellar_chromatophore_thylakoid_membrane.yaml --out /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/organellar_chromatophore_thylakoid_membrane-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/organellar_chromatophore_thylakoid_membrane.yaml --out /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/organellar_chromatophore_thylakoid_membrane-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch36-20261022-i5iwb5rr/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/organellar_chromatophore_thylakoid_membrane-strict.tsv |
| native-causal | /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/organellar_chromatophore_thylakoid_membrane.yaml; Complete native focused graph protein-reference log; zero GENE_OR_PROTEIN nodes | supports | <br>causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes<br> |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/organellar_chromatophore_thylakoid_membrane.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 9 of 9 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- No individual lipid species, protein requirement, stoichiometry, quantitative occurrence estimate, raw image or omics reanalysis is established. Optional molecular inventory is not fabricated.
- GO0070112 definition emphasizes surrounding envelope bilayers, yet its typed children/is_a ancestry include the thylakoid membrane. The target follows the positive native hierarchy; this source-level definition/hierarchy tension is not silently converted into a corpus error.
- Formation necessity is supported at the collective bilayer-definition level only. No depletion/reconstitution experiment or individual molecular requirement is inferred.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The user explicitly authorizes a bundle for every uncovered record, including honest zero-finding observations.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T030055Z-organellar-chromatophore-thylakoid-membrane-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Organellar chromatophore thylakoid membrane scientific review
started_at: '2026-10-22T02:42:21Z'
finished_at: '2026-10-22T03:00:55Z'
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
summary: No concrete defect observed in the exact thylakoid-membrane identity, supported
  parentage, label-only lipid material and source-qualified photosynthetic topology.
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
  - path: data/structures/membrane_organelle/organellar_chromatophore_thylakoid_membrane.yaml
    sha256: 67a0433476fdb5ca77a1a30bb921d4d80603a5ae1c61869162edf87f07d6364b
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
- target_id: GO:0070118
  path: data/structures/membrane_organelle/organellar_chromatophore_thylakoid_membrane.yaml
  label: organellar chromatophore thylakoid membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/organellar_chromatophore_thylakoid_membrane.yaml
    role: maintained scientific record
scope:
  description: 'Entire single record: exact identity, all hierarchy/parts, components,
    taxonomic scope, function, every graph edge, source notes, history and discussions.'
  selection: Target 7 of batch36 in strict uncovered path order from fresh origin/main
    f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0070118
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0070118
  command: just validate data/structures/membrane_organelle/organellar_chromatophore_thylakoid_membrane.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0070118
  command: just validate-strict data/structures/membrane_organelle/organellar_chromatophore_thylakoid_membrane.yaml
    --out /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/organellar_chromatophore_thylakoid_membrane-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal
  name: Native graph protein-reference check
  status: passed
  required: true
  target_ids:
  - GO:0070118
  command: /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/organellar_chromatophore_thylakoid_membrane.yaml
  exit_code: 0
  summary: Native focused graph check passed; graph assertions reviewed separately.
  evidence_ids:
  - native-causal
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0070118
  summary: No named expression-module or regulator inference is asserted; no structured
    individual protein instance or gene-symbol field requires verification.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0070118
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - root36-sources-go
  - root36-sources-GO0070118-isa
  - root36-sources-SL0356
  - root36-sources-tax39716
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0070118
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
  - GO:0070118
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
  - GO:0070118
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
  - GO:0070118
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
  - GO:0070118
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
  - GO:0070118
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
  reference: data/structures/membrane_organelle/organellar_chromatophore_thylakoid_membrane.yaml
  locator: Entire maintained target, all history, components, every graph edge and
    discussions
  accessed_at: '2026-10-22T02:53:38Z'
  support: context_only
  summary: Complete target read, retaining boundary distinctions and historical context;
    no scientific content changed.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, ComponentTypeEnum, EssentialityEnum, StructureCategoryEnum
    and StructureKindEnum
  accessed_at: '2026-10-22T02:53:38Z'
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
- evidence_id: root36-sources-GO0070118-isa
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070118/ancestors?relations=is_a
  locator: Complete results requested with relations=is_a
  accessed_at: '2026-10-22T02:44:35.511706Z'
  support: supports
  summary: The complete is_a-only ancestry for GO0070118 includes GO0042651 thylakoid
    membrane and GO0070112 organellar chromatophore membrane, and lacks GO0055035
    plastid thylakoid membrane. The plastid-specific classification is assessed separately
    against the positive SL0356 hierarchy.
  snapshot_sha256: 964663439387924de7f28043478cf2e40ffbc6a9f9516a5965227e537d1e92be
- evidence_id: root36-sources-SL0356
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0356.json
  locator: Complete native JSON, including nested isA and partOf entries
  accessed_at: '2026-10-22T02:44:36.279604Z'
  support: supports
  summary: Exact native location ID, name, definition, GO mapping and all nested isA/partOf
    entries were read. The source explicitly supplies the plastid-thylakoid classification
    and Paulinella context; protein statistics are not a constituent inventory or
    prevalence count.
  snapshot_sha256: fd631a05c9cdbdd6ee8bc4fa220ede8d59ad460cdaecbc15e98f38709d644934
- evidence_id: root36-sources-tax39716
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/39716
  locator: Complete native taxId, scientificName, rank, lineage and names
  accessed_at: '2026-10-22T02:44:36.288230Z'
  support: supports
  summary: Native ENA confirms taxId39716 as the genus Paulinella. Taxonomic identity
    alone does not establish occurrence frequency.
  snapshot_sha256: d856236448b790cbfd8b00f609d7e21c8e64e5089856db686023a316e91f16ef
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/organellar_chromatophore_thylakoid_membrane.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:42:23Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/organellar_chromatophore_thylakoid_membrane.yaml'
  snapshot_sha256: b1aae1de42296f1395c637576f4959d20dfa48363eac24ced789dae1ce7165b7
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/organellar_chromatophore_thylakoid_membrane.yaml
    --out /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/organellar_chromatophore_thylakoid_membrane-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:42:24Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/organellar_chromatophore_thylakoid_membrane.yaml\
    \ --out /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/organellar_chromatophore_thylakoid_membrane-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch36-20261022-i5iwb5rr/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/organellar_chromatophore_thylakoid_membrane-strict.tsv"
  snapshot_sha256: 3ce2cf89587da54d789c547e7a6ea952037296a14e436b0172a838f7b8aa8fb3
- evidence_id: native-causal
  kind: validation
  reference: /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/organellar_chromatophore_thylakoid_membrane.yaml
  locator: Complete native focused graph protein-reference log; zero GENE_OR_PROTEIN
    nodes
  accessed_at: '2026-10-22T02:52:22.234171Z'
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
  locator: data/structures/membrane_organelle/organellar_chromatophore_thylakoid_membrane.yaml;
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
  topic: Exact whole membrane
  outcome: supported
  target_ids:
  - GO:0070118
  summary: GO0070118 and its exact synonym identify the lipid-bilayer membrane of
    the chromatophore thylakoid. Membrane parthood and enclosed lumen identity remain
    distinct.
  evidence_ids:
  - record
  - root36-sources-go
  - root36-sources-SL0356
- assessment_id: hierarchy
  area: grounding
  topic: Explicit native classifications
  outcome: supported
  target_ids:
  - GO:0070118
  summary: GO is_a ancestry supplies generic thylakoid membrane and organellar chromatophore
    membrane; SL0356 additionally supplies plastid-thylakoid-membrane isA SL0216/GO0055035.
    This supports all maintained parent classes without inventing a missing GO relation.
  evidence_ids:
  - record
  - root36-sources-go
  - root36-sources-GO0070118-isa
  - root36-sources-SL0356
- assessment_id: material
  area: grounding
  topic: Label-only lipid constituent
  outcome: supported
  target_ids:
  - GO:0070118
  summary: The LIPID row describes the collective lipid bilayer material and explicitly
    separates it from the whole-membrane GO/SL identity. No whole-membrane CURIE is
    used as chemical grounding. ESSENTIAL expresses the constitutive bilayer requirement
    of this bilayer-defined structure, not necessity of every individual lipid or
    protein species.
  evidence_ids:
  - record
  - schema
  - root36-sources-go
  - root36-sources-SL0356
- assessment_id: function
  area: evidence
  topic: Source-backed photosynthetic site
  outcome: supported
  target_ids:
  - GO:0070118
  summary: The function and corresponding graph edge cite SL0356 for light-reaction
    complexes. GO0070118 is restricted to the membrane definition. This is a positive
    example of appropriate source separation for the same biological context.
  evidence_ids:
  - record
  - root36-sources-go
  - root36-sources-SL0356
- assessment_id: graph
  area: graph
  topic: Two descriptive edges
  outcome: supported
  target_ids:
  - GO:0070118
  summary: Membrane bounds the lumen and supports light-reaction complexes; both statements
    have exact current source support. NONMECHANISTIC scope does not imply a complete
    photosystem or electron-transport inventory.
  evidence_ids:
  - record
  - root36-sources-go
  - root36-sources-SL0356
- assessment_id: scope
  area: scope
  topic: Bounded genus context
  outcome: supported
  target_ids:
  - GO:0070118
  summary: The verified genus and explicit VARIABLE note preserve photosynthetic-lineage
    limits without implying all Paulinella carry this membrane.
  evidence_ids:
  - record
  - root36-sources-tax39716
  - root36-sources-SL0356
- assessment_id: coverage
  area: completeness
  topic: Entire bounded target
  outcome: supported
  target_ids:
  - GO:0070118
  summary: All current fields, history and any discussions were read. The target has
    no maintained image, protein accession, exact stoichiometry or quantitative physical
    measurement; no optional inventory is invented.
  evidence_ids:
  - record
  - schema
  - root36-sources-go
  - root36-sources-SL0356
- assessment_id: individual-formation
  area: evidence
  topic: Experimental necessity of individual molecules
  outcome: unknown
  target_ids:
  - GO:0070118
  summary: The collective bilayer is constitutive of this bilayer-defined membrane.
    The retained sources do not establish experimentally that an individual lipid
    or protein species is necessary for membrane formation; no individual depletion
    or reconstitution result is inferred.
  evidence_ids:
  - record
  - schema
  - root36-sources-go
  - root36-sources-SL0356
findings: []
actions: []
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- No individual lipid species, protein requirement, stoichiometry, quantitative occurrence
  estimate, raw image or omics reanalysis is established. Optional molecular inventory
  is not fabricated.
- GO0070112 definition emphasizes surrounding envelope bilayers, yet its typed children/is_a
  ancestry include the thylakoid membrane. The target follows the positive native
  hierarchy; this source-level definition/hierarchy tension is not silently converted
  into a corpus error.
- Formation necessity is supported at the collective bilayer-definition level only.
  No depletion/reconstitution experiment or individual molecular requirement is inferred.
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
