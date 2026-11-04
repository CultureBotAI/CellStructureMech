# Prospore septin ring identity, source-boundary and family review

- Review: 20261021T080757Z-prospore-septin-ring-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T07:53:50Z
- Finished UTC: 2026-10-21T08:07:57Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact prospore-ring ontology identity is retained. Two minor issues remain: generic Septin-family grounding and unqualified cytokinesis-site wording relative to the GO definition source.

## Scope And Provenance

Entire single target, all native GO identities, generic family, the definition-source review and relevant primary sporulation text.

Selection: Fourth selected unreviewed path in batch ten, in repository path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0032169 | data/structures/cytoskeleton/prospore_septin_ring.yaml | maintained | prospore septin ring |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0032169 | Focused validator passed. |
| Focused native strict | passed | True | GO:0032169 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0032169 | 6 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | GO:0032169 | No expression-module or transcriptional-regulator mechanism is asserted; localized structural membership is not inferred from expression modules. |
| Claim-level scientific review | passed | True | GO:0032169 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0032169 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0032169 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0032169 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0032169 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0032169 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Exact GO ring class and cytokinetic siblings

identity: supported. Targets: GO:0032169.

The target identifier and direct septin-ring parent are exact. The record correctly distinguishes the bud-neck split rings GO0032177, germ-tube/hyphal rings and pseudohyphal ring. The source conflict does not justify substituting a sibling identifier or merging this record with the filament array.

### GO-derived localization needs source qualification

graph: concern. Targets: GO:0032169.

The component assembly edge is supported. The localization edge and definition repeat GO cytokinesis-site wording, but the source cited by that GO term describes a different sporulation geometry and changing localization. A reader should not be left to infer an ordinary bud-neck septation plane or a persistent contractile ring.

### Developmental state and collective material

scope: supported. Targets: GO:0032169.

The target asserts no exact species or accession examples. The inspected S. cerevisiae studies support state-specific rings and arrays, not all-fungal kinetics, fixed composition or necessity of every paralog. ESSENTIAL concerns collective septin material, not universal viability or successful sporulation.

### Generic Septin family versus localized cohort

grounding: concern. Targets: GO:0032169.

The component label denotes septin proteins, but its grounding rationale waits for a family accession delimiting the full localized cohort. Verified IPR016491 matches the generic family; exact cohort and accessory membership remain independent unresolved questions.

### Preserved authority-source disagreement

provenance: supported. Targets: GO:0032169.

The exact native GO mapping is preserved alongside the contrary qualification in its cited review and relevant primary text. Citation metadata is verified; Fares1996 is used only as an abstract, not as unread experimental detail.

## Findings

### F1: Localized-cohort criterion leaves the generic Septin family ungrounded

minor / open / confirmed; issue key: prospore-septin-ring-generic-family-withheld.

The generic septin-proteins component remains REVIEWED_LABEL_ONLY because no accession was assigned for the complete localized cohort. IPR016491 already identifies the named Septin family. Reconcile grounding, status and rationale without inferring an exhaustive localized paralog set or associated-protein inventory.

### F2: GO-derived cytokinesis-site wording leaves its source conflict unexplained

minor / open / confirmed; issue key: prospore-septin-ring-cytokinesis-source-qualification.

The record faithfully repeats GO0032169, but that term cites Douglas2005 alone. Section14 says sporulation has no equivalent bud neck or septation site and describes early rings followed by sheets/bars and spore-peripheral staining. The record repeats a tight division-plane cytokinesis site without preserving this qualification. Document the ontology-versus-literature scope difference and constrain the topology wording; retain the exact GO identity and distinguish the separate array.

## Recommended Actions And Acceptance Checks

### A1

Under separately authorized curation, ground the generic Septin component to verified IPR016491 and reconcile its status and localized-cohort rationale.

- Retain separate evidence for localized membership and associated proteins.
- Do not add a universal paralog set, stoichiometry or individual essentiality.
- Use the guarded writer and required curation/history, schema, strict, label and generated-page checks.

### A2

Under separately authorized curation, add an explicit source-boundary discussion distinguishing GO wording from the observed sporulation sequence and constrain the descriptive localization prose accordingly.

