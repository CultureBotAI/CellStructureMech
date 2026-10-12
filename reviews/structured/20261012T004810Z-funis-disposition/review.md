# funis: supported finding disposition

- Review: 20261012T004810Z-funis-disposition
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-12T00:48:09Z
- Finished UTC: 2026-10-12T00:48:10Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Exact saved major finding resolved; original observation, histories and PROPOSED status retained.

## Scope And Provenance

Exact saved finding and surrounding-content preservation reassessed, not a repeated whole-record review.

Selection: 20261012T002830Z-funis-audit
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e1f17671498e34d3cfeb6bbca77cc970f2c8a520.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:funis | data/structures/cytoskeleton/funis.yaml | maintained | funis |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| focused | passed | True | cellstructuremech:funis | ................................                                         [100%]<br>32 passed in 42.00s |
| funis-strict | passed | True | cellstructuremech:funis | Actual deterministic check passed; scientific support assessed separately. |
| funis-snippets | passed | True | cellstructuremech:funis | No verbatim snippets; paraphrases assessed separately against inspected text. |
| history | passed | True | cellstructuremech:funis | Actual deterministic check passed; scientific support assessed separately. |
| labels | passed | True | cellstructuremech:funis | id↔label correspondence summary:<br>          OK_CANONICAL: 3545<br>            OK_SYNONYM: 50<br>          OK_EXCEPTION: 6<br>    SKIPPED_NO_ADAPTER: 603<br><br>✅ All id↔label pairs correspond. |
| curies | passed | True | cellstructuremech:funis | resolver control: every resolver accepts a known id and rejects a fabricated one<br><br>identifier liveness summary:<br>  OK             4016<br>  SKIPPED         251<br><br>Every identifier resolves at its issuing authority. |
| traits | passed | True | cellstructuremech:funis | Actual deterministic check passed; scientific support assessed separately. |
| release-qc | passed | True | cellstructuremech:funis | Full local QC passed: 967 passed, 3 skipped in 519.11s (0:08:39). PR and native merge-group gates remain separate. |

## Scientific And Domain Assessments

### Represent funis as part of the cytoskeleton

grounding: supported. Targets: cellstructuremech:funis.

The funis now has the verified intracellular anatomical structure class as its broad parent and cytoskeleton as its containing whole. Microtubule has_part, component scope and the proposed tail-flexion model are unchanged.

## Findings

### F1: Represent funis as part of the cytoskeleton

major / resolved / confirmed; issue key: funis-cytoskeleton-parthood.

The funis now has the verified intracellular anatomical structure class as its broad parent and cytoskeleton as its containing whole. Microtubule has_part, component scope and the proposed tail-flexion model are unchanged.

