# intraconoid microtubule: whole-record scientific review

- Review: 20261011T194853Z-intraconoid_microtubule-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T19:36:09Z
- Finished UTC: 2026-10-11T19:48:53Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Whole native record reviewed; concrete identity, topology or evidence-scope findings saved before scientific edits.

## Scope And Provenance

Entire native YAML: identity, definition, synonyms, hierarchy/parthood, components/essentiality, taxa/examples, functions, all graph relations, evidence, discussions and both history surfaces.

Selection: One exact record in the 909-record review goal; other records have separate coverage.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base decd7c3bffae01c2096c071dc503662b9e71537e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0033289 | data/structures/cytoskeleton/intraconoid_microtubule.yaml | maintained | intraconoid microtubule |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0033289 | Actual deterministic check passed; scientific support assessed separately. |
| strict | passed | True | GO:0033289 | Actual deterministic check passed; scientific support assessed separately. |
| snippets | passed | True | GO:0033289 | No verbatim snippets; paraphrases assessed separately against inspected text. |
| history | passed | True | GO:0033289 | Actual deterministic check passed; scientific support assessed separately. |
| labels | passed | True | GO:0033289 | id↔label correspondence summary:<br>          OK_CANONICAL: 3544<br>            OK_SYNONYM: 50<br>          OK_EXCEPTION: 6<br>    SKIPPED_NO_ADAPTER: 603<br><br>✅ All id↔label pairs correspond. |
| traits | passed | True | GO:0033289 | Actual deterministic check passed; scientific support assessed separately. |
| curies | passed | True | GO:0033289 | resolver control: every resolver accepts a known id and rejects a fabricated one<br><br>identifier liveness summary:<br>  OK             4015<br>  SKIPPED         251<br><br>Every identifier resolves at its issuing authority. |
| reviews | passed | True | GO:0033289 | Actual deterministic check passed; scientific support assessed separately. |
| diff | passed | True | GO:0033289 | Actual deterministic check passed; scientific support assessed separately. |
| contract | passed | True | GO:0033289 | ....                                                                     [100%]<br>4 passed in 103.38s (0:01:43) |
| Exact-baseline native CI QC | passed | True | GO:0033289 | Exact-baseline merge-group full QC verified: 917 passed, 3 skipped. Not a new local full-QC run. |

## Scientific And Domain Assessments

### Claim-by-claim biological scope

evidence: concern. Targets: GO:0033289.

GO microtubule is-a and apical-complex part_of, alpha/beta-tubulin membership, two conventional Toxoplasma microtubules, scaffold context and distinction from ribbon-like conoid fibers are supported. Structural essentiality of tubulin is not organism viability. Only the over-specific ring projection edge and matching prose need correction; original end-factor uncertainty and #1284/#1285 fixes remain valid.

### Prior rationale and intentional unknowns

completeness: supported. Targets: GO:0033289.

No image, dataset, measurement, accession, trait or pathway field is asserted here. Optional missing fields and exact-family grounding TODOs are not findings. Preserve original discussions, dates, both history surfaces and PROPOSED status; deterministic checks are not scientific approval.

## Findings

### F1: Remove the unsupported anterior-ring endpoint inference

major / open / confirmed; issue key: intraconoid-microtubule-anterior-ring-projection.

GO:0033289 says projects through the polar ring without an endpoint or explicit GO ring target. The native graph adds distal ends and grounds the ring to the anterior fiber-origin GO:0020031, while Hu 2006 claim-local text only supports the pair inside the conoid. Li 2023 Results/Figure 2 resolves basal-directed ICMT extension, and modern figures distinguish PCR from APR. The generic source phrase cannot justify this precise anterior-ring relation.

## Recommended Actions And Acceptance Checks

### A1

Remove the unsupported anterior-ring endpoint inference