- Preserve exact GO0032169 identity and distinguish array GO0032165 and bud-neck split rings GO0032177.
- Do not infer a contractile ring, ordinary septation plane, fixed kinetics or identity with the Don1 leading-edge ring.
- Keep GO wording honestly attributed and attach primary/review support at the narrowest applicable claim; run native curation gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| prospore-ring-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032169,GO:0005940,GO:0032172,GO:0032168,GO:0032170,GO:0032177,GO:0032165; All returned definitions, isObsolete flags, exact identifiers and parent-term child relations | supports | Native GO verifies the exact active target definition and each cited parent/sibling identity. Parent-term child relations distinguish is-a specialization from structural parthood. |
| prospore-ring-agent-family | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016491/; Native accession, name, type=family, description and hierarchy; original retrieval timestamp retained | supports | IPR016491 is the Septin family. It supports the generic septin-proteins class without specifying every member of a localized assembly. |
| prospore-ring-agent-douglas-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1128/EC.4.9.1503-1512.2005&amp;format=json&amp;resultType=core; Exact DOI/PMID result, authors, title, year and review publication type | supports | Native metadata verifies Douglas, Alvarez, McCreary and Konopka2005, Septin Function in Yeast Model Systems and Pathogenic Fungi, DOI10.1128/EC.4.9.1503-1512.2005, PMID16151244. |
| record | data/structures/cytoskeleton/prospore_septin_ring.yaml; Entire target, history, component and any sequence examples, all graph edges and discussions | context_only | The complete PROPOSED target was read. The graph is explicitly NONMECHANISTIC. No scientific status or content is changed. |
| policy | docs/CURATION.md; Components: source-neutral family grounding, membership and structure-assembly essentiality | context_only | Generic protein-family identity is separate from localized assembly membership. ESSENTIAL denotes whether the structure forms, not universal cellular viability or each individual paralog requirement. |
| prospore-ring-agent-douglas-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC1214204/; Native PMC1214204 sec14, especially first and second paragraphs; literature-review tier and original receipt retained | partial | The sole PMID behind GO0032169 describes early sporulation rings that broaden into membrane-associated sheets/bars and later surround nascent spores. It explicitly distinguishes sporulation from bud-neck or septation-site division, creating a qualification gap in the GO-derived cytokinesis-site wording. |
| prospore-ring-agent-tachikawa2001 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2150859/?pdf=render; Native PMC2150859 Introduction, Results sec7-sec10 and Discussion sec16; relevant text figure legends | partial | The primary study describes early rings around SPBs, later parallel sheet/bar localization and eventual spore-peripheral localization. Its Don1 leading-edge ring is explicitly distinct from septin bars. These observations do not establish a persistent tight septin ring at a budding-like division plane. |
| prospore-ring-agent-primary-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:8636217%20OR%20EXT_ID:11724821&amp;format=json&amp;resultType=core; Both exact citation records and abstracts | supports | Native metadata verifies Fares/Goetsch/Pringle1996 DOI10.1083/jcb.132.3.399 / PMID8636217 and Tachikawa et al.2001 DOI10.1083/jcb.200107008 / PMID11724821. |
| prospore-ring-agent-fares1996 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2120726/?pdf=render; PMC2120726 identity and abstract only; full body is offered as a PDF that was not recovered | context_only | The primary abstract describes septins near leading edges of expanding membrane sacs and partially redundant sporulation roles. The retrieved article landing HTML does not include Results body text. |
| schema-result | just validate data/structures/cytoskeleton/prospore_septin_ring.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/prospore_septin_ring.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/prospore_septin_ring.yaml --out /private/tmp/cellstructure-batch10-20261021-giynduuy/prospore_septin_ring-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/prospore_septin_ring.yaml --out /private/tmp/cellstructure-batch10-20261021-giynduuy/prospore_septin_ring-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch10-20261021-giynduuy/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch10-20261021-giynduuy/prospore_septin_ring-strict.tsv |
| target-curies | just check-curies-strict; data/structures/cytoskeleton/prospore_septin_ring.yaml; exact collect() scope; SHA-256 identifies the entire original resolver TSV at /private/tmp/cellstructure-record-reviews-UhRFh7/repo/reports/curie_check.tsv, not the derived resolver-slice.json | supports | 6 of 6 collected target identifiers returned OK at the unchanged base. Residuals: none. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- The source qualification does not prove that no septin ring ever occurs during sporulation, and it does not justify collapsing ring and array identities.
- Fares1996 native HTML provides its abstract but not Results text; attempted PDF routes were unavailable. The body-level corroboration is Tachikawa2001.
- Microscopy pixels, three-dimensional movies and raw data were not reanalyzed; primary prose and relevant legends were inspected.
- A complete localized cohort, accessory inventory, universal fungal distribution and individual-paralog essentiality remain unresolved.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Only a review bundle is saved. Maintained scientific content, native status, history and generated pages remain unchanged.
- Root read the complete target and review and verified every native input/source hash; selected primary and review sections were independently inspected. The source-tier and access limitations remain explicit.
- Only this target receives scientific review coverage. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T080757Z-prospore-septin-ring-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Prospore septin ring identity, source-boundary and family review
started_at: '2026-10-21T07:53:50Z'
finished_at: '2026-10-21T08:07:57Z'
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
summary: 'Exact prospore-ring ontology identity is retained. Two minor issues remain:
  generic Septin-family grounding and unqualified cytokinesis-site wording relative
  to the GO definition source.'
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
  - path: data/structures/cytoskeleton/prospore_septin_ring.yaml
    sha256: 56b764eb06dde6d49e5ad5135ab577218f765b63791ffe0483147d4186498da5
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
- target_id: GO:0032169
  path: data/structures/cytoskeleton/prospore_septin_ring.yaml
  label: prospore septin ring
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/prospore_septin_ring.yaml
    role: maintained scientific record