Disposition: The funis now has the verified intracellular anatomical structure class as its broad parent and cytoskeleton as its containing whole. Microtubule has_part, component scope and the proposed tail-flexion model are unchanged. Verified by inspected authority/source evidence, bounded native diff, red/green regressions and full local QC.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/funis.yaml | context_only | Whole corrected YAML reread; exact expected mutation and appended event verified against baseline. |
| rules | docs/CURATION.md | context_only | Parent means is-a; cytoskeletal substructures use part_of the whole framework. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml | context_only | Typed is-a, proper-parthood and evidence-bearing component/graph contracts read. |
| reading | /private/tmp/csm-review-20261012T002200Z/reading-checkpoint.json | context_only | Actual source-reading chronology and abstract/full-text/visual limits retained. |
| predecessors | /private/tmp/csm-review-20261012T002200Z/predecessors.json | context_only | Ignored-inclusive canonical scan found no exact-target predecessor. |
| context | /private/tmp/csm-review-20261012T002200Z/context-search.log | context_only | Ignored/hidden-inclusive identifier and slug search; Git internals and dependency trees excluded. |
| go-relations | /private/tmp/csm-review-20261011T232800Z/read-ahead/go-relations.log | context_only | Complete source-native typed OAK relations inspected; independent QuickGO child relation agrees. |
| adapter | /private/tmp/csm-review-20261011T232800Z/read-ahead/adapter-and-search.json | context_only | Verified 28-row iModulonDB inventory has no applicable Giardia or Tetrahymena dataset; not biological absence evidence. |
| issue-dedup | /private/tmp/csm-review-20261012T002200Z/dedup-funis-cytoskeleton-parthood.log | context_only | All-state exact-key GitHub issue search checked before creation. |
| history-0 | history/records/funis/2026-09-22T091912Z-claude-code-e805b6.yaml | context_only | Complete existing append-only history read; old actor metadata preserved. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0035253,GO%3A0036064,GO%3A0032123,GO%3A0031912,GO%3A0031910,GO%3A0005856,GO%3A0005874,GO%3A0005622,GO%3A0020038; Exact definitions, synonyms, current status and relation types | supports | Deep fiber and cytoskeleton denote distinct scopes; intracellular anatomical structure is a broad class, not a claim of resolved polymer identity. |
| taxon | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5741; Taxon5741 names and synonyms | supports | Giardia duodenalis accepted name with intestinalis/lamblia synonyms; retained label is not wrong identity. |
| primary | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.jsb.2004.01.017%22&amp;format=json&amp;resultType=core; DOI10.1016/j.jsb.2004.01.017; full primary abstract | supports | Field-emission SEM characterizes funis as short microtubule arrays among several cytoskeletal structures. Caudal-axoneme/dense-rod/epiplasm topology is observed; tail-flexion mechanism remains a proposed model. |
| review | https://pmc.ncbi.nlm.nih.gov/articles/PMC8086724/; DOI10.1016/bs.apar.2019.11.001; sections6/7 and Table3 | supports | Review describes cytoplasmic caudal axonemes and funis microtubule sheets while retaining uncertain shape/tail functions. Not an independent primary perturbation experiment. |
| predecessor | reviews/structured/20261012T002830Z-funis-audit/review.yaml | context_only | Original immutable observation committed before scientific edits. |
| red-tests | /private/tmp/csm-review-20261012T002200Z/regressions-red.log | context_only | Four regressions fail before correction; four preservation controls pass. |
| green-tests | /private/tmp/csm-review-20261012T002200Z/post-focused.log | context_only | All eight regressions and guarded-writer tests pass after correction. |
| preservation | /private/tmp/csm-review-20261012T002200Z/preservation.json | context_only | All 907 other records, all909 vectors, prior histories/reviews/legacy files and both clean-review targets unchanged. |
| edit-history | history/records/funis/2026-10-12T002915Z-codex-1cc068.yaml | context_only | Actual Codex EDIT links original review and issue. Its sections are derived from the exact native diff. |

## Limits And Additional Notes

- Same-agent review, not independent human approval or experimental/raw-image reanalysis.
- Frankel chapter metadata only; primary Benchimol paper abstract only, with later Hagen review sections6/7 and Table3 as secondary context. Scope is stated per source; no global full-text inaccessibility claim.
- Source downloads and read-ahead preserve original timestamps and hashes. Current native files, schema, all original histories and local rules were reread and captured against merged main.
- Unknown constituent families and mechanisms remain genuine uncertainties, not absence assertions. iModulonDB lacks applicable taxa and supplies no negative evidence.
- Ciliary rootlet and cryptophyte cortical centrin network are separately reviewed targets; this issue-bearing bundle does not certify them.
- Full local QC now passed; PR and native merge-group gates are separate publication checks. Existing policy/no-adapter and test skips retained.
- This is a same-agent scoped disposition, not a repeated whole-record review. Exact corrected inputs retained by review-base/rootlet-funis-evidence-20261012.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T004810Z-funis-disposition
kind: record
repository: CultureBotAI/CellStructureMech
title: 'funis: supported finding disposition'
started_at: '2026-10-12T00:48:09Z'
finished_at: '2026-10-12T00:48:10Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent whole-record and source assessment; not independent
    human approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Exact saved major finding resolved; original observation, histories and PROPOSED
  status retained.
