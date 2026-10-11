# old mitotic spindle pole body: whole-record scientific review

- Review: 20261011T152738Z-old_mitotic_spindle_pole_body-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T15:18:25Z
- Finished UTC: 2026-10-11T15:27:38Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Entire native record reviewed; one major finding saved before scientific curation.

## Scope And Provenance

Entire native YAML including identity, hierarchy, species scope, all evidence/functions/graph edges, optional fields, discussions and both history surfaces.

Selection: Exact record in the nine-record spindle-pole-body cohort of the 909-record goal; other targets have separate accounting.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 569bf3bbe4e887f7072f50da9a6df010958cc312.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0071957 | data/structures/cytoskeleton/old_mitotic_spindle_pole_body.yaml | maintained | old mitotic spindle pole body |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0071957 | Actual deterministic check passed; scientific support assessed separately. |
| strict | passed | True | GO:0071957 | Actual deterministic check passed; scientific support assessed separately. |
| snippets | passed | True | GO:0071957 | No verbatim snippets; paraphrases assessed separately against inspected text. |
| history | passed | True | GO:0071957 | Actual deterministic check passed; scientific support assessed separately. |
| labels | passed | True | GO:0071957 | id↔label correspondence summary:<br>          OK_CANONICAL: 3544<br>            OK_SYNONYM: 50<br>          OK_EXCEPTION: 6<br>    SKIPPED_NO_ADAPTER: 603<br><br>✅ All id↔label pairs correspond. |
| traits | passed | True | GO:0071957 | Actual deterministic check passed; scientific support assessed separately. |
| curies | passed | True | GO:0071957 | resolver control: every resolver accepts a known id and rejects a fabricated one<br><br>identifier liveness summary:<br>  OK             4014<br>  SKIPPED         251<br><br>Every identifier resolves at its issuing authority. |
| reviews | passed | True | GO:0071957 | Actual deterministic check passed; scientific support assessed separately. |
| diff | passed | True | GO:0071957 | Actual deterministic check passed; scientific support assessed separately. |
| contract | passed | True | GO:0071957 | ....                                                                     [100%]<br>4 passed in 118.23s (0:01:58) |
| Exact-baseline native CI QC | passed | True | GO:0071957 | Exact baseline native merge-group QC: 864 passed, 3 skipped; not a fresh local full-QC run. |

## Scientific And Domain Assessments

### Old versus new versus generic mitotic SPB

grounding: supported. Targets: GO:0071957.

Exact GO:0071957 identity, old SPB synonym, MULTIPROTEIN_COMPLEX kind and GO:0044732 is-a parent are supported. Generic old/new duplication role nodes are not exact signaling identities.

### Species and cell-cycle signaling scope

evidence: concern. Targets: GO:0071957.

The GO-derived definition makes absence of active mitotic-exit proteins unconditional, and the S. pombe example repeats this as a post-duplication property. Grallert 2004 Figure 5 instead shows Cdc7 on both poles early in anaphase B and its later restriction to the new pole; the old pole retains regulators and its signaling can be reactivated by Fin1 perturbation. The definition also folds budding-yeast daughter/bud inheritance into an unqualified statement beside a fission-yeast example. Preserve old-pole identity, but separate species-specific inheritance and cell-cycle-dependent SIN activity. The same unrestricted wording occurs in current GO, so this is an inherited source-scope conflict, not a copied-text transcription error.

### Taxonomy, optional claims and audit boundaries

completeness: supported. Targets: GO:0071957.

S. pombe occurrence is supported. No positive constituent list, exact protein groundings, stoichiometry, measurement, image, dataset, causal graph, trait or pathway is asserted. Component/exclusion TODO remains legitimate; absence of these optional data is not a finding.

## Findings

### F1: Bound old-SPB signaling inactivity to the evidenced species and stage

major / open / confirmed; issue key: old-mitotic-spb-sin-stage-and-species-scope.

