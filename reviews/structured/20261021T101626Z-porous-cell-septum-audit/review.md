# Porous cell septum subtype, evidence and graph review

- Review: 20261021T101626Z-porous-cell-septum-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T09:59:54Z
- Finished UTC: 2026-10-21T10:16:26Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The porous-septum identity and explicitly qualified dolipore components/functions are supported. One minor graph-scope finding remains; source access and inference boundaries are explicit.

## Scope And Provenance

Entire single record; exact native GO/taxon/citation identities,1978/2009 abstract scopes, full2008 body and stated2010 early-online primary passages.

Selection: Ninth selected target in batch eighteen, fixed maintained-path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0000934 | data/structures/envelope/porous_cell_septum.yaml | maintained | porous cell septum |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0000934 | Focused validator passed. |
| Focused native strict | passed | True | GO:0000934 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0000934 | 9 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Claim-level scientific review | passed | True | GO:0000934 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0000934 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0000934 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0000934 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0000934 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0000934 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Broad porous septum and narrower dolipore

identity: supported. Targets: GO:0000934.

The target identity and parent/synonym scope match GO. Its definition includes simple pores and dolipores; prior-work context in the cited2008 Introduction supports the fungal transport/gating distinction. That contextual synthesis is not treated as a new primary experiment in Neurospora or Aspergillus.

### Explicitly qualified dolipore substructures

scope: supported. Targets: GO:0000934.

Both component grounding notes identify dolipore-associated swelling/caps; roles and function descriptions repeatedly preserve that subtype. These are supported example substructures, not proof that every porous septum contains them. UNKNOWN necessity is appropriate and is not replaced with protein-level Spc33 necessity for a different structure. Whole morphological regions do not map to a single sequence family.

### Sampled Agaricomycotina and S.commune

scope: supported. Targets: GO:0000934.

The VARIABLE prevalence row explicitly avoids all-subphylum occurrence. The2009 metadata/abstract supports morphological diversity in a sampled literature survey with limited new observations. The2010 paper directly supports the S.commune genetic model, with the separately described purification and deletion strains kept distinct.

### Closure evidence and hypotheses are distinguished

evidence: supported. Targets: GO:0000934.

The function itself explicitly concerns dolipore septa and paired caps. The2008 localization supports participation as an inference;2010 deletion adds causal closure evidence. The source-level phrase inability to close is not interpreted as100% of measured mutant pores. Neither source establishes the exact molecular release route, a universal ascomycete cap, or a direct developmental turgor mechanism.

### Descriptive graph overstates its explanatory scope

graph: concern. Targets: GO:0000934.

The MECHANISTIC graph only gives two parthood relations and a whole-septum mediates edge. It has no represented gating transition, and its title/node use generic porous septum while edge descriptions are the dolipore example. The biological example is supported, but graph scope should state that restriction and match the represented descriptive topology.

### Optional inventory and access boundaries

completeness: supported. Targets: GO:0000934.

No additional finding is inferred from absent protein rows, exact morphology identifiers, quantitative properties, images or traits. SPC18 and Spc33 are species-specific cap evidence and should not be imported as universal porous-septum constituents. No maintained quote occurs. Definition support can be clarified using the already cited Introduction without inventing a new biological mechanism.

## Findings

### F1: State the graph subtype and descriptive scope

minor / open / confirmed; issue key: porous-septum-graph-scope.

The graph is marked MECHANISTIC but represents only component parthood and a whole-structure mediates edge. Its generic GO0000934 node/title stand for descriptions explicitly limited to the dolipore example. The cited localization evidence does not itself supply a represented causal gating transition.

## Recommended Actions And Acceptance Checks

### A1

Mark the current graph NONMECHANISTIC and explicitly restrict its example to dolipore-bearing fungi, or add a directly supported causal transition at that subtype/species scope. If using the deletion result, cite2010 at the affected edge.

