# Cell surface furrow scientific review

- Review: 20261022T045413Z-cell-surface-furrow-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T04:36:54Z
- Finished UTC: 2026-10-22T04:54:13Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact furrow identity and surface parthood are supported. One major finding concerns unsupported defining biological scope; one minor concerns the parthood-only graph being labelled mechanistic.

## Scope And Provenance

Exactly one entire maintained record; native identities, all claim-bearing fields, source-specific evidence, hierarchy, topology and boundary decisions reviewed. Neighbor records, where frozen, were read only for identity/definition and component-boundary context.

Selection: Target 3 of batch46 in strict uncovered path order at unchanged origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0097610 | data/structures/other/cell_surface_furrow.yaml | maintained | cell surface furrow |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0097610 | Focused validator passed. |
| Focused native strict | passed | True | GO:0097610 | Focused validator passed. |
| Native graph coverage | passed | True | GO:0097610 | No GENE_OR_PROTEIN nodes; native coverage passed. Scientific topology and mechanism claims were assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0097610 | No transcriptomic or expression-module claim is made; localized protein names in literature context are not an iModulon claim. |
| Claim-level scientific review | passed | True | GO:0097610 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0097610 | 6 of 7 collected target identifiers returned OK. PMID:7002229: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0097610 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0097610 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0097610 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0097610 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0097610 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact generic furrow class and topology

identity: supported. Targets: GO:0097610.

Active GO0097610 supports the first two definition sentences, broad/related synonyms, anatomical-structure is-a parent and cell-surface parthood. Cingulum and sulcus remain distinct child classes.

### Unsubstantiated cross-lineage structural and functional extension

evidence: concern. Targets: GO:0097610.

The added definition asserts persistent grooves across excavates, cryptophytes and euglenids, a common alveolar/epiplastid/microtubular support, and hydrodynamic propulsion/prey capture. The cited GO definition states none of those extensions. Taylor is explicitly bibliographic-only in the record and its inspected abstract does not establish this multi-lineage claim. This is material defining scope inflation, not merely a missing citation punctuation issue.

### Bounded Dinophyceae row

scope: supported. Targets: GO:0097610.

ENA resolves Dinophyceae. GO defines cingulum in dinoflagellates and generic furrows as occurring in some dinoflagellates, consistent with the limited VARIABLE row. That row does not justify the broader defining extensions and no unlisted taxon occurrence is independently established.

### Taylor identity and access

evidence: supported. Targets: GO:0097610.

PMID7002229 and the DOI resolve to Taylor1980 On dinoflagellate evolution. Its review abstract establishes bibliographic context only here. The historical no-body note remains honest; current publisher403 likewise supplies no mechanism or exhaustive cross-lineage evidence.

### Only parthood is represented

graph: concern. Targets: GO:0097610.

The sole edge states supported native cell-surface parthood. MECHANISTIC and the assembly/mechanism title overstate this topology. Its PMID metadata-only citation is also weaker than the directly inspected GO relation; retain topology with its appropriate authority.

### Regional component boundary

grounding: supported. Targets: GO:0097610.

No universal molecular constituents can be inferred merely from the generic furrow term. The empty optional inventory is not separately defective; unsupported defining support-material assertions are covered by F1.

### Full target, two bounded corrections

completeness: supported. Targets: GO:0097610.

The entire target, history, three synonyms, distribution, four evidence entries and single graph edge were read. The exact class and parthood survive both proposed corrections.

## Findings

### F1: Constrain the expanded definition to supported biological scope

major / open / confirmed; issue key: cell-surface-furrow-expanded-definition.

The second definition paragraph goes beyond GO0097610 by asserting additional lineages, persistent cortical morphology, shared supporting structures and hydrodynamic functions. Those material claims are not supported by the nearest cited authority or the declared bibliographic-only Taylor source. This finding does not assert that every added example is biologically false.

### F2: Describe the single-edge graph as topology

minor / open / confirmed; issue key: cell-surface-furrow-parthood-graph-scope.

The graph is labelled MECHANISTIC/assembly mechanism although it contains only furrow is part of cell surface. No causal formation transition is represented; the current PMID edge note explicitly supplies metadata only.

## Recommended Actions And Acceptance Checks

### A1

Retain the exact generic GO definition, or support each added lineage, supporting structure and function with inspected claim-specific sources and explicit scope. Do not preserve a universal synthesis merely by attaching one dinoflagellate review.

