# Coccosphere covering identity, division evidence and image provenance review

- Review: 20261021T100146Z-coccosphere-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T09:44:17Z
- Finished UTC: 2026-10-21T10:01:46Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The whole-covering identity, scale parthood, materials, scoped division/separation evidence and licensed Figure2 are supported. No corrective issue was observed; chemistry, mechanism and source-analysis limits remain explicit.

## Scope And Provenance

Entire single maintained record, linked coccolith record and frozen image; native local-ID/GO/ChEBI/taxon identities and three primary sources at the declared claim scopes.

Selection: Tenth selected target in batch seventeen, fixed maintained-path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:coccosphere | data/structures/envelope/coccosphere.yaml | maintained | coccosphere |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | cellstructuremech:coccosphere | Focused validator passed. |
| Focused native strict | passed | True | cellstructuremech:coccosphere | Focused validator passed. |
| Target resolver slice | passed | True | cellstructuremech:coccosphere | 7 identifiers OK; 2 transport/skipped residuals independently resolved. |
| Claim-level scientific review | passed | True | cellstructuremech:coccosphere | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | cellstructuremech:coccosphere | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | cellstructuremech:coccosphere | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | cellstructuremech:coccosphere | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | cellstructuremech:coccosphere | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | cellstructuremech:coccosphere | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Whole covering and structural parthood

identity: supported. Targets: cellstructuremech:coccosphere.

The local coccosphere identity uniquely resolves. External encapsulating structure is a broader parent; has_part points to the separately frozen individual-scale record. Scale, whole covering, vesicle and organic matrix are kept distinct. ENVELOPE_LAYER does not assert exactly one geometric layer.

### Calcite and mixed extracellular material

grounding: supported. Targets: cellstructuremech:coccosphere.

Calcite is correctly grounded. The matrix is supported by lectin staining and retained pattern after decalcification but is not a chemically identified polymer or protein family. Label-only identity and UNKNOWN formation necessity are appropriate. Intracellular tubulin imaged during division is not thereby a constituent of the external covering.

### CS-369 and PLY182g contexts

scope: supported. Targets: cellstructuremech:coccosphere.

Taxon authorities match each species and the older C.pelagicus-subspecies name. Xu documents CS-369 and pooled light/CO2 conditions; Walker documents PLY182g. Counting assumptions, preparation, species differences and treatment context are accurately retained instead of promoting universal plate numbers or layer counts.

### Covering organization and daughter-cell separation

evidence: supported. Targets: cellstructuremech:coccosphere.

SEM supports the collective-covering function. Walker supports rearrangement during division and an association between disrupted covering and failure of daughter-cell separation in Ge/HEDP-treated C.braarudii. The record explicitly distinguishes this from failure of initial cytokinesis, low-Ca effects and universal calcification requirements; it retains confounding-treatment and adhesion-mechanism uncertainty.

### Scale origin and ecological boundaries

scope: supported. Targets: cellstructuremech:coccosphere.

Johns establishes adsorption from external donor scales, including mixed morphotypes/species. Structural has_part does not imply same-host biosynthesis. The record avoids treating every attached scale as a reconstructed covering or assigning a universal antiviral, grazing-protection or photosynthetic benefit.

### Exact SEM figure and source-specific license

provenance: supported. Targets: cellstructuremech:coccosphere.

Local Figure2 SHA-256 and media MD5 match the record and native PMC package. The source caption identifies white1micrometre bars and red neighboring counts. Culture/SEM preparation and estimated whole-sphere counts are correctly qualified. Full source-specific attribution satisfies the inspected CC BY4.0 statement.

### Supported boundaries with acknowledged unknowns

completeness: supported. Targets: cellstructuremech:coccosphere.

