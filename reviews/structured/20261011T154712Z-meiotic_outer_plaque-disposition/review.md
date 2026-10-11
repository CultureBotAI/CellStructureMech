# meiotic outer plaque: saved finding disposition

- Review: 20261011T154712Z-meiotic_outer_plaque-disposition
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T15:32:26Z
- Finished UTC: 2026-10-11T15:47:12Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Exact saved finding resolved; original observation, scientific boundaries and PROPOSED status retained.

## Scope And Provenance

Exact finding reassessment and surrounding-claim preservation, not another whole-record review.

Selection: 20261011T152744Z-meiotic_outer_plaque-audit
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 5d7ac1d3308684bbf0f9ab51e89573491dff73ee.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:meiotic_outer_plaque | data/structures/cytoskeleton/meiotic_outer_plaque.yaml | maintained | meiotic outer plaque |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| meiotic_outer_plaque-schema | passed | True | cellstructuremech:meiotic_outer_plaque | Actual deterministic check passed; scientific support assessed separately. |
| meiotic_outer_plaque-strict | passed | True | cellstructuremech:meiotic_outer_plaque | Actual deterministic check passed; scientific support assessed separately. |
| meiotic_outer_plaque-snippets | passed | True | cellstructuremech:meiotic_outer_plaque | No verbatim snippets; paraphrases assessed separately against inspected text. |
| history | passed | True | cellstructuremech:meiotic_outer_plaque | Actual deterministic check passed; scientific support assessed separately. |
| labels | passed | True | cellstructuremech:meiotic_outer_plaque | id↔label correspondence summary:<br>          OK_CANONICAL: 3544<br>            OK_SYNONYM: 50<br>          OK_EXCEPTION: 6<br>    SKIPPED_NO_ADAPTER: 603<br><br>✅ All id↔label pairs correspond. |
| traits | passed | True | cellstructuremech:meiotic_outer_plaque | Actual deterministic check passed; scientific support assessed separately. |
| curies | passed | True | cellstructuremech:meiotic_outer_plaque | resolver control: every resolver accepts a known id and rejects a fabricated one<br><br>identifier liveness summary:<br>  OK             4014<br>  SKIPPED         251<br><br>Every identifier resolves at its issuing authority. |
| focused | passed | True | cellstructuremech:meiotic_outer_plaque | ..............................                                           [100%]<br>30 passed in 50.85s |
| reviews | passed | True | cellstructuremech:meiotic_outer_plaque | Actual deterministic check passed; scientific support assessed separately. |
| diff | passed | True | cellstructuremech:meiotic_outer_plaque | Actual deterministic check passed; scientific support assessed separately. |
| release-qc-final | passed | True | cellstructuremech:meiotic_outer_plaque | Actual deterministic check passed; scientific support assessed separately. |
| Initial full-QC attempt | failed | False | cellstructuremech:meiotic_outer_plaque | Stopped at I001 in the newly added regression test; extra blank line corrected, and the separately retained full-QC rerun passed. |

## Scientific And Domain Assessments

### Correct the Nickas 2003 article title

evidence: supported. Targets: cellstructuremech:meiotic_outer_plaque.

The Nickas 2003 evidence note now gives the correct Prospore Membrane title; the DOI and all biological claims are unchanged.

## Findings

### F1: Correct the Nickas 2003 article title

minor / resolved / confirmed; issue key: meiotic-outer-plaque-nickas-2003-title.

The Nickas 2003 evidence note now gives the correct Prospore Membrane title; the DOI and all biological claims are unchanged.

