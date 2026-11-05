# Basal-body A-tusk morphology, offsets and image review

- Review: 20261020T040905Z-basal-body-a-tusk-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-20T04:07:23Z
- Finished UTC: 2026-10-20T04:09:05Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The named A-tusk morphology, bounded pairwise offsets, Paramecium scope, contextual map and image provenance are supported. No observed issue; native composition and function remain explicitly unresolved.

## Scope And Provenance

Entire record, primary morphological paper, relevant later linker study, original figures, all identifiers and contextual archive records.

Selection: First unreviewed path of batch4.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:basal_body_a_tusk | data/structures/cytoskeleton/basal_body_a_tusk.yaml | maintained | basal body A-tusk |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | cellstructuremech:basal_body_a_tusk | Focused validator passed. |
| Focused native strict | passed | True | cellstructuremech:basal_body_a_tusk | Focused validator passed. |
| Target resolver slice | passed | True | cellstructuremech:basal_body_a_tusk | 6 identifiers OK; 2 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | cellstructuremech:basal_body_a_tusk | No native gene, expression dataset or transcriptional mechanism is asserted. Neighboring linker gene names are explicitly excluded as compositional evidence. |
| Claim-level scientific review | passed | True | cellstructuremech:basal_body_a_tusk | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | cellstructuremech:basal_body_a_tusk | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | cellstructuremech:basal_body_a_tusk | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | cellstructuremech:basal_body_a_tusk | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | cellstructuremech:basal_body_a_tusk | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | cellstructuremech:basal_body_a_tusk | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Named morphological subassembly

identity: supported. Targets: cellstructuremech:basal_body_a_tusk.

The primary source supports the exact A-tusk name, placement and distinction from the adjacent linker. OTHER and the broad cellular-component parent appropriately avoid an unestablished molecular classification.

### Unknown native constituents

completeness: supported. Targets: cellstructuremech:basal_body_a_tusk.

The absence of assigned components and causal graph reflects a declared scientific unknown. Neither proximity nor the later species-specific linker assignments identifies the tusk’s proteins.

### Paramecium example and preparation strains

scope: supported. Targets: cellstructuremech:basal_body_a_tusk.

The named density is directly supported in Paramecium. Methods support the two preparation strains and reconstruction counts; the record does not assign a specific figure to one strain or infer pan-species distribution.

### Pairwise axial offsets

evidence: supported. Targets: cellstructuremech:basal_body_a_tusk.

The two values and nanometer unit match FigureEV5E. Context explicitly prevents interpreting their sum, sampling intervals or neighboring-structure dimensions as a measured tusk repeat or length.

### Contextual proximal triplet map

provenance: supported. Targets: cellstructuremech:basal_body_a_tusk.

The linked10729 entry is the correct contextual deposit and the neighboring deposit distinctions match the native titles. No sequence-resolved tusk model is asserted.

### Image identity and licensing

evidence: supported. Targets: cellstructuremech:basal_body_a_tusk.

The unchanged hosted Figure5 matches the source bytes and primary licence. Its caption distinguishes segmentation colors, adjacent structures and processing-biased pinhead periodicity from tusk identity.

### No unsupported mechanistic claims

evidence: supported. Targets: cellstructuremech:basal_body_a_tusk.

Open discussion accurately marks function, essentiality and composition as unresolved. Static geometry is not promoted to a functional mechanism or temporal assembly model.

### Native status and historical statements

provenance: supported. Targets: cellstructuremech:basal_body_a_tusk.