- Preserve the GO0000934 versus GO0000937 distinction.
- Do not promote the proposed SPC18 transfer route into demonstrated transport.
- Retain UNKNOWN component formation necessity.
- Run focused schema/strict and native graph checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/envelope/porous_cell_septum.yaml; Entire maintained YAML including definition, components, functions, hierarchy, examples, graph edges, discussions, image metadata and history | context_only | All fields were read after fresh native inspection; the maintained target and PROPOSED state are unchanged. |
| policy | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, CausalNode and source-specific ComplexComposition contracts; essentiality definition; docs/CURATION.md assembly-versus-function guidance and review checklist | context_only | Component family identity, concrete protein identity and source-specific assembly membership are separate. Essentiality asks whether the structure forms without the component; membership and activity do not establish it. Optional fields are not mandatory. CausalNode permits protein complexes; its xrefs contract does not inherit the top-level record equivalence restriction. |
| porous-septum-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0000934,GO%3A0030428,GO%3A0000937; All three complete term definitions, synonyms and relevant child relationships | supports | GO0000934 denotes porous septum and has broad synonym porous septum; GO0030428 lists it as a septum subclass. GO0000937 is its narrower dolipore child, defined by swollen pore-wall and paired caps. The generic class does not require dolipore architecture in every instance. |
| porous-septum-agent-tax-5302 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5302; Complete taxId, scientificName, rank, lineage and relevant synonyms | supports | Native ENA taxonomy identifies Agaricomycotina, subphylum. This receipt attests that identity and rank only, not occurrence or the experimental strain. |
| porous-septum-agent-tax-5334 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5334; Complete taxId, scientificName, rank, lineage and relevant synonyms | supports | Native ENA taxonomy identifies Schizophyllum commune, species. This receipt attests that identity and rank only, not occurrence or the experimental strain. |
| porous-septum-agent-doi-10.1139_m78-129 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1139/m78-129&amp;format=json&amp;resultType=core; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Ultrastructure of the dolipore-parenthesome septum in Hirschiporus pargamenus (Polyporaceae). Authors: Traquair JA, McKeen EM.; PMID 679064; DOI 10.1139/m78-129. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| porous-septum-agent-doi-10.1016_j.mycres.2008.12.007 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016/j.mycres.2008.12.007&amp;format=json&amp;resultType=core; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Septal pore complex morphology in the Agaricomycotina (Basidiomycota) with emphasis on the Cantharellales and Hymenochaetales. Authors: van Driel KG, Humbel BM, Verkleij AJ, Stalpers J, Müller WH, Boekhout T.; PMID 19640404; DOI 10.1016/j.mycres.2008.12.007. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| porous-septum-agent-doi-10.1128_EC.00125-08 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128/EC.00125-08&amp;format=json&amp;resultType=core; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Septal pore cap protein SPC18, isolated from the basidiomycetous fungus Rhizoctonia solani, also resides in pore plugs. Authors: van Driel KG, van Peer AF, Grijpstra J, Wösten HA, Verkleij AJ, Müller WH, Boekhout T.; PMID 18757567; DOI 10.1128/ec.00125-08. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| porous-septum-agent-doi-10.1111_j.1462-2920.2009.02122.x | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1111/j.1462-2920.2009.02122.x&amp;format=json&amp;resultType=core; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies The septal pore cap is an organelle that functions in vegetative growth and mushroom formation of the wood-rot fungus Schizophyllum commune. Authors: van Peer AF, Wang F, van Driel KG, de Jong JF, van Donselaar EG, Müller WH, Boekhout T, Lugones LG, Wösten HA.; PMID 20050873; DOI 10.1111/j.1462-2920.2009.02122.x. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| porous-septum-agent-legacy-PMC2568075 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2568075/; PMC2568075: complete Introduction paragraphs preceding sec1, complete Methods sec1, Results sec13 and Discussion sec17; Figures1-8 captions. Native figure pixels and raw immunogold quantification were not independently analysed. | supports | Van Driel et al.2008 distinguishes ordinary pores from capped dolipores in its prior-work Introduction. Direct R.solani Results localize specific SPC18 antibody to caps and some plug material, not the swelling. The ER-to-cap-to-plug delivery scheme is explicitly a hypothesis, with preparation and antibody-access limits; direct material transfer or all-plug labeling is not demonstrated. |
| porous-septum-agent-peer2010-knaw-pdf | https://wi.knaw.nl/images/ResearchGroups/Publications/2009Peer0002.pdf; Genuine KNAW early-online publisher PDF, DOI matches final2010 article: Introduction and Results pp1-6, Discussion pp6-8, Experimental procedures p8 strains/growth and laser dissection plus purification opening; Figures1-7 captions. Remaining detailed cloning/proteomics Methods, supplements and movies not independently audited. | supports | Van Peer et al.2010 directly links spc33 deletion, loss of visible caps and impaired closure in S.commune. The laser assay has 7/10 wild-type septa closed and 8/10 mutant septa open; it is not a measured100% failure. Growth and temperature-dependent fruiting defects support the bounded example, while turgor explanation remains speculative. Purified cap matrix and membrane-covering evidence are separate from deletion assays. |
| porous-septum-agent-traquair1978-pdf | https://cdnsciencepub.com/doi/pdf/10.1139/m78-129; Actual response body and retrieval receipt | context_only | Publisher response is403 HTML. Exact native metadata/abstract were inspected; no final-paper body access is claimed for this route. |
| porous-septum-agent-traquair1978-publisher | https://cdnsciencepub.com/doi/10.1139/m78-129; Actual response body and retrieval receipt | context_only | Publisher response is403 HTML. Exact native metadata/abstract were inspected; no final-paper body access is claimed for this route. |
| porous-septum-agent-driel2009-publisher | https://www.sciencedirect.com/science/article/pii/S0953756209000203; Actual response body and retrieval receipt | context_only | Publisher response is403 HTML. Exact native metadata/abstract were inspected; no final-paper body access is claimed for this route. |
| schema-result | just validate data/structures/envelope/porous_cell_septum.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/envelope/porous_cell_septum.yaml |
| strict-result | just validate-strict data/structures/envelope/porous_cell_septum.yaml --out /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/porous_cell_septum-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/envelope/porous_cell_septum.yaml --out /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/porous_cell_septum-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch18-20261021-5wxxz5kh/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/porous_cell_septum-strict.tsv |
| target-curies | just check-curies-strict; data/structures/envelope/porous_cell_septum.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 9 of9 collected target identifiers returned OK in this fresh base resolver run. Residuals: none. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- The1978 and final2009 papers were available as exact native metadata/abstracts only; publisher responses were403. A separately recovered thesis chapter differs from the final2009 version and was not used as equivalent final-paper evidence.
- The2008 full Introduction, Methods, Results, Discussion and captions were read, but experimental images and raw labeling data were not independently reanalysed. Its ascomycete and broad fungal statements are prior-work context.
- The genuine2010 early-online publisher PDF supplies the named main-text and Methods passages. Detailed cloning/proteomics procedures, supplementary files, movies and raw data were not independently audited.
- No fresh exhaustive ontology absence search for parenthesome or sequence family survey was performed. Whole-cap and swelling morphology are not equated to individual protein families; no optional census is invented.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T101626Z-porous-cell-septum-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Porous cell septum subtype, evidence and graph review
started_at: '2026-10-21T09:59:54Z'
finished_at: '2026-10-21T10:16:26Z'
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
summary: The porous-septum identity and explicitly qualified dolipore components/functions
  are supported. One minor graph-scope finding remains; source access and inference
  boundaries are explicit.
