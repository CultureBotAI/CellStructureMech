# Split septin rings: identity, topology and component grounding

- Review: 20261021T084039Z-split-septin-rings-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T08:24:46Z
- Finished UTC: 2026-10-21T08:40:39Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Split-pair identity, ontology hierarchy, tentative compartment function and descriptive graph are supported. One minor curation issue is the withheld exact Septin family grounding for the existing generic component.

## Scope And Provenance

Entire single maintained target, every stable identifier, native family and GO relations; claim-bearing ontology-provenance review context; graph and uncertainty limits.

Selection: First selected path in batch twelve, fixed maintained-path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0032176 | data/structures/cytoskeleton/split_septin_rings.yaml | maintained | split septin rings |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0032176 | Focused validator passed. |
| Focused native strict | passed | True | GO:0032176 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0032176 | 7 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | GO:0032176 | No transcriptional regulatory or expression-module claim is asserted. |
| Claim-level scientific review | passed | True | GO:0032176 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0032176 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0032176 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0032176 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0032176 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0032176 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Generic split pair and precursor boundaries

identity: supported. Targets: GO:0032176.

GO0032176 identifies the pair of septin rings, not one ring, a collar, a single septin protein or only the bud-neck subtype. FILAMENT describes this filamentous assembly at the record granularity. No exact synonym collision was established.

### Native is-a and parthood links

scope: supported. Targets: GO:0032176.

Native child relations confirm the asserted septin-cytoskeleton parent and cytoskeleton parthood. The bud-neck split pair is a narrower child. No species or prevalence row is asserted; the definition preserves known budding-yeast occurrence and uncertainty elsewhere.

### Generic family versus unresolved localized membership

grounding: concern. Targets: GO:0032176.

The generic septin-proteins component can be grounded to IPR016491. Deferring it until a family exactly delimits every split-ring-forming septin confuses family identity with developmental membership. ESSENTIAL is interpreted collectively as septin material needed to constitute a septin pair; it does not assert all individual genes are indispensable.

### Tentative cytokinetic compartment boundary

evidence: supported. Targets: GO:0032176.

The function accurately retains thought-to-trap wording. The reviewed examples support confinement of selected membrane-associated factors; they do not make all cytokinesis proteins septin constituents or establish direct interaction, autonomous constriction, or a universal impermeable barrier.

### Nonmechanistic split topology

graph: supported. Targets: GO:0032176.

The assemble-into, splits-into and flank edges faithfully summarize class composition and morphology. The explicit NONMECHANISTIC scope avoids a claim of de novo molecular polymerization, exact recruitment order or a resolved splitting motor. The disjunctive ring-or-collar node is intentionally broader than either single GO identity.

### Optional examples and molecular inventories

completeness: supported. Targets: GO:0032176.

No exact protein examples, image, dimensions, stoichiometry or native splitting mechanism are asserted. Empty optional slots do not create a defect. The open grounding discussion remains useful, but its current family criterion needs the bounded correction below.

### Ontology authority and source tiers

provenance: supported. Targets: GO:0032176.

All asserted GO identities are verified natively. Both supporting paper bodies are reviews, explicitly treated as secondary context; relevant sections were read, not substituted for independent primary experiments. Reused receipts retain original access timestamps and hashes.

## Findings

### F1: The generic septin component has an exact family grounding

minor / open / confirmed; issue key: split-septin-rings-generic-family-withheld.

The septin_proteins row is REVIEWED_LABEL_ONLY because no family accession was assigned for the complete split-ring-forming cohort. Native IPR016491 directly represents the generic Septin family already named by the row. Assigning this class does not require determining which paralogues remain in a particular split pair or asserting that every family member forms this structure. Ground the generic row to InterPro:IPR016491 and retain exact membership as an open question.

## Recommended Actions And Acceptance Checks

### A1

In authorized curation, ground the septin-proteins row to InterPro:IPR016491 and align grounding status and notes. Preserve historical discussion rationale and record current progress in notes; retain unresolved localized cohort and individual essentiality limits.

