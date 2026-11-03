# Meiotic spindle pole body identity, remodeling and membrane-initiation review

- Review: 20261021T074511Z-meiotic-spindle-pole-body-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T07:35:43Z
- Finished UTC: 2026-10-21T07:45:11Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Exact meiotic SPB identity, the budding-yeast meiosis-II MOP boundary and bounded membrane-initiation topology are supported. The optional constituent inventory remains unresolved; no concrete curation defect was established.

## Scope And Provenance

Entire single target, all asserted native identities and citations, the full local MOP reference, claim-relevant primary Results/Discussion and component-boundary checks.

Selection: First selected unreviewed path in batch nine, in repository path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0035974 | data/structures/cytoskeleton/meiotic_spindle_pole_body.yaml | maintained | meiotic spindle pole body |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0035974 | Focused validator passed. |
| Focused native strict | passed | True | GO:0035974 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0035974 | 8 identifiers OK; 1 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | GO:0035974 | No transcriptional-regulator or expression-module mechanism is asserted. Structural localization and optional constituent candidates are not inferred from expression modules. |
| Claim-level scientific review | passed | True | GO:0035974 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0035974 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0035974 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0035974 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0035974 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0035974 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Whole meiotic SPB versus outer-plaque substructure

identity: supported. Targets: GO:0035974.

The definition and is-a parent agree with native GO. The local meiotic outer plaque resolves and remains a part of the whole SPB; the prose and graph do not equate the plaque with the membrane attachment region or with the entire organelle.

### Budding-yeast meiosis-II example

scope: supported. Targets: GO:0035974.

The named species and reference model are supported. The MOP and membrane-initiation claims are expressly scoped to budding yeast and meiosis II. COMMON is qualitative occurrence in this characterized species, not a measured prevalence across cells or fungal lineages.

### Microtubule organization and normal membrane initiation

evidence: supported. Targets: GO:0035974.

The microtubule-organizing function follows the exact GO class. Primary experiments support the remodeled SPB as the normal membrane-initiation and anchoring site. This is compatible with retained precursor targeting or untethered membrane formation in particular mutants; the record asserts neither autonomous fusion catalysis nor universal absolute dependence in every mutant.

### Nonmechanistic subtype, parthood and initiation-site edges

graph: supported. Targets: GO:0035974.

Each edge is supported at its declared level: meiotic SPB subtype, meiosis-II MOP parthood, and membrane initiation at that plaque. No ordered protein recruitment, direct pairwise binding or complete vesicle-fusion pathway is inferred.

### Acknowledged constituent inventory

completeness: supported. Targets: GO:0035974.

Mpc54, Spo21/Mpc70 and Spo74 are bounded budding-yeast MOP candidates. Ady4 stability, common SPB constituents and the distinction between recruitment and permanent membership require care. No exact family accessions, fixed stoichiometry or erroneous component examples are currently asserted. The optional inventory and accession TODO therefore remain limitations, not an observed defect.

### Primary source identities and actual access

provenance: supported. Targets: GO:0035974.

