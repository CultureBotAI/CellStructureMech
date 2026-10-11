# Axonemal central pair: scientific record review

- Review: 20261011T080734Z-axonemal_central_pair-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T08:01:09Z
- Finished UTC: 2026-10-11T08:07:34Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Whole native record reviewed; a bounded provenance finding is saved before separately authorized curation.

## Scope And Provenance

Entire native record, each graph edge, identity/hierarchy, taxonomy, functions, composition scope, optional resources, discussions and both history surfaces.

Selection: One exact sequential target in the 909-record review goal. Adjacent records are context, not certified reviews.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 79fb219ee1c89ae5f9f03e12b7629f28e7bd2e0d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0097540 | data/structures/cytoskeleton/axonemal_central_pair.yaml | maintained | axonemal central pair |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0097540 | Passed deterministic check; not a substitute for scientific evidence assessment. |
| strict | passed | True | GO:0097540 | Passed deterministic check; not a substitute for scientific evidence assessment. |
| snippets | passed | True | GO:0097540 | No verbatim snippets are asserted; paraphrases were reviewed separately. |
| history | passed | True | GO:0097540 | Passed deterministic check; not a substitute for scientific evidence assessment. |
| labels | passed | True | GO:0097540 | id↔label correspondence summary:<br>          OK_CANONICAL: 3544<br>            OK_SYNONYM: 50<br>          OK_EXCEPTION: 6<br>    SKIPPED_NO_ADAPTER: 603<br><br>✅ All id↔label pairs correspond. |
| traits | passed | True | GO:0097540 | Passed deterministic check; not a substitute for scientific evidence assessment. |
| curies | passed | True | GO:0097540 | resolver control: every resolver accepts a known id and rejects a fabricated one<br><br>identifier liveness summary:<br>  OK             4014<br>  SKIPPED         251<br><br>Every identifier resolves at its issuing authority. |
| reviews | passed | True | GO:0097540 | Passed deterministic check; not a substitute for scientific evidence assessment. |
| diff | passed | True | GO:0097540 | Passed deterministic check; not a substitute for scientific evidence assessment. |
| Exact-baseline full CI QC | passed | True | GO:0097540 | Authoritative QC, including the review contract, passed on the exact captured input revision. Not a newly executed local full QC run. |

## Scientific And Domain Assessments

### Central singlet identity, synonyms, C1/C2 topology, function and six graph edges

evidence: supported. Targets: GO:0097540.

Primary evidence supports asymmetric singlets, rather than the erroneous doublets wording in the current GO definition. Exact GO identity and synonyms are otherwise valid. The graph retains explicit bridge endpoints, projection attachment and apparatus parthood without claiming unresolved component inventories.

### Deleted child-record discussion

provenance: concern. Targets: GO:0097540.

Adding both child records answered the split task but did not justify deleting the discussion or implying their finer component boundaries are complete.

### Optional resources and status boundaries

completeness: supported. Targets: GO:0097540.

No native image, quantitative physical-property measurement, dataset accession or protein accession requires separate verification. Historical status stays PROPOSED. Known omitted molecular details are acknowledged tasks, not invented review defects.

## Findings

### F1: Restore the central-pair child-record discussion as retained provenance

minor / open / confirmed; issue key: central-pair-deleted-child-discussion.

The original resolve_c1_c2_microtubule_children discussion was renamed/narrowed after C1 creation, then deleted in dbd02468 after C2 creation. The original rationale, posed date and handoff are absent. Existing history notes the removal but does not replace the native discussion lifecycle, whose RESOLVED state is explicitly retained for provenance.

## Recommended Actions And Acceptance Checks

### A1

Restore the central-pair child-record discussion as retained provenance

- Restore the original discussion identity, posed author/date, exact original rationale and intermediate rationale; retain historical narrowing context.
- Record a current dated resolution of the child-record split with explicit handoff of still-open component/projection tasks to the existing C1/C2 child discussions.
- Preserve all C1/C2 has_part links and every graph edge; do not reopen finished child creation or mark their unresolved molecular boundaries complete.
- Use the guarded writer, append Codex curation and EDIT history, preserve PROPOSED, prior history/reviews and unrelated records, regenerate pages, and pass focused regressions and native QC.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/axonemal_central_pair.yaml | context_only | Entire native YAML read. Exact input hashes captured before formal assessment; initial reading preceded capture. |
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

## Limits And Additional Notes