scope:
  description: Entire single target, all native GO identities, generic family, the
    definition-source review and relevant primary sporulation text.
  selection: Fourth selected unreviewed path in batch ten, in repository path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0032169
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0032169
  command: just validate data/structures/cytoskeleton/prospore_septin_ring.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0032169
  command: just validate-strict data/structures/cytoskeleton/prospore_septin_ring.yaml
    --out /private/tmp/cellstructure-batch10-20261021-giynduuy/prospore_septin_ring-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0032169
  summary: 6 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0032169
  summary: No expression-module or transcriptional-regulator mechanism is asserted;
    localized structural membership is not inferred from expression modules.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0032169
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - prospore-ring-agent-go
  - prospore-ring-agent-family
  - prospore-ring-agent-douglas-metadata
  - record
  - policy
  - prospore-ring-agent-douglas-pmc
  - prospore-ring-agent-tachikawa2001
  - prospore-ring-agent-primary-metadata
  - prospore-ring-agent-fares1996
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0032169
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
  - GO:0032169
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
  - GO:0032169
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
  - GO:0032169
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
  - GO:0032169
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
- evidence_id: prospore-ring-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032169,GO:0005940,GO:0032172,GO:0032168,GO:0032170,GO:0032177,GO:0032165
  locator: All returned definitions, isObsolete flags, exact identifiers and parent-term
    child relations
  accessed_at: '2026-10-21T07:55:02.179429Z'
  support: supports
  summary: Native GO verifies the exact active target definition and each cited parent/sibling
    identity. Parent-term child relations distinguish is-a specialization from structural
    parthood.
  snapshot_sha256: 65a837d7a496399f53acd6d0e5733d4922cbc16f5196f385ca211d04bd7a07ed
- evidence_id: prospore-ring-agent-family
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016491/
  locator: Native accession, name, type=family, description and hierarchy; original
    retrieval timestamp retained
  accessed_at: '2026-10-21T06:58:21.193684Z'
  support: supports
  summary: IPR016491 is the Septin family. It supports the generic septin-proteins
    class without specifying every member of a localized assembly.
  snapshot_sha256: 5797c626d192b641ed5b4b2231e729f9f179bfd6bb18f911689fa08253688c4a
- evidence_id: prospore-ring-agent-douglas-metadata
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
  reference: data/structures/cytoskeleton/prospore_septin_ring.yaml
  locator: Entire target, history, component and any sequence examples, all graph
    edges and discussions
  accessed_at: '2026-10-21T08:00:50Z'
  support: context_only
  summary: The complete PROPOSED target was read. The graph is explicitly NONMECHANISTIC.
    No scientific status or content is changed.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: 'Components: source-neutral family grounding, membership and structure-assembly
    essentiality'
  accessed_at: '2026-10-21T08:00:50Z'
  support: context_only
  summary: Generic protein-family identity is separate from localized assembly membership.
    ESSENTIAL denotes whether the structure forms, not universal cellular viability
    or each individual paralog requirement.
- evidence_id: prospore-ring-agent-douglas-pmc
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1214204/
  locator: Native PMC1214204 sec14, especially first and second paragraphs; literature-review
    tier and original receipt retained
  accessed_at: '2026-10-21T07:11:03.050463Z'
  support: partial
  summary: The sole PMID behind GO0032169 describes early sporulation rings that broaden
    into membrane-associated sheets/bars and later surround nascent spores. It explicitly
    distinguishes sporulation from bud-neck or septation-site division, creating a
    qualification gap in the GO-derived cytokinesis-site wording.
  snapshot_sha256: 31a2dd0109697492854f84701ef3f1d1be31f62312b613ab8432223332b69dd3