- Retain the GO definition as attributed authority, but remove the over-specific anterior-ring projection edge and narrow matching prose to supported conoid-center topology. Append the nomenclature/end-geometry limitation; do not invent an alternative ring attachment or organizer.
- Use guarded writer and actual Codex EDIT history; preserve original observations, history, rationale and PROPOSED status. Pass focused regressions and native QC.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/intraconoid_microtubule.yaml | context_only | Entire native YAML read before judgement; inspected bytes remain unchanged. |
| rules | docs/CURATION.md | context_only | Exact structure identity, narrow source support and conserved component scope. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml | context_only | Components are molecular building blocks; essentiality concerns formation, not survival. COMMON denotes most members, not merely homologous proteins. |
| history | /private/tmp/csm-review-20261011T193501Z/intraconoid_microtubule-discussion-history.json | context_only | All committed discussion and inline-history versions read, including prior evidence-placement rationale. |
| predecessors | /private/tmp/csm-review-20261011T193501Z/exact-target-predecessors.json | context_only | Ignored-inclusive canonical search found no exact-target predecessor. |
| identity | /private/tmp/csm-review-20261011T193501Z/identity-matches.json | context_only | Ignored-inclusive native identity enumeration distinguishes both GO rings, conoid and microtubules. |
| adapter | /private/tmp/csm-review-20261011T193501Z/adapter.log | context_only | Fresh 28-dataset iModulonDB inventory has no applicable Toxoplasma, Apicomplexa or Trypanosoma dataset; not negative biological evidence. |
| append-history-0 | history/records/intraconoid_microtubule/2026-09-22T131003Z-codex-0e4ca6.yaml | context_only | Original append-only event inspected; author metadata and dates preserved. |
| append-history-1 | history/records/intraconoid_microtubule/2026-09-22T132053Z-codex-8c24a0.yaml | context_only | Original append-only event inspected; author metadata and dates preserved. |
| issues-conoid | /private/tmp/csm-review-20261011T193501Z/conoid-all-issues.log | context_only | All-state issue search; relevant #325/#327/#1278/#1279/#1284/#1285 are closed, distinct earlier scope fixes. |
| issues-polar-ring | /private/tmp/csm-review-20261011T193501Z/polar-ring-all-issues.log | context_only | All-state issue search; relevant #325/#327/#1278/#1279/#1284/#1285 are closed, distinct earlier scope fixes. |
| issues-subpellicular | /private/tmp/csm-review-20261011T193501Z/subpellicular-all-issues.log | context_only | All-state issue search; relevant #325/#327/#1278/#1279/#1284/#1285 are closed, distinct earlier scope fixes. |
| issues-basal-ring | /private/tmp/csm-review-20261011T193501Z/basal-ring-all-issues.log | context_only | All-state issue search; relevant #325/#327/#1278/#1279/#1284/#1285 are closed, distinct earlier scope fixes. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0020032,GO:0020031,GO:0020010,GO:0033289,GO:0020025,GO:0005874,GO:0020007,GO:0005856,GO:0070258; Nine exact cellular-component definitions, synonyms and typed relations | supports | GO anterior fiber-origin and posterior SPMT-origin definitions must not be replaced by a name-only APR match; the basal preconoidal synonym conflicts with primary anatomy. |
| taxon-5811 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5811; Exact taxon identity | supports | Taxonomic identity verified; this is not a structure-prevalence measurement. |
| paper-id-2 | DOI:10.1083/jcb.200112086; Exact DOI/PMID/title and abstract | supports | A novel polymer of tubulin forms the conoid of Toxoplasma gondii. |
| paper-2 | DOI:10.1083/jcb.200112086; Primary Results, Discussion and relevant figure captions; claim-local inspection | supports | GO microtubule is-a and apical-complex part_of, alpha/beta-tubulin membership, two conventional Toxoplasma microtubules, scaffold context and distinction from ribbon-like conoid fibers are supported. Structural essentiality of tubulin is not organism viability. Only the over-specific ring projection edge and matching prose need correction; original end-factor uncertainty and #1284/#1285 fixes remain valid. |
| paper-id-6 | DOI:10.1371/journal.ppat.0020013; Exact DOI/PMID/title and abstract | supports | Cytoskeletal components of an invasion machine--the apical complex of Toxoplasma gondii. |
| paper-6 | DOI:10.1371/journal.ppat.0020013; Primary Results, Discussion and relevant figure captions; claim-local inspection | supports | GO microtubule is-a and apical-complex part_of, alpha/beta-tubulin membership, two conventional Toxoplasma microtubules, scaffold context and distinction from ribbon-like conoid fibers are supported. Structural essentiality of tubulin is not organism viability. Only the over-specific ring projection edge and matching prose need correction; original end-factor uncertainty and #1284/#1285 fixes remain valid. |
| hu2002-figure | DOI:10.1083/jcb.200112086; Figure 1, visually inspected | supports | Historical anterior ring above conoid and lower SPMT-origin ring are distinct; positions differ with conoid state. |
| hu2006-figure | DOI:10.1371/journal.ppat.0020013; Figure 1, visually inspected | supports | Historical anterior ring above conoid and lower SPMT-origin ring are distinct; positions differ with conoid state. |
| li2023 | DOI:10.1002/advs.202206595; Results on microtubule orientation, Figure 2 and Methods | supports | Primary cryo-ET of 13 ICMTs finds basal-directed extension from within the conoid, not an established distal projection through the GO anterior fiber-origin ring. |
| li-figure | DOI:10.1002/advs.202206595; Figure 2C/D, visually inspected | supports | ICMTs extend basally from within the conoid; PCR and APR are explicitly separate structures. |