source:
  git_revision: 9c0446c4c0dd4b458787c43a499e4ceab5e179a6
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
  - path: data/structures/envelope/porous_cell_septum.yaml
    sha256: 71ac61741f785e2f38b6a90e7463457e98ab432d9625ef08236e10f4787dd56f
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
- target_id: GO:0000934
  path: data/structures/envelope/porous_cell_septum.yaml
  label: porous cell septum
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/envelope/porous_cell_septum.yaml
    role: maintained scientific record
scope:
  description: Entire single record; exact native GO/taxon/citation identities,1978/2009
    abstract scopes, full2008 body and stated2010 early-online primary passages.
  selection: Ninth selected target in batch eighteen, fixed maintained-path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0000934
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0000934
  command: just validate data/structures/envelope/porous_cell_septum.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0000934
  command: just validate-strict data/structures/envelope/porous_cell_septum.yaml --out
    /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/porous_cell_septum-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0000934
  summary: 9 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0000934
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - porous-septum-agent-go
  - porous-septum-agent-tax-5302
  - porous-septum-agent-tax-5334
  - porous-septum-agent-doi-10.1139_m78-129
  - porous-septum-agent-doi-10.1016_j.mycres.2008.12.007
  - porous-septum-agent-doi-10.1128_EC.00125-08
  - porous-septum-agent-doi-10.1111_j.1462-2920.2009.02122.x
  - porous-septum-agent-legacy-PMC2568075
  - porous-septum-agent-peer2010-knaw-pdf
  - porous-septum-agent-traquair1978-pdf
  - porous-septum-agent-traquair1978-publisher
  - porous-septum-agent-driel2009-publisher
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0000934
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:53Z to
    2026-10-21T09:12:21Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0000934
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1828 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:53Z to
    2026-10-21T09:05:00Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0000934
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:57Z to
    2026-10-21T09:05:46Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0000934
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:57Z to
    2026-10-21T09:05:06Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0000934
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE.
    Transport failures and skipped prefixes are not evidence of resolution. Exact
    target identifiers are assessed separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:57Z to
    2026-10-21T09:45:43Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/envelope/porous_cell_septum.yaml
  locator: Entire maintained YAML including definition, components, functions, hierarchy,
    examples, graph edges, discussions, image metadata and history
  accessed_at: '2026-10-21T10:11:26Z'
  support: context_only
  summary: All fields were read after fresh native inspection; the maintained target
    and PROPOSED state are unchanged.
