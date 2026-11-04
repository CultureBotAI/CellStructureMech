# Golgi-associated vesicle membrane identity, boundaries and source-scope review

- Review: 20261022T015629Z-golgi-associated-vesicle-membrane-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T01:39:20Z
- Finished UTC: 2026-10-22T01:56:29Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Exact membrane identity, generic material scope, subtype relations and five descriptive edges are supported; no concrete finding was established.

## Scope And Provenance

Whole single maintained target; exact native identity/hierarchy, molecular material and formation-necessity distinctions, taxon/source scopes, every graph node/edge and all discussions.

Selection: Target 4 of batch thirty in strict uncovered path order; fresh-base initial inspection/schema/strict all passed before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0030660 | data/structures/membrane_organelle/golgi_associated_vesicle_membrane.yaml | maintained | Golgi-associated vesicle membrane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0030660 | Focused validator passed. |
| Focused native strict | passed | True | GO:0030660 | Focused validator passed. |
| Protein exemplar/actor applicability | not_applicable | False | GO:0030660 | No protein_examples or GENE_OR_PROTEIN graph nodes occur in this target. Mentioning subtype coat systems or imaging markers in literature does not create an asserted accession inventory. |
| Expression-module applicability | not_applicable | False | GO:0030660 | No regulatory transcriptomic or expression-module claim is used. |
| Claim-level scientific review | passed | True | GO:0030660 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0030660 | 12 of 12 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0030660 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0030660 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0030660 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0030660 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0030660 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact class, hierarchy and boundary

identity: supported. Targets: GO:0030660.

The record denotes the correct native GO class. Its parent, boundary/parthood and synonyms are supported at the specified relation scope. Whole vesicles/cisternae and surrounding membranes remain distinct; child-specific COPI and TGN properties are not exported to every member of the generic class.

### Yeast species and experimental boundaries

scope: supported. Targets: GO:0030660.

The yeast canonical example and occurrence statement are supported by the complete primary Letourneur abstract. Functional retrieval and coatomer mutants are not a measured prevalence estimate or a complete organelle-biogenesis assay. Earlier coat-protein source context is not relabelled as a yeast experiment.

### Material constituent versus assembled structure

grounding: supported. Targets: GO:0030660.

The reviewed-label-only row denotes the generic lipid material constituting the membrane boundary. It explicitly withholds the whole-membrane GO term as molecular grounding and makes no precise lipid-species or mixture assertion. No exact family/protein inventory is required for this material row.

### Formation necessity separated from collective boundary identity

grounding: unknown. Targets: GO:0030660.

A bounding bilayer is constitutive of the named membrane-bounded class. The inspected sources do not test removal/substitution of individual lipid species or establish molecule-specific assembly necessity. The collective boundary assertion is not reinterpreted as proof that any named lipid, coatomer subunit or marker is individually required for structure formation.

### Five descriptive membrane and subtype edges

graph: supported. Targets: GO:0030660.

Parthood, enclosure and both direct child-membrane relationships match native GO. Golgi-membrane donation is a structural interpretation of the exact budding definition, with Serafini abstract support limited to the Golgi-derived coated subtype. No universal COPI coat, identified lipid-transfer mechanism or separate membrane function is asserted.

### Whole target and bounded optional inventory

completeness: supported. Targets: GO:0030660.

