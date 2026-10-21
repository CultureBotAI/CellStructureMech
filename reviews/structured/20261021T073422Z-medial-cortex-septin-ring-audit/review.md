# Medial cortex septin ring identity, scope and family review

- Review: 20261021T073422Z-medial-cortex-septin-ring-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T07:23:37Z
- Finished UTC: 2026-10-21T07:34:22Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact structure identity, hierarchy and nonmechanistic topology are supported. One minor, resolvable generic-family grounding gap remains.

## Scope And Provenance

Entire single target and all its native GO references; exact Septin-family entry; relevant body sections of two contextual reviews.

Selection: Eighth unreviewed path in batch eight, in repository path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0036391 | data/structures/cytoskeleton/medial_cortex_septin_ring.yaml | maintained | medial cortex septin ring |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0036391 | Focused validator passed. |
| Focused native strict | passed | True | GO:0036391 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0036391 | 9 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | GO:0036391 | No transcriptional regulation or expression-module mechanism is asserted; the review uses structural ontology and literature context. |
| Claim-level scientific review | passed | True | GO:0036391 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0036391 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0036391 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0036391 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0036391 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0036391 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Exact structure and hierarchy

identity: supported. Targets: GO:0036391.

Exact target identity and parentage agree with native GO. The record denotes the medial-cortex ring of symmetric division; cited sibling identities are retained as distinct localizations.

### Bounded assembly and localization

graph: supported. Targets: GO:0036391.

Both graph edges express collective septin composition and medial-cortex placement at cytokinesis onset. No temporal molecular recruitment sequence, direct binding or autonomous contractility is asserted.

### Collective material and experimental examples

scope: supported. Targets: GO:0036391.

ESSENTIAL concerns the collective septin material class. It is not evidence that every paralog is individually required for viability, cytokinesis or sporulation. Species examples in the consulted reviews provide context without filling an exhaustive taxonomic distribution or conserved subunit list.

### Ontology source and literature tier

provenance: supported. Targets: GO:0036391.

Native GO directly supports the minimal assertions. The two consulted literature sources are reviews; their experimental summaries are scoped context, not a new primary-data audit. No new verbatim snippet is proposed.

### Generic family versus assembly cohort

grounding: concern. Targets: GO:0036391.

The generic septin-proteins row can use verified IPR016491 without resolving the complete medial-cortex cohort. The current rationale treats these distinct tasks together.

## Findings

### F1: Assembly-cohort criterion leaves generic Septin family ungrounded

minor / open / confirmed; issue key: medial-cortex-septin-ring-family-grounding-scope.

The generic septin-proteins row is REVIEWED_LABEL_ONLY while the rationale waits for an exact accession for its complete developmental or localized cohort. Native IPR016491 identifies the named generic Septin family. Reconcile that mapping with the status, notes and TODO, retaining the separate unresolved species-specific and accessory inventory.

## Recommended Actions And Acceptance Checks

### A1

Under separately authorized curation, map the generic septin class to verified IPR016491 and reconcile status/notes/TODO while preserving unresolved assembly membership.

