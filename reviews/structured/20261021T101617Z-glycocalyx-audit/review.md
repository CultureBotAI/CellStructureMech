# Envelope identity, composition and evidence review

- Review: 20261021T101617Z-glycocalyx-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T09:59:35Z
- Finished UTC: 2026-10-21T10:16:17Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The broad glycocalyx identity, subclass boundaries and two bacterial examples are supported. No corrective finding was observed; full-text access and precise material-necessity limits are explicit.

## Scope And Provenance

Entire single record with exact authority identities, declared source-reading scopes, protein checks where applicable and component/function/graph boundaries.

Selection: Target 5 in batch eighteen; exact sorted uncovered path at frozen fresh-main revision.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0030112 | data/structures/envelope/glycocalyx.yaml | maintained | glycocalyx |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0030112 | Focused validator passed. |
| Focused native strict | passed | True | GO:0030112 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0030112 | 13 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | GO:0030112 | No expression-module or transcriptomic inference is made by this structural review. |
| Claim-level scientific review | passed | True | GO:0030112 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0030112 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0030112 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0030112 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0030112 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0030112 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Broad parent with preserved microbial and nonmicrobial subclasses

identity: supported. Targets: GO:0030112.

The native identifier, definition and parent match. Explicit nonmicrobial subclass discussion prevents a microbial example from redefining the complete GO class; capsule and slime layer remain distinct narrower structures.

### A collective matrix is not one chemical species

grounding: supported. Targets: GO:0030112.

The matrix row deliberately names heterogeneous extracellular material rather than one polymer or protein. Label-only status and the open grounding discussion accurately preserve that class boundary. The complete Brown scans corroborate the mixed-material example without supplying a universal exact chemical inventory.

### Defining material versus chemical-class formation requirements

evidence: unknown. Targets: GO:0030112.

ESSENTIAL applies to the complete extracellular material constituting the glycocalyx. That logical constitution does not establish whether the layer forms without any particular glycan, protein or other chemical class. Brown extraction and Hyams capsule comparisons do not resolve universal formation requirements for the broad matrix, so individual necessity remains unknown without a new finding.

### Two bounded bacterial examples

scope: supported. Targets: GO:0030112.

Brown supports the chemically analyzed P.aeruginosa slime example; all five primary scan pages were independently visually read during peer review. Hyams directly supports an organized pneumococcal capsule in named strains. Taxon names agree; neither paper is treated as universal prevalence or functional evidence.

### Explicitly descriptive mature-layer topology

graph: supported. Targets: GO:0030112.

The two edges state material constitution and peripheral location. NONMECHANISTIC and the scope note accurately exclude an unsupported secretion or retention mechanism. No separate function row is mandatory for this broad parent.

### Bounded record-level coverage

completeness: supported. Targets: GO:0030112.

