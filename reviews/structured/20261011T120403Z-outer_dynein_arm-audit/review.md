# outer dynein arm: scientific record review

- Review: 20261011T120403Z-outer_dynein_arm-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T11:56:26Z
- Finished UTC: 2026-10-11T12:04:03Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Entire native record reviewed. One minor composition-versus-assembly wording finding is saved before curation.

## Scope And Provenance

Entire native YAML: identity, hierarchy, parthood, components, taxon and example, function, every graph edge and description, discussions, evidence and both history surfaces.

Selection: One exact record in the 909-record goal; other targets have separate coverage accounting.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base b8492a0b5913cd3301bb30b1c261a9d3f3759574.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0036157 | data/structures/cytoskeleton/outer_dynein_arm.yaml | maintained | outer dynein arm |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0036157 | Actual deterministic check passed; scientific support assessed separately. |
| strict | passed | True | GO:0036157 | Actual deterministic check passed; scientific support assessed separately. |
| snippets | passed | True | GO:0036157 | No verbatim snippets; paraphrases assessed separately against inspected text. |
| history | passed | True | GO:0036157 | Actual deterministic check passed; scientific support assessed separately. |
| labels | passed | True | GO:0036157 | id↔label correspondence summary:<br>          OK_CANONICAL: 3544<br>            OK_SYNONYM: 50<br>          OK_EXCEPTION: 6<br>    SKIPPED_NO_ADAPTER: 603<br><br>✅ All id↔label pairs correspond. |
| traits | passed | True | GO:0036157 | Actual deterministic check passed; scientific support assessed separately. |
| curies | passed | True | GO:0036157 | resolver control: every resolver accepts a known id and rejects a fabricated one<br><br>identifier liveness summary:<br>  OK             4014<br>  SKIPPED         251<br><br>Every identifier resolves at its issuing authority. |
| reviews | passed | True | GO:0036157 | Actual deterministic check passed; scientific support assessed separately. |
| diff | passed | True | GO:0036157 | Actual deterministic check passed; scientific support assessed separately. |
| contract | passed | True | GO:0036157 | ....                                                                     [100%]<br>4 passed in 93.55s (0:01:33) |
| Exact-baseline native CI QC | passed | True | GO:0036157 | Verified exact-baseline merge-group QC: 851 passed, 3 skipped. Not a new local full QC run. |

## Scientific And Domain Assessments

### Structure identity, hierarchy and parthood

grounding: supported. Targets: GO:0036157.

Exact GO identity is valid. Both arm classes are axonemal dynein complexes within the axoneme; these are not single-protein records.

### Composition, taxon, function and all attachment/motility edges

evidence: supported. Targets: GO:0036157.

Label-only component cohorts and UNKNOWN essentiality preserve uncertainty. Chlamydomonas occurrence, demembranated-axoneme example, outer-doublet attachment and coarse microtubule-sliding function are supported. No exact accession, universal chain copy number or direct force measurement is asserted.

### Composition versus assembly semantics

evidence: concern. Targets: GO:0036157.

Three component edges use assemble into, while their descriptions and only edge-local evidence, GO:0036157, state constituent membership. The graph is explicitly NONMECHANISTIC. Assembly predicates and the matching description overstate the represented evidence; this review does not dispute that dynein chains participate in biological assembly.

### Discussions, history, optional resources and status

completeness: supported. Targets: GO:0036157.

The open component-grounding task is an acknowledged limitation, not a defect. No images, datasets, physical measurements, protein-example accessions, trait or pathway links are asserted. Original audit history is retained and native status remains PROPOSED.

## Findings

### F1: Represent outer-arm composition as parthood, not assembly

minor / open / confirmed; issue key: outer-dynein-arm-composition-not-assembly.

Three component edges use assemble into, while their descriptions and only edge-local evidence, GO:0036157, state constituent membership. The graph is explicitly NONMECHANISTIC. Assembly predicates and the matching description overstate the represented evidence; this review does not dispute that dynein chains participate in biological assembly.

## Recommended Actions And Acceptance Checks

### A1

Represent outer-arm composition as parthood, not assembly

