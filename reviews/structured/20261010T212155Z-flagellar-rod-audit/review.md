# bacterial-type flagellum basal body, rod: evidence and scope review

- Review: 20261010T212155Z-flagellar-rod-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-10T21:01:38Z
- Finished UTC: 2026-10-10T21:21:55Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

All present native sections assessed at the captured revision. Unsupported bacterial prevalence requires curation. The FliE label-only rationale also requires updating against current authority evidence.

## Scope And Provenance

One complete maintained record, all present scientific fields and both history surfaces; scientific inputs unchanged.

Selection: Next sequential unassessed record in the all-record worklist: data/structures/appendage/bacterial_type_flagellum_basal_body_rod.yaml
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base eb734ac4a4efcfd2cfb3abaf7562a6695f23c74b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0030694 | data/structures/appendage/bacterial_type_flagellum_basal_body_rod.yaml | maintained | bacterial-type flagellum basal body, rod |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0030694 | Documented check completed successfully; biological support was assessed separately. |
| strict | passed | True | GO:0030694 | Documented check completed successfully; biological support was assessed separately. |
| history | passed | True | GO:0030694 | Documented check completed successfully; biological support was assessed separately. |
| traits | passed | True | GO:0030694 | Documented check completed successfully; biological support was assessed separately. This target has no trait links; this is a corpus-wide check. |
| labels | passed | True | GO:0030694 | Documented check completed successfully; biological support was assessed separately. |
| curies | passed | True | GO:0030694 | Documented check completed successfully; biological support was assessed separately. The full-corpus checker skips unsupported namespaces; a zero exit is not verification of those skipped identifiers. |
| qc | passed | True | GO:0030694 | Documented check completed successfully; biological support was assessed separately. |
| imodulondb-datasets | passed | False | GO:0030694 | Structured adapter consulted: exact Salmonella core gene matches, no iModulon hits. Gene identity context only. |
| imodulondb-flgg | passed | False | GO:0030694 | Structured adapter consulted: exact Salmonella core gene matches, no iModulon hits. Gene identity context only. |
| imodulondb-flie | passed | False | GO:0030694 | Structured adapter consulted: exact Salmonella core gene matches, no iModulon hits. Gene identity context only. |
| imodulondb-flgb | passed | False | GO:0030694 | Structured adapter consulted: exact Salmonella core gene matches, no iModulon hits. Gene identity context only. |
| imodulondb-flgc | passed | False | GO:0030694 | Structured adapter consulted: exact Salmonella core gene matches, no iModulon hits. Gene identity context only. |
| imodulondb-flgf | passed | False | GO:0030694 | Structured adapter consulted: exact Salmonella core gene matches, no iModulon hits. Gene identity context only. |

## Scientific And Domain Assessments

### Structure identity, synonyms, hierarchy and parthood

identity: supported. Targets: GO:0030694.

Exact active GO cellular component denotes the named polymer/ring, not an individual protein. Native definitions and synonyms agree; rod segments belong to the rod and the rod/MS ring to the basal body.

### Every listed constituent, role, essentiality and protein example

evidence: supported. Targets: GO:0030694.

FliF alone is the core MS ring; FlgG is the distal rod; FliE/FlgB/FlgC/FlgF constitute the proximal segment, with FlgG added for the whole rod. Only the relevant components are asserted in this target. Structural membership and cooperative stable assembly support the constituent model; this is not new proof of every deletion phenotype in every lineage. Current protein accessions, reviewed status, genes and LT2 taxon agree.

### Family scope and reviewed-label-only decisions

grounding: concern. Targets: GO:0030694.

FlgB/FlgC and, where present, FlgG exact family identities are supported. FliE now has an exact matched family despite its label-only status. FlgF remains a distinct, bounded grounding uncertainty; an exact-name candidate alone is not sufficient.

### All distribution rows and organism exemplars

scope: concern. Targets: GO:0030694.

The Salmonella exemplar and bacterial/archaellum distinction are supported. COMMON overstates prevalence at the Bacteria denominator. Use a defensible patchy/lineage-dependent category and retain genomic-proxy limits instead of turning marker frequency into observed anatomy.

