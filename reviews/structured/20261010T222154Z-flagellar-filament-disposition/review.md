# bacterial-type flagellum filament: finding dispositions

- Review: 20261010T222154Z-flagellar-filament-disposition
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-10T22:13:28Z
- Finished UTC: 2026-10-10T22:21:54Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Every finding in the linked predecessor is resolved in the inspected maintained inputs. Native scientific status remains PROPOSED.

## Scope And Provenance

Reassessment of the exact prior finding fields, changed claim evidence and append-only provenance, not a new whole-record or corpus-wide assessment. Unchanged assertions retain the original review scope and limitations.

Selection: All findings in 20261010T220818Z-flagellar-filament-audit
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e5f99e3a62526a098cd8a32729c5777d48eb0396.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0009420 | data/structures/appendage/bacterial_type_flagellum_filament.yaml | maintained | bacterial-type flagellum filament |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0009420 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. |
| strict | passed | True | GO:0009420 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. |
| snippets | passed | True | GO:0009420 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. There are no quoted snippet fields in this target; this is not validation of paraphrase meaning. |
| history | passed | True | GO:0009420 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. |
| labels | passed | True | GO:0009420 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. |
| traits | passed | True | GO:0009420 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. |
| curies | passed | True | GO:0009420 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. Unsupported namespaces remain explicitly skipped; scoped authority verification is retained in source evidence. |
| regressions | passed | True | GO:0009420 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. |
| reviews | passed | True | GO:0009420 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. |
| diff | passed | True | GO:0009420 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. |
| Exact-fix-commit authoritative CI QC | passed | True | GO:0009420 | Verified successful authoritative QC step on the exact inspected fix commit, including all corpus tests, generated-site and text-map drift checks. |

## Scientific And Domain Assessments

### Three filament sources have incorrect author attribution

evidence: supported. Targets: GO:0009420.

All current notes use Blum, Halte/Erhardt and Qin with the DOI-resolved Vibrio title. Past curation-event text remains unchanged.

### Inherited definition places a nanometer dimension next to length

evidence: supported. Targets: GO:0009420.

The definition is an explicitly literature-sourced paraphrase without an ambiguous numerical aside. GO identity and external-filament scope remain unchanged; historical #230 is preserved.

### Bacteria-wide COMMON is not supported by a flagellated-lineage statement

evidence: supported. Targets: GO:0009420.

The whole-Bacteria row now uses VARIABLE. Its inspected FliPQR genome survey is explicitly not direct observation of assembled external filaments or proof of this structure in every genome.

## Findings

### F1: Three filament sources have incorrect author attribution

minor / resolved / confirmed; issue key: flagellar-filament-citation-author-title-mismatches.

All current notes use Blum, Halte/Erhardt and Qin with the DOI-resolved Vibrio title. Past curation-event text remains unchanged.

Disposition: All current notes use Blum, Halte/Erhardt and Qin with the DOI-resolved Vibrio title. Past curation-event text remains unchanged. Exact affected fields were checked against the cited primary or authority evidence and passing post-curation gates.

### F2: Inherited definition places a nanometer dimension next to length

minor / resolved / confirmed; issue key: flagellar-filament-definition-length-dimension.

The definition is an explicitly literature-sourced paraphrase without an ambiguous numerical aside. GO identity and external-filament scope remain unchanged; historical #230 is preserved.

Disposition: The definition is an explicitly literature-sourced paraphrase without an ambiguous numerical aside. GO identity and external-filament scope remain unchanged; historical #230 is preserved. Exact affected fields were checked against the cited primary or authority evidence and passing post-curation gates.

### F3: Bacteria-wide COMMON is not supported by a flagellated-lineage statement

major / resolved / confirmed; issue key: flagellar-filament-bacterial-prevalence-common.

The whole-Bacteria row now uses VARIABLE. Its inspected FliPQR genome survey is explicitly not direct observation of assembled external filaments or proof of this structure in every genome.

