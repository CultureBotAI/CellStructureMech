# Scientific review of organellar chromatophore membrane

- Review: 20261022T030051Z-organellar-chromatophore-membrane-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T02:42:12Z
- Finished UTC: 2026-10-22T03:00:51Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Exact organellar chromatophore membrane identity, taxonomic restriction, constituent scope and nonmechanistic topology are supported. No concrete scientific issue observed; finer molecular identity and formation requirements remain bounded unknowns.

## Scope And Provenance

Entire single maintained target plus the four-record boundary set and whole-chromatophore context, frozen at f97b1abe. All asserted fields and directed edges read; source-specific authority and primary-study scopes are explicit.

Selection: Batch36 fixed strict path-order selection, position 3; one maintained record only. Initial focused inspect/schema/strict passed before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0070112 | data/structures/membrane_organelle/organellar_chromatophore_membrane.yaml | maintained | organellar chromatophore membrane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0070112 | Focused validator passed. |
| Focused native strict | passed | True | GO:0070112 | Focused validator passed. |
| Native focused graph reference check | passed | True | GO:0070112 | Native graph check passed; every graph assertion independently inspected. |
| Protein-example applicability | not_applicable | False | GO:0070112 | Entire target contains no individual protein accession, gene-symbol field or protein-example row requiring UniProt gene verification. |
| Expression-module applicability | not_applicable | False | GO:0070112 | No expression-module or regulon assertion appears in this target. |
| Claim-level scientific review | passed | True | GO:0070112 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0070112 | 8 of 8 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0070112 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0070112 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0070112 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0070112 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0070112 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact identity, hierarchy and parthood

identity: supported. Targets: GO:0070112.

GO0070112/SL0352 identify the generic chromatophore membrane class. Although GO definition wording says surrounding bilayers, its own typed children and SL0352 explicitly include thylakoid membrane in the fallback class. The record faithfully distinguishes this general localization from a particular membrane. GO0030659 parentage is directly returned.

### Verified genus with variable presence

scope: supported. Targets: GO:0070112.

Paulinella genus39716 is exact. The target expressly avoids universal presence across genus members; the reviewed photosynthetic/heterotrophic distinction supports VARIABLE without a numerical prevalence inference. The CCAC0185 primary study is one P.chromatophora culture, not an all-species assay.

### Label-only lipid-bilayer material

grounding: supported. Targets: GO:0070112.

The single LIPID row explicitly denotes the lipid-bilayer constituent, has no whole-membrane GO grounding, and documents REVIEWED_LABEL_ONLY status. The correct anatomical identifiers stay on record/structure nodes. Collective bilayer material is constitutive of this membrane class; optional chemical specificity is not invented.

### Specific assembly requirements remain unmeasured

grounding: unknown. Targets: GO:0070112.

ESSENTIAL can be supported at the defining collective bilayer level. No exact lipid species, enzyme or membrane protein is asserted necessary; the native definitions and inspected primary study do not establish individual molecular formation requirements. This assessment remains unknown at that narrower experimental level.

### Every asserted edge and node boundary

graph: supported. Targets: GO:0070112.

All four NONMECHANISTIC edges faithfully express native containment and subclass scope: generic membrane part_of chromatophore, with inner, outer and thylakoid membranes as narrower classes. The graph is a localization-class explanation, not a claim of which membrane contains an unspecified protein.

### Source placement and authority limits

evidence: supported. Targets: GO:0070112.

The target cites ontology/location authorities for defining anatomy and topology, and those exact source claims were checked. Additional primary and secondary bodies provide bounded biological context; they are not substituted as measurements of composition, species prevalence, membrane origin or assembly necessity. No new function is inferred from a static graph.

### Entire target and explicit open issues

completeness: supported. Targets: GO:0070112.