- Preserve GO0097610 identity, current supported synonyms and hierarchy.
- For every retained extension, identify the source passage and its organism/anatomical/function boundary.
- Pass applicable native schema, strict, reference and graph checks.

### A2

Mark the graph NONMECHANISTIC, give it a topology title and scope note, and ground the preserved parthood edge in the verified GO relation. Add mechanistic detail only if separately sourced.

- Preserve the correct furrow-to-surface relation.
- Ensure title, scope label and description describe the actual edge content.
- Do not claim Taylor full-body support from bibliographic metadata.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/cell_surface_furrow.yaml; Entire maintained target including history, all evidence, graph and discussions | context_only | The complete target was read; history documents provenance and does not independently validate current science. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; Structure kinds, hierarchy, material constitution versus formation necessity, COMMON/VARIABLE and graph scope | context_only | Regional topology and causal mechanism are distinct; COMMON means present in most members with losses the exception, and VARIABLE denotes presence in some members. Empty optional molecular inventories are not automatically errors. |
| curation | docs/CURATION.md; Identity, claim-specific evidence and component granularity | context_only | A source must support the particular biological claim; regional records need not duplicate every molecular constituent of localized substructures. |
| cortex46-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005938,GO:0005737,GO:0005886,GO:0030479,GO:0005940,GO:0097610,GO:0110165,GO:0009986,GO:0097611,GO:0097612,GO:0005933,GO:0033101,GO:0005935,GO:0005934; Complete requested GO0005938/0005737/0005886/0030479/0005940/0097610/0110165/0009986/0097611/0097612/0005933/0033101/0005935/0005934 responses; only maintained relevant child links assessed | supports | Current active GO identities, exact definitions/synonyms and relevant typed parent/parthood links were inspected for this target and its named structures. |
| cortex46-agent-tax2864 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2864; Complete native taxonomy response including rank/lineage/names | supports | ENA confirms Dinophyceae at class rank. |
| cortex46-agent-taylor1980-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1016/0303-2647%2880%2990006-4%22; Native id/title/authors/year/DOI and complete abstract | supports | Exact native MED7002229 identity: On dinoflagellate evolution. DOI 10.1016/0303-2647(80)90006-4. Complete abstract read; any body inspection is separately specified. |
| cortex46-agent-taylor1980-publisher | https://www.sciencedirect.com/science/article/pii/0303264780900064; Retained actual access response; not scientific body evidence | context_only | The checked ScienceDirect publisher route returned HTTP403. Native metadata and complete abstract were read; no Taylor article-body claim is certified. |
| schema-result | just validate data/structures/other/cell_surface_furrow.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/cell_surface_furrow.yaml |
| strict-result | just validate-strict data/structures/other/cell_surface_furrow.yaml --out /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/cell_surface_furrow-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/cell_surface_furrow.yaml --out /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/cell_surface_furrow-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch46-20261022-nrgmxxyw/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/cell_surface_furrow-strict.tsv |
| native-graph | /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/repo/.venv/bin/python scripts/uniprot_genes.py --causal-graphs --record data/structures/other/cell_surface_furrow.yaml; Complete native read-only graph coverage report | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/other/cell_surface_furrow.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 6 of 7 collected target identifiers returned OK. PMID:7002229: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Five completed same-base batch26 global gates remain staged for guarded parent integration; no corpus-level result is claimed through this unsaved draft.
- No image pixels, raw experiments, supplementary files or underlying studies cited by the review were independently reanalyzed. Exact primary and authority reading scopes are declared in evidence.
- Taylor1980 is metadata/complete-abstract only; the fresh publisher route returned403. No broad literature absence or claim that every added lineage lacks furrows is asserted.
- The native sulcus child was inspected for boundary context only; its separate definition references were not independently audited because the target does not rely on them.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User goal explicitly authorizes a review for every uncovered target, including honest clean records.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T045413Z-cell-surface-furrow-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Cell surface furrow scientific review
started_at: '2026-10-22T04:36:54Z'
finished_at: '2026-10-22T04:54:13Z'
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
summary: Exact furrow identity and surface parthood are supported. One major finding
  concerns unsupported defining biological scope; one minor concerns the parthood-only
  graph being labelled mechanistic.
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
  - path: data/structures/other/cell_surface_furrow.yaml
    sha256: 6b0093967543186f49c224cfbb592d8131bc723930752e1b17a5536ebc11219d
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
- target_id: GO:0097610
  path: data/structures/other/cell_surface_furrow.yaml
  label: cell surface furrow
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/cell_surface_furrow.yaml
    role: maintained scientific record