- Verify native Septin family name/type and retain independent structure-localization evidence.
- Do not infer a universal subunit set, copy count, taxonomic distribution or individual-paralog essentiality.
- Use the guarded scientific writer and append curation/history records; run native schema, strict, label, history and generated-page checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| medial-ring-prep-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000144,GO:0005940,GO:0032168,GO:0032169,GO:0032170,GO:0032172,GO:0032175,GO:0032177,GO:0036391; All returned definitions, active status and parent-term child relations | supports | Native GO confirms every target and boundary identifier, exact definition and direct is-a parent. The medial-cortex ring remains distinct from bud-neck, split, prospore, mating-projection, hyphal, germ-tube and pseudohyphal localizations. |
| medial-ring-prep-family | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016491/; Native metadata accession, name, type=family and description | supports | IPR016491 is the Septin family. This identifies the generic septin-proteins class without supplying the full localized or developmental assembly cohort. |
| medial-ring-prep-versele-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC1761124/?pdf=render; Native PMC1761124 body sections S2, S4 and S11; Table1; review evidence, not independently repeated primary experiments | supports | Versele and Thorner2005 is a review cited by the GO definition. SectionS2 describes fission-yeast medial-cortex double rings at cytokinesis; sectionsS4/S11 distinguish multi-septin complex architecture from Mid2-dependent higher-order ring organization. Loss delays cytokinesis/separation and does not establish universal viability dependence. |
| medial-ring-prep-douglas-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC1214204/; Native PMC1214204 sec16 | context_only | Douglas2005 is contextual review evidence. Section16 distinguishes late-anaphase fission-yeast ring formation from budding-cell neck architecture; septin deletion primarily delays separation, and individual Spn proteins have different ring-assembly requirements. |
| medial-ring-prep-definition-pmid | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:16009555%20AND%20SRC:MED&amp;format=json&amp;resultType=core; Single exact PMID result: title, DOI, PMID, PMCID, author list, publication type and abstract | supports | Native bibliography verifies the GO definition reference PMID16009555, DOI10.1016/j.tcb.2005.06.007, title, authors and review type. Body scope is separately evidenced. |
| record | data/structures/cytoskeleton/medial_cortex_septin_ring.yaml; Entire target including history, graph and discussions | context_only | The record remains PROPOSED and models a generic class, with no species-specific protein examples, sequence accessions, quantitative copy counts or image claims. The graph is explicitly NONMECHANISTIC. |
| policy | docs/CURATION.md; Components; source-neutral grounding | context_only | Generic protein-family identity is separate from a complete localized cohort and species-specific subunit membership. |
| schema-result | just validate data/structures/cytoskeleton/medial_cortex_septin_ring.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/medial_cortex_septin_ring.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/medial_cortex_septin_ring.yaml --out /private/tmp/cellstructure-batch8-20261021-q561gvty/medial_cortex_septin_ring-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/medial_cortex_septin_ring.yaml --out /private/tmp/cellstructure-batch8-20261021-q561gvty/medial_cortex_septin_ring-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch8-20261021-q561gvty/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch8-20261021-q561gvty/medial_cortex_septin_ring-strict.tsv |
| target-curies | just check-curies-strict; data/structures/cytoskeleton/medial_cortex_septin_ring.yaml; exact collect() scope; SHA-256 identifies the entire original resolver TSV, not the derived resolver-slice.json | supports | 9 of 9 collected target identifiers returned OK at the unchanged base. Residuals: none. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- The consulted literature sources are reviews. Their cited primary experiments, raw data, figure pixels and supplements were not independently reanalyzed in this target audit.
- No species-specific full cohort, accessory boundary, stoichiometry or broad phylogenetic distribution is established by generic family grounding.
- The collective septin-material essentiality does not establish individual paralog necessity or a universal viability phenotype.
- Historical curation decisions are read as provenance; this review neither changes scientific status nor reconciles unrelated earlier issues.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Only the review bundle is saved. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T073422Z-medial-cortex-septin-ring-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Medial cortex septin ring identity, scope and family review
started_at: '2026-10-21T07:23:37Z'
finished_at: '2026-10-21T07:34:22Z'
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
summary: Exact structure identity, hierarchy and nonmechanistic topology are supported.
  One minor, resolvable generic-family grounding gap remains.
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
  - path: data/structures/cytoskeleton/medial_cortex_septin_ring.yaml
    sha256: 9286b6cd14a1d4ee846f71768e3e2c167d3254af72efc0e9437738dd16caddb6
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
- target_id: GO:0036391
  path: data/structures/cytoskeleton/medial_cortex_septin_ring.yaml
  label: medial cortex septin ring
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/medial_cortex_septin_ring.yaml
    role: maintained scientific record
scope:
  description: Entire single target and all its native GO references; exact Septin-family
    entry; relevant body sections of two contextual reviews.
  selection: Eighth unreviewed path in batch eight, in repository path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0036391
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0036391
  command: just validate data/structures/cytoskeleton/medial_cortex_septin_ring.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0036391
  command: just validate-strict data/structures/cytoskeleton/medial_cortex_septin_ring.yaml
    --out /private/tmp/cellstructure-batch8-20261021-q561gvty/medial_cortex_septin_ring-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0036391
  summary: 9 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0036391
  summary: No transcriptional regulation or expression-module mechanism is asserted;
    the review uses structural ontology and literature context.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0036391
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - medial-ring-prep-go
  - medial-ring-prep-family
  - medial-ring-prep-versele-pmc
  - medial-ring-prep-douglas-pmc
  - medial-ring-prep-definition-pmid
  - record
  - policy
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0036391
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch8 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0036391
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch8 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0036391
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch8 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0036391
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch8 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0036391
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch8 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: medial-ring-prep-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000144,GO:0005940,GO:0032168,GO:0032169,GO:0032170,GO:0032172,GO:0032175,GO:0032177,GO:0036391
  locator: All returned definitions, active status and parent-term child relations
  accessed_at: '2026-10-21T07:24:15.806774Z'
  support: supports
  summary: Native GO confirms every target and boundary identifier, exact definition
    and direct is-a parent. The medial-cortex ring remains distinct from bud-neck,
    split, prospore, mating-projection, hyphal, germ-tube and pseudohyphal localizations.
  snapshot_sha256: bd05a1f7c0321aa853ea43d5024f45dd8b008be1fc690cc540edd23157e133cc
