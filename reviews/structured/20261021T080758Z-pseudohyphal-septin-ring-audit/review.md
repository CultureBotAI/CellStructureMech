# Pseudohyphal septin ring localization and generic-family review

- Review: 20261021T080758Z-pseudohyphal-septin-ring-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T07:53:53Z
- Finished UTC: 2026-10-21T08:07:58Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact pseudohyphal ring identity and junction topology are supported. One minor generic Septin-family grounding gap remains.

## Scope And Provenance

Entire single target, asserted GO identities, verified family, review context and relevant Candida primary localization results.

Selection: Fifth selected unreviewed path in batch ten, in repository path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0032170 | data/structures/cytoskeleton/pseudohyphal_septin_ring.yaml | maintained | pseudohyphal septin ring |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0032170 | Focused validator passed. |
| Focused native strict | passed | True | GO:0032170 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0032170 | 2 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | GO:0032170 | No expression-module or transcriptional-regulator mechanism is asserted; localized structural membership is not inferred from expression modules. |
| Claim-level scientific review | passed | True | GO:0032170 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0032170 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0032170 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0032170 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0032170 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0032170 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Pseudohyphal junction ring

identity: supported. Targets: GO:0032170.

GO confirms the exact ring class and direct septin-ring parent. The record does not collapse it into the apical cap, hyphal basal band or germ-tube internal septation ring.

### Collective septin material and junction localization

graph: supported. Targets: GO:0032170.

The component and two graph edges correctly describe septin material assembling at the mother-cell/pseudohyphal-projection junction. No fixed recruitment order, cytokinetic force production, universal paralog set or associated-protein inventory is asserted.

### Morphology-specific evidence and collective essentiality

scope: supported. Targets: GO:0032170.

Primary context concerns induced C. albicans morphologies. The target itself makes no exact species, strain or sequence example claim. Collective septin material is necessary for a septin ring by identity; this is not a claim that every paralog is necessary for cellular viability.

### Generic Septin family versus localized cohort

grounding: concern. Targets: GO:0032170.

The component label denotes septin proteins, but its grounding rationale waits for a family accession delimiting the full localized cohort. Verified IPR016491 matches the generic family; exact cohort and accessory membership remain independent unresolved questions.

### Review and primary source chain

provenance: supported. Targets: GO:0032170.

The ontology-derived statements are corroborated by the GO-cited review and relevant primary results. Historical review references in curation history are provenance, not newly verified resolution of those external issue threads.

## Findings

### F1: Localized-cohort criterion leaves the generic Septin family ungrounded

minor / open / confirmed; issue key: pseudohyphal-septin-ring-generic-family-withheld.

The generic septin-proteins component remains REVIEWED_LABEL_ONLY because no accession was assigned for the complete localized cohort. IPR016491 already identifies the named Septin family. Reconcile grounding, status and rationale without inferring an exhaustive localized paralog set or associated-protein inventory.

## Recommended Actions And Acceptance Checks

### A1

Under separately authorized curation, ground the generic Septin component to verified IPR016491 and reconcile its status and localized-cohort rationale.

