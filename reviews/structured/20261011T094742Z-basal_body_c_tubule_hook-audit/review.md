# Basal body c tubule hook: scientific record review

- Review: 20261011T094742Z-basal_body_c_tubule_hook-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T09:36:13Z
- Finished UTC: 2026-10-11T09:47:42Z
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
| cellstructuremech:basal_body_c_tubule_hook | data/structures/cytoskeleton/basal_body_c_tubule_hook.yaml | maintained | basal body C-tubule hook |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | cellstructuremech:basal_body_c_tubule_hook | Deterministic check passed; scientific assessment is separate. |
| strict | passed | True | cellstructuremech:basal_body_c_tubule_hook | Deterministic check passed; scientific assessment is separate. |
| snippets | passed | True | cellstructuremech:basal_body_c_tubule_hook | No verbatim snippets asserted; paraphrased claims were checked against inspected primary text. |
| history | passed | True | cellstructuremech:basal_body_c_tubule_hook | Deterministic check passed; scientific assessment is separate. |
| labels | passed | True | cellstructuremech:basal_body_c_tubule_hook | id↔label correspondence summary:<br>          OK_CANONICAL: 3544<br>            OK_SYNONYM: 50<br>          OK_EXCEPTION: 6<br>    SKIPPED_NO_ADAPTER: 603<br><br>✅ All id↔label pairs correspond. |
| traits | passed | True | cellstructuremech:basal_body_c_tubule_hook | Deterministic check passed; scientific assessment is separate. |
| curies | passed | True | cellstructuremech:basal_body_c_tubule_hook | resolver control: every resolver accepts a known id and rejects a fabricated one<br><br>identifier liveness summary:<br>  OK             4014<br>  SKIPPED         251<br><br>Every identifier resolves at its issuing authority. |
| reviews | passed | True | cellstructuremech:basal_body_c_tubule_hook | Deterministic check passed; scientific assessment is separate. |
| diff | passed | True | cellstructuremech:basal_body_c_tubule_hook | Deterministic check passed; scientific assessment is separate. |
| Exact-baseline CI full QC | passed | True | cellstructuremech:basal_body_c_tubule_hook | Full QC passed on the exact captured baseline: 843 tests passed, 3 skipped; native and shared review gates passed. Verified CI receipt, not a new local full-QC run. |

## Scientific And Domain Assessments

### Native identity, occurrence, structure/function and measurement support

evidence: supported. Targets: cellstructuremech:basal_body_c_tubule_hook.

The native boundary is the exterior B4/C1 linker across C2-C4, distinct from inner junctions and the luminal crescent. Its distal 8-nm repeat is a spacing, not hook length. Structural linkage is observed, while stiffness, essentiality, POC5/delta-tubulin assignment and direct crescent interaction remain unasserted. OTHER and empty components preserve unknown protein/complex composition. C-stretch equivalence is correctly OPEN.

### is-a versus containing framework

grounding: concern. Targets: cellstructuremech:basal_body_c_tubule_hook.

parent_structures asserts that this individual exterior B-C linker is a type of GO:0005856 cytoskeleton, and identity_and_boundary repeats that classification. The containing cytoskeletal framework is not an is-a superclass of each component. Li 2012 resolves a localized unknown protein or complex, not a whole cytoskeleton. Its composition does not establish a more specific protein-complex class.

### Image, data and discussion boundaries

provenance: supported. Targets: cellstructuremech:basal_body_c_tubule_hook.

Official JATS and Figure 4 MD5 checks passed; CC BY-NC-ND 3.0 matches the link-only native license and author attribution. EMD-5252 is correctly scoped as a whole-triplet deposit. No raw map, reconstruction or molecule identification is claimed. Discussion lifecycle and original rationales are retained; optional empty components/graphs are not defects.

## Findings

### F1: Separate C-tubule hook classification from cytoskeleton parthood

major / open / confirmed; issue key: basal-body-c-tubule-hook-is-a-parent.

parent_structures asserts that this individual exterior B-C linker is a type of GO:0005856 cytoskeleton, and identity_and_boundary repeats that classification. The containing cytoskeletal framework is not an is-a superclass of each component. Li 2012 resolves a localized unknown protein or complex, not a whole cytoskeleton. Its composition does not establish a more specific protein-complex class.

## Recommended Actions And Acceptance Checks

### A1

Separate C-tubule hook classification from cytoskeleton parthood