### Both functions, all graph nodes and every edge

graph: supported. Targets: GO:0030694.

Checked all 9 edges. Axial adjacency, constituent assembly, envelope bushing topology and mechanical coupling are supported in the cited model system. Spatial composition is not interpreted as a directly observed dynamic assembly trajectory. No unsupported stator rotation model is asserted here.

### Stoichiometry and physical properties

quantity: not_applicable. Targets: GO:0030694.

No quantitative physical-property or stoichiometry assertion is present; absent optional measurements are not defects.

### Discussions, histories, status and omitted optional sections

provenance: supported. Targets: GO:0030694.

Read every discussion and both history surfaces. Resolved boundary decisions distinguish neighboring structures and transient assembly factors; PROPOSED is appropriate. No trait, pathway, image, dataset or external complex-composition claim is present. Their absence is not a finding. Bibliographic abstracts and full-text access limits remain explicit.

## Findings

### F1: Bacterial prevalence exceeds the cited evidence

major / open / confirmed; issue key: flagellar-rod-bacterial-prevalence-common.

COMMON means present in most members with exceptional losses under the native enum. The note only conditions occurrence on flagella, while the cited GO definition or assembly review does not establish a majority of Bacteria. Independent genomic evidence favors heterogeneous occurrence and does not justify this majority assertion.

### F2: FliE label-only status is stale against an exact family match

minor / open / confirmed; issue key: flagellar-rod-flie-label-only-status.

The native REVIEWED_LABEL_ONLY flag means no exact family can be asserted. Current InterPro IPR001624 is an integrated FliE family, and the record's reviewed Salmonella FliE example P26462 matches it. This is not an empty optional slot: the positive no-exact-family decision now has a concrete contrary authority result. Historical curation rationale should remain distinguishable from current state.

## Recommended Actions And Acceptance Checks

### A1

Curate the maintained occurrence row to VARIABLE or a narrower evidence-backed taxonomic statement; cite inspected support and retain the distinction between marker-bearing genomes and observed structures. Preserve archaellum distinction and native PROPOSED status.

- The row no longer asserts majority bacterial prevalence without appropriate evidence.
- Schema/strict validation, identifier/label and history checks pass; regenerate maintained-derived products through repository commands if scientific content changes.

### A2

Verify IPR001624 against the declared FliE scope and current reviewed example, add the supported exact grounding and retire the incompatible current label-only status. Retain the historical reason and append a dated current-state explanation. Do not infer an analogous FlgF fix from this evidence.