- evidence_id: policy
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, CausalNode and source-specific ComplexComposition
    contracts; essentiality definition; docs/CURATION.md assembly-versus-function
    guidance and review checklist
  accessed_at: '2026-10-21T10:11:26Z'
  support: context_only
  summary: Component family identity, concrete protein identity and source-specific
    assembly membership are separate. Essentiality asks whether the structure forms
    without the component; membership and activity do not establish it. Optional fields
    are not mandatory. CausalNode permits protein complexes; its xrefs contract does
    not inherit the top-level record equivalence restriction.
- evidence_id: porous-septum-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0000934,GO%3A0030428,GO%3A0000937
  locator: All three complete term definitions, synonyms and relevant child relationships
  accessed_at: '2026-10-21T10:00:25.325229Z'
  support: supports
  summary: GO0000934 denotes porous septum and has broad synonym porous septum; GO0030428
    lists it as a septum subclass. GO0000937 is its narrower dolipore child, defined
    by swollen pore-wall and paired caps. The generic class does not require dolipore
    architecture in every instance.
  snapshot_sha256: 358974173bdf83d06abb7104e1b20b169aa862f302212f4b18f706a5bcf2723f
- evidence_id: porous-septum-agent-tax-5302
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5302
  locator: Complete taxId, scientificName, rank, lineage and relevant synonyms
  accessed_at: '2026-10-21T10:00:25.335842Z'
  support: supports
  summary: Native ENA taxonomy identifies Agaricomycotina, subphylum. This receipt
    attests that identity and rank only, not occurrence or the experimental strain.
  snapshot_sha256: d138ad4b7673cd893a52365970ce0fd5a28ecf3634b0b259cb0709e4d46f808f
- evidence_id: porous-septum-agent-tax-5334
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5334
  locator: Complete taxId, scientificName, rank, lineage and relevant synonyms
  accessed_at: '2026-10-21T10:00:25.406259Z'
  support: supports
  summary: Native ENA taxonomy identifies Schizophyllum commune, species. This receipt
    attests that identity and rank only, not occurrence or the experimental strain.
  snapshot_sha256: fcbb2a4f5232c1dcaf6565e9522d8370a3d134f662ddeb233ff076c90aea0770