- evidence_id: medial-ring-prep-family
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016491/
  locator: Native metadata accession, name, type=family and description
  accessed_at: '2026-10-21T06:58:21.193684Z'
  support: supports
  summary: IPR016491 is the Septin family. This identifies the generic septin-proteins
    class without supplying the full localized or developmental assembly cohort.
  snapshot_sha256: 5797c626d192b641ed5b4b2231e729f9f179bfd6bb18f911689fa08253688c4a
- evidence_id: medial-ring-prep-versele-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1761124/?pdf=render
  locator: Native PMC1761124 body sections S2, S4 and S11; Table1; review evidence,
    not independently repeated primary experiments
  accessed_at: '2026-10-21T07:29:14.610794Z'
  support: supports
  summary: Versele and Thorner2005 is a review cited by the GO definition. SectionS2
    describes fission-yeast medial-cortex double rings at cytokinesis; sectionsS4/S11
    distinguish multi-septin complex architecture from Mid2-dependent higher-order
    ring organization. Loss delays cytokinesis/separation and does not establish universal
    viability dependence.
  snapshot_sha256: bfa7c582507daf47688819cdd2ed31ed4dab32ed0d9e14a0d74d40c29249ac9d
- evidence_id: medial-ring-prep-douglas-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1214204/
  locator: Native PMC1214204 sec16
  accessed_at: '2026-10-21T07:11:03.050463Z'
  support: context_only
  summary: Douglas2005 is contextual review evidence. Section16 distinguishes late-anaphase
    fission-yeast ring formation from budding-cell neck architecture; septin deletion
    primarily delays separation, and individual Spn proteins have different ring-assembly
    requirements.
  snapshot_sha256: 31a2dd0109697492854f84701ef3f1d1be31f62312b613ab8432223332b69dd3
- evidence_id: medial-ring-prep-definition-pmid
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:16009555%20AND%20SRC:MED&format=json&resultType=core
  locator: 'Single exact PMID result: title, DOI, PMID, PMCID, author list, publication
    type and abstract'
  accessed_at: '2026-10-21T07:28:28.777748Z'
  support: supports
  summary: Native bibliography verifies the GO definition reference PMID16009555,
    DOI10.1016/j.tcb.2005.06.007, title, authors and review type. Body scope is separately
    evidenced.
  snapshot_sha256: e357d697a9b677792c488a9a5c9aa2654f106e7bbf22b5c706aaf6fbb0c331e5
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/medial_cortex_septin_ring.yaml
  locator: Entire target including history, graph and discussions
  accessed_at: '2026-10-21T07:32:42Z'
  support: context_only
  summary: The record remains PROPOSED and models a generic class, with no species-specific
    protein examples, sequence accessions, quantitative copy counts or image claims.
    The graph is explicitly NONMECHANISTIC.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Components; source-neutral grounding
  accessed_at: '2026-10-21T07:32:42Z'
  support: context_only
  summary: Generic protein-family identity is separate from a complete localized cohort
    and species-specific subunit membership.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/medial_cortex_septin_ring.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T07:23:39Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/medial_cortex_septin_ring.yaml'
  snapshot_sha256: 77c88014936723461c268cc1fe6d4d64d2399244bbd366439026e822c73c3a64
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/medial_cortex_septin_ring.yaml
    --out /private/tmp/cellstructure-batch8-20261021-q561gvty/medial_cortex_septin_ring-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T07:23:41Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/medial_cortex_septin_ring.yaml\
    \ --out /private/tmp/cellstructure-batch8-20261021-q561gvty/medial_cortex_septin_ring-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch8-20261021-q561gvty/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch8-20261021-q561gvty/medial_cortex_septin_ring-strict.tsv"
  snapshot_sha256: cf5f84fd92bae37a621eda8a55a211d64cb5a19d6706dd2fd72af5312c50bb69
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/medial_cortex_septin_ring.yaml; exact collect()
    scope; SHA-256 identifies the entire original resolver TSV, not the derived resolver-slice.json
  accessed_at: '2026-10-21T07:32:42Z'
  support: supports
  summary: '9 of 9 collected target identifiers returned OK at the unchanged base.
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
  topic: Exact structure and hierarchy
  outcome: supported
  target_ids:
  - GO:0036391
  summary: Exact target identity and parentage agree with native GO. The record denotes
    the medial-cortex ring of symmetric division; cited sibling identities are retained
    as distinct localizations.
  evidence_ids:
  - medial-ring-prep-go
  - record