PROPOSED is retained. Historical search counts are dated provenance, not current corpus counts; the current review assesses the biological boundary and source support independently.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| tusk-paper | https://pmc-oa-opendata.s3.amazonaws.com/PMC7667884.1/PMC7667884.1.xml; A-C-linker Results, Figures5/EV5, Paramecium and subtomogram Methods, Data availability | supports | The primary Results name the A8/A9 protrusion separately from the A-C linker. Figures5/EV5 and Methods distinguish the morphological offsets, adjacent structures, reconstruction sampling, two preparation strains and16 intact proximal regions from11 tomograms. |
| tusk-figure5 | https://pmc-oa-opendata.s3.amazonaws.com/PMC7667884.1/EMBJ-39-e106246-g010.jpg; Complete Figure5, including panelsB-D | supports | Visual inspection confirms the separate dark-teal A-tusk at A8/A9. Other labels concern triplet base, pinhead and linker orientations. The source image matches the maintained SHA2561431f971830fd590ad25381abf065a76a1d99800827c4e6292490af98a1fde34. |
| tusk-figureEV5 | https://pmc-oa-opendata.s3.amazonaws.com/PMC7667884.1/EMBJ-39-e106246-g011.jpg; Visual inspection of FigureEV5, especiallyE | supports | PanelE visibly labels5.2nm above and3.3nm below the indicated neighboring-triplet position. These are two pairwise offsets; panelB’s8.4±0.2nm concerns the linker, and later panels compare several species. |
| tusk-paper-meta | https://pmc-oa-opendata.s3.amazonaws.com/PMC7667884.1/PMC7667884.1.json; Metadata xml/media URLs and checksums; crosschecked JATS licence | supports | The article and both figure MD5 values match native PMC metadata. JATS identifies the hosted Figure5 as g010.jpg and supplies the explicit CC BY4.0 licence. |
| tusk-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005575,GO:0036064; Exact active terms | supports | GO0005575 is the deliberately broad cellular-component parent; GO0036064 denotes ciliary basal body. |
| tusk-tusk-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=tusk&amp;limit=100; Complete zero-result query | context_only | The complete native tusk query returned zero terms. This bounded lexical result supports retaining the local identity rather than assigning an unverified exact GO term. |
| tusk-taxon | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=5888; Exact taxonomy response | supports | NCBITaxon5888 is Paramecium tetraurelia. |
| tusk-uo | https://www.ebi.ac.uk/ols4/api/ontologies/uo/terms?obo_id=UO:0000018; Exact term response | supports | UO0000018 is the active nanometer unit, matching the figure annotations. |
| tusk-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.15252/embj.2020106246&amp;format=json&amp;resultType=core; Exact article metadata | supports | DOI10.15252/embj.2020106246, PMID32954513 and PMC7667884 join to the named Klena2020 study. |
| tusk-emdb10726 | https://www.ebi.ac.uk/emdb/api/entry/EMD-10726; Admin title, release status, natural source and citation | supports | Released native title, organism5888 and citation inspected.10729 is the start-region triplet;10727 is the start-region linker;10726 and10728 are end-region deposits. The record uses10729 as contextual data, not an isolated tusk map. |
| tusk-emdb10727 | https://www.ebi.ac.uk/emdb/api/entry/EMD-10727; Admin title, release status, natural source and citation | supports | Released native title, organism5888 and citation inspected.10729 is the start-region triplet;10727 is the start-region linker;10726 and10728 are end-region deposits. The record uses10729 as contextual data, not an isolated tusk map. |
| tusk-emdb10728 | https://www.ebi.ac.uk/emdb/api/entry/EMD-10728; Admin title, release status, natural source and citation | supports | Released native title, organism5888 and citation inspected.10729 is the start-region triplet;10727 is the start-region linker;10726 and10728 are end-region deposits. The record uses10729 as contextual data, not an isolated tusk map. |
| tusk-emdb10729 | https://www.ebi.ac.uk/emdb/api/entry/EMD-10729; Admin title, release status, natural source and citation | supports | Released native title, organism5888 and citation inspected.10729 is the start-region triplet;10727 is the start-region linker;10726 and10728 are end-region deposits. The record uses10729 as contextual data, not an isolated tusk map. |
| basal-cai | https://pmc-oa-opendata.s3.amazonaws.com/PMC12506977.1/PMC12506977.1.xml; A-C-linker/junction Results and full-JATS lexical search | context_only | The later Tetrahymena study assigns proteins to linker/junction structures but does not identify a named Paramecium A-tusk. A complete case-insensitive search of its JATS finds no tusk occurrence; this absence claim is limited to that article text. |
| record | data/structures/cytoskeleton/basal_body_a_tusk.yaml; Entire target, physical-property context, dataset, discussions and image | context_only | The target explicitly retains unresolved native composition/function, bounds each measurement and separates preparation strains and species. No component, graph or force claim is fabricated. |
| local-id | data/structures/cytoskeleton/basal_body_a_tusk.yaml; Exact identifier; rg --hidden --no-ignore across data/structures | context_only | Only the target declares this local identifier; ignored files were included in the bounded local-identity check. |
| schema-result | just validate data/structures/cytoskeleton/basal_body_a_tusk.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/basal_body_a_tusk.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/basal_body_a_tusk.yaml --out /private/tmp/cellstructure-batch4-20261019-QtBQNE/basal_body_a_tusk-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/basal_body_a_tusk.yaml --out /private/tmp/cellstructure-batch4-20261019-QtBQNE/basal_body_a_tusk-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch4-20261019-QtBQNE/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch4-20261019-QtBQNE/basal_body_a_tusk-strict.tsv |
| target-curies | just check-curies-strict; data/structures/cytoskeleton/basal_body_a_tusk.yaml; exact collect() scope | supports | 6 of8 collected target identifiers returned OK at the unchanged base. Residuals: EMDB:EMD-10729: SKIPPED; resolved by evidence tusk-emdb10729; cellstructuremech:basal_body_a_tusk: SKIPPED; resolved by evidence local-id. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- No sequence-resolved molecular identity, stoichiometry or A-tusk-specific function is established.
- The original figure is not assigned to one of the two preparation strains.
- The two static offsets lack replicate/error estimates; they are not a universal repeat measurement.
- The data checks cover metadata and figures, not reprocessing of deposited three-dimensional maps.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The user explicitly authorizes saving clean reviews.
- Only the review bundle is saved. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T040905Z-basal-body-a-tusk-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Basal-body A-tusk morphology, offsets and image review
started_at: '2026-10-20T04:07:23Z'
finished_at: '2026-10-20T04:09:05Z'
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
summary: The named A-tusk morphology, bounded pairwise offsets, Paramecium scope,
  contextual map and image provenance are supported. No observed issue; native composition
  and function remain explicitly unresolved.
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
  - path: data/images/cytoskeleton/basal_body_a_tusk/pmc7667884_embj2020106246_fig_0005.jpg
    sha256: 1431f971830fd590ad25381abf065a76a1d99800827c4e6292490af98a1fde34
    role: context
  - path: data/structures/cytoskeleton/basal_body_a_tusk.yaml
    sha256: f82923b0febf504980e0c7e006d03d72c9cfdd2b38e225b6ad82adaac4d754c1
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
- target_id: cellstructuremech:basal_body_a_tusk
  path: data/structures/cytoskeleton/basal_body_a_tusk.yaml
  label: basal body A-tusk
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/basal_body_a_tusk.yaml
    role: maintained scientific record
