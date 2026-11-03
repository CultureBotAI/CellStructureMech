# Plastid outer membrane scientific review

- Review: 20261022T032956Z-plastid-outer-membrane-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T03:13:54Z
- Finished UTC: 2026-10-22T03:29:56Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

No concrete defect observed in the maintained identity, bounded evidence and descriptive topology at the declared source-reading scope.

## Scope And Provenance

Entire single maintained target; two adjacent reviewed targets frozen as boundary context only.

Selection: Target 1 of batch39, the next uncovered record in strict path order at fresh origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0009527 | data/structures/membrane_organelle/plastid_outer_membrane.yaml | maintained | plastid outer membrane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0009527 | Focused validator passed. |
| Focused native strict | passed | True | GO:0009527 | Focused validator passed. |
| Native graph protein-reference check | passed | True | GO:0009527 | No named protein node needs accession validation in this topology graph. |
| Expression-module applicability | not_applicable | False | GO:0009527 | No expression-module or transcriptional-regulatory claim is maintained. |
| Claim-level scientific review | passed | True | GO:0009527 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0009527 | 10 of 10 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0009527 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0009527 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0009527 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0009527 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0009527 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Green-lineage plastid compartments

scope: supported. Targets: GO:0009527.

The review and native taxonomy support the stated primary-plastid green lineage context without asserting identical machinery in every plastid.

### Cytoplasm-facing envelope bilayer

identity: supported. Targets: GO:0009527.

Exact GO identity, native SL synonyms and ancestry support the maintained identity and envelope parthood. Cytoplasm orientation and IMS boundary are consistent.

### Collective outer bilayer material

grounding: supported. Targets: GO:0009527.

The reviewed-label-only LIPID row refers to constituent bilayer material; it is not grounded to the whole membrane GO identity. ESSENTIAL is defensible for the defining collective bilayer.

### Individual molecular formation requirements

evidence: unknown. Targets: GO:0009527.

No individual lipid or protein formation requirement is established by these definitions or the abstract; such necessity remains unknown.

### Three descriptive topology edges

graph: supported. Targets: GO:0009527.

Envelope parthood, cytoplasm-facing orientation and IMS delimitation are directly consistent with GO/SL. NONMECHANISTIC correctly bounds this topology.

### Bounded Chlamydomonas envelope example

evidence: supported. Targets: GO:0009527.

The native Jin abstract and species keyword support the outer-envelope example without certifying a strain, full molecular model or universal translocon.

### Open constituent-grounding task

completeness: supported. Targets: GO:0009527.

The molecular grounding TODO remains accurate. Whole membrane GO/SL terms do not fill the separate constituent slot.

### Entire maintained target reviewed

completeness: supported. Targets: GO:0009527.

