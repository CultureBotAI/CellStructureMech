# A axonemal microtubule: finding dispositions

- Review: 20261011T074246Z-a_axonemal_microtubule-disposition
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T07:31:35Z
- Finished UTC: 2026-10-11T07:42:46Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Exact predecessor findings resolved; original evidence-access tiers and biological uncertainties retained. No scientific status promotion.

## Scope And Provenance

Exact predecessor findings, corrected fields and preservation of surrounding claims; not a repeated whole-record scientific review.

Selection: 20261011T071241Z-a_axonemal_microtubule-audit
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7b2a10264b5217ea5be79569b2355f2dbdc4424c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0097649 | data/structures/cytoskeleton/a_axonemal_microtubule.yaml | maintained | A axonemal microtubule |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0097649 | Actual post-curation command passed. Empty quotation checks and resolver skips are not scientific proof. |
| strict | passed | True | GO:0097649 | Actual post-curation command passed. Empty quotation checks and resolver skips are not scientific proof. |
| snippets | passed | True | GO:0097649 | Actual post-curation command passed. Empty quotation checks and resolver skips are not scientific proof. |
| history | passed | True | GO:0097649 | Actual post-curation command passed. Empty quotation checks and resolver skips are not scientific proof. |
| labels | passed | True | GO:0097649 | id↔label correspondence summary:<br>          OK_CANONICAL: 3544<br>            OK_SYNONYM: 50<br>          OK_EXCEPTION: 6<br>    SKIPPED_NO_ADAPTER: 603<br><br>✅ All id↔label pairs correspond. |
| traits | passed | True | GO:0097649 | Actual post-curation command passed. Empty quotation checks and resolver skips are not scientific proof. |
| curies | passed | True | GO:0097649 | resolver control: every resolver accepts a known id and rejects a fabricated one<br>resolving 1 DOI identifier(s)...<br>resolving 2 GO identifier(s)...<br><br>identifier liveness summary:<br>  OK             4014<br>  SKIPPED         251<br><br>Every identifier resolves at its issuing authority. |
| regressions | passed | True | GO:0097649 | ..............................                                           [100%]<br>30 passed in 41.06s |
| reviews | passed | True | GO:0097649 | Actual post-curation command passed. Empty quotation checks and resolver skips are not scientific proof. |
| diff | passed | True | GO:0097649 | Actual post-curation command passed. Empty quotation checks and resolver skips are not scientific proof. |
| website-focused | passed | True | GO:0097649 | Actual post-curation command passed. Empty quotation checks and resolver skips are not scientific proof. |
| release-qc2 | passed | True | GO:0097649 | Authoritative full local QC passed, including tests, all-record schema/history, generated products and contract checks. Remote PR and merge-group checks remain separate publication gates. |
| Initial QC before website-reference integration fix | failed | False | GO:0097649 | Historical failed attempt: one missing external GO website-label assertion, 835 passed and 3 skipped. The catalog, retained sources and rebuild list were corrected; release-qc2 is the final required passing gate. |

## Scientific And Domain Assessments

### Restore the original A-tubule discussion rationale

provenance: supported. Targets: GO:0097649.

The exact original rationale is restored as the prefix, followed by the complete later inner-sheath explanation with a dated reassessment marker. Original posed date, narrowed prompt, OPEN status, child and attachment graph are retained.

## Findings

### F1: Restore the original A-tubule discussion rationale

minor / resolved / confirmed; issue key: a-tubule-original-rationale-preservation.

The exact original rationale is restored as the prefix, followed by the complete later inner-sheath explanation with a dated reassessment marker. Original posed date, narrowed prompt, OPEN status, child and attachment graph are retained.

