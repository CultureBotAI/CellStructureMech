# B axonemal microtubule: scientific record review

- Review: 20261011T094735Z-b_axonemal_microtubule-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T09:35:32Z
- Finished UTC: 2026-10-11T09:47:35Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Entire native record reviewed; one concrete finding saved against original bytes before separately authorized curation.

## Scope And Provenance

Whole native YAML: identity, typed hierarchy, components, species scope, functions, each graph edge if present, measurements, datasets, images, discussions and history.

Selection: One exact target in the 909-record review goal. Supporting neighboring records and source fetches do not certify other targets.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 51cbd8eb58e2082cbb54d629d3a9516c716a249c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0097650 | data/structures/cytoskeleton/b_axonemal_microtubule.yaml | maintained | B axonemal microtubule |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0097650 | Deterministic check passed; scientific assessment is separate. |
| strict | passed | True | GO:0097650 | Deterministic check passed; scientific assessment is separate. |
| snippets | passed | True | GO:0097650 | No verbatim snippets asserted; paraphrased claims were checked against inspected primary text. |
| history | passed | True | GO:0097650 | Deterministic check passed; scientific assessment is separate. |
| labels | passed | True | GO:0097650 | id↔label correspondence summary:<br>          OK_CANONICAL: 3544<br>            OK_SYNONYM: 50<br>          OK_EXCEPTION: 6<br>    SKIPPED_NO_ADAPTER: 603<br><br>✅ All id↔label pairs correspond. |
| traits | passed | True | GO:0097650 | Deterministic check passed; scientific assessment is separate. |
| curies | passed | True | GO:0097650 | resolver control: every resolver accepts a known id and rejects a fabricated one<br><br>identifier liveness summary:<br>  OK             4014<br>  SKIPPED         251<br><br>Every identifier resolves at its issuing authority. |
| reviews | passed | True | GO:0097650 | Deterministic check passed; scientific assessment is separate. |
| diff | passed | True | GO:0097650 | Deterministic check passed; scientific assessment is separate. |
| Exact-baseline CI full QC | passed | True | GO:0097650 | Full QC passed on the exact captured baseline: 843 tests passed, 3 skipped; native and shared review gates passed. Verified CI receipt, not a new local full-QC run. |

## Scientific And Domain Assessments

### Identity, ten-protofilament boundary, species, function and all four graph edges

evidence: supported. Targets: GO:0097650.

GO:0097650 exact identity, broad B-tubule synonym, axonemal-microtubule is-a and doublet parthood are supported. B-sheath has_part follows primary B-lumen evidence despite the known upstream typed-edge conflict. The NONMECHANISTIC graph correctly separates doublet membership, A fusion, B10 inner and B1 outer contacts. No molecular completeness, stoichiometry or universal taxonomic assertion is implied.

### Original versus narrowed rationale

provenance: concern. Targets: GO:0097650.

The rationale originally committed at 4bb42d3a describes the initial coarse B-tubule scope. Child creation at 871db9b2 replaced it with the narrowed inner-sheath wording. Narrowing the prompt was appropriate, but replacing the rationale loses provenance that CURATION.md requires to be appended, not overwritten.

### Optional slots and unresolved molecular work

completeness: supported. Targets: GO:0097650.

No image, dataset accession, protein-family assertion or quantitative measurement is present. Finer MIP identities and copy numbers remain acknowledged tasks, not invented issues.

## Findings

### F1: Restore the original B-tubule discussion rationale

minor / open / confirmed; issue key: b-tubule-discussion-rationale-preservation.

The rationale originally committed at 4bb42d3a describes the initial coarse B-tubule scope. Child creation at 871db9b2 replaced it with the narrowed inner-sheath wording. Narrowing the prompt was appropriate, but replacing the rationale loses provenance that CURATION.md requires to be appended, not overwritten.

## Recommended Actions And Acceptance Checks

### A1

Restore the original B-tubule discussion rationale

