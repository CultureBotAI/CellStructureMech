# bacterial-type flagellum hook-filament junction: scientific evidence review

- Review: 20261010T220818Z-flagellar-hook-filament-junction-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-10T21:54:24Z
- Finished UTC: 2026-10-10T22:08:18Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

All present sections assessed against the captured inputs; supported findings below require bounded curation.

## Scope And Provenance

One complete native record, all present claims and both history surfaces; no sampling.

Selection: Next sequential unassessed target in the 909-record goal worklist: data/structures/appendage/bacterial_type_flagellum_hook_filament_junction.yaml
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base be59206109d6b2b31be9f12680e35633831c9682.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0009422 | data/structures/appendage/bacterial_type_flagellum_hook_filament_junction.yaml | maintained | bacterial-type flagellum hook-filament junction |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0009422 | Documented native check passed; scientific support assessed separately. |
| strict | passed | True | GO:0009422 | Documented native check passed; scientific support assessed separately. |
| history | passed | True | GO:0009422 | Documented native check passed; scientific support assessed separately. |
| labels | passed | True | GO:0009422 | Documented native check passed; scientific support assessed separately. |
| traits | passed | True | GO:0009422 | Documented native check passed; scientific support assessed separately. Corpus-wide gate; this target has no trait links. |
| curies | passed | True | GO:0009422 | Documented native check passed; scientific support assessed separately. Unsupported namespaces are skipped by this global checker; scoped authorities were separately inspected. |
| Redundant baseline local QC | failed | False | GO:0009422 | Stopped the redundant local test run after verifying successful authoritative QC for the identical committed baseline. This local run is not a pass. |
| Exact-baseline authoritative CI QC | passed | True | GO:0009422 | Verified successful Run the authoritative quality gate step executing uv run python scripts/run_qc.py on the exact reviewed Git commit; no tracked working-tree changes. |
| imodulondb-datasets | passed | False | GO:0009422 | Structured source consulted in s_enterica/core. Gene-context hits only; no iModulon hit. FljB absence is not biological negative evidence; FliT product-text hit is not cap membership. |
| imodulondb-flgk | passed | False | GO:0009422 | Structured source consulted in s_enterica/core. Gene-context hits only; no iModulon hit. FljB absence is not biological negative evidence; FliT product-text hit is not cap membership. |
| imodulondb-flgl | passed | False | GO:0009422 | Structured source consulted in s_enterica/core. Gene-context hits only; no iModulon hit. FljB absence is not biological negative evidence; FliT product-text hit is not cap membership. |

## Scientific And Domain Assessments

### Identifier, definition, synonyms, granularity and parthood

identity: supported. Targets: GO:0009422.

Exact active GO cellular component, synonyms and enclosing-flagellum parthood agree. The cap and junction remain distinct adjacent structures under the recorded local boundary; GO also permits a cap-to-filament relation, which does not compel adopting a different local granularity.

### FlgK/FlgL constituents, essentiality, counts and protein example

evidence: supported. Targets: GO:0009422.

Paired junction layers and constituent identities are supported; mature-junction structure is distinct from soluble monomer binding. Native counts are supported, while historical attributions need correction.

### FlgK label-only decision

grounding: concern. Targets: GO:0009422.

Exact integrated FlgK/HAP1 family IPR002371 and independently matched reviewed Salmonella P0A1J5 contradict the current label-only status.

### All three functions and eight graph edges

graph: concern. Targets: GO:0009422.

Coupling, assembly-platform and structurally interpreted buffering are supported in the cited organisms. The soluble-interaction citation is contradicted by its abstract; modern assembled contact remains supported.

### Domain distribution and canonical examples

scope: supported. Targets: GO:0009422.

VARIABLE occurrence is appropriately bounded by the presence of a bacterial flagellar system. Named bacterial examples and the distinction from archaella are supported; no all-species census is inferred.

### Every physical property and stoichiometry assertion

quantity: concern. Targets: GO:0009422.

Species-scoped count fields are distinct from broad bacterial claims. Filament dimensional wording and junction historical citation precision are findings; no unsupported optional measurements were added.

### Discussions, histories, optional sections and mapping status

provenance: supported. Targets: GO:0009422.

Every discussion and target history was read. Boundary decisions keep adjacent structures distinct; PROPOSED remains appropriate. No images, external compositions, traits, pathway links or datasets are asserted here; absent optional sections are not findings. Past events remain historical and unchanged.

## Findings

### F1: Furukawa 2002 is cited for interactions it did not report

major / open / confirmed; issue key: flagellar-junction-flgk-flgl-soluble-interaction-miscitation.

The component note attributes direct monomeric FlgK/FlgL/flagellin interactions to this study, and one edge claims detected FlgK-FlgL binding in solution. Its complete abstract instead reports only HAP3-flagellin aggregation without stable binding and HAP2-HAP3 heterodimers. HAP2 is FliD, not FlgK. Assembled-junction contact is a different, supported claim.