Disposition: The whole-Bacteria row now uses VARIABLE. Its inspected FliPQR genome survey is explicitly not direct observation of assembled external filaments or proof of this structure in every genome. Exact affected fields were checked against the cited primary or authority evidence and passing post-curation gates.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/bacterial_type_flagellum_filament.yaml; Entire YAML, schema and recorded histories | context_only | Re-read the changed target and complete diff against the predecessor; all identified claim corrections are present, with unchanged prior curation events and PROPOSED status. |
| paper-03 | DOI:10.1038/nrmicro1887; PMC author-manuscript full text, introductory organism comparison and Box 1 | supports | Assembly context supports the listed axial parts; Box 1 distinguishes 20-nm thickness from 10-15-micrometer length. It does not establish majority-Bacteria prevalence. |
| paper-06 | DOI:10.1038/s41467-026-71203-7; Full text, authors/title, Results filament reconstruction and Fig. 1 | supports | Qin and colleagues resolve a sheathed Vibrio FlaD2 filament with eleven strands. The native record misattributes this paper and changes its title. |
| paper-06-metadata | DOI:10.1038/s41467-026-71203-7; Europe PMC exact DOI, title and author list | supports | Bibliographic identity and current author list independently checked. |
| paper-07 | DOI:10.1038/s41564-025-02037-0; Full text, native cap/HFJ Results, Figs. 1-6, Discussion, strain Methods | supports | Native Salmonella caps and junctions support five FliD and eleven each of FlgK/FlgL. Campylobacter prefilament caps and Salmonella assembly intermediates support the bounded mechanisms. |
| paper-08 | DOI:10.1038/s41598-019-51440-1; Full text, author metadata, Introduction and Results in-vivo Kurthia reconstruction | supports | Blum and colleagues resolve eleven protofilaments in native Kurthia filaments. The record incorrectly attributes the study to Yonekura. |
| paper-08-metadata | DOI:10.1038/s41598-019-51440-1; Europe PMC exact DOI, title and author list | supports | Bibliographic identity and current author list independently checked. |
| paper-14 | DOI:10.1128/jcm.26.7.1367-1372.1988; Primary abstract | supports | Purified and reconstituted O157:H7 CL-56 flagellar filaments were characterized by microscopy, immunoassay and immunogold; this supports the serotype-level exemplar. |
| paper-15 | DOI:10.1146/annurev.biochem.72.121801.161737; Review abstract | supports | Helical-filament rotation generates swimming; the abstract supports the general function without certifying unseen quantitative motor details. |
| paper-16 | DOI:10.1146/annurev.micro.57.030502.090832; Review abstract | supports | Export through the axial channel and distal assembly are supported; fine-grained assembly evidence is cross-checked with accessible structural papers. |
| paper-17 | DOI:10.3389/fmicb.2015.00023; Review full text, biochemical/genomic/structural comparison with bacterial flagella | supports | Archaella have distinct type-IV-pilus-related architecture, not bacterial flagellin/FlgE/FlgKL/FliD axial structures. |
| paper-18 | DOI:10.3390/biom11020186; Review full text, author metadata and section on transport of substrates | supports | Halte and Erhardt report approximately 20,000 flagellins for a long filament. The native author attribution is incorrect; this is an approximate review-level count. |
| paper-18-metadata | DOI:10.3390/biom11020186; Europe PMC exact DOI, title and author list | supports | Bibliographic identity and current author list independently checked. |
| paper-19 | DOI:10.3390/biom9090462; Full text, Introduction, Results FlgE contacts, Methods | supports | Salmonella FlgE polyhooks support the constituent and universal-joint model. The introduction distinguishes micrometer-long filaments from nanometer-scale hook dimensions. |
| paper-21 | DOI:10.1073/pnas.2512476122; Full text, Results reference-genome survey and Methods | supports | FliPQR markers occur in about 40% of 30,238 reference genomes across 131 phyla. This genomic proxy does not measure assembled filament/hook prevalence. |
| go-0009288 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009288; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| go-0009420 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009420; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| go-0071973 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0071973; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| interpro-ipr001492 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001492/; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| uniprotkb-p06179 | https://rest.uniprot.org/uniprotkb/P06179.json; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| uniprotkb-p52616 | https://rest.uniprot.org/uniprotkb/P52616.json; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| ncbitaxon-2 | https://rest.uniprot.org/taxonomy/2.json; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| ncbitaxon-2157 | https://rest.uniprot.org/taxonomy/2157.json; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| ncbitaxon-83334 | https://rest.uniprot.org/taxonomy/83334.json; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| ncbitaxon-90371 | https://rest.uniprot.org/taxonomy/90371.json; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| ncbitaxon-99287 | https://rest.uniprot.org/taxonomy/99287.json; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| prior-search | reviews/structured/; Exact target IDs in all review.yaml files | context_only | No prior canonical target assessment was found; legacy provenance is not silently treated as review coverage. |
| predecessor | reviews/structured/20261010T220818Z-flagellar-filament-audit/review.yaml | context_only | Immutable original observation; exact issue keys and finding identities are preserved in the successor. |
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
review_id: 20261010T222154Z-flagellar-filament-disposition
kind: record
repository: CultureBotAI/CellStructureMech
title: 'bacterial-type flagellum filament: finding dispositions'
started_at: '2026-10-10T22:13:28Z'
finished_at: '2026-10-10T22:21:54Z'
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
  - path: data/structures/appendage/bacterial_type_flagellum_filament.yaml
    sha256: 9e910646b2084bb7563300b2374620bc2c1d1222a0279cdfeb9b76f05731f9c2
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
  - path: history/records/bacterial_type_flagellum_filament/2026-09-07T031257Z-claude-85c76e.yaml
    sha256: 84bd73726ddadab457de20d8290453b7d3e925d80d7ec7465afcd5c3c1ea2e4c
    role: context
  - path: history/records/bacterial_type_flagellum_filament/2026-09-09T025452Z-claude-ba2271.yaml
    sha256: 03d6c3e6c9b4c9aa9d7332ea9d025dea94861f9df9406df46659bb826f323bd6
    role: context
  - path: history/records/bacterial_type_flagellum_filament/2026-09-09T042811Z-claude-0faddc.yaml
    sha256: 10c6b382667cadb6e5a19258977c74529f192644b57e68203cc5aa49a51bb691
    role: context
  - path: history/records/bacterial_type_flagellum_filament/2026-10-10T221024Z-codex-060448.yaml
    sha256: e70611e864dc917810c4206d7dd90beccdf289cb0e3a34ca3dc9eea3dc619bce
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reviews/structured/20261010T220818Z-flagellar-filament-audit/review.yaml
    sha256: d6f052a12ba7d530cd29e6ea7d85584b116f14b79b20f0023033e97eb4c60c05
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
- target_id: GO:0009420
  path: data/structures/appendage/bacterial_type_flagellum_filament.yaml
  label: bacterial-type flagellum filament
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_filament.yaml
    role: maintained scientific record
