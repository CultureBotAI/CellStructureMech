# SIN/MEN signaling complex: whole-record scientific review

- Review: 20261011T161557Z-sin_men_signaling_complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T16:09:17Z
- Finished UTC: 2026-10-11T16:15:57Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Entire native record reviewed; one minor finding saved before scientific curation.

## Scope And Provenance

Entire maintained YAML: identity, definition, hierarchy, taxonomic examples, functions, evidence, optional fields, discussions and both history surfaces.

Selection: Exact record in the four-record SIN/MEN signaling cohort of the 909-record goal.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ccc6aabffa4d212fbc05cc948bc3f6d071e46f0f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0160065 | data/structures/cytoskeleton/sin_men_signaling_complex.yaml | maintained | SIN/MEN signaling complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0160065 | Actual deterministic check passed; scientific support assessed separately. |
| strict | passed | True | GO:0160065 | Actual deterministic check passed; scientific support assessed separately. |
| snippets | passed | True | GO:0160065 | No verbatim snippets; paraphrases assessed separately against inspected text. |
| history | passed | True | GO:0160065 | Actual deterministic check passed; scientific support assessed separately. |
| labels | passed | True | GO:0160065 | id↔label correspondence summary:<br>          OK_CANONICAL: 3544<br>            OK_SYNONYM: 50<br>          OK_EXCEPTION: 6<br>    SKIPPED_NO_ADAPTER: 603<br><br>✅ All id↔label pairs correspond. |
| traits | passed | True | GO:0160065 | Actual deterministic check passed; scientific support assessed separately. |
| curies | passed | True | GO:0160065 | resolver control: every resolver accepts a known id and rejects a fabricated one<br><br>identifier liveness summary:<br>  OK             4014<br>  SKIPPED         251<br><br>Every identifier resolves at its issuing authority. |
| reviews | passed | True | GO:0160065 | Actual deterministic check passed; scientific support assessed separately. |
| diff | passed | True | GO:0160065 | Actual deterministic check passed; scientific support assessed separately. |
| contract | passed | True | GO:0160065 | ....                                                                     [100%]<br>4 passed in 124.51s (0:02:04) |
| Exact-baseline native CI QC | passed | True | GO:0160065 | Exact baseline merge-group QC passed, including 870 tests passed and 3 skipped; not a new local full-QC run. |

## Scientific And Domain Assessments

### Broad SIN/MEN complex and subtype boundaries

grounding: supported. Targets: GO:0160065.

Exact GO:0160065 identity, GO:0032991 parent and GO:0061499 parthood verified. GO-backed scaffold wording is not a new experimentally measured stoichiometry; narrower SIN and GAP records remain distinct.

### Species, examples and bounded function

evidence: supported. Targets: GO:0160065.

Fission- and budding-yeast model contexts and the broadly phrased septation/mitotic-exit organization function are supported. The SIN branch is not claimed to have every animal Hippo or budding-yeast mechanism.

### Sid2-Fin1 experimental population

evidence: concern. Targets: GO:0160065.

The Grallert 2012 evidence note says Sid2-Fin1 signaling links the SIN pathway to mitotic commitment. The primary paper explicitly concludes that the G2 Sid2/Mob1 population operates outside the SIN context, citing SIN-ablation experiments and cytoplasmic untagged Sid2. A shared SIN component is not evidence that the whole SPB-associated SIN complex mediates this G2 function. This is a bounded evidence-note overstatement, not a defect in the record identity or its septation/mitotic-exit function.

### Optional claims and provenance

completeness: supported. Targets: GO:0160065.

No exact component inventory, essentiality, graph, measurement, image, dataset, trait or pathway is asserted. Component-family grounding remains an acknowledged open task; older boundary discussions and dates are preserved.

## Findings

### F1: Distinguish cytoplasmic Sid2-Fin1 evidence from SPB SIN signaling

minor / open / confirmed; issue key: sin-men-sid2-fin1-evidence-context.

The Grallert 2012 evidence note says Sid2-Fin1 signaling links the SIN pathway to mitotic commitment. The primary paper explicitly concludes that the G2 Sid2/Mob1 population operates outside the SIN context, citing SIN-ablation experiments and cytoplasmic untagged Sid2. A shared SIN component is not evidence that the whole SPB-associated SIN complex mediates this G2 function. This is a bounded evidence-note overstatement, not a defect in the record identity or its septation/mitotic-exit function.

