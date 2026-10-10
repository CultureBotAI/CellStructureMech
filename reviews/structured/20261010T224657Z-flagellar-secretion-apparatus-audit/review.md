# bacterial-type flagellum secretion apparatus: scientific evidence review

- Review: 20261010T224657Z-flagellar-secretion-apparatus-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-10T22:39:19Z
- Finished UTC: 2026-10-10T22:46:57Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Every present native section assessed with source-specific access limits; confirmed findings require separately authorized curation.

## Scope And Provenance

One complete native record, all present claims and history; no sampling.

Selection: Next sequential unassessed target in the 909-record goal worklist: data/structures/appendage/bacterial_type_flagellum_secretion_apparatus.yaml
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base b7453b637b71268e49710d17aa5c34743bce7a6c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0120102 | data/structures/appendage/bacterial_type_flagellum_secretion_apparatus.yaml | maintained | bacterial-type flagellum secretion apparatus |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0120102 | Native check passed. Identifier gate skips unsupported namespaces; scoped authorities were independently inspected. Snippet check is not a scientific-support pass. |
| strict | passed | True | GO:0120102 | Native check passed. Identifier gate skips unsupported namespaces; scoped authorities were independently inspected. Snippet check is not a scientific-support pass. |
| snippets | passed | True | GO:0120102 | Native check passed. Identifier gate skips unsupported namespaces; scoped authorities were independently inspected. Snippet check is not a scientific-support pass. |
| history | passed | True | GO:0120102 | Native check passed. Identifier gate skips unsupported namespaces; scoped authorities were independently inspected. Snippet check is not a scientific-support pass. |
| labels | passed | True | GO:0120102 | Native check passed. Identifier gate skips unsupported namespaces; scoped authorities were independently inspected. Snippet check is not a scientific-support pass. |
| traits | passed | True | GO:0120102 | Native check passed. Identifier gate skips unsupported namespaces; scoped authorities were independently inspected. Snippet check is not a scientific-support pass. |
| curies | passed | True | GO:0120102 | Native check passed. Identifier gate skips unsupported namespaces; scoped authorities were independently inspected. Snippet check is not a scientific-support pass. |
| regressions | passed | True | GO:0120102 | Native check passed. Identifier gate skips unsupported namespaces; scoped authorities were independently inspected. Snippet check is not a scientific-support pass. |
| reviews | passed | True | GO:0120102 | Native check passed. Identifier gate skips unsupported namespaces; scoped authorities were independently inspected. Snippet check is not a scientific-support pass. |
| diff | passed | True | GO:0120102 | Native check passed. Identifier gate skips unsupported namespaces; scoped authorities were independently inspected. Snippet check is not a scientific-support pass. |
| Exact-baseline authoritative CI quality gate | passed | True | GO:0120102 | Successful authoritative QC step runs uv run python scripts/run_qc.py on this exact unchanged baseline; not a claim of a fresh local full-QC run. |
| iModulonDB datasets | passed | False | GO:0120102 | Salmonella core dataset gene-context search. No iModulon hit informed the verdict; text matches are not structure-membership evidence. Campylobacter is not covered. |
| iModulonDB flhA | passed | False | GO:0120102 | Salmonella core dataset gene-context search. No iModulon hit informed the verdict; text matches are not structure-membership evidence. Campylobacter is not covered. |
| iModulonDB flhB | passed | False | GO:0120102 | Salmonella core dataset gene-context search. No iModulon hit informed the verdict; text matches are not structure-membership evidence. Campylobacter is not covered. |
| iModulonDB fliP | passed | False | GO:0120102 | Salmonella core dataset gene-context search. No iModulon hit informed the verdict; text matches are not structure-membership evidence. Campylobacter is not covered. |
| iModulonDB fliQ | passed | False | GO:0120102 | Salmonella core dataset gene-context search. No iModulon hit informed the verdict; text matches are not structure-membership evidence. Campylobacter is not covered. |
| iModulonDB fliR | passed | False | GO:0120102 | Salmonella core dataset gene-context search. No iModulon hit informed the verdict; text matches are not structure-membership evidence. Campylobacter is not covered. |
| iModulonDB fliH | passed | False | GO:0120102 | Salmonella core dataset gene-context search. No iModulon hit informed the verdict; text matches are not structure-membership evidence. Campylobacter is not covered. |
| iModulonDB fliI | passed | False | GO:0120102 | Salmonella core dataset gene-context search. No iModulon hit informed the verdict; text matches are not structure-membership evidence. Campylobacter is not covered. |
| iModulonDB fliJ | passed | False | GO:0120102 | Salmonella core dataset gene-context search. No iModulon hit informed the verdict; text matches are not structure-membership evidence. Campylobacter is not covered. |

## Scientific And Domain Assessments

### Structure identity, definition, synonyms, category and parthood

identity: supported. Targets: GO:0120102.

Exact active GO cellular-component identity. Rotor/stator/motor/export-apparatus boundaries are explicit and not equated with a single protein or whole flagellum.

### Domain distribution and canonical example

scope: concern. Targets: GO:0120102.

Bacteria VARIABLE is conditional on flagellar systems; archaella are distinct. Named taxa resolve; the export-core example overattributes the experiment and is covered by F1.

### All eight components, counts, protein examples and source precision

evidence: concern. Targets: GO:0120102.

Gene/taxon examples and seven family groundings resolve. FliI label-only boundary is justified. ATPase dispensability has mutant evidence; incorrect historical architecture and model-resolution notes require correction.

### All functions and eleven causal edges