The complete record, history, synonyms, parentage, material row, taxon note, each graph node/edge and all discussions were reviewed. No individual protein accession, gene-symbol cohort, quantitative physical measurement or maintained image is asserted. The label-only lipid grounding task remains a scoped open issue; optional molecular inventory is not automatically a finding. Historical access notes are preserved as historical statements.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/organellar_chromatophore_membrane.yaml; Entire maintained YAML, including history, all components, authorities, graph nodes/edges and discussions | context_only | Complete target read; maintained scientific content remains unchanged. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent grounding/status; EssentialityEnum; CausalNode and graph scope | context_only | A label-only molecular/material constituent is distinct from substituting a whole membrane location as its chemical identity. Essentiality concerns whether the structure forms without the component; neither mature localization nor catalytic function proves individual assembly necessity. |
| context-organellar_chromatophore | data/structures/membrane_organelle/organellar_chromatophore.yaml; Complete frozen maintained boundary record | context_only | Read as local representation/topology context only, not independent experimental evidence. Whole chromatophore bytes equal the fully read B35 source; the four membrane/space records were fully read in B36. |
| context-organellar_chromatophore_inner_membrane | data/structures/membrane_organelle/organellar_chromatophore_inner_membrane.yaml; Complete frozen maintained boundary record | context_only | Read as local representation/topology context only, not independent experimental evidence. Whole chromatophore bytes equal the fully read B35 source; the four membrane/space records were fully read in B36. |
| context-organellar_chromatophore_intermembrane_space | data/structures/membrane_organelle/organellar_chromatophore_intermembrane_space.yaml; Complete frozen maintained boundary record | context_only | Read as local representation/topology context only, not independent experimental evidence. Whole chromatophore bytes equal the fully read B35 source; the four membrane/space records were fully read in B36. |
| context-organellar_chromatophore_outer_membrane | data/structures/membrane_organelle/organellar_chromatophore_outer_membrane.yaml; Complete frozen maintained boundary record | context_only | Read as local representation/topology context only, not independent experimental evidence. Whole chromatophore bytes equal the fully read B35 source; the four membrane/space records were fully read in B36. |
| chromatophore-boundary-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070111,GO:0070112,GO:0070113,GO:0070114,GO:0070115,GO:0070118,GO:0009527,GO:0009528,GO:0009529,GO:0030659; Complete ten-term results: id/name/definition/synonyms/isObsolete and typed children | supports | All ten requested terms are active and identify the exact chromatophore compartments and stated broader classes. GO0070112 explicitly has GO0070113/14/18 is_a children, GO0030659 has GO0070112 as an is_a child, and GO0070111 has GO0070112/14/15 as part_of children. Absent direct edges are not invented. |
| chromatophore-boundary-agent-GO0070112-isa | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070112/ancestors?relations=is_a; Complete native ancestors response; query relations=is_a, one exact term | supports | The is_a-only ancestor response for GO:0070112 (organellar chromatophore membrane) includes GO:0030659. This response describes only that queried term; containment and unlisted plastid-specific parents are not inferred from it. |
| chromatophore-boundary-agent-SL0352 | https://rest.uniprot.org/locations/SL-0352.json; Top-level id/name/definition/geneOntologies and immediate isA/partOf entries; nested parent GO cross-references | supports | SL0352 maps exactly to GO0070112 and explicitly applies when outer, inner or thylakoid membrane localization is unspecified. Its partOf is chromatophore/GO0070111; isA is plastid membrane/GO0042170, separate from the GO cytoplasmic-vesicle-membrane classification. Its definition restricts the structure to Paulinella species without a frequency census. |
| chromatophore-boundary-agent-SL0351 | https://rest.uniprot.org/locations/SL-0351.json; Complete definition, exact GO0070111 mapping and isA plastid/GO0009536 | supports | The native location authority describes the Paulinella photosynthetic organelle with two surrounding membranes, residual peptidoglycan between them, and internal thylakoids; its isA is plastid. This establishes compartment context, not a biochemical composition or assembly perturbation assay. |
| chromatophore-boundary-agent-tax39716 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/39716; Complete native taxId/scientificName/rank/lineage fields | supports | ENA taxId39716 is Paulinella at genus rank, under Cercozoa/Rhizaria. This verifies the taxon identity; VARIABLE is evaluated against the biological scope separately. |
| chromatophore-boundary-agent-tax39717 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/39717; Complete native taxId/scientificName/rank/lineage fields | supports | ENA taxId39717 is Paulinella chromatophora at species rank. This checks the additional primary-study context, without exporting its strain results to every genus member. |
| chromatophore-boundary-agent-gabr2020-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1111/jpy.13003; Unique native EuropePMC result DOI/id/title/authorString and abstractText | supports | The exact DOI10.1111/jpy.13003, PMID32289879, title and authors identify the secondary review; complete abstract read. |
| chromatophore-boundary-agent-gabr2020-pmc | https://pmc.ncbi.nlm.nih.gov/articles/7734844/; S2 The Paulinella model and Fig1 caption, reread from the retained genuine PMC author-manuscript body; no figure pixels inspected | supports | The secondary review distinguishes photosynthetic Paulinella lineages from heterotrophic relatives lacking chromatophores. Its model-system section supports qualitative variation within the genus; it is not a numerical prevalence study or primary assembly experiment. |
| chromatophore-boundary-agent-nowack2012-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1073/pnas.1118800109; Unique native EuropePMC result identity and complete abstractText | supports | Exact DOI10.1073/pnas.1118800109 and PMID22371600 identify the primary import study; bibliographic fields and complete abstract are retained separately from body scope. |
| chromatophore-boundary-agent-nowack2012-pmc | https://pmc.ncbi.nlm.nih.gov/articles/3325729/; Results sec2 including Fig1 caption and Methods sec14 Strain and Growth Conditions reread in B36. Earlier B35 read scope is not enlarged here; no source figure pixels or supplementary data inspected. | supports | The primary paper examines P.chromatophora CCAC0185 (subisolate M0880/a); sectioned cells show chromatophores with thylakoids and PsaE immunogold labeling. This corroborates the organelle context but does not itself identify a molecular lipid complement or establish formation necessity of an individual envelope constituent. |
| schema-result | just validate data/structures/membrane_organelle/organellar_chromatophore_membrane.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/organellar_chromatophore_membrane.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/organellar_chromatophore_membrane.yaml --out /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/organellar_chromatophore_membrane-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/organellar_chromatophore_membrane.yaml --out /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/organellar_chromatophore_membrane-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch36-20261022-i5iwb5rr/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/organellar_chromatophore_membrane-strict.tsv |
| focused-causal | /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/organellar_chromatophore_membrane.yaml; /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/membrane/causal.log | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/organellar_chromatophore_membrane.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 8 of 8 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- GO and UniProt location classification differ in some broader plastid parent relations; each statement is attributed to its actual authority, without fabricating an absent GO edge.
- No new primary lipid composition, quantitative taxon census, individual molecular assembly-necessity assay, figure-pixel inspection, raw-data reanalysis or supplementary experiment was performed. Additional primary/secondary reading is restricted to the explicit locators.
- The target contains no numerical physical properties or structured protein examples. Label-only molecular specificity and the exact residual-wall identity, where applicable, remain bounded curation questions rather than invented identities.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T030051Z-organellar-chromatophore-membrane-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Scientific review of organellar chromatophore membrane
started_at: '2026-10-22T02:42:12Z'
finished_at: '2026-10-22T03:00:51Z'
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
summary: Exact organellar chromatophore membrane identity, taxonomic restriction,
  constituent scope and nonmechanistic topology are supported. No concrete scientific
  issue observed; finer molecular identity and formation requirements remain bounded
  unknowns.