All current evidence notes, history, graph relationships and discussions were assessed within the explicit source scopes.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/plastid_outer_membrane.yaml; Entire maintained target including history, taxonomy, evidence, graph and discussions | context_only | All maintained claims read at their current scope; historical curation is not independent evidence. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; Component type/role/essentiality, graph and evidence contracts | context_only | Collective bilayer material is distinguished from whole membrane identity and from individual molecular formation necessity. |
| neighbor-plastid_stroma | data/structures/membrane_organelle/plastid_stroma.yaml; Complete frozen neighboring target | context_only | Boundary context only; a separately reviewed input, not experimental evidence. |
| neighbor-pyrenoid_tubule | data/structures/membrane_organelle/pyrenoid_tubule.yaml; Complete frozen neighboring target | context_only | Boundary context only; a separately reviewed input, not experimental evidence. |
| root39-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009527,GO:0009528,GO:0009529,GO:0009526,GO:0009532,GO:0042170,GO:0009536,GO:0005737,GO:0160223,GO:0016020,GO:1990732,GO:0042651; Complete twelve entries including definitions, synonyms and typed children | supports | Twelve active native entries distinguish plastid outer membrane, stroma, envelope, IMS, cytoplasm, pyrenoid, tubule and generic thylakoid membrane. Typed children distinguish parthood from is-a. |
| root39-sources-tax3055 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055; Complete native ENA3055 response | supports | Native response verifies Chlamydomonas reinhardtii species3055 and green-algal lineage. |
| root39-sources-tax33090 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/33090; Complete ENA33090 response | supports | Native taxonomy verifies Viridiplantae kingdom and eukaryotic lineage. |
| root39-shared-doi-10.1098_rstb.2009.0103 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1098/rstb.2009.0103; Complete native bibliographic identity and abstract | supports | Unique MED20124341, DOI, PMCID2817223 and review identity match Keeling2010. |
| root39-shared-keeling2010-legacy-fresh | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2817223/; Genuine PMC2817223 full sections s1,s3,s6,s9, including embedded caption text; no figure pixels or underlying studies audited. | supports | The evolutionary review distinguishes primary green plastids, two bounding membranes, secondary plastids and retained nonphotosynthetic plastids. Historical evolutionary hypotheses are not treated as comprehensive current consensus. |
| root39-sources-SL-0214 | https://rest.uniprot.org/locations/SL-0214.json; Complete response including nested isA and partOf objects | supports | Exact GO0009527 mapping, three synonyms, cytoplasm-facing orientation and nested plastid membrane/envelope context verified. |
| root39-sources-GO0009527-isa | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009527/ancestors?relations=is_a; Complete native is_a-only response | supports | Native is-a-only ancestry contains generic plastid membrane GO0042170 and membrane GO0016020. |
| root39-shared-doi-10.1016_j.cell.2022.10.030 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.cell.2022.10.030; Bibliographic identity, complete primary abstract, species keyword, meshHeadingList and fullTextUrlList | supports | Unique MED36413996 matches Jin2022. Complete primary abstract describes a Chlamydomonas TOC-TIC complex bridging two envelope membranes; indexed keyword names C.reinhardtii. |
| schema-result | just validate data/structures/membrane_organelle/plastid_outer_membrane.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/plastid_outer_membrane.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/plastid_outer_membrane.yaml --out /private/tmp/cellstructure-batch39-20261022-9ejlvnby/plastid_outer_membrane-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/plastid_outer_membrane.yaml --out /private/tmp/cellstructure-batch39-20261022-9ejlvnby/plastid_outer_membrane-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch39-20261022-9ejlvnby/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch39-20261022-9ejlvnby/plastid_outer_membrane-strict.tsv |
| native-plastid_outer_membrane-causal | /private/tmp/cellstructure-batch39-20261022-9ejlvnby/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/plastid_outer_membrane.yaml; Complete native graph protein-reference log | supports | <br>causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes<br> |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/plastid_outer_membrane.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 10 of 10 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Taxonomic presence values are qualitative at the stated scope, not measured occurrence frequencies. No universal protein inventory, strain census or molecular stoichiometry is inferred.
- No figure pixels, supplementary datasets or raw experimental measurements were independently reanalyzed. No verbatim snippet or image asset is maintained.
- Keeling2010 is secondary evidence at the declared section scope; historical evolutionary hypotheses and old universal mitochondrial statements are not adopted.
- Jin2022 is read as native metadata, complete primary abstract and species keyword only. Both copied publisher/author access failures remain403; no full body, Methods, atomic model or image pixels are claimed.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The user authorizes honest review bundles for all uncovered records, including zero-finding observations.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T032956Z-plastid-outer-membrane-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Plastid outer membrane scientific review
started_at: '2026-10-22T03:13:54Z'
finished_at: '2026-10-22T03:29:56Z'
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
summary: No concrete defect observed in the maintained identity, bounded evidence
  and descriptive topology at the declared source-reading scope.
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
  - path: data/structures/membrane_organelle/plastid_outer_membrane.yaml
    sha256: 59bd8548931d27f711233f542b5f927c0e7b0a68dd611eabb4777ee08003deaa
    role: target
  - path: data/structures/membrane_organelle/plastid_stroma.yaml
    sha256: 86d19307cbe21273498f0d7d6741e61f5ebf002cf78418c34b922d9d4963503b
    role: context
  - path: data/structures/membrane_organelle/pyrenoid_tubule.yaml
    sha256: dd5c61f94612f6c30f259f029b7f4bc4daa8a7d4c0fa8111f6eb0715f78483d7
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
- target_id: GO:0009527
  path: data/structures/membrane_organelle/plastid_outer_membrane.yaml
  label: plastid outer membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/plastid_outer_membrane.yaml
    role: maintained scientific record
