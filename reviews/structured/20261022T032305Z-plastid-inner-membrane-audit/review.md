# Plastid inner membrane scientific review

- Review: 20261022T032305Z-plastid-inner-membrane-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T03:05:51Z
- Finished UTC: 2026-10-22T03:23:05Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

No concrete defect observed in the exact identity, source-bounded exemplar and descriptive topology/class scope of this plastid compartment.

## Scope And Provenance

Entire single maintained target; two adjacent reviewed targets frozen as boundary context only.

Selection: Target 8 of batch38, the next uncovered record in strict path order at fresh origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0009528 | data/structures/membrane_organelle/plastid_inner_membrane.yaml | maintained | plastid inner membrane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0009528 | Focused validator passed. |
| Focused native strict | passed | True | GO:0009528 | Focused validator passed. |
| Native graph protein-reference check | passed | True | GO:0009528 | No named protein node requires an accession in this bounded topology graph. |
| Expression-module applicability | not_applicable | False | GO:0009528 | No expression-module, regulator or transcriptional mechanism is claimed. |
| Claim-level scientific review | passed | True | GO:0009528 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0009528 | 10 of 10 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0009528 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0009528 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0009528 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0009528 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0009528 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Stroma-facing envelope bilayer

identity: supported. Targets: GO:0009528.

Exact GO identity, three SL synonyms, plastid-membrane parent and envelope parthood agree. The IMS is a distinct enclosed region.

### Constituent lipid material

grounding: supported. Targets: GO:0009528.

The reviewed-label-only component describes collective inner bilayer material rather than grounding a chemical lipid to the whole-membrane GO identifier. The essentiality assertion is supported at the defining collective-bilayer level.

### Individual formation requirements

evidence: unknown. Targets: GO:0009528.

No source here tests the requirement of an individual lipid species or protein for formation of this boundary. Such molecular necessity remains unknown.

### Three descriptive topology edges

graph: supported. Targets: GO:0009528.

Parthood in the envelope, bounding stroma and delimiting IMS are supported. NONMECHANISTIC accurately describes the topology; no universal translocon, peptidoglycan or complex-plastid extra membrane is asserted.

### Current molecular-grounding TODO

completeness: supported. Targets: GO:0009528.

The open task accurately leaves a separate chemical constituent CURIE unresolved. Exact whole-membrane GO/SL identifiers do not fill that molecular slot.

### Species-bounded structural example

evidence: supported. Targets: GO:0009528.

Jin2022 primary abstract and indexed species keyword support the maintained Chlamydomonas reinhardtii envelope/IMS example at its stated scale. No full molecular model or strain measurement is certified.

### Green lineage and species identity

scope: supported. Targets: GO:0009528.

Verified taxonomy and the review text support primary plastids in the stated green lineage and the named species context. COMMON does not assert all isolates under all conditions.

### Entire maintained target reviewed

completeness: supported. Targets: GO:0009528.

