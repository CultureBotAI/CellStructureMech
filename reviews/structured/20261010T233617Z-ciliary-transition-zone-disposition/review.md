# Ciliary transition zone: finding disposition

- Review: 20261010T233617Z-ciliary-transition-zone-disposition
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-10T23:29:26Z
- Finished UTC: 2026-10-10T23:36:17Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The exact predecessor grounding finding is resolved. Remaining molecular inventory is still open and native scientific status remains PROPOSED.

## Scope And Provenance

Reassessment of exact prior finding fields, changed evidence and append-only provenance, not a new whole-record or corpus-wide review.

Selection: F1 in 20261010T232629Z-ciliary-transition-zone-audit
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 55bdb80a88cd3045e03825821f9bb96057ebe7d7.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0035869 | data/structures/appendage/ciliary_transition_zone.yaml | maintained | ciliary transition zone |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0035869 | Actual post-curation command passed. Scientific support assessed separately; identifier namespace skips and empty quoted-snippet fields retain their original limits. |
| strict | passed | True | GO:0035869 | Actual post-curation command passed. Scientific support assessed separately; identifier namespace skips and empty quoted-snippet fields retain their original limits. |
| snippets | passed | True | GO:0035869 | Actual post-curation command passed. Scientific support assessed separately; identifier namespace skips and empty quoted-snippet fields retain their original limits. |
| history | passed | True | GO:0035869 | Actual post-curation command passed. Scientific support assessed separately; identifier namespace skips and empty quoted-snippet fields retain their original limits. |
| labels | passed | True | GO:0035869 | Actual post-curation command passed. Scientific support assessed separately; identifier namespace skips and empty quoted-snippet fields retain their original limits. |
| traits | passed | True | GO:0035869 | Actual post-curation command passed. Scientific support assessed separately; identifier namespace skips and empty quoted-snippet fields retain their original limits. |
| curies | passed | True | GO:0035869 | Actual post-curation command passed. Scientific support assessed separately; identifier namespace skips and empty quoted-snippet fields retain their original limits. The BFO resolver control was not exercised because its authority was unreachable; successful command exit does not certify that control. The separate CI identifier-liveness gate passed. |
| regressions | passed | True | GO:0035869 | Actual post-curation command passed. Scientific support assessed separately; identifier namespace skips and empty quoted-snippet fields retain their original limits. |
| reviews | passed | True | GO:0035869 | Actual post-curation command passed. Scientific support assessed separately; identifier namespace skips and empty quoted-snippet fields retain their original limits. |
| diff | passed | True | GO:0035869 | Actual post-curation command passed. Scientific support assessed separately; identifier namespace skips and empty quoted-snippet fields retain their original limits. |
| Exact-fix authoritative CI QC | passed | True | GO:0035869 | Successful authoritative QC including corpus tests, generated-site and embedding drift checks on the exact inspected fix commit. |

## Scientific And Domain Assessments

### Y-link component retains a stale label-only grounding decision

grounding: supported. Targets: GO:0035869.

The assembled linker now has GO:0097537, canonical label Y-shaped link and PROTEIN_COMPLEX type. Its graph node has the same grounding and label. Old grounding and discussion rationales remain with dated superseding explanations. Segment/network label-only scope, UNKNOWN essentiality, original causal edges and OPEN molecular inventory are preserved; no molecular stoichiometry or linker-specific gating mechanism was added.

## Findings

### F1: Y-link component retains a stale label-only grounding decision

minor / resolved / confirmed; issue key: transition-zone-y-link-grounding.

The assembled linker now has GO:0097537, canonical label Y-shaped link and PROTEIN_COMPLEX type. Its graph node has the same grounding and label. Old grounding and discussion rationales remain with dated superseding explanations. Segment/network label-only scope, UNKNOWN essentiality, original causal edges and OPEN molecular inventory are preserved; no molecular stoichiometry or linker-specific gating mechanism was added.