Disposition: The Nickas 2003 evidence note now gives the correct Prospore Membrane title; the DOI and all biological claims are unchanged. Verified by inspected primary text/metadata, bounded diff, red/green regressions and full local QC.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/meiotic_outer_plaque.yaml | context_only | Entire corrected YAML reread; bounded scientific change and actual appended history verified. |
| rules | docs/CURATION.md | context_only | Source support and species/stage scope apply to each material claim. |
| history | /private/tmp/csm-review-20261011T151709Z/meiotic_outer_plaque-discussion-history.json | context_only | Committed discussion and inline-history versions inspected; earlier decisions preserved. |
| history-0 | history/records/meiotic_outer_plaque/2026-09-29T121959Z-codex-8ab09f.yaml | context_only | Append-only original history inspected. |
| legacy-0 | reports/yaml_record_review/20260929T124720Z-meiotic_outer_plaque.md | context_only | Historical no-defect review inspected; not a canonical predecessor or proof of scientific correctness. |
| predecessors | /private/tmp/csm-review-20261011T151709Z/exact-target-predecessors.json | context_only | Ignored-inclusive complete canonical scan found no exact-target predecessor. |
| issue-search | /private/tmp/csm-review-20261011T151709Z/spb-issues.log | context_only | All-state SPB issue search inspected; historical issues concern other defects, not this finding. |
| exact-issue-search | /private/tmp/csm-review-20261011T151709Z/meiotic_outer_plaque-issues.log | context_only | Exact-slug all-state issue search checked for duplicate findings. |
| adapter | /private/tmp/csm-review-20261011T151709Z/adapter.log | context_only | Live iModulonDB inventory has no matching fungal dataset; not negative biological evidence. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005628,GO:0005816,GO:0005824,GO:0005825,GO:0016020,GO:0031322,GO:0032120,GO:0032991,GO:0035974,GO:0044732,GO:0061496,GO:0061498,GO:0070057,GO:0071957,GO:0071958; Exact definitions, synonyms and typed children for cited GO terms | supports | GO identities are nonobsolete. Preserve whole SPB, old/new subtype, outer plaque, MOP remodeling process and membrane-region boundaries. |
| taxon | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; taxId, scientificName and rank | supports | Exact species identity verified; distribution support comes from the cited experimental context. |
| knop | DOI:10.1093/emboj/19.14.3657; Results, Figures 1/2/5 and Discussion | supports | Primary budding-yeast meiosis-II plaque localization, mutant and EM observations support MOP-dependent prospore-membrane initiation; the plaque is not the membrane attachment region. |
| bajgier | DOI:10.1091/mbc.12.6.1611; Abstract, Introduction and Results Spo21/outer plaque | supports | Primary Spo21 localization and deletion experiments support meiosis-specific outer-plaque remodeling, not sufficiency of one protein alone. |
| mathieson | DOI:10.1091/mbc.E10-07-0563; Results Mpc54 nonnull alleles, Figures 4-8 and exocyst recruitment | supports | SK1 mutant analyses separate intact MOP composition from loose vesicle tethering and docking/fusion; these support the bounded docking function and coarse initiation edge. FRET orientation is a model, not asserted as native stoichiometry. |
| nickas | DOI:10.1128/EC.2.3.431-445.2003; Article title; Abstract; MOP localization/mutant Results | supports | The actual article title refers to growth of the prospore membrane, not growth of the spores. Primary Ady4p/Spo74p localization and mutant observations support the retained MOP context. |
| nickas-id | DOI:10.1128/EC.2.3.431-445.2003; Exact DOI and PMID 12796288 title | supports | Publication metadata independently confirms the full article title. |
| go-search | /private/tmp/csm-review-20261011T151709Z/go-candidates-2.json | context_only | All 388 QuickGO search candidates retrieved. Outer-plaque CC and remodeling BP are related, not exact MOP identities. |
| predecessor | reviews/structured/20261011T152744Z-meiotic_outer_plaque-audit/review.yaml | context_only | Immutable observation committed before scientific curation. |
| preservation | /private/tmp/csm-review-20261011T151709Z/preservation.json | context_only | All 907 other native records, 908 other semantic vectors and old history/review/legacy bytes preserved. |
| red | /private/tmp/csm-review-20261011T151709Z/regressions-red.log | context_only | New scope and title regressions fail on the original record bytes; identity controls pass. |
| green | /private/tmp/csm-review-20261011T151709Z/post-focused.log | context_only | Focused regressions and guarded-writer tests pass after correction. |
| edit-history | history/records/meiotic_outer_plaque/2026-10-11T152903Z-codex-782cac.yaml | context_only | Actual appended Codex EDIT links issue and predecessor. |

## Limits And Additional Notes

