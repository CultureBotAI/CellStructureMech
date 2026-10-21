# Invasive-hyphae septin collar protein mapping review

- Review: 20261021T071712Z-hyphae-septin-collar-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T07:15:22Z
- Finished UTC: 2026-10-21T07:17:12Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The collar identity and source-bounded topology are supported, but three protein-to-SEP gene mappings are wrong; generic family grounding is also resolvable.

## Scope And Provenance

Entire single target, all native identifiers, source-defined boundaries and component scope.

Selection: Fifth unreviewed path in batch seven, in repository path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0062140 | data/structures/cytoskeleton/hyphae_septin_collar.yaml | maintained | hyphae septin collar |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0062140 | Focused validator passed. |
| Focused native strict | passed | True | GO:0062140 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0062140 | 9 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | GO:0062140 | No expression-module mechanism or transcriptional-regulator graph is asserted. |
| Claim-level scientific review | passed | True | GO:0062140 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0062140 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0062140 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0062140 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0062140 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0062140 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Invasive collar distinct from division-site ring

identity: supported. Targets: GO:0062140.

Exact GO identity, related synonym and parent agree. The source describes the invasive wall-crossing collar, distinct from the earlier appressorium ring and the septation ring.

### Species example and reference sequence

scope: supported. Targets: GO:0062140.

The species-level example and variable invasive-growth context are source-supported. Reference70-15 accessions are not represented as the exact Guy11 experimental strain.

### SEP symbols and reference loci

grounding: concern. Targets: GO:0062140.

Native accession-to-locus identities resolve, but their asserted SEP3/4/5 correspondences are contradicted by a primary gene-identity table.

### Bounded septin material composition

graph: supported. Targets: GO:0062140.

The graph records septins assembling into the collar without importing an ordered recruitment or full Pmk1 regulatory pathway. Collective septin material essentiality is not a claim that each listed paralog is individually indispensable.

### Generic family versus localized cohort

grounding: concern. Targets: GO:0062140.

A verified family is available for the generic septin-proteins row. Requiring it to delimit the complete localized cohort unnecessarily withholds this mapping.

## Findings

### F1: Three protein examples assign conflicting SEP gene identities

major / open / confirmed; issue key: hyphae-septin-collar-sep-protein-locus-mismatch.

The record calls G4ML89/MGG_06726 SEP3, G4NJK4/MGG_02626 SEP4, and G4N7W8/MGG_06341 SEP5. Primary Table1 instead maps SEP3=MGG_01521, SEP4=MGG_06726, and SEP5=MGG_03087. Native UniProt establishes the accession–ORF pairs but supplies none of the asserted SEP aliases. The identity-only disclaimer does not repair these wrong gene correspondences.

### F2: Localized-cohort criterion blocks verified Septin family grounding

minor / open / confirmed; issue key: hyphae-septin-collar-family-grounding-scope.

The generic septin-proteins component remains REVIEWED_LABEL_ONLY because the rationale requires a family delimiting the complete localized cohort. Native IPR016491 is the verified Septin family. Family identity does not encode localization; reconcile the missing mapping, rationale and TODO while preserving experimental cohort uncertainty.

## Recommended Actions And Acceptance Checks

### A1

Re-resolve each intended SEP example against a primary symbol-to-locus mapping and native sequence authority. Correct or remove conflicting example prose/accessions and inaccurate UniProt attribution under separately authorized curation.

- Every retained SEP symbol, locus and accession denotes the same protein.
- Verify native protein labels, taxon and entry status; preserve reference-strain versus experimental-strain scope.
- Use the2015 table only for gene identity; do not import appressorium localization as invasive-collar membership.
- Run native schema, strict, label, history and generated-page checks.

### A2

Assign the verified Septin family to the generic component class and reconcile grounding status, notes and TODO under separately authorized curation.

