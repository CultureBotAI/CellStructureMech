# Attachment organelle: gliding mechanism and imaging evidence

- Review: 20261010T075315Z-attachment-gliding-evidence
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-10T07:46:35Z
- Finished UTC: 2026-10-10T07:53:15Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One confirmed overstatement of mechanistic certainty and imaging context. This is a bounded finding, not a complete record review.

## Scope And Provenance

Full YAML read; scientific assessment limited to identity and the gliding function plus its cited mechanism evidence.

Selection: Exact attachment_organelle.yaml, not a corpus sample.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ab85e79339bef69350636de06a070cde22e0f8b9.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0033099 | data/structures/appendage/attachment_organelle.yaml | maintained | attachment organelle |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| pre-schema | passed | True | GO:0033099 | Fresh local check passed on the pre-curation target. |
| pre-strict | passed | True | GO:0033099 | Fresh local check passed on the pre-curation target. |
| baseline-qc | passed | True | GO:0033099 | Authoritative QC, including schema, tests, history, generated-site and text-map checks: verified completed/success at the exact unchanged source revision ab85e79339bef69350636de06a070cde22e0f8b9. |
| baseline-labels | passed | True | GO:0033099 | Enforced full-corpus identifier/label correspondence: verified completed/success at the exact unchanged source revision ab85e79339bef69350636de06a070cde22e0f8b9. |
| baseline-identifiers-traits | passed | True | GO:0033099 | Resolver self-test, full identifier liveness and trait-link check: verified completed/success at the exact unchanged source revision ab85e79339bef69350636de06a070cde22e0f8b9. |
| Remaining scientific assessment | skipped | True | GO:0033099 | This observation assesses identity and gliding claim/evidence only. Remaining component essentiality, taxonomy and protein-example claims are not certified. |

## Scientific And Domain Assessments

### Exact structure identity

identity: supported. Targets: GO:0033099.

Whole polar organelle identity is appropriate; its motility function is retained.

### Mechanistic certainty and experimental context

evidence: concern. Targets: GO:0033099.

The cited structural data support a proposed coupling model, not demonstrated dynamic internal-core deformation.

### Other scientific claims

completeness: unknown. Targets: GO:0033099.

The pending whole-record review remains partial; no other claim is certified by this finding.

## Findings

### F1: Separate proposed deformation coupling from demonstrated gliding

major / open / confirmed; issue key: attachment-organelle-gliding-model-overclaim.

functions[1] asserts a core-deformation mechanism as established and describes static ECT as during gliding. The cited 2015/2016 studies propose this mechanism; the already-cited 2021 study reports a bounded negative test for large stepwise motion. Preserve gliding, qualify the model and correct imaging context.

## Recommended Actions And Acceptance Checks

### A1

Qualify deformation coupling as proposed, distinguish frozen ECT from real-time gliding and add the already-cited 2021 test to the narrow function evidence.

- Gliding remains an established organelle function; core-deformation coupling is labeled as a model.
- ECT is described as frozen-hydrated structural imaging, not live dynamic imaging.
- The 2021 failure to detect large steps is not generalized to absence of all conformational change.
- Use guarded writer, append both histories, preserve PROPOSED and pass native gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/attachment_organelle.yaml; Entire YAML read; functions[1].description and functions[1].evidence[0].notes | context_only | The function states core-deformation coupling as fact and describes ECT periodicity measurements as during gliding. |
| identity | https://www.ebi.ac.uk/QuickGO/term/GO:0033099; Cellular-component definition | supports | The exact term denotes the polar membrane extension with an internal cytoskeletal core, involved in adherence, gliding and division. |
| mapping-model | https://doi.org/10.1371/journal.ppat.1005299; Discussion: concluding gliding model; Fig. 6C | refutes | Protein localization supports architecture. The authors propose, rather than directly establish, force transmission and repeated extension/retraction coupling to adhesins. |
| frozen-ect | https://doi.org/10.1128/mBio.00243-16; Results: structural periodicities; Discussion: Possible gliding mechanism; Fig. 5; Methods: Electron cryotomography | refutes | ECT images frozen-hydrated cells at liquid-nitrogen temperature. Variation in structural periodicity motivates a proposed deformation model; it is not real-time imaging of deformation during gliding. The separate phase-contrast video documents cell movement. |
| ruler-test | https://doi.org/10.1371/journal.ppat.1009621; Results: gliding motility; Discussion; S7 Fig. | refutes | Length-engineered HMW2 supports a molecular ruler and length/speed association. Dual-color 50-Hz measurements in 20 cells did not detect large stepwise displacement. This limits, but does not disprove every possible small conformational motion. |
| rule | .claude/skills/curate-yaml-record/references/review-checklist.md; Functions/traits and causal-graph evidence standards | supports | Association must not become established mechanism; predictions remain labeled. |