- Restore the exact original rationale and retain the later rationale with its revision context.
- Preserve current narrowed prompt, OPEN status, original author/date, live graph attachment, B-sheath child, all graph edges and biological fields.
- Use the guarded writer, append Codex curation and EDIT history, preserve PROPOSED, prior history/reviews and unrelated records, regenerate pages, and pass focused regressions and native QC.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/b_axonemal_microtubule.yaml | context_only | Entire native YAML read; formal capture preceded assessment. Initial reading preceded capture. |
| rules | docs/CURATION.md | context_only | parent_structures is is-a, part_of is containment; individual fibers are not cytoskeleton subclasses. Discussion rationale is append-only. |
| history | /private/tmp/csm-review-20261011T093443Z/b_axonemal_microtubule-discussion-history.json | context_only | Complete committed discussion and curation-event history inspected. |
| predecessors | /private/tmp/csm-review-20261011T093443Z/exact-target-predecessors.json | context_only | Ignored-inclusive canonical-review scan found no exact-target predecessor; legacy reports are historical context, not canonical lineage. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005575,GO:0005856,GO:0005879,GO:0032053,GO:0032991,GO:0036064,GO:0097545,GO:0097649,GO:0097650,GO:0110165,GO:0120280,GO:0140180,GO:0140535,GO:0160110,GO:0160112,GO:0160113,GO:0160114; Relevant GO definitions, aspect, obsolescence and typed reverse children | supports | B-tubule identity and axonemal parent/parthood are supported. GO:0005856 denotes the containing framework, not an is-a class for each basal-body subassembly. |
| taxa | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=285686%2C3055%2C5762%2C5888%2C5911%2C63628; Top-level NCBITaxon:3055 Chlamydomonas reinhardtii, rank species | supports | Resolves taxon identity, not biological prevalence. |
| adapter | /private/tmp/csm-review-20261011T093443Z/adapter.log | context_only | Live 28-dataset iModulonDB inventory has no Chlamydomonas dataset. Not applicable; lack of coverage is not negative biological evidence. |
| ma | DOI:10.1016/j.cell.2019.09.030; Primary introduction; Results MIP networks, tubule junctions and Figure 6; experimental model and specimen preparation | supports | Chlamydomonas doublets have 13-PF A and 10-PF B tubules; B01 joins A10/A11, B10 joins A01, and luminal MIP networks are distinct from the wall. |
| child | data/structures/cytoskeleton/axonemal_b_tubule_inner_sheath.yaml | context_only | Existing B-sheath child retains its OPEN molecular task and the already documented current GO A/B relationship discrepancy. B-lumen containment is primary-supported. |
| repository-history | history/records/b_axonemal_microtubule/2026-09-23T174334Z-claude-code-a53df0.yaml | context_only | Creation history read; original actor metadata retained. |

## Limits And Additional Notes

- Same-agent scientific review, not independent human sign-off; all native records remain PROPOSED.
- Exact-baseline full QC is verified in CI; fresh scoped/global checks record actual resolver and label skips. Deterministic checks are not scientific certification.
- No raw micrograph, reconstruction-map or experimental-data reanalysis. Unknown molecular composition and stoichiometry are not certified.
- Ma Europe PMC XML returned an error; official PMC HTML was inspected. Li 2012 ordinary browser page presented a challenge; public official PMC open-data JATS and original media were available and checksum verified.
- Only this exact target is certified by this observation. Eleven other records whose files and resources were gathered in the batch remain pending full scientific assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T094735Z-b_axonemal_microtubule-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'B axonemal microtubule: scientific record review'
started_at: '2026-10-11T09:35:32Z'
finished_at: '2026-10-11T09:47:35Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent record and source review, not independent human scientific
    approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Entire native record reviewed; one concrete finding saved against original
  bytes before separately authorized curation.