## Recommended Actions And Acceptance Checks

### A1

Distinguish cytoplasmic Sid2-Fin1 evidence from SPB SIN signaling

- Correct only the Grallert 2012 note to distinguish cytoplasmic, SIN-independent G2 Sid2-Fin1 signaling from the SPB-associated SIN complex.
- Retain the DOI, all definitions, functions, taxa, synonyms, hierarchy, discussions, original history and PROPOSED status.
- Guarded writer, actual Codex event and append-only EDIT history; focused regressions, regenerated artifacts, full QC and immutable review checks must pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/sin_men_signaling_complex.yaml | context_only | Entire native record read; captured inputs unchanged. |
| rules | docs/CURATION.md | context_only | Evidence must support the narrowest molecular role and experimental context. |
| history | /private/tmp/csm-review-20261011T160813Z/sin_men_signaling_complex-discussion-history.json | context_only | All committed discussions and inline events inspected; prior rationale and dates remain provenance. |
| history-0 | history/records/sin_men_signaling_complex/2026-09-29T184950Z-codex-5a5ae9.yaml | context_only | Original append-only CREATE history inspected. |
| predecessors | /private/tmp/csm-review-20261011T160813Z/exact-target-predecessors.json | context_only | Ignored-inclusive canonical scan found no exact-target predecessor. |
| issue-search | /private/tmp/csm-review-20261011T160813Z/sin-issues.log | context_only | All-state SIN, Spg1, Bub2 and exact-slug issue searches inspected. Prior #2220 concerns a distinct old-SPB record, not these findings. |
| exact-issues | /private/tmp/csm-review-20261011T160813Z/sin_men_signaling_complex-issues.log | context_only | No duplicate exact-slug issue returned by all-state search. |
| adapter | /private/tmp/csm-review-20261011T160813Z/adapter.log | context_only | Live iModulonDB inventory has no matching fungal dataset; absence is not biological evidence. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005816,GO:0032991,GO:0061499,GO:0071957,GO:0071958,GO:0160065,GO:0160066,GO:0160067,GO:1902773,GO:1990334; Exact identities, definitions, synonyms and typed children of all ten cited GO terms | supports | Nonobsolete exact identities and is-a/parthood relations verified. Interphase GO definition itself contains the Spg1/GAP role error. |
| pombe | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896; TaxId, scientificName and rank | supports | Schizosaccharomyces pombe species identity verified. |
| johnson | DOI:10.1038/emboj.2010.317; Introduction; Results, Figures 5 and 7; Discussion; microscopy and synchronization methods | supports | Spg1 is the GTPase and Byr4-Cdc16 its GAP. G2 and nda3 checkpoint experiments support Dma1-dependent Sid4 ubiquitination limiting Plo1 recruitment. The introduction describes Spg1 activation in metaphase, not uniform pre-anaphase inhibition. |
| cerevisiae | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; TaxId, scientificName and rank | supports | Saccharomyces cerevisiae species identity verified. |
| hippo-review | DOI:10.1016/j.semcdb.2012.04.001; Sections 2 and 3; scaffold comparison in section 4 | supports | Secondary synthesis distinguishes budding-yeast MEN mitotic exit and fission-yeast SIN cytokinetic emphasis; no animal taxonomic scope or predicted molecular cascade is promoted into this record. |
| grallert | DOI:10.1038/ncb2514; Results Figures 1-4; final two Results paragraphs; Methods; descriptions of Supplementary Figures 4 and 5 | supports | Sid2/Fin1 controls G2 commitment in the tested S. pombe cells. Persistence under SIN-ablation mutations and cytoplasmic untagged Sid2 led the authors to distinguish this population from SPB-associated SIN. |

## Limits And Additional Notes

