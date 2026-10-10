# bacterial-type flagellum hook: scientific evidence review

- Review: 20261010T220818Z-flagellar-hook-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-10T21:54:22Z
- Finished UTC: 2026-10-10T22:08:18Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

All present sections assessed against the captured inputs; supported findings below require bounded curation.

## Scope And Provenance

One complete native record, all present claims and both history surfaces; no sampling.

Selection: Next sequential unassessed target in the 909-record goal worklist: data/structures/appendage/bacterial_type_flagellum_hook.yaml
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base be59206109d6b2b31be9f12680e35633831c9682.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0009424 | data/structures/appendage/bacterial_type_flagellum_hook.yaml | maintained | bacterial-type flagellum hook |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0009424 | Documented native check passed; scientific support assessed separately. |
| strict | passed | True | GO:0009424 | Documented native check passed; scientific support assessed separately. |
| history | passed | True | GO:0009424 | Documented native check passed; scientific support assessed separately. |
| labels | passed | True | GO:0009424 | Documented native check passed; scientific support assessed separately. |
| traits | passed | True | GO:0009424 | Documented native check passed; scientific support assessed separately. Corpus-wide gate; this target has no trait links. |
| curies | passed | True | GO:0009424 | Documented native check passed; scientific support assessed separately. Unsupported namespaces are skipped by this global checker; scoped authorities were separately inspected. |
| Redundant baseline local QC | failed | False | GO:0009424 | Stopped the redundant local test run after verifying successful authoritative QC for the identical committed baseline. This local run is not a pass. |
| Exact-baseline authoritative CI QC | passed | True | GO:0009424 | Verified successful Run the authoritative quality gate step executing uv run python scripts/run_qc.py on the exact reviewed Git commit; no tracked working-tree changes. |
| imodulondb-datasets | passed | False | GO:0009424 | Structured source consulted in s_enterica/core. Gene-context hits only; no iModulon hit. FljB absence is not biological negative evidence; FliT product-text hit is not cap membership. |
| imodulondb-flge | passed | False | GO:0009424 | Structured source consulted in s_enterica/core. Gene-context hits only; no iModulon hit. FljB absence is not biological negative evidence; FliT product-text hit is not cap membership. |

## Scientific And Domain Assessments

### Identifier, definition, synonyms, granularity and parthood

identity: supported. Targets: GO:0009424.

Exact active GO cellular component, synonyms and enclosing-flagellum parthood agree. The cap and junction remain distinct adjacent structures under the recorded local boundary; GO also permits a cap-to-filament relation, which does not compel adopting a different local granularity.

### FlgE constituent, protein example and cross-taxon grounding decision

evidence: supported. Targets: GO:0009424.

FlgE forms the hook tube in both cited species. The Salmonella example lacks the narrow Campylobacter-family match; the retained label-only decision is justified. Broad FlgE/F/G must not replace it.

### Universal-joint function and all nine graph edges

graph: supported. Targets: GO:0009424.

Every edge retains the distinction between structural contacts, flexible coupling, transmitted rotation and motility. Structural interpretation supports universal-joint mechanics without treating it as a direct time-resolved movie.

### Both domain rows and canonical organisms

scope: concern. Targets: GO:0009424.

Named bacterial exemplars and distinction from archaella are supported. COMMON at the whole-Bacteria denominator is not justified by conditioning the prose on flagellated lineages. Genomic marker prevalence is not anatomical prevalence.

### Every physical property and stoichiometry assertion

quantity: not_applicable. Targets: GO:0009424.

Species-scoped count fields are distinct from broad bacterial claims. Filament dimensional wording and junction historical citation precision are findings; no unsupported optional measurements were added.

### Discussions, histories, optional sections and mapping status

provenance: supported. Targets: GO:0009424.

Every discussion and target history was read. Boundary decisions keep adjacent structures distinct; PROPOSED remains appropriate. No images, external compositions, traits, pathway links or datasets are asserted here; absent optional sections are not findings. Past events remain historical and unchanged.

## Findings

### F1: Bacteria-wide COMMON is not supported by a flagellated-lineage statement

major / open / confirmed; issue key: flagellar-hook-bacterial-prevalence-common.

