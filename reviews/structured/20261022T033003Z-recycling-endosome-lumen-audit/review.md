# Recycling endosome lumen scientific review

- Review: 20261022T033003Z-recycling-endosome-lumen-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T03:14:16Z
- Finished UTC: 2026-10-22T03:30:03Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Exact recycling-endosome lumen identity, hierarchy, membrane boundary and bounded species example are supported; the descriptive graph and deliberate absence of obligatory cargo components are consistent. No concrete curation finding.

## Scope And Provenance

Entire single target including every component, hierarchy, taxon/example, function/graph, source, discussion and history. Additional frozen local inputs are read at the precise scope declared in their evidence rows; literature read extents and image inspection are separately stated.

Selection: Batch39 exact path-ordered target 10; fresh f97b native inspection/schema/strict passed before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0034777 | data/structures/membrane_organelle/recycling_endosome_lumen.yaml | maintained | recycling endosome lumen |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0034777 | Focused validator passed. |
| Focused native strict | passed | True | GO:0034777 | Focused validator passed. |
| Native causal-graphs | passed | True | GO:0034777 | Native check passed; exact scientific scope was assessed separately. |
| Individual protein verification applicability | not_applicable | False | GO:0034777 | No individual protein accession or gene/protein graph node occurs in the target. |
| Expression-module applicability | not_applicable | False | GO:0034777 | No computational expression-module assertion is made; experimental gene interventions do not require expression-module evidence. |
| Claim-level scientific review | passed | True | GO:0034777 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0034777 | 6 of 7 collected target identifiers returned OK. PMID:11683389: UNREACHABLE; Unique native MED result verifies exact PMID, title, DOI and PMC/null identity after the bulk eutils414 failure. Abstract/body scientific scopes remain explicitly bounded in separate evidence rows. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0034777 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0034777 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0034777 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0034777 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0034777 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact organelle/volume identity and hierarchy

identity: supported. Targets: GO:0034777.

The active GO identity, declared definition, hierarchy/parthood, literal synonym scopes and exact SL mapping are supported. Complete boundary neighbors preserve whole-versus-membrane-versus-volume distinctions. The graph uses the proper types for these structural entities.

### Species and life-stage occurrence

scope: supported. Targets: GO:0034777.

The native species identity and Jeffries complete primary abstract support the bounded T. brucei stage-dependent compartment example. VARIABLE describes the qualitative difference in expression/compartment morphology; it is not a measured prevalence fraction. Enclosed lumen is the structural interpretation of those membrane compartments, not an assertion that transferrin receptor is soluble luminal cargo.

### Enclosed volume without obligatory cargo

grounding: supported. Targets: GO:0034777.

The absence of asserted molecular components is appropriate for this generic bounded volume. The membrane is represented as a boundary node and transferrin receptor is not misclassified as a soluble luminal constituent. Individual cargo or protein formation necessity is neither established nor asserted.

### Descriptive compartmentalization and topology

graph: supported. Targets: GO:0034777.

The function and NONMECHANISTIC graph accurately express endosome-lumen specialization, organelle parthood and membrane enclosure. No cargo-selection cascade, Rab11 mechanism or mandatory cargo inventory is claimed. The resolved boundary interpretation is consistent with the current nodes.

### Bounded source audit and unchanged status

provenance: supported. Targets: GO:0034777.

