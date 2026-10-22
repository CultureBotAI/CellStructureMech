# Recycling endosome membrane scientific review

- Review: 20261022T034123Z-recycling-endosome-membrane-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T03:24:50Z
- Finished UTC: 2026-10-22T03:41:23Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Exact membrane identity and topology are supported. No confirmed concrete defect was established; stage-specific transferrin-receptor scope remains limited by abstract-only access.

## Scope And Provenance

Exactly one entire maintained target; native source identity, claim scope, graph/component joins and evidence placement reviewed.

Selection: Target 1 of batch40, next uncovered strict-path-order target at fresh origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0055038 | data/structures/membrane_organelle/recycling_endosome_membrane.yaml | maintained | recycling endosome membrane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0055038 | Focused validator passed. |
| Focused native strict | passed | True | GO:0055038 | Focused validator passed. |
| Focused graph protein-reference check | passed | True | GO:0055038 | Native report verified; syntactic coverage does not establish biological gene-symbol provenance. |
| Expression-module applicability | not_applicable | False | GO:0055038 | No expression-module regulatory claim is maintained. |
| Claim-level scientific review | passed | True | GO:0055038 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0055038 | 6 of 7 collected target identifiers returned OK. PMID:11683389: UNREACHABLE; Exact native MED identity independently verifies PMID, title, DOI and PMC/null mapping after bulk eutils414 failure. Abstract and body scientific scopes remain separately bounded. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0055038 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0055038 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0055038 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0055038 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0055038 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact limiting membrane identity

identity: supported. Targets: GO:0055038.

GO and SL support exact identity, endosome membrane is-a, recycling endosome parthood and synonym. The enclosed lumen is correctly separated from the boundary.

### Collective bilayer material

grounding: supported. Targets: GO:0055038.

The LIPID constituent deliberately lacks whole-membrane GO grounding and describes collective bilayer material. Its constitutional ESSENTIAL label does not imply a particular lipid species or protein is individually required.

### Individual formation requirements

evidence: unknown. Targets: GO:0055038.

Exact lipid species, ratios and individual assembly requirements remain unknown; the open constituent task correctly preserves that distinction.

### Stage-dependent recycling compartments

scope: unknown. Targets: GO:0055038.

The complete Jeffries abstract verifies TbRAB11-positive compartments in both stages and TfR colocalization at paper level. Stage-specific TfR localization is not independently verified from the unavailable body; no extra claim of equal cargo or morphology is inferred.

### Bounded membrane example

evidence: supported. Targets: GO:0055038.

The abstract describes TbRAB11 on endomembranes and receptor colocalization, supporting the existence of the named membrane compartment. Exact strain, cargo distribution in each stage and isolated-membrane composition are not established here.

### Three descriptive topology edges

graph: supported. Targets: GO:0055038.

The is-a, parthood and lumen-boundary edges agree with native authorities. NONMECHANISTIC correctly describes this topology and does not import a Rab11 requirement or trafficking pathway.

### Entire target and unresolved source scope

completeness: supported. Targets: GO:0055038.