Disposition: The exact original rationale is restored as the prefix, followed by the complete later inner-sheath explanation with a dated reassessment marker. Original posed date, narrowed prompt, OPEN status, child and attachment graph are retained. Verified with source-backed inspection, focused regressions and full QC.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/a_axonemal_microtubule.yaml | context_only | Corrected native bytes reread against exact predecessor findings and surrounding source-backed claims. |
| rules | docs/CURATION.md | context_only | Current corrected input reread against the predecessor and inspected authorities; hierarchy guidance now distinguishes filament is-a from framework parthood. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000147,GO:0001534,GO:0005737,GO:0005826,GO:0005856,GO:0005879,GO:0005885,GO:0005938,GO:0015629,GO:0030479,GO:0030864,GO:0036156,GO:0036157,GO:0061645,GO:0097545,GO:0097649,GO:0097650,GO:0099079,GO:0099513,GO:0110165,GO:0160111,GO:0160113,GO:0160114; Current native definitions, synonyms, obsolescence flags and typed child relationships | supports | Exact native GO identities and roles checked. Reverse child lists confirm is-a versus part_of; untyped ancestor reachability alone is not treated as an is-a assertion. |
| taxa | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1423%2C284812%2C3055%2C4896%2C4932%2C559292; Top-level requested NCBI Taxon entries | supports | The six requested taxa and reference-strain names resolve. Taxonomy is not evidence of structure prevalence. |
| adapter | /private/tmp/csm-review-20261011T070221Z/adapter.log | context_only | Live 28-dataset inventory: no matching yeast or Chlamydomonas dataset. Bacillus searches are described separately; noncoverage is not negative biology. |
| ma | DOI:10.1016/j.cell.2019.09.030; Results, Figures 1 and 6 captions, network/junction sections and strain/sample Methods | supports | Chlamydomonas isolated doublets have the complete A tubule and partial B tubule, inner and outer junctions, MIP networks and A-tubule attachments. Coarse current graph is supported without claiming all molecular positions or unprocessed in-situ imaging. |
| nicastro | DOI:10.1126/science.1128618; Primary abstract only | supports | Cryoelectron tomography of Chlamydomonas and sea-urchin axonemes establishes architecture and internal doublet densities; no finer claim relies solely on this abstract. |
| original | git:1ebfb77f:data/structures/cytoskeleton/a_axonemal_microtubule.yaml | context_only | Original discussion inspected via git show; later inner-sheath commit replaced its rationale. |
| predecessor | reviews/structured/20261011T071241Z-a_axonemal_microtubule-audit/review.yaml | context_only | Immutable original observation committed before mutation. |
| preservation | /private/tmp/csm-review-20261011T070221Z/preservation.json | supports | Exactly four native records changed; 905 others and every previous history, canonical review and legacy report remain byte-identical. |
| embeddings | /private/tmp/csm-review-20261011T070221Z/embedding-refresh.json | supports | Only the ring role prose changes the semantic projection. Its pinned-model vector was refreshed; 908 vectors are unchanged. |
| initial-qc | /private/tmp/csm-review-20261011T070221Z/release-qc-command.json | supports | Initial full QC failed one website-label test (835 passed, 3 skipped). New external GO targets required a scoped reference-catalog addition; the final QC supersedes this failed attempt. |
| website-labels | /private/tmp/csm-review-20261011T070221Z/website-reference-fix.json | supports | Added three verified OLS GO source labels and retained their exact response bodies/checksums, preserving every previous catalog reference and source. The declared rebuild list and regression cover all three additions. |

## Limits And Additional Notes

- Same-agent assessment; no independent or human sign-off and no promotion of PROPOSED.
- Europe PMC fullTextXML failed for several sources; official PMC full HTML supplied the readable fallback. Access tiers are specified per source below.
- Nicastro 2006 was inspected at primary-abstract level; GO and Ma 2019 full text provide the coarse claim support. Fine MIP composition remains an acknowledged TODO, not a defect.
- Original access tiers are retained; no new primary experiments, raw-data reanalysis or independent approval are implied. Post-change resolver skips and label pairs without adapters are not certified.
- All six scientific/provenance regressions failed on original records. Initial full QC then exposed a missing website relationship label; a seventh regression failed before the scoped catalog fix. The final 36-test focused/guarded-writer/website suite passes. The failed QC receipt is retained as evidence, not overwritten.
- Disposition inputs are retained by review-base/cytoskeleton-evidence-20261011-r2 after the website-reference integration fix. Final PR and native merge-group results are verified separately.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T074246Z-a_axonemal_microtubule-disposition
kind: record
repository: CultureBotAI/CellStructureMech
title: 'A axonemal microtubule: finding dispositions'
started_at: '2026-10-11T07:31:35Z'
finished_at: '2026-10-11T07:42:46Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent evidence reassessment and adversarial diff inspection,
    not independent human approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Exact predecessor findings resolved; original evidence-access tiers and biological
  uncertainties retained. No scientific status promotion.
