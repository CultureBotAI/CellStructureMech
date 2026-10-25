# Record review of static microtubule bundle (GO:0099070): curation_history[1] causal_graph ID mismatch

- Review: 20261025T071001Z-static-microtubule-bundle-reference-attribution
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-25T06:55:00Z
- Finished UTC: 2026-10-25T07:10:01Z
- Reviewer: antigravity-c3s4-record-review (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Static microtubule bundle (GO:0099070, data/structures/cytoskeleton/static_microtubule_bundle.yaml) has valid GO cellular-component identity, parent/part_of hierarchy (GO:0043209, GO:0005856, GO:0005874), and well-sourced alpha/beta-tubulin subunit composition (alpha_tubulin atb2/TUB1/TUB3 with UniProtKB:P04689, UniProtKB:P09733, UniProtKB:P09734; beta_tubulin nda3/TUB2 with UniProtKB:P05219, UniProtKB:P02557) across Schizosaccharomyces pombe and Saccharomyces cerevisiae supported by DOI:10.1083/jcb.201502025, DOI:10.1083/jcb.201306075, and DOI:10.7554/eLife.89958. One minor provenance discrepancy was identified: curation_history[1].changes (CURATED_CAUSAL_GRAPH) cites graph_id 'static_bundle_stabilization' whereas causal_graphs[0].graph_id is 'static_microtubule_bundle_organization'.

## Scope And Provenance

Single-record audit of static microtubule bundle (GO:0099070) covering identity, composition, citations, causal graphs, and curation history.

Selection: Targeted single-record review of new Cycle 3 Stage 1 record data/structures/cytoskeleton/static_microtubule_bundle.yaml.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 83ec9d5184fb203d87d8c3bd7043792d385193bf.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0099070 | data/structures/cytoskeleton/static_microtubule_bundle.yaml | maintained | static microtubule bundle |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| LinkML schema validation on static_microtubule_bundle.yaml | passed | True | GO:0099070 | No LinkML schema issues found for static_microtubule_bundle.yaml. |
| Strict instance validator on static_microtubule_bundle.yaml | passed | True | GO:0099070 | Zero strict validator errors on static_microtubule_bundle.yaml. |

## Scientific And Domain Assessments

### GO cellular-component identity and S. pombe / S. cerevisiae tubulin composition of static microtubule bundle (GO:0099070)

identity: supported. Targets: GO:0099070.

GO:0099070 identity, parent/part_of hierarchy, alpha/beta-tubulin subunit composition (atb2/TUB1/TUB3 and nda3/TUB2), and citations (DOI:10.1083/jcb.201502025, DOI:10.1083/jcb.201306075, DOI:10.7554/eLife.89958) are accurately grounded.

### Alignment between curation_history[1].changes and causal_graphs[0].graph_id

provenance: concern. Targets: GO:0099070.

curation_history[1].changes cites static_bundle_stabilization instead of causal_graphs[0].graph_id static_microtubule_bundle_organization.

## Findings

### F1: static_microtubule_bundle.yaml curation_history[1].changes cites graph_id static_bundle_stabilization instead of static_microtubule_bundle_organization

minor / open / confirmed; issue key: static-microtubule-bundle-curation-history-graph-id-mismatch.

In data/structures/cytoskeleton/static_microtubule_bundle.yaml (GO:0099070), curation_history[1].changes (action: CURATED_CAUSAL_GRAPH, lines 265-270) cites graph_id 'static_bundle_stabilization' whereas causal_graphs[0].graph_id (line 182) is 'static_microtubule_bundle_organization'.

## Recommended Actions And Acceptance Checks

### A1

Align curation_history[1].changes in data/structures/cytoskeleton/static_microtubule_bundle.yaml to causal_graphs[0].graph_id 'static_microtubule_bundle_organization' and record the update in history/records/static_microtubule_bundle/.

- .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/static_microtubule_bundle.yaml --out /tmp/static_mt_failures.tsv
- .venv/bin/python scripts/validate_history.py

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev_static_mt_history_graph_id | data/structures/cytoskeleton/static_microtubule_bundle.yaml; causal_graphs[0].graph_id (line 182) and curation_history[1].changes (lines 265-270) | supports | static_microtubule_bundle.yaml curation_history[1].changes cites graph_id 'static_bundle_stabilization' whereas causal_graphs[0].graph_id is 'static_microtubule_bundle_organization'. |
| ev_schema_static_mt | scripts/validate_strict.py; schema_static_mt receipt | supports | linkml-validate exited 0 on static_microtubule_bundle.yaml. |
| ev_strict_static_mt | scripts/validate_strict.py; strict_static_mt receipt | supports | validate_strict.py exited 0 on static_microtubule_bundle.yaml. |

## Limits And Additional Notes

- Record edits are deferred to Cycle 3 Stage 5 (resolve_review_findings) per the Stage 4 review-only workflow contract.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261025T071001Z-static-microtubule-bundle-reference-attribution
kind: record
repository: CultureBotAI/CellStructureMech
title: 'Record review of static microtubule bundle (GO:0099070): curation_history[1]
  causal_graph ID mismatch'
started_at: '2026-10-25T06:55:00Z'
finished_at: '2026-10-25T07:10:01Z'
reviewer:
  identity: antigravity-c3s4-record-review
  kind: agent
  model: claude-opus-4-6
  independence: independent
  independence_basis: Reviewed in Cycle 3 Stage 4 record_review against committed
    git revision 83ec9d5184fb203d87d8c3bd7043792d385193bf without record edits in
    this stage.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: PASS_WITH_FOLLOW_UP
scientific_review: true
summary: 'Static microtubule bundle (GO:0099070, data/structures/cytoskeleton/static_microtubule_bundle.yaml)
  has valid GO cellular-component identity, parent/part_of hierarchy (GO:0043209,
  GO:0005856, GO:0005874), and well-sourced alpha/beta-tubulin subunit composition
  (alpha_tubulin atb2/TUB1/TUB3 with UniProtKB:P04689, UniProtKB:P09733, UniProtKB:P09734;
  beta_tubulin nda3/TUB2 with UniProtKB:P05219, UniProtKB:P02557) across Schizosaccharomyces
  pombe and Saccharomyces cerevisiae supported by DOI:10.1083/jcb.201502025, DOI:10.1083/jcb.201306075,
  and DOI:10.7554/eLife.89958. One minor provenance discrepancy was identified: curation_history[1].changes
  (CURATED_CAUSAL_GRAPH) cites graph_id ''static_bundle_stabilization'' whereas causal_graphs[0].graph_id
  is ''static_microtubule_bundle_organization''.'
source:
  git_revision: 83ec9d5184fb203d87d8c3bd7043792d385193bf
  state: git_commit
  inputs:
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
    role: context
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: conf/record_review.yaml
    sha256: d3334a12b8a616a7638f1195748085d2b543fba7df67ad4ff8fcc0ac18f2d3ee
    role: context
  - path: data/structures/cytoskeleton/static_microtubule_bundle.yaml
    sha256: 7b57f98c5e8037cbf1e6848a40f75f9fe6e5b5b0e2fc62d503e17dd58002a24d
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
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
scope:
  description: Single-record audit of static microtubule bundle (GO:0099070) covering
    identity, composition, citations, causal graphs, and curation history.
  selection: Targeted single-record review of new Cycle 3 Stage 1 record data/structures/cytoskeleton/static_microtubule_bundle.yaml.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0099070
targets:
- target_id: GO:0099070
  path: data/structures/cytoskeleton/static_microtubule_bundle.yaml
  label: static microtubule bundle
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 7b57f98c5e8037cbf1e6848a40f75f9fe6e5b5b0e2fc62d503e17dd58002a24d
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/static_microtubule_bundle.yaml
    role: maintained_record
checks:
- check_id: schema_static_mt
  name: LinkML schema validation on static_microtubule_bundle.yaml
  status: passed
  required: true
  summary: No LinkML schema issues found for static_microtubule_bundle.yaml.
  target_ids:
  - GO:0099070
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/static_microtubule_bundle.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_schema_static_mt
- check_id: strict_static_mt
  name: Strict instance validator on static_microtubule_bundle.yaml
  status: passed
  required: true
  summary: Zero strict validator errors on static_microtubule_bundle.yaml.
  target_ids:
  - GO:0099070
  command: .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/static_microtubule_bundle.yaml
    --out /tmp/static_mt_validation_failures.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_strict_static_mt
evidence:
- evidence_id: ev_static_mt_history_graph_id
  kind: record_content
  reference: data/structures/cytoskeleton/static_microtubule_bundle.yaml
  locator: causal_graphs[0].graph_id (line 182) and curation_history[1].changes (lines
    265-270)
  accessed_at: '2026-10-25T07:00:00Z'
  support: supports
  summary: static_microtubule_bundle.yaml curation_history[1].changes cites graph_id
    'static_bundle_stabilization' whereas causal_graphs[0].graph_id is 'static_microtubule_bundle_organization'.
  quote: "- timestamp: '2026-10-24T06:00:00Z'\n  curator: antigravity\n  action: CURATED_CAUSAL_GRAPH\n\
    \  changes: Added alpha_tubulin -> beta_tubulin heterodimerization edge in static_bundle_stabilization\n\
    \    (DOI:10.1083/jcb.201502025, DOI:10.7554/eLife.89958).\n  llm_assisted: true"
  snapshot_sha256: 7b57f98c5e8037cbf1e6848a40f75f9fe6e5b5b0e2fc62d503e17dd58002a24d
- evidence_id: ev_schema_static_mt
  kind: validation
  reference: scripts/validate_strict.py
  locator: schema_static_mt receipt
  accessed_at: '2026-10-25T07:10:01Z'
  support: supports
  summary: linkml-validate exited 0 on static_microtubule_bundle.yaml.
  snapshot_sha256: de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- evidence_id: ev_strict_static_mt
  kind: validation
  reference: scripts/validate_strict.py
  locator: strict_static_mt receipt
  accessed_at: '2026-10-25T07:10:01Z'
  support: supports
  summary: validate_strict.py exited 0 on static_microtubule_bundle.yaml.
  snapshot_sha256: 4068e2e0b74bf07bf0713fa15cc7ac6be42b2386484f2a72e6e2fdf56e31dd88
assessments:
- assessment_id: assess_static_mt_identity
  area: identity
  topic: GO cellular-component identity and S. pombe / S. cerevisiae tubulin composition
    of static microtubule bundle (GO:0099070)
  outcome: supported
  summary: GO:0099070 identity, parent/part_of hierarchy, alpha/beta-tubulin subunit
    composition (atb2/TUB1/TUB3 and nda3/TUB2), and citations (DOI:10.1083/jcb.201502025,
    DOI:10.1083/jcb.201306075, DOI:10.7554/eLife.89958) are accurately grounded.
  target_ids:
  - GO:0099070
  evidence_ids:
  - ev_schema_static_mt
  - ev_strict_static_mt
- assessment_id: assess_static_mt_history_graph_id
  area: provenance
  topic: Alignment between curation_history[1].changes and causal_graphs[0].graph_id
  outcome: concern
  summary: curation_history[1].changes cites static_bundle_stabilization instead of
    causal_graphs[0].graph_id static_microtubule_bundle_organization.
  target_ids:
  - GO:0099070
  evidence_ids:
  - ev_static_mt_history_graph_id
findings:
- finding_id: F1
  issue_key: static-microtubule-bundle-curation-history-graph-id-mismatch
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: static_microtubule_bundle.yaml curation_history[1].changes cites graph_id
    static_bundle_stabilization instead of static_microtubule_bundle_organization
  description: 'In data/structures/cytoskeleton/static_microtubule_bundle.yaml (GO:0099070),
    curation_history[1].changes (action: CURATED_CAUSAL_GRAPH, lines 265-270) cites
    graph_id ''static_bundle_stabilization'' whereas causal_graphs[0].graph_id (line
    182) is ''static_microtubule_bundle_organization''.'
  target_ids:
  - GO:0099070
  field_paths:
  - curation_history[1].changes
  - causal_graphs[0].graph_id
  evidence_ids:
  - ev_static_mt_history_graph_id
  rule_id: docs/CURATION.md:curation-history-accuracy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/static_microtubule_bundle.yaml
    role: maintained_record
  tags:
  - provenance
  - curation-history
  - causal-graphs
  - stage4-record-review
actions:
- action_id: A1
  description: Align curation_history[1].changes in data/structures/cytoskeleton/static_microtubule_bundle.yaml
    to causal_graphs[0].graph_id 'static_microtubule_bundle_organization' and record
    the update in history/records/static_microtubule_bundle/.
  finding_ids:
  - F1
  target_ids:
  - GO:0099070
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/static_microtubule_bundle.yaml
    role: maintained_record
  acceptance_checks:
  - .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/static_microtubule_bundle.yaml
    --out /tmp/static_mt_failures.tsv
  - .venv/bin/python scripts/validate_history.py
limitations:
- Record edits are deferred to Cycle 3 Stage 5 (resolve_review_findings) per the Stage
  4 review-only workflow contract.
tags:
- stage4
- record-review
- static-microtubule-bundle
```