All current fields and the lipid-species TODO were inspected. No concrete identity, component, graph or evidence-placement defect was established at the declared scope; the both-stage TfR wording remains unverified rather than certified.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/recycling_endosome_membrane.yaml; Entire maintained target, including all history, graph edges, evidence and discussions | context_only | Every maintained field was read; historical events are not treated as independent experimental evidence. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; Component type, grounding, essentiality and graph/evidence contracts | context_only | Whole anatomical identity differs from chemical material; function and localization do not establish necessity for structure formation. |
| root40-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0055038,GO:0010008,GO:0055037,GO:0034777,GO:0036007,GO:0110165,GO:0005737,GO:0008218; Complete eight id/name/definition/obsolete/synonym fields and applicable typed children; large generic cytoplasm/anatomy child lists not read exhaustively. | supports | Eight active native entries support exact recycling membrane/lumen/whole identities, endosome-membrane parentage, scintillon definition, bioluminescence and generic anatomy. Typed0055037 children include membrane0055038 and lumen0034777 part_of;0010008 has0055038 is_a. |
| neighbor-recycling_endosome | data/structures/membrane_organelle/recycling_endosome.yaml; Complete frozen boundary neighbor | context_only | Whole organelle and enclosed lumen remain distinct from the limiting membrane; neighbor text is context rather than experimental evidence. |
| neighbor-recycling_endosome_lumen | data/structures/membrane_organelle/recycling_endosome_lumen.yaml; Complete frozen boundary neighbor | context_only | Whole organelle and enclosed lumen remain distinct from the limiting membrane; neighbor text is context rather than experimental evidence. |
| root40-sources-SL0231 | https://rest.uniprot.org/locations/SL-0231.json; Complete native response including nested isA and partOf objects | supports | SL0231 exactly maps recycling endosome membrane to GO0055038, supplies the synonym, isA endosome membrane and partOf recycling endosome. Its complete nested hierarchy preserves typed relation directions. |
| root40-sources-tax5691 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5691; Complete native taxonomy response | supports | Native ENA5691 verifies Trypanosoma brucei species identity and lineage. |
| root40-shared-PMID-11683389 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A11683389%20AND%20SRC%3AMED; Complete native bibliographic identity and primary abstract, not main body | supports | Unique native MED11683389/DOI10.1242/jcs.114.14.2617 identifies Jeffries/Morgan/Field2001. The complete abstract describes TbRAB11-positive procyclic and bloodstream compartments, different stage morphology, and transferrin-receptor/internalized anti-VSG colocalization. It does not explicitly allocate the TfR experiment to both stages. |
| root40-shared-jeffries2001-publisher | https://journals.biologists.com/jcs/article/114/14/2617/26724/A-developmentally-regulated-rab11-homologue-in; Exact native response status and retained body; not readable article text | context_only | Native response status 403 did not provide a readable article body; no full-text inference is made. |
| root40-sources-jeffries2001-citeseer | https://citeseerx.ist.psu.edu/document?doi=7bd9e708f3ecc788733d135c5825a13124b3b88d&amp;repid=rep1&amp;type=pdf; Exact native response status and retained body; not readable article text | context_only | Native response status 404 did not provide a readable article body; no full-text inference is made. |
| root40-sources-jeffries2001-publisher-pdf | https://journals.biologists.com/jcs/article-pdf/114/14/2617/1276757/2617.pdf; Exact native response status and retained body; not readable article text | context_only | Native response status 403 did not provide a readable article body; no full-text inference is made. |
| schema-result | just validate data/structures/membrane_organelle/recycling_endosome_membrane.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/recycling_endosome_membrane.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/recycling_endosome_membrane.yaml --out /private/tmp/cellstructure-batch40-20261022-pllys1sh/recycling_endosome_membrane-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/recycling_endosome_membrane.yaml --out /private/tmp/cellstructure-batch40-20261022-pllys1sh/recycling_endosome_membrane-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch40-20261022-pllys1sh/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch40-20261022-pllys1sh/recycling_endosome_membrane-strict.tsv |
| native-recycling_endosome_membrane-causal | /private/tmp/cellstructure-batch40-20261022-pllys1sh/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/recycling_endosome_membrane.yaml; Complete native graph protein-reference report | supports | <br>causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes<br> |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/recycling_endosome_membrane.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 6 of 7 collected target identifiers returned OK. PMID:11683389: UNREACHABLE; Exact native MED identity independently verifies PMID, title, DOI and PMC/null mapping after bulk eutils414 failure. Abstract and body scientific scopes remain separately bounded. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Taxon presence values are qualitative; no complete species census, universal molecular inventory or measured occurrence frequency is inferred.
- Jeffries2001 was read only as complete native identity and abstract. Publisher responses are403 and the CiteSeer PDF URL returned404 HTML. Stage-specific TfR cargo localization, detailed Methods and image pixels could not be independently checked; neither stage-equivalent cargo nor a contradictory result is inferred.
- No protein accession or molecular necessity is asserted by this target. The generic membrane classification is not a complete organelle mechanism.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User explicitly requests all uncovered reviews, including honest zero-finding observations.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T034123Z-recycling-endosome-membrane-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Recycling endosome membrane scientific review
started_at: '2026-10-22T03:24:50Z'
finished_at: '2026-10-22T03:41:23Z'
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
summary: Exact membrane identity and topology are supported. No confirmed concrete
  defect was established; stage-specific transferrin-receptor scope remains limited
  by abstract-only access.
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
  - path: data/structures/membrane_organelle/recycling_endosome.yaml
    sha256: 7a806e4e4eaddd3578c517d587c4eaaf1c458e4f5cfc2e59065fc0f26594ac48
    role: context
  - path: data/structures/membrane_organelle/recycling_endosome_lumen.yaml
    sha256: 69bc318299125a4de316f2ba3b7fc20e0655bca2d37fa6d43c12afcfa3fc3ce2
    role: context
  - path: data/structures/membrane_organelle/recycling_endosome_membrane.yaml
    sha256: cc07cfcf4d3c8fcfac3594e3dec18791b1e5f40e13d867fcdb4ef355f07aebf0
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
- target_id: GO:0055038
  path: data/structures/membrane_organelle/recycling_endosome_membrane.yaml
  label: recycling endosome membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/recycling_endosome_membrane.yaml
    role: maintained scientific record