Every maintained field, discussion and source placement was read. No exact protein examples, gene/protein graph nodes, molecular stoichiometry, tracked image assets or verbatim snippets are asserted here. Optional coat inventories and unresolved exact lipid chemistry are not automatic findings; historical descriptions remain historical and are not recertified.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/golgi_associated_vesicle_membrane.yaml; Entire maintained target, every field, source placement, history, discussion and graph node/edge | context_only | The exact single target was fully read and remains scientifically unchanged. |
| policy | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent molecular-building-block and grounding definitions; CausalNode.component_ref; essentiality and structure-kind contracts | context_only | Molecular material, complete membrane and enclosed compartment are different identities. A component_ref asserts correspondence to that local component; assembly necessity is distinct from function. |
| graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Actor identity and source-backed edges, graph scope and evidence | context_only | Descriptive topology and experimentally observed marker changes need not imply a complete molecular mechanism. |
| boundary-neighbor | data/structures/membrane_organelle/golgi_associated_vesicle.yaml; Entire frozen boundary-neighbor YAML | context_only | The neighbor was read as boundary context, not as a second target or independent proof of biological claims. |
| golgi-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005798,GO:0030660,GO:0031985,GO:0031410,GO:0030659,GO:0030663,GO:0012510,GO:0030137,GO:0030126,GO:0000139,GO:0035964,GO:0006890,GO:0098791,GO:0005794,GO:0032580; All15 exact IDs, names, definitions, active flags, synonyms and typed returned child relations; no inverse whole-class has_part inference from subtype membership | supports | All15 requested GO terms are active and preserve the whole-vesicle, surrounding membrane, cisterna and Golgi subcompartment distinctions. GO0005798 has COPI-coated vesicle0030137 as an is_a child and membrane0030660 as a part_of child; membrane0030660 has direct is_a children0030663 and0012510. GO0035964 defines Golgi-membrane evagination, and0030137 explicitly includes retrograde transport. GO0031985 has surrounding membrane0032580 as a part_of child; its broader subcompartment0098791 is part_of Golgi0005794. |
| golgi-agent-ancestors-0030660 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030660/ancestors?relations=is_a; Exact requested target and complete is_a-only ancestor list | supports | Native is_a-only ancestry includes cytoplasmic vesicle membrane0030659; the main response separately shows the direct child relation. |
| golgi-agent-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Exact taxId, scientificName, rank, lineage and alternate names | supports | ENA identifies4932 as Saccharomyces cerevisiae, species rank. This verifies the canonical species and distribution label without assigning a strain or measuring prevalence. |
| golgi-agent-serafini1991-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1016/0092-8674%2891%2990176-y%22; Exact PMID/title/DOI/authors and complete abstractText only | supports | Native PMID1680566 identifies Serafini et al.1991 and the exact DOI. The complete primary abstract reports ARF enrichment on Golgi-derived COP-coated vesicles, uncoating-associated removal and GTP-dependent Golgi binding. The proposed GTP-hydrolysis modulation is explicitly a hypothesis; no full body, universal vesicle coat or yeast-specific experiment is inferred. |
| golgi-agent-letourneur1994-med | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A8001155%20AND%20SRC%3AMED; Exact MED PMID8001155, DOI10.1016/0092-8674(94)90011-6, authorString/title and complete abstractText | supports | Native PMID8001155 verifies the exact Letourneur1994 title, DOI and author order. The complete primary abstract describes yeast dilysine-tagged Ste2 retrieval, coatomer mutant defects, RET1 complementation and distinct in-vitro binding results. It supports the scoped yeast COPI retrieval example, not a universal coat on every Golgi-associated vesicle or a direct membrane-budding movie. |
| access-serafini1991-cell | https://www.cell.com/cell/fulltext/0092-8674(91)90176-Y; Actual retained HTTP response, not scientific body | context_only | HTTP403 access response retained; no complete article body is inferred from its size. The separately cited native MED abstract is the inspected scientific scope. |
| access-letourneur1994-publisher | https://www.cell.com/cell/fulltext/0092-8674(94)90011-6; Actual retained HTTP response, not scientific body | context_only | HTTP403 access response retained; no complete article body is inferred from its size. The separately cited native MED abstract is the inspected scientific scope. |
| access-letourneur1994-sciencedirect | https://www.sciencedirect.com/science/article/pii/0092867494900116; Actual retained HTTP response, not scientific body | context_only | HTTP403 access response retained; no complete article body is inferred from its size. The separately cited native MED abstract is the inspected scientific scope. |
| schema-result | just validate data/structures/membrane_organelle/golgi_associated_vesicle_membrane.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/golgi_associated_vesicle_membrane.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/golgi_associated_vesicle_membrane.yaml --out /private/tmp/cellstructure-batch30-20261022-frro2xh0/golgi_associated_vesicle_membrane-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/golgi_associated_vesicle_membrane.yaml --out /private/tmp/cellstructure-batch30-20261022-frro2xh0/golgi_associated_vesicle_membrane-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch30-20261022-frro2xh0/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch30-20261022-frro2xh0/golgi_associated_vesicle_membrane-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/golgi_associated_vesicle_membrane.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 12 of 12 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- The fresh target-resolver slice and all five corpus receipt/manifest checks are integrated in this completed review.
- No exact lipid mixture, individual lipid-species formation necessity or complete coat/protein inventory was established. The review does not infer an inventory defect from an optional field or historical TODO.
- Serafini1991 and Letourneur1994 are complete native primary abstracts only. Publisher responses returned403; no complete primary body, detailed mutant protocol, original image pixels or raw assays were inspected. The zero-hit DOI query for Letourneur is an indexing/access limitation: its PMID8001155 and Crossref identify the exact DOI, title and authors.
- The yeast retrieval result is a COPI subtype example within a broad Golgi-associated-vesicle class. It does not establish that every generic vesicle is COPI coated.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User explicitly authorizes one review per uncovered target, including justified clean reviews, overriding the local issue-only output gate.
- Only unsaved review/support artifacts are written outside the repository; no scientific YAML, history, index, save or Git/publication mutation.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T015629Z-golgi-associated-vesicle-membrane-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Golgi-associated vesicle membrane identity, boundaries and source-scope review
started_at: '2026-10-22T01:39:20Z'
finished_at: '2026-10-22T01:56:29Z'
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
summary: Exact membrane identity, generic material scope, subtype relations and five
  descriptive edges are supported; no concrete finding was established.
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
  - path: data/structures/membrane_organelle/golgi_associated_vesicle.yaml
    sha256: 71af7287ce915ee5a16cef9a81c36b2c46e1b0cb7622a3f5c445fe308bbd81ba
    role: context
  - path: data/structures/membrane_organelle/golgi_associated_vesicle_membrane.yaml
    sha256: 6467fb8e64210d44c66f32b8c6f654c6bdada08ecd35edc36f074667d4ce4413
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
- target_id: GO:0030660
  path: data/structures/membrane_organelle/golgi_associated_vesicle_membrane.yaml
  label: Golgi-associated vesicle membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/golgi_associated_vesicle_membrane.yaml
    role: maintained scientific record