## Limits And Additional Notes

- Same-agent whole-native-record review, not independent human approval or raw-data reanalysis.
- Terminology differs across GO, historical polar-ring papers and modern multilayer APR models. No automatic whole-APR to GO:0020032 equivalence is made.
- QuickGO legacy constraint/documentation URLs returned HTML despite status 200; they were not accepted as JSON evidence. OLS exact identity and linked taxon relation were checked separately. The GO definition reference to a Trypanosoma paper remains an upstream source conflict, not license to expand this apicomplexan record.
- Tran 2010 Europe PMC full-text request failed; actual NCBI XML was retrieved and inspected. Seven other native sources were read through primary XML or the author-hosted PDF; no search snippet was treated as proof.
- Full QC is verified exact-baseline CI; local schema/strict, history, label, CURIE, trait, review and contract checks also ran. Label checks skipped 603 unsupported adapter pairs and CURIE checks skipped 251 identifiers; three baseline tests were skipped. No verbatim snippets exist in these five records.
- The fresh iModulonDB inventory is inapplicable; absence there is not structural absence. No optional unknown was promoted to an issue.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T194853Z-intraconoid_microtubule-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'intraconoid microtubule: whole-record scientific review'
started_at: '2026-10-11T19:36:09Z'
finished_at: '2026-10-11T19:48:53Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent source and record review, not independent human scientific
    approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Whole native record reviewed; concrete identity, topology or evidence-scope
  findings saved before scientific edits.
