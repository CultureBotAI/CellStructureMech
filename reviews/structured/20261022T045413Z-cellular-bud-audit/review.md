# Cellular bud scientific review

- Review: 20261022T045413Z-cellular-bud-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T04:36:56Z
- Finished UTC: 2026-10-22T04:54:13Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Cellular-bud identity, parts, yeast scope and localized-growth example are supported; no concrete curation finding, with explicit primary-text and mechanistic limits.

## Scope And Provenance

Exactly one entire maintained record; native identities, all claim-bearing fields, source-specific evidence, hierarchy, topology and boundary decisions reviewed. Neighbor records, where frozen, were read only for identity/definition and component-boundary context.

Selection: Target 4 of batch46 in strict uncovered path order at unchanged origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0005933 | data/structures/other/cellular_bud.yaml | maintained | cellular bud |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0005933 | Focused validator passed. |
| Focused native strict | passed | True | GO:0005933 | Focused validator passed. |
| Native graph coverage | passed | True | GO:0005933 | No GENE_OR_PROTEIN nodes; native coverage passed. Scientific topology and mechanism claims were assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0005933 | No transcriptomic or expression-module claim is made; localized protein names in literature context are not an iModulon claim. |
| Claim-level scientific review | passed | True | GO:0005933 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0005933 | 11 of 11 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0005933 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0005933 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0005933 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0005933 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0005933 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Daughter outgrowth rather than a protein assembly

identity: supported. Targets: GO:0005933.

The definition is a faithful bounded description of GO0005933. UniProt SL0027 supplies Bud/Growing bud exact naming. The generic bud class can include associated mother/daughter cells after division; the record does not require physical detachment in every organism.

### Membrane, neck and tip

identity: supported. Targets: GO:0005933.

All three has_part links are native GO part_of relationships and are corroborated by the UniProt location hierarchy. The membrane surrounds the outgrowth; the neck and distal tip are regions, not independent organelles.

### Budding-yeast occurrence and example

scope: supported. Targets: GO:0005933.

S.cerevisiae is correctly identified. COMMON retains present-in-most-members/losses-exception meaning, supported by normal yeast budding biology without a measured prevalence census. The canonical example is appropriately narrowed to Pea2/Spa2 localization in the cited study.

### Polarized budding growth

evidence: supported. Targets: GO:0005933.

Valtz Introduction and localization experiments and Glomb cell-cycle synthesis support a growing mother-attached daughter outgrowth followed by cytokinesis. The record does not claim Pea2/Spa2 are sufficient for all bud formation or transfer mating-projection results to the bud.

### Nonmechanistic bud topology

graph: supported. Targets: GO:0005933.

The three edges accurately describe membrane enclosure and neck/tip parthood. NONMECHANISTIC and the explicit scope note match this regional topology.

### No forced molecular inventory

grounding: supported. Targets: GO:0005933.

This whole outgrowth contains many cellular constituents. Its optional component slot need not duplicate the complete cell or polarisome machinery, and no component-formation essentiality is asserted.

### Historical narrowing remains valid

completeness: supported. Targets: GO:0005933.