- Replace the unsupported cytoskeleton is-a parent with conservative GO:0005575 cellular component and retain GO:0036064 basal-body parthood.
- Correct current classification notes with a dated explanation while preserving original rationale, author, dates, status, earlier evidence and scientific unknowns.
- Do not infer a polymeric fiber or identified complex; retain structure kind, measurements, image license/link-only handling, dataset scope and taxon bounds.
- Use the guarded writer, append Codex curation and EDIT history, preserve PROPOSED, prior history/reviews and unrelated records, regenerate pages, and pass focused regressions and native QC.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/basal_body_c_tubule_hook.yaml | context_only | Entire native YAML read; formal capture preceded assessment. Initial reading preceded capture. |
| rules | docs/CURATION.md | context_only | parent_structures is is-a, part_of is containment; individual fibers are not cytoskeleton subclasses. Discussion rationale is append-only. |
| history | /private/tmp/csm-review-20261011T093443Z/basal_body_c_tubule_hook-discussion-history.json | context_only | Complete committed discussion and curation-event history inspected. |
| predecessors | /private/tmp/csm-review-20261011T093443Z/exact-target-predecessors.json | context_only | Ignored-inclusive canonical-review scan found no exact-target predecessor; legacy reports are historical context, not canonical lineage. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005575,GO:0005856,GO:0005879,GO:0032053,GO:0032991,GO:0036064,GO:0097545,GO:0097649,GO:0097650,GO:0110165,GO:0120280,GO:0140180,GO:0140535,GO:0160110,GO:0160112,GO:0160113,GO:0160114; Relevant GO definitions, aspect, obsolescence and typed reverse children | supports | B-tubule identity and axonemal parent/parthood are supported. GO:0005856 denotes the containing framework, not an is-a class for each basal-body subassembly. |
| taxa | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=285686%2C3055%2C5762%2C5888%2C5911%2C63628; Top-level NCBITaxon:3055 Chlamydomonas reinhardtii, rank species | supports | Resolves taxon identity, not biological prevalence. |
| adapter | /private/tmp/csm-review-20261011T093443Z/adapter.log | context_only | Live 28-dataset iModulonDB inventory has no Chlamydomonas dataset. Not applicable; lack of coverage is not negative biological evidence. |
| li2012 | DOI:10.1038/emboj.2011.460; Non-tubulin and longitudinal-variation Results, longitudinal Discussion, reconstruction Methods, Figure 4 and licensing | supports | Directly supports separate distal exterior hook and C3-to-C6/C7 crescent, contextual repeats/span and unknown composition. Density-estimated mass is not biochemical identity. |
| figure4 | https://pmc-oa-opendata.s3.amazonaws.com/PMC3273388.1/emboj2011460f4.jpg; Visually inspected original Figure 4, panels A-C; MD5 083fbb77c122e8f6569e43593024eee5 verified against official PMC manifest | supports | Panel B is the exterior yellow hook; C is the separate luminal crescent; A scale is 10 nm. The native image remains link-only under CC BY-NC-ND 3.0; no media is added to the repository. |
| emdb | https://www.ebi.ac.uk/emdb/api/entry/EMD-5252; Released entry: title, natural source and primary citation | supports | Whole-triplet reconstruction, Chlamydomonas taxon 3055, archive strain cc3491, DOI 10.1038/emboj.2011.460 and PMID 22157822; not an isolated substructure map. |
| unit | https://www.ebi.ac.uk/ols4/api/ontologies/uo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUO_0000018; UO:0000018 definition, label and non-obsolete status | supports | Nanometer; 136 angstrom converts to 13.6 nm. |
| fiber | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0099513; GO:0099513 definition and aspect | supports | Requires a homo/heteropolymeric fiber of protein subunits; the density morphology and mass estimate do not demonstrate this classification. |
| history-2026-10-04T113303Z-codex-235fd4 | history/records/basal_body_c_tubule_hook/2026-10-04T113303Z-codex-235fd4.yaml | context_only | Append-only creation/correction history inspected and retained. |
| history-2026-10-04T113801Z-codex-c4af83 | history/records/basal_body_c_tubule_hook/2026-10-04T113801Z-codex-c4af83.yaml | context_only | Append-only creation/correction history inspected and retained. |
| legacy | reports/yaml_record_review/20261004T114928Z-basal_body_c_tubule_hook.md | context_only | Earlier same-agent clean report incorrectly accepted the broad cytoskeleton class. It remains immutable historical context; the present issue is judged against current native rules. |
| nazarov | DOI:10.15252/embj.2020106249; Peripheral triplet Results, Figure 4I and organism/purification Methods | supports | Teranympha mirabilis C1 C-stretch is a comparison lead, not established equivalence with the distal Chlamydomonas exterior C2-C4 hook. |
| nazarov-figure | https://pmc-oa-opendata.s3.amazonaws.com/PMC7667878.1/EMBJ-39-e106249-g008.jpg; Visually inspected original Figure 4I with explicit Teranympha mirabilis heading and C-stretch marker | supports | Figure matches the bounded comparison; it does not establish homology with the hook. |

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
review_id: 20261011T094742Z-basal_body_c_tubule_hook-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'Basal body c tubule hook: scientific record review'
started_at: '2026-10-11T09:36:13Z'
finished_at: '2026-10-11T09:47:42Z'
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
  - path: data/structures/cytoskeleton/b_axonemal_microtubule.yaml
    sha256: 438f1274f334f407b89cb2f89c27796d3c909385e3535e57151f4d07fbe9c160
    role: context
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
    role: target
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
  - path: data/structures/cytoskeleton/ciliary_basal_body.yaml
    sha256: 8f80489e9683ac36bb07ed5c1c435a1627df5e71c9458f1fcc1f842d65a93128
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
  - path: history/records/basal_body_c_tubule_hook/2026-10-04T113303Z-codex-235fd4.yaml
    sha256: 232a8ba8378fad3e17a432b99346b827f16ff6078aec45a6b3346d2cae869ed0
    role: context
  - path: history/records/basal_body_c_tubule_hook/2026-10-04T113801Z-codex-c4af83.yaml
    sha256: 34d82471867c33c572bf59e5b62282668026eed5d3916c7396a9a4a2250afd47
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reports/yaml_record_review/20261004T114928Z-basal_body_c_tubule_hook.md
    sha256: b038cac01e331846e63410182455d8b362bb8b76d1eba6bf745ef59812d36868
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
targets:
- target_id: cellstructuremech:basal_body_c_tubule_hook
  path: data/structures/cytoskeleton/basal_body_c_tubule_hook.yaml
  label: basal body C-tubule hook
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/basal_body_c_tubule_hook.yaml
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
  - cellstructuremech:basal_body_c_tubule_hook
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_c_tubule_hook
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/basal_body_c_tubule_hook.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Deterministic check passed; scientific assessment is separate.
  scope_note: 2026-10-11T09:39:35Z to 2026-10-11T09:39:37Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_c_tubule_hook
  command: .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/basal_body_c_tubule_hook.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Deterministic check passed; scientific assessment is separate.
  scope_note: 2026-10-11T09:39:37Z to 2026-10-11T09:39:42Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_c_tubule_hook
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/cytoskeleton/basal_body_c_tubule_hook.yaml
    --report /private/tmp/csm-review-20261011T093443Z/basal_body_c_tubule_hook-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: No verbatim snippets asserted; paraphrased claims were checked against
    inspected primary text.
  scope_note: 2026-10-11T09:39:42Z to 2026-10-11T09:40:05Z; log SHA-256 ea0b7017567ede828820d78f7473524f8b65c0c47b98b2794783eb5c77cff18f
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_c_tubule_hook
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
  - cellstructuremech:basal_body_c_tubule_hook
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
  - cellstructuremech:basal_body_c_tubule_hook
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
  - cellstructuremech:basal_body_c_tubule_hook
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
  - cellstructuremech:basal_body_c_tubule_hook
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
  - cellstructuremech:basal_body_c_tubule_hook
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
  - cellstructuremech:basal_body_c_tubule_hook
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
  reference: data/structures/cytoskeleton/basal_body_c_tubule_hook.yaml
  accessed_at: '2026-10-11T09:47:42Z'
  snapshot_sha256: fb30d8f9a7713b2be51b6afd830658a2950397a2b99978423d97768c06aa3899
  support: context_only
  summary: Entire native YAML read; formal capture preceded assessment. Initial reading
    preceded capture.