- assessment_id: topology
  area: graph
  topic: Bounded assembly and localization
  outcome: supported
  target_ids:
  - GO:0036391
  summary: Both graph edges express collective septin composition and medial-cortex
    placement at cytokinesis onset. No temporal molecular recruitment sequence, direct
    binding or autonomous contractility is asserted.
  evidence_ids:
  - medial-ring-prep-go
  - medial-ring-prep-versele-pmc
  - record
- assessment_id: scope
  area: scope
  topic: Collective material and experimental examples
  outcome: supported
  target_ids:
  - GO:0036391
  summary: ESSENTIAL concerns the collective septin material class. It is not evidence
    that every paralog is individually required for viability, cytokinesis or sporulation.
    Species examples in the consulted reviews provide context without filling an exhaustive
    taxonomic distribution or conserved subunit list.
  evidence_ids:
  - medial-ring-prep-versele-pmc
  - medial-ring-prep-douglas-pmc
  - record
- assessment_id: evidence
  area: provenance
  topic: Ontology source and literature tier
  outcome: supported
  target_ids:
  - GO:0036391
  summary: Native GO directly supports the minimal assertions. The two consulted literature
    sources are reviews; their experimental summaries are scoped context, not a new
    primary-data audit. No new verbatim snippet is proposed.
  evidence_ids:
  - medial-ring-prep-go
  - medial-ring-prep-definition-pmid
  - medial-ring-prep-versele-pmc
  - medial-ring-prep-douglas-pmc
- assessment_id: grounding
  area: grounding
  topic: Generic family versus assembly cohort
  outcome: concern
  target_ids:
  - GO:0036391
  summary: The generic septin-proteins row can use verified IPR016491 without resolving
    the complete medial-cortex cohort. The current rationale treats these distinct
    tasks together.
  evidence_ids:
  - medial-ring-prep-family
  - policy
  - record
findings:
- finding_id: F1
  issue_key: medial-cortex-septin-ring-family-grounding-scope
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Assembly-cohort criterion leaves generic Septin family ungrounded
  description: The generic septin-proteins row is REVIEWED_LABEL_ONLY while the rationale
    waits for an exact accession for its complete developmental or localized cohort.
    Native IPR016491 identifies the named generic Septin family. Reconcile that mapping
    with the status, notes and TODO, retaining the separate unresolved species-specific
    and accessory inventory.
  target_ids:
  - GO:0036391
  field_paths:
  - components[component_id=septin_proteins].grounding_status
  - components[component_id=septin_proteins].grounding_notes
  - discussions[discussion_id=resolve_medial_cortex_septin_ring_components]
  evidence_ids:
  - medial-ring-prep-family
  - policy
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/medial_cortex_septin_ring.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components
  native_severity: minor
  normalization_reason: Bounded resolvable family mapping; exact structure identity,
    hierarchy and descriptive graph remain supported.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0036391
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/medial_cortex_septin_ring.yaml
    role: maintained scientific record
  description: Under separately authorized curation, map the generic septin class
    to verified IPR016491 and reconcile status/notes/TODO while preserving unresolved
    assembly membership.
  acceptance_checks:
  - Verify native Septin family name/type and retain independent structure-localization
    evidence.
  - Do not infer a universal subunit set, copy count, taxonomic distribution or individual-paralog
    essentiality.
  - Use the guarded scientific writer and append curation/history records; run native
    schema, strict, label, history and generated-page checks.
  generator: Maintained structure YAML; just render derives pages.
limitations:
- The consulted literature sources are reviews. Their cited primary experiments, raw
  data, figure pixels and supplements were not independently reanalyzed in this target
  audit.
- No species-specific full cohort, accessory boundary, stoichiometry or broad phylogenetic
  distribution is established by generic family grounding.
- The collective septin-material essentiality does not establish individual paralog
  necessity or a universal viability phenotype.
- Historical curation decisions are read as provenance; this review neither changes
  scientific status nor reconciles unrelated earlier issues.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- Only the review bundle is saved. Maintained scientific content, native status, history
  and generated pages remain unchanged.
```