The entire maintained record and cited claim contexts were inspected at the stated source scopes. Exact additional polymer inventories, numerical properties, images, traits and expanded mechanisms are optional. No verbatim quotation requires repair, and no status or history rewrite is proposed. A clean result does not assert exhaustive literature completeness.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/envelope/glycocalyx.yaml; Entire maintained YAML including history, all evidence notes, components, functions, graph edges and discussions | context_only | All maintained fields were read. No scientific edit or mapping-status promotion is made. |
| policy | docs/CURATION.md; Exact identity, claim-level evidence, material versus localization grounding, and component assembly-essentiality contract | context_only | Family identity, concrete protein examples and structure membership are separate; activity and viability are not by themselves formation assays. Optional inventories are not mandatory. |
| root18-sources-glycocalyx-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030112,GO:0030114,GO:0030312,GO:0042603,GO:0120234,GO:0120238,GO:0120239,GO:0120240; All eight returned term definitions, exact hierarchy edges and applicable synonyms | supports | GO0030112 exactly defines a carbohydrate-rich outermost layer, is a child of external encapsulating structure, and parents capsule/slime-layer and four named nonmicrobial glycocalyx classes. Capsule organization and diffuse slime-layer boundaries agree with the maintained discussion. |
| root18-sources-NCBITaxon-287 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/287; Exact taxId, scientificName, rank, lineage and relevant alternative names | supports | Native ENA taxonomy identifies Pseudomonas aeruginosa at species rank. Only this taxon's identity and names are asserted by this row, not occurrence or experimental stock identity. |
| root18-sources-NCBITaxon-1313 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1313; Exact taxId, scientificName, rank, lineage and relevant alternative names | supports | Native ENA taxonomy identifies Streptococcus pneumoniae at species rank. Only this taxon's identity and names are asserted by this row, not occurrence or experimental stock identity. |
| root18-sources-doi-10.1042_bj1120521 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1042/bj1120521; Exact native title, authors, year, source MED, DOI/PMID and abstract fields | supports | Native citation identifies Composition of Pseudomonas aeruginosa slime. PMID 4240755; DOI 10.1042/bj1120521. Bibliographic fields and returned abstract were inspected; this row does not attest a full-text read. |
| root18-sources-doi-10.1128_IAI.00881-09 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1128/IAI.00881-09; Exact native title, authors, year, source MED, DOI/PMID and abstract fields | supports | Native citation identifies The Streptococcus pneumoniae capsule inhibits complement activity and neutrophil phagocytosis by multiple mechanisms. PMID 19948837; DOI 10.1128/iai.00881-09. Bibliographic fields and returned abstract were inspected; this row does not attest a full-text read. |
| root18-sources-doi-10.1146_annurev.mi.35.100181.001503 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1146/annurev.mi.35.100181.001503; Exact native title, authors, year, source MED, DOI/PMID and Review publication type; no abstractText field is returned | supports | Native metadata identifies The bacterial glycocalyx in nature and disease, Costerton, Irvin and Cheng1981, PMID7027902, DOI10.1146/annurev.mi.35.100181.001503, as a review. The result contains no abstractText; only bibliographic identity and source type were checked. |
| root18-sources-legacy-PMC1187742 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1187742/; Exact article identity and complete five-part native abstract; the legacy page exposes scanned full text, not a readable full-body transcript | supports | The native Brown/Foster/Clamp1969 abstract reports chemical analysis of slime from eight P.aeruginosa strains under different media/extraction conditions. It directly supports the bounded canonical example without importing its numerical composition into a universal glycocalyx recipe. |
| root18-sources-legacy-PMC2812187 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2812187/; PMC2812187 abstract1; Introduction preceding sec1; Methods sec2 Bacterial strains and culture conditions and sec3 EM; Results sec10 Confirmation of loss of the capsule layer, including Figure1 caption. Remaining complement/neutrophil experiments not independently audited. | supports | Hyams et al.2010 directly compares encapsulated D39/TIGR4 with capsule-locus mutants and measures an external capsule by electron microscopy. This supports an organized pneumococcal capsule example; immune mechanisms are not generalized to all glycocalyces. |
| root18-sources-costerton-publisher | https://www.annualreviews.org/content/journals/10.1146/annurev.mi.35.100181.001503; Actual source-access response, not article content | context_only | Publisher route returnedHTTP403. Costerton1981 is verified bibliographic context only; neither a native abstract nor a readable full body was recovered. |
| root18-sources-brown1969-pdf | https://portlandpress.com/biochemj/article-pdf/112/4/521/763317/bj1120521.pdf; Actual source-access response, not article content | context_only | Publisher PDF route returnedHTTP403 HTML; no primary PDF read is claimed from this response. |
| root18-sources-brown1969-pmc-pdf | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1187742/pdf/biochemj00703-0128.pdf; Actual source-access response, not article content | context_only | The exact PDF link listed by the PMC page returnedHTTP200 HTML rather than PDF bytes; no full-text read is claimed from this response. |
| schema-result | just validate data/structures/envelope/glycocalyx.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/envelope/glycocalyx.yaml |
| strict-result | just validate-strict data/structures/envelope/glycocalyx.yaml --out /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/glycocalyx-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/envelope/glycocalyx.yaml --out /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/glycocalyx-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch18-20261021-5wxxz5kh/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/glycocalyx-strict.tsv |
| target-curies | just check-curies-strict; data/structures/envelope/glycocalyx.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 13 of13 collected target identifiers returned OK in this fresh base resolver run. Residuals: none. Source-native identity checked separately. |
| root18-sources-brown1969-page1 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/2ddc/1187742/0eb45745023b/biochemj00703-0128.png; Native PMC1187742 PNG scan. Printed p521: title/authors, complete five-part abstract, Introduction, Materials and methods opening (materials and organisms). Entire scan visually read. | supports | The abstract reports eight-strain slime chemical analysis and a predominantly polysaccharide preparation with nucleic acids and minor protein. The Methods opening names the eight strains and culture-media types. This page supports the bounded historical example, not a universal glycocalyx recipe. |
| root18-sources-brown1969-page2 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/2ddc/1187742/7c5292cc3631/biochemj00703-0129.png; Native PMC1187742 PNG scan. Printed p522: Materials and methods continuation (culture, extraction, chemical identification and assays); Results Yield and Composition opening. Entire scan visually read. | supports | Methods describe five-day static37C culture, homogenization or ethylene-glycol extraction, ethanol precipitation and chemical assays. Early Results compare yields and report qualitative similarity across the eight strains and tested media. |
| root18-sources-brown1969-page3 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/2ddc/1187742/eef42817ec9e/biochemj00703-0130.png; Native PMC1187742 PNG scan. Printed p523: Results Composition continuation, Table1 sugar identities, precipitate examination, Quantitative analysis and complete Table2. Entire scan visually read. | supports | This page identifies sugars in hydrolysates and presents Table2 bulk chemical measurements across media and extraction procedures. It supports mixed polysaccharide, nucleic-acid and protein content while preserving the experimental preparation and assay scope. |
| root18-sources-brown1969-page4 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/2ddc/1187742/c7e5013f9446/biochemj00703-0131.png; Native PMC1187742 PNG scan. Printed p524: quantitative Results continuation and Discussion opening through the possible cell-wall/lysis contribution. Entire scan visually read. | supports | The authors discuss extraction-dependent differences and predominantly polysaccharide slime with smaller nucleic-acid/protein fractions. They cannot distinguish a glucose/mannose copolymer from a glucan/mannan mixture and consider possible cell-wall or lysis contributions to some measured sugars. |
| root18-sources-brown1969-page5 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/2ddc/1187742/4fa9e12051bb/biochemj00703-0132.png; Native PMC1187742 PNG scan. Printed p525: final Discussion paragraph, acknowledgments and References. Entire scan visually read. | supports | The final Discussion attributes ribose/deoxyribose plausibly to nucleic acid but also considers GDP-derived biosynthetic intermediates. The remainder contains acknowledgments and the reference list; this page does not itself report the extraction protocol or Table2. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Brown1969 complete primary scan pages521-525 were independently visually read during peer review, including Methods, Results/Table2 and Discussion. PDF routes remain blocked/challenge responses. The historical bulk extraction study does not establish a universal glycocalyx composition or resolve polymer architecture.
- Hyams2010 was read only at the stated identity, culture, capsule-imaging and first-results passages; no new immune mechanism is asserted.
- Costerton1981 full text was not recovered and the exact native metadata has no abstractText. Its use is bibliographic only. The heterogeneous matrix does not support a single polymer or protein-family grounding or a component-specific formation-necessity claim.
- No raw microscopy or quantitative datasets were reanalysed. Historical curator searches and independent historical authorship are not certified.
- The completed fresh-base batch15 global gates are attached only at finalization; identifier transport and label-adapter limits remain explicit.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The user explicitly authorized one review for every uncovered target, including a review with no findings. Only this review bundle is intended for persistence.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T101617Z-glycocalyx-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Envelope identity, composition and evidence review
started_at: '2026-10-21T09:59:35Z'
finished_at: '2026-10-21T10:16:17Z'
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
summary: The broad glycocalyx identity, subclass boundaries and two bacterial examples
  are supported. No corrective finding was observed; full-text access and precise
  material-necessity limits are explicit.
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
  - path: data/structures/envelope/glycocalyx.yaml
    sha256: 4ebec54781652733dfc62c3ee5ef24695e6065aea361cc672d6e8a99f82840d8
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
  - path: scripts/score_causal_graphs.py
    sha256: 5ffe450c5b37c3dc3b0e62672caf0d99b358c8249fcc98a8c4fc7d78e8cd0d2f
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: GO:0030112
  path: data/structures/envelope/glycocalyx.yaml
  label: glycocalyx
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/envelope/glycocalyx.yaml
    role: maintained scientific record