source:
  git_revision: 51cbd8eb58e2082cbb54d629d3a9516c716a249c
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
    sha256: 64862db2087298ae832b8a8410185349cc277151af31d88ce231e43201ab9440
    role: context
  - path: curation/source_queue.tsv
    sha256: 55d8fe79b5edd7d6b42bf4ca9168fe4878240417716e2f4ba423489144b89284
    role: context
  - path: data/structures/cytoskeleton/axonemal_b_tubule_inner_sheath.yaml
    sha256: d1b0e481219c8b248e22e069aaa333074857a9ef8cae74d159e9a9e1f33a733e
    role: context
  - path: data/structures/cytoskeleton/axonemal_doublet_microtubule.yaml
    sha256: deedf652ec4801ed3186c00789cb1c725e5c682f84c2934132489486535848b4
    role: context
  - path: data/structures/cytoskeleton/axonemal_microtubule.yaml
    sha256: 480cd29d1f2e87c07c19dd8d60e50768cdcce29223b28ce2df1d4c956dc46282
    role: context
  - path: data/structures/cytoskeleton/b_axonemal_microtubule.yaml
    sha256: 438f1274f334f407b89cb2f89c27796d3c909385e3535e57151f4d07fbe9c160
    role: target
  - path: data/structures/cytoskeleton/basal_body_a_b_inner_junction.yaml
    sha256: 818592b3a8a807ee94f6de26d50992ac0589c4bdcd261a0443df16dbc16edff9
    role: context
  - path: data/structures/cytoskeleton/basal_body_a_c_linker.yaml
    sha256: 0a7ea087c029443809ba73acf52e83c59170ffa490347c3f7ffed1f37f432b7b
    role: context
  - path: data/structures/cytoskeleton/basal_body_a_tusk.yaml
    sha256: f82923b0febf504980e0c7e006d03d72c9cfdd2b38e225b6ad82adaac4d754c1
    role: context
  - path: data/structures/cytoskeleton/basal_body_b_c_inner_junction.yaml
    sha256: 1fda2a9ff6bec4d4b314bdd8f5995a2a2e21a8f6d11286eed800057257e2028b
    role: context
  - path: data/structures/cytoskeleton/basal_body_c_tubule_hook.yaml
    sha256: fb30d8f9a7713b2be51b6afd830658a2950397a2b99978423d97768c06aa3899
    role: context
  - path: data/structures/cytoskeleton/basal_body_c_tubule_luminal_filament.yaml
    sha256: 3132008bf0f7f5a35282e83dfa93e81ceb92464182c85f59b2a15a10d5ecc540
    role: context
  - path: data/structures/cytoskeleton/basal_body_cartwheel.yaml
    sha256: ad4e6fcf7639e0fffc00b553b0ab2e0e2a8eac5981b87ae9da1ee783ba942957
    role: context
  - path: data/structures/cytoskeleton/basal_body_cartwheel_inner_density.yaml
    sha256: cc7469f2607b02f62b092c115aac1669dd80865e82be6462c10e3dec866dfc00
    role: context
  - path: data/structures/cytoskeleton/basal_body_d2_rod.yaml
    sha256: acd457cb1d0121248e5d11bdebc1d70a815a42f240f31e02eaa556bc54e7bc27
    role: context
  - path: data/structures/cytoskeleton/basal_body_filamentous_cartwheel_inner_density.yaml
    sha256: 5fc268e1a3493fde87ab6856fae60c61025633bdbc9c7d29c08c794c5678d8df
    role: context
  - path: data/structures/cytoskeleton/basal_body_inner_scaffold.yaml
    sha256: b320c60ebc92c55021e2a673b4a4d696ad3a2d8dc8fae6a704cb972814ce2443
    role: context
  - path: data/structures/cytoskeleton/basal_body_pinhead.yaml
    sha256: ef3da1eee8d7e92150c0bf3ab1c6e2c67a410aa366416ab03454e3929e25bff2
    role: context
  - path: data/structures/cytoskeleton/basal_body_triplet_base.yaml
    sha256: c88a6c10f311bce934e37d5583f122fee6cae6f45950117728cb6d1a7905e6f8
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
  - path: history/records/b_axonemal_microtubule/2026-09-23T174334Z-claude-code-a53df0.yaml
    sha256: 75f3976a9633c450e1bed88a1fc8255122ff36eab3fda790e751bf9f423c329c
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
- target_id: GO:0097650
  path: data/structures/cytoskeleton/b_axonemal_microtubule.yaml
  label: B axonemal microtubule
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/b_axonemal_microtubule.yaml
    role: maintained scientific record
