# Ciliary transition zone: scientific evidence review

- Review: 20261010T232629Z-ciliary-transition-zone-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-10T23:15:32Z
- Finished UTC: 2026-10-10T23:26:29Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Complete native record assessed. One bounded stale-grounding issue observed; molecular inventory uncertainties are not treated as defects.

## Scope And Provenance

Entire native record, all present claims and histories; related linker identity checked as context.

Selection: Next sequential unassessed target in the all-909-record goal worklist.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 48e9549a06f45272815b6c7d38321b801d4c800c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0035869 | data/structures/appendage/ciliary_transition_zone.yaml | maintained | ciliary transition zone |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0035869 | Native check passed. Identifier gate skips unsupported namespaces; scoped authorities inspected separately. Snippet validation does not establish paraphrase support. |
| strict | passed | True | GO:0035869 | Native check passed. Identifier gate skips unsupported namespaces; scoped authorities inspected separately. Snippet validation does not establish paraphrase support. |
| snippets | passed | True | GO:0035869 | Native check passed. Identifier gate skips unsupported namespaces; scoped authorities inspected separately. Snippet validation does not establish paraphrase support. |
| history | passed | True | GO:0035869 | Native check passed. Identifier gate skips unsupported namespaces; scoped authorities inspected separately. Snippet validation does not establish paraphrase support. |
| labels | passed | True | GO:0035869 | Native check passed. Identifier gate skips unsupported namespaces; scoped authorities inspected separately. Snippet validation does not establish paraphrase support. |
| traits | passed | True | GO:0035869 | Native check passed. Identifier gate skips unsupported namespaces; scoped authorities inspected separately. Snippet validation does not establish paraphrase support. |
| curies | passed | True | GO:0035869 | Native check passed. Identifier gate skips unsupported namespaces; scoped authorities inspected separately. Snippet validation does not establish paraphrase support. |
| reviews | passed | True | GO:0035869 | Native check passed. Identifier gate skips unsupported namespaces; scoped authorities inspected separately. Snippet validation does not establish paraphrase support. |
| diff | passed | True | GO:0035869 | Native check passed. Identifier gate skips unsupported namespaces; scoped authorities inspected separately. Snippet validation does not establish paraphrase support. |
| Exact-baseline authoritative CI QC | passed | True | GO:0035869 | Successful authoritative QC on the exact unchanged baseline; not a fresh local full-QC run. |
| iModulonDB dataset applicability | passed | False | GO:0035869 | Dataset inventory has no Chlamydomonas coverage. No applicable structured expression query; absence is not negative biological evidence. |

## Scientific And Domain Assessments

### Identity, category, definition, synonyms and cilium parthood

identity: supported. Targets: GO:0035869.

Exact regional GO identity; not equated with external transition fibers, isolated protein or whole cilium.

### All three component groundings and roles

grounding: concern. Targets: GO:0035869.

Exact assembled Y-link term supersedes the label-only rationale. Segment-specific axonemal microtubules and aggregate protein network remain appropriately unresolved; no full molecular inventory is inferred.

### Constituent membership, essentiality and inventory

evidence: supported. Targets: GO:0035869.

Architectural constituents and UNKNOWN essentiality are bounded. Wedge defects are not Y-link-specific deletion, and generic protein membership does not assign every pathway module to every lineage.

### Taxon distribution and canonical example

scope: supported. Targets: GO:0035869.

Chlamydomonas-only native scope and isolated-zone proteomics exemplar match sources; no all-eukaryote frequency inferred.

### Gating function and every causal edge

graph: supported. Targets: GO:0035869.

NONMECHANISTIC graph states architectural connections, parthood and composition regulation. It does not claim a measured transport reaction or complete isolated-link gating mechanism.

### Evidence placement, discussions, status and histories

provenance: supported. Targets: GO:0035869.

Each current claim checked against nearest source. Existing events remain historical; inventory discussion stays OPEN. No images, counts, physical measurements, traits, protein examples or datasets are asserted; optional absence is not a defect.

## Findings

### F1: Y-link component retains a stale label-only grounding decision

minor / open / confirmed; issue key: transition-zone-y-link-grounding.

