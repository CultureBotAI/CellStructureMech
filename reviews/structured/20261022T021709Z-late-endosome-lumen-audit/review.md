# Late endosome lumen identity, source and topology review

- Review: 20261022T021709Z-late-endosome-lumen-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T01:50:45Z
- Finished UTC: 2026-10-22T02:17:09Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

No concrete curation defect observed within the explicitly bounded source scope.

## Scope And Provenance

Entire single target: identity, hierarchy/parthood, material boundaries, source and taxonomic claims, examples, functions and every graph edge.

Selection: Target 5 of batch thirty-one in strict uncovered path order from fresh origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0031906 | data/structures/membrane_organelle/late_endosome_lumen.yaml | maintained | late endosome lumen |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native protein verify | passed | True | GO:0031906 | Focused native check passed; scientific scope assessed separately. |
| Native protein causal-graphs | passed | True | GO:0031906 | Focused native check passed; scientific scope assessed separately. |
| Focused native schema | passed | True | GO:0031906 | Focused validator passed. |
| Focused native strict | passed | True | GO:0031906 | Focused validator passed. |
| Expression-module applicability | not_applicable | False | GO:0031906 | No expression-module claim or dataset is used. Genome preparation, compartment topology and direct recruitment sources apply. |
| Claim-level scientific review | passed | True | GO:0031906 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0031906 | 8 of 10 collected target identifiers returned OK. PMID:11511343: UNREACHABLE; The bulk transport returned414; the independently retrieved exact MED identity confirms PMID11511343, DOI10.1016/s0092-8674(01)00434-2 and Ubiquitin-dependent sorting into the multivesicular body pathway requires the function of a conserved endosomal protein sorting complex, ESCRT-I. Scientific scope remains limited to the separately documented inspections.; PMID:12194857: UNREACHABLE; The bulk transport returned414; the independently retrieved exact MED identity confirms PMID12194857, DOI10.1016/s1534-5807(02)00220-4 and Escrt-III: an endosome-associated heterooligomeric protein complex required for mvb sorting. Scientific scope remains limited to the separately documented inspections. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0031906 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0031906 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0031906 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0031906 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0031906 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact structure and mereology

identity: supported. Targets: GO:0031906.

Native definitions and relations support the late endosome, its enclosing membrane and internal lumen as distinct structures/regions. MVB is a child example rather than a synonym for every late endosome.

### Molecular material versus whole compartment

grounding: supported. Targets: GO:0031906.

The lumen region correctly has no invented molecular inventory.

### Taxon and actual experimental context

scope: supported. Targets: GO:0031906.

Yeast MVB experiments support a late-endosome child example. COMMON is qualitative occurrence. Transient ESCRT complexes are not listed as stable organelle constituents, and the sources are not generalized to every endosome or cargo class.

### Bounded functional evidence

evidence: supported. Targets: GO:0031906.

GO0071985 and the yeast abstracts support cargo sorting into MVB luminal vesicles. Membrane sorting-surface and lumen receiving-space roles remain separate. Vps27 localization/recruitment is directly supported where cited.

### Every target graph edge

graph: supported. Targets: GO:0031906.

All three NONMECHANISTIC edges express supported specialized membrane/lumen is-a, late-endosome parthood and membrane enclosure.

### Unresolved inventories and evidence tiers

evidence: unknown. Targets: GO:0031906.

No complete molecular inventory, quantitative prevalence or isolated physical sufficiency experiment is established. Primary abstracts, selected primary-body sections and review synthesis retain distinct evidentiary roles.

### All maintained fields and native status

completeness: supported. Targets: GO:0031906.

