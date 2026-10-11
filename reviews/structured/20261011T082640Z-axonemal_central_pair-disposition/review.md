# Axonemal central pair: finding disposition

- Review: 20261011T082640Z-axonemal_central_pair-disposition
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T08:14:04Z
- Finished UTC: 2026-10-11T08:26:40Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The exact predecessor finding is resolved in native source attribution or retained discussion provenance. Original evidence-access tiers, upstream conflicts and open biological questions remain explicit. No scientific status promotion.

## Scope And Provenance

Exact predecessor finding, corrected fields and preservation of surrounding claims; not a repeated whole-record scientific review.

Selection: 20261011T080734Z-axonemal_central_pair-audit
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base fc89d38db53c64447f134b82201710456ff93a0e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0097540 | data/structures/cytoskeleton/axonemal_central_pair.yaml | maintained | axonemal central pair |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0097540 | Actual post-curation command passed. Empty quotation checks and resolver skips are not scientific proof. |
| strict | passed | True | GO:0097540 | Actual post-curation command passed. Empty quotation checks and resolver skips are not scientific proof. |
| snippets | passed | True | GO:0097540 | Actual post-curation command passed. Empty quotation checks and resolver skips are not scientific proof. |
| history | passed | True | GO:0097540 | Actual post-curation command passed. Empty quotation checks and resolver skips are not scientific proof. |
| labels | passed | True | GO:0097540 | id↔label correspondence summary:<br>          OK_CANONICAL: 3544<br>            OK_SYNONYM: 50<br>          OK_EXCEPTION: 6<br>    SKIPPED_NO_ADAPTER: 603<br><br>✅ All id↔label pairs correspond. |
| traits | passed | True | GO:0097540 | Actual post-curation command passed. Empty quotation checks and resolver skips are not scientific proof. |
| curies | passed | True | GO:0097540 | resolver control: every resolver accepts a known id and rejects a fabricated one<br><br>identifier liveness summary:<br>  OK             4014<br>  SKIPPED         251<br><br>Every identifier resolves at its issuing authority. |
| regressions | passed | True | GO:0097540 | ...............................                                          [100%]<br>31 passed in 40.28s |
| reviews | passed | True | GO:0097540 | Actual post-curation command passed. Empty quotation checks and resolver skips are not scientific proof. |
| diff | passed | True | GO:0097540 | Actual post-curation command passed. Empty quotation checks and resolver skips are not scientific proof. |
| focused | passed | True | GO:0097540 | 27 tests passed: three new provenance/source-conflict regressions and 24 guarded-writer tests. All three new regressions failed on the original native inputs. |
| release-qc3 | passed | True | GO:0097540 | Authoritative full local QC passed, including all-record tests, schema/history, generated products and contract checks. Remote PR and native merge-group checks remain separate publication gates. |
| QC attempt before final test line wrapping | failed | False | GO:0097540 | This attempt stopped at E501 long-line errors in new regression assertions. Final line wrapping changes no test semantics; release-qc3 is the required complete passing rerun. |
| QC attempt before final test line wrapping | failed | False | GO:0097540 | This attempt stopped at E501 long-line errors in new regression assertions. Final line wrapping changes no test semantics; release-qc3 is the required complete passing rerun. |

## Scientific And Domain Assessments

### Restore the central-pair child-record discussion as retained provenance

provenance: supported. Targets: GO:0097540.

The deleted discussion is restored with its original identity, author, posed date and rationale, plus the intermediate narrowing. Only creation of the two existing C1/C2 child records is marked RESOLVED, dated to the actual restoration. The resolution explicitly hands off molecular-boundary work to the two existing OPEN child discussions; no completion of that science is implied.

## Findings

### F1: Restore the central-pair child-record discussion as retained provenance

minor / resolved / confirmed; issue key: central-pair-deleted-child-discussion.

The deleted discussion is restored with its original identity, author, posed date and rationale, plus the intermediate narrowing. Only creation of the two existing C1/C2 child records is marked RESOLVED, dated to the actual restoration. The resolution explicitly hands off molecular-boundary work to the two existing OPEN child discussions; no completion of that science is implied.