### F2: Historical localization and copy-number descriptions exceed the inspected reports

minor / open / confirmed; issue key: flagellar-junction-historical-localization-count-attribution.

The 1987 abstract reports approximate HAP1 and HAP3 amounts rather than eleven copies each as stated in both component evidence notes. The 1985 abstract localizes HAP layers on filamentless hooks but explicitly says mature HAP3 location was not clarified by the same procedure; the function note loses that distinction. Later evidence supports the native junction model. The scanned Discussion on page 1172 confirms both ranges and explicitly says fine junction localization was not determined; the first two graph edges also overattribute exact layer order to this study.

### F3: FlgK label-only status is contradicted by an exact matched family

minor / open / confirmed; issue key: flagellar-junction-flgk-label-only-status.

REVIEWED_LABEL_ONLY means no exact family can be asserted, but current IPR002371 specifically denotes FlgK/HAP1 and reviewed Salmonella P0A1J5 matches it. This is a stale affirmative grounding decision, not a finding merely because an optional field is empty.

## Recommended Actions And Acceptance Checks

### A1

Remove the false solution-binding attribution; resource assembled FlgK-FlgL and FlgL-filament contact to the inspected native structural study, explicitly preserving experimental context.

- No current note claims soluble FlgK-FlgL binding from Furukawa 2002.
- Native contact remains represented and supported at the component/edge level; in-solution and assembled-state evidence are not conflated.
- Use the guarded writer with both curation histories; retain PROPOSED; pass schema, strict, labels, identifiers, history and QC gates.
- Regenerate embeddings/maps only when their semantic projection changes, and regenerate pages through the documented renderer.

### A2

Correct historical notes to their reported precision and specimen state. Keep the supported Salmonella 11:11 architecture sourced to the newer reconstruction rather than falsely attributing exact counts to the older study.

- Historical count notes preserve approximate ranges, and the 1985 note distinguishes filamentless hooks from mature-junction localization.
- The species-scoped 22-subunit property remains supported; no new all-bacterial count is inferred.
- Use the guarded writer with both curation histories; retain PROPOSED; pass schema, strict, labels, identifiers, history and QC gates.
- Regenerate embeddings/maps only when their semantic projection changes, and regenerate pages through the documented renderer.
- Exact layer-order edge evidence cites the native 2025 reconstruction rather than presenting the 1987 inferred order as measured fine localization.

### A3

Reassess and add the exact matched family, retire the incompatible current label-only status, and preserve historical rationale with a dated explanation. Do not use broad axial-protein domains.

- Current InterPro family type/scope and the reviewed Salmonella match are verified.
- Existing FlgL grounding and protein example remain intact.
- Use the guarded writer with both curation histories; retain PROPOSED; pass schema, strict, labels, identifiers, history and QC gates.
- Regenerate embeddings/maps only when their semantic projection changes, and regenerate pages through the documented renderer.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/bacterial_type_flagellum_hook_filament_junction.yaml; Entire YAML, schema and recorded histories | context_only | All native sections and target repository histories inspected; unchanged input hashes and PROPOSED status retained. |
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
review_id: 20261010T220818Z-flagellar-hook-filament-junction-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'bacterial-type flagellum hook-filament junction: scientific evidence review'
started_at: '2026-10-10T21:54:24Z'
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
  - path: data/structures/appendage/bacterial_type_flagellum_hook_filament_junction.yaml
    sha256: 43bcc4841335bdd1202a06ac1f5291fcdb0843be465db4ff151ba4385f8c0dd7
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
- target_id: GO:0009422
  path: data/structures/appendage/bacterial_type_flagellum_hook_filament_junction.yaml
  label: bacterial-type flagellum hook-filament junction
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_hook_filament_junction.yaml
    role: maintained scientific record