scope:
  description: Reassessment of the exact prior finding fields, changed claim evidence
    and append-only provenance, not a new whole-record or corpus-wide assessment.
    Unchanged assertions retain the original review scope and limitations.
  selection: All findings in 20261010T220818Z-flagellar-filament-audit
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - GO:0009420
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - GO:0009420
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/appendage/bacterial_type_flagellum_filament.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation check passed. Biological support was separately reassessed
    against inspected source text.
  scope_note: 2026-10-10T22:10:56Z to 2026-10-10T22:10:59Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - GO:0009420
  command: .venv/bin/python scripts/validate_strict.py data/structures/appendage/bacterial_type_flagellum_filament.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation check passed. Biological support was separately reassessed
    against inspected source text.
  scope_note: 2026-10-10T22:10:59Z to 2026-10-10T22:11:04Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - GO:0009420
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/appendage/bacterial_type_flagellum_filament.yaml
    --report /private/tmp/csm-review-20261010T215400Z/post-checks/bacterial_type_flagellum_filament-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation check passed. Biological support was separately reassessed
    against inspected source text. There are no quoted snippet fields in this target;
    this is not validation of paraphrase meaning.
  scope_note: 2026-10-10T22:11:04Z to 2026-10-10T22:11:28Z; log SHA-256 e9099a7422bb3713b9242d22a1977b2d526497cc4e7657c68bf12b40546b41a7
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:0009420
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
  - GO:0009420
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
  - GO:0009420
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
  - GO:0009420
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
  - GO:0009420
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
  - GO:0009420
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
  - GO:0009420
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
  - GO:0009420
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
  reference: data/structures/appendage/bacterial_type_flagellum_filament.yaml
  locator: Entire YAML, schema and recorded histories
  accessed_at: '2026-10-10T22:21:54Z'
  support: context_only
  summary: Re-read the changed target and complete diff against the predecessor; all
    identified claim corrections are present, with unchanged prior curation events
    and PROPOSED status.
  snapshot_sha256: 9e910646b2084bb7563300b2374620bc2c1d1222a0279cdfeb9b76f05731f9c2
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
- evidence_id: paper-06
  kind: primary_source
  reference: DOI:10.1038/s41467-026-71203-7
  locator: Full text, authors/title, Results filament reconstruction and Fig. 1
  accessed_at: '2026-10-10T21:55:21Z'
  snapshot_sha256: a573ce570cc35f55acd52d66b132f87f6fda9e43e51ca85ac51bf4a362ec2000
  support: supports
  summary: Qin and colleagues resolve a sheathed Vibrio FlaD2 filament with eleven
    strands. The native record misattributes this paper and changes its title.