- Native family name/type match the class; retain separate localization evidence.
- Do not infer complete paralog membership, individual necessity or universal fungal distribution.
- Run native schema, strict, label, history and generated-page checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| hyphae-collar-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0062140%2CGO%3A0032173%2CGO%3A0032168; All returned definitions, synonyms where present, and parent-term child edges | supports | Native GO confirms exact identity, direct parent relation and distinct future-septation hyphal ring. |
| hyphae-collar-agent-family | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016491/; metadata accession, name, type and description | supports | IPR016491 is the native Septin family; it identifies the generic protein class, not a complete localized cohort. |
| record | data/structures/cytoskeleton/hyphae_septin_collar.yaml; Entire maintained YAML including component and all discussions | context_only | The record is PROPOSED and limits its graph to composition and localization. Family grounding is withheld because no accession delimits the complete localized cohort. |
| policy | docs/CURATION.md; Components; source-neutral family grounding and taxon-paired protein examples | context_only | Generic component family identity is separate from experimental membership, localization and taxon-specific examples. |
| hyphae-collar-agent-taxon-318829 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/318829; taxId, scientificName, synonymy and rank | supports | ENA verifies Pyricularia oryzae, including Magnaporthe oryzae synonym. |
| hyphae-collar-agent-taxon-242507 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/242507; taxId, scientificName, synonymy and rank | supports | ENA verifies reference strain Pyricularia oryzae70-15. |
| hyphae-collar-agent-proteins | https://rest.uniprot.org/uniprotkb/search?query=(accession:G4ML89%20OR%20accession:G4NJK4%20OR%20accession:G4N7W8)&amp;format=json; G4ML89/MGG_06726; G4NJK4/MGG_02626; G4N7W8/MGG_06341; all gene and organism objects | supports | The three native unreviewed entries resolve the stated accessions, protein names, taxon and MGG ORF names. They do not list the claimed SEP aliases or identify those ORFs as primary gene names. |
| hyphae-collar-agent-primary2018 | https://pure.plymouth.ac.uk/ws/portalfiles/portal/39193581/Final%2BAccepted%2BVersion%2BTotal%2BSakukoo2018%2Bfor%2Bdeposit.pdf; Accepted manuscript main text, Figure1F and Figure4B captions, strain Methods; source collaborator also visually inspected figures | supports | Sakulkoo2018 directly reports Sep5-GFP collars at rice cell crossings and disorganization after conditional Pmk1 inhibition. The experimental strains derive from Guy11/pmk1 mutant backgrounds;70-15 is reference-genome context. |
| hyphae-collar-agent-primary2018-alias-check-2015-pdf | https://pure.plymouth.ac.uk/ws/portalfiles/portal/39155300/Plant%20Cell-2015-Gupta-tpc.15.00552-2.pdf; Table1, printed page4/PDF page5 including cover; root visually inspected the table; DOI10.1105/tpc.15.00552 | refutes | Gupta2015 Table1 maps Sep3 to MGG_01521, Sep4 to MGG_06726, Sep5 to MGG_03087 and Sep6 to MGG_07466. Each of the target’s three SEP-to-locus claims conflicts with this table. |
| schema-result | just validate data/structures/cytoskeleton/hyphae_septin_collar.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/hyphae_septin_collar.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/hyphae_septin_collar.yaml --out /private/tmp/cellstructure-batch7-20261021-dz9x5cv0/hyphae_septin_collar-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/hyphae_septin_collar.yaml --out /private/tmp/cellstructure-batch7-20261021-dz9x5cv0/hyphae_septin_collar-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch7-20261021-dz9x5cv0/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch7-20261021-dz9x5cv0/hyphae_septin_collar-strict.tsv |
| target-curies | just check-curies-strict; data/structures/cytoskeleton/hyphae_septin_collar.yaml; exact collect() scope | supports | 9 of9 collected target identifiers returned OK at the unchanged base. Residuals: none. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- The2015 appressorium/exocyst study is used only for gene identity, not invasive-collar localization or functional phenotypes.
- The2018 accepted manuscript was read; publisher-version byte identity, movies and raw experimental data were not examined.
- A generic family does not establish every localized paralog or its individual necessity.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Only the review bundle is saved. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T071712Z-hyphae-septin-collar-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Invasive-hyphae septin collar protein mapping review
started_at: '2026-10-21T07:15:22Z'
finished_at: '2026-10-21T07:17:12Z'
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
summary: The collar identity and source-bounded topology are supported, but three
  protein-to-SEP gene mappings are wrong; generic family grounding is also resolvable.
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
  - path: data/structures/cytoskeleton/hyphae_septin_collar.yaml
    sha256: 9e143ed6218b251660020e57fd99c4758ea02e5ce91e6cf8de3133f626d08f26
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
- target_id: GO:0062140
  path: data/structures/cytoskeleton/hyphae_septin_collar.yaml
  label: hyphae septin collar
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/hyphae_septin_collar.yaml
    role: maintained scientific record
