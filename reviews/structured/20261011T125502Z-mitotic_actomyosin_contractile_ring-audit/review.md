# Mitotic actomyosin ring: whole-record scientific review

- Review: 20261011T125502Z-mitotic_actomyosin_contractile_ring-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T12:42:26Z
- Finished UTC: 2026-10-11T12:55:02Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

One major finding: a GO-derived timing sentence conflates an early budding-yeast Myo1 precursor ring with the later actin-containing contractile ring.

## Scope And Provenance

Entire native YAML, including identity, definition timing, hierarchy, components, taxon, example, function, every graph edge, discussions and both history surfaces.

Selection: Exact GO:0110085 record added to the seven-record bud-neck/septin cohort after a parent-context discrepancy was noticed. All 909 goal records remain in scope.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1d21cc572172b0e9c3d01f39231c82ce45fa4ffa.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0110085 | data/structures/cytoskeleton/mitotic_actomyosin_contractile_ring.yaml | maintained | mitotic actomyosin contractile ring |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| history | passed | True | GO:0110085 | Actual deterministic check passed; scientific support assessed separately. |
| labels | passed | True | GO:0110085 | id↔label correspondence summary:<br>          OK_CANONICAL: 3544<br>            OK_SYNONYM: 50<br>          OK_EXCEPTION: 6<br>    SKIPPED_NO_ADAPTER: 603<br><br>✅ All id↔label pairs correspond. |
| traits | passed | True | GO:0110085 | Actual deterministic check passed; scientific support assessed separately. |
| curies | passed | True | GO:0110085 | resolver control: every resolver accepts a known id and rejects a fabricated one<br><br>identifier liveness summary:<br>  OK             4014<br>  SKIPPED         251<br><br>Every identifier resolves at its issuing authority. |
| reviews | passed | True | GO:0110085 | Actual deterministic check passed; scientific support assessed separately. |
| diff | passed | True | GO:0110085 | Actual deterministic check passed; scientific support assessed separately. |
| schema | passed | True | GO:0110085 | Actual deterministic check passed; scientific support assessed separately. |
| strict | passed | True | GO:0110085 | Actual deterministic check passed; scientific support assessed separately. |
| snippets | passed | True | GO:0110085 | No verbatim snippets; paraphrases assessed separately against inspected text. |
| qc | passed | True | GO:0110085 | Actual deterministic check passed; scientific support assessed separately. |
| contract | passed | True | GO:0110085 | ....                                                                     [100%]<br>4 passed in 86.23s (0:01:26) |

## Scientific And Domain Assessments

### Class and mereology

grounding: supported. Targets: GO:0110085.

GO:0110085 is the mitotic class, not a protein, the generic parent, the meiotic sibling or the localized budding-yeast child. Category and structure kind are appropriate.

### Components, taxonomy, example, function and graph

evidence: supported. Targets: GO:0110085.

Actin and myosin constituent roles, the species-level fission-yeast example and node coalescence are supported. The graph asserts membership only, with no unsupported accessory requirement. UNKNOWN essentiality and label-only groundings preserve uncertainty.

### Budding-yeast precursor versus actomyosin ring

evidence: concern. Targets: GO:0110085.

The final definition sentence says that the S. cerevisiae mitotic contractile ring forms before mitosis. The current GO source has the same wording, but Bi et al. 1998 distinguish an early Myo1 ring from subsequent actin recruitment near the end of anaphase. The definition conflates a myosin precursor with the completed actomyosin structure. Correct the localized timing without changing the GO identity or transferring budding-yeast chronology to the fission-yeast graph.

### Discussions, status, history and optional resources

completeness: supported. Targets: GO:0110085.

Accessory-protein boundaries remain explicitly deferred. No exact protein accession, composition copy number, dataset, image, measurement, trait or pathway link is asserted. Previous discussions and audit history are retained; no human status promotion is appropriate.

## Findings

### F1: Distinguish early Myo1 localization from late actomyosin-ring assembly

major / open / confirmed; issue key: mitotic-ring-budding-yeast-premitotic-actomyosin-conflation.

The final definition sentence says that the S. cerevisiae mitotic contractile ring forms before mitosis. The current GO source has the same wording, but Bi et al. 1998 distinguish an early Myo1 ring from subsequent actin recruitment near the end of anaphase. The definition conflates a myosin precursor with the completed actomyosin structure. Correct the localized timing without changing the GO identity or transferring budding-yeast chronology to the fission-yeast graph.

## Recommended Actions And Acceptance Checks

