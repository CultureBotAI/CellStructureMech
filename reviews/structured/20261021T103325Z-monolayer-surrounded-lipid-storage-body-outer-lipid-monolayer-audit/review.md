# Inclusion identity, composition and evidence review

- Review: 20261021T103325Z-monolayer-surrounded-lipid-storage-body-outer-lipid-monolayer-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T10:13:29Z
- Finished UTC: 2026-10-21T10:33:25Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The outer-monolayer identity, chemical grounding, bounded yeast example and descriptive topology are supported. No concrete curation finding was observed; source-access and individual formation-necessity limits remain explicit.

## Scope And Provenance

Entire single record with exact authority identities, declared source-reading scopes, protein checks where applicable and component/function/graph boundaries.

Selection: Target 8 in batch nineteen; exact sorted uncovered path at frozen fresh-main revision.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0034430 | data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml | maintained | monolayer-surrounded lipid storage body outer lipid monolayer |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0034430 | Focused validator passed. |
| Focused native strict | passed | True | GO:0034430 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0034430 | 7 identifiers OK; 1 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | GO:0034430 | No expression-module or transcriptomic inference is made by this structural review. |
| Claim-level scientific review | passed | True | GO:0034430 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0034430 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0034430 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0034430 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0034430 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0034430 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Outer monolayer separated from whole storage bodies

identity: supported. Targets: GO:0034430.

Exact identity, all synonym types and the membrane kind are supported. The phospholipid surface is a part of the containing droplet rather than the whole neutral-lipid inclusion. Synonym import does not assert experimental coverage of every named organism or plastoglobule boundary.

### Correct chemical class and explicit protein boundary

grounding: supported. Targets: GO:0034430.

CHEBI16247 exactly denotes phospholipid, matching the class-level component and graph node. The monolayer record intentionally represents lipid material; associated proteins can occur on the containing organelle without becoming equivalent to the lipid layer. No obligatory individual lipid species or comprehensive proteome is implied.

### Defining collective layer versus individual molecular requirements

evidence: unknown. Targets: GO:0034430.

The collective phospholipid layer constitutes the defined target. This does not demonstrate that every phospholipid class or species is individually required to form that layer. The reviewed lipidomics documents conditional composition, not a universal molecular-removal experiment; individual formation necessity is left unknown without inventing a corrective issue.

### Yeast evidence retained at species and condition scope

scope: supported. Targets: GO:0034430.

The native taxon identifies S.cerevisiae. The primary study uses BY4741 and listed GFP strains under specified carbon-source conditions; the maintained example remains a species-level model claim and does not prescribe fixed composition. COMMON is qualitative, not a newly measured prevalence.

### Mature surface topology with appropriate nonmechanistic status

graph: supported. Targets: GO:0034430.

The three graph edges describe phospholipid-layer constitution, parthood and enclosure of the hydrophobic core. NONMECHANISTIC and its explicit scope note appropriately exclude ER budding, insertion, growth and lipolysis mechanisms. Surface compartmentalization and associated proteins are directly supported at the stated source tiers.

### Non-yeast extension is deliberately unresolved

scope: supported. Targets: GO:0034430.

The open discussion identifies oil-body and plastoglobule boundaries before taxonomic expansion. Austin abstract supports observed half-bilayer continuity in the tested chloroplast systems; it is not converted into an algal universal. Leaving this as a bounded question is appropriate rather than a missing mandatory inventory.

### Bounded record-level coverage

completeness: supported. Targets: GO:0034430.