scope:
  description: 'Whole native YAML: identity, typed hierarchy, components, species
    scope, functions, each graph edge if present, measurements, datasets, images,
    discussions and history.'
  selection: One exact target in the 909-record review goal. Supporting neighboring
    records and source fetches do not certify other targets.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0097650
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - GO:0097650
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/b_axonemal_microtubule.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Deterministic check passed; scientific assessment is separate.
  scope_note: 2026-10-11T09:36:41Z to 2026-10-11T09:36:45Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - GO:0097650
  command: .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/b_axonemal_microtubule.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Deterministic check passed; scientific assessment is separate.
  scope_note: 2026-10-11T09:36:45Z to 2026-10-11T09:36:49Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - GO:0097650
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/cytoskeleton/b_axonemal_microtubule.yaml
    --report /private/tmp/csm-review-20261011T093443Z/b_axonemal_microtubule-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: No verbatim snippets asserted; paraphrased claims were checked against
    inspected primary text.
  scope_note: 2026-10-11T09:36:49Z to 2026-10-11T09:37:15Z; log SHA-256 0f88b3b7496e573cc36b6d7584c06b922922d244b1ee497ab0f886874603c23d
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:0097650
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Deterministic check passed; scientific assessment is separate.
  scope_note: 2026-10-11T09:43:53Z to 2026-10-11T09:44:07Z; log SHA-256 5d9b82bc59e7d9cf911cc1e399824defed74f28d2bc221a5f8a99c7a0b68a7b2
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - GO:0097650
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: "id↔label correspondence summary:\n          OK_CANONICAL: 3544\n     \
    \       OK_SYNONYM: 50\n          OK_EXCEPTION: 6\n    SKIPPED_NO_ADAPTER: 603\n\
    \n✅ All id↔label pairs correspond."
  scope_note: 2026-10-11T09:44:07Z to 2026-10-11T09:45:37Z; log SHA-256 d423103555a6a5b538a7c811a73a29c24ed0e5a2eae00d1bb94715295f23f7cb
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - GO:0097650
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Deterministic check passed; scientific assessment is separate.
  scope_note: 2026-10-11T09:45:37Z to 2026-10-11T09:45:54Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - GO:0097650
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: "resolver control: every resolver accepts a known id and rejects a fabricated\
    \ one\n\nidentifier liveness summary:\n  OK             4014\n  SKIPPED      \
    \   251\n\nEvery identifier resolves at its issuing authority."
  scope_note: 2026-10-11T09:45:54Z to 2026-10-11T09:46:37Z; log SHA-256 ee1c5f2e78a2d29fcb6781a8ecd722934376595042d2cc261b4465b361d19b79
- check_id: reviews
  name: reviews
  status: passed
  required: true
  target_ids:
  - GO:0097650
  command: .venv/bin/python scripts/record_review.py check
  exit_code: 0
  expected_exit_code: 0
  summary: Deterministic check passed; scientific assessment is separate.
  scope_note: 2026-10-11T09:46:37Z to 2026-10-11T09:47:30Z; log SHA-256 6977b8c182fa916df88248f6c2984e5e154c1fef8362508dd2bc0f1bee21ec69
- check_id: diff
  name: diff
  status: passed
  required: true
  target_ids:
  - GO:0097650
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  summary: Deterministic check passed; scientific assessment is separate.
  scope_note: 2026-10-11T09:47:30Z to 2026-10-11T09:47:30Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- check_id: qc
  name: Exact-baseline CI full QC
  status: passed
  required: true
  target_ids:
  - GO:0097650
  command: gh run view 38128294516 --repo CultureBotAI/CellStructureMech --log
  exit_code: 0
  expected_exit_code: 0
  summary: 'Full QC passed on the exact captured baseline: 843 tests passed, 3 skipped;
    native and shared review gates passed. Verified CI receipt, not a new local full-QC
    run.'
  scope_note: https://github.com/CultureBotAI/CellStructureMech/actions/runs/38128294516;
    log SHA-256 9468c9b1bdd6e9a070a7454474bcd936a189ce2d717d4b20027c93419a46bb49
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/b_axonemal_microtubule.yaml
  accessed_at: '2026-10-11T09:47:35Z'
  snapshot_sha256: 438f1274f334f407b89cb2f89c27796d3c909385e3535e57151f4d07fbe9c160
  support: context_only
  summary: Entire native YAML read; formal capture preceded assessment. Initial reading
    preceded capture.
