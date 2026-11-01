# New spindle pole body SIN complex identity and evidence-scope review

- Review: 20261021T074638Z-new-spindle-pole-body-sin-signaling-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T07:36:35Z
- Finished UTC: 2026-10-21T07:46:38Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Exact complex identity, parentage, species scope and bounded new-pole anaphase function are supported. No concrete curation defect was established; component inventory and experimental interpretation limits remain explicit.

## Scope And Provenance

Entire single target; every asserted native GO, taxon and DOI identity; relevant primary article introduction, results, discussion, captions and methods.

Selection: Sixth unreviewed path in batch nine, in repository path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0160067 | data/structures/cytoskeleton/new_spindle_pole_body_sin_signaling_complex.yaml | maintained | new spindle pole body SIN signaling complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0160067 | Focused validator passed. |
| Focused native strict | passed | True | GO:0160067 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0160067 | 7 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | GO:0160067 | The assertions concern a localized protein signaling assembly, not an expression-module or transcriptional-regulator mechanism. |
| Claim-level scientific review | passed | True | GO:0160067 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0160067 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0160067 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0160067 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0160067 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0160067 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Exact complex and sibling boundaries

identity: supported. Targets: GO:0160067.

The identifier, definition, exact synonym and direct parent agree. The interphase SIN state and two-component GAP are distinct identities, and the signaling complex is not equated with the whole new SPB.

### Association versus parthood

representation: supported. Targets: GO:0160067.

The target describes association with a new mitotic SPB without promoting that wording to a proper-part relation. Its scope is a signaling state, separate from SPB duplication or a whole organelle.

### Anaphase new-pole SIN activation

evidence: supported. Targets: GO:0160067.

GO supports the active-Spg1 new-pole state. The cited primary paper Introduction explains pole-asymmetric activity through earlier work, while its experiments establish bounded Sid4/Plo1/Byr4 regulation. Those evidence tiers support the minimal record without asserting that this paper newly measured pole age or reconstituted the full activation chain.

### Species and experimental context

scope: supported. Targets: GO:0160067.

The S.pombe species example agrees with taxonomy and source. COMMON is qualitative occurrence in the described cell-cycle state, not a population survey. Checkpoint-arrest and synchronization experiments do not imply constitutive active complexes at every SPB.

### Acknowledged constituent grounding

completeness: supported. Targets: GO:0160067.

The record leaves exact Spg1/SIN component mappings open. Source-named regulators and scaffolds suggest future enrichment, but no complete inventory, required mapping or exact modern family match is established by this audit. Optional absent composition and graph fields alone do not constitute defects.

### Citation and actual source access

provenance: supported. Targets: GO:0160067.