scope:
  description: Whole single maintained target; exact native identity/hierarchy, molecular
    material and formation-necessity distinctions, taxon/source scopes, every graph
    node/edge and all discussions.
  selection: Target 4 of batch thirty in strict uncovered path order; fresh-base initial
    inspection/schema/strict all passed before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0030660
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0030660
  command: just validate data/structures/membrane_organelle/golgi_associated_vesicle_membrane.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0030660
  command: just validate-strict data/structures/membrane_organelle/golgi_associated_vesicle_membrane.yaml
    --out /private/tmp/cellstructure-batch30-20261022-frro2xh0/golgi_associated_vesicle_membrane-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: protein-examples
  name: Protein exemplar/actor applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0030660
  summary: No protein_examples or GENE_OR_PROTEIN graph nodes occur in this target.
    Mentioning subtype coat systems or imaging markers in literature does not create
    an asserted accession inventory.
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0030660
  summary: No regulatory transcriptomic or expression-module claim is used.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0030660
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - graph-policy
  - boundary-neighbor
  - golgi-agent-go
  - golgi-agent-ancestors-0030660
  - golgi-agent-tax4932
  - golgi-agent-serafini1991-meta
  - golgi-agent-letourneur1994-med
  - access-serafini1991-cell
  - access-letourneur1994-publisher
  - access-letourneur1994-sciencedirect
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0030660
  summary: 12 of 12 collected target identifiers returned OK. No residuals. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.
  evidence_ids:
  - target-curies
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0030660
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch30 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0030660
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch30 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0030660
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch30 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0030660
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch30 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0030660
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
    and current batch30 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/golgi_associated_vesicle_membrane.yaml
  locator: Entire maintained target, every field, source placement, history, discussion
    and graph node/edge
  accessed_at: '2026-10-22T01:49:08Z'
  support: context_only
  summary: The exact single target was fully read and remains scientifically unchanged.