- Compare component scope against native IPR016491 family description.
- Do not add unverified paralogue examples or universal assembly necessity.
- Run native schema, strict, label, history and generated-page checks after maintained-record changes.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/split_septin_rings.yaml; Entire maintained YAML, including component, function, graph, discussions and history | context_only | The complete target was read after native inspect. No scientific content or PROPOSED status is changed. |
| policy | docs/CURATION.md; Components, evidence and grounding rules | context_only | A generic protein-family component may use the exact family class without resolving every localized paralogue. Optional inventories are not mandatory. |
| split-rings-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032176,GO:0032156,GO:0005856,GO:0032177,GO:0032153,GO:0005940,GO:0032173; Seven exact result IDs; names, definitions, isObsolete and returned child relations | supports | Active GO0032176 exactly matches the definition of the split pair and its tentative protein-trapping function. Returned parent GO0032156 has a direct is_a child link to GO0032176; GO0005856 has its part_of child link. GO0032177 narrows to cellular bud neck, while GO0005940 and GO0032173 identify the unsplit ring and collar. GO0032153 identifies the cell division site. |
| split-rings-agent-family | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016491/; metadata accession, name, type and description; family class distinguished from domain and localized cohort | supports | IPR016491 is the Septin family and explicitly represents filament-forming septin GTPases. It matches the generic septin-proteins row; this does not identify the exact remaining cohort, paralogue-specific necessity or native stoichiometry. Older assembly statements in the descriptive text are not adopted. |
| split-rings-agent-douglas-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC1214204/; PMC1214204 HTML; cell-cycle introduction, sec11 Cytokinesis barrier; sec3 inspected for assembly-model limits | supports | Douglas et al.2005 is a literature review, not a new perturbation experiment. Cell-cycle introductory paragraphs and sec11 describe collar splitting and confinement of selected cytokinesis/septation factors; reviewed cdc12-6 experiments distinguish loss of Spa2/Sec3/Chs2 from retention of the actomyosin ring. No direct binding or universal barrier efficacy is inferred. |
| split-rings-agent-versele-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC1761124/?pdf=render; PMC1761124 HTML despite pdf=render query; S2 Septin functions and embedded Figure3 legend | supports | Versele/Thorner2005 is a literature review. S2 and Figure3 legend distinguish collar-to-pair conversion and tentative cytokinetic confinement from broader septin functions. Fission-yeast comparisons are context, not new taxon distribution rows or universal essentiality. |
| split-rings-agent-douglas-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1128/EC.4.9.1503-1512.2005&amp;format=json&amp;resultType=core; resultList.result exact DOI/title/authors/year/PMID | supports | Native DOI identity confirms Douglas et al.2005, PMID16151244, DOI10.1128/EC.4.9.1503-1512.2005; this is the review named in native GO definition provenance. |
| schema-result | just validate data/structures/cytoskeleton/split_septin_rings.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/split_septin_rings.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/split_septin_rings.yaml --out /private/tmp/cellstructure-batch12-20261021-ipvr425j/split_septin_rings-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/split_septin_rings.yaml --out /private/tmp/cellstructure-batch12-20261021-ipvr425j/split_septin_rings-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch12-20261021-ipvr425j/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch12-20261021-ipvr425j/split_septin_rings-strict.tsv |
| target-curies | just check-curies-strict; data/structures/cytoskeleton/split_septin_rings.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 7 of7 collected target identifiers returned OK at the unchanged base. Residuals: none. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- No new primary perturbation experiment or underlying raw microscopy was reanalyzed; literature context is explicitly review-tier.
- Exact paralogue membership, native stoichiometry, molecular splitting mechanism and universal barrier efficacy remain unresolved and are not asserted.
- No new exhaustive repository or ontology absence claim is made; historical rationale is preserved.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Native inspect/schema/strict all passed before assessment. Parent audit, finalization and persistence remain pending.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T084039Z-split-septin-rings-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'Split septin rings: identity, topology and component grounding'
started_at: '2026-10-21T08:24:46Z'
finished_at: '2026-10-21T08:40:39Z'
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
summary: Split-pair identity, ontology hierarchy, tentative compartment function and
  descriptive graph are supported. One minor curation issue is the withheld exact
  Septin family grounding for the existing generic component.
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
  - path: data/structures/cytoskeleton/split_septin_rings.yaml
    sha256: 580abb6f00c144e871e1fded7fbb2dca8584ecf0d47a599f646558642c3027ff
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
- target_id: GO:0032176
  path: data/structures/cytoskeleton/split_septin_rings.yaml
  label: split septin rings
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/split_septin_rings.yaml
    role: maintained scientific record
