# Coccolith scale identity, material evidence and image provenance review

- Review: 20261021T100145Z-coccolith-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T09:44:09Z
- Finished UTC: 2026-10-21T10:01:45Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The individual-scale identity, calcite grounding, scoped organic-material and adsorption claims, examples and licensed Figure1 are supported. No corrective issue was observed in the reviewed scope.

## Scope And Provenance

Entire single maintained record and frozen local figure; native local-ID/GO/ChEBI/taxon authorities and three primary papers at the declared claim scopes.

Selection: Ninth selected target in batch seventeen, fixed maintained-path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:coccolith | data/structures/envelope/coccolith.yaml | maintained | coccolith |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | cellstructuremech:coccolith | Focused validator passed. |
| Focused native strict | passed | True | cellstructuremech:coccolith | Focused validator passed. |
| Target resolver slice | passed | True | cellstructuremech:coccolith | 7 identifiers OK; 1 transport/skipped residuals independently resolved. |
| Claim-level scientific review | passed | True | cellstructuremech:coccolith | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | cellstructuremech:coccolith | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | cellstructuremech:coccolith | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | cellstructuremech:coccolith | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | cellstructuremech:coccolith | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | cellstructuremech:coccolith | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Individual mineral scale, distinct from covering and vesicle

identity: supported. Targets: cellstructuremech:coccolith.

The local identifier uniquely resolves to the maintained scale record. OTHER kind avoids calling one scale a continuous layer. The broad GO parent is appropriate, while vesicle, entire coccosphere and narrower holo-/heterococcolith types retain separate identities. No unconditional vesicle parthood or exclusively extracellular development is asserted.

### Mineral grounding and unresolved organic chemistry

grounding: supported. Targets: cellstructuremech:coccolith.

The calcite grounding is exact at mineral-material level. Associated organic material is experimentally supported, but oxidation and morphology do not identify one polymer or protein family. REVIEWED_LABEL_ONLY and UNKNOWN necessity correctly preserve that limit. Post-assembly persistence after oxidation does not establish dispensability for formation.

### Two species examples retain their experimental preparation

scope: supported. Targets: cellstructuremech:coccolith.

Native taxa match the named species. RCC1130 is established by the supplement; CCMP374 calcified donor identity is established separately from naked recipient cultures in Johns. No generic crystal count, size, shape, broad prevalence or single-morphotype adsorption rule is promoted.

### Covering element and scoped adsorption

evidence: supported. Targets: cellstructuremech:coccolith.

Individual scales demonstrably contribute to an external covering. The adsorption function is limited to the tested E.huxleyi system and organic-removal comparison. The record does not infer universal adaptive protection, exact adhesion chemistry or nucleation-template mechanism.

### Exact image, license and preparation

provenance: supported. Targets: cellstructuremech:coccolith.

The local unmodified Figure1 byte hashes, PMC accession and media locator agree. JATS licenses the article under CC BY4.0, and attribution agrees with author metadata. Mixed SEM/diagram/AFM content is explicitly described; species and sample preparation remain scoped.

### Boundaries and optional omissions are justified

completeness: supported. Targets: cellstructuremech:coccolith.

