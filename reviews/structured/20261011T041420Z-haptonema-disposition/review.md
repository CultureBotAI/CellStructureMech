# Haptonema: finding disposition

- Review: 20261011T041420Z-haptonema-disposition
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T04:08:54Z
- Finished UTC: 2026-10-11T04:14:20Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The exact predecessor evidence finding is resolved; unresolved biological mechanisms are not claimed to be settled.

## Scope And Provenance

Exact predecessor finding, changed claim/evidence and append-only provenance; not a new whole-record review.

Selection: F1 in 20261011T040559Z-haptonema-audit
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 0de38b61d476d122c1d840698ce6e4e0b2eda0a4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:haptonema | data/structures/appendage/haptonema.yaml | maintained | haptonema |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | cellstructuremech:haptonema | Actual post-curation command passed. Empty quotation checks, resolver skips and unavailable controls do not establish scientific correctness; claim support and target authorities assessed separately. |
| strict | passed | True | cellstructuremech:haptonema | Actual post-curation command passed. Empty quotation checks, resolver skips and unavailable controls do not establish scientific correctness; claim support and target authorities assessed separately. |
| snippets | passed | True | cellstructuremech:haptonema | No quotations present: 0 of 16 citations carry a snippet. No quotation matching occurred; scientific paraphrases were assessed separately. |
| history | passed | True | cellstructuremech:haptonema | Actual post-curation command passed. Empty quotation checks, resolver skips and unavailable controls do not establish scientific correctness; claim support and target authorities assessed separately. |
| labels | passed | True | cellstructuremech:haptonema | Actual post-curation command passed. Empty quotation checks, resolver skips and unavailable controls do not establish scientific correctness; claim support and target authorities assessed separately. |
| traits | passed | True | cellstructuremech:haptonema | Actual post-curation command passed. Empty quotation checks, resolver skips and unavailable controls do not establish scientific correctness; claim support and target authorities assessed separately. |
| curies | passed | True | cellstructuremech:haptonema | All resolver positive/negative controls passed on this rerun; 4010 identifiers OK and 251 skipped. This includes the added Amador DOI; skipped namespaces are not certified. |
| regressions | passed | True | cellstructuremech:haptonema | 27 tests passed: the three targeted evidence-boundary regressions and the guarded-writer test suite. |
| reviews | passed | True | cellstructuremech:haptonema | Actual post-curation command passed. Empty quotation checks, resolver skips and unavailable controls do not establish scientific correctness; claim support and target authorities assessed separately. |
| diff | passed | True | cellstructuremech:haptonema | Actual post-curation command passed. Empty quotation checks, resolver skips and unavailable controls do not establish scientific correctness; claim support and target authorities assessed separately. |
| Exact-fix authoritative CI QC | passed | True | cellstructuremech:haptonema | Full authoritative QC passed on the exact inspected fix commit, including corpus tests and generated site/embedding checks. |

## Scientific And Domain Assessments

### Bound the taxol/calcium note to the measured shape response

evidence: supported. Targets: cellstructuremech:haptonema.

The evidence note now states taxol inhibition of rapid coiling and the calcium-induced right-helix-to-planar-bend response after calcium-free treatment. It explicitly distinguishes that observation from a direct influx measurement. The supported NONMECHANISTIC edge, other claims, prior discussions and PROPOSED status are unchanged.

## Findings

### F1: Bound the taxol/calcium note to the measured shape response

minor / resolved / confirmed; issue key: haptonema-calcium-influx-overstatement.

The evidence note now states taxol inhibition of rapid coiling and the calcium-induced right-helix-to-planar-bend response after calcium-free treatment. It explicitly distinguishes that observation from a direct influx measurement. The supported NONMECHANISTIC edge, other claims, prior discussions and PROPOSED status are unchanged.