source:
  git_revision: decd7c3bffae01c2096c071dc503662b9e71537e
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
  - path: data/structures/cytoskeleton/basal_ring_of_apical_complex.yaml
    sha256: 4d8769618a8ff800cecb0819f7610b513a91a941f484206df8d77b045d1ae3a7
    role: context
  - path: data/structures/cytoskeleton/conoid.yaml
    sha256: 465b1feb203f89341563f9ceec50c0befa64214ab3108841924374cd6ff2ecbe
    role: context
  - path: data/structures/cytoskeleton/intraconoid_microtubule.yaml
    sha256: 21869b3ca8b067a21e86c069cb8a4aebf5a10638a6355ed814a8c7fcab61cedd
    role: target
  - path: data/structures/cytoskeleton/microtubule.yaml
    sha256: 29404191864964cf5b86c3894c7b942d63b83fc4bb1b6b461d7677baad6af305
    role: context
  - path: data/structures/cytoskeleton/polar_ring_of_apical_complex.yaml
    sha256: 88bff381d9f8bb1063acf717d83575b7fa71b60b8e3dc1acc80d73f55df50a2a
    role: context
  - path: data/structures/cytoskeleton/subpellicular_microtubule.yaml
    sha256: 235afbaa4a16ea78b26c182e19c4b9c34d301e3a47284ec9969b1ddbafc44c72
    role: context
  - path: data/structures/other/apical_complex.yaml
    sha256: 72b670707751292b450e4c8bccddb25a4a14e482fc0eaaa85975681694f55952
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
  - path: history/records/intraconoid_microtubule/2026-09-22T131003Z-codex-0e4ca6.yaml
    sha256: 7b95a5c5a1d43b55c9e40acf1df5d37cb6e97fcf4acd189e956243c0a106be40
    role: context
  - path: history/records/intraconoid_microtubule/2026-09-22T132053Z-codex-8c24a0.yaml
    sha256: 8f045d21cf424072f8998dd21ed7c29819c86f89c292a299ffefd9bbeab5d1fc
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
targets:
- target_id: GO:0033289
  path: data/structures/cytoskeleton/intraconoid_microtubule.yaml
  label: intraconoid microtubule
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/intraconoid_microtubule.yaml
    role: maintained scientific record
scope:
  description: 'Entire native YAML: identity, definition, synonyms, hierarchy/parthood,
    components/essentiality, taxa/examples, functions, all graph relations, evidence,
    discussions and both history surfaces.'
  selection: One exact record in the 909-record review goal; other records have separate
    coverage.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0033289
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - GO:0033289
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/intraconoid_microtubule.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T19:41:24Z to 2026-10-11T19:41:29Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - GO:0033289
  command: .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/intraconoid_microtubule.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T19:41:29Z to 2026-10-11T19:41:37Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - GO:0033289
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/cytoskeleton/intraconoid_microtubule.yaml
    --report /private/tmp/csm-review-20261011T193501Z/intraconoid_microtubule-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: No verbatim snippets; paraphrases assessed separately against inspected
    text.
  scope_note: 2026-10-11T19:41:37Z to 2026-10-11T19:42:00Z; log SHA-256 19539338e3ec8ee46e88fd4402d57b05571ffa76495c7c8af6d9dcde78df854e
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:0033289
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T19:42:40Z to 2026-10-11T19:42:59Z; log SHA-256 c3d705502a321602dac206664f3c14d2b2e226b4b934ebd4bef80256c3249095
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - GO:0033289
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: "id↔label correspondence summary:\n          OK_CANONICAL: 3544\n     \
    \       OK_SYNONYM: 50\n          OK_EXCEPTION: 6\n    SKIPPED_NO_ADAPTER: 603\n\
    \n✅ All id↔label pairs correspond."
  scope_note: 2026-10-11T19:42:59Z to 2026-10-11T19:44:29Z; log SHA-256 d423103555a6a5b538a7c811a73a29c24ed0e5a2eae00d1bb94715295f23f7cb
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - GO:0033289
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T19:44:29Z to 2026-10-11T19:44:50Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - GO:0033289
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: "resolver control: every resolver accepts a known id and rejects a fabricated\
    \ one\n\nidentifier liveness summary:\n  OK             4015\n  SKIPPED      \
    \   251\n\nEvery identifier resolves at its issuing authority."
  scope_note: 2026-10-11T19:44:50Z to 2026-10-11T19:45:38Z; log SHA-256 72255ddb5a1980a84b6bf05228c8b8f177d78ea78d9edee2dd80b8893b7712bd
