# bacterial-type flagellum basal body: disposition scope correction

- Review: 20261010T204021Z-flagellum-basal-body-disposition-correction
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-10T20:40:14Z
- Finished UTC: 2026-10-10T20:40:21Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

Provenance-only correction of one resolved finding explanation. No new literature review, native edit, status promotion, or additional scientific finding is claimed.

## Scope And Provenance

Correct the cross-record scope statement for one existing resolved finding; retain all other observations and limitations.

Selection: Exact enclosing-record disposition
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3cab39043f2cb72283ebd43593d8ccd59924b2e9.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0009425 | data/structures/appendage/bacterial_type_flagellum_basal_body.yaml | maintained | bacterial-type flagellum basal body |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| qc post-curation check | passed | True | GO:0009425 | Reused successful full QC at 3cab39043f2cb72283ebd43593d8ccd59924b2e9 for unchanged maintained/generated inputs. This does not claim that the newly added review documents were in that CI run. |

## Scientific And Domain Assessments

### Separate enclosing-structure and individual-component corrections

provenance: supported. Targets: GO:0009425.

The enclosing C-ring component remains CONDITIONAL with the experimental FliI-overproduction and nonmotility limits. That enclosing-record edit did not automatically reclassify individual proteins. Separately, issue #2135 changed FliM/FliN in the standalone C-ring record after individual reassessment; FliG remained ESSENTIAL. This corrects the prior disposition wording, not the scientific resolution.

## Findings

### F1: Qualify C-ring assembly essentiality

major / resolved / confirmed; issue key: flagellar-basal-body-c-ring-assembly-condition.

The enclosing C-ring component remains CONDITIONAL with the experimental FliI-overproduction and nonmotility limits. That enclosing-record edit did not automatically reclassify individual proteins. Separately, issue #2135 changed FliM/FliN in the standalone C-ring record after individual reassessment; FliG remained ESSENTIAL. This corrects the prior disposition wording, not the scientific resolution.

Disposition: The enclosing C-ring component remains CONDITIONAL with the experimental FliI-overproduction and nonmotility limits. That enclosing-record edit did not automatically reclassify individual proteins. Separately, issue #2135 changed FliM/FliN in the standalone C-ring record after individual reassessment; FliG remained ESSENTIAL. This corrects the prior disposition wording, not the scientific resolution.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/bacterial_type_flagellum_basal_body.yaml; Component essentiality or linked disposition scope | supports | The enclosing component remains condition-bound; its supported scientific fix is unchanged. |
| c-ring-record | data/structures/appendage/bacterial_type_flagellum_basal_body_c_ring.yaml; Component essentiality or linked disposition scope | supports | The separate record now marks FliM and FliN CONDITIONAL, while FliG remains ESSENTIAL. |
| prior-disposition | reviews/structured/20261010T203739Z-flagellum-basal-body-disposition/review.yaml; Component essentiality or linked disposition scope | supports | The prior explanation incorrectly says the separate constituents were not reclassified. The bundle is retained unchanged. |
| c-ring-disposition | reviews/structured/20261010T203754Z-flagellum-c-ring-disposition/review.yaml; Component essentiality or linked disposition scope | supports | F3 documents the separately assessed and resolved individual-component change under #2135. |

## Limits And Additional Notes

- This is a provenance-only correction, not another scientific assessment. Other findings retain their exact preceding dispositions.
- The original review limitations remain, including the unavailable whole-flagellum diameter source. No historical review was overwritten.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T204021Z-flagellum-basal-body-disposition-correction
kind: record
repository: CultureBotAI/CellStructureMech
title: 'bacterial-type flagellum basal body: disposition scope correction'
started_at: '2026-10-10T20:40:14Z'
finished_at: '2026-10-10T20:40:21Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same agent reassesses its authorized curation against inspected
    evidence; not independent human review.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: false
summary: Provenance-only correction of one resolved finding explanation. No new literature
  review, native edit, status promotion, or additional scientific finding is claimed.
source:
  git_revision: 3cab39043f2cb72283ebd43593d8ccd59924b2e9
  state: working_tree
  inputs:
  - path: data/structures/appendage/bacterial_type_flagellum_basal_body.yaml
    sha256: b73592ad4ea2dc9ea818266c440fb1e8e8070461592051cc9fa5c9c0c2a5c704
    role: target
  - path: data/structures/appendage/bacterial_type_flagellum_basal_body_c_ring.yaml
    sha256: 844cba3c5b9efc3f1d498f44f0036b0d94371e3975349942e6a69204b7911dbd
    role: context
  - path: docs/record-review-profile.md
    sha256: 6a49c8d35f0a94082a9ad0b8bd8c6a929d85de8339141955f3779bd7ab0eb7e4
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: reviews/structured/20261010T203739Z-flagellum-basal-body-disposition/review.yaml
    sha256: 4f1f804b41a3469df1e5f74eaaf7aad25a342a1478d460dd11a85a7eeb461a20
    role: context
  - path: reviews/structured/20261010T203754Z-flagellum-c-ring-disposition/review.yaml
    sha256: 177b8e836a27ca358cdb4334ac7646e964a62b4d69d25c3b2a51a232cf5a9e86
    role: context
targets:
- target_id: GO:0009425
  path: data/structures/appendage/bacterial_type_flagellum_basal_body.yaml
  label: bacterial-type flagellum basal body
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_basal_body.yaml
    role: maintained scientific record