source:
  git_revision: 7b2a10264b5217ea5be79569b2355f2dbdc4424c
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
  - path: data/structures/cytoskeleton/a_axonemal_microtubule.yaml
    sha256: ce35e4855b506178485b229b515c89a717ddee0a5a9d26fff88ba991fac5b06b
    role: target
  - path: data/structures/cytoskeleton/actin_body.yaml
    sha256: b0abd6f5cb40fec99ab2d5a23a56b7307041f4ac8eda2a32b9db8d57680f22ea
    role: context
  - path: data/structures/cytoskeleton/actin_cortical_patch.yaml
    sha256: 4f089bd321dd3aaf0b6ae169a0f411b48f292efd94cc5bda6c514c47ee093d67
    role: context
  - path: data/structures/cytoskeleton/actomyosin_contractile_ring.yaml
    sha256: 28a3e7b12391a9d3a16eb453974d6e0ed5ab92b925092e395e88f64fa6fe5ab0
    role: context
  - path: data/structures/cytoskeleton/alfa_filament.yaml
    sha256: 546afa4d749c9fe7dd056d62aad7f25d8fcd11b44565974e233abe8b47287bc4
    role: context
  - path: data/structures/cytoskeleton/axonemal_a_tubule_inner_sheath.yaml
    sha256: 23bcdab335f1f6b6f39da802471c2336ab47ed2083b4986133b9558f42d4f7c0
    role: context
  - path: data/structures/cytoskeleton/axonemal_doublet_microtubule.yaml
    sha256: 6a44e0a145c3ba58c9649ca75093614cd97001a451021dc2becf8c170824b270
    role: context
  - path: data/structures/cytoskeleton/axonemal_microtubule.yaml
    sha256: 480cd29d1f2e87c07c19dd8d60e50768cdcce29223b28ce2df1d4c956dc46282
    role: context
  - path: data/website/references.json
    sha256: c927b0e3450345f1cedf484bf3c5901b1ef246418cb65b5ae307f709cdae6cae
    role: context
  - path: docs/CURATION.md
    sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
    role: context
  - path: docs/SCHEMA.md
    sha256: 07b8f936a553a45cc6e8dba924c21e6af48c81b3866725efeb00c8183f0c75a2
    role: context
  - path: docs/WEBSITE_REFERENCES.md
    sha256: 4630510ad5ce5152204fd101dd3f41ca20a32f3e954f23906a165a4f05fa83ca
    role: context
  - path: docs/record-review-profile.md
    sha256: 6a49c8d35f0a94082a9ad0b8bd8c6a929d85de8339141955f3779bd7ab0eb7e4
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/records/a_axonemal_microtubule/2026-09-23T171258Z-claude-code-e68e55.yaml
    sha256: f1649edbe615d3e9edc180628b02c89411cfa544196076629840578f2ae41f0a
    role: context
  - path: history/records/a_axonemal_microtubule/2026-09-23T172416Z-claude-code-55b697.yaml
    sha256: cf039672ef5471c092ab9483845d733edc1d52d2a623f428d080c7826c18db31
    role: context
  - path: history/records/a_axonemal_microtubule/2026-09-23T181240Z-claude-code-cdd7da.yaml
    sha256: d62229e60036d4a79c05fe92259e9bab47a00cc7d9fc3566493f50ec225a65d3
    role: context
  - path: history/records/a_axonemal_microtubule/2026-10-11T071417Z-codex-ac456b.yaml
    sha256: 2ec88ad633cf68c4d37d5d5fe84763150c3663511914a71041ff5bd2b070c25a
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reports/website_reference_sources/20261011-cytoskeleton/go-0030864.json
    sha256: 9db30bf8c07fd4c3b343d8a1c6f320d1186a9b854dae296a6f606297baa560ac
    role: context
  - path: reports/website_reference_sources/20261011-cytoskeleton/go-0061645.json
    sha256: 16e20065f9b08c55b577c91692bb6c852d8bf92c187828db621cafab690a0c00
    role: context
  - path: reports/website_reference_sources/20261011-cytoskeleton/go-0099513.json
    sha256: 89187d136f3c3754e51f50d21064fa345ba71105af505853d6484be1a553165f
    role: context
  - path: reviews/structured/20261011T071241Z-a_axonemal_microtubule-audit/review.yaml
    sha256: ca141a2a562d013be835294b517a018a257eed053888a28bfe1255179ca29234
    role: context
  - path: scripts/build_website_references.py
    sha256: 58d3f40f6c22962916fd114e0eee3b8fae1ce9d05f1bd028e00f56d3c5eb4973
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: tests/test_cytoskeleton_evidence_review.py
    sha256: f41626b355d49deb8b3e358af6f240c44ef28ecf3f0ed0f910acdee7bd68120d
    role: context
  - path: tests/test_website_audit.py
    sha256: 87350de86ced60895216ab7e78388bfc1a917a901024e33c45c6c27c9a4476ae
    role: context