source:
  git_revision: e1f17671498e34d3cfeb6bbca77cc970f2c8a520
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
    sha256: 3acb13884094f40c840ed3452a6209ee9a38b479ae16e4c0bca390c3c290828a
    role: context
  - path: curation/source_queue.tsv
    sha256: 55d8fe79b5edd7d6b42bf4ca9168fe4878240417716e2f4ba423489144b89284
    role: context
  - path: data/structures/cytoskeleton/ciliary_rootlet.yaml
    sha256: 7e83f24e1bd10b9945a81a6f912aae66c8ca18a751aa4147a7d0a5bcf3fa88c9
    role: context
  - path: data/structures/cytoskeleton/cryptophyte_cortical_centrin_network.yaml
    sha256: cb0d5b64a7ea83ca03ae0ec91abad982f682314b29d0e89fe0f62cbaa2072819
    role: context
  - path: data/structures/cytoskeleton/deep_fiber.yaml
    sha256: 7868013c7bf3ce1c327c9106136b716f305afebe4efe5d49412e69278d26d702
    role: context
  - path: data/structures/cytoskeleton/funis.yaml
    sha256: f4410ba245ffdd163c6cbff4adf7292cb348b39ff2952c7484091aaeed4aa9be
    role: target
  - path: data/structures/other/cytostome.yaml
    sha256: e098724aea296245130198ea537eab00b38dd2429c7d91aeac78d09efab7d735
    role: context
  - path: data/structures/other/oral_apparatus.yaml
    sha256: 55dd7652482846930c83b0340be155e52c094dbdf9232427bc76580cbe65a372
    role: context
  - path: docs/CURATION.md
    sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
    role: context
  - path: docs/SCHEMA.md
    sha256: 07b8f936a553a45cc6e8dba924c21e6af48c81b3866725efeb00c8183f0c75a2
    role: context
  - path: docs/SOURCE_QUEUE.md
    sha256: 793e9a16435684b90b0d64b7be4bdfeffbba5ab6ac0ca99eadf25c8548e22729
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
  - path: history/records/funis/2026-09-22T091912Z-claude-code-e805b6.yaml
    sha256: c96b6b34119dfe44289a349e1ed279f75b820901a8119a46c0af709d95a4bbcd
    role: context
  - path: history/records/funis/2026-10-12T002915Z-codex-1cc068.yaml
    sha256: 5de322072649153790188eda44f03267942306188e2be139447570a21dddd01b
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: pages/structures/cytoskeleton/funis.html
    sha256: e6112be62cc694f3a818df6a5ca248993cc86ae2ce10f29a1dd23e6308947fa3
    role: context
  - path: reviews/structured/20261012T002830Z-funis-audit/review.yaml
    sha256: 5da58e29f4d5692cdb331b983281b5fd67dff627adb795f56eb14b09bf694c5c
    role: context
  - path: scripts/render_pages.py
    sha256: b5be74a8a3a0f7190b63da47a86cd8b48cbce4bb955ea0896f29d24f214a9b22
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: src/cellstructuremech/templates/structure.html
    sha256: 417b020a6eda677a1e40ecd3d849bfd5063d83291d7496e1c52a1a3a321f35ed
    role: context
  - path: tests/test_deep_fiber_funis_relations.py
    sha256: c307b1c48d0d48d3ad21298d878286e9b43b977d96f03efd3fabae1651d23068
    role: context
targets:
- target_id: cellstructuremech:funis
  path: data/structures/cytoskeleton/funis.yaml
  label: funis
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/funis.yaml
    role: maintained scientific record
scope:
  description: Exact saved finding and surrounding-content preservation reassessed,
    not a repeated whole-record review.
  selection: 20261012T002830Z-funis-audit
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:funis
checks:
- check_id: focused
  name: focused
  status: passed
  required: true
  target_ids:
  - cellstructuremech:funis
  command: .venv/bin/python -m pytest -q tests/test_deep_fiber_funis_relations.py
    tests/test_write_validated.py
  exit_code: 0
  expected_exit_code: 0
  summary: '................................                                         [100%]

    32 passed in 42.00s'
  scope_note: 2026-10-12T00:31:02Z to 2026-10-12T00:31:45Z; log SHA-256 cee29fb2a73fef3e82623d260f7304c7fa70cbb7ae0507c3f690ecae4e36af52