scope:
  description: Entire single target, all native identifiers, source-defined boundaries
    and component scope.
  selection: Fifth unreviewed path in batch seven, in repository path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0062140
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0062140
  command: just validate data/structures/cytoskeleton/hyphae_septin_collar.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0062140
  command: just validate-strict data/structures/cytoskeleton/hyphae_septin_collar.yaml
    --out /private/tmp/cellstructure-batch7-20261021-dz9x5cv0/hyphae_septin_collar-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0062140
  summary: 9 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0062140
  summary: No expression-module mechanism or transcriptional-regulator graph is asserted.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0062140
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - hyphae-collar-agent-go
  - hyphae-collar-agent-family
  - record
  - policy
  - hyphae-collar-agent-taxon-318829
  - hyphae-collar-agent-taxon-242507
  - hyphae-collar-agent-proteins
  - hyphae-collar-agent-primary2018
  - hyphae-collar-agent-primary2018-alias-check-2015-pdf
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0062140
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch7 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0062140
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch7 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0062140
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch7 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0062140
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch7 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0062140
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch7 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: hyphae-collar-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0062140%2CGO%3A0032173%2CGO%3A0032168
  locator: All returned definitions, synonyms where present, and parent-term child
    edges
  accessed_at: '2026-10-21T07:10:23.659011Z'
  support: supports
  summary: Native GO confirms exact identity, direct parent relation and distinct
    future-septation hyphal ring.
  snapshot_sha256: d0c961779a5a3d3f3d2f0cedfd02428e86406f5f630548d5d79fc12141eb5db0
- evidence_id: hyphae-collar-agent-family
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016491/
  locator: metadata accession, name, type and description
  accessed_at: '2026-10-21T06:58:21.193684Z'
  support: supports
  summary: IPR016491 is the native Septin family; it identifies the generic protein
    class, not a complete localized cohort.
  snapshot_sha256: 5797c626d192b641ed5b4b2231e729f9f179bfd6bb18f911689fa08253688c4a
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/hyphae_septin_collar.yaml
  locator: Entire maintained YAML including component and all discussions
  accessed_at: '2026-10-21T07:17:12Z'
  support: context_only
  summary: The record is PROPOSED and limits its graph to composition and localization.
    Family grounding is withheld because no accession delimits the complete localized
    cohort.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Components; source-neutral family grounding and taxon-paired protein examples
  accessed_at: '2026-10-21T07:17:12Z'
  support: context_only
  summary: Generic component family identity is separate from experimental membership,
    localization and taxon-specific examples.
- evidence_id: hyphae-collar-agent-taxon-318829
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/318829
  locator: taxId, scientificName, synonymy and rank
  accessed_at: '2026-10-21T07:10:23.755388Z'
  support: supports
  summary: ENA verifies Pyricularia oryzae, including Magnaporthe oryzae synonym.
  snapshot_sha256: 2b63a207df9f0e7efbbaec3e5e429627dab76ce6fe3e1723a5c9f4b3cdecfe3b
- evidence_id: hyphae-collar-agent-taxon-242507
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/242507
  locator: taxId, scientificName, synonymy and rank
  accessed_at: '2026-10-21T07:10:23.691908Z'
  support: supports
  summary: ENA verifies reference strain Pyricularia oryzae70-15.
  snapshot_sha256: 9e174fe2314bab4bedf6e2102d2a363406c1e785666442e06af65ec45d5f1d31
- evidence_id: hyphae-collar-agent-proteins
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?query=(accession:G4ML89%20OR%20accession:G4NJK4%20OR%20accession:G4N7W8)&format=json
  locator: G4ML89/MGG_06726; G4NJK4/MGG_02626; G4N7W8/MGG_06341; all gene and organism
    objects
  accessed_at: '2026-10-21T07:10:23.976274Z'
  support: supports
  summary: The three native unreviewed entries resolve the stated accessions, protein
    names, taxon and MGG ORF names. They do not list the claimed SEP aliases or identify
    those ORFs as primary gene names.
  snapshot_sha256: 78387114bae556cffb4ad8ea16b997d4aeecf7030dd783ea44faf1025c8c7441
