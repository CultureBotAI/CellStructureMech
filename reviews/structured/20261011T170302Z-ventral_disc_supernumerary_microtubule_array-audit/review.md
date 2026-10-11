# ventral disc supernumerary microtubule array: whole-record scientific review

- Review: 20261011T170302Z-ventral_disc_supernumerary_microtubule_array-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T16:52:47Z
- Finished UTC: 2026-10-11T17:03:02Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Whole native record reviewed; concrete findings saved before scientific edits.

## Scope And Provenance

Entire native YAML: identity, definition, synonym scope, partonomy, components, taxon/example, functions, every graph edge, evidence, discussions and both history surfaces.

Selection: Exact record in seven-record ventral-disc cohort of the 909-record goal.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 2810e5b8a40317e07e5d92ced38455597e328633.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0097596 | data/structures/cytoskeleton/ventral_disc_supernumerary_microtubule_array.yaml | maintained | ventral disc supernumerary microtubule array |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0097596 | Actual deterministic check passed; scientific support assessed separately. |
| strict | passed | True | GO:0097596 | Actual deterministic check passed; scientific support assessed separately. |
| snippets | passed | True | GO:0097596 | No verbatim snippets; paraphrases assessed separately against inspected text. |
| history | passed | True | GO:0097596 | Actual deterministic check passed; scientific support assessed separately. |
| labels | passed | True | GO:0097596 | id↔label correspondence summary:<br>          OK_CANONICAL: 3544<br>            OK_SYNONYM: 50<br>          OK_EXCEPTION: 6<br>    SKIPPED_NO_ADAPTER: 603<br><br>✅ All id↔label pairs correspond. |
| traits | passed | True | GO:0097596 | Actual deterministic check passed; scientific support assessed separately. |
| curies | passed | True | GO:0097596 | [not exercised] ComplexPortal: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>resolver control: 1 resolver(s) could not be exercised because their authority was unreachable; the rest accept a known id and reject a fabricated one<br><br>identifier liveness summary:<br>  OK             4014<br>  SKIPPED         251<br><br>Every identifier resolves at its issuing authority. |
| reviews | passed | True | GO:0097596 | Actual deterministic check passed; scientific support assessed separately. |
| diff | passed | True | GO:0097596 | Actual deterministic check passed; scientific support assessed separately. |
| contract | passed | True | GO:0097596 | ....                                                                     [100%]<br>4 passed in 100.22s (0:01:40) |
| Exact-baseline native CI QC | passed | True | GO:0097596 | Exact baseline merge-group QC passed: 876 tests passed, 3 skipped. Not a new local full-QC run. |

## Scientific And Domain Assessments

### Structure identity, partonomy and cohort boundaries

grounding: supported. Targets: GO:0097596.

Exact GO identity and six distinct disc substructures retained; organelle versus array versus topological region is not flattened. Tubulin remains a molecular constituent, not a structure identity.

### Taxon, components and retained biological claims

evidence: supported. Targets: GO:0097596.

Giardia trophozoite context and WBC6 experimental scope support existing species examples. Broad tubulin/structural cohorts retain UNKNOWN essentiality and unresolved accessions. No new stoichiometry or force mechanism is inferred.

### Retained composition and disc parthood

evidence: supported. Targets: GO:0097596.

Tubulin constituency, microtubule has_part and ventral-disc part_of are supported. Prior removal of generic assembly and invented topology function is retained.

### Qualify supernumerary-array orientation by its primary reconstruction

evidence: concern. Targets: GO:0097596.

The definition and first graph edge universally repeat the GO description of a left-handed array generally dorsal to the main array. The cited Schwartz 2012 Results describe a short right-handed fragment, and Figure 1F explicitly places the reconstructed supernumerary microtubules ventral to the main array. Hagen 2011 instead describes a left-handed partial array and observes slightly dorsal or ventral localization in Figure 5. Preserve this source disagreement; do not replace one universal orientation with another. Prior #1001 removed unsupported assembly/function claims but did not resolve this primary-source conflict.

### Optional fields and provenance

