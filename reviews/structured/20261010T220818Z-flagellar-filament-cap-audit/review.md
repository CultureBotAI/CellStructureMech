# bacterial-type flagellum filament cap: scientific evidence review

- Review: 20261010T220818Z-flagellar-filament-cap-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-10T21:54:19Z
- Finished UTC: 2026-10-10T22:08:18Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

All present sections assessed against the captured inputs; supported findings below require bounded curation.

## Scope And Provenance

One complete native record, all present claims and both history surfaces; no sampling.

Selection: Next sequential unassessed target in the 909-record goal worklist: data/structures/appendage/bacterial_type_flagellum_filament_cap.yaml
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base be59206109d6b2b31be9f12680e35633831c9682.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0009421 | data/structures/appendage/bacterial_type_flagellum_filament_cap.yaml | maintained | bacterial-type flagellum filament cap |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0009421 | Documented native check passed; scientific support assessed separately. |
| strict | passed | True | GO:0009421 | Documented native check passed; scientific support assessed separately. |
| history | passed | True | GO:0009421 | Documented native check passed; scientific support assessed separately. |
| labels | passed | True | GO:0009421 | Documented native check passed; scientific support assessed separately. |
| traits | passed | True | GO:0009421 | Documented native check passed; scientific support assessed separately. Corpus-wide gate; this target has no trait links. |
| curies | passed | True | GO:0009421 | Documented native check passed; scientific support assessed separately. Unsupported namespaces are skipped by this global checker; scoped authorities were separately inspected. |
| Redundant baseline local QC | failed | False | GO:0009421 | Stopped the redundant local test run after verifying successful authoritative QC for the identical committed baseline. This local run is not a pass. |
| Exact-baseline authoritative CI QC | passed | True | GO:0009421 | Verified successful Run the authoritative quality gate step executing uv run python scripts/run_qc.py on the exact reviewed Git commit; no tracked working-tree changes. |
| imodulondb-datasets | passed | False | GO:0009421 | Structured source consulted in s_enterica/core. Gene-context hits only; no iModulon hit. FljB absence is not biological negative evidence; FliT product-text hit is not cap membership. |
| imodulondb-flid | passed | False | GO:0009421 | Structured source consulted in s_enterica/core. Gene-context hits only; no iModulon hit. FljB absence is not biological negative evidence; FliT product-text hit is not cap membership. |

## Scientific And Domain Assessments

### Identifier, definition, synonyms, granularity and parthood

identity: supported. Targets: GO:0009421.

Exact active GO cellular component, synonyms and enclosing-flagellum parthood agree. The cap and junction remain distinct adjacent structures under the recorded local boundary; GO also permits a cap-to-filament relation, which does not compel adopting a different local granularity.

### FliD membership, essentiality, grounding and examples

evidence: supported. Targets: GO:0009421.

FliD is the cap constituent; essentiality concerns cap formation, not every species needing a cap for filament formation. Grounding and protein identity match, and isolated-oligomer diversity remains bounded.

### Two functions and all six assembly edges

graph: concern. Targets: GO:0009421.

Underlying cap-mediated incorporation is supported. One note overstates the observational basis of the older domain-movement study; newer structural support does not retroactively change its methods.

### Domain distribution and canonical examples

scope: supported. Targets: GO:0009421.

VARIABLE occurrence is appropriately bounded by the presence of a bacterial flagellar system. Named bacterial examples and the distinction from archaella are supported; no all-species census is inferred.

### Every physical property and stoichiometry assertion

quantity: supported. Targets: GO:0009421.

Species-scoped count fields are distinct from broad bacterial claims. Filament dimensional wording and junction historical citation precision are findings; no unsupported optional measurements were added.

### Discussions, histories, optional sections and mapping status

provenance: supported. Targets: GO:0009421.

Every discussion and target history was read. Boundary decisions keep adjacent structures distinct; PROPOSED remains appropriate. No images, external compositions, traits, pathway links or datasets are asserted here; absent optional sections are not findings. Past events remain historical and unchanged.

## Findings

### F1: A modeled cap-growth interpretation is described as visualized growth conformations

minor / open / confirmed; issue key: flagellar-cap-2003-model-observation-wording.

The edge note says the 2003 study visualized cap-filament conformations during flagellar growth. The full Results and Fig. 5 distinguish isolated-cap microscopy from a docked cap-filament model; inferred domain rearrangements are visualized and measured in that model. The biological incorporation claim remains supported, but the note should identify modeling rather than imply directly observed growing-complex conformations.

