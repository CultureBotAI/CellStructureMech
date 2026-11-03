# New mitotic spindle pole body age, signaling and species-scope review

- Review: 20261021T074637Z-new-mitotic-spindle-pole-body-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T07:36:24Z
- Finished UTC: 2026-10-21T07:46:37Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Exact new mitotic SPB identity, synonym, fission-yeast example and bounded signaling-asymmetry context are supported. The acknowledged regulatory/structural inventory gap remains a limitation; no concrete curation defect was established.

## Scope And Provenance

Entire single target, native GO and taxonomy, exact cited primary identity and claim-relevant body, plus full local generic-SPB context for the stated identifier boundary.

Selection: Fifth selected unreviewed path in batch nine, in repository path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0071958 | data/structures/cytoskeleton/new_mitotic_spindle_pole_body.yaml | maintained | new mitotic spindle pole body |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0071958 | Focused validator passed. |
| Focused native strict | passed | True | GO:0071958 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0071958 | 5 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | GO:0071958 | No transcriptional-regulator or expression-module mechanism is asserted. Structural localization and optional constituent candidates are not inferred from expression modules. |
| Claim-level scientific review | passed | True | GO:0071958 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0071958 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0071958 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0071958 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0071958 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0071958 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### New pole as a distinct age/asymmetry structure

identity: supported. Targets: GO:0071958.

The exact definition, synonym, parent and old-pole sibling agree with native GO. The target denotes a newly duplicated organelle, not the SIN complex or a NIMA kinase protein.

### Fission-yeast species and cell-cycle restriction

scope: supported. Targets: GO:0071958.

The S. pombe example is experimentally supported. The record does not claim broad fungal occurrence or spatial inheritance rules from budding yeast. Active SIN is enriched on the new pole late in anaphase B/G1; the general localization description does not assert exclusivity for every signaling protein at every stage.

### Primary age-labeling and differential signaling

evidence: supported. Targets: GO:0071958.

Pcp1-RFP labeling and Cdc7 localization establish the age bias of the active SIN. Fin1 behaves differently and depends on parental SPB history. The current record merely cites SIN/NIMA asymmetry and avoids promoting Fin1 into an exclusively new-pole component.

### Generic local duplication roles versus the exact GO class

grounding: supported. Targets: GO:0071958.

The record correctly distinguishes its GO age/asymmetry identity from generic old_spb/new_spb duplication placeholders. The broader local record was inspected as context without reviewing or changing its independent biological claims.

### Transient regulators versus structural constituents

completeness: supported. Targets: GO:0071958.

The open component discussion correctly keeps localized SIN and NIMA-related proteins separate from conserved structural inventory. Cdc7/Fin1 localization does not alone justify permanent constituent membership or a universal family mapping. No wrong component accession or required missing representation was established.

### Bounded identity record without an asserted mechanism

graph: supported. Targets: GO:0071958.

