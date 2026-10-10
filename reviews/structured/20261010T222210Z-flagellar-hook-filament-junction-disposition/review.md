# bacterial-type flagellum hook-filament junction: finding dispositions

- Review: 20261010T222210Z-flagellar-hook-filament-junction-disposition
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-10T22:13:38Z
- Finished UTC: 2026-10-10T22:22:10Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Every finding in the linked predecessor is resolved in the inspected maintained inputs. Native scientific status remains PROPOSED.

## Scope And Provenance

Reassessment of the exact prior finding fields, changed claim evidence and append-only provenance, not a new whole-record or corpus-wide assessment. Unchanged assertions retain the original review scope and limitations.

Selection: All findings in 20261010T220818Z-flagellar-hook-filament-junction-audit
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e5f99e3a62526a098cd8a32729c5777d48eb0396.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0009422 | data/structures/appendage/bacterial_type_flagellum_hook_filament_junction.yaml | maintained | bacterial-type flagellum hook-filament junction |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0009422 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. |
| strict | passed | True | GO:0009422 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. |
| snippets | passed | True | GO:0009422 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. There are no quoted snippet fields in this target; this is not validation of paraphrase meaning. |
| history | passed | True | GO:0009422 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. |
| labels | passed | True | GO:0009422 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. |
| traits | passed | True | GO:0009422 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. |
| curies | passed | True | GO:0009422 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. Unsupported namespaces remain explicitly skipped; scoped authority verification is retained in source evidence. |
| regressions | passed | True | GO:0009422 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. |
| reviews | passed | True | GO:0009422 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. |
| diff | passed | True | GO:0009422 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. |
| Exact-fix-commit authoritative CI QC | passed | True | GO:0009422 | Verified successful authoritative QC step on the exact inspected fix commit, including all corpus tests, generated-site and text-map drift checks. |

## Scientific And Domain Assessments

### Furukawa 2002 is cited for interactions it did not report

evidence: supported. Targets: GO:0009422.

The affected component and contact edge now cite the 2025 assembled-junction structure. The older citation is retained as bounding evidence and explicitly does not assert FlgK-FlgL solution binding.

### Historical localization and copy-number descriptions exceed the inspected reports

evidence: supported. Targets: GO:0009422.

The 1987 notes retain approximate HAP1 10-20 and HAP3 10-40 estimates and the fine-localization limitation. The 1985 note distinguishes filamentless hooks from mature HAP3 localization. Modern layer-order evidence and species-scoped 11:11/22 counts are retained from 2025.

### FlgK label-only status is contradicted by an exact matched family

evidence: supported. Targets: GO:0009422.

FlgK now grounds to verified IPR002371 with the reviewed Salmonella P0A1J5 match recorded. The incompatible current label-only status is removed; its rationale is preserved with a dated superseding note. FlgL and the separate label-only FlgE decision are unchanged.

## Findings

### F1: Furukawa 2002 is cited for interactions it did not report

major / resolved / confirmed; issue key: flagellar-junction-flgk-flgl-soluble-interaction-miscitation.

The affected component and contact edge now cite the 2025 assembled-junction structure. The older citation is retained as bounding evidence and explicitly does not assert FlgK-FlgL solution binding.

Disposition: The affected component and contact edge now cite the 2025 assembled-junction structure. The older citation is retained as bounding evidence and explicitly does not assert FlgK-FlgL solution binding. Exact affected fields were checked against the cited primary or authority evidence and passing post-curation gates.

### F2: Historical localization and copy-number descriptions exceed the inspected reports

minor / resolved / confirmed; issue key: flagellar-junction-historical-localization-count-attribution.

The 1987 notes retain approximate HAP1 10-20 and HAP3 10-40 estimates and the fine-localization limitation. The 1985 note distinguishes filamentless hooks from mature HAP3 localization. Modern layer-order evidence and species-scoped 11:11/22 counts are retained from 2025.

Disposition: The 1987 notes retain approximate HAP1 10-20 and HAP3 10-40 estimates and the fine-localization limitation. The 1985 note distinguishes filamentless hooks from mature HAP3 localization. Modern layer-order evidence and species-scoped 11:11/22 counts are retained from 2025. Exact affected fields were checked against the cited primary or authority evidence and passing post-curation gates.

### F3: FlgK label-only status is contradicted by an exact matched family

minor / resolved / confirmed; issue key: flagellar-junction-flgk-label-only-status.