scope:
  description: One complete native record, all present claims and both history surfaces;
    no sampling.
  selection: 'Next sequential unassessed target in the 909-record goal worklist: data/structures/appendage/bacterial_type_flagellum_hook_filament_junction.yaml'
  coverage: full
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
  summary: Documented native check passed; scientific support assessed separately.
  scope_note: 2026-10-10T21:54:59Z to 2026-10-10T21:55:02Z; /private/tmp/csm-review-20261010T215400Z/checks/bacterial_type_flagellum_hook_filament_junction-schema.log;
    SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - GO:0009422
  command: .venv/bin/python scripts/validate_strict.py data/structures/appendage/bacterial_type_flagellum_hook_filament_junction.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Documented native check passed; scientific support assessed separately.
  scope_note: 2026-10-10T21:55:02Z to 2026-10-10T21:55:05Z; /private/tmp/csm-review-20261010T215400Z/checks/bacterial_type_flagellum_hook_filament_junction-strict.log;
    SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:0009422
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
  - GO:0009422
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
  - GO:0009422
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
  - GO:0009422
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
  - GO:0009422
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
  - GO:0009422
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
  - GO:0009422
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  exit_code: 0
  expected_exit_code: 0
  summary: Structured source consulted in s_enterica/core. Gene-context hits only;
    no iModulon hit. FljB absence is not biological negative evidence; FliT product-text
    hit is not cap membership.
  scope_note: 2026-10-10T21:56:15Z to 2026-10-10T21:56:15Z; log SHA-256 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- check_id: imodulondb-flgk
  name: imodulondb-flgk
  status: passed
  required: false
  target_ids:
  - GO:0009422
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism s_enterica --dataset core --query flgK
  exit_code: 0
  expected_exit_code: 0
  summary: Structured source consulted in s_enterica/core. Gene-context hits only;
    no iModulon hit. FljB absence is not biological negative evidence; FliT product-text
    hit is not cap membership.
  scope_note: 2026-10-10T21:56:17Z to 2026-10-10T21:56:18Z; log SHA-256 7276580fcc31c3f15279197a01493ec9da5e47c68cf5d1de69b8aeaa8fb3c3c1
- check_id: imodulondb-flgl
  name: imodulondb-flgl
  status: passed
  required: false
  target_ids:
  - GO:0009422
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism s_enterica --dataset core --query flgL
  exit_code: 0
  expected_exit_code: 0
  summary: Structured source consulted in s_enterica/core. Gene-context hits only;
    no iModulon hit. FljB absence is not biological negative evidence; FliT product-text
    hit is not cap membership.
  scope_note: 2026-10-10T21:56:18Z to 2026-10-10T21:56:18Z; log SHA-256 cb992e281a1bc0ec6f49c119b77ac30aed853fc0ef2d50f7c270ed99407fdd97
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/appendage/bacterial_type_flagellum_hook_filament_junction.yaml
  locator: Entire YAML, schema and recorded histories
  accessed_at: '2026-10-10T22:08:18Z'
  support: context_only
  summary: All native sections and target repository histories inspected; unchanged
    input hashes and PROPOSED status retained.
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
assessments:
- assessment_id: identity
  area: identity
  topic: Identifier, definition, synonyms, granularity and parthood
  outcome: supported
  target_ids:
  - GO:0009422
  evidence_ids:
  - record
  - go-0009422
  - go-0009288
  - paper-07
  summary: Exact active GO cellular component, synonyms and enclosing-flagellum parthood
    agree. The cap and junction remain distinct adjacent structures under the recorded
    local boundary; GO also permits a cap-to-filament relation, which does not compel
    adopting a different local granularity.
- assessment_id: composition
  area: evidence
  topic: FlgK/FlgL constituents, essentiality, counts and protein example
  outcome: supported
  target_ids:
  - GO:0009422
  evidence_ids:
  - record
  - paper-07
  - paper-13
  - interpro-ipr013384
  - uniprotkb-p16326
  summary: Paired junction layers and constituent identities are supported; mature-junction
    structure is distinct from soluble monomer binding. Native counts are supported,
    while historical attributions need correction.
  dimensions:
  - name: experimental_scope
    value: Cited bacterial model organisms and preparations; source-specific conditions
      retained
    definition: Scope of structural and assembly observations, not universal morphology
    evidence_ids:
    - paper-07
- assessment_id: grounding
  area: grounding
  topic: FlgK label-only decision
  outcome: concern
  target_ids:
  - GO:0009422
  evidence_ids:
  - record
  - flgk-family
  - flgk-protein
  summary: Exact integrated FlgK/HAP1 family IPR002371 and independently matched reviewed
    Salmonella P0A1J5 contradict the current label-only status.
- assessment_id: functions-graph
  area: graph
  topic: All three functions and eight graph edges
  outcome: concern
  target_ids:
  - GO:0009422
  evidence_ids:
  - record
  - paper-01
  - paper-07
  - paper-12
  - paper-13
  summary: Coupling, assembly-platform and structurally interpreted buffering are
    supported in the cited organisms. The soluble-interaction citation is contradicted
    by its abstract; modern assembled contact remains supported.
- assessment_id: taxonomy
  area: scope
  topic: Domain distribution and canonical examples
  outcome: supported
  target_ids:
  - GO:0009422
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
  outcome: concern
  target_ids:
  - GO:0009422
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
  - GO:0009422
  evidence_ids:
  - record
  - prior-search
  summary: Every discussion and target history was read. Boundary decisions keep adjacent
    structures distinct; PROPOSED remains appropriate. No images, external compositions,
    traits, pathway links or datasets are asserted here; absent optional sections
    are not findings. Past events remain historical and unchanged.