scope:
  description: Entire single maintained target; two adjacent reviewed targets frozen
    as boundary context only.
  selection: Target 1 of batch39, the next uncovered record in strict path order at
    fresh origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0009527
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0009527
  command: just validate data/structures/membrane_organelle/plastid_outer_membrane.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0009527
  command: just validate-strict data/structures/membrane_organelle/plastid_outer_membrane.yaml
    --out /private/tmp/cellstructure-batch39-20261022-9ejlvnby/plastid_outer_membrane-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-plastid_outer_membrane-causal
  name: Native graph protein-reference check
  status: passed
  required: true
  target_ids:
  - GO:0009527
  command: /private/tmp/cellstructure-batch39-20261022-9ejlvnby/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/plastid_outer_membrane.yaml
  exit_code: 0
  summary: No named protein node needs accession validation in this topology graph.
  evidence_ids:
  - native-plastid_outer_membrane-causal
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0009527
  summary: No expression-module or transcriptional-regulatory claim is maintained.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0009527
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - neighbor-plastid_stroma
  - neighbor-pyrenoid_tubule
  - root39-sources-go
  - root39-sources-tax3055
  - root39-sources-tax33090
  - root39-shared-doi-10.1098_rstb.2009.0103
  - root39-shared-keeling2010-legacy-fresh
  - root39-sources-SL-0214
  - root39-sources-GO0009527-isa
  - root39-shared-doi-10.1016_j.cell.2022.10.030
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0009527
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
  - GO:0009527
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
  - GO:0009527
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
  - GO:0009527
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
  - GO:0009527
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
  - GO:0009527
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
  reference: data/structures/membrane_organelle/plastid_outer_membrane.yaml
  locator: Entire maintained target including history, taxonomy, evidence, graph and
    discussions
  accessed_at: '2026-10-22T03:21:03Z'
  support: context_only
  summary: All maintained claims read at their current scope; historical curation
    is not independent evidence.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Component type/role/essentiality, graph and evidence contracts
  accessed_at: '2026-10-22T03:21:03Z'
  support: context_only
  summary: Collective bilayer material is distinguished from whole membrane identity
    and from individual molecular formation necessity.
- evidence_id: neighbor-plastid_stroma
  kind: record_content
  reference: data/structures/membrane_organelle/plastid_stroma.yaml
  locator: Complete frozen neighboring target
  accessed_at: '2026-10-22T03:21:03Z'
  support: context_only
  summary: Boundary context only; a separately reviewed input, not experimental evidence.
- evidence_id: neighbor-pyrenoid_tubule
  kind: record_content
  reference: data/structures/membrane_organelle/pyrenoid_tubule.yaml
  locator: Complete frozen neighboring target
  accessed_at: '2026-10-22T03:21:03Z'
  support: context_only
  summary: Boundary context only; a separately reviewed input, not experimental evidence.
- evidence_id: root39-sources-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009527,GO:0009528,GO:0009529,GO:0009526,GO:0009532,GO:0042170,GO:0009536,GO:0005737,GO:0160223,GO:0016020,GO:1990732,GO:0042651
  locator: Complete twelve entries including definitions, synonyms and typed children
  accessed_at: '2026-10-22T03:14:50.738635Z'
  support: supports
  summary: Twelve active native entries distinguish plastid outer membrane, stroma,
    envelope, IMS, cytoplasm, pyrenoid, tubule and generic thylakoid membrane. Typed
    children distinguish parthood from is-a.
  snapshot_sha256: 522624e56dc56e29f2adc22adaf51fc1ac86b8502f02868d67ab523f72f8cfae
- evidence_id: root39-sources-tax3055
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055
  locator: Complete native ENA3055 response
  accessed_at: '2026-10-22T03:14:50.739440Z'
  support: supports
  summary: Native response verifies Chlamydomonas reinhardtii species3055 and green-algal
    lineage.
  snapshot_sha256: e3861fe6706cefe2e079e15c0178a65e95efaad3890f548f25e721553eaa93a0