- evidence_id: rules
  kind: record_content
  reference: docs/CURATION.md
  accessed_at: '2026-10-11T09:47:42Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  support: context_only
  summary: parent_structures is is-a, part_of is containment; individual fibers are
    not cytoskeleton subclasses. Discussion rationale is append-only.
- evidence_id: history
  kind: record_content
  reference: /private/tmp/csm-review-20261011T093443Z/basal_body_c_tubule_hook-discussion-history.json
  accessed_at: '2026-10-11T09:47:42Z'
  snapshot_sha256: ab4ac2a96470d6c50af5bb1339adf1b10d50e269b781a646bfa77a838b55ce55
  support: context_only
  summary: Complete committed discussion and curation-event history inspected.
- evidence_id: predecessors
  kind: validation
  reference: /private/tmp/csm-review-20261011T093443Z/exact-target-predecessors.json
  accessed_at: '2026-10-11T09:47:42Z'
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
  accessed_at: '2026-10-11T09:47:42Z'
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
  support: context_only
  summary: Live 28-dataset iModulonDB inventory has no Chlamydomonas dataset. Not
    applicable; lack of coverage is not negative biological evidence.
- evidence_id: li2012
  kind: primary_source
  reference: DOI:10.1038/emboj.2011.460
  locator: Non-tubulin and longitudinal-variation Results, longitudinal Discussion,
    reconstruction Methods, Figure 4 and licensing
  accessed_at: '2026-10-11T09:44:47Z'
  snapshot_sha256: 88f7ba4bc99d15a2f5bb6b614f143fac8fb754906aa0a5691a8ab3086975f392
  support: supports
  summary: Directly supports separate distal exterior hook and C3-to-C6/C7 crescent,
    contextual repeats/span and unknown composition. Density-estimated mass is not
    biochemical identity.