All fields and the historical canonical-example correction were reviewed. The maintained example now matches the inspected localization result; no new issue is observed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/cellular_bud.yaml; Entire maintained target including history, all evidence, graph and discussions | context_only | The complete target was read; history documents provenance and does not independently validate current science. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; Structure kinds, hierarchy, material constitution versus formation necessity, COMMON/VARIABLE and graph scope | context_only | Regional topology and causal mechanism are distinct; COMMON means present in most members with losses the exception, and VARIABLE denotes presence in some members. Empty optional molecular inventories are not automatically errors. |
| curation | docs/CURATION.md; Identity, claim-specific evidence and component granularity | context_only | A source must support the particular biological claim; regional records need not duplicate every molecular constituent of localized substructures. |
| cortex46-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005938,GO:0005737,GO:0005886,GO:0030479,GO:0005940,GO:0097610,GO:0110165,GO:0009986,GO:0097611,GO:0097612,GO:0005933,GO:0033101,GO:0005935,GO:0005934; Complete requested GO0005938/0005737/0005886/0030479/0005940/0097610/0110165/0009986/0097611/0097612/0005933/0033101/0005935/0005934 responses; only maintained relevant child links assessed | supports | Current active GO identities, exact definitions/synonyms and relevant typed parent/parthood links were inspected for this target and its named structures. |
| cortex46-agent-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete native taxonomy response including rank/lineage/names | supports | ENA confirms Saccharomyces cerevisiae at species rank. |
| cortex46-agent-glomb2016-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.3389/fcell.2016.00123%22; Native id/title/authors/year/DOI and complete abstract | supports | Exact native MED27857941 identity: Septin Organization and Functions in Budding Yeast. DOI 10.3389/fcell.2016.00123. Complete abstract read; any body inspection is separately specified. |
| cortex46-agent-glomb2016-xml | https://pmc.ncbi.nlm.nih.gov/articles/PMC5093138/?report=xml; Complete main scientific prose: article paragraphs8–25, especially16–21 and Figure2 caption; abstract and bibliographic identity; reference list and figure pixels not certified | supports | The secondary review distinguishes mitotic yeast septins and their ring/collar/split-ring transitions at the mother-bud neck, and describes the cortical scaffold and cytokinesis context. It is not a primary experiment or a universal timing assay. |
| cortex46-agent-valtz1996-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1083/jcb.135.3.725%22; Native id/title/authors/year/DOI and complete abstract | supports | Exact native MED8909546 identity: Pea2 protein of yeast is localized to sites of polarized growth and is required for efficient mating and bipolar budding. DOI 10.1083/jcb.135.3.725. Complete abstract read; any body inspection is separately specified. |
| cortex46-agent-valtz1996-pdf | https://pdfs.semanticscholar.org/8982/cdabd9dce19878a052f4e0fd2474e5ed5917.pdf; Genuine PDF extracted text: p725 Abstract/Introduction; p726 yeast growth conditions; p728 Immunofluorescence Methods; pp731–733 Pea2 budding-cell localization with Fig4/5 captions; pp734–735 Fig6 and Pea2/Spa2 mutant-localization Results. No image pixels or sequence-alignment analysis. | supports | Pea2 localizes to polarized-growth sites in haploid/diploid budding cells and relocalizes to the neck before cytokinesis; Spa2/Pea2 show dependent localization in the tested mutants. The canonical example is restricted to this localization evidence, not a complete budding mechanism. |
| cortex46-agent-SL-0027 | https://rest.uniprot.org/locations/SL-0027.json; Complete native entry including definitions/synonyms/partOf; nested unrelated membrane descriptions are context only | supports | Native location identity, GO mapping and maintained bud-part relationship agree. |
| cortex46-agent-SL-0028 | https://rest.uniprot.org/locations/SL-0028.json; Complete native entry including definitions/synonyms/partOf; nested unrelated membrane descriptions are context only | supports | Native location identity, GO mapping and maintained bud-part relationship agree. |
| cortex46-agent-SL-0029 | https://rest.uniprot.org/locations/SL-0029.json; Complete native entry including definitions/synonyms/partOf; nested unrelated membrane descriptions are context only | supports | Native location identity, GO mapping and maintained bud-part relationship agree. |
| cortex46-agent-SL-0030 | https://rest.uniprot.org/locations/SL-0030.json; Complete native entry including definitions/synonyms/partOf; nested unrelated membrane descriptions are context only | supports | Native location identity, GO mapping and maintained bud-part relationship agree. |
| schema-result | just validate data/structures/other/cellular_bud.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/cellular_bud.yaml |
| strict-result | just validate-strict data/structures/other/cellular_bud.yaml --out /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/cellular_bud-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/cellular_bud.yaml --out /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/cellular_bud-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch46-20261022-nrgmxxyw/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/cellular_bud-strict.tsv |
| native-graph | /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/repo/.venv/bin/python scripts/uniprot_genes.py --causal-graphs --record data/structures/other/cellular_bud.yaml; Complete native read-only graph coverage report | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/other/cellular_bud.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 11 of 11 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Five completed same-base batch26 global gates remain staged for guarded parent integration; no corpus-level result is claimed through this unsaved draft.
- No image pixels, raw experiments, supplementary files or underlying studies cited by the review were independently reanalyzed. Exact primary and authority reading scopes are declared in evidence.
- Valtz1996 was inspected as extracted PDF text over the listed sections, not as a full image-level or all-page analysis. The same study contains mating and budding experiments; only the budding localization result supports this canonical example.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User goal explicitly authorizes a review for every uncovered target, including honest clean records.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T045413Z-cellular-bud-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Cellular bud scientific review
started_at: '2026-10-22T04:36:56Z'
finished_at: '2026-10-22T04:54:13Z'
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
summary: Cellular-bud identity, parts, yeast scope and localized-growth example are
  supported; no concrete curation finding, with explicit primary-text and mechanistic
  limits.
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
  - path: data/structures/other/cellular_bud.yaml
    sha256: fbf8f5612bc661a91f8f2991018db67cae34dd7859360b981ef05a99a9582ea8
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
- target_id: GO:0005933
  path: data/structures/other/cellular_bud.yaml
  label: cellular bud
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/cellular_bud.yaml
    role: maintained scientific record