The entire maintained record and cited claim contexts were inspected at the stated source scopes. Exact additional polymer inventories, numerical properties, images, traits and expanded mechanisms are optional. No verbatim quotation requires repair, and no status or history rewrite is proposed. A clean result does not assert exhaustive literature completeness.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml; Entire maintained YAML including history, all evidence notes, components, functions, graph edges and discussions | context_only | All maintained fields were read. No scientific edit or mapping-status promotion is made. |
| policy | docs/CURATION.md; Exact identity, claim-level evidence, material versus localization grounding, and component assembly-essentiality contract | context_only | Family identity, concrete protein examples and structure membership are separate; activity and viability are not by themselves formation assays. Optional inventories are not mandatory. |
| root19-sources-lipid-monolayer-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005811,GO:0034430; Both complete definitions, comments, synonyms and returned relations | supports | The exact GO target and all five synonym scopes match; its definition is a single phospholipid layer. GO0005811 identifies the containing lipid droplet and its monolayer/protein distinction. The maintained spelling fixes the authority typo without changing meaning. |
| root19-sources-CHEBI-16247 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/16247/; Exact accession, name, definition where present, synonyms and chemical-class relations | supports | Released three-star CHEBI:16247 identifies phospholipid. Its chemical-class identity and returned definition/ontology relations are assessed independently of placement in a wall or membrane. |
| root19-sources-NCBITaxon-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Exact taxId, scientificName, rank, lineage and relevant alternative names | supports | Native ENA taxonomy identifies Saccharomyces cerevisiae at species rank. Only this taxon's identity and names are asserted by this row, not occurrence or experimental stock identity. |
| root19-sources-doi-10.1007_s00018-015-1903-5 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1007/s00018-015-1903-5; Exact native title, authors, year, source MED, DOI/PMID and abstract fields | supports | Native citation identifies Lipid droplet dynamics in budding yeast. PMID 25894691; DOI 10.1007/s00018-015-1903-5. Exact bibliographic fields and the complete returned abstract were inspected; this row does not attest a full-text read. |
| root19-sources-PMID-29397034 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A29397034%20AND%20SRC%3AMED; Exact native title, authors, year, source MED, DOI/PMID and abstract fields | supports | Native citation identifies Lipid droplet-mediated lipid and protein homeostasis in budding yeast. PMID 29397034; DOI 10.1002/1873-3468.12996. Exact bibliographic fields and the complete returned abstract were inspected; this row does not attest a full-text read. |
| root19-sources-doi-10.1016_j.bbalip.2011.07.015 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.bbalip.2011.07.015; Exact native title, authors, year, source MED, DOI/PMID and abstract fields | supports | Native citation identifies Lipid particles/droplets of the yeast Saccharomyces cerevisiae revisited: lipidome meets proteome. PMID 21820081; DOI 10.1016/j.bbalip.2011.07.015. Exact bibliographic fields and the complete returned abstract were inspected; this row does not attest a full-text read. |
| root19-sources-doi-10.1105_tpc.105.039859 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1105/tpc.105.039859; Exact native title, authors, year, source MED, DOI/PMID and abstract fields | supports | Native citation identifies Plastoglobules are lipoprotein subcompartments of the chloroplast that are permanently coupled to thylakoid membranes and contain biosynthetic enzymes. PMID 16731586; DOI 10.1105/tpc.105.039859. Exact bibliographic fields and the complete returned abstract were inspected; this row does not attest a full-text read. |
| root19-sources-jats-PMC5947121 | https://pmc-oa-opendata.s3.amazonaws.com/PMC5947121.1/PMC5947121.1.xml; Complete direct text of feb212996-sec-0002 and feb212996-sec-0003, including Figure1 caption but excluding nested protein-machinery subsections; remaining review not audited. | supports | Graef2018 describes neutral TAG/SE cores enclosed by one phospholipid leaflet and variable lipid/protein composition. Its biogenesis introduction distinguishes the mature surface from proposed ER-origin mechanisms. The record does not import those mechanisms. |
| root19-sources-jats-PMC3229976 | https://pmc-oa-opendata.s3.amazonaws.com/PMC3229976.1/PMC3229976.1.xml; Introduction s0005; Methods s0015/s0020/s0030 and strain Table1 t0005; Results s0055/s0060. No complete proteomics section, all tables or raw spectra reanalysis. | supports | Grillitsch2011 Introduction describes the phospholipid monolayer and associated surface proteins as cited background. The study directly supports a yeast lipid-particle example and fraction-lipidomics measurements: Methods identify stationary-phase glucose/oleate cultures and fractionation/lipid analysis; Results and Table1 show class and molecular-species variation. Fraction lipidomics is not direct imaging of each leaflet or proof of one universally required phospholipid species. |
| root19-sources-wang2015-publisher | https://link.springer.com/article/10.1007/s00018-015-1903-5; Publisher Abs1-section/Abs1-content complete abstract and access-page boundary; full review body not available | context_only | The publisher supplied metadata and an abstract/access page, not the Wang review body. Its abstract supports budding-yeast lipid-droplet context but does not independently expose the monolayer sentence. Direct topical corroboration comes from the separately cited Graef body and Grillitsch primary study. |
| root19-sources-legacy-PMC11113813 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11113813/; Actual source-access response, not article content | context_only | The PMC route returned a browser challenge, not the Wang full text. |
| root19-sources-legacy-PMC1488921 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1488921/; Actual source-access response, not article content | context_only | The PMC route returned a browser challenge. Austin2006 is checked through its exact native metadata and complete abstract, whose direct half-bilayer/thylakoid statement supports the bounded open discussion. |
| lipid-neighbor | data/structures/inclusion/lipid_droplet.yaml; Identity, definition, kind, parents/parthood, components and discussions fields | context_only | The containing droplet has a neutral-lipid core; its definition permits associated proteins. It is not equivalent to the isolated outer monolayer. |
| plastoglobule-neighbor | data/structures/inclusion/plastoglobule.yaml; Identity, definition, kind, parents/parthood, components and discussions fields | context_only | The plastoglobule record distinguishes higher-plant thylakoid continuity from the algal evidence. This boundary context was inspected without conducting a separate review of its sources. |
| schema-result | just validate data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml |
| strict-result | just validate-strict data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml --out /private/tmp/cellstructure-batch19-20261021-9bkzflrr/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml --out /private/tmp/cellstructure-batch19-20261021-9bkzflrr/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch19-20261021-9bkzflrr/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer-strict.tsv |
| target-curies | just check-curies-strict; data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 7 of8 collected target identifiers returned OK in this fresh base resolver run. Residuals: PMID:29397034: UNREACHABLE; resolved by evidence root19-sources-PMID-29397034. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Wang2015 full text was not recovered: its publisher response is an abstract/access page and PMC supplied a browser challenge. Exact monolayer attribution in that inaccessible body remains unchecked; the same coarse claim is directly supported in the separately cited Graef and Grillitsch texts.
- Austin2006 was read at exact native metadata and complete abstract scope, not its body, images or raw tomography. The existing open non-yeast boundary question is preserved.
- Graef and Grillitsch were read only at the declared sections. No comprehensive species inventory, protein census, raw lipidomics or individual-component formation assay is claimed.
- Neighbor records were inspected only at the declared boundary fields; their experimental claims and histories are not independently reviewed in this bundle.
- No raw microscopy or quantitative datasets were reanalysed. Historical curator searches and independent historical authorship are not certified.
- The completed fresh-base batch15 global gates are attached only at finalization; identifier transport and label-adapter limits remain explicit.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The user explicitly authorized one review for every uncovered target, including a review with no findings. Only this review bundle is intended for persistence.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T103325Z-monolayer-surrounded-lipid-storage-body-outer-lipid-monolayer-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Inclusion identity, composition and evidence review
started_at: '2026-10-21T10:13:29Z'
finished_at: '2026-10-21T10:33:25Z'
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
summary: The outer-monolayer identity, chemical grounding, bounded yeast example and
  descriptive topology are supported. No concrete curation finding was observed; source-access
  and individual formation-necessity limits remain explicit.
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
  - path: data/structures/inclusion/lipid_droplet.yaml
    sha256: 379b5b516486c6bc55055e3289a565c7854b3088a5c13ebe6f614df5c1688a7a
    role: context
  - path: data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml
    sha256: d72e9789b2d49d4fe380c06834e31dfe9eaf46fb6a412ddecdc9c8e1742b7a87
    role: target
  - path: data/structures/inclusion/plastoglobule.yaml
    sha256: ba5f8ac9dd4b54fefc917e1d6ed8587fdabdb2cf6152f1e331511bfc8ee38027
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
  - path: scripts/score_causal_graphs.py
    sha256: 5ffe450c5b37c3dc3b0e62672caf0d99b358c8249fcc98a8c4fc7d78e8cd0d2f
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: GO:0034430
  path: data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml
  label: monolayer-surrounded lipid storage body outer lipid monolayer
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml
    role: maintained scientific record