### A1

Correct only the S. cerevisiae timing clause and document the primary-evidence qualification to the GO definition.

- Definition distinguishes Myo1 localization before budding from actin joining near the end of anaphase.
- Add claim-linked Bi et al. evidence and a durable discussion preserving the GO-versus-primary-source disagreement.
- Keep GO identity, parentage, fission-yeast fields, graph, existing discussions and status unchanged.
- Use guarded writer and append actual Codex curation/EDIT history; preserve all earlier reviews.
- Focused regressions fail before the fix and pass afterward; refresh local embeddings and pages, then pass native QC and review validation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/mitotic_actomyosin_contractile_ring.yaml | context_only | Entire current native YAML read; captured source bytes unchanged. |
| rules | docs/CURATION.md | context_only | Narrow claim support and preservation of biological state and taxonomic context. |
| history | history/records/mitotic_actomyosin_contractile_ring/2026-09-29T221314Z-codex-93751d.yaml | context_only | Original CREATE history agrees with record scope; status remains PROPOSED. |
| legacy | reports/yaml_record_review/20260929T223341Z-mitotic_actomyosin_contractile_ring.md | context_only | Historical clean review compared the GO payload; it did not reconcile its timing with budding-yeast experiments. Retained unchanged. |
| predecessors | /private/tmp/csm-review-20261011T123803Z/parent-predecessors.json | context_only | Ignored-inclusive canonical scan found no exact-target predecessor. |
| issue-search | /private/tmp/csm-review-20261011T123803Z/parent-bud-timing-issues.log | context_only | All-state issue search for the exact timing phrase returned no hits; checked alongside record-label search. |
| myo1-issue-search | /private/tmp/csm-review-20261011T123803Z/myo1-issues.log | context_only | All-state Myo1 issue search returned no hits; broader wording checked before filing. |
| anaphase-issue-search | /private/tmp/csm-review-20261011T123803Z/anaphase-issues.log | context_only | All-state anaphase issue search returned no hits; broader timing wording checked before filing. |
| adapter | /private/tmp/csm-review-20261011T123803Z/adapter.log | context_only | Live iModulonDB inventory has no relevant fungal dataset; absence is not negative biological evidence. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005826,GO:0110085,GO:0110086,GO:0000142; GO:0110085 definition; GO:0005826 typed children; GO:0000142 and GO:0110086 boundaries | supports | Exact class, parent, child and meiotic sibling identities are sound. The current GO definition itself contains the disputed premitotic timing, so this is an inherited scientific error, not a copying mistake. |
| taxon | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896; TaxId 4896, scientificName and species rank | supports | Schizosaccharomyces pombe taxon identity verified. |
| bi | DOI:10.1083/jcb.142.5.1301; Results: actin ring timing, Myo1 ring timing, coincidence of actin and Myo1 rings; Discussion: Sequential Assembly of Myosin and Actin into the Contractile Ring | supports | Bi et al. distinguish early Myo1 localization from actin recruitment near the end of anaphase. The actin-containing contractile ring is not already assembled before mitosis. The study uses Myo1-GFP, phalloidin staining and cell-cycle staging in S. cerevisiae. |
| wu | DOI:10.1083/jcb.200602032; Results: node composition, Myo2-positive nodes and actin-dependent coalescence; Discussion; Materials and methods | supports | Wu et al. support the separate fission-yeast claims using tagged proteins expressed from native loci, live imaging and Lat-A perturbation. These results do not establish budding-yeast timing. |
| wu-id | DOI:10.1083/jcb.200602032; DOI, PMID16864655, title, year and authors | supports | Exact cited article identity verified; informal lead/senior-author wording does not change the resolved DOI or the supported experimental claim. |

## Limits And Additional Notes

- Same-agent whole-record review, not independent human scientific approval.
- No raw-image or raw-data reanalysis; primary Results, Methods and relevant discussion were inspected.
- iModulonDB has no matching fungal dataset; ontology label/identifier namespace skips and three existing empty-parameter test skips remain explicit.
- The seven clean bud-neck/septin records have separate operational coverage and no review-output records.
- The error is present upstream in GO. No external ontology changes or submission are claimed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T125502Z-mitotic_actomyosin_contractile_ring-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'Mitotic actomyosin ring: whole-record scientific review'
started_at: '2026-10-11T12:42:26Z'
finished_at: '2026-10-11T12:55:02Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent source and record review, not independent human approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'One major finding: a GO-derived timing sentence conflates an early budding-yeast
  Myo1 precursor ring with the later actin-containing contractile ring.'