Disposition: The assembled linker now has GO:0097537, canonical label Y-shaped link and PROTEIN_COMPLEX type. Its graph node has the same grounding and label. Old grounding and discussion rationales remain with dated superseding explanations. Segment/network label-only scope, UNKNOWN essentiality, original causal edges and OPEN molecular inventory are preserved; no molecular stoichiometry or linker-specific gating mechanism was added. Verified against active exact GO identity, retained primary-source limits, post-curation gates and exact-commit authoritative QC.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/ciliary_transition_zone.yaml; Entire YAML, linked cilium/linker context and native histories | context_only | Changed record and full diff re-read. Exact assembled-link identity and graph agree, former rationale retained as superseded, other components unchanged, molecular inventory OPEN, and PROPOSED status retained. |
| zone | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0035869; Exact identity, definition and synonyms | supports | Active GO regional identity; Y-shaped links are constituents, not synonyms of the entire transition zone. |
| link | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097537; Exact identity, definition and synonyms | supports | Active exact Y-shaped protein-complex term, explicitly placed in the ciliary transition zone; matches the currently label-only assembled linker. |
| link-ancestry | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097537/ancestors?relations=is_a,part_of; is_a and part_of ancestry | supports | Linker belongs to the protein-containing-complex hierarchy and lies within the transition zone. Combined ancestry is not treated as pure is-a. |
| cilium | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005929; Identity and definition | supports | Exact enclosing cilium identity, not bacterial flagellum. |
| taxon | https://rest.uniprot.org/taxonomy/3055.json; Taxonomic identity | supports | Chlamydomonas reinhardtii identity matches examples and scoped experiments. |
| craige | DOI:10.1083/jcb.201006105; Results and Figures 3-5 captions; Discussion | supports | CEP290 mutant and localization experiments support normal connector tethering and altered protein composition. Rare residual Y-links and simultaneous wedge defects do not establish isolated Y-link sufficiency. |
| diener | DOI:10.1016/j.cub.2014.11.066; Results: isolation and ultrastructure of transition zones | supports | Isolated transition-zone vesicles were fractionated with cell-wall material and analyzed by proteomics. Isolation loses outer microtubules/stellate structure; native exemplar does not claim an intact in-situ purified molecular inventory. |
| wang | DOI:10.1038/s41467-022-31751-0; Results: transition-zone architecture, localization independence and mutant composition | supports | TCTN1 loss affects wedge-shaped structures, not evident Y-link architecture in the scored sections; CEP290/NPHP4/TCTN1 have distinct composition effects. Current native text preserves these distinctions. |
| garcia | DOI:10.1101/cshperspect.a028134; Review sections on transition-zone architecture and modules | supports | Secondary review context for regional gating and incomplete, lineage-dependent molecular inventory; not a new primary experiment. |
| prior-search | reviews/structured/ and reports/yaml_record_review/; GO:0035869 and transition-zone-y-link-grounding | context_only | No canonical predecessor targeting this exact record found within the ignored-inclusive review roots. Related linker report is not a transition-zone review. |
| predecessor | reviews/structured/20261010T232629Z-ciliary-transition-zone-audit/review.yaml | context_only | Immutable original observation, retained with exact finding ID and stable issue key. |
| preservation | /private/tmp/csm-review-20261010T231420Z/preservation.json | supports | Only the transition-zone native record changed. Other 908 records, all 1651 prior history files, 54 prior canonical bundles and 210 legacy reports retain identical bytes. Prior in-record events preserved. |

## Limits And Additional Notes

- Scoped same-agent disposition, not independent human scientific approval or completion of the all-909-record goal.
- Original source access tiers, snapshots and access times are retained. Exact assembled-link grounding does not complete the molecular inventory or isolate a Y-link-specific transport mechanism.
- Identifier checker namespace skips and quoted-snippet limitations persist; specific authorities and claim support were separately inspected. The local BFO resolver control was unavailable because its authority was unreachable; it is not claimed as exercised.
- Full QC is CI for the exact fix commit. Final review-only PR-head and merge-queue checks remain separate publication gates.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T233617Z-ciliary-transition-zone-disposition
kind: record
repository: CultureBotAI/CellStructureMech
title: 'Ciliary transition zone: finding disposition'
started_at: '2026-10-10T23:29:26Z'
finished_at: '2026-10-10T23:36:17Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent evidence-backed reassessment of the saved finding
    after curation; separate adversarial diff pass recorded on the PR. Not independent
    human sign-off.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The exact predecessor grounding finding is resolved. Remaining molecular
  inventory is still open and native scientific status remains PROPOSED.