- check_id: funis-strict
  name: funis-strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:funis
  command: .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/funis.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-12T00:32:14Z to 2026-10-12T00:32:20Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: funis-snippets
  name: funis-snippets
  status: passed
  required: true
  target_ids:
  - cellstructuremech:funis
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/cytoskeleton/funis.yaml
    --report /private/tmp/csm-review-20261012T002200Z/post-funis-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: No verbatim snippets; paraphrases assessed separately against inspected
    text.
  scope_note: 2026-10-12T00:32:20Z to 2026-10-12T00:32:46Z; log SHA-256 76a62fd5ec31e6ba130825b4a29c72af0af9ccf523b06b12b351759481bf488c
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - cellstructuremech:funis
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-12T00:32:46Z to 2026-10-12T00:33:01Z; log SHA-256 366443aee9a0bb48ec439583d63f969bf2625f5f7c0147eecbb4e6bc03dab6b9
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - cellstructuremech:funis
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: "id↔label correspondence summary:\n          OK_CANONICAL: 3545\n     \
    \       OK_SYNONYM: 50\n          OK_EXCEPTION: 6\n    SKIPPED_NO_ADAPTER: 603\n\
    \n✅ All id↔label pairs correspond."
  scope_note: 2026-10-12T00:33:01Z to 2026-10-12T00:34:16Z; log SHA-256 459523b233cf29c593d6ebe49a38d5ed4484b1f98496dc47ea4fdc17be729286
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - cellstructuremech:funis
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: "resolver control: every resolver accepts a known id and rejects a fabricated\
    \ one\n\nidentifier liveness summary:\n  OK             4016\n  SKIPPED      \
    \   251\n\nEvery identifier resolves at its issuing authority."
  scope_note: 2026-10-12T00:34:16Z to 2026-10-12T00:35:06Z; log SHA-256 f38fdf2889286b712ede050fc9d6de36ecb8830b57fbc4dfbf38421c176168c8
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - cellstructuremech:funis
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-12T00:35:06Z to 2026-10-12T00:35:33Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: release-qc
  name: release-qc
  status: passed
  required: true
  target_ids:
  - cellstructuremech:funis
  command: just qc
  exit_code: 0
  expected_exit_code: 0
  summary: 'Full local QC passed: 967 passed, 3 skipped in 519.11s (0:08:39). PR and
    native merge-group gates remain separate.'
  scope_note: 2026-10-12T00:35:33Z to 2026-10-12T00:47:44Z; log SHA-256 9db0412c193926184e88a89ab6ca8c5b1056ce2ce06df98d940e58a9aa8991c9
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/funis.yaml
  accessed_at: '2026-10-12T00:48:10Z'
  snapshot_sha256: f4410ba245ffdd163c6cbff4adf7292cb348b39ff2952c7484091aaeed4aa9be
  support: context_only
  summary: Whole corrected YAML reread; exact expected mutation and appended event
    verified against baseline.
- evidence_id: rules
  kind: record_content
  reference: docs/CURATION.md
  accessed_at: '2026-10-12T00:28:30Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  support: context_only
  summary: Parent means is-a; cytoskeletal substructures use part_of the whole framework.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  accessed_at: '2026-10-12T00:28:30Z'
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
  support: context_only
  summary: Typed is-a, proper-parthood and evidence-bearing component/graph contracts
    read.
- evidence_id: reading
  kind: validation
  reference: /private/tmp/csm-review-20261012T002200Z/reading-checkpoint.json
  accessed_at: '2026-10-12T00:28:30Z'
  snapshot_sha256: 1892aa466bea1ad65c69242c2a47aa1607ebec569557c6be532c8e23cae6ff6a
  support: context_only
  summary: Actual source-reading chronology and abstract/full-text/visual limits retained.
- evidence_id: predecessors
  kind: validation
  reference: /private/tmp/csm-review-20261012T002200Z/predecessors.json
  accessed_at: '2026-10-12T00:28:30Z'
  snapshot_sha256: 119428c024fe92271825015756b954df34b27304b559895c8c99912b4c573cb3
  support: context_only
  summary: Ignored-inclusive canonical scan found no exact-target predecessor.
- evidence_id: context
  kind: validation
  reference: /private/tmp/csm-review-20261012T002200Z/context-search.log
  accessed_at: '2026-10-12T00:28:30Z'
  snapshot_sha256: 34448ef49a4cc26fe4a72fb1813acf298576382550c772c1fe4c87f25a06cffa
  support: context_only
  summary: Ignored/hidden-inclusive identifier and slug search; Git internals and
    dependency trees excluded.