## Limits And Additional Notes

- Other components, including P30 assembly essentiality, remain unassessed; the membrane target was read but has no completed verdict from this batch.
- No new full-corpus local QC was run before this observation: verified successful CI at the identical unchanged commit supplies baseline deterministic results. Fresh local gates follow the separately authorized fix.
- iModulonDB complete 28-dataset inventory was read; no Mycoplasma/Mycoplasmoides dataset applies. This is not negative biological evidence.
- Ignored and hidden files were included in searches across reviews, legacy record reports and history. Prior P1 essentiality findings are separate and remain resolved.
- No native scientific record or history changed before this issue-bearing observation was saved.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T075315Z-attachment-gliding-evidence
kind: record
repository: CultureBotAI/CellStructureMech
title: 'Attachment organelle: gliding mechanism and imaging evidence'
started_at: '2026-10-10T07:46:35Z'
finished_at: '2026-10-10T07:53:15Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same agent continuing the corpus audit and later implementing
    separately authorized fixes; no independent scientific sign-off.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: One confirmed overstatement of mechanistic certainty and imaging context.
  This is a bounded finding, not a complete record review.
source:
  git_revision: ab85e79339bef69350636de06a070cde22e0f8b9
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
    role: context
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/appendage/attachment_organelle.yaml
    sha256: 84aa1125628ddc73b95ae788333569da468344c9beb1cf99793363e65c492164
    role: target
  - path: docs/CURATION.md
    sha256: c3e482fbf381edcf0238e579648b779c3a8803a1d888b89397ad6fc8808dd07d
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
  - path: history/README.md
    sha256: 1636df44f28547f440242afcb4a05ac293b9714b4d7b809cecc30b975e44a522
    role: context
  - path: history/records/attachment_organelle/2026-09-06T150543Z-claude-459ee1.yaml
    sha256: cd0da0beec435828bc3ff1e604c42af6bff609c6509c346f0dc280ba19550a25
    role: context
  - path: history/records/attachment_organelle/2026-09-06T152541Z-claude-c2f4d9.yaml
    sha256: e4eb2edc91e2032dbf94dab07b8846bedbd06e19349f85d234d11c4b76986a39
    role: context
  - path: history/records/attachment_organelle/2026-10-10T070837Z-Codex-5596d4.yaml
    sha256: da925b58cbea8dcb7438ba3fab90de6415acd3a50bd49611d86800d5e1973497
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reviews/structured/20261010T070627Z-attachment-assembly/review.yaml
    sha256: a975e4dd0b75cda1322a6e18d16c5e2dd84bdaf5528dd5ab1d50b20ff112b0b0
    role: context
  - path: reviews/structured/20261010T072543Z-attachment-finding-dispositions/review.yaml
    sha256: 7815a953362800c676e7a92bfd22d4998184cdb2c47cd08f8c48c4b5b195ccc4
    role: context
  - path: scripts/run_qc.py
    sha256: eaabba8bf5c6a772b9749b865bbc76ccfe214070b44ce01eaf49b41c7ddf65a1
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: GO:0033099
  path: data/structures/appendage/attachment_organelle.yaml
  label: attachment organelle
  kind: maintained
  record_class: CellStructureRecord
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/attachment_organelle.yaml
    role: maintained scientific record
scope:
  description: Full YAML read; scientific assessment limited to identity and the gliding
    function plus its cited mechanism evidence.
  selection: Exact attachment_organelle.yaml, not a corpus sample.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - GO:0033099