findings:
- finding_id: F1
  issue_key: flagellar-junction-flgk-flgl-soluble-interaction-miscitation
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Furukawa 2002 is cited for interactions it did not report
  description: The component note attributes direct monomeric FlgK/FlgL/flagellin
    interactions to this study, and one edge claims detected FlgK-FlgL binding in
    solution. Its complete abstract instead reports only HAP3-flagellin aggregation
    without stable binding and HAP2-HAP3 heterodimers. HAP2 is FliD, not FlgK. Assembled-junction
    contact is a different, supported claim.
  target_ids:
  - GO:0009422
  field_paths:
  - components[1].evidence[1]
  - causal_graphs[0].edges[3].evidence[0]
  evidence_ids:
  - record
  - paper-01
  - paper-07
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_hook_filament_junction.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#evidence
  native_severity: major
  normalization_reason: Material unsupported scientific assertion.
- finding_id: F2
  issue_key: flagellar-junction-historical-localization-count-attribution
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Historical localization and copy-number descriptions exceed the inspected
    reports
  description: The 1987 abstract reports approximate HAP1 and HAP3 amounts rather
    than eleven copies each as stated in both component evidence notes. The 1985 abstract
    localizes HAP layers on filamentless hooks but explicitly says mature HAP3 location
    was not clarified by the same procedure; the function note loses that distinction.
    Later evidence supports the native junction model. The scanned Discussion on page
    1172 confirms both ranges and explicitly says fine junction localization was not
    determined; the first two graph edges also overattribute exact layer order to
    this study.
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
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_hook_filament_junction.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#evidence
  native_severity: minor
  normalization_reason: Bounded wording, grounding or provenance defect; identity
    otherwise remains stable.
- finding_id: F3
  issue_key: flagellar-junction-flgk-label-only-status
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: FlgK label-only status is contradicted by an exact matched family
  description: REVIEWED_LABEL_ONLY means no exact family can be asserted, but current
    IPR002371 specifically denotes FlgK/HAP1 and reviewed Salmonella P0A1J5 matches
    it. This is a stale affirmative grounding decision, not a finding merely because
    an optional field is empty.
  target_ids:
  - GO:0009422
  field_paths:
  - components[0].grounding_status
  - components[0].grounding_notes
  evidence_ids:
  - record
  - flgk-family
  - flgk-protein
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_hook_filament_junction.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#evidence
  native_severity: minor
  normalization_reason: Bounded wording, grounding or provenance defect; identity
    otherwise remains stable.
actions:
- action_id: A1
  description: Remove the false solution-binding attribution; resource assembled FlgK-FlgL
    and FlgL-filament contact to the inspected native structural study, explicitly
    preserving experimental context.
  finding_ids:
  - F1
  target_ids:
  - GO:0009422
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_hook_filament_junction.yaml
    role: maintained scientific record
  acceptance_checks:
  - No current note claims soluble FlgK-FlgL binding from Furukawa 2002.
  - Native contact remains represented and supported at the component/edge level;
    in-solution and assembled-state evidence are not conflated.
  - Use the guarded writer with both curation histories; retain PROPOSED; pass schema,
    strict, labels, identifiers, history and QC gates.
  - Regenerate embeddings/maps only when their semantic projection changes, and regenerate
    pages through the documented renderer.
  generator: Guarded record writer, append-only history, text embedding/map refresh
    if required, and just render.
- action_id: A2
  description: Correct historical notes to their reported precision and specimen state.
    Keep the supported Salmonella 11:11 architecture sourced to the newer reconstruction
    rather than falsely attributing exact counts to the older study.
  finding_ids:
  - F2
  target_ids:
  - GO:0009422
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_hook_filament_junction.yaml
    role: maintained scientific record
  acceptance_checks:
  - Historical count notes preserve approximate ranges, and the 1985 note distinguishes
    filamentless hooks from mature-junction localization.
  - The species-scoped 22-subunit property remains supported; no new all-bacterial
    count is inferred.
  - Use the guarded writer with both curation histories; retain PROPOSED; pass schema,
    strict, labels, identifiers, history and QC gates.
  - Regenerate embeddings/maps only when their semantic projection changes, and regenerate
    pages through the documented renderer.
  - Exact layer-order edge evidence cites the native 2025 reconstruction rather than
    presenting the 1987 inferred order as measured fine localization.
  generator: Guarded record writer, append-only history, text embedding/map refresh
    if required, and just render.
- action_id: A3
  description: Reassess and add the exact matched family, retire the incompatible
    current label-only status, and preserve historical rationale with a dated explanation.
    Do not use broad axial-protein domains.
  finding_ids:
  - F3
  target_ids:
  - GO:0009422
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_hook_filament_junction.yaml
    role: maintained scientific record
  acceptance_checks:
  - Current InterPro family type/scope and the reviewed Salmonella match are verified.
  - Existing FlgL grounding and protein example remain intact.
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