scope:
  description: Entire record, primary morphological paper, relevant later linker study,
    original figures, all identifiers and contextual archive records.
  selection: First unreviewed path of batch4.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:basal_body_a_tusk
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_a_tusk
  command: just validate data/structures/cytoskeleton/basal_body_a_tusk.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_a_tusk
  command: just validate-strict data/structures/cytoskeleton/basal_body_a_tusk.yaml
    --out /private/tmp/cellstructure-batch4-20261019-QtBQNE/basal_body_a_tusk-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_a_tusk
  summary: 6 identifiers OK; 2 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - local-id
  - tusk-emdb10729
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - cellstructuremech:basal_body_a_tusk
  summary: No native gene, expression dataset or transcriptional mechanism is asserted.
    Neighboring linker gene names are explicitly excluded as compositional evidence.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_a_tusk
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - tusk-paper
  - tusk-figure5
  - tusk-figureEV5
  - tusk-paper-meta
  - tusk-go
  - tusk-tusk-search
  - tusk-taxon
  - tusk-uo
  - tusk-epmc
  - tusk-emdb10726
  - tusk-emdb10727
  - tusk-emdb10728
  - tusk-emdb10729
  - basal-cai
  - record
  - local-id
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_a_tusk
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch3 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_a_tusk
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch3 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_a_tusk
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch3 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_a_tusk
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch3 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_a_tusk
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch3 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: tusk-paper
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC7667884.1/PMC7667884.1.xml
  locator: A-C-linker Results, Figures5/EV5, Paramecium and subtomogram Methods, Data
    availability
  accessed_at: '2026-10-20T04:07:36.772127Z'
  support: supports
  summary: The primary Results name the A8/A9 protrusion separately from the A-C linker.
    Figures5/EV5 and Methods distinguish the morphological offsets, adjacent structures,
    reconstruction sampling, two preparation strains and16 intact proximal regions
    from11 tomograms.
  snapshot_sha256: 5116fa9428a3a69c7a3baca7e80ad82dc6d050ed8db9d88b37982136407d6184
