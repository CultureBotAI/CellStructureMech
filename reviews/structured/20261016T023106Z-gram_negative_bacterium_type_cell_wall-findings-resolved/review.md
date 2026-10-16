# Gram-negative-bacterium-type cell wall: scoped finding dispositions

- Review: 20261016T023106Z-gram_negative_bacterium_type_cell_wall-findings-resolved
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-16T02:23:00Z
- Finished UTC: 2026-10-16T02:31:06Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Resolved 2 previously observed finding(s) in issue #2313. Correct peptidoglycan/Lpp acyl donor-acceptor direction and type Lol as a pathway.

## Scope And Provenance

Reassess only the listed predecessor findings against corrected maintained fields and preserved source scope.

Selection: data/structures/envelope/gram_negative_bacterium_type_cell_wall.yaml
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base fb9cc359dff64d09193399c63d5650f9ef75656d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0009276 | data/structures/envelope/gram_negative_bacterium_type_cell_wall.yaml | maintained | Gram-negative-bacterium-type cell wall |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| ci-qc | passed | True | GO:0009276 | Executed 2026-10-16T02:23:11Z to 2026-10-16T02:26:28Z; log SHA-256 bf293f5df5e6d265e50eadbb1376b4568d20a16a491e9b3dbbdb62a3c92c4caf. |
| history | passed | True | GO:0009276 | Executed 2026-10-16T02:21:55Z to 2026-10-16T02:22:11Z; log SHA-256 f2b178c96cecd3568904a23477f3849af3781b06d1293fb6daee625454acdc6e. |
| strict | passed | True | GO:0009276 | Executed 2026-10-16T02:22:11Z to 2026-10-16T02:22:27Z; log SHA-256 4b444ea3fc980fd4c8e810a737238daf08760933c04ded087fb2bc78166fe1c7. |
| render-check | passed | True | GO:0009276 | Executed 2026-10-16T02:22:27Z to 2026-10-16T02:23:03Z; log SHA-256 b798d21a609b296cdc2aeb317f68fc259c4e86ee43942b4a3c5008b32b9bfa5e. |
| review-archive | passed | True | GO:0009276 | Executed 2026-10-16T02:23:33Z to 2026-10-16T02:25:59Z; log SHA-256 c5396768e27f8e9f7d783841b4bbc23801ceabfd8bbba6f1194f675723be2814. |
| diff-check | passed | True | GO:0009276 | Executed 2026-10-16T02:25:59Z to 2026-10-16T02:25:59Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855. |
| labels | passed | True | GO:0009276 | Executed 2026-10-16T01:58:15Z to 2026-10-16T02:03:51Z; log SHA-256 2a1330c26aac5bd248a2fd3a3a7b9c882d2b3bb202365c555e5d6415d1c2203d. |
| traits | passed | True | GO:0009276 | Executed 2026-10-16T02:03:51Z to 2026-10-16T02:04:36Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f. |
| curie-self-test | passed | True | GO:0009276 | Executed 2026-10-16T02:04:36Z to 2026-10-16T02:05:09Z; log SHA-256 de2bcfc9df8102d7a85eea7bee03e76f6f978cf22673a2a241ea01f865b3b2b8. |
| curies | passed | True | GO:0009276 | Executed 2026-10-16T02:05:09Z to 2026-10-16T02:06:58Z; log SHA-256 ebd9ac70fa2773f37d94819e5fa2e4bb4fad813ec79dbf9c59eb386d446f8a77. |
| Local aggregate QC invocation | failed | False | GO:0009276 | 1003 tests passed and 3 skipped, then the history subprocess selected an unavailable pyenv shim because the virtual environment was not first on PATH. Remaining local gates were rerun with PATH corrected; required aggregate QC is supplied by the passing ci-qc check, not this failed invocation. |

## Scientific And Domain Assessments

### Evidence and representation changes for the listed finding keys

consistency: supported. Targets: GO:0009276.

Correct peptidoglycan/Lpp acyl donor-acceptor direction and type Lol as a pathway.

Checked the diff against each predecessor description and acceptance intent. Taxon-specific examples are not promoted to universal mechanisms; unknown formation requirements and disputed observations remain explicit. This is not a new comprehensive record review.

## Findings

### F1: Correct the Lpp-anchoring donor/acceptor roles

major / resolved / confirmed; issue key: gram-negative-wall-ldt-donor-acceptor.

