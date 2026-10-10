# bacterial-type flagellum basal body, proximal rod: finding dispositions

- Review: 20261010T213525Z-flagellar-proximal-rod-disposition
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-10T21:30:03Z
- Finished UTC: 2026-10-10T21:35:25Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Reassessed and resolved 2 exact findings after guarded curation. Unchanged fields retain the predecessor assessment and source-access limits; PROPOSED is retained.

## Scope And Provenance

Post-curation reassessment at committed source revision 4c68079e4d2a15d27acc3f24b65b68cd828a0652, with full native YAML re-read. Every input byte matches the initial post-curation capture. Unchanged fields retain the exact predecessor assessment and limitations; not a new corpus-wide audit.

Selection: Reassess all findings from exact predecessor 20261010T212153Z-flagellar-proximal-rod-audit for target GO:0009429.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 4c68079e4d2a15d27acc3f24b65b68cd828a0652.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0009429 | data/structures/appendage/bacterial_type_flagellum_basal_body_proximal_rod.yaml | maintained | bacterial-type flagellum basal body, proximal rod |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| embeddings after curation | passed | True | GO:0009429 | Fresh post-curation command passed. Deterministic checks do not establish scientific truth. |
| render after curation | passed | True | GO:0009429 | Fresh post-curation command passed. Deterministic checks do not establish scientific truth. |
| focused-tests after curation | passed | True | GO:0009429 | Fresh post-curation command passed. Deterministic checks do not establish scientific truth. |
| history after curation | passed | True | GO:0009429 | Fresh post-curation command passed. Deterministic checks do not establish scientific truth. |
| labels after curation | passed | True | GO:0009429 | Fresh post-curation command passed. Deterministic checks do not establish scientific truth. |
| traits after curation | passed | True | GO:0009429 | Fresh post-curation command passed. Deterministic checks do not establish scientific truth. |
| curies after curation | passed | True | GO:0009429 | Fresh post-curation command passed. Deterministic checks do not establish scientific truth. |
| schema after curation | passed | True | GO:0009429 | Fresh post-curation command passed. Deterministic checks do not establish scientific truth. |
| strict after curation | passed | True | GO:0009429 | Fresh post-curation command passed. Deterministic checks do not establish scientific truth. |
| qc-ci after curation | passed | True | GO:0009429 | Verified successful authoritative full QC in GitHub Actions run 38087712870 at exact source commit 4c68079e4d2a15d27acc3f24b65b68cd828a0652. All jobs and the authoritative quality-gate step succeeded; inspected input bytes match this commit. This is CI evidence, not a completed local full-QC claim. |
| whitespace after curation | passed | True | GO:0009429 | Fresh post-curation command passed. Deterministic checks do not establish scientific truth. |

## Scientific And Domain Assessments

### Structure identity, synonyms, hierarchy and parthood

identity: supported. Targets: GO:0009429.

Exact active GO cellular component denotes the named polymer/ring, not an individual protein. Native definitions and synonyms agree; rod segments belong to the rod and the rod/MS ring to the basal body.

### Every listed constituent, role, essentiality and protein example

evidence: supported. Targets: GO:0009429.

FliF alone is the core MS ring; FlgG is the distal rod; FliE/FlgB/FlgC/FlgF constitute the proximal segment, with FlgG added for the whole rod. Only the relevant components are asserted in this target. Structural membership and cooperative stable assembly support the constituent model; this is not new proof of every deletion phenotype in every lineage. Current protein accessions, reviewed status, genes and LT2 taxon agree.

### Family scope and reviewed-label-only decisions

grounding: supported. Targets: GO:0009429.

FliE is grounded to exact family IPR001624, matched by reviewed P26462. Its obsolete label-only status is removed while the former rationale is retained with a dated superseding decision. Other components, including FlgF, are unchanged.

### All distribution rows and organism exemplars

scope: supported. Targets: GO:0009429.

