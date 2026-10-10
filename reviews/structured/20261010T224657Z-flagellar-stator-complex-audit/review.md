# bacterial-type flagellum stator complex: scientific evidence review

- Review: 20261010T224657Z-flagellar-stator-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-10T22:39:21Z
- Finished UTC: 2026-10-10T22:46:57Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Every present native section assessed with source-specific access limits; confirmed findings require separately authorized curation.

## Scope And Provenance

One complete native record, all present claims and history; no sampling.

Selection: Next sequential unassessed target in the 909-record goal worklist: data/structures/appendage/bacterial_type_flagellum_stator_complex.yaml
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base b7453b637b71268e49710d17aa5c34743bce7a6c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0120101 | data/structures/appendage/bacterial_type_flagellum_stator_complex.yaml | maintained | bacterial-type flagellum stator complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0120101 | Native check passed. Identifier gate skips unsupported namespaces; scoped authorities were independently inspected. Snippet check is not a scientific-support pass. |
| strict | passed | True | GO:0120101 | Native check passed. Identifier gate skips unsupported namespaces; scoped authorities were independently inspected. Snippet check is not a scientific-support pass. |
| snippets | passed | True | GO:0120101 | Native check passed. Identifier gate skips unsupported namespaces; scoped authorities were independently inspected. Snippet check is not a scientific-support pass. |
| history | passed | True | GO:0120101 | Native check passed. Identifier gate skips unsupported namespaces; scoped authorities were independently inspected. Snippet check is not a scientific-support pass. |
| labels | passed | True | GO:0120101 | Native check passed. Identifier gate skips unsupported namespaces; scoped authorities were independently inspected. Snippet check is not a scientific-support pass. |
| traits | passed | True | GO:0120101 | Native check passed. Identifier gate skips unsupported namespaces; scoped authorities were independently inspected. Snippet check is not a scientific-support pass. |
| curies | passed | True | GO:0120101 | Native check passed. Identifier gate skips unsupported namespaces; scoped authorities were independently inspected. Snippet check is not a scientific-support pass. |
| regressions | passed | True | GO:0120101 | Native check passed. Identifier gate skips unsupported namespaces; scoped authorities were independently inspected. Snippet check is not a scientific-support pass. |
| reviews | passed | True | GO:0120101 | Native check passed. Identifier gate skips unsupported namespaces; scoped authorities were independently inspected. Snippet check is not a scientific-support pass. |
| diff | passed | True | GO:0120101 | Native check passed. Identifier gate skips unsupported namespaces; scoped authorities were independently inspected. Snippet check is not a scientific-support pass. |
| Exact-baseline authoritative CI quality gate | passed | True | GO:0120101 | Successful authoritative QC step runs uv run python scripts/run_qc.py on this exact unchanged baseline; not a claim of a fresh local full-QC run. |
| iModulonDB datasets | passed | False | GO:0120101 | Salmonella core dataset gene-context search. No iModulon hit informed the verdict; text matches are not structure-membership evidence. Campylobacter is not covered. |
| iModulonDB motA | passed | False | GO:0120101 | Salmonella core dataset gene-context search. No iModulon hit informed the verdict; text matches are not structure-membership evidence. Campylobacter is not covered. |
| iModulonDB motB | passed | False | GO:0120101 | Salmonella core dataset gene-context search. No iModulon hit informed the verdict; text matches are not structure-membership evidence. Campylobacter is not covered. |

## Scientific And Domain Assessments

### Structure identity, definition, synonyms, category and parthood

identity: supported. Targets: GO:0120101.

Exact active GO cellular-component identity. Rotor/stator/motor/export-apparatus boundaries are explicit and not equated with a single protein or whole flagellum.

### Domain distribution and canonical example

scope: supported. Targets: GO:0120101.

Bacteria VARIABLE is conditional on flagellar systems; archaella are distinct. Named taxa resolve; the export-core example overattributes the experiment and is covered by F1.

### All constituents, roles and essentiality

evidence: concern. Targets: GO:0120101.

A/B stator and MS/C-ring rotor boundaries retained. Constitutive requirements are interpreted for the named complete subcomplex, not whole-flagellum assembly. 5:2 structure is observed; a complete rotational mechanism was modeled in the cited 2020 studies.

### All functions and every causal edge

graph: concern. Targets: GO:0120101.

Ion-driven torque and stator contacts supported; distinguish model-derived trajectories, E. coli measured rotation/exchange and Borrelia static architecture. CheY/FliM, MS/C-ring and rod coupling in the motor are supported by their cited experiments/structural interpretations.

### A/B label-only decisions

grounding: concern. Targets: GO:0120101.

IPR047055 explicitly includes MotA/PomA/LafT and matches reviewed examples. B-subunit alternatives remain broad domains/families; no exact B-family replacement is justified by this bounded search.

### Every stoichiometry and physical property

quantity: supported. Targets: GO:0120101.

Stator 5:2 and seven-subunit property are restricted to solved cores; motor has no extra count/measurement claim. Legacy GO A4B2 is explicitly declined.

### Discussions, histories, status and optional sections

provenance: supported. Targets: GO:0120101.

Both history surfaces and resolved boundaries were read. Preserve historical events, stable identity and PROPOSED status. No images, traits, external complex compositions or transcriptomic datasets are asserted; empty optional fields do not qualify as findings.

## Findings

### F1: Rotation claims exceed the context of the cited 2020 models

minor / open / confirmed; issue key: flagellar-stator-rotation-evidence-scope.

