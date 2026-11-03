# Spindle pole scope, gamma-complex identity and source review

- Review: 20261021T094825Z-spindle-pole-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T09:24:39Z
- Finished UTC: 2026-10-21T09:48:25Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Generic spindle-pole and gamma-complex identities and the yeast reference case are supported. One major source/taxon-scope issue and two minor synonym/graph-scope issues remain; assembly necessity is explicitly unverified.

## Scope And Provenance

Entire single target, native region/complex/process/taxon identities, source-specific SPB versus general-pole boundary, all component/function/graph claims and review-versus-primary evidence scope.

Selection: Tenth selected target in batch sixteen, fixed maintained-path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0000922 | data/structures/cytoskeleton/spindle_pole.yaml | maintained | spindle pole |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0000922 | Focused validator passed. |
| Focused native strict | passed | True | GO:0000922 | Focused validator passed. |
| Claim-level scientific review | passed | True | GO:0000922 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Target resolver slice with native transport-failure cross-checks | passed | True | GO:0000922 | 12 of 12 exact target identifiers returned OK. No target residuals. The shared command exit zero is not interpreted as successful network resolution for transport failures. |
| Full corpus QC | passed | True | GO:0000922 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0000922 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0000922 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0000922 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0000922 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Generic pole is broader than a spindle pole body

identity: supported. Targets: GO:0000922.

The target is the polar spindle region, with spindle parthood and a species-specific SPB structural example. It is not equated to only the budding-yeast SPB. The native definition says it usually contains an MTOC; the record distribution also acknowledges acentrosomal poles.

### GO0000930 correctly covers generic gamma-tubulin complexes

grounding: supported. Targets: GO:0000922.

The component label and role explicitly cover gamma-TuSC/gamma-TuRC. Native GO0000930 is the generic gamma-tubulin complex with species-variable partners; its small-complex and ring-complex children must not be confused with the parent. This mapping does not assert that every complex has universal ring geometry or the same subunits.

### The broad pole definition adds a source-unmatched molecular roster

evidence: concern. Targets: GO:0000922.

The appended text combines kinesin-14, NuMA/Pkl1/Mto1 and gamma-tubulin-ring machinery across yeasts, fungi, microalgae and protists. GO supplies the generic regional definition, while Jaspersen is a yeast-SPB review with a centrosome comparison. Its readable sections and Viswanath core context do not establish that entire named combination throughout those groups.

### Keep yeast pole-duplication evidence at its actual scope

scope: concern. Targets: GO:0000922.

The review supports budding-yeast SPB duplication, bridge cleavage and Cin8/Kip1-dependent separation. Its centrosome comparison explicitly preserves similarities and differences. The record evidence notes generalize this to spindle-pole duplication across eukaryotes, including the acentrosomal scope it otherwise acknowledges, without matching evidence.

### Presence and nucleation do not establish universal assembly necessity

evidence: unknown. Targets: GO:0000922.

Both components are ESSENTIAL. Source evidence for yeast MTOC organization and gamma-complex nucleation supports membership/function in that system, but does not show that the broad spindle-pole structure fails to form without each generic component across its taxonomic scope. The schema criterion is formation, not catalytic function, cell viability or presence in the intact reference architecture.

### Broad occurrence and canonical yeast architecture

scope: supported. Targets: GO:0000922.

Eukaryota and S.cerevisiae labels/ranks are correct; the yeast canonical SPB architecture example is supported. COMMON is not treated as a measured prevalence. The broad terminal-region identity does not authorize exporting the exact yeast molecular or duplication mechanism to every eukaryote.

### GO does not supply the maintained narrow synonym

provenance: concern. Targets: GO:0000922.

Native GO0000922 contains no synonym annotation in the inspected response. Mitotic spindle pole is a plausible narrower phrase, but its GO source attribution is unsupported and should be repaired rather than mistaken for a source-provided synonym.

### Organizational description lacks a represented causal transition

graph: concern. Targets: GO:0000922.

The graph links MTOC/gamma-complex/SPB parts and whole-pole functions. Its text describes nucleation/anchoring and duplication, but the edges do not represent those transitions or the component-to-function dependency. Keep supported topology distinct from the stronger MECHANISTIC scope claim.

### No forced molecular census for a generic polar region

completeness: supported. Targets: GO:0000922.