- Retain separate evidence for localized membership and associated proteins.
- Do not add a universal paralog set, stoichiometry or individual essentiality.
- Use the guarded writer and required curation/history, schema, strict, label and generated-page checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| pseudohyphal-ring-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032170,GO:0005940,GO:0032172,GO:0032168; All returned definitions, isObsolete flags, exact identifiers and parent-term child relations | supports | Native GO verifies the exact active target definition and each cited parent/sibling identity. Parent-term child relations distinguish is-a specialization from structural parthood. |
| pseudohyphal-ring-agent-family | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016491/; Native accession, name, type=family, description and hierarchy; original retrieval timestamp retained | supports | IPR016491 is the Septin family. It supports the generic septin-proteins class without specifying every member of a localized assembly. |
| pseudohyphal-ring-agent-douglas-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1128/EC.4.9.1503-1512.2005&amp;format=json&amp;resultType=core; Exact DOI/PMID result, authors, title, year and review publication type | supports | Native metadata verifies Douglas, Alvarez, McCreary and Konopka2005, Septin Function in Yeast Model Systems and Pathogenic Fungi, DOI10.1128/EC.4.9.1503-1512.2005, PMID16151244. |
| record | data/structures/cytoskeleton/pseudohyphal_septin_ring.yaml; Entire target, history, component and any sequence examples, all graph edges and discussions | context_only | The complete PROPOSED target was read. The graph is explicitly NONMECHANISTIC. No scientific status or content is changed. |
| policy | docs/CURATION.md; Components: source-neutral family grounding, membership and structure-assembly essentiality | context_only | Generic protein-family identity is separate from localized assembly membership. ESSENTIAL denotes whether the structure forms, not universal cellular viability or each individual paralog requirement. |
| pseudohyphal-ring-agent-douglas-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC1214204/; Native PMC1214204 sec17; literature-review tier, original timestamp retained | supports | The review distinguishes the mother-cell/pseudohyphal junction ring from a hyphal internal septation ring, basal band and apical cap. |
| pseudohyphal-ring-agent-warenda2002 | https://pmc.ncbi.nlm.nih.gov/articles/PMC117938/?pdf=render; Native PMC117938 Results sec9/Figure2 caption and Discussion sec17; pseudohyphal induction versus serum-induced hyphal growth | supports | Primary Cdc10-GFP imaging shows rings at pseudohyphal necks; hyphal induction yields a distinct diffuse basal pattern followed by internal septation rings. This supports the morphology-dependent boundary without defining a universal complete subunit cohort. |
| pseudohyphal-ring-agent-primary-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:11454197%20OR%20EXT_ID:12181342%20OR%20EXT_ID:19915075&amp;format=json&amp;resultType=core; Relevant exact records and abstracts; Zhang2010 result is not used for this target | supports | Native metadata verifies Warenda/Konopka2002 DOI10.1091/mbc.E02-01-0013, PMID12181342, and Sudbery2001 PMID11454197/DOI10.1046/j.1365-2958.2001.02459.x. Sudbery abstract independently describes the pseudohyphal-neck versus hyphal-internal ring distinction. |
| schema-result | just validate data/structures/cytoskeleton/pseudohyphal_septin_ring.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/pseudohyphal_septin_ring.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/pseudohyphal_septin_ring.yaml --out /private/tmp/cellstructure-batch10-20261021-giynduuy/pseudohyphal_septin_ring-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/pseudohyphal_septin_ring.yaml --out /private/tmp/cellstructure-batch10-20261021-giynduuy/pseudohyphal_septin_ring-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch10-20261021-giynduuy/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch10-20261021-giynduuy/pseudohyphal_septin_ring-strict.tsv |
| target-curies | just check-curies-strict; data/structures/cytoskeleton/pseudohyphal_septin_ring.yaml; exact collect() scope; SHA-256 identifies the entire original resolver TSV at /private/tmp/cellstructure-record-reviews-UhRFh7/repo/reports/curie_check.tsv, not the derived resolver-slice.json | supports | 2 of 2 collected target identifiers returned OK at the unchanged base. Residuals: none. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Primary article prose and relevant figure legends were read; microscopy pixels, raw data and all supplements were not independently reanalyzed.
- The observed Candida conditions do not establish an exhaustive fungal distribution, fixed septin cohort or invariant temporal behavior.
- Exact localized paralogs and septin-associated proteins remain unresolved; the generic family mapping does not resolve those separate questions.
- Sudbery2001 is used at metadata/abstract level here; no unavailable body passage is treated as read.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Only a review bundle is saved. Maintained scientific content, native status, history and generated pages remain unchanged.
- Root read the complete target and review and verified every native input/source hash; selected primary and review sections were independently inspected. The source-tier and access limitations remain explicit.
- Only this target receives scientific review coverage. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T080758Z-pseudohyphal-septin-ring-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Pseudohyphal septin ring localization and generic-family review
started_at: '2026-10-21T07:53:53Z'
finished_at: '2026-10-21T08:07:58Z'
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
summary: Exact pseudohyphal ring identity and junction topology are supported. One
  minor generic Septin-family grounding gap remains.
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
  - path: data/structures/cytoskeleton/pseudohyphal_septin_ring.yaml
    sha256: 725c892c096cf75b48bb0a26a1aad5d657d9e5e716851f07211b161ba4d04533
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
- target_id: GO:0032170
  path: data/structures/cytoskeleton/pseudohyphal_septin_ring.yaml
  label: pseudohyphal septin ring
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/pseudohyphal_septin_ring.yaml
    role: maintained scientific record