Disposition: The evidence note now states taxol inhibition of rapid coiling and the calcium-induced right-helix-to-planar-bend response after calcium-free treatment. It explicitly distinguishes that observation from a direct influx measurement. The supported NONMECHANISTIC edge, other claims, prior discussions and PROPOSED status are unchanged. Verified against the original inspected primary sources, focused regressions, preservation assertions and exact-fix CI.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/haptonema.yaml; Entire native YAML and append-only histories | context_only | The evidence note now states taxol inhibition of rapid coiling and the calcium-induced right-helix-to-planar-bend response after calcium-free treatment. It explicitly distinguishes that observation from a direct influx measurement. The supported NONMECHANISTIC edge, other claims, prior discussions and PROPOSED status are unchanged. |
| prior-search | reviews/structured/ and reports/yaml_record_review/; haptonema and exact identifier | context_only | No earlier exact-target review finding found in these bounded roots. Prior issues #773 and #775 concern canonical-example citation and clade presence respectively, not these new findings. |
| nomura | DOI:10.1242/bio.036590; Introduction, Results including Fig. 6, Discussion and Materials and Methods | supports | NIES-4122 microtubule architecture and rapid coiling support the scaffold and calcium-dependent behavior. Taxol inhibited normal coiling; adding CaCl2 after calcium-free taxol treatment converted a right-handed helix to planar bending. The inspected assay measures shape response, not unchanged calcium influx. |
| taxon-clade | https://rest.uniprot.org/taxonomy/2830.json; Exact taxonomy identity | supports | Haptophyta identity matches the VARIABLE distribution row. |
| taxon-example | https://rest.uniprot.org/taxonomy/35142.json; Name and synonyms | supports | Haptolina hirta includes the historical Chrysochromulina hirta name used in the feeding study. |
| go-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=haptonema&amp;limit=100; Exact lexical query haptonema | context_only | No match in this bounded GO query; does not prove absence from every ontology. Native identity avoids substituting a broader microtubule term. |
| kawachi1991 | DOI:10.2216/i0031-8884-30-6-563.1; Author-uploaded primary abstract and figure captions on ResearchGate; not unavailable PDF preview | supports | Particles adhere to the C. hirta haptonema, aggregate and are delivered to the cell for phagocytosis. Supports capture and transport without assigning a molecular motor. |
| kawachi1995 | DOI:10.2216/i0031-8884-34-3-193.1; Author-uploaded primary abstract and figure captions on ResearchGate; body font encoding not reliably readable | supports | In C. spinifera spine scales capture particles and the haptonema delivers them. The native note only attributes a feeding role, not direct capture in this species. |
| andersen | DOI:10.3732/ajb.91.10.1508; Publisher review Introduction and flagellar-apparatus section; secondary synthesis | supports | Explicit secondary loss of haptonemata supports VARIABLE Haptophyta presence. This is review evidence, not a new experiment. |
| predecessor | reviews/structured/20261011T040559Z-haptonema-audit/review.yaml | context_only | Immutable pre-mutation finding, with exact F1 and stable-key lineage preserved. |
| preservation | /private/tmp/csm-review-20261011T035459Z/preservation.json | supports | Only haptonema and mastigoneme native records changed; the other 907 and all prior history/review/report bytes are preserved. |
| embeddings | /private/tmp/csm-review-20261011T035459Z/embedding-refresh.json | supports | Pinned-model regeneration changed only the mastigoneme semantic vector; 908 other embedding records remained identical. Derived map and neighbors were regenerated. |

## Limits And Additional Notes

- Nomura full main-text sections were inspected; supplemental movies or unseen assays are not claimed as reviewed. The finding is bounded to the inspected experiment.
- Kawachi papers were assessed from primary abstracts and captions on author-uploaded pages; publisher access was blocked and the 1995 body encoding was unreliable. Andersen is explicitly secondary synthesis.
- Same-agent assessment, not independent human sign-off or completion of the 909-record goal.
- No applicable iModulonDB dataset; this is not evidence of biological absence. No quotations were present to verify, so paraphrases required separate source inspection.
- This successor resolves only the exact prior finding, not all remaining biological uncertainty. Original source access tiers and snapshot times are preserved.
- Full QC is CI on the exact fix commit. Final review-only head and merge-group checks are separate publication gates. Resolver namespace skips and unavailable controls are not positive verification.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T041420Z-haptonema-disposition
kind: record
repository: CultureBotAI/CellStructureMech
title: 'Haptonema: finding disposition'
started_at: '2026-10-11T04:08:54Z'
finished_at: '2026-10-11T04:14:20Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent reassessment of the exact fix commit and adversarial
    diff inspection; not independent human approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The exact predecessor evidence finding is resolved; unresolved biological
  mechanisms are not claimed to be settled.