The two class-level components have valid identities. Exact protein examples, stoichiometry, family splitting and full centrosome/SPB inventories are optional. The material problem is unsupported broad mechanism, with assembly necessity explicitly unresolved; optional inventory is not promoted to a finding.

## Findings

### F1: Bound the specific pole mechanism and duplication claims to their evidence

major / open / confirmed; issue key: spindle-pole-mechanism-taxonomic-source-inflation.

The definition adds a combined kinesin-14/NuMA/Pkl1/Mto1/gamma-ring mechanism across broad microbial eukaryote groups while citing only the generic GO definition. The function and graph evidence further say the yeast-focused review establishes pole duplication/separation across eukaryotes. The inspected review and primary yeast-core context support narrower claims; neither establishes this whole combined generalization.

### F2: Repair the source attribution of the narrow pole synonym

minor / open / confirmed; issue key: spindle-pole-narrow-synonym-go-provenance.

The phrase mitotic spindle pole is labeled a GO0000922 narrow synonym, but the native term does not supply that synonym. Preserve it only with an appropriate independent source/curator provenance or use the source-provided annotations.

### F3: Match graph scope to the represented relationships

minor / open / confirmed; issue key: spindle_pole_mechanism-static-graph-scope.

The FUNCTION graph contains structural parthood and whole-structure-to-process mediates edges. Its descriptions mention biological activities, but the graph does not connect an explicit assembly or functional transition to those activities. MECHANISTIC overstates what is represented; this is a scope classification concern, not a claim that the supported topology is false or a demand for atomic detail.

## Recommended Actions And Acceptance Checks

### A1

During authorized curation, retain the generic regional definition and qualify named molecular/duplication mechanisms to directly supported organisms and spindle stages, or supply inspected sources covering the broader assertion.

- Preserve the difference between a spindle pole, yeast SPB, centrosome and acentrosomal pole.
- Retain GO0000930 for the generic gamma-complex class; do not replace it with a falsely universal ring-only identity.
- Do not describe review synthesis as primary experimental proof.
- Resolve component assembly necessity separately from nucleation activity.
- Run focused schema, strict-reference and causal-graph checks.

### A2

During authorized curation, correct the source for the added phrase rather than treating plausible wording as a native GO annotation.

- Verify the exact source string and synonym scope.
- Do not invent an ontology synonym when the response contains none.
- Run focused schema and strict-reference checks.

### A3

During authorized curation, mark the current descriptive graph NONMECHANISTIC with a clear scope note, or represent a specific source-supported transition at an explicit organism and developmental scope.