Disposition: The deleted discussion is restored with its original identity, author, posed date and rationale, plus the intermediate narrowing. Only creation of the two existing C1/C2 child records is marked RESOLVED, dated to the actual restoration. The resolution explicitly hands off molecular-boundary work to the two existing OPEN child discussions; no completion of that science is implied. Verified by source-backed inspection, focused regressions and full QC.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/axonemal_central_pair.yaml | context_only | Corrected native bytes reread against the exact predecessor, inspected authorities and committed discussion history; surrounding graph, hierarchy and open scientific tasks retained. |
| rules | docs/CURATION.md | context_only | Claim-specific source support and append-only discussion rationale; discussions are provenance, not disposable task text. |
| history | /private/tmp/csm-review-20261011T075940Z/axonemal_central_pair-discussion-history.json | context_only | All Git revisions touching this target parsed; complete historical discussion objects inspected with their revision identities. |
| prior-review-search | /private/tmp/csm-review-20261011T075940Z/exact-target-predecessors.json | context_only | Gitignore-independent recursive structured-review scan found no exact-target predecessor. Similar referenced GO terms are not target reviews. |
| context | /private/tmp/csm-review-20261011T075940Z/context-read.log | context_only | Both history surfaces and earlier issue corrections were inspected. Historical actor metadata was preserved rather than reattributed. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005930,GO:0097540,GO:0097649,GO:0097650,GO:0160110,GO:0160111,GO:0160112,GO:1990716,GO:1990717,GO:1990718,GO:1990719,GO:1990720; Twelve exact cellular-component identities, definitions, synonyms, obsolescence flags and typed child relations | supports | Current GO supports the structure identities and coarse central-apparatus boundaries. Typed relations, not untyped ancestor reachability, establish parthood. |
| taxa | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=3055; Requested top-level NCBITaxon:3055 | supports | Current taxonomy resolves Chlamydomonas reinhardtii; species authority does not prove prevalence. |
| adapter | /private/tmp/csm-review-20261011T075940Z/adapter.log | context_only | The live 28-dataset iModulonDB inventory has no Chlamydomonas dataset. Adapter coverage is not negative biological evidence. |
| carbajal | DOI:10.1002/cm.21094; Primary Methods, Table I, Results on C1/C2/projections and bridge connectivity, Figure 5 caption, bridge Discussion | supports | Chlamydomonas central singlets and their bridge/projections were resolved in isolated axonemes. The bridge has a 16-nm repeat and the C1/C2 pair is asymmetric; detailed component assignments are not inferred from generic densities. |
| child-c1 | data/structures/cytoskeleton/c1_axonemal_microtubule.yaml | context_only | Exact child exists; its component and named-projection boundaries remain in an OPEN child discussion. |
| child-c2 | data/structures/cytoskeleton/c2_axonemal_microtubule.yaml | context_only | Exact child exists; wall, MIP and projection boundaries remain in an OPEN child discussion. |
| discussion-search | /private/tmp/csm-review-20261011T075940Z/discussion-search.log | context_only | Ignored-inclusive search across data, history, reviews and reports confirms both former central-pair discussion IDs are absent from current maintained content. |
| predecessor | reviews/structured/20261011T080734Z-axonemal_central_pair-audit/review.yaml | context_only | Immutable original observation committed before native mutation. |
| preservation | /private/tmp/csm-review-20261011T075940Z/preservation.json | supports | Exactly three native records changed; 906 others and every previous history, canonical review and legacy report remain byte-identical. |
| embeddings | /private/tmp/csm-review-20261011T075940Z/embedding-preservation.json | supports | All 909 semantic inputs and cached vectors remain unchanged; only source notes, discussions and history changed. |
| focused-tests | /private/tmp/csm-review-20261011T075940Z/focused-command.json | supports | All 27 focused and guarded-writer tests passed after correction. |
| red-tests | /private/tmp/csm-review-20261011T075940Z/regressions-red-command.json | supports | The new tests failed against the original records, establishing that they detect each observed defect. |

## Limits And Additional Notes