graph: concern. Targets: GO:0120102.

Axial substrate export, ATPase association and substrate ordering are supported. Core geometry, experimental provenance and ion-coupling conditions require the bounded fixes below.

### All stoichiometries; no separate physical properties

quantity: concern. Targets: GO:0120102.

Counts are biologically plausible but require correct preparation, organism and modeled-versus-measured attribution; no new universal counts should be introduced.

### Discussions, histories, status and optional sections

provenance: supported. Targets: GO:0120102.

Both history surfaces and resolved boundaries were read. Preserve historical events, stable identity and PROPOSED status. No images, traits, external complex compositions or transcriptomic datasets are asserted; empty optional fields do not qualify as findings.

## Findings

### F1: Modern export-core architecture is falsely attributed to Fukumura 2017

major / open / confirmed; issue key: flagellar-export-core-stoichiometry-provenance.

Multiple component, exemplar, function, graph and discussion claims assign a FliP5Q4R1-FlhB1 reconstruction to the 2017 paper. It reports isolated FliP hexamers and detergent-sensitive associations. Kuhlen 2018 resolves Salmonella FliP5Q4R1; Kuhlen 2020 resolves Vibrio mimicus FliP5Q4R1-FlhB1. The latter also places FlhB around the base, not as a cap, and FliR within a helical P/R core.

### F2: ATPase model is described as a resolved complete complex

minor / open / confirmed; issue key: flagellar-export-atpase-model-provenance.

FliH/FliI/FliJ component notes use resolved/placed language for the complete FliH12-FliI6-FliJ1 complex. The primary abstract distinguishes the solved FliH C-terminal dimer-FliI heterotrimer from a hexamer model. The graph already partly uses modeled, so the current notes are inconsistent.

### F3: Sodium coupling is conflated with the intact ATPase-assisted state

major / open / confirmed; issue key: flagellar-export-dual-fuel-atpase-context.

The energy function combines soluble ATPase and proton-or-sodium driving force without experimental conditions. The cited 2016 study finds sodium-dependent export when the ATPase system is compromised and no sodium dependence with the entire FliH/FliI/FliJ complex. Broad component and graph wording likewise drops this key contrast.

## Recommended Actions And Acceptance Checks

### A1

Resource modern counts/geometry to the inspected 2018/2020 structures with organism context. Correct cap/ring and whole-apparatus localization wording; do not infer an assembly sequence from a static structure. Preserve FliO historical evidence and exclusion rationale.

- No current claim attributes a 5:4:1:1 reconstruction to 2017.
- Salmonella PQR and Vibrio PQR-FlhB are distinguished; modern counts remain supported at each claim.
- FlhB wraps the gate base, FliR is integrated, and FliQ peripheral; historical events are unchanged.
- Guarded write, both append-only histories, PROPOSED status, regenerated affected artifacts, native validators and authoritative QC pass.

### A2

Identify the solved fragment heterotrimer and modeled full ATPase assembly, including count context; retain supported membership.

- No complete FliH12-FliI6-FliJ1 reconstruction is attributed to Imada 2016.
- Measured fragment structure and assembled model are explicitly distinct.
- Guarded write, both append-only histories, PROPOSED status, regenerated affected artifacts, native validators and authoritative QC pass.

### A3

State the Salmonella wild-type PMF versus ATPase-compromised sodium-capable contrast at the function and energy edge; add appropriate source support to FlhA coupling.