scope:
  description: Entire single record with exact authority identities, declared source-reading
    scopes, protein checks where applicable and component/function/graph boundaries.
  selection: Target 5 in batch eighteen; exact sorted uncovered path at frozen fresh-main
    revision.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0030112
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0030112
  command: just validate data/structures/envelope/glycocalyx.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0030112
  command: just validate-strict data/structures/envelope/glycocalyx.yaml --out /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/glycocalyx-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0030112
  summary: 13 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0030112
  summary: No expression-module or transcriptomic inference is made by this structural
    review.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0030112
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - root18-sources-glycocalyx-go
  - root18-sources-NCBITaxon-287
  - root18-sources-NCBITaxon-1313
  - root18-sources-doi-10.1042_bj1120521
  - root18-sources-doi-10.1128_IAI.00881-09
  - root18-sources-doi-10.1146_annurev.mi.35.100181.001503
  - root18-sources-legacy-PMC1187742
  - root18-sources-legacy-PMC2812187
  - root18-sources-costerton-publisher
  - root18-sources-brown1969-pdf
  - root18-sources-brown1969-pmc-pdf
  - root18-sources-brown1969-page1
  - root18-sources-brown1969-page2
  - root18-sources-brown1969-page3
  - root18-sources-brown1969-page4
  - root18-sources-brown1969-page5
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0030112
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
  - GO:0030112
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
  - GO:0030112
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
  - GO:0030112
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
  - GO:0030112
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
  reference: data/structures/envelope/glycocalyx.yaml
  locator: Entire maintained YAML including history, all evidence notes, components,
    functions, graph edges and discussions
  accessed_at: '2026-10-21T10:07:58Z'
  support: context_only
  summary: All maintained fields were read. No scientific edit or mapping-status promotion
    is made.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact identity, claim-level evidence, material versus localization grounding,
    and component assembly-essentiality contract
  accessed_at: '2026-10-21T10:07:58Z'
  support: context_only
  summary: Family identity, concrete protein examples and structure membership are
    separate; activity and viability are not by themselves formation assays. Optional
    inventories are not mandatory.