Bacterial occurrence is VARIABLE. The cited FliPQR genomic-marker survey is explicitly not direct observation or a prevalence estimate for this particular rod/ring. Archaeal distinction and canonical examples are unchanged.

### Both functions, all graph nodes and every edge

graph: supported. Targets: GO:0009429.

Checked all 6 edges. Axial adjacency, constituent assembly, envelope bushing topology and mechanical coupling are supported in the cited model system. Spatial composition is not interpreted as a directly observed dynamic assembly trajectory. No unsupported stator rotation model is asserted here.

### Stoichiometry and physical properties

quantity: not_applicable. Targets: GO:0009429.

No quantitative physical-property or stoichiometry assertion is present; absent optional measurements are not defects.

### Discussions, histories, status and omitted optional sections

provenance: supported. Targets: GO:0009429.

Preserved earlier histories and discussions. Authorized curation adds one native event and one append-only repository history per changed target. Prior review bundles remain immutable; PROPOSED is retained.

## Findings

### F1: Bacterial prevalence exceeds the cited evidence

major / resolved / confirmed; issue key: flagellar-proximal-rod-bacterial-prevalence-common.

The Bacteria row now uses VARIABLE and an inspected genomic survey. Its FliPQR marker frequency is explicitly not direct observation or a prevalence estimate for the particular rod/ring.

Disposition: The Bacteria row now uses VARIABLE and an inspected genomic survey. Its FliPQR marker frequency is explicitly not direct observation or a prevalence estimate for the particular rod/ring. Exact affected fields were checked against inspected primary/authority sources; all post-curation native gates passed.

### F2: FliE label-only status is stale against an exact family match

minor / resolved / confirmed; issue key: flagellar-proximal-rod-flie-label-only-status.

FliE now grounds to verified IPR001624/P26462. The incompatible current label-only status is removed and its historical rationale has a dated superseding note; FlgF remains unchanged.