checks:
- check_id: pre-schema
  name: pre-schema
  status: passed
  required: true
  target_ids:
  - GO:0033099
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/appendage/attachment_organelle.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Fresh local check passed on the pre-curation target.
  scope_note: 2026-10-10T07:51:39Z to 2026-10-10T07:51:49Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: pre-strict
  name: pre-strict
  status: passed
  required: true
  target_ids:
  - GO:0033099
  command: .venv/bin/python scripts/validate_strict.py data/structures/appendage/attachment_organelle.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Fresh local check passed on the pre-curation target.
  scope_note: 2026-10-10T07:51:49Z to 2026-10-10T07:51:58Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: baseline-qc
  name: baseline-qc
  status: passed
  required: true
  target_ids:
  - GO:0033099
  command: gh run view 38035131858 --json headSha,status,conclusion,jobs
  exit_code: 0
  expected_exit_code: 0
  summary: 'Authoritative QC, including schema, tests, history, generated-site and
    text-map checks: verified completed/success at the exact unchanged source revision
    ab85e79339bef69350636de06a070cde22e0f8b9.'
  scope_note: https://github.com/CultureBotAI/CellStructureMech/actions/runs/38035131858;
    reused baseline CI results, not a fresh local execution of its gates. Queried
    2026-10-10T07:50-07:52Z.
- check_id: baseline-labels
  name: baseline-labels
  status: passed
  required: true
  target_ids:
  - GO:0033099
  command: gh run view 38035131786 --json headSha,status,conclusion,jobs
  exit_code: 0
  expected_exit_code: 0
  summary: 'Enforced full-corpus identifier/label correspondence: verified completed/success
    at the exact unchanged source revision ab85e79339bef69350636de06a070cde22e0f8b9.'
  scope_note: https://github.com/CultureBotAI/CellStructureMech/actions/runs/38035131786;
    reused baseline CI results, not a fresh local execution of its gates. Queried
    2026-10-10T07:50-07:52Z.
- check_id: baseline-identifiers-traits
  name: baseline-identifiers-traits
  status: passed
  required: true
  target_ids:
  - GO:0033099
  command: gh run view 38035131860 --json headSha,status,conclusion,jobs
  exit_code: 0
  expected_exit_code: 0
  summary: 'Resolver self-test, full identifier liveness and trait-link check: verified
    completed/success at the exact unchanged source revision ab85e79339bef69350636de06a070cde22e0f8b9.'
  scope_note: https://github.com/CultureBotAI/CellStructureMech/actions/runs/38035131860;
    reused baseline CI results, not a fresh local execution of its gates. Queried
    2026-10-10T07:50-07:52Z.
- check_id: remaining-science
  name: Remaining scientific assessment
  status: skipped
  required: true
  target_ids:
  - GO:0033099
  summary: This observation assesses identity and gliding claim/evidence only. Remaining
    component essentiality, taxonomy and protein-example claims are not certified.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/appendage/attachment_organelle.yaml
  locator: Entire YAML read; functions[1].description and functions[1].evidence[0].notes
  accessed_at: '2026-10-10T07:53:15Z'
  snapshot_sha256: 84aa1125628ddc73b95ae788333569da468344c9beb1cf99793363e65c492164
  support: context_only
  summary: The function states core-deformation coupling as fact and describes ECT
    periodicity measurements as during gliding.
- evidence_id: identity
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/term/GO:0033099
  locator: Cellular-component definition
  accessed_at: '2026-10-10T07:47:55Z'
  snapshot_sha256: 7386b48d2989ab4eb1369b50a8f4fb75cc4fd7f1685e63842bacf75d5de52251
  support: supports
  summary: The exact term denotes the polar membrane extension with an internal cytoskeletal
    core, involved in adherence, gliding and division.
- evidence_id: mapping-model
  kind: primary_source
  reference: https://doi.org/10.1371/journal.ppat.1005299
  locator: 'Discussion: concluding gliding model; Fig. 6C'
  accessed_at: '2026-10-10T07:47:49Z'
  snapshot_sha256: eb873beb04aa5fe98c83fe843d0b7537b62ae2738115308ea9da521d1ed42557
  support: refutes
  summary: Protein localization supports architecture. The authors propose, rather
    than directly establish, force transmission and repeated extension/retraction
    coupling to adhesins.
- evidence_id: frozen-ect
  kind: primary_source
  reference: https://doi.org/10.1128/mBio.00243-16
  locator: 'Results: structural periodicities; Discussion: Possible gliding mechanism;
    Fig. 5; Methods: Electron cryotomography'
  accessed_at: '2026-10-10T07:47:54Z'
  snapshot_sha256: 7d579ad7ba828670d16c6e9e9a73c4a692a56d52366b08be6e97b59e0249f793
  support: refutes
  summary: ECT images frozen-hydrated cells at liquid-nitrogen temperature. Variation
    in structural periodicity motivates a proposed deformation model; it is not real-time
    imaging of deformation during gliding. The separate phase-contrast video documents
    cell movement.