scope:
  description: Exactly one entire maintained target; native source identity, claim
    scope, graph/component joins and evidence placement reviewed.
  selection: Target 1 of batch40, next uncovered strict-path-order target at fresh
    origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0055038
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0055038
  command: just validate data/structures/membrane_organelle/recycling_endosome_membrane.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0055038
  command: just validate-strict data/structures/membrane_organelle/recycling_endosome_membrane.yaml
    --out /private/tmp/cellstructure-batch40-20261022-pllys1sh/recycling_endosome_membrane-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-recycling_endosome_membrane-causal
  name: Focused graph protein-reference check
  status: passed
  required: true
  target_ids:
  - GO:0055038
  command: /private/tmp/cellstructure-batch40-20261022-pllys1sh/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/recycling_endosome_membrane.yaml
  exit_code: 0
  summary: Native report verified; syntactic coverage does not establish biological
    gene-symbol provenance.
  evidence_ids:
  - native-recycling_endosome_membrane-causal
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0055038
  summary: No expression-module regulatory claim is maintained.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0055038
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - root40-sources-go
  - neighbor-recycling_endosome
  - neighbor-recycling_endosome_lumen
  - root40-sources-SL0231
  - root40-sources-tax5691
  - root40-shared-PMID-11683389
  - root40-shared-jeffries2001-publisher
  - root40-sources-jeffries2001-citeseer
  - root40-sources-jeffries2001-publisher-pdf
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0055038
  summary: '6 of 7 collected target identifiers returned OK. PMID:11683389: UNREACHABLE;
    Exact native MED identity independently verifies PMID, title, DOI and PMC/null
    mapping after bulk eutils414 failure. Abstract and body scientific scopes remain
    separately bounded. Native source checks are separately scoped; skipped or unreachable
    identifiers are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - root40-shared-PMID-11683389
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0055038
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch40 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0055038
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch40 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0055038
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch40 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0055038
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch40 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0055038
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
    and current batch40 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/recycling_endosome_membrane.yaml
  locator: Entire maintained target, including all history, graph edges, evidence
    and discussions
  accessed_at: '2026-10-22T03:34:05Z'
  support: context_only
  summary: Every maintained field was read; historical events are not treated as independent
    experimental evidence.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Component type, grounding, essentiality and graph/evidence contracts
  accessed_at: '2026-10-22T03:34:05Z'
  support: context_only
  summary: Whole anatomical identity differs from chemical material; function and
    localization do not establish necessity for structure formation.
- evidence_id: root40-sources-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0055038,GO:0010008,GO:0055037,GO:0034777,GO:0036007,GO:0110165,GO:0005737,GO:0008218
  locator: Complete eight id/name/definition/obsolete/synonym fields and applicable
    typed children; large generic cytoplasm/anatomy child lists not read exhaustively.
  accessed_at: '2026-10-22T03:25:30.380686Z'
  support: supports
  summary: Eight active native entries support exact recycling membrane/lumen/whole
    identities, endosome-membrane parentage, scintillon definition, bioluminescence
    and generic anatomy. Typed0055037 children include membrane0055038 and lumen0034777
    part_of;0010008 has0055038 is_a.
  snapshot_sha256: 28aadf5adf9f417e6728df757ba86e0e67db2fe8f5908323fcac875a983deb53
- evidence_id: neighbor-recycling_endosome
  kind: record_content
  reference: data/structures/membrane_organelle/recycling_endosome.yaml
  locator: Complete frozen boundary neighbor
  accessed_at: '2026-10-22T03:34:05Z'
  support: context_only
  summary: Whole organelle and enclosed lumen remain distinct from the limiting membrane;
    neighbor text is context rather than experimental evidence.
