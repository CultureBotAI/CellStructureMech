# Germ-tube septin cap identity and family-grounding review

- Review: 20261021T070257Z-germ-tube-septin-cap-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T07:00:35Z
- Finished UTC: 2026-10-21T07:02:57Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact germ-tube septin cap identity and topology are supported. One minor finding concerns withholding the verified Septin family mapping on a localized-cohort criterion.

## Scope And Provenance

Complete one-record review, all cited GO boundaries, native Septin family and scoped published localization context.

Selection: Eighth distinct unreviewed path in batch six, in repository path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0032171 | data/structures/cytoskeleton/germ_tube_septin_cap.yaml | maintained | germ tube septin cap |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0032171 | Focused validator passed. |
| Focused native strict | passed | True | GO:0032171 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0032171 | 6 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | GO:0032171 | No named gene/regulator or expression-module assertion is present. Native ontology/family identity and localization context address the stated claims. |
| Claim-level scientific review | passed | True | GO:0032171 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0032171 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0032171 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0032171 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0032171 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0032171 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Distinct morphogenetic location and state

identity: supported. Targets: GO:0032171.

Exact native identity and broader parent are supported. The leading-edge cap is distinct from hyphal caps and future-septation rings, and direct germ-tube parthood is supported.

### Generic septin constituent class

evidence: supported. Targets: GO:0032171.

GO supports the septin class as a structural constituent. Collective ESSENTIAL denotes class-level necessity, not indispensability of every paralogue or a complete associated-protein inventory.

### Localization-specific cohort criterion

grounding: concern. Targets: GO:0032171.

The reviewed-label-only rationale seeks a family that exactly delimits the complete localized cohort. Verified IPR016491 denotes the generic Septin component class; the role/evidence already carry localization scope.

### Nonmechanistic cap topology

graph: supported. Targets: GO:0032171.

All four edges are supported: septin composition, apical localization, spatial ergosterol coincidence and germ-tube parthood. No directed membrane recruitment mechanism is asserted.

### Bounded topology with resolvable family gap

completeness: supported. Targets: GO:0032171.

The boundary discussion is coherent; the component-family TODO has a verified generic resolution.

## Findings

### F1: Localized-cohort criterion blocks verified Septin family grounding

minor / open / confirmed; issue key: germ-tube-septin-cap-family-grounding-scope.

The generic septin proteins component remains REVIEWED_LABEL_ONLY because its rationale requires a family delimiting the complete germ-tube cap cohort. IPR016491 is the verified Septin family. Component family identity need not encode localization; retain that experimental scope in role/evidence and reconcile the missing mapping, rationale and family TODO.

## Recommended Actions And Acceptance Checks

### A1

Under separately authorized curation, assign InterPro:IPR016491 to the generic septin class and reconcile grounding status, notes and family TODO. Retain localization evidence and the nonmechanistic cap/ergosterol boundary.