- Same-agent scientific review, not independent human sign-off; no promotion of native status.
- Full QC is verified on the exact baseline CI revision. Native scoped and global checks ran locally; skipped authority namespaces and label pairs are not certified.
- No raw-image, reconstruction-map, movie or experimental-data reanalysis. Structure-level evidence is not a complete protein-family or stoichiometric inventory.
- Europe PMC XML access failed for the two full-text papers; official PMC HTML was inspected instead. Nicastro full-text context was recovered from author-uploaded browser-readable text after a PDF mirror timeout. Direct AmiGO fetch was forbidden; browser-readable AmiGO and current EBI APIs supplied the ontology cross-check.
- GO has source discrepancies: B-inner-sheath typed A-tubule parthood and central-pair definition doublets wording. These do not justify replacing primary-supported B-lumen containment or C1/C2 singlets with incorrect biology.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T080734Z-axonemal_central_pair-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'Axonemal central pair: scientific record review'
started_at: '2026-10-11T08:01:09Z'
finished_at: '2026-10-11T08:07:34Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent source and record review, not independent human approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Whole native record reviewed; a bounded provenance finding is saved before
  separately authorized curation.
source:
  git_revision: 79fb219ee1c89ae5f9f03e12b7629f28e7bd2e0d
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
    sha256: a773a4aabeab7791de6fe9f1681490278a6bd9f390bb80968421289de35ddfa5
    role: context
  - path: data/structures/cytoskeleton/axonemal_central_apparatus.yaml
    sha256: ed28229657dadd657afe1628b8ed9266505b3294a742494e2f03ce9ca6848df8
    role: context
  - path: data/structures/cytoskeleton/axonemal_central_bridge.yaml
    sha256: 37f3fa4c739ac1a6ce6225225cffe4340895d8412fafea8d65a62770ad8bbaea
    role: context
  - path: data/structures/cytoskeleton/axonemal_central_pair.yaml
    sha256: c4df2fad59f33728b87b498e3934aae6ce638166ef2dfd9bb82bbfb424abad8e
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
- target_id: GO:0097540
  path: data/structures/cytoskeleton/axonemal_central_pair.yaml
  label: axonemal central pair
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/axonemal_central_pair.yaml
    role: maintained scientific record
scope:
  description: Entire native record, each graph edge, identity/hierarchy, taxonomy,
    functions, composition scope, optional resources, discussions and both history
    surfaces.
  selection: One exact sequential target in the 909-record review goal. Adjacent records
    are context, not certified reviews.
  coverage: full
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
  summary: Passed deterministic check; not a substitute for scientific evidence assessment.
  scope_note: 2026-10-11T08:02:51Z to 2026-10-11T08:02:54Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - GO:0097540
  command: .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/axonemal_central_pair.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Passed deterministic check; not a substitute for scientific evidence assessment.
  scope_note: 2026-10-11T08:02:54Z to 2026-10-11T08:02:58Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - GO:0097540
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/cytoskeleton/axonemal_central_pair.yaml
    --report /private/tmp/csm-review-20261011T075940Z/axonemal_central_pair-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: No verbatim snippets are asserted; paraphrases were reviewed separately.
  scope_note: 2026-10-11T08:02:58Z to 2026-10-11T08:03:23Z; log SHA-256 785078ce2bcf1768a1c53d29d9a373434d5679e0deb020f7e9d6b4131fd08e86
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:0097540
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Passed deterministic check; not a substitute for scientific evidence assessment.
  scope_note: 2026-10-11T08:03:23Z to 2026-10-11T08:03:38Z; log SHA-256 43df0083dc52abe9dcf42ffb28027516bf341d2f07b59a1fef83be3ad7095c99
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
  scope_note: 2026-10-11T08:03:38Z to 2026-10-11T08:05:02Z; log SHA-256 d423103555a6a5b538a7c811a73a29c24ed0e5a2eae00d1bb94715295f23f7cb
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - GO:0097540
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Passed deterministic check; not a substitute for scientific evidence assessment.
  scope_note: 2026-10-11T08:05:02Z to 2026-10-11T08:05:22Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
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
  scope_note: 2026-10-11T08:05:22Z to 2026-10-11T08:06:14Z; log SHA-256 ee1c5f2e78a2d29fcb6781a8ecd722934376595042d2cc261b4465b361d19b79
- check_id: reviews
  name: reviews
  status: passed
  required: true
  target_ids:
  - GO:0097540
  command: .venv/bin/python scripts/record_review.py check
  exit_code: 0
  expected_exit_code: 0
  summary: Passed deterministic check; not a substitute for scientific evidence assessment.
  scope_note: 2026-10-11T08:06:14Z to 2026-10-11T08:07:11Z; log SHA-256 7de34fba04d9014207be9a2a89eb289511744c57d15f5dae0bc69f3852a8f48b