- Same-agent scoped disposition, not independent human approval.
- Original GO wording is preserved as an explicitly superseded scope interpretation in historical discussions; upstream GO is not changed.
- Open component groundings and existing namespace/test skips remain explicit.
- PR and separate native merge-group gates remain publication requirements; exact corrected source retained by review-base/spb-signaling-scope-20261011.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T154712Z-meiotic_outer_plaque-disposition
kind: record
repository: CultureBotAI/CellStructureMech
title: 'meiotic outer plaque: saved finding disposition'
started_at: '2026-10-11T15:32:26Z'
finished_at: '2026-10-11T15:47:12Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent scientific review, not independent human approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Exact saved finding resolved; original observation, scientific boundaries
  and PROPOSED status retained.
source:
  git_revision: 5d7ac1d3308684bbf0f9ab51e89573491dff73ee
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
  - path: README.md
    sha256: 7354ab3cdd2e80719041752e623b51c95369a7f1463ce3cf615d196448b156ce
    role: context
  - path: curation/source_queue.tsv
    sha256: 55d8fe79b5edd7d6b42bf4ca9168fe4878240417716e2f4ba423489144b89284
    role: context
  - path: data/structures/cytoskeleton/meiotic_outer_plaque.yaml
    sha256: 5482b05be175efef27e7e2acd73c2a7fb6cddbd69ebe7c430ed0adc3f858bfe9
    role: target
  - path: data/structures/cytoskeleton/meiotic_spindle_pole_body.yaml
    sha256: 2a99651652ccaa1b26dd8149e44976824366dbe2157a708fb1df0560323b8a75
    role: context
  - path: data/structures/cytoskeleton/mitotic_spindle_pole_body.yaml
    sha256: 6f26eef2c9a8c923eb0c851b4d65b90a696322095208e731be170b6b0c9f0329
    role: context
  - path: data/structures/cytoskeleton/new_mitotic_spindle_pole_body.yaml
    sha256: 33ac955370a7476c7bb3f3fca4cfc9464120890e6a3e57fcb3b32d5e2504fb82
    role: context
  - path: data/structures/cytoskeleton/old_mitotic_spindle_pole_body.yaml
    sha256: 84c9dc88c397f90a6c90dc61031b9f5334baa65580eaecc16cc851cacc54840b
    role: context
  - path: data/structures/cytoskeleton/outer_plaque_of_spindle_pole_body.yaml
    sha256: 2aa7db5e2c632a9934dda8fbc3c57a85d1742c6aa7322e769f6f162103f17142
    role: context
  - path: data/structures/cytoskeleton/spindle_pole_body.yaml
    sha256: 50885e021c246e17e29beb27f7dc98e37ee4d34878648fea4fd8b565bbb2fc78
    role: context
  - path: data/structures/cytoskeleton/spindle_pole_body_duplication_plaque.yaml
    sha256: e321abc96c81de9d3b524b7a68e2cefc4f28aaf72df105b42c96e1c6b8e994c3
    role: context
  - path: data/structures/cytoskeleton/spindle_pole_body_satellite.yaml
    sha256: a6a16f2dc3c09895fb7f4af93e1cad023c01b75dd424b99a1177ce93b516acb3
    role: context
  - path: data/structures/spore/prospore_membrane_spindle_pole_body_attachment_site.yaml
    sha256: 7349483b810c10d202f0288406bd16468b713c8688c61238d3ce6d6d94222396
    role: context
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
  - path: history/records/meiotic_outer_plaque/2026-09-29T121959Z-codex-8ab09f.yaml
    sha256: 67ec238a7d0a73195a783af8ba069dd14578f5ae18cf9279bed51bef5d7deefc
    role: context
  - path: history/records/meiotic_outer_plaque/2026-10-11T152903Z-codex-782cac.yaml
    sha256: 40b77ffc371fab998603d9c9688f19e6f976b9a4d3abbe6f95cef0c111c508cc
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reports/yaml_record_review/20260929T124720Z-meiotic_outer_plaque.md
    sha256: 7afea07b70681e9da37f7f0c709e923ecb3338b44c8cb279d522f95cbc9b3e4c
    role: context
  - path: reviews/structured/20261011T152744Z-meiotic_outer_plaque-audit/review.yaml
    sha256: 1cef15b7b02e5a49d84d31392d6cf28c077aaa978ef587d06d529136f2d54ba3
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: tests/test_spb_evidence_scope.py
    sha256: a699b0611308d4062f7a9241e33a7294658987d048d5d8f5fb56ae88c23cd49e
    role: context