- evidence_id: root39-sources-tax33090
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/33090
  locator: Complete ENA33090 response
  accessed_at: '2026-10-22T03:14:50.739369Z'
  support: supports
  summary: Native taxonomy verifies Viridiplantae kingdom and eukaryotic lineage.
  snapshot_sha256: b1394e36c6896d7ec64cdb301a239f2bc49bc435a22cc21fdba8fdc6217e2d11
- evidence_id: root39-shared-doi-10.1098_rstb.2009.0103
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1098/rstb.2009.0103
  locator: Complete native bibliographic identity and abstract
  accessed_at: '2026-10-21T10:41:48.128898Z'
  support: supports
  summary: Unique MED20124341, DOI, PMCID2817223 and review identity match Keeling2010.
  snapshot_sha256: cb4b9f46ce9002adf2521e02ef9aa676bb65af752c0b025c4015b37a21d9aa0b
- evidence_id: root39-shared-keeling2010-legacy-fresh
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2817223/
  locator: Genuine PMC2817223 full sections s1,s3,s6,s9, including embedded caption
    text; no figure pixels or underlying studies audited.
  accessed_at: '2026-10-22T03:10:09.264490Z'
  support: supports
  summary: The evolutionary review distinguishes primary green plastids, two bounding
    membranes, secondary plastids and retained nonphotosynthetic plastids. Historical
    evolutionary hypotheses are not treated as comprehensive current consensus.
  snapshot_sha256: b00d7b5af35e8b00a2bee348bdb1b68c01c070514bf9adb1af7bd337ecae8394
- evidence_id: root39-sources-SL-0214
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0214.json
  locator: Complete response including nested isA and partOf objects
  accessed_at: '2026-10-22T03:14:51.497809Z'
  support: supports
  summary: Exact GO0009527 mapping, three synonyms, cytoplasm-facing orientation and
    nested plastid membrane/envelope context verified.
  snapshot_sha256: c849d1946fe23f77351fae5e9e4bcf0515e14578d37497cb0d320bc7ffb0dd93
- evidence_id: root39-sources-GO0009527-isa
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009527/ancestors?relations=is_a
  locator: Complete native is_a-only response
  accessed_at: '2026-10-22T03:14:50.739047Z'
  support: supports
  summary: Native is-a-only ancestry contains generic plastid membrane GO0042170 and
    membrane GO0016020.
  snapshot_sha256: 973849fad45f274e222f032a2d4b55248c515ddaad9e1233a3ef6eb7640b5342
- evidence_id: root39-shared-doi-10.1016_j.cell.2022.10.030
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.cell.2022.10.030
  locator: Bibliographic identity, complete primary abstract, species keyword, meshHeadingList
    and fullTextUrlList
  accessed_at: '2026-10-21T10:41:48.146550Z'
  support: supports
  summary: Unique MED36413996 matches Jin2022. Complete primary abstract describes
    a Chlamydomonas TOC-TIC complex bridging two envelope membranes; indexed keyword
    names C.reinhardtii.
  snapshot_sha256: f4fc2108c3825f4a38c42eb7d109ac334b6e4d413ff1216d0d013925a2780061
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/plastid_outer_membrane.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:13:56Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/plastid_outer_membrane.yaml'
  snapshot_sha256: c4311a43f9554d9177d5ee0225b819c5951d3bd2d54544145fdc39ea63b8922c
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/plastid_outer_membrane.yaml
    --out /private/tmp/cellstructure-batch39-20261022-9ejlvnby/plastid_outer_membrane-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:13:57Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/plastid_outer_membrane.yaml\
    \ --out /private/tmp/cellstructure-batch39-20261022-9ejlvnby/plastid_outer_membrane-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch39-20261022-9ejlvnby/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch39-20261022-9ejlvnby/plastid_outer_membrane-strict.tsv"
  snapshot_sha256: dc9f874557846a3892acfd9cad6875f051220f4928eac28f9f41b9552380849a