All three cited DOI identities are verified, including the two cited only in the component TODO. The primary article bodies were actually read at the claim-relevant sections. The Mathieson publisher route failed but native PMC full text was recovered; its incomplete metadata availability flag is not evidence that the body is unavailable.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/meiotic_spindle_pole_body.yaml; Entire maintained YAML, including definition, history, species examples, all evidence, graph if present, and discussions | context_only | The complete PROPOSED record was read. Its scope and open composition discussion are assessed separately from optional future enrichment. No scientific content or status is changed. |
| policy | docs/CURATION.md; Structure identity, hierarchy, component grounding, evidence and scientific-status rules | context_only | Whole structures, substructures, constituent protein families and transient regulatory localization require distinct scope. Empty optional component inventories do not by themselves establish a defect. |
| meiotic-spb-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0035974%2CGO%3A0005816%2CGO%3A0031322%2CGO%3A0005628%2CGO%3A0005824%2CGO%3A0070057; All six returned definitions, active flags and parent child relations | supports | GO0035974 is the active meiotic SPB class under GO0005816. GO0031322 denotes the remodeling process; GO0005628 the prospore membrane; GO0005824 the outer plaque; GO0070057 the membrane attachment region. These are distinct entities. |
| meiotic-spb-agent-taxon | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; taxId, scientificName, rank and lineage | supports | ENA confirms NCBITaxon4932 is Saccharomyces cerevisiae at species rank. |
| meiotic-spb-agent-knop2000-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1093/emboj/19.14.3657&amp;format=json&amp;resultType=core; Exact native EuropePMC result: DOI, PMID, title, authors, year, journal and availability fields | supports | Knop and Strasser2000: DOI10.1093/emboj/19.14.3657, PMID10899120, PMC313968, exact title and authors. |
| meiotic-spb-agent-bajgier2001-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1091/mbc.12.6.1611&amp;format=json&amp;resultType=core; Exact native EuropePMC result: DOI, PMID, title, authors, year, journal and availability fields | supports | Bajgier et al.2001: DOI10.1091/mbc.12.6.1611, PMID11408572, PMC37328, exact title and authors. |
| meiotic-spb-agent-mathieson2010-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1091/mbc.E10-07-0563&amp;format=json&amp;resultType=core; Exact native EuropePMC result: DOI, PMID, title, authors, year, journal and availability fields | supports | Mathieson et al.2010: DOI10.1091/mbc.E10-07-0563, PMID20826607, exact title and authors. This metadata response omits its PMCID; the separately inspected native PMC2965686 article resolves full-text availability. |
| meiotic-spb-agent-knop2000 | https://pmc.ncbi.nlm.nih.gov/articles/PMC313968/?pdf=render; Native PMC313968 HTML, Results sections sec4 and sec7-sec9; Discussion sec11-sec12; figure legends as text. Actual article body, not a PDF or challenge response. | supports | Budding-yeast primary experiments connect Mpc54/Mpc70-dependent meiotic outer-plaque assembly to normal prospore-membrane formation. Precursor targeting can persist without mature plaque assembly. The body distinguishes the whole SPB, its meiosis-II plaque and the growing membrane; fusion-machinery recruitment in Discussion is a model. |
| meiotic-spb-agent-bajgier2001 | https://pmc.ncbi.nlm.nih.gov/articles/PMC37328/?pdf=render; Native PMC37328 HTML, Results sec8, sec11-sec12 and sec15; Discussion sec17; source-specific mutant and meiotic-stage context | supports | Spo21/Mpc70 contributes to meiosis-specific SPB modification. spo21 deletion disrupts plaque and membrane formation while meiotic divisions proceed. cnm67 mutants can form untethered prospore membranes, limiting any claim that attachment to an intact SPB is universally indispensable. |
| meiotic-spb-agent-mathieson2010-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC2965686/?pdf=render; Native PMC2965686 HTML, Results sec11 and sec14-sec18; Discussion sec20-sec23; article identity/DOI in header and text figure legends | supports | Selected Mpc54 point mutants retain meiotic-plaque composition and ultrastructure while impairing vesicle docking and recruitment of Sec4/exocyst factors. The FRET-based model places Mpc54/Spo21 N termini toward the membrane-facing surface; Ady4 is not a stable component, and Spo74 placement is unresolved. Proposed direct binding or exchange mechanisms remain interpretation. |
| local-mop | data/structures/cytoskeleton/meiotic_outer_plaque.yaml; Entire referenced local record; exact identifier cellstructuremech:meiotic_outer_plaque; captured as additional native inspect input | context_only | The internal identifier resolves to the maintained meiosis-II outer-plaque substructure, not the whole meiotic SPB or a region of the membrane. Exact-identifier search included ignored files under data/structures. |
| schema-result | just validate data/structures/cytoskeleton/meiotic_spindle_pole_body.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/meiotic_spindle_pole_body.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/meiotic_spindle_pole_body.yaml --out /private/tmp/cellstructure-batch9-20261021-t98tzqpa/meiotic_spindle_pole_body-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/meiotic_spindle_pole_body.yaml --out /private/tmp/cellstructure-batch9-20261021-t98tzqpa/meiotic_spindle_pole_body-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch9-20261021-t98tzqpa/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch9-20261021-t98tzqpa/meiotic_spindle_pole_body-strict.tsv |
| target-curies | just check-curies-strict; data/structures/cytoskeleton/meiotic_spindle_pole_body.yaml; exact collect() scope; SHA-256 identifies the entire original resolver TSV at /private/tmp/cellstructure-record-reviews-UhRFh7/repo/reports/curie_check.tsv, not derived resolver-slice.json | supports | 8 of 9 collected target identifiers returned OK at the unchanged base. Residuals: cellstructuremech:meiotic_outer_plaque: SKIPPED; resolved by evidence local-mop. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- The primary article text and relevant figure legends were read; this review did not reanalyze microscopy pixels, raw data, movies or all supplementary material.
- The optional whole-SPB/MOP component inventory, exact source-neutral family mappings and molecular copy counts remain unresolved. Named candidates are not new record assertions.
- Normal MOP-mediated membrane initiation does not imply that every precursor-targeting step or experimentally untethered membrane depends absolutely on a mature plaque.
- The Mathieson publisher URL returned403; the genuine PMC2965686 HTML resolves body access. EuropePMC metadata lacks the PMCID despite that actual article being available.
- Public readability was established; no figure or article reuse license is inferred, and no image is reused.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The explicit user goal requests a review for every selected target, including records without a concrete issue. No finding was invented to satisfy that persistence instruction.
- Only a review bundle is saved. Maintained scientific content, native status, history and generated pages remain unchanged.
- Parent independently read the full target, full referenced MOP context, draft, receipt hashes and selected primary Results/Discussion sections; the source collaborator inspected the remaining claim-bearing sections. Parent accepts the bounded assessments before saving.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T074511Z-meiotic-spindle-pole-body-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Meiotic spindle pole body identity, remodeling and membrane-initiation review
started_at: '2026-10-21T07:35:43Z'
finished_at: '2026-10-21T07:45:11Z'
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
summary: Exact meiotic SPB identity, the budding-yeast meiosis-II MOP boundary and
  bounded membrane-initiation topology are supported. The optional constituent inventory
  remains unresolved; no concrete curation defect was established.
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
  - path: data/structures/cytoskeleton/meiotic_outer_plaque.yaml
    sha256: 5482b05be175efef27e7e2acd73c2a7fb6cddbd69ebe7c430ed0adc3f858bfe9
    role: context
  - path: data/structures/cytoskeleton/meiotic_spindle_pole_body.yaml
    sha256: 2a99651652ccaa1b26dd8149e44976824366dbe2157a708fb1df0560323b8a75
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
- target_id: GO:0035974
  path: data/structures/cytoskeleton/meiotic_spindle_pole_body.yaml
  label: meiotic spindle pole body
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/meiotic_spindle_pole_body.yaml
    role: maintained scientific record