FlgK now grounds to verified IPR002371 with the reviewed Salmonella P0A1J5 match recorded. The incompatible current label-only status is removed; its rationale is preserved with a dated superseding note. FlgL and the separate label-only FlgE decision are unchanged.

Disposition: FlgK now grounds to verified IPR002371 with the reviewed Salmonella P0A1J5 match recorded. The incompatible current label-only status is removed; its rationale is preserved with a dated superseding note. FlgL and the separate label-only FlgE decision are unchanged. Exact affected fields were checked against the cited primary or authority evidence and passing post-curation gates.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/bacterial_type_flagellum_hook_filament_junction.yaml; Entire YAML, schema and recorded histories | context_only | Re-read the changed target and complete diff against the predecessor; all identified claim corrections are present, with unchanged prior curation events and PROPOSED status. |
| paper-01 | DOI:10.1016/S0022-2836(02)00139-0; Primary abstract, complete reported pair-association results | supports | Only flagellin-induced HAP3 aggregation without stable binding and stable HAP2-HAP3 heterodimers are reported; not soluble FlgK-FlgL binding. |
| paper-03 | DOI:10.1038/nrmicro1887; PMC author-manuscript full text, introductory organism comparison and Box 1 | supports | Assembly context supports the listed axial parts; Box 1 distinguishes 20-nm thickness from 10-15-micrometer length. It does not establish majority-Bacteria prevalence. |
| paper-07 | DOI:10.1038/s41564-025-02037-0; Full text, native cap/HFJ Results, Figs. 1-6, Discussion, strain Methods | supports | Native Salmonella caps and junctions support five FliD and eleven each of FlgK/FlgL. Campylobacter prefilament caps and Salmonella assembly intermediates support the bounded mechanisms. |
| paper-12 | DOI:10.1128/jb.162.1.183-189.1985; Primary abstract | supports | Antibody localization supports HAP layering on filamentless hooks; mature HAP1 junction localization was supported, while mature HAP2/HAP3 positions were not clarified by that procedure. |
| paper-13 | DOI:10.1128/jb.169.3.1168-1173.1987; Primary abstract, localization and protein composition measurements | supports | HAP1/HAP3 localize to the junction and HAP2 to the tip. Estimated amounts were 10-20 HAP1 and 10-40 HAP3, not an exact eleven each. |
| paper-16 | DOI:10.1146/annurev.micro.57.030502.090832; Review abstract | supports | Export through the axial channel and distal assembly are supported; fine-grained assembly evidence is cross-checked with accessible structural papers. |
| paper-17 | DOI:10.3389/fmicb.2015.00023; Review full text, biochemical/genomic/structural comparison with bacterial flagella | supports | Archaella have distinct type-IV-pilus-related architecture, not bacterial flagellin/FlgE/FlgKL/FliD axial structures. |
| go-0009288 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009288; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| go-0009420 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009420; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| go-0009421 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009421; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| go-0009422 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009422; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| go-0009424 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009424; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| interpro-ipr001492 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001492/; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| interpro-ipr013384 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013384/; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| uniprotkb-p16326 | https://rest.uniprot.org/uniprotkb/P16326.json; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| ncbitaxon-2 | https://rest.uniprot.org/taxonomy/2.json; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| ncbitaxon-2157 | https://rest.uniprot.org/taxonomy/2157.json; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| ncbitaxon-28901 | https://rest.uniprot.org/taxonomy/28901.json; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| ncbitaxon-99287 | https://rest.uniprot.org/taxonomy/99287.json; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| flgk-family | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002371/; Entry type, definition and integrated signatures | supports | IPR002371 is an exact FlgK/HAP1 family, not a generic axial-protein domain. |
| flgk-protein | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AflgK%29+AND+%28organism_id%3A99287%29+AND+%28reviewed%3Atrue%29&amp;format=json; Reviewed gene_exact:flgK, taxon 99287; returned P0A1J5 and InterPro cross-references | supports | The single reviewed Salmonella FlgK result independently matches IPR002371. |
| prior-search | reviews/structured/; Exact target IDs in all review.yaml files | context_only | No prior canonical target assessment was found; legacy provenance is not silently treated as review coverage. |
| junction1987-scan | DOI:10.1128/jb.169.3.1168-1173.1987; Scanned page 1172, Discussion final left-column paragraph continuing at top right | supports | Gel electrophoresis estimates 10-20 HAP1 and 10-40 HAP3 per flagellum; fine junction localization was not determined. The exact eleven-each count is not measured here. |
| predecessor | reviews/structured/20261010T220818Z-flagellar-hook-filament-junction-audit/review.yaml | context_only | Immutable original observation; exact issue keys and finding identities are preserved in the successor. |
| preservation | /private/tmp/csm-review-20261010T215400Z/preservation.json | supports | Verified only four scientific records changed, all pre-existing history/review/legacy-report bytes remained unchanged, and prior in-record events and native PROPOSED status were preserved. |