- check_id: diff
  name: diff
  status: passed
  required: true
  target_ids:
  - GO:0097540
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  summary: Passed deterministic check; not a substitute for scientific evidence assessment.
  scope_note: 2026-10-11T08:07:11Z to 2026-10-11T08:07:11Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- check_id: qc
  name: Exact-baseline full CI QC
  status: passed
  required: true
  target_ids:
  - GO:0097540
  command: gh run view 38122790434 --repo CultureBotAI/CellStructureMech --log
  exit_code: 0
  expected_exit_code: 0
  summary: Authoritative QC, including the review contract, passed on the exact captured
    input revision. Not a newly executed local full QC run.
  scope_note: https://github.com/CultureBotAI/CellStructureMech/actions/runs/38122790434;
    log SHA-256 a9a6eab001ff8ef989b6365db140ff92be2219a853743c6a628f3d9ac8bfc714
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/axonemal_central_pair.yaml
  accessed_at: '2026-10-11T08:07:34Z'
  snapshot_sha256: c4df2fad59f33728b87b498e3934aae6ce638166ef2dfd9bb82bbfb424abad8e
  support: context_only
  summary: Entire native YAML read. Exact input hashes captured before formal assessment;
    initial reading preceded capture.
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
assessments:
- assessment_id: biology
  area: evidence
  topic: Central singlet identity, synonyms, C1/C2 topology, function and six graph
    edges
  outcome: supported
  target_ids:
  - GO:0097540
  evidence_ids:
  - record
  - go
  - taxa
  - carbajal
  summary: Primary evidence supports asymmetric singlets, rather than the erroneous
    doublets wording in the current GO definition. Exact GO identity and synonyms
    are otherwise valid. The graph retains explicit bridge endpoints, projection attachment
    and apparatus parthood without claiming unresolved component inventories.
- assessment_id: provenance
  area: provenance
  topic: Deleted child-record discussion
  outcome: concern
  target_ids:
  - GO:0097540
  evidence_ids:
  - history
  - discussion-search
  - child-c1
  - child-c2
  - rules
  summary: Adding both child records answered the split task but did not justify deleting
    the discussion or implying their finer component boundaries are complete.
- assessment_id: resources
  area: completeness
  topic: Optional resources and status boundaries
  outcome: supported
  target_ids:
  - GO:0097540
  evidence_ids:
  - record
  - rules
  - context
  summary: No native image, quantitative physical-property measurement, dataset accession
    or protein accession requires separate verification. Historical status stays PROPOSED.
    Known omitted molecular details are acknowledged tasks, not invented review defects.
findings:
- finding_id: F1
  issue_key: central-pair-deleted-child-discussion
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Restore the central-pair child-record discussion as retained provenance
  description: The original resolve_c1_c2_microtubule_children discussion was renamed/narrowed
    after C1 creation, then deleted in dbd02468 after C2 creation. The original rationale,
    posed date and handoff are absent. Existing history notes the removal but does
    not replace the native discussion lifecycle, whose RESOLVED state is explicitly
    retained for provenance.
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
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/axonemal_central_pair.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: minor
  normalization_reason: A bounded source-attribution or discussion-provenance defect;
    the biological identity and structure boundaries remain supported.
actions:
- action_id: A1
  description: Restore the central-pair child-record discussion as retained provenance
  finding_ids:
  - F1
  target_ids:
  - GO:0097540
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/axonemal_central_pair.yaml
    role: maintained scientific record
  acceptance_checks:
  - Restore the original discussion identity, posed author/date, exact original rationale
    and intermediate rationale; retain historical narrowing context.
  - Record a current dated resolution of the child-record split with explicit handoff
    of still-open component/projection tasks to the existing C1/C2 child discussions.
  - Preserve all C1/C2 has_part links and every graph edge; do not reopen finished
    child creation or mark their unresolved molecular boundaries complete.
  - Use the guarded writer, append Codex curation and EDIT history, preserve PROPOSED,
    prior history/reviews and unrelated records, regenerate pages, and pass focused
    regressions and native QC.
limitations:
- Same-agent scientific review, not independent human sign-off; no promotion of native
  status.
- Full QC is verified on the exact baseline CI revision. Native scoped and global
  checks ran locally; skipped authority namespaces and label pairs are not certified.
- No raw-image, reconstruction-map, movie or experimental-data reanalysis. Structure-level
  evidence is not a complete protein-family or stoichiometric inventory.
- Europe PMC XML access failed for the two full-text papers; official PMC HTML was
  inspected instead. Nicastro full-text context was recovered from author-uploaded
  browser-readable text after a PDF mirror timeout. Direct AmiGO fetch was forbidden;
  browser-readable AmiGO and current EBI APIs supplied the ontology cross-check.
- 'GO has source discrepancies: B-inner-sheath typed A-tubule parthood and central-pair
  definition doublets wording. These do not justify replacing primary-supported B-lumen
  containment or C1/C2 singlets with incorrect biology.'
```