source:
  git_revision: 1d21cc572172b0e9c3d01f39231c82ce45fa4ffa
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
  - path: data/structures/cytoskeleton/actomyosin_contractile_ring.yaml
    sha256: 28a3e7b12391a9d3a16eb453974d6e0ed5ab92b925092e395e88f64fa6fe5ab0
    role: context
  - path: data/structures/cytoskeleton/cellular_bud_neck_contractile_ring.yaml
    sha256: d1f8d46a6a0f9d76873166cbb22365e787189f3d05b08e8aac334d320331f2dd
    role: context
  - path: data/structures/cytoskeleton/cellular_bud_neck_septin_collar.yaml
    sha256: d7865addf83d9295f0c8f8c73f9604f12b3fe95bbe8ea2de209298ddab022b94
    role: context
  - path: data/structures/cytoskeleton/cellular_bud_neck_septin_ring.yaml
    sha256: 7f05e8a5a7fe577b0e47118606fc1a3e6a87b5ed57cec09c1f5346b8fd6993e9
    role: context
  - path: data/structures/cytoskeleton/cellular_bud_neck_split_septin_rings.yaml
    sha256: c76ed8c617acf9966daa42ca587f49cc352795bc3e2b9fe702359075c49a9cff
    role: context
  - path: data/structures/cytoskeleton/mitotic_actomyosin_contractile_ring.yaml
    sha256: 52d2a828c47a777ba10d816852d39b29b69f8843f27d9de2f7130b408de4e737
    role: target
  - path: data/structures/cytoskeleton/septin_collar.yaml
    sha256: 163589ad60ecc9dac5684babab33dc3b88a16ee87823fadcf69f7afca437d63d
    role: context
  - path: data/structures/cytoskeleton/septin_ring.yaml
    sha256: 78bdf9cfbc79c52a73cd1368f4e2d3dee46fb94a5bcf860477cc02057569bfec
    role: context
  - path: data/structures/cytoskeleton/split_septin_rings.yaml
    sha256: 580abb6f00c144e871e1fded7fbb2dca8584ecf0d47a599f646558642c3027ff
    role: context
  - path: data/structures/other/cellular_bud_neck.yaml
    sha256: 5c7f0d1c4c048d162593483fc2e0210697dff88f4dcf5d7e3b1d194f35e7e6e8
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
  - path: history/records/cellular_bud_neck_contractile_ring/2026-09-29T213316Z-codex-c2ac04.yaml
    sha256: ec0cf44fe919676b404c23157c7599df2518e04366f530c7010d956e54a74807
    role: context
  - path: history/records/mitotic_actomyosin_contractile_ring/2026-09-29T221314Z-codex-93751d.yaml
    sha256: 1ebe3b607c361d7d9eeca034e1f1d868c6908d08d858e9597b489a9484e959a4
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reports/yaml_record_review/20260929T215210Z-cellular_bud_neck_contractile_ring.md
    sha256: 84da52fee7ed252c1c95c08eb9cfbfdc9527ebdc4b1ea339bb9d8bc9d283d224
    role: context
  - path: reports/yaml_record_review/20260929T223341Z-mitotic_actomyosin_contractile_ring.md
    sha256: 44eec0f12c5ab85a124ec086a7c827b8f683001f63fad400beec15f9a729dad0
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
targets:
- target_id: GO:0110085
  path: data/structures/cytoskeleton/mitotic_actomyosin_contractile_ring.yaml
  label: mitotic actomyosin contractile ring
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/mitotic_actomyosin_contractile_ring.yaml
    role: maintained scientific record
scope:
  description: Entire native YAML, including identity, definition timing, hierarchy,
    components, taxon, example, function, every graph edge, discussions and both history
    surfaces.
  selection: Exact GO:0110085 record added to the seven-record bud-neck/septin cohort
    after a parent-context discrepancy was noticed. All 909 goal records remain in
    scope.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0110085