completeness: supported. Targets: GO:0097596.

No image, physical-property slot, exact protein accession, complex composition, dataset, trait or pathway assertion is present. Optional absence and existing component-grounding TODOs are not defects.

## Findings

### F1: Qualify supernumerary-array orientation by its primary reconstruction

major / open / confirmed; issue key: ventral-disc-supernumerary-topology-source-conflict.

The definition and first graph edge universally repeat the GO description of a left-handed array generally dorsal to the main array. The cited Schwartz 2012 Results describe a short right-handed fragment, and Figure 1F explicitly places the reconstructed supernumerary microtubules ventral to the main array. Hagen 2011 instead describes a left-handed partial array and observes slightly dorsal or ventral localization in Figure 5. Preserve this source disagreement; do not replace one universal orientation with another. Prior #1001 removed unsupported assembly/function claims but did not resolve this primary-source conflict.

## Recommended Actions And Acceptance Checks

### A1

Qualify supernumerary-array orientation by its primary reconstruction

- Use a neutral structural identity and explicitly Schwartz-2012-bounded right-handed/ventral reconstruction in definition and topology graph; retain the GO/Hagen conflict and do not restore a function or assembly mechanism.
- Preserve PROPOSED status, prior discussions/history and unknown groundings; guarded writer, actual Codex EDIT, focused regressions, generated artifacts and full QC must pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/ventral_disc_supernumerary_microtubule_array.yaml | context_only | Entire native YAML read; inspected bytes unchanged. |
| rules | docs/CURATION.md | context_only | Source-neutral molecular labels and evidence bounded to the narrowest supported claim. |
| history | /private/tmp/csm-review-20261011T165130Z/ventral_disc_supernumerary_microtubule_array-discussion-history.json | context_only | All committed discussion and inline-event versions inspected; earlier dates and rationale retained. |
| history-0 | history/records/ventral_disc_supernumerary_microtubule_array/2026-09-15T163453Z-codex-6d6057.yaml | context_only | Original CREATE and correction events inspected; not a new canonical review. |
| history-1 | history/records/ventral_disc_supernumerary_microtubule_array/2026-09-15T164147Z-codex-0ba9bd.yaml | context_only | Original CREATE and correction events inspected; not a new canonical review. |
| predecessors | /private/tmp/csm-review-20261011T165130Z/exact-target-predecessors.json | context_only | Ignored-inclusive scan found no exact-target canonical predecessor. |
| identity-search | /private/tmp/csm-review-20261011T165130Z/identity-scan.log | context_only | Ignored-inclusive identifier/slug/alias search across native records, reviews, reports, history and source queue. Seven distinct disc entities retained; median body and generic microtubule remain separate. |
| issue-search | /private/tmp/csm-review-20261011T165130Z/disc-issues.log | context_only | All-state ventral-disc issue search inspected, including closed #484, #988 and #1001; none resolves these exact whole-disc or source-conflict findings. |
| adapter | /private/tmp/csm-review-20261011T165130Z/adapter.log | context_only | Live iModulonDB inventory has no matching Giardia dataset. Not negative biological evidence. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005874,GO:0097591,GO:0097592,GO:0097593,GO:0097594,GO:0097595,GO:0097596,GO:0097597; Exact eight nonobsolete CC terms; definitions, typed part_of children and synonym scopes | supports | Exact identities and parthood retained; GO itself contains the contractile-protein and supernumerary-orientation claims under review. |
| taxon | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5741; TaxId, rank, scientificName and otherNames | supports | TaxId 5741 is the species Giardia duodenalis, with Giardia intestinalis and Giardia lamblia listed as synonyms. Existing accepted synonym label is not a new species or strain. |
| schwartz | DOI:10.1371/journal.pone.0043783; Results: whole-cell architecture; Figure 1F and Figures 2-7 captions; Table 1; Discussion; methods | supports | Primary tomography supports distinct main array, supernumerary array, microribbons, crossbridges, overlap and crest. Supernumerary reconstruction is a short right-handed fragment ventral to the main array, not a universal dorsal-left-handed rule. |
| figure-1 | /private/tmp/csm-review-20261011T165130Z/schwartz-fig1.jpg | context_only | Actual Figure 1 inspected with caption, including yellow supernumerary array and white main array in panel F; not raw tomogram reanalysis. |
| hagen2011 | DOI:10.1371/journal.pntd.0001442; Results Figures 4-6 and Table 1; Discussion of actin/crest and supernumerary array; methods | supports | Proteomics, immunogold localization and FRAP support stable structural cohorts. Figure 5 reports supernumerary localization slightly dorsal or ventral; its left-handed description conflicts with Schwartz 2012. Discussion rejects the earlier classical actin/myosin account as established disc machinery. |