## Recommended Actions And Acceptance Checks

### A1

Describe the 2003 source as isolated-cap imaging plus structural modeling, or add the newer direct assembly-intermediate evidence without rewriting what the old study measured.

- The older note explicitly identifies modeling; no claim of a directly observed growth sequence remains attributed to that paper.
- Use the guarded writer with both curation histories; retain PROPOSED; pass schema, strict, labels, identifiers, history and QC gates.
- Regenerate embeddings/maps only when their semantic projection changes, and regenerate pages through the documented renderer.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/bacterial_type_flagellum_filament_cap.yaml; Entire YAML, schema and recorded histories | context_only | All native sections and target repository histories inspected; unchanged input hashes and PROPOSED status retained. |
| paper-00 | DOI:10.1006/jmbi.1996.0349; Primary abstract | supports | Purified FliD forms cap-like assemblies and restores swimming to a Salmonella fliD mutant; isolated oligomers are not native copy-number measurements. |
| paper-05 | DOI:10.1038/s41467-020-16981-4; Full text, Introduction and Results cap structure and filament symmetry | supports | Full-length C. jejuni FliD forms pentamers; isolated crystallographic diversity is distinguished from native-cap architecture. |
| paper-07 | DOI:10.1038/s41564-025-02037-0; Full text, native cap/HFJ Results, Figs. 1-6, Discussion, strain Methods | supports | Native Salmonella caps and junctions support five FliD and eleven each of FlgK/FlgL. Campylobacter prefilament caps and Salmonella assembly intermediates support the bounded mechanisms. |
| paper-09 | DOI:10.1073/pnas.2534343100; PMC full text, Results Model of the Cap-Filament Complex, Fig. 5 and Discussion Possible Domain Movements | supports | Isolated-cap microscopy plus a docked model supports inferred growth-associated conformations; domain displacements were measured in the model, not a directly imaged growth sequence. |
| paper-10 | DOI:10.1099/mic.0.25948-0; Review abstract | supports | Broad comparison of distinct prokaryotic motility structures; no unseen measurements are certified. |
| paper-11 | DOI:10.1126/science.290.5499.2148; Primary abstract | supports | Cap-filament and isolated-cap microscopy motivated a rotary assembly model; inferred motion is distinguished from a direct movie of growth. |
| paper-17 | DOI:10.3389/fmicb.2015.00023; Review full text, biochemical/genomic/structural comparison with bacterial flagella | supports | Archaella have distinct type-IV-pilus-related architecture, not bacterial flagellin/FlgE/FlgKL/FliD axial structures. |
| paper-20 | DOI:10.7554/eLife.18857; Full text, Introduction, Results isolated FliD oligomers and Discussion | supports | Purified constructs show diverse oligomeric states; these do not establish variable native cap counts in every species. |
| go-0009288 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009288; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| go-0009420 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009420; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| go-0009421 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009421; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| go-0009422 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009422; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| interpro-ipr001492 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001492/; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| interpro-ipr040026 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR040026/; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| uniprotkb-p16328 | https://rest.uniprot.org/uniprotkb/P16328.json; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| ncbitaxon-197 | https://rest.uniprot.org/taxonomy/197.json; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| ncbitaxon-2 | https://rest.uniprot.org/taxonomy/2.json; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| ncbitaxon-2157 | https://rest.uniprot.org/taxonomy/2157.json; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| ncbitaxon-28901 | https://rest.uniprot.org/taxonomy/28901.json; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| ncbitaxon-99287 | https://rest.uniprot.org/taxonomy/99287.json; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| prior-search | reviews/structured/; Exact target IDs in all review.yaml files | context_only | No prior canonical target assessment was found; legacy provenance is not silently treated as review coverage. |

## Limits And Additional Notes