Entire target, all graph edges, source placements, discussions and history inspected. No maintained image asset, numeric physical property, trait link, protein example or verbatim snippet is asserted. PROPOSED remains unchanged; historic issue closures are not independently recertified.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/late_endosome_lumen.yaml; Entire maintained target, all sources, examples, graph edges, discussions and history | context_only | Full target read; no scientific record or native status changed. |
| policy | docs/CURATION.md; Exact identity, hierarchy versus parthood and narrow source support | context_only | Whole structures, enclosed volumes and molecular material remain distinct; optional inventories do not require speculative completion. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, graph nodes and essentiality | context_only | Constitutive boundary material is not a knockout assertion about every chemical species. A descriptive graph still needs support at each edge. |
| root31-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005770,GO:0005768,GO:0005771,GO:0010008,GO:0031904,GO:0031906,GO:0031902,GO:0071985,GO:0000813,GO:0000814,GO:0000815,GO:0031039,GO:0005634,GO:0000228; Complete names, definitions, synonyms, active flags and all returned child relations for fourteen identifiers | supports | All fourteen active native entries were read. GO0005770 is an endosome child with MVB as an is_a child. Exact membrane0031902 and lumen0031906 are late-endosome parts, with direct generic membrane/lumen parents. GO0071985 describes MVB luminal-vesicle cargo entry. ESCRT definitions match the sorting context. Macronucleus0031039 denotes the transcriptional polyploid ciliate compartment, distinct from nuclear chromosome0000228. |
| root31-sources-katzmann2001-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A11511343%20AND%20SRC%3AMED; Exact selected MED bibliography, ordered authors and complete abstractText | supports | Exact MED PMID11511343, DOI10.1016/s0092-8674(01)00434-2, Ubiquitin-dependent sorting into the multivesicular body pathway requires the function of a conserved endosomal protein sorting complex, ESCRT-I., Katzmann DJ, Babst M, Emr SD.. The complete primary abstract supports yeast ESCRT-I ubiquitin recognition and required MVB cargo sorting; its historical subunit description is not treated as a complete current inventory. |
| root31-sources-babst2002-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A12194857%20AND%20SRC%3AMED; Exact selected MED bibliography, ordered authors and complete abstractText | supports | Exact MED PMID12194857, DOI10.1016/s1534-5807(02)00220-4, Escrt-III: an endosome-associated heterooligomeric protein complex required for mvb sorting., Babst M, Katzmann DJ, Estepa-Sabal EJ, Meerloo T, Emr SD.. The complete primary abstract describes transient yeast ESCRT-III assembly, endosomal recruitment and MVB sorting requirements. It does not independently isolate the physical force of membrane deformation. |
| root31-sources-SL0336 | https://rest.uniprot.org/locations/SL-0336.json; Complete location ID/name/definition/synonyms, exact GO mapping, isA and partOf | supports | The exact native entry maps to GO0031906, with endosome-lumen is_a and late-endosome partOf. The recorded exact synonym matches. Nested generic entries are not confused with the target identity. |
| root31-sources-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Exact taxId, scientificName, rank, lineage and otherNames | supports | ENA4932 is Saccharomyces cerevisiae at species rank. Qualitative occurrence is not a measured prevalence or an exact experimental-strain determination. |
| native-verify | /private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/late_endosome_lumen.yaml --verify; Entire retained focused native output | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/late_endosome_lumen.yaml --causal-graphs; Entire retained focused native output | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/membrane_organelle/late_endosome_lumen.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/late_endosome_lumen.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/late_endosome_lumen.yaml --out /private/tmp/cellstructure-batch31-20261022-ag46a4d4/late_endosome_lumen-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/late_endosome_lumen.yaml --out /private/tmp/cellstructure-batch31-20261022-ag46a4d4/late_endosome_lumen-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch31-20261022-ag46a4d4/late_endosome_lumen-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/late_endosome_lumen.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 8 of 10 collected target identifiers returned OK. PMID:11511343: UNREACHABLE; The bulk transport returned414; the independently retrieved exact MED identity confirms PMID11511343, DOI10.1016/s0092-8674(01)00434-2 and Ubiquitin-dependent sorting into the multivesicular body pathway requires the function of a conserved endosomal protein sorting complex, ESCRT-I. Scientific scope remains limited to the separately documented inspections.; PMID:12194857: UNREACHABLE; The bulk transport returned414; the independently retrieved exact MED identity confirms PMID12194857, DOI10.1016/s1534-5807(02)00220-4 and Escrt-III: an endosome-associated heterooligomeric protein complex required for mvb sorting. Scientific scope remains limited to the separately documented inspections. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- COMMON is qualitative occurrence, not measured prevalence. Historical authorship and earlier issue dispositions are not independently recertified.
- Katzmann2001 and, where cited, Babst2002 were read as complete primary abstracts only. They do not establish every physical mechanism or exact experimental genotype.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The user explicitly authorizes bundles for every uncovered record, including honest no-finding reviews. Scientific content remains unchanged.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T021709Z-late-endosome-lumen-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Late endosome lumen identity, source and topology review
started_at: '2026-10-22T01:50:45Z'
finished_at: '2026-10-22T02:17:09Z'
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
summary: No concrete curation defect observed within the explicitly bounded source
  scope.
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
  - path: .claude/skills/uniprot-protein-examples/SKILL.md
    sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
    role: context
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/membrane_organelle/late_endosome.yaml
    sha256: af154194fa19aa780722ab1444ffedd803936571c202be13ce49983c7d9352a0
    role: context
  - path: data/structures/membrane_organelle/late_endosome_lumen.yaml
    sha256: f4f801cc662e9d680eec7749b54e4c69b699e76e8af5faba7b27316d3b0ecc91
    role: target
  - path: data/structures/membrane_organelle/late_endosome_membrane.yaml
    sha256: abd97317590eaf6f8b21b611d08470cc92e1a3b8bb4773381d092e2e4ddb27cc
    role: context
  - path: data/structures/membrane_organelle/multivesicular_body.yaml
    sha256: cf6713b73e225eb2413a2a8b8a0fc9dfb6cf84a12f10133e3dcbec03791585a9
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
  - path: scripts/uniprot_genes.py
    sha256: feb9042b212bc639bc2603c186c6e328fa142c2641e93fc1418ad5a14e1d5faf
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: GO:0031906
  path: data/structures/membrane_organelle/late_endosome_lumen.yaml
  label: late endosome lumen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/late_endosome_lumen.yaml
    role: maintained scientific record