scope:
  description: Exactly one entire maintained record; native identities, all claim-bearing
    fields, source-specific evidence, hierarchy, topology and boundary decisions reviewed.
    Neighbor records, where frozen, were read only for identity/definition and component-boundary
    context.
  selection: Target 3 of batch46 in strict uncovered path order at unchanged origin/main
    f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0097610
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0097610
  command: just validate data/structures/other/cell_surface_furrow.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0097610
  command: just validate-strict data/structures/other/cell_surface_furrow.yaml --out
    /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/cell_surface_furrow-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-graph
  name: Native graph coverage
  status: passed
  required: true
  target_ids:
  - GO:0097610
  command: /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/repo/.venv/bin/python
    scripts/uniprot_genes.py --causal-graphs --record data/structures/other/cell_surface_furrow.yaml
  exit_code: 0
  summary: No GENE_OR_PROTEIN nodes; native coverage passed. Scientific topology and
    mechanism claims were assessed separately.
  evidence_ids:
  - native-graph
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0097610
  summary: No transcriptomic or expression-module claim is made; localized protein
    names in literature context are not an iModulon claim.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0097610
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - cortex46-agent-go
  - cortex46-agent-tax2864
  - cortex46-agent-taylor1980-meta
  - cortex46-agent-taylor1980-publisher
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0097610
  summary: '6 of 7 collected target identifiers returned OK. PMID:7002229: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.'
  evidence_ids:
  - target-curies
  - cortex46-agent-taylor1980-meta
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0097610
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch46 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0097610
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch46 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0097610
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch46 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0097610
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch46 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0097610
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
    and current batch46 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/cell_surface_furrow.yaml
  locator: Entire maintained target including history, all evidence, graph and discussions
  accessed_at: '2026-10-22T04:42:22Z'
  support: context_only
  summary: The complete target was read; history documents provenance and does not
    independently validate current science.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Structure kinds, hierarchy, material constitution versus formation necessity,
    COMMON/VARIABLE and graph scope
  accessed_at: '2026-10-22T04:42:22Z'
  support: context_only
  summary: Regional topology and causal mechanism are distinct; COMMON means present
    in most members with losses the exception, and VARIABLE denotes presence in some
    members. Empty optional molecular inventories are not automatically errors.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Identity, claim-specific evidence and component granularity
  accessed_at: '2026-10-22T04:42:22Z'
  support: context_only
  summary: A source must support the particular biological claim; regional records
    need not duplicate every molecular constituent of localized substructures.
- evidence_id: cortex46-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005938,GO:0005737,GO:0005886,GO:0030479,GO:0005940,GO:0097610,GO:0110165,GO:0009986,GO:0097611,GO:0097612,GO:0005933,GO:0033101,GO:0005935,GO:0005934
  locator: Complete requested GO0005938/0005737/0005886/0030479/0005940/0097610/0110165/0009986/0097611/0097612/0005933/0033101/0005935/0005934
    responses; only maintained relevant child links assessed
  accessed_at: '2026-10-22T04:38:31.207999Z'
  support: supports
  summary: Current active GO identities, exact definitions/synonyms and relevant typed
    parent/parthood links were inspected for this target and its named structures.
  snapshot_sha256: 04958c90f60f753443ae327ebf353b3ab6ac7a8bfaf5cea58634921b40b55b5a
- evidence_id: cortex46-agent-tax2864
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2864
  locator: Complete native taxonomy response including rank/lineage/names
  accessed_at: '2026-10-22T04:38:31.953633Z'
  support: supports
  summary: ENA confirms Dinophyceae at class rank.
  snapshot_sha256: da7d6dfa6d6784e4eb22bc3f3e05878f3aae5a281a4996ee25a2012d580f27d4
- evidence_id: cortex46-agent-taylor1980-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1016/0303-2647%2880%2990006-4%22
  locator: Native id/title/authors/year/DOI and complete abstract
  accessed_at: '2026-10-22T04:38:32.559443Z'
  support: supports
  summary: 'Exact native MED7002229 identity: On dinoflagellate evolution. DOI 10.1016/0303-2647(80)90006-4.
    Complete abstract read; any body inspection is separately specified.'
  snapshot_sha256: 80a9eb9f4a264f3da7791104aab23f1bd5206723a493b5e0115d9674c6a265ca