- evidence_id: go-relations
  kind: authority
  reference: /private/tmp/csm-review-20261011T232800Z/read-ahead/go-relations.log
  accessed_at: '2026-10-12T00:28:30Z'
  snapshot_sha256: fecf076834d1980872137b74aa8029c6a0e0a3657684d9dfe0c5f73078bbff7f
  support: context_only
  summary: Complete source-native typed OAK relations inspected; independent QuickGO
    child relation agrees.
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/csm-review-20261011T232800Z/read-ahead/adapter-and-search.json
  accessed_at: '2026-10-12T00:28:30Z'
  snapshot_sha256: a875b409f9a310bf6cf60e00bf7dfab5ba819e21a4cf33ced0109b185f6aafad
  support: context_only
  summary: Verified 28-row iModulonDB inventory has no applicable Giardia or Tetrahymena
    dataset; not biological absence evidence.
- evidence_id: issue-dedup
  kind: validation
  reference: /private/tmp/csm-review-20261012T002200Z/dedup-funis-cytoskeleton-parthood.log
  accessed_at: '2026-10-12T00:28:30Z'
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
  support: context_only
  summary: All-state exact-key GitHub issue search checked before creation.
- evidence_id: history-0
  kind: record_content
  reference: history/records/funis/2026-09-22T091912Z-claude-code-e805b6.yaml
  accessed_at: '2026-10-12T00:28:30Z'
  snapshot_sha256: c96b6b34119dfe44289a349e1ed279f75b820901a8119a46c0af709d95a4bbcd
  support: context_only
  summary: Complete existing append-only history read; old actor metadata preserved.
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0035253,GO%3A0036064,GO%3A0032123,GO%3A0031912,GO%3A0031910,GO%3A0005856,GO%3A0005874,GO%3A0005622,GO%3A0020038
  locator: Exact definitions, synonyms, current status and relation types
  accessed_at: '2026-10-11T23:40:12Z'
  snapshot_sha256: 4e17ce630b3097095683c4e2cb5d087a27eccc9bfef5168522e532c407d6b9a3
  support: supports
  summary: Deep fiber and cytoskeleton denote distinct scopes; intracellular anatomical
    structure is a broad class, not a claim of resolved polymer identity.
- evidence_id: taxon
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5741
  locator: Taxon5741 names and synonyms
  accessed_at: '2026-10-11T23:40:27Z'
  snapshot_sha256: 1dcdc380972a71a0a24c80755d8bbacdcb0b6d9988bb5fb1e05ba43f50580dd3
  support: supports
  summary: Giardia duodenalis accepted name with intestinalis/lamblia synonyms; retained
    label is not wrong identity.
- evidence_id: primary
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.jsb.2004.01.017%22&format=json&resultType=core
  locator: DOI10.1016/j.jsb.2004.01.017; full primary abstract
  accessed_at: '2026-10-11T23:38:34Z'
  snapshot_sha256: f0b3acf75f9291d31340ef7a7c9a0a0f089e18e628e2d62f5baa305201b09583
  support: supports
  summary: Field-emission SEM characterizes funis as short microtubule arrays among
    several cytoskeletal structures. Caudal-axoneme/dense-rod/epiplasm topology is
    observed; tail-flexion mechanism remains a proposed model.
- evidence_id: review
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC8086724/
  locator: DOI10.1016/bs.apar.2019.11.001; sections6/7 and Table3
  accessed_at: '2026-10-11T23:39:13Z'
  snapshot_sha256: b85ef5e57906c7de5b1c9512f84d947cc3d227fc2edaaafa490efaf3af920211
  support: supports
  summary: Review describes cytoplasmic caudal axonemes and funis microtubule sheets
    while retaining uncertain shape/tail functions. Not an independent primary perturbation
    experiment.
- evidence_id: predecessor
  kind: prior_review
  reference: reviews/structured/20261012T002830Z-funis-audit/review.yaml
  accessed_at: '2026-10-12T00:48:10Z'
  snapshot_sha256: 5da58e29f4d5692cdb331b983281b5fd67dff627adb795f56eb14b09bf694c5c
  support: context_only
  summary: Original immutable observation committed before scientific edits.
- evidence_id: red-tests
  kind: validation
  reference: /private/tmp/csm-review-20261012T002200Z/regressions-red.log
  accessed_at: '2026-10-12T00:48:10Z'
  snapshot_sha256: 49dd292636472c404c239d7eff5f906242f102ffa0f66dfacf2295c20ebe988f
  support: context_only
  summary: Four regressions fail before correction; four preservation controls pass.