scope:
  description: 'Entire single target: identity, hierarchy/parthood, material boundaries,
    source and taxonomic claims, examples, functions and every graph edge.'
  selection: Target 5 of batch thirty-one in strict uncovered path order from fresh
    origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0031906
checks:
- check_id: native-verify
  name: Native protein verify
  status: passed
  required: true
  target_ids:
  - GO:0031906
  command: /private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/late_endosome_lumen.yaml
    --verify
  exit_code: 0
  summary: Focused native check passed; scientific scope assessed separately.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Native protein causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0031906
  command: /private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/late_endosome_lumen.yaml
    --causal-graphs
  exit_code: 0
  summary: Focused native check passed; scientific scope assessed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0031906
  command: just validate data/structures/membrane_organelle/late_endosome_lumen.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0031906
  command: just validate-strict data/structures/membrane_organelle/late_endosome_lumen.yaml
    --out /private/tmp/cellstructure-batch31-20261022-ag46a4d4/late_endosome_lumen-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0031906
  summary: No expression-module claim or dataset is used. Genome preparation, compartment
    topology and direct recruitment sources apply.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0031906
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - schema
  - root31-sources-go
  - root31-sources-katzmann2001-meta
  - root31-sources-babst2002-meta
  - root31-sources-SL0336
  - root31-sources-tax4932
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0031906
  summary: '8 of 10 collected target identifiers returned OK. PMID:11511343: UNREACHABLE;
    The bulk transport returned414; the independently retrieved exact MED identity
    confirms PMID11511343, DOI10.1016/s0092-8674(01)00434-2 and Ubiquitin-dependent
    sorting into the multivesicular body pathway requires the function of a conserved
    endosomal protein sorting complex, ESCRT-I. Scientific scope remains limited to
    the separately documented inspections.; PMID:12194857: UNREACHABLE; The bulk transport
    returned414; the independently retrieved exact MED identity confirms PMID12194857,
    DOI10.1016/s1534-5807(02)00220-4 and Escrt-III: an endosome-associated heterooligomeric
    protein complex required for mvb sorting. Scientific scope remains limited to
    the separately documented inspections. Native source checks are separately scoped;
    skipped or unreachable identifiers are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - root31-sources-katzmann2001-meta
  - root31-sources-babst2002-meta
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0031906
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch31 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0031906
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch31 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0031906
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch31 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0031906
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch31 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0031906
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
    and current batch31 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/late_endosome_lumen.yaml
  locator: Entire maintained target, all sources, examples, graph edges, discussions
    and history
  accessed_at: '2026-10-22T02:01:23Z'
  support: context_only
  summary: Full target read; no scientific record or native status changed.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact identity, hierarchy versus parthood and narrow source support
  accessed_at: '2026-10-22T02:01:23Z'
  support: context_only
  summary: Whole structures, enclosed volumes and molecular material remain distinct;
    optional inventories do not require speculative completion.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, graph nodes and essentiality
  accessed_at: '2026-10-22T02:01:23Z'
  support: context_only
  summary: Constitutive boundary material is not a knockout assertion about every
    chemical species. A descriptive graph still needs support at each edge.