All target claims were reviewed at the declared source read scopes, with primary/secondary/abstract/native authority tiers separated. No scientific mutation, mapping-status promotion, review persistence or publication is implied.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/recycling_endosome_lumen.yaml; Entire maintained YAML including all fields, graphs, history and discussions | context_only | The entire target was read; scientific content, status and history remain unchanged. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent type/grounding/formation-necessity and graph/component_ref contracts | context_only | A LIPID molecular constituent is distinct from a complete GO membrane structure. Accurate OTHER structural constituents are not categorically forbidden. Constitution, localization, regulatory activity and cell viability do not establish individual formation necessity. |
| recycling-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0055037,GO:0055038,GO:0034777,GO:0005768,GO:0031904; Complete native definitions, synonyms and explicitly typed child relations | supports | Five active GO entries distinguish recycling endosome, its whole membrane and lumen, generic endosome and endosome lumen. GO0005768 lists0055037 is_a;0055037 lists0055038 and0034777 part_of;0031904 lists0034777 is_a. Exact whole synonyms and lumen definition agree. |
| recycling-agent-SL0345 | https://rest.uniprot.org/locations/SL-0345.json; Complete exact native location definition, synonym, GO map and typed hierarchy | supports | SL0345 exactly maps Recycling endosome lumen to GO0034777, lists Recycling endosomal lumen, isA Endosome lumen and partOf Recycling endosome. |
| recycling-agent-tax5691 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5691; Complete native taxId/name/rank/lineage | supports | ENA5691 confirms Trypanosoma brucei at species rank. This response alone does not establish stage-specific anatomy, strain or abundance. |
| recycling-agent-PMID-11683389 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A11683389%20AND%20SRC%3AMED; Unique MED identity/title/authors/DOI/year and complete primary abstract; no main body | supports | Exact PMID11683389/DOI10.1242/jcs.114.14.2617 identifies Jeffries/Morgan/Field2001. Complete abstract describes TbRAB11-positive procyclic and bloodstream compartments, higher bloodstream expression, larger posterior compartment, and transferrin-receptor/internalized anti-VSG colocalization. |
| neighbor-recycling_endosome | data/structures/membrane_organelle/recycling_endosome.yaml; Entire frozen maintained boundary neighbor | context_only | Whole organelle, membrane and enclosed volume are distinct; neighbor content is contextual, not independent experimental evidence. |
| neighbor-recycling_endosome_membrane | data/structures/membrane_organelle/recycling_endosome_membrane.yaml; Entire frozen maintained boundary neighbor | context_only | Whole organelle, membrane and enclosed volume are distinct; neighbor content is contextual, not independent experimental evidence. |
| schema-result | just validate data/structures/membrane_organelle/recycling_endosome_lumen.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/recycling_endosome_lumen.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/recycling_endosome_lumen.yaml --out /private/tmp/cellstructure-batch39-20261022-9ejlvnby/recycling_endosome_lumen-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/recycling_endosome_lumen.yaml --out /private/tmp/cellstructure-batch39-20261022-9ejlvnby/recycling_endosome_lumen-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch39-20261022-9ejlvnby/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch39-20261022-9ejlvnby/recycling_endosome_lumen-strict.tsv |
| recycling-lumen-causal-graphs | /private/tmp/cellstructure-batch39-20261022-9ejlvnby/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/recycling_endosome_lumen.yaml; Complete native read-only log | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/recycling_endosome_lumen.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 6 of 7 collected target identifiers returned OK. PMID:11683389: UNREACHABLE; Unique native MED result verifies exact PMID, title, DOI and PMC/null identity after the bulk eutils414 failure. Abstract/body scientific scopes remain explicitly bounded in separate evidence rows. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Jeffries2001 was verified by exact native MED identity and its complete abstract; the attempted publisher body returned403. No strain-specific ultrastructural measurements or complete original Methods were certified.
- The source supports the species compartment example at abstract-level resolution; it is not a dedicated lumen proteome, molecular inventory or formation-necessity assay. No such claim is required by this volume record.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User all-record goal authorizes honest clean reviews; no issue was invented for the local issue-only convention. Parent owns finalization, persistence and integration of the five same-base full-corpus gates.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T033003Z-recycling-endosome-lumen-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Recycling endosome lumen scientific review
started_at: '2026-10-22T03:14:16Z'
finished_at: '2026-10-22T03:30:03Z'
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
summary: Exact recycling-endosome lumen identity, hierarchy, membrane boundary and
  bounded species example are supported; the descriptive graph and deliberate absence
  of obligatory cargo components are consistent. No concrete curation finding.
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
    role: target
  - path: data/structures/membrane_organelle/recycling_endosome_membrane.yaml
    sha256: cc07cfcf4d3c8fcfac3594e3dec18791b1e5f40e13d867fcdb4ef355f07aebf0
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
- target_id: GO:0034777
  path: data/structures/membrane_organelle/recycling_endosome_lumen.yaml
  label: recycling endosome lumen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/recycling_endosome_lumen.yaml
    role: maintained scientific record
scope:
  description: Entire single target including every component, hierarchy, taxon/example,
    function/graph, source, discussion and history. Additional frozen local inputs
    are read at the precise scope declared in their evidence rows; literature read
    extents and image inspection are separately stated.
  selection: Batch39 exact path-ordered target 10; fresh f97b native inspection/schema/strict
    passed before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0034777
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0034777
  command: just validate data/structures/membrane_organelle/recycling_endosome_lumen.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0034777
  command: just validate-strict data/structures/membrane_organelle/recycling_endosome_lumen.yaml
    --out /private/tmp/cellstructure-batch39-20261022-9ejlvnby/recycling_endosome_lumen-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: causal-graphs
  name: Native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0034777
  command: /private/tmp/cellstructure-batch39-20261022-9ejlvnby/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/recycling_endosome_lumen.yaml
  exit_code: 0
  summary: Native check passed; exact scientific scope was assessed separately.
  evidence_ids:
  - recycling-lumen-causal-graphs
