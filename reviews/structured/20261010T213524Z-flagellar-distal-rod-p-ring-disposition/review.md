# bacterial-type flagellum basal body, distal rod, P ring: finding dispositions

- Review: 20261010T213524Z-flagellar-distal-rod-p-ring-disposition
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-10T21:29:56Z
- Finished UTC: 2026-10-10T21:35:24Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Reassessed and resolved 1 exact findings after guarded curation. Unchanged fields retain the predecessor assessment and source-access limits; PROPOSED is retained.

## Scope And Provenance

Post-curation reassessment at committed source revision 4c68079e4d2a15d27acc3f24b65b68cd828a0652, with full native YAML re-read. Every input byte matches the initial post-curation capture. Unchanged fields retain the exact predecessor assessment and limitations; not a new corpus-wide audit.

Selection: Reassess all findings from exact predecessor 20261010T212149Z-flagellar-distal-rod-p-ring-audit for target GO:0009428.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 4c68079e4d2a15d27acc3f24b65b68cd828a0652.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0009428 | data/structures/appendage/bacterial_type_flagellum_basal_body_distal_rod_p_ring.yaml | maintained | bacterial-type flagellum basal body, distal rod, P ring |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| embeddings after curation | passed | True | GO:0009428 | Fresh post-curation command passed. Deterministic checks do not establish scientific truth. |
| render after curation | passed | True | GO:0009428 | Fresh post-curation command passed. Deterministic checks do not establish scientific truth. |
| focused-tests after curation | passed | True | GO:0009428 | Fresh post-curation command passed. Deterministic checks do not establish scientific truth. |
| history after curation | passed | True | GO:0009428 | Fresh post-curation command passed. Deterministic checks do not establish scientific truth. |
| labels after curation | passed | True | GO:0009428 | Fresh post-curation command passed. Deterministic checks do not establish scientific truth. |
| traits after curation | passed | True | GO:0009428 | Fresh post-curation command passed. Deterministic checks do not establish scientific truth. |
| curies after curation | passed | True | GO:0009428 | Fresh post-curation command passed. Deterministic checks do not establish scientific truth. |
| schema after curation | passed | True | GO:0009428 | Fresh post-curation command passed. Deterministic checks do not establish scientific truth. |
| strict after curation | passed | True | GO:0009428 | Fresh post-curation command passed. Deterministic checks do not establish scientific truth. |
| qc-ci after curation | passed | True | GO:0009428 | Verified successful authoritative full QC in GitHub Actions run 38087712870 at exact source commit 4c68079e4d2a15d27acc3f24b65b68cd828a0652. All jobs and the authoritative quality-gate step succeeded; inspected input bytes match this commit. This is CI evidence, not a completed local full-QC claim. |
| whitespace after curation | passed | True | GO:0009428 | Fresh post-curation command passed. Deterministic checks do not establish scientific truth. |

## Scientific And Domain Assessments

### Structure identity, synonyms, hierarchy and parthood

identity: supported. Targets: GO:0009428.

Exact active GO cellular component denotes the named polymer/ring, not an individual protein. Native definitions and synonyms agree; rod segments belong to the rod and the rod/MS ring to the basal body.

### Every listed constituent, role, essentiality and protein example

evidence: supported. Targets: GO:0009428.

FlgI forms the P ring. IPR001782 and reviewed P15930/flgI match the declared component. ESSENTIAL refers to P-ring formation, not survival or motility of the enclosing cell.

### Constituent family scope

grounding: supported. Targets: GO:0009428.

Current exact constituent-family grounding is consistent with the native protein example and does not substitute a broader rod/hook family.

### All distribution rows and organism exemplars

scope: supported. Targets: GO:0009428.

VARIABLE is retained without LP-dependent exclusion. The Borrelia structural counterexample is bounded to the imaged organism; LP/peptidoglycan function text is explicitly Salmonella-scoped.

### Both functions, all graph nodes and every edge

graph: supported. Targets: GO:0009428.

Both functions and all six graph edges now explicitly retain Salmonella scope for LP-bushing and peptidoglycan-localization claims. The Borrelia counterexample is not assigned that model-specific physiology.

### Stoichiometry and physical properties

quantity: supported. Targets: GO:0009428.

The 26-FlgI count is explicitly Salmonella and agrees with the LP-ring reconstruction.

### Discussions, histories, status and omitted optional sections

provenance: supported. Targets: GO:0009428.

Preserved earlier histories and discussions. Authorized curation adds one native event and one append-only repository history per changed target. Prior review bundles remain immutable; PROPOSED is retained.