- evidence_id: hyphae-collar-agent-primary2018
  kind: primary_source
  reference: https://pure.plymouth.ac.uk/ws/portalfiles/portal/39193581/Final%2BAccepted%2BVersion%2BTotal%2BSakukoo2018%2Bfor%2Bdeposit.pdf
  locator: Accepted manuscript main text, Figure1F and Figure4B captions, strain Methods;
    source collaborator also visually inspected figures
  accessed_at: '2026-10-21T07:10:27.185563Z'
  support: supports
  summary: Sakulkoo2018 directly reports Sep5-GFP collars at rice cell crossings and
    disorganization after conditional Pmk1 inhibition. The experimental strains derive
    from Guy11/pmk1 mutant backgrounds;70-15 is reference-genome context.
  snapshot_sha256: 1f6c16204a56bf596045d45074394f065db4da30576840e28278b30d7c353d8b
- evidence_id: hyphae-collar-agent-primary2018-alias-check-2015-pdf
  kind: primary_source
  reference: https://pure.plymouth.ac.uk/ws/portalfiles/portal/39155300/Plant%20Cell-2015-Gupta-tpc.15.00552-2.pdf
  locator: Table1, printed page4/PDF page5 including cover; root visually inspected
    the table; DOI10.1105/tpc.15.00552
  accessed_at: '2026-10-21T07:11:54.761768Z'
  support: refutes
  summary: Gupta2015 Table1 maps Sep3 to MGG_01521, Sep4 to MGG_06726, Sep5 to MGG_03087
    and Sep6 to MGG_07466. Each of the target’s three SEP-to-locus claims conflicts
    with this table.
  snapshot_sha256: b69416a6e3e6e9f695a41f7109e7f3095124c2a8411d158a9db9e3d8e33ffcde
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/hyphae_septin_collar.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T07:15:28Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/hyphae_septin_collar.yaml'
  snapshot_sha256: 88cf2ac446f6ce53074f4425e9aab6c0334a512392044cce6198494d6673ac95
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/hyphae_septin_collar.yaml
    --out /private/tmp/cellstructure-batch7-20261021-dz9x5cv0/hyphae_septin_collar-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T07:15:33Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/hyphae_septin_collar.yaml\
    \ --out /private/tmp/cellstructure-batch7-20261021-dz9x5cv0/hyphae_septin_collar-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch7-20261021-dz9x5cv0/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch7-20261021-dz9x5cv0/hyphae_septin_collar-strict.tsv"
  snapshot_sha256: d848984ea2046f5d8f55f985b2130b03918efba0c9545c31470d99fc3563d4ee
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/hyphae_septin_collar.yaml; exact collect()
    scope
  accessed_at: '2026-10-21T07:17:12Z'
  support: supports
  summary: '9 of9 collected target identifiers returned OK at the unchanged base.
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
  topic: Invasive collar distinct from division-site ring
  outcome: supported
  target_ids:
  - GO:0062140
  summary: Exact GO identity, related synonym and parent agree. The source describes
    the invasive wall-crossing collar, distinct from the earlier appressorium ring
    and the septation ring.
  evidence_ids:
  - hyphae-collar-agent-go
  - hyphae-collar-agent-primary2018
  - record
- assessment_id: scope
  area: scope
  topic: Species example and reference sequence
  outcome: supported
  target_ids:
  - GO:0062140
  summary: The species-level example and variable invasive-growth context are source-supported.
    Reference70-15 accessions are not represented as the exact Guy11 experimental
    strain.
  evidence_ids:
  - hyphae-collar-agent-taxon-318829
  - hyphae-collar-agent-taxon-242507
  - hyphae-collar-agent-primary2018
  - hyphae-collar-agent-proteins
- assessment_id: examples
  area: grounding
  topic: SEP symbols and reference loci
  outcome: concern
  target_ids:
  - GO:0062140
  summary: Native accession-to-locus identities resolve, but their asserted SEP3/4/5
    correspondences are contradicted by a primary gene-identity table.
  evidence_ids:
  - hyphae-collar-agent-proteins
  - hyphae-collar-agent-primary2018-alias-check-2015-pdf
  - record