- IPR001624 is verified as the exact FliE family, not a domain or broader homologous superfamily.
- P26462 family match and current gene/taxon identity are recorded; native label correspondence, strict schema and history gates pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/bacterial_type_flagellum_basal_body_rod.yaml; Entire native YAML, schema enums, and recorded repository histories | context_only | Full record and histories read. All input hashes remain as captured. PROPOSED status retained; no curation events appended. |
| paper-00 | DOI:10.1016/j.cell.2021.03.057; Primary abstract | supports | Cryo-EM of a Salmonella rod-hook-motor complex identifies MS-ring, FliE and FlgB contacts involved in mechanical coupling. |
| paper-01 | DOI:10.1038/nrmicro1887; Review abstract and publisher preview/key points, not subscription main text | supports | The inspected text addresses coordinated flagellar gene regulation and assembly in Gram-negative bacteria, not a denominator-bearing estimate of bacterial prevalence. |
| paper-03 | DOI:10.1038/s41467-021-24715-3; Full text: Introduction, Results LP-ring reconstruction and FlgH/FlgI structures, Figs. 1-4, methods | supports | Salmonella FlgH and FlgI form the outer-membrane and peptidoglycan sides of a 26-fold LP bushing around the distal rod. |
| paper-04 | DOI:10.1038/s41564-021-00895-y; Author manuscript full text: Introduction, rod reconstruction, Fig. 2, MS-ring contacts, Fig. 3, methods | supports | Intact Salmonella basal bodies resolve proximal FliE/FlgB/FlgC/FlgF, distal FlgG, and their spatial contacts. The measured architecture is not an all-bacterial prevalence survey. |
| paper-06 | DOI:10.1128/jb.182.11.3029-3036.2000; Primary abstract; no successful full-text retrieval | supports | Genetic suppressors and affinity blotting support strong FliE-FlgB interaction. The older proposed junction model is distinguished from later resolved structures. |
| paper-09 | DOI:10.3389/fmicb.2015.00023; Review full text: historical structural/genomic comparisons, paragraphs 15-18 | supports | Archaella are evolutionarily and structurally distinct from the bacterial rod-and-ring apparatus; the source describes EM and genomic evidence for this distinction. |
| paper-10 | DOI:10.1128/jb.182.11.3029-3036.2000; Primary abstract; identical paper to DOI evidence paper-06 | supports | PMID 10809679 resolves to the FliE-FlgB interaction study cited in UniProt localization provenance. |
| paper-11 | DOI:10.1006/jmbi.2001.4963; Primary abstract | supports | Salmonella FlgJ mutant experiments support its assembly role and interactions with FliE/FlgB; they do not make FlgJ a mature rod constituent. |
| paper-12 | DOI:10.1016/j.jmb.2004.03.070; Primary abstract | supports | All five Salmonella rod proteins were purified from an E. coli expression system. In-vitro fibrils were explicitly distinguished from the native rod; the source describes rod torque transmission. |
| paper-13 | DOI:10.1073/pnas.89.11.4801; Primary abstract | supports | Mass measurements of isolated Salmonella basal-body subcomplexes support historical rod-protein localization and approximate composition, not replacement of later cryo-EM counts. |
| go-0009424 | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0009424; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| go-0009425 | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0009425; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| go-0009426 | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0009426; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| go-0009429 | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0009429; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| go-0030694 | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0030694; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| interpro-ipr006299 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006299/; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| interpro-ipr006300 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006300/; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| interpro-ipr012834 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012834/; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| uniprotkb-p0a1i7 | https://rest.uniprot.org/uniprotkb/P0A1I7.json; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| uniprotkb-p0a1j3 | https://rest.uniprot.org/uniprotkb/P0A1J3.json; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| uniprotkb-p16323 | https://rest.uniprot.org/uniprotkb/P16323.json; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| uniprotkb-p16437 | https://rest.uniprot.org/uniprotkb/P16437.json; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| uniprotkb-p26462 | https://rest.uniprot.org/uniprotkb/P26462.json; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| ncbitaxon-2 | https://rest.uniprot.org/taxonomy/2.json; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| ncbitaxon-2157 | https://rest.uniprot.org/taxonomy/2157.json; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| ncbitaxon-90371 | https://rest.uniprot.org/taxonomy/90371.json; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| ncbitaxon-99287 | https://rest.uniprot.org/taxonomy/99287.json; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| synonym-scopes | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009426,GO:0009427,GO:0009428,GO:0009429,GO:0009431,GO:0030694; Exact six GO records, definitions and typed synonyms | supports | Source synonym types checked against QuickGO, alongside exact OLS identities. |
| distribution | DOI:10.1073/pnas.2512476122; Results computational distribution paragraph; Methods reference-genome/HMM design | refutes | Across 30,238 GTDB genomes from 131 phyla, approximately 40% carry FliPQR markers. This is a genomic proxy, not a microscopy census or direct rod/ring prevalence measurement. |
| assembly | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2F0022-2836%2892%2990958-m%22&amp;format=json&amp;resultType=core; Primary abstract | supports | Salmonella precursor analysis distinguishes autonomous MS-ring formation from cooperative assembly of FliE and the four rod proteins into a stable structure. The unseen individual mutant results are not certified. |
| flie-family | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001624/; metadata accession, family type, name, integrated signatures | refutes | Exact FliE family IPR001624 is present. The curated Salmonella example P26462 independently carries this family cross-reference. |
| flgf-family-context | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012836/; Narrow family entry and current P16323 cross-references | context_only | A narrower FlgF entry exists, but P16323 does not currently match it. No automatic FlgF grounding is justified by name alone. |
| prior-search | reviews/; Recursive structured target-ID inspection | context_only | No previous canonical target review for this record. Prior bibliography mentions are not target assessments. |