- evidence_id: cortex46-agent-taylor1980-publisher
  kind: database
  reference: https://www.sciencedirect.com/science/article/pii/0303264780900064
  locator: Retained actual access response; not scientific body evidence
  accessed_at: '2026-10-22T04:40:20.155787Z'
  support: context_only
  summary: The checked ScienceDirect publisher route returned HTTP403. Native metadata
    and complete abstract were read; no Taylor article-body claim is certified.
  snapshot_sha256: 0c9e2eed6ea145a6e08de80886870445bea0cec547d957ec5e5317d95ae8726c
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/cell_surface_furrow.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:36:55Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/cell_surface_furrow.yaml'
  snapshot_sha256: 8d5509c25b135f7501f089748c2e53e0d86a58e92b443d408cce924e0862b1d0
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/cell_surface_furrow.yaml --out
    /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/cell_surface_furrow-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:36:56Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/cell_surface_furrow.yaml\
    \ --out /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/cell_surface_furrow-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch46-20261022-nrgmxxyw/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/cell_surface_furrow-strict.tsv"
  snapshot_sha256: 8f512689a39c751bc738f6e893ac186723120578eaa825660e74d5c3183373d4
- evidence_id: native-graph
  kind: validation
  reference: /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/repo/.venv/bin/python
    scripts/uniprot_genes.py --causal-graphs --record data/structures/other/cell_surface_furrow.yaml
  locator: Complete native read-only graph coverage report
  accessed_at: '2026-10-22T04:38:45.984227Z'
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
  locator: data/structures/other/cell_surface_furrow.yaml; native collect() exact
    identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '6 of 7 collected target identifiers returned OK. PMID:7002229: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.'
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
  topic: Exact generic furrow class and topology
  outcome: supported
  target_ids:
  - GO:0097610
  summary: Active GO0097610 supports the first two definition sentences, broad/related
    synonyms, anatomical-structure is-a parent and cell-surface parthood. Cingulum
    and sulcus remain distinct child classes.
  evidence_ids:
  - record
  - cortex46-agent-go
- assessment_id: definition
  area: evidence
  topic: Unsubstantiated cross-lineage structural and functional extension
  outcome: concern
  target_ids:
  - GO:0097610
  summary: The added definition asserts persistent grooves across excavates, cryptophytes
    and euglenids, a common alveolar/epiplastid/microtubular support, and hydrodynamic
    propulsion/prey capture. The cited GO definition states none of those extensions.
    Taylor is explicitly bibliographic-only in the record and its inspected abstract
    does not establish this multi-lineage claim. This is material defining scope inflation,
    not merely a missing citation punctuation issue.
  evidence_ids:
  - record
  - curation
  - cortex46-agent-go
  - cortex46-agent-taylor1980-meta
- assessment_id: scope
  area: scope
  topic: Bounded Dinophyceae row
  outcome: supported
  target_ids:
  - GO:0097610
  summary: ENA resolves Dinophyceae. GO defines cingulum in dinoflagellates and generic
    furrows as occurring in some dinoflagellates, consistent with the limited VARIABLE
    row. That row does not justify the broader defining extensions and no unlisted
    taxon occurrence is independently established.
  evidence_ids:
  - record
  - schema
  - cortex46-agent-go
  - cortex46-agent-tax2864
- assessment_id: source-tier
  area: evidence
  topic: Taylor identity and access
  outcome: supported
  target_ids:
  - GO:0097610
  summary: PMID7002229 and the DOI resolve to Taylor1980 On dinoflagellate evolution.
    Its review abstract establishes bibliographic context only here. The historical
    no-body note remains honest; current publisher403 likewise supplies no mechanism
    or exhaustive cross-lineage evidence.
  evidence_ids:
  - record
  - cortex46-agent-taylor1980-meta
  - cortex46-agent-taylor1980-publisher
- assessment_id: graph
  area: graph
  topic: Only parthood is represented
  outcome: concern
  target_ids:
  - GO:0097610
  summary: The sole edge states supported native cell-surface parthood. MECHANISTIC
    and the assembly/mechanism title overstate this topology. Its PMID metadata-only
    citation is also weaker than the directly inspected GO relation; retain topology
    with its appropriate authority.
  evidence_ids:
  - record
  - schema
  - cortex46-agent-go
  - cortex46-agent-taylor1980-meta
