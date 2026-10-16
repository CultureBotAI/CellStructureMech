# respiratory chain complex III: scoped finding dispositions

- Review: 20261016T023023Z-respiratory_chain_complex_iii-findings-resolved
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-16T02:23:00Z
- Finished UTC: 2026-10-16T02:30:23Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Resolved 1 previously observed finding(s) in issue #2308. Retain the Rieske subunit label-only instead of using a domain as a protein-family grounding.

## Scope And Provenance

Reassess only the listed predecessor findings against corrected maintained fields and preserved source scope.

Selection: data/structures/energy_complex/respiratory_chain_complex_iii.yaml
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base fb9cc359dff64d09193399c63d5650f9ef75656d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0045275 | data/structures/energy_complex/respiratory_chain_complex_iii.yaml | maintained | respiratory chain complex III |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| ci-qc | passed | True | GO:0045275 | Executed 2026-10-16T02:23:11Z to 2026-10-16T02:26:28Z; log SHA-256 bf293f5df5e6d265e50eadbb1376b4568d20a16a491e9b3dbbdb62a3c92c4caf. |
| history | passed | True | GO:0045275 | Executed 2026-10-16T02:21:55Z to 2026-10-16T02:22:11Z; log SHA-256 f2b178c96cecd3568904a23477f3849af3781b06d1293fb6daee625454acdc6e. |
| strict | passed | True | GO:0045275 | Executed 2026-10-16T02:22:11Z to 2026-10-16T02:22:27Z; log SHA-256 4b444ea3fc980fd4c8e810a737238daf08760933c04ded087fb2bc78166fe1c7. |
| render-check | passed | True | GO:0045275 | Executed 2026-10-16T02:22:27Z to 2026-10-16T02:23:03Z; log SHA-256 b798d21a609b296cdc2aeb317f68fc259c4e86ee43942b4a3c5008b32b9bfa5e. |
| review-archive | passed | True | GO:0045275 | Executed 2026-10-16T02:23:33Z to 2026-10-16T02:25:59Z; log SHA-256 c5396768e27f8e9f7d783841b4bbc23801ceabfd8bbba6f1194f675723be2814. |
| diff-check | passed | True | GO:0045275 | Executed 2026-10-16T02:25:59Z to 2026-10-16T02:25:59Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855. |
| labels | passed | True | GO:0045275 | Executed 2026-10-16T01:58:15Z to 2026-10-16T02:03:51Z; log SHA-256 2a1330c26aac5bd248a2fd3a3a7b9c882d2b3bb202365c555e5d6415d1c2203d. |
| traits | passed | True | GO:0045275 | Executed 2026-10-16T02:03:51Z to 2026-10-16T02:04:36Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f. |
| curie-self-test | passed | True | GO:0045275 | Executed 2026-10-16T02:04:36Z to 2026-10-16T02:05:09Z; log SHA-256 de2bcfc9df8102d7a85eea7bee03e76f6f978cf22673a2a241ea01f865b3b2b8. |
| curies | passed | True | GO:0045275 | Executed 2026-10-16T02:05:09Z to 2026-10-16T02:06:58Z; log SHA-256 ebd9ac70fa2773f37d94819e5fa2e4bb4fad813ec79dbf9c59eb386d446f8a77. |
| Local aggregate QC invocation | failed | False | GO:0045275 | 1003 tests passed and 3 skipped, then the history subprocess selected an unavailable pyenv shim because the virtual environment was not first on PATH. Remaining local gates were rerun with PATH corrected; required aggregate QC is supplied by the passing ci-qc check, not this failed invocation. |

## Scientific And Domain Assessments

### Evidence and representation changes for the listed finding keys

consistency: supported. Targets: GO:0045275.

Retain the Rieske subunit label-only instead of using a domain as a protein-family grounding.

Checked the diff against each predecessor description and acceptance intent. Taxon-specific examples are not promoted to universal mechanisms; unknown formation requirements and disputed observations remain explicit. This is not a new comprehensive record review.

## Findings

### F1: Do not use an InterPro domain as the Rieske whole-protein family identity

major / resolved / confirmed; issue key: complex-iii-rieske-entry-type.

The Rieske component and its GENE_OR_PROTEIN node both ground to IPR006317, and the component evidence note calls that entry a family. Current standalone and reviewed-protein InterPro responses instead classify it as a domain. The187-residue Q02762 match spans10-187; matching almost all of this example does not turn a domain accession into an integrated protein-family identity. This violates the native grounding distinction, not the supported biological membership or reaction. IPR014349 is a family but includes b6f Rieske and AioB, so replacing the identifier with that broader family would create a different scope error.