source:
  git_revision: 0de38b61d476d122c1d840698ce6e4e0b2eda0a4
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
  - path: data/structures/appendage/haptonema.yaml
    sha256: b2d4340d05ba2a5eb3309ba1c9ab7d656ab0a43b43a8e36f16b6eebc86b993e3
    role: target
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
  - path: history/records/haptonema/2026-09-13T104036Z-codex-e4306d.yaml
    sha256: 2c41a2651c993ed0b02bfd855fa518789f753a2d63fc17a8751994b4e52a94fd
    role: context
  - path: history/records/haptonema/2026-10-11T040641Z-codex-02b4a5.yaml
    sha256: 1a41bf39551387fab48d0fc6a8413f5c77261cc2b85eee3d5350755eaac3aecf
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reviews/structured/20261011T040559Z-haptonema-audit/review.yaml
    sha256: c9564d0eca03e39e3fc9cfcf384e464599de49da715c7387eeb42d70b9ed7a33
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: tests/test_appendage_evidence_review.py
    sha256: 651e4aa9d83431cdf509b9f5556a36cdb6d998cebdaa45336d02e06b927b3c51
    role: context
targets:
- target_id: cellstructuremech:haptonema
  path: data/structures/appendage/haptonema.yaml
  label: haptonema
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/haptonema.yaml
    role: maintained scientific record
scope:
  description: Exact predecessor finding, changed claim/evidence and append-only provenance;
    not a new whole-record review.
  selection: F1 in 20261011T040559Z-haptonema-audit
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:haptonema
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:haptonema
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/appendage/haptonema.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Empty quotation checks, resolver skips
    and unavailable controls do not establish scientific correctness; claim support
    and target authorities assessed separately.
  scope_note: 2026-10-11T04:06:54Z to 2026-10-11T04:06:58Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:haptonema
  command: .venv/bin/python scripts/validate_strict.py data/structures/appendage/haptonema.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Empty quotation checks, resolver skips
    and unavailable controls do not establish scientific correctness; claim support
    and target authorities assessed separately.
  scope_note: 2026-10-11T04:06:58Z to 2026-10-11T04:07:04Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - cellstructuremech:haptonema
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/appendage/haptonema.yaml
    --report /private/tmp/csm-review-20261011T035459Z/haptonema-post-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: 'No quotations present: 0 of 16 citations carry a snippet. No quotation
    matching occurred; scientific paraphrases were assessed separately.'
  scope_note: 2026-10-11T04:07:04Z to 2026-10-11T04:07:34Z; log SHA-256 76a62fd5ec31e6ba130825b4a29c72af0af9ccf523b06b12b351759481bf488c
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - cellstructuremech:haptonema
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Empty quotation checks, resolver skips
    and unavailable controls do not establish scientific correctness; claim support
    and target authorities assessed separately.
  scope_note: 2026-10-11T04:08:15Z to 2026-10-11T04:08:37Z; log SHA-256 1681e9bb52c501d5ad826d30ec6540fee542dcf71d98302d7a1b47ebde38f150
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - cellstructuremech:haptonema
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Empty quotation checks, resolver skips
    and unavailable controls do not establish scientific correctness; claim support
    and target authorities assessed separately.
  scope_note: 2026-10-11T04:08:37Z to 2026-10-11T04:10:24Z; log SHA-256 d423103555a6a5b538a7c811a73a29c24ed0e5a2eae00d1bb94715295f23f7cb
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - cellstructuremech:haptonema
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Empty quotation checks, resolver skips
    and unavailable controls do not establish scientific correctness; claim support
    and target authorities assessed separately.
  scope_note: 2026-10-11T04:10:24Z to 2026-10-11T04:10:49Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - cellstructuremech:haptonema
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: All resolver positive/negative controls passed on this rerun; 4010 identifiers
    OK and 251 skipped. This includes the added Amador DOI; skipped namespaces are
    not certified.
  scope_note: 2026-10-11T04:10:49Z to 2026-10-11T04:11:49Z; log SHA-256 3af0d37cc5343e69b09927707d77aaf28fff7efc5ab0269c7f614e76e80384c2