The target has no causal graph, explicit functional mechanism, protein examples, molecular copy counts or image claims. Their absence is optional incompleteness, not an inferred defect. No unasserted causal mechanism is judged supported.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/new_mitotic_spindle_pole_body.yaml; Entire maintained YAML, including definition, history, species examples, all evidence, graph if present, and discussions | context_only | The complete PROPOSED record was read. Its scope and open composition discussion are assessed separately from optional future enrichment. No scientific content or status is changed. |
| policy | docs/CURATION.md; Structure identity, hierarchy, component grounding, evidence and scientific-status rules | context_only | Whole structures, substructures, constituent protein families and transient regulatory localization require distinct scope. Empty optional component inventories do not by themselves establish a defect. |
| new-mitotic-spb-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0071958%2CGO%3A0071957%2CGO%3A0044732; All three exact definitions, synonym scopes, active flags and parent-term child relations | supports | GO0071958 is the active new mitotic SPB class, with exact synonym new SPB and parent GO0044732. GO0071957 denotes the distinct old, pre-existing sibling. |
| new-mitotic-spb-agent-taxon | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896; taxId, scientificName, rank and lineage | supports | ENA confirms Schizosaccharomyces pombe, NCBITaxon4896, at species rank. |
| new-mitotic-spb-agent-grallert2004-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1101/gad.296204&amp;format=json&amp;resultType=core; Exact EuropePMC core result: citation identity and availability fields | supports | Native metadata verifies Grallert et al.2004, DOI10.1101/gad.296204, PMID15132994, PMC406291, exact title, authors and journal. |
| new-mitotic-spb-agent-grallert2004 | https://pmc.ncbi.nlm.nih.gov/articles/PMC406291/?pdf=render; Native PMC406291 HTML: Results sec4-sec5 and sec8-sec9; Discussion sec12-sec14; Methods sec19-sec20; Figure2, Figure5 and Figure8 legends as text | supports | Primary S. pombe lineage labeling identifies active SIN on the new SPB in late anaphase B/G1. Fin1 instead always associates with the old SPB and with only half of new SPBs, depending on parental history. Early localization to both poles and age-dependent maturation delimit the signaling claim. |
| generic-spb | data/structures/cytoskeleton/spindle_pole_body.yaml; Entire local context record, especially old_spb/new_spb graph nodes and their duplication roles; captured as an additional native inspect input | context_only | The generic duplication-role nodes are ungrounded placeholders in the broader SPB context. They are not asserted there as exact records for fission-yeast GO age/asymmetry terms. |
| schema-result | just validate data/structures/cytoskeleton/new_mitotic_spindle_pole_body.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/new_mitotic_spindle_pole_body.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/new_mitotic_spindle_pole_body.yaml --out /private/tmp/cellstructure-batch9-20261021-t98tzqpa/new_mitotic_spindle_pole_body-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/new_mitotic_spindle_pole_body.yaml --out /private/tmp/cellstructure-batch9-20261021-t98tzqpa/new_mitotic_spindle_pole_body-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch9-20261021-t98tzqpa/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch9-20261021-t98tzqpa/new_mitotic_spindle_pole_body-strict.tsv |
| target-curies | just check-curies-strict; data/structures/cytoskeleton/new_mitotic_spindle_pole_body.yaml; exact collect() scope; SHA-256 identifies the entire original resolver TSV at /private/tmp/cellstructure-record-reviews-UhRFh7/repo/reports/curie_check.tsv, not derived resolver-slice.json | supports | 5 of 5 collected target identifiers returned OK at the unchanged base. Residuals: none. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- The primary article text and relevant figure legends were read; microscopy pixels, movies and all raw lineage observations were not independently reanalyzed.
- Active SIN on the new pole late in anaphase B/G1 must not be generalized to every SIN/NIMA protein or every cell-cycle stage. Fin1 binds all old poles and only a history-dependent subset of new poles.
- The optional structural and transient-signaling inventories remain unresolved. No accession, stoichiometry or protein-family assignment is added by this review.
- COMMON is qualitative species occurrence, not a measured proportion of cells, strains or fungi.
- The generic local SPB record is a boundary-check input, not an additional reviewed target.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The explicit user goal requests a review for every selected target, including records without a concrete issue. No finding was invented to satisfy that persistence instruction.
- Only a review bundle is saved. Maintained scientific content, native status, history and generated pages remain unchanged.
- Parent independently read the full target, source packet, draft, all source/input hashes and selected claim-bearing source sections. Source collaborator inspected the other cited sections and full local boundary context. Parent accepts these bounded assessments before saving.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T074637Z-new-mitotic-spindle-pole-body-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: New mitotic spindle pole body age, signaling and species-scope review
started_at: '2026-10-21T07:36:24Z'
finished_at: '2026-10-21T07:46:37Z'
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
summary: Exact new mitotic SPB identity, synonym, fission-yeast example and bounded
  signaling-asymmetry context are supported. The acknowledged regulatory/structural
  inventory gap remains a limitation; no concrete curation defect was established.
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
  - path: data/structures/cytoskeleton/new_mitotic_spindle_pole_body.yaml
    sha256: 33ac955370a7476c7bb3f3fca4cfc9464120890e6a3e57fcb3b32d5e2504fb82
    role: target
  - path: data/structures/cytoskeleton/spindle_pole_body.yaml
    sha256: 50885e021c246e17e29beb27f7dc98e37ee4d34878648fea4fd8b565bbb2fc78
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
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: GO:0071958
  path: data/structures/cytoskeleton/new_mitotic_spindle_pole_body.yaml
  label: new mitotic spindle pole body
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/new_mitotic_spindle_pole_body.yaml
    role: maintained scientific record