- evidence_id: rules
  kind: record_content
  reference: docs/CURATION.md
  accessed_at: '2026-10-11T09:47:35Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  support: context_only
  summary: parent_structures is is-a, part_of is containment; individual fibers are
    not cytoskeleton subclasses. Discussion rationale is append-only.
- evidence_id: history
  kind: record_content
  reference: /private/tmp/csm-review-20261011T093443Z/b_axonemal_microtubule-discussion-history.json
  accessed_at: '2026-10-11T09:47:35Z'
  snapshot_sha256: bd5bb8fd945ddc93098e4833a4049fae9cb2969b07397b4990ff74fec6302136
  support: context_only
  summary: Complete committed discussion and curation-event history inspected.
- evidence_id: predecessors
  kind: validation
  reference: /private/tmp/csm-review-20261011T093443Z/exact-target-predecessors.json
  accessed_at: '2026-10-11T09:47:35Z'
  snapshot_sha256: b8cb7a2be3d74d5e013507af93d561be33a033653302a0851f787235026ead84
  support: context_only
  summary: Ignored-inclusive canonical-review scan found no exact-target predecessor;
    legacy reports are historical context, not canonical lineage.
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005575,GO:0005856,GO:0005879,GO:0032053,GO:0032991,GO:0036064,GO:0097545,GO:0097649,GO:0097650,GO:0110165,GO:0120280,GO:0140180,GO:0140535,GO:0160110,GO:0160112,GO:0160113,GO:0160114
  locator: Relevant GO definitions, aspect, obsolescence and typed reverse children
  accessed_at: '2026-10-11T09:44:12Z'
  snapshot_sha256: 55218f64ea9ce115bdafbfb9b583c1799457662afcd378d4d01d29704fdc8d09
  support: supports
  summary: B-tubule identity and axonemal parent/parthood are supported. GO:0005856
    denotes the containing framework, not an is-a class for each basal-body subassembly.
- evidence_id: taxa
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=285686%2C3055%2C5762%2C5888%2C5911%2C63628
  locator: Top-level NCBITaxon:3055 Chlamydomonas reinhardtii, rank species
  accessed_at: '2026-10-11T09:36:27Z'
  snapshot_sha256: dc9bf03533798607ae6a53c723c8b6f9c70991fc4b14d36a48a152a3c938d348
  support: supports
  summary: Resolves taxon identity, not biological prevalence.
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/csm-review-20261011T093443Z/adapter.log
  accessed_at: '2026-10-11T09:47:35Z'
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
  support: context_only
  summary: Live 28-dataset iModulonDB inventory has no Chlamydomonas dataset. Not
    applicable; lack of coverage is not negative biological evidence.
- evidence_id: ma
  kind: primary_source
  reference: DOI:10.1016/j.cell.2019.09.030
  locator: Primary introduction; Results MIP networks, tubule junctions and Figure
    6; experimental model and specimen preparation
  accessed_at: '2026-10-11T09:38:39Z'
  snapshot_sha256: d2509facbaa0004a0963bc4722cda3b68d9e3eba7f8c1700f7c3f060440b9b90
  support: supports
  summary: Chlamydomonas doublets have 13-PF A and 10-PF B tubules; B01 joins A10/A11,
    B10 joins A01, and luminal MIP networks are distinct from the wall.
- evidence_id: child
  kind: record_content
  reference: data/structures/cytoskeleton/axonemal_b_tubule_inner_sheath.yaml
  accessed_at: '2026-10-11T09:47:35Z'
  snapshot_sha256: d1b0e481219c8b248e22e069aaa333074857a9ef8cae74d159e9a9e1f33a733e
  support: context_only
  summary: Existing B-sheath child retains its OPEN molecular task and the already
    documented current GO A/B relationship discrepancy. B-lumen containment is primary-supported.
