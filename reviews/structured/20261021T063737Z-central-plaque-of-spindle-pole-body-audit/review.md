# General spindle-pole-body central-plaque evidence review

- Review: 20261021T063737Z-central-plaque-of-spindle-pole-body-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T06:36:41Z
- Finished UTC: 2026-10-21T06:37:37Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Exact central-plaque identity, SPB parthood, species example and both topology edges are supported. No concrete curation defect was found.

## Scope And Provenance

Entire maintained general central-plaque record; native ontology/taxonomy, cited identities, relevant2017 primary-study text and2004 public author manuscript.

Selection: Seventh remaining unreviewed path in batch5, in repository path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0005823 | data/structures/cytoskeleton/central_plaque_of_spindle_pole_body.yaml | maintained | central plaque of spindle pole body |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0005823 | Focused validator passed. |
| Focused native strict | passed | True | GO:0005823 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0005823 | 8 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | GO:0005823 | No gene, regulator or expression-module assertion occurs in this target; structural and ontology evidence addresses the claims. |
| Claim-level scientific review | passed | True | GO:0005823 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0005823 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0005823 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0005823 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0005823 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0005823 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### General envelope-embedded central plaque

identity: supported. Targets: GO:0005823.

The target matches GO and the sources, distinct from the mitotic subtype and adjacent plaques.

### Component of the SPB

grounding: supported. Targets: GO:0005823.

Native GO confirms part_of; the record does not miscast containment as subtype.

### Principal-plaque terminology

evidence: supported. Targets: GO:0005823.

The exact ontology definition is supported by the review. Three principal plaques does not exclude the additional intermediate layers discussed by the sources.

### S. cerevisiae model

scope: supported. Targets: GO:0005823.

The cited literature supports the named species and canonical architecture. COMMON is not a prevalence estimate or a claim that all fungi share identical plaque architecture.

### Two coarse topology relationships

graph: supported. Targets: GO:0005823.

SPB parthood and envelope embedding are directly supported. NONMECHANISTIC preserves the difference from a detailed assembly model.

### Acknowledged constituent follow-up

completeness: supported. Targets: GO:0005823.

Known core proteins occur in the cited literature, but this target makes no exhaustive composition claim. The open TODO is a limitation; no required component field or unsupported identity was found.

### Proposed record and maintained ownership

provenance: supported. Targets: GO:0005823.

The record preserves PROPOSED status and its boundary discussions are coherent. Scientific follow-up belongs in maintained YAML with native curation/history gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| central-plaque-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005823,GO:0005816,GO:0005635,GO:0005822,GO:0005824; Five native definitions and child relations | supports | All five terms are active. GO0005823 exactly matches the definition; GO0005816 lists it as part_of. Inner and outer plaques have distinct nuclear/cytoplasmic positions, while the central plaque is envelope-embedded. |
| mitotic-plaque-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1146/annurev.cellbio.20.022003.114106%20OR%20DOI:10.1091/mbc.E17-06-0397&amp;format=json&amp;resultType=core; Exact bibliographic identities | supports | Both cited DOI/title pairs match Jaspersen/Winey2004 and Viswanath2017. |
| mitotic-plaque-paper | https://pmc-oa-opendata.s3.amazonaws.com/PMC5687031.1/PMC5687031.1.xml; Introduction, core Results and model-validation sections, Figure1 caption and modeling Discussion | supports | The2017 primary study models the S. cerevisiae SPB core at the nuclear envelope using integrated experimental restraints. Figure1 distinguishes three plaques and two intermediate layers; the study does not make all modeled subunit contacts direct observations. |
| ring-taxon | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=4932,559292; Species record | supports | Native NCBI taxonomy identifies4932 as Saccharomyces cerevisiae. |
| review-full | https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function; Public author manuscript, Introduction/SPB Structure pp5–6 and core/meiotic context | supports | The cited review supports the S. cerevisiae reference system and membrane-spanning central plaque, separate from inner/outer plaques and intermediate layers. It is review-level synthesis, not a new experiment. |
| record | data/structures/cytoskeleton/central_plaque_of_spindle_pole_body.yaml; Entire maintained target | context_only | Read exact identity, parthood, species/example, two topology edges, boundary discussion and component TODO. No protein census, function, measurement, image or trait-link claim is asserted. |
| identity-search | data/structures/cytoskeleton/central_plaque_of_spindle_pole_body.yaml; Ignored-inclusive identifier search across data/structures | context_only | Only this record declares GO0005823. |
| schema-result | just validate data/structures/cytoskeleton/central_plaque_of_spindle_pole_body.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/central_plaque_of_spindle_pole_body.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/central_plaque_of_spindle_pole_body.yaml --out /private/tmp/cellstructure-batch5-20261020-aEelh1/central_plaque_of_spindle_pole_body-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/central_plaque_of_spindle_pole_body.yaml --out /private/tmp/cellstructure-batch5-20261020-aEelh1/central_plaque_of_spindle_pole_body-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch5-20261020-aEelh1/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch5-20261020-aEelh1/central_plaque_of_spindle_pole_body-strict.tsv |
| target-curies | just check-curies-strict; data/structures/cytoskeleton/central_plaque_of_spindle_pole_body.yaml; exact collect() scope | supports | 8 of8 collected target identifiers returned OK at the unchanged base. Residuals: none. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- The component boundary is explicitly unfinished; the record is not a complete SPB-core protein census.
- Three principal plaques does not exclude intermediate layers IL1/IL2.
- COMMON denotes a characterized cell-cycle structure in the model species rather than measured prevalence or universal fungal architecture.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Only the review bundle is saved. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T063737Z-central-plaque-of-spindle-pole-body-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: General spindle-pole-body central-plaque evidence review
started_at: '2026-10-21T06:36:41Z'
finished_at: '2026-10-21T06:37:37Z'
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
summary: Exact central-plaque identity, SPB parthood, species example and both topology
  edges are supported. No concrete curation defect was found.
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
  - path: data/structures/cytoskeleton/central_plaque_of_spindle_pole_body.yaml
    sha256: b81ebcb1048c0454cde531ad51c3b0df92769b6c7236e07012ce9e3cef369527
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
- target_id: GO:0005823
  path: data/structures/cytoskeleton/central_plaque_of_spindle_pole_body.yaml
  label: central plaque of spindle pole body
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/central_plaque_of_spindle_pole_body.yaml
    role: maintained scientific record