scope:
  description: Entire single target, asserted GO identities, verified family, review
    context and relevant Candida primary localization results.
  selection: Fifth selected unreviewed path in batch ten, in repository path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0032170
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0032170
  command: just validate data/structures/cytoskeleton/pseudohyphal_septin_ring.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0032170
  command: just validate-strict data/structures/cytoskeleton/pseudohyphal_septin_ring.yaml
    --out /private/tmp/cellstructure-batch10-20261021-giynduuy/pseudohyphal_septin_ring-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0032170
  summary: 2 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0032170
  summary: No expression-module or transcriptional-regulator mechanism is asserted;
    localized structural membership is not inferred from expression modules.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0032170
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - pseudohyphal-ring-agent-go
  - pseudohyphal-ring-agent-family
  - pseudohyphal-ring-agent-douglas-metadata
  - record
  - policy
  - pseudohyphal-ring-agent-douglas-pmc
  - pseudohyphal-ring-agent-warenda2002
  - pseudohyphal-ring-agent-primary-metadata
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0032170
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch10 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0032170
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch10 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0032170
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch10 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0032170
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch10 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0032170
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch10 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: pseudohyphal-ring-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032170,GO:0005940,GO:0032172,GO:0032168
  locator: All returned definitions, isObsolete flags, exact identifiers and parent-term
    child relations
  accessed_at: '2026-10-21T07:55:02.179602Z'
  support: supports
  summary: Native GO verifies the exact active target definition and each cited parent/sibling
    identity. Parent-term child relations distinguish is-a specialization from structural
    parthood.
  snapshot_sha256: 3f924f9134a02cc5e72a0236ea06ae621c1480af51ea51954aeefb41d06a6dea
- evidence_id: pseudohyphal-ring-agent-family
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016491/
  locator: Native accession, name, type=family, description and hierarchy; original
    retrieval timestamp retained
  accessed_at: '2026-10-21T06:58:21.193684Z'
  support: supports
  summary: IPR016491 is the Septin family. It supports the generic septin-proteins
    class without specifying every member of a localized assembly.
  snapshot_sha256: 5797c626d192b641ed5b4b2231e729f9f179bfd6bb18f911689fa08253688c4a
- evidence_id: pseudohyphal-ring-agent-douglas-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1128/EC.4.9.1503-1512.2005&format=json&resultType=core
  locator: Exact DOI/PMID result, authors, title, year and review publication type
  accessed_at: '2026-10-21T06:58:21.193422Z'
  support: supports
  summary: Native metadata verifies Douglas, Alvarez, McCreary and Konopka2005, Septin
    Function in Yeast Model Systems and Pathogenic Fungi, DOI10.1128/EC.4.9.1503-1512.2005,
    PMID16151244.
  snapshot_sha256: 1c4a6be031ab36975c4a274aec9c9d0182e2928499b9ee140022a8a1a4b80d1d
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/pseudohyphal_septin_ring.yaml
  locator: Entire target, history, component and any sequence examples, all graph
    edges and discussions
  accessed_at: '2026-10-21T07:58:48Z'
  support: context_only
  summary: The complete PROPOSED target was read. The graph is explicitly NONMECHANISTIC.
    No scientific status or content is changed.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: 'Components: source-neutral family grounding, membership and structure-assembly
    essentiality'
  accessed_at: '2026-10-21T07:58:48Z'
  support: context_only
  summary: Generic protein-family identity is separate from localized assembly membership.
    ESSENTIAL denotes whether the structure forms, not universal cellular viability
    or each individual paralog requirement.