- Change only the three constituent-to-arm predicates to are part of; retain all other edges and their evidence.
- Use constituent wording in the graph description without changing its location or motor-function claims.
- Preserve all component inventories, source notes, discussions, status and original history.
- Guarded writer, appended Codex curation and EDIT history, focused regressions, generated pages and native QC must pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/outer_dynein_arm.yaml | context_only | Entire maintained record inspected before judgement; captured bytes unchanged. |
| rules | docs/CURATION.md | context_only | Evidence must support the narrowest claim and graph relation; unknown component details need not be invented. |
| history | /private/tmp/csm-review-20261011T115516Z/outer_dynein_arm-discussion-history.json | context_only | All committed discussion and inline-event versions inspected; original rationale and dates retained. |
| append-history-0 | history/records/outer_dynein_arm/2026-09-23T085622Z-codex-3c5935.yaml | context_only | Original CREATE/review history and actor metadata inspected. |
| prior-issues | /private/tmp/csm-review-20261011T115516Z/inner-prior-issue.log | context_only | Closed issue 1385 corrected the inner-arm edge to static parthood; its description was not updated. This is context, not a canonical predecessor. |
| issue-search | /private/tmp/csm-review-20261011T115516Z/dynein-all-issues.log | context_only | All-state dynein issue search checked before creating findings. |
| predecessors | /private/tmp/csm-review-20261011T115516Z/exact-target-predecessors.json | context_only | Ignored-inclusive canonical scan found no exact-target predecessor. |
| adapter | /private/tmp/csm-review-20261011T115516Z/adapter.log | context_only | No Chlamydomonas coverage in the live 28-dataset iModulonDB inventory; not negative biological evidence. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005858,GO:0005879,GO:0005930,GO:0036156,GO:0036157,GO:0051012,GO:0097540,GO:1990717,GO:1990719,GO:1990720; Exact dynein-arm/axonemal-dynein definitions, typed is_a and part_of relations, microtubule-sliding identity | supports | The arm terms describe constituent chains and location. They do not supply an assembly pathway or establish individual chain cohorts as sufficient assembly inputs. |
| taxon | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055; TaxId 3055 scientificName and species rank | supports | Chlamydomonas reinhardtii identity verified; species prevalence is assessed from structural context, not taxonomy. |
| paper-id | DOI:10.1126/science.1128618; Exact DOI, PMID 16917055, title and primary abstract | supports | Nicastro et al. 2006 publication identity verified. |
| primary-text | DOI:10.1126/science.1128618; Author-uploaded full text: https://www.researchgate.net/publication/6871150_The_Molecular_Architecture_of_Axonemes_Revealed_by_Cryoelectron_Tomography ; introduction, specimen paragraph, dynein-position section, IDA organization section, Figures 1/3 captions | supports | Inspected actual article text supports Chlamydomonas arm location, motor-chain membership and sliding-force context. Structural observations and a motility model are not direct tests of how individual chain cohorts assemble a complete arm. |

## Limits And Additional Notes

- Same-agent whole-record review, not independent human approval.
- No raw-image or experimental-data reanalysis; actual primary text was inspected through public author-uploaded web retrieval.
- Full QC is verified exact-baseline CI; local scoped/global and contract checks ran separately. Resolver/label namespace skips and existing test skips remain explicit.
- Unknown exact chain-family groundings, accessory subunits and beat-cycle regulation remain legitimate curation TODOs. No matching iModulonDB coverage.
- C1/C2 records have separate clean operational coverage; this issue-only bundle does not certify them.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T120403Z-outer_dynein_arm-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'outer dynein arm: scientific record review'
started_at: '2026-10-11T11:56:26Z'
finished_at: '2026-10-11T12:04:03Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent source and native-record review, not independent
    human approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Entire native record reviewed. One minor composition-versus-assembly wording
  finding is saved before curation.
source:
  git_revision: b8492a0b5913cd3301bb30b1c261a9d3f3759574
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
  - path: data/structures/cytoskeleton/axonemal_dynein_complex.yaml
    sha256: 9158b3b827892de2d3f14320353af5fbd6ef8ef3cfae114687b9e6725f7ce44e
    role: context
  - path: data/structures/cytoskeleton/axoneme.yaml
    sha256: 0b91b4cd41d1a34bdc3883d988f31009effc74347b881cdc5c9b66014704e223
    role: context
  - path: data/structures/cytoskeleton/c1_axonemal_microtubule.yaml
    sha256: 2f4f420d4958d3133a60a7b072e517361d7c2c4908acb4e307bd2033095f18f4
    role: context
  - path: data/structures/cytoskeleton/c2_axonemal_microtubule.yaml
    sha256: 97c8666ddef318d146a2d902a225f8b0313468bcf54fa32d81d5f1d127798a44
    role: context
  - path: data/structures/cytoskeleton/inner_dynein_arm.yaml
    sha256: 6ea8fde6434c952487523b582d7f7d4ab3b109b43d8ebcdff95b05e8792b5efa
    role: context
  - path: data/structures/cytoskeleton/outer_dynein_arm.yaml
    sha256: 603e0ea1e7be6fd3394503046ecdcf070ac1b772f44da330293712359c4ddfa8
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
  - path: history/records/outer_dynein_arm/2026-09-23T085622Z-codex-3c5935.yaml
    sha256: b00baaacb24a056ba6e8d7fe8b6f4a00108af198456a7ffb46a870a14b316a22
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
- target_id: GO:0036157
  path: data/structures/cytoskeleton/outer_dynein_arm.yaml
  label: outer dynein arm
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/outer_dynein_arm.yaml
    role: maintained scientific record