No concrete corrective issue was observed. Unidentified vesicle particles are not imported as scale constituents; unresolved organic inventory and crystal-ordering mechanisms remain explicit. No causal graph, trait link or numeric property is required solely because the source contains one. No verbatim snippet or status promotion is present.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/envelope/coccolith.yaml; Entire maintained YAML including definition, components, functions, hierarchy, examples, graph edges, discussions, image metadata and history | context_only | All fields were read after fresh native inspection; the maintained target and PROPOSED state are unchanged. |
| policy | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, CausalNode and source-specific ComplexComposition contracts; essentiality definition; docs/CURATION.md assembly-versus-function guidance and review checklist | context_only | Component family identity, concrete protein identity and source-specific assembly membership are separate. Essentiality asks whether the structure forms without the component; membership and activity do not establish it. Optional fields are not mandatory. CausalNode permits protein complexes; its xrefs contract does not inherit the top-level record equivalence restriction. |
| coccolith-agent-local-ids | rg --no-ignore --hidden -n --glob *.yaml ^identifier: cellstructuremech:(coccolith&#124;coccosphere)$ data/structures; Exact top-level identifier fields across maintained data/structures | supports | Exactly one maintained record defines cellstructuremech:coccolith and exactly one defines cellstructuremech:coccosphere. The target identity and, for coccosphere, the linked coccolith record were read and frozen as native inspection inputs. This resolves repository-local identifiers, not an external equivalence. |
| coccolith-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0110165; Native GO0110165 name and complete definition | supports | GO0110165 is a broad cellular anatomical structure class, including substances produced by cells at the stated granularity. It does not impose a permanently intracellular or extracellular stage and is not asserted as exact coccolith identity. |
| coccolith-agent-chebi-46719 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/46719/; Released entry name, chemical data and ontology relations; no textual definition is supplied | supports | CHEBI46719 identifies calcite and its calcium-carbonate/carbonate-mineral relationships. This is the mineral material, not an exact organic-scale or whole-covering identity. |
| coccolith-agent-tax-127549 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/127549; Complete taxId, scientificName, rank, lineage and relevant synonyms | supports | Native ENA taxonomy identifies Calcidiscus leptoporus, species. This receipt attests that identity and rank only, not occurrence or the experimental strain. |
| coccolith-agent-tax-2903 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2903; Complete taxId, scientificName, rank, lineage and relevant synonyms | supports | Native ENA taxonomy identifies Emiliania huxleyi, species; Gephyrocapsa huxleyi is retained as a synonym. This receipt attests that identity and rank only, not occurrence or the experimental strain. |
| coccolith-agent-doi-10.1021_jacs.6c02151 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1021/jacs.6c02151%22; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Spatial Relations between Coccoliths and Their Confining Membrane During Crystal Morphogenesis. Authors: Avrahami EM, Karpov D, Aram L, Elad N, Safadi R, Rosenhek-Goldian I, Sui XM, de Haan D, Varsano N, Cohen SR, Zlotnikov I, Gal A.; PMID 41875313; DOI 10.1021/jacs.6c02151. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| coccolith-agent-doi-10.1093_pnasnexus_pgag104 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1093/pnasnexus/pgag104%22; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Templateless crystallization of holococcolith crystals visualized by intracellular site-specific three-dimensional microscopy. Authors: Ben-Joseph O, Meng YF, Aram L, Abu Freha I, Lansky Z, Safadi R, de Haan D, Rechav K, Kaplan-Ashiri I, Varsano N, Gal A.; PMID 42005959; DOI 10.1093/pnasnexus/pgag104. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| coccolith-agent-doi-10.1126_sciadv.adc8728 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1126/sciadv.adc8728%22; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Adsorptive exchange of coccolith biominerals facilitates viral infection. Authors: Johns CT, Bondoc-Naumovitz KG, Matthews A, Matson PG, Iglesias-Rodriguez MD, Taylor AR, Fuchs HL, Bidle KD.; PMID 36662866; DOI 10.1126/sciadv.adc8728. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| coccolith-agent-jats-PMC13067266 | https://pmc-oa-opendata.s3.amazonaws.com/PMC13067266.1/PMC13067266.1.xml; PMC13067266: Introduction, complete Results including Figures1-5 captions, Discussion and Conclusions; exact article identity and JATS permissions/ALI CC BY4.0 URL. No raw tomography was reanalysed. | supports | Avrahami et al.2026 distinguishes mature C.leptoporus scales from the intracellular formation vesicle. Figure1 and Results support the two-shield/stem morphology for this example. Luminal membrane particles in Figure4 remain unidentified and do not justify adding a full ATPase or vesicle transporters as mature-scale constituents. Morphogenesis control remains incompletely resolved. |
| coccolith-agent-avrahami2026-supp | https://pmc-oa-opendata.s3.amazonaws.com/PMC13067266.1/ja6c02151_si_001.pdf; Actual supplementary PDF Materials/Methods: Cell cultures, Coccolith isolation for ex situ imaging, SEM, Correlative AFM/SEM; adjacent freeze-fracture and cryofixation preparation context. Supplementary Figures and downstream tomography processing were not fully audited. | supports | Supplementary Methods identify RCC1130 and distinguish isolated/cleaned ex situ scales for SEM/AFM from cryofixed intracellular preparations. Figure1 is not a cryotomography figure. |
| coccolith-agent-jats-PMC13089448 | https://pmc-oa-opendata.s3.amazonaws.com/PMC13089448.1/PMC13089448.1.xml; PMC13089448: Results paragraphs on mature structure, site-specific cryoET, crystal-scale distances/morphology and growth-condition effects; Discussion and Conclusion; Figure1/3/5 captions. Methods supplement and raw datasets were not analysed. | supports | Ben-Joseph et al.2026 observes holococcolith calcite rhombohedra and organic base plates, with most intracellular crystals spatially separated from plates. Discussion cannot exclude undetected small nucleators and leaves crystal ordering unresolved. These observations justify avoiding a universal base-plate-templated mechanism. |
| coccolith-agent-jats-PMC9858585 | https://pmc-oa-opendata.s3.amazonaws.com/PMC9858585.1/PMC9858585.1.xml; PMC9858585: Introduction as prior-work context; Results/Discussion Xenospheres result from adsorption, Free coccoliths alter calcification state, Adsorption mediated by organic matter (Figures1-3 captions), and Multifaceted ecological roles (Figure6 model); Methods Culture growth/maintenance, Coccolith isolation/treatment, Exogenous additions, SEM. Detailed virus-encounter modelling, raw data and supplementary videos were not independently analysed. | supports | Johns et al.2023 directly distinguishes free scales, host-produced coverings and acquired scales. Calcified CCMP374 donors and naked recipients are separate preparations. Hypochlorite removal of associated organics reduces attachment while mineral morphology persists; this does not identify a receptor or test de novo assembly. Adsorption differs by morphotype and physiological/ecological effects remain contextual. |
| coccolith-agent-image | data/images/envelope/coccolith/pmc13067266_fig1.jpg; Full Figure1 A-F: SEM cell/scales and diagram, AFM height images/projections. Figure1 caption and supplementary culture/isolation/SEM/AFM Methods read. | supports | Full Figure1 pixels agree with the caption: SEM cell and scale views, diagram, and AFM maps/projections. AFM sampled regions are not whole-scale dimensions. Exact CC BY4.0 permissions and author attribution were checked against JATS and native metadata. Local SHA-256 matches the record; local MD5 30aa4e061b96edbf874a64bb6f8064e2 matches the exact native PMC media entry. |
| coccolith-agent-package-PMC13067266 | https://pmc-oa-opendata.s3.amazonaws.com/metadata/PMC13067266.1.json; Complete article/package identity, license_code and matching media_urls entry | supports | PMC package version1 verifies exact DOI, title, PMCID, CC BY code and the media filename/MD5. The exact CC BY4.0 version is established from the separately inspected JATS permissions, not inferred from the abbreviated package code. |
| schema-result | just validate data/structures/envelope/coccolith.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/envelope/coccolith.yaml |
| strict-result | just validate-strict data/structures/envelope/coccolith.yaml --out /private/tmp/cellstructure-batch17-20261021-vub_b2nx/coccolith-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/envelope/coccolith.yaml --out /private/tmp/cellstructure-batch17-20261021-vub_b2nx/coccolith-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch17-20261021-vub_b2nx/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch17-20261021-vub_b2nx/coccolith-strict.tsv |
| target-curies | just check-curies-strict; data/structures/envelope/coccolith.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 7 of8 collected target identifiers returned OK in this fresh base resolver run. Residuals: cellstructuremech:coccolith: SKIPPED; resolved by evidence coccolith-agent-local-ids. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- This is a record-level claim audit, not a reanalysis of microscopy volumes, AFM measurements, adsorption statistics or environmental samples.
- Primary read scope is the named main-text passages, captions and culture/SEM/AFM supplement sections. Holococcolith supplementary methods and Johns detailed virus-encounter model were not independently audited.
- Exact current GO-wide synonym absence and the historical curator searches were not reconstructed. The current repository-local identifiers were checked by ignored-inclusive exact-ID search; the broader GO authority is not asserted as exact equivalence.
- The mixed organic material remains chemically unresolved and assembly necessity remains UNKNOWN. No issue is inferred from optional missing inventory.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The user-authorized coverage task requests a validated observation for every uncovered target, including clean records.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T100145Z-coccolith-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Coccolith scale identity, material evidence and image provenance review
started_at: '2026-10-21T09:44:09Z'
finished_at: '2026-10-21T10:01:45Z'
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
summary: The individual-scale identity, calcite grounding, scoped organic-material
  and adsorption claims, examples and licensed Figure1 are supported. No corrective
  issue was observed in the reviewed scope.
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
  - path: data/images/envelope/coccolith/pmc13067266_fig1.jpg
    sha256: 35772c3d477f71c47c7c2e0d6e91fbd6086b9061126c7bee92cec70fcd95f939
    role: context
  - path: data/structures/envelope/coccolith.yaml
    sha256: 8932b1ad635cf2e272c74fb8d4f00e6036b851ec2baa3daa3b5c3b52cc6979fa
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
- target_id: cellstructuremech:coccolith
  path: data/structures/envelope/coccolith.yaml
  label: coccolith
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/envelope/coccolith.yaml
    role: maintained scientific record
scope:
  description: Entire single maintained record and frozen local figure; native local-ID/GO/ChEBI/taxon
    authorities and three primary papers at the declared claim scopes.
  selection: Ninth selected target in batch seventeen, fixed maintained-path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:coccolith
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:coccolith
  command: just validate data/structures/envelope/coccolith.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:coccolith
  command: just validate-strict data/structures/envelope/coccolith.yaml --out /private/tmp/cellstructure-batch17-20261021-vub_b2nx/coccolith-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - cellstructuremech:coccolith
  summary: 7 identifiers OK; 1 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - coccolith-agent-local-ids
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:coccolith
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - coccolith-agent-local-ids
  - coccolith-agent-go
  - coccolith-agent-chebi-46719
  - coccolith-agent-tax-127549
  - coccolith-agent-tax-2903
  - coccolith-agent-doi-10.1021_jacs.6c02151
  - coccolith-agent-doi-10.1093_pnasnexus_pgag104
  - coccolith-agent-doi-10.1126_sciadv.adc8728
  - coccolith-agent-jats-PMC13067266
  - coccolith-agent-avrahami2026-supp
  - coccolith-agent-jats-PMC13089448
  - coccolith-agent-jats-PMC9858585
  - coccolith-agent-image
  - coccolith-agent-package-PMC13067266
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:coccolith
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
  - cellstructuremech:coccolith
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
  - cellstructuremech:coccolith
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
  - cellstructuremech:coccolith
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
  - cellstructuremech:coccolith
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
  reference: data/structures/envelope/coccolith.yaml
  locator: Entire maintained YAML including definition, components, functions, hierarchy,
    examples, graph edges, discussions, image metadata and history
  accessed_at: '2026-10-21T09:56:44Z'
  support: context_only
  summary: All fields were read after fresh native inspection; the maintained target
    and PROPOSED state are unchanged.
- evidence_id: policy
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, CausalNode and source-specific ComplexComposition
    contracts; essentiality definition; docs/CURATION.md assembly-versus-function
    guidance and review checklist
  accessed_at: '2026-10-21T09:56:44Z'
  support: context_only
  summary: Component family identity, concrete protein identity and source-specific
    assembly membership are separate. Essentiality asks whether the structure forms
    without the component; membership and activity do not establish it. Optional fields
    are not mandatory. CausalNode permits protein complexes; its xrefs contract does
    not inherit the top-level record equivalence restriction.
- evidence_id: coccolith-agent-local-ids
  kind: search
  reference: 'rg --no-ignore --hidden -n --glob *.yaml ^identifier: cellstructuremech:(coccolith|coccosphere)$
    data/structures'
  locator: Exact top-level identifier fields across maintained data/structures
  accessed_at: '2026-10-21T09:49:35.109765Z'
  support: supports
  summary: Exactly one maintained record defines cellstructuremech:coccolith and exactly
    one defines cellstructuremech:coccosphere. The target identity and, for coccosphere,
    the linked coccolith record were read and frozen as native inspection inputs.
    This resolves repository-local identifiers, not an external equivalence.
  snapshot_sha256: c5d1a782c2869d127fc98502ed00b6b7901499b1952a7ffe7f3993910a372d0c
  search_scope: Entire data/structures, including ignored and hidden YAML files; exact
    anchored identifiers only.
- evidence_id: coccolith-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0110165
  locator: Native GO0110165 name and complete definition
  accessed_at: '2026-10-21T09:46:58.945219Z'
  support: supports
  summary: GO0110165 is a broad cellular anatomical structure class, including substances
    produced by cells at the stated granularity. It does not impose a permanently
    intracellular or extracellular stage and is not asserted as exact coccolith identity.
  snapshot_sha256: 8af7ebd70cc7d5662c02c9f11811d9e04292105c71f15ff9e79a283c2c9a240d
- evidence_id: coccolith-agent-chebi-46719
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/46719/
  locator: Released entry name, chemical data and ontology relations; no textual definition
    is supplied
  accessed_at: '2026-10-21T09:46:59.709142Z'
  support: supports
  summary: CHEBI46719 identifies calcite and its calcium-carbonate/carbonate-mineral
    relationships. This is the mineral material, not an exact organic-scale or whole-covering
    identity.
  snapshot_sha256: 2012a33c8e9e7d723675c94c04b56a2c8ea7dfd1a36c8f637500bfc172fe6053
- evidence_id: coccolith-agent-tax-127549
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/127549
  locator: Complete taxId, scientificName, rank, lineage and relevant synonyms
  accessed_at: '2026-10-21T09:46:59.008582Z'
  support: supports
  summary: Native ENA taxonomy identifies Calcidiscus leptoporus, species. This receipt
    attests that identity and rank only, not occurrence or the experimental strain.
  snapshot_sha256: b40f70d18d46271a012610371904101819726ec1f4fc1054ca41a87a2b88e8c2
- evidence_id: coccolith-agent-tax-2903
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2903
  locator: Complete taxId, scientificName, rank, lineage and relevant synonyms
  accessed_at: '2026-10-21T09:46:59.091924Z'
  support: supports
  summary: Native ENA taxonomy identifies Emiliania huxleyi, species; Gephyrocapsa
    huxleyi is retained as a synonym. This receipt attests that identity and rank
    only, not occurrence or the experimental strain.
  snapshot_sha256: 4a759692cee77328f36e4f9ee6cd7184df92f049cae1b89b7f0e47db08f783e9
- evidence_id: coccolith-agent-doi-10.1021_jacs.6c02151
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1021/jacs.6c02151%22
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:46:59.637167Z'
  support: supports
  summary: 'Native metadata identifies Spatial Relations between Coccoliths and Their
    Confining Membrane During Crystal Morphogenesis. Authors: Avrahami EM, Karpov
    D, Aram L, Elad N, Safadi R, Rosenhek-Goldian I, Sui XM, de Haan D, Varsano N,
    Cohen SR, Zlotnikov I, Gal A.; PMID 41875313; DOI 10.1021/jacs.6c02151. Bibliographic
    identity and available abstract only; not a substitute for inspected article body.'
  snapshot_sha256: cb5a83a1be76d5c079cfdc3dfedfbaf99850f07b0ccddee828b4210354222e76
- evidence_id: coccolith-agent-doi-10.1093_pnasnexus_pgag104
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1093/pnasnexus/pgag104%22
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:46:59.705195Z'
  support: supports
  summary: 'Native metadata identifies Templateless crystallization of holococcolith
    crystals visualized by intracellular site-specific three-dimensional microscopy.
    Authors: Ben-Joseph O, Meng YF, Aram L, Abu Freha I, Lansky Z, Safadi R, de Haan
    D, Rechav K, Kaplan-Ashiri I, Varsano N, Gal A.; PMID 42005959; DOI 10.1093/pnasnexus/pgag104.
    Bibliographic identity and available abstract only; not a substitute for inspected
    article body.'
  snapshot_sha256: ff8b27a96f99ea4845e1d25d983e65f74434420824c1f994471da79c614a78a7
- evidence_id: coccolith-agent-doi-10.1126_sciadv.adc8728
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1126/sciadv.adc8728%22
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:46:59.707630Z'
  support: supports
  summary: 'Native metadata identifies Adsorptive exchange of coccolith biominerals
    facilitates viral infection. Authors: Johns CT, Bondoc-Naumovitz KG, Matthews
    A, Matson PG, Iglesias-Rodriguez MD, Taylor AR, Fuchs HL, Bidle KD.; PMID 36662866;
    DOI 10.1126/sciadv.adc8728. Bibliographic identity and available abstract only;
    not a substitute for inspected article body.'
  snapshot_sha256: fd7e42e22e587ba4629e6c56a65227e3130ce28e1ce6a5939b4fa99cf637932d
- evidence_id: coccolith-agent-jats-PMC13067266
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC13067266.1/PMC13067266.1.xml
  locator: 'PMC13067266: Introduction, complete Results including Figures1-5 captions,
    Discussion and Conclusions; exact article identity and JATS permissions/ALI CC
    BY4.0 URL. No raw tomography was reanalysed.'
  accessed_at: '2026-10-21T09:47:02.250454Z'
  support: supports
  summary: Avrahami et al.2026 distinguishes mature C.leptoporus scales from the intracellular
    formation vesicle. Figure1 and Results support the two-shield/stem morphology
    for this example. Luminal membrane particles in Figure4 remain unidentified and
    do not justify adding a full ATPase or vesicle transporters as mature-scale constituents.
    Morphogenesis control remains incompletely resolved.
  snapshot_sha256: c65411d5c5adb24f2e42120962c24d0fd3ecaffda72f9f485a728a313f2acdef
- evidence_id: coccolith-agent-avrahami2026-supp
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC13067266.1/ja6c02151_si_001.pdf
  locator: 'Actual supplementary PDF Materials/Methods: Cell cultures, Coccolith isolation
    for ex situ imaging, SEM, Correlative AFM/SEM; adjacent freeze-fracture and cryofixation
    preparation context. Supplementary Figures and downstream tomography processing
    were not fully audited.'
  accessed_at: '2026-10-21T09:48:11.208939Z'
  support: supports
  summary: Supplementary Methods identify RCC1130 and distinguish isolated/cleaned
    ex situ scales for SEM/AFM from cryofixed intracellular preparations. Figure1
    is not a cryotomography figure.
  snapshot_sha256: b919d05e8a48887245d56be37a7aa917366f68cdf058e6b742bae29d385a3248
- evidence_id: coccolith-agent-jats-PMC13089448
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC13089448.1/PMC13089448.1.xml
  locator: 'PMC13089448: Results paragraphs on mature structure, site-specific cryoET,
    crystal-scale distances/morphology and growth-condition effects; Discussion and
    Conclusion; Figure1/3/5 captions. Methods supplement and raw datasets were not
    analysed.'
  accessed_at: '2026-10-21T09:47:36.067259Z'
  support: supports
  summary: Ben-Joseph et al.2026 observes holococcolith calcite rhombohedra and organic
    base plates, with most intracellular crystals spatially separated from plates.
    Discussion cannot exclude undetected small nucleators and leaves crystal ordering
    unresolved. These observations justify avoiding a universal base-plate-templated
    mechanism.
  snapshot_sha256: 84016e30c9834977c7d3ab23851d8c595232e0b161027d97cf88556101007d30
- evidence_id: coccolith-agent-jats-PMC9858585
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC9858585.1/PMC9858585.1.xml
  locator: 'PMC9858585: Introduction as prior-work context; Results/Discussion Xenospheres
    result from adsorption, Free coccoliths alter calcification state, Adsorption
    mediated by organic matter (Figures1-3 captions), and Multifaceted ecological
    roles (Figure6 model); Methods Culture growth/maintenance, Coccolith isolation/treatment,
    Exogenous additions, SEM. Detailed virus-encounter modelling, raw data and supplementary
    videos were not independently analysed.'
  accessed_at: '2026-10-21T09:47:36.068366Z'
  support: supports
  summary: Johns et al.2023 directly distinguishes free scales, host-produced coverings
    and acquired scales. Calcified CCMP374 donors and naked recipients are separate
    preparations. Hypochlorite removal of associated organics reduces attachment while
    mineral morphology persists; this does not identify a receptor or test de novo
    assembly. Adsorption differs by morphotype and physiological/ecological effects
    remain contextual.
  snapshot_sha256: 560f029155372cb75ad9eaef3c7fd554da9c6d5d2a4f90c929eabed0648160a5
- evidence_id: coccolith-agent-image
  kind: record_content
  reference: data/images/envelope/coccolith/pmc13067266_fig1.jpg
  locator: 'Full Figure1 A-F: SEM cell/scales and diagram, AFM height images/projections.
    Figure1 caption and supplementary culture/isolation/SEM/AFM Methods read.'
  accessed_at: '2026-10-21T09:53:46.932000Z'
  support: supports
  summary: 'Full Figure1 pixels agree with the caption: SEM cell and scale views,
    diagram, and AFM maps/projections. AFM sampled regions are not whole-scale dimensions.
    Exact CC BY4.0 permissions and author attribution were checked against JATS and
    native metadata. Local SHA-256 matches the record; local MD5 30aa4e061b96edbf874a64bb6f8064e2
    matches the exact native PMC media entry.'
  snapshot_sha256: 35772c3d477f71c47c7c2e0d6e91fbd6086b9061126c7bee92cec70fcd95f939
- evidence_id: coccolith-agent-package-PMC13067266
  kind: database
  reference: https://pmc-oa-opendata.s3.amazonaws.com/metadata/PMC13067266.1.json
  locator: Complete article/package identity, license_code and matching media_urls
    entry
  accessed_at: '2026-10-21T09:47:02.445499Z'
  support: supports
  summary: PMC package version1 verifies exact DOI, title, PMCID, CC BY code and the
    media filename/MD5. The exact CC BY4.0 version is established from the separately
    inspected JATS permissions, not inferred from the abbreviated package code.
  snapshot_sha256: c0f3e27d29496c54202003a39fbd3ae7bd13a12d1e9dbc57e77bcdc05d8f4bc2
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/envelope/coccolith.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:44:14Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/envelope/coccolith.yaml'
  snapshot_sha256: 468001ba2370146e58844e78cfabdbec449c5d15b53895d2bffa08948f9e4673
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/envelope/coccolith.yaml --out /private/tmp/cellstructure-batch17-20261021-vub_b2nx/coccolith-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:44:16Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/envelope/coccolith.yaml\
    \ --out /private/tmp/cellstructure-batch17-20261021-vub_b2nx/coccolith-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch17-20261021-vub_b2nx/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch17-20261021-vub_b2nx/coccolith-strict.tsv"
  snapshot_sha256: 444730da2295fddeddd7ebfceb676dab1f6ea9bcff439ef4eaa1f5f037759537
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/envelope/coccolith.yaml; exact collect() scope; hash identifies
    the entire original resolver TSV
  accessed_at: '2026-10-21T09:56:44Z'
  support: supports
  summary: '7 of8 collected target identifiers returned OK in this fresh base resolver
    run. Residuals: cellstructuremech:coccolith: SKIPPED; resolved by evidence coccolith-agent-local-ids.
    Source-native identity checked separately.'
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
  topic: Individual mineral scale, distinct from covering and vesicle
  outcome: supported
  target_ids:
  - cellstructuremech:coccolith
  summary: The local identifier uniquely resolves to the maintained scale record.
    OTHER kind avoids calling one scale a continuous layer. The broad GO parent is
    appropriate, while vesicle, entire coccosphere and narrower holo-/heterococcolith
    types retain separate identities. No unconditional vesicle parthood or exclusively
    extracellular development is asserted.
  evidence_ids:
  - coccolith-agent-local-ids
  - coccolith-agent-go
  - coccolith-agent-jats-PMC13067266
  - coccolith-agent-jats-PMC13089448
  - coccolith-agent-jats-PMC9858585
  - record
- assessment_id: material
  area: grounding
  topic: Mineral grounding and unresolved organic chemistry
  outcome: supported
  target_ids:
  - cellstructuremech:coccolith
  summary: The calcite grounding is exact at mineral-material level. Associated organic
    material is experimentally supported, but oxidation and morphology do not identify
    one polymer or protein family. REVIEWED_LABEL_ONLY and UNKNOWN necessity correctly
    preserve that limit. Post-assembly persistence after oxidation does not establish
    dispensability for formation.
  evidence_ids:
  - coccolith-agent-chebi-46719
  - coccolith-agent-jats-PMC13067266
  - coccolith-agent-jats-PMC13089448
  - coccolith-agent-jats-PMC9858585
  - record
  - policy
- assessment_id: examples
  area: scope
  topic: Two species examples retain their experimental preparation
  outcome: supported
  target_ids:
  - cellstructuremech:coccolith
  summary: Native taxa match the named species. RCC1130 is established by the supplement;
    CCMP374 calcified donor identity is established separately from naked recipient
    cultures in Johns. No generic crystal count, size, shape, broad prevalence or
    single-morphotype adsorption rule is promoted.
  evidence_ids:
  - coccolith-agent-tax-127549
  - coccolith-agent-tax-2903
  - coccolith-agent-doi-10.1021_jacs.6c02151
  - coccolith-agent-doi-10.1093_pnasnexus_pgag104
  - coccolith-agent-doi-10.1126_sciadv.adc8728
  - coccolith-agent-jats-PMC13067266
  - coccolith-agent-avrahami2026-supp
  - coccolith-agent-jats-PMC9858585
  - record
- assessment_id: functions
  area: evidence
  topic: Covering element and scoped adsorption
  outcome: supported
  target_ids:
  - cellstructuremech:coccolith
  summary: Individual scales demonstrably contribute to an external covering. The
    adsorption function is limited to the tested E.huxleyi system and organic-removal
    comparison. The record does not infer universal adaptive protection, exact adhesion
    chemistry or nucleation-template mechanism.
  evidence_ids:
  - coccolith-agent-jats-PMC13067266
  - coccolith-agent-jats-PMC13089448
  - coccolith-agent-jats-PMC9858585
  - record
- assessment_id: image
  area: provenance
  topic: Exact image, license and preparation
  outcome: supported
  target_ids:
  - cellstructuremech:coccolith
  summary: The local unmodified Figure1 byte hashes, PMC accession and media locator
    agree. JATS licenses the article under CC BY4.0, and attribution agrees with author
    metadata. Mixed SEM/diagram/AFM content is explicitly described; species and sample
    preparation remain scoped.
  evidence_ids:
  - coccolith-agent-image
  - coccolith-agent-package-PMC13067266
  - coccolith-agent-jats-PMC13067266
  - coccolith-agent-avrahami2026-supp
  - coccolith-agent-doi-10.1021_jacs.6c02151
  - coccolith-agent-doi-10.1093_pnasnexus_pgag104
  - coccolith-agent-doi-10.1126_sciadv.adc8728
  - record
- assessment_id: coverage
  area: completeness
  topic: Boundaries and optional omissions are justified
  outcome: supported
  target_ids:
  - cellstructuremech:coccolith
  summary: No concrete corrective issue was observed. Unidentified vesicle particles
    are not imported as scale constituents; unresolved organic inventory and crystal-ordering
    mechanisms remain explicit. No causal graph, trait link or numeric property is
    required solely because the source contains one. No verbatim snippet or status
    promotion is present.
  evidence_ids:
  - coccolith-agent-jats-PMC13067266
  - coccolith-agent-jats-PMC13089448
  - coccolith-agent-jats-PMC9858585
  - record
  - policy
findings: []
actions: []
limitations:
- This is a record-level claim audit, not a reanalysis of microscopy volumes, AFM
  measurements, adsorption statistics or environmental samples.
- Primary read scope is the named main-text passages, captions and culture/SEM/AFM
  supplement sections. Holococcolith supplementary methods and Johns detailed virus-encounter
  model were not independently audited.
- Exact current GO-wide synonym absence and the historical curator searches were not
  reconstructed. The current repository-local identifiers were checked by ignored-inclusive
  exact-ID search; the broader GO authority is not asserted as exact equivalence.
- The mixed organic material remains chemically unresolved and assembly necessity
  remains UNKNOWN. No issue is inferred from optional missing inventory.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- The user-authorized coverage task requests a validated observation for every uncovered
  target, including clean records.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