- evidence_id: figure4
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3273388.1/emboj2011460f4.jpg
  locator: Visually inspected original Figure 4, panels A-C; MD5 083fbb77c122e8f6569e43593024eee5
    verified against official PMC manifest
  accessed_at: '2026-10-11T09:45:36Z'
  snapshot_sha256: 5d9bc448a64e0f228a4dbe62f78b1d6917253b985e501a79a2bf10c0e9cef022
  support: supports
  summary: Panel B is the exterior yellow hook; C is the separate luminal crescent;
    A scale is 10 nm. The native image remains link-only under CC BY-NC-ND 3.0; no
    media is added to the repository.
- evidence_id: emdb
  kind: authority
  reference: https://www.ebi.ac.uk/emdb/api/entry/EMD-5252
  locator: 'Released entry: title, natural source and primary citation'
  accessed_at: '2026-10-11T09:44:30Z'
  snapshot_sha256: 9b57cace8eba48262976b13b4bb1ed072dba283166071643d0a5fe82e56aa741
  support: supports
  summary: Whole-triplet reconstruction, Chlamydomonas taxon 3055, archive strain
    cc3491, DOI 10.1038/emboj.2011.460 and PMID 22157822; not an isolated substructure
    map.
- evidence_id: unit
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUO_0000018
  locator: UO:0000018 definition, label and non-obsolete status
  accessed_at: '2026-10-11T09:44:13Z'
  snapshot_sha256: 5aa4d11cd0f398ac65be12b58f91295efae620bb2e5c345bd0fd81c6f0e09c5c
  support: supports
  summary: Nanometer; 136 angstrom converts to 13.6 nm.
- evidence_id: fiber
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0099513
  locator: GO:0099513 definition and aspect
  accessed_at: '2026-10-11T09:45:36Z'
  snapshot_sha256: 69212ecd630a102ae807c05bc31423674c8ce1ab3157055a35c53725b977f11f
  support: supports
  summary: Requires a homo/heteropolymeric fiber of protein subunits; the density
    morphology and mass estimate do not demonstrate this classification.
- evidence_id: history-2026-10-04T113303Z-codex-235fd4
  kind: record_content
  reference: history/records/basal_body_c_tubule_hook/2026-10-04T113303Z-codex-235fd4.yaml
  accessed_at: '2026-10-11T09:47:42Z'
  snapshot_sha256: 232a8ba8378fad3e17a432b99346b827f16ff6078aec45a6b3346d2cae869ed0
  support: context_only
  summary: Append-only creation/correction history inspected and retained.
- evidence_id: history-2026-10-04T113801Z-codex-c4af83
  kind: record_content
  reference: history/records/basal_body_c_tubule_hook/2026-10-04T113801Z-codex-c4af83.yaml
  accessed_at: '2026-10-11T09:47:42Z'
  snapshot_sha256: 34d82471867c33c572bf59e5b62282668026eed5d3916c7396a9a4a2250afd47
  support: context_only
  summary: Append-only creation/correction history inspected and retained.
- evidence_id: legacy
  kind: prior_review
  reference: reports/yaml_record_review/20261004T114928Z-basal_body_c_tubule_hook.md
  accessed_at: '2026-10-11T09:47:42Z'
  snapshot_sha256: b038cac01e331846e63410182455d8b362bb8b76d1eba6bf745ef59812d36868
  support: context_only
  summary: Earlier same-agent clean report incorrectly accepted the broad cytoskeleton
    class. It remains immutable historical context; the present issue is judged against
    current native rules.