## Limits And Additional Notes

- Same-agent scientific review, not independent human sign-off or raw-data reanalysis.
- Actual full article text and captions were inspected. Nosala XML returned HTTP 500; official PMC HTML was readable. Schwartz XML is valid JATS beginning with DOCTYPE; its full PMC HTML was used by the reader. Normal web-tool PMC URLs returned interstitials and were not used as evidence.
- Full QC is exact-baseline CI; local schema/strict/snippet/global/contract checks ran separately. Existing namespace and three empty-parameter test skips remain explicit.
- Five other ventral-disc records have clean operational coverage and no review bundles; this bundle does not itself certify those targets. Unknown force generation and component identities remain open.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T170302Z-ventral_disc_supernumerary_microtubule_array-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'ventral disc supernumerary microtubule array: whole-record scientific review'
started_at: '2026-10-11T16:52:47Z'
finished_at: '2026-10-11T17:03:02Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent scientific review, not independent human approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Whole native record reviewed; concrete findings saved before scientific edits.
source:
  git_revision: 2810e5b8a40317e07e5d92ced38455597e328633
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
  - path: data/structures/cytoskeleton/microtubule.yaml
    sha256: 29404191864964cf5b86c3894c7b942d63b83fc4bb1b6b461d7677baad6af305
    role: context
  - path: data/structures/cytoskeleton/ventral_disc.yaml
    sha256: 163ababaa18f8fc9b6d85694e9a3c0520de681f7b4100be22c1e84fb45371759
    role: context
  - path: data/structures/cytoskeleton/ventral_disc_crossbridge.yaml
    sha256: bb35ddad7c8b15916d19fa6e5ad334ca3476221330372020fdf4adc8565db67b
    role: context
  - path: data/structures/cytoskeleton/ventral_disc_dorsal_microribbon.yaml
    sha256: 6bcdbfaaf84c4b6152147340dcbb6f5958d6dc6aca2288e034c3f2c357819425
    role: context
  - path: data/structures/cytoskeleton/ventral_disc_lateral_crest.yaml
    sha256: 6a8127a748d9dcdb2e429d05d817626c02ffed35eb545eb501c0b101758db32b
    role: context
  - path: data/structures/cytoskeleton/ventral_disc_microtubule_array.yaml
    sha256: 184540d5a0f41b8f04fa8e4cac937dc657481eaa999e5420ec315476801a07e3
    role: context
  - path: data/structures/cytoskeleton/ventral_disc_overlap_zone.yaml
    sha256: 983f27caa2fde019c9ab576e64c54bd354b6528a65e0f9ef9cdfbb87abb365ce
    role: context
  - path: data/structures/cytoskeleton/ventral_disc_supernumerary_microtubule_array.yaml
    sha256: 51be0fc3c9459918375889e7848a7ff07d1dea3d2280097b6e044e2eaa59cb8c
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
  - path: history/records/ventral_disc_supernumerary_microtubule_array/2026-09-15T163453Z-codex-6d6057.yaml
    sha256: ba059c951344d3c98eeafe2b25e8146452a81f6c9812272ef565d8ff13bbf3ef
    role: context
  - path: history/records/ventral_disc_supernumerary_microtubule_array/2026-09-15T164147Z-codex-0ba9bd.yaml
    sha256: 2affed4098b0ca1d22e9afb080ca62e957233c230c3e9c0a30c1eb51a04c454d
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
- target_id: GO:0097596
  path: data/structures/cytoskeleton/ventral_disc_supernumerary_microtubule_array.yaml
  label: ventral disc supernumerary microtubule array
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ventral_disc_supernumerary_microtubule_array.yaml
    role: maintained scientific record