Unqualified A-ring rotation descriptions are sourced to static structures and proposed mechanisms. Deme also permits an oscillating ratchet. Hosu 2025 supplies newer E. coli motion evidence, but does not turn the older studies into direct motion measurements or prove every Mot/Pom trajectory.

### F2: Dynamic exchange lacks a directly matched source and experimental scope

minor / open / confirmed; issue key: flagellar-stator-exchange-evidence-scope.

The exchange function is supported by anchoring/static-structure studies, without attaching the direct turnover source. Chang explicitly distinguishes exchange-prone systems from Borrelia motors. The unqualified wording obscures that limitation.

### F3: A-subunit label-only decision is contradicted by an exact family

minor / open / confirmed; issue key: flagellar-stator-mota-family-grounding.

The record affirmatively says no integrated MotA/PomA family was identified. Current IPR047055 is a family explicitly containing MotA, PomA and LafT, and is matched by reviewed MotA and PomA proteins. This is a stale decision, not a finding based on an empty optional field.

## Recommended Actions And Acceptance Checks

### A1

Qualify model-derived statements and add the newer direct evidence with E. coli scope; retain supported 5:2 architecture.

- 2020 observations and proposed motion are distinguishable in primary claim text, not only bibliography notes.
- New evidence does not assert a measured rotation direction or universal sodium-stator trajectory.
- Guarded write, both append-only histories, PROPOSED status, regenerated affected artifacts, native validators and authoritative QC pass.

### A2

Attach Leake 2006 and scope demonstrated exchange to E. coli; retain separate peptidoglycan-anchoring and Borrelia structural evidence.

- The turnover claim names the experimentally studied organism and the appropriate source.
- Static imaging is not represented as a turnover measurement.
- Guarded write, both append-only histories, PROPOSED status, regenerated affected artifacts, native validators and authoritative QC pass.

### A3

Ground the A subunit to IPR047055 with its canonical label and retain the prior decision as dated provenance. Do not replace the B-subunit label-only decision with a broad OmpA/domain match.

- Grounding, canonical label and current status agree; gene symbols and B-subunit scope are preserved.
- Guarded write, both append-only histories, PROPOSED status, regenerated affected artifacts, native validators and authoritative QC pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/bacterial_type_flagellum_stator_complex.yaml; Entire target YAML, schema and recorded input histories | context_only | Complete record read; maintained ownership and PROPOSED status retained. Neighboring parts checked for identity/parthood, not counted as new reviews. |
| paper-01 | DOI:10.1016/S0022-2836(03)00096-2; Abstract | supports | Abstract: ion-coupling experiments with Mot/Pom chimeras distinguish the A/B core from MotX/MotY accessories. |
| paper-03 | DOI:10.1016/j.cell.2020.08.016; Abstract | supports | Abstract: five MotA and two MotB subunits were resolved; motion and switching were mechanistic models, not direct movies. Campylobacter provenance independently checked with EMDB. |
| paper-05 | DOI:10.1016/j.str.2018.02.016; Abstract | supports | Abstract: MotB L119P fragment binds peptidoglycan; NMR, crystallography and in-vivo crosslinking support activation-linked rearrangement. Not a stator-turnover experiment. |
| paper-09 | DOI:10.1038/nrmicro1887; Review context | supports | Review context: coordinated assembly and conditional occurrence in flagellated bacteria; not an all-Bacteria prevalence census. |
| paper-11 | DOI:10.1038/s41564-020-0788-8; Full text Results, coupling-of-ion-flow section, Discussion and Methods | supports | Full text Results, coupling-of-ion-flow section, Discussion and Methods: 5:2 stators include Vibrio PomAB and MotAB preparations; processive rotation and oscillating ratchet were alternative models. |
| paper-23 | DOI:10.3389/fmicb.2015.00023; Review abstract and established comparative context | supports | Review abstract and established comparative context: archaella are type-IV-pilus-related, not bacterial flagellar structures. |
| paper-24 | DOI:10.7554/eLife.48979; Full text Introduction and Discussion | supports | Full text Introduction and Discussion: Borrelia in-situ stator contacts and conformational changes; exchange is cited for other systems and may differ in scaffolded motors. |
| go-0009274 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009274; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| go-0009433 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009433; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| go-0120100 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0120100; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| go-0120101 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0120101; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| ncbitaxon-197 | https://rest.uniprot.org/taxonomy/197.json; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| ncbitaxon-2 | https://rest.uniprot.org/taxonomy/2.json; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| ncbitaxon-2157 | https://rest.uniprot.org/taxonomy/2157.json; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| hosu2025 | DOI:10.1073/pnas.2515291122; Results, Fig. 2, Discussion and Methods | supports | E. coli polarized photobleaching measures MotA rotation relative to anchored MotB; this does not measure rotation direction or every sodium stator. |
| leake2006 | DOI:10.1038/nature05135; Primary abstract | supports | GFP-MotB exchange measured in functioning E. coli motors by fluorescence recovery/loss; does not establish exchange in every bacterial motor. |
| ipr047055 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR047055/; Entry type and complete family/domain description | supports | MotA-like is an integrated family explicitly including MotA/PomA/LafT. Alternatives are narrower, broad domains, or unrelated-family mixtures. |
| ipr022522 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR022522/; Entry type and complete family/domain description | supports | MotA-like is an integrated family explicitly including MotA/PomA/LafT. Alternatives are narrower, broad domains, or unrelated-family mixtures. |
| ipr025713 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR025713/; Entry type and complete family/domain description | supports | MotA-like is an integrated family explicitly including MotA/PomA/LafT. Alternatives are narrower, broad domains, or unrelated-family mixtures. |
| ipr050330 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050330/; Entry type and complete family/domain description | supports | MotA-like is an integrated family explicitly including MotA/PomA/LafT. Alternatives are narrower, broad domains, or unrelated-family mixtures. |
| ipr002898 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002898/; Entry type and complete family/domain description | supports | MotA-like is an integrated family explicitly including MotA/PomA/LafT. Alternatives are narrower, broad domains, or unrelated-family mixtures. |
| ipr006665 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006665/; Entry type and complete family/domain description | supports | MotA-like is an integrated family explicitly including MotA/PomA/LafT. Alternatives are narrower, broad domains, or unrelated-family mixtures. |
| mota-proteins | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AmotA+AND+reviewed%3Atrue&amp;format=json&amp;size=5; Reviewed exact-gene search, first five results | supports | Bounded gene search cross-checks family matches; an empty PomB result is not proof of biological or database absence. |
| motb-proteins | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AmotB+AND+reviewed%3Atrue&amp;format=json&amp;size=5; Reviewed exact-gene search, first five results | supports | Bounded gene search cross-checks family matches; an empty PomB result is not proof of biological or database absence. |
| poma-proteins | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ApomA+AND+reviewed%3Atrue&amp;format=json&amp;size=5; Reviewed exact-gene search, first five results | supports | Bounded gene search cross-checks family matches; an empty PomB result is not proof of biological or database absence. |
| pomb-proteins | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ApomB+AND+reviewed%3Atrue&amp;format=json&amp;size=5; Reviewed exact-gene search, first five results | supports | Bounded gene search cross-checks family matches; an empty PomB result is not proof of biological or database absence. |
| campylobacter-structure | https://www.ebi.ac.uk/emdb/api/entry/EMD-10828; Deposited sample and publication metadata | supports | Campylobacter jejuni MotAB deposition linked to Santiveri 2020 supports canonical organism and solved stoichiometry context. |
| prior-search | reviews/structured/ and reports/yaml_record_review/; Exact target IDs, labels and slugs | context_only | No canonical assessment targeting this exact record; related whole-flagellum/basal-body/C-ring reviews are context, not predecessors. |