source:
  git_revision: 55bdb80a88cd3045e03825821f9bb96057ebe7d7
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
  - path: data/structures/appendage/ciliary_transition_zone.yaml
    sha256: 838186be48d1218255acf36ab66224651934d821c588b570f9f2f9c12166fb3f
    role: target
  - path: data/structures/appendage/cilium.yaml
    sha256: 2536d421f9c482abf35c2d2bf026eb6158ddfec5c2df1f319ca80698cbb56bb8
    role: context
  - path: data/structures/appendage/y_shaped_link.yaml
    sha256: 89637052ba32ba24d695d33a540116783a09124de805feeaa9430f1f5c702841
    role: context
  - path: docs/CURATION.md
    sha256: c3e482fbf381edcf0238e579648b779c3a8803a1d888b89397ad6fc8808dd07d
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
  - path: history/README.md
    sha256: 1636df44f28547f440242afcb4a05ac293b9714b4d7b809cecc30b975e44a522
    role: context
  - path: history/records/ciliary_transition_zone/2026-09-15T140438Z-codex-d1abb5.yaml
    sha256: 8dafa05b894669c3391bffe5b9f650266166a21c5dc2cb4044102152b001cbb6
    role: context
  - path: history/records/ciliary_transition_zone/2026-09-15T141310Z-codex-28d402.yaml
    sha256: c6b3c5987e417cdf36c0551dca1fc6df0789b1f51506d90ddeaadeee7fa302ad
    role: context
  - path: history/records/ciliary_transition_zone/2026-10-10T232709Z-codex-bccaa4.yaml
    sha256: 6c8a660f86ef7407c116a557bbd77356dfcc7aab502f6b7fa8a89da67e7015a6
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reviews/structured/20261010T232629Z-ciliary-transition-zone-audit/review.yaml
    sha256: 2f7f8d572d1c9bb7005892557bab64c32653c1f64a22330ae20587e4cc7e195b
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: tests/test_ciliary_review_corrections.py
    sha256: a09637efb709a10003f63e3d801411d770f9655b72e8ea26c40f201a5d0e069b
    role: context
targets:
- target_id: GO:0035869
  path: data/structures/appendage/ciliary_transition_zone.yaml
  label: ciliary transition zone
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/ciliary_transition_zone.yaml
    role: maintained scientific record
scope:
  description: Reassessment of exact prior finding fields, changed evidence and append-only
    provenance, not a new whole-record or corpus-wide review.
  selection: F1 in 20261010T232629Z-ciliary-transition-zone-audit
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - GO:0035869
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - GO:0035869
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/appendage/ciliary_transition_zone.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Scientific support assessed separately;
    identifier namespace skips and empty quoted-snippet fields retain their original
    limits.
  scope_note: 2026-10-10T23:27:38Z to 2026-10-10T23:27:43Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - GO:0035869
  command: .venv/bin/python scripts/validate_strict.py data/structures/appendage/ciliary_transition_zone.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Scientific support assessed separately;
    identifier namespace skips and empty quoted-snippet fields retain their original
    limits.
  scope_note: 2026-10-10T23:27:43Z to 2026-10-10T23:27:47Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - GO:0035869
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/appendage/ciliary_transition_zone.yaml
    --report /private/tmp/csm-review-20261010T231420Z/post-checks/snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Scientific support assessed separately;
    identifier namespace skips and empty quoted-snippet fields retain their original
    limits.
  scope_note: 2026-10-10T23:27:47Z to 2026-10-10T23:28:17Z; log SHA-256 8ab0e226e4a7798b5560bcfe3eaa39d55396d27e3164fd4c4459b189a4fd82d9
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:0035869
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Scientific support assessed separately;
    identifier namespace skips and empty quoted-snippet fields retain their original
    limits.
  scope_note: 2026-10-10T23:28:17Z to 2026-10-10T23:28:39Z; log SHA-256 087db2f1d2d2af6ce25e6ecdfd166a152d5cc0e25521151fe3cbb0c59df1a223
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - GO:0035869
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Scientific support assessed separately;
    identifier namespace skips and empty quoted-snippet fields retain their original
    limits.
  scope_note: 2026-10-10T23:28:39Z to 2026-10-10T23:31:30Z; log SHA-256 d423103555a6a5b538a7c811a73a29c24ed0e5a2eae00d1bb94715295f23f7cb
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - GO:0035869
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Scientific support assessed separately;
    identifier namespace skips and empty quoted-snippet fields retain their original
    limits.
  scope_note: 2026-10-10T23:31:30Z to 2026-10-10T23:32:04Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - GO:0035869
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Scientific support assessed separately;
    identifier namespace skips and empty quoted-snippet fields retain their original
    limits. The BFO resolver control was not exercised because its authority was unreachable;
    successful command exit does not certify that control. The separate CI identifier-liveness
    gate passed.
  scope_note: 2026-10-10T23:32:04Z to 2026-10-10T23:33:24Z; log SHA-256 2e9bc07c9919e1e93c42cc1faaf08e9652ad00faacba05e189c139f5e1eb1afc