The component says no exact source-neutral CURIE for assembled linker material was curated. Active GO:0097537 exactly denotes the Y-shaped linker complex, and the repository already contains its evidence-backed record. This is a bounded stale grounding rationale, not a wrong whole-zone identity or an unknown molecular inventory.

## Recommended Actions And Acceptance Checks

### A1

Ground the assembled linker to GO:0097537 with its canonical label and protein-complex type; synchronize graph identity. Preserve the previous rationale as dated superseded history, and clarify that the remaining OPEN inventory task concerns molecules/segments, not the known assembled linker identity.

- Exact GO term, label and type agree without replacing the whole-zone identity.
- Link component and graph agree; no universal essentiality, stoichiometry or Y-link-specific gating claim added.
- Other two label-only decisions and UNKNOWN essentiality preserved.
- Guarded write, both append-only histories, PROPOSED status, affected generated artifacts and native QC pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/ciliary_transition_zone.yaml; Entire YAML, linked cilium/linker context and native histories | context_only | Complete record and histories read; PROPOSED status and maintained ownership confirmed. Prior in-record events preserve earlier assertions, not current scientific claims. |
| zone | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0035869; Exact identity, definition and synonyms | supports | Active GO regional identity; Y-shaped links are constituents, not synonyms of the entire transition zone. |
| link | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097537; Exact identity, definition and synonyms | supports | Active exact Y-shaped protein-complex term, explicitly placed in the ciliary transition zone; matches the currently label-only assembled linker. |
| link-ancestry | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097537/ancestors?relations=is_a,part_of; is_a and part_of ancestry | supports | Linker belongs to the protein-containing-complex hierarchy and lies within the transition zone. Combined ancestry is not treated as pure is-a. |
| cilium | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005929; Identity and definition | supports | Exact enclosing cilium identity, not bacterial flagellum. |
| taxon | https://rest.uniprot.org/taxonomy/3055.json; Taxonomic identity | supports | Chlamydomonas reinhardtii identity matches examples and scoped experiments. |
| craige | DOI:10.1083/jcb.201006105; Results and Figures 3-5 captions; Discussion | supports | CEP290 mutant and localization experiments support normal connector tethering and altered protein composition. Rare residual Y-links and simultaneous wedge defects do not establish isolated Y-link sufficiency. |
| diener | DOI:10.1016/j.cub.2014.11.066; Results: isolation and ultrastructure of transition zones | supports | Isolated transition-zone vesicles were fractionated with cell-wall material and analyzed by proteomics. Isolation loses outer microtubules/stellate structure; native exemplar does not claim an intact in-situ purified molecular inventory. |
| wang | DOI:10.1038/s41467-022-31751-0; Results: transition-zone architecture, localization independence and mutant composition | supports | TCTN1 loss affects wedge-shaped structures, not evident Y-link architecture in the scored sections; CEP290/NPHP4/TCTN1 have distinct composition effects. Current native text preserves these distinctions. |
| garcia | DOI:10.1101/cshperspect.a028134; Review sections on transition-zone architecture and modules | supports | Secondary review context for regional gating and incomplete, lineage-dependent molecular inventory; not a new primary experiment. |
| prior-search | reviews/structured/ and reports/yaml_record_review/; GO:0035869 and transition-zone-y-link-grounding | context_only | No canonical predecessor targeting this exact record found within the ignored-inclusive review roots. Related linker report is not a transition-zone review. |

## Limits And Additional Notes

- Same-agent review, not human scientific approval or completion of the all-909-record goal.
- Europe PMC full-text requests for two sources failed; official PMC S3 XML with metadata MD5 verification was inspected instead. The four cited sources were assessed in the listed sections, not every unrelated experiment.
- Authoritative full QC is verified CI for the exact unchanged baseline; local listed checks were separately run. Identifier namespace skips and empty quoted-snippet fields do not prove scientific support.
- iModulonDB lacks applicable Chlamydomonas dataset coverage; this is not negative evidence. Molecular stoichiometry, complete constituents and precise gating mechanisms remain unresolved rather than fabricated.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T232629Z-ciliary-transition-zone-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'Ciliary transition zone: scientific evidence review'
started_at: '2026-10-10T23:15:32Z'
finished_at: '2026-10-10T23:26:29Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent assessment of existing inputs, before scientific
    mutation. Not independent human approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Complete native record assessed. One bounded stale-grounding issue observed;
  molecular inventory uncertainties are not treated as defects.