targets:
- target_id: GO:0097649
  path: data/structures/cytoskeleton/a_axonemal_microtubule.yaml
  label: A axonemal microtubule
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/a_axonemal_microtubule.yaml
    role: maintained scientific record
scope:
  description: Exact predecessor findings, corrected fields and preservation of surrounding
    claims; not a repeated whole-record scientific review.
  selection: 20261011T071241Z-a_axonemal_microtubule-audit
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - GO:0097649
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - GO:0097649
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/a_axonemal_microtubule.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Empty quotation checks and resolver
    skips are not scientific proof.
  scope_note: 2026-10-11T07:14:57Z to 2026-10-11T07:15:00Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - GO:0097649
  command: .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/a_axonemal_microtubule.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Empty quotation checks and resolver
    skips are not scientific proof.
  scope_note: 2026-10-11T07:15:00Z to 2026-10-11T07:15:05Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - GO:0097649
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/cytoskeleton/a_axonemal_microtubule.yaml
    --report /private/tmp/csm-review-20261011T070221Z/a_axonemal_microtubule-post-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Empty quotation checks and resolver
    skips are not scientific proof.
  scope_note: 2026-10-11T07:15:05Z to 2026-10-11T07:15:36Z; log SHA-256 ecd0efc8a56a310b96762f36b527925f72a30e7945c22e9cb19b4442726aca15
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:0097649
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Empty quotation checks and resolver
    skips are not scientific proof.
  scope_note: 2026-10-11T07:17:40Z to 2026-10-11T07:18:03Z; log SHA-256 43df0083dc52abe9dcf42ffb28027516bf341d2f07b59a1fef83be3ad7095c99
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - GO:0097649
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: "id↔label correspondence summary:\n          OK_CANONICAL: 3544\n     \
    \       OK_SYNONYM: 50\n          OK_EXCEPTION: 6\n    SKIPPED_NO_ADAPTER: 603\n\
    \n✅ All id↔label pairs correspond."
  scope_note: 2026-10-11T07:18:03Z to 2026-10-11T07:20:08Z; log SHA-256 d423103555a6a5b538a7c811a73a29c24ed0e5a2eae00d1bb94715295f23f7cb
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - GO:0097649
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Empty quotation checks and resolver
    skips are not scientific proof.
  scope_note: 2026-10-11T07:20:08Z to 2026-10-11T07:20:33Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - GO:0097649
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: "resolver control: every resolver accepts a known id and rejects a fabricated\
    \ one\nresolving 1 DOI identifier(s)...\nresolving 2 GO identifier(s)...\n\nidentifier\
    \ liveness summary:\n  OK             4014\n  SKIPPED         251\n\nEvery identifier\
    \ resolves at its issuing authority."
  scope_note: 2026-10-11T07:20:33Z to 2026-10-11T07:21:26Z; log SHA-256 50e90c5e078fa1a80bc98cbcf63406c48835855a34569abb5fa8367b605a10fb