## Limits And Additional Notes

- Scoped same-agent disposition of prior findings, not human scientific approval or completion of the 909-record review goal.
- Original source access tiers, snapshots and access times are retained. Historical abstract-only access is not upgraded to unseen full-text evidence; the separately inspected 1987 Discussion scan remains explicit.
- Genomic marker occurrence is not direct anatomical observation, and structural modeling is not direct observation of molecular trajectories.
- The global identifier checker skips unsupported namespaces; separately inspected exact authorities provide scoped support, not blanket certification.
- Full QC is verified CI at the exact fix commit. Final review-only PR-head and merge-queue checks remain separate publication gates.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T222210Z-flagellar-hook-filament-junction-disposition
kind: record
repository: CultureBotAI/CellStructureMech
title: 'bacterial-type flagellum hook-filament junction: finding dispositions'
started_at: '2026-10-10T22:13:38Z'
finished_at: '2026-10-10T22:22:10Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent evidence-backed verification of the exact saved findings
    after curation; separate adversarial diff pass is recorded on the PR. Not independent
    human sign-off.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Every finding in the linked predecessor is resolved in the inspected maintained
  inputs. Native scientific status remains PROPOSED.
source:
  git_revision: e5f99e3a62526a098cd8a32729c5777d48eb0396
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
  - path: data/structures/appendage/bacterial_type_flagellum.yaml
    sha256: 4e3e6bf50835a3134d50e5a20a87cdfa86e1e37c21085757402df7dd628095e6
    role: context
  - path: data/structures/appendage/bacterial_type_flagellum_hook_filament_junction.yaml
    sha256: eb3204728ca6c7b8d73ca436fb7f21a6092e25db827775efb585d16ba67a9055
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
  - path: history/records/bacterial_type_flagellum_hook_filament_junction/2026-09-09T023000Z-claude-524d01.yaml
    sha256: 861709f97bd36ee97c6228fe0e88ad727e8a707b21e1962c521925484edeb417
    role: context
  - path: history/records/bacterial_type_flagellum_hook_filament_junction/2026-09-09T024024Z-claude-1c0125.yaml
    sha256: 4afd0fb78b05cc036aa83f322f1e579931a56d5bf95d5404ef7b5371a20c3f78
    role: context
  - path: history/records/bacterial_type_flagellum_hook_filament_junction/2026-10-10T221031Z-codex-c6f753.yaml
    sha256: 431d7b5a83d33e3346a44d0b54987d18a15d79f65f6ef908bc5be9e2a20351f4
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reviews/structured/20261010T220818Z-flagellar-hook-filament-junction-audit/review.yaml
    sha256: 122f4dc90f11b7912c7923e0ddc31a4676983cb189886fbb12b1a61e35851de3
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: tests/test_flagellar_review_corrections.py
    sha256: d421acdc3f9ed08bad36b96d4897391c8c27f05306f6f178d71d8637576bfc8b
    role: context
targets:
- target_id: GO:0009422
  path: data/structures/appendage/bacterial_type_flagellum_hook_filament_junction.yaml
  label: bacterial-type flagellum hook-filament junction
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_hook_filament_junction.yaml
    role: maintained scientific record