- evidence_id: policy
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent molecular-building-block and grounding definitions;
    CausalNode.component_ref; essentiality and structure-kind contracts
  accessed_at: '2026-10-22T01:49:08Z'
  support: context_only
  summary: Molecular material, complete membrane and enclosed compartment are different
    identities. A component_ref asserts correspondence to that local component; assembly
    necessity is distinct from function.
- evidence_id: graph-policy
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Actor identity and source-backed edges, graph scope and evidence
  accessed_at: '2026-10-22T01:49:08Z'
  support: context_only
  summary: Descriptive topology and experimentally observed marker changes need not
    imply a complete molecular mechanism.
- evidence_id: boundary-neighbor
  kind: record_content
  reference: data/structures/membrane_organelle/golgi_associated_vesicle.yaml
  locator: Entire frozen boundary-neighbor YAML
  accessed_at: '2026-10-22T01:49:08Z'
  support: context_only
  summary: The neighbor was read as boundary context, not as a second target or independent
    proof of biological claims.
- evidence_id: golgi-agent-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005798,GO:0030660,GO:0031985,GO:0031410,GO:0030659,GO:0030663,GO:0012510,GO:0030137,GO:0030126,GO:0000139,GO:0035964,GO:0006890,GO:0098791,GO:0005794,GO:0032580
  locator: All15 exact IDs, names, definitions, active flags, synonyms and typed returned
    child relations; no inverse whole-class has_part inference from subtype membership
  accessed_at: '2026-10-22T01:45:26.519695Z'
  support: supports
  summary: All15 requested GO terms are active and preserve the whole-vesicle, surrounding
    membrane, cisterna and Golgi subcompartment distinctions. GO0005798 has COPI-coated
    vesicle0030137 as an is_a child and membrane0030660 as a part_of child; membrane0030660
    has direct is_a children0030663 and0012510. GO0035964 defines Golgi-membrane evagination,
    and0030137 explicitly includes retrograde transport. GO0031985 has surrounding
    membrane0032580 as a part_of child; its broader subcompartment0098791 is part_of
    Golgi0005794.
  snapshot_sha256: 34aaae1d7d364a5ac751463694b3d5efaa32914ff567ac6f20cee1e204da2385
- evidence_id: golgi-agent-ancestors-0030660
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030660/ancestors?relations=is_a
  locator: Exact requested target and complete is_a-only ancestor list
  accessed_at: '2026-10-22T01:45:26.485126Z'
  support: supports
  summary: Native is_a-only ancestry includes cytoplasmic vesicle membrane0030659;
    the main response separately shows the direct child relation.
  snapshot_sha256: ace1741ac3eb1f5654030c258ee29087ff5c1f64f72f1c947078f27d70690a44
- evidence_id: golgi-agent-tax4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Exact taxId, scientificName, rank, lineage and alternate names
  accessed_at: '2026-10-22T01:10:58.502766Z'
  support: supports
  summary: ENA identifies4932 as Saccharomyces cerevisiae, species rank. This verifies
    the canonical species and distribution label without assigning a strain or measuring
    prevalence.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: golgi-agent-serafini1991-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1016/0092-8674%2891%2990176-y%22
  locator: Exact PMID/title/DOI/authors and complete abstractText only
  accessed_at: '2026-10-22T01:41:12.704965Z'
  support: supports
  summary: Native PMID1680566 identifies Serafini et al.1991 and the exact DOI. The
    complete primary abstract reports ARF enrichment on Golgi-derived COP-coated vesicles,
    uncoating-associated removal and GTP-dependent Golgi binding. The proposed GTP-hydrolysis
    modulation is explicitly a hypothesis; no full body, universal vesicle coat or
    yeast-specific experiment is inferred.
  snapshot_sha256: dea8968c03304cd9777691eda5c7ba9969cbd3d2e353a2a5c9ac6ff2ac69538f
