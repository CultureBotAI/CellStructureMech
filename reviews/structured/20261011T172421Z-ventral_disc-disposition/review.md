# ventral disc: saved finding dispositions

- Review: 20261011T172421Z-ventral_disc-disposition
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T17:24:15Z
- Finished UTC: 2026-10-11T17:24:21Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Exact saved findings resolved with evidence-backed local corrections; original observations and PROPOSED status retained.

## Scope And Provenance

Exact saved findings and surrounding-claim preservation, not a second whole-record review.

Selection: 20261011T170255Z-ventral_disc-audit
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ab0cc2c8e040815f4b3686169598bc9123a1bcc7.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0097597 | data/structures/cytoskeleton/ventral_disc.yaml | maintained | ventral disc |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| ventral_disc-schema | passed | True | GO:0097597 | Actual deterministic check passed; scientific support assessed separately. |
| ventral_disc-strict | passed | True | GO:0097597 | Actual deterministic check passed; scientific support assessed separately. |
| ventral_disc-snippets | passed | True | GO:0097597 | No verbatim snippets; paraphrases assessed separately against inspected text. |
| history | passed | True | GO:0097597 | Actual deterministic check passed; scientific support assessed separately. |
| labels | passed | True | GO:0097597 | id↔label correspondence summary:<br>          OK_CANONICAL: 3544<br>            OK_SYNONYM: 50<br>          OK_EXCEPTION: 6<br>    SKIPPED_NO_ADAPTER: 603<br><br>✅ All id↔label pairs correspond. |
| traits | passed | True | GO:0097597 | Actual deterministic check passed; scientific support assessed separately. |
| curies | passed | True | GO:0097597 | [not exercised] ComplexPortal: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>resolver control: 1 resolver(s) could not be exercised because their authority was unreachable; the rest accept a known id and reject a fabricated one<br><br>identifier liveness summary:<br>  OK             4014<br>  SKIPPED         251<br><br>Every identifier resolves at its issuing authority. |
| focused | passed | True | GO:0097597 | ...............................                                          [100%]<br>31 passed in 66.99s (0:01:06) |
| reviews | passed | True | GO:0097597 | Actual deterministic check passed; scientific support assessed separately. |
| diff | passed | True | GO:0097597 | Actual deterministic check passed; scientific support assessed separately. |
| release-qc | passed | True | GO:0097597 | Full local QC passed: 883 passed, 3 skipped in 878.18s (0:14:38). PR and native merge-group gates remain separate. |

## Scientific And Domain Assessments

### Remove the unsupported classical contractile-protein mechanism

evidence: supported. Targets: GO:0097597.

The definition now describes microtubule architecture and attachment, cites primary structural evidence and appends the inherited classical-contractile-protein source conflict without excluding all possible actin regulation or contraction.

### Match the two related synonyms to their GO scope

evidence: supported. Targets: GO:0097597.

The two GO-related synonyms now have RELATED_SYNONYM scope; exact synonym and source strings are retained.

### Use a source-neutral alpha/beta tubulin label

evidence: supported. Targets: GO:0097597.

The component and matching node use alpha- and beta-tubulins; stable IDs, role, evidence, essentiality and unresolved grounding are unchanged.

## Findings

### F1: Remove the unsupported classical contractile-protein mechanism

major / resolved / confirmed; issue key: ventral-disc-classical-contractile-protein-claim.

The definition now describes microtubule architecture and attachment, cites primary structural evidence and appends the inherited classical-contractile-protein source conflict without excluding all possible actin regulation or contraction.

Disposition: The definition now describes microtubule architecture and attachment, cites primary structural evidence and appends the inherited classical-contractile-protein source conflict without excluding all possible actin regulation or contraction. Verified against primary text, scoped diff, red/green regressions and full local QC.

### F2: Match the two related synonyms to their GO scope

minor / resolved / confirmed; issue key: ventral-disc-go-synonym-scopes.

The two GO-related synonyms now have RELATED_SYNONYM scope; exact synonym and source strings are retained.