source:
  git_revision: 48e9549a06f45272815b6c7d38321b801d4c800c
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
  - path: data/structures/appendage/ciliary_transition_zone.yaml
    sha256: 1002a4c178f558fd94bcd13b33e477ce09f0538da87a5606f3fa323b65b25df0
    role: target
  - path: data/structures/appendage/cilium.yaml
    sha256: 2536d421f9c482abf35c2d2bf026eb6158ddfec5c2df1f319ca80698cbb56bb8
    role: context
  - path: data/structures/appendage/y_shaped_link.yaml
    sha256: 89637052ba32ba24d695d33a540116783a09124de805feeaa9430f1f5c702841
    role: context
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
  - path: history/records/ciliary_transition_zone/2026-09-15T140438Z-codex-d1abb5.yaml
    sha256: 8dafa05b894669c3391bffe5b9f650266166a21c5dc2cb4044102152b001cbb6
    role: context
  - path: history/records/ciliary_transition_zone/2026-09-15T141310Z-codex-28d402.yaml
    sha256: c6b3c5987e417cdf36c0551dca1fc6df0789b1f51506d90ddeaadeee7fa302ad
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
- target_id: GO:0035869
  path: data/structures/appendage/ciliary_transition_zone.yaml
  label: ciliary transition zone
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/ciliary_transition_zone.yaml
    role: maintained scientific record
scope:
  description: Entire native record, all present claims and histories; related linker
    identity checked as context.
  selection: Next sequential unassessed target in the all-909-record goal worklist.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0035869
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - GO:0035869
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/appendage/ciliary_transition_zone.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Native check passed. Identifier gate skips unsupported namespaces; scoped
    authorities inspected separately. Snippet validation does not establish paraphrase
    support.
  scope_note: 2026-10-10T23:17:28Z to 2026-10-10T23:17:33Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - GO:0035869
  command: .venv/bin/python scripts/validate_strict.py data/structures/appendage/ciliary_transition_zone.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Native check passed. Identifier gate skips unsupported namespaces; scoped
    authorities inspected separately. Snippet validation does not establish paraphrase
    support.
  scope_note: 2026-10-10T23:17:33Z to 2026-10-10T23:17:38Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - GO:0035869
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/appendage/ciliary_transition_zone.yaml
    --report /private/tmp/csm-review-20261010T231420Z/checks/ciliary_transition_zone-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: Native check passed. Identifier gate skips unsupported namespaces; scoped
    authorities inspected separately. Snippet validation does not establish paraphrase
    support.
  scope_note: 2026-10-10T23:17:38Z to 2026-10-10T23:18:34Z; log SHA-256 dcaf5b9dfacf71de98bb95ec16cf870fbad4758354ffcad0ef4d5903fd2ac10e
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:0035869
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Native check passed. Identifier gate skips unsupported namespaces; scoped
    authorities inspected separately. Snippet validation does not establish paraphrase
    support.
  scope_note: 2026-10-10T23:19:55Z to 2026-10-10T23:20:39Z; log SHA-256 4b9a602c272c2a2c4b63a7fe2117a11dd354c25b685adcde10c8e4ceea274afe
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - GO:0035869
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Native check passed. Identifier gate skips unsupported namespaces; scoped
    authorities inspected separately. Snippet validation does not establish paraphrase
    support.
  scope_note: 2026-10-10T23:20:39Z to 2026-10-10T23:24:01Z; log SHA-256 4e7c08d40597390917ae73f20ed6755095022904244e88833405c338595173d1
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - GO:0035869
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Native check passed. Identifier gate skips unsupported namespaces; scoped
    authorities inspected separately. Snippet validation does not establish paraphrase
    support.
  scope_note: 2026-10-10T23:24:01Z to 2026-10-10T23:24:27Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - GO:0035869
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Native check passed. Identifier gate skips unsupported namespaces; scoped
    authorities inspected separately. Snippet validation does not establish paraphrase
    support.
  scope_note: 2026-10-10T23:24:27Z to 2026-10-10T23:25:19Z; log SHA-256 22cafeea4eafe84d9ebe3dba07b73cf3e93c8bc9f25e824a31c7484d28e09072