No concrete corrective issue was observed. Exact matrix chemistry, assembly mechanism, counts, causal graph and traits are not mandatory inventories. Omitted intracellular cytoskeleton is an explicit boundary decision, not a claim that it cannot affect division or trafficking. PROPOSED status and historical events remain unchanged.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/envelope/coccosphere.yaml; Entire maintained YAML including definition, components, functions, hierarchy, examples, graph edges, discussions, image metadata and history | context_only | All fields were read after fresh native inspection; the maintained target and PROPOSED state are unchanged. |
| policy | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, CausalNode and source-specific ComplexComposition contracts; essentiality definition; docs/CURATION.md assembly-versus-function guidance and review checklist | context_only | Component family identity, concrete protein identity and source-specific assembly membership are separate. Essentiality asks whether the structure forms without the component; membership and activity do not establish it. Optional fields are not mandatory. CausalNode permits protein complexes; its xrefs contract does not inherit the top-level record equivalence restriction. |
| coccosphere-agent-local-ids | rg --no-ignore --hidden -n --glob *.yaml ^identifier: cellstructuremech:(coccolith&#124;coccosphere)$ data/structures; Exact top-level identifier fields across maintained data/structures | supports | Exactly one maintained record defines cellstructuremech:coccolith and exactly one defines cellstructuremech:coccosphere. The target identity and, for coccosphere, the linked coccolith record were read and frozen as native inspection inputs. This resolves repository-local identifiers, not an external equivalence. |
| scale-input | data/structures/envelope/coccolith.yaml; Entire linked maintained record, frozen as an additional native inspect input | context_only | The linked record denotes an individual mineral scale and preserves its formation-vesicle/whole-covering distinction. Its text was read to resolve has_part, not treated as primary evidence for this covering biology. |
| coccosphere-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030312; Complete term definition, comment and child-relation scope | supports | GO0030312 identifies the broader external encapsulating structure outside the plasma membrane and surrounding a cell. It does not equate the specific coccosphere with all external walls or the organic matrix alone. |
| coccosphere-agent-chebi-46719 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/46719/; Released entry name, chemical data and ontology relationships | supports | CHEBI46719 is calcite, the mineral material of the covering scales. This exact chemical identity does not assert a fixed number of scales or an identified extracellular polymer. |
| coccosphere-agent-tax-2903 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2903; Complete taxId, scientificName, rank, lineage and relevant synonyms | supports | Native ENA taxonomy identifies Emiliania huxleyi, species. This receipt attests that identity and rank only, not occurrence or the experimental strain. |
| coccosphere-agent-tax-221442 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/221442; Complete taxId, scientificName, rank, lineage and relevant synonyms | supports | Native ENA taxonomy identifies Coccolithus braarudii, species; C.pelagicus subsp.braarudii is a synonym. This receipt attests that identity and rank only, not occurrence or the experimental strain. |
| coccosphere-agent-doi-10.7717_peerj.4608 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.7717/peerj.4608%22; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Coccolith arrangement follows Eulerian mathematics in the coccolithophore &lt;i&gt;Emiliania huxleyi&lt;/i&gt;. Authors: Xu K, Hutchins D, Gao K.; PMID 29666762; DOI 10.7717/peerj.4608. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| coccosphere-agent-doi-10.1111_nph.15272 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1111/nph.15272%22; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies The requirement for calcification differs between ecologically important coccolithophore species. Authors: Walker CE, Taylor AR, Langer G, Durak GM, Heath S, Probert I, Tyrrell T, Brownlee C, Wheeler GL.; PMID 29916209; DOI 10.1111/nph.15272. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| coccosphere-agent-doi-10.1126_sciadv.adc8728 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1126/sciadv.adc8728%22; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Adsorptive exchange of coccolith biominerals facilitates viral infection. Authors: Johns CT, Bondoc-Naumovitz KG, Matthews A, Matson PG, Iglesias-Rodriguez MD, Taylor AR, Fuchs HL, Bidle KD.; PMID 36662866; DOI 10.1126/sciadv.adc8728. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| coccosphere-agent-jats-PMC5896503 | https://pmc-oa-opendata.s3.amazonaws.com/PMC5896503.1/PMC5896503.1.xml; PMC5896503: complete Materials/Methods; Results Coccospheres contain only one layer, Number of bordering coccoliths per coccolith including Table1/Figure2 and simulation discussion; Assembliy processes of coccosphere and Conclusion. Exact JATS CC BY4.0 permissions and attribution requirements. Other detailed mathematical derivations and supplementary workbook were not recalculated. | supports | Xu, Hutchins and Gao2018 observes interlocking E.huxleyi CS-369 coverings. Methods pool culture conditions and estimate total scales by doubling visible fully interlocked plates under uniform-distribution assumptions. The one-layer statement is an operational interlocking definition; topology simulations and cellular sensing proposals are distinct from direct observation. |
| coccosphere-agent-jats-PMC6175242 | https://pmc-oa-opendata.s3.amazonaws.com/PMC6175242.1/PMC6175242.1.xml; PMC6175242: Methods sec0003 algal strains/culture, sec0005-0009 perturbations, sec0011 time-lapse, sec0012 fluorescence including in situ decalcification, sec0013 SEM; Results sec0019 photosynthesis, sec0020 division, sec0021 separation perturbations, sec0022 organic layer (Figures5-9 captions), complete sec0023 Discussion. Other growth Results, immunofluorescence Methods, movies and raw datasets were not fully audited. | supports | Walker et al.2018 directly observes C.braarudii covering rearrangement during division. Ge/HEDP perturbations produce persistent pairs with two nuclei and separate plasma membranes after initial cytokinesis; low-Ca inhibition differs. ConA-positive patterned extracellular material and contact-zone observations support an organizational role without identifying an adhesion molecule. Discussion retains possible additional treatment effects and species differences. |
| coccosphere-agent-jats-PMC9858585 | https://pmc-oa-opendata.s3.amazonaws.com/PMC9858585.1/PMC9858585.1.xml; PMC9858585: Introduction as prior-work context; Results/Discussion Xenospheres result from adsorption, Free coccoliths alter calcification state, Adsorption mediated by organic matter (Figures1-3 captions), and Multifaceted ecological roles (Figure6 model); Methods Culture growth/maintenance, Coccolith isolation/treatment, Exogenous additions, SEM. Detailed virus-encounter modelling, raw data and supplementary videos were not independently analysed. | supports | Johns et al.2023 directly distinguishes free scales, host-produced coverings and acquired scales. Calcified CCMP374 donors and naked recipients are separate preparations. Hypochlorite removal of associated organics reduces attachment while mineral morphology persists; this does not identify a receptor or test de novo assembly. Adsorption differs by morphotype and physiological/ecological effects remain contextual. |
| coccosphere-agent-image | data/images/envelope/coccosphere/pmc5896503_fig_2.jpg; Full Figure2 A-F: six SEM images of interlocking coverings, red neighboring-plate annotations and white1micrometre bars. Native Figure2 caption and culture/counting/SEM Methods read. | supports | Full Figure2 pixels show six SEM covering panels A-F with white1micrometre bars and red neighboring-plate labels. Native caption, exact CC BY4.0 JATS permission and source-specific author/title/journal/DOI attribution agree. Local SHA-256 matches the record; local MD5 f9e1e8ae4903f47abc657f2dc8098415 matches the exact native PMC media entry. |
| coccosphere-agent-package-PMC5896503 | https://pmc-oa-opendata.s3.amazonaws.com/metadata/PMC5896503.1.json; Complete article/package identity, license_code and matching media_urls entry | supports | PMC package version1 verifies exact DOI, title, PMCID, CC BY code and the media filename/MD5. The exact CC BY4.0 version is established from the separately inspected JATS permissions, not inferred from the abbreviated package code. |
| schema-result | just validate data/structures/envelope/coccosphere.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/envelope/coccosphere.yaml |
| strict-result | just validate-strict data/structures/envelope/coccosphere.yaml --out /private/tmp/cellstructure-batch17-20261021-vub_b2nx/coccosphere-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/envelope/coccosphere.yaml --out /private/tmp/cellstructure-batch17-20261021-vub_b2nx/coccosphere-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch17-20261021-vub_b2nx/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch17-20261021-vub_b2nx/coccosphere-strict.tsv |
| target-curies | just check-curies-strict; data/structures/envelope/coccosphere.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 7 of9 collected target identifiers returned OK in this fresh base resolver run. Residuals: cellstructuremech:coccolith: SKIPPED; resolved by evidence coccosphere-agent-local-ids; cellstructuremech:coccosphere: SKIPPED; resolved by evidence coccosphere-agent-local-ids. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- The reviewed primary text/caption/method scopes are explicit. Walker movies, all growth assays, immunofluorescence preparation and raw datasets were not reanalysed; its Figure5-9 captions and accompanying Results were read, but those figures were not separately pixel-audited here.
- Xu mathematical simulations and supplementary workbook were not independently recalculated. The review supports preservation of their assumptions, not universal correctness of the proposed geometric model.
- Historical ontology-search absence claims were not reconstructed. Exact repository-local definitions and the maintained coccolith dependency were verified with ignored-inclusive search and frozen inputs.
- Matrix molecular identity, precise adhesion mechanism and formation necessity remain unresolved as the record states. No clean result here implies exhaustive literature coverage.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The user-authorized coverage task requests a validated observation for every uncovered target, including clean records.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T100146Z-coccosphere-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Coccosphere covering identity, division evidence and image provenance review
started_at: '2026-10-21T09:44:17Z'
finished_at: '2026-10-21T10:01:46Z'
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
summary: The whole-covering identity, scale parthood, materials, scoped division/separation
  evidence and licensed Figure2 are supported. No corrective issue was observed; chemistry,
  mechanism and source-analysis limits remain explicit.
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
  - path: data/images/envelope/coccosphere/pmc5896503_fig_2.jpg
    sha256: 5f3b2473ff6c3e1e281c8ae71b4c2d72dd32536e8c9b80e08f761c72b0bff765
    role: context
  - path: data/structures/envelope/coccolith.yaml
    sha256: 8932b1ad635cf2e272c74fb8d4f00e6036b851ec2baa3daa3b5c3b52cc6979fa
    role: context
  - path: data/structures/envelope/coccosphere.yaml
    sha256: b72167a6093a734226fc2c9458c475f7a05120e8d2077d5f7b7007ee0a5cd299
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
- target_id: cellstructuremech:coccosphere
  path: data/structures/envelope/coccosphere.yaml
  label: coccosphere
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/envelope/coccosphere.yaml
    role: maintained scientific record
scope:
  description: Entire single maintained record, linked coccolith record and frozen
    image; native local-ID/GO/ChEBI/taxon identities and three primary sources at
    the declared claim scopes.
  selection: Tenth selected target in batch seventeen, fixed maintained-path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:coccosphere
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:coccosphere
  command: just validate data/structures/envelope/coccosphere.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:coccosphere
  command: just validate-strict data/structures/envelope/coccosphere.yaml --out /private/tmp/cellstructure-batch17-20261021-vub_b2nx/coccosphere-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - cellstructuremech:coccosphere
  summary: 7 identifiers OK; 2 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - coccosphere-agent-local-ids
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:coccosphere
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - coccosphere-agent-local-ids
  - scale-input
  - coccosphere-agent-go
  - coccosphere-agent-chebi-46719
  - coccosphere-agent-tax-2903
  - coccosphere-agent-tax-221442
  - coccosphere-agent-doi-10.7717_peerj.4608
  - coccosphere-agent-doi-10.1111_nph.15272
  - coccosphere-agent-doi-10.1126_sciadv.adc8728
  - coccosphere-agent-jats-PMC5896503
  - coccosphere-agent-jats-PMC6175242
  - coccosphere-agent-jats-PMC9858585
  - coccosphere-agent-image
  - coccosphere-agent-package-PMC5896503
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:coccosphere
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
  - cellstructuremech:coccosphere
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
  - cellstructuremech:coccosphere
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
  - cellstructuremech:coccosphere
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
  - cellstructuremech:coccosphere
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
  reference: data/structures/envelope/coccosphere.yaml
  locator: Entire maintained YAML including definition, components, functions, hierarchy,
    examples, graph edges, discussions, image metadata and history
  accessed_at: '2026-10-21T09:56:47Z'
  support: context_only
  summary: All fields were read after fresh native inspection; the maintained target
    and PROPOSED state are unchanged.
- evidence_id: policy
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, CausalNode and source-specific ComplexComposition
    contracts; essentiality definition; docs/CURATION.md assembly-versus-function
    guidance and review checklist
  accessed_at: '2026-10-21T09:56:47Z'
  support: context_only
  summary: Component family identity, concrete protein identity and source-specific
    assembly membership are separate. Essentiality asks whether the structure forms
    without the component; membership and activity do not establish it. Optional fields
    are not mandatory. CausalNode permits protein complexes; its xrefs contract does
    not inherit the top-level record equivalence restriction.
- evidence_id: coccosphere-agent-local-ids
  kind: search
  reference: 'rg --no-ignore --hidden -n --glob *.yaml ^identifier: cellstructuremech:(coccolith|coccosphere)$
    data/structures'
  locator: Exact top-level identifier fields across maintained data/structures
  accessed_at: '2026-10-21T09:49:35.110863Z'
  support: supports
  summary: Exactly one maintained record defines cellstructuremech:coccolith and exactly
    one defines cellstructuremech:coccosphere. The target identity and, for coccosphere,
    the linked coccolith record were read and frozen as native inspection inputs.
    This resolves repository-local identifiers, not an external equivalence.
  snapshot_sha256: c5d1a782c2869d127fc98502ed00b6b7901499b1952a7ffe7f3993910a372d0c
  search_scope: Entire data/structures, including ignored and hidden YAML files; exact
    anchored identifiers only.
- evidence_id: scale-input
  kind: record_content
  reference: data/structures/envelope/coccolith.yaml
  locator: Entire linked maintained record, frozen as an additional native inspect
    input
  accessed_at: '2026-10-21T09:56:47Z'
  support: context_only
  summary: The linked record denotes an individual mineral scale and preserves its
    formation-vesicle/whole-covering distinction. Its text was read to resolve has_part,
    not treated as primary evidence for this covering biology.
- evidence_id: coccosphere-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030312
  locator: Complete term definition, comment and child-relation scope
  accessed_at: '2026-10-21T09:47:00.531146Z'
  support: supports
  summary: GO0030312 identifies the broader external encapsulating structure outside
    the plasma membrane and surrounding a cell. It does not equate the specific coccosphere
    with all external walls or the organic matrix alone.
  snapshot_sha256: ab65d98850dd6a2845a8b4697a5ad61328ce31f453366335f7b30b44e62ab6b6
- evidence_id: coccosphere-agent-chebi-46719
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/46719/
  locator: Released entry name, chemical data and ontology relationships
  accessed_at: '2026-10-21T09:47:01.596726Z'
  support: supports
  summary: CHEBI46719 is calcite, the mineral material of the covering scales. This
    exact chemical identity does not assert a fixed number of scales or an identified
    extracellular polymer.
  snapshot_sha256: 2012a33c8e9e7d723675c94c04b56a2c8ea7dfd1a36c8f637500bfc172fe6053
- evidence_id: coccosphere-agent-tax-2903
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2903
  locator: Complete taxId, scientificName, rank, lineage and relevant synonyms
  accessed_at: '2026-10-21T09:47:00.612730Z'
  support: supports
  summary: Native ENA taxonomy identifies Emiliania huxleyi, species. This receipt
    attests that identity and rank only, not occurrence or the experimental strain.
  snapshot_sha256: e66e5ff5bd50e8c2736f1d3bd7afd7d27b8c62ef753454708067bc1c1ef9af22
- evidence_id: coccosphere-agent-tax-221442
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/221442
  locator: Complete taxId, scientificName, rank, lineage and relevant synonyms
  accessed_at: '2026-10-21T09:47:00.610592Z'
  support: supports
  summary: Native ENA taxonomy identifies Coccolithus braarudii, species; C.pelagicus
    subsp.braarudii is a synonym. This receipt attests that identity and rank only,
    not occurrence or the experimental strain.
  snapshot_sha256: 86cd1d58d7ed04eff71d8d5aa520bc80771da9f7066eea0722f916fc521e5b4f
- evidence_id: coccosphere-agent-doi-10.7717_peerj.4608
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.7717/peerj.4608%22
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:47:01.218809Z'
  support: supports
  summary: 'Native metadata identifies Coccolith arrangement follows Eulerian mathematics
    in the coccolithophore <i>Emiliania huxleyi</i>. Authors: Xu K, Hutchins D, Gao
    K.; PMID 29666762; DOI 10.7717/peerj.4608. Bibliographic identity and available
    abstract only; not a substitute for inspected article body.'
  snapshot_sha256: a16d33329068b76cc1977dcc86925dc82ca894b25e772d569c77d8646409ad03
- evidence_id: coccosphere-agent-doi-10.1111_nph.15272
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1111/nph.15272%22
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:47:00.801194Z'
  support: supports
  summary: 'Native metadata identifies The requirement for calcification differs between
    ecologically important coccolithophore species. Authors: Walker CE, Taylor AR,
    Langer G, Durak GM, Heath S, Probert I, Tyrrell T, Brownlee C, Wheeler GL.; PMID
    29916209; DOI 10.1111/nph.15272. Bibliographic identity and available abstract
    only; not a substitute for inspected article body.'
  snapshot_sha256: ce3ef948e83d0a2c20cb357f669f39d3380603af412e2a52accd46f48705f734
- evidence_id: coccosphere-agent-doi-10.1126_sciadv.adc8728
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1126/sciadv.adc8728%22
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:47:01.137241Z'
  support: supports
  summary: 'Native metadata identifies Adsorptive exchange of coccolith biominerals
    facilitates viral infection. Authors: Johns CT, Bondoc-Naumovitz KG, Matthews
    A, Matson PG, Iglesias-Rodriguez MD, Taylor AR, Fuchs HL, Bidle KD.; PMID 36662866;
    DOI 10.1126/sciadv.adc8728. Bibliographic identity and available abstract only;
    not a substitute for inspected article body.'
  snapshot_sha256: 20a1f09fbab45fd3a6c2164af6dfc37998b1551ea76baaee9592a20b7d876209
- evidence_id: coccosphere-agent-jats-PMC5896503
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5896503.1/PMC5896503.1.xml
  locator: 'PMC5896503: complete Materials/Methods; Results Coccospheres contain only
    one layer, Number of bordering coccoliths per coccolith including Table1/Figure2
    and simulation discussion; Assembliy processes of coccosphere and Conclusion.
    Exact JATS CC BY4.0 permissions and attribution requirements. Other detailed mathematical
    derivations and supplementary workbook were not recalculated.'
  accessed_at: '2026-10-21T09:47:02.450764Z'
  support: supports
  summary: Xu, Hutchins and Gao2018 observes interlocking E.huxleyi CS-369 coverings.
    Methods pool culture conditions and estimate total scales by doubling visible
    fully interlocked plates under uniform-distribution assumptions. The one-layer
    statement is an operational interlocking definition; topology simulations and
    cellular sensing proposals are distinct from direct observation.
  snapshot_sha256: 1cacc8199b6eef01b6199bbb1bc94a72f351908023aa776071e40db8d1b9606a
- evidence_id: coccosphere-agent-jats-PMC6175242
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6175242.1/PMC6175242.1.xml
  locator: 'PMC6175242: Methods sec0003 algal strains/culture, sec0005-0009 perturbations,
    sec0011 time-lapse, sec0012 fluorescence including in situ decalcification, sec0013
    SEM; Results sec0019 photosynthesis, sec0020 division, sec0021 separation perturbations,
    sec0022 organic layer (Figures5-9 captions), complete sec0023 Discussion. Other
    growth Results, immunofluorescence Methods, movies and raw datasets were not fully
    audited.'
  accessed_at: '2026-10-21T09:47:36.068869Z'
  support: supports
  summary: Walker et al.2018 directly observes C.braarudii covering rearrangement
    during division. Ge/HEDP perturbations produce persistent pairs with two nuclei
    and separate plasma membranes after initial cytokinesis; low-Ca inhibition differs.
    ConA-positive patterned extracellular material and contact-zone observations support
    an organizational role without identifying an adhesion molecule. Discussion retains
    possible additional treatment effects and species differences.
  snapshot_sha256: 9c69e3449019fc71795394ac8771c330504f62aeb849f1234a8339a1e3fc0dba
- evidence_id: coccosphere-agent-jats-PMC9858585
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC9858585.1/PMC9858585.1.xml
  locator: 'PMC9858585: Introduction as prior-work context; Results/Discussion Xenospheres
    result from adsorption, Free coccoliths alter calcification state, Adsorption
    mediated by organic matter (Figures1-3 captions), and Multifaceted ecological
    roles (Figure6 model); Methods Culture growth/maintenance, Coccolith isolation/treatment,
    Exogenous additions, SEM. Detailed virus-encounter modelling, raw data and supplementary
    videos were not independently analysed.'
  accessed_at: '2026-10-21T09:47:36.639823Z'
  support: supports
  summary: Johns et al.2023 directly distinguishes free scales, host-produced coverings
    and acquired scales. Calcified CCMP374 donors and naked recipients are separate
    preparations. Hypochlorite removal of associated organics reduces attachment while
    mineral morphology persists; this does not identify a receptor or test de novo
    assembly. Adsorption differs by morphotype and physiological/ecological effects
    remain contextual.
  snapshot_sha256: 560f029155372cb75ad9eaef3c7fd554da9c6d5d2a4f90c929eabed0648160a5
- evidence_id: coccosphere-agent-image
  kind: record_content
  reference: data/images/envelope/coccosphere/pmc5896503_fig_2.jpg
  locator: 'Full Figure2 A-F: six SEM images of interlocking coverings, red neighboring-plate
    annotations and white1micrometre bars. Native Figure2 caption and culture/counting/SEM
    Methods read.'
  accessed_at: '2026-10-21T09:53:46.932000Z'
  support: supports
  summary: Full Figure2 pixels show six SEM covering panels A-F with white1micrometre
    bars and red neighboring-plate labels. Native caption, exact CC BY4.0 JATS permission
    and source-specific author/title/journal/DOI attribution agree. Local SHA-256
    matches the record; local MD5 f9e1e8ae4903f47abc657f2dc8098415 matches the exact
    native PMC media entry.
  snapshot_sha256: 5f3b2473ff6c3e1e281c8ae71b4c2d72dd32536e8c9b80e08f761c72b0bff765
- evidence_id: coccosphere-agent-package-PMC5896503
  kind: database
  reference: https://pmc-oa-opendata.s3.amazonaws.com/metadata/PMC5896503.1.json
  locator: Complete article/package identity, license_code and matching media_urls
    entry
  accessed_at: '2026-10-21T09:47:02.461894Z'
  support: supports
  summary: PMC package version1 verifies exact DOI, title, PMCID, CC BY code and the
    media filename/MD5. The exact CC BY4.0 version is established from the separately
    inspected JATS permissions, not inferred from the abbreviated package code.
  snapshot_sha256: f40beaf82ceab05c10bc9aafe2cfe53281ccf87903430bba9d58f5358eb51103
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/envelope/coccosphere.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:44:19Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/envelope/coccosphere.yaml'
  snapshot_sha256: b7bee934d67eba2cc811bf8239a8e9e149afcf2a0a5cefd0348e4cba38e9e255
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/envelope/coccosphere.yaml --out
    /private/tmp/cellstructure-batch17-20261021-vub_b2nx/coccosphere-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:44:21Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/envelope/coccosphere.yaml\
    \ --out /private/tmp/cellstructure-batch17-20261021-vub_b2nx/coccosphere-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch17-20261021-vub_b2nx/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch17-20261021-vub_b2nx/coccosphere-strict.tsv"
  snapshot_sha256: f1dba22aee985d4a047c54476c18e5bee46ab0786dd5206bc7eb5a12d417c491
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/envelope/coccosphere.yaml; exact collect() scope; hash
    identifies the entire original resolver TSV
  accessed_at: '2026-10-21T09:56:47Z'
  support: supports
  summary: '7 of9 collected target identifiers returned OK in this fresh base resolver
    run. Residuals: cellstructuremech:coccolith: SKIPPED; resolved by evidence coccosphere-agent-local-ids;
    cellstructuremech:coccosphere: SKIPPED; resolved by evidence coccosphere-agent-local-ids.
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
  topic: Whole covering and structural parthood
  outcome: supported
  target_ids:
  - cellstructuremech:coccosphere
  summary: The local coccosphere identity uniquely resolves. External encapsulating
    structure is a broader parent; has_part points to the separately frozen individual-scale
    record. Scale, whole covering, vesicle and organic matrix are kept distinct. ENVELOPE_LAYER
    does not assert exactly one geometric layer.
  evidence_ids:
  - coccosphere-agent-local-ids
  - scale-input
  - coccosphere-agent-go
  - coccosphere-agent-jats-PMC5896503
  - coccosphere-agent-jats-PMC6175242
  - coccosphere-agent-jats-PMC9858585
  - record
- assessment_id: components
  area: grounding
  topic: Calcite and mixed extracellular material
  outcome: supported
  target_ids:
  - cellstructuremech:coccosphere
  summary: Calcite is correctly grounded. The matrix is supported by lectin staining
    and retained pattern after decalcification but is not a chemically identified
    polymer or protein family. Label-only identity and UNKNOWN formation necessity
    are appropriate. Intracellular tubulin imaged during division is not thereby a
    constituent of the external covering.
  evidence_ids:
  - coccosphere-agent-chebi-46719
  - coccosphere-agent-jats-PMC6175242
  - record
  - policy
- assessment_id: examples
  area: scope
  topic: CS-369 and PLY182g contexts
  outcome: supported
  target_ids:
  - cellstructuremech:coccosphere
  summary: Taxon authorities match each species and the older C.pelagicus-subspecies
    name. Xu documents CS-369 and pooled light/CO2 conditions; Walker documents PLY182g.
    Counting assumptions, preparation, species differences and treatment context are
    accurately retained instead of promoting universal plate numbers or layer counts.
  evidence_ids:
  - coccosphere-agent-tax-2903
  - coccosphere-agent-tax-221442
  - coccosphere-agent-doi-10.7717_peerj.4608
  - coccosphere-agent-doi-10.1111_nph.15272
  - coccosphere-agent-doi-10.1126_sciadv.adc8728
  - coccosphere-agent-jats-PMC5896503
  - coccosphere-agent-jats-PMC6175242
  - record
- assessment_id: functions
  area: evidence
  topic: Covering organization and daughter-cell separation
  outcome: supported
  target_ids:
  - cellstructuremech:coccosphere
  summary: SEM supports the collective-covering function. Walker supports rearrangement
    during division and an association between disrupted covering and failure of daughter-cell
    separation in Ge/HEDP-treated C.braarudii. The record explicitly distinguishes
    this from failure of initial cytokinesis, low-Ca effects and universal calcification
    requirements; it retains confounding-treatment and adhesion-mechanism uncertainty.
  evidence_ids:
  - coccosphere-agent-jats-PMC5896503
  - coccosphere-agent-jats-PMC6175242
  - record
- assessment_id: acquisition
  area: scope
  topic: Scale origin and ecological boundaries
  outcome: supported
  target_ids:
  - cellstructuremech:coccosphere
  summary: Johns establishes adsorption from external donor scales, including mixed
    morphotypes/species. Structural has_part does not imply same-host biosynthesis.
    The record avoids treating every attached scale as a reconstructed covering or
    assigning a universal antiviral, grazing-protection or photosynthetic benefit.
  evidence_ids:
  - coccosphere-agent-jats-PMC9858585
  - coccosphere-agent-jats-PMC6175242
  - record
- assessment_id: image
  area: provenance
  topic: Exact SEM figure and source-specific license
  outcome: supported
  target_ids:
  - cellstructuremech:coccosphere
  summary: Local Figure2 SHA-256 and media MD5 match the record and native PMC package.
    The source caption identifies white1micrometre bars and red neighboring counts.
    Culture/SEM preparation and estimated whole-sphere counts are correctly qualified.
    Full source-specific attribution satisfies the inspected CC BY4.0 statement.
  evidence_ids:
  - coccosphere-agent-image
  - coccosphere-agent-package-PMC5896503
  - coccosphere-agent-jats-PMC5896503
  - coccosphere-agent-doi-10.7717_peerj.4608
  - coccosphere-agent-doi-10.1111_nph.15272
  - coccosphere-agent-doi-10.1126_sciadv.adc8728
  - record
- assessment_id: coverage
  area: completeness
  topic: Supported boundaries with acknowledged unknowns
  outcome: supported
  target_ids:
  - cellstructuremech:coccosphere
  summary: No concrete corrective issue was observed. Exact matrix chemistry, assembly
    mechanism, counts, causal graph and traits are not mandatory inventories. Omitted
    intracellular cytoskeleton is an explicit boundary decision, not a claim that
    it cannot affect division or trafficking. PROPOSED status and historical events
    remain unchanged.
  evidence_ids:
  - coccosphere-agent-jats-PMC5896503
  - coccosphere-agent-jats-PMC6175242
  - coccosphere-agent-jats-PMC9858585
  - record
  - policy
findings: []
actions: []
limitations:
- The reviewed primary text/caption/method scopes are explicit. Walker movies, all
  growth assays, immunofluorescence preparation and raw datasets were not reanalysed;
  its Figure5-9 captions and accompanying Results were read, but those figures were
  not separately pixel-audited here.
- Xu mathematical simulations and supplementary workbook were not independently recalculated.
  The review supports preservation of their assumptions, not universal correctness
  of the proposed geometric model.
- Historical ontology-search absence claims were not reconstructed. Exact repository-local
  definitions and the maintained coccolith dependency were verified with ignored-inclusive
  search and frozen inputs.
- Matrix molecular identity, precise adhesion mechanism and formation necessity remain
  unresolved as the record states. No clean result here implies exhaustive literature
  coverage.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- The user-authorized coverage task requests a validated observation for every uncovered
  target, including clean records.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