- evidence_id: nazarov
  kind: primary_source
  reference: DOI:10.15252/embj.2020106249
  locator: Peripheral triplet Results, Figure 4I and organism/purification Methods
  accessed_at: '2026-10-11T09:44:50Z'
  snapshot_sha256: da696473d57237f2bfd808b07dd5b1070267e0b46775f92f22bb134e07d6da47
  support: supports
  summary: Teranympha mirabilis C1 C-stretch is a comparison lead, not established
    equivalence with the distal Chlamydomonas exterior C2-C4 hook.
- evidence_id: nazarov-figure
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC7667878.1/EMBJ-39-e106249-g008.jpg
  locator: Visually inspected original Figure 4I with explicit Teranympha mirabilis
    heading and C-stretch marker
  accessed_at: '2026-10-11T09:44:58Z'
  snapshot_sha256: 3f53fa8d66e6190e7ed2eabef754711bdc455d3598a67123f723641a4c51de33
  support: supports
  summary: Figure matches the bounded comparison; it does not establish homology with
    the hook.
assessments:
- assessment_id: biology
  area: evidence
  topic: Native identity, occurrence, structure/function and measurement support
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_c_tubule_hook
  evidence_ids:
  - record
  - go
  - taxa
  - li2012
  - figure4
  - emdb
  - unit
  - nazarov
  - nazarov-figure
  summary: The native boundary is the exterior B4/C1 linker across C2-C4, distinct
    from inner junctions and the luminal crescent. Its distal 8-nm repeat is a spacing,
    not hook length. Structural linkage is observed, while stiffness, essentiality,
    POC5/delta-tubulin assignment and direct crescent interaction remain unasserted.
    OTHER and empty components preserve unknown protein/complex composition. C-stretch
    equivalence is correctly OPEN.
- assessment_id: hierarchy
  area: grounding
  topic: is-a versus containing framework
  outcome: concern
  target_ids:
  - cellstructuremech:basal_body_c_tubule_hook
  evidence_ids:
  - record
  - go
  - fiber
  - rules
  - li2012
  summary: parent_structures asserts that this individual exterior B-C linker is a
    type of GO:0005856 cytoskeleton, and identity_and_boundary repeats that classification.
    The containing cytoskeletal framework is not an is-a superclass of each component.
    Li 2012 resolves a localized unknown protein or complex, not a whole cytoskeleton.
    Its composition does not establish a more specific protein-complex class.
- assessment_id: resources
  area: provenance
  topic: Image, data and discussion boundaries
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_c_tubule_hook
  evidence_ids:
  - record
  - go
  - taxa
  - li2012
  - figure4
  - emdb
  - unit
  - nazarov
  - nazarov-figure
  summary: Official JATS and Figure 4 MD5 checks passed; CC BY-NC-ND 3.0 matches the
    link-only native license and author attribution. EMD-5252 is correctly scoped
    as a whole-triplet deposit. No raw map, reconstruction or molecule identification
    is claimed. Discussion lifecycle and original rationales are retained; optional
    empty components/graphs are not defects.
findings:
- finding_id: F1
  issue_key: basal-body-c-tubule-hook-is-a-parent
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Separate C-tubule hook classification from cytoskeleton parthood
  description: parent_structures asserts that this individual exterior B-C linker
    is a type of GO:0005856 cytoskeleton, and identity_and_boundary repeats that classification.
    The containing cytoskeletal framework is not an is-a superclass of each component.
    Li 2012 resolves a localized unknown protein or complex, not a whole cytoskeleton.
    Its composition does not establish a more specific protein-complex class.
  target_ids:
  - cellstructuremech:basal_body_c_tubule_hook
  field_paths:
  - parent_structures
  - discussions[0].notes
  evidence_ids:
  - record
  - go
  - fiber
  - rules
  - li2012
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/basal_body_c_tubule_hook.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: major
  normalization_reason: Unsupported ontology superclass is a major wrong-grounding
    defect under the native rubric, even though the local identity and observed morphology
    remain correct.
actions:
- action_id: A1
  description: Separate C-tubule hook classification from cytoskeleton parthood
  finding_ids:
  - F1
  target_ids:
  - cellstructuremech:basal_body_c_tubule_hook
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/basal_body_c_tubule_hook.yaml
    role: maintained scientific record
  acceptance_checks:
  - Replace the unsupported cytoskeleton is-a parent with conservative GO:0005575
    cellular component and retain GO:0036064 basal-body parthood.
  - Correct current classification notes with a dated explanation while preserving
    original rationale, author, dates, status, earlier evidence and scientific unknowns.
  - Do not infer a polymeric fiber or identified complex; retain structure kind, measurements,
    image license/link-only handling, dataset scope and taxon bounds.
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