scope:
  description: Entire single record with exact authority identities, declared source-reading
    scopes, protein checks where applicable and component/function/graph boundaries.
  selection: Target 8 in batch nineteen; exact sorted uncovered path at frozen fresh-main
    revision.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0034430
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0034430
  command: just validate data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0034430
  command: just validate-strict data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml
    --out /private/tmp/cellstructure-batch19-20261021-9bkzflrr/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0034430
  summary: 7 identifiers OK; 1 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - root19-sources-PMID-29397034
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0034430
  summary: No expression-module or transcriptomic inference is made by this structural
    review.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0034430
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - root19-sources-lipid-monolayer-go
  - root19-sources-CHEBI-16247
  - root19-sources-NCBITaxon-4932
  - root19-sources-doi-10.1007_s00018-015-1903-5
  - root19-sources-PMID-29397034
  - root19-sources-doi-10.1016_j.bbalip.2011.07.015
  - root19-sources-doi-10.1105_tpc.105.039859
  - root19-sources-jats-PMC5947121
  - root19-sources-jats-PMC3229976
  - root19-sources-wang2015-publisher
  - root19-sources-legacy-PMC11113813
  - root19-sources-legacy-PMC1488921
  - lipid-neighbor
  - plastoglobule-neighbor
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0034430
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
  - GO:0034430
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
  - GO:0034430
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
  - GO:0034430
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
  - GO:0034430
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
  reference: data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml
  locator: Entire maintained YAML including history, all evidence notes, components,
    functions, graph edges and discussions
  accessed_at: '2026-10-21T10:21:17Z'
  support: context_only
  summary: All maintained fields were read. No scientific edit or mapping-status promotion
    is made.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact identity, claim-level evidence, material versus localization grounding,
    and component assembly-essentiality contract
  accessed_at: '2026-10-21T10:21:17Z'
  support: context_only
  summary: Family identity, concrete protein examples and structure membership are
    separate; activity and viability are not by themselves formation assays. Optional
    inventories are not mandatory.