checks:
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:0110085
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T12:43:42Z to 2026-10-11T12:44:02Z; log SHA-256 e002f7ee670d93f9ac79e90f87c45b6741dfd42a7e96f25c08bbe5bdf4bebe56
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - GO:0110085
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: "id↔label correspondence summary:\n          OK_CANONICAL: 3544\n     \
    \       OK_SYNONYM: 50\n          OK_EXCEPTION: 6\n    SKIPPED_NO_ADAPTER: 603\n\
    \n✅ All id↔label pairs correspond."
  scope_note: 2026-10-11T12:44:02Z to 2026-10-11T12:45:49Z; log SHA-256 d423103555a6a5b538a7c811a73a29c24ed0e5a2eae00d1bb94715295f23f7cb
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - GO:0110085
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T12:45:49Z to 2026-10-11T12:46:22Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - GO:0110085
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: "resolver control: every resolver accepts a known id and rejects a fabricated\
    \ one\n\nidentifier liveness summary:\n  OK             4014\n  SKIPPED      \
    \   251\n\nEvery identifier resolves at its issuing authority."
  scope_note: 2026-10-11T12:46:22Z to 2026-10-11T12:47:13Z; log SHA-256 ee1c5f2e78a2d29fcb6781a8ecd722934376595042d2cc261b4465b361d19b79
- check_id: reviews
  name: reviews
  status: passed
  required: true
  target_ids:
  - GO:0110085
  command: .venv/bin/python scripts/record_review.py check --base 1d21cc572172b0e9c3d01f39231c82ce45fa4ffa
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T12:47:13Z to 2026-10-11T12:48:43Z; log SHA-256 68a34d0b8faeae378e36007a7a4f0c6e1ae2d1611c2eb6e7028c00784ebc6d4e
- check_id: diff
  name: diff
  status: passed
  required: true
  target_ids:
  - GO:0110085
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T12:48:43Z to 2026-10-11T12:48:43Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - GO:0110085
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/mitotic_actomyosin_contractile_ring.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T12:42:58Z to 2026-10-11T12:43:02Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - GO:0110085
  command: .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/mitotic_actomyosin_contractile_ring.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T12:43:02Z to 2026-10-11T12:43:07Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - GO:0110085
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/cytoskeleton/mitotic_actomyosin_contractile_ring.yaml
    --report /private/tmp/csm-review-20261011T123803Z/mitotic_actomyosin_contractile_ring-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: No verbatim snippets; paraphrases assessed separately against inspected
    text.
  scope_note: 2026-10-11T12:43:07Z to 2026-10-11T12:43:41Z; log SHA-256 dcaf5b9dfacf71de98bb95ec16cf870fbad4758354ffcad0ef4d5903fd2ac10e
- check_id: qc
  name: qc
  status: passed
  required: true
  target_ids:
  - GO:0110085
  command: .venv/bin/python scripts/run_qc.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T12:41:33Z to 2026-10-11T12:54:58Z; log SHA-256 f469045336eaf6266a243eeada519ca3fe4b1a2b854c491de781ef4a5567d0a1
- check_id: contract
  name: contract
  status: passed
  required: true
  target_ids:
  - GO:0110085
  command: .venv/bin/python -m pytest -q tests/test_record_review_contract.py
  exit_code: 0
  expected_exit_code: 0
  summary: '....                                                                     [100%]

    4 passed in 86.23s (0:01:26)'
  scope_note: 2026-10-11T12:39:22Z to 2026-10-11T12:40:49Z; log SHA-256 bfbe96b58067c73486aa4c599e5a8d6ef0278b01100a2c2cc5d4b7c02bc3ccfa
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/mitotic_actomyosin_contractile_ring.yaml
  accessed_at: '2026-10-11T12:55:02Z'
  snapshot_sha256: 52d2a828c47a777ba10d816852d39b29b69f8843f27d9de2f7130b408de4e737
  support: context_only
  summary: Entire current native YAML read; captured source bytes unchanged.
- evidence_id: rules
  kind: record_content
  reference: docs/CURATION.md
  accessed_at: '2026-10-11T12:55:02Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  support: context_only
  summary: Narrow claim support and preservation of biological state and taxonomic
    context.
- evidence_id: history
  kind: record_content
  reference: history/records/mitotic_actomyosin_contractile_ring/2026-09-29T221314Z-codex-93751d.yaml
  accessed_at: '2026-10-11T12:55:02Z'
  snapshot_sha256: 1ebe3b607c361d7d9eeca034e1f1d868c6908d08d858e9597b489a9484e959a4
  support: context_only
  summary: Original CREATE history agrees with record scope; status remains PROPOSED.
- evidence_id: legacy
  kind: prior_review
  reference: reports/yaml_record_review/20260929T223341Z-mitotic_actomyosin_contractile_ring.md
  accessed_at: '2026-10-11T12:55:02Z'
  snapshot_sha256: 44eec0f12c5ab85a124ec086a7c827b8f683001f63fad400beec15f9a729dad0
  support: context_only
  summary: Historical clean review compared the GO payload; it did not reconcile its
    timing with budding-yeast experiments. Retained unchanged.