- evidence_id: ruler-test
  kind: primary_source
  reference: https://doi.org/10.1371/journal.ppat.1009621
  locator: 'Results: gliding motility; Discussion; S7 Fig.'
  accessed_at: '2026-10-10T07:47:49Z'
  snapshot_sha256: a92f1eadb0b76bf1d95c011cfb51bbe9344f49ef56dcfd4787cacc822b971a6d
  support: refutes
  summary: Length-engineered HMW2 supports a molecular ruler and length/speed association.
    Dual-color 50-Hz measurements in 20 cells did not detect large stepwise displacement.
    This limits, but does not disprove every possible small conformational motion.
- evidence_id: rule
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Functions/traits and causal-graph evidence standards
  accessed_at: '2026-10-10T07:53:15Z'
  support: supports
  summary: Association must not become established mechanism; predictions remain labeled.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact structure identity
  outcome: supported
  target_ids:
  - GO:0033099
  evidence_ids:
  - record
  - identity
  summary: Whole polar organelle identity is appropriate; its motility function is
    retained.
- assessment_id: gliding
  area: evidence
  topic: Mechanistic certainty and experimental context
  outcome: concern
  target_ids:
  - GO:0033099
  evidence_ids:
  - record
  - mapping-model
  - frozen-ect
  - ruler-test
  - rule
  summary: The cited structural data support a proposed coupling model, not demonstrated
    dynamic internal-core deformation.
  dimensions:
  - name: experimental-context
    value: M. pneumoniae; protein mapping, frozen-hydrated ECT, and length-engineered
      HMW2 with live fluorescence tracking
    definition: Distinct methods and their scope; frozen structural observations are
      not real-time mechanism measurements.
    evidence_ids:
    - mapping-model
    - frozen-ect
    - ruler-test
- assessment_id: remaining
  area: completeness
  topic: Other scientific claims
  outcome: unknown
  target_ids:
  - GO:0033099
  evidence_ids:
  - record
  summary: The pending whole-record review remains partial; no other claim is certified
    by this finding.
findings:
- finding_id: F1
  issue_key: attachment-organelle-gliding-model-overclaim
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Separate proposed deformation coupling from demonstrated gliding
  description: functions[1] asserts a core-deformation mechanism as established and
    describes static ECT as during gliding. The cited 2015/2016 studies propose this
    mechanism; the already-cited 2021 study reports a bounded negative test for large
    stepwise motion. Preserve gliding, qualify the model and correct imaging context.
  target_ids:
  - GO:0033099
  field_paths:
  - functions[1].description
  - functions[1].evidence
  evidence_ids:
  - record
  - mapping-model
  - frozen-ect
  - ruler-test
  - rule
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/attachment_organelle.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md#field-by-field-audit
  native_severity: major
  normalization_reason: A mechanistic assertion exceeds the cited primary experiments;
    it is not merely stylistic wording.
actions:
- action_id: A1
  description: Qualify deformation coupling as proposed, distinguish frozen ECT from
    real-time gliding and add the already-cited 2021 test to the narrow function evidence.
  finding_ids:
  - F1
  target_ids:
  - GO:0033099
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/attachment_organelle.yaml
    role: maintained scientific record
  generator: just text-embeddings-refresh; just render
  acceptance_checks:
  - Gliding remains an established organelle function; core-deformation coupling is
    labeled as a model.
  - ECT is described as frozen-hydrated structural imaging, not live dynamic imaging.
  - The 2021 failure to detect large steps is not generalized to absence of all conformational
    change.
  - Use guarded writer, append both histories, preserve PROPOSED and pass native gates.
limitations:
- Other components, including P30 assembly essentiality, remain unassessed; the membrane
  target was read but has no completed verdict from this batch.
- 'No new full-corpus local QC was run before this observation: verified successful
  CI at the identical unchanged commit supplies baseline deterministic results. Fresh
  local gates follow the separately authorized fix.'
- iModulonDB complete 28-dataset inventory was read; no Mycoplasma/Mycoplasmoides
  dataset applies. This is not negative biological evidence.
- Ignored and hidden files were included in searches across reviews, legacy record
  reports and history. Prior P1 essentiality findings are separate and remain resolved.
- No native scientific record or history changed before this issue-bearing observation
  was saved.
```