- check_id: regressions
  name: regressions
  status: passed
  required: true
  target_ids:
  - cellstructuremech:haptonema
  command: .venv/bin/python -m pytest -q tests/test_appendage_evidence_review.py tests/test_write_validated.py
  exit_code: 0
  expected_exit_code: 0
  summary: '27 tests passed: the three targeted evidence-boundary regressions and
    the guarded-writer test suite.'
  scope_note: 2026-10-11T04:11:49Z to 2026-10-11T04:12:37Z; log SHA-256 b381cdec8d1cd302489092ca64605a1c379dd82650c39fdd00f6277c381e8ef8
- check_id: reviews
  name: reviews
  status: passed
  required: true
  target_ids:
  - cellstructuremech:haptonema
  command: .venv/bin/python scripts/record_review.py check --base 7dc2dbb326ca4e7c2f6d8e9cc24859dd3afdbc23
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Empty quotation checks, resolver skips
    and unavailable controls do not establish scientific correctness; claim support
    and target authorities assessed separately.
  scope_note: 2026-10-11T04:12:37Z to 2026-10-11T04:13:36Z; log SHA-256 5c590b541f02777c8b0077e3b5a13cc5cbe12919aa28a246a2827587f270e5b9
- check_id: diff
  name: diff
  status: passed
  required: true
  target_ids:
  - cellstructuremech:haptonema
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Empty quotation checks, resolver skips
    and unavailable controls do not establish scientific correctness; claim support
    and target authorities assessed separately.
  scope_note: 2026-10-11T04:13:36Z to 2026-10-11T04:13:36Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- check_id: qc
  name: Exact-fix authoritative CI QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:haptonema
  command: gh run view 38110671225 --json databaseId,status,conclusion,headSha,event,jobs,startedAt,updatedAt,url;
    gh run view 38110671225 --log
  exit_code: 0
  expected_exit_code: 0
  summary: Full authoritative QC passed on the exact inspected fix commit, including
    corpus tests and generated site/embedding checks.
  scope_note: 2026-10-11T04:09:48Z to 2026-10-11T04:14:00Z; https://github.com/CultureBotAI/CellStructureMech/actions/runs/38110671225;
    log SHA-256 3a31320371f9a6b35f9e8f2f71c5fd58a9c1a93f5b6c34c68354d0256719e272
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/appendage/haptonema.yaml
  locator: Entire native YAML and append-only histories
  accessed_at: '2026-10-11T04:14:20Z'
  snapshot_sha256: b2d4340d05ba2a5eb3309ba1c9ab7d656ab0a43b43a8e36f16b6eebc86b993e3
  support: context_only
  summary: The evidence note now states taxol inhibition of rapid coiling and the
    calcium-induced right-helix-to-planar-bend response after calcium-free treatment.
    It explicitly distinguishes that observation from a direct influx measurement.
    The supported NONMECHANISTIC edge, other claims, prior discussions and PROPOSED
    status are unchanged.
- evidence_id: prior-search
  kind: search
  reference: reviews/structured/ and reports/yaml_record_review/
  locator: haptonema and exact identifier
  accessed_at: '2026-10-11T04:05:59Z'
  support: context_only
  search_scope: rg --no-ignore --hidden in both review roots and the exact history
    directory included ignored files. GitHub all-state search for mastigoneme OR haptonema
    returned three earlier distinct, closed issues.
  summary: 'No earlier exact-target review finding found in these bounded roots. Prior
    issues #773 and #775 concern canonical-example citation and clade presence respectively,
    not these new findings.'