The directed uses-acceptor edge and its description reverse the roles assigned by the cited paper. Peptidoglycan supplies the acyl donor; the Lpp terminal-lysine side-chain amine is the acceptor. Correct the edge and prose while retaining the original paper's distinction between observed linkage and catalytic interpretation.

Disposition: Correct peptidoglycan/Lpp acyl donor-acceptor direction and type Lol as a pathway. The listed maintained fields now address this earlier defect; validation passed. This closes the missing qualification, representation or provenance issue, not any underlying scientific uncertainty documented in the record.

### F2: Do not type the Lol pathway as one protein entity

minor / resolved / confirmed; issue key: gram-negative-wall-lol-pathway-node-type.

The node label denotes a pathway spanning distinct proteins, but GENE_OR_PROTEIN is restricted to proteins, families and complexes. Use the native PATHWAY type, or remodel with source-supported protein actors and matching edges; do not relabel the entire route as one complex.

Disposition: Correct peptidoglycan/Lpp acyl donor-acceptor direction and type Lol as a pathway. The listed maintained fields now address this earlier defect; validation passed. This closes the missing qualification, representation or provenance issue, not any underlying scientific uncertainty documented in the record.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/structures/envelope/gram_negative_bacterium_type_cell_wall.yaml; Post-fix YAML; specific field paths retained on each finding | supports | Correct peptidoglycan/Lpp acyl donor-acceptor direction and type Lol as a pathway. |
| history | history/records/gram_negative_bacterium_type_cell_wall/2026-10-16T015052Z-Codex-da94d9.yaml; Entire appended event, including source scope and issue/PR links | supports | New append-only provenance documents the authorized correction. Original history and discussion rationale prefixes are preserved; native mapping_status remains PROPOSED. |
| prior | reviews/structured/20261012T120038Z-gram-negative-wall-ldt-lol-semantics/review.yaml; Exact findings and their original evidence/limitations | context_only | Original issue-bearing observations retained byte-identically. Their full-record coverage and source-access limitations are not promoted by this finding-only follow-up. |
| sources | reviews/structured/20261012T120038Z-gram-negative-wall-ldt-lol-semantics/review.yaml; Source observations reassessed during remediation, with claim-level scope retained in the appended history | supports | Remediation source checks: Magnet et al. 2007 DOI:10.1128/JB.00084-07 NCBI full-text abstract and linkage analysis; Native LolCDE/LolA/LolB pathway scope. This entry records the source reassessment scope, not a claim that every cited full text was freshly fetched or completely read. Primary abstracts remain abstract-only evidence; prior readable passages are distinguished from failed reaccess. |
| validation | PR #2296 local verification; Commands and log hashes in Checks | supports | Fresh repository gates passed against corrected records. Deterministic checks do not prove scientific completeness. The separate preservation audit includes ignored files. |

## Limits And Additional Notes

- Same-agent adversarial self-review of the remediation diff, not independent human or second-agent approval.
- Partial, finding-only review: all listed issue keys were reassessed, not all claims in this record or the 909-record corpus. Earlier partial-review limitations and open native curation TODOs remain. No native scientific-status promotion.
- Only new supported dispositions are saved. Original review bundles, historical reports and append-only events were preserved. No clean-review placeholder was created.
- No new quotation snippets were added. Source access was bounded by the listed abstract/full-text/authority observations; inaccessible or error responses were not used as source text.
- The first local aggregate QC attempt failed at history-command startup after the full test suite passed. PATH was corrected for remaining local gates; the complete required QC run passed in GitHub CI on the inspected committed native bytes.
- Prior whole-record review remains incomplete. Previously unverified topics: Taxonomy and prototype limits; Nearest-source coverage.
- Fresh Magnet 2007 abstract confirms the protein acyl acceptor; linkage detail relies on the prior source inspection. A fresh full-body endpoint did not expose the complete article.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T023106Z-gram_negative_bacterium_type_cell_wall-findings-resolved
kind: record
repository: CultureBotAI/CellStructureMech
title: 'Gram-negative-bacterium-type cell wall: scoped finding dispositions'
started_at: '2026-10-16T02:23:00Z'
finished_at: '2026-10-16T02:31:06Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Separate adversarial pass by the same agent that implemented
    the corrections.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: pass_with_limitations