scope:
  description: Reassessment of the exact prior finding fields, changed claim evidence
    and append-only provenance, not a new whole-record or corpus-wide assessment.
    Unchanged assertions retain the original review scope and limitations.
  selection: All findings in 20261010T220818Z-flagellar-hook-filament-junction-audit
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - GO:0009422
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - GO:0009422
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/appendage/bacterial_type_flagellum_hook_filament_junction.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation check passed. Biological support was separately reassessed
    against inspected source text.
  scope_note: 2026-10-10T22:12:34Z to 2026-10-10T22:12:37Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - GO:0009422
  command: .venv/bin/python scripts/validate_strict.py data/structures/appendage/bacterial_type_flagellum_hook_filament_junction.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation check passed. Biological support was separately reassessed
    against inspected source text.
  scope_note: 2026-10-10T22:12:37Z to 2026-10-10T22:12:41Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - GO:0009422
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/appendage/bacterial_type_flagellum_hook_filament_junction.yaml
    --report /private/tmp/csm-review-20261010T215400Z/post-checks/bacterial_type_flagellum_hook_filament_junction-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation check passed. Biological support was separately reassessed
    against inspected source text. There are no quoted snippet fields in this target;
    this is not validation of paraphrase meaning.
  scope_note: 2026-10-10T22:12:41Z to 2026-10-10T22:13:03Z; log SHA-256 573297eda56e7d9b22aaf87f339e6ec6773b660111f537ab41f0646cd1637a0e
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:0009422
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation check passed. Biological support was separately reassessed
    against inspected source text.
  scope_note: 2026-10-10T22:13:03Z to 2026-10-10T22:13:19Z; log SHA-256 453a059dea6bf1bb79107a0d2f5efc9bf8f952e10f056940483df1bb3af09972
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - GO:0009422
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation check passed. Biological support was separately reassessed
    against inspected source text.
  scope_note: 2026-10-10T22:13:19Z to 2026-10-10T22:15:06Z; log SHA-256 d10699bb2abeb0de144fe64b442a139ade489d962490ec567e25ab8301d90d66
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - GO:0009422
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation check passed. Biological support was separately reassessed
    against inspected source text.
  scope_note: 2026-10-10T22:15:06Z to 2026-10-10T22:15:28Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - GO:0009422
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation check passed. Biological support was separately reassessed
    against inspected source text. Unsupported namespaces remain explicitly skipped;
    scoped authority verification is retained in source evidence.
  scope_note: 2026-10-10T22:15:28Z to 2026-10-10T22:16:09Z; log SHA-256 4c6456cba44861f8cec5b1bca7cbe9a95b0af58c95cc855b4f14854bb589a72b
- check_id: regressions
  name: regressions
  status: passed
  required: true
  target_ids:
  - GO:0009422
  command: .venv/bin/python -m pytest -q tests/test_flagellar_review_corrections.py
    tests/test_write_validated.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation check passed. Biological support was separately reassessed
    against inspected source text.
  scope_note: 2026-10-10T22:16:09Z to 2026-10-10T22:16:56Z; log SHA-256 5d5ade60c286c78e74b3fd49c71173c18a2e77bc609dd5c44db1bfe1d0dfa29e
- check_id: reviews
  name: reviews
  status: passed
  required: true
  target_ids:
  - GO:0009422
  command: .venv/bin/python scripts/record_review.py check --base be59206109d6b2b31be9f12680e35633831c9682
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation check passed. Biological support was separately reassessed
    against inspected source text.
  scope_note: 2026-10-10T22:16:56Z to 2026-10-10T22:17:28Z; log SHA-256 dfe8dfadcc7011bc03f161fd75b7cf99b1afcc6ebb189984f0ec95d0ff0c48b9
- check_id: diff
  name: diff
  status: passed
  required: true
  target_ids:
  - GO:0009422
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation check passed. Biological support was separately reassessed
    against inspected source text.
  scope_note: 2026-10-10T22:17:28Z to 2026-10-10T22:17:29Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- check_id: qc
  name: Exact-fix-commit authoritative CI QC
  status: passed
  required: true
  target_ids:
  - GO:0009422
  command: gh run view 38090614355 --json databaseId,conclusion,headSha,event,jobs,startedAt,updatedAt,url
  exit_code: 0
  expected_exit_code: 0
  summary: Verified successful authoritative QC step on the exact inspected fix commit,
    including all corpus tests, generated-site and text-map drift checks.
  scope_note: 2026-10-10T22:14:27Z to 2026-10-10T22:20:37Z; https://github.com/CultureBotAI/CellStructureMech/actions/runs/38090614355;
    log SHA-256 9a2d142c149d2c38142b8495e73a3e8db4533350d3d3659eaa94785b1147d963
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/appendage/bacterial_type_flagellum_hook_filament_junction.yaml
  locator: Entire YAML, schema and recorded histories
  accessed_at: '2026-10-10T22:22:10Z'
  support: context_only
  summary: Re-read the changed target and complete diff against the predecessor; all
    identified claim corrections are present, with unchanged prior curation events
    and PROPOSED status.
  snapshot_sha256: eb3204728ca6c7b8d73ca436fb7f21a6092e25db827775efb585d16ba67a9055