All current evidence notes, histories, graph edges and discussions were assessed; no unrelated optional protein inventory, measurement or evolutionary model was invented.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/plastid_inner_membrane.yaml; Entire maintained target including history, taxonomy, evidence, graph and discussions | context_only | All maintained claims read at their current scope; historical curation is not independent evidence. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; Component type/role/essentiality, graph and evidence contracts | context_only | Collective bilayer material and whole membrane identity are distinguished; individual molecular formation necessity requires separate evidence. |
| neighbor-plastid_intermembrane_space | data/structures/membrane_organelle/plastid_intermembrane_space.yaml; Complete frozen neighboring target | context_only | Boundary and generic-class context only; this input is not new experimental evidence and has a separate review. |
| neighbor-plastid_membrane | data/structures/membrane_organelle/plastid_membrane.yaml; Complete frozen neighboring target | context_only | Boundary and generic-class context only; this input is not new experimental evidence and has a separate review. |
| root38-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009528,GO:0009529,GO:0009527,GO:0009526,GO:0009532,GO:0042170,GO:0009536,GO:0016020,GO:0055035,GO:0033113,GO:0160211; Complete eleven native entries including definitions, exact synonym scopes and all typed children | supports | Eleven active entries distinguish generic membrane, plastid membrane, envelope, inner/outer bilayers, IMS and stroma. GO0042170 has explicit is_a child placement for plastid thylakoid, cyanelle and apicoplast membranes; this is broader than its envelope-focused definition text. |
| root38-sources-tax33090 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/33090; Complete ENA33090 response | supports | Native taxonomy verifies Viridiplantae kingdom identity and Eukaryota lineage; it is not an occurrence census. |
| root38-sources-tax3055 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055; Complete ENA3055 response | supports | Native taxonomy verifies Chlamydomonas reinhardtii species3055 and green-algal lineage. No strain-specific assertion is inferred. |
| plastid-agent-doi-10.1098_rstb.2009.0103 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1098/rstb.2009.0103; Native title/authors/year/DOI/PMCID/publication types and complete abstract | supports | Unique MED20124341, DOI and PMCID2817223 match Keeling2010. This is a secondary evolutionary review. |
| plastid-agent-keeling2010-legacy-fresh | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2817223/; Genuine PMC2817223 body; complete sections s1,s3,s6,s9 including embedded figure captions. Other sections, figure pixels and underlying studies not independently audited. | supports | The review supports primary plastids in green algae/land plants, two bounding membranes, additional membranes in secondary plastids and retained nonphotosynthetic plastids. Historical evolutionary hypotheses and old universal mitochondrial statements are not adopted. |
| root38-sources-SL-0211 | https://rest.uniprot.org/locations/SL-0211.json; Complete native response including nested isA/partOf objects | supports | SL0211 maps to exact GO0009528, gives the three maintained synonyms and describes separation of stroma from IMS. Nested isA generic membrane and envelope context are distinguished. |
| root38-sources-SL-0212 | https://rest.uniprot.org/locations/SL-0212.json; Complete native response including nested partOf objects | supports | SL0212 maps to exact GO0009529, gives the maintained synonym and explicit envelope partOf relation. |
| plastid-agent-doi-10.1016_j.cell.2022.10.030 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.cell.2022.10.030; Complete native primary abstract, bibliographic identity, keywordList, meshHeadingList and fullTextUrlList; no article body retrieved | supports | Unique MED36413996 and exact Jin2022 DOI/title verified. The primary abstract reports a Chlamydomonas TOC-TIC structure bridging two envelope membranes with an IMS scaffold; indexed keywords explicitly name C.reinhardtii. This supports the bounded species example and membrane orientation without claiming a strain or new molecular necessity. |
| root38-sources-GO0009528-isa | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009528/ancestors?relations=is_a; Complete native one-term is_a ancestor response | supports | The exact inner-membrane is_a-only response includes generic plastid membrane GO0042170. |
| schema-result | just validate data/structures/membrane_organelle/plastid_inner_membrane.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/plastid_inner_membrane.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/plastid_inner_membrane.yaml --out /private/tmp/cellstructure-batch38-20261022-tpqg0c05/plastid_inner_membrane-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/plastid_inner_membrane.yaml --out /private/tmp/cellstructure-batch38-20261022-tpqg0c05/plastid_inner_membrane-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch38-20261022-tpqg0c05/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch38-20261022-tpqg0c05/plastid_inner_membrane-strict.tsv |
| native-plastid_inner_membrane-causal | /private/tmp/cellstructure-batch38-20261022-tpqg0c05/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/plastid_inner_membrane.yaml; Complete native protein-reference graph log | supports | <br>causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes<br> |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/plastid_inner_membrane.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 10 of 10 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Keeling2010 is a secondary review read in the declared sections; its historical hypotheses are not treated as current comprehensive phylogenetic consensus. No image pixels, supplementary data or raw experiments were reanalyzed.
- Occurrence values are qualitative and bounded by the stated taxa and source context; no strain census, universal protein complement, membrane stoichiometry or measured physical quantity is inferred. No verbatim snippet or image asset is maintained.
- Jin2022 is verified through native bibliographic metadata, complete primary abstract and species keyword. Publisher/author routes retained in the shared packet returned403; no full Methods, figure pixels, atomic model or strain-specific experiment was independently read.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User authorizes honest review bundles for all uncovered records, including zero-finding observations.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T032305Z-plastid-inner-membrane-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Plastid inner membrane scientific review
started_at: '2026-10-22T03:05:51Z'
finished_at: '2026-10-22T03:23:05Z'
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
summary: No concrete defect observed in the exact identity, source-bounded exemplar
  and descriptive topology/class scope of this plastid compartment.
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
  - path: data/structures/membrane_organelle/plastid_inner_membrane.yaml
    sha256: ceb12c6ee4451216ae406f17f68ea2d3730a6da302b38e8bb8fcabc532a6a4fa
    role: target
  - path: data/structures/membrane_organelle/plastid_intermembrane_space.yaml
    sha256: 2ef21406931fb90ec3aead7f57ee12a4376ad3d95276c7db3c2a7ab324c73c5d
    role: context
  - path: data/structures/membrane_organelle/plastid_membrane.yaml
    sha256: ae09183c12ecb85ac2135b3615b9a613985285039f5730126227fde982e55bef
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
- target_id: GO:0009528
  path: data/structures/membrane_organelle/plastid_inner_membrane.yaml
  label: plastid inner membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/plastid_inner_membrane.yaml
    role: maintained scientific record