## Limits And Additional Notes

- A complete assessment of this record is not completion of the 909-record goal, a new experimental result, or human scientific approval. Proposed fixes are not performed by this review.
- Some historical sources were inspected as abstracts only. Europe PMC full-text endpoints returned errors for several records; BioC sometimes returned an error document rather than article text. Publisher access attempts included subscription previews and HTTP 403 responses. No unread main-text details or figures are certified.
- The distribution survey uses FliPQR markers in a reference-genome sample. Its frequency is not direct observation of this rod/ring and is not a census of all bacterial cells, species or environments.
- Source-supported assembly and topology primarily concern Salmonella. Broad family labels are not proof of identical stoichiometry or accessory architecture across every bacterial lineage.
- The full-corpus identifier checker skips unsupported namespaces. Fresh scoped GO, InterPro, UniProt and taxon checks are separately recorded; the successful global exit is not blanket identifier certification.
- The optional HTML inspection initially found BeautifulSoup unavailable; the standard-library HTMLParser was then used to inspect publisher previews. This was a tooling fallback, not a failed native scientific gate.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T212155Z-flagellar-rod-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'bacterial-type flagellum basal body, rod: evidence and scope review'
started_at: '2026-10-10T21:01:38Z'
finished_at: '2026-10-10T21:21:55Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Agent audit of pre-existing maintained records; not independent
    human approval. Scientific inputs were not edited in this assessment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: All present native sections assessed at the captured revision. Unsupported
  bacterial prevalence requires curation. The FliE label-only rationale also requires
  updating against current authority evidence.
source:
  git_revision: eb734ac4a4efcfd2cfb3abaf7562a6695f23c74b
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
  - path: data/structures/appendage/bacterial_type_flagellum_basal_body_rod.yaml
    sha256: 27f00ae726115e7335762c646e87ba54aa3befda04727e3ee1e3f96fc10f49b7
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
  - path: history/records/bacterial_type_flagellum_basal_body_rod/2026-09-07T043237Z-claude-code-b01ade.yaml
    sha256: 07aefff08d117f1b72f02eabf9bf99b64660fbbab07a889d6a6b12daeb69f92e
    role: context
  - path: history/records/bacterial_type_flagellum_basal_body_rod/2026-09-21T103302Z-codex-0e3c9c.yaml
    sha256: 2697952e6556e7e44fd79a33049aea3d673f36001f771c06df256c673bd17fd1
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
- target_id: GO:0030694
  path: data/structures/appendage/bacterial_type_flagellum_basal_body_rod.yaml
  label: bacterial-type flagellum basal body, rod
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_basal_body_rod.yaml
    role: maintained scientific record
