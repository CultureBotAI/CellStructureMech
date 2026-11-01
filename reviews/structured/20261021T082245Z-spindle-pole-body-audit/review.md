# spindle pole body identity, source and composition review

- Review: 20261021T082245Z-spindle-pole-body-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T08:09:21Z
- Finished UTC: 2026-10-21T08:22:45Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The whole-SPB identity, budding-yeast functions and descriptive duplication graph are supported. One minor curation issue remains: the existing general gamma-tubulin-complex component has an exact available GO grounding despite its label-only status.

## Scope And Provenance

Entire single target; every asserted stable identifier and citation; native authority definitions; cited review passages and claim-bearing primary source text; graph and composition boundaries.

Selection: Seventh selected path in batch eleven, following fixed repository path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0005816 | data/structures/cytoskeleton/spindle_pole_body.yaml | maintained | spindle pole body |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0005816 | Focused validator passed. |
| Focused native strict | passed | True | GO:0005816 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0005816 | 4 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | GO:0005816 | No expression module or transcriptional-regulator claim is asserted; structural composition and localization are assessed from structural sources. |
| Claim-level scientific review | passed | True | GO:0005816 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0005816 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0005816 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0005816 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0005816 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0005816 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Whole fungal MTOC and exact GO identity

identity: supported. Targets: GO:0005816.

The identifier, definition and SPB synonym exactly match active GO0005816. The bounded budding-yeast example does not contradict the broader fungal class definition. The target is a multiprotein organelle, not a single protein or duplication-stage intermediate.

### Whole organelle and subassembly boundaries

scope: supported. Targets: GO:0005816.

No incorrect is-a or part_of links are asserted. The two components are bounded to core scaffold and gamma-tubulin nucleation complexes. CPX1420 is only IL2; CPX1198 is only an organism-specific gamma-TuSC and neither is a whole-record equivalent.

### Available exact general complex grounding

grounding: concern. Targets: GO:0005816.

The core component is properly retained as a heterogeneous scaffold aggregate. However, the existing broad gamma-tubulin-complex component has an exact active GO0000930 match. Its REVIEWED_LABEL_ONLY state and explanation defer narrower fungal small/ring identifiers while overlooking the already appropriate general class. This is a bounded grounding defect in an asserted component, not a demand to populate optional protein examples or fixed source compositions.

### Nuclear/cytoplasmic nucleation and bipolar spindle assembly

evidence: supported. Targets: GO:0005816.

The review and primary structural context support the SPB as a microtubule organizing center on both faces. Duplication and separation provide the two poles for the mitotic spindle; the record does not claim isolated-core sufficiency, universal individual-protein essentiality or an autonomous gamma-TuSC mechanism.

### Descriptive old-to-new assembly topology

graph: supported. Targets: GO:0005816.

The ASSEMBLY graph expressly marked NONMECHANISTIC represents formation of a neighboring SPB at the half bridge. Its templates-assembly edge is supported at this positional/topological level and does not assert transfer of particular old-pole proteins, strict conservative inheritance, or a fully resolved molecular sequence.

### Integrative model experimental boundaries

scope: supported. Targets: GO:0005816.

The 2017 model addresses CP/IL2 and portions of layer-spanning proteins. K. lactis calmodulin supplied a crystal constraint, while in vivo FRET concerns S. cerevisiae. The initial two-layer Spc29 model was rejected by tagged EM; the final reduced core stoichiometry and possible peripheral Spc29 pool are modeling interpretations. None is promoted into a quantitative record assertion.

### Optional inventory and measurements

completeness: supported. Targets: GO:0005816.

The acknowledged subassembly TODO is useful. No image, fixed dimension, copy count or constituent protein example is asserted. Additional plaque, half-bridge or protein rows are optional enrichments; the observed issue is restricted to an exact grounding for the already-present general gamma-tubulin-complex row.

### Source identities, tiers and access

provenance: supported. Targets: GO:0005816.

Both cited DOI identities are verified. The 2004 source is a review read as browser-extracted author manuscript; the 2017 source is primary integrative work read as native JATS. Reused source receipts keep their original timestamps and hashes, without adopting inherited browser status200 as native HTTP proof.

### Maintained record and scientific status