- Full-QC evidence is the successful authoritative CI step for the identical baseline commit. The redundant local QC test run was explicitly cancelled and is not claimed as passed. All other listed native checks ran locally.
- This is a completed scoped agent assessment, not human approval, a new experiment or completion of the 909-record goal. Findings are not yet fixed.
- Some historical papers and subscription reviews remain abstract-only; source-specific locators identify coverage. PMC HTML provided the complete 2003 cap study and 2008 assembly review after API failures. The 1987 junction Discussion scan on page 1172 was also inspected. BioC HTTP 200 error documents and HTML returned by the PDF link are not full-text evidence.
- Berg/Macnab broad review assertions are bounded by their accessible abstracts and independently inspected structural sources. Unread detailed methods, figures and numeric claims are not certified.
- Three-dimensional reconstructions and structural interpretations are not direct time-resolved observation of every molecular trajectory. Original specimen and taxon scope remain important.
- Global identifier liveness skips unsupported namespaces. Scoped GO, InterPro, UniProt and taxon records were separately checked; a successful corpus gate is not blanket authority certification.
- iModulonDB searches are gene-context cross-checks only. No module hit informed a phenotype or localization claim; missing FljB and product-text FliT hits are not biological negative/positive membership evidence.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T220818Z-flagellar-filament-cap-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'bacterial-type flagellum filament cap: scientific evidence review'
started_at: '2026-10-10T21:54:19Z'
finished_at: '2026-10-10T22:08:18Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Agent audit of existing records, not independent human approval.
    No scientific input was changed during assessment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: All present sections assessed against the captured inputs; supported findings
  below require bounded curation.
source:
  git_revision: be59206109d6b2b31be9f12680e35633831c9682
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
  - path: data/structures/appendage/bacterial_type_flagellum_filament_cap.yaml
    sha256: 5e9a31e1401116ce2b4a79723719b944976bfa6c041825fa805e9871ff02128c
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
  - path: history/records/bacterial_type_flagellum_filament_cap/2026-09-09T025452Z-claude-edfc1c.yaml
    sha256: cb74a5c73637d6d16a6ccd41e12bebfd5a5534073928db70dd5254c4b5cc1581
    role: context
  - path: history/records/bacterial_type_flagellum_filament_cap/2026-09-09T042811Z-claude-481520.yaml
    sha256: da5a1b3dab8a58b4afd291f9d9986dfe8057972560f51afba6650e306a16eb16
    role: context
  - path: history/records/bacterial_type_flagellum_filament_cap/2026-09-21T140304Z-codex-83572b.yaml
    sha256: 0228398c40c80e989b1431fff76cfc86b7a0153ec945f98342e06ddcb7cbfc11
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
- target_id: GO:0009421
  path: data/structures/appendage/bacterial_type_flagellum_filament_cap.yaml
  label: bacterial-type flagellum filament cap
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_filament_cap.yaml
    role: maintained scientific record
scope:
  description: One complete native record, all present claims and both history surfaces;
    no sampling.
  selection: 'Next sequential unassessed target in the 909-record goal worklist: data/structures/appendage/bacterial_type_flagellum_filament_cap.yaml'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0009421
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - GO:0009421
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/appendage/bacterial_type_flagellum_filament_cap.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Documented native check passed; scientific support assessed separately.
  scope_note: 2026-10-10T21:54:48Z to 2026-10-10T21:54:50Z; /private/tmp/csm-review-20261010T215400Z/checks/bacterial_type_flagellum_filament_cap-schema.log;
    SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - GO:0009421
  command: .venv/bin/python scripts/validate_strict.py data/structures/appendage/bacterial_type_flagellum_filament_cap.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Documented native check passed; scientific support assessed separately.
  scope_note: 2026-10-10T21:54:50Z to 2026-10-10T21:54:54Z; /private/tmp/csm-review-20261010T215400Z/checks/bacterial_type_flagellum_filament_cap-strict.log;
    SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:0009421
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Documented native check passed; scientific support assessed separately.
  scope_note: 2026-10-10T21:55:05Z to 2026-10-10T21:55:21Z; /private/tmp/csm-review-20261010T215400Z/checks/history.log;
    SHA-256 abfbb2717efb404ff8dee093a93f8fe33e5aeb399a96bd495dd0054c1f24460b
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - GO:0009421
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Documented native check passed; scientific support assessed separately.
  scope_note: 2026-10-10T21:55:21Z to 2026-10-10T21:57:27Z; /private/tmp/csm-review-20261010T215400Z/checks/labels.log;
    SHA-256 fb85db22c28daa12e83acf2916598842ac20181441224ad5273ae4d30fb2fa1a
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - GO:0009421
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Documented native check passed; scientific support assessed separately.
    Corpus-wide gate; this target has no trait links.
  scope_note: 2026-10-10T21:57:27Z to 2026-10-10T21:57:50Z; /private/tmp/csm-review-20261010T215400Z/checks/traits.log;
    SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - GO:0009421
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Documented native check passed; scientific support assessed separately.
    Unsupported namespaces are skipped by this global checker; scoped authorities
    were separately inspected.
  scope_note: 2026-10-10T21:57:50Z to 2026-10-10T21:58:51Z; /private/tmp/csm-review-20261010T215400Z/checks/curies.log;
    SHA-256 946174cb7e32f828267648f6cf473c1f94440f8aeb2b29a4670d591e165662cd