- check_id: reviews
  name: reviews
  status: passed
  required: true
  target_ids:
  - GO:0033289
  command: .venv/bin/python scripts/record_review.py check --base decd7c3bffae01c2096c071dc503662b9e71537e
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T19:45:38Z to 2026-10-11T19:46:53Z; log SHA-256 24939831179ca0b4b253d635786b31063d5047eb8f21a48a453f77c1d298bf52
- check_id: diff
  name: diff
  status: passed
  required: true
  target_ids:
  - GO:0033289
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T19:46:53Z to 2026-10-11T19:46:53Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- check_id: contract
  name: contract
  status: passed
  required: true
  target_ids:
  - GO:0033289
  command: .venv/bin/python -m pytest -q tests/test_record_review_contract.py
  exit_code: 0
  expected_exit_code: 0
  summary: '....                                                                     [100%]

    4 passed in 103.38s (0:01:43)'
  scope_note: 2026-10-11T19:37:11Z to 2026-10-11T19:38:56Z; log SHA-256 c988dfe997b3bad8a672d0456746c3a54229ef59b582a49ee58f94d63f3744e9
- check_id: qc
  name: Exact-baseline native CI QC
  status: passed
  required: true
  target_ids:
  - GO:0033289
  command: gh run view 38168116275 --repo CultureBotAI/CellStructureMech --log
  exit_code: 0
  expected_exit_code: 0
  summary: 'Exact-baseline merge-group full QC verified: 917 passed, 3 skipped. Not
    a new local full-QC run.'
  scope_note: https://github.com/CultureBotAI/CellStructureMech/actions/runs/38168116275;
    log SHA-256 29adcd56424480bd3334fe477ea668151e7c12bc0f7b99f1ab669bf677cf38a0
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/intraconoid_microtubule.yaml
  accessed_at: '2026-10-11T19:48:53Z'
  snapshot_sha256: 21869b3ca8b067a21e86c069cb8a4aebf5a10638a6355ed814a8c7fcab61cedd
  support: context_only
  summary: Entire native YAML read before judgement; inspected bytes remain unchanged.
- evidence_id: rules
  kind: record_content
  reference: docs/CURATION.md
  accessed_at: '2026-10-11T19:48:53Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  support: context_only
  summary: Exact structure identity, narrow source support and conserved component
    scope.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  accessed_at: '2026-10-11T19:48:53Z'
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
  support: context_only
  summary: Components are molecular building blocks; essentiality concerns formation,
    not survival. COMMON denotes most members, not merely homologous proteins.
- evidence_id: history
  kind: record_content
  reference: /private/tmp/csm-review-20261011T193501Z/intraconoid_microtubule-discussion-history.json
  accessed_at: '2026-10-11T19:48:53Z'
  snapshot_sha256: e491f90a65741ab42b961c376e5704bd23b94c5b5039bc56c3df043f1878bc63
  support: context_only
  summary: All committed discussion and inline-history versions read, including prior
    evidence-placement rationale.
- evidence_id: predecessors
  kind: validation
  reference: /private/tmp/csm-review-20261011T193501Z/exact-target-predecessors.json
  accessed_at: '2026-10-11T19:48:53Z'
  snapshot_sha256: d0841513bf1b0a191371501f5f3a56e12093739b0a821d29da881d298c76ef7c
  support: context_only
  summary: Ignored-inclusive canonical search found no exact-target predecessor.
- evidence_id: identity
  kind: validation
  reference: /private/tmp/csm-review-20261011T193501Z/identity-matches.json
  accessed_at: '2026-10-11T19:48:53Z'
  snapshot_sha256: ed9c902d12e2a155a62c4ab4c00a65c86590ac99122b521bc1908fd81d63a995
  support: context_only
  summary: Ignored-inclusive native identity enumeration distinguishes both GO rings,
    conoid and microtubules.
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/csm-review-20261011T193501Z/adapter.log
  accessed_at: '2026-10-11T19:48:53Z'
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
  support: context_only
  summary: Fresh 28-dataset iModulonDB inventory has no applicable Toxoplasma, Apicomplexa
    or Trypanosoma dataset; not negative biological evidence.
- evidence_id: append-history-0
  kind: record_content
  reference: history/records/intraconoid_microtubule/2026-09-22T131003Z-codex-0e4ca6.yaml
  accessed_at: '2026-10-11T19:48:53Z'
  snapshot_sha256: 7b95a5c5a1d43b55c9e40acf1df5d37cb6e97fcf4acd189e956243c0a106be40
  support: context_only
  summary: Original append-only event inspected; author metadata and dates preserved.