ownership: supported. Targets: GO:0005816.

The maintained structure YAML owns future curation. No generated page, mapping status, scientific history or repository history has been changed. Native schema and strict checks passed; these checks do not substitute for source review.

## Findings

### F1: The existing gamma-tubulin complex class has an exact GO grounding

minor / open / confirmed; issue key: spindle-pole-body-gamma-tubulin-complex-grounding.

The component gamma_tubulin_complexes is REVIEWED_LABEL_ONLY, with notes deferring exact fungal small-complex or plaque-bound ring-complex identifiers. Native GO0000930 directly denotes the general multiprotein gamma-tubulin complex class already asserted by this component; its definition includes MTOC localization and nucleation, and its children distinguish small and ring complexes. Ground this existing broad row to GO:0000930, or document a concrete narrower scope mismatch if the intended row changes. This does not require species-specific CPX composition, an exhaustive inventory, or replacement of the heterogeneous core component.

## Recommended Actions And Acceptance Checks

### A1

In later authorized curation, add GO:0000930 to the existing gamma-tubulin-complex component and align grounding_status/notes with the verified general class. Preserve the specific small/ring and plaque-assembly limitations; do not equate a species-specific CPX entry with the whole SPB. Preserve historical discussion rationale and record any current progress in notes.

- Compare the revised component scope against the active GO0000930 definition and its small/ring subtypes.
- Retain the supported nuclear/cytoplasmic nucleation-site role without adding autonomous nucleation sufficiency or universal stoichiometry.
- Run native schema, strict, label, history and generated-page checks after maintained-record curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/spindle_pole_body.yaml; Entire maintained YAML including all history, claims, evidence, discussions and graph | context_only | The entire target was read before assessment; the record remains PROPOSED and no maintained content is changed. |
| policy | docs/CURATION.md; Identifiers, Components, Evidence and scientific-status rules | context_only | GO identifies an exact structural class when available. REVIEWED_LABEL_ONLY requires justification that no exact term is available. Optional component lists and organism-specific complex inventories are not mandatory. |
| spb-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005816,GO:0032991,GO:0005825,GO:0008274,GO:0008275,GO:0000930; results selected by exact IDs; definition, isObsolete, synonyms and child relations; only the explicitly described returned definitions inform this review | supports | Native GO confirms active spindle pole body GO0005816, exact synonym SPB and fungal MTOC definition; GO0005825 is the distinct half bridge and an explicit part_of child of GO0005816. GO0032991 denotes protein-containing complex. GO0000930 is the general gamma-tubulin complex class, with small and ring subtypes GO0008275 and GO0000931. |
| spb-agent-taxon | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; taxId, scientificName, rank and lineage | supports | NCBITaxon4932 is Saccharomyces cerevisiae at species rank. The record does not assert a particular experimental strain or quantitative prevalence. |
| spb-agent-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1146/annurev.cellbio.20.022003.114106%22%20OR%20DOI%3A%2210.1091/mbc.E17-06-0397%22%20OR%20DOI%3A%2210.1083/jcb.145.4.809%22%20OR%20DOI%3A%2210.1534/genetics.111.128710%22; Four native resultList.result entries: DOI, title, authorString, pubYear, PMID, PMCID, abstractText and pubTypeList | supports | Exact citation identities are verified: Jaspersen/Winey2004 PMID15473833; Viswanath2017 PMID28814505/PMC5687031; Adams/Kilmartin1999 PMID10330408/PMC2133189; Winey/Bloom2012 PMID22491889/PMC3316638. The 2004 and 2012 bodies synthesize previous work; generic database publication-type tags do not make the 2012 review a new experiment. |
| spb-agent-jaspersen-browser | https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function; Author-manuscript pp5–10; browser lines187–427. Exact JSON-serialized browser text, not native HTTP response bytes; inherited status200 metadata is not treated as verified HTTP status. | supports | The 2004 literature review describes budding-yeast nuclear-envelope SPBs with inner, central and outer plaques plus intermediate layers, an adjacent half bridge, and the protein scaffold connecting nuclear and cytoplasmic nucleation sites. This is a review, not a new localization experiment. |
| spb-agent-jaspersen-duplication-browser | https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function; Author-manuscript pp15–18, browser lines619–705 and730–743; Figure3 legend lines1418–1433. Browser-extracted text with original receipt retained, not publisher-PDF bytes. | supports | The review describes half-bridge elongation and distal cytoplasmic satellite deposition, expansion into a layered duplication plaque, then membrane insertion and nuclear-component assembly. It separately describes bridge severing and bipolar-spindle separation. Molecular bridge retraction and individual recruitment details remain models. |
| spb-agent-jaspersen-nucleation-browser | https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function; Author-manuscript pp24–26, browser lines978–1073; exact serialized browser response with no HTTP status supplied. | supports | The review distinguishes alpha/beta microtubule polymers from associated gamma-tubulin complexes. Tub4/Spc97/Spc98 complexes occupy both SPB faces via Spc110 or Spc72. Low nucleation by isolated soluble complexes is not evidence that each scaffold constituent autonomously nucleates microtubules. |
| spb-agent-viswanath2017 | https://pmc-oa-opendata.s3.amazonaws.com/PMC5687031.1/PMC5687031.1.xml; Native PMC OA S3 JATS for PMC5687031: Introduction/Figure1; Results Gathering of data, Representations and restraints, Initial models, The C-termini of Spc29 are in a single layer, Molecular architecture with reduced Spc29; Discussion; Methods Composition and stoichiometry, In vivo FRET, System representation. | supports | Primary Bayesian integrative modeling supports a CP/IL2 core scaffold built from portions of Spc42, Spc29, Spc110, Cmd1 and Cnm67. FRET, crystallography, SAXS, EM and genetic constraints are combined. The inferred Spc29 conformations and modeled copy ratio are not fixed whole-SPB stoichiometry; calmodulin cross-linking and Spc110 assembly remain proposed models. |
| spb-agent-CPX-1198 | https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-1198; complexAc, name, species, systematicName, participants, functions and properties; original receipt | context_only | Native CPX1198 denotes the Saccharomyces cerevisiae gamma-tubulin small complex (taxon559292), a species-specific assembly with Tub4/Spc97/Spc98 and nucleotide participants. It is a candidate subassembly rather than identity for the whole SPB or every gamma-tubulin complex. Its narrower scope is not needed to establish the GO0000930 match. |
| spb-agent-CPX-1420 | https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-1420; complexAc, name, species, systematicName and properties | context_only | CPX1420 denotes the Saccharomyces cerevisiae intermediate-layer-2 complex (taxon559292) with Spc42/Cnm67. Its scope does not identify the entire CP/IL2 core or whole SPB. |
| schema-result | just validate data/structures/cytoskeleton/spindle_pole_body.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/spindle_pole_body.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/spindle_pole_body.yaml --out /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/../spindle_pole_body-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/spindle_pole_body.yaml --out /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/../spindle_pole_body-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/../spindle_pole_body-strict.tsv |
| target-curies | just check-curies-strict; data/structures/cytoskeleton/spindle_pole_body.yaml; exact collect() scope; snapshot_sha256 hashes the entire original /private/tmp/cellstructure-record-reviews-UhRFh7/repo/reports/curie_check.tsv, not the derived resolver-slice.json | supports | 4 of 4 collected target identifiers returned OK at the unchanged base. Residuals: none. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- The 2004 review was read at claim-bearing structural, duplication and nucleation passages through browser text. Underlying historical studies and the complete review were not all independently reread.
- The 2017 primary main-text sections and relevant figure legends were read; no raw-model rerun, microscopy-pixel reanalysis or complete supplementary-data audit was performed.
- Model copy ratios, exact Spc29 conformation and proposed calmodulin domain swaps are not established as universal composition or direct in vivo mechanism.
- The optional whole-SPB constituent inventory and species-specific complex compositions remain incomplete. CPX1198/1420 are narrow candidates rather than whole-record equivalences.
- COMMON is qualitative occurrence in the characterized species, not measured prevalence across fungi or cells.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Native inspection preceded assessment. The complete target and claim-bearing source sections were read by the source collaborator; parent audit, finalization, shared checks and saving remain pending.
- The explicit user goal requests coverage of every selected target, including clean records; no issue is invented to justify a bundle.
- Unsaved review draft only. Maintained scientific records, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T082245Z-spindle-pole-body-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: spindle pole body identity, source and composition review
started_at: '2026-10-21T08:09:21Z'
finished_at: '2026-10-21T08:22:45Z'
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
summary: 'The whole-SPB identity, budding-yeast functions and descriptive duplication
  graph are supported. One minor curation issue remains: the existing general gamma-tubulin-complex
  component has an exact available GO grounding despite its label-only status.'