- evidence_id: neighbor-recycling_endosome_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/recycling_endosome_lumen.yaml
  locator: Complete frozen boundary neighbor
  accessed_at: '2026-10-22T03:34:05Z'
  support: context_only
  summary: Whole organelle and enclosed lumen remain distinct from the limiting membrane;
    neighbor text is context rather than experimental evidence.
- evidence_id: root40-sources-SL0231
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0231.json
  locator: Complete native response including nested isA and partOf objects
  accessed_at: '2026-10-22T03:25:30.381246Z'
  support: supports
  summary: SL0231 exactly maps recycling endosome membrane to GO0055038, supplies
    the synonym, isA endosome membrane and partOf recycling endosome. Its complete
    nested hierarchy preserves typed relation directions.
  snapshot_sha256: c8db985f628cf33bc8b2826b2776cd38cdd0849d15e8e5999d537aa3f1176c36
- evidence_id: root40-sources-tax5691
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5691
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T03:25:31.015744Z'
  support: supports
  summary: Native ENA5691 verifies Trypanosoma brucei species identity and lineage.
  snapshot_sha256: ba78ff6fe5de62b2654b61e249c2c87b239dca0208950b0e4ecf3ef2d81c99be
- evidence_id: root40-shared-PMID-11683389
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A11683389%20AND%20SRC%3AMED
  locator: Complete native bibliographic identity and primary abstract, not main body
  accessed_at: '2026-10-22T03:15:33.333082Z'
  support: supports
  summary: Unique native MED11683389/DOI10.1242/jcs.114.14.2617 identifies Jeffries/Morgan/Field2001.
    The complete abstract describes TbRAB11-positive procyclic and bloodstream compartments,
    different stage morphology, and transferrin-receptor/internalized anti-VSG colocalization.
    It does not explicitly allocate the TfR experiment to both stages.
  snapshot_sha256: 47119d081d8f1c7a80b63125de10f3688288733071805146639a1877e40653f0
- evidence_id: root40-shared-jeffries2001-publisher
  kind: primary_source
  reference: https://journals.biologists.com/jcs/article/114/14/2617/26724/A-developmentally-regulated-rab11-homologue-in
  locator: Exact native response status and retained body; not readable article text
  accessed_at: '2026-10-22T03:16:03.366249Z'
  support: context_only
  summary: Native response status 403 did not provide a readable article body; no
    full-text inference is made.
  snapshot_sha256: 95e86dfe4f121dfacbaef5eee6046634994717818f0cf88d0adb472685fc80ec
- evidence_id: root40-sources-jeffries2001-citeseer
  kind: primary_source
  reference: https://citeseerx.ist.psu.edu/document?doi=7bd9e708f3ecc788733d135c5825a13124b3b88d&repid=rep1&type=pdf
  locator: Exact native response status and retained body; not readable article text
  accessed_at: '2026-10-22T03:25:30.381836Z'
  support: context_only
  summary: Native response status 404 did not provide a readable article body; no
    full-text inference is made.
  snapshot_sha256: 554e614a9163c3f666a79940743bc929b124952c8d49f9bc4c4774629c62c49b
- evidence_id: root40-sources-jeffries2001-publisher-pdf
  kind: primary_source
  reference: https://journals.biologists.com/jcs/article-pdf/114/14/2617/1276757/2617.pdf
  locator: Exact native response status and retained body; not readable article text
  accessed_at: '2026-10-22T03:29:41.323304Z'
  support: context_only
  summary: Native response status 403 did not provide a readable article body; no
    full-text inference is made.
  snapshot_sha256: a11fd88909fecde84acde9b7493e57a8e43e7fb748d3df9ebe250dac753fcf36
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/recycling_endosome_membrane.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:24:52Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/recycling_endosome_membrane.yaml'
  snapshot_sha256: bce2e25a97dc59de8204e31d093b238d48155df87e0a95ed771ada725ec60d98
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/recycling_endosome_membrane.yaml
    --out /private/tmp/cellstructure-batch40-20261022-pllys1sh/recycling_endosome_membrane-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:24:53Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/recycling_endosome_membrane.yaml\
    \ --out /private/tmp/cellstructure-batch40-20261022-pllys1sh/recycling_endosome_membrane-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch40-20261022-pllys1sh/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch40-20261022-pllys1sh/recycling_endosome_membrane-strict.tsv"
  snapshot_sha256: b9d5ab7742428983d29f0da860d9dd1e00effba1de070a8cedd2c9671f718308