The GO-derived definition makes absence of active mitotic-exit proteins unconditional, and the S. pombe example repeats this as a post-duplication property. Grallert 2004 Figure 5 instead shows Cdc7 on both poles early in anaphase B and its later restriction to the new pole; the old pole retains regulators and its signaling can be reactivated by Fin1 perturbation. The definition also folds budding-yeast daughter/bud inheritance into an unqualified statement beside a fission-yeast example. Preserve old-pole identity, but separate species-specific inheritance and cell-cycle-dependent SIN activity. The same unrestricted wording occurs in current GO, so this is an inherited source-scope conflict, not a copied-text transcription error.

## Recommended Actions And Acceptance Checks

### A1

Bound old-SPB signaling inactivity to the evidenced species and stage

- Use a literature-backed local definition identifying the pre-existing pole and explicitly limit old-pole SIN downregulation to the later anaphase B context in S. pombe; do not imply universal protein absence.
- Scope the S. pombe canonical example consistently and separate budding-yeast daughter/bud inheritance from this example.
- Add claim-local Figure 5/6 evidence and an appended resolved clarification of the inherited GO conflict; preserve original discussions and their dates.
- Retain GO:0071957 identity, exact synonym, parentage, species row, open grounding task and PROPOSED status.
- Guarded writer; actual Codex curation and append-only EDIT history; red/green regressions, generated artifacts, full QC and canonical review checks pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/old_mitotic_spindle_pole_body.yaml | context_only | Entire native YAML read before assessment; inspected bytes unchanged. |
| rules | docs/CURATION.md | context_only | Source support and species/stage scope apply to each material claim. |
| history | /private/tmp/csm-review-20261011T151709Z/old_mitotic_spindle_pole_body-discussion-history.json | context_only | Committed discussion and inline-history versions inspected; earlier decisions preserved. |
| history-0 | history/records/old_mitotic_spindle_pole_body/2026-09-29T181148Z-codex-331120.yaml | context_only | Append-only original history inspected. |
| legacy-0 | reports/yaml_record_review/20260929T182700Z-old_mitotic_spindle_pole_body.md | context_only | Historical no-defect review inspected; not a canonical predecessor or proof of scientific correctness. |
| predecessors | /private/tmp/csm-review-20261011T151709Z/exact-target-predecessors.json | context_only | Ignored-inclusive complete canonical scan found no exact-target predecessor. |
| issue-search | /private/tmp/csm-review-20261011T151709Z/spb-issues.log | context_only | All-state SPB issue search inspected; historical issues concern other defects, not this finding. |
| exact-issue-search | /private/tmp/csm-review-20261011T151709Z/old_mitotic_spindle_pole_body-issues.log | context_only | Exact-slug all-state issue search checked for duplicate findings. |
| adapter | /private/tmp/csm-review-20261011T151709Z/adapter.log | context_only | Live iModulonDB inventory has no matching fungal dataset; not negative biological evidence. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005628,GO:0005816,GO:0005824,GO:0005825,GO:0016020,GO:0031322,GO:0032120,GO:0032991,GO:0035974,GO:0044732,GO:0061496,GO:0061498,GO:0070057,GO:0071957,GO:0071958; Exact definitions, synonyms and typed children for cited GO terms | supports | GO identities are nonobsolete. Preserve whole SPB, old/new subtype, outer plaque, MOP remodeling process and membrane-region boundaries. |
| taxon | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896; taxId, scientificName and rank | supports | Exact species identity verified; distribution support comes from the cited experimental context. |
| grallert | DOI:10.1101/gad.296204; Introduction; Results old/new Pcp1-RFP lineage; Figure 5 A-C and caption; Figure 6; Discussion SIN active on new SPB | supports | Primary S. pombe experiments distinguish old/new SPBs with Pcp1-RFP and Cdc7. Figure 5 explicitly shows both poles carrying Cdc7 early in anaphase B and only the new pole later. Fin1 perturbation reactivates old-pole signaling. Bud/daughter inheritance is discussed separately for S. cerevisiae. |
| new-sibling | data/structures/cytoskeleton/new_mitotic_spindle_pole_body.yaml | context_only | Entire new-pole sibling read; localization is not stated as exclusive at every stage. |