- Same-agent whole-native-record review, not independent human approval or raw experimental-data reanalysis.
- Exact-baseline native CI supplies full QC. Local scoped/global and contract checks ran separately; resolver/label namespace skips and three empty-parameter test skips are explicit.
- Initial Europe PMC XML requests and normal PMC pages failed or returned interstitials. Actual article text was inspected from alternate official PMC representations; HTTP 200 alone was not treated as readable.
- The two other cohort records have separate clean coverage accounting; no review output is created for absent optional fields or acknowledged unknowns.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T161557Z-sin_men_signaling_complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'SIN/MEN signaling complex: whole-record scientific review'
started_at: '2026-10-11T16:09:17Z'
finished_at: '2026-10-11T16:15:57Z'
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
  git_revision: ccc6aabffa4d212fbc05cc948bc3f6d071e46f0f
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
  - path: data/structures/cytoskeleton/interphase_sin_signaling_complex.yaml
    sha256: 4b0e362cb8ffe1656a428f80a2893ddb06cbb889bef27d9d433a82e52e3a61e2
    role: context
  - path: data/structures/cytoskeleton/new_spindle_pole_body_sin_signaling_complex.yaml
    sha256: 84ade1d5217bae8fa401f096724d0892e76378469bec45c6ea25e961a0e28cae
    role: context
  - path: data/structures/cytoskeleton/outer_plaque_of_mitotic_spindle_pole_body.yaml
    sha256: 9197bc8f9b1fed339d56314bb682274576fa41bb94b26e2d09823e14a26ec226
    role: context
  - path: data/structures/cytoskeleton/sin_men_signaling_complex.yaml
    sha256: b55ca6d18a6a88c237076c582ebce7d4531e7c0a01bd0cf4edab8286c34f5ec0
    role: target
  - path: data/structures/cytoskeleton/sin_men_two_component_gap_complex.yaml
    sha256: 922665d09fdb8ddf24c904aefc3ccd0ec99a36f92d4d33f71a42c732036ecbdd
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
  - path: history/records/sin_men_signaling_complex/2026-09-29T184950Z-codex-5a5ae9.yaml
    sha256: 55205376f60e9c77bada3c007805ca5cabb8d849e3facab66566eb86cabbbd12
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reports/yaml_record_review/20260929T190718Z-sin_men_signaling_complex.md
    sha256: 4e58ba8deb34b6059a4d43b4095ee72055b446d0d19c39b3bc0c60ef92a32273
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
targets:
- target_id: GO:0160065
  path: data/structures/cytoskeleton/sin_men_signaling_complex.yaml
  label: SIN/MEN signaling complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/sin_men_signaling_complex.yaml
    role: maintained scientific record
scope:
  description: 'Entire maintained YAML: identity, definition, hierarchy, taxonomic
    examples, functions, evidence, optional fields, discussions and both history surfaces.'
  selection: Exact record in the four-record SIN/MEN signaling cohort of the 909-record
    goal.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0160065
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - GO:0160065
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/sin_men_signaling_complex.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T16:08:55Z to 2026-10-11T16:08:59Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - GO:0160065
  command: .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/sin_men_signaling_complex.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T16:08:59Z to 2026-10-11T16:09:06Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - GO:0160065
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/cytoskeleton/sin_men_signaling_complex.yaml
    --report /private/tmp/csm-review-20261011T160813Z/sin_men_signaling_complex-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: No verbatim snippets; paraphrases assessed separately against inspected
    text.
  scope_note: 2026-10-11T16:09:06Z to 2026-10-11T16:09:40Z; log SHA-256 16c4260243799d7f29be9bb803c57fd9fcc8a62b8c606d351b6de810de4cc228
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:0160065
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T16:11:44Z to 2026-10-11T16:12:00Z; log SHA-256 5176da9b48957f964a8a859b60ee792cb11f0923ef13345fbc9515affa329825
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - GO:0160065
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: "id↔label correspondence summary:\n          OK_CANONICAL: 3544\n     \
    \       OK_SYNONYM: 50\n          OK_EXCEPTION: 6\n    SKIPPED_NO_ADAPTER: 603\n\
    \n✅ All id↔label pairs correspond."
  scope_note: 2026-10-11T16:12:00Z to 2026-10-11T16:13:27Z; log SHA-256 d423103555a6a5b538a7c811a73a29c24ed0e5a2eae00d1bb94715295f23f7cb
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - GO:0160065
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T16:13:27Z to 2026-10-11T16:13:46Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - GO:0160065
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: "resolver control: every resolver accepts a known id and rejects a fabricated\
    \ one\n\nidentifier liveness summary:\n  OK             4014\n  SKIPPED      \
    \   251\n\nEvery identifier resolves at its issuing authority."
  scope_note: 2026-10-11T16:13:46Z to 2026-10-11T16:14:33Z; log SHA-256 ee1c5f2e78a2d29fcb6781a8ecd722934376595042d2cc261b4465b361d19b79
