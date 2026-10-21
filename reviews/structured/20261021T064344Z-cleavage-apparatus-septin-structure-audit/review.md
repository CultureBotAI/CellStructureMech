# Cleavage-apparatus septin-structure identity and family review

- Review: 20261021T064344Z-cleavage-apparatus-septin-structure-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T06:42:51Z
- Finished UTC: 2026-10-21T06:43:44Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact generic identity, parent, three containment links, child boundaries and four topology edges are supported. One minor finding identifies an unnecessary localization-specific criterion for Septin family grounding.

## Scope And Provenance

Entire maintained record, every directly cited ontology term and relation, and the verified native Septin family.

Selection: Tenth remaining unreviewed path in batch5, in repository path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0032161 | data/structures/cytoskeleton/cleavage_apparatus_septin_structure.yaml | maintained | cleavage apparatus septin structure |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0032161 | Focused validator passed. |
| Focused native strict | passed | True | GO:0032161 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0032161 | 10 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | GO:0032161 | No organism, gene or expression-module claim is asserted; native ontology and protein-family identity are the relevant structured sources. |
| Claim-level scientific review | passed | True | GO:0032161 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0032161 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0032161 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0032161 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0032161 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0032161 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Generic cleavage-plane septin structure

identity: supported. Targets: GO:0032161.

The definition denotes a structural class, not a process or single protein. The localized ring/collar/split-ring children remain distinct.

### Subtype, containment and children

grounding: supported. Targets: GO:0032161.

Native GO confirms the parent, cell cortex, division-site and septin-cytoskeleton parthood, plus the five localized children.

### Septin class-level constituent

evidence: supported. Targets: GO:0032161.

The septin constituent and its class-level structural necessity are directly supported by the definition. No paralog-specific essentiality or exact stoichiometry is inferred.

### Localized-cohort criterion blocks generic family mapping

grounding: concern. Targets: GO:0032161.

The generic Septin family has a verified identifier. Requiring one family term to encode the complete cleavage-plane cohort is inconsistent with the repository component model.

### Four nonmechanistic topology edges

graph: supported. Targets: GO:0032161.

Septin assembly, cleavage-plane localization and the two represented containment edges are supported. The cell-division-site localization node and septin-cytoskeleton structure node have appropriate types.

### No universal child-specific mechanism

scope: supported. Targets: GO:0032161.

The record explicitly avoids a single assembly mechanism across bud-neck, prospore and medial-cortex structures. No species distribution or experimental phenotype is asserted.

### Distinct associated-protein question

completeness: supported. Targets: GO:0032161.

The record-scoped TODO correctly keeps associated-protein constituent status open across different children. The family-grounding portion can be resolved without pretending that associated composition is complete.

### Proposed ontology-backed class

provenance: supported. Targets: GO:0032161.

Status remains PROPOSED and future changes belong in maintained YAML with native history/render gates. No generated page was used as independent evidence.

## Findings

### F1: Cleavage-plane cohort criterion blocks verified Septin family grounding

minor / open / confirmed; issue key: cleavage-apparatus-septin-structure-family-grounding-scope.

The generic septin proteins component remains REVIEWED_LABEL_ONLY because its rationale seeks a term for the complete cleavage-plane cohort. IPR016491 denotes the verified Septin family. Repository component identity is taxon-agnostic and does not need to encode every localized state. Reconcile the mapping and rationale while retaining the independent associated-protein boundary question.

## Recommended Actions And Acceptance Checks

### A1

Under separately authorized curation, ground the septin class to verified IPR016491 and reconcile its status/notes. Resolve the family portion of the TODO while preserving the associated-protein boundary review across child structures.