- evidence_id: root31-sources-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005770,GO:0005768,GO:0005771,GO:0010008,GO:0031904,GO:0031906,GO:0031902,GO:0071985,GO:0000813,GO:0000814,GO:0000815,GO:0031039,GO:0005634,GO:0000228
  locator: Complete names, definitions, synonyms, active flags and all returned child
    relations for fourteen identifiers
  accessed_at: '2026-10-22T01:51:20.292950Z'
  support: supports
  summary: All fourteen active native entries were read. GO0005770 is an endosome
    child with MVB as an is_a child. Exact membrane0031902 and lumen0031906 are late-endosome
    parts, with direct generic membrane/lumen parents. GO0071985 describes MVB luminal-vesicle
    cargo entry. ESCRT definitions match the sorting context. Macronucleus0031039
    denotes the transcriptional polyploid ciliate compartment, distinct from nuclear
    chromosome0000228.
  snapshot_sha256: 9247adc57897e68974e7ff5d2e137b8a39b0af19d4dbba94a647479312167c7a
- evidence_id: root31-sources-katzmann2001-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A11511343%20AND%20SRC%3AMED
  locator: Exact selected MED bibliography, ordered authors and complete abstractText
  accessed_at: '2026-10-22T01:10:57.861587Z'
  support: supports
  summary: Exact MED PMID11511343, DOI10.1016/s0092-8674(01)00434-2, Ubiquitin-dependent
    sorting into the multivesicular body pathway requires the function of a conserved
    endosomal protein sorting complex, ESCRT-I., Katzmann DJ, Babst M, Emr SD.. The
    complete primary abstract supports yeast ESCRT-I ubiquitin recognition and required
    MVB cargo sorting; its historical subunit description is not treated as a complete
    current inventory.
  snapshot_sha256: 89b0ab16f1c997094ab3253063701f5097b815c030e16320d5d41f485e3d50a9
- evidence_id: root31-sources-babst2002-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A12194857%20AND%20SRC%3AMED
  locator: Exact selected MED bibliography, ordered authors and complete abstractText
  accessed_at: '2026-10-22T01:10:58.446989Z'
  support: supports
  summary: 'Exact MED PMID12194857, DOI10.1016/s1534-5807(02)00220-4, Escrt-III: an
    endosome-associated heterooligomeric protein complex required for mvb sorting.,
    Babst M, Katzmann DJ, Estepa-Sabal EJ, Meerloo T, Emr SD.. The complete primary
    abstract describes transient yeast ESCRT-III assembly, endosomal recruitment and
    MVB sorting requirements. It does not independently isolate the physical force
    of membrane deformation.'
  snapshot_sha256: 154c66e5c81005bcb646718e07a114e6c610e20c4a80803a5505061f4c107317
- evidence_id: root31-sources-SL0336
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0336.json
  locator: Complete location ID/name/definition/synonyms, exact GO mapping, isA and
    partOf
  accessed_at: '2026-10-22T01:51:20.292553Z'
  support: supports
  summary: The exact native entry maps to GO0031906, with endosome-lumen is_a and
    late-endosome partOf. The recorded exact synonym matches. Nested generic entries
    are not confused with the target identity.
  snapshot_sha256: 8c1a29e54193d2163b81d98bb3ee9362906c24904d35012ee021ce307ebbab37
- evidence_id: root31-sources-tax4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Exact taxId, scientificName, rank, lineage and otherNames
  accessed_at: '2026-10-22T01:10:58.502766Z'
  support: supports
  summary: ENA4932 is Saccharomyces cerevisiae at species rank. Qualitative occurrence
    is not a measured prevalence or an exact experimental-strain determination.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/late_endosome_lumen.yaml
    --verify
  locator: Entire retained focused native output
  accessed_at: '2026-10-22T01:51:18.936849Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/late_endosome_lumen.yaml
    --causal-graphs
  locator: Entire retained focused native output
  accessed_at: '2026-10-22T01:51:19.462084Z'
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
  reference: just validate data/structures/membrane_organelle/late_endosome_lumen.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T01:50:47Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/late_endosome_lumen.yaml'
  snapshot_sha256: 07a7714d624d24125c55c516c70a8a8936b9039985481199899e7c0066fca7c2
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/late_endosome_lumen.yaml
    --out /private/tmp/cellstructure-batch31-20261022-ag46a4d4/late_endosome_lumen-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T01:50:48Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/late_endosome_lumen.yaml\
    \ --out /private/tmp/cellstructure-batch31-20261022-ag46a4d4/late_endosome_lumen-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch31-20261022-ag46a4d4/late_endosome_lumen-strict.tsv"
  snapshot_sha256: d5837d7f7ce099c72abc76397fa45f7230d001384ab7aa7b884beb4567eeb58f
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/late_endosome_lumen.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '8 of 10 collected target identifiers returned OK. PMID:11511343: UNREACHABLE;
    The bulk transport returned414; the independently retrieved exact MED identity
    confirms PMID11511343, DOI10.1016/s0092-8674(01)00434-2 and Ubiquitin-dependent
    sorting into the multivesicular body pathway requires the function of a conserved
    endosomal protein sorting complex, ESCRT-I. Scientific scope remains limited to
    the separately documented inspections.; PMID:12194857: UNREACHABLE; The bulk transport
    returned414; the independently retrieved exact MED identity confirms PMID12194857,
    DOI10.1016/s1534-5807(02)00220-4 and Escrt-III: an endosome-associated heterooligomeric
    protein complex required for mvb sorting. Scientific scope remains limited to
    the separately documented inspections. Native source checks are separately scoped;
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
  topic: Exact structure and mereology
  outcome: supported
  target_ids:
  - GO:0031906
  summary: Native definitions and relations support the late endosome, its enclosing
    membrane and internal lumen as distinct structures/regions. MVB is a child example
    rather than a synonym for every late endosome.
  evidence_ids:
  - record
  - policy
  - root31-sources-go
  - root31-sources-SL0336