## Findings

### F1: P-ring absence is incorrectly inferred from absence of an LP-ring complex

major / resolved / confirmed; issue key: flagellar-p-ring-presence-without-l-ring.

The P-ring row remains VARIABLE but no longer excludes P rings when L/LP is absent. It cites the bounded Borrelia structural observation. LP-bushing claims are Salmonella-scoped, with FlgI essentiality and the organism-bound copy count retained.

Disposition: The P-ring row remains VARIABLE but no longer excludes P rings when L/LP is absent. It cites the bounded Borrelia structural observation. LP-bushing claims are Salmonella-scoped, with FlgI essentiality and the organism-bound copy count retained. Exact affected fields were checked against inspected primary/authority sources; all post-curation native gates passed.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/bacterial_type_flagellum_basal_body_distal_rod_p_ring.yaml; Entire native YAML, schema enums, and recorded repository histories | supports | Full corrected record re-read. Only authorized fields and the new curation event changed; historical events, unrelated claims and PROPOSED status are preserved. Remove LP-dependent P-ring exclusion using bounded Borrelia imaging evidence; explicitly scope the LP-bushing functions and graph to Salmonella. Preserve FlgI essentiality and copy count. |
| paper-01 | DOI:10.1038/nrmicro1887; Review abstract and publisher preview/key points, not subscription main text | supports | The inspected text addresses coordinated flagellar gene regulation and assembly in Gram-negative bacteria, not a denominator-bearing estimate of bacterial prevalence. |
| paper-03 | DOI:10.1038/s41467-021-24715-3; Full text: Introduction, Results LP-ring reconstruction and FlgH/FlgI structures, Figs. 1-4, methods | supports | Salmonella FlgH and FlgI form the outer-membrane and peptidoglycan sides of a 26-fold LP bushing around the distal rod. |
| paper-05 | DOI:10.1128/jb.01580-14; Primary abstract | supports | Salmonella L-ring assembly promotes rod-cap removal and the rod-to-hook transition. This is contextual assembly evidence, not grounds to add a transient assembly factor as a mature constituent. |
| paper-07 | DOI:10.1128/jb.171.7.3890-3900.1989; Primary abstract | supports | The sequenced Salmonella flgH, flgI and fliF genes encode L-, P- and M-ring proteins, respectively. |
| paper-09 | DOI:10.3389/fmicb.2015.00023; Review full text: historical structural/genomic comparisons, paragraphs 15-18 | supports | Archaella are evolutionarily and structurally distinct from the bacterial rod-and-ring apparatus; the source describes EM and genomic evidence for this distinction. |
| go-0009425 | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0009425; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| go-0009426 | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0009426; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| go-0009427 | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0009427; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| go-0009428 | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0009428; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| interpro-ipr001782 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001782/; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| uniprotkb-p15930 | https://rest.uniprot.org/uniprotkb/P15930.json; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| ncbitaxon-2 | https://rest.uniprot.org/taxonomy/2.json; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| ncbitaxon-2157 | https://rest.uniprot.org/taxonomy/2157.json; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| ncbitaxon-90371 | https://rest.uniprot.org/taxonomy/90371.json; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| ncbitaxon-99287 | https://rest.uniprot.org/taxonomy/99287.json; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| synonym-scopes | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009426,GO:0009427,GO:0009428,GO:0009429,GO:0009431,GO:0030694; Exact six GO records, definitions and typed synonyms | supports | Source synonym types checked against QuickGO, alongside exact OLS identities. |
| go-scope-definitions | https://geneontology.org/docs/ontology-documentation/; Optional elements: synonym scopes | context_only | Exact denotes equivalence; related denotes imprecise relationship. These are semantic scopes, not confidence ratings. |
| borrelia-p-ring | DOI:10.1128/JB.00340-09; Publisher full text: Results flgI mutants, Fig. 5; https://journals.asm.org/doi/10.1128/jb.00340-09 | supports | Supports the corrected, narrower claim: Borrelia flgI mutants lose the P-ring torus; downstream flgJ controls retain it. Continued motility does not mean that P rings form without FlgI. |
| motor-diversity | DOI:10.1038/emboj.2011.186; Full text: Rod and L/P-rings; https://pmc.ncbi.nlm.nih.gov/articles/PMC3160247/ | supports | Supports the corrected, narrower claim: Comparative tomography distinguishes Borrelia P rings despite absent L rings from Treponema primitia, which lacks both. This contradicts LP-dependent P-ring exclusion. |
| chevance-delegated | https://pmc.ncbi.nlm.nih.gov/articles/PMC5963726/; Review article full text, delegated inspection: opening envelope comparison, Box 1 and Figs. 1-2 | context_only | Independent agent inspected the full review article. The parent snapshot covers only abstract/preview; its hash is not a full-text attestation. |
| cohen-delegated | https://journals.asm.org/doi/10.1128/jb.01580-14; Primary full text, delegated inspection: Introduction, Results and Figs. 1/3/4 | context_only | Independent agent inspected rod-to-hook transition experiments. Parent evidence paper-05 remains an abstract-only snapshot, not a full-text hash. |
| predecessor | reviews/structured/20261010T212149Z-flagellar-distal-rod-p-ring-audit/review.yaml | context_only | Exact immutable source findings; original limitations and historical source access are retained. |
| scope-proof | /private/tmp/csm-review-20261010T210100Z/scope-proof.json | supports | Compared every prior native record, history, structured bundle and legacy report, including hidden/ignored files. Exactly six intended native records changed; old provenance is byte-identical. |