- check_id: local-qc-cancelled
  name: Redundant baseline local QC
  status: failed
  required: false
  target_ids:
  - GO:0009421
  command: .venv/bin/python scripts/run_qc.py
  exit_code: 241
  summary: Stopped the redundant local test run after verifying successful authoritative
    QC for the identical committed baseline. This local run is not a pass.
  scope_note: /private/tmp/csm-review-20261010T215400Z/checks/qc.log; SHA-256 36e1b947e8d3030a74ce46b9ff1135c9a555410a315b496f8d212d3f103f8979
- check_id: qc
  name: Exact-baseline authoritative CI QC
  status: passed
  required: true
  target_ids:
  - GO:0009421
  command: gh run view 38089193671 --json conclusion,headSha,event,jobs,startedAt,updatedAt,url
  exit_code: 0
  expected_exit_code: 0
  summary: Verified successful Run the authoritative quality gate step executing uv
    run python scripts/run_qc.py on the exact reviewed Git commit; no tracked working-tree
    changes.
  scope_note: 2026-10-10T21:51:38Z to 2026-10-10T21:55:50Z; https://github.com/CultureBotAI/CellStructureMech/actions/runs/38089193671;
    log SHA-256 5e9fad9070d81d98183c122a6f6c73dae87794e445f0f7719121a3fe8fbe2bdd
- check_id: imodulondb-datasets
  name: imodulondb-datasets
  status: passed
  required: false
  target_ids:
  - GO:0009421
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  exit_code: 0
  expected_exit_code: 0
  summary: Structured source consulted in s_enterica/core. Gene-context hits only;
    no iModulon hit. FljB absence is not biological negative evidence; FliT product-text
    hit is not cap membership.
  scope_note: 2026-10-10T21:56:15Z to 2026-10-10T21:56:15Z; log SHA-256 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- check_id: imodulondb-flid
  name: imodulondb-flid
  status: passed
  required: false
  target_ids:
  - GO:0009421
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism s_enterica --dataset core --query fliD
  exit_code: 0
  expected_exit_code: 0
  summary: Structured source consulted in s_enterica/core. Gene-context hits only;
    no iModulon hit. FljB absence is not biological negative evidence; FliT product-text
    hit is not cap membership.
  scope_note: 2026-10-10T21:56:16Z to 2026-10-10T21:56:17Z; log SHA-256 92aa0fb3a7470c5183938d4d65fc44f4b087442cb6eb0c0913a0c385cd3ed531
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/appendage/bacterial_type_flagellum_filament_cap.yaml
  locator: Entire YAML, schema and recorded histories
  accessed_at: '2026-10-10T22:08:18Z'
  support: context_only
  summary: All native sections and target repository histories inspected; unchanged
    input hashes and PROPOSED status retained.
- evidence_id: paper-00
  kind: primary_source
  reference: DOI:10.1006/jmbi.1996.0349
  locator: Primary abstract
  accessed_at: '2026-10-10T21:55:12Z'
  snapshot_sha256: abc9bd181bd80755b2f5b1a44666438655688a9ba9fea6a194db643fe32af33e
  support: supports
  summary: Purified FliD forms cap-like assemblies and restores swimming to a Salmonella
    fliD mutant; isolated oligomers are not native copy-number measurements.
- evidence_id: paper-05
  kind: primary_source
  reference: DOI:10.1038/s41467-020-16981-4
  locator: Full text, Introduction and Results cap structure and filament symmetry
  accessed_at: '2026-10-10T21:55:19Z'
  snapshot_sha256: a5c2acb06146a60c0a06cee131048bfec4db2142fdb40fdf241e8ec0aee647b3
  support: supports
  summary: Full-length C. jejuni FliD forms pentamers; isolated crystallographic diversity
    is distinguished from native-cap architecture.
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
- evidence_id: paper-09
  kind: primary_source
  reference: DOI:10.1073/pnas.2534343100
  locator: PMC full text, Results Model of the Cap-Filament Complex, Fig. 5 and Discussion
    Possible Domain Movements
  accessed_at: '2026-10-10T22:00:00Z'
  snapshot_sha256: 9459b193903167d5e16ad731a133889d7b850a43b44c23547c80db2934aca09c
  support: supports
  summary: Isolated-cap microscopy plus a docked model supports inferred growth-associated
    conformations; domain displacements were measured in the model, not a directly
    imaged growth sequence.