scope:
  description: Entire single target, all asserted native identities and citations,
    the full local MOP reference, claim-relevant primary Results/Discussion and component-boundary
    checks.
  selection: First selected unreviewed path in batch nine, in repository path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0035974
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0035974
  command: just validate data/structures/cytoskeleton/meiotic_spindle_pole_body.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0035974
  command: just validate-strict data/structures/cytoskeleton/meiotic_spindle_pole_body.yaml
    --out /private/tmp/cellstructure-batch9-20261021-t98tzqpa/meiotic_spindle_pole_body-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0035974
  summary: 8 identifiers OK; 1 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - local-mop
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0035974
  summary: No transcriptional-regulator or expression-module mechanism is asserted.
    Structural localization and optional constituent candidates are not inferred from
    expression modules.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0035974
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - meiotic-spb-agent-go
  - meiotic-spb-agent-taxon
  - meiotic-spb-agent-knop2000-metadata
  - meiotic-spb-agent-bajgier2001-metadata
  - meiotic-spb-agent-mathieson2010-metadata
  - meiotic-spb-agent-knop2000
  - meiotic-spb-agent-bajgier2001
  - meiotic-spb-agent-mathieson2010-pmc
  - local-mop
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0035974
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
  - GO:0035974
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
  - GO:0035974
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
  - GO:0035974
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
  - GO:0035974
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
  reference: data/structures/cytoskeleton/meiotic_spindle_pole_body.yaml
  locator: Entire maintained YAML, including definition, history, species examples,
    all evidence, graph if present, and discussions
  accessed_at: '2026-10-21T07:44:35Z'
  support: context_only
  summary: The complete PROPOSED record was read. Its scope and open composition discussion
    are assessed separately from optional future enrichment. No scientific content
    or status is changed.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Structure identity, hierarchy, component grounding, evidence and scientific-status
    rules
  accessed_at: '2026-10-21T07:44:35Z'
  support: context_only
  summary: Whole structures, substructures, constituent protein families and transient
    regulatory localization require distinct scope. Empty optional component inventories
    do not by themselves establish a defect.