scope:
  description: 'Entire native YAML: identity, hierarchy, parthood, components, taxon
    and example, function, every graph edge and description, discussions, evidence
    and both history surfaces.'
  selection: One exact record in the 909-record goal; other targets have separate
    coverage accounting.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0036157
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - GO:0036157
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/outer_dynein_arm.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T11:58:32Z to 2026-10-11T11:58:35Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - GO:0036157
  command: .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/outer_dynein_arm.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T11:58:35Z to 2026-10-11T11:58:40Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - GO:0036157
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/cytoskeleton/outer_dynein_arm.yaml
    --report /private/tmp/csm-review-20261011T115516Z/outer_dynein_arm-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: No verbatim snippets; paraphrases assessed separately against inspected
    text.
  scope_note: 2026-10-11T11:58:40Z to 2026-10-11T11:59:13Z; log SHA-256 19539338e3ec8ee46e88fd4402d57b05571ffa76495c7c8af6d9dcde78df854e
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:0036157
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T11:59:13Z to 2026-10-11T11:59:34Z; log SHA-256 b6444e684401cdf21a031611896cf2c8abe38a769f74d7f2494567d4ca7eea04
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - GO:0036157
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: "id↔label correspondence summary:\n          OK_CANONICAL: 3544\n     \
    \       OK_SYNONYM: 50\n          OK_EXCEPTION: 6\n    SKIPPED_NO_ADAPTER: 603\n\
    \n✅ All id↔label pairs correspond."
  scope_note: 2026-10-11T11:59:34Z to 2026-10-11T12:01:28Z; log SHA-256 d423103555a6a5b538a7c811a73a29c24ed0e5a2eae00d1bb94715295f23f7cb
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - GO:0036157
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T12:01:28Z to 2026-10-11T12:01:55Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - GO:0036157
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: "resolver control: every resolver accepts a known id and rejects a fabricated\
    \ one\n\nidentifier liveness summary:\n  OK             4014\n  SKIPPED      \
    \   251\n\nEvery identifier resolves at its issuing authority."
  scope_note: 2026-10-11T12:01:55Z to 2026-10-11T12:02:49Z; log SHA-256 ee1c5f2e78a2d29fcb6781a8ecd722934376595042d2cc261b4465b361d19b79
- check_id: reviews
  name: reviews
  status: passed
  required: true
  target_ids:
  - GO:0036157
  command: .venv/bin/python scripts/record_review.py check --base b8492a0b5913cd3301bb30b1c261a9d3f3759574
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T12:02:49Z to 2026-10-11T12:03:54Z; log SHA-256 447d9c639cc60fd9ee6fc02a4d40dbdefa5afabe6053baab116979ce20805467
- check_id: diff
  name: diff
  status: passed
  required: true
  target_ids:
  - GO:0036157
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T12:03:54Z to 2026-10-11T12:03:54Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- check_id: contract
  name: contract
  status: passed
  required: true
  target_ids:
  - GO:0036157
  command: .venv/bin/python -m pytest -q tests/test_record_review_contract.py
  exit_code: 0
  expected_exit_code: 0
  summary: '....                                                                     [100%]

    4 passed in 93.55s (0:01:33)'
  scope_note: 2026-10-11T11:55:52Z to 2026-10-11T11:57:27Z; log SHA-256 4732593e9a19ce8a93f6f7c76b33bf107d0ed065213af5366e019c2420aa0ec6
- check_id: qc
  name: Exact-baseline native CI QC
  status: passed
  required: true
  target_ids:
  - GO:0036157
  command: gh run view 38136810050 --repo CultureBotAI/CellStructureMech --log
  exit_code: 0
  expected_exit_code: 0
  summary: 'Verified exact-baseline merge-group QC: 851 passed, 3 skipped. Not a new
    local full QC run.'
  scope_note: https://github.com/CultureBotAI/CellStructureMech/actions/runs/38136810050;
    log SHA-256 9a566cce6a9ca3783d046c571e28512b94d8f05ff921fd8b8807e9db38a6d585
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/outer_dynein_arm.yaml
  accessed_at: '2026-10-11T12:04:03Z'
  snapshot_sha256: 603e0ea1e7be6fd3394503046ecdcf070ac1b772f44da330293712359c4ddfa8
  support: context_only
  summary: Entire maintained record inspected before judgement; captured bytes unchanged.