- check_id: protein-applicability
  name: Individual protein verification applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0034777
  summary: No individual protein accession or gene/protein graph node occurs in the
    target.
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0034777
  summary: No computational expression-module assertion is made; experimental gene
    interventions do not require expression-module evidence.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0034777
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - recycling-agent-go
  - recycling-agent-SL0345
  - recycling-agent-tax5691
  - recycling-agent-PMID-11683389
  - neighbor-recycling_endosome
  - neighbor-recycling_endosome_membrane
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0034777
  summary: '6 of 7 collected target identifiers returned OK. PMID:11683389: UNREACHABLE;
    Unique native MED result verifies exact PMID, title, DOI and PMC/null identity
    after the bulk eutils414 failure. Abstract/body scientific scopes remain explicitly
    bounded in separate evidence rows. Native source checks are separately scoped;
    skipped or unreachable identifiers are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - recycling-agent-PMID-11683389
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0034777
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch39 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0034777
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch39 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0034777
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch39 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0034777
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch39 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0034777
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
    and current batch39 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/recycling_endosome_lumen.yaml
  locator: Entire maintained YAML including all fields, graphs, history and discussions
  accessed_at: '2026-10-22T03:22:44Z'
  support: context_only
  summary: The entire target was read; scientific content, status and history remain
    unchanged.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent type/grounding/formation-necessity and graph/component_ref
    contracts
  accessed_at: '2026-10-22T03:22:44Z'
  support: context_only
  summary: A LIPID molecular constituent is distinct from a complete GO membrane structure.
    Accurate OTHER structural constituents are not categorically forbidden. Constitution,
    localization, regulatory activity and cell viability do not establish individual
    formation necessity.
- evidence_id: recycling-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0055037,GO:0055038,GO:0034777,GO:0005768,GO:0031904
  locator: Complete native definitions, synonyms and explicitly typed child relations
  accessed_at: '2026-10-22T03:15:32.604047Z'
  support: supports
  summary: Five active GO entries distinguish recycling endosome, its whole membrane
    and lumen, generic endosome and endosome lumen. GO0005768 lists0055037 is_a;0055037
    lists0055038 and0034777 part_of;0031904 lists0034777 is_a. Exact whole synonyms
    and lumen definition agree.
  snapshot_sha256: b5375b82c484a03cfcc9a63275193399fc2f0bda198944f0d0721c8ed14d9eb4
- evidence_id: recycling-agent-SL0345
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0345.json
  locator: Complete exact native location definition, synonym, GO map and typed hierarchy
  accessed_at: '2026-10-22T03:15:32.604586Z'
  support: supports
  summary: SL0345 exactly maps Recycling endosome lumen to GO0034777, lists Recycling
    endosomal lumen, isA Endosome lumen and partOf Recycling endosome.
  snapshot_sha256: c63ca9bd1055d1cb224612d7610c2451a92f253a07790db1a69dceafdf24501c
- evidence_id: recycling-agent-tax5691
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5691
  locator: Complete native taxId/name/rank/lineage
  accessed_at: '2026-10-22T03:15:32.604662Z'
  support: supports
  summary: ENA5691 confirms Trypanosoma brucei at species rank. This response alone
    does not establish stage-specific anatomy, strain or abundance.
  snapshot_sha256: ba78ff6fe5de62b2654b61e249c2c87b239dca0208950b0e4ecf3ef2d81c99be
- evidence_id: recycling-agent-PMID-11683389
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A11683389%20AND%20SRC%3AMED
  locator: Unique MED identity/title/authors/DOI/year and complete primary abstract;
    no main body
  accessed_at: '2026-10-22T03:15:33.333082Z'
  support: supports
  summary: Exact PMID11683389/DOI10.1242/jcs.114.14.2617 identifies Jeffries/Morgan/Field2001.
    Complete abstract describes TbRAB11-positive procyclic and bloodstream compartments,
    higher bloodstream expression, larger posterior compartment, and transferrin-receptor/internalized
    anti-VSG colocalization.
  snapshot_sha256: 47119d081d8f1c7a80b63125de10f3688288733071805146639a1877e40653f0
- evidence_id: neighbor-recycling_endosome
  kind: record_content
  reference: data/structures/membrane_organelle/recycling_endosome.yaml
  locator: Entire frozen maintained boundary neighbor
  accessed_at: '2026-10-22T03:22:44Z'
  support: context_only
  summary: Whole organelle, membrane and enclosed volume are distinct; neighbor content
    is contextual, not independent experimental evidence.