- No claim says the intact Salmonella ATPase-assisted system used sodium in that experiment.
- Retain demonstrated sodium capability with genotype and condition context; do not generalize to every bacterial export apparatus.
- Guarded write, both append-only histories, PROPOSED status, regenerated affected artifacts, native validators and authoritative QC pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/bacterial_type_flagellum_secretion_apparatus.yaml; Entire target YAML, schema and recorded input histories | context_only | Complete record read; maintained ownership and PROPOSED status retained. Neighboring parts checked for identity/parthood, not counted as new reviews. |
| paper-00 | DOI:10.1007/82_2019_170; Abstract | supports | Abstract: membrane export gate and cytoplasmic ATPase are distinct parts of the basal-body export machinery. |
| paper-02 | DOI:10.1016/j.bbamcr.2013.09.005; Abstract | supports | Abstract: axial protein export, ATPase-assisted entry and FliJ-FlhA coupling; older FliO inventory is refined by later assembly studies. |
| paper-09 | DOI:10.1038/nrmicro1887; Review context | supports | Review context: coordinated assembly and conditional occurrence in flagellated bacteria; not an all-Bacteria prevalence census. |
| paper-12 | DOI:10.1038/s42003-024-06081-0; Full text Introduction, mutant Results and Fig. 1 | supports | Full text Introduction, mutant Results and Fig. 1: FlhA GYXLI-mutant phenotypes support ATPase-assisted ordering; Fig. 1 uses modeled ATPase assembly. |
| paper-13 | DOI:10.1073/pnas.1524025113; Abstract | supports | Abstract: solved FliH C-terminal homodimer-FliI complex is distinct from the proposed hexamer model; complete ATPase assembly was not directly resolved by this paper. |
| paper-16 | DOI:10.1111/mmi.12529; Abstract | supports | Abstract: fluorescence measurements estimate about nine FlhA molecules and show coordinated assembly with the MS ring. |
| paper-18 | DOI:10.1128/JB.181.5.1388-1394.1999; Abstract | supports | Abstract: mutant substrate-export assays distinguish rod/hook and filament export classes; historic uncertainties do not override later FliJ evidence. |
| paper-19 | DOI:10.1128/JB.182.15.4207-4215.2000; Full text Introduction and Discussion | supports | Full text Introduction and Discussion: FliJ interactions are explicitly discussed as prior work; null mutants retain leaky motility, and temperature-shift experiments identify FliJ as a general export factor. |
| paper-20 | DOI:10.1371/journal.pbio.2002281; Full text Introduction and Results, oligomeric state and copurification sections | supports | Full text Introduction and Results, oligomeric state and copurification sections: isolated FliP hexamers and detergent-dependent associations, not FliP5Q4R1FlhB1 reconstruction. |
| paper-21 | DOI:10.1371/journal.pgen.1001143; Abstract and full-text introductory context | supports | Abstract and full-text introductory context: FliO deletion/bypass and coexpression experiments support an assembly/stability role outside the conserved mature core. |
| paper-22 | DOI:10.1371/journal.ppat.1005495; Full text Results sodium blockers, ATPase deletions and Discussion | supports | Full text Results sodium blockers, ATPase deletions and Discussion: sodium-dependent export in ATPase-compromised Salmonella contrasts with PMF-coupled wild type. |
| paper-23 | DOI:10.3389/fmicb.2015.00023; Review abstract and established comparative context | supports | Review abstract and established comparative context: archaella are type-IV-pilus-related, not bacterial flagellar structures. |
| go-0009425 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009425; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| go-0009431 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009431; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| go-0120102 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0120102; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| interpro-ipr000563 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000563/; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| interpro-ipr005837 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005837/; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| interpro-ipr006136 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006136/; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| interpro-ipr006301 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006301/; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| interpro-ipr006303 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006303/; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| interpro-ipr006305 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006305/; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| interpro-ipr012823 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012823/; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| uniprotkb-p0a1k1 | https://rest.uniprot.org/uniprotkb/P0A1K1.json; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| uniprotkb-p0a1l5 | https://rest.uniprot.org/uniprotkb/P0A1L5.json; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| uniprotkb-p15934 | https://rest.uniprot.org/uniprotkb/P15934.json; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| uniprotkb-p26465 | https://rest.uniprot.org/uniprotkb/P26465.json; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| uniprotkb-p40727 | https://rest.uniprot.org/uniprotkb/P40727.json; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| uniprotkb-p40729 | https://rest.uniprot.org/uniprotkb/P40729.json; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| uniprotkb-p54700 | https://rest.uniprot.org/uniprotkb/P54700.json; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| uniprotkb-p54702 | https://rest.uniprot.org/uniprotkb/P54702.json; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| ncbitaxon-2 | https://rest.uniprot.org/taxonomy/2.json; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| ncbitaxon-2157 | https://rest.uniprot.org/taxonomy/2157.json; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| ncbitaxon-90371 | https://rest.uniprot.org/taxonomy/90371.json; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| ncbitaxon-99287 | https://rest.uniprot.org/taxonomy/99287.json; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| kuhlen2018 | DOI:10.1038/s41594-018-0086-9; Results, stoichiometry and helical architecture | supports | Salmonella Typhimurium FliP5Q4R1 is directly reconstructed; FliR is integrated and FliQ is peripheral, not an independently measured assembly sequence. |
| kuhlen2020 | DOI:10.1038/s41467-020-15071-9; Results, architecture, topology and Methods | supports | Vibrio mimicus FliP5Q4R1-FlhB1 shows FlhB around the base; this is not a Salmonella 2017 reconstruction. |
| ipr005714 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005714/; Family scope | supports | Mixed flagellar/injectisome ATPase family and narrower FliI clade support retaining FliI label-only scope. |
| ipr020005 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020005/; Family scope | supports | Mixed flagellar/injectisome ATPase family and narrower FliI clade support retaining FliI label-only scope. |
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
review_id: 20261010T224657Z-flagellar-secretion-apparatus-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'bacterial-type flagellum secretion apparatus: scientific evidence review'
started_at: '2026-10-10T22:39:19Z'
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
  - path: data/structures/appendage/bacterial_type_flagellum_basal_body.yaml
    sha256: b73592ad4ea2dc9ea818266c440fb1e8e8070461592051cc9fa5c9c0c2a5c704
    role: context
  - path: data/structures/appendage/bacterial_type_flagellum_secretion_apparatus.yaml
    sha256: 09e7db75a8d0ac2c5b552f17880a029494229348275688dff2ec4cda7fcc7644
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
  - path: history/records/bacterial_type_flagellum_secretion_apparatus/2026-09-08T055224Z-claude-bc0dba.yaml
    sha256: 80a5ef3637eb2418cc604ee423af6348b2c45d3a43a18c7d1c45f0c753b6ffae
    role: context
  - path: history/records/bacterial_type_flagellum_secretion_apparatus/2026-09-08T055441Z-claude-68f36e.yaml
    sha256: 5e99658109c70a538b3342395310c86e4e9f120ccd3e98c3580a87aba33b9a2a
    role: context
  - path: history/records/bacterial_type_flagellum_secretion_apparatus/2026-09-08T063710Z-claude-886121.yaml
    sha256: d215737aa30dd4629698a4a5463f0b0de9248901e94ec183fbda34ddf613ef2f
    role: context
  - path: history/records/bacterial_type_flagellum_secretion_apparatus/2026-09-08T064542Z-claude-624821.yaml
    sha256: 6cee8b94451a3941c494fa373db8c0b57d3c644812a7987a881a3734d90bd6a4
    role: context
  - path: history/records/bacterial_type_flagellum_secretion_apparatus/2026-09-08T065716Z-claude-3234a8.yaml
    sha256: b7ccb84d2c5b8ab7a17a72b0a0af54b87a8a02fe4733d2ba74f63a2c57ed7ecf
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
- target_id: GO:0120102
  path: data/structures/appendage/bacterial_type_flagellum_secretion_apparatus.yaml
  label: bacterial-type flagellum secretion apparatus
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_secretion_apparatus.yaml
    role: maintained scientific record