- evidence_id: golgi-agent-letourneur1994-med
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A8001155%20AND%20SRC%3AMED
  locator: Exact MED PMID8001155, DOI10.1016/0092-8674(94)90011-6, authorString/title
    and complete abstractText
  accessed_at: '2026-10-22T01:46:55.479211Z'
  support: supports
  summary: Native PMID8001155 verifies the exact Letourneur1994 title, DOI and author
    order. The complete primary abstract describes yeast dilysine-tagged Ste2 retrieval,
    coatomer mutant defects, RET1 complementation and distinct in-vitro binding results.
    It supports the scoped yeast COPI retrieval example, not a universal coat on every
    Golgi-associated vesicle or a direct membrane-budding movie.
  snapshot_sha256: 114ac82ffa987599676b5331dd2d7d8975632094481f9220370985844929d635
- evidence_id: access-serafini1991-cell
  kind: authority
  reference: https://www.cell.com/cell/fulltext/0092-8674(91)90176-Y
  locator: Actual retained HTTP response, not scientific body
  accessed_at: '2026-10-22T01:44:32.306978Z'
  support: context_only
  summary: HTTP403 access response retained; no complete article body is inferred
    from its size. The separately cited native MED abstract is the inspected scientific
    scope.
  snapshot_sha256: 6972679c7bd4e7b1461adf79687f6311c03e8c381103a82e2b6f6343d98da530
- evidence_id: access-letourneur1994-publisher
  kind: authority
  reference: https://www.cell.com/cell/fulltext/0092-8674(94)90011-6
  locator: Actual retained HTTP response, not scientific body
  accessed_at: '2026-10-22T01:46:34.074436Z'
  support: context_only
  summary: HTTP403 access response retained; no complete article body is inferred
    from its size. The separately cited native MED abstract is the inspected scientific
    scope.
  snapshot_sha256: f6940b783e555dd1a3a22d3ff4c0002a416ddd3b82be3cbee605bf1f90aa8034
- evidence_id: access-letourneur1994-sciencedirect
  kind: authority
  reference: https://www.sciencedirect.com/science/article/pii/0092867494900116
  locator: Actual retained HTTP response, not scientific body
  accessed_at: '2026-10-22T01:46:54.977502Z'
  support: context_only
  summary: HTTP403 access response retained; no complete article body is inferred
    from its size. The separately cited native MED abstract is the inspected scientific
    scope.
  snapshot_sha256: 42326a4dc339a96379218685865d2af0cb6d6e6735c4db0aaac191d5da5431da
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/golgi_associated_vesicle_membrane.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T01:39:22Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/golgi_associated_vesicle_membrane.yaml'
  snapshot_sha256: 391e746e62266e594106ef3eb2da49c8487eb77c38eb754142c8e59f3f5fd881
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/golgi_associated_vesicle_membrane.yaml
    --out /private/tmp/cellstructure-batch30-20261022-frro2xh0/golgi_associated_vesicle_membrane-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T01:39:23Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/golgi_associated_vesicle_membrane.yaml\
    \ --out /private/tmp/cellstructure-batch30-20261022-frro2xh0/golgi_associated_vesicle_membrane-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch30-20261022-frro2xh0/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch30-20261022-frro2xh0/golgi_associated_vesicle_membrane-strict.tsv"
  snapshot_sha256: c1d95a3365d019430d9aaf9920ed4acadf149494c531845e47e29d08ab01526a
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/golgi_associated_vesicle_membrane.yaml;
    native collect() exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 12 of 12 collected target identifiers returned OK. No residuals. Native
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
  topic: Exact class, hierarchy and boundary
  outcome: supported
  target_ids:
  - GO:0030660
  summary: The record denotes the correct native GO class. Its parent, boundary/parthood
    and synonyms are supported at the specified relation scope. Whole vesicles/cisternae
    and surrounding membranes remain distinct; child-specific COPI and TGN properties
    are not exported to every member of the generic class.
  evidence_ids:
  - record
  - boundary-neighbor
  - golgi-agent-go
  - golgi-agent-ancestors-0030660