scope:
  description: Exactly one entire maintained record; native identities, all claim-bearing
    fields, source-specific evidence, hierarchy, topology and boundary decisions reviewed.
    Neighbor records, where frozen, were read only for identity/definition and component-boundary
    context.
  selection: Target 4 of batch46 in strict uncovered path order at unchanged origin/main
    f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0005933
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0005933
  command: just validate data/structures/other/cellular_bud.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0005933
  command: just validate-strict data/structures/other/cellular_bud.yaml --out /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/cellular_bud-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-graph
  name: Native graph coverage
  status: passed
  required: true
  target_ids:
  - GO:0005933
  command: /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/repo/.venv/bin/python
    scripts/uniprot_genes.py --causal-graphs --record data/structures/other/cellular_bud.yaml
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
  - GO:0005933
  summary: No transcriptomic or expression-module claim is made; localized protein
    names in literature context are not an iModulon claim.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0005933
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - cortex46-agent-go
  - cortex46-agent-tax4932
  - cortex46-agent-glomb2016-meta
  - cortex46-agent-glomb2016-xml
  - cortex46-agent-valtz1996-meta
  - cortex46-agent-valtz1996-pdf
  - cortex46-agent-SL-0027
  - cortex46-agent-SL-0028
  - cortex46-agent-SL-0029
  - cortex46-agent-SL-0030
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0005933
  summary: 11 of 11 collected target identifiers returned OK. No residuals. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.
  evidence_ids:
  - target-curies
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0005933
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
  - GO:0005933
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
  - GO:0005933
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
  - GO:0005933
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
  - GO:0005933
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
  reference: data/structures/other/cellular_bud.yaml
  locator: Entire maintained target including history, all evidence, graph and discussions
  accessed_at: '2026-10-22T04:42:26Z'
  support: context_only
  summary: The complete target was read; history documents provenance and does not
    independently validate current science.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Structure kinds, hierarchy, material constitution versus formation necessity,
    COMMON/VARIABLE and graph scope
  accessed_at: '2026-10-22T04:42:26Z'
  support: context_only
  summary: Regional topology and causal mechanism are distinct; COMMON means present
    in most members with losses the exception, and VARIABLE denotes presence in some
    members. Empty optional molecular inventories are not automatically errors.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Identity, claim-specific evidence and component granularity
  accessed_at: '2026-10-22T04:42:26Z'
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
- evidence_id: cortex46-agent-tax4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete native taxonomy response including rank/lineage/names
  accessed_at: '2026-10-22T04:38:31.951602Z'
  support: supports
  summary: ENA confirms Saccharomyces cerevisiae at species rank.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: cortex46-agent-glomb2016-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.3389/fcell.2016.00123%22
  locator: Native id/title/authors/year/DOI and complete abstract
  accessed_at: '2026-10-22T04:38:31.986655Z'
  support: supports
  summary: 'Exact native MED27857941 identity: Septin Organization and Functions in
    Budding Yeast. DOI 10.3389/fcell.2016.00123. Complete abstract read; any body
    inspection is separately specified.'
  snapshot_sha256: 55c3cbb796781b2226675513f630ca62ac15cb7cbbccd65ded4794bd175fbd11
- evidence_id: cortex46-agent-glomb2016-xml
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC5093138/?report=xml
  locator: 'Complete main scientific prose: article paragraphs8–25, especially16–21
    and Figure2 caption; abstract and bibliographic identity; reference list and figure
    pixels not certified'
  accessed_at: '2026-10-21T08:12:09.597497Z'
  support: supports
  summary: The secondary review distinguishes mitotic yeast septins and their ring/collar/split-ring
    transitions at the mother-bud neck, and describes the cortical scaffold and cytokinesis
    context. It is not a primary experiment or a universal timing assay.
  snapshot_sha256: 73f8135ddd5beb0a4f937757190372a5a881bc331a34a9e837b6c1264f0c35d8