scope:
  description: One complete native record, all present claims and history; no sampling.
  selection: 'Next sequential unassessed target in the 909-record goal worklist: data/structures/appendage/bacterial_type_flagellum_secretion_apparatus.yaml'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0120102
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - GO:0120102
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/appendage/bacterial_type_flagellum_secretion_apparatus.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Native check passed. Identifier gate skips unsupported namespaces; scoped
    authorities were independently inspected. Snippet check is not a scientific-support
    pass.
  scope_note: 2026-10-10T22:41:45Z to 2026-10-10T22:41:49Z; /private/tmp/csm-review-20261010T223824Z/checks/bacterial_type_flagellum_secretion_apparatus-schema.log;
    SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - GO:0120102
  command: .venv/bin/python scripts/validate_strict.py data/structures/appendage/bacterial_type_flagellum_secretion_apparatus.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Native check passed. Identifier gate skips unsupported namespaces; scoped
    authorities were independently inspected. Snippet check is not a scientific-support
    pass.
  scope_note: 2026-10-10T22:41:49Z to 2026-10-10T22:41:54Z; /private/tmp/csm-review-20261010T223824Z/checks/bacterial_type_flagellum_secretion_apparatus-strict.log;
    SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - GO:0120102
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/appendage/bacterial_type_flagellum_secretion_apparatus.yaml
    --report /private/tmp/csm-review-20261010T223824Z/checks/bacterial_type_flagellum_secretion_apparatus-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: Native check passed. Identifier gate skips unsupported namespaces; scoped
    authorities were independently inspected. Snippet check is not a scientific-support
    pass.
  scope_note: 2026-10-10T22:41:54Z to 2026-10-10T22:42:20Z; /private/tmp/csm-review-20261010T223824Z/checks/bacterial_type_flagellum_secretion_apparatus-snippets.log;
    SHA-256 6dd37ee986417b7e52fb91ab9180146c6a9f8269ac7688c88c58917880bac1f0
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:0120102
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
  - GO:0120102
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
  - GO:0120102
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
  - GO:0120102
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
  - GO:0120102
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
  - GO:0120102
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
  - GO:0120102
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
  - GO:0120102
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
  - GO:0120102
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  exit_code: 0
  summary: Salmonella core dataset gene-context search. No iModulon hit informed the
    verdict; text matches are not structure-membership evidence. Campylobacter is
    not covered.
  scope_note: 2026-10-10T22:40:49Z to 2026-10-10T22:40:50Z; log SHA-256 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- check_id: adapter-flha
  name: iModulonDB flhA
  status: passed
  required: false
  target_ids:
  - GO:0120102
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism s_enterica --dataset core --query flhA
  exit_code: 0
  summary: Salmonella core dataset gene-context search. No iModulon hit informed the
    verdict; text matches are not structure-membership evidence. Campylobacter is
    not covered.
  scope_note: 2026-10-10T22:40:54Z to 2026-10-10T22:40:55Z; log SHA-256 1c1b538ae1e8db2852d92fd68e3ae12312a5c6283d7c5ac22dd745278f4c150c
- check_id: adapter-flhb
  name: iModulonDB flhB
  status: passed
  required: false
  target_ids:
  - GO:0120102
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism s_enterica --dataset core --query flhB
  exit_code: 0
  summary: Salmonella core dataset gene-context search. No iModulon hit informed the
    verdict; text matches are not structure-membership evidence. Campylobacter is
    not covered.
  scope_note: 2026-10-10T22:40:55Z to 2026-10-10T22:40:55Z; log SHA-256 3f62a770c54e6437af0859b8fe58932280403b11fd810d149f448d3b0531d2bd
- check_id: adapter-flip
  name: iModulonDB fliP
  status: passed
  required: false
  target_ids:
  - GO:0120102
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism s_enterica --dataset core --query fliP
  exit_code: 0
  summary: Salmonella core dataset gene-context search. No iModulon hit informed the
    verdict; text matches are not structure-membership evidence. Campylobacter is
    not covered.
  scope_note: 2026-10-10T22:40:55Z to 2026-10-10T22:40:56Z; log SHA-256 97d350dea0ca638d1ed91508392872be9937f2d56de565abc263e00ca1fdb191
- check_id: adapter-fliq
  name: iModulonDB fliQ
  status: passed
  required: false
  target_ids:
  - GO:0120102
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism s_enterica --dataset core --query fliQ
  exit_code: 0
  summary: Salmonella core dataset gene-context search. No iModulon hit informed the
    verdict; text matches are not structure-membership evidence. Campylobacter is
    not covered.
  scope_note: 2026-10-10T22:40:56Z to 2026-10-10T22:40:57Z; log SHA-256 488aa5c55fbeee2a694620b2910282bee347c142853cce50ff37ef0ff44c8750