- evidence_id: root19-sources-lipid-monolayer-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005811,GO:0034430
  locator: Both complete definitions, comments, synonyms and returned relations
  accessed_at: '2026-10-21T10:14:46.837768Z'
  support: supports
  summary: The exact GO target and all five synonym scopes match; its definition is
    a single phospholipid layer. GO0005811 identifies the containing lipid droplet
    and its monolayer/protein distinction. The maintained spelling fixes the authority
    typo without changing meaning.
  snapshot_sha256: be2beacb7198f4be9b541c7a730115400736e3f32e29a8cb0bd23d26db532d84
- evidence_id: root19-sources-CHEBI-16247
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/16247/
  locator: Exact accession, name, definition where present, synonyms and chemical-class
    relations
  accessed_at: '2026-10-21T10:14:46.923321Z'
  support: supports
  summary: Released three-star CHEBI:16247 identifies phospholipid. Its chemical-class
    identity and returned definition/ontology relations are assessed independently
    of placement in a wall or membrane.
  snapshot_sha256: c43d6c08d37ee710679ce93e8a797e2fd09bc8f8fd8e800adcba56ebcc4c1f7a
- evidence_id: root19-sources-NCBITaxon-4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Exact taxId, scientificName, rank, lineage and relevant alternative names
  accessed_at: '2026-10-21T10:14:46.809211Z'
  support: supports
  summary: Native ENA taxonomy identifies Saccharomyces cerevisiae at species rank.
    Only this taxon's identity and names are asserted by this row, not occurrence
    or experimental stock identity.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: root19-sources-doi-10.1007_s00018-015-1903-5
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1007/s00018-015-1903-5
  locator: Exact native title, authors, year, source MED, DOI/PMID and abstract fields
  accessed_at: '2026-10-21T10:14:47.490950Z'
  support: supports
  summary: Native citation identifies Lipid droplet dynamics in budding yeast. PMID
    25894691; DOI 10.1007/s00018-015-1903-5. Exact bibliographic fields and the complete
    returned abstract were inspected; this row does not attest a full-text read.
  snapshot_sha256: ed3aad072d8b2156972b5e3ed819d713987f89d01996e073300b2ec37216cbf3
- evidence_id: root19-sources-PMID-29397034
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A29397034%20AND%20SRC%3AMED
  locator: Exact native title, authors, year, source MED, DOI/PMID and abstract fields
  accessed_at: '2026-10-21T10:14:46.982743Z'
  support: supports
  summary: Native citation identifies Lipid droplet-mediated lipid and protein homeostasis
    in budding yeast. PMID 29397034; DOI 10.1002/1873-3468.12996. Exact bibliographic
    fields and the complete returned abstract were inspected; this row does not attest
    a full-text read.
  snapshot_sha256: ace3ce9e7715ed1e6f59aa9460c9a704105df09f87aff397a4e63c17c1296dc3