- evidence_id: paper-10
  kind: primary_source
  reference: DOI:10.1099/mic.0.25948-0
  locator: Review abstract
  accessed_at: '2026-10-10T21:55:27Z'
  snapshot_sha256: 7a922088cf46c8d785b5d1372a6bee753506b88d4243f25802bb376b026a1cf6
  support: supports
  summary: Broad comparison of distinct prokaryotic motility structures; no unseen
    measurements are certified.
- evidence_id: paper-11
  kind: primary_source
  reference: DOI:10.1126/science.290.5499.2148
  locator: Primary abstract
  accessed_at: '2026-10-10T21:55:28Z'
  snapshot_sha256: 86d7a0eb2907c4cab1b37ae9a32601e9ff1a1a17c6ecaeae9efceaad73df19eb
  support: supports
  summary: Cap-filament and isolated-cap microscopy motivated a rotary assembly model;
    inferred motion is distinguished from a direct movie of growth.
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
- evidence_id: paper-20
  kind: primary_source
  reference: DOI:10.7554/eLife.18857
  locator: Full text, Introduction, Results isolated FliD oligomers and Discussion
  accessed_at: '2026-10-10T21:55:39Z'
  snapshot_sha256: 211c9646765522fb7f3c45123622bed50520cf06a83c7cf9abd9bc24af9dcafe
  support: supports
  summary: Purified constructs show diverse oligomeric states; these do not establish
    variable native cap counts in every species.
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
- evidence_id: interpro-ipr040026
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR040026/
  locator: Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon
    or family metadata as applicable
  accessed_at: '2026-10-10T21:55:48Z'
  snapshot_sha256: 1499a9107c1ab1c8add97f66838c6f8ebc71dc71441db32db12463e04fc5b617
  support: supports
  summary: Current authority record inspected. Gene identity is not experimental proof
    of membership.
- evidence_id: uniprotkb-p16328
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P16328.json
  locator: Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon
    or family metadata as applicable
  accessed_at: '2026-10-10T21:55:51Z'
  snapshot_sha256: ee5e39f25accb24022ae6c68509ad54d527cff2da02423680f913722f959c59d
  support: supports
  summary: Current authority record inspected. Gene identity is not experimental proof
    of membership.
- evidence_id: ncbitaxon-197
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/197.json
  locator: Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon
    or family metadata as applicable
  accessed_at: '2026-10-10T21:55:53Z'
  snapshot_sha256: 7346dd32eb9f3fb96e5a5f775bb9a0dc8dc761a5dd41712b84d65f148ed90c77
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
- evidence_id: prior-search
  kind: search
  reference: reviews/structured/
  locator: Exact target IDs in all review.yaml files
  accessed_at: '2026-10-10T22:08:18Z'
  support: context_only
  search_scope: Path.rglob of reviews/structured including hidden and ignored entries;
    40 canonical reviews parsed; exact target ID GO:0009421. Also rg --no-ignore --hidden
    across reviews and reports/yaml_record_review.
  summary: No prior canonical target assessment was found; legacy provenance is not
    silently treated as review coverage.
assessments:
- assessment_id: identity
  area: identity
  topic: Identifier, definition, synonyms, granularity and parthood
  outcome: supported
  target_ids:
  - GO:0009421
  evidence_ids:
  - record
  - go-0009421
  - go-0009288
  - paper-07
  summary: Exact active GO cellular component, synonyms and enclosing-flagellum parthood
    agree. The cap and junction remain distinct adjacent structures under the recorded
    local boundary; GO also permits a cap-to-filament relation, which does not compel
    adopting a different local granularity.
- assessment_id: composition
  area: evidence
  topic: FliD membership, essentiality, grounding and examples
  outcome: supported
  target_ids:
  - GO:0009421
  evidence_ids:
  - record
  - paper-00
  - paper-05
  - paper-07
  - paper-20
  - interpro-ipr040026
  - uniprotkb-p16328
  summary: FliD is the cap constituent; essentiality concerns cap formation, not every
    species needing a cap for filament formation. Grounding and protein identity match,
    and isolated-oligomer diversity remains bounded.
  dimensions:
  - name: experimental_scope
    value: Cited bacterial model organisms and preparations; source-specific conditions
      retained
    definition: Scope of structural and assembly observations, not universal morphology
    evidence_ids:
    - paper-07