source:
  git_revision: 99692a3d5f16a7dcd6db7e3811344c299a977b81
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
  - path: data/structures/cytoskeleton/spindle_pole_body.yaml
    sha256: 50885e021c246e17e29beb27f7dc98e37ee4d34878648fea4fd8b565bbb2fc78
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
- target_id: GO:0005816
  path: data/structures/cytoskeleton/spindle_pole_body.yaml
  label: spindle pole body
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_pole_body.yaml
    role: maintained scientific record
scope:
  description: Entire single target; every asserted stable identifier and citation;
    native authority definitions; cited review passages and claim-bearing primary
    source text; graph and composition boundaries.
  selection: Seventh selected path in batch eleven, following fixed repository path
    order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0005816
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0005816
  command: just validate data/structures/cytoskeleton/spindle_pole_body.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0005816
  command: just validate-strict data/structures/cytoskeleton/spindle_pole_body.yaml
    --out /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/../spindle_pole_body-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0005816
  summary: 4 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0005816
  summary: No expression module or transcriptional-regulator claim is asserted; structural
    composition and localization are assessed from structural sources.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0005816
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - spb-agent-go
  - spb-agent-taxon
  - spb-agent-epmc
  - spb-agent-jaspersen-browser
  - spb-agent-jaspersen-duplication-browser
  - spb-agent-jaspersen-nucleation-browser
  - spb-agent-viswanath2017
  - spb-agent-CPX-1198
  - spb-agent-CPX-1420
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0005816
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch11 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0005816
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch11 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0005816
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch11 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0005816
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch11 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0005816
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch11 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/spindle_pole_body.yaml
  locator: Entire maintained YAML including all history, claims, evidence, discussions
    and graph
  accessed_at: '2026-10-21T08:14:28Z'
  support: context_only
  summary: The entire target was read before assessment; the record remains PROPOSED
    and no maintained content is changed.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Identifiers, Components, Evidence and scientific-status rules
  accessed_at: '2026-10-21T08:14:28Z'
  support: context_only
  summary: GO identifies an exact structural class when available. REVIEWED_LABEL_ONLY
    requires justification that no exact term is available. Optional component lists
    and organism-specific complex inventories are not mandatory.
