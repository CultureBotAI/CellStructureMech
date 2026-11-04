# Record review of Woronin body (GO:0140266): missing repository-level history ledger

- Review: 20261023T091801Z-woronin-body-missing-history
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-23T09:10:00Z
- Finished UTC: 2026-10-23T09:18:01Z
- Reviewer: antigravity-stage4-record-review (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Woronin body (GO:0140266, data/structures/membrane_organelle/woronin_body.yaml) has accurate peroxisome-derived dense-core organelle identity, Pezizomycotina taxonomic scope, HEX-1 and WSC component grounding, verified Neurospora crassa OR74A UniProtKB protein examples (P87252, Q7S4P4), and source-backed septal-pore plugging and cortical-tethering causal graphs. However, it is the only record among all 978 corpus records that lacks a repository-level curation history directory and YAML ledger under history/records/woronin_body/, violating CLAUDE.md rule 8.

## Scope And Provenance

Single-record audit of Woronin body (GO:0140266) covering identity, composition, causal graphs, evidence, and repository-level history provenance.

Selection: Targeted single-record review after whole-corpus audit identified Woronin body as the sole record lacking a history/records/&lt;stem&gt;/ ledger.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 13c6b0d85338aa96d330b8d699587dfe270a21f9.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0140266 | data/structures/membrane_organelle/woronin_body.yaml | maintained | Woronin body |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| LinkML schema validation on woronin_body.yaml | passed | True | GO:0140266 | No LinkML schema issues found for woronin_body.yaml. |
| Strict instance validator on woronin_body.yaml | passed | True | GO:0140266 | Zero strict validator errors or warnings on woronin_body.yaml. |
| Repository-level history validation | passed | True | GO:0140266 | Existing 1903 history files validate, but validate_history.py does not check 1:1 coverage from data/structures/**/*.yaml to history/records/&lt;stem&gt;/. |

## Scientific And Domain Assessments

### Identity, hierarchy, composition, causal graphs, and evidence of Woronin body (GO:0140266)

identity: supported. Targets: GO:0140266.

Identity (GO:0140266), parent/part_of hierarchy (GO:0043231, GO:0005737), HEX-1 and WSC components, N. crassa OR74A UniProtKB protein examples, and assembly/function causal graphs are accurately grounded and supported by cited primary literature.

### Repository-level curation history coverage under history/records/woronin_body/

provenance: concern. Targets: GO:0140266.

woronin_body.yaml is the only record out of 978 in data/structures/ without a corresponding history/records/&lt;stem&gt;/ ledger directory.

## Findings

### F1: woronin_body.yaml is missing its repository-level history ledger under history/records/woronin_body/

minor / open / confirmed; issue key: woronin-body-missing-history.

data/structures/membrane_organelle/woronin_body.yaml contains 4 inline curation_history entries (created in commit a220d8400268740afc59decc917820cfa60f8008 on 2026-09-12 and updated through 2026-10-18), but has zero repository-level history YAML files under history/records/woronin_body/. Every other record in the 978-record corpus (977/978) has at least one repository-level history file under history/records/&lt;stem&gt;/.

## Recommended Actions And Acceptance Checks

### A1

Create a backfill CurationEvent YAML ledger under history/records/woronin_body/ recording the git-verified provenance of data/structures/membrane_organelle/woronin_body.yaml and validate with scripts/validate_history.py.

- test -d history/records/woronin_body
- .venv/bin/python scripts/validate_history.py

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev_woronin_record | data/structures/membrane_organelle/woronin_body.yaml; lines 1-249 | supports | Inspecting woronin_body.yaml confirms accurate GO:0140266 identity, Pezizomycotina scope, HEX-1/WSC components with N. crassa OR74A UniProtKB examples, and source-backed causal graphs. |
| ev_woronin_curation_history | data/structures/membrane_organelle/woronin_body.yaml; curation_history[0..3] (lines 11-36) vs history/records/ | supports | woronin_body.yaml records 4 inline curation_history events (CREATED_RECORD on 2026-09-12T10:15:23Z through EDIT on 2026-10-18T05:29:52Z), yet no history/records/woronin_body/ directory exists in the repository. |
| ev_schema_woronin | scripts/validate_strict.py; schema_woronin receipt | supports | linkml-validate exited 0 on woronin_body.yaml. |
| ev_strict_woronin | scripts/validate_strict.py; strict_woronin receipt | supports | validate_strict.py exited 0 on woronin_body.yaml. |
| ev_history_validator | scripts/validate_history.py; history receipt | context_only | validate_history.py validates 1903 existing history YAML files but does not check whether any data/structures/**/*.yaml record lacks a history/records/&lt;stem&gt;/ directory. |

## Limits And Additional Notes

- Repository-level history ledger under history/records/woronin_body/ is currently absent and queued for Stage 5 remediation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261023T091801Z-woronin-body-missing-history
kind: record
repository: CultureBotAI/CellStructureMech
title: 'Record review of Woronin body (GO:0140266): missing repository-level history
  ledger'
started_at: '2026-10-23T09:10:00Z'
finished_at: '2026-10-23T09:18:01Z'
reviewer:
  identity: antigravity-stage4-record-review
  kind: agent
  model: claude-opus-4-6
  independence: independent
  independence_basis: Reviewed in Cycle 1 Stage 4 record_review against committed
    git revision 13c6b0d85338aa96d330b8d699587dfe270a21f9 without record edits in
    this stage.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: PASS_WITH_FOLLOW_UP
scientific_review: true
summary: Woronin body (GO:0140266, data/structures/membrane_organelle/woronin_body.yaml)
  has accurate peroxisome-derived dense-core organelle identity, Pezizomycotina taxonomic
  scope, HEX-1 and WSC component grounding, verified Neurospora crassa OR74A UniProtKB
  protein examples (P87252, Q7S4P4), and source-backed septal-pore plugging and cortical-tethering
  causal graphs. However, it is the only record among all 978 corpus records that
  lacks a repository-level curation history directory and YAML ledger under history/records/woronin_body/,
  violating CLAUDE.md rule 8.
source:
  git_revision: 13c6b0d85338aa96d330b8d699587dfe270a21f9
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
  - path: data/structures/membrane_organelle/woronin_body.yaml
    sha256: 24e7471985cc32dfced99dee41e11ca767c421cfe7a7f24262dda3858793ad34
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
  description: Single-record audit of Woronin body (GO:0140266) covering identity,
    composition, causal graphs, evidence, and repository-level history provenance.
  selection: Targeted single-record review after whole-corpus audit identified Woronin
    body as the sole record lacking a history/records/<stem>/ ledger.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0140266
targets:
- target_id: GO:0140266
  path: data/structures/membrane_organelle/woronin_body.yaml
  label: Woronin body
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 24e7471985cc32dfced99dee41e11ca767c421cfe7a7f24262dda3858793ad34
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/woronin_body.yaml
    role: maintained_record
checks:
- check_id: schema_woronin
  name: LinkML schema validation on woronin_body.yaml
  status: passed
  required: true
  summary: No LinkML schema issues found for woronin_body.yaml.
  target_ids:
  - GO:0140266
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/woronin_body.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_schema_woronin
- check_id: strict_woronin
  name: Strict instance validator on woronin_body.yaml
  status: passed
  required: true
  summary: Zero strict validator errors or warnings on woronin_body.yaml.
  target_ids:
  - GO:0140266
  command: .venv/bin/python scripts/validate_strict.py data/structures/membrane_organelle/woronin_body.yaml
    --out /tmp/woronin_failures.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_strict_woronin
- check_id: history_corpus
  name: Repository-level history validation
  status: passed
  required: true
  summary: Existing 1903 history files validate, but validate_history.py does not
    check 1:1 coverage from data/structures/**/*.yaml to history/records/<stem>/.
  target_ids:
  - GO:0140266
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_history_validator
  - ev_woronin_curation_history
evidence:
- evidence_id: ev_woronin_record
  kind: record_content
  reference: data/structures/membrane_organelle/woronin_body.yaml
  locator: lines 1-249
  accessed_at: '2026-10-23T09:13:54Z'
  support: supports
  summary: Inspecting woronin_body.yaml confirms accurate GO:0140266 identity, Pezizomycotina
    scope, HEX-1/WSC components with N. crassa OR74A UniProtKB examples, and source-backed
    causal graphs.
  snapshot_sha256: 24e7471985cc32dfced99dee41e11ca767c421cfe7a7f24262dda3858793ad34
- evidence_id: ev_woronin_curation_history
  kind: record_content
  reference: data/structures/membrane_organelle/woronin_body.yaml
  locator: curation_history[0..3] (lines 11-36) vs history/records/
  accessed_at: '2026-10-23T09:13:54Z'
  support: supports
  summary: woronin_body.yaml records 4 inline curation_history events (CREATED_RECORD
    on 2026-09-12T10:15:23Z through EDIT on 2026-10-18T05:29:52Z), yet no history/records/woronin_body/
    directory exists in the repository.
  quote: "timestamp: '2026-09-12T10:15:23Z'\n  curator: antigravity-agent\n  action:\
    \ CREATED_RECORD\n  changes: Created comprehensive record for the fungal Woronin\
    \ body (GO:0140266)"
  snapshot_sha256: 24e7471985cc32dfced99dee41e11ca767c421cfe7a7f24262dda3858793ad34
- evidence_id: ev_schema_woronin
  kind: validation
  reference: scripts/validate_strict.py
  locator: schema_woronin receipt
  accessed_at: '2026-10-23T09:13:56Z'
  support: supports
  summary: linkml-validate exited 0 on woronin_body.yaml.
  snapshot_sha256: de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- evidence_id: ev_strict_woronin
  kind: validation
  reference: scripts/validate_strict.py
  locator: strict_woronin receipt
  accessed_at: '2026-10-23T09:16:04Z'
  support: supports
  summary: validate_strict.py exited 0 on woronin_body.yaml.
  snapshot_sha256: e206c7c81acecd6aee42df7c2d035be87518410e760ce254f0caacd0b9ab1e5b
- evidence_id: ev_history_validator
  kind: validation
  reference: scripts/validate_history.py
  locator: history receipt
  accessed_at: '2026-10-23T09:10:36Z'
  support: context_only
  summary: validate_history.py validates 1903 existing history YAML files but does
    not check whether any data/structures/**/*.yaml record lacks a history/records/<stem>/
    directory.
  snapshot_sha256: 58cd0a9db943ec58f980604094a2207f5c3d0da48b8cafbd4389e4e771cea1be
assessments:
- assessment_id: assess_woronin_scientific
  area: identity
  topic: Identity, hierarchy, composition, causal graphs, and evidence of Woronin
    body (GO:0140266)
  outcome: supported
  summary: Identity (GO:0140266), parent/part_of hierarchy (GO:0043231, GO:0005737),
    HEX-1 and WSC components, N. crassa OR74A UniProtKB protein examples, and assembly/function
    causal graphs are accurately grounded and supported by cited primary literature.
  target_ids:
  - GO:0140266
  evidence_ids:
  - ev_woronin_record
  - ev_schema_woronin
  - ev_strict_woronin
- assessment_id: assess_woronin_provenance
  area: provenance
  topic: Repository-level curation history coverage under history/records/woronin_body/
  outcome: concern
  summary: woronin_body.yaml is the only record out of 978 in data/structures/ without
    a corresponding history/records/<stem>/ ledger directory.
  target_ids:
  - GO:0140266
  evidence_ids:
  - ev_woronin_curation_history
  - ev_history_validator
findings:
- finding_id: F1
  issue_key: woronin-body-missing-history
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: woronin_body.yaml is missing its repository-level history ledger under history/records/woronin_body/
  description: data/structures/membrane_organelle/woronin_body.yaml contains 4 inline
    curation_history entries (created in commit a220d8400268740afc59decc917820cfa60f8008
    on 2026-09-12 and updated through 2026-10-18), but has zero repository-level history
    YAML files under history/records/woronin_body/. Every other record in the 978-record
    corpus (977/978) has at least one repository-level history file under history/records/<stem>/.
  target_ids:
  - GO:0140266
  field_paths:
  - curation_history
  evidence_ids:
  - ev_woronin_curation_history
  - ev_history_validator
  rule_id: CLAUDE.md:repository-level-history-for-every-curation-change
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/woronin_body.yaml
    role: maintained_record
  - repository: CultureBotAI/CellStructureMech
    path: src/cellstructuremech/schema/history.yaml
    role: history_schema
  tags:
  - history
  - provenance
  - stage4-record-review
actions:
- action_id: A1
  description: Create a backfill CurationEvent YAML ledger under history/records/woronin_body/
    recording the git-verified provenance of data/structures/membrane_organelle/woronin_body.yaml
    and validate with scripts/validate_history.py.
  finding_ids:
  - F1
  target_ids:
  - GO:0140266
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/woronin_body.yaml
    role: maintained_record
  acceptance_checks:
  - test -d history/records/woronin_body
  - .venv/bin/python scripts/validate_history.py
limitations:
- Repository-level history ledger under history/records/woronin_body/ is currently
  absent and queued for Stage 5 remediation.
tags:
- stage4
- record-review
- woronin-body
```