## Limits And Additional Notes

- All present native sections were assessed, but some cited papers remain abstract-only. Source locators distinguish inspected abstracts from inspected full-text sections; inaccessible detailed methods and figures are not certified.
- Several Europe PMC full-text endpoints returned HTTP 500. Some PMC HTML responses were browser challenges; the alternate Imada BioC response was an HTTP-200 error document, not article text. Its abstract clearly distinguishes the solved fragment from the model.
- Successful authoritative full-QC evidence is CI for the exact unchanged baseline commit; other listed native validators were run locally. Identifier checks may skip unsupported namespaces and snippet checks do not establish scientific support.
- This agent self-review is not human approval and does not finish the all-909-record goal. Findings are saved before any scientific curation.
- iModulonDB gene hits are computational context only; no iModulon hit informed the verdict. Campylobacter is not covered, and missing search hits are not negative biological evidence.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T224657Z-flagellar-stator-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'bacterial-type flagellum stator complex: scientific evidence review'
started_at: '2026-10-10T22:39:21Z'
finished_at: '2026-10-10T22:46:57Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Agent assessment of existing records; not independent human
    scientific approval. Scientific inputs were unchanged during review.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Every present native section assessed with source-specific access limits;
  confirmed findings require separately authorized curation.
source:
  git_revision: b7453b637b71268e49710d17aa5c34743bce7a6c
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
  - path: data/structures/appendage/bacterial_type_flagellum_motor.yaml
    sha256: 8106c0c442166dc94efa20211ec9502a56f9919f13d05045c327bae3ccd2afc1
    role: context
  - path: data/structures/appendage/bacterial_type_flagellum_stator_complex.yaml
    sha256: 30c0e7cc7d82b69b9c279eddfd075c005847db26bf1a04e9b0a58157bf59e772
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
  - path: history/records/bacterial_type_flagellum_stator_complex/2026-09-08T041542Z-claude-481cc0.yaml
    sha256: f6f23ba5694ed8776617d40f66a2592c03792569ab08a171d2e455afabd59cb1
    role: context
  - path: history/records/bacterial_type_flagellum_stator_complex/2026-09-08T042328Z-claude-605873.yaml
    sha256: 29fdc402ec53d0d2c0d84e08443d20409e8a033b700593132c59a473109ae240
    role: context
  - path: history/records/bacterial_type_flagellum_stator_complex/2026-09-08T042544Z-claude-158451.yaml
    sha256: 7485b67815635fcc667d59494b6c17554278f4750eb71a7a45c5a593137b88fa
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
- target_id: GO:0120101
  path: data/structures/appendage/bacterial_type_flagellum_stator_complex.yaml
  label: bacterial-type flagellum stator complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_stator_complex.yaml
    role: maintained scientific record