scope:
  description: 'Entire native YAML: identity, definition, synonym scope, partonomy,
    components, taxon/example, functions, every graph edge, evidence, discussions
    and both history surfaces.'
  selection: Exact record in seven-record ventral-disc cohort of the 909-record goal.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0097596
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - GO:0097596
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/ventral_disc_supernumerary_microtubule_array.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T16:55:41Z to 2026-10-11T16:55:44Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - GO:0097596
  command: .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/ventral_disc_supernumerary_microtubule_array.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T16:55:44Z to 2026-10-11T16:55:47Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - GO:0097596
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/cytoskeleton/ventral_disc_supernumerary_microtubule_array.yaml
    --report /private/tmp/csm-review-20261011T165130Z/ventral_disc_supernumerary_microtubule_array-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: No verbatim snippets; paraphrases assessed separately against inspected
    text.
  scope_note: 2026-10-11T16:55:47Z to 2026-10-11T16:56:21Z; log SHA-256 0805a8c1c7f9477fbb857f14b39ec7bd84c8a8ad91d67b9a7a403e94819c977e
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:0097596
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T16:56:21Z to 2026-10-11T16:56:43Z; log SHA-256 a57139d93421c43f7ae7718817e6e3763d6bfd7b84ad38c69ed3ad0bf87878f8
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - GO:0097596
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: "id↔label correspondence summary:\n          OK_CANONICAL: 3544\n     \
    \       OK_SYNONYM: 50\n          OK_EXCEPTION: 6\n    SKIPPED_NO_ADAPTER: 603\n\
    \n✅ All id↔label pairs correspond."
  scope_note: 2026-10-11T16:56:43Z to 2026-10-11T16:58:37Z; log SHA-256 d423103555a6a5b538a7c811a73a29c24ed0e5a2eae00d1bb94715295f23f7cb
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - GO:0097596
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T16:58:37Z to 2026-10-11T16:59:03Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - GO:0097596
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: "[not exercised] ComplexPortal: the issuing authority was unreachable after\
    \ 1 attempts, so this resolver was not exercised\nresolver control: 1 resolver(s)\
    \ could not be exercised because their authority was unreachable; the rest accept\
    \ a known id and reject a fabricated one\n\nidentifier liveness summary:\n  OK\
    \             4014\n  SKIPPED         251\n\nEvery identifier resolves at its\
    \ issuing authority."
  scope_note: 2026-10-11T16:59:03Z to 2026-10-11T17:00:33Z; log SHA-256 be1b6f89c9cf85143fb3db11eb38ed3603082d9a70cbc12b029414c8b16386e5
- check_id: reviews
  name: reviews
  status: passed
  required: true
  target_ids:
  - GO:0097596
  command: .venv/bin/python scripts/record_review.py check --base 2810e5b8a40317e07e5d92ced38455597e328633
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T17:00:33Z to 2026-10-11T17:02:02Z; log SHA-256 206c3a4d1033cfdc90c828fc9239cc849b86637aaed10802a73735206cdd35f0
- check_id: diff
  name: diff
  status: passed
  required: true
  target_ids:
  - GO:0097596
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T17:02:02Z to 2026-10-11T17:02:03Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- check_id: contract
  name: contract
  status: passed
  required: true
  target_ids:
  - GO:0097596
  command: .venv/bin/python -m pytest -q tests/test_record_review_contract.py
  exit_code: 0
  expected_exit_code: 0
  summary: '....                                                                     [100%]

    4 passed in 100.22s (0:01:40)'
  scope_note: 2026-10-11T16:52:02Z to 2026-10-11T16:53:43Z; log SHA-256 d044621aad48f4d710b9ce1ca60070879e2fbf49dead7bbf9ddc2c9da2ef403b