- evidence_id: spb-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005816,GO:0032991,GO:0005825,GO:0008274,GO:0008275,GO:0000930
  locator: results selected by exact IDs; definition, isObsolete, synonyms and child
    relations; only the explicitly described returned definitions inform this review
  accessed_at: '2026-10-21T08:10:26.048714Z'
  support: supports
  summary: Native GO confirms active spindle pole body GO0005816, exact synonym SPB
    and fungal MTOC definition; GO0005825 is the distinct half bridge and an explicit
    part_of child of GO0005816. GO0032991 denotes protein-containing complex. GO0000930
    is the general gamma-tubulin complex class, with small and ring subtypes GO0008275
    and GO0000931.
  snapshot_sha256: 0351bb754bafd4c13ddd0abfa8da47ccb2146941d3c3457e7f28ce368ed12bc8
- evidence_id: spb-agent-taxon
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: taxId, scientificName, rank and lineage
  accessed_at: '2026-10-21T07:43:25.788893Z'
  support: supports
  summary: NCBITaxon4932 is Saccharomyces cerevisiae at species rank. The record does
    not assert a particular experimental strain or quantitative prevalence.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: spb-agent-epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1146/annurev.cellbio.20.022003.114106%22%20OR%20DOI%3A%2210.1091/mbc.E17-06-0397%22%20OR%20DOI%3A%2210.1083/jcb.145.4.809%22%20OR%20DOI%3A%2210.1534/genetics.111.128710%22
  locator: 'Four native resultList.result entries: DOI, title, authorString, pubYear,
    PMID, PMCID, abstractText and pubTypeList'
  accessed_at: '2026-10-21T08:10:26.049286Z'
  support: supports
  summary: 'Exact citation identities are verified: Jaspersen/Winey2004 PMID15473833;
    Viswanath2017 PMID28814505/PMC5687031; Adams/Kilmartin1999 PMID10330408/PMC2133189;
    Winey/Bloom2012 PMID22491889/PMC3316638. The 2004 and 2012 bodies synthesize previous
    work; generic database publication-type tags do not make the 2012 review a new
    experiment.'
  snapshot_sha256: 86b296e6c25eed0e77d9474c794a5530abcb91f16f6382f1edf182501bb42345