- Native family name/type match the generic Septin component class.
- No unverified paralogue, whole-cohort inventory or universal fungal distribution is introduced.
- Run native schema, strict, controlled-label, history and generated-page checks after curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| cap-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0032171,GO%3A0032159,GO%3A0032179,GO%3A0032164,GO%3A0032172; Complete native definitions and child relations for target and all cited boundary GO terms | supports | Native GO definitions and relations verify the exact localized cap identity, broader parent and germ-tube parthood, hyphal-cap and internal-ring boundaries. All cited terms are active. |
| cap-agent-family | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016491/; InterPro family name/type and scope | supports | IPR016491 is the full Septin family, an exact taxon-agnostic component class. Its identity need not delimit one localized cap or ring cohort. |
| cap-agent-primary-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22Septin%20function%20in%20Candida%20albicans%20morphogenesis%22%20OR%20TITLE:%22Lipid%20raft%20polarization%20contributes%20to%20hyphal%20growth%20in%20Candida%20albicans%22%20OR%20TITLE:%22The%20germ%20tubes%20of%20Candida%20albicans%20hyphae%20and%20pseudohyphae%22&amp;format=json&amp;resultType=core; Europe PMC primary identities and complete abstracts; PMID11454197 and associated septin studies | supports | Native article metadata and abstracts resolve the primary context. Sudbery2001 distinguishes the internal future-septation ring from early mother/germ-tube neck signal and the pseudohyphal neck ring. No primary full-text methods are assumed. |
| douglas-body | https://www.researchgate.net/publication/7611364_Septin_Function_in_Yeast_Model_Systems_and_Pathogenic_Fungi; Douglas et al.2005, Septins in C. albicans, pp.1508–1509; browser-readable full body inspected by read-only source collaborator; re-inspected during pre-save audit at the recorded access time | supports | The inspected review distinguishes the faint apical cap, diffuse basal band and later tight internal septation ring. Ergosterol enrichment spatially coincides with the apical cap; this does not prove recruitment or causal lipid-domain organization. Used as scoped published context, not primary perturbation evidence. |
| cap-agent-douglas-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1128/EC.4.9.1503-1512.2005&amp;format=json&amp;resultType=core; DOI10.1128/EC.4.9.1503-1512.2005 native metadata | supports | Native DOI/article metadata confirms Douglas et al.2005, Septin function in yeast model systems and pathogenic fungi. |
| record | data/structures/cytoskeleton/germ_tube_septin_cap.yaml; Entire maintained target | context_only | The target is PROPOSED, curates a generic septin constituent class and a NONMECHANISTIC topology graph, and has no organism-specific protein accession, measured dimension, image or universal fungal distribution assertion. |
| policy | docs/CURATION.md; Components: taxon-agnostic family or class | context_only | Family identity is separate from localized experimental role. A family term need not encode the complete localized cohort; exact family mappings should not be withheld solely for that reason. |
| schema-result | just validate data/structures/cytoskeleton/germ_tube_septin_cap.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/germ_tube_septin_cap.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/germ_tube_septin_cap.yaml --out /private/tmp/cellstructure-batch6-20261021-hj8mnf9r/germ_tube_septin_cap-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/germ_tube_septin_cap.yaml --out /private/tmp/cellstructure-batch6-20261021-hj8mnf9r/germ_tube_septin_cap-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch6-20261021-hj8mnf9r/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch6-20261021-hj8mnf9r/germ_tube_septin_cap-strict.tsv |
| target-curies | just check-curies-strict; data/structures/cytoskeleton/germ_tube_septin_cap.yaml; exact collect() scope | supports | 6 of6 collected target identifiers returned OK at the unchanged base. Residuals: none. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- The cited/source-linked2005 review body was inspected through a public author-uploaded browser display. Primary full-text routes returned API500, PMC challenge pages or failed alternative PDFs; primary methods and figures were not verified.
- Source C. albicans observations are context, not a universal fungal prevalence claim or proof of necessity for every septin paralogue.
- The topology graph establishes composition and location only; molecular recruitment order, accessory inventory and selective functional necessity remain outside its scope.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- A read-only collaborator inspected the native terms, family and published context; root read the complete target after native inspection.
- Only the review bundle is saved. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T070257Z-germ-tube-septin-cap-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Germ-tube septin cap identity and family-grounding review
started_at: '2026-10-21T07:00:35Z'
finished_at: '2026-10-21T07:02:57Z'
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
summary: Exact germ-tube septin cap identity and topology are supported. One minor
  finding concerns withholding the verified Septin family mapping on a localized-cohort
  criterion.
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
  - path: data/structures/cytoskeleton/germ_tube_septin_cap.yaml
    sha256: 2b38e6f9051b64b36fe4bb52206122b35d060e5146d548622573303fe0378732
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
- target_id: GO:0032171
  path: data/structures/cytoskeleton/germ_tube_septin_cap.yaml
  label: germ tube septin cap
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/germ_tube_septin_cap.yaml
    role: maintained scientific record
scope:
  description: Complete one-record review, all cited GO boundaries, native Septin
    family and scoped published localization context.
  selection: Eighth distinct unreviewed path in batch six, in repository path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0032171
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0032171
  command: just validate data/structures/cytoskeleton/germ_tube_septin_cap.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0032171
  command: just validate-strict data/structures/cytoskeleton/germ_tube_septin_cap.yaml
    --out /private/tmp/cellstructure-batch6-20261021-hj8mnf9r/germ_tube_septin_cap-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0032171
  summary: 6 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0032171
  summary: No named gene/regulator or expression-module assertion is present. Native
    ontology/family identity and localization context address the stated claims.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0032171
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - cap-agent-go
  - cap-agent-family
  - cap-agent-primary-metadata
  - douglas-body
  - cap-agent-douglas-metadata
  - record
  - policy
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0032171
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch6 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0032171
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch6 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0032171
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch6 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0032171
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch6 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0032171
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch6 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: cap-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0032171,GO%3A0032159,GO%3A0032179,GO%3A0032164,GO%3A0032172
  locator: Complete native definitions and child relations for target and all cited
    boundary GO terms
  accessed_at: '2026-10-21T06:58:21.189568Z'
  support: supports
  summary: Native GO definitions and relations verify the exact localized cap identity,
    broader parent and germ-tube parthood, hyphal-cap and internal-ring boundaries.
    All cited terms are active.
  snapshot_sha256: ac41a6e83fb73965a885e9e3be0e191257c4a2cb9dac043b3f77ac361a8855d4