scientific_review: true
summary: 'Resolved 2 previously observed finding(s) in issue #2313. Correct peptidoglycan/Lpp
  acyl donor-acceptor direction and type Lol as a pathway.'
source:
  git_revision: fb9cc359dff64d09193399c63d5650f9ef75656d
  state: working_tree
  inputs:
  - path: data/structures/envelope/gram_negative_bacterium_type_cell_wall.yaml
    sha256: 6d95ada30f0591242e79078c4f1aeec41ea7caa10edb1244081e93056b14f2b1
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
  - path: history/records/gram_negative_bacterium_type_cell_wall/2026-10-16T015052Z-Codex-da94d9.yaml
    sha256: 2d321415bc0663f225e78b4a6bfd373ec30e366239138c8cb18039eb523b9ecf
    role: context
  - path: reviews/structured/20261012T120038Z-gram-negative-wall-ldt-lol-semantics/review.yaml
    sha256: a10a0664316b77d199f22e7b8022379db296349856650f0ca7f8250afeb7e560
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: tests/test_energy_envelope_inclusion_review.py
    sha256: 7382113a3b52dc3f9dc8368df26f9c024fc35c6862c008f491c802d64274a93d
    role: context
targets:
- target_id: GO:0009276
  path: data/structures/envelope/gram_negative_bacterium_type_cell_wall.yaml
  label: Gram-negative-bacterium-type cell wall
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/envelope/gram_negative_bacterium_type_cell_wall.yaml
    role: maintained scientific record
scope:
  description: Reassess only the listed predecessor findings against corrected maintained
    fields and preserved source scope.
  selection: data/structures/envelope/gram_negative_bacterium_type_cell_wall.yaml
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - GO:0009276
checks:
- check_id: ci-qc
  name: ci-qc
  status: passed
  required: true
  command: gh run watch 38840066294 --repo CultureBotAI/CellStructureMech --interval
    15 --exit-status
  exit_code: 0
  target_ids:
  - GO:0009276
  evidence_ids:
  - validation
  summary: Executed 2026-10-16T02:23:11Z to 2026-10-16T02:26:28Z; log SHA-256 bf293f5df5e6d265e50eadbb1376b4568d20a16a491e9b3dbbdb62a3c92c4caf.
  scope_note: Full-corpus gate on unchanged scientific input bytes. ci-qc is the GitHub
    clean-environment full QC run on the inspected committed remediation snapshot.
    Original configured skips and non-adapter identifiers remain outside coverage.
    Pre-save archive check covers the 226 earlier bundles, not these successors.
- check_id: history
  name: history
  status: passed
  required: true
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CellStructureMech/.venv/bin/python
    scripts/validate_history.py
  exit_code: 0
  target_ids:
  - GO:0009276
  evidence_ids:
  - validation
  summary: Executed 2026-10-16T02:21:55Z to 2026-10-16T02:22:11Z; log SHA-256 f2b178c96cecd3568904a23477f3849af3781b06d1293fb6daee625454acdc6e.
  scope_note: Full-corpus gate on unchanged scientific input bytes. ci-qc is the GitHub
    clean-environment full QC run on the inspected committed remediation snapshot.
    Original configured skips and non-adapter identifiers remain outside coverage.
    Pre-save archive check covers the 226 earlier bundles, not these successors.
- check_id: strict
  name: strict
  status: passed
  required: true
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CellStructureMech/.venv/bin/python
    scripts/validate_strict.py --quiet
  exit_code: 0
  target_ids:
  - GO:0009276
  evidence_ids:
  - validation
  summary: Executed 2026-10-16T02:22:11Z to 2026-10-16T02:22:27Z; log SHA-256 4b444ea3fc980fd4c8e810a737238daf08760933c04ded087fb2bc78166fe1c7.
  scope_note: Full-corpus gate on unchanged scientific input bytes. ci-qc is the GitHub
    clean-environment full QC run on the inspected committed remediation snapshot.
    Original configured skips and non-adapter identifiers remain outside coverage.
    Pre-save archive check covers the 226 earlier bundles, not these successors.