- check_id: adapter-flir
  name: iModulonDB fliR
  status: passed
  required: false
  target_ids:
  - GO:0120102
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism s_enterica --dataset core --query fliR
  exit_code: 0
  summary: Salmonella core dataset gene-context search. No iModulon hit informed the
    verdict; text matches are not structure-membership evidence. Campylobacter is
    not covered.
  scope_note: 2026-10-10T22:40:57Z to 2026-10-10T22:40:57Z; log SHA-256 1e3af1de2209132e01067f19ba84dd33ff0d06292a99c3f8b5252cec77263f93
- check_id: adapter-flih
  name: iModulonDB fliH
  status: passed
  required: false
  target_ids:
  - GO:0120102
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism s_enterica --dataset core --query fliH
  exit_code: 0
  summary: Salmonella core dataset gene-context search. No iModulon hit informed the
    verdict; text matches are not structure-membership evidence. Campylobacter is
    not covered.
  scope_note: 2026-10-10T22:40:57Z to 2026-10-10T22:40:58Z; log SHA-256 0dbfc2f1ae3605a18262043b65af3b829c8f48e1f8dcb38a058a15c2cb24571d
- check_id: adapter-flii
  name: iModulonDB fliI
  status: passed
  required: false
  target_ids:
  - GO:0120102
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism s_enterica --dataset core --query fliI
  exit_code: 0
  summary: Salmonella core dataset gene-context search. No iModulon hit informed the
    verdict; text matches are not structure-membership evidence. Campylobacter is
    not covered.
  scope_note: 2026-10-10T22:40:58Z to 2026-10-10T22:40:58Z; log SHA-256 efca146f2b6eaf9fbd249a5e047288c5a200ab5b2e8b972a6769bd7e05fce57d
- check_id: adapter-flij
  name: iModulonDB fliJ
  status: passed
  required: false
  target_ids:
  - GO:0120102
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism s_enterica --dataset core --query fliJ
  exit_code: 0
  summary: Salmonella core dataset gene-context search. No iModulon hit informed the
    verdict; text matches are not structure-membership evidence. Campylobacter is
    not covered.
  scope_note: 2026-10-10T22:40:58Z to 2026-10-10T22:40:59Z; log SHA-256 1642e41da3db1fc403440a5dc66f5c1612f933d96f168292fb7688bc4135f141
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/appendage/bacterial_type_flagellum_secretion_apparatus.yaml
  locator: Entire target YAML, schema and recorded input histories
  accessed_at: '2026-10-10T22:46:57Z'
  support: context_only
  summary: Complete record read; maintained ownership and PROPOSED status retained.
    Neighboring parts checked for identity/parthood, not counted as new reviews.
- evidence_id: paper-00
  kind: primary_source
  reference: DOI:10.1007/82_2019_170
  locator: Abstract
  accessed_at: '2026-10-10T22:40:28Z'
  snapshot_sha256: 094767a5fb71610b43bac3627fc935a1fb967390844a1e8066c891674acd192d
  support: supports
  summary: 'Abstract: membrane export gate and cytoplasmic ATPase are distinct parts
    of the basal-body export machinery.'
- evidence_id: paper-02
  kind: primary_source
  reference: DOI:10.1016/j.bbamcr.2013.09.005
  locator: Abstract
  accessed_at: '2026-10-10T22:40:29Z'
  snapshot_sha256: 768fdf17054ce15656cd912d6c62453168a473b0b797ae87873af30bbfdd566a
  support: supports
  summary: 'Abstract: axial protein export, ATPase-assisted entry and FliJ-FlhA coupling;
    older FliO inventory is refined by later assembly studies.'
- evidence_id: paper-09
  kind: primary_source
  reference: DOI:10.1038/nrmicro1887
  locator: Review context
  accessed_at: '2026-10-10T22:40:35Z'
  snapshot_sha256: 648eac60aca511dba55bd983fcc746cd1c173f143b5259fa8bd78daa609ca3c6
  support: supports
  summary: 'Review context: coordinated assembly and conditional occurrence in flagellated
    bacteria; not an all-Bacteria prevalence census.'
- evidence_id: paper-12
  kind: primary_source
  reference: DOI:10.1038/s42003-024-06081-0
  locator: Full text Introduction, mutant Results and Fig. 1
  accessed_at: '2026-10-10T22:40:41Z'
  snapshot_sha256: 19258fd6576cbf0b5a726a667e820d14d51f11174007c61426fe6ef8f07b871f
  support: supports
  summary: 'Full text Introduction, mutant Results and Fig. 1: FlhA GYXLI-mutant phenotypes
    support ATPase-assisted ordering; Fig. 1 uses modeled ATPase assembly.'
- evidence_id: paper-13
  kind: primary_source
  reference: DOI:10.1073/pnas.1524025113
  locator: Abstract
  accessed_at: '2026-10-10T22:40:42Z'
  snapshot_sha256: 9342e85433a3a3bf79436962b57ceb97039f92d2a65d19cdff9a2e887d6406c0
  support: supports
  summary: 'Abstract: solved FliH C-terminal homodimer-FliI complex is distinct from
    the proposed hexamer model; complete ATPase assembly was not directly resolved
    by this paper.'
- evidence_id: paper-16
  kind: primary_source
  reference: DOI:10.1111/mmi.12529
  locator: Abstract
  accessed_at: '2026-10-10T22:40:46Z'
  snapshot_sha256: 47b9098caf7be7493c050705a75707031ca7907595972f61051c37f3d2cf3547
  support: supports
  summary: 'Abstract: fluorescence measurements estimate about nine FlhA molecules
    and show coordinated assembly with the MS ring.'