- evidence_id: nomura
  kind: primary_source
  reference: DOI:10.1242/bio.036590
  locator: Introduction, Results including Fig. 6, Discussion and Materials and Methods
  accessed_at: '2026-10-11T03:57:07Z'
  snapshot_sha256: b01fa9e239c67f2e3130906f6b144243dcdf63ae2b3f7fd3d36099c7b0fe1559
  support: supports
  summary: NIES-4122 microtubule architecture and rapid coiling support the scaffold
    and calcium-dependent behavior. Taxol inhibited normal coiling; adding CaCl2 after
    calcium-free taxol treatment converted a right-handed helix to planar bending.
    The inspected assay measures shape response, not unchanged calcium influx.
- evidence_id: taxon-clade
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/2830.json
  locator: Exact taxonomy identity
  accessed_at: '2026-10-11T03:57:22Z'
  snapshot_sha256: 5c1967ec75f6ec3db677bb2f29619d984b218e777dadfa53ca0af5ffda543e66
  support: supports
  summary: Haptophyta identity matches the VARIABLE distribution row.
- evidence_id: taxon-example
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/35142.json
  locator: Name and synonyms
  accessed_at: '2026-10-11T03:57:23Z'
  snapshot_sha256: e51f95793844c6030c1454334ec2780bbe3b7782578d0bf1d33815d4dd176a99
  support: supports
  summary: Haptolina hirta includes the historical Chrysochromulina hirta name used
    in the feeding study.
- evidence_id: go-search
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=haptonema&limit=100
  locator: Exact lexical query haptonema
  accessed_at: '2026-10-11T03:57:20Z'
  snapshot_sha256: f3a7dae9b1e9335291e3940cdf0e5f8dadf9335da7b9547710606b5106c63f86
  support: context_only
  summary: No match in this bounded GO query; does not prove absence from every ontology.
    Native identity avoids substituting a broader microtubule term.
  search_scope: Exact lexical query haptonema; only the recorded QuickGO service query,
    not an exhaustive ontology or repository absence search.
- evidence_id: kawachi1991
  kind: primary_source
  reference: DOI:10.2216/i0031-8884-30-6-563.1
  locator: Author-uploaded primary abstract and figure captions on ResearchGate; not
    unavailable PDF preview
  accessed_at: '2026-10-11T04:05:59Z'
  support: supports
  summary: Particles adhere to the C. hirta haptonema, aggregate and are delivered
    to the cell for phagocytosis. Supports capture and transport without assigning
    a molecular motor.
- evidence_id: kawachi1995
  kind: primary_source
  reference: DOI:10.2216/i0031-8884-34-3-193.1
  locator: Author-uploaded primary abstract and figure captions on ResearchGate; body
    font encoding not reliably readable
  accessed_at: '2026-10-11T04:05:59Z'
  support: supports
  summary: In C. spinifera spine scales capture particles and the haptonema delivers
    them. The native note only attributes a feeding role, not direct capture in this
    species.
- evidence_id: andersen
  kind: primary_source
  reference: DOI:10.3732/ajb.91.10.1508
  locator: Publisher review Introduction and flagellar-apparatus section; secondary
    synthesis
  accessed_at: '2026-10-11T04:05:59Z'
  support: supports
  summary: Explicit secondary loss of haptonemata supports VARIABLE Haptophyta presence.
    This is review evidence, not a new experiment.
- evidence_id: predecessor
  kind: prior_review
  reference: reviews/structured/20261011T040559Z-haptonema-audit/review.yaml
  accessed_at: '2026-10-11T04:14:20Z'
  snapshot_sha256: c9564d0eca03e39e3fc9cfcf384e464599de49da715c7387eeb42d70b9ed7a33
  support: context_only
  summary: Immutable pre-mutation finding, with exact F1 and stable-key lineage preserved.
