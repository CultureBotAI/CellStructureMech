# meiotic outer plaque: whole-record scientific review

- Review: 20261011T152744Z-meiotic_outer_plaque-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T15:18:35Z
- Finished UTC: 2026-10-11T15:27:44Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Entire native record reviewed; one minor finding saved before scientific curation.

## Scope And Provenance

Entire native YAML including identity, hierarchy, species scope, all evidence/functions/graph edges, optional fields, discussions and both history surfaces.

Selection: Exact record in the nine-record spindle-pole-body cohort of the 909-record goal; other targets have separate accounting.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 569bf3bbe4e887f7072f50da9a6df010958cc312.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:meiotic_outer_plaque | data/structures/cytoskeleton/meiotic_outer_plaque.yaml | maintained | meiotic outer plaque |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | cellstructuremech:meiotic_outer_plaque | Actual deterministic check passed; scientific support assessed separately. |
| strict | passed | True | cellstructuremech:meiotic_outer_plaque | Actual deterministic check passed; scientific support assessed separately. |
| snippets | passed | True | cellstructuremech:meiotic_outer_plaque | No verbatim snippets; paraphrases assessed separately against inspected text. |
| history | passed | True | cellstructuremech:meiotic_outer_plaque | Actual deterministic check passed; scientific support assessed separately. |
| labels | passed | True | cellstructuremech:meiotic_outer_plaque | id↔label correspondence summary:<br>          OK_CANONICAL: 3544<br>            OK_SYNONYM: 50<br>          OK_EXCEPTION: 6<br>    SKIPPED_NO_ADAPTER: 603<br><br>✅ All id↔label pairs correspond. |
| traits | passed | True | cellstructuremech:meiotic_outer_plaque | Actual deterministic check passed; scientific support assessed separately. |
| curies | passed | True | cellstructuremech:meiotic_outer_plaque | resolver control: every resolver accepts a known id and rejects a fabricated one<br><br>identifier liveness summary:<br>  OK             4014<br>  SKIPPED         251<br><br>Every identifier resolves at its issuing authority. |
| reviews | passed | True | cellstructuremech:meiotic_outer_plaque | Actual deterministic check passed; scientific support assessed separately. |
| diff | passed | True | cellstructuremech:meiotic_outer_plaque | Actual deterministic check passed; scientific support assessed separately. |
| contract | passed | True | cellstructuremech:meiotic_outer_plaque | ....                                                                     [100%]<br>4 passed in 118.23s (0:01:58) |
| Exact-baseline native CI QC | passed | True | cellstructuremech:meiotic_outer_plaque | Exact baseline native merge-group QC: 864 passed, 3 skipped; not a fresh local full-QC run. |

## Scientific And Domain Assessments

### MOP structure and neighbors

grounding: supported. Targets: cellstructuremech:meiotic_outer_plaque.

Local structure identity is distinct from remodeling BP, mitotic outer plaque and GO:0070057 membrane attachment site. Broad outer-plaque is-a parent and SPB parthood fit the inspected biological specialization.

### Species, examples, functions and every graph edge

evidence: supported. Targets: cellstructuremech:meiotic_outer_plaque.

S. cerevisiae meiosis-II context, MOP synonymy, remodeling, SPB parthood and membrane initiation/docking are supported. NONMECHANISTIC graph does not impose individual recruitment order, direct interaction or universal stoichiometry.

### Bibliographic title accuracy

evidence: concern. Targets: cellstructuremech:meiotic_outer_plaque.

The evidence note for DOI:10.1128/EC.2.3.431-445.2003 misstates the Nickas 2003 article title as promoting growth of the Spores. Both the inspected article and PMID 12796288 metadata say growth of the Prospore Membrane. The DOI and biological MOP claims remain correct; this is a bounded bibliographic transcription defect.

### Optional fields, component TODO and histories

completeness: supported. Targets: cellstructuremech:meiotic_outer_plaque.

Exact family groundings remain explicitly open; no unwarranted essentiality, accession, image, measurement, dataset, trait or pathway is introduced. Native status and historical boundary decisions are preserved.

## Findings

### F1: Correct the Nickas 2003 article title