The native enum means present in most members with exceptional losses. The note describes already-flagellated bacteria instead, while the accessed assembly-review material does not establish a majority of all Bacteria. The independent reference-genome survey supports patchy occurrence but is not a direct anatomy census.

## Recommended Actions And Acceptance Checks

### A1

Use VARIABLE or a narrower evidence-backed taxon scope, with explicit genomic-proxy limits. Preserve the bacterial/archaellum distinction and avoid treating marker absence as proof of anatomical absence.

- No majority-Bacteria assertion remains without a suitable denominator-bearing source.
- Evidence explicitly distinguishes sampled genomes, flagellar markers and assembled structures.
- Use the guarded writer with both curation histories; retain PROPOSED; pass schema, strict, labels, identifiers, history and QC gates.
- Regenerate embeddings/maps only when their semantic projection changes, and regenerate pages through the documented renderer.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/bacterial_type_flagellum_hook.yaml; Entire YAML, schema and recorded histories | context_only | All native sections and target repository histories inspected; unchanged input hashes and PROPOSED status retained. |
| paper-02 | DOI:10.1038/ncomms13425; Full text, Results hook architecture and FlgE interfaces; Methods sample | supports | C. jejuni 81116-derived fliK mutant polyhooks resolve a FlgE tube; this supports the listed constituent and species exemplar. |
| paper-03 | DOI:10.1038/nrmicro1887; PMC author-manuscript full text, introductory organism comparison and Box 1 | supports | Assembly context supports the listed axial parts; Box 1 distinguishes 20-nm thickness from 10-15-micrometer length. It does not establish majority-Bacteria prevalence. |
| paper-04 | DOI:10.1038/s41467-019-13252-9; Full text, Results/Discussion universal-joint model and Methods | supports | Salmonella SJW880 polyhook reconstruction supports torsional rigidity with bending flexibility and hook-to-filament coupling. |
| paper-07 | DOI:10.1038/s41564-025-02037-0; Full text, native cap/HFJ Results, Figs. 1-6, Discussion, strain Methods | supports | Native Salmonella caps and junctions support five FliD and eleven each of FlgK/FlgL. Campylobacter prefilament caps and Salmonella assembly intermediates support the bounded mechanisms. |
| paper-15 | DOI:10.1146/annurev.biochem.72.121801.161737; Review abstract | supports | Helical-filament rotation generates swimming; the abstract supports the general function without certifying unseen quantitative motor details. |
| paper-16 | DOI:10.1146/annurev.micro.57.030502.090832; Review abstract | supports | Export through the axial channel and distal assembly are supported; fine-grained assembly evidence is cross-checked with accessible structural papers. |
| paper-17 | DOI:10.3389/fmicb.2015.00023; Review full text, biochemical/genomic/structural comparison with bacterial flagella | supports | Archaella have distinct type-IV-pilus-related architecture, not bacterial flagellin/FlgE/FlgKL/FliD axial structures. |
| paper-19 | DOI:10.3390/biom9090462; Full text, Introduction, Results FlgE contacts, Methods | supports | Salmonella FlgE polyhooks support the constituent and universal-joint model. The introduction distinguishes micrometer-long filaments from nanometer-scale hook dimensions. |
| paper-21 | DOI:10.1073/pnas.2512476122; Full text, Results reference-genome survey and Methods | supports | FliPQR markers occur in about 40% of 30,238 reference genomes across 131 phyla. This genomic proxy does not measure assembled filament/hook prevalence. |
| go-0009288 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009288; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| go-0009420 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009420; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| go-0009424 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009424; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| go-0009425 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009425; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| go-0071973 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0071973; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| uniprotkb-p0a1j1 | https://rest.uniprot.org/uniprotkb/P0A1J1.json; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| ncbitaxon-197 | https://rest.uniprot.org/taxonomy/197.json; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| ncbitaxon-2 | https://rest.uniprot.org/taxonomy/2.json; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| ncbitaxon-2157 | https://rest.uniprot.org/taxonomy/2157.json; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| ncbitaxon-90371 | https://rest.uniprot.org/taxonomy/90371.json; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| ncbitaxon-99287 | https://rest.uniprot.org/taxonomy/99287.json; Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon or family metadata as applicable | supports | Current authority record inspected. Gene identity is not experimental proof of membership. |
| ipr020013 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020013/; Family scope, integrated signatures and description | supports | Broad FlgE/F/G family and narrow epsilonproteobacterial FlgE family do not justify a common exact grounding for the declared cross-taxon hook scope. |
| ipr012835 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012835/; Family scope, integrated signatures and description | supports | Broad FlgE/F/G family and narrow epsilonproteobacterial FlgE family do not justify a common exact grounding for the declared cross-taxon hook scope. |
| prior-search | reviews/structured/; Exact target IDs in all review.yaml files | context_only | No prior canonical target assessment was found; legacy provenance is not silently treated as review coverage. |