- Keep supported identity and parthood relationships.
- Do not infer an assembly requirement merely from composition or localization.
- Any added mechanistic edge must cite the source that actually establishes that transition.
- Run focused schema, strict-reference and causal-graph validation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/spindle_pole.yaml; Entire maintained YAML including all imported participants, component examples, functions, graph edges, discussions and history | context_only | All fields were read after fresh native inspection; the maintained target and PROPOSED state are unchanged. |
| policy | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, CausalNode and source-specific ComplexComposition contracts; essentiality definition; docs/CURATION.md assembly-versus-function guidance and review checklist | context_only | Component family identity, concrete protein identity and source-specific assembly membership are separate. Essentiality asks whether the structure forms without the component; membership and activity do not establish it. Optional fields are not mandatory. CausalNode permits protein complexes; its xrefs contract does not inherit the top-level record equivalence restriction. |
| pole-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000226,GO:0000922,GO:0000930,GO:0005815,GO:0005816,GO:0005819,GO:0051225,GO:0110165; All returned term identities, definitions, synonym annotations and relevant child relations: GO:0000226, GO:0000922, GO:0000930, GO:0005815, GO:0005816, GO:0005819, GO:0051225, GO:0110165. GO0000922 supplies no synonym annotation in this response. | supports | Native definitions distinguish the target structure, its returned related structural classes and relevant processes. Exact returned synonyms and source-specific relations were checked separately from plausible curator-authored language. |
| pole-agent-tax-2759 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759; Complete taxon identity, rank and lineage | supports | Native taxonomy confirms the named organism and rank; broad clade occurrence is separate from a molecular mechanism established in one yeast. |
| pole-agent-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete taxon identity, rank and lineage | supports | Native taxonomy confirms the named organism and rank; broad clade occurrence is separate from a molecular mechanism established in one yeast. |
| pole-agent-doi-annurev.cellbio.20.022003.114106 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1146/annurev.cellbio.20.022003.114106; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies The budding yeast spindle pole body: structure, duplication, and function. Authors: Jaspersen SL, Winey M.; PMID 15473833; DOI 10.1146/annurev.cellbio.20.022003.114106. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| pole-agent-jaspersen-browser | https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function; Author-manuscript browser extraction, pages5–10, displayed lines185–410: Introduction, SPB organization and core components. This is captured browser text; legacy metadata status200 is not an independently recorded native HTTP response. | supports | Jaspersen and Winey2004 is a review focused on the budding-yeast SPB, its layered structure and nuclear/cytoplasmic microtubule organization. The author manuscript is review-tier context rather than primary experimental proof for all eukaryotic poles. |
| pole-agent-jaspersen-duplication-browser | https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function; Author-manuscript browser extraction: duplication/separation pages15–20, displayed lines619–705 and730–800; intervening omitted lines were not read. | supports | The review describes budding-yeast SPB duplication and bridge cleavage followed by Cin8/Kip1-dependent pole separation. This supports a scoped yeast pathway, not a uniform pole-duplication mechanism for every microbial eukaryote. |
| pole-agent-jaspersen-nucleation-browser | https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function; Author-manuscript browser extraction: pages24–26 displayed lines976–1077, and pages30–32 lines1213–1308. Read scope includes gamma-tubulin machinery and the SPB/centrosome comparison, not the entire review. | supports | The review treats Tub4/Spc97/Spc98 nucleation complexes, Spc110/Spc72 targeting and comparison with centrosomes. Similarities coexist with structural and duplication differences; mechanistic models and inferred minus-end capping retain their stated uncertainty. |
| pole-agent-viswanath2017 | https://pmc-oa-opendata.s3.amazonaws.com/PMC5687031.1/PMC5687031.1.xml; Native PMC5687031.1 JATS: complete Introduction including Figure1 caption. Additional initial Results were consulted but no conclusion here depends on a complete Results audit. | supports | Viswanath et al.2017 provides primary integrative structural work on the yeast SPB core. Its Introduction and Figure1 distinguish inner/outer plaques and gamma-TuSC assemblies; these contextual claims do not constitute an all-taxon pole census or universal molecular mechanism. |
| pole-agent-doi-mbc.E17-06-0397 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1091/mbc.E17-06-0397; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies The molecular architecture of the yeast spindle pole body core determined by Bayesian integrative modeling. Authors: Viswanath S, Bonomi M, Kim SJ, Klenchin VA, Taylor KC, Yabut KC, Umbreit NT, Van Epps HA, Meehl J, Jones MH, Russel D, Velazquez-Muriel JA, Winey M, Rayment I, Davis TN, Sali A, Muller EG.; PMID 28814505; DOI 10.1091/mbc.e17-06-0397. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| schema-result | just validate data/structures/cytoskeleton/spindle_pole.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/spindle_pole.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/spindle_pole.yaml --out /private/tmp/cellstructure-batch16-20261021-fjx428vi/spindle_pole-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/spindle_pole.yaml --out /private/tmp/cellstructure-batch16-20261021-fjx428vi/spindle_pole-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch16-20261021-fjx428vi/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch16-20261021-fjx428vi/spindle_pole-strict.tsv |
| target-curies-result | just check-curies-strict; data/structures/cytoskeleton/spindle_pole.yaml; exact native collect() target slice of original fresh-base TSV | supports | 12 of 12 exact target identifiers returned OK. No target residuals. The shared command exit zero is not interpreted as successful network resolution for transport failures. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Jaspersen and Winey2004 is review-tier evidence read through the listed author-manuscript browser extracts, not a complete native publisher full-text download. Original captured times/hashes are retained; legacy status200 on one extraction does not attest to a native HTTP response.
- Viswanath2017 is used for its Introduction/Figure1 yeast-SPB structural context. No claim of a full Results audit, all-eukaryote census or primary proof for every introductory statement is made.
- Native ontology and source texts support generic identity and a yeast reference system; they do not establish universal MTOC/gamma-complex assembly necessity or the full listed molecular cohort throughout microbial eukaryotes. No counterexample to component necessity is invented from the word usually alone.
- The record contains no exact protein examples, images or source-specific complex import requiring separate protein or image-license checks. The generic gamma-complex mapping is deliberately retained; no universal ring geometry follows from it.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- All12 fresh batch16 inspection input hashes verified; focused schema and strict-reference gates passed.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T094825Z-spindle-pole-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Spindle pole scope, gamma-complex identity and source review
started_at: '2026-10-21T09:24:39Z'
finished_at: '2026-10-21T09:48:25Z'
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
summary: Generic spindle-pole and gamma-complex identities and the yeast reference
  case are supported. One major source/taxon-scope issue and two minor synonym/graph-scope
  issues remain; assembly necessity is explicitly unverified.
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
  - path: data/structures/cytoskeleton/spindle_pole.yaml
    sha256: c456f99ee99fc90e9b8fcf99e303abddf46bfa0c9c0f473ec3059ed8a0044204
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
- target_id: GO:0000922
  path: data/structures/cytoskeleton/spindle_pole.yaml
  label: spindle pole
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_pole.yaml
    role: maintained scientific record