- check_id: reviews
  name: reviews
  status: passed
  required: true
  target_ids:
  - GO:0160065
  command: .venv/bin/python scripts/record_review.py check --base ccc6aabffa4d212fbc05cc948bc3f6d071e46f0f
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T16:14:33Z to 2026-10-11T16:15:37Z; log SHA-256 178fc02e47efe3f0ef3334ea51eb36c180497b72f9c24b0a27ac8aa8458d2037
- check_id: diff
  name: diff
  status: passed
  required: true
  target_ids:
  - GO:0160065
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T16:15:37Z to 2026-10-11T16:15:37Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- check_id: contract
  name: contract
  status: passed
  required: true
  target_ids:
  - GO:0160065
  command: .venv/bin/python -m pytest -q tests/test_record_review_contract.py
  exit_code: 0
  expected_exit_code: 0
  summary: '....                                                                     [100%]

    4 passed in 124.51s (0:02:04)'
  scope_note: 2026-10-11T16:08:52Z to 2026-10-11T16:10:57Z; log SHA-256 303d818f895774b3b8b6633d08ca9f9da310cd3c9963b0331791f443b31ffc6e
- check_id: qc
  name: Exact-baseline native CI QC
  status: passed
  required: true
  target_ids:
  - GO:0160065
  command: gh run view 38153527070 --repo CultureBotAI/CellStructureMech --log
  exit_code: 0
  expected_exit_code: 0
  summary: Exact baseline merge-group QC passed, including 870 tests passed and 3
    skipped; not a new local full-QC run.
  scope_note: https://github.com/CultureBotAI/CellStructureMech/actions/runs/38153527070;
    log SHA-256 b7a8e8bda85017955dfefbee655844bbebbfb1ffac6b02372a0a5598bdf1feba
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/sin_men_signaling_complex.yaml
  accessed_at: '2026-10-11T16:15:57Z'
  snapshot_sha256: b55ca6d18a6a88c237076c582ebce7d4531e7c0a01bd0cf4edab8286c34f5ec0
  support: context_only
  summary: Entire native record read; captured inputs unchanged.
- evidence_id: rules
  kind: record_content
  reference: docs/CURATION.md
  accessed_at: '2026-10-11T16:15:57Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  support: context_only
  summary: Evidence must support the narrowest molecular role and experimental context.
- evidence_id: history
  kind: record_content
  reference: /private/tmp/csm-review-20261011T160813Z/sin_men_signaling_complex-discussion-history.json
  accessed_at: '2026-10-11T16:15:57Z'
  snapshot_sha256: ca021defea1e8ff2ea027ebcbc39a17a2dc5653c2ed70c9dc053afafc2f94841
  support: context_only
  summary: All committed discussions and inline events inspected; prior rationale
    and dates remain provenance.
- evidence_id: history-0
  kind: record_content
  reference: history/records/sin_men_signaling_complex/2026-09-29T184950Z-codex-5a5ae9.yaml
  accessed_at: '2026-10-11T16:15:57Z'
  snapshot_sha256: 55205376f60e9c77bada3c007805ca5cabb8d849e3facab66566eb86cabbbd12
  support: context_only
  summary: Original append-only CREATE history inspected.
- evidence_id: predecessors
  kind: validation
  reference: /private/tmp/csm-review-20261011T160813Z/exact-target-predecessors.json
  accessed_at: '2026-10-11T16:15:57Z'
  snapshot_sha256: 33a10072c6ed2937e408183317e1cad173e154bca268ef2ad9824f8ac2b9c7e0
  support: context_only
  summary: Ignored-inclusive canonical scan found no exact-target predecessor.
- evidence_id: issue-search
  kind: validation
  reference: /private/tmp/csm-review-20261011T160813Z/sin-issues.log
  accessed_at: '2026-10-11T16:15:57Z'
  snapshot_sha256: 5d832bed44ec67e5691e41903869175a80db31283dbd9b4bda9662225ca81e86
  support: context_only
  summary: 'All-state SIN, Spg1, Bub2 and exact-slug issue searches inspected. Prior
    #2220 concerns a distinct old-SPB record, not these findings.'