- check_id: qc
  name: Exact-baseline native CI QC
  status: passed
  required: true
  target_ids:
  - GO:0097596
  command: gh run view 38156604240 --repo CultureBotAI/CellStructureMech --log
  exit_code: 0
  expected_exit_code: 0
  summary: 'Exact baseline merge-group QC passed: 876 tests passed, 3 skipped. Not
    a new local full-QC run.'
  scope_note: https://github.com/CultureBotAI/CellStructureMech/actions/runs/38156604240;
    log SHA-256 bdbc0d403656942a24c7997d33d818873687d76cf853b4b4b8565415d990dc2a
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/ventral_disc_supernumerary_microtubule_array.yaml
  accessed_at: '2026-10-11T17:03:02Z'
  snapshot_sha256: 51be0fc3c9459918375889e7848a7ff07d1dea3d2280097b6e044e2eaa59cb8c
  support: context_only
  summary: Entire native YAML read; inspected bytes unchanged.
- evidence_id: rules
  kind: record_content
  reference: docs/CURATION.md
  accessed_at: '2026-10-11T17:03:02Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  support: context_only
  summary: Source-neutral molecular labels and evidence bounded to the narrowest supported
    claim.
- evidence_id: history
  kind: record_content
  reference: /private/tmp/csm-review-20261011T165130Z/ventral_disc_supernumerary_microtubule_array-discussion-history.json
  accessed_at: '2026-10-11T17:03:02Z'
  snapshot_sha256: 5e5463096468c1f4be1647579b77705f2d167b120d7bc56d569aa432db3e29c9
  support: context_only
  summary: All committed discussion and inline-event versions inspected; earlier dates
    and rationale retained.
- evidence_id: history-0
  kind: record_content
  reference: history/records/ventral_disc_supernumerary_microtubule_array/2026-09-15T163453Z-codex-6d6057.yaml
  accessed_at: '2026-10-11T17:03:02Z'
  snapshot_sha256: ba059c951344d3c98eeafe2b25e8146452a81f6c9812272ef565d8ff13bbf3ef
  support: context_only
  summary: Original CREATE and correction events inspected; not a new canonical review.
- evidence_id: history-1
  kind: record_content
  reference: history/records/ventral_disc_supernumerary_microtubule_array/2026-09-15T164147Z-codex-0ba9bd.yaml
  accessed_at: '2026-10-11T17:03:02Z'
  snapshot_sha256: 2affed4098b0ca1d22e9afb080ca62e957233c230c3e9c0a30c1eb51a04c454d
  support: context_only
  summary: Original CREATE and correction events inspected; not a new canonical review.
- evidence_id: predecessors
  kind: validation
  reference: /private/tmp/csm-review-20261011T165130Z/exact-target-predecessors.json
  accessed_at: '2026-10-11T17:03:02Z'
  snapshot_sha256: 238a70e93754193431f6bbef9d45643fd74e1a06da1b62ac34db4c568354ce15
  support: context_only
  summary: Ignored-inclusive scan found no exact-target canonical predecessor.
- evidence_id: identity-search
  kind: validation
  reference: /private/tmp/csm-review-20261011T165130Z/identity-scan.log
  accessed_at: '2026-10-11T17:03:02Z'
  snapshot_sha256: 27e8508adb572f4f64f375c26ca87c642ae7e3b9bd94ad18f7b26363b4a80962
  support: context_only
  summary: Ignored-inclusive identifier/slug/alias search across native records, reviews,
    reports, history and source queue. Seven distinct disc entities retained; median
    body and generic microtubule remain separate.