scope:
  description: Entire single target, native region/complex/process/taxon identities,
    source-specific SPB versus general-pole boundary, all component/function/graph
    claims and review-versus-primary evidence scope.
  selection: Tenth selected target in batch sixteen, fixed maintained-path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0000922
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0000922
  command: just validate data/structures/cytoskeleton/spindle_pole.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0000922
  command: just validate-strict data/structures/cytoskeleton/spindle_pole.yaml --out
    /private/tmp/cellstructure-batch16-20261021-fjx428vi/spindle_pole-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0000922
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - pole-agent-go
  - pole-agent-tax-2759
  - pole-agent-tax-4932
  - pole-agent-doi-annurev.cellbio.20.022003.114106
  - pole-agent-jaspersen-browser
  - pole-agent-jaspersen-duplication-browser
  - pole-agent-jaspersen-nucleation-browser
  - pole-agent-viswanath2017
  - pole-agent-doi-mbc.E17-06-0397
- check_id: target-curies
  name: Target resolver slice with native transport-failure cross-checks
  status: passed
  required: true
  target_ids:
  - GO:0000922
  summary: 12 of 12 exact target identifiers returned OK. No target residuals. The
    shared command exit zero is not interpreted as successful network resolution for
    transport failures.
  evidence_ids:
  - target-curies-result
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0000922
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
  - GO:0000922
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
  - GO:0000922
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
  - GO:0000922
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
  - GO:0000922
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
  reference: data/structures/cytoskeleton/spindle_pole.yaml
  locator: Entire maintained YAML including all imported participants, component examples,
    functions, graph edges, discussions and history
  accessed_at: '2026-10-21T09:37:04Z'
  support: context_only
  summary: All fields were read after fresh native inspection; the maintained target
    and PROPOSED state are unchanged.
- evidence_id: policy
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, CausalNode and source-specific ComplexComposition
    contracts; essentiality definition; docs/CURATION.md assembly-versus-function
    guidance and review checklist
  accessed_at: '2026-10-21T09:37:04Z'
  support: context_only
  summary: Component family identity, concrete protein identity and source-specific
    assembly membership are separate. Essentiality asks whether the structure forms
    without the component; membership and activity do not establish it. Optional fields
    are not mandatory. CausalNode permits protein complexes; its xrefs contract does
    not inherit the top-level record equivalence restriction.
- evidence_id: pole-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000226,GO:0000922,GO:0000930,GO:0005815,GO:0005816,GO:0005819,GO:0051225,GO:0110165
  locator: 'All returned term identities, definitions, synonym annotations and relevant
    child relations: GO:0000226, GO:0000922, GO:0000930, GO:0005815, GO:0005816, GO:0005819,
    GO:0051225, GO:0110165. GO0000922 supplies no synonym annotation in this response.'
  accessed_at: '2026-10-21T09:26:00.491089Z'
  support: supports
  summary: Native definitions distinguish the target structure, its returned related
    structural classes and relevant processes. Exact returned synonyms and source-specific
    relations were checked separately from plausible curator-authored language.
  snapshot_sha256: a1e41b4887689d9747ff0d411edf75471105dc608579a4a7f7ee69d47dd59cc1
- evidence_id: pole-agent-tax-2759
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759
  locator: Complete taxon identity, rank and lineage
  accessed_at: '2026-10-21T09:26:00.598634Z'
  support: supports
  summary: Native taxonomy confirms the named organism and rank; broad clade occurrence
    is separate from a molecular mechanism established in one yeast.
  snapshot_sha256: 47d02c524bbdc511eb1fc377bdedc484b5cb6d3504611b0cbc6c280a65f140b4