- evidence_id: tusk-figure5
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC7667884.1/EMBJ-39-e106246-g010.jpg
  locator: Complete Figure5, including panelsB-D
  accessed_at: '2026-10-20T04:07:36.849735Z'
  support: supports
  summary: Visual inspection confirms the separate dark-teal A-tusk at A8/A9. Other
    labels concern triplet base, pinhead and linker orientations. The source image
    matches the maintained SHA2561431f971830fd590ad25381abf065a76a1d99800827c4e6292490af98a1fde34.
  snapshot_sha256: 1431f971830fd590ad25381abf065a76a1d99800827c4e6292490af98a1fde34
- evidence_id: tusk-figureEV5
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC7667884.1/EMBJ-39-e106246-g011.jpg
  locator: Visual inspection of FigureEV5, especiallyE
  accessed_at: '2026-10-20T04:07:59.416196Z'
  support: supports
  summary: PanelE visibly labels5.2nm above and3.3nm below the indicated neighboring-triplet
    position. These are two pairwise offsets; panelB’s8.4±0.2nm concerns the linker,
    and later panels compare several species.
  snapshot_sha256: 2cc673a81215f2f58e7d311657428ebef43eb09ff2d7f504f503c46d93d07ef0
- evidence_id: tusk-paper-meta
  kind: database
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC7667884.1/PMC7667884.1.json
  locator: Metadata xml/media URLs and checksums; crosschecked JATS licence
  accessed_at: '2026-10-20T04:07:36.562450Z'
  support: supports
  summary: The article and both figure MD5 values match native PMC metadata. JATS
    identifies the hosted Figure5 as g010.jpg and supplies the explicit CC BY4.0 licence.
  snapshot_sha256: 0ec250e461c0b021eff66c3668b7b0dc5701968e9102faeabd16bfa5e902c65b
- evidence_id: tusk-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005575,GO:0036064
  locator: Exact active terms
  accessed_at: '2026-10-20T04:07:36.961865Z'
  support: supports
  summary: GO0005575 is the deliberately broad cellular-component parent; GO0036064
    denotes ciliary basal body.
  snapshot_sha256: 7c8d41180a651ce3aaffb75ec8644c0283fed46b4cc4f8ec69a143a6e71c97d8
- evidence_id: tusk-tusk-search
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=tusk&limit=100
  locator: Complete zero-result query
  accessed_at: '2026-10-20T04:07:37.458448Z'
  support: context_only
  summary: The complete native tusk query returned zero terms. This bounded lexical
    result supports retaining the local identity rather than assigning an unverified
    exact GO term.
  snapshot_sha256: f3a7dae9b1e9335291e3940cdf0e5f8dadf9335da7b9547710606b5106c63f86
- evidence_id: tusk-taxon
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=5888
  locator: Exact taxonomy response
  accessed_at: '2026-10-20T04:07:36.781682Z'
  support: supports
  summary: NCBITaxon5888 is Paramecium tetraurelia.
  snapshot_sha256: 596cc922f484502eb5c3608ed45943d1486fb9b2e620d7805a76f2984ec0ad6b
- evidence_id: tusk-uo
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uo/terms?obo_id=UO:0000018
  locator: Exact term response
  accessed_at: '2026-10-20T04:07:37.417486Z'
  support: supports
  summary: UO0000018 is the active nanometer unit, matching the figure annotations.
  snapshot_sha256: 4c7db9c8cb664724cfeb7ded951492cac50dd7c8bdc275363486b3e34df94bf8
- evidence_id: tusk-epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.15252/embj.2020106246&format=json&resultType=core
  locator: Exact article metadata
  accessed_at: '2026-10-20T04:07:37.473964Z'
  support: supports
  summary: DOI10.15252/embj.2020106246, PMID32954513 and PMC7667884 join to the named
    Klena2020 study.
  snapshot_sha256: fc5be273d2b5b8a6a8e0508133e82627d15be3c057345cafce1b51fd4fb1c685