- evidence_id: native-plastid_outer_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batch39-20261022-9ejlvnby/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/plastid_outer_membrane.yaml
  locator: Complete native graph protein-reference log
  accessed_at: '2026-10-22T03:20:01.238563Z'
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
  locator: data/structures/membrane_organelle/plastid_outer_membrane.yaml; native
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
- assessment_id: taxonomy
  area: scope
  topic: Green-lineage plastid compartments
  outcome: supported
  target_ids:
  - GO:0009527
  summary: The review and native taxonomy support the stated primary-plastid green
    lineage context without asserting identical machinery in every plastid.
  evidence_ids:
  - record
  - root39-sources-tax33090
  - root39-sources-tax3055
  - root39-shared-doi-10.1098_rstb.2009.0103
  - root39-shared-keeling2010-legacy-fresh
- assessment_id: identity
  area: identity
  topic: Cytoplasm-facing envelope bilayer
  outcome: supported
  target_ids:
  - GO:0009527
  summary: Exact GO identity, native SL synonyms and ancestry support the maintained
    identity and envelope parthood. Cytoplasm orientation and IMS boundary are consistent.
  evidence_ids:
  - record
  - root39-sources-go
  - root39-sources-SL-0214
  - root39-sources-GO0009527-isa
- assessment_id: material
  area: grounding
  topic: Collective outer bilayer material
  outcome: supported
  target_ids:
  - GO:0009527
  summary: The reviewed-label-only LIPID row refers to constituent bilayer material;
    it is not grounded to the whole membrane GO identity. ESSENTIAL is defensible
    for the defining collective bilayer.
  evidence_ids:
  - record
  - schema
  - root39-sources-go
  - root39-sources-SL-0214
- assessment_id: formation
  area: evidence
  topic: Individual molecular formation requirements
  outcome: unknown
  target_ids:
  - GO:0009527
  summary: No individual lipid or protein formation requirement is established by
    these definitions or the abstract; such necessity remains unknown.
  evidence_ids:
  - record
  - schema
  - root39-sources-go
  - root39-shared-doi-10.1016_j.cell.2022.10.030
- assessment_id: graph
  area: graph
  topic: Three descriptive topology edges
  outcome: supported
  target_ids:
  - GO:0009527
  summary: Envelope parthood, cytoplasm-facing orientation and IMS delimitation are
    directly consistent with GO/SL. NONMECHANISTIC correctly bounds this topology.
  evidence_ids:
  - record
  - root39-sources-go
  - root39-sources-SL-0214
- assessment_id: example
  area: evidence
  topic: Bounded Chlamydomonas envelope example
  outcome: supported
  target_ids:
  - GO:0009527
  summary: The native Jin abstract and species keyword support the outer-envelope
    example without certifying a strain, full molecular model or universal translocon.
  evidence_ids:
  - record
  - root39-sources-tax3055
  - root39-shared-doi-10.1016_j.cell.2022.10.030
- assessment_id: tasks
  area: completeness
  topic: Open constituent-grounding task
  outcome: supported
  target_ids:
  - GO:0009527
  summary: The molecular grounding TODO remains accurate. Whole membrane GO/SL terms
    do not fill the separate constituent slot.
  evidence_ids:
  - record
  - schema
  - root39-sources-go
  - root39-sources-SL-0214
- assessment_id: coverage
  area: completeness
  topic: Entire maintained target reviewed
  outcome: supported
  target_ids:
  - GO:0009527
  summary: All current evidence notes, history, graph relationships and discussions
    were assessed within the explicit source scopes.
  evidence_ids:
  - record
  - schema
  - root39-sources-go
findings: []
actions: []
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Taxonomic presence values are qualitative at the stated scope, not measured occurrence
  frequencies. No universal protein inventory, strain census or molecular stoichiometry
  is inferred.
- No figure pixels, supplementary datasets or raw experimental measurements were independently
  reanalyzed. No verbatim snippet or image asset is maintained.
- Keeling2010 is secondary evidence at the declared section scope; historical evolutionary
  hypotheses and old universal mitochondrial statements are not adopted.
- Jin2022 is read as native metadata, complete primary abstract and species keyword
  only. Both copied publisher/author access failures remain403; no full body, Methods,
  atomic model or image pixels are claimed.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The user authorizes honest review bundles for all uncovered records, including zero-finding
  observations.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