- evidence_id: pole-agent-tax-4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete taxon identity, rank and lineage
  accessed_at: '2026-10-21T09:26:00.981577Z'
  support: supports
  summary: Native taxonomy confirms the named organism and rank; broad clade occurrence
    is separate from a molecular mechanism established in one yeast.
  snapshot_sha256: be57b95543b586448f6bd2889db42e91038e90ae2d12e8f654050c92af5b9087
- evidence_id: pole-agent-doi-annurev.cellbio.20.022003.114106
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1146/annurev.cellbio.20.022003.114106
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:26:01.224135Z'
  support: supports
  summary: 'Native metadata identifies The budding yeast spindle pole body: structure,
    duplication, and function. Authors: Jaspersen SL, Winey M.; PMID 15473833; DOI
    10.1146/annurev.cellbio.20.022003.114106. Bibliographic identity and available
    abstract only; not a substitute for inspected article body.'
  snapshot_sha256: efa766051d38f45bd9e4159bbbb7baf72a1958fd54dc81c63c488d70f1762d03
- evidence_id: pole-agent-jaspersen-browser
  kind: authority
  reference: https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function
  locator: 'Author-manuscript browser extraction, pages5–10, displayed lines185–410:
    Introduction, SPB organization and core components. This is captured browser text;
    legacy metadata status200 is not an independently recorded native HTTP response.'
  accessed_at: '2026-10-21T07:24:18Z'
  support: supports
  summary: Jaspersen and Winey2004 is a review focused on the budding-yeast SPB, its
    layered structure and nuclear/cytoplasmic microtubule organization. The author
    manuscript is review-tier context rather than primary experimental proof for all
    eukaryotic poles.
  snapshot_sha256: 8aa2398ded5512b2450c936e832c11bc46d77ac317e4c01a2f7a6b9f1a4fce4e
- evidence_id: pole-agent-jaspersen-duplication-browser
  kind: authority
  reference: https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function
  locator: 'Author-manuscript browser extraction: duplication/separation pages15–20,
    displayed lines619–705 and730–800; intervening omitted lines were not read.'
  accessed_at: '2026-10-21T07:40:49Z'
  support: supports
  summary: The review describes budding-yeast SPB duplication and bridge cleavage
    followed by Cin8/Kip1-dependent pole separation. This supports a scoped yeast
    pathway, not a uniform pole-duplication mechanism for every microbial eukaryote.
  snapshot_sha256: 4995a36ec89d47c8e1fe3cf967df63ac1f3c357d9e16d69dd2b01c22408b7d05
- evidence_id: pole-agent-jaspersen-nucleation-browser
  kind: authority
  reference: https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function
  locator: 'Author-manuscript browser extraction: pages24–26 displayed lines976–1077,
    and pages30–32 lines1213–1308. Read scope includes gamma-tubulin machinery and
    the SPB/centrosome comparison, not the entire review.'
  accessed_at: '2026-10-21T07:43:49.372408Z'
  support: supports
  summary: The review treats Tub4/Spc97/Spc98 nucleation complexes, Spc110/Spc72 targeting
    and comparison with centrosomes. Similarities coexist with structural and duplication
    differences; mechanistic models and inferred minus-end capping retain their stated
    uncertainty.
  snapshot_sha256: 5c038e01761413d522e0ea145ffefb28f289f6f2f5cc3b55c8deb377bf2aa0cf
- evidence_id: pole-agent-viswanath2017
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5687031.1/PMC5687031.1.xml
  locator: 'Native PMC5687031.1 JATS: complete Introduction including Figure1 caption.
    Additional initial Results were consulted but no conclusion here depends on a
    complete Results audit.'
  accessed_at: '2026-10-20T07:38:52.830471Z'
  support: supports
  summary: Viswanath et al.2017 provides primary integrative structural work on the
    yeast SPB core. Its Introduction and Figure1 distinguish inner/outer plaques and
    gamma-TuSC assemblies; these contextual claims do not constitute an all-taxon
    pole census or universal molecular mechanism.
  snapshot_sha256: 004836a027b7fad21def4f6e9eebc94ec5f1e07679d123407a062241f6edb580