- evidence_id: append-history-1
  kind: record_content
  reference: history/records/intraconoid_microtubule/2026-09-22T132053Z-codex-8c24a0.yaml
  accessed_at: '2026-10-11T19:48:53Z'
  snapshot_sha256: 8f045d21cf424072f8998dd21ed7c29819c86f89c292a299ffefd9bbeab5d1fc
  support: context_only
  summary: Original append-only event inspected; author metadata and dates preserved.
- evidence_id: issues-conoid
  kind: validation
  reference: /private/tmp/csm-review-20261011T193501Z/conoid-all-issues.log
  accessed_at: '2026-10-11T19:48:53Z'
  snapshot_sha256: 164bcac2e5821041d6052d8b2a9d7b0808b24b08d459c4dd5811d6655e7abae7
  support: context_only
  summary: 'All-state issue search; relevant #325/#327/#1278/#1279/#1284/#1285 are
    closed, distinct earlier scope fixes.'
- evidence_id: issues-polar-ring
  kind: validation
  reference: /private/tmp/csm-review-20261011T193501Z/polar-ring-all-issues.log
  accessed_at: '2026-10-11T19:48:53Z'
  snapshot_sha256: 7a031d03103036fe2c21b65176b9b5467795b5ac57920179bef06c46c49bda7c
  support: context_only
  summary: 'All-state issue search; relevant #325/#327/#1278/#1279/#1284/#1285 are
    closed, distinct earlier scope fixes.'
- evidence_id: issues-subpellicular
  kind: validation
  reference: /private/tmp/csm-review-20261011T193501Z/subpellicular-all-issues.log
  accessed_at: '2026-10-11T19:48:53Z'
  snapshot_sha256: 9c5646441328b9656f41ecf30951e5b2bc7f86d4098fcd4e5a291e0eaa8a74ae
  support: context_only
  summary: 'All-state issue search; relevant #325/#327/#1278/#1279/#1284/#1285 are
    closed, distinct earlier scope fixes.'
- evidence_id: issues-basal-ring
  kind: validation
  reference: /private/tmp/csm-review-20261011T193501Z/basal-ring-all-issues.log
  accessed_at: '2026-10-11T19:48:53Z'
  snapshot_sha256: d790eab41acfead93e20c8b60b5e5df1ec030d472c7901dcf95ac402ab24cc91
  support: context_only
  summary: 'All-state issue search; relevant #325/#327/#1278/#1279/#1284/#1285 are
    closed, distinct earlier scope fixes.'
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0020032,GO:0020031,GO:0020010,GO:0033289,GO:0020025,GO:0005874,GO:0020007,GO:0005856,GO:0070258
  locator: Nine exact cellular-component definitions, synonyms and typed relations
  accessed_at: '2026-10-11T19:38:04Z'
  snapshot_sha256: 4148a58bcec8ed0265ac75202c4d9f0212ae36d059ed734289e2e60437cfe22b
  support: supports
  summary: GO anterior fiber-origin and posterior SPMT-origin definitions must not
    be replaced by a name-only APR match; the basal preconoidal synonym conflicts
    with primary anatomy.
- evidence_id: taxon-5811
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5811
  locator: Exact taxon identity
  accessed_at: '2026-10-11T19:38:05Z'
  snapshot_sha256: cbb209002c87051ce78d0a34bc169d2f6623f6bbfbb21edad170d43eb16d4032
  support: supports
  summary: Taxonomic identity verified; this is not a structure-prevalence measurement.
- evidence_id: paper-id-2
  kind: primary_source
  reference: DOI:10.1083/jcb.200112086
  locator: Exact DOI/PMID/title and abstract
  accessed_at: '2026-10-11T19:39:07Z'
  snapshot_sha256: 6b818ee604c5bc4bd06629be3d318cda4d2f8e91b1363f1c622cfa9653c5bcb8
  support: supports
  summary: A novel polymer of tubulin forms the conoid of Toxoplasma gondii.