source:
  git_revision: f97b1abe2d78971b6f66b9083087d7a94cf3c0cc
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
  - path: data/structures/membrane_organelle/organellar_chromatophore.yaml
    sha256: 6e9805392c72104f5f1d6e9ee70767c49f480b22130da0e6f293bcf8f6a1bec0
    role: context
  - path: data/structures/membrane_organelle/organellar_chromatophore_inner_membrane.yaml
    sha256: e3c244a36b1484e5d3ca95aa114de0a719660aa4d76ae1811ed12584b3d72b1e
    role: context
  - path: data/structures/membrane_organelle/organellar_chromatophore_intermembrane_space.yaml
    sha256: f67ae10cda248a93eba761943f430c0ea5e6d4550dcf9514611822866d2c98ed
    role: context
  - path: data/structures/membrane_organelle/organellar_chromatophore_membrane.yaml
    sha256: 179b7a8a2519cb216889baed1305e54b1de332688cbb7bac1c24857f1209a794
    role: target
  - path: data/structures/membrane_organelle/organellar_chromatophore_outer_membrane.yaml
    sha256: f7d415a8e211d48ef9ecf5f0bb1b96a0ac3336c1ce6498d78d9bf0033bce3c11
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
- target_id: GO:0070112
  path: data/structures/membrane_organelle/organellar_chromatophore_membrane.yaml
  label: organellar chromatophore membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/organellar_chromatophore_membrane.yaml
    role: maintained scientific record