- assessment_id: topology
  area: graph
  topic: Bounded septin material composition
  outcome: supported
  target_ids:
  - GO:0062140
  summary: The graph records septins assembling into the collar without importing
    an ordered recruitment or full Pmk1 regulatory pathway. Collective septin material
    essentiality is not a claim that each listed paralog is individually indispensable.
  evidence_ids:
  - hyphae-collar-agent-go
  - hyphae-collar-agent-primary2018
  - record
- assessment_id: family
  area: grounding
  topic: Generic family versus localized cohort
  outcome: concern
  target_ids:
  - GO:0062140
  summary: A verified family is available for the generic septin-proteins row. Requiring
    it to delimit the complete localized cohort unnecessarily withholds this mapping.
  evidence_ids:
  - hyphae-collar-agent-family
  - policy
  - record
findings:
- finding_id: F1
  issue_key: hyphae-septin-collar-sep-protein-locus-mismatch
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Three protein examples assign conflicting SEP gene identities
  description: The record calls G4ML89/MGG_06726 SEP3, G4NJK4/MGG_02626 SEP4, and
    G4N7W8/MGG_06341 SEP5. Primary Table1 instead maps SEP3=MGG_01521, SEP4=MGG_06726,
    and SEP5=MGG_03087. Native UniProt establishes the accession–ORF pairs but supplies
    none of the asserted SEP aliases. The identity-only disclaimer does not repair
    these wrong gene correspondences.
  target_ids:
  - GO:0062140
  field_paths:
  - components[component_id=septin_proteins].protein_examples
  evidence_ids:
  - hyphae-collar-agent-proteins
  - hyphae-collar-agent-primary2018-alias-check-2015-pdf
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/hyphae_septin_collar.yaml
    role: maintained scientific record
  rule_id: CLAUDE.md:Never guess a CURIE
  native_severity: major
  normalization_reason: Wrong protein-to-gene identities materially misidentify the
    named examples; whole-structure identity remains correct.
- finding_id: F2
  issue_key: hyphae-septin-collar-family-grounding-scope
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Localized-cohort criterion blocks verified Septin family grounding
  description: The generic septin-proteins component remains REVIEWED_LABEL_ONLY because
    the rationale requires a family delimiting the complete localized cohort. Native
    IPR016491 is the verified Septin family. Family identity does not encode localization;
    reconcile the missing mapping, rationale and TODO while preserving experimental
    cohort uncertainty.
  target_ids:
  - GO:0062140
  field_paths:
  - components[component_id=septin_proteins].grounding_status
  - components[component_id=septin_proteins].grounding_notes
  - discussions[discussion_id=resolve_hyphae_septin_collar_grounding]
  evidence_ids:
  - hyphae-collar-agent-family
  - policy
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/hyphae_septin_collar.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components
  native_severity: minor
  normalization_reason: Bounded resolvable family-mapping gap; no wrong family has
    been assigned.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0062140
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/hyphae_septin_collar.yaml
    role: maintained scientific record
  description: Re-resolve each intended SEP example against a primary symbol-to-locus
    mapping and native sequence authority. Correct or remove conflicting example prose/accessions
    and inaccurate UniProt attribution under separately authorized curation.
  acceptance_checks:
  - Every retained SEP symbol, locus and accession denotes the same protein.
  - Verify native protein labels, taxon and entry status; preserve reference-strain
    versus experimental-strain scope.
  - Use the2015 table only for gene identity; do not import appressorium localization
    as invasive-collar membership.
  - Run native schema, strict, label, history and generated-page checks.
  generator: Maintained structure YAML; just render derives pages.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0062140
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/hyphae_septin_collar.yaml
    role: maintained scientific record
  description: Assign the verified Septin family to the generic component class and
    reconcile grounding status, notes and TODO under separately authorized curation.
  acceptance_checks:
  - Native family name/type match the class; retain separate localization evidence.
  - Do not infer complete paralog membership, individual necessity or universal fungal
    distribution.
  - Run native schema, strict, label, history and generated-page checks.
  generator: Maintained structure YAML; just render derives pages.
limitations:
- The2015 appressorium/exocyst study is used only for gene identity, not invasive-collar
  localization or functional phenotypes.
- The2018 accepted manuscript was read; publisher-version byte identity, movies and
  raw experimental data were not examined.
- A generic family does not establish every localized paralog or its individual necessity.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- Only the review bundle is saved. Maintained scientific content, native status, history
  and generated pages remain unchanged.
```