- evidence_id: paper-2
  kind: primary_source
  reference: DOI:10.1083/jcb.200112086
  locator: Primary Results, Discussion and relevant figure captions; claim-local inspection
  accessed_at: '2026-10-11T19:39:09Z'
  snapshot_sha256: c677539617169e02dc6d430a39f94635c3a114b94e880cff322d4581cb818b70
  support: supports
  summary: 'GO microtubule is-a and apical-complex part_of, alpha/beta-tubulin membership,
    two conventional Toxoplasma microtubules, scaffold context and distinction from
    ribbon-like conoid fibers are supported. Structural essentiality of tubulin is
    not organism viability. Only the over-specific ring projection edge and matching
    prose need correction; original end-factor uncertainty and #1284/#1285 fixes remain
    valid.'
- evidence_id: paper-id-6
  kind: primary_source
  reference: DOI:10.1371/journal.ppat.0020013
  locator: Exact DOI/PMID/title and abstract
  accessed_at: '2026-10-11T19:39:15Z'
  snapshot_sha256: 01d184f8d009f4db3522c1d575aac4ffe23b8d7c06d18847e868014adbd6a52c
  support: supports
  summary: Cytoskeletal components of an invasion machine--the apical complex of Toxoplasma
    gondii.
- evidence_id: paper-6
  kind: primary_source
  reference: DOI:10.1371/journal.ppat.0020013
  locator: Primary Results, Discussion and relevant figure captions; claim-local inspection
  accessed_at: '2026-10-11T19:39:16Z'
  snapshot_sha256: dae4c4fe8cc077716338da2deccb2dea30a94147adc3fd3d81f778421cda256d
  support: supports
  summary: 'GO microtubule is-a and apical-complex part_of, alpha/beta-tubulin membership,
    two conventional Toxoplasma microtubules, scaffold context and distinction from
    ribbon-like conoid fibers are supported. Structural essentiality of tubulin is
    not organism viability. Only the over-specific ring projection edge and matching
    prose need correction; original end-factor uncertainty and #1284/#1285 fixes remain
    valid.'
- evidence_id: hu2002-figure
  kind: primary_source
  reference: DOI:10.1083/jcb.200112086
  locator: Figure 1, visually inspected
  accessed_at: '2026-10-11T19:43:45Z'
  snapshot_sha256: e07ce1a5d003fc30bf35f56984bfe6d83c7bc919b1578fcd4fbec51ed6ff5fe5
  support: supports
  summary: Historical anterior ring above conoid and lower SPMT-origin ring are distinct;
    positions differ with conoid state.
- evidence_id: hu2006-figure
  kind: primary_source
  reference: DOI:10.1371/journal.ppat.0020013
  locator: Figure 1, visually inspected
  accessed_at: '2026-10-11T19:43:45Z'
  snapshot_sha256: e8cb2be02c6748963937ec56fea7f46edabab3412c64a366743ce203ef38c1da
  support: supports
  summary: Historical anterior ring above conoid and lower SPMT-origin ring are distinct;
    positions differ with conoid state.
- evidence_id: li2023
  kind: primary_source
  reference: DOI:10.1002/advs.202206595
  locator: Results on microtubule orientation, Figure 2 and Methods
  accessed_at: '2026-10-11T19:44:47Z'
  snapshot_sha256: 37079db35056aa0b4a8afdbe487e70f88f099b995dc00fa002bc122ec966bae6
  support: supports
  summary: Primary cryo-ET of 13 ICMTs finds basal-directed extension from within
    the conoid, not an established distal projection through the GO anterior fiber-origin
    ring.
- evidence_id: li-figure
  kind: primary_source
  reference: DOI:10.1002/advs.202206595
  locator: Figure 2C/D, visually inspected
  accessed_at: '2026-10-11T19:46:22Z'
  snapshot_sha256: dab0e3d9aa6e2b8504ca0af3872e5fef67b1d550ff0d9b5c83c2cae238b19fd9
  support: supports
  summary: ICMTs extend basally from within the conoid; PCR and APR are explicitly
    separate structures.