Citation metadata and actual native article prose were read. Failed XML routes were not used as scientific evidence; the recovered HTML supports the scoped review. No primary experimental finding is inferred solely from the bibliographic abstract.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| new-sin-prep-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0071958,GO:0160065,GO:0160066,GO:0160067,GO:1990334; All five returned definitions, active flags, synonym scopes and parent-term child relations | supports | Native GO confirms exact GO0160067 definition and spelling synonym, direct GO0160065 parent, and distinct interphase, two-component GAP and new-mitotic-SPB identities. The target is a signaling complex associated with the SPB, not the whole SPB. |
| new-sin-prep-species | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896; taxId, scientificName, rank | supports | Taxon4896 is Schizosaccharomyces pombe at species rank. |
| new-sin-prep-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1038/emboj.2010.317&amp;format=json&amp;resultType=core; Single DOI result title, author list, DOI/PMID/PMCID and complete abstract | supports | The exact DOI resolves to Johnson and Gould2011, Dma1 ubiquitinates the SIN scaffold, Sid4, to impede the mitotic localization of Plo1 kinase, PMID21131906/PMC3025462. |
| new-sin-prep-paper-html | https://pmc.ncbi.nlm.nih.gov/articles/PMC3025462/?pdf=render; Actual PMC3025462 HTML: Introduction; Results sections3,5-9 and associated captions; Discussion sections10-14/Figure8; Methods16,17,20,22 | supports | Introduction describes Spg1 activation and anaphase-B asymmetry: Byr4-Cdc16 returns to the old SPB, leaving SIN activity at the new pole. The novel study tests Dma1/Sid4 ubiquitination and Plo1/Byr4 localization in checkpoint and interphase conditions. Figure8 presents a mechanistic model; it is not a purified reconstitution of the whole complex. |
| record | data/structures/cytoskeleton/new_spindle_pole_body_sin_signaling_complex.yaml; Entire maintained YAML including history, function, examples and discussions | context_only | The target remains PROPOSED. It records the narrow new-SPB anaphase signaling state and no broader fungal prevalence, fixed stoichiometry, exact protein accession or complete constituent inventory. It intentionally does not infer parthood from association. |
| schema-result | just validate data/structures/cytoskeleton/new_spindle_pole_body_sin_signaling_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/new_spindle_pole_body_sin_signaling_complex.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/new_spindle_pole_body_sin_signaling_complex.yaml --out /private/tmp/cellstructure-batch9-20261021-t98tzqpa/new_spindle_pole_body_sin_signaling_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/new_spindle_pole_body_sin_signaling_complex.yaml --out /private/tmp/cellstructure-batch9-20261021-t98tzqpa/new_spindle_pole_body_sin_signaling_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch9-20261021-t98tzqpa/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch9-20261021-t98tzqpa/new_spindle_pole_body_sin_signaling_complex-strict.tsv |
| target-curies | just check-curies-strict; data/structures/cytoskeleton/new_spindle_pole_body_sin_signaling_complex.yaml; exact collect() scope; SHA-256 identifies the entire original resolver TSV, not resolver-slice.json | supports | 7 of 7 collected target identifiers returned OK at the unchanged base. Residuals: none. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Pole-age asymmetry is background synthesis in the cited primary article, citing earlier experiments; those earlier papers were not all independently reread in this target review.
- The primary experiments use nda3-KM311 cold arrest, cdc25-22 G2 arrest and HU/lactose-gradient synchronization. These assays do not establish universal strain prevalence or a complete invariant complex.
- Figure8 is a proposed mechanism. Plo1-dependent Byr4 phosphorylation and localization do not by themselves reconstitute the complete Spg1 activation pathway.
- Article figure pixels, movies, supplements, strain table and raw data were not independently evaluated. Relevant body and captions were read.
- Native S3 XML/metadata routes returned404 and EuropePMC XML returned500; actual PMC HTML was recovered. No source-body absence is claimed.
- No exhaustive protein-family search or full constituent inventory was performed. The existing component TODO remains open.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The explicit user goal requests saving every selected target, including qualified passes; no finding was invented to justify persistence.
- Only the review bundle is saved. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T074638Z-new-spindle-pole-body-sin-signaling-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: New spindle pole body SIN complex identity and evidence-scope review
started_at: '2026-10-21T07:36:35Z'
finished_at: '2026-10-21T07:46:38Z'
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
summary: Exact complex identity, parentage, species scope and bounded new-pole anaphase
  function are supported. No concrete curation defect was established; component inventory
  and experimental interpretation limits remain explicit.
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
  - path: data/structures/cytoskeleton/new_spindle_pole_body_sin_signaling_complex.yaml
    sha256: 84ade1d5217bae8fa401f096724d0892e76378469bec45c6ea25e961a0e28cae
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
- target_id: GO:0160067
  path: data/structures/cytoskeleton/new_spindle_pole_body_sin_signaling_complex.yaml
  label: new spindle pole body SIN signaling complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/new_spindle_pole_body_sin_signaling_complex.yaml
    role: maintained scientific record