- evidence_id: native-recycling_endosome_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batch40-20261022-pllys1sh/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/recycling_endosome_membrane.yaml
  locator: Complete native graph protein-reference report
  accessed_at: '2026-10-22T03:31:54.828302Z'
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
  locator: data/structures/membrane_organelle/recycling_endosome_membrane.yaml; native
    collect() exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '6 of 7 collected target identifiers returned OK. PMID:11683389: UNREACHABLE;
    Exact native MED identity independently verifies PMID, title, DOI and PMC/null
    mapping after bulk eutils414 failure. Abstract and body scientific scopes remain
    separately bounded. Native source checks are separately scoped; skipped or unreachable
    identifiers are not silently counted as resolved.'
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
  topic: Exact limiting membrane identity
  outcome: supported
  target_ids:
  - GO:0055038
  summary: GO and SL support exact identity, endosome membrane is-a, recycling endosome
    parthood and synonym. The enclosed lumen is correctly separated from the boundary.
  evidence_ids:
  - record
  - root40-sources-go
  - root40-sources-SL0231
- assessment_id: composition
  area: grounding
  topic: Collective bilayer material
  outcome: supported
  target_ids:
  - GO:0055038
  summary: The LIPID constituent deliberately lacks whole-membrane GO grounding and
    describes collective bilayer material. Its constitutional ESSENTIAL label does
    not imply a particular lipid species or protein is individually required.
  evidence_ids:
  - record
  - schema
  - root40-sources-go
  - root40-sources-SL0231
- assessment_id: formation
  area: evidence
  topic: Individual formation requirements
  outcome: unknown
  target_ids:
  - GO:0055038
  summary: Exact lipid species, ratios and individual assembly requirements remain
    unknown; the open constituent task correctly preserves that distinction.
  evidence_ids:
  - record
  - schema
  - root40-sources-go
- assessment_id: taxonomy
  area: scope
  topic: Stage-dependent recycling compartments
  outcome: unknown
  target_ids:
  - GO:0055038
  summary: The complete Jeffries abstract verifies TbRAB11-positive compartments in
    both stages and TfR colocalization at paper level. Stage-specific TfR localization
    is not independently verified from the unavailable body; no extra claim of equal
    cargo or morphology is inferred.
  evidence_ids:
  - record
  - root40-sources-tax5691
  - root40-shared-PMID-11683389
- assessment_id: example
  area: evidence
  topic: Bounded membrane example
  outcome: supported
  target_ids:
  - GO:0055038
  summary: The abstract describes TbRAB11 on endomembranes and receptor colocalization,
    supporting the existence of the named membrane compartment. Exact strain, cargo
    distribution in each stage and isolated-membrane composition are not established
    here.
  evidence_ids:
  - record
  - root40-sources-tax5691
  - root40-shared-PMID-11683389
- assessment_id: graph
  area: graph
  topic: Three descriptive topology edges
  outcome: supported
  target_ids:
  - GO:0055038
  summary: The is-a, parthood and lumen-boundary edges agree with native authorities.
    NONMECHANISTIC correctly describes this topology and does not import a Rab11 requirement
    or trafficking pathway.
  evidence_ids:
  - record
  - root40-sources-go
  - root40-sources-SL0231
- assessment_id: coverage
  area: completeness
  topic: Entire target and unresolved source scope
  outcome: supported
  target_ids:
  - GO:0055038
  summary: All current fields and the lipid-species TODO were inspected. No concrete
    identity, component, graph or evidence-placement defect was established at the
    declared scope; the both-stage TfR wording remains unverified rather than certified.
  evidence_ids:
  - record
  - schema
  - root40-sources-go
  - root40-shared-PMID-11683389
findings: []
actions: []
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Taxon presence values are qualitative; no complete species census, universal molecular
  inventory or measured occurrence frequency is inferred.
- Jeffries2001 was read only as complete native identity and abstract. Publisher responses
  are403 and the CiteSeer PDF URL returned404 HTML. Stage-specific TfR cargo localization,
  detailed Methods and image pixels could not be independently checked; neither stage-equivalent
  cargo nor a contradictory result is inferred.
- No protein accession or molecular necessity is asserted by this target. The generic
  membrane classification is not a complete organelle mechanism.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User explicitly requests all uncovered reviews, including honest zero-finding observations.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