Disposition: Retain the Rieske subunit label-only instead of using a domain as a protein-family grounding. The listed maintained fields now address this earlier defect; validation passed. This closes the missing qualification, representation or provenance issue, not any underlying scientific uncertainty documented in the record.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/structures/energy_complex/respiratory_chain_complex_iii.yaml; Post-fix YAML; specific field paths retained on each finding | supports | Retain the Rieske subunit label-only instead of using a domain as a protein-family grounding. |
| history | history/records/respiratory_chain_complex_iii/2026-10-16T014905Z-Codex-36819e.yaml; Entire appended event, including source scope and issue/PR links | supports | New append-only provenance documents the authorized correction. Original history and discussion rationale prefixes are preserved; native mapping_status remains PROPOSED. |
| prior | reviews/structured/20261012T102837Z-complex-iii-rieske-entry-type/review.yaml; Exact findings and their original evidence/limitations | context_only | Original issue-bearing observations retained byte-identically. Their full-record coverage and source-access limitations are not promoted by this finding-only follow-up. |
| sources | reviews/structured/20261012T102837Z-complex-iii-rieske-entry-type/review.yaml; Source observations reassessed during remediation, with claim-level scope retained in the appended history | supports | Remediation source checks: InterPro IPR006317 metadata.type=domain; Native PDB:2QJP membership retained. This entry records the source reassessment scope, not a claim that every cited full text was freshly fetched or completely read. Primary abstracts remain abstract-only evidence; prior readable passages are distinguished from failed reaccess. |
| validation | PR #2296 local verification; Commands and log hashes in Checks | supports | Fresh repository gates passed against corrected records. Deterministic checks do not prove scientific completeness. The separate preservation audit includes ignored files. |

## Limits And Additional Notes

- Same-agent adversarial self-review of the remediation diff, not independent human or second-agent approval.
- Partial, finding-only review: all listed issue keys were reassessed, not all claims in this record or the 909-record corpus. Earlier partial-review limitations and open native curation TODOs remain. No native scientific-status promotion.
- Only new supported dispositions are saved. Original review bundles, historical reports and append-only events were preserved. No clean-review placeholder was created.
- No new quotation snippets were added. Source access was bounded by the listed abstract/full-text/authority observations; inaccessible or error responses were not used as source text.
- The first local aggregate QC attempt failed at history-command startup after the full test suite passed. PATH was corrected for remaining local gates; the complete required QC run passed in GitHub CI on the inspected committed native bytes.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T023023Z-respiratory_chain_complex_iii-findings-resolved
kind: record
repository: CultureBotAI/CellStructureMech
title: 'respiratory chain complex III: scoped finding dispositions'
started_at: '2026-10-16T02:23:00Z'
finished_at: '2026-10-16T02:30:23Z'
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
summary: 'Resolved 1 previously observed finding(s) in issue #2308. Retain the Rieske
  subunit label-only instead of using a domain as a protein-family grounding.'
source:
  git_revision: fb9cc359dff64d09193399c63d5650f9ef75656d
  state: working_tree
  inputs:
  - path: data/structures/energy_complex/respiratory_chain_complex_iii.yaml
    sha256: c9c489d6e32702edf24734b1879e37baa0b7d7ca4e6b7fc7779432298d20ee1b
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
  - path: history/records/respiratory_chain_complex_iii/2026-10-16T014905Z-Codex-36819e.yaml
    sha256: 4ecd02900aa7df0003641b4b3029c6ce73262b3ec3d9a0d9554ff66e0bb74746
    role: context
  - path: reviews/structured/20261012T102837Z-complex-iii-rieske-entry-type/review.yaml
    sha256: 1c2d9e01574a49ba0d9e16fe31f3d827b60221cc6306a553722a5835b84a9755
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: tests/test_energy_envelope_inclusion_review.py
    sha256: 7382113a3b52dc3f9dc8368df26f9c024fc35c6862c008f491c802d64274a93d
    role: context
targets:
- target_id: GO:0045275
  path: data/structures/energy_complex/respiratory_chain_complex_iii.yaml
  label: respiratory chain complex III
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/respiratory_chain_complex_iii.yaml
    role: maintained scientific record
scope:
  description: Reassess only the listed predecessor findings against corrected maintained
    fields and preserved source scope.
  selection: data/structures/energy_complex/respiratory_chain_complex_iii.yaml
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - GO:0045275
checks:
- check_id: ci-qc
  name: ci-qc
  status: passed
  required: true
  command: gh run watch 38840066294 --repo CultureBotAI/CellStructureMech --interval
    15 --exit-status
  exit_code: 0
  target_ids:
  - GO:0045275
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
  - GO:0045275
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
  - GO:0045275
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
  - GO:0045275
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
  - GO:0045275
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
  - GO:0045275
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
  - GO:0045275
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
  - GO:0045275
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
  - GO:0045275
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
  - GO:0045275
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
  - GO:0045275
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
  reference: data/structures/energy_complex/respiratory_chain_complex_iii.yaml
  locator: Post-fix YAML; specific field paths retained on each finding
  accessed_at: '2026-10-16T02:30:23Z'
  snapshot_sha256: c9c489d6e32702edf24734b1879e37baa0b7d7ca4e6b7fc7779432298d20ee1b
  support: supports
  summary: Retain the Rieske subunit label-only instead of using a domain as a protein-family
    grounding.