scope:
  description: Entire single maintained target plus the four-record boundary set and
    whole-chromatophore context, frozen at f97b1abe. All asserted fields and directed
    edges read; source-specific authority and primary-study scopes are explicit.
  selection: Batch36 fixed strict path-order selection, position 3; one maintained
    record only. Initial focused inspect/schema/strict passed before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0070112
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0070112
  command: just validate data/structures/membrane_organelle/organellar_chromatophore_membrane.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0070112
  command: just validate-strict data/structures/membrane_organelle/organellar_chromatophore_membrane.yaml
    --out /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/organellar_chromatophore_membrane-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: focused-causal
  name: Native focused graph reference check
  status: passed
  required: true
  target_ids:
  - GO:0070112
  command: /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/organellar_chromatophore_membrane.yaml
  exit_code: 0
  summary: Native graph check passed; every graph assertion independently inspected.
  evidence_ids:
  - focused-causal
- check_id: protein-verification
  name: Protein-example applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0070112
  summary: Entire target contains no individual protein accession, gene-symbol field
    or protein-example row requiring UniProt gene verification.
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0070112
  summary: No expression-module or regulon assertion appears in this target.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0070112
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - context-organellar_chromatophore
  - context-organellar_chromatophore_inner_membrane
  - context-organellar_chromatophore_intermembrane_space
  - context-organellar_chromatophore_outer_membrane
  - chromatophore-boundary-agent-go
  - chromatophore-boundary-agent-GO0070112-isa
  - chromatophore-boundary-agent-SL0352
  - chromatophore-boundary-agent-SL0351
  - chromatophore-boundary-agent-tax39716
  - chromatophore-boundary-agent-tax39717
  - chromatophore-boundary-agent-gabr2020-meta
  - chromatophore-boundary-agent-gabr2020-pmc
  - chromatophore-boundary-agent-nowack2012-meta
  - chromatophore-boundary-agent-nowack2012-pmc
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0070112
  summary: 8 of 8 collected target identifiers returned OK. No residuals. Native source
    checks are separately scoped; skipped or unreachable identifiers are not silently
    counted as resolved.
  evidence_ids:
  - target-curies
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0070112
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
  - GO:0070112
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
  - GO:0070112
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
  - GO:0070112
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
  - GO:0070112
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
  reference: data/structures/membrane_organelle/organellar_chromatophore_membrane.yaml
  locator: Entire maintained YAML, including history, all components, authorities,
    graph nodes/edges and discussions
  accessed_at: '2026-10-22T02:52:30Z'
  support: context_only
  summary: Complete target read; maintained scientific content remains unchanged.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent grounding/status; EssentialityEnum; CausalNode and
    graph scope
  accessed_at: '2026-10-22T02:52:30Z'
  support: context_only
  summary: A label-only molecular/material constituent is distinct from substituting
    a whole membrane location as its chemical identity. Essentiality concerns whether
    the structure forms without the component; neither mature localization nor catalytic
    function proves individual assembly necessity.
- evidence_id: context-organellar_chromatophore
  kind: record_content
  reference: data/structures/membrane_organelle/organellar_chromatophore.yaml
  locator: Complete frozen maintained boundary record
  accessed_at: '2026-10-22T02:52:30Z'
  support: context_only
  summary: Read as local representation/topology context only, not independent experimental
    evidence. Whole chromatophore bytes equal the fully read B35 source; the four
    membrane/space records were fully read in B36.
- evidence_id: context-organellar_chromatophore_inner_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/organellar_chromatophore_inner_membrane.yaml
  locator: Complete frozen maintained boundary record
  accessed_at: '2026-10-22T02:52:30Z'
  support: context_only
  summary: Read as local representation/topology context only, not independent experimental
    evidence. Whole chromatophore bytes equal the fully read B35 source; the four
    membrane/space records were fully read in B36.
- evidence_id: context-organellar_chromatophore_intermembrane_space
  kind: record_content
  reference: data/structures/membrane_organelle/organellar_chromatophore_intermembrane_space.yaml
  locator: Complete frozen maintained boundary record
  accessed_at: '2026-10-22T02:52:30Z'
  support: context_only
  summary: Read as local representation/topology context only, not independent experimental
    evidence. Whole chromatophore bytes equal the fully read B35 source; the four
    membrane/space records were fully read in B36.