- check_id: reviews
  name: reviews
  status: passed
  required: true
  target_ids:
  - GO:0035869
  command: .venv/bin/python scripts/record_review.py check --base 48e9549a06f45272815b6c7d38321b801d4c800c
  exit_code: 0
  expected_exit_code: 0
  summary: Native check passed. Identifier gate skips unsupported namespaces; scoped
    authorities inspected separately. Snippet validation does not establish paraphrase
    support.
  scope_note: 2026-10-10T23:25:19Z to 2026-10-10T23:26:07Z; log SHA-256 453050e90003355513c3b3f2b765ad04f2eb0e9b48061a474bbee0280c9bd447
- check_id: diff
  name: diff
  status: passed
  required: true
  target_ids:
  - GO:0035869
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  summary: Native check passed. Identifier gate skips unsupported namespaces; scoped
    authorities inspected separately. Snippet validation does not establish paraphrase
    support.
  scope_note: 2026-10-10T23:26:07Z to 2026-10-10T23:26:08Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- check_id: qc
  name: Exact-baseline authoritative CI QC
  status: passed
  required: true
  target_ids:
  - GO:0035869
  command: gh run view 38093800970 --json headSha,status,conclusion,jobs,url; gh run
    view 38093800970 --log
  exit_code: 0
  expected_exit_code: 0
  summary: Successful authoritative QC on the exact unchanged baseline; not a fresh
    local full-QC run.
  scope_note: https://github.com/CultureBotAI/CellStructureMech/actions/runs/38093800970;
    log SHA-256 0f2a9127749d8f9304de883ba12bb2239dadb07df14dbcf504dfcda16daec4a9
- check_id: adapter
  name: iModulonDB dataset applicability
  status: passed
  required: false
  target_ids:
  - GO:0035869
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  exit_code: 0
  summary: Dataset inventory has no Chlamydomonas coverage. No applicable structured
    expression query; absence is not negative biological evidence.
  scope_note: 2026-10-10T23:17:04Z to 2026-10-10T23:17:05Z; SHA-256 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/appendage/ciliary_transition_zone.yaml
  locator: Entire YAML, linked cilium/linker context and native histories
  accessed_at: '2026-10-10T23:26:29Z'
  snapshot_sha256: 1002a4c178f558fd94bcd13b33e477ce09f0538da87a5606f3fa323b65b25df0
  support: context_only
  summary: Complete record and histories read; PROPOSED status and maintained ownership
    confirmed. Prior in-record events preserve earlier assertions, not current scientific
    claims.
- evidence_id: zone
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0035869
  locator: Exact identity, definition and synonyms
  accessed_at: '2026-10-10T23:15:30Z'
  snapshot_sha256: 53717c0b5d03b56da3697589e576a8a14f0ec5ea563d3531e2ea9e501533981c
  support: supports
  summary: Active GO regional identity; Y-shaped links are constituents, not synonyms
    of the entire transition zone.
- evidence_id: link
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097537
  locator: Exact identity, definition and synonyms
  accessed_at: '2026-10-10T23:15:33Z'
  snapshot_sha256: bc3b53cec4d839726633ca8c4afcb7917793b2555537383d9dbe714bb4ea8a6e
  support: supports
  summary: Active exact Y-shaped protein-complex term, explicitly placed in the ciliary
    transition zone; matches the currently label-only assembled linker.
- evidence_id: link-ancestry
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097537/ancestors?relations=is_a,part_of
  locator: is_a and part_of ancestry
  accessed_at: '2026-10-10T23:17:32Z'
  snapshot_sha256: ef55b84dc232e1e58082cdfaf10a0a2aacf5ab1ae439107e78b1a13dd98c4e74
  support: supports
  summary: Linker belongs to the protein-containing-complex hierarchy and lies within
    the transition zone. Combined ancestry is not treated as pure is-a.
- evidence_id: cilium
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005929
  locator: Identity and definition
  accessed_at: '2026-10-10T23:15:27Z'
  snapshot_sha256: 5720b98b130e903527e1a96849ac46ee6978e83369e460c0f278f16ef9aca041
  support: supports
  summary: Exact enclosing cilium identity, not bacterial flagellum.