- evidence_id: porous-septum-agent-doi-10.1139_m78-129
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1139/m78-129&format=json&resultType=core
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T10:00:27.115570Z'
  support: supports
  summary: 'Native metadata identifies Ultrastructure of the dolipore-parenthesome
    septum in Hirschiporus pargamenus (Polyporaceae). Authors: Traquair JA, McKeen
    EM.; PMID 679064; DOI 10.1139/m78-129. Bibliographic identity and available abstract
    only; not a substitute for inspected article body.'
  snapshot_sha256: 664310e0c1081f1ffbcba5c8ac8bbe933b3a2d4fc88f1d0dc3aa2bc1ad244b64
- evidence_id: porous-septum-agent-doi-10.1016_j.mycres.2008.12.007
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016/j.mycres.2008.12.007&format=json&resultType=core
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T10:00:27.152924Z'
  support: supports
  summary: 'Native metadata identifies Septal pore complex morphology in the Agaricomycotina
    (Basidiomycota) with emphasis on the Cantharellales and Hymenochaetales. Authors:
    van Driel KG, Humbel BM, Verkleij AJ, Stalpers J, Müller WH, Boekhout T.; PMID
    19640404; DOI 10.1016/j.mycres.2008.12.007. Bibliographic identity and available
    abstract only; not a substitute for inspected article body.'
  snapshot_sha256: 1bf623ea910deecd0c0d90d11bbf35fd3830a1e3662a7a9ea1095f877e73a38c
- evidence_id: porous-septum-agent-doi-10.1128_EC.00125-08
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128/EC.00125-08&format=json&resultType=core
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T10:00:27.169433Z'
  support: supports
  summary: 'Native metadata identifies Septal pore cap protein SPC18, isolated from
    the basidiomycetous fungus Rhizoctonia solani, also resides in pore plugs. Authors:
    van Driel KG, van Peer AF, Grijpstra J, Wösten HA, Verkleij AJ, Müller WH, Boekhout
    T.; PMID 18757567; DOI 10.1128/ec.00125-08. Bibliographic identity and available
    abstract only; not a substitute for inspected article body.'
  snapshot_sha256: 204d3f39ccb5c23bf966ee73aca1ee9b4c04b81d05a201a801797a731854ea63
- evidence_id: porous-septum-agent-doi-10.1111_j.1462-2920.2009.02122.x
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1111/j.1462-2920.2009.02122.x&format=json&resultType=core
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T10:00:27.334662Z'
  support: supports
  summary: 'Native metadata identifies The septal pore cap is an organelle that functions
    in vegetative growth and mushroom formation of the wood-rot fungus Schizophyllum
    commune. Authors: van Peer AF, Wang F, van Driel KG, de Jong JF, van Donselaar
    EG, Müller WH, Boekhout T, Lugones LG, Wösten HA.; PMID 20050873; DOI 10.1111/j.1462-2920.2009.02122.x.
    Bibliographic identity and available abstract only; not a substitute for inspected
    article body.'
  snapshot_sha256: 98afa4f3276bdc0f44cfb92a8569d31fcf92812b10e06a146dda93ebee78ad91
- evidence_id: porous-septum-agent-legacy-PMC2568075
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2568075/
  locator: 'PMC2568075: complete Introduction paragraphs preceding sec1, complete
    Methods sec1, Results sec13 and Discussion sec17; Figures1-8 captions. Native
    figure pixels and raw immunogold quantification were not independently analysed.'
  accessed_at: '2026-10-21T10:03:10.049178Z'
  support: supports
  summary: Van Driel et al.2008 distinguishes ordinary pores from capped dolipores
    in its prior-work Introduction. Direct R.solani Results localize specific SPC18
    antibody to caps and some plug material, not the swelling. The ER-to-cap-to-plug
    delivery scheme is explicitly a hypothesis, with preparation and antibody-access
    limits; direct material transfer or all-plug labeling is not demonstrated.
  snapshot_sha256: d0cf2987ea5ca7e8b57d9f29a8a6456d466c7ddf6b2439e4d3875727c9bb6fed