Disposition: FliE now grounds to verified IPR001624/P26462. The incompatible current label-only status is removed and its historical rationale has a dated superseding note; FlgF remains unchanged. Exact affected fields were checked against inspected primary/authority sources; all post-curation native gates passed.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/bacterial_type_flagellum_basal_body_proximal_rod.yaml; Entire native YAML, schema enums, and recorded repository histories | supports | Full corrected record re-read. Only authorized fields and the new curation event changed; historical events, unrelated claims and PROPOSED status are preserved. Replace unsupported majority bacterial prevalence with lineage-dependent occurrence and an explicitly qualified genomic survey. Ground FliE to verified IPR001624/P26462 while retaining the earlier label-only rationale and leaving FlgF unchanged. |
| paper-00 | DOI:10.1016/j.cell.2021.03.057; Primary abstract | supports | Cryo-EM of a Salmonella rod-hook-motor complex identifies MS-ring, FliE and FlgB contacts involved in mechanical coupling. |
| paper-04 | DOI:10.1038/s41564-021-00895-y; Author manuscript full text: Introduction, rod reconstruction, Fig. 2, MS-ring contacts, Fig. 3, methods | supports | Intact Salmonella basal bodies resolve proximal FliE/FlgB/FlgC/FlgF, distal FlgG, and their spatial contacts. The measured architecture is not an all-bacterial prevalence survey. |
| paper-06 | DOI:10.1128/jb.182.11.3029-3036.2000; Primary abstract; no successful full-text retrieval | supports | Genetic suppressors and affinity blotting support strong FliE-FlgB interaction. The older proposed junction model is distinguished from later resolved structures. |
| paper-09 | DOI:10.3389/fmicb.2015.00023; Review full text: historical structural/genomic comparisons, paragraphs 15-18 | supports | Archaella are evolutionarily and structurally distinct from the bacterial rod-and-ring apparatus; the source describes EM and genomic evidence for this distinction. |
| paper-10 | DOI:10.1128/jb.182.11.3029-3036.2000; Primary abstract; identical paper to DOI evidence paper-06 | supports | PMID 10809679 resolves to the FliE-FlgB interaction study cited in UniProt localization provenance. |
| paper-11 | DOI:10.1006/jmbi.2001.4963; Primary abstract | supports | Salmonella FlgJ mutant experiments support its assembly role and interactions with FliE/FlgB; they do not make FlgJ a mature rod constituent. |
| paper-12 | DOI:10.1016/j.jmb.2004.03.070; Primary abstract | supports | All five Salmonella rod proteins were purified from an E. coli expression system. In-vitro fibrils were explicitly distinguished from the native rod; the source describes rod torque transmission. |
| paper-13 | DOI:10.1073/pnas.89.11.4801; Primary abstract | supports | Mass measurements of isolated Salmonella basal-body subcomplexes support historical rod-protein localization and approximate composition, not replacement of later cryo-EM counts. |
| go-0009426 | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0009426; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| go-0009429 | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0009429; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| go-0030694 | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0030694; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| interpro-ipr006299 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006299/; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| interpro-ipr006300 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006300/; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| uniprotkb-p0a1i7 | https://rest.uniprot.org/uniprotkb/P0A1I7.json; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| uniprotkb-p16323 | https://rest.uniprot.org/uniprotkb/P16323.json; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| uniprotkb-p16437 | https://rest.uniprot.org/uniprotkb/P16437.json; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| uniprotkb-p26462 | https://rest.uniprot.org/uniprotkb/P26462.json; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| ncbitaxon-2 | https://rest.uniprot.org/taxonomy/2.json; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| ncbitaxon-2157 | https://rest.uniprot.org/taxonomy/2157.json; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| ncbitaxon-90371 | https://rest.uniprot.org/taxonomy/90371.json; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| ncbitaxon-99287 | https://rest.uniprot.org/taxonomy/99287.json; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| synonym-scopes | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009426,GO:0009427,GO:0009428,GO:0009429,GO:0009431,GO:0030694; Exact six GO records, definitions and typed synonyms | supports | Source synonym types checked against QuickGO, alongside exact OLS identities. |
| distribution | DOI:10.1073/pnas.2512476122; Results computational distribution paragraph; Methods reference-genome/HMM design | supports | Supports the corrected, narrower claim: Across 30,238 GTDB genomes from 131 phyla, approximately 40% carry FliPQR markers. This is a genomic proxy, not a microscopy census or direct rod/ring prevalence measurement. |
| assembly | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2F0022-2836%2892%2990958-m%22&amp;format=json&amp;resultType=core; Primary abstract | supports | Salmonella precursor analysis distinguishes autonomous MS-ring formation from cooperative assembly of FliE and the four rod proteins into a stable structure. The unseen individual mutant results are not certified. |
| flie-family | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001624/; metadata accession, family type, name, integrated signatures | supports | Supports the corrected, narrower claim: Exact FliE family IPR001624 is present. The curated Salmonella example P26462 independently carries this family cross-reference. |
| flgf-family-context | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012836/; Narrow family entry and current P16323 cross-references | context_only | A narrower FlgF entry exists, but P16323 does not currently match it. No automatic FlgF grounding is justified by name alone. |
| predecessor | reviews/structured/20261010T212153Z-flagellar-proximal-rod-audit/review.yaml | context_only | Exact immutable source findings; original limitations and historical source access are retained. |
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
review_id: 20261010T213525Z-flagellar-proximal-rod-disposition
kind: record
repository: CultureBotAI/CellStructureMech
title: 'bacterial-type flagellum basal body, proximal rod: finding dispositions'
started_at: '2026-10-10T21:30:03Z'
finished_at: '2026-10-10T21:35:25Z'
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
summary: Reassessed and resolved 2 exact findings after guarded curation. Unchanged
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
  - path: data/structures/appendage/bacterial_type_flagellum_basal_body_proximal_rod.yaml
    sha256: 4c852e861f6dd4a3f12dd7de9c752c590d2cd04dfaca7633703f5d4b96a85fae
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
  - path: history/records/bacterial_type_flagellum_basal_body_proximal_rod/2026-09-07T061129Z-claude-6323c8.yaml
    sha256: 166585563dc69949f2ec5d24edef842e08f7610297c83e09998e59ea59a7c126
    role: context
  - path: history/records/bacterial_type_flagellum_basal_body_proximal_rod/2026-09-21T103301Z-codex-876e6f.yaml
    sha256: c5e3a853d072e3d9653e1085bceb6521c54f22e268b2e2fdb6dbf9af5c7b5bcd
    role: context
  - path: history/records/bacterial_type_flagellum_basal_body_proximal_rod/2026-10-10T212418Z-Codex-055f31.yaml
    sha256: 769fe8a65c1749350963a1a81367453ca26d9c0bad5dcf3c7e9571b08c53e69b
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reviews/structured/20261010T212153Z-flagellar-proximal-rod-audit/review.yaml
    sha256: 37571924020abcae3b4ee25efdc61b80c43d8b2af22e561ae6c68a31c37880a0
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
- target_id: GO:0009429
  path: data/structures/appendage/bacterial_type_flagellum_basal_body_proximal_rod.yaml
  label: bacterial-type flagellum basal body, proximal rod
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_basal_body_proximal_rod.yaml
    role: maintained scientific record