scope:
  description: Entire single maintained target, every stable identifier, native family
    and GO relations; claim-bearing ontology-provenance review context; graph and
    uncertainty limits.
  selection: First selected path in batch twelve, fixed maintained-path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0032176
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0032176
  command: just validate data/structures/cytoskeleton/split_septin_rings.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0032176
  command: just validate-strict data/structures/cytoskeleton/split_septin_rings.yaml
    --out /private/tmp/cellstructure-batch12-20261021-ipvr425j/split_septin_rings-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0032176
  summary: 7 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0032176
  summary: No transcriptional regulatory or expression-module claim is asserted.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0032176
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - split-rings-agent-go
  - split-rings-agent-family
  - split-rings-agent-douglas-pmc
  - split-rings-agent-versele-pmc
  - split-rings-agent-douglas-metadata
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0032176
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch12 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0032176
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch12 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0032176
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch12 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0032176
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch12 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0032176
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch12 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/split_septin_rings.yaml
  locator: Entire maintained YAML, including component, function, graph, discussions
    and history
  accessed_at: '2026-10-21T08:26:49Z'
  support: context_only
  summary: The complete target was read after native inspect. No scientific content
    or PROPOSED status is changed.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Components, evidence and grounding rules
  accessed_at: '2026-10-21T08:26:49Z'
  support: context_only
  summary: A generic protein-family component may use the exact family class without
    resolving every localized paralogue. Optional inventories are not mandatory.
- evidence_id: split-rings-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032176,GO:0032156,GO:0005856,GO:0032177,GO:0032153,GO:0005940,GO:0032173
  locator: Seven exact result IDs; names, definitions, isObsolete and returned child
    relations
  accessed_at: '2026-10-21T08:24:42.676380Z'
  support: supports
  summary: Active GO0032176 exactly matches the definition of the split pair and its
    tentative protein-trapping function. Returned parent GO0032156 has a direct is_a
    child link to GO0032176; GO0005856 has its part_of child link. GO0032177 narrows
    to cellular bud neck, while GO0005940 and GO0032173 identify the unsplit ring
    and collar. GO0032153 identifies the cell division site.
  snapshot_sha256: 063edda467c6a954eb7089a93e2953af863c6a9f8237d9d5eab53a1bbb7e07ea
- evidence_id: split-rings-agent-family
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016491/
  locator: metadata accession, name, type and description; family class distinguished
    from domain and localized cohort
  accessed_at: '2026-10-21T08:24:42.677210Z'
  support: supports
  summary: IPR016491 is the Septin family and explicitly represents filament-forming
    septin GTPases. It matches the generic septin-proteins row; this does not identify
    the exact remaining cohort, paralogue-specific necessity or native stoichiometry.
    Older assembly statements in the descriptive text are not adopted.
  snapshot_sha256: 5797c626d192b641ed5b4b2231e729f9f179bfd6bb18f911689fa08253688c4a
- evidence_id: split-rings-agent-douglas-pmc
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1214204/
  locator: PMC1214204 HTML; cell-cycle introduction, sec11 Cytokinesis barrier; sec3
    inspected for assembly-model limits
  accessed_at: '2026-10-21T07:11:03.050463Z'
  support: supports
  summary: Douglas et al.2005 is a literature review, not a new perturbation experiment.
    Cell-cycle introductory paragraphs and sec11 describe collar splitting and confinement
    of selected cytokinesis/septation factors; reviewed cdc12-6 experiments distinguish
    loss of Spa2/Sec3/Chs2 from retention of the actomyosin ring. No direct binding
    or universal barrier efficacy is inferred.
  snapshot_sha256: 31a2dd0109697492854f84701ef3f1d1be31f62312b613ab8432223332b69dd3