- evidence_id: pseudohyphal-ring-agent-douglas-pmc
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1214204/
  locator: Native PMC1214204 sec17; literature-review tier, original timestamp retained
  accessed_at: '2026-10-21T07:11:03.050463Z'
  support: supports
  summary: The review distinguishes the mother-cell/pseudohyphal junction ring from
    a hyphal internal septation ring, basal band and apical cap.
  snapshot_sha256: 31a2dd0109697492854f84701ef3f1d1be31f62312b613ab8432223332b69dd3
- evidence_id: pseudohyphal-ring-agent-warenda2002
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC117938/?pdf=render
  locator: Native PMC117938 Results sec9/Figure2 caption and Discussion sec17; pseudohyphal
    induction versus serum-induced hyphal growth
  accessed_at: '2026-10-21T07:55:41.272909Z'
  support: supports
  summary: Primary Cdc10-GFP imaging shows rings at pseudohyphal necks; hyphal induction
    yields a distinct diffuse basal pattern followed by internal septation rings.
    This supports the morphology-dependent boundary without defining a universal complete
    subunit cohort.
  snapshot_sha256: 7b0552af320b38fa21e9800ad0e493cf04cb5f02f85d578e45acd0340f634cdb
- evidence_id: pseudohyphal-ring-agent-primary-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:11454197%20OR%20EXT_ID:12181342%20OR%20EXT_ID:19915075&format=json&resultType=core
  locator: Relevant exact records and abstracts; Zhang2010 result is not used for
    this target
  accessed_at: '2026-10-21T07:55:02.786179Z'
  support: supports
  summary: Native metadata verifies Warenda/Konopka2002 DOI10.1091/mbc.E02-01-0013,
    PMID12181342, and Sudbery2001 PMID11454197/DOI10.1046/j.1365-2958.2001.02459.x.
    Sudbery abstract independently describes the pseudohyphal-neck versus hyphal-internal
    ring distinction.
  snapshot_sha256: 58f7e5efb372dd4a4ada8d719d795922ba1fd216d101f7fe33dbf9adb0a9d244
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/pseudohyphal_septin_ring.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T07:53:54Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/pseudohyphal_septin_ring.yaml'
  snapshot_sha256: 8d8b68ed45ba9687cdf6b2e9b31c8621d9f02205c12106ff2eacb2a1d9c037a8
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/pseudohyphal_septin_ring.yaml
    --out /private/tmp/cellstructure-batch10-20261021-giynduuy/pseudohyphal_septin_ring-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T07:53:56Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/pseudohyphal_septin_ring.yaml\
    \ --out /private/tmp/cellstructure-batch10-20261021-giynduuy/pseudohyphal_septin_ring-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch10-20261021-giynduuy/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch10-20261021-giynduuy/pseudohyphal_septin_ring-strict.tsv"
  snapshot_sha256: 609b1d45ec26ed90c031da5a751f7a026873f4b443ba1ca5bcfb1cca0bd2f0ca
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/pseudohyphal_septin_ring.yaml; exact collect()
    scope; SHA-256 identifies the entire original resolver TSV at /private/tmp/cellstructure-record-reviews-UhRFh7/repo/reports/curie_check.tsv,
    not the derived resolver-slice.json
  accessed_at: '2026-10-21T07:58:48Z'
  support: supports
  summary: '2 of 2 collected target identifiers returned OK at the unchanged base.
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
  topic: Pseudohyphal junction ring
  outcome: supported
  target_ids:
  - GO:0032170
  summary: GO confirms the exact ring class and direct septin-ring parent. The record
    does not collapse it into the apical cap, hyphal basal band or germ-tube internal
    septation ring.
  evidence_ids:
  - pseudohyphal-ring-agent-go
  - pseudohyphal-ring-agent-douglas-pmc
  - pseudohyphal-ring-agent-warenda2002
  - record
- assessment_id: graph
  area: graph
  topic: Collective septin material and junction localization
  outcome: supported
  target_ids:
  - GO:0032170
  summary: The component and two graph edges correctly describe septin material assembling
    at the mother-cell/pseudohyphal-projection junction. No fixed recruitment order,
    cytokinetic force production, universal paralog set or associated-protein inventory
    is asserted.
  evidence_ids:
  - pseudohyphal-ring-agent-go
  - pseudohyphal-ring-agent-douglas-pmc
  - pseudohyphal-ring-agent-warenda2002
  - record