- check_id: render-check
  name: render-check
  status: passed
  required: true
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CellStructureMech/.venv/bin/python
    scripts/render_pages.py --check
  exit_code: 0
  target_ids:
  - GO:0009276
  evidence_ids:
  - validation
  summary: Executed 2026-10-16T02:22:27Z to 2026-10-16T02:23:03Z; log SHA-256 b798d21a609b296cdc2aeb317f68fc259c4e86ee43942b4a3c5008b32b9bfa5e.
  scope_note: Full-corpus gate on unchanged scientific input bytes. ci-qc is the GitHub
    clean-environment full QC run on the inspected committed remediation snapshot.
    Original configured skips and non-adapter identifiers remain outside coverage.
    Pre-save archive check covers the 226 earlier bundles, not these successors.
- check_id: review-archive
  name: review-archive
  status: passed
  required: true
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CellStructureMech/.venv/bin/python
    scripts/record_review.py check
  exit_code: 0
  target_ids:
  - GO:0009276
  evidence_ids:
  - validation
  summary: Executed 2026-10-16T02:23:33Z to 2026-10-16T02:25:59Z; log SHA-256 c5396768e27f8e9f7d783841b4bbc23801ceabfd8bbba6f1194f675723be2814.
  scope_note: Full-corpus gate on unchanged scientific input bytes. ci-qc is the GitHub
    clean-environment full QC run on the inspected committed remediation snapshot.
    Original configured skips and non-adapter identifiers remain outside coverage.
    Pre-save archive check covers the 226 earlier bundles, not these successors.
- check_id: diff-check
  name: diff-check
  status: passed
  required: true
  command: git diff --check
  exit_code: 0
  target_ids:
  - GO:0009276
  evidence_ids:
  - validation
  summary: Executed 2026-10-16T02:25:59Z to 2026-10-16T02:25:59Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.
  scope_note: Full-corpus gate on unchanged scientific input bytes. ci-qc is the GitHub
    clean-environment full QC run on the inspected committed remediation snapshot.
    Original configured skips and non-adapter identifiers remain outside coverage.
    Pre-save archive check covers the 226 earlier bundles, not these successors.
- check_id: labels
  name: labels
  status: passed
  required: true
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CellStructureMech/.venv/bin/python
    scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  target_ids:
  - GO:0009276
  evidence_ids:
  - validation
  summary: Executed 2026-10-16T01:58:15Z to 2026-10-16T02:03:51Z; log SHA-256 2a1330c26aac5bd248a2fd3a3a7b9c882d2b3bb202365c555e5d6415d1c2203d.
  scope_note: Full-corpus gate on unchanged scientific input bytes. ci-qc is the GitHub
    clean-environment full QC run on the inspected committed remediation snapshot.
    Original configured skips and non-adapter identifiers remain outside coverage.
    Pre-save archive check covers the 226 earlier bundles, not these successors.
- check_id: traits
  name: traits
  status: passed
  required: true
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CellStructureMech/.venv/bin/python
    scripts/check_trait_links.py --check
  exit_code: 0
  target_ids:
  - GO:0009276
  evidence_ids:
  - validation
  summary: Executed 2026-10-16T02:03:51Z to 2026-10-16T02:04:36Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f.
  scope_note: Full-corpus gate on unchanged scientific input bytes. ci-qc is the GitHub
    clean-environment full QC run on the inspected committed remediation snapshot.
    Original configured skips and non-adapter identifiers remain outside coverage.
    Pre-save archive check covers the 226 earlier bundles, not these successors.
- check_id: curie-self-test
  name: curie-self-test
  status: passed
  required: true
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CellStructureMech/.venv/bin/python
    scripts/check_curies.py --self-test
  exit_code: 0
  target_ids:
  - GO:0009276
  evidence_ids:
  - validation
  summary: Executed 2026-10-16T02:04:36Z to 2026-10-16T02:05:09Z; log SHA-256 de2bcfc9df8102d7a85eea7bee03e76f6f978cf22673a2a241ea01f865b3b2b8.
  scope_note: Full-corpus gate on unchanged scientific input bytes. ci-qc is the GitHub
    clean-environment full QC run on the inspected committed remediation snapshot.
    Original configured skips and non-adapter identifiers remain outside coverage.
    Pre-save archive check covers the 226 earlier bundles, not these successors.