- evidence_id: cortex46-agent-valtz1996-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1083/jcb.135.3.725%22
  locator: Native id/title/authors/year/DOI and complete abstract
  accessed_at: '2026-10-22T04:38:32.557137Z'
  support: supports
  summary: 'Exact native MED8909546 identity: Pea2 protein of yeast is localized to
    sites of polarized growth and is required for efficient mating and bipolar budding.
    DOI 10.1083/jcb.135.3.725. Complete abstract read; any body inspection is separately
    specified.'
  snapshot_sha256: 5995f18fa905450fc26415293cae1475f7acb5da7cc4752f3db0356906c58c43
- evidence_id: cortex46-agent-valtz1996-pdf
  kind: primary_source
  reference: https://pdfs.semanticscholar.org/8982/cdabd9dce19878a052f4e0fd2474e5ed5917.pdf
  locator: 'Genuine PDF extracted text: p725 Abstract/Introduction; p726 yeast growth
    conditions; p728 Immunofluorescence Methods; pp731–733 Pea2 budding-cell localization
    with Fig4/5 captions; pp734–735 Fig6 and Pea2/Spa2 mutant-localization Results.
    No image pixels or sequence-alignment analysis.'
  accessed_at: '2026-10-21T09:48:11.208322Z'
  support: supports
  summary: Pea2 localizes to polarized-growth sites in haploid/diploid budding cells
    and relocalizes to the neck before cytokinesis; Spa2/Pea2 show dependent localization
    in the tested mutants. The canonical example is restricted to this localization
    evidence, not a complete budding mechanism.
  snapshot_sha256: c06951939912dcb3700b5cd867b40a7d9c2a74f41460bb93f31839852509d9c9
- evidence_id: cortex46-agent-SL-0027
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0027.json
  locator: Complete native entry including definitions/synonyms/partOf; nested unrelated
    membrane descriptions are context only
  accessed_at: '2026-10-22T04:38:31.208429Z'
  support: supports
  summary: Native location identity, GO mapping and maintained bud-part relationship
    agree.
  snapshot_sha256: 3367af44f7485396df649e631b15487f577a11026c6701fbbd535fec005f759d
- evidence_id: cortex46-agent-SL-0028
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0028.json
  locator: Complete native entry including definitions/synonyms/partOf; nested unrelated
    membrane descriptions are context only
  accessed_at: '2026-10-22T04:38:31.208566Z'
  support: supports
  summary: Native location identity, GO mapping and maintained bud-part relationship
    agree.
  snapshot_sha256: de42296b0da87c46a5410f4d244378b490c2d8744bdf0cc134a5cb48100f79be
- evidence_id: cortex46-agent-SL-0029
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0029.json
  locator: Complete native entry including definitions/synonyms/partOf; nested unrelated
    membrane descriptions are context only
  accessed_at: '2026-10-22T04:38:31.208713Z'
  support: supports
  summary: Native location identity, GO mapping and maintained bud-part relationship
    agree.
  snapshot_sha256: b75910789f9dbd212cb0c9adadae4638f350b4d79a5ea69cae38559f7d33b931
- evidence_id: cortex46-agent-SL-0030
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0030.json
  locator: Complete native entry including definitions/synonyms/partOf; nested unrelated
    membrane descriptions are context only
  accessed_at: '2026-10-22T04:38:31.208783Z'
  support: supports
  summary: Native location identity, GO mapping and maintained bud-part relationship
    agree.
  snapshot_sha256: 6947119e52ad8021360b342a15d99f13085292f3e4d9a0dcf499ddddbd1272fc
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/cellular_bud.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:36:57Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/cellular_bud.yaml'
  snapshot_sha256: e2173c6c82fc3d3e412580cb5db7c76b112bf9d5a308bdd1524d49d3e4d47b23
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/cellular_bud.yaml --out /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/cellular_bud-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:36:58Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/cellular_bud.yaml\
    \ --out /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/cellular_bud-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch46-20261022-nrgmxxyw/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/cellular_bud-strict.tsv"
  snapshot_sha256: 363711b771f53238560f605ea8c9f2344091e3d2a1c64039bdc706c4213d459c