- check_id: regressions
  name: regressions
  status: passed
  required: true
  target_ids:
  - GO:0035869
  command: .venv/bin/python -m pytest -q tests/test_ciliary_review_corrections.py
    tests/test_write_validated.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Scientific support assessed separately;
    identifier namespace skips and empty quoted-snippet fields retain their original
    limits.
  scope_note: 2026-10-10T23:33:24Z to 2026-10-10T23:34:18Z; log SHA-256 b36b9b3bbdc59cf3e8644983baf360489730ffdcc80dfce1abb8b49f7d2b71b2
- check_id: reviews
  name: reviews
  status: passed
  required: true
  target_ids:
  - GO:0035869
  command: .venv/bin/python scripts/record_review.py check --base 48e9549a06f45272815b6c7d38321b801d4c800c
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Scientific support assessed separately;
    identifier namespace skips and empty quoted-snippet fields retain their original
    limits.
  scope_note: 2026-10-10T23:34:18Z to 2026-10-10T23:35:45Z; log SHA-256 1cb8b5a6341d70ec4bc81e9cd18b1e42fbd00448e29ef3f99a4c5504f20063ef
- check_id: diff
  name: diff
  status: passed
  required: true
  target_ids:
  - GO:0035869
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Scientific support assessed separately;
    identifier namespace skips and empty quoted-snippet fields retain their original
    limits.
  scope_note: 2026-10-10T23:35:45Z to 2026-10-10T23:35:45Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- check_id: qc
  name: Exact-fix authoritative CI QC
  status: passed
  required: true
  target_ids:
  - GO:0035869
  command: gh run view 38095210336 --json databaseId,conclusion,headSha,event,jobs,startedAt,updatedAt,url;
    gh run view 38095210336 --log
  exit_code: 0
  expected_exit_code: 0
  summary: Successful authoritative QC including corpus tests, generated-site and
    embedding drift checks on the exact inspected fix commit.
  scope_note: 2026-10-10T23:30:17Z to 2026-10-10T23:35:19Z; https://github.com/CultureBotAI/CellStructureMech/actions/runs/38095210336;
    log SHA-256 a9ef33c4a2de7f1ae8a3566568657b51a792e3eb13c475409edb8b4cbff600e5
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/appendage/ciliary_transition_zone.yaml
  locator: Entire YAML, linked cilium/linker context and native histories
  accessed_at: '2026-10-10T23:36:17Z'
  snapshot_sha256: 838186be48d1218255acf36ab66224651934d821c588b570f9f2f9c12166fb3f
  support: context_only
  summary: Changed record and full diff re-read. Exact assembled-link identity and
    graph agree, former rationale retained as superseded, other components unchanged,
    molecular inventory OPEN, and PROPOSED status retained.
- evidence_id: zone
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0035869
  locator: Exact identity, definition and synonyms
  accessed_at: '2026-10-10T23:15:30Z'
  snapshot_sha256: 53717c0b5d03b56da3697589e576a8a14f0ec5ea563d3531e2ea9e501533981c
  support: supports
  summary: Active GO regional identity; Y-shaped links are constituents, not synonyms
    of the entire transition zone.