- evidence_id: taxon
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/3055.json
  locator: Taxonomic identity
  accessed_at: '2026-10-10T23:15:39Z'
  snapshot_sha256: 31e68163918c110c000e261d4edc5ae389b11e9992f43540ba3b89a9471ce850
  support: supports
  summary: Chlamydomonas reinhardtii identity matches examples and scoped experiments.
- evidence_id: craige
  kind: primary_source
  reference: DOI:10.1083/jcb.201006105
  locator: Results and Figures 3-5 captions; Discussion
  accessed_at: '2026-10-10T23:15:19Z'
  snapshot_sha256: a83f54c0f615e5ac6f3fa935a59ace211da887d0d8c92cbebf04dddc25715f7c
  support: supports
  summary: CEP290 mutant and localization experiments support normal connector tethering
    and altered protein composition. Rare residual Y-links and simultaneous wedge
    defects do not establish isolated Y-link sufficiency.
- evidence_id: diener
  kind: primary_source
  reference: DOI:10.1016/j.cub.2014.11.066
  locator: 'Results: isolation and ultrastructure of transition zones'
  accessed_at: '2026-10-10T23:17:06Z'
  snapshot_sha256: 3fcda6631400e1aaf86713554e4a18e089f7a4b0c3a8e7fe0b95ccb7ee759ee4
  support: supports
  summary: Isolated transition-zone vesicles were fractionated with cell-wall material
    and analyzed by proteomics. Isolation loses outer microtubules/stellate structure;
    native exemplar does not claim an intact in-situ purified molecular inventory.
- evidence_id: wang
  kind: primary_source
  reference: DOI:10.1038/s41467-022-31751-0
  locator: 'Results: transition-zone architecture, localization independence and mutant
    composition'
  accessed_at: '2026-10-10T23:15:15Z'
  snapshot_sha256: 026e49670797cdcbf1f206ff808cd0c87bc56041593c9947ffa32be9ea8a39bd
  support: supports
  summary: TCTN1 loss affects wedge-shaped structures, not evident Y-link architecture
    in the scored sections; CEP290/NPHP4/TCTN1 have distinct composition effects.
    Current native text preserves these distinctions.
- evidence_id: garcia
  kind: primary_source
  reference: DOI:10.1101/cshperspect.a028134
  locator: Review sections on transition-zone architecture and modules
  accessed_at: '2026-10-10T23:17:10Z'
  snapshot_sha256: 4849b5ab5d2090ad1da6304724c8a976d2d574b325c6f6c0af203fe417acf4f9
  support: supports
  summary: Secondary review context for regional gating and incomplete, lineage-dependent
    molecular inventory; not a new primary experiment.
- evidence_id: prior-search
  kind: search
  reference: reviews/structured/ and reports/yaml_record_review/
  locator: GO:0035869 and transition-zone-y-link-grounding
  accessed_at: '2026-10-10T23:26:29Z'
  support: context_only
  search_scope: rg --no-ignore --hidden searched all YAML/Markdown in both review
    roots; related Y-link legacy report read as context.
  summary: No canonical predecessor targeting this exact record found within the ignored-inclusive
    review roots. Related linker report is not a transition-zone review.
assessments:
- assessment_id: identity
  area: identity
  topic: Identity, category, definition, synonyms and cilium parthood
  outcome: supported
  target_ids:
  - GO:0035869
  evidence_ids:
  - record
  - zone
  - cilium
  summary: Exact regional GO identity; not equated with external transition fibers,
    isolated protein or whole cilium.
- assessment_id: grounding
  area: grounding
  topic: All three component groundings and roles
  outcome: concern
  target_ids:
  - GO:0035869
  evidence_ids:
  - record
  - link
  - link-ancestry
  - craige
  summary: Exact assembled Y-link term supersedes the label-only rationale. Segment-specific
    axonemal microtubules and aggregate protein network remain appropriately unresolved;
    no full molecular inventory is inferred.