- evidence_id: pole-agent-doi-mbc.E17-06-0397
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1091/mbc.E17-06-0397
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:26:01.178870Z'
  support: supports
  summary: 'Native metadata identifies The molecular architecture of the yeast spindle
    pole body core determined by Bayesian integrative modeling. Authors: Viswanath
    S, Bonomi M, Kim SJ, Klenchin VA, Taylor KC, Yabut KC, Umbreit NT, Van Epps HA,
    Meehl J, Jones MH, Russel D, Velazquez-Muriel JA, Winey M, Rayment I, Davis TN,
    Sali A, Muller EG.; PMID 28814505; DOI 10.1091/mbc.e17-06-0397. Bibliographic
    identity and available abstract only; not a substitute for inspected article body.'
  snapshot_sha256: cffb3902bb3dc1c67a795170c81ecde54b141b008060bb39765e59b8148ed66f
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/spindle_pole.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:24:44Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/spindle_pole.yaml'
  snapshot_sha256: 20c38be7819ad345b753ab9bfeec433d5f9cad333b8884f12d1d5296e6cc9bfd
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/spindle_pole.yaml --out
    /private/tmp/cellstructure-batch16-20261021-fjx428vi/spindle_pole-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:24:47Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/spindle_pole.yaml\
    \ --out /private/tmp/cellstructure-batch16-20261021-fjx428vi/spindle_pole-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch16-20261021-fjx428vi/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch16-20261021-fjx428vi/spindle_pole-strict.tsv"
  snapshot_sha256: a83c6d714e5246d1f44361b61f80a0f7670be7c18fc29237c6b75779e48cbaf2
- evidence_id: target-curies-result
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/spindle_pole.yaml; exact native collect()
    target slice of original fresh-base TSV
  accessed_at: '2026-10-21T09:48:00.673425Z'
  support: supports
  summary: 12 of 12 exact target identifiers returned OK. No target residuals. The
    shared command exit zero is not interpreted as successful network resolution for
    transport failures.
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
  topic: Generic pole is broader than a spindle pole body
  outcome: supported
  target_ids:
  - GO:0000922
  summary: The target is the polar spindle region, with spindle parthood and a species-specific
    SPB structural example. It is not equated to only the budding-yeast SPB. The native
    definition says it usually contains an MTOC; the record distribution also acknowledges
    acentrosomal poles.
  evidence_ids:
  - pole-agent-go
  - pole-agent-jaspersen-browser
  - pole-agent-tax-2759
  - pole-agent-tax-4932
  - record
- assessment_id: gamma-complex
  area: grounding
  topic: GO0000930 correctly covers generic gamma-tubulin complexes
  outcome: supported
  target_ids:
  - GO:0000922
  summary: The component label and role explicitly cover gamma-TuSC/gamma-TuRC. Native
    GO0000930 is the generic gamma-tubulin complex with species-variable partners;
    its small-complex and ring-complex children must not be confused with the parent.
    This mapping does not assert that every complex has universal ring geometry or
    the same subunits.
  evidence_ids:
  - pole-agent-go
  - pole-agent-jaspersen-nucleation-browser
  - pole-agent-viswanath2017
  - record
  - policy
- assessment_id: molecular-scope
  area: evidence
  topic: The broad pole definition adds a source-unmatched molecular roster
  outcome: concern
  target_ids:
  - GO:0000922
  summary: The appended text combines kinesin-14, NuMA/Pkl1/Mto1 and gamma-tubulin-ring
    machinery across yeasts, fungi, microalgae and protists. GO supplies the generic
    regional definition, while Jaspersen is a yeast-SPB review with a centrosome comparison.
    Its readable sections and Viswanath core context do not establish that entire
    named combination throughout those groups.
  evidence_ids:
  - pole-agent-go
  - pole-agent-jaspersen-browser
  - pole-agent-jaspersen-duplication-browser
  - pole-agent-jaspersen-nucleation-browser
  - pole-agent-viswanath2017
  - record
- assessment_id: duplication-scope
  area: scope
  topic: Keep yeast pole-duplication evidence at its actual scope
  outcome: concern
  target_ids:
  - GO:0000922
  summary: The review supports budding-yeast SPB duplication, bridge cleavage and
    Cin8/Kip1-dependent separation. Its centrosome comparison explicitly preserves
    similarities and differences. The record evidence notes generalize this to spindle-pole
    duplication across eukaryotes, including the acentrosomal scope it otherwise acknowledges,
    without matching evidence.
  evidence_ids:
  - pole-agent-jaspersen-duplication-browser
  - pole-agent-jaspersen-nucleation-browser
  - pole-agent-jaspersen-browser
  - record