- evidence_id: history
  kind: record_content
  reference: history/records/respiratory_chain_complex_iii/2026-10-16T014905Z-Codex-36819e.yaml
  locator: Entire appended event, including source scope and issue/PR links
  accessed_at: '2026-10-16T02:30:23Z'
  support: supports
  summary: New append-only provenance documents the authorized correction. Original
    history and discussion rationale prefixes are preserved; native mapping_status
    remains PROPOSED.
- evidence_id: prior
  kind: prior_review
  reference: reviews/structured/20261012T102837Z-complex-iii-rieske-entry-type/review.yaml
  locator: Exact findings and their original evidence/limitations
  accessed_at: '2026-10-16T02:30:23Z'
  support: context_only
  summary: Original issue-bearing observations retained byte-identically. Their full-record
    coverage and source-access limitations are not promoted by this finding-only follow-up.
- evidence_id: sources
  kind: prior_review
  reference: reviews/structured/20261012T102837Z-complex-iii-rieske-entry-type/review.yaml
  locator: Source observations reassessed during remediation, with claim-level scope
    retained in the appended history
  accessed_at: '2026-10-16T02:30:23Z'
  support: supports
  summary: 'Remediation source checks: InterPro IPR006317 metadata.type=domain; Native
    PDB:2QJP membership retained. This entry records the source reassessment scope,
    not a claim that every cited full text was freshly fetched or completely read.
    Primary abstracts remain abstract-only evidence; prior readable passages are distinguished
    from failed reaccess.'
- evidence_id: validation
  kind: validation
  reference: 'PR #2296 local verification'
  locator: Commands and log hashes in Checks
  accessed_at: '2026-10-16T02:30:23Z'
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
  - GO:0045275
  evidence_ids:
  - native
  - history
  - prior
  - sources
  - validation
  summary: Retain the Rieske subunit label-only instead of using a domain as a protein-family
    grounding.
  details: Checked the diff against each predecessor description and acceptance intent.
    Taxon-specific examples are not promoted to universal mechanisms; unknown formation
    requirements and disputed observations remain explicit. This is not a new comprehensive
    record review.
findings:
- finding_id: F1
  issue_key: complex-iii-rieske-entry-type
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Do not use an InterPro domain as the Rieske whole-protein family identity
  description: The Rieske component and its GENE_OR_PROTEIN node both ground to IPR006317,
    and the component evidence note calls that entry a family. Current standalone
    and reviewed-protein InterPro responses instead classify it as a domain. The187-residue
    Q02762 match spans10-187; matching almost all of this example does not turn a
    domain accession into an integrated protein-family identity. This violates the
    native grounding distinction, not the supported biological membership or reaction.
    IPR014349 is a family but includes b6f Rieske and AioB, so replacing the identifier
    with that broader family would create a different scope error.
  target_ids:
  - GO:0045275
  field_paths:
  - components[component_id=rieske_iron_sulfur_subunit].grounding
  - components[component_id=rieske_iron_sulfur_subunit].evidence[reference=InterPro:IPR006317].notes
  - causal_graphs[graph_id=complex_iii_quinol_cytochrome_c_coupling].nodes[node_id=rieske_iron_sulfur_subunit].grounding
  evidence_ids:
  - native
  - history
  - prior
  - sources
  - validation
  rule_id: review-checklist:component-identity-and-source-type
  native_severity: major
  normalization_reason: Wrong identifier granularity is used as formal component/node
    identity and repeated as family evidence. This is a grounding defect, not merely
    spelling; the complete complex identity and biological roles remain supported.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/respiratory_chain_complex_iii.yaml
    role: maintained scientific record
  disposition_reason: Retain the Rieske subunit label-only instead of using a domain
    as a protein-family grounding. The listed maintained fields now address this earlier
    defect; validation passed. This closes the missing qualification, representation
    or provenance issue, not any underlying scientific uncertainty documented in the
    record.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261012T102837Z-complex-iii-rieske-entry-type
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2308
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
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261012T102837Z-complex-iii-rieske-entry-type
  relationship: Scoped successor for the explicitly cited finding occurrences only
links:
- https://github.com/CultureBotAI/CellStructureMech/issues/2308
- https://github.com/CultureBotAI/CellStructureMech/pull/2296
```