- evidence_id: rules
  kind: record_content
  reference: docs/CURATION.md
  accessed_at: '2026-10-11T12:04:03Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  support: context_only
  summary: Evidence must support the narrowest claim and graph relation; unknown component
    details need not be invented.
- evidence_id: history
  kind: record_content
  reference: /private/tmp/csm-review-20261011T115516Z/outer_dynein_arm-discussion-history.json
  accessed_at: '2026-10-11T12:04:03Z'
  snapshot_sha256: abad054f19700455ffc088e7401c29168e27af3c6e86b66b9cfb76d5d4c900c3
  support: context_only
  summary: All committed discussion and inline-event versions inspected; original
    rationale and dates retained.
- evidence_id: append-history-0
  kind: record_content
  reference: history/records/outer_dynein_arm/2026-09-23T085622Z-codex-3c5935.yaml
  accessed_at: '2026-10-11T12:04:03Z'
  snapshot_sha256: b00baaacb24a056ba6e8d7fe8b6f4a00108af198456a7ffb46a870a14b316a22
  support: context_only
  summary: Original CREATE/review history and actor metadata inspected.
- evidence_id: prior-issues
  kind: prior_review
  reference: /private/tmp/csm-review-20261011T115516Z/inner-prior-issue.log
  accessed_at: '2026-10-11T12:04:03Z'
  snapshot_sha256: db61b08dd2957e419bca1afd1698aca12a135b994ec840bb70bbbd1c31af21b5
  support: context_only
  summary: Closed issue 1385 corrected the inner-arm edge to static parthood; its
    description was not updated. This is context, not a canonical predecessor.
- evidence_id: issue-search
  kind: validation
  reference: /private/tmp/csm-review-20261011T115516Z/dynein-all-issues.log
  accessed_at: '2026-10-11T12:04:03Z'
  snapshot_sha256: e7c74f0c2811a0f7bbae786e748b462cfeb45735ccd20135723acad6c51e55dd
  support: context_only
  summary: All-state dynein issue search checked before creating findings.
- evidence_id: predecessors
  kind: validation
  reference: /private/tmp/csm-review-20261011T115516Z/exact-target-predecessors.json
  accessed_at: '2026-10-11T12:04:03Z'
  snapshot_sha256: 186da3531c676cf51472a73accb334683dda8283ac5f1e6c4ff62145aa1955d6
  support: context_only
  summary: Ignored-inclusive canonical scan found no exact-target predecessor.
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/csm-review-20261011T115516Z/adapter.log
  accessed_at: '2026-10-11T12:04:03Z'
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
  support: context_only
  summary: No Chlamydomonas coverage in the live 28-dataset iModulonDB inventory;
    not negative biological evidence.
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005858,GO:0005879,GO:0005930,GO:0036156,GO:0036157,GO:0051012,GO:0097540,GO:1990717,GO:1990719,GO:1990720
  locator: Exact dynein-arm/axonemal-dynein definitions, typed is_a and part_of relations,
    microtubule-sliding identity
  accessed_at: '2026-10-11T11:56:47Z'
  snapshot_sha256: 46cf9606bf3ed226a1d3d55b65c11f8b510cd14b644607267d1e4b898b802baa
  support: supports
  summary: The arm terms describe constituent chains and location. They do not supply
    an assembly pathway or establish individual chain cohorts as sufficient assembly
    inputs.
- evidence_id: taxon
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055
  locator: TaxId 3055 scientificName and species rank
  accessed_at: '2026-10-11T11:56:48Z'
  snapshot_sha256: e3861fe6706cefe2e079e15c0178a65e95efaad3890f548f25e721553eaa93a0
  support: supports
  summary: Chlamydomonas reinhardtii identity verified; species prevalence is assessed
    from structural context, not taxonomy.
- evidence_id: paper-id
  kind: primary_source
  reference: DOI:10.1126/science.1128618
  locator: Exact DOI, PMID 16917055, title and primary abstract
  accessed_at: '2026-10-11T11:56:20Z'
  snapshot_sha256: d770ed57ab44095ac4a836cb572e8c5f510cbe41ea00f2237bda26bfe6e7b991
  support: supports
  summary: Nicastro et al. 2006 publication identity verified.