## Limits And Additional Notes

- Full-QC evidence is the successful authoritative CI step for the identical baseline commit. The redundant local QC test run was explicitly cancelled and is not claimed as passed. All other listed native checks ran locally.
- This is a completed scoped agent assessment, not human approval, a new experiment or completion of the 909-record goal. Findings are not yet fixed.
- Some historical papers and subscription reviews remain abstract-only; source-specific locators identify coverage. PMC HTML provided the complete 2003 cap study and 2008 assembly review after API failures. The 1987 junction Discussion scan on page 1172 was also inspected. BioC HTTP 200 error documents and HTML returned by the PDF link are not full-text evidence.
- Berg/Macnab broad review assertions are bounded by their accessible abstracts and independently inspected structural sources. Unread detailed methods, figures and numeric claims are not certified.
- Three-dimensional reconstructions and structural interpretations are not direct time-resolved observation of every molecular trajectory. Original specimen and taxon scope remain important.
- Global identifier liveness skips unsupported namespaces. Scoped GO, InterPro, UniProt and taxon records were separately checked; a successful corpus gate is not blanket authority certification.
- iModulonDB searches are gene-context cross-checks only. No module hit informed a phenotype or localization claim; missing FljB and product-text FliT hits are not biological negative/positive membership evidence.
- The distribution study uses FliPQR markers in reference genomes; it is neither microscopy of this structure nor an unbiased census of bacterial cells or species.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T220818Z-flagellar-hook-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'bacterial-type flagellum hook: scientific evidence review'
started_at: '2026-10-10T21:54:22Z'
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
  - path: data/structures/appendage/bacterial_type_flagellum_hook.yaml
    sha256: 5e0788121b9e983c3e780febed02f18fa1a617998a5d228cdfb382cb81c63278
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
  - path: history/records/bacterial_type_flagellum_hook/2026-09-07T033500Z-claude-e75791.yaml
    sha256: 4585751e89670f4efbb3c9122fecd5627d318ea8e374ffd08798080e30bcc806
    role: context
  - path: history/records/bacterial_type_flagellum_hook/2026-09-07T041813Z-claude-code-259069.yaml
    sha256: dfa0423275b07e1893248371fb344d74174583c0ebc49b44dc5ea64da2b73d12
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
- target_id: GO:0009424
  path: data/structures/appendage/bacterial_type_flagellum_hook.yaml
  label: bacterial-type flagellum hook
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_hook.yaml
    role: maintained scientific record
scope:
  description: One complete native record, all present claims and both history surfaces;
    no sampling.
  selection: 'Next sequential unassessed target in the 909-record goal worklist: data/structures/appendage/bacterial_type_flagellum_hook.yaml'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0009424
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - GO:0009424
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/appendage/bacterial_type_flagellum_hook.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Documented native check passed; scientific support assessed separately.
  scope_note: 2026-10-10T21:54:54Z to 2026-10-10T21:54:56Z; /private/tmp/csm-review-20261010T215400Z/checks/bacterial_type_flagellum_hook-schema.log;
    SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - GO:0009424
  command: .venv/bin/python scripts/validate_strict.py data/structures/appendage/bacterial_type_flagellum_hook.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Documented native check passed; scientific support assessed separately.
  scope_note: 2026-10-10T21:54:56Z to 2026-10-10T21:54:59Z; /private/tmp/csm-review-20261010T215400Z/checks/bacterial_type_flagellum_hook-strict.log;
    SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:0009424
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
  - GO:0009424
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
  - GO:0009424
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
  - GO:0009424
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
  - GO:0009424
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
  - GO:0009424
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
  - GO:0009424
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  exit_code: 0
  expected_exit_code: 0
  summary: Structured source consulted in s_enterica/core. Gene-context hits only;
    no iModulon hit. FljB absence is not biological negative evidence; FliT product-text
    hit is not cap membership.
  scope_note: 2026-10-10T21:56:15Z to 2026-10-10T21:56:15Z; log SHA-256 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- check_id: imodulondb-flge
  name: imodulondb-flge
  status: passed
  required: false
  target_ids:
  - GO:0009424
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism s_enterica --dataset core --query flgE
  exit_code: 0
  expected_exit_code: 0
  summary: Structured source consulted in s_enterica/core. Gene-context hits only;
    no iModulon hit. FljB absence is not biological negative evidence; FliT product-text
    hit is not cap membership.
  scope_note: 2026-10-10T21:56:17Z to 2026-10-10T21:56:17Z; log SHA-256 9e64aae7c7042264d7533ac32ab160a03135d96490151407cf2398a907048b81
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/appendage/bacterial_type_flagellum_hook.yaml
  locator: Entire YAML, schema and recorded histories
  accessed_at: '2026-10-10T22:08:18Z'
  support: context_only
  summary: All native sections and target repository histories inspected; unchanged
    input hashes and PROPOSED status retained.