- evidence_id: cap-agent-family
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016491/
  locator: InterPro family name/type and scope
  accessed_at: '2026-10-21T06:58:21.193684Z'
  support: supports
  summary: IPR016491 is the full Septin family, an exact taxon-agnostic component
    class. Its identity need not delimit one localized cap or ring cohort.
  snapshot_sha256: 5797c626d192b641ed5b4b2231e729f9f179bfd6bb18f911689fa08253688c4a
- evidence_id: cap-agent-primary-metadata
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22Septin%20function%20in%20Candida%20albicans%20morphogenesis%22%20OR%20TITLE:%22Lipid%20raft%20polarization%20contributes%20to%20hyphal%20growth%20in%20Candida%20albicans%22%20OR%20TITLE:%22The%20germ%20tubes%20of%20Candida%20albicans%20hyphae%20and%20pseudohyphae%22&format=json&resultType=core
  locator: Europe PMC primary identities and complete abstracts; PMID11454197 and
    associated septin studies
  accessed_at: '2026-10-21T06:59:10.582347Z'
  support: supports
  summary: Native article metadata and abstracts resolve the primary context. Sudbery2001
    distinguishes the internal future-septation ring from early mother/germ-tube neck
    signal and the pseudohyphal neck ring. No primary full-text methods are assumed.
  snapshot_sha256: b255025d436279a35a03aeae4342d1d3ab37db723123b56ada5e38095adcc603
- evidence_id: douglas-body
  kind: primary_source
  reference: https://www.researchgate.net/publication/7611364_Septin_Function_in_Yeast_Model_Systems_and_Pathogenic_Fungi
  locator: Douglas et al.2005, Septins in C. albicans, pp.1508–1509; browser-readable
    full body inspected by read-only source collaborator; re-inspected during pre-save
    audit at the recorded access time
  accessed_at: '2026-10-21T07:02:31Z'
  support: supports
  summary: The inspected review distinguishes the faint apical cap, diffuse basal
    band and later tight internal septation ring. Ergosterol enrichment spatially
    coincides with the apical cap; this does not prove recruitment or causal lipid-domain
    organization. Used as scoped published context, not primary perturbation evidence.
- evidence_id: cap-agent-douglas-metadata
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1128/EC.4.9.1503-1512.2005&format=json&resultType=core
  locator: DOI10.1128/EC.4.9.1503-1512.2005 native metadata
  accessed_at: '2026-10-21T06:58:21.193422Z'
  support: supports
  summary: Native DOI/article metadata confirms Douglas et al.2005, Septin function
    in yeast model systems and pathogenic fungi.
  snapshot_sha256: 1c4a6be031ab36975c4a274aec9c9d0182e2928499b9ee140022a8a1a4b80d1d
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/germ_tube_septin_cap.yaml
  locator: Entire maintained target
  accessed_at: '2026-10-21T07:01:51Z'
  support: context_only
  summary: The target is PROPOSED, curates a generic septin constituent class and
    a NONMECHANISTIC topology graph, and has no organism-specific protein accession,
    measured dimension, image or universal fungal distribution assertion.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: 'Components: taxon-agnostic family or class'
  accessed_at: '2026-10-21T07:01:51Z'
  support: context_only
  summary: Family identity is separate from localized experimental role. A family
    term need not encode the complete localized cohort; exact family mappings should
    not be withheld solely for that reason.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/germ_tube_septin_cap.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T07:00:38Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/germ_tube_septin_cap.yaml'
  snapshot_sha256: a36402e41c76e87a9032823667ad31e95a007a19ab08ef2ec5e5c177d334477e
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/germ_tube_septin_cap.yaml
    --out /private/tmp/cellstructure-batch6-20261021-hj8mnf9r/germ_tube_septin_cap-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T07:00:40Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/germ_tube_septin_cap.yaml\
    \ --out /private/tmp/cellstructure-batch6-20261021-hj8mnf9r/germ_tube_septin_cap-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch6-20261021-hj8mnf9r/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch6-20261021-hj8mnf9r/germ_tube_septin_cap-strict.tsv"
  snapshot_sha256: c7ab950fa56818ae7f80395b0081afcf4d254295763fcd850bfad3cab739c1f6
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/germ_tube_septin_cap.yaml; exact collect()
    scope
  accessed_at: '2026-10-21T07:01:51Z'
  support: supports
  summary: '6 of6 collected target identifiers returned OK at the unchanged base.
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
  topic: Distinct morphogenetic location and state
  outcome: supported
  target_ids:
  - GO:0032171
  summary: Exact native identity and broader parent are supported. The leading-edge
    cap is distinct from hyphal caps and future-septation rings, and direct germ-tube
    parthood is supported.
  evidence_ids:
  - cap-agent-go
  - cap-agent-primary-metadata
  - douglas-body
  - record