Disposition: The two GO-related synonyms now have RELATED_SYNONYM scope; exact synonym and source strings are retained. Verified against primary text, scoped diff, red/green regressions and full local QC.

### F3: Use a source-neutral alpha/beta tubulin label

minor / resolved / confirmed; issue key: ventral-disc-source-neutral-tubulin-label.

The component and matching node use alpha- and beta-tubulins; stable IDs, role, evidence, essentiality and unresolved grounding are unchanged.

Disposition: The component and matching node use alpha- and beta-tubulins; stable IDs, role, evidence, essentiality and unresolved grounding are unchanged. Verified against primary text, scoped diff, red/green regressions and full local QC.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/ventral_disc.yaml | context_only | Corrected whole YAML reread and compared with source and original observation. |
| rules | docs/CURATION.md | context_only | Source-neutral molecular labels and evidence bounded to the narrowest supported claim. |
| history | /private/tmp/csm-review-20261011T165130Z/ventral_disc-discussion-history.json | context_only | All committed discussion and inline-event versions inspected; earlier dates and rationale retained. |
| history-0 | history/records/ventral_disc/2026-09-11T130228Z-codex-6d430a.yaml | context_only | Original CREATE and correction events inspected; not a new canonical review. |
| history-1 | history/records/ventral_disc/2026-09-11T131330Z-codex-bc5f80.yaml | context_only | Original CREATE and correction events inspected; not a new canonical review. |
| predecessors | /private/tmp/csm-review-20261011T165130Z/exact-target-predecessors.json | context_only | Ignored-inclusive scan found no exact-target canonical predecessor. |
| identity-search | /private/tmp/csm-review-20261011T165130Z/identity-scan.log | context_only | Ignored-inclusive identifier/slug/alias search across native records, reviews, reports, history and source queue. Seven distinct disc entities retained; median body and generic microtubule remain separate. |
| issue-search | /private/tmp/csm-review-20261011T165130Z/disc-issues.log | context_only | All-state ventral-disc issue search inspected, including closed #484, #988 and #1001; none resolves these exact whole-disc or source-conflict findings. |
| adapter | /private/tmp/csm-review-20261011T165130Z/adapter.log | context_only | Live iModulonDB inventory has no matching Giardia dataset. Not negative biological evidence. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005874,GO:0097591,GO:0097592,GO:0097593,GO:0097594,GO:0097595,GO:0097596,GO:0097597; Exact eight nonobsolete CC terms; definitions, typed part_of children and synonym scopes | supports | Exact identities and parthood retained; GO itself contains the contractile-protein and supernumerary-orientation claims under review. |
| taxon | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5741; TaxId, rank, scientificName and otherNames | supports | TaxId 5741 is the species Giardia duodenalis, with Giardia intestinalis and Giardia lamblia listed as synonyms. Existing accepted synonym label is not a new species or strain. |
| schwartz | DOI:10.1371/journal.pone.0043783; Results: whole-cell architecture; Figure 1F and Figures 2-7 captions; Table 1; Discussion; methods | supports | Primary tomography supports distinct main array, supernumerary array, microribbons, crossbridges, overlap and crest. Supernumerary reconstruction is a short right-handed fragment ventral to the main array, not a universal dorsal-left-handed rule. |
| figure-1 | /private/tmp/csm-review-20261011T165130Z/schwartz-fig1.jpg | context_only | Actual Figure 1 inspected with caption, including yellow supernumerary array and white main array in panel F; not raw tomogram reanalysis. |
| hagen2011 | DOI:10.1371/journal.pntd.0001442; Results Figures 4-6 and Table 1; Discussion of actin/crest and supernumerary array; methods | supports | Proteomics, immunogold localization and FRAP support stable structural cohorts. Figure 5 reports supernumerary localization slightly dorsal or ventral; its left-handed description conflicts with Schwartz 2012. Discussion rejects the earlier classical actin/myosin account as established disc machinery. |
| nosala | DOI:10.1242/jcs.227355; Abstract, Results Figures 1-6, Discussion and methods | supports | Disc-associated proteins occupy distinct regions; two studied depletion phenotypes affect stability. Does not establish that every DAP is essential or specify all force-generating proteins. |
| hagen2025 | DOI:10.1091/mbc.E23-12-0515; Results on MBP mutants/attachment, Discussion and methods | supports | Domed architecture contributes to attachment. Discussion distinguishes the early actin-based crest hypothesis from later localization and leaves the attachment force mechanism unresolved. |
| predecessor | reviews/structured/20261011T170255Z-ventral_disc-audit/review.yaml | context_only | Immutable observation committed before native edits. |
| preservation | /private/tmp/csm-review-20261011T165130Z/preservation.json | context_only | All 907 other native records and semantic vectors, prior histories, reviews and legacy reports preserved. |
| red | /private/tmp/csm-review-20261011T165130Z/regressions-red.log | context_only | Focused regressions demonstrated original defects before curation. |
| green | /private/tmp/csm-review-20261011T165130Z/post-focused.log | context_only | All focused regression and guarded-writer tests passed. |
| edit-history | history/records/ventral_disc/2026-10-11T170338Z-codex-2ec89f.yaml | context_only | Actual append-only Codex EDIT links all issues and original observation. |