targets:
- target_id: cellstructuremech:meiotic_outer_plaque
  path: data/structures/cytoskeleton/meiotic_outer_plaque.yaml
  label: meiotic outer plaque
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/meiotic_outer_plaque.yaml
    role: maintained scientific record
scope:
  description: Exact finding reassessment and surrounding-claim preservation, not
    another whole-record review.
  selection: 20261011T152744Z-meiotic_outer_plaque-audit
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:meiotic_outer_plaque
checks:
- check_id: meiotic_outer_plaque-schema
  name: meiotic_outer_plaque-schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:meiotic_outer_plaque
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/meiotic_outer_plaque.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T15:29:56Z to 2026-10-11T15:29:59Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: meiotic_outer_plaque-strict
  name: meiotic_outer_plaque-strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:meiotic_outer_plaque
  command: .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/meiotic_outer_plaque.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T15:29:59Z to 2026-10-11T15:30:04Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: meiotic_outer_plaque-snippets
  name: meiotic_outer_plaque-snippets
  status: passed
  required: true
  target_ids:
  - cellstructuremech:meiotic_outer_plaque
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/cytoskeleton/meiotic_outer_plaque.yaml
    --report /private/tmp/csm-review-20261011T151709Z/post-meiotic_outer_plaque-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: No verbatim snippets; paraphrases assessed separately against inspected
    text.
  scope_note: 2026-10-11T15:30:04Z to 2026-10-11T15:30:29Z; log SHA-256 ce3f8b903c129e79d003c3769d89f364c4afeb3dcf52c486d926dbc4ede9f157
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - cellstructuremech:meiotic_outer_plaque
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T15:30:29Z to 2026-10-11T15:30:46Z; log SHA-256 5176da9b48957f964a8a859b60ee792cb11f0923ef13345fbc9515affa329825
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - cellstructuremech:meiotic_outer_plaque
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: "id↔label correspondence summary:\n          OK_CANONICAL: 3544\n     \
    \       OK_SYNONYM: 50\n          OK_EXCEPTION: 6\n    SKIPPED_NO_ADAPTER: 603\n\
    \n✅ All id↔label pairs correspond."
  scope_note: 2026-10-11T15:30:46Z to 2026-10-11T15:32:26Z; log SHA-256 d423103555a6a5b538a7c811a73a29c24ed0e5a2eae00d1bb94715295f23f7cb
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - cellstructuremech:meiotic_outer_plaque
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T15:32:26Z to 2026-10-11T15:32:46Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - cellstructuremech:meiotic_outer_plaque
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: "resolver control: every resolver accepts a known id and rejects a fabricated\
    \ one\n\nidentifier liveness summary:\n  OK             4014\n  SKIPPED      \
    \   251\n\nEvery identifier resolves at its issuing authority."
  scope_note: 2026-10-11T15:32:46Z to 2026-10-11T15:33:37Z; log SHA-256 ee1c5f2e78a2d29fcb6781a8ecd722934376595042d2cc261b4465b361d19b79
- check_id: focused
  name: focused
  status: passed
  required: true
  target_ids:
  - cellstructuremech:meiotic_outer_plaque
  command: .venv/bin/python -m pytest -q tests/test_spb_evidence_scope.py tests/test_write_validated.py
  exit_code: 0
  expected_exit_code: 0
  summary: '..............................                                           [100%]

    30 passed in 50.85s'
  scope_note: 2026-10-11T15:33:37Z to 2026-10-11T15:34:29Z; log SHA-256 174760f755eeea4184bb2038e5ff7740ce9e419b2e3ae9eb352100e9620ee805