- evidence_id: context-organellar_chromatophore_outer_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/organellar_chromatophore_outer_membrane.yaml
  locator: Complete frozen maintained boundary record
  accessed_at: '2026-10-22T02:52:30Z'
  support: context_only
  summary: Read as local representation/topology context only, not independent experimental
    evidence. Whole chromatophore bytes equal the fully read B35 source; the four
    membrane/space records were fully read in B36.
- evidence_id: chromatophore-boundary-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070111,GO:0070112,GO:0070113,GO:0070114,GO:0070115,GO:0070118,GO:0009527,GO:0009528,GO:0009529,GO:0030659
  locator: 'Complete ten-term results: id/name/definition/synonyms/isObsolete and
    typed children'
  accessed_at: '2026-10-22T02:49:39.963419Z'
  support: supports
  summary: All ten requested terms are active and identify the exact chromatophore
    compartments and stated broader classes. GO0070112 explicitly has GO0070113/14/18
    is_a children, GO0030659 has GO0070112 as an is_a child, and GO0070111 has GO0070112/14/15
    as part_of children. Absent direct edges are not invented.
  snapshot_sha256: bb642c269ae36b3b1795c3a020aa28810f848dd7825576fc80afa0df4927285c
- evidence_id: chromatophore-boundary-agent-GO0070112-isa
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070112/ancestors?relations=is_a
  locator: Complete native ancestors response; query relations=is_a, one exact term
  accessed_at: '2026-10-22T02:49:40.677634Z'
  support: supports
  summary: The is_a-only ancestor response for GO:0070112 (organellar chromatophore
    membrane) includes GO:0030659. This response describes only that queried term;
    containment and unlisted plastid-specific parents are not inferred from it.
  snapshot_sha256: c098937855de2e7e3c9085ac74f1ddaa945727690154a344dd0a24c58c8c3eac
- evidence_id: chromatophore-boundary-agent-SL0352
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0352.json
  locator: Top-level id/name/definition/geneOntologies and immediate isA/partOf entries;
    nested parent GO cross-references
  accessed_at: '2026-10-22T02:49:39.963796Z'
  support: supports
  summary: SL0352 maps exactly to GO0070112 and explicitly applies when outer, inner
    or thylakoid membrane localization is unspecified. Its partOf is chromatophore/GO0070111;
    isA is plastid membrane/GO0042170, separate from the GO cytoplasmic-vesicle-membrane
    classification. Its definition restricts the structure to Paulinella species without
    a frequency census.
  snapshot_sha256: 3bbd1251c9b67c87fdd3a88c0fb7e326a36c0c823f30fe6a9825472786bfc8dc
- evidence_id: chromatophore-boundary-agent-SL0351
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0351.json
  locator: Complete definition, exact GO0070111 mapping and isA plastid/GO0009536
  accessed_at: '2026-10-22T02:37:50.466589Z'
  support: supports
  summary: The native location authority describes the Paulinella photosynthetic organelle
    with two surrounding membranes, residual peptidoglycan between them, and internal
    thylakoids; its isA is plastid. This establishes compartment context, not a biochemical
    composition or assembly perturbation assay.
  snapshot_sha256: 8a511ebab3aeb225c94971707064b4de8201b1bc8f6672c0e32f550ee72ae5c2
- evidence_id: chromatophore-boundary-agent-tax39716
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/39716
  locator: Complete native taxId/scientificName/rank/lineage fields
  accessed_at: '2026-10-22T02:44:36.288230Z'
  support: supports
  summary: ENA taxId39716 is Paulinella at genus rank, under Cercozoa/Rhizaria. This
    verifies the taxon identity; VARIABLE is evaluated against the biological scope
    separately.
  snapshot_sha256: d856236448b790cbfd8b00f609d7e21c8e64e5089856db686023a316e91f16ef
- evidence_id: chromatophore-boundary-agent-tax39717
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/39717
  locator: Complete native taxId/scientificName/rank/lineage fields
  accessed_at: '2026-10-22T02:44:36.289679Z'
  support: supports
  summary: ENA taxId39717 is Paulinella chromatophora at species rank. This checks
    the additional primary-study context, without exporting its strain results to
    every genus member.
  snapshot_sha256: 11763b1d5106d7c4445bbe97d3755f012b4a6ddb4d806de48dfbbcec488f56f3