- assessment_id: functions-graph
  area: graph
  topic: Two functions and all six assembly edges
  outcome: concern
  target_ids:
  - GO:0009421
  evidence_ids:
  - record
  - paper-07
  - paper-09
  - paper-11
  summary: Underlying cap-mediated incorporation is supported. One note overstates
    the observational basis of the older domain-movement study; newer structural support
    does not retroactively change its methods.
- assessment_id: taxonomy
  area: scope
  topic: Domain distribution and canonical examples
  outcome: supported
  target_ids:
  - GO:0009421
  evidence_ids:
  - record
  - paper-07
  - paper-17
  summary: VARIABLE occurrence is appropriately bounded by the presence of a bacterial
    flagellar system. Named bacterial examples and the distinction from archaella
    are supported; no all-species census is inferred.
- assessment_id: quantities
  area: quantity
  topic: Every physical property and stoichiometry assertion
  outcome: supported
  target_ids:
  - GO:0009421
  evidence_ids:
  - record
  - paper-07
  summary: Species-scoped count fields are distinct from broad bacterial claims. Filament
    dimensional wording and junction historical citation precision are findings; no
    unsupported optional measurements were added.
- assessment_id: provenance-status
  area: provenance
  topic: Discussions, histories, optional sections and mapping status
  outcome: supported
  target_ids:
  - GO:0009421
  evidence_ids:
  - record
  - prior-search
  summary: Every discussion and target history was read. Boundary decisions keep adjacent
    structures distinct; PROPOSED remains appropriate. No images, external compositions,
    traits, pathway links or datasets are asserted here; absent optional sections
    are not findings. Past events remain historical and unchanged.
findings:
- finding_id: F1
  issue_key: flagellar-cap-2003-model-observation-wording
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: A modeled cap-growth interpretation is described as visualized growth conformations
  description: The edge note says the 2003 study visualized cap-filament conformations
    during flagellar growth. The full Results and Fig. 5 distinguish isolated-cap
    microscopy from a docked cap-filament model; inferred domain rearrangements are
    visualized and measured in that model. The biological incorporation claim remains
    supported, but the note should identify modeling rather than imply directly observed
    growing-complex conformations.
  target_ids:
  - GO:0009421
  field_paths:
  - causal_graphs[0].edges[3].evidence[0].notes
  evidence_ids:
  - record
  - paper-09
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_filament_cap.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#evidence
  native_severity: minor
  normalization_reason: Bounded wording, grounding or provenance defect; identity
    otherwise remains stable.
actions:
- action_id: A1
  description: Describe the 2003 source as isolated-cap imaging plus structural modeling,
    or add the newer direct assembly-intermediate evidence without rewriting what
    the old study measured.
  finding_ids:
  - F1
  target_ids:
  - GO:0009421
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_filament_cap.yaml
    role: maintained scientific record
  acceptance_checks:
  - The older note explicitly identifies modeling; no claim of a directly observed
    growth sequence remains attributed to that paper.
  - Use the guarded writer with both curation histories; retain PROPOSED; pass schema,
    strict, labels, identifiers, history and QC gates.
  - Regenerate embeddings/maps only when their semantic projection changes, and regenerate
    pages through the documented renderer.
  generator: Guarded record writer, append-only history, text embedding/map refresh
    if required, and just render.
limitations:
- Full-QC evidence is the successful authoritative CI step for the identical baseline
  commit. The redundant local QC test run was explicitly cancelled and is not claimed
  as passed. All other listed native checks ran locally.
- This is a completed scoped agent assessment, not human approval, a new experiment
  or completion of the 909-record goal. Findings are not yet fixed.
- Some historical papers and subscription reviews remain abstract-only; source-specific
  locators identify coverage. PMC HTML provided the complete 2003 cap study and 2008
  assembly review after API failures. The 1987 junction Discussion scan on page 1172
  was also inspected. BioC HTTP 200 error documents and HTML returned by the PDF link
  are not full-text evidence.
- Berg/Macnab broad review assertions are bounded by their accessible abstracts and
  independently inspected structural sources. Unread detailed methods, figures and
  numeric claims are not certified.
- Three-dimensional reconstructions and structural interpretations are not direct
  time-resolved observation of every molecular trajectory. Original specimen and taxon
  scope remain important.
- Global identifier liveness skips unsupported namespaces. Scoped GO, InterPro, UniProt
  and taxon records were separately checked; a successful corpus gate is not blanket
  authority certification.
- iModulonDB searches are gene-context cross-checks only. No module hit informed a
  phenotype or localization claim; missing FljB and product-text FliT hits are not
  biological negative/positive membership evidence.
```