- evidence_id: link
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097537
  locator: Exact identity, definition and synonyms
  accessed_at: '2026-10-10T23:15:33Z'
  snapshot_sha256: bc3b53cec4d839726633ca8c4afcb7917793b2555537383d9dbe714bb4ea8a6e
  support: supports
  summary: Active exact Y-shaped protein-complex term, explicitly placed in the ciliary
    transition zone; matches the currently label-only assembled linker.
- evidence_id: link-ancestry
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097537/ancestors?relations=is_a,part_of
  locator: is_a and part_of ancestry
  accessed_at: '2026-10-10T23:17:32Z'
  snapshot_sha256: ef55b84dc232e1e58082cdfaf10a0a2aacf5ab1ae439107e78b1a13dd98c4e74
  support: supports
  summary: Linker belongs to the protein-containing-complex hierarchy and lies within
    the transition zone. Combined ancestry is not treated as pure is-a.
- evidence_id: cilium
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005929
  locator: Identity and definition
  accessed_at: '2026-10-10T23:15:27Z'
  snapshot_sha256: 5720b98b130e903527e1a96849ac46ee6978e83369e460c0f278f16ef9aca041
  support: supports
  summary: Exact enclosing cilium identity, not bacterial flagellum.
- evidence_id: taxon
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/3055.json
  locator: Taxonomic identity
  accessed_at: '2026-10-10T23:15:39Z'
  snapshot_sha256: 31e68163918c110c000e261d4edc5ae389b11e9992f43540ba3b89a9471ce850
  support: supports
  summary: Chlamydomonas reinhardtii identity matches examples and scoped experiments.
- evidence_id: craige
  kind: primary_source
  reference: DOI:10.1083/jcb.201006105
  locator: Results and Figures 3-5 captions; Discussion
  accessed_at: '2026-10-10T23:15:19Z'
  snapshot_sha256: a83f54c0f615e5ac6f3fa935a59ace211da887d0d8c92cbebf04dddc25715f7c
  support: supports
  summary: CEP290 mutant and localization experiments support normal connector tethering
    and altered protein composition. Rare residual Y-links and simultaneous wedge
    defects do not establish isolated Y-link sufficiency.
- evidence_id: diener
  kind: primary_source
  reference: DOI:10.1016/j.cub.2014.11.066
  locator: 'Results: isolation and ultrastructure of transition zones'
  accessed_at: '2026-10-10T23:17:06Z'
  snapshot_sha256: 3fcda6631400e1aaf86713554e4a18e089f7a4b0c3a8e7fe0b95ccb7ee759ee4
  support: supports
  summary: Isolated transition-zone vesicles were fractionated with cell-wall material
    and analyzed by proteomics. Isolation loses outer microtubules/stellate structure;
    native exemplar does not claim an intact in-situ purified molecular inventory.
- evidence_id: wang
  kind: primary_source
  reference: DOI:10.1038/s41467-022-31751-0
  locator: 'Results: transition-zone architecture, localization independence and mutant
    composition'
  accessed_at: '2026-10-10T23:15:15Z'
  snapshot_sha256: 026e49670797cdcbf1f206ff808cd0c87bc56041593c9947ffa32be9ea8a39bd
  support: supports
  summary: TCTN1 loss affects wedge-shaped structures, not evident Y-link architecture
    in the scored sections; CEP290/NPHP4/TCTN1 have distinct composition effects.
    Current native text preserves these distinctions.
- evidence_id: garcia
  kind: primary_source
  reference: DOI:10.1101/cshperspect.a028134
  locator: Review sections on transition-zone architecture and modules
  accessed_at: '2026-10-10T23:17:10Z'
  snapshot_sha256: 4849b5ab5d2090ad1da6304724c8a976d2d574b325c6f6c0af203fe417acf4f9
  support: supports
  summary: Secondary review context for regional gating and incomplete, lineage-dependent
    molecular inventory; not a new primary experiment.
- evidence_id: prior-search
  kind: search
  reference: reviews/structured/ and reports/yaml_record_review/
  locator: GO:0035869 and transition-zone-y-link-grounding
  accessed_at: '2026-10-10T23:26:29Z'
  support: context_only
  search_scope: rg --no-ignore --hidden searched all YAML/Markdown in both review
    roots; related Y-link legacy report read as context.
  summary: No canonical predecessor targeting this exact record found within the ignored-inclusive
    review roots. Related linker report is not a transition-zone review.