- evidence_id: tusk-emdb10726
  kind: authority
  reference: https://www.ebi.ac.uk/emdb/api/entry/EMD-10726
  locator: Admin title, release status, natural source and citation
  accessed_at: '2026-10-20T04:07:37.620588Z'
  support: supports
  summary: Released native title, organism5888 and citation inspected.10729 is the
    start-region triplet;10727 is the start-region linker;10726 and10728 are end-region
    deposits. The record uses10729 as contextual data, not an isolated tusk map.
  snapshot_sha256: 58cebaeacbb0aa96022d51cc2e575167dbc7b53c9d1f1473a8cc5fe2ebac19d4
- evidence_id: tusk-emdb10727
  kind: authority
  reference: https://www.ebi.ac.uk/emdb/api/entry/EMD-10727
  locator: Admin title, release status, natural source and citation
  accessed_at: '2026-10-20T04:07:38.078163Z'
  support: supports
  summary: Released native title, organism5888 and citation inspected.10729 is the
    start-region triplet;10727 is the start-region linker;10726 and10728 are end-region
    deposits. The record uses10729 as contextual data, not an isolated tusk map.
  snapshot_sha256: 6fb33d249a0bed05c662904d275357c2352d338887a56427b11bb166c7bffab9
- evidence_id: tusk-emdb10728
  kind: authority
  reference: https://www.ebi.ac.uk/emdb/api/entry/EMD-10728
  locator: Admin title, release status, natural source and citation
  accessed_at: '2026-10-20T04:07:38.108046Z'
  support: supports
  summary: Released native title, organism5888 and citation inspected.10729 is the
    start-region triplet;10727 is the start-region linker;10726 and10728 are end-region
    deposits. The record uses10729 as contextual data, not an isolated tusk map.
  snapshot_sha256: 720aaa30a6a1551795a4bc2c314ae33df53be46e29e411a3b441d9b097cb5dc3
- evidence_id: tusk-emdb10729
  kind: authority
  reference: https://www.ebi.ac.uk/emdb/api/entry/EMD-10729
  locator: Admin title, release status, natural source and citation
  accessed_at: '2026-10-20T04:07:38.169902Z'
  support: supports
  summary: Released native title, organism5888 and citation inspected.10729 is the
    start-region triplet;10727 is the start-region linker;10726 and10728 are end-region
    deposits. The record uses10729 as contextual data, not an isolated tusk map.
  snapshot_sha256: 29cd3ebac1c41715ca0bfa7254842b6ce3b5e591e1dd9b9c165607eba2a8032d
- evidence_id: basal-cai
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC12506977.1/PMC12506977.1.xml
  locator: A-C-linker/junction Results and full-JATS lexical search
  accessed_at: '2026-10-20T04:01:04.096242Z'
  support: context_only
  summary: The later Tetrahymena study assigns proteins to linker/junction structures
    but does not identify a named Paramecium A-tusk. A complete case-insensitive search
    of its JATS finds no tusk occurrence; this absence claim is limited to that article
    text.
  snapshot_sha256: ab8bf23b7821eaa514f3eebd1c4f281e1eb1c2af9ef4dc429aced2fe5dfcb04a
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/basal_body_a_tusk.yaml
  locator: Entire target, physical-property context, dataset, discussions and image
  accessed_at: '2026-10-20T04:09:04Z'
  support: context_only
  summary: The target explicitly retains unresolved native composition/function, bounds
    each measurement and separates preparation strains and species. No component,
    graph or force claim is fabricated.