- evidence_id: porous-septum-agent-peer2010-knaw-pdf
  kind: primary_source
  reference: https://wi.knaw.nl/images/ResearchGroups/Publications/2009Peer0002.pdf
  locator: 'Genuine KNAW early-online publisher PDF, DOI matches final2010 article:
    Introduction and Results pp1-6, Discussion pp6-8, Experimental procedures p8 strains/growth
    and laser dissection plus purification opening; Figures1-7 captions. Remaining
    detailed cloning/proteomics Methods, supplements and movies not independently
    audited.'
  accessed_at: '2026-10-21T10:01:24.897522Z'
  support: supports
  summary: Van Peer et al.2010 directly links spc33 deletion, loss of visible caps
    and impaired closure in S.commune. The laser assay has 7/10 wild-type septa closed
    and 8/10 mutant septa open; it is not a measured100% failure. Growth and temperature-dependent
    fruiting defects support the bounded example, while turgor explanation remains
    speculative. Purified cap matrix and membrane-covering evidence are separate from
    deletion assays.
  snapshot_sha256: 9310b0d3b6a841022ccca534b654ae46799eb58089a8d99f4a63462e4d12404c
- evidence_id: porous-septum-agent-traquair1978-pdf
  kind: authority
  reference: https://cdnsciencepub.com/doi/pdf/10.1139/m78-129
  locator: Actual response body and retrieval receipt
  accessed_at: '2026-10-21T10:01:24.901354Z'
  support: context_only
  summary: Publisher response is403 HTML. Exact native metadata/abstract were inspected;
    no final-paper body access is claimed for this route.
  snapshot_sha256: 756d10d893328fcc07f5bdea76e669b5b7835058b948c9e1f51e1fc2d3346249
- evidence_id: porous-septum-agent-traquair1978-publisher
  kind: authority
  reference: https://cdnsciencepub.com/doi/10.1139/m78-129
  locator: Actual response body and retrieval receipt
  accessed_at: '2026-10-21T10:01:24.898774Z'
  support: context_only
  summary: Publisher response is403 HTML. Exact native metadata/abstract were inspected;
    no final-paper body access is claimed for this route.
  snapshot_sha256: 2f60157c51ed8449445e2ba541d96b3d970509f604782a2944a6b40b75b86cb7
- evidence_id: porous-septum-agent-driel2009-publisher
  kind: authority
  reference: https://www.sciencedirect.com/science/article/pii/S0953756209000203
  locator: Actual response body and retrieval receipt
  accessed_at: '2026-10-21T10:01:24.901688Z'
  support: context_only
  summary: Publisher response is403 HTML. Exact native metadata/abstract were inspected;
    no final-paper body access is claimed for this route.
  snapshot_sha256: ceb21a49ec586d6921ccb94a460c026070585512f6f23f7e4dceb8d1d9c5bbbf
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/envelope/porous_cell_septum.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:59:56Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/envelope/porous_cell_septum.yaml'
  snapshot_sha256: beb8993f82e032b45b55d37dd0998b1f887c29e3cc9eb78219b78e987ff5ee2d
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/envelope/porous_cell_septum.yaml
    --out /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/porous_cell_septum-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:59:58Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/envelope/porous_cell_septum.yaml\
    \ --out /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/porous_cell_septum-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch18-20261021-5wxxz5kh/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/porous_cell_septum-strict.tsv"
  snapshot_sha256: 16de6087a673f248319a49ac5ba3dd66caf977125ee25cc4239c14a897e1755d
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/envelope/porous_cell_septum.yaml; exact collect() scope;
    hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T10:11:26Z'
  support: supports
  summary: '9 of9 collected target identifiers returned OK in this fresh base resolver
    run. Residuals: none. Source-native identity checked separately.'
  snapshot_sha256: d428d95fd13ac608f3786bcf74a032c768ac80e494b9673013e1e4d27de9ad66
- evidence_id: global-qc-result
  kind: validation
  reference: just qc
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82
  accessed_at: '2026-10-21T09:12:21Z'
  support: supports
  summary: 'Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  snapshot_sha256: 2cf77f0998cf42f98e103ee00a0f23cd610d5fcfd4814d7438d3e76bc9ef3d6d
- evidence_id: global-history-result
  kind: validation
  reference: just validate-history
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0
  accessed_at: '2026-10-21T09:05:00Z'
  support: supports
  summary: Exit 0. All 1828 history records validated; URI precheck reported zero
    invalid references.
  snapshot_sha256: 793664cc55dee807ad6725ace8cbdeb817e07c968f017af7ab0b5183a67b3df0