- assessment_id: scope
  area: scope
  topic: Morphology-specific evidence and collective essentiality
  outcome: supported
  target_ids:
  - GO:0032170
  summary: Primary context concerns induced C. albicans morphologies. The target itself
    makes no exact species, strain or sequence example claim. Collective septin material
    is necessary for a septin ring by identity; this is not a claim that every paralog
    is necessary for cellular viability.
  evidence_ids:
  - pseudohyphal-ring-agent-warenda2002
  - pseudohyphal-ring-agent-douglas-pmc
  - record
  - policy
- assessment_id: family
  area: grounding
  topic: Generic Septin family versus localized cohort
  outcome: concern
  target_ids:
  - GO:0032170
  summary: The component label denotes septin proteins, but its grounding rationale
    waits for a family accession delimiting the full localized cohort. Verified IPR016491
    matches the generic family; exact cohort and accessory membership remain independent
    unresolved questions.
  evidence_ids:
  - pseudohyphal-ring-agent-family
  - record
  - policy
- assessment_id: provenance
  area: provenance
  topic: Review and primary source chain
  outcome: supported
  target_ids:
  - GO:0032170
  summary: The ontology-derived statements are corroborated by the GO-cited review
    and relevant primary results. Historical review references in curation history
    are provenance, not newly verified resolution of those external issue threads.
  evidence_ids:
  - pseudohyphal-ring-agent-go
  - pseudohyphal-ring-agent-douglas-metadata
  - pseudohyphal-ring-agent-douglas-pmc
  - pseudohyphal-ring-agent-primary-metadata
  - pseudohyphal-ring-agent-warenda2002
  - record
findings:
- finding_id: F1
  issue_key: pseudohyphal-septin-ring-generic-family-withheld
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Localized-cohort criterion leaves the generic Septin family ungrounded
  description: The generic septin-proteins component remains REVIEWED_LABEL_ONLY because
    no accession was assigned for the complete localized cohort. IPR016491 already
    identifies the named Septin family. Reconcile grounding, status and rationale
    without inferring an exhaustive localized paralog set or associated-protein inventory.
  target_ids:
  - GO:0032170
  field_paths:
  - components[component_id=septin_proteins].grounding_status
  - components[component_id=septin_proteins].grounding_notes
  - discussions
  evidence_ids:
  - pseudohyphal-ring-agent-family
  - record
  - policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/pseudohyphal_septin_ring.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components
  native_severity: minor
  normalization_reason: A bounded, resolvable generic-family mapping gap; no change
    to exact structure identity is implied.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0032170
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/pseudohyphal_septin_ring.yaml
    role: maintained scientific record
  description: Under separately authorized curation, ground the generic Septin component
    to verified IPR016491 and reconcile its status and localized-cohort rationale.
  acceptance_checks:
  - Retain separate evidence for localized membership and associated proteins.
  - Do not add a universal paralog set, stoichiometry or individual essentiality.
  - Use the guarded writer and required curation/history, schema, strict, label and
    generated-page checks.
  generator: Maintained structure YAML; pages derive through just render.
limitations:
- Primary article prose and relevant figure legends were read; microscopy pixels,
  raw data and all supplements were not independently reanalyzed.
- The observed Candida conditions do not establish an exhaustive fungal distribution,
  fixed septin cohort or invariant temporal behavior.
- Exact localized paralogs and septin-associated proteins remain unresolved; the generic
  family mapping does not resolve those separate questions.
- Sudbery2001 is used at metadata/abstract level here; no unavailable body passage
  is treated as read.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- Only a review bundle is saved. Maintained scientific content, native status, history
  and generated pages remain unchanged.
- Root read the complete target and review and verified every native input/source
  hash; selected primary and review sections were independently inspected. The source-tier
  and access limitations remain explicit.
- Only this target receives scientific review coverage. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