- evidence_id: split-rings-agent-versele-pmc
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1761124/?pdf=render
  locator: PMC1761124 HTML despite pdf=render query; S2 Septin functions and embedded
    Figure3 legend
  accessed_at: '2026-10-21T07:29:14.610794Z'
  support: supports
  summary: Versele/Thorner2005 is a literature review. S2 and Figure3 legend distinguish
    collar-to-pair conversion and tentative cytokinetic confinement from broader septin
    functions. Fission-yeast comparisons are context, not new taxon distribution rows
    or universal essentiality.
  snapshot_sha256: bfa7c582507daf47688819cdd2ed31ed4dab32ed0d9e14a0d74d40c29249ac9d
- evidence_id: split-rings-agent-douglas-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1128/EC.4.9.1503-1512.2005&format=json&resultType=core
  locator: resultList.result exact DOI/title/authors/year/PMID
  accessed_at: '2026-10-21T06:58:21.193422Z'
  support: supports
  summary: Native DOI identity confirms Douglas et al.2005, PMID16151244, DOI10.1128/EC.4.9.1503-1512.2005;
    this is the review named in native GO definition provenance.
  snapshot_sha256: 1c4a6be031ab36975c4a274aec9c9d0182e2928499b9ee140022a8a1a4b80d1d
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/split_septin_rings.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:24:48Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/split_septin_rings.yaml'
  snapshot_sha256: 11f93417f88bc596e5e035eeeb0f99cc742c1f2de6dc86a902e82c96f474cd61
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/split_septin_rings.yaml
    --out /private/tmp/cellstructure-batch12-20261021-ipvr425j/split_septin_rings-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:24:50Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/split_septin_rings.yaml\
    \ --out /private/tmp/cellstructure-batch12-20261021-ipvr425j/split_septin_rings-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch12-20261021-ipvr425j/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch12-20261021-ipvr425j/split_septin_rings-strict.tsv"
  snapshot_sha256: 10ae5d4830d5e01a4283b68a66d53b01e3a34293b4236e829f45ac3bb94efe55
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/split_septin_rings.yaml; exact collect() scope;
    hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T08:26:49Z'
  support: supports
  summary: '7 of7 collected target identifiers returned OK at the unchanged base.
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
  topic: Generic split pair and precursor boundaries
  outcome: supported
  target_ids:
  - GO:0032176
  summary: GO0032176 identifies the pair of septin rings, not one ring, a collar,
    a single septin protein or only the bud-neck subtype. FILAMENT describes this
    filamentous assembly at the record granularity. No exact synonym collision was
    established.
  evidence_ids:
  - split-rings-agent-go
  - record
- assessment_id: hierarchy
  area: scope
  topic: Native is-a and parthood links
  outcome: supported
  target_ids:
  - GO:0032176
  summary: Native child relations confirm the asserted septin-cytoskeleton parent
    and cytoskeleton parthood. The bud-neck split pair is a narrower child. No species
    or prevalence row is asserted; the definition preserves known budding-yeast occurrence
    and uncertainty elsewhere.
  evidence_ids:
  - split-rings-agent-go
  - record
- assessment_id: composition
  area: grounding
  topic: Generic family versus unresolved localized membership
  outcome: concern
  target_ids:
  - GO:0032176
  summary: The generic septin-proteins component can be grounded to IPR016491. Deferring
    it until a family exactly delimits every split-ring-forming septin confuses family
    identity with developmental membership. ESSENTIAL is interpreted collectively
    as septin material needed to constitute a septin pair; it does not assert all
    individual genes are indispensable.
  evidence_ids:
  - split-rings-agent-family
  - split-rings-agent-go
  - record
  - policy