- evidence_id: meiotic-spb-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0035974%2CGO%3A0005816%2CGO%3A0031322%2CGO%3A0005628%2CGO%3A0005824%2CGO%3A0070057
  locator: All six returned definitions, active flags and parent child relations
  accessed_at: '2026-10-21T07:36:47.661727Z'
  support: supports
  summary: GO0035974 is the active meiotic SPB class under GO0005816. GO0031322 denotes
    the remodeling process; GO0005628 the prospore membrane; GO0005824 the outer plaque;
    GO0070057 the membrane attachment region. These are distinct entities.
  snapshot_sha256: cf3f57c87019a739f5f8ec0b5ee1fb0d71dd2e65fd7dd9c2a8a866da5eef70a6
- evidence_id: meiotic-spb-agent-taxon
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: taxId, scientificName, rank and lineage
  accessed_at: '2026-10-21T07:36:47.663798Z'
  support: supports
  summary: ENA confirms NCBITaxon4932 is Saccharomyces cerevisiae at species rank.
  snapshot_sha256: be57b95543b586448f6bd2889db42e91038e90ae2d12e8f654050c92af5b9087
- evidence_id: meiotic-spb-agent-knop2000-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1093/emboj/19.14.3657&format=json&resultType=core
  locator: 'Exact native EuropePMC result: DOI, PMID, title, authors, year, journal
    and availability fields'
  accessed_at: '2026-10-21T07:36:48.287275Z'
  support: supports
  summary: 'Knop and Strasser2000: DOI10.1093/emboj/19.14.3657, PMID10899120, PMC313968,
    exact title and authors.'
  snapshot_sha256: 349682920200ce7c16b752e509cf8c44e7fb87cfe93a8afc4b724b150b7b61b0
- evidence_id: meiotic-spb-agent-bajgier2001-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1091/mbc.12.6.1611&format=json&resultType=core
  locator: 'Exact native EuropePMC result: DOI, PMID, title, authors, year, journal
    and availability fields'
  accessed_at: '2026-10-21T07:36:48.347606Z'
  support: supports
  summary: 'Bajgier et al.2001: DOI10.1091/mbc.12.6.1611, PMID11408572, PMC37328,
    exact title and authors.'
  snapshot_sha256: 83c5dfbd96f2d5da321735d88518341c2c7f34d2dbf885fcb3ca8689efff53e6
- evidence_id: meiotic-spb-agent-mathieson2010-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1091/mbc.E10-07-0563&format=json&resultType=core
  locator: 'Exact native EuropePMC result: DOI, PMID, title, authors, year, journal
    and availability fields'
  accessed_at: '2026-10-21T07:36:48.349756Z'
  support: supports
  summary: 'Mathieson et al.2010: DOI10.1091/mbc.E10-07-0563, PMID20826607, exact
    title and authors. This metadata response omits its PMCID; the separately inspected
    native PMC2965686 article resolves full-text availability.'
  snapshot_sha256: 0e097a8534eedd42b2c0908c58a03d79af4ffbc60ff928c0e989081b61efa43c
- evidence_id: meiotic-spb-agent-knop2000
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC313968/?pdf=render
  locator: Native PMC313968 HTML, Results sections sec4 and sec7-sec9; Discussion
    sec11-sec12; figure legends as text. Actual article body, not a PDF or challenge
    response.
  accessed_at: '2026-10-21T07:37:23.466715Z'
  support: supports
  summary: Budding-yeast primary experiments connect Mpc54/Mpc70-dependent meiotic
    outer-plaque assembly to normal prospore-membrane formation. Precursor targeting
    can persist without mature plaque assembly. The body distinguishes the whole SPB,
    its meiosis-II plaque and the growing membrane; fusion-machinery recruitment in
    Discussion is a model.
  snapshot_sha256: 89e24f8eb71ab8a06baee2867ccd1df6f6ac0b12a25289ce4c076cb851e1721c