- evidence_id: paper-01
  kind: primary_source
  reference: DOI:10.1016/S0022-2836(02)00139-0
  locator: Primary abstract, complete reported pair-association results
  accessed_at: '2026-10-10T21:55:13Z'
  snapshot_sha256: 020c2b3dbfadf8a61155070673ae3423373a4b1d3d2eb7edd0abc7cfb58f0a19
  support: supports
  summary: Only flagellin-induced HAP3 aggregation without stable binding and stable
    HAP2-HAP3 heterodimers are reported; not soluble FlgK-FlgL binding.
- evidence_id: paper-03
  kind: primary_source
  reference: DOI:10.1038/nrmicro1887
  locator: PMC author-manuscript full text, introductory organism comparison and Box
    1
  accessed_at: '2026-10-10T22:00:01Z'
  snapshot_sha256: 6e99f9e9c57ee1fd0ac73d42f6908c2509d60aafa3fc0ac57398f78088ffd68d
  support: supports
  summary: Assembly context supports the listed axial parts; Box 1 distinguishes 20-nm
    thickness from 10-15-micrometer length. It does not establish majority-Bacteria
    prevalence.
- evidence_id: paper-07
  kind: primary_source
  reference: DOI:10.1038/s41564-025-02037-0
  locator: Full text, native cap/HFJ Results, Figs. 1-6, Discussion, strain Methods
  accessed_at: '2026-10-10T21:55:23Z'
  snapshot_sha256: c8d05e1a03bf39c95b7b8e1da4b770b05c8152118e9ffafac7c088b40ced7896
  support: supports
  summary: Native Salmonella caps and junctions support five FliD and eleven each
    of FlgK/FlgL. Campylobacter prefilament caps and Salmonella assembly intermediates
    support the bounded mechanisms.
- evidence_id: paper-12
  kind: primary_source
  reference: DOI:10.1128/jb.162.1.183-189.1985
  locator: Primary abstract
  accessed_at: '2026-10-10T21:55:28Z'
  snapshot_sha256: 1ded5f31383ea5778ddc856e7fca24df6c96aae94a975a55d9f78f507f4fbc38
  support: supports
  summary: Antibody localization supports HAP layering on filamentless hooks; mature
    HAP1 junction localization was supported, while mature HAP2/HAP3 positions were
    not clarified by that procedure.
- evidence_id: paper-13
  kind: primary_source
  reference: DOI:10.1128/jb.169.3.1168-1173.1987
  locator: Primary abstract, localization and protein composition measurements
  accessed_at: '2026-10-10T21:55:30Z'
  snapshot_sha256: 98b71b6b229f42c2789df1685693ca1e46b38b9e2637b5f8f9725c16f04d2f4d
  support: supports
  summary: HAP1/HAP3 localize to the junction and HAP2 to the tip. Estimated amounts
    were 10-20 HAP1 and 10-40 HAP3, not an exact eleven each.
- evidence_id: paper-16
  kind: primary_source
  reference: DOI:10.1146/annurev.micro.57.030502.090832
  locator: Review abstract
  accessed_at: '2026-10-10T21:55:33Z'
  snapshot_sha256: 68caf42cabe3749c93733a366e2bda96e3fb414eb0f71a846df6d91eb67b7f58
  support: supports
  summary: Export through the axial channel and distal assembly are supported; fine-grained
    assembly evidence is cross-checked with accessible structural papers.
- evidence_id: paper-17
  kind: primary_source
  reference: DOI:10.3389/fmicb.2015.00023
  locator: Review full text, biochemical/genomic/structural comparison with bacterial
    flagella
  accessed_at: '2026-10-10T21:55:34Z'
  snapshot_sha256: c2cec0461a17865f7242ef36df178bfc68d00c1f1e292b75f9682a6ba5461464
  support: supports
  summary: Archaella have distinct type-IV-pilus-related architecture, not bacterial
    flagellin/FlgE/FlgKL/FliD axial structures.
- evidence_id: go-0009288
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009288
  locator: Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon
    or family metadata as applicable
  accessed_at: '2026-10-10T21:55:43Z'
  snapshot_sha256: f681e68df545139e6df14e2e60d0d507f83f373323aa09f5092914546194dbd3
  support: supports
  summary: Current authority record inspected. Gene identity is not experimental proof
    of membership.
- evidence_id: go-0009420
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009420
  locator: Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon
    or family metadata as applicable
  accessed_at: '2026-10-10T21:55:43Z'
  snapshot_sha256: 7b23f915e8a7ac61a986403d9cc5cc5793acb065a5085838cc9ecf5b94951939
  support: supports
  summary: Current authority record inspected. Gene identity is not experimental proof
    of membership.