- evidence_id: predecessor
  kind: prior_review
  reference: reviews/structured/20261010T232629Z-ciliary-transition-zone-audit/review.yaml
  accessed_at: '2026-10-10T23:36:17Z'
  snapshot_sha256: 2f7f8d572d1c9bb7005892557bab64c32653c1f64a22330ae20587e4cc7e195b
  support: context_only
  summary: Immutable original observation, retained with exact finding ID and stable
    issue key.
- evidence_id: preservation
  kind: validation
  reference: /private/tmp/csm-review-20261010T231420Z/preservation.json
  accessed_at: '2026-10-10T23:27:42Z'
  snapshot_sha256: 8832e576d4f4589bcf5baf0193e3f2a74d26d709b94ce6931c1551b3ef980b85
  support: supports
  summary: Only the transition-zone native record changed. Other 908 records, all
    1651 prior history files, 54 prior canonical bundles and 210 legacy reports retain
    identical bytes. Prior in-record events preserved.
assessments:
- assessment_id: resolved-f1
  area: grounding
  topic: Y-link component retains a stale label-only grounding decision
  outcome: supported
  target_ids:
  - GO:0035869
  evidence_ids:
  - record
  - link
  - link-ancestry
  - craige
  - predecessor
  - preservation
  summary: The assembled linker now has GO:0097537, canonical label Y-shaped link
    and PROTEIN_COMPLEX type. Its graph node has the same grounding and label. Old
    grounding and discussion rationales remain with dated superseding explanations.
    Segment/network label-only scope, UNKNOWN essentiality, original causal edges
    and OPEN molecular inventory are preserved; no molecular stoichiometry or linker-specific
    gating mechanism was added.
findings:
- finding_id: F1
  issue_key: transition-zone-y-link-grounding
  category: grounding
  severity: minor
  status: resolved
  certainty: confirmed
  title: Y-link component retains a stale label-only grounding decision
  description: The assembled linker now has GO:0097537, canonical label Y-shaped link
    and PROTEIN_COMPLEX type. Its graph node has the same grounding and label. Old
    grounding and discussion rationales remain with dated superseding explanations.
    Segment/network label-only scope, UNKNOWN essentiality, original causal edges
    and OPEN molecular inventory are preserved; no molecular stoichiometry or linker-specific
    gating mechanism was added.
  target_ids:
  - GO:0035869
  field_paths:
  - components[0].grounding_status
  - components[0].grounding_notes
  - causal_graphs[0].nodes[1]
  - discussions[0]
  evidence_ids:
  - record
  - link
  - link-ancestry
  - craige
  - predecessor
  - preservation
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/ciliary_transition_zone.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: minor
  normalization_reason: Nonblocking exact-grounding gap with otherwise sound structure
    identity and explicitly incomplete molecular inventory.
  disposition_reason: The assembled linker now has GO:0097537, canonical label Y-shaped
    link and PROTEIN_COMPLEX type. Its graph node has the same grounding and label.
    Old grounding and discussion rationales remain with dated superseding explanations.
    Segment/network label-only scope, UNKNOWN essentiality, original causal edges
    and OPEN molecular inventory are preserved; no molecular stoichiometry or linker-specific
    gating mechanism was added. Verified against active exact GO identity, retained
    primary-source limits, post-curation gates and exact-commit authoritative QC.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261010T232629Z-ciliary-transition-zone-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2164
actions: []
limitations:
- Scoped same-agent disposition, not independent human scientific approval or completion
  of the all-909-record goal.
- Original source access tiers, snapshots and access times are retained. Exact assembled-link
  grounding does not complete the molecular inventory or isolate a Y-link-specific
  transport mechanism.
- Identifier checker namespace skips and quoted-snippet limitations persist; specific
  authorities and claim support were separately inspected. The local BFO resolver
  control was unavailable because its authority was unreachable; it is not claimed
  as exercised.
- Full QC is CI for the exact fix commit. Final review-only PR-head and merge-queue
  checks remain separate publication gates.
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261010T232629Z-ciliary-transition-zone-audit
  relationship: Resolves F1 without rewriting the original observation.
links:
- https://github.com/CultureBotAI/CellStructureMech/issues/2164
```