- evidence_id: primary-text
  kind: primary_source
  reference: DOI:10.1126/science.1128618
  locator: 'Author-uploaded full text: https://www.researchgate.net/publication/6871150_The_Molecular_Architecture_of_Axonemes_Revealed_by_Cryoelectron_Tomography
    ; introduction, specimen paragraph, dynein-position section, IDA organization
    section, Figures 1/3 captions'
  accessed_at: '2026-10-11T12:04:03Z'
  support: supports
  summary: Inspected actual article text supports Chlamydomonas arm location, motor-chain
    membership and sliding-force context. Structural observations and a motility model
    are not direct tests of how individual chain cohorts assemble a complete arm.
assessments:
- assessment_id: identity
  area: grounding
  topic: Structure identity, hierarchy and parthood
  outcome: supported
  target_ids:
  - GO:0036157
  evidence_ids:
  - record
  - go
  summary: Exact GO identity is valid. Both arm classes are axonemal dynein complexes
    within the axoneme; these are not single-protein records.
- assessment_id: biology
  area: evidence
  topic: Composition, taxon, function and all attachment/motility edges
  outcome: supported
  target_ids:
  - GO:0036157
  evidence_ids:
  - record
  - go
  - taxon
  - primary-text
  summary: Label-only component cohorts and UNKNOWN essentiality preserve uncertainty.
    Chlamydomonas occurrence, demembranated-axoneme example, outer-doublet attachment
    and coarse microtubule-sliding function are supported. No exact accession, universal
    chain copy number or direct force measurement is asserted.
- assessment_id: graph-scope
  area: evidence
  topic: Composition versus assembly semantics
  outcome: concern
  target_ids:
  - GO:0036157
  evidence_ids:
  - record
  - go
  - primary-text
  - prior-issues
  - rules
  summary: Three component edges use assemble into, while their descriptions and only
    edge-local evidence, GO:0036157, state constituent membership. The graph is explicitly
    NONMECHANISTIC. Assembly predicates and the matching description overstate the
    represented evidence; this review does not dispute that dynein chains participate
    in biological assembly.
- assessment_id: provenance
  area: completeness
  topic: Discussions, history, optional resources and status
  outcome: supported
  target_ids:
  - GO:0036157
  evidence_ids:
  - record
  - history
  - rules
  summary: The open component-grounding task is an acknowledged limitation, not a
    defect. No images, datasets, physical measurements, protein-example accessions,
    trait or pathway links are asserted. Original audit history is retained and native
    status remains PROPOSED.
findings:
- finding_id: F1
  issue_key: outer-dynein-arm-composition-not-assembly
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Represent outer-arm composition as parthood, not assembly
  description: Three component edges use assemble into, while their descriptions and
    only edge-local evidence, GO:0036157, state constituent membership. The graph
    is explicitly NONMECHANISTIC. Assembly predicates and the matching description
    overstate the represented evidence; this review does not dispute that dynein chains
    participate in biological assembly.
  target_ids:
  - GO:0036157
  field_paths:
  - causal_graphs[0].description
  - causal_graphs[0].edges[0].predicate
  - causal_graphs[0].edges[1].predicate
  - causal_graphs[0].edges[2].predicate
  evidence_ids:
  - record
  - go
  - primary-text
  - prior-issues
  - rules
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/outer_dynein_arm.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: minor
  normalization_reason: Bounded predicate/description overstatement in a coarse nonmechanistic
    graph. Identity, constituent membership and motor function remain supported; no
    false protein identity or universal mechanism is established.
actions:
- action_id: A1
  description: Represent outer-arm composition as parthood, not assembly
  finding_ids:
  - F1
  target_ids:
  - GO:0036157
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/outer_dynein_arm.yaml
    role: maintained scientific record
  acceptance_checks:
  - Change only the three constituent-to-arm predicates to are part of; retain all
    other edges and their evidence.
  - Use constituent wording in the graph description without changing its location
    or motor-function claims.
  - Preserve all component inventories, source notes, discussions, status and original
    history.
  - Guarded writer, appended Codex curation and EDIT history, focused regressions,
    generated pages and native QC must pass.
limitations:
- Same-agent whole-record review, not independent human approval.
- No raw-image or experimental-data reanalysis; actual primary text was inspected
  through public author-uploaded web retrieval.
- Full QC is verified exact-baseline CI; local scoped/global and contract checks ran
  separately. Resolver/label namespace skips and existing test skips remain explicit.
- Unknown exact chain-family groundings, accessory subunits and beat-cycle regulation
  remain legitimate curation TODOs. No matching iModulonDB coverage.
- C1/C2 records have separate clean operational coverage; this issue-only bundle does
  not certify them.
```