- check_id: regressions
  name: regressions
  status: passed
  required: true
  target_ids:
  - GO:0097649
  command: .venv/bin/python -m pytest -q tests/test_cytoskeleton_evidence_review.py
    tests/test_write_validated.py
  exit_code: 0
  expected_exit_code: 0
  summary: '..............................                                           [100%]

    30 passed in 41.06s'
  scope_note: 2026-10-11T07:21:26Z to 2026-10-11T07:22:08Z; log SHA-256 eee409a9ff5e8aea0c93184f64a23f06f11ca564d09e8d6f7f8dccfce218177a
- check_id: reviews
  name: reviews
  status: passed
  required: true
  target_ids:
  - GO:0097649
  command: .venv/bin/python scripts/record_review.py check --base d9cea09379282886022064c57c012efe0db3beaf
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Empty quotation checks and resolver
    skips are not scientific proof.
  scope_note: 2026-10-11T07:22:08Z to 2026-10-11T07:22:58Z; log SHA-256 66cc7b44151eb9d7ab3d0a63c5bf146c2180025929640e06c6a11b4e61bcda45
- check_id: diff
  name: diff
  status: passed
  required: true
  target_ids:
  - GO:0097649
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Empty quotation checks and resolver
    skips are not scientific proof.
  scope_note: 2026-10-11T07:22:58Z to 2026-10-11T07:22:58Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- check_id: website-focused
  name: website-focused
  status: passed
  required: true
  target_ids:
  - GO:0097649
  command: .venv/bin/python -m pytest -q tests/test_cytoskeleton_evidence_review.py
    tests/test_write_validated.py tests/test_website_audit.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Empty quotation checks and resolver
    skips are not scientific proof.
  scope_note: 2026-10-11T07:30:30Z to 2026-10-11T07:31:16Z; log SHA-256 8bf7d26f3470b6750a036f9fbd30b42775c0702e35e55cd4c1b8f02cb9911706
- check_id: release-qc2
  name: release-qc2
  status: passed
  required: true
  target_ids:
  - GO:0097649
  command: .venv/bin/python scripts/run_qc.py
  exit_code: 0
  expected_exit_code: 0
  summary: Authoritative full local QC passed, including tests, all-record schema/history,
    generated products and contract checks. Remote PR and merge-group checks remain
    separate publication gates.
  scope_note: 2026-10-11T07:31:34Z to 2026-10-11T07:42:35Z; log SHA-256 98a3036efdb29edc42c613dc0e46ce11261f0a4f509f07406b0db78bece55ee4
- check_id: initial-qc-superseded
  name: Initial QC before website-reference integration fix
  status: failed
  required: false
  target_ids:
  - GO:0097649
  command: .venv/bin/python scripts/run_qc.py
  exit_code: 1
  expected_exit_code: 0
  summary: 'Historical failed attempt: one missing external GO website-label assertion,
    835 passed and 3 skipped. The catalog, retained sources and rebuild list were
    corrected; release-qc2 is the final required passing gate.'
  scope_note: Superseded candidate 027cbb55ab63bc21417ee964617fc8edc2c85ca0; 2026-10-11T07:16:54Z
    to 2026-10-11T07:28:34Z; log SHA-256 9c517a6729ccdc107e20eef7432b990f7f3d89abab59200eadbcd2057c23c975
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/a_axonemal_microtubule.yaml
  accessed_at: '2026-10-11T07:42:46Z'
  snapshot_sha256: ce35e4855b506178485b229b515c89a717ddee0a5a9d26fff88ba991fac5b06b
  support: context_only
  summary: Corrected native bytes reread against exact predecessor findings and surrounding
    source-backed claims.