- evidence_id: chromatophore-boundary-agent-gabr2020-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1111/jpy.13003
  locator: Unique native EuropePMC result DOI/id/title/authorString and abstractText
  accessed_at: '2026-10-22T02:37:49.243652Z'
  support: supports
  summary: The exact DOI10.1111/jpy.13003, PMID32289879, title and authors identify
    the secondary review; complete abstract read.
  snapshot_sha256: 92316c5a8ceb42a149eed745d90d18ef7138e9981df6099868707d5706f534b4
- evidence_id: chromatophore-boundary-agent-gabr2020-pmc
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/7734844/
  locator: S2 The Paulinella model and Fig1 caption, reread from the retained genuine
    PMC author-manuscript body; no figure pixels inspected
  accessed_at: '2026-10-22T02:39:41.678213Z'
  support: supports
  summary: The secondary review distinguishes photosynthetic Paulinella lineages from
    heterotrophic relatives lacking chromatophores. Its model-system section supports
    qualitative variation within the genus; it is not a numerical prevalence study
    or primary assembly experiment.
  snapshot_sha256: 4cb5e9956e00937ea3f62ff80af921075a27b1cd6951c7d460b530c200993396
- evidence_id: chromatophore-boundary-agent-nowack2012-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1073/pnas.1118800109
  locator: Unique native EuropePMC result identity and complete abstractText
  accessed_at: '2026-10-22T02:37:48.587487Z'
  support: supports
  summary: Exact DOI10.1073/pnas.1118800109 and PMID22371600 identify the primary
    import study; bibliographic fields and complete abstract are retained separately
    from body scope.
  snapshot_sha256: 8f62b9fd80b8ca0fc14ec7ba0953bc2fb5becd33876f6d27bd7f6cd5198d364b
- evidence_id: chromatophore-boundary-agent-nowack2012-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/3325729/
  locator: Results sec2 including Fig1 caption and Methods sec14 Strain and Growth
    Conditions reread in B36. Earlier B35 read scope is not enlarged here; no source
    figure pixels or supplementary data inspected.
  accessed_at: '2026-10-22T02:39:41.676639Z'
  support: supports
  summary: The primary paper examines P.chromatophora CCAC0185 (subisolate M0880/a);
    sectioned cells show chromatophores with thylakoids and PsaE immunogold labeling.
    This corroborates the organelle context but does not itself identify a molecular
    lipid complement or establish formation necessity of an individual envelope constituent.
  snapshot_sha256: df4b05048ab13ce50055bc6357bdc95ef2a5195af3269700d7b791f514864c94
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/organellar_chromatophore_membrane.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:42:13Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/organellar_chromatophore_membrane.yaml'
  snapshot_sha256: 53c1e46600dead1c8e0e6d77c12851f3973bef9ce440b1da2b493b8196e3fb98
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/organellar_chromatophore_membrane.yaml
    --out /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/organellar_chromatophore_membrane-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:42:14Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/organellar_chromatophore_membrane.yaml\
    \ --out /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/organellar_chromatophore_membrane-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch36-20261022-i5iwb5rr/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/organellar_chromatophore_membrane-strict.tsv"
  snapshot_sha256: a10fb343368ec7d3c2d45eec092306bc7e2ca2b07e2e5763eb7091f91ae81b94
- evidence_id: focused-causal
  kind: validation
  reference: /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/organellar_chromatophore_membrane.yaml
  locator: /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/membrane/causal.log
  accessed_at: '2026-10-22T02:50:38.795041Z'
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
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/organellar_chromatophore_membrane.yaml;
    native collect() exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 8 of 8 collected target identifiers returned OK. No residuals. Native source
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
  topic: Exact identity, hierarchy and parthood
  outcome: supported
  target_ids:
  - GO:0070112
  summary: GO0070112/SL0352 identify the generic chromatophore membrane class. Although
    GO definition wording says surrounding bilayers, its own typed children and SL0352
    explicitly include thylakoid membrane in the fallback class. The record faithfully
    distinguishes this general localization from a particular membrane. GO0030659
    parentage is directly returned.
  evidence_ids:
  - chromatophore-boundary-agent-go
  - chromatophore-boundary-agent-GO0070112-isa
  - chromatophore-boundary-agent-SL0352
  - chromatophore-boundary-agent-SL0351
  - record