scope:
  description: One complete native record, all present claims and history; no sampling.
  selection: 'Next sequential unassessed target in the 909-record goal worklist: data/structures/appendage/bacterial_type_flagellum_stator_complex.yaml'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0120101
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - GO:0120101
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/appendage/bacterial_type_flagellum_stator_complex.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Native check passed. Identifier gate skips unsupported namespaces; scoped
    authorities were independently inspected. Snippet check is not a scientific-support
    pass.
  scope_note: 2026-10-10T22:42:20Z to 2026-10-10T22:42:23Z; /private/tmp/csm-review-20261010T223824Z/checks/bacterial_type_flagellum_stator_complex-schema.log;
    SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - GO:0120101
  command: .venv/bin/python scripts/validate_strict.py data/structures/appendage/bacterial_type_flagellum_stator_complex.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Native check passed. Identifier gate skips unsupported namespaces; scoped
    authorities were independently inspected. Snippet check is not a scientific-support
    pass.
  scope_note: 2026-10-10T22:42:23Z to 2026-10-10T22:42:28Z; /private/tmp/csm-review-20261010T223824Z/checks/bacterial_type_flagellum_stator_complex-strict.log;
    SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - GO:0120101
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/appendage/bacterial_type_flagellum_stator_complex.yaml
    --report /private/tmp/csm-review-20261010T223824Z/checks/bacterial_type_flagellum_stator_complex-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: Native check passed. Identifier gate skips unsupported namespaces; scoped
    authorities were independently inspected. Snippet check is not a scientific-support
    pass.
  scope_note: 2026-10-10T22:42:28Z to 2026-10-10T22:42:51Z; /private/tmp/csm-review-20261010T223824Z/checks/bacterial_type_flagellum_stator_complex-snippets.log;
    SHA-256 e9099a7422bb3713b9242d22a1977b2d526497cc4e7657c68bf12b40546b41a7
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:0120101
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Native check passed. Identifier gate skips unsupported namespaces; scoped
    authorities were independently inspected. Snippet check is not a scientific-support
    pass.
  scope_note: 2026-10-10T22:42:51Z to 2026-10-10T22:43:06Z; /private/tmp/csm-review-20261010T223824Z/checks/history.log;
    SHA-256 453a059dea6bf1bb79107a0d2f5efc9bf8f952e10f056940483df1bb3af09972
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - GO:0120101
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Native check passed. Identifier gate skips unsupported namespaces; scoped
    authorities were independently inspected. Snippet check is not a scientific-support
    pass.
  scope_note: 2026-10-10T22:43:06Z to 2026-10-10T22:44:41Z; /private/tmp/csm-review-20261010T223824Z/checks/labels.log;
    SHA-256 d10699bb2abeb0de144fe64b442a139ade489d962490ec567e25ab8301d90d66
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - GO:0120101
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Native check passed. Identifier gate skips unsupported namespaces; scoped
    authorities were independently inspected. Snippet check is not a scientific-support
    pass.
  scope_note: 2026-10-10T22:44:41Z to 2026-10-10T22:44:59Z; /private/tmp/csm-review-20261010T223824Z/checks/traits.log;
    SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - GO:0120101
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Native check passed. Identifier gate skips unsupported namespaces; scoped
    authorities were independently inspected. Snippet check is not a scientific-support
    pass.
  scope_note: 2026-10-10T22:44:59Z to 2026-10-10T22:45:43Z; /private/tmp/csm-review-20261010T223824Z/checks/curies.log;
    SHA-256 63e0b92fcb2428d27ca591a7e11b58978b427c668b14adf707deec14cb1bd0bf
- check_id: regressions
  name: regressions
  status: passed
  required: true
  target_ids:
  - GO:0120101
  command: .venv/bin/python -m pytest -q tests/test_flagellar_review_corrections.py
    tests/test_write_validated.py
  exit_code: 0
  expected_exit_code: 0
  summary: Native check passed. Identifier gate skips unsupported namespaces; scoped
    authorities were independently inspected. Snippet check is not a scientific-support
    pass.
  scope_note: 2026-10-10T22:45:43Z to 2026-10-10T22:46:19Z; /private/tmp/csm-review-20261010T223824Z/checks/regressions.log;
    SHA-256 592294348f6bb5fead3555feb82170eb9125c74f8bd82a14bd119a153bf6433f
- check_id: reviews
  name: reviews
  status: passed
  required: true
  target_ids:
  - GO:0120101
  command: .venv/bin/python scripts/record_review.py check --base b7453b637b71268e49710d17aa5c34743bce7a6c
  exit_code: 0
  expected_exit_code: 0
  summary: Native check passed. Identifier gate skips unsupported namespaces; scoped
    authorities were independently inspected. Snippet check is not a scientific-support
    pass.
  scope_note: 2026-10-10T22:46:19Z to 2026-10-10T22:46:53Z; /private/tmp/csm-review-20261010T223824Z/checks/reviews.log;
    SHA-256 396e4a723e26dd3e64050a9ac05524ead64707f89f2673a92d2f198ef7d1bdea
- check_id: diff
  name: diff
  status: passed
  required: true
  target_ids:
  - GO:0120101
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  summary: Native check passed. Identifier gate skips unsupported namespaces; scoped
    authorities were independently inspected. Snippet check is not a scientific-support
    pass.
  scope_note: 2026-10-10T22:46:53Z to 2026-10-10T22:46:54Z; /private/tmp/csm-review-20261010T223824Z/checks/diff.log;
    SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- check_id: qc
  name: Exact-baseline authoritative CI quality gate
  status: passed
  required: true
  target_ids:
  - GO:0120101
  command: gh run view 38091677561 --json headSha,status,conclusion,jobs,url; gh run
    view 38091677561 --log
  exit_code: 0
  expected_exit_code: 0
  summary: Successful authoritative QC step runs uv run python scripts/run_qc.py on
    this exact unchanged baseline; not a claim of a fresh local full-QC run.
  scope_note: https://github.com/CultureBotAI/CellStructureMech/actions/runs/38091677561;
    log SHA-256 2f15865aacc8eda04a6085e987f164b7c545285daffe4807dc80aa206def9b0e