- evidence_id: prospore-ring-agent-tachikawa2001
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2150859/?pdf=render
  locator: Native PMC2150859 Introduction, Results sec7-sec10 and Discussion sec16;
    relevant text figure legends
  accessed_at: '2026-10-21T07:55:41.272676Z'
  support: partial
  summary: The primary study describes early rings around SPBs, later parallel sheet/bar
    localization and eventual spore-peripheral localization. Its Don1 leading-edge
    ring is explicitly distinct from septin bars. These observations do not establish
    a persistent tight septin ring at a budding-like division plane.
  snapshot_sha256: 27192ba28363973204c857601dde3518874638519f0d30c6d5b5b7f20719bba2
- evidence_id: prospore-ring-agent-primary-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:8636217%20OR%20EXT_ID:11724821&format=json&resultType=core
  locator: Both exact citation records and abstracts
  accessed_at: '2026-10-21T07:55:41.273105Z'
  support: supports
  summary: Native metadata verifies Fares/Goetsch/Pringle1996 DOI10.1083/jcb.132.3.399
    / PMID8636217 and Tachikawa et al.2001 DOI10.1083/jcb.200107008 / PMID11724821.
  snapshot_sha256: 9258e41297864eda4a4bdbc339d2cfe5af94ab335a4f6f804ea2a3d3d7bbe73c
- evidence_id: prospore-ring-agent-fares1996
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2120726/?pdf=render
  locator: PMC2120726 identity and abstract only; full body is offered as a PDF that
    was not recovered
  accessed_at: '2026-10-21T07:55:41.272287Z'
  support: context_only
  summary: The primary abstract describes septins near leading edges of expanding
    membrane sacs and partially redundant sporulation roles. The retrieved article
    landing HTML does not include Results body text.
  snapshot_sha256: a4c9121a768170b8f8b79844cd58c0c94d8cb30553b40438519415c89b3d48be
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/prospore_septin_ring.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T07:53:51Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/prospore_septin_ring.yaml'
  snapshot_sha256: 44b012d922ebd4c00001d692f201b662b0f8da35f694fc1224dfd932638543fe
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/prospore_septin_ring.yaml
    --out /private/tmp/cellstructure-batch10-20261021-giynduuy/prospore_septin_ring-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T07:53:53Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/prospore_septin_ring.yaml\
    \ --out /private/tmp/cellstructure-batch10-20261021-giynduuy/prospore_septin_ring-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch10-20261021-giynduuy/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch10-20261021-giynduuy/prospore_septin_ring-strict.tsv"
  snapshot_sha256: 95e98c430e65e4865a82d82538c13e6c96ab6eb88864cea1499ac3aff91ca588
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/prospore_septin_ring.yaml; exact collect()
    scope; SHA-256 identifies the entire original resolver TSV at /private/tmp/cellstructure-record-reviews-UhRFh7/repo/reports/curie_check.tsv,
    not the derived resolver-slice.json
  accessed_at: '2026-10-21T08:00:50Z'
  support: supports
  summary: '6 of 6 collected target identifiers returned OK at the unchanged base.
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
  topic: Exact GO ring class and cytokinetic siblings
  outcome: supported
  target_ids:
  - GO:0032169
  summary: The target identifier and direct septin-ring parent are exact. The record
    correctly distinguishes the bud-neck split rings GO0032177, germ-tube/hyphal rings
    and pseudohyphal ring. The source conflict does not justify substituting a sibling
    identifier or merging this record with the filament array.
  evidence_ids:
  - prospore-ring-agent-go
  - prospore-ring-agent-douglas-pmc
  - prospore-ring-agent-tachikawa2001
  - record
- assessment_id: topology
  area: graph
  topic: GO-derived localization needs source qualification
  outcome: concern
  target_ids:
  - GO:0032169
  summary: The component assembly edge is supported. The localization edge and definition
    repeat GO cytokinesis-site wording, but the source cited by that GO term describes
    a different sporulation geometry and changing localization. A reader should not
    be left to infer an ordinary bud-neck septation plane or a persistent contractile
    ring.
  evidence_ids:
  - prospore-ring-agent-go
  - prospore-ring-agent-douglas-pmc
  - prospore-ring-agent-tachikawa2001
  - record
- assessment_id: scope
  area: scope
  topic: Developmental state and collective material
  outcome: supported
  target_ids:
  - GO:0032169
  summary: The target asserts no exact species or accession examples. The inspected
    S. cerevisiae studies support state-specific rings and arrays, not all-fungal
    kinetics, fixed composition or necessity of every paralog. ESSENTIAL concerns
    collective septin material, not universal viability or successful sporulation.
  evidence_ids:
  - prospore-ring-agent-douglas-pmc
  - prospore-ring-agent-tachikawa2001
  - record
  - policy