- Same-agent scientific review, not independent human sign-off; no promotion of native status.
- No raw-image, reconstruction-map, movie or experimental-data reanalysis. Structure-level evidence is not a complete protein-family or stoichiometric inventory.
- Europe PMC XML access failed for the two full-text papers; official PMC HTML was inspected instead. Nicastro full-text context was recovered from author-uploaded browser-readable text after a PDF mirror timeout. Direct AmiGO fetch was forbidden; browser-readable AmiGO and current EBI APIs supplied the ontology cross-check.
- GO has source discrepancies: B-inner-sheath typed A-tubule parthood and central-pair definition doublets wording. These do not justify replacing primary-supported B-lumen containment or C1/C2 singlets with incorrect biology.
- Original source-access tiers are retained; no new primary experiments, raw-data reanalysis or independent approval are implied. Post-change resolver skips and label pairs without adapters are not certified.
- Three regressions failed on the original records; all 27 focused and guarded-writer tests pass after correction. The upstream GO B-sheath relationship discrepancy and existing molecular-boundary tasks remain unresolved where relevant.
- Exact disposition inputs are retained by review-base/axonemal-provenance-20261011. Final PR and separate native merge-group checks are publication gates verified outside this observation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T082640Z-axonemal_central_pair-disposition
kind: record
repository: CultureBotAI/CellStructureMech
title: 'Axonemal central pair: finding disposition'
started_at: '2026-10-11T08:14:04Z'
finished_at: '2026-10-11T08:26:40Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent reassessment of corrected inputs and adversarial
    diff inspection, not independent human approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The exact predecessor finding is resolved in native source attribution or
  retained discussion provenance. Original evidence-access tiers, upstream conflicts
  and open biological questions remain explicit. No scientific status promotion.
source:
  git_revision: fc89d38db53c64447f134b82201710456ff93a0e
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
  - path: data/structures/cytoskeleton/axonemal_a_tubule_inner_sheath.yaml
    sha256: 23bcdab335f1f6b6f39da802471c2336ab47ed2083b4986133b9558f42d4f7c0
    role: context
  - path: data/structures/cytoskeleton/axonemal_b_tubule_inner_sheath.yaml
    sha256: d1b0e481219c8b248e22e069aaa333074857a9ef8cae74d159e9a9e1f33a733e
    role: context
  - path: data/structures/cytoskeleton/axonemal_central_apparatus.yaml
    sha256: 74e419f358ba3717a764cd93cb5c0e4e892c7015094ed6457518994526ee1899
    role: context
  - path: data/structures/cytoskeleton/axonemal_central_bridge.yaml
    sha256: 37f3fa4c739ac1a6ce6225225cffe4340895d8412fafea8d65a62770ad8bbaea
    role: context
  - path: data/structures/cytoskeleton/axonemal_central_pair.yaml
    sha256: 5e6d9301edf395d718469728f33d6fd7aad90d01bea8bf84b31ba6a742e7cf75
    role: target
  - path: data/structures/cytoskeleton/c1_axonemal_microtubule.yaml
    sha256: 2f4f420d4958d3133a60a7b072e517361d7c2c4908acb4e307bd2033095f18f4
    role: context
  - path: data/structures/cytoskeleton/c2_axonemal_microtubule.yaml
    sha256: 97c8666ddef318d146a2d902a225f8b0313468bcf54fa32d81d5f1d127798a44
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
  - path: history/records/axonemal_central_pair/2026-09-23T155109Z-codex-8b4d6e.yaml
    sha256: 7a8acdcd53b8bd2e5ea8d514425f8cb425b0a4d9e3036008fd8bbb41001616b8
    role: context
  - path: history/records/axonemal_central_pair/2026-09-23T160107Z-codex-3b56f6.yaml
    sha256: f9d60593db693d8b26ba74513845fe9f4db76fcff274f5d79af3a18d362bf80a
    role: context
  - path: history/records/axonemal_central_pair/2026-10-11T080955Z-codex-f508ef.yaml
    sha256: 693a32a5248eba21f6462744e43597f7de1b96a80fa0d04a64883c40482383d8
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reviews/structured/20261011T080734Z-axonemal_central_pair-audit/review.yaml
    sha256: ce700b3e6cdf5c833a7a1eb2e510a33350adc00706f40fff1d397b82cf4159cf
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: tests/test_axonemal_provenance_review.py
    sha256: 749a7a86bc61f6d2d42a815d2d8d71d4b4682e12a5a7c676f0637e90a30d1e15
    role: context
targets:
- target_id: GO:0097540
  path: data/structures/cytoskeleton/axonemal_central_pair.yaml
  label: axonemal central pair
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/axonemal_central_pair.yaml
    role: maintained scientific record