- evidence_id: root19-sources-doi-10.1016_j.bbalip.2011.07.015
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.bbalip.2011.07.015
  locator: Exact native title, authors, year, source MED, DOI/PMID and abstract fields
  accessed_at: '2026-10-21T10:14:47.561723Z'
  support: supports
  summary: 'Native citation identifies Lipid particles/droplets of the yeast Saccharomyces
    cerevisiae revisited: lipidome meets proteome. PMID 21820081; DOI 10.1016/j.bbalip.2011.07.015.
    Exact bibliographic fields and the complete returned abstract were inspected;
    this row does not attest a full-text read.'
  snapshot_sha256: 42ed5c12f8c1a4a5b447b75aabceb748bbbb300715465604076a434d275bc02f
- evidence_id: root19-sources-doi-10.1105_tpc.105.039859
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1105/tpc.105.039859
  locator: Exact native title, authors, year, source MED, DOI/PMID and abstract fields
  accessed_at: '2026-10-21T10:14:47.580236Z'
  support: supports
  summary: Native citation identifies Plastoglobules are lipoprotein subcompartments
    of the chloroplast that are permanently coupled to thylakoid membranes and contain
    biosynthetic enzymes. PMID 16731586; DOI 10.1105/tpc.105.039859. Exact bibliographic
    fields and the complete returned abstract were inspected; this row does not attest
    a full-text read.
  snapshot_sha256: 1a40d09be3b95c2cbd39a962f7c6e3f6359a5bd771bb8c091e3cf2f2603a5f85
- evidence_id: root19-sources-jats-PMC5947121
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5947121.1/PMC5947121.1.xml
  locator: Complete direct text of feb212996-sec-0002 and feb212996-sec-0003, including
    Figure1 caption but excluding nested protein-machinery subsections; remaining
    review not audited.
  accessed_at: '2026-10-21T10:15:36.295044Z'
  support: supports
  summary: Graef2018 describes neutral TAG/SE cores enclosed by one phospholipid leaflet
    and variable lipid/protein composition. Its biogenesis introduction distinguishes
    the mature surface from proposed ER-origin mechanisms. The record does not import
    those mechanisms.
  snapshot_sha256: 8c520a2ae66e79618d8112cd69b5c8712ef50fcddda7e2bc07ebf920f344ef7d
- evidence_id: root19-sources-jats-PMC3229976
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3229976.1/PMC3229976.1.xml
  locator: Introduction s0005; Methods s0015/s0020/s0030 and strain Table1 t0005;
    Results s0055/s0060. No complete proteomics section, all tables or raw spectra
    reanalysis.
  accessed_at: '2026-10-21T10:15:35.988570Z'
  support: supports
  summary: 'Grillitsch2011 Introduction describes the phospholipid monolayer and associated
    surface proteins as cited background. The study directly supports a yeast lipid-particle
    example and fraction-lipidomics measurements: Methods identify stationary-phase
    glucose/oleate cultures and fractionation/lipid analysis; Results and Table1 show
    class and molecular-species variation. Fraction lipidomics is not direct imaging
    of each leaflet or proof of one universally required phospholipid species.'
  snapshot_sha256: 557af7ea56ca661d74f43edabb9ad51b40ba8fe267d6d907f975306e2ff20cd2
- evidence_id: root19-sources-wang2015-publisher
  kind: authority
  reference: https://link.springer.com/article/10.1007/s00018-015-1903-5
  locator: Publisher Abs1-section/Abs1-content complete abstract and access-page boundary;
    full review body not available
  accessed_at: '2026-10-21T10:17:50.569049Z'
  support: context_only
  summary: The publisher supplied metadata and an abstract/access page, not the Wang
    review body. Its abstract supports budding-yeast lipid-droplet context but does
    not independently expose the monolayer sentence. Direct topical corroboration
    comes from the separately cited Graef body and Grillitsch primary study.
  snapshot_sha256: 94199914d66b3829a01742cf0ff826adb5f6e3f3be313b2babc7c4c95d710025