## Limits And Additional Notes

- Scoped reassessment of these exact findings, not completion of the 909-record audit or human scientific approval. Native status remains PROPOSED.
- Original source-access tiers and timestamps are retained. Reused abstracts and delegated full-text inspection are not new downloads; no unseen historical text is certified.
- The genomic survey is not direct observation of rods/rings or proof of absence in individual genomes. Borrelia P-ring evidence does not establish universal localization or function.
- The full-corpus identifier checker skips unsupported namespaces. Scoped authority checks in the predecessor provide separate provenance and do not turn that successful exit into blanket certification.
- This disposition is same-agent verification; a separate adversarial PR pass is recorded in the publication workflow, not represented as human approval here.
- Full-QC evidence is verified exact-source CI. A duplicate local full-QC run was still active when this evidence was collected and is not claimed as passed here. Final-head and merge-queue CI remain separate publication gates.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T213524Z-flagellar-distal-rod-p-ring-disposition
kind: record
repository: CultureBotAI/CellStructureMech
title: 'bacterial-type flagellum basal body, distal rod, P ring: finding dispositions'
started_at: '2026-10-10T21:29:56Z'
finished_at: '2026-10-10T21:35:24Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same agent reassesses authorized curation against inspected
    sources and native gates. This is not independent human approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Reassessed and resolved 1 exact findings after guarded curation. Unchanged
  fields retain the predecessor assessment and source-access limits; PROPOSED is retained.
source:
  git_revision: 4c68079e4d2a15d27acc3f24b65b68cd828a0652
  state: git_commit
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
  - path: data/structures/appendage/bacterial_type_flagellum_basal_body_distal_rod_p_ring.yaml
    sha256: b01c50266f84c7b8a3f98434cd00dc9ef9c88f6be9f121cfb10a372d635509a4
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
  - path: history/README.md
    sha256: 1636df44f28547f440242afcb4a05ac293b9714b4d7b809cecc30b975e44a522
    role: context
  - path: history/records/bacterial_type_flagellum_basal_body_distal_rod_p_ring/2026-09-07T195014Z-claude-304c89.yaml
    sha256: 0850370e5309452ce0057d75a14d99c56c82b7b74d2a65b14e675389fde17875
    role: context
  - path: history/records/bacterial_type_flagellum_basal_body_distal_rod_p_ring/2026-09-21T140304Z-codex-fedd3d.yaml
    sha256: 3f5721f9c6935d1f57dd0b631571b02b8fe1420d684dbc03f2c7d1e8056dbfc5
    role: context
  - path: history/records/bacterial_type_flagellum_basal_body_distal_rod_p_ring/2026-10-10T212411Z-Codex-81622c.yaml
    sha256: 60741cd08e8e4b0bc9e19035ce4e479b15dfb0cd6ac69555268bcbbe0d5c1d10
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reviews/structured/20261010T212149Z-flagellar-distal-rod-p-ring-audit/review.yaml
    sha256: 4e392dc15af690b12cd01f14f7182b03372a8e93774f0b9a5e94b92b62df3b2e
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: tests/test_flagellar_review_corrections.py
    sha256: bfbe17633847b77f5d24516101216e9263a007df003e2a1551bb09d6304f62ca
    role: context
targets:
- target_id: GO:0009428
  path: data/structures/appendage/bacterial_type_flagellum_basal_body_distal_rod_p_ring.yaml
  label: bacterial-type flagellum basal body, distal rod, P ring
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_basal_body_distal_rod_p_ring.yaml
    role: maintained scientific record