- evidence_id: exact-issues
  kind: validation
  reference: /private/tmp/csm-review-20261011T160813Z/sin_men_signaling_complex-issues.log
  accessed_at: '2026-10-11T16:15:57Z'
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
  support: context_only
  summary: No duplicate exact-slug issue returned by all-state search.
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/csm-review-20261011T160813Z/adapter.log
  accessed_at: '2026-10-11T16:15:57Z'
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
  support: context_only
  summary: Live iModulonDB inventory has no matching fungal dataset; absence is not
    biological evidence.
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005816,GO:0032991,GO:0061499,GO:0071957,GO:0071958,GO:0160065,GO:0160066,GO:0160067,GO:1902773,GO:1990334
  locator: Exact identities, definitions, synonyms and typed children of all ten cited
    GO terms
  accessed_at: '2026-10-11T16:09:44Z'
  snapshot_sha256: 955957c96302813b49581c5d1bee32ebe2e8db24bd4139ec1f7dabaab125e398
  support: supports
  summary: Nonobsolete exact identities and is-a/parthood relations verified. Interphase
    GO definition itself contains the Spg1/GAP role error.
- evidence_id: pombe
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896
  locator: TaxId, scientificName and rank
  accessed_at: '2026-10-11T16:09:45Z'
  snapshot_sha256: cdb53b3f4ab5e6bb4476de3bf0db333ae647e307a9fa8f98108827f98fe7f4d3
  support: supports
  summary: Schizosaccharomyces pombe species identity verified.
- evidence_id: johnson
  kind: primary_source
  reference: DOI:10.1038/emboj.2010.317
  locator: Introduction; Results, Figures 5 and 7; Discussion; microscopy and synchronization
    methods
  accessed_at: '2026-10-11T16:10:11Z'
  snapshot_sha256: dbe1a1ec2e907299e89b1aac957a57abf54070e018514d7db25bf19de53d6383
  support: supports
  summary: Spg1 is the GTPase and Byr4-Cdc16 its GAP. G2 and nda3 checkpoint experiments
    support Dma1-dependent Sid4 ubiquitination limiting Plo1 recruitment. The introduction
    describes Spg1 activation in metaphase, not uniform pre-anaphase inhibition.
- evidence_id: cerevisiae
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: TaxId, scientificName and rank
  accessed_at: '2026-10-11T16:09:45Z'
  snapshot_sha256: c4e5f7b0462251e0d309ae5ad59f47eb6b3846cbe9fcb8506648a7898d4ad1a8
  support: supports
  summary: Saccharomyces cerevisiae species identity verified.
- evidence_id: hippo-review
  kind: authority
  reference: DOI:10.1016/j.semcdb.2012.04.001
  locator: Sections 2 and 3; scaffold comparison in section 4
  accessed_at: '2026-10-11T16:10:11Z'
  snapshot_sha256: 6612a27c0f9af3e4774b4f9ceaba9cad558d3d1cced9a4b5462baf14e0558e10
  support: supports
  summary: Secondary synthesis distinguishes budding-yeast MEN mitotic exit and fission-yeast
    SIN cytokinetic emphasis; no animal taxonomic scope or predicted molecular cascade
    is promoted into this record.
- evidence_id: grallert
  kind: primary_source
  reference: DOI:10.1038/ncb2514
  locator: Results Figures 1-4; final two Results paragraphs; Methods; descriptions
    of Supplementary Figures 4 and 5
  accessed_at: '2026-10-11T16:08:58Z'
  snapshot_sha256: 167951feb8f53cd8e0852da24b6da3a9f8d9a6db3136dab57fd7f461ff9a5fc6
  support: supports
  summary: Sid2/Fin1 controls G2 commitment in the tested S. pombe cells. Persistence
    under SIN-ablation mutations and cytoplasmic untagged Sid2 led the authors to
    distinguish this population from SPB-associated SIN.