minor / open / confirmed; issue key: meiotic-outer-plaque-nickas-2003-title.

The evidence note for DOI:10.1128/EC.2.3.431-445.2003 misstates the Nickas 2003 article title as promoting growth of the Spores. Both the inspected article and PMID 12796288 metadata say growth of the Prospore Membrane. The DOI and biological MOP claims remain correct; this is a bounded bibliographic transcription defect.

## Recommended Actions And Acceptance Checks

### A1

Correct the Nickas 2003 article title

- Replace only the incorrect article-title phrase with Prospore Membrane; preserve the DOI, attribution and all biological assertions.
- Preserve structure identity, definition source, species, functions, every graph edge, discussions and PROPOSED status.
- Guarded writer; actual Codex curation and append-only EDIT history; red/green regressions, generated artifacts, full QC and canonical review checks pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/meiotic_outer_plaque.yaml | context_only | Entire native YAML read before assessment; inspected bytes unchanged. |
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

## Limits And Additional Notes

- Same-agent whole-record review, not independent human approval or raw experimental-data reanalysis.
- Exact-baseline CI supplies full QC; local scoped/global and contract checks ran separately. Existing resolver/label namespace skips and three empty-parameter test skips remain explicit.
- Initial EuropePMC XML errors and PMC interstitials were not counted as readable sources; actual full text was recovered through the public PMC article endpoint.
- Other seven cohort records have separate coverage accounting; no review-output record is created solely for a clean review or acknowledged unknown.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T152744Z-meiotic_outer_plaque-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'meiotic outer plaque: whole-record scientific review'
started_at: '2026-10-11T15:18:35Z'
finished_at: '2026-10-11T15:27:44Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent scientific review, not independent human approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Entire native record reviewed; one minor finding saved before scientific
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
    sha256: c89ff0d9be03e42ecad0b3033a50ed3e12aadb4add3790723041976299712abb
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
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reports/yaml_record_review/20260929T124720Z-meiotic_outer_plaque.md
    sha256: 7afea07b70681e9da37f7f0c709e923ecb3338b44c8cb279d522f95cbc9b3e4c
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
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
  description: Entire native YAML including identity, hierarchy, species scope, all
    evidence/functions/graph edges, optional fields, discussions and both history
    surfaces.
  selection: Exact record in the nine-record spindle-pole-body cohort of the 909-record
    goal; other targets have separate accounting.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:meiotic_outer_plaque
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:meiotic_outer_plaque
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/meiotic_outer_plaque.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T15:22:15Z to 2026-10-11T15:22:17Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:meiotic_outer_plaque
  command: .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/meiotic_outer_plaque.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T15:22:17Z to 2026-10-11T15:22:21Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - cellstructuremech:meiotic_outer_plaque
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/cytoskeleton/meiotic_outer_plaque.yaml
    --report /private/tmp/csm-review-20261011T151709Z/meiotic_outer_plaque-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: No verbatim snippets; paraphrases assessed separately against inspected
    text.
  scope_note: 2026-10-11T15:22:21Z to 2026-10-11T15:22:38Z; log SHA-256 ce3f8b903c129e79d003c3769d89f364c4afeb3dcf52c486d926dbc4ede9f157
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
  scope_note: 2026-10-11T15:23:00Z to 2026-10-11T15:23:13Z; log SHA-256 adc88225145bbf62341c14eb54c6cbe98e801cda6570f5db1b1ab7083cc78fe8
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
  scope_note: 2026-10-11T15:23:13Z to 2026-10-11T15:24:32Z; log SHA-256 d423103555a6a5b538a7c811a73a29c24ed0e5a2eae00d1bb94715295f23f7cb
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
  scope_note: 2026-10-11T15:24:32Z to 2026-10-11T15:24:50Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
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
  scope_note: 2026-10-11T15:24:50Z to 2026-10-11T15:25:56Z; log SHA-256 ee1c5f2e78a2d29fcb6781a8ecd722934376595042d2cc261b4465b361d19b79
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
  scope_note: 2026-10-11T15:25:56Z to 2026-10-11T15:27:26Z; log SHA-256 f40e19ef9d662df4837c43a0224e8ba5aa11671fcc0627a8b469b1c950c169ff
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
  scope_note: 2026-10-11T15:27:26Z to 2026-10-11T15:27:26Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- check_id: contract
  name: contract
  status: passed
  required: true
  target_ids:
  - cellstructuremech:meiotic_outer_plaque
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
  - cellstructuremech:meiotic_outer_plaque
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
  reference: data/structures/cytoskeleton/meiotic_outer_plaque.yaml
  accessed_at: '2026-10-11T15:27:44Z'
  snapshot_sha256: 5d878236a2393fec21c4ca1acc13700c6c905a259c33eb4dfb7181b11cc38b67
  support: context_only
  summary: Entire native YAML read before assessment; inspected bytes unchanged.
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
assessments:
- assessment_id: identity
  area: grounding
  topic: MOP structure and neighbors
  outcome: supported
  target_ids:
  - cellstructuremech:meiotic_outer_plaque
  evidence_ids:
  - record
  - go
  - go-search
  - knop
  - bajgier
  summary: Local structure identity is distinct from remodeling BP, mitotic outer
    plaque and GO:0070057 membrane attachment site. Broad outer-plaque is-a parent
    and SPB parthood fit the inspected biological specialization.