- assessment_id: assembly-necessity
  area: evidence
  topic: Presence and nucleation do not establish universal assembly necessity
  outcome: unknown
  target_ids:
  - GO:0000922
  summary: Both components are ESSENTIAL. Source evidence for yeast MTOC organization
    and gamma-complex nucleation supports membership/function in that system, but
    does not show that the broad spindle-pole structure fails to form without each
    generic component across its taxonomic scope. The schema criterion is formation,
    not catalytic function, cell viability or presence in the intact reference architecture.
  evidence_ids:
  - pole-agent-go
  - pole-agent-jaspersen-browser
  - pole-agent-jaspersen-nucleation-browser
  - pole-agent-viswanath2017
  - record
  - policy
- assessment_id: taxonomy-example
  area: scope
  topic: Broad occurrence and canonical yeast architecture
  outcome: supported
  target_ids:
  - GO:0000922
  summary: Eukaryota and S.cerevisiae labels/ranks are correct; the yeast canonical
    SPB architecture example is supported. COMMON is not treated as a measured prevalence.
    The broad terminal-region identity does not authorize exporting the exact yeast
    molecular or duplication mechanism to every eukaryote.
  evidence_ids:
  - pole-agent-go
  - pole-agent-tax-2759
  - pole-agent-tax-4932
  - pole-agent-jaspersen-browser
  - pole-agent-viswanath2017
  - record
- assessment_id: synonym
  area: provenance
  topic: GO does not supply the maintained narrow synonym
  outcome: concern
  target_ids:
  - GO:0000922
  summary: Native GO0000922 contains no synonym annotation in the inspected response.
    Mitotic spindle pole is a plausible narrower phrase, but its GO source attribution
    is unsupported and should be repaired rather than mistaken for a source-provided
    synonym.
  evidence_ids:
  - pole-agent-go
  - record
- assessment_id: graph
  area: graph
  topic: Organizational description lacks a represented causal transition
  outcome: concern
  target_ids:
  - GO:0000922
  summary: The graph links MTOC/gamma-complex/SPB parts and whole-pole functions.
    Its text describes nucleation/anchoring and duplication, but the edges do not
    represent those transitions or the component-to-function dependency. Keep supported
    topology distinct from the stronger MECHANISTIC scope claim.
  evidence_ids:
  - pole-agent-go
  - pole-agent-jaspersen-browser
  - pole-agent-jaspersen-duplication-browser
  - pole-agent-jaspersen-nucleation-browser
  - policy
  - record
- assessment_id: completeness
  area: completeness
  topic: No forced molecular census for a generic polar region
  outcome: supported
  target_ids:
  - GO:0000922
  summary: The two class-level components have valid identities. Exact protein examples,
    stoichiometry, family splitting and full centrosome/SPB inventories are optional.
    The material problem is unsupported broad mechanism, with assembly necessity explicitly
    unresolved; optional inventory is not promoted to a finding.
  evidence_ids:
  - pole-agent-go
  - pole-agent-jaspersen-browser
  - pole-agent-jaspersen-nucleation-browser
  - policy
  - record
findings:
- finding_id: F1
  issue_key: spindle-pole-mechanism-taxonomic-source-inflation
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Bound the specific pole mechanism and duplication claims to their evidence
  description: The definition adds a combined kinesin-14/NuMA/Pkl1/Mto1/gamma-ring
    mechanism across broad microbial eukaryote groups while citing only the generic
    GO definition. The function and graph evidence further say the yeast-focused review
    establishes pole duplication/separation across eukaryotes. The inspected review
    and primary yeast-core context support narrower claims; neither establishes this
    whole combined generalization.
  target_ids:
  - GO:0000922
  field_paths:
  - definition
  - definition_source
  - functions[function_id=bipolar_spindle_assembly]
  - causal_graphs[graph_id=spindle_pole_mechanism].nodes[node_id=bipolar_spindle_assembly]
  - causal_graphs[graph_id=spindle_pole_mechanism].edges[subject=spindle_pole,predicate=mediates,object=bipolar_spindle_assembly]
  evidence_ids:
  - pole-agent-go
  - pole-agent-jaspersen-browser
  - pole-agent-jaspersen-duplication-browser
  - pole-agent-jaspersen-nucleation-browser
  - pole-agent-viswanath2017
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_pole.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: major
  normalization_reason: This is molecular and taxonomic scope inflation affecting
    the stated causal mechanism. Generic spindle-pole and gamma-complex identities
    remain correct.