- evidence_id: paper-06-metadata
  kind: database
  reference: DOI:10.1038/s41467-026-71203-7
  locator: Europe PMC exact DOI, title and author list
  accessed_at: '2026-10-10T21:55:20Z'
  snapshot_sha256: ecd53909016b8dcb277a25a537e4c988c51194cda56b9c2e5f712a5d8f31247c
  support: supports
  summary: Bibliographic identity and current author list independently checked.
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
- evidence_id: paper-08
  kind: primary_source
  reference: DOI:10.1038/s41598-019-51440-1
  locator: Full text, author metadata, Introduction and Results in-vivo Kurthia reconstruction
  accessed_at: '2026-10-10T21:55:25Z'
  snapshot_sha256: 66f39520bc10a5b835715828e2a9938d8a8bdbc4205950e7b259531b705329e7
  support: supports
  summary: Blum and colleagues resolve eleven protofilaments in native Kurthia filaments.
    The record incorrectly attributes the study to Yonekura.
- evidence_id: paper-08-metadata
  kind: database
  reference: DOI:10.1038/s41598-019-51440-1
  locator: Europe PMC exact DOI, title and author list
  accessed_at: '2026-10-10T21:55:24Z'
  snapshot_sha256: f68d778c210a6877685797978fd1e701e9c2a178dc8651e193e59159c99fe016
  support: supports
  summary: Bibliographic identity and current author list independently checked.
- evidence_id: paper-14
  kind: primary_source
  reference: DOI:10.1128/jcm.26.7.1367-1372.1988
  locator: Primary abstract
  accessed_at: '2026-10-10T21:55:31Z'
  snapshot_sha256: 6af1b9c29e4e754c21205be354e7e195096126d7ffcb895124581b8544382536
  support: supports
  summary: Purified and reconstituted O157:H7 CL-56 flagellar filaments were characterized
    by microscopy, immunoassay and immunogold; this supports the serotype-level exemplar.
- evidence_id: paper-15
  kind: primary_source
  reference: DOI:10.1146/annurev.biochem.72.121801.161737
  locator: Review abstract
  accessed_at: '2026-10-10T21:55:32Z'
  snapshot_sha256: 4c2938da11aeddedf2691f6bca3667182d4a49446eaf8bc12de59bf84c81ac9a
  support: supports
  summary: Helical-filament rotation generates swimming; the abstract supports the
    general function without certifying unseen quantitative motor details.
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
- evidence_id: paper-18
  kind: primary_source
  reference: DOI:10.3390/biom11020186
  locator: Review full text, author metadata and section on transport of substrates
  accessed_at: '2026-10-10T21:55:36Z'
  snapshot_sha256: 2f4a7d1f075cdd8f454d354c31192a07f9373119e2cfd15a8d24fe2aaca7e911
  support: supports
  summary: Halte and Erhardt report approximately 20,000 flagellins for a long filament.
    The native author attribution is incorrect; this is an approximate review-level
    count.
- evidence_id: paper-18-metadata
  kind: database
  reference: DOI:10.3390/biom11020186
  locator: Europe PMC exact DOI, title and author list
  accessed_at: '2026-10-10T21:55:35Z'
  snapshot_sha256: be4a6f64fbc1de25ec45b9ccf4883536a928f52ce28077dd2953fb910afa29bb
  support: supports
  summary: Bibliographic identity and current author list independently checked.