scope:
  description: Post-curation reassessment at committed source revision 4c68079e4d2a15d27acc3f24b65b68cd828a0652,
    with full native YAML re-read. Every input byte matches the initial post-curation
    capture. Unchanged fields retain the exact predecessor assessment and limitations;
    not a new corpus-wide audit.
  selection: Reassess all findings from exact predecessor 20261010T212149Z-flagellar-distal-rod-p-ring-audit
    for target GO:0009428.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0009428
checks:
- check_id: post-embeddings
  name: embeddings after curation
  status: passed
  required: true
  target_ids:
  - GO:0009428
  command: .venv/bin/python scripts/build_text_embedding_map.py --refresh
  exit_code: 0
  expected_exit_code: 0
  summary: Fresh post-curation command passed. Deterministic checks do not establish
    scientific truth.
  scope_note: 2026-10-10T21:24:38Z to 2026-10-10T21:26:27Z; log SHA-256 ae6be9d22466aa26960d2fe48f036d5cd9cf3978da6bb51fe488569b60c2bbb2
- check_id: post-render
  name: render after curation
  status: passed
  required: true
  target_ids:
  - GO:0009428
  command: .venv/bin/python scripts/render_pages.py
  exit_code: 0
  expected_exit_code: 0
  summary: Fresh post-curation command passed. Deterministic checks do not establish
    scientific truth.
  scope_note: 2026-10-10T21:26:27Z to 2026-10-10T21:26:46Z; log SHA-256 4c56c037ad334a4629db5c24de168dd94cfbb8945fc70e61abcc11db167241c0
- check_id: post-focused-tests
  name: focused-tests after curation
  status: passed
  required: true
  target_ids:
  - GO:0009428
  command: .venv/bin/python -m pytest -q tests/test_flagellar_review_corrections.py
    tests/test_record_review_contract.py
  exit_code: 0
  expected_exit_code: 0
  summary: Fresh post-curation command passed. Deterministic checks do not establish
    scientific truth.
  scope_note: 2026-10-10T21:26:46Z to 2026-10-10T21:27:10Z; log SHA-256 ff9b47c892f973404e8f7839c64afa100e8d2c0e1898500eceb6e37ff5148354
- check_id: post-history
  name: history after curation
  status: passed
  required: true
  target_ids:
  - GO:0009428
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Fresh post-curation command passed. Deterministic checks do not establish
    scientific truth.
  scope_note: 2026-10-10T21:27:46Z to 2026-10-10T21:27:59Z; log SHA-256 abfbb2717efb404ff8dee093a93f8fe33e5aeb399a96bd495dd0054c1f24460b
- check_id: post-labels
  name: labels after curation
  status: passed
  required: true
  target_ids:
  - GO:0009428
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Fresh post-curation command passed. Deterministic checks do not establish
    scientific truth.
  scope_note: 2026-10-10T21:27:59Z to 2026-10-10T21:29:32Z; log SHA-256 fb85db22c28daa12e83acf2916598842ac20181441224ad5273ae4d30fb2fa1a
- check_id: post-traits
  name: traits after curation
  status: passed
  required: true
  target_ids:
  - GO:0009428
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Fresh post-curation command passed. Deterministic checks do not establish
    scientific truth.
  scope_note: 2026-10-10T21:29:32Z to 2026-10-10T21:29:52Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: post-curies
  name: curies after curation
  status: passed
  required: true
  target_ids:
  - GO:0009428
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Fresh post-curation command passed. Deterministic checks do not establish
    scientific truth.
  scope_note: 2026-10-10T21:29:52Z to 2026-10-10T21:30:43Z; log SHA-256 ba160bae6fe80fab10b126d2861330d59ba5440bc20747d741ee4600c9232855