## Limits And Additional Notes

- Same-agent scoped disposition, not independent human approval.
- Original inspected snapshots and Figure 1 remain the evidence basis; no claim of a new download or raw tomogram reanalysis.
- The conflicting upstream descriptions remain unresolved scientifically; the local wording is explicitly study-bounded. Unknown force generation and component groundings remain open.
- Existing namespace/test skips remain explicit. PR and separate native merge-group gates are publication requirements. Corrected source retained by review-base/ventral-disc-evidence-20261011.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T172421Z-ventral_disc-disposition
kind: record
repository: CultureBotAI/CellStructureMech
title: 'ventral disc: saved finding dispositions'
started_at: '2026-10-11T17:24:15Z'
finished_at: '2026-10-11T17:24:21Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent scientific review, not independent human approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Exact saved findings resolved with evidence-backed local corrections; original
  observations and PROPOSED status retained.
source:
  git_revision: ab0cc2c8e040815f4b3686169598bc9123a1bcc7
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
  - path: data/structures/cytoskeleton/ventral_disc.yaml
    sha256: da4539d720be1cfa7e1e1b5ca12d86f57ededaebc6a869bdd2fc4bf13fb5680b
    role: target
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
    sha256: 54772643689f75f239cddf783180ab3eb0443695ea60080d966cbeb2fb0efe1f
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
  - path: history/records/ventral_disc/2026-09-11T130228Z-codex-6d430a.yaml
    sha256: 5265909c28ddc5bd0ed0230c2b9e91e68db880d30501c4c897cb12792619f4aa
    role: context
  - path: history/records/ventral_disc/2026-09-11T131330Z-codex-bc5f80.yaml
    sha256: fd72d315e9f36658e6ca144b7bcbc8914bcecd68b4037a5b655aa0291de670f4
    role: context
  - path: history/records/ventral_disc/2026-10-11T170338Z-codex-2ec89f.yaml
    sha256: f25c4a1f160b2b23712386383f60baf6193f829ea574e510647a953c67d0c03c
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reviews/structured/20261011T170255Z-ventral_disc-audit/review.yaml
    sha256: d0595ff566c9b56645975de05f5228f2a3f05728bc6369e6d7e6d81660dcad95
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: tests/test_ventral_disc_evidence_scope.py
    sha256: 887bd96efd0a4492c9b82081c8f67d27df11810e25a6305b5bf83f748b6c13b5
    role: context
targets:
- target_id: GO:0097597
  path: data/structures/cytoskeleton/ventral_disc.yaml
  label: ventral disc
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ventral_disc.yaml
    role: maintained scientific record