- evidence_id: spb-agent-jaspersen-browser
  kind: authority
  reference: https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function
  locator: Author-manuscript pp5–10; browser lines187–427. Exact JSON-serialized browser
    text, not native HTTP response bytes; inherited status200 metadata is not treated
    as verified HTTP status.
  accessed_at: '2026-10-21T07:24:18Z'
  support: supports
  summary: The 2004 literature review describes budding-yeast nuclear-envelope SPBs
    with inner, central and outer plaques plus intermediate layers, an adjacent half
    bridge, and the protein scaffold connecting nuclear and cytoplasmic nucleation
    sites. This is a review, not a new localization experiment.
  snapshot_sha256: 8aa2398ded5512b2450c936e832c11bc46d77ac317e4c01a2f7a6b9f1a4fce4e
- evidence_id: spb-agent-jaspersen-duplication-browser
  kind: authority
  reference: https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function
  locator: Author-manuscript pp15–18, browser lines619–705 and730–743; Figure3 legend
    lines1418–1433. Browser-extracted text with original receipt retained, not publisher-PDF
    bytes.
  accessed_at: '2026-10-21T07:40:49Z'
  support: supports
  summary: The review describes half-bridge elongation and distal cytoplasmic satellite
    deposition, expansion into a layered duplication plaque, then membrane insertion
    and nuclear-component assembly. It separately describes bridge severing and bipolar-spindle
    separation. Molecular bridge retraction and individual recruitment details remain
    models.
  snapshot_sha256: 4995a36ec89d47c8e1fe3cf967df63ac1f3c357d9e16d69dd2b01c22408b7d05
- evidence_id: spb-agent-jaspersen-nucleation-browser
  kind: authority
  reference: https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function
  locator: Author-manuscript pp24–26, browser lines978–1073; exact serialized browser
    response with no HTTP status supplied.
  accessed_at: '2026-10-21T07:43:49.372408Z'
  support: supports
  summary: The review distinguishes alpha/beta microtubule polymers from associated
    gamma-tubulin complexes. Tub4/Spc97/Spc98 complexes occupy both SPB faces via
    Spc110 or Spc72. Low nucleation by isolated soluble complexes is not evidence
    that each scaffold constituent autonomously nucleates microtubules.
  snapshot_sha256: 5c038e01761413d522e0ea145ffefb28f289f6f2f5cc3b55c8deb377bf2aa0cf
- evidence_id: spb-agent-viswanath2017
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5687031.1/PMC5687031.1.xml
  locator: 'Native PMC OA S3 JATS for PMC5687031: Introduction/Figure1; Results Gathering
    of data, Representations and restraints, Initial models, The C-termini of Spc29
    are in a single layer, Molecular architecture with reduced Spc29; Discussion;
    Methods Composition and stoichiometry, In vivo FRET, System representation.'
  accessed_at: '2026-10-20T07:38:52.830471Z'
  support: supports
  summary: Primary Bayesian integrative modeling supports a CP/IL2 core scaffold built
    from portions of Spc42, Spc29, Spc110, Cmd1 and Cnm67. FRET, crystallography,
    SAXS, EM and genetic constraints are combined. The inferred Spc29 conformations
    and modeled copy ratio are not fixed whole-SPB stoichiometry; calmodulin cross-linking
    and Spc110 assembly remain proposed models.
  snapshot_sha256: 004836a027b7fad21def4f6e9eebc94ec5f1e07679d123407a062241f6edb580