scope:
  description: Entire single target, native GO and taxonomy, exact cited primary identity
    and claim-relevant body, plus full local generic-SPB context for the stated identifier
    boundary.
  selection: Fifth selected unreviewed path in batch nine, in repository path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0071958
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0071958
  command: just validate data/structures/cytoskeleton/new_mitotic_spindle_pole_body.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0071958
  command: just validate-strict data/structures/cytoskeleton/new_mitotic_spindle_pole_body.yaml
    --out /private/tmp/cellstructure-batch9-20261021-t98tzqpa/new_mitotic_spindle_pole_body-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0071958
  summary: 5 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0071958
  summary: No transcriptional-regulator or expression-module mechanism is asserted.
    Structural localization and optional constituent candidates are not inferred from
    expression modules.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0071958
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - new-mitotic-spb-agent-go
  - new-mitotic-spb-agent-taxon
  - new-mitotic-spb-agent-grallert2004-metadata
  - new-mitotic-spb-agent-grallert2004
  - generic-spb
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0071958
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch9 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0071958
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch9 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0071958
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch9 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0071958
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch9 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0071958
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch9 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/new_mitotic_spindle_pole_body.yaml
  locator: Entire maintained YAML, including definition, history, species examples,
    all evidence, graph if present, and discussions
  accessed_at: '2026-10-21T07:45:53Z'
  support: context_only
  summary: The complete PROPOSED record was read. Its scope and open composition discussion
    are assessed separately from optional future enrichment. No scientific content
    or status is changed.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Structure identity, hierarchy, component grounding, evidence and scientific-status
    rules
  accessed_at: '2026-10-21T07:45:53Z'
  support: context_only
  summary: Whole structures, substructures, constituent protein families and transient
    regulatory localization require distinct scope. Empty optional component inventories
    do not by themselves establish a defect.
- evidence_id: new-mitotic-spb-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0071958%2CGO%3A0071957%2CGO%3A0044732
  locator: All three exact definitions, synonym scopes, active flags and parent-term
    child relations
  accessed_at: '2026-10-21T07:36:47.665055Z'
  support: supports
  summary: GO0071958 is the active new mitotic SPB class, with exact synonym new SPB
    and parent GO0044732. GO0071957 denotes the distinct old, pre-existing sibling.
  snapshot_sha256: 74dfb3320a1e69bc33faae1ffb5c0351bd84650b4e86f798ae5bf92f26d18f62
- evidence_id: new-mitotic-spb-agent-taxon
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896
  locator: taxId, scientificName, rank and lineage
  accessed_at: '2026-10-21T07:36:47.665156Z'
  support: supports
  summary: ENA confirms Schizosaccharomyces pombe, NCBITaxon4896, at species rank.
  snapshot_sha256: 42c5b7d3d99341137803612d6404cd3884e2d06ec8a740b1ad38163c678f6721
- evidence_id: new-mitotic-spb-agent-grallert2004-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1101/gad.296204&format=json&resultType=core
  locator: 'Exact EuropePMC core result: citation identity and availability fields'
  accessed_at: '2026-10-21T07:36:48.351248Z'
  support: supports
  summary: Native metadata verifies Grallert et al.2004, DOI10.1101/gad.296204, PMID15132994,
    PMC406291, exact title, authors and journal.
  snapshot_sha256: c64265cb102adbe7e47950968adbe885a01ff480f027d6a79adbe472465f5488
- evidence_id: new-mitotic-spb-agent-grallert2004
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC406291/?pdf=render
  locator: 'Native PMC406291 HTML: Results sec4-sec5 and sec8-sec9; Discussion sec12-sec14;
    Methods sec19-sec20; Figure2, Figure5 and Figure8 legends as text'
  accessed_at: '2026-10-21T07:37:23.467605Z'
  support: supports
  summary: Primary S. pombe lineage labeling identifies active SIN on the new SPB
    in late anaphase B/G1. Fin1 instead always associates with the old SPB and with
    only half of new SPBs, depending on parental history. Early localization to both
    poles and age-dependent maturation delimit the signaling claim.
  snapshot_sha256: 4d6cf33e789cdec2e69d996bae55b2c97234ac737064b920972202b39d2c4950
- evidence_id: generic-spb
  kind: record_content
  reference: data/structures/cytoskeleton/spindle_pole_body.yaml
  locator: Entire local context record, especially old_spb/new_spb graph nodes and
    their duplication roles; captured as an additional native inspect input
  accessed_at: '2026-10-21T07:45:53Z'
  support: context_only
  summary: The generic duplication-role nodes are ungrounded placeholders in the broader
    SPB context. They are not asserted there as exact records for fission-yeast GO
    age/asymmetry terms.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/new_mitotic_spindle_pole_body.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T07:36:30Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/new_mitotic_spindle_pole_body.yaml'
  snapshot_sha256: 00bf2d78cd2a18634c928455c05568f2d8f3823c7630ba34aded822c7d802648
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/new_mitotic_spindle_pole_body.yaml
    --out /private/tmp/cellstructure-batch9-20261021-t98tzqpa/new_mitotic_spindle_pole_body-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T07:36:35Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/new_mitotic_spindle_pole_body.yaml\
    \ --out /private/tmp/cellstructure-batch9-20261021-t98tzqpa/new_mitotic_spindle_pole_body-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch9-20261021-t98tzqpa/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch9-20261021-t98tzqpa/new_mitotic_spindle_pole_body-strict.tsv"
  snapshot_sha256: 5af6ddc7214a52324e4a7c3e25b657fc4594d1a19dc0e1ca5038188728efa743
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/new_mitotic_spindle_pole_body.yaml; exact
    collect() scope; SHA-256 identifies the entire original resolver TSV at /private/tmp/cellstructure-record-reviews-UhRFh7/repo/reports/curie_check.tsv,
    not derived resolver-slice.json
  accessed_at: '2026-10-21T07:45:53Z'
  support: supports
  summary: '5 of 5 collected target identifiers returned OK at the unchanged base.
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
  topic: New pole as a distinct age/asymmetry structure
  outcome: supported
  target_ids:
  - GO:0071958
  summary: The exact definition, synonym, parent and old-pole sibling agree with native
    GO. The target denotes a newly duplicated organelle, not the SIN complex or a
    NIMA kinase protein.
  evidence_ids:
  - new-mitotic-spb-agent-go
  - new-mitotic-spb-agent-grallert2004
  - record