scope:
  description: Post-curation reassessment at committed source revision 4c68079e4d2a15d27acc3f24b65b68cd828a0652,
    with full native YAML re-read. Every input byte matches the initial post-curation
    capture. Unchanged fields retain the exact predecessor assessment and limitations;
    not a new corpus-wide audit.
  selection: Reassess all findings from exact predecessor 20261010T212153Z-flagellar-proximal-rod-audit
    for target GO:0009429.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0009429
checks:
- check_id: post-embeddings
  name: embeddings after curation
  status: passed
  required: true
  target_ids:
  - GO:0009429
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
  - GO:0009429
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
  - GO:0009429
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
  - GO:0009429
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
  - GO:0009429
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
  - GO:0009429
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
  - GO:0009429
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
  - GO:0009429
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/appendage/bacterial_type_flagellum_basal_body_proximal_rod.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Fresh post-curation command passed. Deterministic checks do not establish
    scientific truth.
  scope_note: 2026-10-10T21:27:34Z to 2026-10-10T21:27:36Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: post-strict
  name: strict after curation
  status: passed
  required: true
  target_ids:
  - GO:0009429
  command: .venv/bin/python scripts/validate_strict.py data/structures/appendage/bacterial_type_flagellum_basal_body_proximal_rod.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Fresh post-curation command passed. Deterministic checks do not establish
    scientific truth.
  scope_note: 2026-10-10T21:27:36Z to 2026-10-10T21:27:40Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: post-qc-ci
  name: qc-ci after curation
  status: passed
  required: true
  target_ids:
  - GO:0009429
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
  - GO:0009429
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  summary: Fresh post-curation command passed. Deterministic checks do not establish
    scientific truth.
  scope_note: 2026-10-10T21:35:13Z to 2026-10-10T21:35:13Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/appendage/bacterial_type_flagellum_basal_body_proximal_rod.yaml
  locator: Entire native YAML, schema enums, and recorded repository histories
  accessed_at: '2026-10-10T21:35:25Z'
  support: supports
  summary: Full corrected record re-read. Only authorized fields and the new curation
    event changed; historical events, unrelated claims and PROPOSED status are preserved.
    Replace unsupported majority bacterial prevalence with lineage-dependent occurrence
    and an explicitly qualified genomic survey. Ground FliE to verified IPR001624/P26462
    while retaining the earlier label-only rationale and leaving FlgF unchanged.
- evidence_id: paper-00
  kind: primary_source
  reference: DOI:10.1016/j.cell.2021.03.057
  locator: Primary abstract
  accessed_at: '2026-10-10T21:02:10Z'
  snapshot_sha256: 7cad5919d0b75e34ceeeece1f50d2ee4b418b5f4124d3ff2f3c638ba9e17a79f
  support: supports
  summary: Cryo-EM of a Salmonella rod-hook-motor complex identifies MS-ring, FliE
    and FlgB contacts involved in mechanical coupling.