assessments:
- assessment_id: identity
  area: grounding
  topic: Broad SIN/MEN complex and subtype boundaries
  outcome: supported
  target_ids:
  - GO:0160065
  evidence_ids:
  - record
  - go
  - johnson
  summary: Exact GO:0160065 identity, GO:0032991 parent and GO:0061499 parthood verified.
    GO-backed scaffold wording is not a new experimentally measured stoichiometry;
    narrower SIN and GAP records remain distinct.
- assessment_id: biology
  area: evidence
  topic: Species, examples and bounded function
  outcome: supported
  target_ids:
  - GO:0160065
  evidence_ids:
  - record
  - pombe
  - cerevisiae
  - johnson
  - hippo-review
  summary: Fission- and budding-yeast model contexts and the broadly phrased septation/mitotic-exit
    organization function are supported. The SIN branch is not claimed to have every
    animal Hippo or budding-yeast mechanism.
- assessment_id: source-scope
  area: evidence
  topic: Sid2-Fin1 experimental population
  outcome: concern
  target_ids:
  - GO:0160065
  evidence_ids:
  - record
  - grallert
  - rules
  summary: The Grallert 2012 evidence note says Sid2-Fin1 signaling links the SIN
    pathway to mitotic commitment. The primary paper explicitly concludes that the
    G2 Sid2/Mob1 population operates outside the SIN context, citing SIN-ablation
    experiments and cytoplasmic untagged Sid2. A shared SIN component is not evidence
    that the whole SPB-associated SIN complex mediates this G2 function. This is a
    bounded evidence-note overstatement, not a defect in the record identity or its
    septation/mitotic-exit function.
- assessment_id: remaining
  area: completeness
  topic: Optional claims and provenance
  outcome: supported
  target_ids:
  - GO:0160065
  evidence_ids:
  - record
  - history
  - rules
  summary: No exact component inventory, essentiality, graph, measurement, image,
    dataset, trait or pathway is asserted. Component-family grounding remains an acknowledged
    open task; older boundary discussions and dates are preserved.
findings:
- finding_id: F1
  issue_key: sin-men-sid2-fin1-evidence-context
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Distinguish cytoplasmic Sid2-Fin1 evidence from SPB SIN signaling
  description: The Grallert 2012 evidence note says Sid2-Fin1 signaling links the
    SIN pathway to mitotic commitment. The primary paper explicitly concludes that
    the G2 Sid2/Mob1 population operates outside the SIN context, citing SIN-ablation
    experiments and cytoplasmic untagged Sid2. A shared SIN component is not evidence
    that the whole SPB-associated SIN complex mediates this G2 function. This is a
    bounded evidence-note overstatement, not a defect in the record identity or its
    septation/mitotic-exit function.
  target_ids:
  - GO:0160065
  field_paths:
  - evidence[reference=DOI:10.1038/ncb2514].notes
  evidence_ids:
  - record
  - grallert
  - rules
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/sin_men_signaling_complex.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: minor
  normalization_reason: Nonblocking evidence-note context error; no asserted mitotic-entry
    function or causal graph depends on it, so severity is minor.
actions:
- action_id: A1
  description: Distinguish cytoplasmic Sid2-Fin1 evidence from SPB SIN signaling
  finding_ids:
  - F1
  target_ids:
  - GO:0160065
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/sin_men_signaling_complex.yaml
    role: maintained scientific record
  acceptance_checks:
  - Correct only the Grallert 2012 note to distinguish cytoplasmic, SIN-independent
    G2 Sid2-Fin1 signaling from the SPB-associated SIN complex.
  - Retain the DOI, all definitions, functions, taxa, synonyms, hierarchy, discussions,
    original history and PROPOSED status.
  - Guarded writer, actual Codex event and append-only EDIT history; focused regressions,
    regenerated artifacts, full QC and immutable review checks must pass.
limitations:
- Same-agent whole-native-record review, not independent human approval or raw experimental-data
  reanalysis.
- Exact-baseline native CI supplies full QC. Local scoped/global and contract checks
  ran separately; resolver/label namespace skips and three empty-parameter test skips
  are explicit.
- Initial Europe PMC XML requests and normal PMC pages failed or returned interstitials.
  Actual article text was inspected from alternate official PMC representations; HTTP
  200 alone was not treated as readable.
- The two other cohort records have separate clean coverage accounting; no review
  output is created for absent optional fields or acknowledged unknowns.
```