- Family name/type and accession match native InterPro.
- The generic family mapping does not imply one conserved child-specific assembly mechanism or complete associated-protein census.
- Run native schema, strict, product-label, history and generated-page checks after curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| cleavage-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032161,GO:0110165,GO:0005938,GO:0032153,GO:0032156,GO:0000144,GO:0032174,GO:0032177,GO:0032169,GO:0036391; Ten definitions and explicit target child relations | supports | All ten GO terms are active. The exact definition, cellular-anatomical-structure parent, all three part_of relations and all five named localized child terms match native GO. |
| collar-IPR016491 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016491/; Native family name/type and scope | supports | IPR016491 is the Septin family. Its broad taxonomic and localization scope is appropriate to a generic septin protein class, with localized roles specified separately. |
| record | data/structures/cytoskeleton/cleavage_apparatus_septin_structure.yaml; Entire maintained YAML | context_only | Read generic structure identity, one parent, three containment links, septin component, four graph edges and two discussions. No particular organism, sequence example, measurement or common assembly pathway is asserted. |
| policy | docs/CURATION.md; Components: taxon-agnostic family and label-only rules | context_only | Components represent taxon-agnostic families/classes; REVIEWED_LABEL_ONLY requires absence of an exact term rather than absence of a localization-specific cohort term. |
| identity-search | data/structures/cytoskeleton/cleavage_apparatus_septin_structure.yaml; Ignored-inclusive identifier search across data/structures | context_only | Only this target declares GO0032161. |
| schema-result | just validate data/structures/cytoskeleton/cleavage_apparatus_septin_structure.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/cleavage_apparatus_septin_structure.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/cleavage_apparatus_septin_structure.yaml --out /private/tmp/cellstructure-batch5-20261020-aEelh1/cleavage_apparatus_septin_structure-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/cleavage_apparatus_septin_structure.yaml --out /private/tmp/cellstructure-batch5-20261020-aEelh1/cleavage_apparatus_septin_structure-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch5-20261020-aEelh1/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch5-20261020-aEelh1/cleavage_apparatus_septin_structure-strict.tsv |
| target-curies | just check-curies-strict; data/structures/cytoskeleton/cleavage_apparatus_septin_structure.yaml; exact collect() scope | supports | 10 of10 collected target identifiers returned OK at the unchanged base. Residuals: none. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- This is an ontology-backed generic class rather than an organism-specific experimental assembly model.
- Associated-protein constituent boundaries remain open and may differ across localized child structures.
- Class-level septin necessity does not establish universal essentiality of individual paralogs.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Only the review bundle is saved. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T064344Z-cleavage-apparatus-septin-structure-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Cleavage-apparatus septin-structure identity and family review
started_at: '2026-10-21T06:42:51Z'
finished_at: '2026-10-21T06:43:44Z'
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
summary: Exact generic identity, parent, three containment links, child boundaries
  and four topology edges are supported. One minor finding identifies an unnecessary
  localization-specific criterion for Septin family grounding.
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
  - path: data/structures/cytoskeleton/cleavage_apparatus_septin_structure.yaml
    sha256: 07dd82a0f5ad6f6a473e9305c85bf0de6ca336f573878668664e2ee44dbc90e1
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
- target_id: GO:0032161
  path: data/structures/cytoskeleton/cleavage_apparatus_septin_structure.yaml
  label: cleavage apparatus septin structure
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/cleavage_apparatus_septin_structure.yaml
    role: maintained scientific record
scope:
  description: Entire maintained record, every directly cited ontology term and relation,
    and the verified native Septin family.
  selection: Tenth remaining unreviewed path in batch5, in repository path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0032161
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0032161
  command: just validate data/structures/cytoskeleton/cleavage_apparatus_septin_structure.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0032161
  command: just validate-strict data/structures/cytoskeleton/cleavage_apparatus_septin_structure.yaml
    --out /private/tmp/cellstructure-batch5-20261020-aEelh1/cleavage_apparatus_septin_structure-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0032161
  summary: 10 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0032161
  summary: No organism, gene or expression-module claim is asserted; native ontology
    and protein-family identity are the relevant structured sources.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0032161
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - cleavage-go
  - collar-IPR016491
  - record
  - policy
  - identity-search
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0032161
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch5 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0032161
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch5 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0032161
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch5 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0032161
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch5 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0032161
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch5 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: cleavage-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032161,GO:0110165,GO:0005938,GO:0032153,GO:0032156,GO:0000144,GO:0032174,GO:0032177,GO:0032169,GO:0036391
  locator: Ten definitions and explicit target child relations
  accessed_at: '2026-10-21T06:43:11.876099Z'
  support: supports
  summary: All ten GO terms are active. The exact definition, cellular-anatomical-structure
    parent, all three part_of relations and all five named localized child terms match
    native GO.
  snapshot_sha256: 6affdfe5624192f3225949ff2710f56c494c3a53001908d136bf4bd85030b82d