- check_id: curies
  name: curies
  status: passed
  required: true
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CellStructureMech/.venv/bin/python
    scripts/check_curies.py --check --report /private/tmp/csm-pr-20261016T013940Z/curie-report.tsv
  exit_code: 0
  target_ids:
  - GO:0009276
  evidence_ids:
  - validation
  summary: Executed 2026-10-16T02:05:09Z to 2026-10-16T02:06:58Z; log SHA-256 ebd9ac70fa2773f37d94819e5fa2e4bb4fad813ec79dbf9c59eb386d446f8a77.
  scope_note: Full-corpus gate on unchanged scientific input bytes. ci-qc is the GitHub
    clean-environment full QC run on the inspected committed remediation snapshot.
    Original configured skips and non-adapter identifiers remain outside coverage.
    Pre-save archive check covers the 226 earlier bundles, not these successors.
- check_id: local-qc-environment
  name: Local aggregate QC invocation
  status: failed
  required: false
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CellStructureMech/.venv/bin/python
    scripts/run_qc.py
  exit_code: 1
  target_ids:
  - GO:0009276
  evidence_ids:
  - validation
  summary: 1003 tests passed and 3 skipped, then the history subprocess selected an
    unavailable pyenv shim because the virtual environment was not first on PATH.
    Remaining local gates were rerun with PATH corrected; required aggregate QC is
    supplied by the passing ci-qc check, not this failed invocation.
  scope_note: Original log SHA-256 6ba6de0909cb40a58a06305657c9a4259a8c42bbdde2b4e9da60d37a79e7773d;
    no validator was weakened or tests skipped to pass.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/structures/envelope/gram_negative_bacterium_type_cell_wall.yaml
  locator: Post-fix YAML; specific field paths retained on each finding
  accessed_at: '2026-10-16T02:31:06Z'
  snapshot_sha256: 6d95ada30f0591242e79078c4f1aeec41ea7caa10edb1244081e93056b14f2b1
  support: supports
  summary: Correct peptidoglycan/Lpp acyl donor-acceptor direction and type Lol as
    a pathway.
- evidence_id: history
  kind: record_content
  reference: history/records/gram_negative_bacterium_type_cell_wall/2026-10-16T015052Z-Codex-da94d9.yaml
  locator: Entire appended event, including source scope and issue/PR links
  accessed_at: '2026-10-16T02:31:06Z'
  support: supports
  summary: New append-only provenance documents the authorized correction. Original
    history and discussion rationale prefixes are preserved; native mapping_status
    remains PROPOSED.
- evidence_id: prior
  kind: prior_review
  reference: reviews/structured/20261012T120038Z-gram-negative-wall-ldt-lol-semantics/review.yaml
  locator: Exact findings and their original evidence/limitations
  accessed_at: '2026-10-16T02:31:06Z'
  support: context_only
  summary: Original issue-bearing observations retained byte-identically. Their full-record
    coverage and source-access limitations are not promoted by this finding-only follow-up.
- evidence_id: sources
  kind: prior_review
  reference: reviews/structured/20261012T120038Z-gram-negative-wall-ldt-lol-semantics/review.yaml
  locator: Source observations reassessed during remediation, with claim-level scope
    retained in the appended history
  accessed_at: '2026-10-16T02:31:06Z'
  support: supports
  summary: 'Remediation source checks: Magnet et al. 2007 DOI:10.1128/JB.00084-07
    NCBI full-text abstract and linkage analysis; Native LolCDE/LolA/LolB pathway
    scope. This entry records the source reassessment scope, not a claim that every
    cited full text was freshly fetched or completely read. Primary abstracts remain
    abstract-only evidence; prior readable passages are distinguished from failed
    reaccess.'
- evidence_id: validation
  kind: validation
  reference: 'PR #2296 local verification'
  locator: Commands and log hashes in Checks
  accessed_at: '2026-10-16T02:31:06Z'
  support: supports
  summary: Fresh repository gates passed against corrected records. Deterministic
    checks do not prove scientific completeness. The separate preservation audit includes
    ignored files.
assessments:
- assessment_id: scoped-remediation
  area: consistency
  topic: Evidence and representation changes for the listed finding keys
  outcome: supported
  target_ids:
  - GO:0009276
  evidence_ids:
  - native
  - history
  - prior
  - sources
  - validation
  summary: Correct peptidoglycan/Lpp acyl donor-acceptor direction and type Lol as
    a pathway.
  details: Checked the diff against each predecessor description and acceptance intent.
    Taxon-specific examples are not promoted to universal mechanisms; unknown formation
    requirements and disputed observations remain explicit. This is not a new comprehensive
    record review.