scope:
  description: Entire maintained general central-plaque record; native ontology/taxonomy,
    cited identities, relevant2017 primary-study text and2004 public author manuscript.
  selection: Seventh remaining unreviewed path in batch5, in repository path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0005823
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0005823
  command: just validate data/structures/cytoskeleton/central_plaque_of_spindle_pole_body.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0005823
  command: just validate-strict data/structures/cytoskeleton/central_plaque_of_spindle_pole_body.yaml
    --out /private/tmp/cellstructure-batch5-20261020-aEelh1/central_plaque_of_spindle_pole_body-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0005823
  summary: 8 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0005823
  summary: No gene, regulator or expression-module assertion occurs in this target;
    structural and ontology evidence addresses the claims.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0005823
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - central-plaque-go
  - mitotic-plaque-epmc
  - mitotic-plaque-paper
  - ring-taxon
  - review-full
  - record
  - identity-search
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0005823
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
  - GO:0005823
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
  - GO:0005823
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
  - GO:0005823
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
  - GO:0005823
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
- evidence_id: central-plaque-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005823,GO:0005816,GO:0005635,GO:0005822,GO:0005824
  locator: Five native definitions and child relations
  accessed_at: '2026-10-21T06:37:06.647233Z'
  support: supports
  summary: All five terms are active. GO0005823 exactly matches the definition; GO0005816
    lists it as part_of. Inner and outer plaques have distinct nuclear/cytoplasmic
    positions, while the central plaque is envelope-embedded.
  snapshot_sha256: 3f75dad510f4d35c9eadfc7307d905ef461144b60992d3386c92f78c818463b6
- evidence_id: mitotic-plaque-epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1146/annurev.cellbio.20.022003.114106%20OR%20DOI:10.1091/mbc.E17-06-0397&format=json&resultType=core
  locator: Exact bibliographic identities
  accessed_at: '2026-10-20T07:38:16.397203Z'
  support: supports
  summary: Both cited DOI/title pairs match Jaspersen/Winey2004 and Viswanath2017.
  snapshot_sha256: c1324c0278e062e09f8737a5df93165c9b1cb749c51ea2b06f5101e9eb4787bb
- evidence_id: mitotic-plaque-paper
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5687031.1/PMC5687031.1.xml
  locator: Introduction, core Results and model-validation sections, Figure1 caption
    and modeling Discussion
  accessed_at: '2026-10-20T07:38:52.830471Z'
  support: supports
  summary: The2017 primary study models the S. cerevisiae SPB core at the nuclear
    envelope using integrated experimental restraints. Figure1 distinguishes three
    plaques and two intermediate layers; the study does not make all modeled subunit
    contacts direct observations.
  snapshot_sha256: 004836a027b7fad21def4f6e9eebc94ec5f1e07679d123407a062241f6edb580
- evidence_id: ring-taxon
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=4932,559292
  locator: Species record
  accessed_at: '2026-10-20T07:26:49.146723Z'
  support: supports
  summary: Native NCBI taxonomy identifies4932 as Saccharomyces cerevisiae.
  snapshot_sha256: a0110fd4b27dc6aa4f9c3ae5db622f12e6d58f6309580788781290225ca768bb