## Limits And Additional Notes

- Same-agent whole-record review, not independent human approval or raw experimental-data reanalysis.
- Exact-baseline CI supplies full QC; local scoped/global and contract checks ran separately. Existing resolver/label namespace skips and three empty-parameter test skips remain explicit.
- Initial EuropePMC XML errors and PMC interstitials were not counted as readable sources; actual full text was recovered through the public PMC article endpoint.
- Other seven cohort records have separate coverage accounting; no review-output record is created solely for a clean review or acknowledged unknown.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T152738Z-old_mitotic_spindle_pole_body-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'old mitotic spindle pole body: whole-record scientific review'
started_at: '2026-10-11T15:18:25Z'
finished_at: '2026-10-11T15:27:38Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent scientific review, not independent human approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Entire native record reviewed; one major finding saved before scientific
  curation.
source:
  git_revision: 569bf3bbe4e887f7072f50da9a6df010958cc312
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
    sha256: 5d878236a2393fec21c4ca1acc13700c6c905a259c33eb4dfb7181b11cc38b67
    role: context
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
    sha256: c89ff0d9be03e42ecad0b3033a50ed3e12aadb4add3790723041976299712abb
    role: target
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
  - path: history/records/old_mitotic_spindle_pole_body/2026-09-29T181148Z-codex-331120.yaml
    sha256: bf07b31cf9b7f26a358abe55d0a8cedf76b929627a8aa68c8239fb5685c5ca5e
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reports/yaml_record_review/20260929T182700Z-old_mitotic_spindle_pole_body.md
    sha256: 5051119982a5d0d8c79a057319a088cee51ba607b91279edde26466d490ff837
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
targets:
- target_id: GO:0071957
  path: data/structures/cytoskeleton/old_mitotic_spindle_pole_body.yaml
  label: old mitotic spindle pole body
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/old_mitotic_spindle_pole_body.yaml
    role: maintained scientific record
scope:
  description: Entire native YAML including identity, hierarchy, species scope, all
    evidence/functions/graph edges, optional fields, discussions and both history
    surfaces.
  selection: Exact record in the nine-record spindle-pole-body cohort of the 909-record
    goal; other targets have separate accounting.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0071957
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - GO:0071957
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/old_mitotic_spindle_pole_body.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T15:20:48Z to 2026-10-11T15:20:50Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - GO:0071957
  command: .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/old_mitotic_spindle_pole_body.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T15:20:50Z to 2026-10-11T15:20:55Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - GO:0071957
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/cytoskeleton/old_mitotic_spindle_pole_body.yaml
    --report /private/tmp/csm-review-20261011T151709Z/old_mitotic_spindle_pole_body-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: No verbatim snippets; paraphrases assessed separately against inspected
    text.
  scope_note: 2026-10-11T15:20:55Z to 2026-10-11T15:21:18Z; log SHA-256 0805a8c1c7f9477fbb857f14b39ec7bd84c8a8ad91d67b9a7a403e94819c977e
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:0071957
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T15:23:00Z to 2026-10-11T15:23:13Z; log SHA-256 adc88225145bbf62341c14eb54c6cbe98e801cda6570f5db1b1ab7083cc78fe8
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - GO:0071957
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: "id↔label correspondence summary:\n          OK_CANONICAL: 3544\n     \
    \       OK_SYNONYM: 50\n          OK_EXCEPTION: 6\n    SKIPPED_NO_ADAPTER: 603\n\
    \n✅ All id↔label pairs correspond."
  scope_note: 2026-10-11T15:23:13Z to 2026-10-11T15:24:32Z; log SHA-256 d423103555a6a5b538a7c811a73a29c24ed0e5a2eae00d1bb94715295f23f7cb
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - GO:0071957
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T15:24:32Z to 2026-10-11T15:24:50Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - GO:0071957
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: "resolver control: every resolver accepts a known id and rejects a fabricated\
    \ one\n\nidentifier liveness summary:\n  OK             4014\n  SKIPPED      \
    \   251\n\nEvery identifier resolves at its issuing authority."
  scope_note: 2026-10-11T15:24:50Z to 2026-10-11T15:25:56Z; log SHA-256 ee1c5f2e78a2d29fcb6781a8ecd722934376595042d2cc261b4465b361d19b79