- assessment_id: composition
  area: grounding
  topic: Molecular material versus whole compartment
  outcome: supported
  target_ids:
  - GO:0031906
  summary: The lumen region correctly has no invented molecular inventory.
  evidence_ids:
  - record
  - schema
  - root31-sources-go
- assessment_id: scope
  area: scope
  topic: Taxon and actual experimental context
  outcome: supported
  target_ids:
  - GO:0031906
  summary: Yeast MVB experiments support a late-endosome child example. COMMON is
    qualitative occurrence. Transient ESCRT complexes are not listed as stable organelle
    constituents, and the sources are not generalized to every endosome or cargo class.
  evidence_ids:
  - record
  - root31-sources-tax4932
  - root31-sources-katzmann2001-meta
  - root31-sources-babst2002-meta
- assessment_id: function
  area: evidence
  topic: Bounded functional evidence
  outcome: supported
  target_ids:
  - GO:0031906
  summary: GO0071985 and the yeast abstracts support cargo sorting into MVB luminal
    vesicles. Membrane sorting-surface and lumen receiving-space roles remain separate.
    Vps27 localization/recruitment is directly supported where cited.
  evidence_ids:
  - record
  - root31-sources-go
  - root31-sources-katzmann2001-meta
  - root31-sources-babst2002-meta
- assessment_id: graph
  area: graph
  topic: Every target graph edge
  outcome: supported
  target_ids:
  - GO:0031906
  summary: All three NONMECHANISTIC edges express supported specialized membrane/lumen
    is-a, late-endosome parthood and membrane enclosure.
  evidence_ids:
  - record
  - root31-sources-go
  - root31-sources-katzmann2001-meta
  - root31-sources-babst2002-meta
  - root31-sources-SL0336
- assessment_id: limits
  area: evidence
  topic: Unresolved inventories and evidence tiers
  outcome: unknown
  target_ids:
  - GO:0031906
  summary: No complete molecular inventory, quantitative prevalence or isolated physical
    sufficiency experiment is established. Primary abstracts, selected primary-body
    sections and review synthesis retain distinct evidentiary roles.
  evidence_ids:
  - record
  - schema
  - root31-sources-go
  - root31-sources-katzmann2001-meta
  - root31-sources-babst2002-meta
- assessment_id: coverage
  area: completeness
  topic: All maintained fields and native status
  outcome: supported
  target_ids:
  - GO:0031906
  summary: Entire target, all graph edges, source placements, discussions and history
    inspected. No maintained image asset, numeric physical property, trait link, protein
    example or verbatim snippet is asserted. PROPOSED remains unchanged; historic
    issue closures are not independently recertified.
  evidence_ids:
  - record
  - policy
  - root31-sources-go
  - root31-sources-katzmann2001-meta
  - root31-sources-babst2002-meta
findings: []
actions: []
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- COMMON is qualitative occurrence, not measured prevalence. Historical authorship
  and earlier issue dispositions are not independently recertified.
- Katzmann2001 and, where cited, Babst2002 were read as complete primary abstracts
  only. They do not establish every physical mechanism or exact experimental genotype.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The user explicitly authorizes bundles for every uncovered record, including honest
  no-finding reviews. Scientific content remains unchanged.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