- evidence_id: review-full
  kind: primary_source
  reference: https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function
  locator: Public author manuscript, Introduction/SPB Structure pp5–6 and core/meiotic
    context
  accessed_at: '2026-10-21T06:37:37Z'
  support: supports
  summary: The cited review supports the S. cerevisiae reference system and membrane-spanning
    central plaque, separate from inner/outer plaques and intermediate layers. It
    is review-level synthesis, not a new experiment.
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/central_plaque_of_spindle_pole_body.yaml
  locator: Entire maintained target
  accessed_at: '2026-10-21T06:37:37Z'
  support: context_only
  summary: Read exact identity, parthood, species/example, two topology edges, boundary
    discussion and component TODO. No protein census, function, measurement, image
    or trait-link claim is asserted.
- evidence_id: identity-search
  kind: record_content
  reference: data/structures/cytoskeleton/central_plaque_of_spindle_pole_body.yaml
  locator: Ignored-inclusive identifier search across data/structures
  accessed_at: '2026-10-21T06:37:37Z'
  support: context_only
  summary: Only this record declares GO0005823.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/central_plaque_of_spindle_pole_body.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T06:36:43Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/central_plaque_of_spindle_pole_body.yaml'
  snapshot_sha256: 65cbd11495a67637c7c3a3b1f239237e0ffebf5a77a955dacffe426e8e553f75
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/central_plaque_of_spindle_pole_body.yaml
    --out /private/tmp/cellstructure-batch5-20261020-aEelh1/central_plaque_of_spindle_pole_body-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T06:36:45Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/central_plaque_of_spindle_pole_body.yaml\
    \ --out /private/tmp/cellstructure-batch5-20261020-aEelh1/central_plaque_of_spindle_pole_body-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch5-20261020-aEelh1/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch5-20261020-aEelh1/central_plaque_of_spindle_pole_body-strict.tsv"
  snapshot_sha256: 3896ca669a9414790b05ac3c1c08451c15d6112b83c5cfab4b1260c5e7ceabd7
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/central_plaque_of_spindle_pole_body.yaml;
    exact collect() scope
  accessed_at: '2026-10-21T06:37:37Z'
  support: supports
  summary: '8 of8 collected target identifiers returned OK at the unchanged base.
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
  topic: General envelope-embedded central plaque
  outcome: supported
  target_ids:
  - GO:0005823
  summary: The target matches GO and the sources, distinct from the mitotic subtype
    and adjacent plaques.
  evidence_ids:
  - central-plaque-go
  - mitotic-plaque-paper
  - review-full
  - record
- assessment_id: parthood
  area: grounding
  topic: Component of the SPB
  outcome: supported
  target_ids:
  - GO:0005823
  summary: Native GO confirms part_of; the record does not miscast containment as
    subtype.
  evidence_ids:
  - central-plaque-go
  - record
- assessment_id: definition
  area: evidence
  topic: Principal-plaque terminology
  outcome: supported
  target_ids:
  - GO:0005823
  summary: The exact ontology definition is supported by the review. Three principal
    plaques does not exclude the additional intermediate layers discussed by the sources.
  evidence_ids:
  - central-plaque-go
  - mitotic-plaque-paper
  - review-full
- assessment_id: taxa
  area: scope
  topic: S. cerevisiae model
  outcome: supported
  target_ids:
  - GO:0005823
  summary: The cited literature supports the named species and canonical architecture.
    COMMON is not a prevalence estimate or a claim that all fungi share identical
    plaque architecture.
  evidence_ids:
  - ring-taxon
  - mitotic-plaque-paper
  - review-full
  - record
- assessment_id: graph
  area: graph
  topic: Two coarse topology relationships
  outcome: supported
  target_ids:
  - GO:0005823
  summary: SPB parthood and envelope embedding are directly supported. NONMECHANISTIC
    preserves the difference from a detailed assembly model.
  evidence_ids:
  - central-plaque-go
  - mitotic-plaque-paper
  - record
- assessment_id: composition
  area: completeness
  topic: Acknowledged constituent follow-up
  outcome: supported
  target_ids:
  - GO:0005823
  summary: Known core proteins occur in the cited literature, but this target makes
    no exhaustive composition claim. The open TODO is a limitation; no required component
    field or unsupported identity was found.
  evidence_ids:
  - mitotic-plaque-paper
  - review-full
  - record
- assessment_id: status
  area: provenance
  topic: Proposed record and maintained ownership
  outcome: supported
  target_ids:
  - GO:0005823
  summary: The record preserves PROPOSED status and its boundary discussions are coherent.
    Scientific follow-up belongs in maintained YAML with native curation/history gates.
  evidence_ids:
  - record
  - central-plaque-go
findings: []
actions: []
limitations:
- The component boundary is explicitly unfinished; the record is not a complete SPB-core
  protein census.
- Three principal plaques does not exclude intermediate layers IL1/IL2.
- COMMON denotes a characterized cell-cycle structure in the model species rather
  than measured prevalence or universal fungal architecture.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- Only the review bundle is saved. Maintained scientific content, native status, history
  and generated pages remain unchanged.
```