- evidence_id: paper-18
  kind: primary_source
  reference: DOI:10.1128/JB.181.5.1388-1394.1999
  locator: Abstract
  accessed_at: '2026-10-10T22:40:48Z'
  snapshot_sha256: 4bf4116fb7df61b9a40845e045056bb3e2ab2ada22063a2014da1c2b341c4df8
  support: supports
  summary: 'Abstract: mutant substrate-export assays distinguish rod/hook and filament
    export classes; historic uncertainties do not override later FliJ evidence.'
- evidence_id: paper-19
  kind: primary_source
  reference: DOI:10.1128/JB.182.15.4207-4215.2000
  locator: Full text Introduction and Discussion
  accessed_at: '2026-10-10T22:41:31Z'
  snapshot_sha256: 57c2e837c363c9fd3e5933975b7dba79c9e73cee5cf9740084aa3d5ab52ec869
  support: supports
  summary: 'Full text Introduction and Discussion: FliJ interactions are explicitly
    discussed as prior work; null mutants retain leaky motility, and temperature-shift
    experiments identify FliJ as a general export factor.'
- evidence_id: paper-20
  kind: primary_source
  reference: DOI:10.1371/journal.pbio.2002281
  locator: Full text Introduction and Results, oligomeric state and copurification
    sections
  accessed_at: '2026-10-10T22:40:52Z'
  snapshot_sha256: 269798c3e008d2d3c5fc49e39fb99dbb5a12e381b8e9bf106115bb65f8071b60
  support: supports
  summary: 'Full text Introduction and Results, oligomeric state and copurification
    sections: isolated FliP hexamers and detergent-dependent associations, not FliP5Q4R1FlhB1
    reconstruction.'
- evidence_id: paper-21
  kind: primary_source
  reference: DOI:10.1371/journal.pgen.1001143
  locator: Abstract and full-text introductory context
  accessed_at: '2026-10-10T22:40:53Z'
  snapshot_sha256: d72bc529b0e03696b62ddfd195cc88e8a133f99f36a7197e50b3deb14e232a83
  support: supports
  summary: 'Abstract and full-text introductory context: FliO deletion/bypass and
    coexpression experiments support an assembly/stability role outside the conserved
    mature core.'
- evidence_id: paper-22
  kind: primary_source
  reference: DOI:10.1371/journal.ppat.1005495
  locator: Full text Results sodium blockers, ATPase deletions and Discussion
  accessed_at: '2026-10-10T22:40:55Z'
  snapshot_sha256: 5b4edd242fc3d5653a65316bdcacb05220f6d3aa27dda347f8ba35a5c625426b
  support: supports
  summary: 'Full text Results sodium blockers, ATPase deletions and Discussion: sodium-dependent
    export in ATPase-compromised Salmonella contrasts with PMF-coupled wild type.'
- evidence_id: paper-23
  kind: primary_source
  reference: DOI:10.3389/fmicb.2015.00023
  locator: Review abstract and established comparative context
  accessed_at: '2026-10-10T22:40:56Z'
  snapshot_sha256: 5e2b4c125d1d01c22b2d7eb326b7e73bb6b17e9d1c0b660c785ea11667745677
  support: supports
  summary: 'Review abstract and established comparative context: archaella are type-IV-pilus-related,
    not bacterial flagellar structures.'
- evidence_id: go-0009425
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009425
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:01Z'
  snapshot_sha256: 9fce7e21efecbd6edee814457befdcbf6d3ae546aaefe4cc9aa56657b40e75c3
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: go-0009431
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009431
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:01Z'
  snapshot_sha256: 8fa717593fed9c5b9a18b86d902b375a8f28422667e63070ee4988be66704544
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: go-0120102
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0120102
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:04Z'
  snapshot_sha256: 055a3f19d9543943bae1968a31e6e38237a324177cfc4838170addef9e155be7
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: interpro-ipr000563
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000563/
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:06Z'
  snapshot_sha256: da032e6daa2729b74eab74384f35cb289030007d77375d61d0991c9d3f468bf1
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: interpro-ipr005837
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005837/
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:06Z'
  snapshot_sha256: 4aeec8e78fa51c118c7c252827abac929456c4f49696138dbf23754cc6d7ab9f
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: interpro-ipr006136
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006136/
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:07Z'
  snapshot_sha256: 17aa937c9237830f6fdbfd313d8d0621128189f71d80499a3a959f068ddc25ca
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: interpro-ipr006301
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006301/
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:07Z'
  snapshot_sha256: dac127fb9423cd80fcb00ffcbc6a9a52aad30aa017cf4277cdc4ff7bb72f9b89
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: interpro-ipr006303
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006303/
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:09Z'
  snapshot_sha256: 0eff657e3ceedd37a2a443a9c9d2ce8b8ba805208086256ed9e4daa6ede92835
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: interpro-ipr006305
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006305/
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:09Z'
  snapshot_sha256: 7116fae07149a094a565ba362726d4ef2be82f599e451a54b8ba6fa7424d9459
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: interpro-ipr012823
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012823/
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:10Z'
  snapshot_sha256: 9ed57d962a1db87bea7ed65bca0eff2dbef1c0e0cd8f9bcdde4c9ce7ae95ce98
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: uniprotkb-p0a1k1
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0A1K1.json
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:11Z'
  snapshot_sha256: dccaeed0ce183620be6057154dac4fce1ed00f3344d843146f4959bb79be63f5
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: uniprotkb-p0a1l5
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0A1L5.json
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:11Z'
  snapshot_sha256: 213efa332ee418f7e57cde18af9bd30c03b40eec8058df89129ca4f2760eeb25
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: uniprotkb-p15934
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P15934.json
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:12Z'
  snapshot_sha256: 8cb6c4b9232608015ae7dffabf69d04620c734bea1d8213cb523d658252a23f1
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: uniprotkb-p26465
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P26465.json
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:12Z'
  snapshot_sha256: f90c3356bc134ea01f7deb28628cdac4d92ab835cfed5ef610676a12e8283c9b
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: uniprotkb-p40727
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P40727.json
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:13Z'
  snapshot_sha256: 83267535894609c8071bf26fd3ac30e3aace016fdbc663160e3ab52cf6f1c948
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: uniprotkb-p40729
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P40729.json
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:14Z'
  snapshot_sha256: 1ad67856f963a01dc7a862d448e7c57ece9db0b4683ea5cf6045551058ce8f6d
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: uniprotkb-p54700
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P54700.json
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:15Z'
  snapshot_sha256: 92716e36e5df581ba3fbbce12fe8b0e098050165c2d445ee5de84530e1645944
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: uniprotkb-p54702
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P54702.json
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:15Z'
  snapshot_sha256: f5d8f69e84b8946a569a6f9661857dabe309aeb56662affcfe4172ca2abaf808
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
- evidence_id: ncbitaxon-90371
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/90371.json
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:18Z'
  snapshot_sha256: 46c958747209e78a835996643e63aafb6d1e94a8a632f0094dba733eb1bd3dee
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: ncbitaxon-99287
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/99287.json
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:18Z'
  snapshot_sha256: 107ebfece75c5a7147abe7547dec9166f87ff267e6cbc3f67bea9ab9df694a59
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: kuhlen2018
  kind: primary_source
  reference: DOI:10.1038/s41594-018-0086-9
  locator: Results, stoichiometry and helical architecture
  accessed_at: '2026-10-10T22:42:25Z'
  snapshot_sha256: 84119543ebc833359db85a898054a9d7373eb9461856beaf55e6dfeb3d5a8bae
  support: supports
  summary: Salmonella Typhimurium FliP5Q4R1 is directly reconstructed; FliR is integrated
    and FliQ is peripheral, not an independently measured assembly sequence.