- assessment_id: taxon
  area: scope
  topic: Verified genus with variable presence
  outcome: supported
  target_ids:
  - GO:0070112
  summary: Paulinella genus39716 is exact. The target expressly avoids universal presence
    across genus members; the reviewed photosynthetic/heterotrophic distinction supports
    VARIABLE without a numerical prevalence inference. The CCAC0185 primary study
    is one P.chromatophora culture, not an all-species assay.
  evidence_ids:
  - chromatophore-boundary-agent-tax39716
  - chromatophore-boundary-agent-tax39717
  - chromatophore-boundary-agent-SL0352
  - chromatophore-boundary-agent-gabr2020-pmc
  - chromatophore-boundary-agent-nowack2012-pmc
- assessment_id: composition
  area: grounding
  topic: Label-only lipid-bilayer material
  outcome: supported
  target_ids:
  - GO:0070112
  summary: The single LIPID row explicitly denotes the lipid-bilayer constituent,
    has no whole-membrane GO grounding, and documents REVIEWED_LABEL_ONLY status.
    The correct anatomical identifiers stay on record/structure nodes. Collective
    bilayer material is constitutive of this membrane class; optional chemical specificity
    is not invented.
  evidence_ids:
  - chromatophore-boundary-agent-go
  - chromatophore-boundary-agent-SL0352
  - record
  - schema
- assessment_id: necessity
  area: grounding
  topic: Specific assembly requirements remain unmeasured
  outcome: unknown
  target_ids:
  - GO:0070112
  summary: ESSENTIAL can be supported at the defining collective bilayer level. No
    exact lipid species, enzyme or membrane protein is asserted necessary; the native
    definitions and inspected primary study do not establish individual molecular
    formation requirements. This assessment remains unknown at that narrower experimental
    level.
  evidence_ids:
  - chromatophore-boundary-agent-go
  - chromatophore-boundary-agent-SL0352
  - chromatophore-boundary-agent-nowack2012-pmc
  - schema
- assessment_id: graph
  area: graph
  topic: Every asserted edge and node boundary
  outcome: supported
  target_ids:
  - GO:0070112
  summary: 'All four NONMECHANISTIC edges faithfully express native containment and
    subclass scope: generic membrane part_of chromatophore, with inner, outer and
    thylakoid membranes as narrower classes. The graph is a localization-class explanation,
    not a claim of which membrane contains an unspecified protein.'
  evidence_ids:
  - chromatophore-boundary-agent-go
  - chromatophore-boundary-agent-SL0352
  - chromatophore-boundary-agent-SL0351
  - record
- assessment_id: evidence
  area: evidence
  topic: Source placement and authority limits
  outcome: supported
  target_ids:
  - GO:0070112
  summary: The target cites ontology/location authorities for defining anatomy and
    topology, and those exact source claims were checked. Additional primary and secondary
    bodies provide bounded biological context; they are not substituted as measurements
    of composition, species prevalence, membrane origin or assembly necessity. No
    new function is inferred from a static graph.
  evidence_ids:
  - chromatophore-boundary-agent-go
  - chromatophore-boundary-agent-SL0352
  - chromatophore-boundary-agent-SL0351
  - chromatophore-boundary-agent-gabr2020-pmc
  - chromatophore-boundary-agent-nowack2012-pmc
- assessment_id: coverage
  area: completeness
  topic: Entire target and explicit open issues
  outcome: supported
  target_ids:
  - GO:0070112
  summary: The complete record, history, synonyms, parentage, material row, taxon
    note, each graph node/edge and all discussions were reviewed. No individual protein
    accession, gene-symbol cohort, quantitative physical measurement or maintained
    image is asserted. The label-only lipid grounding task remains a scoped open issue;
    optional molecular inventory is not automatically a finding. Historical access
    notes are preserved as historical statements.
  evidence_ids:
  - record
  - schema
  - chromatophore-boundary-agent-go
  - chromatophore-boundary-agent-SL0352
findings: []
actions: []
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- GO and UniProt location classification differ in some broader plastid parent relations;
  each statement is attributed to its actual authority, without fabricating an absent
  GO edge.
- No new primary lipid composition, quantitative taxon census, individual molecular
  assembly-necessity assay, figure-pixel inspection, raw-data reanalysis or supplementary
  experiment was performed. Additional primary/secondary reading is restricted to
  the explicit locators.
- The target contains no numerical physical properties or structured protein examples.
  Label-only molecular specificity and the exact residual-wall identity, where applicable,
  remain bounded curation questions rather than invented identities.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