- check_id: adapter-datasets
  name: iModulonDB datasets
  status: passed
  required: false
  target_ids:
  - GO:0120101
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  exit_code: 0
  summary: Salmonella core dataset gene-context search. No iModulon hit informed the
    verdict; text matches are not structure-membership evidence. Campylobacter is
    not covered.
  scope_note: 2026-10-10T22:40:49Z to 2026-10-10T22:40:50Z; log SHA-256 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- check_id: adapter-mota
  name: iModulonDB motA
  status: passed
  required: false
  target_ids:
  - GO:0120101
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism s_enterica --dataset core --query motA
  exit_code: 0
  summary: Salmonella core dataset gene-context search. No iModulon hit informed the
    verdict; text matches are not structure-membership evidence. Campylobacter is
    not covered.
  scope_note: 2026-10-10T22:40:53Z to 2026-10-10T22:40:53Z; log SHA-256 80e729bcdf73eb10e0410431ea16e5dde7c5bdf8aea5cf501cd3ed0c2f76c7ba
- check_id: adapter-motb
  name: iModulonDB motB
  status: passed
  required: false
  target_ids:
  - GO:0120101
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism s_enterica --dataset core --query motB
  exit_code: 0
  summary: Salmonella core dataset gene-context search. No iModulon hit informed the
    verdict; text matches are not structure-membership evidence. Campylobacter is
    not covered.
  scope_note: 2026-10-10T22:40:53Z to 2026-10-10T22:40:54Z; log SHA-256 6048df4bb1eb08837e3ee81d71bed949fa1372500ebe5ab0e189ae754709b1e8
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/appendage/bacterial_type_flagellum_stator_complex.yaml
  locator: Entire target YAML, schema and recorded input histories
  accessed_at: '2026-10-10T22:46:57Z'
  support: context_only
  summary: Complete record read; maintained ownership and PROPOSED status retained.
    Neighboring parts checked for identity/parthood, not counted as new reviews.
- evidence_id: paper-01
  kind: primary_source
  reference: DOI:10.1016/S0022-2836(03)00096-2
  locator: Abstract
  accessed_at: '2026-10-10T22:40:29Z'
  snapshot_sha256: 8919ebe29443b7d30762a7138cabf1df7143ee91fc95b5fa462ad4d9415c5a45
  support: supports
  summary: 'Abstract: ion-coupling experiments with Mot/Pom chimeras distinguish the
    A/B core from MotX/MotY accessories.'
- evidence_id: paper-03
  kind: primary_source
  reference: DOI:10.1016/j.cell.2020.08.016
  locator: Abstract
  accessed_at: '2026-10-10T22:40:30Z'
  snapshot_sha256: ed7bc59593098f61fd42172109253eea289f0af4e88155b081df4140b41d23e6
  support: supports
  summary: 'Abstract: five MotA and two MotB subunits were resolved; motion and switching
    were mechanistic models, not direct movies. Campylobacter provenance independently
    checked with EMDB.'
- evidence_id: paper-05
  kind: primary_source
  reference: DOI:10.1016/j.str.2018.02.016
  locator: Abstract
  accessed_at: '2026-10-10T22:40:31Z'
  snapshot_sha256: 0ef80132e76e1f74714ebf8df86b2bc29919e795704f8da61348d97d44ea139a
  support: supports
  summary: 'Abstract: MotB L119P fragment binds peptidoglycan; NMR, crystallography
    and in-vivo crosslinking support activation-linked rearrangement. Not a stator-turnover
    experiment.'
- evidence_id: paper-09
  kind: primary_source
  reference: DOI:10.1038/nrmicro1887
  locator: Review context
  accessed_at: '2026-10-10T22:40:35Z'
  snapshot_sha256: 648eac60aca511dba55bd983fcc746cd1c173f143b5259fa8bd78daa609ca3c6
  support: supports
  summary: 'Review context: coordinated assembly and conditional occurrence in flagellated
    bacteria; not an all-Bacteria prevalence census.'
- evidence_id: paper-11
  kind: primary_source
  reference: DOI:10.1038/s41564-020-0788-8
  locator: Full text Results, coupling-of-ion-flow section, Discussion and Methods
  accessed_at: '2026-10-10T22:40:39Z'
  snapshot_sha256: 2250b535735358b44b02046731afdf6ad1fac623468bfd82d7145248b1a6b072
  support: supports
  summary: 'Full text Results, coupling-of-ion-flow section, Discussion and Methods:
    5:2 stators include Vibrio PomAB and MotAB preparations; processive rotation and
    oscillating ratchet were alternative models.'
- evidence_id: paper-23
  kind: primary_source
  reference: DOI:10.3389/fmicb.2015.00023
  locator: Review abstract and established comparative context
  accessed_at: '2026-10-10T22:40:56Z'
  snapshot_sha256: 5e2b4c125d1d01c22b2d7eb326b7e73bb6b17e9d1c0b660c785ea11667745677
  support: supports
  summary: 'Review abstract and established comparative context: archaella are type-IV-pilus-related,
    not bacterial flagellar structures.'
- evidence_id: paper-24
  kind: primary_source
  reference: DOI:10.7554/eLife.48979
  locator: Full text Introduction and Discussion
  accessed_at: '2026-10-10T22:40:59Z'
  snapshot_sha256: bf6a96bd205a6cbaea786a35c1c2c68367f8d7f97ddddea875c45760113e1b68
  support: supports
  summary: 'Full text Introduction and Discussion: Borrelia in-situ stator contacts
    and conformational changes; exchange is cited for other systems and may differ
    in scaffolded motors.'