- evidence_id: kuhlen2020
  kind: primary_source
  reference: DOI:10.1038/s41467-020-15071-9
  locator: Results, architecture, topology and Methods
  accessed_at: '2026-10-10T22:42:27Z'
  snapshot_sha256: 79e116a60e00199c24c484a4bd7dcd945673fc7edb0211c15a9de27c7c11180e
  support: supports
  summary: Vibrio mimicus FliP5Q4R1-FlhB1 shows FlhB around the base; this is not
    a Salmonella 2017 reconstruction.
- evidence_id: ipr005714
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005714/
  locator: Family scope
  accessed_at: '2026-10-10T22:42:34Z'
  snapshot_sha256: 2ca94be2375f8785c55b6e9cb0b2e8a4d081481056375a1d0aca5a3cdda6e72f
  support: supports
  summary: Mixed flagellar/injectisome ATPase family and narrower FliI clade support
    retaining FliI label-only scope.
- evidence_id: ipr020005
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020005/
  locator: Family scope
  accessed_at: '2026-10-10T22:42:35Z'
  snapshot_sha256: 4bde8c0f0532639f234f9e2d7e30b1f90a35401436779ee783afa4e6dd9a14cd
  support: supports
  summary: Mixed flagellar/injectisome ATPase family and narrower FliI clade support
    retaining FliI label-only scope.
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
  - GO:0120102
  evidence_ids:
  - record
  - go-0120102
  summary: Exact active GO cellular-component identity. Rotor/stator/motor/export-apparatus
    boundaries are explicit and not equated with a single protein or whole flagellum.
- assessment_id: taxonomy
  area: scope
  topic: Domain distribution and canonical example
  outcome: concern
  target_ids:
  - GO:0120102
  evidence_ids:
  - record
  - paper-23
  summary: Bacteria VARIABLE is conditional on flagellar systems; archaella are distinct.
    Named taxa resolve; the export-core example overattributes the experiment and
    is covered by F1.
- assessment_id: composition
  area: evidence
  topic: All eight components, counts, protein examples and source precision
  outcome: concern
  target_ids:
  - GO:0120102
  evidence_ids:
  - record
  - paper-13
  - paper-16
  - paper-20
  - kuhlen2018
  - kuhlen2020
  summary: Gene/taxon examples and seven family groundings resolve. FliI label-only
    boundary is justified. ATPase dispensability has mutant evidence; incorrect historical
    architecture and model-resolution notes require correction.
  dimensions:
  - name: evidence_tier
    value: Primary structural/functional experiments versus explicitly identified
      mechanistic models
    definition: Observed assembly or dynamics are distinguished from model-derived
      trajectories and organism extrapolation
    evidence_ids:
    - paper-13
    - paper-22
- assessment_id: function-graph
  area: graph
  topic: All functions and eleven causal edges
  outcome: concern
  target_ids:
  - GO:0120102
  evidence_ids:
  - record
  - paper-12
  - paper-19
  - paper-20
  - paper-22
  - kuhlen2018
  - kuhlen2020
  summary: Axial substrate export, ATPase association and substrate ordering are supported.
    Core geometry, experimental provenance and ion-coupling conditions require the
    bounded fixes below.