- evidence_id: paper-04
  kind: primary_source
  reference: DOI:10.1038/s41564-021-00895-y
  locator: 'Author manuscript full text: Introduction, rod reconstruction, Fig. 2,
    MS-ring contacts, Fig. 3, methods'
  accessed_at: '2026-10-10T21:02:20Z'
  snapshot_sha256: f3634f84b0d0fdcebd3677b2080c1ec5064e9feac3199142d2adbcc1e01c501b
  support: supports
  summary: Intact Salmonella basal bodies resolve proximal FliE/FlgB/FlgC/FlgF, distal
    FlgG, and their spatial contacts. The measured architecture is not an all-bacterial
    prevalence survey.
- evidence_id: paper-06
  kind: primary_source
  reference: DOI:10.1128/jb.182.11.3029-3036.2000
  locator: Primary abstract; no successful full-text retrieval
  accessed_at: '2026-10-10T21:02:21Z'
  snapshot_sha256: 878ce16adb21f910d2dba66f4a8a41dedfab01e75876d95b41450cd9427c72fb
  support: supports
  summary: Genetic suppressors and affinity blotting support strong FliE-FlgB interaction.
    The older proposed junction model is distinguished from later resolved structures.
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
- evidence_id: paper-10
  kind: primary_source
  reference: DOI:10.1128/jb.182.11.3029-3036.2000
  locator: Primary abstract; identical paper to DOI evidence paper-06
  accessed_at: '2026-10-10T21:02:28Z'
  snapshot_sha256: c78bf66de7c2c66781b756bd39855c13e24adc2b804163b7c69d32ba1f0eab2b
  support: supports
  summary: PMID 10809679 resolves to the FliE-FlgB interaction study cited in UniProt
    localization provenance.
- evidence_id: paper-11
  kind: primary_source
  reference: DOI:10.1006/jmbi.2001.4963
  locator: Primary abstract
  accessed_at: '2026-10-10T21:02:30Z'
  snapshot_sha256: 24904fd10c7be77fd37f113de0c846e1674582aaefc5e876b4b8cf395dc5b286
  support: supports
  summary: Salmonella FlgJ mutant experiments support its assembly role and interactions
    with FliE/FlgB; they do not make FlgJ a mature rod constituent.
- evidence_id: paper-12
  kind: primary_source
  reference: DOI:10.1016/j.jmb.2004.03.070
  locator: Primary abstract
  accessed_at: '2026-10-10T21:02:31Z'
  snapshot_sha256: 4a1e98d20683e5f80e7f17f7c6943186c75504a3771565c938d5b68b0d4735d8
  support: supports
  summary: All five Salmonella rod proteins were purified from an E. coli expression
    system. In-vitro fibrils were explicitly distinguished from the native rod; the
    source describes rod torque transmission.
- evidence_id: paper-13
  kind: primary_source
  reference: DOI:10.1073/pnas.89.11.4801
  locator: Primary abstract
  accessed_at: '2026-10-10T21:02:31Z'
  snapshot_sha256: db571c2a7457a2b0b0e0bc0c0a8f215f6647ecc608ebb1fefc1044c31221a6c0
  support: supports
  summary: Mass measurements of isolated Salmonella basal-body subcomplexes support
    historical rod-protein localization and approximate composition, not replacement
    of later cryo-EM counts.
- evidence_id: go-0009426
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0009426
  locator: Exact identifier, active status, identity, and relevant source metadata
  accessed_at: '2026-10-10T21:02:16Z'
  snapshot_sha256: 80a529608eb0e2d1f4acc639ea016e6cd38afe34f0a2d4f1fb4dfb8c7029fcb2
  support: supports
  summary: Authority identity checked; protein examples are gene/taxon identity context,
    not independent proof of structure membership.