- check_id: reviews
  name: reviews
  status: passed
  required: true
  target_ids:
  - GO:0071957
  command: .venv/bin/python scripts/record_review.py check --base 569bf3bbe4e887f7072f50da9a6df010958cc312
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T15:25:56Z to 2026-10-11T15:27:26Z; log SHA-256 f40e19ef9d662df4837c43a0224e8ba5aa11671fcc0627a8b469b1c950c169ff
- check_id: diff
  name: diff
  status: passed
  required: true
  target_ids:
  - GO:0071957
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T15:27:26Z to 2026-10-11T15:27:26Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- check_id: contract
  name: contract
  status: passed
  required: true
  target_ids:
  - GO:0071957
  command: .venv/bin/python -m pytest -q tests/test_record_review_contract.py
  exit_code: 0
  expected_exit_code: 0
  summary: '....                                                                     [100%]

    4 passed in 118.23s (0:01:58)'
  scope_note: 2026-10-11T15:17:41Z to 2026-10-11T15:19:41Z; log SHA-256 902ee3de268df3199a159f88b0a81b922b5149db8f8206f4cba846f153ffaca2
- check_id: qc
  name: Exact-baseline native CI QC
  status: passed
  required: true
  target_ids:
  - GO:0071957
  command: gh run view 38149034088 --repo CultureBotAI/CellStructureMech --log
  exit_code: 0
  expected_exit_code: 0
  summary: 'Exact baseline native merge-group QC: 864 passed, 3 skipped; not a fresh
    local full-QC run.'
  scope_note: https://github.com/CultureBotAI/CellStructureMech/actions/runs/38149034088;
    log SHA-256 e3efbb2d3dd7f705b0eb1ffe7c84f9c9d54e4d3c8b4d77521870c257bfd0b3b6
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/old_mitotic_spindle_pole_body.yaml
  accessed_at: '2026-10-11T15:27:38Z'
  snapshot_sha256: c89ff0d9be03e42ecad0b3033a50ed3e12aadb4add3790723041976299712abb
  support: context_only
  summary: Entire native YAML read before assessment; inspected bytes unchanged.
- evidence_id: rules
  kind: record_content
  reference: docs/CURATION.md
  accessed_at: '2026-10-11T15:27:38Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  support: context_only
  summary: Source support and species/stage scope apply to each material claim.
- evidence_id: history
  kind: record_content
  reference: /private/tmp/csm-review-20261011T151709Z/old_mitotic_spindle_pole_body-discussion-history.json
  accessed_at: '2026-10-11T15:27:38Z'
  snapshot_sha256: 87e18dbfdf7e8a0c137a55c7180b027cb5d5810da9d7ddfe273dd637caa40e45
  support: context_only
  summary: Committed discussion and inline-history versions inspected; earlier decisions
    preserved.
- evidence_id: history-0
  kind: record_content
  reference: history/records/old_mitotic_spindle_pole_body/2026-09-29T181148Z-codex-331120.yaml
  accessed_at: '2026-10-11T15:27:38Z'
  snapshot_sha256: bf07b31cf9b7f26a358abe55d0a8cedf76b929627a8aa68c8239fb5685c5ca5e
  support: context_only
  summary: Append-only original history inspected.