- assessment_id: quantities
  area: quantity
  topic: All stoichiometries; no separate physical properties
  outcome: concern
  target_ids:
  - GO:0120102
  evidence_ids:
  - record
  - paper-13
  - paper-16
  - kuhlen2018
  - kuhlen2020
  summary: Counts are biologically plausible but require correct preparation, organism
    and modeled-versus-measured attribution; no new universal counts should be introduced.
- assessment_id: provenance
  area: provenance
  topic: Discussions, histories, status and optional sections
  outcome: supported
  target_ids:
  - GO:0120102
  evidence_ids:
  - record
  - prior-search
  summary: Both history surfaces and resolved boundaries were read. Preserve historical
    events, stable identity and PROPOSED status. No images, traits, external complex
    compositions or transcriptomic datasets are asserted; empty optional fields do
    not qualify as findings.
findings:
- finding_id: F1
  issue_key: flagellar-export-core-stoichiometry-provenance
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Modern export-core architecture is falsely attributed to Fukumura 2017
  description: Multiple component, exemplar, function, graph and discussion claims
    assign a FliP5Q4R1-FlhB1 reconstruction to the 2017 paper. It reports isolated
    FliP hexamers and detergent-sensitive associations. Kuhlen 2018 resolves Salmonella
    FliP5Q4R1; Kuhlen 2020 resolves Vibrio mimicus FliP5Q4R1-FlhB1. The latter also
    places FlhB around the base, not as a cap, and FliR within a helical P/R core.
  target_ids:
  - GO:0120102
  field_paths:
  - definition
  - components[1:5]
  - canonical_examples[0]
  - functions[1]
  - causal_graphs[0].description
  - causal_graphs[0].edges[0:3]
  - causal_graphs[0].edges[10]
  - discussions[0].rationale
  evidence_ids:
  - record
  - paper-20
  - kuhlen2018
  - kuhlen2020
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_secretion_apparatus.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#evidence
  native_severity: major
  normalization_reason: Unsupported or conflicting scientific scope.
- finding_id: F2
  issue_key: flagellar-export-atpase-model-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: ATPase model is described as a resolved complete complex
  description: FliH/FliI/FliJ component notes use resolved/placed language for the
    complete FliH12-FliI6-FliJ1 complex. The primary abstract distinguishes the solved
    FliH C-terminal dimer-FliI heterotrimer from a hexamer model. The graph already
    partly uses modeled, so the current notes are inconsistent.
  target_ids:
  - GO:0120102
  field_paths:
  - components[5:8].stoichiometry
  - components[5:8].evidence
  - causal_graphs[0].edges[4:6]
  evidence_ids:
  - record
  - paper-13
  - paper-12
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_secretion_apparatus.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#evidence
  native_severity: minor
  normalization_reason: Bounded provenance, claim-qualification or grounding defect;
    record identity is sound.
- finding_id: F3
  issue_key: flagellar-export-dual-fuel-atpase-context
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Sodium coupling is conflated with the intact ATPase-assisted state
  description: The energy function combines soluble ATPase and proton-or-sodium driving
    force without experimental conditions. The cited 2016 study finds sodium-dependent
    export when the ATPase system is compromised and no sodium dependence with the
    entire FliH/FliI/FliJ complex. Broad component and graph wording likewise drops
    this key contrast.
  target_ids:
  - GO:0120102
  field_paths:
  - components[0].role
  - components[6].evidence[1]
  - functions[2]
  - causal_graphs[0].description
  - causal_graphs[0].nodes
  - causal_graphs[0].edges[8]
  evidence_ids:
  - record
  - paper-22
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_secretion_apparatus.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#evidence
  native_severity: major
  normalization_reason: Unsupported or conflicting scientific scope.
actions:
- action_id: A1
  description: Resource modern counts/geometry to the inspected 2018/2020 structures
    with organism context. Correct cap/ring and whole-apparatus localization wording;
    do not infer an assembly sequence from a static structure. Preserve FliO historical
    evidence and exclusion rationale.
  finding_ids:
  - F1
  target_ids:
  - GO:0120102
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_secretion_apparatus.yaml
    role: maintained scientific record
  acceptance_checks:
  - No current claim attributes a 5:4:1:1 reconstruction to 2017.
  - Salmonella PQR and Vibrio PQR-FlhB are distinguished; modern counts remain supported
    at each claim.
  - FlhB wraps the gate base, FliR is integrated, and FliQ peripheral; historical
    events are unchanged.
  - Guarded write, both append-only histories, PROPOSED status, regenerated affected
    artifacts, native validators and authoritative QC pass.
- action_id: A2
  description: Identify the solved fragment heterotrimer and modeled full ATPase assembly,
    including count context; retain supported membership.
  finding_ids:
  - F2
  target_ids:
  - GO:0120102
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_secretion_apparatus.yaml
    role: maintained scientific record
  acceptance_checks:
  - No complete FliH12-FliI6-FliJ1 reconstruction is attributed to Imada 2016.
  - Measured fragment structure and assembled model are explicitly distinct.
  - Guarded write, both append-only histories, PROPOSED status, regenerated affected
    artifacts, native validators and authoritative QC pass.
- action_id: A3
  description: State the Salmonella wild-type PMF versus ATPase-compromised sodium-capable
    contrast at the function and energy edge; add appropriate source support to FlhA
    coupling.
  finding_ids:
  - F3
  target_ids:
  - GO:0120102
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_secretion_apparatus.yaml
    role: maintained scientific record
  acceptance_checks:
  - No claim says the intact Salmonella ATPase-assisted system used sodium in that
    experiment.
  - Retain demonstrated sodium capability with genotype and condition context; do
    not generalize to every bacterial export apparatus.
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