- evidence_id: go-0009274
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009274
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:00Z'
  snapshot_sha256: 7537b72bc1f481b91ed2b9eb404bf7b61ddc0c3d4c04a1745d5c33ad7af1b604
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: go-0009433
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009433
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:02Z'
  snapshot_sha256: 2dff37996895f1d80a7d89878d916a2fbcd0c787ca925b7223375f9ba3e66a40
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: go-0120100
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0120100
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:03Z'
  snapshot_sha256: 66ebccd6448ecf8935cb12ab851dd382e1cf09579d0eec0c58619bb30497a73b
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: go-0120101
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0120101
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:04Z'
  snapshot_sha256: b66361210ff4cadc3cbf771ff6415a9f205fcfddf22b234a2428339f1ed43eff
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: ncbitaxon-197
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/197.json
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:16Z'
  snapshot_sha256: 7346dd32eb9f3fb96e5a5f775bb9a0dc8dc761a5dd41712b84d65f148ed90c77
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: ncbitaxon-2
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/2.json
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:17Z'
  snapshot_sha256: 8074c9bcd59cd4da1da4bc9ec98c040bbecd52ef5c91c4c4bb9bed0f3a7cb5a9
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: ncbitaxon-2157
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/2157.json
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:17Z'
  snapshot_sha256: 14f5852a1db0f9f5ef8d60e4a11c1916bf005bf549c57dd4bc860d39194a1799
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: hosu2025
  kind: primary_source
  reference: DOI:10.1073/pnas.2515291122
  locator: Results, Fig. 2, Discussion and Methods
  accessed_at: '2026-10-10T22:41:32Z'
  snapshot_sha256: fc24ba6f21145cc7393d410061c9fbb338353d85222338758e4173c9b6220533
  support: supports
  summary: E. coli polarized photobleaching measures MotA rotation relative to anchored
    MotB; this does not measure rotation direction or every sodium stator.
- evidence_id: leake2006
  kind: primary_source
  reference: DOI:10.1038/nature05135
  locator: Primary abstract
  accessed_at: '2026-10-10T22:41:33Z'
  snapshot_sha256: 19f0bc7def0abb3a8030edd50960e52d32268f16ba670a9bb07dd951f80a390b
  support: supports
  summary: GFP-MotB exchange measured in functioning E. coli motors by fluorescence
    recovery/loss; does not establish exchange in every bacterial motor.
- evidence_id: ipr047055
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR047055/
  locator: Entry type and complete family/domain description
  accessed_at: '2026-10-10T22:42:40Z'
  snapshot_sha256: 7d009e86c040fd31abe97acd37092073a3ce78b4e3e717fb943c059d9f77549a
  support: supports
  summary: MotA-like is an integrated family explicitly including MotA/PomA/LafT.
    Alternatives are narrower, broad domains, or unrelated-family mixtures.
- evidence_id: ipr022522
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR022522/
  locator: Entry type and complete family/domain description
  accessed_at: '2026-10-10T22:42:36Z'
  snapshot_sha256: 4bd53a0b33400552433dbdc83e05095e6260544b67bb8442d89d374558ec5b7a
  support: supports
  summary: MotA-like is an integrated family explicitly including MotA/PomA/LafT.
    Alternatives are narrower, broad domains, or unrelated-family mixtures.
- evidence_id: ipr025713
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR025713/
  locator: Entry type and complete family/domain description
  accessed_at: '2026-10-10T22:42:37Z'
  snapshot_sha256: 67caa5798ab5a42b0dd34ea7829d017d753079b26217da4167f6e8b68f28ba29
  support: supports
  summary: MotA-like is an integrated family explicitly including MotA/PomA/LafT.
    Alternatives are narrower, broad domains, or unrelated-family mixtures.
- evidence_id: ipr050330
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050330/
  locator: Entry type and complete family/domain description
  accessed_at: '2026-10-10T22:42:40Z'
  snapshot_sha256: 34125ff0dbe649f6cdf83e47f283d084ece2d1a7537572e0b5444282850d7288
  support: supports
  summary: MotA-like is an integrated family explicitly including MotA/PomA/LafT.
    Alternatives are narrower, broad domains, or unrelated-family mixtures.
- evidence_id: ipr002898
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002898/
  locator: Entry type and complete family/domain description
  accessed_at: '2026-10-10T22:42:33Z'
  snapshot_sha256: 9b24f5c01cc61ab3b12873224dbdf95e84eac06794b1253f677e61fa6b8e0de2
  support: supports
  summary: MotA-like is an integrated family explicitly including MotA/PomA/LafT.
    Alternatives are narrower, broad domains, or unrelated-family mixtures.
- evidence_id: ipr006665
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006665/
  locator: Entry type and complete family/domain description
  accessed_at: '2026-10-10T22:42:34Z'
  snapshot_sha256: c170b9b182156f8b2e5310140f94899b9a8a2ef8ae4c5add06d60cfa29f862ec
  support: supports
  summary: MotA-like is an integrated family explicitly including MotA/PomA/LafT.
    Alternatives are narrower, broad domains, or unrelated-family mixtures.
- evidence_id: mota-proteins
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AmotA+AND+reviewed%3Atrue&format=json&size=5
  locator: Reviewed exact-gene search, first five results
  accessed_at: '2026-10-10T22:42:29Z'
  snapshot_sha256: 9b503de9ab55c664ee7feeb9baf5cd6bd398070b87eae28a34e02c3d4b7cce62
  support: supports
  summary: Bounded gene search cross-checks family matches; an empty PomB result is
    not proof of biological or database absence.