- evidence_id: go-0009429
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0009429
  locator: Exact identifier, active status, identity, and relevant source metadata
  accessed_at: '2026-10-10T21:02:18Z'
  snapshot_sha256: d9a8fd473f0c62edc2f61ce46669f01e16ec2c7ec7a37a1f429e90975304752a
  support: supports
  summary: Authority identity checked; protein examples are gene/taxon identity context,
    not independent proof of structure membership.
- evidence_id: go-0030694
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0030694
  locator: Exact identifier, active status, identity, and relevant source metadata
  accessed_at: '2026-10-10T21:02:19Z'
  snapshot_sha256: 5eabb2fb50f4dde24f8c5da7274caecd1a5f6a3a73a0da8b2695e3ace9026e00
  support: supports
  summary: Authority identity checked; protein examples are gene/taxon identity context,
    not independent proof of structure membership.
- evidence_id: interpro-ipr006299
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006299/
  locator: Exact identifier, active status, identity, and relevant source metadata
  accessed_at: '2026-10-10T21:02:22Z'
  snapshot_sha256: 58fa140385043dfb34415d275d4158ebfee94f26a108d0ea6f716227eef4678a
  support: supports
  summary: Authority identity checked; protein examples are gene/taxon identity context,
    not independent proof of structure membership.
- evidence_id: interpro-ipr006300
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006300/
  locator: Exact identifier, active status, identity, and relevant source metadata
  accessed_at: '2026-10-10T21:02:23Z'
  snapshot_sha256: a0d8ebd5605bc3a4ab0a42aa1bc7fab4d6907c51df20c7b1bbbef1128fb2c761
  support: supports
  summary: Authority identity checked; protein examples are gene/taxon identity context,
    not independent proof of structure membership.
- evidence_id: uniprotkb-p0a1i7
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0A1I7.json
  locator: Exact identifier, active status, identity, and relevant source metadata
  accessed_at: '2026-10-10T21:02:27Z'
  snapshot_sha256: ad304bc866322da726bb42d2f175e416e9f1e5aa93b529bd5895f1c686c1ee5f
  support: supports
  summary: Authority identity checked; protein examples are gene/taxon identity context,
    not independent proof of structure membership.
- evidence_id: uniprotkb-p16323
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P16323.json
  locator: Exact identifier, active status, identity, and relevant source metadata
  accessed_at: '2026-10-10T21:02:30Z'
  snapshot_sha256: 923827e90e750b1b60a0174fec24302a863cefb3df38a159829251af52ad9b93
  support: supports
  summary: Authority identity checked; protein examples are gene/taxon identity context,
    not independent proof of structure membership.
- evidence_id: uniprotkb-p16437
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P16437.json
  locator: Exact identifier, active status, identity, and relevant source metadata
  accessed_at: '2026-10-10T21:02:31Z'
  snapshot_sha256: 0b7bec6a86d108bce9fb42965e1c24412152df5b0d43df00baa8161564d73bc5
  support: supports
  summary: Authority identity checked; protein examples are gene/taxon identity context,
    not independent proof of structure membership.
- evidence_id: uniprotkb-p26462
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P26462.json
  locator: Exact identifier, active status, identity, and relevant source metadata
  accessed_at: '2026-10-10T21:02:32Z'
  snapshot_sha256: 7269184f9b8fa723f0f1a55a0c2002773e25274f3e112c550909dfbd7766c911
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
- evidence_id: distribution
  kind: primary_source
  reference: DOI:10.1073/pnas.2512476122
  locator: Results computational distribution paragraph; Methods reference-genome/HMM
    design
  accessed_at: '2026-10-10T21:03:53Z'
  snapshot_sha256: 6cedc1bf8fd502b010e3123a8cd40e566506804de364f6d959a52120457af9f6
  support: supports
  summary: 'Supports the corrected, narrower claim: Across 30,238 GTDB genomes from
    131 phyla, approximately 40% carry FliPQR markers. This is a genomic proxy, not
    a microscopy census or direct rod/ring prevalence measurement.'