scope:
  description: Exact saved findings and surrounding-claim preservation, not a second
    whole-record review.
  selection: 20261011T170255Z-ventral_disc-audit
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - GO:0097597
checks:
- check_id: ventral_disc-schema
  name: ventral_disc-schema
  status: passed
  required: true
  target_ids:
  - GO:0097597
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/ventral_disc.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T17:03:54Z to 2026-10-11T17:03:57Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: ventral_disc-strict
  name: ventral_disc-strict
  status: passed
  required: true
  target_ids:
  - GO:0097597
  command: .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/ventral_disc.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T17:03:57Z to 2026-10-11T17:04:01Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: ventral_disc-snippets
  name: ventral_disc-snippets
  status: passed
  required: true
  target_ids:
  - GO:0097597
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/cytoskeleton/ventral_disc.yaml
    --report /private/tmp/csm-review-20261011T165130Z/post-ventral_disc-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: No verbatim snippets; paraphrases assessed separately against inspected
    text.
  scope_note: 2026-10-11T17:04:01Z to 2026-10-11T17:04:32Z; log SHA-256 d5410cb4043ed5e182322a5b6ed767a778104ffad00e966c87fd22a49a4c4f22
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:0097597
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T17:05:07Z to 2026-10-11T17:05:24Z; log SHA-256 a454941f6e4cdaf7e2a2bef570001bfff59209562b91d4bfa67737b7f11fbf47
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - GO:0097597
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: "id↔label correspondence summary:\n          OK_CANONICAL: 3544\n     \
    \       OK_SYNONYM: 50\n          OK_EXCEPTION: 6\n    SKIPPED_NO_ADAPTER: 603\n\
    \n✅ All id↔label pairs correspond."
  scope_note: 2026-10-11T17:05:24Z to 2026-10-11T17:07:15Z; log SHA-256 d423103555a6a5b538a7c811a73a29c24ed0e5a2eae00d1bb94715295f23f7cb
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - GO:0097597
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T17:07:15Z to 2026-10-11T17:08:08Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - GO:0097597
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: "[not exercised] ComplexPortal: the issuing authority was unreachable after\
    \ 1 attempts, so this resolver was not exercised\nresolver control: 1 resolver(s)\
    \ could not be exercised because their authority was unreachable; the rest accept\
    \ a known id and reject a fabricated one\n\nidentifier liveness summary:\n  OK\
    \             4014\n  SKIPPED         251\n\nEvery identifier resolves at its\
    \ issuing authority."
  scope_note: 2026-10-11T17:08:08Z to 2026-10-11T17:09:29Z; log SHA-256 be1b6f89c9cf85143fb3db11eb38ed3603082d9a70cbc12b029414c8b16386e5
- check_id: focused
  name: focused
  status: passed
  required: true
  target_ids:
  - GO:0097597
  command: .venv/bin/python -m pytest -q tests/test_ventral_disc_evidence_scope.py
    tests/test_write_validated.py
  exit_code: 0
  expected_exit_code: 0
  summary: '...............................                                          [100%]

    31 passed in 66.99s (0:01:06)'
  scope_note: 2026-10-11T17:09:29Z to 2026-10-11T17:10:38Z; log SHA-256 35ebb91a642be30c9ff0240cf6037258a566211ca8c3ccae6d3a1a289ca4aafe
- check_id: reviews
  name: reviews
  status: passed
  required: true
  target_ids:
  - GO:0097597
  command: .venv/bin/python scripts/record_review.py check --base 2810e5b8a40317e07e5d92ced38455597e328633
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T17:10:38Z to 2026-10-11T17:12:21Z; log SHA-256 1bee193ec6976c5afcbc0c86a5d388db3543dc5b213f9ba9cfe1c3e900988bb3
- check_id: diff
  name: diff
  status: passed
  required: true
  target_ids:
  - GO:0097597
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T17:12:21Z to 2026-10-11T17:12:22Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- check_id: release-qc
  name: release-qc
  status: passed
  required: true
  target_ids:
  - GO:0097597
  command: .venv/bin/python scripts/run_qc.py
  exit_code: 0
  expected_exit_code: 0
  summary: 'Full local QC passed: 883 passed, 3 skipped in 878.18s (0:14:38). PR and
    native merge-group gates remain separate.'
  scope_note: 2026-10-11T17:05:34Z to 2026-10-11T17:23:30Z; log SHA-256 1c4c2c600fcee9f81749c1662104163b42b3a26c56b6260d992a0da30776e586
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/ventral_disc.yaml
  accessed_at: '2026-10-11T17:24:21Z'
  snapshot_sha256: da4539d720be1cfa7e1e1b5ca12d86f57ededaebc6a869bdd2fc4bf13fb5680b
  support: context_only
  summary: Corrected whole YAML reread and compared with source and original observation.