scope:
  description: One complete maintained record, all present scientific fields and both
    history surfaces; scientific inputs unchanged.
  selection: 'Next sequential unassessed record in the all-record worklist: data/structures/appendage/bacterial_type_flagellum_basal_body_rod.yaml'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0030694
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - GO:0030694
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/appendage/bacterial_type_flagellum_basal_body_rod.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Documented check completed successfully; biological support was assessed
    separately.
  scope_note: 2026-10-10T21:02:23Z to 2026-10-10T21:02:26Z; log /private/tmp/csm-review-20261010T210100Z/bacterial_type_flagellum_basal_body_rod-schema.log;
    SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - GO:0030694
  command: .venv/bin/python scripts/validate_strict.py data/structures/appendage/bacterial_type_flagellum_basal_body_rod.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Documented check completed successfully; biological support was assessed
    separately.
  scope_note: 2026-10-10T21:02:26Z to 2026-10-10T21:02:31Z; log /private/tmp/csm-review-20261010T210100Z/bacterial_type_flagellum_basal_body_rod-strict.log;
    SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:0030694
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Documented check completed successfully; biological support was assessed
    separately.
  scope_note: 2026-10-10T21:02:31Z to 2026-10-10T21:02:46Z; log /private/tmp/csm-review-20261010T210100Z/history.log;
    SHA-256 cd1ede9d4a81c377c87a16b4887bfe0d4d500f6bba69a84f56b7ab8216c1e150
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - GO:0030694
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Documented check completed successfully; biological support was assessed
    separately. This target has no trait links; this is a corpus-wide check.
  scope_note: 2026-10-10T21:02:46Z to 2026-10-10T21:03:09Z; log /private/tmp/csm-review-20261010T210100Z/traits.log;
    SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - GO:0030694
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Documented check completed successfully; biological support was assessed
    separately.
  scope_note: 2026-10-10T21:03:09Z to 2026-10-10T21:05:56Z; log /private/tmp/csm-review-20261010T210100Z/labels.log;
    SHA-256 553dd4c9f88c8a5289a33f588649f4677e541cc9da09ecd6c78c0e9f3cae8917
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - GO:0030694
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Documented check completed successfully; biological support was assessed
    separately. The full-corpus checker skips unsupported namespaces; a zero exit
    is not verification of those skipped identifiers.
  scope_note: 2026-10-10T21:05:56Z to 2026-10-10T21:07:04Z; log /private/tmp/csm-review-20261010T210100Z/curies.log;
    SHA-256 8e131ce6be4c631f49ce1e0d8482937405bcc0843606a5008085f409b7fa84e0
- check_id: qc
  name: qc
  status: passed
  required: true
  target_ids:
  - GO:0030694
  command: .venv/bin/python scripts/run_qc.py
  exit_code: 0
  expected_exit_code: 0
  summary: Documented check completed successfully; biological support was assessed
    separately.
  scope_note: 2026-10-10T21:07:04Z to 2026-10-10T21:20:06Z; log /private/tmp/csm-review-20261010T210100Z/qc.log;
    SHA-256 098224747786ffb3eccf9f4a8d798514935a3fb24b101b78242d2b0fb74f4abc
- check_id: imodulondb-datasets
  name: imodulondb-datasets
  status: passed
  required: false
  target_ids:
  - GO:0030694
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  exit_code: 0
  expected_exit_code: 0
  summary: 'Structured adapter consulted: exact Salmonella core gene matches, no iModulon
    hits. Gene identity context only.'
  scope_note: 2026-10-10T21:03:59Z to 2026-10-10T21:04:01Z; log SHA-256 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- check_id: imodulondb-flgg
  name: imodulondb-flgg
  status: passed
  required: false
  target_ids:
  - GO:0030694
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism s_enterica --dataset core --query flgG
  exit_code: 0
  expected_exit_code: 0
  summary: 'Structured adapter consulted: exact Salmonella core gene matches, no iModulon
    hits. Gene identity context only.'
  scope_note: 2026-10-10T21:04:01Z to 2026-10-10T21:04:03Z; log SHA-256 ad71c4743af5e90865cec9caee340fdffb3a8088e89f4a1f59383638f62668ac
- check_id: imodulondb-flie
  name: imodulondb-flie
  status: passed
  required: false
  target_ids:
  - GO:0030694
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism s_enterica --dataset core --query fliE
  exit_code: 0
  expected_exit_code: 0
  summary: 'Structured adapter consulted: exact Salmonella core gene matches, no iModulon
    hits. Gene identity context only.'
  scope_note: 2026-10-10T21:04:08Z to 2026-10-10T21:04:09Z; log SHA-256 f0143fed8bb0b96cb2750f5e7bc832104bd10a1eca0117a1fb52986937528301