- evidence_id: paper-02
  kind: primary_source
  reference: DOI:10.1038/ncomms13425
  locator: Full text, Results hook architecture and FlgE interfaces; Methods sample
  accessed_at: '2026-10-10T21:55:14Z'
  snapshot_sha256: d024d1c3daf01c30c16d49cd5f3e356b75b1f31df9ef292040490b6a07bc2df0
  support: supports
  summary: C. jejuni 81116-derived fliK mutant polyhooks resolve a FlgE tube; this
    supports the listed constituent and species exemplar.
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
- evidence_id: paper-04
  kind: primary_source
  reference: DOI:10.1038/s41467-019-13252-9
  locator: Full text, Results/Discussion universal-joint model and Methods
  accessed_at: '2026-10-10T21:55:17Z'
  snapshot_sha256: 79b9ff864d5ced183bf60bfbc9f8b7111f550efd2eb792443aed96df4d020d98
  support: supports
  summary: Salmonella SJW880 polyhook reconstruction supports torsional rigidity with
    bending flexibility and hook-to-filament coupling.
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
- evidence_id: go-0009425
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009425
  locator: Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon
    or family metadata as applicable
  accessed_at: '2026-10-10T21:55:46Z'
  snapshot_sha256: 9fce7e21efecbd6edee814457befdcbf6d3ae546aaefe4cc9aa56657b40e75c3
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
- evidence_id: uniprotkb-p0a1j1
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0A1J1.json
  locator: Exact identity, active/reviewed status, definition, typed synonyms, gene/taxon
    or family metadata as applicable
  accessed_at: '2026-10-10T21:55:49Z'
  snapshot_sha256: d38958f6bab34260fde99a0597b66dbca9ceb127a06edc6287965aed4daa146d
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
- evidence_id: ipr020013
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020013/
  locator: Family scope, integrated signatures and description
  accessed_at: '2026-10-10T21:55:57Z'
  snapshot_sha256: edb69e1603a4fc1dcbf4cfa68c1a7d8a1298965e9adc73fb85731123c63a648d
  support: supports
  summary: Broad FlgE/F/G family and narrow epsilonproteobacterial FlgE family do
    not justify a common exact grounding for the declared cross-taxon hook scope.
- evidence_id: ipr012835
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012835/
  locator: Family scope, integrated signatures and description
  accessed_at: '2026-10-10T21:55:57Z'
  snapshot_sha256: 4dd654200d0e65e518424ba3acb2e02e3f3de33f3f4bb8b4da1718efa678e04d
  support: supports
  summary: Broad FlgE/F/G family and narrow epsilonproteobacterial FlgE family do
    not justify a common exact grounding for the declared cross-taxon hook scope.
- evidence_id: prior-search
  kind: search
  reference: reviews/structured/
  locator: Exact target IDs in all review.yaml files
  accessed_at: '2026-10-10T22:08:18Z'
  support: context_only
  search_scope: Path.rglob of reviews/structured including hidden and ignored entries;
    40 canonical reviews parsed; exact target ID GO:0009424. Also rg --no-ignore --hidden
    across reviews and reports/yaml_record_review.
  summary: No prior canonical target assessment was found; legacy provenance is not
    silently treated as review coverage.