- evidence_id: paper-19
  kind: primary_source
  reference: DOI:10.3390/biom9090462
  locator: Full text, Introduction, Results FlgE contacts, Methods
  accessed_at: '2026-10-10T21:55:38Z'
  snapshot_sha256: 62513de500f132421593c72d0d62975e2b168cbf9d6156c8fd36216121118f82
  support: supports
  summary: Salmonella FlgE polyhooks support the constituent and universal-joint model.
    The introduction distinguishes micrometer-long filaments from nanometer-scale
    hook dimensions.
- evidence_id: paper-21
  kind: primary_source
  reference: DOI:10.1073/pnas.2512476122
  locator: Full text, Results reference-genome survey and Methods
  accessed_at: '2026-10-10T21:55:42Z'
  snapshot_sha256: 6cedc1bf8fd502b010e3123a8cd40e566506804de364f6d959a52120457af9f6
  support: supports
  summary: FliPQR markers occur in about 40% of 30,238 reference genomes across 131
    phyla. This genomic proxy does not measure assembled filament/hook prevalence.
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
- evidence_id: go-0071973
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0071973
  locator: Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon
    or family metadata as applicable
  accessed_at: '2026-10-10T21:55:46Z'
  snapshot_sha256: 4524f50c1c85dc83f482e61a3f8530fb9a760453ef399c9c04194f642c9d04e6
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
- evidence_id: uniprotkb-p06179
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P06179.json
  locator: Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon
    or family metadata as applicable
  accessed_at: '2026-10-10T21:55:49Z'
  snapshot_sha256: d7581a1c33bae41b8a5cad7676fd290f48e49b783f129bf544ac125d5801a450
  support: supports
  summary: Current authority record inspected. Gene identity is not experimental proof
    of membership.
- evidence_id: uniprotkb-p52616
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P52616.json
  locator: Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon
    or family metadata as applicable
  accessed_at: '2026-10-10T21:55:52Z'
  snapshot_sha256: 795005e3625a12dbc336b1a68b72ede793ade300c94abb8335cae3db9c5219b0
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
- evidence_id: ncbitaxon-83334
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/83334.json
  locator: Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon
    or family metadata as applicable
  accessed_at: '2026-10-10T21:55:55Z'
  snapshot_sha256: 8a22ae71ff5a8b8fac877f045fcd02598ec70eb7de80210bffb02068293a7de9
  support: supports
  summary: Current authority record inspected. Gene identity is not experimental proof
    of membership.
- evidence_id: ncbitaxon-90371
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/90371.json
  locator: Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon
    or family metadata as applicable
  accessed_at: '2026-10-10T21:55:56Z'
  snapshot_sha256: 46c958747209e78a835996643e63aafb6d1e94a8a632f0094dba733eb1bd3dee
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
- evidence_id: prior-search
  kind: search
  reference: reviews/structured/
  locator: Exact target IDs in all review.yaml files
  accessed_at: '2026-10-10T22:08:18Z'
  support: context_only
  search_scope: Path.rglob of reviews/structured including hidden and ignored entries;
    40 canonical reviews parsed; exact target ID GO:0009420. Also rg --no-ignore --hidden
    across reviews and reports/yaml_record_review.
  summary: No prior canonical target assessment was found; legacy provenance is not
    silently treated as review coverage.
- evidence_id: predecessor
  kind: prior_review
  reference: reviews/structured/20261010T220818Z-flagellar-filament-audit/review.yaml
  accessed_at: '2026-10-10T22:21:54Z'
  snapshot_sha256: d6f052a12ba7d530cd29e6ea7d85584b116f14b79b20f0023033e97eb4c60c05
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
  topic: Three filament sources have incorrect author attribution
  outcome: supported
  target_ids:
  - GO:0009420
  evidence_ids:
  - record
  - paper-06-metadata
  - paper-08-metadata
  - paper-18-metadata
  - predecessor
  - preservation
  summary: All current notes use Blum, Halte/Erhardt and Qin with the DOI-resolved
    Vibrio title. Past curation-event text remains unchanged.
- assessment_id: resolved-f2
  area: evidence
  topic: Inherited definition places a nanometer dimension next to length
  outcome: supported
  target_ids:
  - GO:0009420
  evidence_ids:
  - record
  - go-0009420
  - paper-03
  - paper-19
  - predecessor
  - preservation
  summary: 'The definition is an explicitly literature-sourced paraphrase without
    an ambiguous numerical aside. GO identity and external-filament scope remain unchanged;
    historical #230 is preserved.'