- check_id: imodulondb-flgb
  name: imodulondb-flgb
  status: passed
  required: false
  target_ids:
  - GO:0030694
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism s_enterica --dataset core --query flgB
  exit_code: 0
  expected_exit_code: 0
  summary: 'Structured adapter consulted: exact Salmonella core gene matches, no iModulon
    hits. Gene identity context only.'
  scope_note: 2026-10-10T21:04:09Z to 2026-10-10T21:04:10Z; log SHA-256 08d15b33ebf13dcbe000b6486f6815b57a797971455e3d59b0ea120437382e7d
- check_id: imodulondb-flgc
  name: imodulondb-flgc
  status: passed
  required: false
  target_ids:
  - GO:0030694
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism s_enterica --dataset core --query flgC
  exit_code: 0
  expected_exit_code: 0
  summary: 'Structured adapter consulted: exact Salmonella core gene matches, no iModulon
    hits. Gene identity context only.'
  scope_note: 2026-10-10T21:04:10Z to 2026-10-10T21:04:11Z; log SHA-256 9b818e8987e3b55e61eafee0188b428c85fb2e3c6559a2bf2da5af9017a173e2
- check_id: imodulondb-flgf
  name: imodulondb-flgf
  status: passed
  required: false
  target_ids:
  - GO:0030694
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism s_enterica --dataset core --query flgF
  exit_code: 0
  expected_exit_code: 0
  summary: 'Structured adapter consulted: exact Salmonella core gene matches, no iModulon
    hits. Gene identity context only.'
  scope_note: 2026-10-10T21:04:11Z to 2026-10-10T21:04:12Z; log SHA-256 830991104fdd36c8d9787efd3cb4bd6b9d4250308784eb48b360a4c53d869b25
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/appendage/bacterial_type_flagellum_basal_body_rod.yaml
  locator: Entire native YAML, schema enums, and recorded repository histories
  accessed_at: '2026-10-10T21:21:53Z'
  support: context_only
  summary: Full record and histories read. All input hashes remain as captured. PROPOSED
    status retained; no curation events appended.
- evidence_id: paper-00
  kind: primary_source
  reference: DOI:10.1016/j.cell.2021.03.057
  locator: Primary abstract
  accessed_at: '2026-10-10T21:02:10Z'
  snapshot_sha256: 7cad5919d0b75e34ceeeece1f50d2ee4b418b5f4124d3ff2f3c638ba9e17a79f
  support: supports
  summary: Cryo-EM of a Salmonella rod-hook-motor complex identifies MS-ring, FliE
    and FlgB contacts involved in mechanical coupling.
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
- evidence_id: go-0009424
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0009424
  locator: Exact identifier, active status, identity, and relevant source metadata
  accessed_at: '2026-10-10T21:02:15Z'
  snapshot_sha256: 0ea0c99c4cc0f3538a77323eb000284f8e030f65cc83bc8aadf9f89b67d35dd3
  support: supports
  summary: Authority identity checked; protein examples are gene/taxon identity context,
    not independent proof of structure membership.
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
- evidence_id: interpro-ipr012834
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012834/
  locator: Exact identifier, active status, identity, and relevant source metadata
  accessed_at: '2026-10-10T21:02:24Z'
  snapshot_sha256: ba3bef26f5cc2d5eecf4ed292f15d52ffad6b9f2b32cd97718c4ec76407cf498
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
- evidence_id: uniprotkb-p0a1j3
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0A1J3.json
  locator: Exact identifier, active status, identity, and relevant source metadata
  accessed_at: '2026-10-10T21:02:27Z'
  snapshot_sha256: c94a06ad955d8e8ac5c26cd84625aab04c4bcb990499b0b9d11addbe7fc7f6ba
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
  support: refutes
  summary: Across 30,238 GTDB genomes from 131 phyla, approximately 40% carry FliPQR
    markers. This is a genomic proxy, not a microscopy census or direct rod/ring prevalence
    measurement.
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
  support: refutes
  summary: Exact FliE family IPR001624 is present. The curated Salmonella example
    P26462 independently carries this family cross-reference.