- evidence_id: preservation
  kind: validation
  reference: /private/tmp/csm-review-20261011T035459Z/preservation.json
  accessed_at: '2026-10-11T04:08:07Z'
  snapshot_sha256: 811516e3467cb183ec94aad29391e5a34769d7e2cf3233365da7f0c25b327809
  support: supports
  summary: Only haptonema and mastigoneme native records changed; the other 907 and
    all prior history/review/report bytes are preserved.
- evidence_id: embeddings
  kind: validation
  reference: /private/tmp/csm-review-20261011T035459Z/embedding-refresh.json
  accessed_at: '2026-10-11T04:14:20Z'
  snapshot_sha256: dbdc194f210274a19e3bb6cc2d29290117a725e81013190511cdd9d6e3627f70
  support: supports
  summary: Pinned-model regeneration changed only the mastigoneme semantic vector;
    908 other embedding records remained identical. Derived map and neighbors were
    regenerated.
assessments:
- assessment_id: resolved-f1
  area: evidence
  topic: Bound the taxol/calcium note to the measured shape response
  outcome: supported
  target_ids:
  - cellstructuremech:haptonema
  evidence_ids:
  - record
  - nomura
  - predecessor
  - preservation
  summary: The evidence note now states taxol inhibition of rapid coiling and the
    calcium-induced right-helix-to-planar-bend response after calcium-free treatment.
    It explicitly distinguishes that observation from a direct influx measurement.
    The supported NONMECHANISTIC edge, other claims, prior discussions and PROPOSED
    status are unchanged.
findings:
- finding_id: F1
  issue_key: haptonema-calcium-influx-overstatement
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: Bound the taxol/calcium note to the measured shape response
  description: The evidence note now states taxol inhibition of rapid coiling and
    the calcium-induced right-helix-to-planar-bend response after calcium-free treatment.
    It explicitly distinguishes that observation from a direct influx measurement.
    The supported NONMECHANISTIC edge, other claims, prior discussions and PROPOSED
    status are unchanged.
  target_ids:
  - cellstructuremech:haptonema
  field_paths:
  - causal_graphs[0].edges[1].evidence[0].notes
  evidence_ids:
  - record
  - nomura
  - predecessor
  - preservation
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/haptonema.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: minor
  normalization_reason: Bounded experimental-detail overstatement; the supported coarse
    edge remains valid.
  disposition_reason: The evidence note now states taxol inhibition of rapid coiling
    and the calcium-induced right-helix-to-planar-bend response after calcium-free
    treatment. It explicitly distinguishes that observation from a direct influx measurement.
    The supported NONMECHANISTIC edge, other claims, prior discussions and PROPOSED
    status are unchanged. Verified against the original inspected primary sources,
    focused regressions, preservation assertions and exact-fix CI.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261011T040559Z-haptonema-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2168
actions: []
limitations:
- Nomura full main-text sections were inspected; supplemental movies or unseen assays
  are not claimed as reviewed. The finding is bounded to the inspected experiment.
- Kawachi papers were assessed from primary abstracts and captions on author-uploaded
  pages; publisher access was blocked and the 1995 body encoding was unreliable. Andersen
  is explicitly secondary synthesis.
- Same-agent assessment, not independent human sign-off or completion of the 909-record
  goal.
- No applicable iModulonDB dataset; this is not evidence of biological absence. No
  quotations were present to verify, so paraphrases required separate source inspection.
- This successor resolves only the exact prior finding, not all remaining biological
  uncertainty. Original source access tiers and snapshot times are preserved.
- Full QC is CI on the exact fix commit. Final review-only head and merge-group checks
  are separate publication gates. Resolver namespace skips and unavailable controls
  are not positive verification.
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261011T040559Z-haptonema-audit
  relationship: Resolves F1 without rewriting the original observation.
links:
- https://github.com/CultureBotAI/CellStructureMech/issues/2168
```