- evidence_id: collar-IPR016491
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016491/
  locator: Native family name/type and scope
  accessed_at: '2026-10-20T07:32:51.027110Z'
  support: supports
  summary: IPR016491 is the Septin family. Its broad taxonomic and localization scope
    is appropriate to a generic septin protein class, with localized roles specified
    separately.
  snapshot_sha256: 5797c626d192b641ed5b4b2231e729f9f179bfd6bb18f911689fa08253688c4a
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/cleavage_apparatus_septin_structure.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T06:43:44Z'
  support: context_only
  summary: Read generic structure identity, one parent, three containment links, septin
    component, four graph edges and two discussions. No particular organism, sequence
    example, measurement or common assembly pathway is asserted.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: 'Components: taxon-agnostic family and label-only rules'
  accessed_at: '2026-10-21T06:43:44Z'
  support: context_only
  summary: Components represent taxon-agnostic families/classes; REVIEWED_LABEL_ONLY
    requires absence of an exact term rather than absence of a localization-specific
    cohort term.
- evidence_id: identity-search
  kind: record_content
  reference: data/structures/cytoskeleton/cleavage_apparatus_septin_structure.yaml
  locator: Ignored-inclusive identifier search across data/structures
  accessed_at: '2026-10-21T06:43:44Z'
  support: context_only
  summary: Only this target declares GO0032161.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/cleavage_apparatus_septin_structure.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T06:42:55Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/cleavage_apparatus_septin_structure.yaml'
  snapshot_sha256: 716e8ce9512cf76add068cb320dc4a127eacaee3dead600aad03a5b78d296b33
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/cleavage_apparatus_septin_structure.yaml
    --out /private/tmp/cellstructure-batch5-20261020-aEelh1/cleavage_apparatus_septin_structure-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T06:42:59Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/cleavage_apparatus_septin_structure.yaml\
    \ --out /private/tmp/cellstructure-batch5-20261020-aEelh1/cleavage_apparatus_septin_structure-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch5-20261020-aEelh1/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch5-20261020-aEelh1/cleavage_apparatus_septin_structure-strict.tsv"
  snapshot_sha256: 30e54a91a875802a973a280722064ad5ac20a2dc22dd50417d36f6c6d45e71c3
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/cleavage_apparatus_septin_structure.yaml;
    exact collect() scope
  accessed_at: '2026-10-21T06:43:44Z'
  support: supports
  summary: '10 of10 collected target identifiers returned OK at the unchanged base.
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
  topic: Generic cleavage-plane septin structure
  outcome: supported
  target_ids:
  - GO:0032161
  summary: The definition denotes a structural class, not a process or single protein.
    The localized ring/collar/split-ring children remain distinct.
  evidence_ids:
  - cleavage-go
  - record
- assessment_id: relations
  area: grounding
  topic: Subtype, containment and children
  outcome: supported
  target_ids:
  - GO:0032161
  summary: Native GO confirms the parent, cell cortex, division-site and septin-cytoskeleton
    parthood, plus the five localized children.
  evidence_ids:
  - cleavage-go
- assessment_id: composition
  area: evidence
  topic: Septin class-level constituent
  outcome: supported
  target_ids:
  - GO:0032161
  summary: The septin constituent and its class-level structural necessity are directly
    supported by the definition. No paralog-specific essentiality or exact stoichiometry
    is inferred.
  evidence_ids:
  - cleavage-go
  - record