- assessment_id: composition
  area: evidence
  topic: Generic septin constituent class
  outcome: supported
  target_ids:
  - GO:0032171
  summary: GO supports the septin class as a structural constituent. Collective ESSENTIAL
    denotes class-level necessity, not indispensability of every paralogue or a complete
    associated-protein inventory.
  evidence_ids:
  - cap-agent-go
  - record
- assessment_id: family
  area: grounding
  topic: Localization-specific cohort criterion
  outcome: concern
  target_ids:
  - GO:0032171
  summary: The reviewed-label-only rationale seeks a family that exactly delimits
    the complete localized cohort. Verified IPR016491 denotes the generic Septin component
    class; the role/evidence already carry localization scope.
  evidence_ids:
  - cap-agent-family
  - policy
  - record
- assessment_id: graph
  area: graph
  topic: Nonmechanistic cap topology
  outcome: supported
  target_ids:
  - GO:0032171
  summary: 'All four edges are supported: septin composition, apical localization,
    spatial ergosterol coincidence and germ-tube parthood. No directed membrane recruitment
    mechanism is asserted.'
  evidence_ids:
  - cap-agent-go
  - cap-agent-primary-metadata
  - douglas-body
  - record
- assessment_id: completeness
  area: completeness
  topic: Bounded topology with resolvable family gap
  outcome: supported
  target_ids:
  - GO:0032171
  summary: The boundary discussion is coherent; the component-family TODO has a verified
    generic resolution.
  evidence_ids:
  - cap-agent-go
  - cap-agent-family
  - record
findings:
- finding_id: F1
  issue_key: germ-tube-septin-cap-family-grounding-scope
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Localized-cohort criterion blocks verified Septin family grounding
  description: The generic septin proteins component remains REVIEWED_LABEL_ONLY because
    its rationale requires a family delimiting the complete germ-tube cap cohort.
    IPR016491 is the verified Septin family. Component family identity need not encode
    localization; retain that experimental scope in role/evidence and reconcile the
    missing mapping, rationale and family TODO.
  target_ids:
  - GO:0032171
  field_paths:
  - components[component_id=septin_proteins].grounding_status
  - components[component_id=septin_proteins].grounding_notes
  - discussions[discussion_id=resolve_germ_tube_septin_cap_grounding]
  evidence_ids:
  - cap-agent-family
  - policy
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/germ_tube_septin_cap.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components
  native_severity: minor
  normalization_reason: The assembly identity and topology are supported; this is
    a bounded resolvable family-mapping gap rather than a wrong assigned identifier.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0032171
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/germ_tube_septin_cap.yaml
    role: maintained scientific record
  description: Under separately authorized curation, assign InterPro:IPR016491 to
    the generic septin class and reconcile grounding status, notes and family TODO.
    Retain localization evidence and the nonmechanistic cap/ergosterol boundary.
  acceptance_checks:
  - Native family name/type match the generic Septin component class.
  - No unverified paralogue, whole-cohort inventory or universal fungal distribution
    is introduced.
  - Run native schema, strict, controlled-label, history and generated-page checks
    after curation.
  generator: Maintained structure YAML; just render derives pages.
limitations:
- The cited/source-linked2005 review body was inspected through a public author-uploaded
  browser display. Primary full-text routes returned API500, PMC challenge pages or
  failed alternative PDFs; primary methods and figures were not verified.
- Source C. albicans observations are context, not a universal fungal prevalence claim
  or proof of necessity for every septin paralogue.
- The topology graph establishes composition and location only; molecular recruitment
  order, accessory inventory and selective functional necessity remain outside its
  scope.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- A read-only collaborator inspected the native terms, family and published context;
  root read the complete target after native inspection.
- Only the review bundle is saved. Maintained scientific content, native status, history
  and generated pages remain unchanged.
```