- evidence_id: rules
  kind: record_content
  reference: docs/CURATION.md
  accessed_at: '2026-10-11T17:02:55Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  support: context_only
  summary: Source-neutral molecular labels and evidence bounded to the narrowest supported
    claim.
- evidence_id: history
  kind: record_content
  reference: /private/tmp/csm-review-20261011T165130Z/ventral_disc-discussion-history.json
  accessed_at: '2026-10-11T17:02:55Z'
  snapshot_sha256: 2c873bd1ac09379437adf93a56356fe22e91554f2bbb602bca40823cf510ce10
  support: context_only
  summary: All committed discussion and inline-event versions inspected; earlier dates
    and rationale retained.
- evidence_id: history-0
  kind: record_content
  reference: history/records/ventral_disc/2026-09-11T130228Z-codex-6d430a.yaml
  accessed_at: '2026-10-11T17:02:55Z'
  snapshot_sha256: 5265909c28ddc5bd0ed0230c2b9e91e68db880d30501c4c897cb12792619f4aa
  support: context_only
  summary: Original CREATE and correction events inspected; not a new canonical review.
- evidence_id: history-1
  kind: record_content
  reference: history/records/ventral_disc/2026-09-11T131330Z-codex-bc5f80.yaml
  accessed_at: '2026-10-11T17:02:55Z'
  snapshot_sha256: fd72d315e9f36658e6ca144b7bcbc8914bcecd68b4037a5b655aa0291de670f4
  support: context_only
  summary: Original CREATE and correction events inspected; not a new canonical review.
- evidence_id: predecessors
  kind: validation
  reference: /private/tmp/csm-review-20261011T165130Z/exact-target-predecessors.json
  accessed_at: '2026-10-11T17:02:55Z'
  snapshot_sha256: 238a70e93754193431f6bbef9d45643fd74e1a06da1b62ac34db4c568354ce15
  support: context_only
  summary: Ignored-inclusive scan found no exact-target canonical predecessor.
- evidence_id: identity-search
  kind: validation
  reference: /private/tmp/csm-review-20261011T165130Z/identity-scan.log
  accessed_at: '2026-10-11T17:02:55Z'
  snapshot_sha256: 27e8508adb572f4f64f375c26ca87c642ae7e3b9bd94ad18f7b26363b4a80962
  support: context_only
  summary: Ignored-inclusive identifier/slug/alias search across native records, reviews,
    reports, history and source queue. Seven distinct disc entities retained; median
    body and generic microtubule remain separate.
- evidence_id: issue-search
  kind: validation
  reference: /private/tmp/csm-review-20261011T165130Z/disc-issues.log
  accessed_at: '2026-10-11T17:02:55Z'
  snapshot_sha256: b31a2cedd2a4a03f21d1f72974dcc2f635d5f617e5dcdbb72099f9a4c5fdd899
  support: context_only
  summary: 'All-state ventral-disc issue search inspected, including closed #484,
    #988 and #1001; none resolves these exact whole-disc or source-conflict findings.'
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/csm-review-20261011T165130Z/adapter.log
  accessed_at: '2026-10-11T17:02:55Z'
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
  accessed_at: '2026-10-11T17:02:55Z'
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
- evidence_id: nosala
  kind: primary_source
  reference: DOI:10.1242/jcs.227355
  locator: Abstract, Results Figures 1-6, Discussion and methods
  accessed_at: '2026-10-11T16:53:03Z'
  snapshot_sha256: 6e4f147b0905dd7f5a83575c0b249f6d6254ade3f43dc283e8ad6544d9ad622b
  support: supports
  summary: Disc-associated proteins occupy distinct regions; two studied depletion
    phenotypes affect stability. Does not establish that every DAP is essential or
    specify all force-generating proteins.