- evidence_id: issue-search
  kind: validation
  reference: /private/tmp/csm-review-20261011T165130Z/disc-issues.log
  accessed_at: '2026-10-11T17:03:02Z'
  snapshot_sha256: b31a2cedd2a4a03f21d1f72974dcc2f635d5f617e5dcdbb72099f9a4c5fdd899
  support: context_only
  summary: 'All-state ventral-disc issue search inspected, including closed #484,
    #988 and #1001; none resolves these exact whole-disc or source-conflict findings.'
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/csm-review-20261011T165130Z/adapter.log
  accessed_at: '2026-10-11T17:03:02Z'
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
  support: context_only
  summary: Live iModulonDB inventory has no matching Giardia dataset. Not negative
    biological evidence.
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005874,GO:0097591,GO:0097592,GO:0097593,GO:0097594,GO:0097595,GO:0097596,GO:0097597
  locator: Exact eight nonobsolete CC terms; definitions, typed part_of children and
    synonym scopes
  accessed_at: '2026-10-11T16:52:59Z'
  snapshot_sha256: 6da3fda3b00797df51456e6e3e38108b747a107298a2c792533bea60f8650638
  support: supports
  summary: Exact identities and parthood retained; GO itself contains the contractile-protein
    and supernumerary-orientation claims under review.
- evidence_id: taxon
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5741
  locator: TaxId, rank, scientificName and otherNames
  accessed_at: '2026-10-11T16:53:00Z'
  snapshot_sha256: 1dcdc380972a71a0a24c80755d8bbacdcb0b6d9988bb5fb1e05ba43f50580dd3
  support: supports
  summary: TaxId 5741 is the species Giardia duodenalis, with Giardia intestinalis
    and Giardia lamblia listed as synonyms. Existing accepted synonym label is not
    a new species or strain.
- evidence_id: schwartz
  kind: primary_source
  reference: DOI:10.1371/journal.pone.0043783
  locator: 'Results: whole-cell architecture; Figure 1F and Figures 2-7 captions;
    Table 1; Discussion; methods'
  accessed_at: '2026-10-11T16:53:03Z'
  snapshot_sha256: cb10066d132c51723c8472aed40495970b76bc0634052590bd3ee7f35972038c
  support: supports
  summary: Primary tomography supports distinct main array, supernumerary array, microribbons,
    crossbridges, overlap and crest. Supernumerary reconstruction is a short right-handed
    fragment ventral to the main array, not a universal dorsal-left-handed rule.
- evidence_id: figure-1
  kind: record_content
  reference: /private/tmp/csm-review-20261011T165130Z/schwartz-fig1.jpg
  accessed_at: '2026-10-11T17:03:02Z'
  snapshot_sha256: 5466f1c6ef79affdc54ec3f2f7948714c32282e1221cc4d4e1775a618919a92e
  support: context_only
  summary: Actual Figure 1 inspected with caption, including yellow supernumerary
    array and white main array in panel F; not raw tomogram reanalysis.
- evidence_id: hagen2011
  kind: primary_source
  reference: DOI:10.1371/journal.pntd.0001442
  locator: Results Figures 4-6 and Table 1; Discussion of actin/crest and supernumerary
    array; methods
  accessed_at: '2026-10-11T16:52:07Z'
  snapshot_sha256: 4764e6ef8d323277737b63dbb374bbdb8011ff87153ed54603d74bd616b5e608
  support: supports
  summary: Proteomics, immunogold localization and FRAP support stable structural
    cohorts. Figure 5 reports supernumerary localization slightly dorsal or ventral;
    its left-handed description conflicts with Schwartz 2012. Discussion rejects the
    earlier classical actin/myosin account as established disc machinery.
assessments:
- assessment_id: identity
  area: grounding
  topic: Structure identity, partonomy and cohort boundaries
  outcome: supported
  target_ids:
  - GO:0097596
  evidence_ids:
  - record
  - go
  - identity-search
  summary: Exact GO identity and six distinct disc substructures retained; organelle
    versus array versus topological region is not flattened. Tubulin remains a molecular
    constituent, not a structure identity.
- assessment_id: scope
  area: evidence
  topic: Taxon, components and retained biological claims
  outcome: supported
  target_ids:
  - GO:0097596
  evidence_ids:
  - record
  - taxon
  - schwartz
  - hagen2011
  summary: Giardia trophozoite context and WBC6 experimental scope support existing
    species examples. Broad tubulin/structural cohorts retain UNKNOWN essentiality
    and unresolved accessions. No new stoichiometry or force mechanism is inferred.