scope:
  description: Entire single target; every asserted native GO, taxon and DOI identity;
    relevant primary article introduction, results, discussion, captions and methods.
  selection: Sixth unreviewed path in batch nine, in repository path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0160067
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0160067
  command: just validate data/structures/cytoskeleton/new_spindle_pole_body_sin_signaling_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0160067
  command: just validate-strict data/structures/cytoskeleton/new_spindle_pole_body_sin_signaling_complex.yaml
    --out /private/tmp/cellstructure-batch9-20261021-t98tzqpa/new_spindle_pole_body_sin_signaling_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0160067
  summary: 7 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0160067
  summary: The assertions concern a localized protein signaling assembly, not an expression-module
    or transcriptional-regulator mechanism.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0160067
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - new-sin-prep-go
  - new-sin-prep-species
  - new-sin-prep-epmc
  - new-sin-prep-paper-html
  - record
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0160067
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
  - GO:0160067
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
  - GO:0160067
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
  - GO:0160067
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
  - GO:0160067
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
- evidence_id: new-sin-prep-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0071958,GO:0160065,GO:0160066,GO:0160067,GO:1990334
  locator: All five returned definitions, active flags, synonym scopes and parent-term
    child relations
  accessed_at: '2026-10-21T07:37:31.900788Z'
  support: supports
  summary: Native GO confirms exact GO0160067 definition and spelling synonym, direct
    GO0160065 parent, and distinct interphase, two-component GAP and new-mitotic-SPB
    identities. The target is a signaling complex associated with the SPB, not the
    whole SPB.
  snapshot_sha256: 06fba1d1f2ef39145692a64bda546596ecbc1315c90fd314e689ab0d58852e6c
- evidence_id: new-sin-prep-species
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896
  locator: taxId, scientificName, rank
  accessed_at: '2026-10-21T07:37:31.929559Z'
  support: supports
  summary: Taxon4896 is Schizosaccharomyces pombe at species rank.
  snapshot_sha256: 42c5b7d3d99341137803612d6404cd3884e2d06ec8a740b1ad38163c678f6721
- evidence_id: new-sin-prep-epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1038/emboj.2010.317&format=json&resultType=core
  locator: Single DOI result title, author list, DOI/PMID/PMCID and complete abstract
  accessed_at: '2026-10-21T07:37:32.015617Z'
  support: supports
  summary: The exact DOI resolves to Johnson and Gould2011, Dma1 ubiquitinates the
    SIN scaffold, Sid4, to impede the mitotic localization of Plo1 kinase, PMID21131906/PMC3025462.
  snapshot_sha256: aee80cef63e67f5a3d0babbad6f40b588d62fae282f1cf628f45f5bc6e15144f
- evidence_id: new-sin-prep-paper-html
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3025462/?pdf=render
  locator: 'Actual PMC3025462 HTML: Introduction; Results sections3,5-9 and associated
    captions; Discussion sections10-14/Figure8; Methods16,17,20,22'
  accessed_at: '2026-10-21T07:38:36.977672Z'
  support: supports
  summary: 'Introduction describes Spg1 activation and anaphase-B asymmetry: Byr4-Cdc16
    returns to the old SPB, leaving SIN activity at the new pole. The novel study
    tests Dma1/Sid4 ubiquitination and Plo1/Byr4 localization in checkpoint and interphase
    conditions. Figure8 presents a mechanistic model; it is not a purified reconstitution
    of the whole complex.'
  snapshot_sha256: 317b8a934b9cbbe4bf982be4015c95a502a80ae22db1a0f9b3c23c2c4392486f
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/new_spindle_pole_body_sin_signaling_complex.yaml
  locator: Entire maintained YAML including history, function, examples and discussions
  accessed_at: '2026-10-21T07:40:49Z'
  support: context_only
  summary: The target remains PROPOSED. It records the narrow new-SPB anaphase signaling
    state and no broader fungal prevalence, fixed stoichiometry, exact protein accession
    or complete constituent inventory. It intentionally does not infer parthood from
    association.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/new_spindle_pole_body_sin_signaling_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T07:36:39Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/new_spindle_pole_body_sin_signaling_complex.yaml'
  snapshot_sha256: 8d23135a2852c6eda4192a9a3550eea1284d10861272065618fbef09f10f0b92
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/new_spindle_pole_body_sin_signaling_complex.yaml
    --out /private/tmp/cellstructure-batch9-20261021-t98tzqpa/new_spindle_pole_body_sin_signaling_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T07:36:44Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/new_spindle_pole_body_sin_signaling_complex.yaml\
    \ --out /private/tmp/cellstructure-batch9-20261021-t98tzqpa/new_spindle_pole_body_sin_signaling_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch9-20261021-t98tzqpa/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch9-20261021-t98tzqpa/new_spindle_pole_body_sin_signaling_complex-strict.tsv"
  snapshot_sha256: c86d5c8270a30cc9e729e20fd23e679dd15f018193efab32ec6cf135cc8eb48f
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/new_spindle_pole_body_sin_signaling_complex.yaml;
    exact collect() scope; SHA-256 identifies the entire original resolver TSV, not
    resolver-slice.json
  accessed_at: '2026-10-21T07:40:49Z'
  support: supports
  summary: '7 of 7 collected target identifiers returned OK at the unchanged base.
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
  topic: Exact complex and sibling boundaries
  outcome: supported
  target_ids:
  - GO:0160067
  summary: The identifier, definition, exact synonym and direct parent agree. The
    interphase SIN state and two-component GAP are distinct identities, and the signaling
    complex is not equated with the whole new SPB.
  evidence_ids:
  - new-sin-prep-go
  - record