- evidence_id: global-products-result
  kind: validation
  reference: just validate-products
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26
  accessed_at: '2026-10-21T09:05:46Z'
  support: supports
  summary: 'Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  snapshot_sha256: dd07915effbb88aa88c56f6c102542b3cea4d9c70f381d943a664796a79c6917
- evidence_id: global-traits-result
  kind: validation
  reference: just check-trait-links --check
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad
  accessed_at: '2026-10-21T09:05:06Z'
  support: supports
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  snapshot_sha256: 6eab64b59433928ec8e0df9b0046dbccf479c84bb0911c315feebc344d536007
- evidence_id: global-curies-result
  kind: validation
  reference: just check-curies-strict
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d
  accessed_at: '2026-10-21T09:45:43Z'
  support: supports
  summary: Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE.
    Transport failures and skipped prefixes are not evidence of resolution. Exact
    target identifiers are assessed separately in this review.
  snapshot_sha256: 4b17ccc07b33ceab3eeb8631b1cf075f5f750c5a6f4820455b1930e3aa165286
assessments:
- assessment_id: identity
  area: identity
  topic: Broad porous septum and narrower dolipore
  outcome: supported
  target_ids:
  - GO:0000934
  summary: The target identity and parent/synonym scope match GO. Its definition includes
    simple pores and dolipores; prior-work context in the cited2008 Introduction supports
    the fungal transport/gating distinction. That contextual synthesis is not treated
    as a new primary experiment in Neurospora or Aspergillus.
  evidence_ids:
  - porous-septum-agent-go
  - porous-septum-agent-legacy-PMC2568075
  - record
- assessment_id: components
  area: scope
  topic: Explicitly qualified dolipore substructures
  outcome: supported
  target_ids:
  - GO:0000934
  summary: Both component grounding notes identify dolipore-associated swelling/caps;
    roles and function descriptions repeatedly preserve that subtype. These are supported
    example substructures, not proof that every porous septum contains them. UNKNOWN
    necessity is appropriate and is not replaced with protein-level Spc33 necessity
    for a different structure. Whole morphological regions do not map to a single
    sequence family.
  evidence_ids:
  - porous-septum-agent-go
  - porous-septum-agent-legacy-PMC2568075
  - porous-septum-agent-peer2010-knaw-pdf
  - porous-septum-agent-doi-10.1139_m78-129
  - porous-septum-agent-doi-10.1016_j.mycres.2008.12.007
  - porous-septum-agent-doi-10.1128_EC.00125-08
  - porous-septum-agent-doi-10.1111_j.1462-2920.2009.02122.x
  - record
  - policy
- assessment_id: taxa
  area: scope
  topic: Sampled Agaricomycotina and S.commune
  outcome: supported
  target_ids:
  - GO:0000934
  summary: The VARIABLE prevalence row explicitly avoids all-subphylum occurrence.
    The2009 metadata/abstract supports morphological diversity in a sampled literature
    survey with limited new observations. The2010 paper directly supports the S.commune
    genetic model, with the separately described purification and deletion strains
    kept distinct.
  evidence_ids:
  - porous-septum-agent-tax-5302
  - porous-septum-agent-tax-5334
  - porous-septum-agent-doi-10.1139_m78-129
  - porous-septum-agent-doi-10.1016_j.mycres.2008.12.007
  - porous-septum-agent-doi-10.1128_EC.00125-08
  - porous-septum-agent-doi-10.1111_j.1462-2920.2009.02122.x
  - porous-septum-agent-peer2010-knaw-pdf
  - record
- assessment_id: function
  area: evidence
  topic: Closure evidence and hypotheses are distinguished
  outcome: supported
  target_ids:
  - GO:0000934
  summary: The function itself explicitly concerns dolipore septa and paired caps.
    The2008 localization supports participation as an inference;2010 deletion adds
    causal closure evidence. The source-level phrase inability to close is not interpreted
    as100% of measured mutant pores. Neither source establishes the exact molecular
    release route, a universal ascomycete cap, or a direct developmental turgor mechanism.
  evidence_ids:
  - porous-septum-agent-legacy-PMC2568075
  - porous-septum-agent-peer2010-knaw-pdf
  - record