- assessment_id: composition
  area: evidence
  topic: Constituent membership, essentiality and inventory
  outcome: supported
  target_ids:
  - GO:0035869
  evidence_ids:
  - record
  - zone
  - craige
  - wang
  - garcia
  summary: Architectural constituents and UNKNOWN essentiality are bounded. Wedge
    defects are not Y-link-specific deletion, and generic protein membership does
    not assign every pathway module to every lineage.
  dimensions:
  - name: evidence_tier
    value: Authority architecture; primary mutant/localization/proteomic evidence;
      secondary review context
    definition: Structural presence, observed mutant consequences and proposed gating
      mechanisms are distinct.
    evidence_ids:
    - zone
    - craige
    - diener
    - wang
    - garcia
- assessment_id: taxonomy
  area: scope
  topic: Taxon distribution and canonical example
  outcome: supported
  target_ids:
  - GO:0035869
  evidence_ids:
  - record
  - taxon
  - wang
  - diener
  summary: Chlamydomonas-only native scope and isolated-zone proteomics exemplar match
    sources; no all-eukaryote frequency inferred.
- assessment_id: function
  area: graph
  topic: Gating function and every causal edge
  outcome: supported
  target_ids:
  - GO:0035869
  evidence_ids:
  - record
  - zone
  - craige
  - wang
  - garcia
  summary: NONMECHANISTIC graph states architectural connections, parthood and composition
    regulation. It does not claim a measured transport reaction or complete isolated-link
    gating mechanism.
- assessment_id: provenance
  area: provenance
  topic: Evidence placement, discussions, status and histories
  outcome: supported
  target_ids:
  - GO:0035869
  evidence_ids:
  - record
  - craige
  - diener
  - wang
  - garcia
  summary: Each current claim checked against nearest source. Existing events remain
    historical; inventory discussion stays OPEN. No images, counts, physical measurements,
    traits, protein examples or datasets are asserted; optional absence is not a defect.
findings:
- finding_id: F1
  issue_key: transition-zone-y-link-grounding
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Y-link component retains a stale label-only grounding decision
  description: The component says no exact source-neutral CURIE for assembled linker
    material was curated. Active GO:0097537 exactly denotes the Y-shaped linker complex,
    and the repository already contains its evidence-backed record. This is a bounded
    stale grounding rationale, not a wrong whole-zone identity or an unknown molecular
    inventory.
  target_ids:
  - GO:0035869
  field_paths:
  - components[0].grounding_status
  - components[0].grounding_notes
  - causal_graphs[0].nodes[1]
  - discussions[0]
  evidence_ids:
  - record
  - link
  - link-ancestry
  - craige
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/ciliary_transition_zone.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: minor
  normalization_reason: Nonblocking exact-grounding gap with otherwise sound structure
    identity and explicitly incomplete molecular inventory.
actions:
- action_id: A1
  description: Ground the assembled linker to GO:0097537 with its canonical label
    and protein-complex type; synchronize graph identity. Preserve the previous rationale
    as dated superseded history, and clarify that the remaining OPEN inventory task
    concerns molecules/segments, not the known assembled linker identity.
  finding_ids:
  - F1
  target_ids:
  - GO:0035869
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/ciliary_transition_zone.yaml
    role: maintained scientific record
  acceptance_checks:
  - Exact GO term, label and type agree without replacing the whole-zone identity.
  - Link component and graph agree; no universal essentiality, stoichiometry or Y-link-specific
    gating claim added.
  - Other two label-only decisions and UNKNOWN essentiality preserved.
  - Guarded write, both append-only histories, PROPOSED status, affected generated
    artifacts and native QC pass.
limitations:
- Same-agent review, not human scientific approval or completion of the all-909-record
  goal.
- Europe PMC full-text requests for two sources failed; official PMC S3 XML with metadata
  MD5 verification was inspected instead. The four cited sources were assessed in
  the listed sections, not every unrelated experiment.
- Authoritative full QC is verified CI for the exact unchanged baseline; local listed
  checks were separately run. Identifier namespace skips and empty quoted-snippet
  fields do not prove scientific support.
- iModulonDB lacks applicable Chlamydomonas dataset coverage; this is not negative
  evidence. Molecular stoichiometry, complete constituents and precise gating mechanisms
  remain unresolved rather than fabricated.
```