- assessment_id: scope
  area: scope
  topic: Yeast species and experimental boundaries
  outcome: supported
  target_ids:
  - GO:0030660
  summary: The yeast canonical example and occurrence statement are supported by the
    complete primary Letourneur abstract. Functional retrieval and coatomer mutants
    are not a measured prevalence estimate or a complete organelle-biogenesis assay.
    Earlier coat-protein source context is not relabelled as a yeast experiment.
  evidence_ids:
  - record
  - golgi-agent-tax4932
  - golgi-agent-serafini1991-meta
  - golgi-agent-letourneur1994-med
- assessment_id: composition
  area: grounding
  topic: Material constituent versus assembled structure
  outcome: supported
  target_ids:
  - GO:0030660
  summary: The reviewed-label-only row denotes the generic lipid material constituting
    the membrane boundary. It explicitly withholds the whole-membrane GO term as molecular
    grounding and makes no precise lipid-species or mixture assertion. No exact family/protein
    inventory is required for this material row.
  evidence_ids:
  - record
  - policy
  - golgi-agent-go
- assessment_id: necessity
  area: grounding
  topic: Formation necessity separated from collective boundary identity
  outcome: unknown
  target_ids:
  - GO:0030660
  summary: A bounding bilayer is constitutive of the named membrane-bounded class.
    The inspected sources do not test removal/substitution of individual lipid species
    or establish molecule-specific assembly necessity. The collective boundary assertion
    is not reinterpreted as proof that any named lipid, coatomer subunit or marker
    is individually required for structure formation.
  evidence_ids:
  - record
  - policy
  - golgi-agent-go
  - golgi-agent-serafini1991-meta
  - golgi-agent-letourneur1994-med
- assessment_id: function-graph
  area: graph
  topic: Five descriptive membrane and subtype edges
  outcome: supported
  target_ids:
  - GO:0030660
  summary: Parthood, enclosure and both direct child-membrane relationships match
    native GO. Golgi-membrane donation is a structural interpretation of the exact
    budding definition, with Serafini abstract support limited to the Golgi-derived
    coated subtype. No universal COPI coat, identified lipid-transfer mechanism or
    separate membrane function is asserted.
  evidence_ids:
  - record
  - graph-policy
  - golgi-agent-go
  - golgi-agent-serafini1991-meta
  - golgi-agent-letourneur1994-med
- assessment_id: completeness
  area: completeness
  topic: Whole target and bounded optional inventory
  outcome: supported
  target_ids:
  - GO:0030660
  summary: Every maintained field, discussion and source placement was read. No exact
    protein examples, gene/protein graph nodes, molecular stoichiometry, tracked image
    assets or verbatim snippets are asserted here. Optional coat inventories and unresolved
    exact lipid chemistry are not automatic findings; historical descriptions remain
    historical and are not recertified.
  evidence_ids:
  - record
  - policy
  - golgi-agent-go
  - golgi-agent-serafini1991-meta
  - golgi-agent-letourneur1994-med
findings: []
actions: []
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- The fresh target-resolver slice and all five corpus receipt/manifest checks are
  integrated in this completed review.
- No exact lipid mixture, individual lipid-species formation necessity or complete
  coat/protein inventory was established. The review does not infer an inventory defect
  from an optional field or historical TODO.
- 'Serafini1991 and Letourneur1994 are complete native primary abstracts only. Publisher
  responses returned403; no complete primary body, detailed mutant protocol, original
  image pixels or raw assays were inspected. The zero-hit DOI query for Letourneur
  is an indexing/access limitation: its PMID8001155 and Crossref identify the exact
  DOI, title and authors.'
- The yeast retrieval result is a COPI subtype example within a broad Golgi-associated-vesicle
  class. It does not establish that every generic vesicle is COPI coated.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User explicitly authorizes one review per uncovered target, including justified
  clean reviews, overriding the local issue-only output gate.
- Only unsaved review/support artifacts are written outside the repository; no scientific
  YAML, history, index, save or Git/publication mutation.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