- assessment_id: resolved-f3
  area: evidence
  topic: Bacteria-wide COMMON is not supported by a flagellated-lineage statement
  outcome: supported
  target_ids:
  - GO:0009420
  evidence_ids:
  - record
  - paper-03
  - paper-21
  - predecessor
  - preservation
  summary: The whole-Bacteria row now uses VARIABLE. Its inspected FliPQR genome survey
    is explicitly not direct observation of assembled external filaments or proof
    of this structure in every genome.
findings:
- finding_id: F1
  issue_key: flagellar-filament-citation-author-title-mismatches
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  title: Three filament sources have incorrect author attribution
  description: All current notes use Blum, Halte/Erhardt and Qin with the DOI-resolved
    Vibrio title. Past curation-event text remains unchanged.
  target_ids:
  - GO:0009420
  field_paths:
  - components[0].evidence[1:4].notes
  - evidence[2:4].notes
  - causal_graphs[0].edges[0:2].evidence
  evidence_ids:
  - record
  - paper-06-metadata
  - paper-08-metadata
  - paper-18-metadata
  - predecessor
  - preservation
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_filament.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#evidence
  native_severity: minor
  normalization_reason: Bounded wording, grounding or provenance defect; identity
    otherwise remains stable.
  disposition_reason: All current notes use Blum, Halte/Erhardt and Qin with the DOI-resolved
    Vibrio title. Past curation-event text remains unchanged. Exact affected fields
    were checked against the cited primary or authority evidence and passing post-curation
    gates.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261010T220818Z-flagellar-filament-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2147
- finding_id: F2
  issue_key: flagellar-filament-definition-length-dimension
  category: quantity
  severity: minor
  status: resolved
  certainty: confirmed
  title: Inherited definition places a nanometer dimension next to length
  description: 'The definition is an explicitly literature-sourced paraphrase without
    an ambiguous numerical aside. GO identity and external-filament scope remain unchanged;
    historical #230 is preserved.'
  target_ids:
  - GO:0009420
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - record
  - go-0009420
  - paper-03
  - paper-19
  - predecessor
  - preservation
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_filament.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#evidence
  native_severity: minor
  normalization_reason: Bounded wording, grounding or provenance defect; identity
    otherwise remains stable.
  disposition_reason: 'The definition is an explicitly literature-sourced paraphrase
    without an ambiguous numerical aside. GO identity and external-filament scope
    remain unchanged; historical #230 is preserved. Exact affected fields were checked
    against the cited primary or authority evidence and passing post-curation gates.'
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261010T220818Z-flagellar-filament-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2148
- finding_id: F3
  issue_key: flagellar-filament-bacterial-prevalence-common
  category: scope
  severity: major
  status: resolved
  certainty: confirmed
  title: Bacteria-wide COMMON is not supported by a flagellated-lineage statement
  description: The whole-Bacteria row now uses VARIABLE. Its inspected FliPQR genome
    survey is explicitly not direct observation of assembled external filaments or
    proof of this structure in every genome.
  target_ids:
  - GO:0009420
  field_paths:
  - taxonomic_distribution[0].presence
  - taxonomic_distribution[0].reference
  evidence_ids:
  - record
  - paper-03
  - paper-21
  - predecessor
  - preservation
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_filament.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#evidence
  native_severity: major
  normalization_reason: Material unsupported scientific assertion.
  disposition_reason: The whole-Bacteria row now uses VARIABLE. Its inspected FliPQR
    genome survey is explicitly not direct observation of assembled external filaments
    or proof of this structure in every genome. Exact affected fields were checked
    against the cited primary or authority evidence and passing post-curation gates.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261010T220818Z-flagellar-filament-audit
    finding_id: F3
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2149
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
  review_id: 20261010T220818Z-flagellar-filament-audit
  relationship: Resolves all exact predecessor findings without rewriting the original
    observation.
links:
- https://github.com/CultureBotAI/CellStructureMech/issues/2147
- https://github.com/CultureBotAI/CellStructureMech/issues/2148
- https://github.com/CultureBotAI/CellStructureMech/issues/2149
```