- check_id: reviews
  name: reviews
  status: passed
  required: true
  target_ids:
  - cellstructuremech:meiotic_outer_plaque
  command: .venv/bin/python scripts/record_review.py check --base 569bf3bbe4e887f7072f50da9a6df010958cc312
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T15:34:29Z to 2026-10-11T15:36:20Z; log SHA-256 cb3b6a6344229f3dbee8553ba36a486b6b0581ce3ce4a6438b4d6a63360f0bf4
- check_id: diff
  name: diff
  status: passed
  required: true
  target_ids:
  - cellstructuremech:meiotic_outer_plaque
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T15:36:21Z to 2026-10-11T15:36:21Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- check_id: release-qc-final
  name: release-qc-final
  status: passed
  required: true
  target_ids:
  - cellstructuremech:meiotic_outer_plaque
  command: just qc
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T15:31:44Z to 2026-10-11T15:46:30Z; log SHA-256 0be0db319e827e58ac455a48dbe9e36f19eb8187c552fbe83dd6137aa83a0346
- check_id: initial-qc-lint
  name: Initial full-QC attempt
  status: failed
  required: false
  target_ids:
  - cellstructuremech:meiotic_outer_plaque
  command: just qc
  exit_code: 1
  expected_exit_code: 0
  summary: Stopped at I001 in the newly added regression test; extra blank line corrected,
    and the separately retained full-QC rerun passed.
  scope_note: 2026-10-11T15:31:05Z to 2026-10-11T15:31:06Z; log SHA-256 0b21623f486e9aab0f423375af02c5d05a55aab15db431d289419b6be11ac48f
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/meiotic_outer_plaque.yaml
  accessed_at: '2026-10-11T15:47:12Z'
  snapshot_sha256: 5482b05be175efef27e7e2acd73c2a7fb6cddbd69ebe7c430ed0adc3f858bfe9
  support: context_only
  summary: Entire corrected YAML reread; bounded scientific change and actual appended
    history verified.
- evidence_id: rules
  kind: record_content
  reference: docs/CURATION.md
  accessed_at: '2026-10-11T15:27:44Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  support: context_only
  summary: Source support and species/stage scope apply to each material claim.
- evidence_id: history
  kind: record_content
  reference: /private/tmp/csm-review-20261011T151709Z/meiotic_outer_plaque-discussion-history.json
  accessed_at: '2026-10-11T15:27:44Z'
  snapshot_sha256: 0110f5ede1b64ab372878b45e0b557425b4c1da0f06ba4c0c1b9828d565520cb
  support: context_only
  summary: Committed discussion and inline-history versions inspected; earlier decisions
    preserved.
- evidence_id: history-0
  kind: record_content
  reference: history/records/meiotic_outer_plaque/2026-09-29T121959Z-codex-8ab09f.yaml
  accessed_at: '2026-10-11T15:27:44Z'
  snapshot_sha256: 67ec238a7d0a73195a783af8ba069dd14578f5ae18cf9279bed51bef5d7deefc
  support: context_only
  summary: Append-only original history inspected.
- evidence_id: legacy-0
  kind: prior_review
  reference: reports/yaml_record_review/20260929T124720Z-meiotic_outer_plaque.md
  accessed_at: '2026-10-11T15:27:44Z'
  snapshot_sha256: 7afea07b70681e9da37f7f0c709e923ecb3338b44c8cb279d522f95cbc9b3e4c
  support: context_only
  summary: Historical no-defect review inspected; not a canonical predecessor or proof
    of scientific correctness.
- evidence_id: predecessors
  kind: validation
  reference: /private/tmp/csm-review-20261011T151709Z/exact-target-predecessors.json
  accessed_at: '2026-10-11T15:27:44Z'
  snapshot_sha256: c6bd0214502e1a9a8f241ffda0fd6afecd2faa69f57ad244e68165a7ddbeb84d
  support: context_only
  summary: Ignored-inclusive complete canonical scan found no exact-target predecessor.
- evidence_id: issue-search
  kind: validation
  reference: /private/tmp/csm-review-20261011T151709Z/spb-issues.log
  accessed_at: '2026-10-11T15:27:44Z'
  snapshot_sha256: 105161b4440092ef6565bcbb62b383fbf06e4d40dfbc72900cf4bb1db64d196a
  support: context_only
  summary: All-state SPB issue search inspected; historical issues concern other defects,
    not this finding.