- check_id: post-schema
  name: schema after curation
  status: passed
  required: true
  target_ids:
  - GO:0009428
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/appendage/bacterial_type_flagellum_basal_body_distal_rod_p_ring.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Fresh post-curation command passed. Deterministic checks do not establish
    scientific truth.
  scope_note: 2026-10-10T21:27:22Z to 2026-10-10T21:27:24Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: post-strict
  name: strict after curation
  status: passed
  required: true
  target_ids:
  - GO:0009428
  command: .venv/bin/python scripts/validate_strict.py data/structures/appendage/bacterial_type_flagellum_basal_body_distal_rod_p_ring.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Fresh post-curation command passed. Deterministic checks do not establish
    scientific truth.
  scope_note: 2026-10-10T21:27:24Z to 2026-10-10T21:27:28Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: post-qc-ci
  name: qc-ci after curation
  status: passed
  required: true
  target_ids:
  - GO:0009428
  command: gh run view 38087712870 --json headSha,status,conclusion,jobs,url
  exit_code: 0
  expected_exit_code: 0
  summary: Verified successful authoritative full QC in GitHub Actions run 38087712870
    at exact source commit 4c68079e4d2a15d27acc3f24b65b68cd828a0652. All jobs and
    the authoritative quality-gate step succeeded; inspected input bytes match this
    commit. This is CI evidence, not a completed local full-QC claim.
  scope_note: 2026-10-10T21:35:10Z to 2026-10-10T21:35:13Z; log SHA-256 cdc7b8dc787c2c369b310eeadb3110f48470b9a2c6a7175a755994579f936a83
- check_id: post-whitespace
  name: whitespace after curation
  status: passed
  required: true
  target_ids:
  - GO:0009428
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  summary: Fresh post-curation command passed. Deterministic checks do not establish
    scientific truth.
  scope_note: 2026-10-10T21:35:13Z to 2026-10-10T21:35:13Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/appendage/bacterial_type_flagellum_basal_body_distal_rod_p_ring.yaml
  locator: Entire native YAML, schema enums, and recorded repository histories
  accessed_at: '2026-10-10T21:35:24Z'
  support: supports
  summary: Full corrected record re-read. Only authorized fields and the new curation
    event changed; historical events, unrelated claims and PROPOSED status are preserved.
    Remove LP-dependent P-ring exclusion using bounded Borrelia imaging evidence;
    explicitly scope the LP-bushing functions and graph to Salmonella. Preserve FlgI
    essentiality and copy count.
- evidence_id: paper-01
  kind: primary_source
  reference: DOI:10.1038/nrmicro1887
  locator: Review abstract and publisher preview/key points, not subscription main
    text
  accessed_at: '2026-10-10T21:02:11Z'
  snapshot_sha256: b6de5192cc8b8ac8aa8cb36af2fcd988ba41e8bd360247925f29c3723d5abbf9
  support: supports
  summary: The inspected text addresses coordinated flagellar gene regulation and
    assembly in Gram-negative bacteria, not a denominator-bearing estimate of bacterial
    prevalence.
- evidence_id: paper-03
  kind: primary_source
  reference: DOI:10.1038/s41467-021-24715-3
  locator: 'Full text: Introduction, Results LP-ring reconstruction and FlgH/FlgI
    structures, Figs. 1-4, methods'
  accessed_at: '2026-10-10T21:02:17Z'
  snapshot_sha256: 276579bf73c6911c33fc38b5105f2a1c9f955bd49503b59ec62630f0b9580f00
  support: supports
  summary: Salmonella FlgH and FlgI form the outer-membrane and peptidoglycan sides
    of a 26-fold LP bushing around the distal rod.
- evidence_id: paper-05
  kind: primary_source
  reference: DOI:10.1128/jb.01580-14
  locator: Primary abstract
  accessed_at: '2026-10-10T21:02:20Z'
  snapshot_sha256: 85e37f25a3442e41e26997f5c4f6554b76cbcab78cd6b92a484ced7b33124c1c
  support: supports
  summary: Salmonella L-ring assembly promotes rod-cap removal and the rod-to-hook
    transition. This is contextual assembly evidence, not grounds to add a transient
    assembly factor as a mature constituent.
- evidence_id: paper-07
  kind: primary_source
  reference: DOI:10.1128/jb.171.7.3890-3900.1989
  locator: Primary abstract
  accessed_at: '2026-10-10T21:02:23Z'
  snapshot_sha256: b8d262114b3343f311d435327dce3ed4d55150bce26ae5da088ba883efd6971a
  support: supports
  summary: The sequenced Salmonella flgH, flgI and fliF genes encode L-, P- and M-ring
    proteins, respectively.
- evidence_id: paper-09
  kind: primary_source
  reference: DOI:10.3389/fmicb.2015.00023
  locator: 'Review full text: historical structural/genomic comparisons, paragraphs
    15-18'
  accessed_at: '2026-10-10T21:02:27Z'
  snapshot_sha256: c2cec0461a17865f7242ef36df178bfc68d00c1f1e292b75f9682a6ba5461464
  support: supports
  summary: Archaella are evolutionarily and structurally distinct from the bacterial
    rod-and-ring apparatus; the source describes EM and genomic evidence for this
    distinction.