- evidence_id: root18-sources-glycocalyx-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030112,GO:0030114,GO:0030312,GO:0042603,GO:0120234,GO:0120238,GO:0120239,GO:0120240
  locator: All eight returned term definitions, exact hierarchy edges and applicable
    synonyms
  accessed_at: '2026-10-21T10:00:59.283845Z'
  support: supports
  summary: GO0030112 exactly defines a carbohydrate-rich outermost layer, is a child
    of external encapsulating structure, and parents capsule/slime-layer and four
    named nonmicrobial glycocalyx classes. Capsule organization and diffuse slime-layer
    boundaries agree with the maintained discussion.
  snapshot_sha256: a9200105bc5aa4d0aac784073122244c94e3d5e50c951b2ad2d7e88d5b69cc3f
- evidence_id: root18-sources-NCBITaxon-287
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/287
  locator: Exact taxId, scientificName, rank, lineage and relevant alternative names
  accessed_at: '2026-10-21T10:00:59.368456Z'
  support: supports
  summary: Native ENA taxonomy identifies Pseudomonas aeruginosa at species rank.
    Only this taxon's identity and names are asserted by this row, not occurrence
    or experimental stock identity.
  snapshot_sha256: f910ca54823b9c44e1ee274cf7a95b5d704eab096e7ad63ea6efb8687762d8e8