- evidence_id: exact-issue-search
  kind: validation
  reference: /private/tmp/csm-review-20261011T151709Z/meiotic_outer_plaque-issues.log
  accessed_at: '2026-10-11T15:27:44Z'
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
  support: context_only
  summary: Exact-slug all-state issue search checked for duplicate findings.
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/csm-review-20261011T151709Z/adapter.log
  accessed_at: '2026-10-11T15:27:44Z'
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
  support: context_only
  summary: Live iModulonDB inventory has no matching fungal dataset; not negative
    biological evidence.
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005628,GO:0005816,GO:0005824,GO:0005825,GO:0016020,GO:0031322,GO:0032120,GO:0032991,GO:0035974,GO:0044732,GO:0061496,GO:0061498,GO:0070057,GO:0071957,GO:0071958
  locator: Exact definitions, synonyms and typed children for cited GO terms
  accessed_at: '2026-10-11T15:18:34Z'
  snapshot_sha256: f5c5843c474b3bbfdbf959e41465081d3693520ae46a1fdd1c2cb7a288cb65fa
  support: supports
  summary: GO identities are nonobsolete. Preserve whole SPB, old/new subtype, outer
    plaque, MOP remodeling process and membrane-region boundaries.
- evidence_id: taxon
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: taxId, scientificName and rank
  accessed_at: '2026-10-11T15:18:35Z'
  snapshot_sha256: c4e5f7b0462251e0d309ae5ad59f47eb6b3846cbe9fcb8506648a7898d4ad1a8
  support: supports
  summary: Exact species identity verified; distribution support comes from the cited
    experimental context.
- evidence_id: knop
  kind: primary_source
  reference: DOI:10.1093/emboj/19.14.3657
  locator: Results, Figures 1/2/5 and Discussion
  accessed_at: '2026-10-11T15:18:37Z'
  snapshot_sha256: 0772e1f585db789595bfe7e0e3e1eadf2bdca335d45902f203182ba791d713f8
  support: supports
  summary: Primary budding-yeast meiosis-II plaque localization, mutant and EM observations
    support MOP-dependent prospore-membrane initiation; the plaque is not the membrane
    attachment region.
- evidence_id: bajgier
  kind: primary_source
  reference: DOI:10.1091/mbc.12.6.1611
  locator: Abstract, Introduction and Results Spo21/outer plaque
  accessed_at: '2026-10-11T15:18:56Z'
  snapshot_sha256: 51a6f2c3a7a7fd5ae4a21a0b8f146335c621fd1924cb0520d5c9775979376650
  support: supports
  summary: Primary Spo21 localization and deletion experiments support meiosis-specific
    outer-plaque remodeling, not sufficiency of one protein alone.
- evidence_id: mathieson
  kind: primary_source
  reference: DOI:10.1091/mbc.E10-07-0563
  locator: Results Mpc54 nonnull alleles, Figures 4-8 and exocyst recruitment
  accessed_at: '2026-10-11T15:17:50Z'
  snapshot_sha256: 5253a7b379b09c33dbfc881b05ba2cd5fd2364e90185b0505c668e65373f0157
  support: supports
  summary: SK1 mutant analyses separate intact MOP composition from loose vesicle
    tethering and docking/fusion; these support the bounded docking function and coarse
    initiation edge. FRET orientation is a model, not asserted as native stoichiometry.
- evidence_id: nickas
  kind: primary_source
  reference: DOI:10.1128/EC.2.3.431-445.2003
  locator: Article title; Abstract; MOP localization/mutant Results
  accessed_at: '2026-10-11T15:18:56Z'
  snapshot_sha256: 348c9ae05c4f86e2a42c1424b23fcff96bcd31b6748af5ddf9a163b7391596d5
  support: supports
  summary: The actual article title refers to growth of the prospore membrane, not
    growth of the spores. Primary Ady4p/Spo74p localization and mutant observations
    support the retained MOP context.
- evidence_id: nickas-id
  kind: authority
  reference: DOI:10.1128/EC.2.3.431-445.2003
  locator: Exact DOI and PMID 12796288 title
  accessed_at: '2026-10-11T15:18:00Z'
  snapshot_sha256: 5c1b644cd05bf219478e1c8a1da2dd42fdeed6caf7768ef73e5c597b53f31272
  support: supports
  summary: Publication metadata independently confirms the full article title.
- evidence_id: go-search
  kind: validation
  reference: /private/tmp/csm-review-20261011T151709Z/go-candidates-2.json
  accessed_at: '2026-10-11T15:27:44Z'
  snapshot_sha256: 8bb336c878501b7f480e21da991a41a0f581cb1d743038c4da9694f2f01a0495
  support: context_only
  summary: All 388 QuickGO search candidates retrieved. Outer-plaque CC and remodeling
    BP are related, not exact MOP identities.