- evidence_id: neighbor-recycling_endosome_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/recycling_endosome_membrane.yaml
  locator: Entire frozen maintained boundary neighbor
  accessed_at: '2026-10-22T03:22:44Z'
  support: context_only
  summary: Whole organelle, membrane and enclosed volume are distinct; neighbor content
    is contextual, not independent experimental evidence.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/recycling_endosome_lumen.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:14:17Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/recycling_endosome_lumen.yaml'
  snapshot_sha256: 70e9af22931c2db7fcd939e1266462a4f3e6af9eec2c776521728dab2fd7b124
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/recycling_endosome_lumen.yaml
    --out /private/tmp/cellstructure-batch39-20261022-9ejlvnby/recycling_endosome_lumen-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:14:18Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/recycling_endosome_lumen.yaml\
    \ --out /private/tmp/cellstructure-batch39-20261022-9ejlvnby/recycling_endosome_lumen-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch39-20261022-9ejlvnby/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch39-20261022-9ejlvnby/recycling_endosome_lumen-strict.tsv"
  snapshot_sha256: 555b80d616bc840fcc9e6a3af3f4ef1e15cdfa09881482e263e4e6c58f13acd0
- evidence_id: recycling-lumen-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch39-20261022-9ejlvnby/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/recycling_endosome_lumen.yaml
  locator: Complete native read-only log
  accessed_at: '2026-10-22T03:20:21.380459Z'
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
  locator: data/structures/membrane_organelle/recycling_endosome_lumen.yaml; native
    collect() exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '6 of 7 collected target identifiers returned OK. PMID:11683389: UNREACHABLE;
    Unique native MED result verifies exact PMID, title, DOI and PMC/null identity
    after the bulk eutils414 failure. Abstract/body scientific scopes remain explicitly
    bounded in separate evidence rows. Native source checks are separately scoped;
    skipped or unreachable identifiers are not silently counted as resolved.'
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
  topic: Exact organelle/volume identity and hierarchy
  outcome: supported
  target_ids:
  - GO:0034777
  summary: The active GO identity, declared definition, hierarchy/parthood, literal
    synonym scopes and exact SL mapping are supported. Complete boundary neighbors
    preserve whole-versus-membrane-versus-volume distinctions. The graph uses the
    proper types for these structural entities.
  evidence_ids:
  - record
  - recycling-agent-go
  - recycling-agent-SL0345
- assessment_id: scope
  area: scope
  topic: Species and life-stage occurrence
  outcome: supported
  target_ids:
  - GO:0034777
  summary: The native species identity and Jeffries complete primary abstract support
    the bounded T. brucei stage-dependent compartment example. VARIABLE describes
    the qualitative difference in expression/compartment morphology; it is not a measured
    prevalence fraction. Enclosed lumen is the structural interpretation of those
    membrane compartments, not an assertion that transferrin receptor is soluble luminal
    cargo.
  evidence_ids:
  - record
  - recycling-agent-tax5691
  - recycling-agent-PMID-11683389
  - recycling-agent-go
- assessment_id: components
  area: grounding
  topic: Enclosed volume without obligatory cargo
  outcome: supported
  target_ids:
  - GO:0034777
  summary: The absence of asserted molecular components is appropriate for this generic
    bounded volume. The membrane is represented as a boundary node and transferrin
    receptor is not misclassified as a soluble luminal constituent. Individual cargo
    or protein formation necessity is neither established nor asserted.
  evidence_ids:
  - record
  - schema
  - recycling-agent-go
- assessment_id: function-graph
  area: graph
  topic: Descriptive compartmentalization and topology
  outcome: supported
  target_ids:
  - GO:0034777
  summary: The function and NONMECHANISTIC graph accurately express endosome-lumen
    specialization, organelle parthood and membrane enclosure. No cargo-selection
    cascade, Rab11 mechanism or mandatory cargo inventory is claimed. The resolved
    boundary interpretation is consistent with the current nodes.
  evidence_ids:
  - record
  - recycling-agent-go
  - recycling-agent-SL0345
- assessment_id: provenance
  area: provenance
  topic: Bounded source audit and unchanged status
  outcome: supported
  target_ids:
  - GO:0034777
  summary: All target claims were reviewed at the declared source read scopes, with
    primary/secondary/abstract/native authority tiers separated. No scientific mutation,
    mapping-status promotion, review persistence or publication is implied.
  evidence_ids:
  - record
  - recycling-agent-go
  - recycling-agent-SL0345
  - recycling-agent-tax5691
  - recycling-agent-PMID-11683389
findings: []
actions: []
limitations:
- Jeffries2001 was verified by exact native MED identity and its complete abstract;
  the attempted publisher body returned403. No strain-specific ultrastructural measurements
  or complete original Methods were certified.
- The source supports the species compartment example at abstract-level resolution;
  it is not a dedicated lumen proteome, molecular inventory or formation-necessity
  assay. No such claim is required by this volume record.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User all-record goal authorizes honest clean reviews; no issue was invented for
  the local issue-only convention. Parent owns finalization, persistence and integration
  of the five same-base full-corpus gates.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