- evidence_id: predecessors
  kind: validation
  reference: /private/tmp/csm-review-20261011T123803Z/parent-predecessors.json
  accessed_at: '2026-10-11T12:55:02Z'
  snapshot_sha256: 25df8e19ea163d1cb8575eec3b42fa7898543c6e60c5871b97a94d6b2c96793c
  support: context_only
  summary: Ignored-inclusive canonical scan found no exact-target predecessor.
- evidence_id: issue-search
  kind: validation
  reference: /private/tmp/csm-review-20261011T123803Z/parent-bud-timing-issues.log
  accessed_at: '2026-10-11T12:55:02Z'
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
  support: context_only
  summary: All-state issue search for the exact timing phrase returned no hits; checked
    alongside record-label search.
- evidence_id: myo1-issue-search
  kind: validation
  reference: /private/tmp/csm-review-20261011T123803Z/myo1-issues.log
  accessed_at: '2026-10-11T12:55:02Z'
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
  support: context_only
  summary: All-state Myo1 issue search returned no hits; broader wording checked before
    filing.
- evidence_id: anaphase-issue-search
  kind: validation
  reference: /private/tmp/csm-review-20261011T123803Z/anaphase-issues.log
  accessed_at: '2026-10-11T12:55:02Z'
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
  support: context_only
  summary: All-state anaphase issue search returned no hits; broader timing wording
    checked before filing.
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/csm-review-20261011T123803Z/adapter.log
  accessed_at: '2026-10-11T12:55:02Z'
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
  support: context_only
  summary: Live iModulonDB inventory has no relevant fungal dataset; absence is not
    negative biological evidence.
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005826,GO:0110085,GO:0110086,GO:0000142
  locator: GO:0110085 definition; GO:0005826 typed children; GO:0000142 and GO:0110086
    boundaries
  accessed_at: '2026-10-11T12:42:57Z'
  snapshot_sha256: 9c298f0690a87d7f7702c2738ff7f82d59d2cef4f62d55c401fa3c78b3eeab0f
  support: supports
  summary: Exact class, parent, child and meiotic sibling identities are sound. The
    current GO definition itself contains the disputed premitotic timing, so this
    is an inherited scientific error, not a copying mistake.
- evidence_id: taxon
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896
  locator: TaxId 4896, scientificName and species rank
  accessed_at: '2026-10-11T12:42:58Z'
  snapshot_sha256: 42c5b7d3d99341137803612d6404cd3884e2d06ec8a740b1ad38163c678f6721
  support: supports
  summary: Schizosaccharomyces pombe taxon identity verified.
- evidence_id: bi
  kind: primary_source
  reference: DOI:10.1083/jcb.142.5.1301
  locator: 'Results: actin ring timing, Myo1 ring timing, coincidence of actin and
    Myo1 rings; Discussion: Sequential Assembly of Myosin and Actin into the Contractile
    Ring'
  accessed_at: '2026-10-11T12:39:09Z'
  snapshot_sha256: 7eaa6a99a99ef3faca62f60be5e7f93c3c3fbb2ed328003fc9b88e1eedff54a5
  support: supports
  summary: Bi et al. distinguish early Myo1 localization from actin recruitment near
    the end of anaphase. The actin-containing contractile ring is not already assembled
    before mitosis. The study uses Myo1-GFP, phalloidin staining and cell-cycle staging
    in S. cerevisiae.
- evidence_id: wu
  kind: primary_source
  reference: DOI:10.1083/jcb.200602032
  locator: 'Results: node composition, Myo2-positive nodes and actin-dependent coalescence;
    Discussion; Materials and methods'
  accessed_at: '2026-10-11T12:42:57Z'
  snapshot_sha256: e7500572069d2c5a68fe4c52694b55638d7a8a07ae9eb134feee4843c7e92865
  support: supports
  summary: Wu et al. support the separate fission-yeast claims using tagged proteins
    expressed from native loci, live imaging and Lat-A perturbation. These results
    do not establish budding-yeast timing.
- evidence_id: wu-id
  kind: primary_source
  reference: DOI:10.1083/jcb.200602032
  locator: DOI, PMID16864655, title, year and authors
  accessed_at: '2026-10-11T12:42:55Z'
  snapshot_sha256: ef5627f473f84a107a3bf6d2a78ff8c444ab9c1abf5dd561fecfb373d9a960c5
  support: supports
  summary: Exact cited article identity verified; informal lead/senior-author wording
    does not change the resolved DOI or the supported experimental claim.