- evidence_id: motb-proteins
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AmotB+AND+reviewed%3Atrue&format=json&size=5
  locator: Reviewed exact-gene search, first five results
  accessed_at: '2026-10-10T22:42:30Z'
  snapshot_sha256: ea9f75ef99ea68c3e2e6d77fc3cb5cf18e7f1bfb15c799d00936da009a672eaa
  support: supports
  summary: Bounded gene search cross-checks family matches; an empty PomB result is
    not proof of biological or database absence.
- evidence_id: poma-proteins
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ApomA+AND+reviewed%3Atrue&format=json&size=5
  locator: Reviewed exact-gene search, first five results
  accessed_at: '2026-10-10T22:42:31Z'
  snapshot_sha256: 7723ca9e4c0f108706cbb98882ce7c57409c081504eaf45f5cdad7313053906a
  support: supports
  summary: Bounded gene search cross-checks family matches; an empty PomB result is
    not proof of biological or database absence.
- evidence_id: pomb-proteins
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ApomB+AND+reviewed%3Atrue&format=json&size=5
  locator: Reviewed exact-gene search, first five results
  accessed_at: '2026-10-10T22:42:31Z'
  snapshot_sha256: 5021e624e752b001ce3e3846e8f158ed4aeb93a4c9a72fdb35a0c5b14a0eea84
  support: supports
  summary: Bounded gene search cross-checks family matches; an empty PomB result is
    not proof of biological or database absence.
- evidence_id: campylobacter-structure
  kind: authority
  reference: https://www.ebi.ac.uk/emdb/api/entry/EMD-10828
  locator: Deposited sample and publication metadata
  accessed_at: '2026-10-10T22:43:46Z'
  snapshot_sha256: 9d1f0ef2fe20e53e19516c805d73366d52df3f54774f033fe17c5449511833cc
  support: supports
  summary: Campylobacter jejuni MotAB deposition linked to Santiveri 2020 supports
    canonical organism and solved stoichiometry context.
- evidence_id: prior-search
  kind: search
  reference: reviews/structured/ and reports/yaml_record_review/
  locator: Exact target IDs, labels and slugs
  accessed_at: '2026-10-10T22:46:57Z'
  support: context_only
  search_scope: Path.rglob parsed all 48 canonical review YAMLs including ignored/hidden
    entries; rg --no-ignore --hidden searched reviews and legacy reports for target
    IDs/slugs.
  summary: No canonical assessment targeting this exact record; related whole-flagellum/basal-body/C-ring
    reviews are context, not predecessors.
assessments:
- assessment_id: identity
  area: identity
  topic: Structure identity, definition, synonyms, category and parthood
  outcome: supported
  target_ids:
  - GO:0120101
  evidence_ids:
  - record
  - go-0120101
  summary: Exact active GO cellular-component identity. Rotor/stator/motor/export-apparatus
    boundaries are explicit and not equated with a single protein or whole flagellum.
- assessment_id: taxonomy
  area: scope
  topic: Domain distribution and canonical example
  outcome: supported
  target_ids:
  - GO:0120101
  evidence_ids:
  - record
  - paper-23
  summary: Bacteria VARIABLE is conditional on flagellar systems; archaella are distinct.
    Named taxa resolve; the export-core example overattributes the experiment and
    is covered by F1.
- assessment_id: composition
  area: evidence
  topic: All constituents, roles and essentiality
  outcome: concern
  target_ids:
  - GO:0120101
  evidence_ids:
  - record
  - paper-03
  - paper-11
  summary: A/B stator and MS/C-ring rotor boundaries retained. Constitutive requirements
    are interpreted for the named complete subcomplex, not whole-flagellum assembly.
    5:2 structure is observed; a complete rotational mechanism was modeled in the
    cited 2020 studies.
  dimensions:
  - name: evidence_tier
    value: Primary structural/functional experiments versus explicitly identified
      mechanistic models
    definition: Observed assembly or dynamics are distinguished from model-derived
      trajectories and organism extrapolation
    evidence_ids:
    - paper-11
    - hosu2025
- assessment_id: function-graph
  area: graph
  topic: All functions and every causal edge
  outcome: concern
  target_ids:
  - GO:0120101
  evidence_ids:
  - record
  - paper-05
  - paper-11
  - paper-24
  - hosu2025
  - leake2006
  summary: Ion-driven torque and stator contacts supported; distinguish model-derived
    trajectories, E. coli measured rotation/exchange and Borrelia static architecture.
    CheY/FliM, MS/C-ring and rod coupling in the motor are supported by their cited
    experiments/structural interpretations.
- assessment_id: grounding
  area: grounding
  topic: A/B label-only decisions
  outcome: concern
  target_ids:
  - GO:0120101
  evidence_ids:
  - ipr047055
  - ipr022522
  - ipr025713
  - mota-proteins
  - poma-proteins
  summary: IPR047055 explicitly includes MotA/PomA/LafT and matches reviewed examples.
    B-subunit alternatives remain broad domains/families; no exact B-family replacement
    is justified by this bounded search.
- assessment_id: quantities
  area: quantity
  topic: Every stoichiometry and physical property
  outcome: supported
  target_ids:
  - GO:0120101
  evidence_ids:
  - record
  - paper-03
  - paper-11
  summary: Stator 5:2 and seven-subunit property are restricted to solved cores; motor
    has no extra count/measurement claim. Legacy GO A4B2 is explicitly declined.