- evidence_id: legacy-0
  kind: prior_review
  reference: reports/yaml_record_review/20260929T182700Z-old_mitotic_spindle_pole_body.md
  accessed_at: '2026-10-11T15:27:38Z'
  snapshot_sha256: 5051119982a5d0d8c79a057319a088cee51ba607b91279edde26466d490ff837
  support: context_only
  summary: Historical no-defect review inspected; not a canonical predecessor or proof
    of scientific correctness.
- evidence_id: predecessors
  kind: validation
  reference: /private/tmp/csm-review-20261011T151709Z/exact-target-predecessors.json
  accessed_at: '2026-10-11T15:27:38Z'
  snapshot_sha256: c6bd0214502e1a9a8f241ffda0fd6afecd2faa69f57ad244e68165a7ddbeb84d
  support: context_only
  summary: Ignored-inclusive complete canonical scan found no exact-target predecessor.
- evidence_id: issue-search
  kind: validation
  reference: /private/tmp/csm-review-20261011T151709Z/spb-issues.log
  accessed_at: '2026-10-11T15:27:38Z'
  snapshot_sha256: 105161b4440092ef6565bcbb62b383fbf06e4d40dfbc72900cf4bb1db64d196a
  support: context_only
  summary: All-state SPB issue search inspected; historical issues concern other defects,
    not this finding.
- evidence_id: exact-issue-search
  kind: validation
  reference: /private/tmp/csm-review-20261011T151709Z/old_mitotic_spindle_pole_body-issues.log
  accessed_at: '2026-10-11T15:27:38Z'
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
  support: context_only
  summary: Exact-slug all-state issue search checked for duplicate findings.
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/csm-review-20261011T151709Z/adapter.log
  accessed_at: '2026-10-11T15:27:38Z'
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
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896
  locator: taxId, scientificName and rank
  accessed_at: '2026-10-11T15:18:34Z'
  snapshot_sha256: 42c5b7d3d99341137803612d6404cd3884e2d06ec8a740b1ad38163c678f6721
  support: supports
  summary: Exact species identity verified; distribution support comes from the cited
    experimental context.
- evidence_id: grallert
  kind: primary_source
  reference: DOI:10.1101/gad.296204
  locator: Introduction; Results old/new Pcp1-RFP lineage; Figure 5 A-C and caption;
    Figure 6; Discussion SIN active on new SPB
  accessed_at: '2026-10-11T15:21:54Z'
  snapshot_sha256: da9da982927eb90bd53ad7fe74d6f61901d7186b5ffd3e27bd220e09ca4af448
  support: supports
  summary: Primary S. pombe experiments distinguish old/new SPBs with Pcp1-RFP and
    Cdc7. Figure 5 explicitly shows both poles carrying Cdc7 early in anaphase B and
    only the new pole later. Fin1 perturbation reactivates old-pole signaling. Bud/daughter
    inheritance is discussed separately for S. cerevisiae.
- evidence_id: new-sibling
  kind: record_content
  reference: data/structures/cytoskeleton/new_mitotic_spindle_pole_body.yaml
  accessed_at: '2026-10-11T15:27:38Z'
  snapshot_sha256: 33ac955370a7476c7bb3f3fca4cfc9464120890e6a3e57fcb3b32d5e2504fb82
  support: context_only
  summary: Entire new-pole sibling read; localization is not stated as exclusive at
    every stage.
assessments:
- assessment_id: identity
  area: grounding
  topic: Old versus new versus generic mitotic SPB
  outcome: supported
  target_ids:
  - GO:0071957
  evidence_ids:
  - record
  - go
  - grallert
  - new-sibling
  summary: Exact GO:0071957 identity, old SPB synonym, MULTIPROTEIN_COMPLEX kind and
    GO:0044732 is-a parent are supported. Generic old/new duplication role nodes are
    not exact signaling identities.