scope:
  description: Exact predecessor finding, corrected fields and preservation of surrounding
    claims; not a repeated whole-record scientific review.
  selection: 20261011T080734Z-axonemal_central_pair-audit
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - GO:0097540
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - GO:0097540
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/axonemal_central_pair.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Empty quotation checks and resolver
    skips are not scientific proof.
  scope_note: 2026-10-11T08:11:20Z to 2026-10-11T08:11:23Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - GO:0097540
  command: .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/axonemal_central_pair.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Empty quotation checks and resolver
    skips are not scientific proof.
  scope_note: 2026-10-11T08:11:23Z to 2026-10-11T08:11:28Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - GO:0097540
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/cytoskeleton/axonemal_central_pair.yaml
    --report /private/tmp/csm-review-20261011T075940Z/axonemal_central_pair-post-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Empty quotation checks and resolver
    skips are not scientific proof.
  scope_note: 2026-10-11T08:11:28Z to 2026-10-11T08:11:56Z; log SHA-256 19539338e3ec8ee46e88fd4402d57b05571ffa76495c7c8af6d9dcde78df854e
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:0097540
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Empty quotation checks and resolver
    skips are not scientific proof.
  scope_note: 2026-10-11T08:11:56Z to 2026-10-11T08:12:14Z; log SHA-256 a334cb99b68bf9bff7dc6f7cbf42e376c52117e8773d42811c4f87cdf4e017da
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - GO:0097540
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: "id↔label correspondence summary:\n          OK_CANONICAL: 3544\n     \
    \       OK_SYNONYM: 50\n          OK_EXCEPTION: 6\n    SKIPPED_NO_ADAPTER: 603\n\
    \n✅ All id↔label pairs correspond."
  scope_note: 2026-10-11T08:12:14Z to 2026-10-11T08:13:45Z; log SHA-256 d423103555a6a5b538a7c811a73a29c24ed0e5a2eae00d1bb94715295f23f7cb
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - GO:0097540
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Empty quotation checks and resolver
    skips are not scientific proof.
  scope_note: 2026-10-11T08:13:45Z to 2026-10-11T08:14:17Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - GO:0097540
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: "resolver control: every resolver accepts a known id and rejects a fabricated\
    \ one\n\nidentifier liveness summary:\n  OK             4014\n  SKIPPED      \
    \   251\n\nEvery identifier resolves at its issuing authority."
  scope_note: 2026-10-11T08:14:17Z to 2026-10-11T08:15:30Z; log SHA-256 ee1c5f2e78a2d29fcb6781a8ecd722934376595042d2cc261b4465b361d19b79
- check_id: regressions
  name: regressions
  status: passed
  required: true
  target_ids:
  - GO:0097540
  command: .venv/bin/python -m pytest -q tests/test_cytoskeleton_evidence_review.py
    tests/test_write_validated.py
  exit_code: 0
  expected_exit_code: 0
  summary: '...............................                                          [100%]

    31 passed in 40.28s'
  scope_note: 2026-10-11T08:15:30Z to 2026-10-11T08:16:12Z; log SHA-256 5192d11a4e174ef47199ca758dc9a489757dab437582385c30c7dea78db3141c
- check_id: reviews
  name: reviews
  status: passed
  required: true
  target_ids:
  - GO:0097540
  command: .venv/bin/python scripts/record_review.py check --base 79fb219ee1c89ae5f9f03e12b7629f28e7bd2e0d
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Empty quotation checks and resolver
    skips are not scientific proof.
  scope_note: 2026-10-11T08:16:12Z to 2026-10-11T08:17:10Z; log SHA-256 a26a9986c7d231d4cfd83d4f80704b6e0268ad988f2d32dd137287dc294a063c
- check_id: diff
  name: diff
  status: passed
  required: true
  target_ids:
  - GO:0097540
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Empty quotation checks and resolver
    skips are not scientific proof.
  scope_note: 2026-10-11T08:17:10Z to 2026-10-11T08:17:11Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- check_id: focused
  name: focused
  status: passed
  required: true
  target_ids:
  - GO:0097540
  command: .venv/bin/python -m pytest -q tests/test_axonemal_provenance_review.py
    tests/test_write_validated.py
  exit_code: 0
  expected_exit_code: 0
  summary: '27 tests passed: three new provenance/source-conflict regressions and
    24 guarded-writer tests. All three new regressions failed on the original native
    inputs.'
  scope_note: 2026-10-11T08:09:59Z to 2026-10-11T08:10:44Z; log SHA-256 7779ca7227b7a47917795d926ae9b5b8fd7af9525af8e37797bb0c08888e59bf