- assessment_id: composition
  area: grounding
  topic: Regional component boundary
  outcome: supported
  target_ids:
  - GO:0097610
  summary: No universal molecular constituents can be inferred merely from the generic
    furrow term. The empty optional inventory is not separately defective; unsupported
    defining support-material assertions are covered by F1.
  evidence_ids:
  - record
  - curation
  - cortex46-agent-go
- assessment_id: coverage
  area: completeness
  topic: Full target, two bounded corrections
  outcome: supported
  target_ids:
  - GO:0097610
  summary: The entire target, history, three synonyms, distribution, four evidence
    entries and single graph edge were read. The exact class and parthood survive
    both proposed corrections.
  evidence_ids:
  - record
  - cortex46-agent-go
  - cortex46-agent-taylor1980-meta
findings:
- finding_id: F1
  issue_key: cell-surface-furrow-expanded-definition
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Constrain the expanded definition to supported biological scope
  description: The second definition paragraph goes beyond GO0097610 by asserting
    additional lineages, persistent cortical morphology, shared supporting structures
    and hydrodynamic functions. Those material claims are not supported by the nearest
    cited authority or the declared bibliographic-only Taylor source. This finding
    does not assert that every added example is biologically false.
  target_ids:
  - GO:0097610
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - record
  - curation
  - cortex46-agent-go
  - cortex46-agent-taylor1980-meta
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/cell_surface_furrow.yaml
    role: maintained scientific record
  rule_id: Claim-specific evidence and graph scope
  native_severity: major
  normalization_reason: The biological class remains identifiable, but unsupported
    defining cross-lineage structure and function materially expand its meaning.
- finding_id: F2
  issue_key: cell-surface-furrow-parthood-graph-scope
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Describe the single-edge graph as topology
  description: The graph is labelled MECHANISTIC/assembly mechanism although it contains
    only furrow is part of cell surface. No causal formation transition is represented;
    the current PMID edge note explicitly supplies metadata only.
  target_ids:
  - GO:0097610
  field_paths:
  - causal_graphs[0].scope_status
  - causal_graphs[0].scope_notes
  - causal_graphs[0].title
  - causal_graphs[0].description
  - causal_graphs[0].edges[0].evidence
  evidence_ids:
  - record
  - schema
  - cortex46-agent-go
  - cortex46-agent-taylor1980-meta
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/cell_surface_furrow.yaml
    role: maintained scientific record
  rule_id: Claim-specific evidence and graph scope
  native_severity: minor
  normalization_reason: The represented parthood is correct and can be preserved;
    the bounded problem is graph classification and source placement, independent
    of the defining scope correction.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0097610
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/cell_surface_furrow.yaml
    role: maintained scientific record
  description: Retain the exact generic GO definition, or support each added lineage,
    supporting structure and function with inspected claim-specific sources and explicit
    scope. Do not preserve a universal synthesis merely by attaching one dinoflagellate
    review.
  acceptance_checks:
  - Preserve GO0097610 identity, current supported synonyms and hierarchy.
  - For every retained extension, identify the source passage and its organism/anatomical/function
    boundary.
  - Pass applicable native schema, strict, reference and graph checks.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0097610
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/cell_surface_furrow.yaml
    role: maintained scientific record
  description: Mark the graph NONMECHANISTIC, give it a topology title and scope note,
    and ground the preserved parthood edge in the verified GO relation. Add mechanistic
    detail only if separately sourced.
  acceptance_checks:
  - Preserve the correct furrow-to-surface relation.
  - Ensure title, scope label and description describe the actual edge content.
  - Do not claim Taylor full-body support from bibliographic metadata.
limitations:
- Five completed same-base batch26 global gates remain staged for guarded parent integration;
  no corpus-level result is claimed through this unsaved draft.
- No image pixels, raw experiments, supplementary files or underlying studies cited
  by the review were independently reanalyzed. Exact primary and authority reading
  scopes are declared in evidence.
- Taylor1980 is metadata/complete-abstract only; the fresh publisher route returned403.
  No broad literature absence or claim that every added lineage lacks furrows is asserted.
- The native sulcus child was inspected for boundary context only; its separate definition
  references were not independently audited because the target does not rely on them.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User goal explicitly authorizes a review for every uncovered target, including honest
  clean records.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