- assessment_id: scope
  area: evidence
  topic: Species and cell-cycle signaling scope
  outcome: concern
  target_ids:
  - GO:0071957
  evidence_ids:
  - record
  - go
  - grallert
  - rules
  summary: The GO-derived definition makes absence of active mitotic-exit proteins
    unconditional, and the S. pombe example repeats this as a post-duplication property.
    Grallert 2004 Figure 5 instead shows Cdc7 on both poles early in anaphase B and
    its later restriction to the new pole; the old pole retains regulators and its
    signaling can be reactivated by Fin1 perturbation. The definition also folds budding-yeast
    daughter/bud inheritance into an unqualified statement beside a fission-yeast
    example. Preserve old-pole identity, but separate species-specific inheritance
    and cell-cycle-dependent SIN activity. The same unrestricted wording occurs in
    current GO, so this is an inherited source-scope conflict, not a copied-text transcription
    error.
- assessment_id: remaining
  area: completeness
  topic: Taxonomy, optional claims and audit boundaries
  outcome: supported
  target_ids:
  - GO:0071957
  evidence_ids:
  - record
  - taxon
  - grallert
  - history
  summary: S. pombe occurrence is supported. No positive constituent list, exact protein
    groundings, stoichiometry, measurement, image, dataset, causal graph, trait or
    pathway is asserted. Component/exclusion TODO remains legitimate; absence of these
    optional data is not a finding.
findings:
- finding_id: F1
  issue_key: old-mitotic-spb-sin-stage-and-species-scope
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Bound old-SPB signaling inactivity to the evidenced species and stage
  description: The GO-derived definition makes absence of active mitotic-exit proteins
    unconditional, and the S. pombe example repeats this as a post-duplication property.
    Grallert 2004 Figure 5 instead shows Cdc7 on both poles early in anaphase B and
    its later restriction to the new pole; the old pole retains regulators and its
    signaling can be reactivated by Fin1 perturbation. The definition also folds budding-yeast
    daughter/bud inheritance into an unqualified statement beside a fission-yeast
    example. Preserve old-pole identity, but separate species-specific inheritance
    and cell-cycle-dependent SIN activity. The same unrestricted wording occurs in
    current GO, so this is an inherited source-scope conflict, not a copied-text transcription
    error.
  target_ids:
  - GO:0071957
  field_paths:
  - definition
  - definition_source
  - canonical_examples[0].note
  - evidence
  - discussions
  evidence_ids:
  - record
  - go
  - grallert
  - rules
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/old_mitotic_spindle_pole_body.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: major
  normalization_reason: Unsupported species/stage generalization in the definition
    and example is a substantive scope defect; exact structure identity remains correct,
    so not a blocker.
actions:
- action_id: A1
  description: Bound old-SPB signaling inactivity to the evidenced species and stage
  finding_ids:
  - F1
  target_ids:
  - GO:0071957
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/old_mitotic_spindle_pole_body.yaml
    role: maintained scientific record
  acceptance_checks:
  - Use a literature-backed local definition identifying the pre-existing pole and
    explicitly limit old-pole SIN downregulation to the later anaphase B context in
    S. pombe; do not imply universal protein absence.
  - Scope the S. pombe canonical example consistently and separate budding-yeast daughter/bud
    inheritance from this example.
  - Add claim-local Figure 5/6 evidence and an appended resolved clarification of
    the inherited GO conflict; preserve original discussions and their dates.
  - Retain GO:0071957 identity, exact synonym, parentage, species row, open grounding
    task and PROPOSED status.
  - Guarded writer; actual Codex curation and append-only EDIT history; red/green
    regressions, generated artifacts, full QC and canonical review checks pass.
limitations:
- Same-agent whole-record review, not independent human approval or raw experimental-data
  reanalysis.
- Exact-baseline CI supplies full QC; local scoped/global and contract checks ran
  separately. Existing resolver/label namespace skips and three empty-parameter test
  skips remain explicit.
- Initial EuropePMC XML errors and PMC interstitials were not counted as readable
  sources; actual full text was recovered through the public PMC article endpoint.
- Other seven cohort records have separate coverage accounting; no review-output record
  is created solely for a clean review or acknowledged unknown.
```