- evidence_id: assembly
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2F0022-2836%2892%2990958-m%22&format=json&resultType=core
  locator: Primary abstract
  accessed_at: '2026-10-10T21:07:19Z'
  snapshot_sha256: 1a77628f5a6768343941b8ca40dcb7e36c44bab86d3f2a97a850a79fdcee282c
  support: supports
  summary: Salmonella precursor analysis distinguishes autonomous MS-ring formation
    from cooperative assembly of FliE and the four rod proteins into a stable structure.
    The unseen individual mutant results are not certified.
- evidence_id: flie-family
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001624/
  locator: metadata accession, family type, name, integrated signatures
  accessed_at: '2026-10-10T21:03:50Z'
  snapshot_sha256: 1ceca64f71b5bbea67b413cf482aee366d361202dfd03dfd5c32c2d3fff35110
  support: supports
  summary: 'Supports the corrected, narrower claim: Exact FliE family IPR001624 is
    present. The curated Salmonella example P26462 independently carries this family
    cross-reference.'
- evidence_id: flgf-family-context
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012836/
  locator: Narrow family entry and current P16323 cross-references
  accessed_at: '2026-10-10T21:03:51Z'
  snapshot_sha256: c12aeb168174a57471a3dac64298ac6ca3bee48548a27ecbd95f96ba0e45fb8b
  support: context_only
  summary: A narrower FlgF entry exists, but P16323 does not currently match it. No
    automatic FlgF grounding is justified by name alone.
- evidence_id: predecessor
  kind: prior_review
  reference: reviews/structured/20261010T212153Z-flagellar-proximal-rod-audit/review.yaml
  accessed_at: '2026-10-10T21:35:25Z'
  snapshot_sha256: 37571924020abcae3b4ee25efdc61b80c43d8b2af22e561ae6c68a31c37880a0
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
  - GO:0009429
  evidence_ids:
  - record
  - synonym-scopes
  - go-0009429
  summary: Exact active GO cellular component denotes the named polymer/ring, not
    an individual protein. Native definitions and synonyms agree; rod segments belong
    to the rod and the rod/MS ring to the basal body.
- assessment_id: composition
  area: evidence
  topic: Every listed constituent, role, essentiality and protein example
  outcome: supported
  target_ids:
  - GO:0009429
  evidence_ids:
  - record
  - assembly
  - paper-04
  - paper-12
  summary: FliF alone is the core MS ring; FlgG is the distal rod; FliE/FlgB/FlgC/FlgF
    constitute the proximal segment, with FlgG added for the whole rod. Only the relevant
    components are asserted in this target. Structural membership and cooperative
    stable assembly support the constituent model; this is not new proof of every
    deletion phenotype in every lineage. Current protein accessions, reviewed status,
    genes and LT2 taxon agree.
  dimensions:
  - name: experimental-scope
    value: Salmonella preparations; no new all-lineage experimental survey
    definition: Scope of direct composition and assembly support
    evidence_ids:
    - paper-04
    - paper-12
- assessment_id: grounding
  area: grounding
  topic: Family scope and reviewed-label-only decisions
  outcome: supported
  target_ids:
  - GO:0009429
  evidence_ids:
  - record
  - flie-family
  - uniprotkb-p26462
  - flgf-family-context
  summary: FliE is grounded to exact family IPR001624, matched by reviewed P26462.
    Its obsolete label-only status is removed while the former rationale is retained
    with a dated superseding decision. Other components, including FlgF, are unchanged.
- assessment_id: taxonomy
  area: scope
  topic: All distribution rows and organism exemplars
  outcome: supported
  target_ids:
  - GO:0009429
  evidence_ids:
  - record
  - paper-09
  - distribution
  - paper-04
  - paper-12
  summary: Bacterial occurrence is VARIABLE. The cited FliPQR genomic-marker survey
    is explicitly not direct observation or a prevalence estimate for this particular
    rod/ring. Archaeal distinction and canonical examples are unchanged.