- evidence_id: root18-sources-NCBITaxon-1313
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1313
  locator: Exact taxId, scientificName, rank, lineage and relevant alternative names
  accessed_at: '2026-10-21T10:00:59.349040Z'
  support: supports
  summary: Native ENA taxonomy identifies Streptococcus pneumoniae at species rank.
    Only this taxon's identity and names are asserted by this row, not occurrence
    or experimental stock identity.
  snapshot_sha256: 07b4370dea0d2ae7c95239a13aadb2d8ad0def57b1d6cec5124f8f8389707e56
- evidence_id: root18-sources-doi-10.1042_bj1120521
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1042/bj1120521
  locator: Exact native title, authors, year, source MED, DOI/PMID and abstract fields
  accessed_at: '2026-10-21T10:00:59.567026Z'
  support: supports
  summary: Native citation identifies Composition of Pseudomonas aeruginosa slime.
    PMID 4240755; DOI 10.1042/bj1120521. Bibliographic fields and returned abstract
    were inspected; this row does not attest a full-text read.
  snapshot_sha256: 502f6f80bc5c1c54dfa8aad1e16211bfacdee37c19ccfd7bb7794a172e085759
- evidence_id: root18-sources-doi-10.1128_IAI.00881-09
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1128/IAI.00881-09
  locator: Exact native title, authors, year, source MED, DOI/PMID and abstract fields
  accessed_at: '2026-10-21T10:00:59.951390Z'
  support: supports
  summary: Native citation identifies The Streptococcus pneumoniae capsule inhibits
    complement activity and neutrophil phagocytosis by multiple mechanisms. PMID 19948837;
    DOI 10.1128/iai.00881-09. Bibliographic fields and returned abstract were inspected;
    this row does not attest a full-text read.
  snapshot_sha256: e0803055e77d0ff0065a30ca84c33483af886b6e3f06a5d36a7d2a87ee0d67ca
- evidence_id: root18-sources-doi-10.1146_annurev.mi.35.100181.001503
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1146/annurev.mi.35.100181.001503
  locator: Exact native title, authors, year, source MED, DOI/PMID and Review publication
    type; no abstractText field is returned
  accessed_at: '2026-10-21T10:01:00.017088Z'
  support: supports
  summary: Native metadata identifies The bacterial glycocalyx in nature and disease,
    Costerton, Irvin and Cheng1981, PMID7027902, DOI10.1146/annurev.mi.35.100181.001503,
    as a review. The result contains no abstractText; only bibliographic identity
    and source type were checked.
  snapshot_sha256: 7f3bc0ef1f0c6104485e4f708052699f6dffea0aa7e7775aee7f58694fddc3fb
- evidence_id: root18-sources-legacy-PMC1187742
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1187742/
  locator: Exact article identity and complete five-part native abstract; the legacy
    page exposes scanned full text, not a readable full-body transcript
  accessed_at: '2026-10-21T10:02:33.292441Z'
  support: supports
  summary: The native Brown/Foster/Clamp1969 abstract reports chemical analysis of
    slime from eight P.aeruginosa strains under different media/extraction conditions.
    It directly supports the bounded canonical example without importing its numerical
    composition into a universal glycocalyx recipe.
  snapshot_sha256: e244a8c3361673a7d490b5a7d171f76fe66be4ac338f356435cab4aa6452d5e4
- evidence_id: root18-sources-legacy-PMC2812187
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2812187/
  locator: PMC2812187 abstract1; Introduction preceding sec1; Methods sec2 Bacterial
    strains and culture conditions and sec3 EM; Results sec10 Confirmation of loss
    of the capsule layer, including Figure1 caption. Remaining complement/neutrophil
    experiments not independently audited.
  accessed_at: '2026-10-21T10:02:33.346815Z'
  support: supports
  summary: Hyams et al.2010 directly compares encapsulated D39/TIGR4 with capsule-locus
    mutants and measures an external capsule by electron microscopy. This supports
    an organized pneumococcal capsule example; immune mechanisms are not generalized
    to all glycocalyces.
  snapshot_sha256: e1c70f23a6c81f19791b481cddd8ada4b572a2c69bdbe258dc9a88eb48c420df