- evidence_id: hagen2025
  kind: primary_source
  reference: DOI:10.1091/mbc.E23-12-0515
  locator: Results on MBP mutants/attachment, Discussion and methods
  accessed_at: '2026-10-11T16:52:03Z'
  snapshot_sha256: 4f3eee7f0d22c08dcb7204436f84d95795f9a8db30fccbb492e4ec67df6f145e
  support: supports
  summary: Domed architecture contributes to attachment. Discussion distinguishes
    the early actin-based crest hypothesis from later localization and leaves the
    attachment force mechanism unresolved.
- evidence_id: predecessor
  kind: prior_review
  reference: reviews/structured/20261011T170255Z-ventral_disc-audit/review.yaml
  accessed_at: '2026-10-11T17:24:21Z'
  snapshot_sha256: d0595ff566c9b56645975de05f5228f2a3f05728bc6369e6d7e6d81660dcad95
  support: context_only
  summary: Immutable observation committed before native edits.
- evidence_id: preservation
  kind: validation
  reference: /private/tmp/csm-review-20261011T165130Z/preservation.json
  accessed_at: '2026-10-11T17:24:21Z'
  snapshot_sha256: 31a2707880e39e6d26ffb3b62cb9bac32644b5432ffeee11faf77e4f2a9d5c4a
  support: context_only
  summary: All 907 other native records and semantic vectors, prior histories, reviews
    and legacy reports preserved.
- evidence_id: red
  kind: validation
  reference: /private/tmp/csm-review-20261011T165130Z/regressions-red.log
  accessed_at: '2026-10-11T17:24:21Z'
  snapshot_sha256: dbd45ba5f09a9e9dc1e4bd315868084c4e9ef9003ec01004f9959bdee6844b00
  support: context_only
  summary: Focused regressions demonstrated original defects before curation.
- evidence_id: green
  kind: validation
  reference: /private/tmp/csm-review-20261011T165130Z/post-focused.log
  accessed_at: '2026-10-11T17:24:21Z'
  snapshot_sha256: 35ebb91a642be30c9ff0240cf6037258a566211ca8c3ccae6d3a1a289ca4aafe
  support: context_only
  summary: All focused regression and guarded-writer tests passed.
- evidence_id: edit-history
  kind: record_content
  reference: history/records/ventral_disc/2026-10-11T170338Z-codex-2ec89f.yaml
  accessed_at: '2026-10-11T17:24:21Z'
  snapshot_sha256: f25c4a1f160b2b23712386383f60baf6193f829ea574e510647a953c67d0c03c
  support: context_only
  summary: Actual append-only Codex EDIT links all issues and original observation.
assessments:
- assessment_id: resolved-F1
  area: evidence
  topic: Remove the unsupported classical contractile-protein mechanism
  outcome: supported
  target_ids:
  - GO:0097597
  evidence_ids:
  - record
  - go
  - hagen2011
  - hagen2025
  - rules
  - predecessor
  - preservation
  - red
  - green
  - edit-history
  summary: The definition now describes microtubule architecture and attachment, cites
    primary structural evidence and appends the inherited classical-contractile-protein
    source conflict without excluding all possible actin regulation or contraction.
- assessment_id: resolved-F2
  area: evidence
  topic: Match the two related synonyms to their GO scope
  outcome: supported
  target_ids:
  - GO:0097597
  evidence_ids:
  - record
  - go
  - predecessor
  - preservation
  - red
  - green
  - edit-history
  summary: The two GO-related synonyms now have RELATED_SYNONYM scope; exact synonym
    and source strings are retained.
- assessment_id: resolved-F3
  area: evidence
  topic: Use a source-neutral alpha/beta tubulin label
  outcome: supported
  target_ids:
  - GO:0097597
  evidence_ids:
  - record
  - rules
  - schwartz
  - issue-search
  - predecessor
  - preservation
  - red
  - green
  - edit-history
  summary: The component and matching node use alpha- and beta-tubulins; stable IDs,
    role, evidence, essentiality and unresolved grounding are unchanged.