- evidence_id: local-id
  kind: record_content
  reference: data/structures/cytoskeleton/basal_body_a_tusk.yaml
  locator: Exact identifier; rg --hidden --no-ignore across data/structures
  accessed_at: '2026-10-20T04:09:04Z'
  support: context_only
  summary: Only the target declares this local identifier; ignored files were included
    in the bounded local-identity check.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/basal_body_a_tusk.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-20T04:07:26Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/basal_body_a_tusk.yaml'
  snapshot_sha256: 975826da32e00daf5fd5fdd9bad63b2cdb7b5802696f34c18d62545e3b18eb22
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/basal_body_a_tusk.yaml
    --out /private/tmp/cellstructure-batch4-20261019-QtBQNE/basal_body_a_tusk-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-20T04:07:27Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/basal_body_a_tusk.yaml\
    \ --out /private/tmp/cellstructure-batch4-20261019-QtBQNE/basal_body_a_tusk-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch4-20261019-QtBQNE/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch4-20261019-QtBQNE/basal_body_a_tusk-strict.tsv"
  snapshot_sha256: 30042aa57ce26b1970d2fb3852a0661c5dca7ba57b6c0fb93ed500721057f90b
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/basal_body_a_tusk.yaml; exact collect() scope
  accessed_at: '2026-10-20T04:09:04Z'
  support: supports
  summary: '6 of8 collected target identifiers returned OK at the unchanged base.
    Residuals: EMDB:EMD-10729: SKIPPED; resolved by evidence tusk-emdb10729; cellstructuremech:basal_body_a_tusk:
    SKIPPED; resolved by evidence local-id. Source-native identity checked separately.'
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
  topic: Named morphological subassembly
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_a_tusk
  summary: The primary source supports the exact A-tusk name, placement and distinction
    from the adjacent linker. OTHER and the broad cellular-component parent appropriately
    avoid an unestablished molecular classification.
  evidence_ids:
  - tusk-paper
  - tusk-figure5
  - tusk-go
  - tusk-tusk-search
  - record
- assessment_id: composition
  area: completeness
  topic: Unknown native constituents
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_a_tusk
  summary: The absence of assigned components and causal graph reflects a declared
    scientific unknown. Neither proximity nor the later species-specific linker assignments
    identifies the tusk’s proteins.
  evidence_ids:
  - tusk-paper
  - basal-cai
  - record
- assessment_id: scope
  area: scope
  topic: Paramecium example and preparation strains
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_a_tusk
  summary: The named density is directly supported in Paramecium. Methods support
    the two preparation strains and reconstruction counts; the record does not assign
    a specific figure to one strain or infer pan-species distribution.
  evidence_ids:
  - tusk-paper
  - tusk-taxon
  - tusk-figureEV5
  - record
- assessment_id: measurements
  area: evidence
  topic: Pairwise axial offsets
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_a_tusk
  summary: The two values and nanometer unit match FigureEV5E. Context explicitly
    prevents interpreting their sum, sampling intervals or neighboring-structure dimensions
    as a measured tusk repeat or length.
  evidence_ids:
  - tusk-paper
  - tusk-figureEV5
  - tusk-uo
  - record
- assessment_id: dataset
  area: provenance
  topic: Contextual proximal triplet map
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_a_tusk
  summary: The linked10729 entry is the correct contextual deposit and the neighboring
    deposit distinctions match the native titles. No sequence-resolved tusk model
    is asserted.
  evidence_ids:
  - tusk-emdb10726
  - tusk-emdb10727
  - tusk-emdb10728
  - tusk-emdb10729
  - tusk-paper
  - record
- assessment_id: image
  area: evidence
  topic: Image identity and licensing
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_a_tusk
  summary: The unchanged hosted Figure5 matches the source bytes and primary licence.
    Its caption distinguishes segmentation colors, adjacent structures and processing-biased
    pinhead periodicity from tusk identity.
  evidence_ids:
  - tusk-paper
  - tusk-figure5
  - tusk-figureEV5
  - tusk-paper-meta
  - record
- assessment_id: function
  area: evidence
  topic: No unsupported mechanistic claims
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_a_tusk
  summary: Open discussion accurately marks function, essentiality and composition
    as unresolved. Static geometry is not promoted to a functional mechanism or temporal
    assembly model.
  evidence_ids:
  - tusk-paper
  - basal-cai
  - record
- assessment_id: status
  area: provenance
  topic: Native status and historical statements
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_a_tusk
  summary: PROPOSED is retained. Historical search counts are dated provenance, not
    current corpus counts; the current review assesses the biological boundary and
    source support independently.
  evidence_ids:
  - tusk-paper
  - record
findings: []
actions: []
limitations:
- No sequence-resolved molecular identity, stoichiometry or A-tusk-specific function
  is established.
- The original figure is not assigned to one of the two preparation strains.
- The two static offsets lack replicate/error estimates; they are not a universal
  repeat measurement.
- The data checks cover metadata and figures, not reprocessing of deposited three-dimensional
  maps.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- The user explicitly authorizes saving clean reviews.
- Only the review bundle is saved. Maintained scientific content, native status, history
  and generated pages remain unchanged.
```