- evidence_id: green-tests
  kind: validation
  reference: /private/tmp/csm-review-20261012T002200Z/post-focused.log
  accessed_at: '2026-10-12T00:48:10Z'
  snapshot_sha256: cee29fb2a73fef3e82623d260f7304c7fa70cbb7ae0507c3f690ecae4e36af52
  support: context_only
  summary: All eight regressions and guarded-writer tests pass after correction.
- evidence_id: preservation
  kind: validation
  reference: /private/tmp/csm-review-20261012T002200Z/preservation.json
  accessed_at: '2026-10-12T00:48:10Z'
  snapshot_sha256: abb7a802a60e1adc3f84502c584487e0374abaa0f962a017a6e830b1cbe896dd
  support: context_only
  summary: All 907 other records, all909 vectors, prior histories/reviews/legacy files
    and both clean-review targets unchanged.
- evidence_id: edit-history
  kind: record_content
  reference: history/records/funis/2026-10-12T002915Z-codex-1cc068.yaml
  accessed_at: '2026-10-12T00:48:10Z'
  snapshot_sha256: 5de322072649153790188eda44f03267942306188e2be139447570a21dddd01b
  support: context_only
  summary: Actual Codex EDIT links original review and issue. Its sections are derived
    from the exact native diff.
assessments:
- assessment_id: resolved
  area: grounding
  topic: Represent funis as part of the cytoskeleton
  outcome: supported
  target_ids:
  - cellstructuremech:funis
  evidence_ids:
  - record
  - rules
  - schema
  - go
  - primary
  - review
  - predecessor
  - red-tests
  - green-tests
  - preservation
  - edit-history
  summary: The funis now has the verified intracellular anatomical structure class
    as its broad parent and cytoskeleton as its containing whole. Microtubule has_part,
    component scope and the proposed tail-flexion model are unchanged.
findings:
- finding_id: F1
  issue_key: funis-cytoskeleton-parthood
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Represent funis as part of the cytoskeleton
  description: The funis now has the verified intracellular anatomical structure class
    as its broad parent and cytoskeleton as its containing whole. Microtubule has_part,
    component scope and the proposed tail-flexion model are unchanged.
  target_ids:
  - cellstructuremech:funis
  field_paths:
  - parent_structures
  - part_of
  evidence_ids:
  - record
  - rules
  - schema
  - go
  - primary
  - review
  - predecessor
  - red-tests
  - green-tests
  - preservation
  - edit-history
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/funis.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: major
  normalization_reason: Wrong is-a versus proper-parthood relation changes structured
    biological meaning; exact record identity otherwise remains supported.
  disposition_reason: The funis now has the verified intracellular anatomical structure
    class as its broad parent and cytoskeleton as its containing whole. Microtubule
    has_part, component scope and the proposed tail-flexion model are unchanged. Verified
    by inspected authority/source evidence, bounded native diff, red/green regressions
    and full local QC.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261012T002830Z-funis-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2273
actions: []
limitations:
- Same-agent review, not independent human approval or experimental/raw-image reanalysis.
- Frankel chapter metadata only; primary Benchimol paper abstract only, with later
  Hagen review sections6/7 and Table3 as secondary context. Scope is stated per source;
  no global full-text inaccessibility claim.
- Source downloads and read-ahead preserve original timestamps and hashes. Current
  native files, schema, all original histories and local rules were reread and captured
  against merged main.
- Unknown constituent families and mechanisms remain genuine uncertainties, not absence
  assertions. iModulonDB lacks applicable taxa and supplies no negative evidence.
- Ciliary rootlet and cryptophyte cortical centrin network are separately reviewed
  targets; this issue-bearing bundle does not certify them.
- Full local QC now passed; PR and native merge-group gates are separate publication
  checks. Existing policy/no-adapter and test skips retained.
- This is a same-agent scoped disposition, not a repeated whole-record review. Exact
  corrected inputs retained by review-base/rootlet-funis-evidence-20261012.
links:
- https://github.com/CultureBotAI/CellStructureMech/issues/2273
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261012T002830Z-funis-audit
  relationship: Resolves the exact original finding occurrence without replacing its
    bundle.
```