findings:
- finding_id: F1
  issue_key: gram-negative-wall-ldt-donor-acceptor
  category: graph
  severity: major
  status: resolved
  certainty: confirmed
  title: Correct the Lpp-anchoring donor/acceptor roles
  description: The directed uses-acceptor edge and its description reverse the roles
    assigned by the cited paper. Peptidoglycan supplies the acyl donor; the Lpp terminal-lysine
    side-chain amine is the acceptor. Correct the edge and prose while retaining the
    original paper's distinction between observed linkage and catalytic interpretation.
  target_ids:
  - GO:0009276
  field_paths:
  - causal_graphs[graph_id=lpp_lol_pg_tether_assembly].edges[subject=ldt_lpp,predicate=uses
    acceptor,object=thin_peptidoglycan]
  evidence_ids:
  - native
  - history
  - prior
  - sources
  - validation
  rule_id: review-checklist:causal-edge-mechanistic-evidence
  native_severity: major
  normalization_reason: Wrong directed chemical mechanism, not merely prose style;
    record identity remains correct.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/envelope/gram_negative_bacterium_type_cell_wall.yaml
    role: maintained scientific record
  disposition_reason: Correct peptidoglycan/Lpp acyl donor-acceptor direction and
    type Lol as a pathway. The listed maintained fields now address this earlier defect;
    validation passed. This closes the missing qualification, representation or provenance
    issue, not any underlying scientific uncertainty documented in the record.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261012T120038Z-gram-negative-wall-ldt-lol-semantics
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2313
- finding_id: F2
  issue_key: gram-negative-wall-lol-pathway-node-type
  category: representation
  severity: minor
  status: resolved
  certainty: confirmed
  title: Do not type the Lol pathway as one protein entity
  description: The node label denotes a pathway spanning distinct proteins, but GENE_OR_PROTEIN
    is restricted to proteins, families and complexes. Use the native PATHWAY type,
    or remodel with source-supported protein actors and matching edges; do not relabel
    the entire route as one complex.
  target_ids:
  - GO:0009276
  field_paths:
  - causal_graphs[graph_id=lpp_lol_pg_tether_assembly].nodes[node_id=lol_pathway].node_type
  evidence_ids:
  - native
  - history
  - prior
  - sources
  - validation
  rule_id: cellstructuremech:CausalNode-type-semantics
  native_severity: minor
  normalization_reason: Localized semantic typing defect; the intended traffic route
    is understandable and structure identity is unaffected.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/envelope/gram_negative_bacterium_type_cell_wall.yaml
    role: maintained scientific record
  disposition_reason: Correct peptidoglycan/Lpp acyl donor-acceptor direction and
    type Lol as a pathway. The listed maintained fields now address this earlier defect;
    validation passed. This closes the missing qualification, representation or provenance
    issue, not any underlying scientific uncertainty documented in the record.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261012T120038Z-gram-negative-wall-ldt-lol-semantics
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2313
actions: []
limitations:
- Same-agent adversarial self-review of the remediation diff, not independent human
  or second-agent approval.
- 'Partial, finding-only review: all listed issue keys were reassessed, not all claims
  in this record or the 909-record corpus. Earlier partial-review limitations and
  open native curation TODOs remain. No native scientific-status promotion.'
- Only new supported dispositions are saved. Original review bundles, historical reports
  and append-only events were preserved. No clean-review placeholder was created.
- No new quotation snippets were added. Source access was bounded by the listed abstract/full-text/authority
  observations; inaccessible or error responses were not used as source text.
- The first local aggregate QC attempt failed at history-command startup after the
  full test suite passed. PATH was corrected for remaining local gates; the complete
  required QC run passed in GitHub CI on the inspected committed native bytes.
- 'Prior whole-record review remains incomplete. Previously unverified topics: Taxonomy
  and prototype limits; Nearest-source coverage.'
- Fresh Magnet 2007 abstract confirms the protein acyl acceptor; linkage detail relies
  on the prior source inspection. A fresh full-body endpoint did not expose the complete
  article.
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261012T120038Z-gram-negative-wall-ldt-lol-semantics
  relationship: Scoped successor for the explicitly cited finding occurrences only
links:
- https://github.com/CultureBotAI/CellStructureMech/issues/2313
- https://github.com/CultureBotAI/CellStructureMech/pull/2296
```