- evidence_id: meiotic-spb-agent-bajgier2001
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC37328/?pdf=render
  locator: Native PMC37328 HTML, Results sec8, sec11-sec12 and sec15; Discussion sec17;
    source-specific mutant and meiotic-stage context
  accessed_at: '2026-10-21T07:37:23.467272Z'
  support: supports
  summary: Spo21/Mpc70 contributes to meiosis-specific SPB modification. spo21 deletion
    disrupts plaque and membrane formation while meiotic divisions proceed. cnm67
    mutants can form untethered prospore membranes, limiting any claim that attachment
    to an intact SPB is universally indispensable.
  snapshot_sha256: 414d78fc89d642394c04c1868383dc35beccc24e19f55da4f159339c39235da9
- evidence_id: meiotic-spb-agent-mathieson2010-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2965686/?pdf=render
  locator: Native PMC2965686 HTML, Results sec11 and sec14-sec18; Discussion sec20-sec23;
    article identity/DOI in header and text figure legends
  accessed_at: '2026-10-21T07:37:51.204155Z'
  support: supports
  summary: Selected Mpc54 point mutants retain meiotic-plaque composition and ultrastructure
    while impairing vesicle docking and recruitment of Sec4/exocyst factors. The FRET-based
    model places Mpc54/Spo21 N termini toward the membrane-facing surface; Ady4 is
    not a stable component, and Spo74 placement is unresolved. Proposed direct binding
    or exchange mechanisms remain interpretation.
  snapshot_sha256: 7bc3047dd15a265fedc4770a608b941dda8129630afdac28bc5c9e5ee1f5e06c
- evidence_id: local-mop
  kind: record_content
  reference: data/structures/cytoskeleton/meiotic_outer_plaque.yaml
  locator: Entire referenced local record; exact identifier cellstructuremech:meiotic_outer_plaque;
    captured as additional native inspect input
  accessed_at: '2026-10-21T07:44:35Z'
  support: context_only
  summary: The internal identifier resolves to the maintained meiosis-II outer-plaque
    substructure, not the whole meiotic SPB or a region of the membrane. Exact-identifier
    search included ignored files under data/structures.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/meiotic_spindle_pole_body.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T07:35:46Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/meiotic_spindle_pole_body.yaml'
  snapshot_sha256: e43c1bea085344614d9bafd76c5aaeafbafb2941ccc2431575d0bf3f1dd7fe18
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/meiotic_spindle_pole_body.yaml
    --out /private/tmp/cellstructure-batch9-20261021-t98tzqpa/meiotic_spindle_pole_body-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T07:35:51Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/meiotic_spindle_pole_body.yaml\
    \ --out /private/tmp/cellstructure-batch9-20261021-t98tzqpa/meiotic_spindle_pole_body-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch9-20261021-t98tzqpa/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch9-20261021-t98tzqpa/meiotic_spindle_pole_body-strict.tsv"
  snapshot_sha256: a5dacf7857019908f6bbcb3f35bd711af4b0651d07e293c579a9c4609dfd17aa
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/meiotic_spindle_pole_body.yaml; exact collect()
    scope; SHA-256 identifies the entire original resolver TSV at /private/tmp/cellstructure-record-reviews-UhRFh7/repo/reports/curie_check.tsv,
    not derived resolver-slice.json
  accessed_at: '2026-10-21T07:44:35Z'
  support: supports
  summary: '8 of 9 collected target identifiers returned OK at the unchanged base.
    Residuals: cellstructuremech:meiotic_outer_plaque: SKIPPED; resolved by evidence
    local-mop. Source-native identity checked separately.'
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
  topic: Whole meiotic SPB versus outer-plaque substructure
  outcome: supported
  target_ids:
  - GO:0035974
  summary: The definition and is-a parent agree with native GO. The local meiotic
    outer plaque resolves and remains a part of the whole SPB; the prose and graph
    do not equate the plaque with the membrane attachment region or with the entire
    organelle.
  evidence_ids:
  - meiotic-spb-agent-go
  - local-mop
  - meiotic-spb-agent-knop2000
  - record