- evidence_id: go-0009425
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0009425
  locator: Exact identifier, active status, identity, and relevant source metadata
  accessed_at: '2026-10-10T21:02:15Z'
  snapshot_sha256: ba237444d9aaed5133ec4da342e0d2d5392ac51591dcbc7fe9f7e8db9127df26
  support: supports
  summary: Authority identity checked; protein examples are gene/taxon identity context,
    not independent proof of structure membership.
- evidence_id: go-0009426
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0009426
  locator: Exact identifier, active status, identity, and relevant source metadata
  accessed_at: '2026-10-10T21:02:16Z'
  snapshot_sha256: 80a529608eb0e2d1f4acc639ea016e6cd38afe34f0a2d4f1fb4dfb8c7029fcb2
  support: supports
  summary: Authority identity checked; protein examples are gene/taxon identity context,
    not independent proof of structure membership.
- evidence_id: go-0009427
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0009427
  locator: Exact identifier, active status, identity, and relevant source metadata
  accessed_at: '2026-10-10T21:02:17Z'
  snapshot_sha256: 7eba63fd2fcdabbdae2c5adc803cf7d0f03eb1fbbc5c78eb9daf7af9969e785f
  support: supports
  summary: Authority identity checked; protein examples are gene/taxon identity context,
    not independent proof of structure membership.
- evidence_id: go-0009428
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0009428
  locator: Exact identifier, active status, identity, and relevant source metadata
  accessed_at: '2026-10-10T21:02:17Z'
  snapshot_sha256: 7a65181a67156eb5867af5379a92cc18c06035562e940c74a367abb7a17ebdfe
  support: supports
  summary: Authority identity checked; protein examples are gene/taxon identity context,
    not independent proof of structure membership.
- evidence_id: interpro-ipr001782
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001782/
  locator: Exact identifier, active status, identity, and relevant source metadata
  accessed_at: '2026-10-10T21:02:21Z'
  snapshot_sha256: b21fa233203353908068e2f898abfd3a0285975b5c7cc1ca135a5eb195ce7573
  support: supports
  summary: Authority identity checked; protein examples are gene/taxon identity context,
    not independent proof of structure membership.
- evidence_id: uniprotkb-p15930
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P15930.json
  locator: Exact identifier, active status, identity, and relevant source metadata
  accessed_at: '2026-10-10T21:02:30Z'
  snapshot_sha256: 8c164cbf45eeda9d481e78be011b23720e971a901f6e68be0d2252533339073f
  support: supports
  summary: Authority identity checked; protein examples are gene/taxon identity context,
    not independent proof of structure membership.
- evidence_id: ncbitaxon-2
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/2.json
  locator: Exact identifier, active status, identity, and relevant source metadata
  accessed_at: '2026-10-10T21:02:24Z'
  snapshot_sha256: 8074c9bcd59cd4da1da4bc9ec98c040bbecd52ef5c91c4c4bb9bed0f3a7cb5a9
  support: supports
  summary: Authority identity checked; protein examples are gene/taxon identity context,
    not independent proof of structure membership.
- evidence_id: ncbitaxon-2157
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/2157.json
  locator: Exact identifier, active status, identity, and relevant source metadata
  accessed_at: '2026-10-10T21:02:25Z'
  snapshot_sha256: 14f5852a1db0f9f5ef8d60e4a11c1916bf005bf549c57dd4bc860d39194a1799
  support: supports
  summary: Authority identity checked; protein examples are gene/taxon identity context,
    not independent proof of structure membership.
- evidence_id: ncbitaxon-90371
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/90371.json
  locator: Exact identifier, active status, identity, and relevant source metadata
  accessed_at: '2026-10-10T21:02:25Z'
  snapshot_sha256: 46c958747209e78a835996643e63aafb6d1e94a8a632f0094dba733eb1bd3dee
  support: supports
  summary: Authority identity checked; protein examples are gene/taxon identity context,
    not independent proof of structure membership.
- evidence_id: ncbitaxon-99287
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/99287.json
  locator: Exact identifier, active status, identity, and relevant source metadata
  accessed_at: '2026-10-10T21:02:26Z'
  snapshot_sha256: 107ebfece75c5a7147abe7547dec9166f87ff267e6cbc3f67bea9ab9df694a59
  support: supports
  summary: Authority identity checked; protein examples are gene/taxon identity context,
    not independent proof of structure membership.