- assessment_id: provenance
  area: provenance
  topic: Discussions, histories, status and optional sections
  outcome: supported
  target_ids:
  - GO:0120101
  evidence_ids:
  - record
  - prior-search
  summary: Both history surfaces and resolved boundaries were read. Preserve historical
    events, stable identity and PROPOSED status. No images, traits, external complex
    compositions or transcriptomic datasets are asserted; empty optional fields do
    not qualify as findings.
findings:
- finding_id: F1
  issue_key: flagellar-stator-rotation-evidence-scope
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Rotation claims exceed the context of the cited 2020 models
  description: Unqualified A-ring rotation descriptions are sourced to static structures
    and proposed mechanisms. Deme also permits an oscillating ratchet. Hosu 2025 supplies
    newer E. coli motion evidence, but does not turn the older studies into direct
    motion measurements or prove every Mot/Pom trajectory.
  target_ids:
  - GO:0120101
  field_paths:
  - causal_graphs[0].edges
  - functions[0]
  - components[0].role
  - causal_graphs[0].description
  evidence_ids:
  - record
  - paper-03
  - paper-11
  - hosu2025
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_stator_complex.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#evidence
  native_severity: minor
  normalization_reason: Bounded provenance, claim-qualification or grounding defect;
    record identity is sound.
- finding_id: F2
  issue_key: flagellar-stator-exchange-evidence-scope
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Dynamic exchange lacks a directly matched source and experimental scope
  description: The exchange function is supported by anchoring/static-structure studies,
    without attaching the direct turnover source. Chang explicitly distinguishes exchange-prone
    systems from Borrelia motors. The unqualified wording obscures that limitation.
  target_ids:
  - GO:0120101
  field_paths:
  - functions[1]
  evidence_ids:
  - record
  - paper-05
  - paper-24
  - leake2006
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_stator_complex.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#evidence
  native_severity: minor
  normalization_reason: Bounded provenance, claim-qualification or grounding defect;
    record identity is sound.
- finding_id: F3
  issue_key: flagellar-stator-mota-family-grounding
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: A-subunit label-only decision is contradicted by an exact family
  description: The record affirmatively says no integrated MotA/PomA family was identified.
    Current IPR047055 is a family explicitly containing MotA, PomA and LafT, and is
    matched by reviewed MotA and PomA proteins. This is a stale decision, not a finding
    based on an empty optional field.
  target_ids:
  - GO:0120101
  field_paths:
  - components[0].grounding_status
  - components[0].grounding_notes
  evidence_ids:
  - record
  - ipr047055
  - mota-proteins
  - poma-proteins
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_stator_complex.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#evidence
  native_severity: minor
  normalization_reason: Bounded provenance, claim-qualification or grounding defect;
    record identity is sound.
actions:
- action_id: A1
  description: Qualify model-derived statements and add the newer direct evidence
    with E. coli scope; retain supported 5:2 architecture.
  finding_ids:
  - F1
  target_ids:
  - GO:0120101
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_stator_complex.yaml
    role: maintained scientific record
  acceptance_checks:
  - 2020 observations and proposed motion are distinguishable in primary claim text,
    not only bibliography notes.
  - New evidence does not assert a measured rotation direction or universal sodium-stator
    trajectory.
  - Guarded write, both append-only histories, PROPOSED status, regenerated affected
    artifacts, native validators and authoritative QC pass.
- action_id: A2
  description: Attach Leake 2006 and scope demonstrated exchange to E. coli; retain
    separate peptidoglycan-anchoring and Borrelia structural evidence.
  finding_ids:
  - F2
  target_ids:
  - GO:0120101
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_stator_complex.yaml
    role: maintained scientific record
  acceptance_checks:
  - The turnover claim names the experimentally studied organism and the appropriate
    source.
  - Static imaging is not represented as a turnover measurement.
  - Guarded write, both append-only histories, PROPOSED status, regenerated affected
    artifacts, native validators and authoritative QC pass.
- action_id: A3
  description: Ground the A subunit to IPR047055 with its canonical label and retain
    the prior decision as dated provenance. Do not replace the B-subunit label-only
    decision with a broad OmpA/domain match.
  finding_ids:
  - F3
  target_ids:
  - GO:0120101
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_stator_complex.yaml
    role: maintained scientific record
  acceptance_checks:
  - Grounding, canonical label and current status agree; gene symbols and B-subunit
    scope are preserved.
  - Guarded write, both append-only histories, PROPOSED status, regenerated affected
    artifacts, native validators and authoritative QC pass.
limitations:
- All present native sections were assessed, but some cited papers remain abstract-only.
  Source locators distinguish inspected abstracts from inspected full-text sections;
  inaccessible detailed methods and figures are not certified.
- Several Europe PMC full-text endpoints returned HTTP 500. Some PMC HTML responses
  were browser challenges; the alternate Imada BioC response was an HTTP-200 error
  document, not article text. Its abstract clearly distinguishes the solved fragment
  from the model.
- Successful authoritative full-QC evidence is CI for the exact unchanged baseline
  commit; other listed native validators were run locally. Identifier checks may skip
  unsupported namespaces and snippet checks do not establish scientific support.
- This agent self-review is not human approval and does not finish the all-909-record
  goal. Findings are saved before any scientific curation.
- iModulonDB gene hits are computational context only; no iModulon hit informed the
  verdict. Campylobacter is not covered, and missing search hits are not negative
  biological evidence.
```