- assessment_id: scope
  area: scope
  topic: Budding-yeast meiosis-II example
  outcome: supported
  target_ids:
  - GO:0035974
  summary: The named species and reference model are supported. The MOP and membrane-initiation
    claims are expressly scoped to budding yeast and meiosis II. COMMON is qualitative
    occurrence in this characterized species, not a measured prevalence across cells
    or fungal lineages.
  evidence_ids:
  - meiotic-spb-agent-go
  - meiotic-spb-agent-taxon
  - meiotic-spb-agent-knop2000
  - meiotic-spb-agent-bajgier2001
  - record
- assessment_id: function
  area: evidence
  topic: Microtubule organization and normal membrane initiation
  outcome: supported
  target_ids:
  - GO:0035974
  summary: The microtubule-organizing function follows the exact GO class. Primary
    experiments support the remodeled SPB as the normal membrane-initiation and anchoring
    site. This is compatible with retained precursor targeting or untethered membrane
    formation in particular mutants; the record asserts neither autonomous fusion
    catalysis nor universal absolute dependence in every mutant.
  evidence_ids:
  - meiotic-spb-agent-go
  - meiotic-spb-agent-knop2000
  - meiotic-spb-agent-bajgier2001
  - meiotic-spb-agent-mathieson2010-pmc
  - record
- assessment_id: graph
  area: graph
  topic: Nonmechanistic subtype, parthood and initiation-site edges
  outcome: supported
  target_ids:
  - GO:0035974
  summary: 'Each edge is supported at its declared level: meiotic SPB subtype, meiosis-II
    MOP parthood, and membrane initiation at that plaque. No ordered protein recruitment,
    direct pairwise binding or complete vesicle-fusion pathway is inferred.'
  evidence_ids:
  - meiotic-spb-agent-go
  - meiotic-spb-agent-knop2000
  - local-mop
  - record
- assessment_id: composition
  area: completeness
  topic: Acknowledged constituent inventory
  outcome: supported
  target_ids:
  - GO:0035974
  summary: Mpc54, Spo21/Mpc70 and Spo74 are bounded budding-yeast MOP candidates.
    Ady4 stability, common SPB constituents and the distinction between recruitment
    and permanent membership require care. No exact family accessions, fixed stoichiometry
    or erroneous component examples are currently asserted. The optional inventory
    and accession TODO therefore remain limitations, not an observed defect.
  evidence_ids:
  - meiotic-spb-agent-knop2000
  - meiotic-spb-agent-bajgier2001
  - meiotic-spb-agent-mathieson2010-pmc
  - record
  - policy
- assessment_id: provenance
  area: provenance
  topic: Primary source identities and actual access
  outcome: supported
  target_ids:
  - GO:0035974
  summary: All three cited DOI identities are verified, including the two cited only
    in the component TODO. The primary article bodies were actually read at the claim-relevant
    sections. The Mathieson publisher route failed but native PMC full text was recovered;
    its incomplete metadata availability flag is not evidence that the body is unavailable.
  evidence_ids:
  - meiotic-spb-agent-knop2000-metadata
  - meiotic-spb-agent-bajgier2001-metadata
  - meiotic-spb-agent-mathieson2010-metadata
  - meiotic-spb-agent-knop2000
  - meiotic-spb-agent-bajgier2001
  - meiotic-spb-agent-mathieson2010-pmc
findings: []
actions: []
limitations:
- The primary article text and relevant figure legends were read; this review did
  not reanalyze microscopy pixels, raw data, movies or all supplementary material.
- The optional whole-SPB/MOP component inventory, exact source-neutral family mappings
  and molecular copy counts remain unresolved. Named candidates are not new record
  assertions.
- Normal MOP-mediated membrane initiation does not imply that every precursor-targeting
  step or experimentally untethered membrane depends absolutely on a mature plaque.
- The Mathieson publisher URL returned403; the genuine PMC2965686 HTML resolves body
  access. EuropePMC metadata lacks the PMCID despite that actual article being available.
- Public readability was established; no figure or article reuse license is inferred,
  and no image is reused.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- The explicit user goal requests a review for every selected target, including records
  without a concrete issue. No finding was invented to satisfy that persistence instruction.
- Only a review bundle is saved. Maintained scientific content, native status, history
  and generated pages remain unchanged.
- Parent independently read the full target, full referenced MOP context, draft, receipt
  hashes and selected primary Results/Discussion sections; the source collaborator
  inspected the remaining claim-bearing sections. Parent accepts the bounded assessments
  before saving.
```