- evidence_id: flgf-family-context
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012836/
  locator: Narrow family entry and current P16323 cross-references
  accessed_at: '2026-10-10T21:03:51Z'
  snapshot_sha256: c12aeb168174a57471a3dac64298ac6ca3bee48548a27ecbd95f96ba0e45fb8b
  support: context_only
  summary: A narrower FlgF entry exists, but P16323 does not currently match it. No
    automatic FlgF grounding is justified by name alone.
- evidence_id: prior-search
  kind: search
  reference: reviews/
  locator: Recursive structured target-ID inspection
  accessed_at: '2026-10-10T21:21:55Z'
  support: context_only
  search_scope: All reviews/**/review.yaml, including hidden and ignored files, parsed
    for exact target ID GO:0030694; 28 canonical bundles inspected.
  summary: No previous canonical target review for this record. Prior bibliography
    mentions are not target assessments.
assessments:
- assessment_id: identity
  area: identity
  topic: Structure identity, synonyms, hierarchy and parthood
  outcome: supported
  target_ids:
  - GO:0030694
  evidence_ids:
  - record
  - synonym-scopes
  - go-0030694
  summary: Exact active GO cellular component denotes the named polymer/ring, not
    an individual protein. Native definitions and synonyms agree; rod segments belong
    to the rod and the rod/MS ring to the basal body.
- assessment_id: composition
  area: evidence
  topic: Every listed constituent, role, essentiality and protein example
  outcome: supported
  target_ids:
  - GO:0030694
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
  outcome: concern
  target_ids:
  - GO:0030694
  evidence_ids:
  - record
  - flie-family
  - uniprotkb-p26462
  - flgf-family-context
  summary: FlgB/FlgC and, where present, FlgG exact family identities are supported.
    FliE now has an exact matched family despite its label-only status. FlgF remains
    a distinct, bounded grounding uncertainty; an exact-name candidate alone is not
    sufficient.
- assessment_id: taxonomy
  area: scope
  topic: All distribution rows and organism exemplars
  outcome: concern
  target_ids:
  - GO:0030694
  evidence_ids:
  - record
  - paper-09
  - distribution
  - paper-04
  - paper-12
  summary: The Salmonella exemplar and bacterial/archaellum distinction are supported.
    COMMON overstates prevalence at the Bacteria denominator. Use a defensible patchy/lineage-dependent
    category and retain genomic-proxy limits instead of turning marker frequency into
    observed anatomy.
- assessment_id: functions-graph
  area: graph
  topic: Both functions, all graph nodes and every edge
  outcome: supported
  target_ids:
  - GO:0030694
  evidence_ids:
  - record
  - paper-00
  - paper-04
  - paper-06
  - paper-12
  summary: Checked all 9 edges. Axial adjacency, constituent assembly, envelope bushing
    topology and mechanical coupling are supported in the cited model system. Spatial
    composition is not interpreted as a directly observed dynamic assembly trajectory.
    No unsupported stator rotation model is asserted here.
- assessment_id: quantities
  area: quantity
  topic: Stoichiometry and physical properties
  outcome: not_applicable
  target_ids:
  - GO:0030694
  evidence_ids:
  - record
  summary: No quantitative physical-property or stoichiometry assertion is present;
    absent optional measurements are not defects.
- assessment_id: provenance
  area: provenance
  topic: Discussions, histories, status and omitted optional sections
  outcome: supported
  target_ids:
  - GO:0030694
  evidence_ids:
  - record
  - prior-search
  summary: Read every discussion and both history surfaces. Resolved boundary decisions
    distinguish neighboring structures and transient assembly factors; PROPOSED is
    appropriate. No trait, pathway, image, dataset or external complex-composition
    claim is present. Their absence is not a finding. Bibliographic abstracts and
    full-text access limits remain explicit.