- evidence_id: root19-sources-legacy-PMC11113813
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11113813/
  locator: Actual source-access response, not article content
  accessed_at: '2026-10-21T10:16:39.096237Z'
  support: context_only
  summary: The PMC route returned a browser challenge, not the Wang full text.
  snapshot_sha256: fcafe76535e21161e7d0513180fa621f4601aa0cd2fc112fb73466b654504675
- evidence_id: root19-sources-legacy-PMC1488921
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1488921/
  locator: Actual source-access response, not article content
  accessed_at: '2026-10-21T10:16:39.092781Z'
  support: context_only
  summary: The PMC route returned a browser challenge. Austin2006 is checked through
    its exact native metadata and complete abstract, whose direct half-bilayer/thylakoid
    statement supports the bounded open discussion.
  snapshot_sha256: 2e866943f15528b67dfb946cb138279e523a74652d5db55390999f4815bf6652
- evidence_id: lipid-neighbor
  kind: record_content
  reference: data/structures/inclusion/lipid_droplet.yaml
  locator: Identity, definition, kind, parents/parthood, components and discussions
    fields
  accessed_at: '2026-10-21T10:21:17Z'
  support: context_only
  summary: The containing droplet has a neutral-lipid core; its definition permits
    associated proteins. It is not equivalent to the isolated outer monolayer.
- evidence_id: plastoglobule-neighbor
  kind: record_content
  reference: data/structures/inclusion/plastoglobule.yaml
  locator: Identity, definition, kind, parents/parthood, components and discussions
    fields
  accessed_at: '2026-10-21T10:21:17Z'
  support: context_only
  summary: The plastoglobule record distinguishes higher-plant thylakoid continuity
    from the algal evidence. This boundary context was inspected without conducting
    a separate review of its sources.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:13:30Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml'
  snapshot_sha256: 7fd106604ab467eded2731fd07d123467e5d448dce5aa5899c159ad65836a2a3
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml
    --out /private/tmp/cellstructure-batch19-20261021-9bkzflrr/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:13:32Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml\
    \ --out /private/tmp/cellstructure-batch19-20261021-9bkzflrr/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch19-20261021-9bkzflrr/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer-strict.tsv"
  snapshot_sha256: b03773e00e64ad286178247e107daa1784b666edb78557a9c7f905d231c4e426
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml;
    exact collect() scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T10:21:17Z'
  support: supports
  summary: '7 of8 collected target identifiers returned OK in this fresh base resolver
    run. Residuals: PMID:29397034: UNREACHABLE; resolved by evidence root19-sources-PMID-29397034.
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
  topic: Outer monolayer separated from whole storage bodies
  outcome: supported
  target_ids:
  - GO:0034430
  summary: Exact identity, all synonym types and the membrane kind are supported.
    The phospholipid surface is a part of the containing droplet rather than the whole
    neutral-lipid inclusion. Synonym import does not assert experimental coverage
    of every named organism or plastoglobule boundary.
  evidence_ids:
  - root19-sources-lipid-monolayer-go
  - root19-sources-jats-PMC3229976
  - root19-sources-jats-PMC5947121
  - lipid-neighbor
  - plastoglobule-neighbor
  - record
- assessment_id: material
  area: grounding
  topic: Correct chemical class and explicit protein boundary
  outcome: supported
  target_ids:
  - GO:0034430
  summary: CHEBI16247 exactly denotes phospholipid, matching the class-level component
    and graph node. The monolayer record intentionally represents lipid material;
    associated proteins can occur on the containing organelle without becoming equivalent
    to the lipid layer. No obligatory individual lipid species or comprehensive proteome
    is implied.
  evidence_ids:
  - root19-sources-lipid-monolayer-go
  - root19-sources-CHEBI-16247
  - root19-sources-jats-PMC3229976
  - root19-sources-jats-PMC5947121
  - record
  - policy
- assessment_id: necessity
  area: evidence
  topic: Defining collective layer versus individual molecular requirements
  outcome: unknown
  target_ids:
  - GO:0034430
  summary: The collective phospholipid layer constitutes the defined target. This
    does not demonstrate that every phospholipid class or species is individually
    required to form that layer. The reviewed lipidomics documents conditional composition,
    not a universal molecular-removal experiment; individual formation necessity is
    left unknown without inventing a corrective issue.
  evidence_ids:
  - root19-sources-lipid-monolayer-go
  - root19-sources-CHEBI-16247
  - root19-sources-jats-PMC3229976
  - root19-sources-jats-PMC5947121
  - record
  - policy