- assessment_id: functions-graph
  area: graph
  topic: Both functions, all graph nodes and every edge
  outcome: supported
  target_ids:
  - GO:0009429
  evidence_ids:
  - record
  - paper-00
  - paper-04
  - paper-06
  - paper-12
  summary: Checked all 6 edges. Axial adjacency, constituent assembly, envelope bushing
    topology and mechanical coupling are supported in the cited model system. Spatial
    composition is not interpreted as a directly observed dynamic assembly trajectory.
    No unsupported stator rotation model is asserted here.
- assessment_id: quantities
  area: quantity
  topic: Stoichiometry and physical properties
  outcome: not_applicable
  target_ids:
  - GO:0009429
  evidence_ids:
  - record
  summary: No quantitative physical-property or stoichiometry assertion is present;
    absent optional measurements are not defects.
- assessment_id: provenance
  area: provenance
  topic: Discussions, histories, status and omitted optional sections
  outcome: supported
  target_ids:
  - GO:0009429
  evidence_ids:
  - record
  - predecessor
  - scope-proof
  summary: Preserved earlier histories and discussions. Authorized curation adds one
    native event and one append-only repository history per changed target. Prior
    review bundles remain immutable; PROPOSED is retained.
findings:
- finding_id: F1
  issue_key: flagellar-proximal-rod-bacterial-prevalence-common
  category: scope
  severity: major
  status: resolved
  certainty: confirmed
  title: Bacterial prevalence exceeds the cited evidence
  description: The Bacteria row now uses VARIABLE and an inspected genomic survey.
    Its FliPQR marker frequency is explicitly not direct observation or a prevalence
    estimate for the particular rod/ring.
  target_ids:
  - GO:0009429
  field_paths:
  - taxonomic_distribution[0].presence
  - taxonomic_distribution[0].reference
  evidence_ids:
  - record
  - distribution
  - go-0009429
  - predecessor
  - scope-proof
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_basal_body_proximal_rod.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#evidence
  native_severity: major
  normalization_reason: Material taxonomic scope inflation under the native rubric.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261010T212153Z-flagellar-proximal-rod-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2142
  disposition_reason: The Bacteria row now uses VARIABLE and an inspected genomic
    survey. Its FliPQR marker frequency is explicitly not direct observation or a
    prevalence estimate for the particular rod/ring. Exact affected fields were checked
    against inspected primary/authority sources; all post-curation native gates passed.
- finding_id: F2
  issue_key: flagellar-proximal-rod-flie-label-only-status
  category: grounding
  severity: minor
  status: resolved
  certainty: confirmed
  title: FliE label-only status is stale against an exact family match
  description: FliE now grounds to verified IPR001624/P26462. The incompatible current
    label-only status is removed and its historical rationale has a dated superseding
    note; FlgF remains unchanged.
  target_ids:
  - GO:0009429
  field_paths:
  - components[0].grounding_status
  - components[0].grounding_notes
  evidence_ids:
  - record
  - flie-family
  - uniprotkb-p26462
  - predecessor
  - scope-proof
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_basal_body_proximal_rod.yaml
    role: maintained scientific record
  rule_id: src/cellstructuremech/schema/cellstructuremech.yaml#ComponentGroundingStatusEnum
  native_severity: minor
  normalization_reason: Bounded grounding/provenance correction; protein and structure
    identity are otherwise correct.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261010T212153Z-flagellar-proximal-rod-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2143
  disposition_reason: FliE now grounds to verified IPR001624/P26462. The incompatible
    current label-only status is removed and its historical rationale has a dated
    superseding note; FlgF remains unchanged. Exact affected fields were checked against
    inspected primary/authority sources; all post-curation native gates passed.
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
  review_id: 20261010T212153Z-flagellar-proximal-rod-audit
  relationship: Resolves every finding in this exact predecessor without rewriting
    it.
links:
- https://github.com/CultureBotAI/CellStructureMech/issues/2142
- https://github.com/CultureBotAI/CellStructureMech/issues/2143
```