- check_id: release-qc3
  name: release-qc3
  status: passed
  required: true
  target_ids:
  - GO:0097540
  command: .venv/bin/python scripts/run_qc.py
  exit_code: 0
  expected_exit_code: 0
  summary: Authoritative full local QC passed, including all-record tests, schema/history,
    generated products and contract checks. Remote PR and native merge-group checks
    remain separate publication gates.
  scope_note: 2026-10-11T08:13:12Z to 2026-10-11T08:26:24Z; log SHA-256 7e6c1d5b63369aee031c6bd9274b1311115edc30dd7fefd9bfc90f9f53d690a9
- check_id: release-qc-superseded
  name: QC attempt before final test line wrapping
  status: failed
  required: false
  target_ids:
  - GO:0097540
  command: .venv/bin/python scripts/run_qc.py
  exit_code: 1
  expected_exit_code: 0
  summary: This attempt stopped at E501 long-line errors in new regression assertions.
    Final line wrapping changes no test semantics; release-qc3 is the required complete
    passing rerun.
  scope_note: 2026-10-11T08:11:34Z to 2026-10-11T08:11:35Z; log SHA-256 f85cdd922603d6c6bbe3f9de54c62c34fb41d0e6d8905096ebbf879a310b5fa8
- check_id: release-qc2-superseded
  name: QC attempt before final test line wrapping
  status: failed
  required: false
  target_ids:
  - GO:0097540
  command: .venv/bin/python scripts/run_qc.py
  exit_code: 1
  expected_exit_code: 0
  summary: This attempt stopped at E501 long-line errors in new regression assertions.
    Final line wrapping changes no test semantics; release-qc3 is the required complete
    passing rerun.
  scope_note: 2026-10-11T08:12:54Z to 2026-10-11T08:12:54Z; log SHA-256 6412b6e3f8e0b2d8dcbb2fabb97315b54f7d52a9189ab632387bb22cd49285aa
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/axonemal_central_pair.yaml
  accessed_at: '2026-10-11T08:26:40Z'
  snapshot_sha256: 5e6d9301edf395d718469728f33d6fd7aad90d01bea8bf84b31ba6a742e7cf75
  support: context_only
  summary: Corrected native bytes reread against the exact predecessor, inspected
    authorities and committed discussion history; surrounding graph, hierarchy and
    open scientific tasks retained.
- evidence_id: rules
  kind: record_content
  reference: docs/CURATION.md
  accessed_at: '2026-10-11T08:07:34Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  support: context_only
  summary: Claim-specific source support and append-only discussion rationale; discussions
    are provenance, not disposable task text.
- evidence_id: history
  kind: record_content
  reference: /private/tmp/csm-review-20261011T075940Z/axonemal_central_pair-discussion-history.json
  accessed_at: '2026-10-11T08:07:34Z'
  snapshot_sha256: 5433c4080f8354efd28b29bfad1c547f0e59b6245e1d8d128057ee7b6051d147
  support: context_only
  summary: All Git revisions touching this target parsed; complete historical discussion
    objects inspected with their revision identities.
- evidence_id: prior-review-search
  kind: validation
  reference: /private/tmp/csm-review-20261011T075940Z/exact-target-predecessors.json
  accessed_at: '2026-10-11T08:07:34Z'
  snapshot_sha256: 855e7ae24216379497f503c8517f580fb48c0d941b58f243e80bcb5feae304ba
  support: context_only
  summary: Gitignore-independent recursive structured-review scan found no exact-target
    predecessor. Similar referenced GO terms are not target reviews.
- evidence_id: context
  kind: validation
  reference: /private/tmp/csm-review-20261011T075940Z/context-read.log
  accessed_at: '2026-10-11T08:07:34Z'
  snapshot_sha256: b1fcdc28aac89ea8fe5cae27d8b239851c139f0c29b149cd0970145e92ba436a
  support: context_only
  summary: Both history surfaces and earlier issue corrections were inspected. Historical
    actor metadata was preserved rather than reattributed.
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005930,GO:0097540,GO:0097649,GO:0097650,GO:0160110,GO:0160111,GO:0160112,GO:1990716,GO:1990717,GO:1990718,GO:1990719,GO:1990720
  locator: Twelve exact cellular-component identities, definitions, synonyms, obsolescence
    flags and typed child relations
  accessed_at: '2026-10-11T08:00:19Z'
  snapshot_sha256: da1b50524ef9c2d1138352b75f67d918abc5c69977196864f5ef3cc42255482d
  support: supports
  summary: Current GO supports the structure identities and coarse central-apparatus
    boundaries. Typed relations, not untyped ancestor reachability, establish parthood.