findings:
- finding_id: F1
  issue_key: flagellar-rod-bacterial-prevalence-common
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Bacterial prevalence exceeds the cited evidence
  description: COMMON means present in most members with exceptional losses under
    the native enum. The note only conditions occurrence on flagella, while the cited
    GO definition or assembly review does not establish a majority of Bacteria. Independent
    genomic evidence favors heterogeneous occurrence and does not justify this majority
    assertion.
  target_ids:
  - GO:0030694
  field_paths:
  - taxonomic_distribution[0].presence
  - taxonomic_distribution[0].reference
  evidence_ids:
  - record
  - distribution
  - paper-01
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_basal_body_rod.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#evidence
  native_severity: major
  normalization_reason: Material taxonomic scope inflation under the native rubric.
- finding_id: F2
  issue_key: flagellar-rod-flie-label-only-status
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: FliE label-only status is stale against an exact family match
  description: 'The native REVIEWED_LABEL_ONLY flag means no exact family can be asserted.
    Current InterPro IPR001624 is an integrated FliE family, and the record''s reviewed
    Salmonella FliE example P26462 matches it. This is not an empty optional slot:
    the positive no-exact-family decision now has a concrete contrary authority result.
    Historical curation rationale should remain distinguishable from current state.'
  target_ids:
  - GO:0030694
  field_paths:
  - components[0].grounding_status
  - components[0].grounding_notes
  evidence_ids:
  - record
  - flie-family
  - uniprotkb-p26462
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_basal_body_rod.yaml
    role: maintained scientific record
  rule_id: src/cellstructuremech/schema/cellstructuremech.yaml#ComponentGroundingStatusEnum
  native_severity: minor
  normalization_reason: Bounded grounding/provenance correction; protein and structure
    identity are otherwise correct.
actions:
- action_id: A1
  description: Curate the maintained occurrence row to VARIABLE or a narrower evidence-backed
    taxonomic statement; cite inspected support and retain the distinction between
    marker-bearing genomes and observed structures. Preserve archaellum distinction
    and native PROPOSED status.
  finding_ids:
  - F1
  target_ids:
  - GO:0030694
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_basal_body_rod.yaml
    role: maintained scientific record
  acceptance_checks:
  - The row no longer asserts majority bacterial prevalence without appropriate evidence.
  - Schema/strict validation, identifier/label and history checks pass; regenerate
    maintained-derived products through repository commands if scientific content
    changes.
  generator: Guarded record writer, curation event, append-only history, text embedding/map
    refresh as required, and just render.
- action_id: A2
  description: Verify IPR001624 against the declared FliE scope and current reviewed
    example, add the supported exact grounding and retire the incompatible current
    label-only status. Retain the historical reason and append a dated current-state
    explanation. Do not infer an analogous FlgF fix from this evidence.
  finding_ids:
  - F2
  target_ids:
  - GO:0030694
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_basal_body_rod.yaml
    role: maintained scientific record
  acceptance_checks:
  - IPR001624 is verified as the exact FliE family, not a domain or broader homologous
    superfamily.
  - P26462 family match and current gene/taxon identity are recorded; native label
    correspondence, strict schema and history gates pass.
  generator: Guarded record writer, curation event, append-only repository history,
    and just render.
limitations:
- A complete assessment of this record is not completion of the 909-record goal, a
  new experimental result, or human scientific approval. Proposed fixes are not performed
  by this review.
- Some historical sources were inspected as abstracts only. Europe PMC full-text endpoints
  returned errors for several records; BioC sometimes returned an error document rather
  than article text. Publisher access attempts included subscription previews and
  HTTP 403 responses. No unread main-text details or figures are certified.
- The distribution survey uses FliPQR markers in a reference-genome sample. Its frequency
  is not direct observation of this rod/ring and is not a census of all bacterial
  cells, species or environments.
- Source-supported assembly and topology primarily concern Salmonella. Broad family
  labels are not proof of identical stoichiometry or accessory architecture across
  every bacterial lineage.
- The full-corpus identifier checker skips unsupported namespaces. Fresh scoped GO,
  InterPro, UniProt and taxon checks are separately recorded; the successful global
  exit is not blanket identifier certification.
- The optional HTML inspection initially found BeautifulSoup unavailable; the standard-library
  HTMLParser was then used to inspect publisher previews. This was a tooling fallback,
  not a failed native scientific gate.
```