- evidence_id: rules
  kind: record_content
  reference: docs/CURATION.md
  accessed_at: '2026-10-11T07:42:46Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  support: context_only
  summary: Current corrected input reread against the predecessor and inspected authorities;
    hierarchy guidance now distinguishes filament is-a from framework parthood.
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000147,GO:0001534,GO:0005737,GO:0005826,GO:0005856,GO:0005879,GO:0005885,GO:0005938,GO:0015629,GO:0030479,GO:0030864,GO:0036156,GO:0036157,GO:0061645,GO:0097545,GO:0097649,GO:0097650,GO:0099079,GO:0099513,GO:0110165,GO:0160111,GO:0160113,GO:0160114
  locator: Current native definitions, synonyms, obsolescence flags and typed child
    relationships
  accessed_at: '2026-10-11T07:04:57Z'
  snapshot_sha256: 71f14150527ed018024bb5682b4d3b88750c50919ca386ca9bac5766e8df4480
  support: supports
  summary: Exact native GO identities and roles checked. Reverse child lists confirm
    is-a versus part_of; untyped ancestor reachability alone is not treated as an
    is-a assertion.
- evidence_id: taxa
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1423%2C284812%2C3055%2C4896%2C4932%2C559292
  locator: Top-level requested NCBI Taxon entries
  accessed_at: '2026-10-11T07:05:02Z'
  snapshot_sha256: 785915aef9110dcf4728409ac02274f8c858aba27b08779ae5e3b0d2c5a37108
  support: supports
  summary: The six requested taxa and reference-strain names resolve. Taxonomy is
    not evidence of structure prevalence.
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/csm-review-20261011T070221Z/adapter.log
  accessed_at: '2026-10-11T07:12:41Z'
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
  support: context_only
  summary: 'Live 28-dataset inventory: no matching yeast or Chlamydomonas dataset.
    Bacillus searches are described separately; noncoverage is not negative biology.'
- evidence_id: ma
  kind: primary_source
  reference: DOI:10.1016/j.cell.2019.09.030
  locator: Results, Figures 1 and 6 captions, network/junction sections and strain/sample
    Methods
  accessed_at: '2026-10-11T07:05:01Z'
  snapshot_sha256: da58fc1d507070c2a51f1a87287cf2210df6616a0cd05e933b37e9ee081d580c
  support: supports
  summary: Chlamydomonas isolated doublets have the complete A tubule and partial
    B tubule, inner and outer junctions, MIP networks and A-tubule attachments. Coarse
    current graph is supported without claiming all molecular positions or unprocessed
    in-situ imaging.
- evidence_id: nicastro
  kind: primary_source
  reference: DOI:10.1126/science.1128618
  locator: Primary abstract only
  accessed_at: '2026-10-11T07:03:44Z'
  snapshot_sha256: dc5a628f1cfe67da937413ea897415a623f29682c4fcc83f9a7540d564467a27
  support: supports
  summary: Cryoelectron tomography of Chlamydomonas and sea-urchin axonemes establishes
    architecture and internal doublet densities; no finer claim relies solely on this
    abstract.
- evidence_id: original
  kind: record_content
  reference: git:1ebfb77f:data/structures/cytoskeleton/a_axonemal_microtubule.yaml
  accessed_at: '2026-10-11T07:12:41Z'
  snapshot_sha256: 2275b63b64ca99958fac185dc313de99055d16ab515bb6a27039847f5fc4df3b
  support: context_only
  summary: Original discussion inspected via git show; later inner-sheath commit replaced
    its rationale.
- evidence_id: predecessor
  kind: prior_review
  reference: reviews/structured/20261011T071241Z-a_axonemal_microtubule-audit/review.yaml
  accessed_at: '2026-10-11T07:42:46Z'
  snapshot_sha256: ca141a2a562d013be835294b517a018a257eed053888a28bfe1255179ca29234
  support: context_only
  summary: Immutable original observation committed before mutation.
- evidence_id: preservation
  kind: validation
  reference: /private/tmp/csm-review-20261011T070221Z/preservation.json
  accessed_at: '2026-10-11T07:42:46Z'
  snapshot_sha256: a8380b5cd1ad915ceb45ab1209a052728fb829c9b9a5795aa0caab6cf628d09f
  support: supports
  summary: Exactly four native records changed; 905 others and every previous history,
    canonical review and legacy report remain byte-identical.