assessments:
- assessment_id: biology
  area: evidence
  topic: Claim-by-claim biological scope
  outcome: concern
  target_ids:
  - GO:0033289
  evidence_ids:
  - record
  - go
  - paper-2
  - paper-6
  summary: 'GO microtubule is-a and apical-complex part_of, alpha/beta-tubulin membership,
    two conventional Toxoplasma microtubules, scaffold context and distinction from
    ribbon-like conoid fibers are supported. Structural essentiality of tubulin is
    not organism viability. Only the over-specific ring projection edge and matching
    prose need correction; original end-factor uncertainty and #1284/#1285 fixes remain
    valid.'
- assessment_id: provenance
  area: completeness
  topic: Prior rationale and intentional unknowns
  outcome: supported
  target_ids:
  - GO:0033289
  evidence_ids:
  - record
  - rules
  - history
  - schema
  summary: No image, dataset, measurement, accession, trait or pathway field is asserted
    here. Optional missing fields and exact-family grounding TODOs are not findings.
    Preserve original discussions, dates, both history surfaces and PROPOSED status;
    deterministic checks are not scientific approval.
findings:
- finding_id: F1
  issue_key: intraconoid-microtubule-anterior-ring-projection
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Remove the unsupported anterior-ring endpoint inference
  description: GO:0033289 says projects through the polar ring without an endpoint
    or explicit GO ring target. The native graph adds distal ends and grounds the
    ring to the anterior fiber-origin GO:0020031, while Hu 2006 claim-local text only
    supports the pair inside the conoid. Li 2023 Results/Figure 2 resolves basal-directed
    ICMT extension, and modern figures distinguish PCR from APR. The generic source
    phrase cannot justify this precise anterior-ring relation.
  target_ids:
  - GO:0033289
  field_paths:
  - functions[0].description
  - causal_graphs[0].description
  - causal_graphs[0].nodes[3]
  - causal_graphs[0].edges[2]
  evidence_ids:
  - record
  - go
  - paper-2
  - paper-6
  - li2023
  - li-figure
  - hu2006-figure
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/intraconoid_microtubule.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: major
  normalization_reason: Material claim-scope, topology or grounding error.
actions:
- action_id: A1
  description: Remove the unsupported anterior-ring endpoint inference
  finding_ids:
  - F1
  target_ids:
  - GO:0033289
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/intraconoid_microtubule.yaml
    role: maintained scientific record
  acceptance_checks:
  - Retain the GO definition as attributed authority, but remove the over-specific
    anterior-ring projection edge and narrow matching prose to supported conoid-center
    topology. Append the nomenclature/end-geometry limitation; do not invent an alternative
    ring attachment or organizer.
  - Use guarded writer and actual Codex EDIT history; preserve original observations,
    history, rationale and PROPOSED status. Pass focused regressions and native QC.
limitations:
- Same-agent whole-native-record review, not independent human approval or raw-data
  reanalysis.
- Terminology differs across GO, historical polar-ring papers and modern multilayer
  APR models. No automatic whole-APR to GO:0020032 equivalence is made.
- QuickGO legacy constraint/documentation URLs returned HTML despite status 200; they
  were not accepted as JSON evidence. OLS exact identity and linked taxon relation
  were checked separately. The GO definition reference to a Trypanosoma paper remains
  an upstream source conflict, not license to expand this apicomplexan record.
- Tran 2010 Europe PMC full-text request failed; actual NCBI XML was retrieved and
  inspected. Seven other native sources were read through primary XML or the author-hosted
  PDF; no search snippet was treated as proof.
- Full QC is verified exact-baseline CI; local schema/strict, history, label, CURIE,
  trait, review and contract checks also ran. Label checks skipped 603 unsupported
  adapter pairs and CURIE checks skipped 251 identifiers; three baseline tests were
  skipped. No verbatim snippets exist in these five records.
- The fresh iModulonDB inventory is inapplicable; absence there is not structural
  absence. No optional unknown was promoted to an issue.
```