- evidence_id: predecessor
  kind: prior_review
  reference: reviews/structured/20261011T152744Z-meiotic_outer_plaque-audit/review.yaml
  accessed_at: '2026-10-11T15:47:12Z'
  snapshot_sha256: 1cef15b7b02e5a49d84d31392d6cf28c077aaa978ef587d06d529136f2d54ba3
  support: context_only
  summary: Immutable observation committed before scientific curation.
- evidence_id: preservation
  kind: validation
  reference: /private/tmp/csm-review-20261011T151709Z/preservation.json
  accessed_at: '2026-10-11T15:47:12Z'
  snapshot_sha256: c4986880eb3cb928b5e12c1bfe3fb9ef698ab657344b5b6e5671009116305372
  support: context_only
  summary: All 907 other native records, 908 other semantic vectors and old history/review/legacy
    bytes preserved.
- evidence_id: red
  kind: validation
  reference: /private/tmp/csm-review-20261011T151709Z/regressions-red.log
  accessed_at: '2026-10-11T15:47:12Z'
  snapshot_sha256: 45dfb9266955d80ffc725f303a73939572a63fad7435051c7ef0bbdf778ec430
  support: context_only
  summary: New scope and title regressions fail on the original record bytes; identity
    controls pass.
- evidence_id: green
  kind: validation
  reference: /private/tmp/csm-review-20261011T151709Z/post-focused.log
  accessed_at: '2026-10-11T15:47:12Z'
  snapshot_sha256: 174760f755eeea4184bb2038e5ff7740ce9e419b2e3ae9eb352100e9620ee805
  support: context_only
  summary: Focused regressions and guarded-writer tests pass after correction.
- evidence_id: edit-history
  kind: record_content
  reference: history/records/meiotic_outer_plaque/2026-10-11T152903Z-codex-782cac.yaml
  accessed_at: '2026-10-11T15:47:12Z'
  snapshot_sha256: 40b77ffc371fab998603d9c9688f19e6f976b9a4d3abbe6f95cef0c111c508cc
  support: context_only
  summary: Actual appended Codex EDIT links issue and predecessor.
assessments:
- assessment_id: resolved
  area: evidence
  topic: Correct the Nickas 2003 article title
  outcome: supported
  target_ids:
  - cellstructuremech:meiotic_outer_plaque
  evidence_ids:
  - record
  - nickas
  - nickas-id
  - rules
  - predecessor
  - preservation
  - red
  - green
  - edit-history
  summary: The Nickas 2003 evidence note now gives the correct Prospore Membrane title;
    the DOI and all biological claims are unchanged.
findings:
- finding_id: F1
  issue_key: meiotic-outer-plaque-nickas-2003-title
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: Correct the Nickas 2003 article title
  description: The Nickas 2003 evidence note now gives the correct Prospore Membrane
    title; the DOI and all biological claims are unchanged.
  target_ids:
  - cellstructuremech:meiotic_outer_plaque
  field_paths:
  - evidence[reference=DOI:10.1128/EC.2.3.431-445.2003].notes
  evidence_ids:
  - record
  - nickas
  - nickas-id
  - rules
  - predecessor
  - preservation
  - red
  - green
  - edit-history
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/meiotic_outer_plaque.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: minor
  normalization_reason: Nonblocking citation-title inaccuracy; valid DOI and supported
    scientific claims do not justify major severity.
  disposition_reason: The Nickas 2003 evidence note now gives the correct Prospore
    Membrane title; the DOI and all biological claims are unchanged. Verified by inspected
    primary text/metadata, bounded diff, red/green regressions and full local QC.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261011T152744Z-meiotic_outer_plaque-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2221
actions: []
limitations:
- Same-agent scoped disposition, not independent human approval.
- Original GO wording is preserved as an explicitly superseded scope interpretation
  in historical discussions; upstream GO is not changed.
- Open component groundings and existing namespace/test skips remain explicit.
- PR and separate native merge-group gates remain publication requirements; exact
  corrected source retained by review-base/spb-signaling-scope-20261011.
links:
- https://github.com/CultureBotAI/CellStructureMech/issues/2221
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261011T152744Z-meiotic_outer_plaque-audit
  relationship: Resolves exact predecessor without replacing it.
```