- assessment_id: function
  area: evidence
  topic: Tentative cytokinetic compartment boundary
  outcome: supported
  target_ids:
  - GO:0032176
  summary: The function accurately retains thought-to-trap wording. The reviewed examples
    support confinement of selected membrane-associated factors; they do not make
    all cytokinesis proteins septin constituents or establish direct interaction,
    autonomous constriction, or a universal impermeable barrier.
  evidence_ids:
  - split-rings-agent-go
  - split-rings-agent-douglas-pmc
  - split-rings-agent-versele-pmc
  - record
- assessment_id: graph
  area: graph
  topic: Nonmechanistic split topology
  outcome: supported
  target_ids:
  - GO:0032176
  summary: The assemble-into, splits-into and flank edges faithfully summarize class
    composition and morphology. The explicit NONMECHANISTIC scope avoids a claim of
    de novo molecular polymerization, exact recruitment order or a resolved splitting
    motor. The disjunctive ring-or-collar node is intentionally broader than either
    single GO identity.
  evidence_ids:
  - split-rings-agent-go
  - split-rings-agent-douglas-pmc
  - split-rings-agent-versele-pmc
  - record
- assessment_id: completeness
  area: completeness
  topic: Optional examples and molecular inventories
  outcome: supported
  target_ids:
  - GO:0032176
  summary: No exact protein examples, image, dimensions, stoichiometry or native splitting
    mechanism are asserted. Empty optional slots do not create a defect. The open
    grounding discussion remains useful, but its current family criterion needs the
    bounded correction below.
  evidence_ids:
  - split-rings-agent-go
  - split-rings-agent-family
  - record
  - policy
- assessment_id: provenance
  area: provenance
  topic: Ontology authority and source tiers
  outcome: supported
  target_ids:
  - GO:0032176
  summary: All asserted GO identities are verified natively. Both supporting paper
    bodies are reviews, explicitly treated as secondary context; relevant sections
    were read, not substituted for independent primary experiments. Reused receipts
    retain original access timestamps and hashes.
  evidence_ids:
  - split-rings-agent-go
  - split-rings-agent-douglas-pmc
  - split-rings-agent-versele-pmc
  - split-rings-agent-douglas-metadata
  - record
findings:
- finding_id: F1
  issue_key: split-septin-rings-generic-family-withheld
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: The generic septin component has an exact family grounding
  description: The septin_proteins row is REVIEWED_LABEL_ONLY because no family accession
    was assigned for the complete split-ring-forming cohort. Native IPR016491 directly
    represents the generic Septin family already named by the row. Assigning this
    class does not require determining which paralogues remain in a particular split
    pair or asserting that every family member forms this structure. Ground the generic
    row to InterPro:IPR016491 and retain exact membership as an open question.
  target_ids:
  - GO:0032176
  field_paths:
  - components[component_id=septin_proteins].grounding
  - components[component_id=septin_proteins].grounding_status
  - components[component_id=septin_proteins].grounding_notes
  - discussions[discussion_id=resolve_split_septin_rings_grounding]
  evidence_ids:
  - split-rings-agent-family
  - split-rings-agent-go
  - record
  - policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/split_septin_rings.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components
  native_severity: minor
  normalization_reason: The structure and function remain supported; this is a resolvable
    family mapping for an existing generic component.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0032176
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/split_septin_rings.yaml
    role: maintained scientific record
  description: In authorized curation, ground the septin-proteins row to InterPro:IPR016491
    and align grounding status and notes. Preserve historical discussion rationale
    and record current progress in notes; retain unresolved localized cohort and individual
    essentiality limits.
  acceptance_checks:
  - Compare component scope against native IPR016491 family description.
  - Do not add unverified paralogue examples or universal assembly necessity.
  - Run native schema, strict, label, history and generated-page checks after maintained-record
    changes.
  generator: Maintained structure YAML; generated pages derive from it.
limitations:
- No new primary perturbation experiment or underlying raw microscopy was reanalyzed;
  literature context is explicitly review-tier.
- Exact paralogue membership, native stoichiometry, molecular splitting mechanism
  and universal barrier efficacy remain unresolved and are not asserted.
- No new exhaustive repository or ontology absence claim is made; historical rationale
  is preserved.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- Native inspect/schema/strict all passed before assessment. Parent audit, finalization
  and persistence remain pending.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