scope:
  description: Entire single maintained target; two adjacent reviewed targets frozen
    as boundary context only.
  selection: Target 8 of batch38, the next uncovered record in strict path order at
    fresh origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0009528
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0009528
  command: just validate data/structures/membrane_organelle/plastid_inner_membrane.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0009528
  command: just validate-strict data/structures/membrane_organelle/plastid_inner_membrane.yaml
    --out /private/tmp/cellstructure-batch38-20261022-tpqg0c05/plastid_inner_membrane-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-plastid_inner_membrane-causal
  name: Native graph protein-reference check
  status: passed
  required: true
  target_ids:
  - GO:0009528
  command: /private/tmp/cellstructure-batch38-20261022-tpqg0c05/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/plastid_inner_membrane.yaml
  exit_code: 0
  summary: No named protein node requires an accession in this bounded topology graph.
  evidence_ids:
  - native-plastid_inner_membrane-causal
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0009528
  summary: No expression-module, regulator or transcriptional mechanism is claimed.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0009528
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - neighbor-plastid_intermembrane_space
  - neighbor-plastid_membrane
  - root38-sources-go
  - root38-sources-tax33090
  - root38-sources-tax3055
  - plastid-agent-doi-10.1098_rstb.2009.0103
  - plastid-agent-keeling2010-legacy-fresh
  - root38-sources-SL-0211
  - root38-sources-SL-0212
  - plastid-agent-doi-10.1016_j.cell.2022.10.030
  - root38-sources-GO0009528-isa
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0009528
  summary: 10 of 10 collected target identifiers returned OK. No residuals. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.
  evidence_ids:
  - target-curies
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0009528
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch38 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0009528
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch38 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0009528
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch38 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0009528
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch38 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0009528
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
    and current batch38 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/plastid_inner_membrane.yaml
  locator: Entire maintained target including history, taxonomy, evidence, graph and
    discussions
  accessed_at: '2026-10-22T03:12:58Z'
  support: context_only
  summary: All maintained claims read at their current scope; historical curation
    is not independent evidence.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Component type/role/essentiality, graph and evidence contracts
  accessed_at: '2026-10-22T03:12:58Z'
  support: context_only
  summary: Collective bilayer material and whole membrane identity are distinguished;
    individual molecular formation necessity requires separate evidence.
- evidence_id: neighbor-plastid_intermembrane_space
  kind: record_content
  reference: data/structures/membrane_organelle/plastid_intermembrane_space.yaml
  locator: Complete frozen neighboring target
  accessed_at: '2026-10-22T03:12:58Z'
  support: context_only
  summary: Boundary and generic-class context only; this input is not new experimental
    evidence and has a separate review.
- evidence_id: neighbor-plastid_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/plastid_membrane.yaml
  locator: Complete frozen neighboring target
  accessed_at: '2026-10-22T03:12:58Z'
  support: context_only
  summary: Boundary and generic-class context only; this input is not new experimental
    evidence and has a separate review.
- evidence_id: root38-sources-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009528,GO:0009529,GO:0009527,GO:0009526,GO:0009532,GO:0042170,GO:0009536,GO:0016020,GO:0055035,GO:0033113,GO:0160211
  locator: Complete eleven native entries including definitions, exact synonym scopes
    and all typed children
  accessed_at: '2026-10-22T03:10:07.199177Z'
  support: supports
  summary: Eleven active entries distinguish generic membrane, plastid membrane, envelope,
    inner/outer bilayers, IMS and stroma. GO0042170 has explicit is_a child placement
    for plastid thylakoid, cyanelle and apicoplast membranes; this is broader than
    its envelope-focused definition text.
  snapshot_sha256: 783947f5ec27dbe90af20be5c48ea3893f0146f8ad653fd6e585a9c3577c6ba0
- evidence_id: root38-sources-tax33090
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/33090
  locator: Complete ENA33090 response
  accessed_at: '2026-10-22T03:10:07.933079Z'
  support: supports
  summary: Native taxonomy verifies Viridiplantae kingdom identity and Eukaryota lineage;
    it is not an occurrence census.
  snapshot_sha256: 5edd98868e71b65ad827c23592102272c4e9e3ce6f29421e9263dcff0a3410f4