- evidence_id: go-0009421
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009421
  locator: Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon
    or family metadata as applicable
  accessed_at: '2026-10-10T21:55:44Z'
  snapshot_sha256: 961d27af13a45b6772e74c0797a1344b4a1d9f30ac6a4eb8878fc00713a34c49
  support: supports
  summary: Current authority record inspected. Gene identity is not experimental proof
    of membership.
- evidence_id: go-0009422
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009422
  locator: Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon
    or family metadata as applicable
  accessed_at: '2026-10-10T21:55:44Z'
  snapshot_sha256: e4731ba25499f77fc1c68a40ceef802ba1d9cce069aec3ad7adb75cee136888d
  support: supports
  summary: Current authority record inspected. Gene identity is not experimental proof
    of membership.
- evidence_id: go-0009424
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009424
  locator: Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon
    or family metadata as applicable
  accessed_at: '2026-10-10T21:55:45Z'
  snapshot_sha256: faad16480ea34f9a816b9e5d4d40530337e025152568347f69d56b87192ef99a
  support: supports
  summary: Current authority record inspected. Gene identity is not experimental proof
    of membership.
- evidence_id: interpro-ipr001492
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001492/
  locator: Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon
    or family metadata as applicable
  accessed_at: '2026-10-10T21:55:47Z'
  snapshot_sha256: 412be2b849def6075db63e78f069de9051b598d879399e454c2211a5e061816c
  support: supports
  summary: Current authority record inspected. Gene identity is not experimental proof
    of membership.
- evidence_id: interpro-ipr013384
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013384/
  locator: Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon
    or family metadata as applicable
  accessed_at: '2026-10-10T21:55:47Z'
  snapshot_sha256: 2ea6dad9611ab8ca8e7e21b179c202107ff8f2bd3ad54df1f182b7c5f2953491
  support: supports
  summary: Current authority record inspected. Gene identity is not experimental proof
    of membership.
- evidence_id: uniprotkb-p16326
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P16326.json
  locator: Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon
    or family metadata as applicable
  accessed_at: '2026-10-10T21:55:50Z'
  snapshot_sha256: 70ed1e4ea94073fd96c5b745de1fd7a21523d3a69bab9e37d0e0c18bea680de5
  support: supports
  summary: Current authority record inspected. Gene identity is not experimental proof
    of membership.
- evidence_id: ncbitaxon-2
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/2.json
  locator: Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon
    or family metadata as applicable
  accessed_at: '2026-10-10T21:55:53Z'
  snapshot_sha256: 8074c9bcd59cd4da1da4bc9ec98c040bbecd52ef5c91c4c4bb9bed0f3a7cb5a9
  support: supports
  summary: Current authority record inspected. Gene identity is not experimental proof
    of membership.
- evidence_id: ncbitaxon-2157
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/2157.json
  locator: Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon
    or family metadata as applicable
  accessed_at: '2026-10-10T21:55:54Z'
  snapshot_sha256: 14f5852a1db0f9f5ef8d60e4a11c1916bf005bf549c57dd4bc860d39194a1799
  support: supports
  summary: Current authority record inspected. Gene identity is not experimental proof
    of membership.
- evidence_id: ncbitaxon-28901
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/28901.json
  locator: Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon
    or family metadata as applicable
  accessed_at: '2026-10-10T21:55:55Z'
  snapshot_sha256: aa833d5045292b85ee922673060f18f02bf5d38464232670ee7be952579fccd8
  support: supports
  summary: Current authority record inspected. Gene identity is not experimental proof
    of membership.
- evidence_id: ncbitaxon-99287
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/99287.json
  locator: Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon
    or family metadata as applicable
  accessed_at: '2026-10-10T21:55:56Z'
  snapshot_sha256: 107ebfece75c5a7147abe7547dec9166f87ff267e6cbc3f67bea9ab9df694a59
  support: supports
  summary: Current authority record inspected. Gene identity is not experimental proof
    of membership.
- evidence_id: flgk-family
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002371/
  locator: Entry type, definition and integrated signatures
  accessed_at: '2026-10-10T21:55:58Z'
  snapshot_sha256: 08a425ff425456a1f44f749f2528a31f0cd5b939194d7e294f06501cf3d1662c
  support: supports
  summary: IPR002371 is an exact FlgK/HAP1 family, not a generic axial-protein domain.
- evidence_id: flgk-protein
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AflgK%29+AND+%28organism_id%3A99287%29+AND+%28reviewed%3Atrue%29&format=json
  locator: Reviewed gene_exact:flgK, taxon 99287; returned P0A1J5 and InterPro cross-references
  accessed_at: '2026-10-10T21:55:59Z'
  snapshot_sha256: b2a1859fc99f1e8c43794656a31f2eae16501e98d097efb337c97eef73fa4d3c
  support: supports
  summary: The single reviewed Salmonella FlgK result independently matches IPR002371.