- assessment_id: family
  area: grounding
  topic: Generic Septin family versus localized cohort
  outcome: concern
  target_ids:
  - GO:0032169
  summary: The component label denotes septin proteins, but its grounding rationale
    waits for a family accession delimiting the full localized cohort. Verified IPR016491
    matches the generic family; exact cohort and accessory membership remain independent
    unresolved questions.
  evidence_ids:
  - prospore-ring-agent-family
  - record
  - policy
- assessment_id: provenance
  area: provenance
  topic: Preserved authority-source disagreement
  outcome: supported
  target_ids:
  - GO:0032169
  summary: The exact native GO mapping is preserved alongside the contrary qualification
    in its cited review and relevant primary text. Citation metadata is verified;
    Fares1996 is used only as an abstract, not as unread experimental detail.
  evidence_ids:
  - prospore-ring-agent-go
  - prospore-ring-agent-douglas-metadata
  - prospore-ring-agent-douglas-pmc
  - prospore-ring-agent-primary-metadata
  - prospore-ring-agent-tachikawa2001
  - prospore-ring-agent-fares1996
findings:
- finding_id: F1
  issue_key: prospore-septin-ring-generic-family-withheld
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
  - GO:0032169
  field_paths:
  - components[component_id=septin_proteins].grounding_status
  - components[component_id=septin_proteins].grounding_notes
  - discussions
  evidence_ids:
  - prospore-ring-agent-family
  - record
  - policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/prospore_septin_ring.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components
  native_severity: minor
  normalization_reason: A bounded, resolvable generic-family mapping gap; no change
    to exact structure identity is implied.
- finding_id: F2
  issue_key: prospore-septin-ring-cytokinesis-source-qualification
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: GO-derived cytokinesis-site wording leaves its source conflict unexplained
  description: The record faithfully repeats GO0032169, but that term cites Douglas2005
    alone. Section14 says sporulation has no equivalent bud neck or septation site
    and describes early rings followed by sheets/bars and spore-peripheral staining.
    The record repeats a tight division-plane cytokinesis site without preserving
    this qualification. Document the ontology-versus-literature scope difference and
    constrain the topology wording; retain the exact GO identity and distinguish the
    separate array.
  target_ids:
  - GO:0032169
  field_paths:
  - definition
  - components[component_id=septin_proteins].role
  - causal_graphs[graph_id=prospore_septin_ring_topology]
  - discussions[discussion_id=prospore_septin_ring_boundary]
  evidence_ids:
  - prospore-ring-agent-go
  - prospore-ring-agent-douglas-pmc
  - prospore-ring-agent-tachikawa2001
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/prospore_septin_ring.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:Evidence Rules
  native_severity: minor
  normalization_reason: The ontology mapping is exact and the ring-shaped state exists.
    The defect is an unqualified imported localization interpretation, not demonstrated
    wrong structure identity.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0032169
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/prospore_septin_ring.yaml
    role: maintained scientific record
  description: Under separately authorized curation, ground the generic Septin component
    to verified IPR016491 and reconcile its status and localized-cohort rationale.
  acceptance_checks:
  - Retain separate evidence for localized membership and associated proteins.
  - Do not add a universal paralog set, stoichiometry or individual essentiality.
  - Use the guarded writer and required curation/history, schema, strict, label and
    generated-page checks.
  generator: Maintained structure YAML; pages derive through just render.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0032169
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/prospore_septin_ring.yaml
    role: maintained scientific record
  description: Under separately authorized curation, add an explicit source-boundary
    discussion distinguishing GO wording from the observed sporulation sequence and
    constrain the descriptive localization prose accordingly.
  acceptance_checks:
  - Preserve exact GO0032169 identity and distinguish array GO0032165 and bud-neck
    split rings GO0032177.
  - Do not infer a contractile ring, ordinary septation plane, fixed kinetics or identity
    with the Don1 leading-edge ring.
  - Keep GO wording honestly attributed and attach primary/review support at the narrowest
    applicable claim; run native curation gates.
  generator: Maintained structure YAML; pages derive through just render.
limitations:
- The source qualification does not prove that no septin ring ever occurs during sporulation,
  and it does not justify collapsing ring and array identities.
- Fares1996 native HTML provides its abstract but not Results text; attempted PDF
  routes were unavailable. The body-level corroboration is Tachikawa2001.
- Microscopy pixels, three-dimensional movies and raw data were not reanalyzed; primary
  prose and relevant legends were inspected.
- A complete localized cohort, accessory inventory, universal fungal distribution
  and individual-paralog essentiality remain unresolved.
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