scope:
  description: Correct the cross-record scope statement for one existing resolved
    finding; retain all other observations and limitations.
  selection: Exact enclosing-record disposition
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0009425
checks:
- check_id: qc
  name: qc post-curation check
  status: passed
  required: true
  target_ids:
  - GO:0009425
  command: gh run view 38084106846 --json headSha,status,conclusion,jobs
  exit_code: 0
  expected_exit_code: 0
  summary: Reused successful full QC at 3cab39043f2cb72283ebd43593d8ccd59924b2e9 for
    unchanged maintained/generated inputs. This does not claim that the newly added
    review documents were in that CI run.
  scope_note: 2026-10-10T20:36:26.166190+00:00 to 2026-10-10T20:36:32.396762+00:00;
    log SHA-256 3257c203664bc81d236e139d08b0da071b62b645608baaa5c4ef54e8cb65d631
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/appendage/bacterial_type_flagellum_basal_body.yaml
  locator: Component essentiality or linked disposition scope
  accessed_at: '2026-10-10T20:40:21Z'
  support: supports
  snapshot_sha256: b73592ad4ea2dc9ea818266c440fb1e8e8070461592051cc9fa5c9c0c2a5c704
  summary: The enclosing component remains condition-bound; its supported scientific
    fix is unchanged.
- evidence_id: c-ring-record
  kind: record_content
  reference: data/structures/appendage/bacterial_type_flagellum_basal_body_c_ring.yaml
  locator: Component essentiality or linked disposition scope
  accessed_at: '2026-10-10T20:40:21Z'
  support: supports
  snapshot_sha256: 844cba3c5b9efc3f1d498f44f0036b0d94371e3975349942e6a69204b7911dbd
  summary: The separate record now marks FliM and FliN CONDITIONAL, while FliG remains
    ESSENTIAL.
- evidence_id: prior-disposition
  kind: record_content
  reference: reviews/structured/20261010T203739Z-flagellum-basal-body-disposition/review.yaml
  locator: Component essentiality or linked disposition scope
  accessed_at: '2026-10-10T20:40:21Z'
  support: supports
  snapshot_sha256: 4f1f804b41a3469df1e5f74eaaf7aad25a342a1478d460dd11a85a7eeb461a20
  summary: The prior explanation incorrectly says the separate constituents were not
    reclassified. The bundle is retained unchanged.
- evidence_id: c-ring-disposition
  kind: record_content
  reference: reviews/structured/20261010T203754Z-flagellum-c-ring-disposition/review.yaml
  locator: Component essentiality or linked disposition scope
  accessed_at: '2026-10-10T20:40:21Z'
  support: supports
  snapshot_sha256: 177b8e836a27ca358cdb4334ac7646e964a62b4d69d25c3b2a51a232cf5a9e86
  summary: 'F3 documents the separately assessed and resolved individual-component
    change under #2135.'
assessments:
- assessment_id: scope-correction
  area: provenance
  topic: Separate enclosing-structure and individual-component corrections
  outcome: supported
  target_ids:
  - GO:0009425
  evidence_ids:
  - record
  - c-ring-record
  - prior-disposition
  - c-ring-disposition
  summary: 'The enclosing C-ring component remains CONDITIONAL with the experimental
    FliI-overproduction and nonmotility limits. That enclosing-record edit did not
    automatically reclassify individual proteins. Separately, issue #2135 changed
    FliM/FliN in the standalone C-ring record after individual reassessment; FliG
    remained ESSENTIAL. This corrects the prior disposition wording, not the scientific
    resolution.'
findings:
- finding_id: F1
  issue_key: flagellar-basal-body-c-ring-assembly-condition
  category: evidence
  severity: major
  status: resolved
  certainty: confirmed
  title: Qualify C-ring assembly essentiality
  description: 'The enclosing C-ring component remains CONDITIONAL with the experimental
    FliI-overproduction and nonmotility limits. That enclosing-record edit did not
    automatically reclassify individual proteins. Separately, issue #2135 changed
    FliM/FliN in the standalone C-ring record after individual reassessment; FliG
    remained ESSENTIAL. This corrects the prior disposition wording, not the scientific
    resolution.'
  target_ids:
  - GO:0009425
  field_paths:
  - components[1].essentiality
  evidence_ids:
  - record
  - c-ring-record
  - prior-disposition
  - c-ring-disposition
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_basal_body.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#components
  native_severity: major
  normalization_reason: Material evidence/scope defect under the native rubric.
  disposition_reason: 'The enclosing C-ring component remains CONDITIONAL with the
    experimental FliI-overproduction and nonmotility limits. That enclosing-record
    edit did not automatically reclassify individual proteins. Separately, issue #2135
    changed FliM/FliN in the standalone C-ring record after individual reassessment;
    FliG remained ESSENTIAL. This corrects the prior disposition wording, not the
    scientific resolution.'
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261010T203739Z-flagellum-basal-body-disposition
    finding_id: F3
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2132
  - https://github.com/CultureBotAI/CellStructureMech/issues/2136
actions: []
limitations:
- This is a provenance-only correction, not another scientific assessment. Other findings
  retain their exact preceding dispositions.
- The original review limitations remain, including the unavailable whole-flagellum
  diameter source. No historical review was overwritten.
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261010T203739Z-flagellum-basal-body-disposition
  relationship: corrects one disposition explanation, preserving its resolved status
- repository: CultureBotAI/CellStructureMech
  review_id: 20261010T203754Z-flagellum-c-ring-disposition
  relationship: distinguishes the separate FliM/FliN resolution
```