- assessment_id: remaining-graph
  area: evidence
  topic: Retained composition and disc parthood
  outcome: supported
  target_ids:
  - GO:0097596
  evidence_ids:
  - record
  - go
  - schwartz
  summary: Tubulin constituency, microtubule has_part and ventral-disc part_of are
    supported. Prior removal of generic assembly and invented topology function is
    retained.
- assessment_id: finding-1
  area: evidence
  topic: Qualify supernumerary-array orientation by its primary reconstruction
  outcome: concern
  target_ids:
  - GO:0097596
  evidence_ids:
  - record
  - go
  - schwartz
  - figure-1
  - hagen2011
  - issue-search
  - rules
  summary: 'The definition and first graph edge universally repeat the GO description
    of a left-handed array generally dorsal to the main array. The cited Schwartz
    2012 Results describe a short right-handed fragment, and Figure 1F explicitly
    places the reconstructed supernumerary microtubules ventral to the main array.
    Hagen 2011 instead describes a left-handed partial array and observes slightly
    dorsal or ventral localization in Figure 5. Preserve this source disagreement;
    do not replace one universal orientation with another. Prior #1001 removed unsupported
    assembly/function claims but did not resolve this primary-source conflict.'
- assessment_id: optional
  area: completeness
  topic: Optional fields and provenance
  outcome: supported
  target_ids:
  - GO:0097596
  evidence_ids:
  - record
  - history
  - rules
  summary: No image, physical-property slot, exact protein accession, complex composition,
    dataset, trait or pathway assertion is present. Optional absence and existing
    component-grounding TODOs are not defects.
findings:
- finding_id: F1
  issue_key: ventral-disc-supernumerary-topology-source-conflict
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Qualify supernumerary-array orientation by its primary reconstruction
  description: 'The definition and first graph edge universally repeat the GO description
    of a left-handed array generally dorsal to the main array. The cited Schwartz
    2012 Results describe a short right-handed fragment, and Figure 1F explicitly
    places the reconstructed supernumerary microtubules ventral to the main array.
    Hagen 2011 instead describes a left-handed partial array and observes slightly
    dorsal or ventral localization in Figure 5. Preserve this source disagreement;
    do not replace one universal orientation with another. Prior #1001 removed unsupported
    assembly/function claims but did not resolve this primary-source conflict.'
  target_ids:
  - GO:0097596
  field_paths:
  - definition
  - definition_source
  - causal_graphs[0]
  - evidence
  - discussions
  evidence_ids:
  - record
  - go
  - schwartz
  - figure-1
  - hagen2011
  - issue-search
  - rules
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ventral_disc_supernumerary_microtubule_array.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: major
  normalization_reason: Substantive molecular/topological source-scope defect.
actions:
- action_id: A1
  description: Qualify supernumerary-array orientation by its primary reconstruction
  finding_ids:
  - F1
  target_ids:
  - GO:0097596
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ventral_disc_supernumerary_microtubule_array.yaml
    role: maintained scientific record
  acceptance_checks:
  - Use a neutral structural identity and explicitly Schwartz-2012-bounded right-handed/ventral
    reconstruction in definition and topology graph; retain the GO/Hagen conflict
    and do not restore a function or assembly mechanism.
  - Preserve PROPOSED status, prior discussions/history and unknown groundings; guarded
    writer, actual Codex EDIT, focused regressions, generated artifacts and full QC
    must pass.
limitations:
- Same-agent scientific review, not independent human sign-off or raw-data reanalysis.
- Actual full article text and captions were inspected. Nosala XML returned HTTP 500;
  official PMC HTML was readable. Schwartz XML is valid JATS beginning with DOCTYPE;
  its full PMC HTML was used by the reader. Normal web-tool PMC URLs returned interstitials
  and were not used as evidence.
- Full QC is exact-baseline CI; local schema/strict/snippet/global/contract checks
  ran separately. Existing namespace and three empty-parameter test skips remain explicit.
- Five other ventral-disc records have clean operational coverage and no review bundles;
  this bundle does not itself certify those targets. Unknown force generation and
  component identities remain open.
```