- assessment_id: biology
  area: evidence
  topic: Species, examples, functions and every graph edge
  outcome: supported
  target_ids:
  - cellstructuremech:meiotic_outer_plaque
  evidence_ids:
  - record
  - taxon
  - knop
  - bajgier
  - mathieson
  - nickas
  summary: S. cerevisiae meiosis-II context, MOP synonymy, remodeling, SPB parthood
    and membrane initiation/docking are supported. NONMECHANISTIC graph does not impose
    individual recruitment order, direct interaction or universal stoichiometry.
- assessment_id: citation
  area: evidence
  topic: Bibliographic title accuracy
  outcome: concern
  target_ids:
  - cellstructuremech:meiotic_outer_plaque
  evidence_ids:
  - record
  - nickas
  - nickas-id
  - rules
  summary: The evidence note for DOI:10.1128/EC.2.3.431-445.2003 misstates the Nickas
    2003 article title as promoting growth of the Spores. Both the inspected article
    and PMID 12796288 metadata say growth of the Prospore Membrane. The DOI and biological
    MOP claims remain correct; this is a bounded bibliographic transcription defect.
- assessment_id: remaining
  area: completeness
  topic: Optional fields, component TODO and histories
  outcome: supported
  target_ids:
  - cellstructuremech:meiotic_outer_plaque
  evidence_ids:
  - record
  - history
  - rules
  summary: Exact family groundings remain explicitly open; no unwarranted essentiality,
    accession, image, measurement, dataset, trait or pathway is introduced. Native
    status and historical boundary decisions are preserved.
findings:
- finding_id: F1
  issue_key: meiotic-outer-plaque-nickas-2003-title
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the Nickas 2003 article title
  description: The evidence note for DOI:10.1128/EC.2.3.431-445.2003 misstates the
    Nickas 2003 article title as promoting growth of the Spores. Both the inspected
    article and PMID 12796288 metadata say growth of the Prospore Membrane. The DOI
    and biological MOP claims remain correct; this is a bounded bibliographic transcription
    defect.
  target_ids:
  - cellstructuremech:meiotic_outer_plaque
  field_paths:
  - evidence[reference=DOI:10.1128/EC.2.3.431-445.2003].notes
  evidence_ids:
  - record
  - nickas
  - nickas-id
  - rules
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/meiotic_outer_plaque.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: minor
  normalization_reason: Nonblocking citation-title inaccuracy; valid DOI and supported
    scientific claims do not justify major severity.
actions:
- action_id: A1
  description: Correct the Nickas 2003 article title
  finding_ids:
  - F1
  target_ids:
  - cellstructuremech:meiotic_outer_plaque
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/meiotic_outer_plaque.yaml
    role: maintained scientific record
  acceptance_checks:
  - Replace only the incorrect article-title phrase with Prospore Membrane; preserve
    the DOI, attribution and all biological assertions.
  - Preserve structure identity, definition source, species, functions, every graph
    edge, discussions and PROPOSED status.
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