- evidence_id: prior-search
  kind: search
  reference: reviews/structured/
  locator: Exact target IDs in all review.yaml files
  accessed_at: '2026-10-10T22:08:18Z'
  support: context_only
  search_scope: Path.rglob of reviews/structured including hidden and ignored entries;
    40 canonical reviews parsed; exact target ID GO:0009422. Also rg --no-ignore --hidden
    across reviews and reports/yaml_record_review.
  summary: No prior canonical target assessment was found; legacy provenance is not
    silently treated as review coverage.
- evidence_id: junction1987-scan
  kind: primary_source
  reference: DOI:10.1128/jb.169.3.1168-1173.1987
  locator: Scanned page 1172, Discussion final left-column paragraph continuing at
    top right
  accessed_at: '2026-10-10T22:03:13Z'
  snapshot_sha256: 1081411547662daf839637f617b041277830873855c1c422501aa50968205dc5
  support: supports
  summary: Gel electrophoresis estimates 10-20 HAP1 and 10-40 HAP3 per flagellum;
    fine junction localization was not determined. The exact eleven-each count is
    not measured here.
- evidence_id: predecessor
  kind: prior_review
  reference: reviews/structured/20261010T220818Z-flagellar-hook-filament-junction-audit/review.yaml
  accessed_at: '2026-10-10T22:22:10Z'
  snapshot_sha256: 122f4dc90f11b7912c7923e0ddc31a4676983cb189886fbb12b1a61e35851de3
  support: context_only
  summary: Immutable original observation; exact issue keys and finding identities
    are preserved in the successor.
- evidence_id: preservation
  kind: validation
  reference: /private/tmp/csm-review-20261010T215400Z/preservation.json
  accessed_at: '2026-10-10T22:12:56Z'
  snapshot_sha256: feb9ed368c5790afec60f8a0280f93c51363bd7867135a5cb6b66d0a86a5f271
  support: supports
  summary: Verified only four scientific records changed, all pre-existing history/review/legacy-report
    bytes remained unchanged, and prior in-record events and native PROPOSED status
    were preserved.
assessments:
- assessment_id: resolved-f1
  area: evidence
  topic: Furukawa 2002 is cited for interactions it did not report
  outcome: supported
  target_ids:
  - GO:0009422
  evidence_ids:
  - record
  - paper-01
  - paper-07
  - predecessor
  - preservation
  summary: The affected component and contact edge now cite the 2025 assembled-junction
    structure. The older citation is retained as bounding evidence and explicitly
    does not assert FlgK-FlgL solution binding.
- assessment_id: resolved-f2
  area: evidence
  topic: Historical localization and copy-number descriptions exceed the inspected
    reports
  outcome: supported
  target_ids:
  - GO:0009422
  evidence_ids:
  - record
  - paper-12
  - paper-13
  - paper-07
  - junction1987-scan
  - predecessor
  - preservation
  summary: The 1987 notes retain approximate HAP1 10-20 and HAP3 10-40 estimates and
    the fine-localization limitation. The 1985 note distinguishes filamentless hooks
    from mature HAP3 localization. Modern layer-order evidence and species-scoped
    11:11/22 counts are retained from 2025.
- assessment_id: resolved-f3
  area: evidence
  topic: FlgK label-only status is contradicted by an exact matched family
  outcome: supported
  target_ids:
  - GO:0009422
  evidence_ids:
  - record
  - flgk-family
  - flgk-protein
  - predecessor
  - preservation
  summary: FlgK now grounds to verified IPR002371 with the reviewed Salmonella P0A1J5
    match recorded. The incompatible current label-only status is removed; its rationale
    is preserved with a dated superseding note. FlgL and the separate label-only FlgE
    decision are unchanged.