- evidence_id: taxa
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=3055
  locator: Requested top-level NCBITaxon:3055
  accessed_at: '2026-10-11T08:00:23Z'
  snapshot_sha256: a17bc1c97fea9112288574ef15727ed7e37c42787a430ef074ae5fc654547e6b
  support: supports
  summary: Current taxonomy resolves Chlamydomonas reinhardtii; species authority
    does not prove prevalence.
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/csm-review-20261011T075940Z/adapter.log
  accessed_at: '2026-10-11T08:07:34Z'
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
  support: context_only
  summary: The live 28-dataset iModulonDB inventory has no Chlamydomonas dataset.
    Adapter coverage is not negative biological evidence.
- evidence_id: carbajal
  kind: primary_source
  reference: DOI:10.1002/cm.21094
  locator: Primary Methods, Table I, Results on C1/C2/projections and bridge connectivity,
    Figure 5 caption, bridge Discussion
  accessed_at: '2026-10-11T08:00:28Z'
  snapshot_sha256: 14454453521710f50b818d71f76a0e9704716b8feaf252701a45a61d97a99d1b
  support: supports
  summary: Chlamydomonas central singlets and their bridge/projections were resolved
    in isolated axonemes. The bridge has a 16-nm repeat and the C1/C2 pair is asymmetric;
    detailed component assignments are not inferred from generic densities.
- evidence_id: child-c1
  kind: record_content
  reference: data/structures/cytoskeleton/c1_axonemal_microtubule.yaml
  accessed_at: '2026-10-11T08:07:34Z'
  snapshot_sha256: 2f4f420d4958d3133a60a7b072e517361d7c2c4908acb4e307bd2033095f18f4
  support: context_only
  summary: Exact child exists; its component and named-projection boundaries remain
    in an OPEN child discussion.
- evidence_id: child-c2
  kind: record_content
  reference: data/structures/cytoskeleton/c2_axonemal_microtubule.yaml
  accessed_at: '2026-10-11T08:07:34Z'
  snapshot_sha256: 97c8666ddef318d146a2d902a225f8b0313468bcf54fa32d81d5f1d127798a44
  support: context_only
  summary: Exact child exists; wall, MIP and projection boundaries remain in an OPEN
    child discussion.
- evidence_id: discussion-search
  kind: validation
  reference: /private/tmp/csm-review-20261011T075940Z/discussion-search.log
  accessed_at: '2026-10-11T08:07:34Z'
  snapshot_sha256: debe0c063a07c1c7d4ce44655a72efeaf557aab411c127309075d7bc16960dbd
  support: context_only
  summary: Ignored-inclusive search across data, history, reviews and reports confirms
    both former central-pair discussion IDs are absent from current maintained content.
- evidence_id: predecessor
  kind: prior_review
  reference: reviews/structured/20261011T080734Z-axonemal_central_pair-audit/review.yaml
  accessed_at: '2026-10-11T08:26:40Z'
  snapshot_sha256: ce700b3e6cdf5c833a7a1eb2e510a33350adc00706f40fff1d397b82cf4159cf
  support: context_only
  summary: Immutable original observation committed before native mutation.
- evidence_id: preservation
  kind: validation
  reference: /private/tmp/csm-review-20261011T075940Z/preservation.json
  accessed_at: '2026-10-11T08:26:40Z'
  snapshot_sha256: 63419e4d4cb174d69a424efa9b2012cd7080a35c46225eff4369ef6a025e8625
  support: supports
  summary: Exactly three native records changed; 906 others and every previous history,
    canonical review and legacy report remain byte-identical.
- evidence_id: embeddings
  kind: validation
  reference: /private/tmp/csm-review-20261011T075940Z/embedding-preservation.json
  accessed_at: '2026-10-11T08:26:40Z'
  snapshot_sha256: 9eae4ffc9b26a107f80d6f1f4f4eb1bea1e1179e5b24fd85529977cfabfb60d9
  support: supports
  summary: All 909 semantic inputs and cached vectors remain unchanged; only source
    notes, discussions and history changed.