assessments:
- assessment_id: identity
  area: identity
  topic: Identifier, definition, synonyms, granularity and parthood
  outcome: supported
  target_ids:
  - GO:0009424
  evidence_ids:
  - record
  - go-0009424
  - go-0009288
  - paper-07
  summary: Exact active GO cellular component, synonyms and enclosing-flagellum parthood
    agree. The cap and junction remain distinct adjacent structures under the recorded
    local boundary; GO also permits a cap-to-filament relation, which does not compel
    adopting a different local granularity.
- assessment_id: composition
  area: evidence
  topic: FlgE constituent, protein example and cross-taxon grounding decision
  outcome: supported
  target_ids:
  - GO:0009424
  evidence_ids:
  - record
  - paper-02
  - paper-04
  - paper-19
  - uniprotkb-p0a1j1
  - ipr020013
  - ipr012835
  summary: FlgE forms the hook tube in both cited species. The Salmonella example
    lacks the narrow Campylobacter-family match; the retained label-only decision
    is justified. Broad FlgE/F/G must not replace it.
  dimensions:
  - name: experimental_scope
    value: Cited bacterial model organisms and preparations; source-specific conditions
      retained
    definition: Scope of structural and assembly observations, not universal morphology
    evidence_ids:
    - paper-07
- assessment_id: functions-graph
  area: graph
  topic: Universal-joint function and all nine graph edges
  outcome: supported
  target_ids:
  - GO:0009424
  evidence_ids:
  - record
  - paper-02
  - paper-04
  - paper-19
  - paper-15
  - paper-16
  summary: Every edge retains the distinction between structural contacts, flexible
    coupling, transmitted rotation and motility. Structural interpretation supports
    universal-joint mechanics without treating it as a direct time-resolved movie.
- assessment_id: taxonomy
  area: scope
  topic: Both domain rows and canonical organisms
  outcome: concern
  target_ids:
  - GO:0009424
  evidence_ids:
  - record
  - paper-03
  - paper-17
  - paper-21
  summary: Named bacterial exemplars and distinction from archaella are supported.
    COMMON at the whole-Bacteria denominator is not justified by conditioning the
    prose on flagellated lineages. Genomic marker prevalence is not anatomical prevalence.
- assessment_id: quantities
  area: quantity
  topic: Every physical property and stoichiometry assertion
  outcome: not_applicable
  target_ids:
  - GO:0009424
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
  - GO:0009424
  evidence_ids:
  - record
  - prior-search
  summary: Every discussion and target history was read. Boundary decisions keep adjacent
    structures distinct; PROPOSED remains appropriate. No images, external compositions,
    traits, pathway links or datasets are asserted here; absent optional sections
    are not findings. Past events remain historical and unchanged.
findings:
- finding_id: F1
  issue_key: flagellar-hook-bacterial-prevalence-common
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Bacteria-wide COMMON is not supported by a flagellated-lineage statement
  description: The native enum means present in most members with exceptional losses.
    The note describes already-flagellated bacteria instead, while the accessed assembly-review
    material does not establish a majority of all Bacteria. The independent reference-genome
    survey supports patchy occurrence but is not a direct anatomy census.
  target_ids:
  - GO:0009424
  field_paths:
  - taxonomic_distribution[0].presence
  - taxonomic_distribution[0].reference
  evidence_ids:
  - record
  - paper-03
  - paper-21
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_hook.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#evidence
  native_severity: major
  normalization_reason: Material unsupported scientific assertion.
actions:
- action_id: A1
  description: Use VARIABLE or a narrower evidence-backed taxon scope, with explicit
    genomic-proxy limits. Preserve the bacterial/archaellum distinction and avoid
    treating marker absence as proof of anatomical absence.
  finding_ids:
  - F1
  target_ids:
  - GO:0009424
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_hook.yaml
    role: maintained scientific record
  acceptance_checks:
  - No majority-Bacteria assertion remains without a suitable denominator-bearing
    source.
  - Evidence explicitly distinguishes sampled genomes, flagellar markers and assembled
    structures.
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
- The distribution study uses FliPQR markers in reference genomes; it is neither microscopy
  of this structure nor an unbiased census of bacterial cells or species.
```