- assessment_id: scope
  area: scope
  topic: Fission-yeast species and cell-cycle restriction
  outcome: supported
  target_ids:
  - GO:0071958
  summary: The S. pombe example is experimentally supported. The record does not claim
    broad fungal occurrence or spatial inheritance rules from budding yeast. Active
    SIN is enriched on the new pole late in anaphase B/G1; the general localization
    description does not assert exclusivity for every signaling protein at every stage.
  evidence_ids:
  - new-mitotic-spb-agent-go
  - new-mitotic-spb-agent-taxon
  - new-mitotic-spb-agent-grallert2004
  - record
- assessment_id: evidence
  area: evidence
  topic: Primary age-labeling and differential signaling
  outcome: supported
  target_ids:
  - GO:0071958
  summary: Pcp1-RFP labeling and Cdc7 localization establish the age bias of the active
    SIN. Fin1 behaves differently and depends on parental SPB history. The current
    record merely cites SIN/NIMA asymmetry and avoids promoting Fin1 into an exclusively
    new-pole component.
  evidence_ids:
  - new-mitotic-spb-agent-grallert2004
  - new-mitotic-spb-agent-grallert2004-metadata
  - record
- assessment_id: boundary
  area: grounding
  topic: Generic local duplication roles versus the exact GO class
  outcome: supported
  target_ids:
  - GO:0071958
  summary: The record correctly distinguishes its GO age/asymmetry identity from generic
    old_spb/new_spb duplication placeholders. The broader local record was inspected
    as context without reviewing or changing its independent biological claims.
  evidence_ids:
  - new-mitotic-spb-agent-go
  - generic-spb
  - record
- assessment_id: composition
  area: completeness
  topic: Transient regulators versus structural constituents
  outcome: supported
  target_ids:
  - GO:0071958
  summary: The open component discussion correctly keeps localized SIN and NIMA-related
    proteins separate from conserved structural inventory. Cdc7/Fin1 localization
    does not alone justify permanent constituent membership or a universal family
    mapping. No wrong component accession or required missing representation was established.
  evidence_ids:
  - new-mitotic-spb-agent-grallert2004
  - record
  - policy
- assessment_id: representation
  area: graph
  topic: Bounded identity record without an asserted mechanism
  outcome: supported
  target_ids:
  - GO:0071958
  summary: The target has no causal graph, explicit functional mechanism, protein
    examples, molecular copy counts or image claims. Their absence is optional incompleteness,
    not an inferred defect. No unasserted causal mechanism is judged supported.
  evidence_ids:
  - new-mitotic-spb-agent-go
  - new-mitotic-spb-agent-grallert2004
  - record
findings: []
actions: []
limitations:
- The primary article text and relevant figure legends were read; microscopy pixels,
  movies and all raw lineage observations were not independently reanalyzed.
- Active SIN on the new pole late in anaphase B/G1 must not be generalized to every
  SIN/NIMA protein or every cell-cycle stage. Fin1 binds all old poles and only a
  history-dependent subset of new poles.
- The optional structural and transient-signaling inventories remain unresolved. No
  accession, stoichiometry or protein-family assignment is added by this review.
- COMMON is qualitative species occurrence, not a measured proportion of cells, strains
  or fungi.
- The generic local SPB record is a boundary-check input, not an additional reviewed
  target.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- The explicit user goal requests a review for every selected target, including records
  without a concrete issue. No finding was invented to satisfy that persistence instruction.
- Only a review bundle is saved. Maintained scientific content, native status, history
  and generated pages remain unchanged.
- Parent independently read the full target, source packet, draft, all source/input
  hashes and selected claim-bearing source sections. Source collaborator inspected
  the other cited sections and full local boundary context. Parent accepts these bounded
  assessments before saving.
```