- assessment_id: taxa
  area: scope
  topic: Yeast evidence retained at species and condition scope
  outcome: supported
  target_ids:
  - GO:0034430
  summary: The native taxon identifies S.cerevisiae. The primary study uses BY4741
    and listed GFP strains under specified carbon-source conditions; the maintained
    example remains a species-level model claim and does not prescribe fixed composition.
    COMMON is qualitative, not a newly measured prevalence.
  evidence_ids:
  - root19-sources-NCBITaxon-4932
  - root19-sources-jats-PMC3229976
  - root19-sources-jats-PMC5947121
  - root19-sources-doi-10.1007_s00018-015-1903-5
  - root19-sources-PMID-29397034
  - root19-sources-doi-10.1016_j.bbalip.2011.07.015
  - root19-sources-doi-10.1105_tpc.105.039859
  - record
- assessment_id: function-graph
  area: graph
  topic: Mature surface topology with appropriate nonmechanistic status
  outcome: supported
  target_ids:
  - GO:0034430
  summary: The three graph edges describe phospholipid-layer constitution, parthood
    and enclosure of the hydrophobic core. NONMECHANISTIC and its explicit scope note
    appropriately exclude ER budding, insertion, growth and lipolysis mechanisms.
    Surface compartmentalization and associated proteins are directly supported at
    the stated source tiers.
  evidence_ids:
  - root19-sources-lipid-monolayer-go
  - root19-sources-CHEBI-16247
  - root19-sources-jats-PMC3229976
  - root19-sources-jats-PMC5947121
  - record
- assessment_id: boundary
  area: scope
  topic: Non-yeast extension is deliberately unresolved
  outcome: supported
  target_ids:
  - GO:0034430
  summary: The open discussion identifies oil-body and plastoglobule boundaries before
    taxonomic expansion. Austin abstract supports observed half-bilayer continuity
    in the tested chloroplast systems; it is not converted into an algal universal.
    Leaving this as a bounded question is appropriate rather than a missing mandatory
    inventory.
  evidence_ids:
  - root19-sources-doi-10.1105_tpc.105.039859
  - root19-sources-lipid-monolayer-go
  - plastoglobule-neighbor
  - record
- assessment_id: coverage
  area: completeness
  topic: Bounded record-level coverage
  outcome: supported
  target_ids:
  - GO:0034430
  summary: The entire maintained record and cited claim contexts were inspected at
    the stated source scopes. Exact additional polymer inventories, numerical properties,
    images, traits and expanded mechanisms are optional. No verbatim quotation requires
    repair, and no status or history rewrite is proposed. A clean result does not
    assert exhaustive literature completeness.
  evidence_ids:
  - record
  - policy
  - root19-sources-lipid-monolayer-go
  - root19-sources-CHEBI-16247
  - root19-sources-NCBITaxon-4932
  - root19-sources-doi-10.1007_s00018-015-1903-5
  - root19-sources-PMID-29397034
  - root19-sources-doi-10.1016_j.bbalip.2011.07.015
  - root19-sources-doi-10.1105_tpc.105.039859
  - root19-sources-jats-PMC5947121
  - root19-sources-jats-PMC3229976
  - root19-sources-wang2015-publisher
  - root19-sources-legacy-PMC11113813
  - root19-sources-legacy-PMC1488921
  - lipid-neighbor
  - plastoglobule-neighbor
findings: []
actions: []
limitations:
- 'Wang2015 full text was not recovered: its publisher response is an abstract/access
  page and PMC supplied a browser challenge. Exact monolayer attribution in that inaccessible
  body remains unchecked; the same coarse claim is directly supported in the separately
  cited Graef and Grillitsch texts.'
- Austin2006 was read at exact native metadata and complete abstract scope, not its
  body, images or raw tomography. The existing open non-yeast boundary question is
  preserved.
- Graef and Grillitsch were read only at the declared sections. No comprehensive species
  inventory, protein census, raw lipidomics or individual-component formation assay
  is claimed.
- Neighbor records were inspected only at the declared boundary fields; their experimental
  claims and histories are not independently reviewed in this bundle.
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