- evidence_id: root18-sources-costerton-publisher
  kind: authority
  reference: https://www.annualreviews.org/content/journals/10.1146/annurev.mi.35.100181.001503
  locator: Actual source-access response, not article content
  accessed_at: '2026-10-21T10:02:15.853925Z'
  support: context_only
  summary: Publisher route returnedHTTP403. Costerton1981 is verified bibliographic
    context only; neither a native abstract nor a readable full body was recovered.
  snapshot_sha256: 764eda9ecaa6644ba2d0a6da60e2186d3a5d11980ab0f0208a586ffe534105f5
- evidence_id: root18-sources-brown1969-pdf
  kind: authority
  reference: https://portlandpress.com/biochemj/article-pdf/112/4/521/763317/bj1120521.pdf
  locator: Actual source-access response, not article content
  accessed_at: '2026-10-21T10:02:15.829767Z'
  support: context_only
  summary: Publisher PDF route returnedHTTP403 HTML; no primary PDF read is claimed
    from this response.
  snapshot_sha256: 63a15e672cdee4be9e86a8309c44e12c0103263a37b3cade3eb0a4a0a771488b
- evidence_id: root18-sources-brown1969-pmc-pdf
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1187742/pdf/biochemj00703-0128.pdf
  locator: Actual source-access response, not article content
  accessed_at: '2026-10-21T10:05:55.894109Z'
  support: context_only
  summary: The exact PDF link listed by the PMC page returnedHTTP200 HTML rather than
    PDF bytes; no full-text read is claimed from this response.
  snapshot_sha256: 899202edef12b499e42b1a57893d6625e93b3253a362d3c71f1e2dd2d85fe673
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/envelope/glycocalyx.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:59:38Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/envelope/glycocalyx.yaml'
  snapshot_sha256: 59d2b46f21e6d86a770b3a7083f2a8d7b8aa047c28c283d42143d30cffba620b
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/envelope/glycocalyx.yaml --out /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/glycocalyx-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:59:40Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/envelope/glycocalyx.yaml\
    \ --out /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/glycocalyx-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch18-20261021-5wxxz5kh/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/glycocalyx-strict.tsv"
  snapshot_sha256: 314deb3226c3500241a6452762e0aed99c27ed7217bba045b15a636dbc19d511
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/envelope/glycocalyx.yaml; exact collect() scope; hash identifies
    the entire original resolver TSV
  accessed_at: '2026-10-21T10:07:58Z'
  support: supports
  summary: '13 of13 collected target identifiers returned OK in this fresh base resolver
    run. Residuals: none. Source-native identity checked separately.'
  snapshot_sha256: d428d95fd13ac608f3786bcf74a032c768ac80e494b9673013e1e4d27de9ad66
- evidence_id: root18-sources-brown1969-page1
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/2ddc/1187742/0eb45745023b/biochemj00703-0128.png
  locator: 'Native PMC1187742 PNG scan. Printed p521: title/authors, complete five-part
    abstract, Introduction, Materials and methods opening (materials and organisms).
    Entire scan visually read.'
  accessed_at: '2026-10-21T10:06:32.342178Z'
  support: supports
  summary: The abstract reports eight-strain slime chemical analysis and a predominantly
    polysaccharide preparation with nucleic acids and minor protein. The Methods opening
    names the eight strains and culture-media types. This page supports the bounded
    historical example, not a universal glycocalyx recipe.
  snapshot_sha256: 50f562ca73cc787982faef026ecc61f6bfbab1290ce168c5e50833cfb9f598a2
- evidence_id: root18-sources-brown1969-page2
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/2ddc/1187742/7c5292cc3631/biochemj00703-0129.png
  locator: 'Native PMC1187742 PNG scan. Printed p522: Materials and methods continuation
    (culture, extraction, chemical identification and assays); Results Yield and Composition
    opening. Entire scan visually read.'
  accessed_at: '2026-10-21T10:06:32.342594Z'
  support: supports
  summary: Methods describe five-day static37C culture, homogenization or ethylene-glycol
    extraction, ethanol precipitation and chemical assays. Early Results compare yields
    and report qualitative similarity across the eight strains and tested media.
  snapshot_sha256: 41ece3885374b6f0fa57af4aec821c75099140dff2138d627d9326bf87959e60