- finding_id: F2
  issue_key: spindle-pole-narrow-synonym-go-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Repair the source attribution of the narrow pole synonym
  description: The phrase mitotic spindle pole is labeled a GO0000922 narrow synonym,
    but the native term does not supply that synonym. Preserve it only with an appropriate
    independent source/curator provenance or use the source-provided annotations.
  target_ids:
  - GO:0000922
  field_paths:
  - synonyms[synonym_text=mitotic spindle pole]
  evidence_ids:
  - pole-agent-go
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_pole.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: minor
  normalization_reason: The phrase is a plausible narrowing and does not change target
    identity; the defect is a bounded source-provenance claim.
- finding_id: F3
  issue_key: spindle_pole_mechanism-static-graph-scope
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Match graph scope to the represented relationships
  description: The FUNCTION graph contains structural parthood and whole-structure-to-process
    mediates edges. Its descriptions mention biological activities, but the graph
    does not connect an explicit assembly or functional transition to those activities.
    MECHANISTIC overstates what is represented; this is a scope classification concern,
    not a claim that the supported topology is false or a demand for atomic detail.
  target_ids:
  - GO:0000922
  field_paths:
  - causal_graphs[graph_id=spindle_pole_mechanism].scope_status
  - causal_graphs[graph_id=spindle_pole_mechanism].scope_notes
  - causal_graphs[graph_id=spindle_pole_mechanism].edges
  evidence_ids:
  - pole-agent-go
  - pole-agent-jaspersen-browser
  - pole-agent-jaspersen-duplication-browser
  - pole-agent-jaspersen-nucleation-browser
  - policy
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_pole.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: minor
  normalization_reason: The identities and many relationships remain useful. The bounded
    correction concerns the promised explanatory scope, not biological identity or
    missing optional components.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0000922
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_pole.yaml
    role: maintained scientific record
  description: During authorized curation, retain the generic regional definition
    and qualify named molecular/duplication mechanisms to directly supported organisms
    and spindle stages, or supply inspected sources covering the broader assertion.
  acceptance_checks:
  - Preserve the difference between a spindle pole, yeast SPB, centrosome and acentrosomal
    pole.
  - Retain GO0000930 for the generic gamma-complex class; do not replace it with a
    falsely universal ring-only identity.
  - Do not describe review synthesis as primary experimental proof.
  - Resolve component assembly necessity separately from nucleation activity.
  - Run focused schema, strict-reference and causal-graph checks.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0000922
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_pole.yaml
    role: maintained scientific record
  description: During authorized curation, correct the source for the added phrase
    rather than treating plausible wording as a native GO annotation.
  acceptance_checks:
  - Verify the exact source string and synonym scope.
  - Do not invent an ontology synonym when the response contains none.
  - Run focused schema and strict-reference checks.
- action_id: A3
  finding_ids:
  - F3
  target_ids:
  - GO:0000922
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_pole.yaml
    role: maintained scientific record
  description: During authorized curation, mark the current descriptive graph NONMECHANISTIC
    with a clear scope note, or represent a specific source-supported transition at
    an explicit organism and developmental scope.
  acceptance_checks:
  - Keep supported identity and parthood relationships.
  - Do not infer an assembly requirement merely from composition or localization.
  - Any added mechanistic edge must cite the source that actually establishes that
    transition.
  - Run focused schema, strict-reference and causal-graph validation.
limitations:
- Jaspersen and Winey2004 is review-tier evidence read through the listed author-manuscript
  browser extracts, not a complete native publisher full-text download. Original captured
  times/hashes are retained; legacy status200 on one extraction does not attest to
  a native HTTP response.
- Viswanath2017 is used for its Introduction/Figure1 yeast-SPB structural context.
  No claim of a full Results audit, all-eukaryote census or primary proof for every
  introductory statement is made.
- Native ontology and source texts support generic identity and a yeast reference
  system; they do not establish universal MTOC/gamma-complex assembly necessity or
  the full listed molecular cohort throughout microbial eukaryotes. No counterexample
  to component necessity is invented from the word usually alone.
- The record contains no exact protein examples, images or source-specific complex
  import requiring separate protein or image-license checks. The generic gamma-complex
  mapping is deliberately retained; no universal ring geometry follows from it.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- All12 fresh batch16 inspection input hashes verified; focused schema and strict-reference
  gates passed.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