- evidence_id: root38-sources-tax3055
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055
  locator: Complete ENA3055 response
  accessed_at: '2026-10-22T03:10:07.936636Z'
  support: supports
  summary: Native taxonomy verifies Chlamydomonas reinhardtii species3055 and green-algal
    lineage. No strain-specific assertion is inferred.
  snapshot_sha256: e3861fe6706cefe2e079e15c0178a65e95efaad3890f548f25e721553eaa93a0
- evidence_id: plastid-agent-doi-10.1098_rstb.2009.0103
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1098/rstb.2009.0103
  locator: Native title/authors/year/DOI/PMCID/publication types and complete abstract
  accessed_at: '2026-10-21T10:41:48.128898Z'
  support: supports
  summary: Unique MED20124341, DOI and PMCID2817223 match Keeling2010. This is a secondary
    evolutionary review.
  snapshot_sha256: cb4b9f46ce9002adf2521e02ef9aa676bb65af752c0b025c4015b37a21d9aa0b
- evidence_id: plastid-agent-keeling2010-legacy-fresh
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2817223/
  locator: Genuine PMC2817223 body; complete sections s1,s3,s6,s9 including embedded
    figure captions. Other sections, figure pixels and underlying studies not independently
    audited.
  accessed_at: '2026-10-22T03:10:09.264490Z'
  support: supports
  summary: The review supports primary plastids in green algae/land plants, two bounding
    membranes, additional membranes in secondary plastids and retained nonphotosynthetic
    plastids. Historical evolutionary hypotheses and old universal mitochondrial statements
    are not adopted.
  snapshot_sha256: b00d7b5af35e8b00a2bee348bdb1b68c01c070514bf9adb1af7bd337ecae8394
- evidence_id: root38-sources-SL-0211
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0211.json
  locator: Complete native response including nested isA/partOf objects
  accessed_at: '2026-10-22T03:10:08.481652Z'
  support: supports
  summary: SL0211 maps to exact GO0009528, gives the three maintained synonyms and
    describes separation of stroma from IMS. Nested isA generic membrane and envelope
    context are distinguished.
  snapshot_sha256: a1d5aada6f9ece1571ec375df8c0ab1e2a3dbab0398a46de53ab9957199147d8
- evidence_id: root38-sources-SL-0212
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0212.json
  locator: Complete native response including nested partOf objects
  accessed_at: '2026-10-22T03:10:08.488763Z'
  support: supports
  summary: SL0212 maps to exact GO0009529, gives the maintained synonym and explicit
    envelope partOf relation.
  snapshot_sha256: e45d81d88e3d6f167d665d42f1721da6eb6a2c6e69821dee5c9d2740afb514aa
- evidence_id: plastid-agent-doi-10.1016_j.cell.2022.10.030
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.cell.2022.10.030
  locator: Complete native primary abstract, bibliographic identity, keywordList,
    meshHeadingList and fullTextUrlList; no article body retrieved
  accessed_at: '2026-10-21T10:41:48.146550Z'
  support: supports
  summary: Unique MED36413996 and exact Jin2022 DOI/title verified. The primary abstract
    reports a Chlamydomonas TOC-TIC structure bridging two envelope membranes with
    an IMS scaffold; indexed keywords explicitly name C.reinhardtii. This supports
    the bounded species example and membrane orientation without claiming a strain
    or new molecular necessity.
  snapshot_sha256: f4fc2108c3825f4a38c42eb7d109ac334b6e4d413ff1216d0d013925a2780061
- evidence_id: root38-sources-GO0009528-isa
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009528/ancestors?relations=is_a
  locator: Complete native one-term is_a ancestor response
  accessed_at: '2026-10-22T03:10:07.199635Z'
  support: supports
  summary: The exact inner-membrane is_a-only response includes generic plastid membrane
    GO0042170.
  snapshot_sha256: 7c67a7ded5c201a3d929a1091e0a36c2713bc11fd4ded92a7eea80713f3e61e5
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/plastid_inner_membrane.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:05:52Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/plastid_inner_membrane.yaml'
  snapshot_sha256: 33e2dc284e2af6ba487a259ebf95a408a7f2a8ed98f17a982ccc342551e9943c
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/plastid_inner_membrane.yaml
    --out /private/tmp/cellstructure-batch38-20261022-tpqg0c05/plastid_inner_membrane-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:05:53Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/plastid_inner_membrane.yaml\
    \ --out /private/tmp/cellstructure-batch38-20261022-tpqg0c05/plastid_inner_membrane-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch38-20261022-tpqg0c05/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch38-20261022-tpqg0c05/plastid_inner_membrane-strict.tsv"
  snapshot_sha256: e6684607cac292ecf9c70d6ef8565ebf1bad0b80e91f3ef4946c0141a82ff3d1