- evidence_id: root18-sources-brown1969-page3
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/2ddc/1187742/eef42817ec9e/biochemj00703-0130.png
  locator: 'Native PMC1187742 PNG scan. Printed p523: Results Composition continuation,
    Table1 sugar identities, precipitate examination, Quantitative analysis and complete
    Table2. Entire scan visually read.'
  accessed_at: '2026-10-21T10:06:32.342769Z'
  support: supports
  summary: This page identifies sugars in hydrolysates and presents Table2 bulk chemical
    measurements across media and extraction procedures. It supports mixed polysaccharide,
    nucleic-acid and protein content while preserving the experimental preparation
    and assay scope.
  snapshot_sha256: b8ea09a9d8713a0cc136728a061bd8c1f822063baa25e313c3cb24863433adb2
- evidence_id: root18-sources-brown1969-page4
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/2ddc/1187742/c7e5013f9446/biochemj00703-0131.png
  locator: 'Native PMC1187742 PNG scan. Printed p524: quantitative Results continuation
    and Discussion opening through the possible cell-wall/lysis contribution. Entire
    scan visually read.'
  accessed_at: '2026-10-21T10:06:32.342955Z'
  support: supports
  summary: The authors discuss extraction-dependent differences and predominantly
    polysaccharide slime with smaller nucleic-acid/protein fractions. They cannot
    distinguish a glucose/mannose copolymer from a glucan/mannan mixture and consider
    possible cell-wall or lysis contributions to some measured sugars.
  snapshot_sha256: dc4d865f3e08e42db8604cbe16ecbd7d45860ff984918d70339dd00aafea0540
- evidence_id: root18-sources-brown1969-page5
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/2ddc/1187742/4fa9e12051bb/biochemj00703-0132.png
  locator: 'Native PMC1187742 PNG scan. Printed p525: final Discussion paragraph,
    acknowledgments and References. Entire scan visually read.'
  accessed_at: '2026-10-21T10:06:32.343197Z'
  support: supports
  summary: The final Discussion attributes ribose/deoxyribose plausibly to nucleic
    acid but also considers GDP-derived biosynthetic intermediates. The remainder
    contains acknowledgments and the reference list; this page does not itself report
    the extraction protocol or Table2.
  snapshot_sha256: 15d776120aeca92a97a387790947353e1fb7deec037086540e68dc3427616d03
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
  topic: Broad parent with preserved microbial and nonmicrobial subclasses
  outcome: supported
  target_ids:
  - GO:0030112
  summary: The native identifier, definition and parent match. Explicit nonmicrobial
    subclass discussion prevents a microbial example from redefining the complete
    GO class; capsule and slime layer remain distinct narrower structures.
  evidence_ids:
  - root18-sources-glycocalyx-go
  - record
- assessment_id: composition
  area: grounding
  topic: A collective matrix is not one chemical species
  outcome: supported
  target_ids:
  - GO:0030112
  summary: The matrix row deliberately names heterogeneous extracellular material
    rather than one polymer or protein. Label-only status and the open grounding discussion
    accurately preserve that class boundary. The complete Brown scans corroborate
    the mixed-material example without supplying a universal exact chemical inventory.
  evidence_ids:
  - root18-sources-glycocalyx-go
  - root18-sources-legacy-PMC1187742
  - record
  - policy
  - root18-sources-brown1969-page1
  - root18-sources-brown1969-page2
  - root18-sources-brown1969-page3
  - root18-sources-brown1969-page4
  - root18-sources-brown1969-page5
- assessment_id: formation-necessity
  area: evidence
  topic: Defining material versus chemical-class formation requirements
  outcome: unknown
  target_ids:
  - GO:0030112
  summary: ESSENTIAL applies to the complete extracellular material constituting the
    glycocalyx. That logical constitution does not establish whether the layer forms
    without any particular glycan, protein or other chemical class. Brown extraction
    and Hyams capsule comparisons do not resolve universal formation requirements
    for the broad matrix, so individual necessity remains unknown without a new finding.
  evidence_ids:
  - record
  - policy
  - root18-sources-glycocalyx-go
  - root18-sources-legacy-PMC2812187
  - root18-sources-brown1969-page1
  - root18-sources-brown1969-page2
  - root18-sources-brown1969-page3
  - root18-sources-brown1969-page4
  - root18-sources-brown1969-page5