- assessment_id: graph
  area: graph
  topic: Descriptive graph overstates its explanatory scope
  outcome: concern
  target_ids:
  - GO:0000934
  summary: The MECHANISTIC graph only gives two parthood relations and a whole-septum
    mediates edge. It has no represented gating transition, and its title/node use
    generic porous septum while edge descriptions are the dolipore example. The biological
    example is supported, but graph scope should state that restriction and match
    the represented descriptive topology.
  evidence_ids:
  - porous-septum-agent-go
  - porous-septum-agent-legacy-PMC2568075
  - porous-septum-agent-peer2010-knaw-pdf
  - record
  - policy
- assessment_id: coverage
  area: completeness
  topic: Optional inventory and access boundaries
  outcome: supported
  target_ids:
  - GO:0000934
  summary: No additional finding is inferred from absent protein rows, exact morphology
    identifiers, quantitative properties, images or traits. SPC18 and Spc33 are species-specific
    cap evidence and should not be imported as universal porous-septum constituents.
    No maintained quote occurs. Definition support can be clarified using the already
    cited Introduction without inventing a new biological mechanism.
  evidence_ids:
  - porous-septum-agent-go
  - porous-septum-agent-legacy-PMC2568075
  - porous-septum-agent-peer2010-knaw-pdf
  - porous-septum-agent-doi-10.1139_m78-129
  - porous-septum-agent-doi-10.1016_j.mycres.2008.12.007
  - porous-septum-agent-doi-10.1128_EC.00125-08
  - porous-septum-agent-doi-10.1111_j.1462-2920.2009.02122.x
  - record
  - policy
findings:
- finding_id: F1
  issue_key: porous-septum-graph-scope
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: State the graph subtype and descriptive scope
  description: The graph is marked MECHANISTIC but represents only component parthood
    and a whole-structure mediates edge. Its generic GO0000934 node/title stand for
    descriptions explicitly limited to the dolipore example. The cited localization
    evidence does not itself supply a represented causal gating transition.
  target_ids:
  - GO:0000934
  field_paths:
  - causal_graphs[graph_id=porous_cell_septum_mechanism].scope_status
  - causal_graphs[graph_id=porous_cell_septum_mechanism].scope_notes
  - causal_graphs[graph_id=porous_cell_septum_mechanism].description
  evidence_ids:
  - porous-septum-agent-go
  - porous-septum-agent-legacy-PMC2568075
  - porous-septum-agent-peer2010-knaw-pdf
  - record
  - policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/envelope/porous_cell_septum.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: minor
  normalization_reason: Supported dolipore biology and correct broad identity can
    remain; the required correction is bounded graph interpretation.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0000934
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/envelope/porous_cell_septum.yaml
    role: maintained scientific record
  description: Mark the current graph NONMECHANISTIC and explicitly restrict its example
    to dolipore-bearing fungi, or add a directly supported causal transition at that
    subtype/species scope. If using the deletion result, cite2010 at the affected
    edge.
  acceptance_checks:
  - Preserve the GO0000934 versus GO0000937 distinction.
  - Do not promote the proposed SPC18 transfer route into demonstrated transport.
  - Retain UNKNOWN component formation necessity.
  - Run focused schema/strict and native graph checks.
limitations:
- The1978 and final2009 papers were available as exact native metadata/abstracts only;
  publisher responses were403. A separately recovered thesis chapter differs from
  the final2009 version and was not used as equivalent final-paper evidence.
- The2008 full Introduction, Methods, Results, Discussion and captions were read,
  but experimental images and raw labeling data were not independently reanalysed.
  Its ascomycete and broad fungal statements are prior-work context.
- The genuine2010 early-online publisher PDF supplies the named main-text and Methods
  passages. Detailed cloning/proteomics procedures, supplementary files, movies and
  raw data were not independently audited.
- No fresh exhaustive ontology absence search for parenthesome or sequence family
  survey was performed. Whole-cap and swelling morphology are not equated to individual
  protein families; no optional census is invented.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