findings:
- finding_id: F1
  issue_key: ventral-disc-classical-contractile-protein-claim
  category: evidence
  severity: major
  status: resolved
  certainty: confirmed
  title: Remove the unsupported classical contractile-protein mechanism
  description: The definition now describes microtubule architecture and attachment,
    cites primary structural evidence and appends the inherited classical-contractile-protein
    source conflict without excluding all possible actin regulation or contraction.
  target_ids:
  - GO:0097597
  field_paths:
  - definition
  - definition_source
  - evidence
  - discussions
  evidence_ids:
  - record
  - go
  - hagen2011
  - hagen2025
  - rules
  - predecessor
  - preservation
  - red
  - green
  - edit-history
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ventral_disc.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: major
  normalization_reason: Substantive molecular/topological source-scope defect.
  disposition_reason: The definition now describes microtubule architecture and attachment,
    cites primary structural evidence and appends the inherited classical-contractile-protein
    source conflict without excluding all possible actin regulation or contraction.
    Verified against primary text, scoped diff, red/green regressions and full local
    QC.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261011T170255Z-ventral_disc-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2226
- finding_id: F2
  issue_key: ventral-disc-go-synonym-scopes
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: Match the two related synonyms to their GO scope
  description: The two GO-related synonyms now have RELATED_SYNONYM scope; exact synonym
    and source strings are retained.
  target_ids:
  - GO:0097597
  field_paths:
  - synonyms
  evidence_ids:
  - record
  - go
  - predecessor
  - preservation
  - red
  - green
  - edit-history
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ventral_disc.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: minor
  normalization_reason: Bounded synonym-scope or source-neutral naming inconsistency;
    exact record identity remains correct.
  disposition_reason: The two GO-related synonyms now have RELATED_SYNONYM scope;
    exact synonym and source strings are retained. Verified against primary text,
    scoped diff, red/green regressions and full local QC.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261011T170255Z-ventral_disc-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2227
- finding_id: F3
  issue_key: ventral-disc-source-neutral-tubulin-label
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: Use a source-neutral alpha/beta tubulin label
  description: The component and matching node use alpha- and beta-tubulins; stable
    IDs, role, evidence, essentiality and unresolved grounding are unchanged.
  target_ids:
  - GO:0097597
  field_paths:
  - components[component_id=ventral_disc_tubulins].label
  - causal_graphs[0].nodes[node_id=ventral_disc_tubulins].label
  evidence_ids:
  - record
  - rules
  - schwartz
  - issue-search
  - predecessor
  - preservation
  - red
  - green
  - edit-history
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ventral_disc.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: minor
  normalization_reason: Bounded synonym-scope or source-neutral naming inconsistency;
    exact record identity remains correct.
  disposition_reason: The component and matching node use alpha- and beta-tubulins;
    stable IDs, role, evidence, essentiality and unresolved grounding are unchanged.
    Verified against primary text, scoped diff, red/green regressions and full local
    QC.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261011T170255Z-ventral_disc-audit
    finding_id: F3
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2228
actions: []
limitations:
- Same-agent scoped disposition, not independent human approval.
- Original inspected snapshots and Figure 1 remain the evidence basis; no claim of
  a new download or raw tomogram reanalysis.
- The conflicting upstream descriptions remain unresolved scientifically; the local
  wording is explicitly study-bounded. Unknown force generation and component groundings
  remain open.
- Existing namespace/test skips remain explicit. PR and separate native merge-group
  gates are publication requirements. Corrected source retained by review-base/ventral-disc-evidence-20261011.
links:
- https://github.com/CultureBotAI/CellStructureMech/issues/2226
- https://github.com/CultureBotAI/CellStructureMech/issues/2227
- https://github.com/CultureBotAI/CellStructureMech/issues/2228
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261011T170255Z-ventral_disc-audit
  relationship: Resolves exact predecessor findings without replacing the observation.
```