- assessment_id: examples
  area: scope
  topic: Two bounded bacterial examples
  outcome: supported
  target_ids:
  - GO:0030112
  summary: Brown supports the chemically analyzed P.aeruginosa slime example; all
    five primary scan pages were independently visually read during peer review. Hyams
    directly supports an organized pneumococcal capsule in named strains. Taxon names
    agree; neither paper is treated as universal prevalence or functional evidence.
  evidence_ids:
  - root18-sources-doi-10.1042_bj1120521
  - root18-sources-doi-10.1128_IAI.00881-09
  - root18-sources-legacy-PMC1187742
  - root18-sources-legacy-PMC2812187
  - root18-sources-NCBITaxon-287
  - root18-sources-NCBITaxon-1313
  - record
  - root18-sources-brown1969-page1
  - root18-sources-brown1969-page2
  - root18-sources-brown1969-page3
  - root18-sources-brown1969-page4
  - root18-sources-brown1969-page5
- assessment_id: graph
  area: graph
  topic: Explicitly descriptive mature-layer topology
  outcome: supported
  target_ids:
  - GO:0030112
  summary: The two edges state material constitution and peripheral location. NONMECHANISTIC
    and the scope note accurately exclude an unsupported secretion or retention mechanism.
    No separate function row is mandatory for this broad parent.
  evidence_ids:
  - root18-sources-glycocalyx-go
  - record
- assessment_id: coverage
  area: completeness
  topic: Bounded record-level coverage
  outcome: supported
  target_ids:
  - GO:0030112
  summary: The entire maintained record and cited claim contexts were inspected at
    the stated source scopes. Exact additional polymer inventories, numerical properties,
    images, traits and expanded mechanisms are optional. No verbatim quotation requires
    repair, and no status or history rewrite is proposed. A clean result does not
    assert exhaustive literature completeness.
  evidence_ids:
  - record
  - policy
  - root18-sources-glycocalyx-go
  - root18-sources-NCBITaxon-287
  - root18-sources-NCBITaxon-1313
  - root18-sources-doi-10.1042_bj1120521
  - root18-sources-doi-10.1128_IAI.00881-09
  - root18-sources-doi-10.1146_annurev.mi.35.100181.001503
  - root18-sources-legacy-PMC1187742
  - root18-sources-legacy-PMC2812187
  - root18-sources-costerton-publisher
  - root18-sources-brown1969-pdf
  - root18-sources-brown1969-pmc-pdf
  - root18-sources-brown1969-page1
  - root18-sources-brown1969-page2
  - root18-sources-brown1969-page3
  - root18-sources-brown1969-page4
  - root18-sources-brown1969-page5
findings: []
actions: []
limitations:
- Brown1969 complete primary scan pages521-525 were independently visually read during
  peer review, including Methods, Results/Table2 and Discussion. PDF routes remain
  blocked/challenge responses. The historical bulk extraction study does not establish
  a universal glycocalyx composition or resolve polymer architecture.
- Hyams2010 was read only at the stated identity, culture, capsule-imaging and first-results
  passages; no new immune mechanism is asserted.
- Costerton1981 full text was not recovered and the exact native metadata has no abstractText.
  Its use is bibliographic only. The heterogeneous matrix does not support a single
  polymer or protein-family grounding or a component-specific formation-necessity
  claim.
- No raw microscopy or quantitative datasets were reanalysed. Historical curator searches
  and independent historical authorship are not certified.
- The completed fresh-base batch15 global gates are attached only at finalization;
  identifier transport and label-adapter limits remain explicit.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- The user explicitly authorized one review for every uncovered target, including
  a review with no findings. Only this review bundle is intended for persistence.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