- assessment_id: family
  area: grounding
  topic: Localized-cohort criterion blocks generic family mapping
  outcome: concern
  target_ids:
  - GO:0032161
  summary: The generic Septin family has a verified identifier. Requiring one family
    term to encode the complete cleavage-plane cohort is inconsistent with the repository
    component model.
  evidence_ids:
  - collar-IPR016491
  - policy
  - record
- assessment_id: graph
  area: graph
  topic: Four nonmechanistic topology edges
  outcome: supported
  target_ids:
  - GO:0032161
  summary: Septin assembly, cleavage-plane localization and the two represented containment
    edges are supported. The cell-division-site localization node and septin-cytoskeleton
    structure node have appropriate types.
  evidence_ids:
  - cleavage-go
  - record
- assessment_id: scope
  area: scope
  topic: No universal child-specific mechanism
  outcome: supported
  target_ids:
  - GO:0032161
  summary: The record explicitly avoids a single assembly mechanism across bud-neck,
    prospore and medial-cortex structures. No species distribution or experimental
    phenotype is asserted.
  evidence_ids:
  - cleavage-go
  - record
- assessment_id: accessories
  area: completeness
  topic: Distinct associated-protein question
  outcome: supported
  target_ids:
  - GO:0032161
  summary: The record-scoped TODO correctly keeps associated-protein constituent status
    open across different children. The family-grounding portion can be resolved without
    pretending that associated composition is complete.
  evidence_ids:
  - cleavage-go
  - collar-IPR016491
  - record
- assessment_id: status
  area: provenance
  topic: Proposed ontology-backed class
  outcome: supported
  target_ids:
  - GO:0032161
  summary: Status remains PROPOSED and future changes belong in maintained YAML with
    native history/render gates. No generated page was used as independent evidence.
  evidence_ids:
  - record
  - cleavage-go
findings:
- finding_id: F1
  issue_key: cleavage-apparatus-septin-structure-family-grounding-scope
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Cleavage-plane cohort criterion blocks verified Septin family grounding
  description: The generic septin proteins component remains REVIEWED_LABEL_ONLY because
    its rationale seeks a term for the complete cleavage-plane cohort. IPR016491 denotes
    the verified Septin family. Repository component identity is taxon-agnostic and
    does not need to encode every localized state. Reconcile the mapping and rationale
    while retaining the independent associated-protein boundary question.
  target_ids:
  - GO:0032161
  field_paths:
  - components[component_id=septin_proteins].grounding_status
  - components[component_id=septin_proteins].grounding_notes
  - discussions[discussion_id=resolve_cleavage_apparatus_septin_associated_proteins]
  evidence_ids:
  - collar-IPR016491
  - policy
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/cleavage_apparatus_septin_structure.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components
  native_severity: minor
  normalization_reason: This is a bounded absent mapping and rationale defect. Structure
    identity, hierarchy and topology remain supported.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0032161
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/cleavage_apparatus_septin_structure.yaml
    role: maintained scientific record
  description: Under separately authorized curation, ground the septin class to verified
    IPR016491 and reconcile its status/notes. Resolve the family portion of the TODO
    while preserving the associated-protein boundary review across child structures.
  acceptance_checks:
  - Family name/type and accession match native InterPro.
  - The generic family mapping does not imply one conserved child-specific assembly
    mechanism or complete associated-protein census.
  - Run native schema, strict, product-label, history and generated-page checks after
    curation.
  generator: Maintained YAML; just render derives pages.
limitations:
- This is an ontology-backed generic class rather than an organism-specific experimental
  assembly model.
- Associated-protein constituent boundaries remain open and may differ across localized
  child structures.
- Class-level septin necessity does not establish universal essentiality of individual
  paralogs.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- Only the review bundle is saved. Maintained scientific content, native status, history
  and generated pages remain unchanged.
```