- evidence_id: spb-agent-CPX-1198
  kind: database
  reference: https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-1198
  locator: complexAc, name, species, systematicName, participants, functions and properties;
    original receipt
  accessed_at: '2026-10-21T07:24:55.987262Z'
  support: context_only
  summary: Native CPX1198 denotes the Saccharomyces cerevisiae gamma-tubulin small
    complex (taxon559292), a species-specific assembly with Tub4/Spc97/Spc98 and nucleotide
    participants. It is a candidate subassembly rather than identity for the whole
    SPB or every gamma-tubulin complex. Its narrower scope is not needed to establish
    the GO0000930 match.
  snapshot_sha256: f05394b9065d166f761d6fd535af76985428be3b25a84eeed670e3c530221d6f
- evidence_id: spb-agent-CPX-1420
  kind: database
  reference: https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-1420
  locator: complexAc, name, species, systematicName and properties
  accessed_at: '2026-10-21T07:24:55.987399Z'
  support: context_only
  summary: CPX1420 denotes the Saccharomyces cerevisiae intermediate-layer-2 complex
    (taxon559292) with Spc42/Cnm67. Its scope does not identify the entire CP/IL2
    core or whole SPB.
  snapshot_sha256: 629216f46c134e503436c972d2879084e6065dce79a71fd68113f650ce6cca4c
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/spindle_pole_body.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:09:22Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/spindle_pole_body.yaml'
  snapshot_sha256: 9460852f77a705fe15be3e30a0f3c9934dcfd46aa88d1d6d6d51ace1a71df7a9
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/spindle_pole_body.yaml
    --out /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/../spindle_pole_body-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:09:24Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/spindle_pole_body.yaml\
    \ --out /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/../spindle_pole_body-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/../spindle_pole_body-strict.tsv"
  snapshot_sha256: 8cfc27ab701bc14df0bd27908364d52c7064b918fa63fa49a9b6dc4d81fed189
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/spindle_pole_body.yaml; exact collect() scope;
    snapshot_sha256 hashes the entire original /private/tmp/cellstructure-record-reviews-UhRFh7/repo/reports/curie_check.tsv,
    not the derived resolver-slice.json
  accessed_at: '2026-10-21T08:14:28Z'
  support: supports
  summary: '4 of 4 collected target identifiers returned OK at the unchanged base.
    Residuals: none. Source-native identity checked separately.'
  snapshot_sha256: 68d64e4e86437df228658f43be4d47b41054fe882fedf357e660293691a0a061
- evidence_id: global-qc-result
  kind: validation
  reference: just qc
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec
  accessed_at: '2026-10-19T07:38:12Z'
  support: supports
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  snapshot_sha256: 7b6165ba8532d080a336f7a5a4c29b456fdf7182dd596410b700dfe60af61a06
- evidence_id: global-history-result
  kind: validation
  reference: just validate-history
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0
  accessed_at: '2026-10-19T07:29:37Z'
  support: supports
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  snapshot_sha256: b98e3eecd58a81fa46033e6baca6977811a439f119b943fd5d9931964adb2680
- evidence_id: global-products-result
  kind: validation
  reference: just validate-products
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad
  accessed_at: '2026-10-19T07:32:39Z'
  support: supports
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  snapshot_sha256: 2a1330c26aac5bd248a2fd3a3a7b9c882d2b3bb202365c555e5d6415d1c2203d
- evidence_id: global-traits-result
  kind: validation
  reference: just check-trait-links --check
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad
  accessed_at: '2026-10-19T07:29:45Z'
  support: supports
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  snapshot_sha256: 6eab64b59433928ec8e0df9b0046dbccf479c84bb0911c315feebc344d536007
- evidence_id: global-curies-result
  kind: validation
  reference: just check-curies-strict
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4
  accessed_at: '2026-10-19T08:04:01Z'
  support: supports
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  snapshot_sha256: 7cb413edccc92ee6ce79a32cd2b96a59bc4da37f2cb7b326eaca51a64f723cfb
assessments:
- assessment_id: identity
  area: identity
  topic: Whole fungal MTOC and exact GO identity
  outcome: supported
  target_ids:
  - GO:0005816
  summary: The identifier, definition and SPB synonym exactly match active GO0005816.
    The bounded budding-yeast example does not contradict the broader fungal class
    definition. The target is a multiprotein organelle, not a single protein or duplication-stage
    intermediate.
  evidence_ids:
  - spb-agent-go
  - spb-agent-taxon
  - spb-agent-jaspersen-browser
  - record