- evidence_id: focused-tests
  kind: validation
  reference: /private/tmp/csm-review-20261011T075940Z/focused-command.json
  accessed_at: '2026-10-11T08:26:40Z'
  snapshot_sha256: a373c07a0a38100fc91382b56bdecbd23ba63b21563b0ac524758dcd23b98bd3
  support: supports
  summary: All 27 focused and guarded-writer tests passed after correction.
- evidence_id: red-tests
  kind: validation
  reference: /private/tmp/csm-review-20261011T075940Z/regressions-red-command.json
  accessed_at: '2026-10-11T08:26:40Z'
  snapshot_sha256: 2db316745513678a54723a518c4ee2a992bc2b9f1d71af78c08307b3ea7c1d1e
  support: supports
  summary: The new tests failed against the original records, establishing that they
    detect each observed defect.
assessments:
- assessment_id: resolved-f1
  area: provenance
  topic: Restore the central-pair child-record discussion as retained provenance
  outcome: supported
  target_ids:
  - GO:0097540
  evidence_ids:
  - record
  - history
  - discussion-search
  - child-c1
  - child-c2
  - rules
  - predecessor
  - preservation
  - focused-tests
  summary: The deleted discussion is restored with its original identity, author,
    posed date and rationale, plus the intermediate narrowing. Only creation of the
    two existing C1/C2 child records is marked RESOLVED, dated to the actual restoration.
    The resolution explicitly hands off molecular-boundary work to the two existing
    OPEN child discussions; no completion of that science is implied.
findings:
- finding_id: F1
  issue_key: central-pair-deleted-child-discussion
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  title: Restore the central-pair child-record discussion as retained provenance
  description: The deleted discussion is restored with its original identity, author,
    posed date and rationale, plus the intermediate narrowing. Only creation of the
    two existing C1/C2 child records is marked RESOLVED, dated to the actual restoration.
    The resolution explicitly hands off molecular-boundary work to the two existing
    OPEN child discussions; no completion of that science is implied.
  target_ids:
  - GO:0097540
  field_paths:
  - discussions
  evidence_ids:
  - record
  - history
  - discussion-search
  - child-c1
  - child-c2
  - rules
  - predecessor
  - preservation
  - focused-tests
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/axonemal_central_pair.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: minor
  normalization_reason: A bounded source-attribution or discussion-provenance defect;
    the biological identity and structure boundaries remain supported.
  disposition_reason: The deleted discussion is restored with its original identity,
    author, posed date and rationale, plus the intermediate narrowing. Only creation
    of the two existing C1/C2 child records is marked RESOLVED, dated to the actual
    restoration. The resolution explicitly hands off molecular-boundary work to the
    two existing OPEN child discussions; no completion of that science is implied.
    Verified by source-backed inspection, focused regressions and full QC.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261011T080734Z-axonemal_central_pair-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2196
actions: []
limitations:
- Same-agent scientific review, not independent human sign-off; no promotion of native
  status.
- No raw-image, reconstruction-map, movie or experimental-data reanalysis. Structure-level
  evidence is not a complete protein-family or stoichiometric inventory.
- Europe PMC XML access failed for the two full-text papers; official PMC HTML was
  inspected instead. Nicastro full-text context was recovered from author-uploaded
  browser-readable text after a PDF mirror timeout. Direct AmiGO fetch was forbidden;
  browser-readable AmiGO and current EBI APIs supplied the ontology cross-check.
- 'GO has source discrepancies: B-inner-sheath typed A-tubule parthood and central-pair
  definition doublets wording. These do not justify replacing primary-supported B-lumen
  containment or C1/C2 singlets with incorrect biology.'
- Original source-access tiers are retained; no new primary experiments, raw-data
  reanalysis or independent approval are implied. Post-change resolver skips and label
  pairs without adapters are not certified.
- Three regressions failed on the original records; all 27 focused and guarded-writer
  tests pass after correction. The upstream GO B-sheath relationship discrepancy and
  existing molecular-boundary tasks remain unresolved where relevant.
- Exact disposition inputs are retained by review-base/axonemal-provenance-20261011.
  Final PR and separate native merge-group checks are publication gates verified outside
  this observation.
links:
- https://github.com/CultureBotAI/CellStructureMech/issues/2196
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261011T080734Z-axonemal_central_pair-audit
  relationship: Resolves the exact predecessor finding without rewriting the original
    observation.
```