- evidence_id: synonym-scopes
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009426,GO:0009427,GO:0009428,GO:0009429,GO:0009431,GO:0030694
  locator: Exact six GO records, definitions and typed synonyms
  accessed_at: '2026-10-10T21:07:18Z'
  snapshot_sha256: e2c49b3c09a47ea7664f38b08da93cb0c6005f67f5d78cfd4375e3fcb55b5fd8
  support: supports
  summary: Source synonym types checked against QuickGO, alongside exact OLS identities.
- evidence_id: go-scope-definitions
  kind: authority
  reference: https://geneontology.org/docs/ontology-documentation/
  locator: 'Optional elements: synonym scopes'
  accessed_at: '2026-10-10T21:16:13Z'
  support: context_only
  summary: Exact denotes equivalence; related denotes imprecise relationship. These
    are semantic scopes, not confidence ratings.
- evidence_id: borrelia-p-ring
  kind: primary_source
  reference: DOI:10.1128/JB.00340-09
  locator: 'Publisher full text: Results flgI mutants, Fig. 5; https://journals.asm.org/doi/10.1128/jb.00340-09'
  accessed_at: '2026-10-10T21:16:13Z'
  support: supports
  summary: 'Supports the corrected, narrower claim: Borrelia flgI mutants lose the
    P-ring torus; downstream flgJ controls retain it. Continued motility does not
    mean that P rings form without FlgI.'
- evidence_id: motor-diversity
  kind: primary_source
  reference: DOI:10.1038/emboj.2011.186
  locator: 'Full text: Rod and L/P-rings; https://pmc.ncbi.nlm.nih.gov/articles/PMC3160247/'
  accessed_at: '2026-10-10T21:16:13Z'
  support: supports
  summary: 'Supports the corrected, narrower claim: Comparative tomography distinguishes
    Borrelia P rings despite absent L rings from Treponema primitia, which lacks both.
    This contradicts LP-dependent P-ring exclusion.'
- evidence_id: chevance-delegated
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC5963726/
  locator: 'Review article full text, delegated inspection: opening envelope comparison,
    Box 1 and Figs. 1-2'
  accessed_at: '2026-10-10T21:03:04Z'
  support: context_only
  summary: Independent agent inspected the full review article. The parent snapshot
    covers only abstract/preview; its hash is not a full-text attestation.
- evidence_id: cohen-delegated
  kind: primary_source
  reference: https://journals.asm.org/doi/10.1128/jb.01580-14
  locator: 'Primary full text, delegated inspection: Introduction, Results and Figs.
    1/3/4'
  accessed_at: '2026-10-10T21:03:04Z'
  support: context_only
  summary: Independent agent inspected rod-to-hook transition experiments. Parent
    evidence paper-05 remains an abstract-only snapshot, not a full-text hash.
- evidence_id: predecessor
  kind: prior_review
  reference: reviews/structured/20261010T212149Z-flagellar-distal-rod-p-ring-audit/review.yaml
  accessed_at: '2026-10-10T21:35:24Z'
  snapshot_sha256: 4e392dc15af690b12cd01f14f7182b03372a8e93774f0b9a5e94b92b62df3b2e
  support: context_only
  summary: Exact immutable source findings; original limitations and historical source
    access are retained.
- evidence_id: scope-proof
  kind: validation
  reference: /private/tmp/csm-review-20261010T210100Z/scope-proof.json
  accessed_at: '2026-10-10T21:24:44Z'
  snapshot_sha256: b954eb30b5595f668f4edde566b3e62b6dc45ff8749254f6ba6c823a0387950e
  support: supports
  summary: Compared every prior native record, history, structured bundle and legacy
    report, including hidden/ignored files. Exactly six intended native records changed;
    old provenance is byte-identical.
assessments:
- assessment_id: identity
  area: identity
  topic: Structure identity, synonyms, hierarchy and parthood
  outcome: supported
  target_ids:
  - GO:0009428
  evidence_ids:
  - record
  - synonym-scopes
  - go-0009428
  summary: Exact active GO cellular component denotes the named polymer/ring, not
    an individual protein. Native definitions and synonyms agree; rod segments belong
    to the rod and the rod/MS ring to the basal body.
- assessment_id: composition
  area: evidence
  topic: Every listed constituent, role, essentiality and protein example
  outcome: supported
  target_ids:
  - GO:0009428
  evidence_ids:
  - record
  - paper-03
  - paper-07
  - borrelia-p-ring
  summary: FlgI forms the P ring. IPR001782 and reviewed P15930/flgI match the declared
    component. ESSENTIAL refers to P-ring formation, not survival or motility of the
    enclosing cell.
  dimensions:
  - name: experimental-scope
    value: Salmonella preparations; no new all-lineage experimental survey
    definition: Scope of direct composition and assembly support
    evidence_ids:
    - paper-03
    - paper-07