- assessment_id: hierarchy
  area: scope
  topic: Whole organelle and subassembly boundaries
  outcome: supported
  target_ids:
  - GO:0005816
  summary: No incorrect is-a or part_of links are asserted. The two components are
    bounded to core scaffold and gamma-tubulin nucleation complexes. CPX1420 is only
    IL2; CPX1198 is only an organism-specific gamma-TuSC and neither is a whole-record
    equivalent.
  evidence_ids:
  - spb-agent-go
  - spb-agent-viswanath2017
  - spb-agent-CPX-1198
  - spb-agent-CPX-1420
  - record
- assessment_id: composition
  area: grounding
  topic: Available exact general complex grounding
  outcome: concern
  target_ids:
  - GO:0005816
  summary: The core component is properly retained as a heterogeneous scaffold aggregate.
    However, the existing broad gamma-tubulin-complex component has an exact active
    GO0000930 match. Its REVIEWED_LABEL_ONLY state and explanation defer narrower
    fungal small/ring identifiers while overlooking the already appropriate general
    class. This is a bounded grounding defect in an asserted component, not a demand
    to populate optional protein examples or fixed source compositions.
  evidence_ids:
  - spb-agent-go
  - spb-agent-jaspersen-nucleation-browser
  - spb-agent-CPX-1198
  - record
  - policy
- assessment_id: functions
  area: evidence
  topic: Nuclear/cytoplasmic nucleation and bipolar spindle assembly
  outcome: supported
  target_ids:
  - GO:0005816
  summary: The review and primary structural context support the SPB as a microtubule
    organizing center on both faces. Duplication and separation provide the two poles
    for the mitotic spindle; the record does not claim isolated-core sufficiency,
    universal individual-protein essentiality or an autonomous gamma-TuSC mechanism.
  evidence_ids:
  - spb-agent-jaspersen-browser
  - spb-agent-jaspersen-duplication-browser
  - spb-agent-jaspersen-nucleation-browser
  - spb-agent-viswanath2017
  - record
- assessment_id: graph
  area: graph
  topic: Descriptive old-to-new assembly topology
  outcome: supported
  target_ids:
  - GO:0005816
  summary: The ASSEMBLY graph expressly marked NONMECHANISTIC represents formation
    of a neighboring SPB at the half bridge. Its templates-assembly edge is supported
    at this positional/topological level and does not assert transfer of particular
    old-pole proteins, strict conservative inheritance, or a fully resolved molecular
    sequence.
  evidence_ids:
  - spb-agent-jaspersen-duplication-browser
  - spb-agent-jaspersen-browser
  - record
- assessment_id: primary-model
  area: scope
  topic: Integrative model experimental boundaries
  outcome: supported
  target_ids:
  - GO:0005816
  summary: The 2017 model addresses CP/IL2 and portions of layer-spanning proteins.
    K. lactis calmodulin supplied a crystal constraint, while in vivo FRET concerns
    S. cerevisiae. The initial two-layer Spc29 model was rejected by tagged EM; the
    final reduced core stoichiometry and possible peripheral Spc29 pool are modeling
    interpretations. None is promoted into a quantitative record assertion.
  evidence_ids:
  - spb-agent-viswanath2017
  - record
- assessment_id: completeness
  area: completeness
  topic: Optional inventory and measurements
  outcome: supported
  target_ids:
  - GO:0005816
  summary: The acknowledged subassembly TODO is useful. No image, fixed dimension,
    copy count or constituent protein example is asserted. Additional plaque, half-bridge
    or protein rows are optional enrichments; the observed issue is restricted to
    an exact grounding for the already-present general gamma-tubulin-complex row.
  evidence_ids:
  - spb-agent-go
  - spb-agent-viswanath2017
  - record
  - policy