- evidence_id: repository-history
  kind: record_content
  reference: history/records/b_axonemal_microtubule/2026-09-23T174334Z-claude-code-a53df0.yaml
  accessed_at: '2026-10-11T09:47:35Z'
  snapshot_sha256: 75f3976a9633c450e1bed88a1fc8255122ff36eab3fda790e751bf9f423c329c
  support: context_only
  summary: Creation history read; original actor metadata retained.
assessments:
- assessment_id: biology
  area: evidence
  topic: Identity, ten-protofilament boundary, species, function and all four graph
    edges
  outcome: supported
  target_ids:
  - GO:0097650
  evidence_ids:
  - record
  - go
  - taxa
  - ma
  - child
  summary: GO:0097650 exact identity, broad B-tubule synonym, axonemal-microtubule
    is-a and doublet parthood are supported. B-sheath has_part follows primary B-lumen
    evidence despite the known upstream typed-edge conflict. The NONMECHANISTIC graph
    correctly separates doublet membership, A fusion, B10 inner and B1 outer contacts.
    No molecular completeness, stoichiometry or universal taxonomic assertion is implied.
- assessment_id: provenance
  area: provenance
  topic: Original versus narrowed rationale
  outcome: concern
  target_ids:
  - GO:0097650
  evidence_ids:
  - record
  - rules
  - history
  summary: The rationale originally committed at 4bb42d3a describes the initial coarse
    B-tubule scope. Child creation at 871db9b2 replaced it with the narrowed inner-sheath
    wording. Narrowing the prompt was appropriate, but replacing the rationale loses
    provenance that CURATION.md requires to be appended, not overwritten.
- assessment_id: resources
  area: completeness
  topic: Optional slots and unresolved molecular work
  outcome: supported
  target_ids:
  - GO:0097650
  evidence_ids:
  - record
  - child
  summary: No image, dataset accession, protein-family assertion or quantitative measurement
    is present. Finer MIP identities and copy numbers remain acknowledged tasks, not
    invented issues.
findings:
- finding_id: F1
  issue_key: b-tubule-discussion-rationale-preservation
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Restore the original B-tubule discussion rationale
  description: The rationale originally committed at 4bb42d3a describes the initial
    coarse B-tubule scope. Child creation at 871db9b2 replaced it with the narrowed
    inner-sheath wording. Narrowing the prompt was appropriate, but replacing the
    rationale loses provenance that CURATION.md requires to be appended, not overwritten.
  target_ids:
  - GO:0097650
  field_paths:
  - discussions[0].rationale
  evidence_ids:
  - record
  - rules
  - history
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/b_axonemal_microtubule.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: minor
  normalization_reason: A bounded source-attribution or discussion-provenance defect;
    the biological identity and structure boundaries remain supported.
actions:
- action_id: A1
  description: Restore the original B-tubule discussion rationale
  finding_ids:
  - F1
  target_ids:
  - GO:0097650
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/b_axonemal_microtubule.yaml
    role: maintained scientific record
  acceptance_checks:
  - Restore the exact original rationale and retain the later rationale with its revision
    context.
  - Preserve current narrowed prompt, OPEN status, original author/date, live graph
    attachment, B-sheath child, all graph edges and biological fields.
  - Use the guarded writer, append Codex curation and EDIT history, preserve PROPOSED,
    prior history/reviews and unrelated records, regenerate pages, and pass focused
    regressions and native QC.
limitations:
- Same-agent scientific review, not independent human sign-off; all native records
  remain PROPOSED.
- Exact-baseline full QC is verified in CI; fresh scoped/global checks record actual
  resolver and label skips. Deterministic checks are not scientific certification.
- No raw micrograph, reconstruction-map or experimental-data reanalysis. Unknown molecular
  composition and stoichiometry are not certified.
- Ma Europe PMC XML returned an error; official PMC HTML was inspected. Li 2012 ordinary
  browser page presented a challenge; public official PMC open-data JATS and original
  media were available and checksum verified.
- Only this exact target is certified by this observation. Eleven other records whose
  files and resources were gathered in the batch remain pending full scientific assessment.
```