- evidence_id: native-graph
  kind: validation
  reference: /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/repo/.venv/bin/python
    scripts/uniprot_genes.py --causal-graphs --record data/structures/other/cellular_bud.yaml
  locator: Complete native read-only graph coverage report
  accessed_at: '2026-10-22T04:38:46.594869Z'
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
  locator: data/structures/other/cellular_bud.yaml; native collect() exact identifier
    slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 11 of 11 collected target identifiers returned OK. No residuals. Native
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
  topic: Daughter outgrowth rather than a protein assembly
  outcome: supported
  target_ids:
  - GO:0005933
  summary: The definition is a faithful bounded description of GO0005933. UniProt
    SL0027 supplies Bud/Growing bud exact naming. The generic bud class can include
    associated mother/daughter cells after division; the record does not require physical
    detachment in every organism.
  evidence_ids:
  - record
  - cortex46-agent-go
  - cortex46-agent-SL-0027
  - cortex46-agent-SL-0028
  - cortex46-agent-SL-0029
  - cortex46-agent-SL-0030
- assessment_id: topology
  area: identity
  topic: Membrane, neck and tip
  outcome: supported
  target_ids:
  - GO:0005933
  summary: All three has_part links are native GO part_of relationships and are corroborated
    by the UniProt location hierarchy. The membrane surrounds the outgrowth; the neck
    and distal tip are regions, not independent organelles.
  evidence_ids:
  - record
  - cortex46-agent-go
  - cortex46-agent-SL-0027
  - cortex46-agent-SL-0028
  - cortex46-agent-SL-0029
  - cortex46-agent-SL-0030
- assessment_id: scope
  area: scope
  topic: Budding-yeast occurrence and example
  outcome: supported
  target_ids:
  - GO:0005933
  summary: S.cerevisiae is correctly identified. COMMON retains present-in-most-members/losses-exception
    meaning, supported by normal yeast budding biology without a measured prevalence
    census. The canonical example is appropriately narrowed to Pea2/Spa2 localization
    in the cited study.
  evidence_ids:
  - record
  - schema
  - cortex46-agent-tax4932
  - cortex46-agent-valtz1996-pdf
  - cortex46-agent-glomb2016-xml
- assessment_id: function
  area: evidence
  topic: Polarized budding growth
  outcome: supported
  target_ids:
  - GO:0005933
  summary: Valtz Introduction and localization experiments and Glomb cell-cycle synthesis
    support a growing mother-attached daughter outgrowth followed by cytokinesis.
    The record does not claim Pea2/Spa2 are sufficient for all bud formation or transfer
    mating-projection results to the bud.
  evidence_ids:
  - record
  - cortex46-agent-go
  - cortex46-agent-valtz1996-pdf
  - cortex46-agent-glomb2016-xml
- assessment_id: graph
  area: graph
  topic: Nonmechanistic bud topology
  outcome: supported
  target_ids:
  - GO:0005933
  summary: The three edges accurately describe membrane enclosure and neck/tip parthood.
    NONMECHANISTIC and the explicit scope note match this regional topology.
  evidence_ids:
  - record
  - schema
  - cortex46-agent-go
  - cortex46-agent-SL-0027
  - cortex46-agent-SL-0028
  - cortex46-agent-SL-0029
  - cortex46-agent-SL-0030
- assessment_id: composition
  area: grounding
  topic: No forced molecular inventory
  outcome: supported
  target_ids:
  - GO:0005933
  summary: This whole outgrowth contains many cellular constituents. Its optional
    component slot need not duplicate the complete cell or polarisome machinery, and
    no component-formation essentiality is asserted.
  evidence_ids:
  - record
  - curation
  - cortex46-agent-go
  - cortex46-agent-valtz1996-pdf
- assessment_id: coverage
  area: completeness
  topic: Historical narrowing remains valid
  outcome: supported
  target_ids:
  - GO:0005933
  summary: All fields and the historical canonical-example correction were reviewed.
    The maintained example now matches the inspected localization result; no new issue
    is observed.
  evidence_ids:
  - record
  - cortex46-agent-valtz1996-pdf
  - cortex46-agent-go
findings: []
actions: []
limitations:
- Five completed same-base batch26 global gates remain staged for guarded parent integration;
  no corpus-level result is claimed through this unsaved draft.
- No image pixels, raw experiments, supplementary files or underlying studies cited
  by the review were independently reanalyzed. Exact primary and authority reading
  scopes are declared in evidence.
- Valtz1996 was inspected as extracted PDF text over the listed sections, not as a
  full image-level or all-page analysis. The same study contains mating and budding
  experiments; only the budding localization result supports this canonical example.
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