- assessment_id: provenance
  area: provenance
  topic: Source identities, tiers and access
  outcome: supported
  target_ids:
  - GO:0005816
  summary: Both cited DOI identities are verified. The 2004 source is a review read
    as browser-extracted author manuscript; the 2017 source is primary integrative
    work read as native JATS. Reused source receipts keep their original timestamps
    and hashes, without adopting inherited browser status200 as native HTTP proof.
  evidence_ids:
  - spb-agent-epmc
  - spb-agent-jaspersen-browser
  - spb-agent-jaspersen-duplication-browser
  - spb-agent-jaspersen-nucleation-browser
  - spb-agent-viswanath2017
- assessment_id: ownership
  area: ownership
  topic: Maintained record and scientific status
  outcome: supported
  target_ids:
  - GO:0005816
  summary: The maintained structure YAML owns future curation. No generated page,
    mapping status, scientific history or repository history has been changed. Native
    schema and strict checks passed; these checks do not substitute for source review.
  evidence_ids:
  - record
  - policy
  - schema-result
  - strict-result
findings:
- finding_id: F1
  issue_key: spindle-pole-body-gamma-tubulin-complex-grounding
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: The existing gamma-tubulin complex class has an exact GO grounding
  description: The component gamma_tubulin_complexes is REVIEWED_LABEL_ONLY, with
    notes deferring exact fungal small-complex or plaque-bound ring-complex identifiers.
    Native GO0000930 directly denotes the general multiprotein gamma-tubulin complex
    class already asserted by this component; its definition includes MTOC localization
    and nucleation, and its children distinguish small and ring complexes. Ground
    this existing broad row to GO:0000930, or document a concrete narrower scope mismatch
    if the intended row changes. This does not require species-specific CPX composition,
    an exhaustive inventory, or replacement of the heterogeneous core component.
  target_ids:
  - GO:0005816
  field_paths:
  - components[component_id=gamma_tubulin_complexes].grounding
  - components[component_id=gamma_tubulin_complexes].grounding_status
  - components[component_id=gamma_tubulin_complexes].grounding_notes
  evidence_ids:
  - spb-agent-go
  - spb-agent-jaspersen-nucleation-browser
  - record
  - policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_pole_body.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components
  native_severity: minor
  normalization_reason: The scientific identity and function remain supported; the
    defect is a resolvable exact grounding for an existing component class.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0005816
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_pole_body.yaml
    role: maintained scientific record
  description: In later authorized curation, add GO:0000930 to the existing gamma-tubulin-complex
    component and align grounding_status/notes with the verified general class. Preserve
    the specific small/ring and plaque-assembly limitations; do not equate a species-specific
    CPX entry with the whole SPB. Preserve historical discussion rationale and record
    any current progress in notes.
  acceptance_checks:
  - Compare the revised component scope against the active GO0000930 definition and
    its small/ring subtypes.
  - Retain the supported nuclear/cytoplasmic nucleation-site role without adding autonomous
    nucleation sufficiency or universal stoichiometry.
  - Run native schema, strict, label, history and generated-page checks after maintained-record
    curation.
  generator: Maintained structure YAML; just render derives pages.
limitations:
- The 2004 review was read at claim-bearing structural, duplication and nucleation
  passages through browser text. Underlying historical studies and the complete review
  were not all independently reread.
- The 2017 primary main-text sections and relevant figure legends were read; no raw-model
  rerun, microscopy-pixel reanalysis or complete supplementary-data audit was performed.
- Model copy ratios, exact Spc29 conformation and proposed calmodulin domain swaps
  are not established as universal composition or direct in vivo mechanism.
- The optional whole-SPB constituent inventory and species-specific complex compositions
  remain incomplete. CPX1198/1420 are narrow candidates rather than whole-record equivalences.
- COMMON is qualitative occurrence in the characterized species, not measured prevalence
  across fungi or cells.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- Native inspection preceded assessment. The complete target and claim-bearing source
  sections were read by the source collaborator; parent audit, finalization, shared
  checks and saving remain pending.
- The explicit user goal requests coverage of every selected target, including clean
  records; no issue is invented to justify a bundle.
- Unsaved review draft only. Maintained scientific records, native status, history
  and generated pages remain unchanged.
```