- assessment_id: localization
  area: representation
  topic: Association versus parthood
  outcome: supported
  target_ids:
  - GO:0160067
  summary: The target describes association with a new mitotic SPB without promoting
    that wording to a proper-part relation. Its scope is a signaling state, separate
    from SPB duplication or a whole organelle.
  evidence_ids:
  - new-sin-prep-go
  - new-sin-prep-paper-html
  - record
- assessment_id: function
  area: evidence
  topic: Anaphase new-pole SIN activation
  outcome: supported
  target_ids:
  - GO:0160067
  summary: GO supports the active-Spg1 new-pole state. The cited primary paper Introduction
    explains pole-asymmetric activity through earlier work, while its experiments
    establish bounded Sid4/Plo1/Byr4 regulation. Those evidence tiers support the
    minimal record without asserting that this paper newly measured pole age or reconstituted
    the full activation chain.
  evidence_ids:
  - new-sin-prep-go
  - new-sin-prep-paper-html
  - new-sin-prep-epmc
  - record
- assessment_id: scope
  area: scope
  topic: Species and experimental context
  outcome: supported
  target_ids:
  - GO:0160067
  summary: The S.pombe species example agrees with taxonomy and source. COMMON is
    qualitative occurrence in the described cell-cycle state, not a population survey.
    Checkpoint-arrest and synchronization experiments do not imply constitutive active
    complexes at every SPB.
  evidence_ids:
  - new-sin-prep-species
  - new-sin-prep-paper-html
  - record
- assessment_id: completeness
  area: completeness
  topic: Acknowledged constituent grounding
  outcome: supported
  target_ids:
  - GO:0160067
  summary: The record leaves exact Spg1/SIN component mappings open. Source-named
    regulators and scaffolds suggest future enrichment, but no complete inventory,
    required mapping or exact modern family match is established by this audit. Optional
    absent composition and graph fields alone do not constitute defects.
  evidence_ids:
  - new-sin-prep-go
  - new-sin-prep-paper-html
  - record
- assessment_id: provenance
  area: provenance
  topic: Citation and actual source access
  outcome: supported
  target_ids:
  - GO:0160067
  summary: Citation metadata and actual native article prose were read. Failed XML
    routes were not used as scientific evidence; the recovered HTML supports the scoped
    review. No primary experimental finding is inferred solely from the bibliographic
    abstract.
  evidence_ids:
  - new-sin-prep-epmc
  - new-sin-prep-paper-html
findings: []
actions: []
limitations:
- Pole-age asymmetry is background synthesis in the cited primary article, citing
  earlier experiments; those earlier papers were not all independently reread in this
  target review.
- The primary experiments use nda3-KM311 cold arrest, cdc25-22 G2 arrest and HU/lactose-gradient
  synchronization. These assays do not establish universal strain prevalence or a
  complete invariant complex.
- Figure8 is a proposed mechanism. Plo1-dependent Byr4 phosphorylation and localization
  do not by themselves reconstitute the complete Spg1 activation pathway.
- Article figure pixels, movies, supplements, strain table and raw data were not independently
  evaluated. Relevant body and captions were read.
- Native S3 XML/metadata routes returned404 and EuropePMC XML returned500; actual
  PMC HTML was recovered. No source-body absence is claimed.
- No exhaustive protein-family search or full constituent inventory was performed.
  The existing component TODO remains open.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- The explicit user goal requests saving every selected target, including qualified
  passes; no finding was invented to justify persistence.
- Only the review bundle is saved. Maintained scientific content, native status, history
  and generated pages remain unchanged.
```