- evidence_id: native-plastid_inner_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batch38-20261022-tpqg0c05/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/plastid_inner_membrane.yaml
  locator: Complete native protein-reference graph log
  accessed_at: '2026-10-22T03:11:57.366093Z'
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
  locator: data/structures/membrane_organelle/plastid_inner_membrane.yaml; native
    collect() exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 10 of 10 collected target identifiers returned OK. No residuals. Native
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
  topic: Stroma-facing envelope bilayer
  outcome: supported
  target_ids:
  - GO:0009528
  summary: Exact GO identity, three SL synonyms, plastid-membrane parent and envelope
    parthood agree. The IMS is a distinct enclosed region.
  evidence_ids:
  - record
  - root38-sources-go
  - root38-sources-SL-0211
  - root38-sources-GO0009528-isa
- assessment_id: material
  area: grounding
  topic: Constituent lipid material
  outcome: supported
  target_ids:
  - GO:0009528
  summary: The reviewed-label-only component describes collective inner bilayer material
    rather than grounding a chemical lipid to the whole-membrane GO identifier. The
    essentiality assertion is supported at the defining collective-bilayer level.
  evidence_ids:
  - record
  - schema
  - root38-sources-go
  - root38-sources-SL-0211
- assessment_id: formation
  area: evidence
  topic: Individual formation requirements
  outcome: unknown
  target_ids:
  - GO:0009528
  summary: No source here tests the requirement of an individual lipid species or
    protein for formation of this boundary. Such molecular necessity remains unknown.
  evidence_ids:
  - record
  - schema
  - root38-sources-go
- assessment_id: graph
  area: graph
  topic: Three descriptive topology edges
  outcome: supported
  target_ids:
  - GO:0009528
  summary: Parthood in the envelope, bounding stroma and delimiting IMS are supported.
    NONMECHANISTIC accurately describes the topology; no universal translocon, peptidoglycan
    or complex-plastid extra membrane is asserted.
  evidence_ids:
  - record
  - root38-sources-go
  - root38-sources-SL-0211
  - root38-sources-SL-0212
- assessment_id: tasks
  area: completeness
  topic: Current molecular-grounding TODO
  outcome: supported
  target_ids:
  - GO:0009528
  summary: The open task accurately leaves a separate chemical constituent CURIE unresolved.
    Exact whole-membrane GO/SL identifiers do not fill that molecular slot.
  evidence_ids:
  - record
  - schema
  - root38-sources-go
  - root38-sources-SL-0211
- assessment_id: example
  area: evidence
  topic: Species-bounded structural example
  outcome: supported
  target_ids:
  - GO:0009528
  summary: Jin2022 primary abstract and indexed species keyword support the maintained
    Chlamydomonas reinhardtii envelope/IMS example at its stated scale. No full molecular
    model or strain measurement is certified.
  evidence_ids:
  - record
  - plastid-agent-doi-10.1016_j.cell.2022.10.030
  - root38-sources-tax3055
- assessment_id: taxonomy
  area: scope
  topic: Green lineage and species identity
  outcome: supported
  target_ids:
  - GO:0009528
  summary: Verified taxonomy and the review text support primary plastids in the stated
    green lineage and the named species context. COMMON does not assert all isolates
    under all conditions.
  evidence_ids:
  - record
  - root38-sources-tax33090
  - root38-sources-tax3055
  - plastid-agent-doi-10.1098_rstb.2009.0103
  - plastid-agent-keeling2010-legacy-fresh
- assessment_id: coverage
  area: completeness
  topic: Entire maintained target reviewed
  outcome: supported
  target_ids:
  - GO:0009528
  summary: All current evidence notes, histories, graph edges and discussions were
    assessed; no unrelated optional protein inventory, measurement or evolutionary
    model was invented.
  evidence_ids:
  - record
  - schema
  - root38-sources-go
findings: []
actions: []
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Keeling2010 is a secondary review read in the declared sections; its historical
  hypotheses are not treated as current comprehensive phylogenetic consensus. No image
  pixels, supplementary data or raw experiments were reanalyzed.
- Occurrence values are qualitative and bounded by the stated taxa and source context;
  no strain census, universal protein complement, membrane stoichiometry or measured
  physical quantity is inferred. No verbatim snippet or image asset is maintained.
- Jin2022 is verified through native bibliographic metadata, complete primary abstract
  and species keyword. Publisher/author routes retained in the shared packet returned403;
  no full Methods, figure pixels, atomic model or strain-specific experiment was independently
  read.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User authorizes honest review bundles for all uncovered records, including zero-finding
  observations.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