assessments:
- assessment_id: identity
  area: grounding
  topic: Class and mereology
  outcome: supported
  target_ids:
  - GO:0110085
  evidence_ids:
  - record
  - go
  summary: GO:0110085 is the mitotic class, not a protein, the generic parent, the
    meiotic sibling or the localized budding-yeast child. Category and structure kind
    are appropriate.
- assessment_id: biology
  area: evidence
  topic: Components, taxonomy, example, function and graph
  outcome: supported
  target_ids:
  - GO:0110085
  evidence_ids:
  - record
  - go
  - taxon
  - wu
  summary: Actin and myosin constituent roles, the species-level fission-yeast example
    and node coalescence are supported. The graph asserts membership only, with no
    unsupported accessory requirement. UNKNOWN essentiality and label-only groundings
    preserve uncertainty.
- assessment_id: timing
  area: evidence
  topic: Budding-yeast precursor versus actomyosin ring
  outcome: concern
  target_ids:
  - GO:0110085
  evidence_ids:
  - record
  - go
  - bi
  - rules
  summary: The final definition sentence says that the S. cerevisiae mitotic contractile
    ring forms before mitosis. The current GO source has the same wording, but Bi
    et al. 1998 distinguish an early Myo1 ring from subsequent actin recruitment near
    the end of anaphase. The definition conflates a myosin precursor with the completed
    actomyosin structure. Correct the localized timing without changing the GO identity
    or transferring budding-yeast chronology to the fission-yeast graph.
- assessment_id: audit
  area: completeness
  topic: Discussions, status, history and optional resources
  outcome: supported
  target_ids:
  - GO:0110085
  evidence_ids:
  - record
  - history
  - legacy
  - rules
  summary: Accessory-protein boundaries remain explicitly deferred. No exact protein
    accession, composition copy number, dataset, image, measurement, trait or pathway
    link is asserted. Previous discussions and audit history are retained; no human
    status promotion is appropriate.
findings:
- finding_id: F1
  issue_key: mitotic-ring-budding-yeast-premitotic-actomyosin-conflation
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Distinguish early Myo1 localization from late actomyosin-ring assembly
  description: The final definition sentence says that the S. cerevisiae mitotic contractile
    ring forms before mitosis. The current GO source has the same wording, but Bi
    et al. 1998 distinguish an early Myo1 ring from subsequent actin recruitment near
    the end of anaphase. The definition conflates a myosin precursor with the completed
    actomyosin structure. Correct the localized timing without changing the GO identity
    or transferring budding-yeast chronology to the fission-yeast graph.
  target_ids:
  - GO:0110085
  field_paths:
  - definition
  evidence_ids:
  - record
  - go
  - bi
  - rules
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/mitotic_actomyosin_contractile_ring.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: major
  normalization_reason: A material cell-cycle claim conflates distinct assembly states;
    identity remains valid, so this is not an identity blocker.
actions:
- action_id: A1
  description: Correct only the S. cerevisiae timing clause and document the primary-evidence
    qualification to the GO definition.
  finding_ids:
  - F1
  target_ids:
  - GO:0110085
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/mitotic_actomyosin_contractile_ring.yaml
    role: maintained scientific record
  generator: scripts/build_text_embedding_map.py --refresh; scripts/render_pages.py
  acceptance_checks:
  - Definition distinguishes Myo1 localization before budding from actin joining near
    the end of anaphase.
  - Add claim-linked Bi et al. evidence and a durable discussion preserving the GO-versus-primary-source
    disagreement.
  - Keep GO identity, parentage, fission-yeast fields, graph, existing discussions
    and status unchanged.
  - Use guarded writer and append actual Codex curation/EDIT history; preserve all
    earlier reviews.
  - Focused regressions fail before the fix and pass afterward; refresh local embeddings
    and pages, then pass native QC and review validation.
limitations:
- Same-agent whole-record review, not independent human scientific approval.
- No raw-image or raw-data reanalysis; primary Results, Methods and relevant discussion
  were inspected.
- iModulonDB has no matching fungal dataset; ontology label/identifier namespace skips
  and three existing empty-parameter test skips remain explicit.
- The seven clean bud-neck/septin records have separate operational coverage and no
  review-output records.
- The error is present upstream in GO. No external ontology changes or submission
  are claimed.
```