- evidence_id: embeddings
  kind: validation
  reference: /private/tmp/csm-review-20261011T070221Z/embedding-refresh.json
  accessed_at: '2026-10-11T07:42:46Z'
  snapshot_sha256: a0724280c8297248e06d86cc721000f9aec28383b8a764dd398784170079d031
  support: supports
  summary: Only the ring role prose changes the semantic projection. Its pinned-model
    vector was refreshed; 908 vectors are unchanged.
- evidence_id: initial-qc
  kind: validation
  reference: /private/tmp/csm-review-20261011T070221Z/release-qc-command.json
  accessed_at: '2026-10-11T07:42:46Z'
  snapshot_sha256: ea3e136d333665286973ed46dc9dd1f9b19f5360e6649a4de95da7ecbd480cec
  support: supports
  summary: Initial full QC failed one website-label test (835 passed, 3 skipped).
    New external GO targets required a scoped reference-catalog addition; the final
    QC supersedes this failed attempt.
- evidence_id: website-labels
  kind: validation
  reference: /private/tmp/csm-review-20261011T070221Z/website-reference-fix.json
  accessed_at: '2026-10-11T07:42:46Z'
  snapshot_sha256: d83f8b7e28d7b9b6f0d25ac26dbf3b6afc0ead54c589ac12ccba3d296f5f7457
  support: supports
  summary: Added three verified OLS GO source labels and retained their exact response
    bodies/checksums, preserving every previous catalog reference and source. The
    declared rebuild list and regression cover all three additions.
assessments:
- assessment_id: resolved-f1
  area: provenance
  topic: Restore the original A-tubule discussion rationale
  outcome: supported
  target_ids:
  - GO:0097649
  evidence_ids:
  - original
  - record
  - rules
  - predecessor
  - preservation
  summary: The exact original rationale is restored as the prefix, followed by the
    complete later inner-sheath explanation with a dated reassessment marker. Original
    posed date, narrowed prompt, OPEN status, child and attachment graph are retained.
findings:
- finding_id: F1
  issue_key: a-tubule-original-rationale-preservation
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  title: Restore the original A-tubule discussion rationale
  description: The exact original rationale is restored as the prefix, followed by
    the complete later inner-sheath explanation with a dated reassessment marker.
    Original posed date, narrowed prompt, OPEN status, child and attachment graph
    are retained.
  target_ids:
  - GO:0097649
  field_paths:
  - discussions[0].rationale
  evidence_ids:
  - original
  - record
  - rules
  - predecessor
  - preservation
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/a_axonemal_microtubule.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: minor
  normalization_reason: Bounded bibliographic or append-only provenance defect; biological
    identity remains valid.
  disposition_reason: The exact original rationale is restored as the prefix, followed
    by the complete later inner-sheath explanation with a dated reassessment marker.
    Original posed date, narrowed prompt, OPEN status, child and attachment graph
    are retained. Verified with source-backed inspection, focused regressions and
    full QC.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261011T071241Z-a_axonemal_microtubule-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2187
actions: []
limitations:
- Same-agent assessment; no independent or human sign-off and no promotion of PROPOSED.
- Europe PMC fullTextXML failed for several sources; official PMC full HTML supplied
  the readable fallback. Access tiers are specified per source below.
- Nicastro 2006 was inspected at primary-abstract level; GO and Ma 2019 full text
  provide the coarse claim support. Fine MIP composition remains an acknowledged TODO,
  not a defect.
- Original access tiers are retained; no new primary experiments, raw-data reanalysis
  or independent approval are implied. Post-change resolver skips and label pairs
  without adapters are not certified.
- All six scientific/provenance regressions failed on original records. Initial full
  QC then exposed a missing website relationship label; a seventh regression failed
  before the scoped catalog fix. The final 36-test focused/guarded-writer/website
  suite passes. The failed QC receipt is retained as evidence, not overwritten.
- Disposition inputs are retained by review-base/cytoskeleton-evidence-20261011-r2
  after the website-reference integration fix. Final PR and native merge-group results
  are verified separately.
links:
- https://github.com/CultureBotAI/CellStructureMech/issues/2187
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261011T071241Z-a_axonemal_microtubule-audit
  relationship: Resolves exact predecessor findings without rewriting their original
    observations.
```