- assessment_id: grounding
  area: grounding
  topic: Constituent family scope
  outcome: supported
  target_ids:
  - GO:0009428
  evidence_ids:
  - record
  - interpro-ipr001782
  summary: Current exact constituent-family grounding is consistent with the native
    protein example and does not substitute a broader rod/hook family.
- assessment_id: taxonomy
  area: scope
  topic: All distribution rows and organism exemplars
  outcome: supported
  target_ids:
  - GO:0009428
  evidence_ids:
  - record
  - paper-09
  - borrelia-p-ring
  - motor-diversity
  summary: VARIABLE is retained without LP-dependent exclusion. The Borrelia structural
    counterexample is bounded to the imaged organism; LP/peptidoglycan function text
    is explicitly Salmonella-scoped.
- assessment_id: functions-graph
  area: graph
  topic: Both functions, all graph nodes and every edge
  outcome: supported
  target_ids:
  - GO:0009428
  evidence_ids:
  - record
  - paper-03
  - motor-diversity
  summary: Both functions and all six graph edges now explicitly retain Salmonella
    scope for LP-bushing and peptidoglycan-localization claims. The Borrelia counterexample
    is not assigned that model-specific physiology.
- assessment_id: quantities
  area: quantity
  topic: Stoichiometry and physical properties
  outcome: supported
  target_ids:
  - GO:0009428
  evidence_ids:
  - record
  - paper-03
  summary: The 26-FlgI count is explicitly Salmonella and agrees with the LP-ring
    reconstruction.
- assessment_id: provenance
  area: provenance
  topic: Discussions, histories, status and omitted optional sections
  outcome: supported
  target_ids:
  - GO:0009428
  evidence_ids:
  - record
  - predecessor
  - scope-proof
  summary: Preserved earlier histories and discussions. Authorized curation adds one
    native event and one append-only repository history per changed target. Prior
    review bundles remain immutable; PROPOSED is retained.
findings:
- finding_id: F1
  issue_key: flagellar-p-ring-presence-without-l-ring
  category: scope
  severity: major
  status: resolved
  certainty: confirmed
  title: P-ring absence is incorrectly inferred from absence of an LP-ring complex
  description: The P-ring row remains VARIABLE but no longer excludes P rings when
    L/LP is absent. It cites the bounded Borrelia structural observation. LP-bushing
    claims are Salmonella-scoped, with FlgI essentiality and the organism-bound copy
    count retained.
  target_ids:
  - GO:0009428
  field_paths:
  - taxonomic_distribution[0].note
  evidence_ids:
  - record
  - borrelia-p-ring
  - motor-diversity
  - predecessor
  - scope-proof
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_basal_body_distal_rod_p_ring.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#evidence
  native_severity: major
  normalization_reason: Direct false-negative taxonomic exclusion contradicted by
    primary imaging evidence.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261010T212149Z-flagellar-distal-rod-p-ring-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2140
  disposition_reason: The P-ring row remains VARIABLE but no longer excludes P rings
    when L/LP is absent. It cites the bounded Borrelia structural observation. LP-bushing
    claims are Salmonella-scoped, with FlgI essentiality and the organism-bound copy
    count retained. Exact affected fields were checked against inspected primary/authority
    sources; all post-curation native gates passed.
actions: []
limitations:
- Scoped reassessment of these exact findings, not completion of the 909-record audit
  or human scientific approval. Native status remains PROPOSED.
- Original source-access tiers and timestamps are retained. Reused abstracts and delegated
  full-text inspection are not new downloads; no unseen historical text is certified.
- The genomic survey is not direct observation of rods/rings or proof of absence in
  individual genomes. Borrelia P-ring evidence does not establish universal localization
  or function.
- The full-corpus identifier checker skips unsupported namespaces. Scoped authority
  checks in the predecessor provide separate provenance and do not turn that successful
  exit into blanket certification.
- This disposition is same-agent verification; a separate adversarial PR pass is recorded
  in the publication workflow, not represented as human approval here.
- Full-QC evidence is verified exact-source CI. A duplicate local full-QC run was
  still active when this evidence was collected and is not claimed as passed here.
  Final-head and merge-queue CI remain separate publication gates.
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261010T212149Z-flagellar-distal-rod-p-ring-audit
  relationship: Resolves every finding in this exact predecessor without rewriting
    it.
links:
- https://github.com/CultureBotAI/CellStructureMech/issues/2140
```