findings:
- finding_id: F1
  issue_key: flagellar-junction-flgk-flgl-soluble-interaction-miscitation
  category: evidence
  severity: major
  status: resolved
  certainty: confirmed
  title: Furukawa 2002 is cited for interactions it did not report
  description: The affected component and contact edge now cite the 2025 assembled-junction
    structure. The older citation is retained as bounding evidence and explicitly
    does not assert FlgK-FlgL solution binding.
  target_ids:
  - GO:0009422
  field_paths:
  - components[1].evidence[1]
  - causal_graphs[0].edges[3].evidence[0]
  evidence_ids:
  - record
  - paper-01
  - paper-07
  - predecessor
  - preservation
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_hook_filament_junction.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#evidence
  native_severity: major
  normalization_reason: Material unsupported scientific assertion.
  disposition_reason: The affected component and contact edge now cite the 2025 assembled-junction
    structure. The older citation is retained as bounding evidence and explicitly
    does not assert FlgK-FlgL solution binding. Exact affected fields were checked
    against the cited primary or authority evidence and passing post-curation gates.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261010T220818Z-flagellar-hook-filament-junction-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2152
- finding_id: F2
  issue_key: flagellar-junction-historical-localization-count-attribution
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  title: Historical localization and copy-number descriptions exceed the inspected
    reports
  description: The 1987 notes retain approximate HAP1 10-20 and HAP3 10-40 estimates
    and the fine-localization limitation. The 1985 note distinguishes filamentless
    hooks from mature HAP3 localization. Modern layer-order evidence and species-scoped
    11:11/22 counts are retained from 2025.
  target_ids:
  - GO:0009422
  field_paths:
  - components[0].evidence[0].notes
  - components[1].evidence[0].notes
  - functions[0].evidence[0].notes
  - causal_graphs[0].edges[0].evidence[0]
  - causal_graphs[0].edges[1].evidence[0]
  evidence_ids:
  - record
  - paper-12
  - paper-13
  - paper-07
  - junction1987-scan
  - predecessor
  - preservation
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_hook_filament_junction.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#evidence
  native_severity: minor
  normalization_reason: Bounded wording, grounding or provenance defect; identity
    otherwise remains stable.
  disposition_reason: The 1987 notes retain approximate HAP1 10-20 and HAP3 10-40
    estimates and the fine-localization limitation. The 1985 note distinguishes filamentless
    hooks from mature HAP3 localization. Modern layer-order evidence and species-scoped
    11:11/22 counts are retained from 2025. Exact affected fields were checked against
    the cited primary or authority evidence and passing post-curation gates.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261010T220818Z-flagellar-hook-filament-junction-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2153
- finding_id: F3
  issue_key: flagellar-junction-flgk-label-only-status
  category: grounding
  severity: minor
  status: resolved
  certainty: confirmed
  title: FlgK label-only status is contradicted by an exact matched family
  description: FlgK now grounds to verified IPR002371 with the reviewed Salmonella
    P0A1J5 match recorded. The incompatible current label-only status is removed;
    its rationale is preserved with a dated superseding note. FlgL and the separate
    label-only FlgE decision are unchanged.
  target_ids:
  - GO:0009422
  field_paths:
  - components[0].grounding_status
  - components[0].grounding_notes
  evidence_ids:
  - record
  - flgk-family
  - flgk-protein
  - predecessor
  - preservation
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_hook_filament_junction.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#evidence
  native_severity: minor
  normalization_reason: Bounded wording, grounding or provenance defect; identity
    otherwise remains stable.
  disposition_reason: FlgK now grounds to verified IPR002371 with the reviewed Salmonella
    P0A1J5 match recorded. The incompatible current label-only status is removed;
    its rationale is preserved with a dated superseding note. FlgL and the separate
    label-only FlgE decision are unchanged. Exact affected fields were checked against
    the cited primary or authority evidence and passing post-curation gates.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261010T220818Z-flagellar-hook-filament-junction-audit
    finding_id: F3
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2154
actions: []
limitations:
- Scoped same-agent disposition of prior findings, not human scientific approval or
  completion of the 909-record review goal.
- Original source access tiers, snapshots and access times are retained. Historical
  abstract-only access is not upgraded to unseen full-text evidence; the separately
  inspected 1987 Discussion scan remains explicit.
- Genomic marker occurrence is not direct anatomical observation, and structural modeling
  is not direct observation of molecular trajectories.
- The global identifier checker skips unsupported namespaces; separately inspected
  exact authorities provide scoped support, not blanket certification.
- Full QC is verified CI at the exact fix commit. Final review-only PR-head and merge-queue
  checks remain separate publication gates.
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261010T220818Z-flagellar-hook-filament-junction-audit
  relationship: Resolves all exact predecessor findings without rewriting the original
    observation.
links:
- https://github.com/CultureBotAI/CellStructureMech/issues/2152
- https://github.com/CultureBotAI/CellStructureMech/issues/2153
- https://github.com/CultureBotAI/CellStructureMech/issues/2154
```
