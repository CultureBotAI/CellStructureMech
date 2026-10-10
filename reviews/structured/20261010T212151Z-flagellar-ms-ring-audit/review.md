# bacterial-type flagellum basal body, MS ring: evidence and scope review

- Review: 20261010T212151Z-flagellar-ms-ring-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-10T21:01:32Z
- Finished UTC: 2026-10-10T21:21:51Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

All present native sections assessed at the captured revision. Unsupported bacterial prevalence requires curation.

## Scope And Provenance

One complete maintained record, all present scientific fields and both history surfaces; scientific inputs unchanged.

Selection: Next sequential unassessed record in the all-record worklist: data/structures/appendage/bacterial_type_flagellum_basal_body_ms_ring.yaml
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base eb734ac4a4efcfd2cfb3abaf7562a6695f23c74b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0009431 | data/structures/appendage/bacterial_type_flagellum_basal_body_ms_ring.yaml | maintained | bacterial-type flagellum basal body, MS ring |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0009431 | Documented check completed successfully; biological support was assessed separately. |
| strict | passed | True | GO:0009431 | Documented check completed successfully; biological support was assessed separately. |
| history | passed | True | GO:0009431 | Documented check completed successfully; biological support was assessed separately. |
| traits | passed | True | GO:0009431 | Documented check completed successfully; biological support was assessed separately. This target has no trait links; this is a corpus-wide check. |
| labels | passed | True | GO:0009431 | Documented check completed successfully; biological support was assessed separately. |
| curies | passed | True | GO:0009431 | Documented check completed successfully; biological support was assessed separately. The full-corpus checker skips unsupported namespaces; a zero exit is not verification of those skipped identifiers. |
| qc | passed | True | GO:0009431 | Documented check completed successfully; biological support was assessed separately. |
| imodulondb-datasets | passed | False | GO:0009431 | Structured adapter consulted: exact Salmonella core gene matches, no iModulon hits. Gene identity context only. |
| imodulondb-flif | passed | False | GO:0009431 | Structured adapter consulted: exact Salmonella core gene matches, no iModulon hits. Gene identity context only. |

## Scientific And Domain Assessments

### Structure identity, synonyms, hierarchy and parthood

identity: supported. Targets: GO:0009431.

Exact active GO cellular component denotes the named polymer/ring, not an individual protein. Native definitions and synonyms agree; rod segments belong to the rod and the rod/MS ring to the basal body.

### Every listed constituent, role, essentiality and protein example

evidence: supported. Targets: GO:0009431.

FliF alone is the core MS ring; FlgG is the distal rod; FliE/FlgB/FlgC/FlgF constitute the proximal segment, with FlgG added for the whole rod. Only the relevant components are asserted in this target. Structural membership and cooperative stable assembly support the constituent model; this is not new proof of every deletion phenotype in every lineage. Current protein accessions, reviewed status, genes and LT2 taxon agree.

### Constituent family scope

grounding: supported. Targets: GO:0009431.

Current exact constituent-family grounding is consistent with the native protein example and does not substitute a broader rod/hook family.

### All distribution rows and organism exemplars

scope: concern. Targets: GO:0009431.

The Salmonella exemplar and bacterial/archaellum distinction are supported. COMMON overstates prevalence at the Bacteria denominator. Use a defensible patchy/lineage-dependent category and retain genomic-proxy limits instead of turning marker frequency into observed anatomy.

### Both functions, all graph nodes and every edge

graph: supported. Targets: GO:0009431.

Checked all 6 edges. Axial adjacency, constituent assembly, envelope bushing topology and mechanical coupling are supported in the cited model system. Spatial composition is not interpreted as a directly observed dynamic assembly trajectory. No unsupported stator rotation model is asserted here.

### Stoichiometry and physical properties

quantity: supported. Targets: GO:0009431.

The 34-subunit value is explicitly native Salmonella and supported by Kawamoto 2021; it is not generalized to every species or isolated/recombinant construct.

### Discussions, histories, status and omitted optional sections

provenance: supported. Targets: GO:0009431.

Read every discussion and both history surfaces. Resolved boundary decisions distinguish neighboring structures and transient assembly factors; PROPOSED is appropriate. No trait, pathway, image, dataset or external complex-composition claim is present. Their absence is not a finding. Bibliographic abstracts and full-text access limits remain explicit.

## Findings

### F1: Bacterial prevalence exceeds the cited evidence

major / open / confirmed; issue key: flagellar-ms-ring-bacterial-prevalence-common.

COMMON means present in most members with exceptional losses under the native enum. The note only conditions occurrence on flagella, while the cited GO definition or assembly review does not establish a majority of Bacteria. Independent genomic evidence favors heterogeneous occurrence and does not justify this majority assertion.

## Recommended Actions And Acceptance Checks

### A1

Curate the maintained occurrence row to VARIABLE or a narrower evidence-backed taxonomic statement; cite inspected support and retain the distinction between marker-bearing genomes and observed structures. Preserve archaellum distinction and native PROPOSED status.

- The row no longer asserts majority bacterial prevalence without appropriate evidence.
- Schema/strict validation, identifier/label and history checks pass; regenerate maintained-derived products through repository commands if scientific content changes.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/bacterial_type_flagellum_basal_body_ms_ring.yaml; Entire native YAML, schema enums, and recorded repository histories | context_only | Full record and histories read. All input hashes remain as captured. PROPOSED status retained; no curation events appended. |
| paper-00 | DOI:10.1016/j.cell.2021.03.057; Primary abstract | supports | Cryo-EM of a Salmonella rod-hook-motor complex identifies MS-ring, FliE and FlgB contacts involved in mechanical coupling. |
| paper-01 | DOI:10.1038/nrmicro1887; Review abstract and publisher preview/key points, not subscription main text | supports | The inspected text addresses coordinated flagellar gene regulation and assembly in Gram-negative bacteria, not a denominator-bearing estimate of bacterial prevalence. |
| paper-02 | DOI:10.1038/s41467-021-24507-9; Full text: Results native basal-body symmetry, Fig. 1, export-gate core, Discussion and strain methods | supports | The studied native Salmonella MS ring contains 34 FliF subunits. This supports the explicitly organism-bound count, scaffold and export-gate accommodation claims. |
| paper-07 | DOI:10.1128/jb.171.7.3890-3900.1989; Primary abstract | supports | The sequenced Salmonella flgH, flgI and fliF genes encode L-, P- and M-ring proteins, respectively. |
| paper-08 | DOI:10.1146/annurev.micro.57.030502.090832; Review abstract and publisher access page only | supports | General axial export and distal assembly context; no unseen measurements or detailed mechanisms are certified. |
| paper-09 | DOI:10.3389/fmicb.2015.00023; Review full text: historical structural/genomic comparisons, paragraphs 15-18 | supports | Archaella are evolutionarily and structurally distinct from the bacterial rod-and-ring apparatus; the source describes EM and genomic evidence for this distinction. |
| go-0009425 | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0009425; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| go-0009431 | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0009431; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| go-0030694 | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0030694; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| go-0120102 | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0120102; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| interpro-ipr000067 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000067/; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| uniprotkb-p15928 | https://rest.uniprot.org/uniprotkb/P15928.json; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| ncbitaxon-2 | https://rest.uniprot.org/taxonomy/2.json; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| ncbitaxon-2157 | https://rest.uniprot.org/taxonomy/2157.json; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| ncbitaxon-90371 | https://rest.uniprot.org/taxonomy/90371.json; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| ncbitaxon-99287 | https://rest.uniprot.org/taxonomy/99287.json; Exact identifier, active status, identity, and relevant source metadata | supports | Authority identity checked; protein examples are gene/taxon identity context, not independent proof of structure membership. |
| synonym-scopes | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009426,GO:0009427,GO:0009428,GO:0009429,GO:0009431,GO:0030694; Exact six GO records, definitions and typed synonyms | supports | Source synonym types checked against QuickGO, alongside exact OLS identities. |
| distribution | DOI:10.1073/pnas.2512476122; Results computational distribution paragraph; Methods reference-genome/HMM design | refutes | Across 30,238 GTDB genomes from 131 phyla, approximately 40% carry FliPQR markers. This is a genomic proxy, not a microscopy census or direct rod/ring prevalence measurement. |
| assembly | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2F0022-2836%2892%2990958-m%22&amp;format=json&amp;resultType=core; Primary abstract | supports | Salmonella precursor analysis distinguishes autonomous MS-ring formation from cooperative assembly of FliE and the four rod proteins into a stable structure. The unseen individual mutant results are not certified. |
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
review_id: 20261010T212151Z-flagellar-ms-ring-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'bacterial-type flagellum basal body, MS ring: evidence and scope review'
started_at: '2026-10-10T21:01:32Z'
finished_at: '2026-10-10T21:21:51Z'
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
  bacterial prevalence requires curation.
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
  - path: data/structures/appendage/bacterial_type_flagellum_basal_body_ms_ring.yaml
    sha256: d2e79a994111fd864551a087bb32437cf66dad092f047a2692e577afcec56815
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
  - path: history/records/bacterial_type_flagellum_basal_body_ms_ring/2026-09-08T025144Z-claude-aacedd.yaml
    sha256: e87d73585f19dd81d4ec774348544b3e7d09bdcd4b2f80c99cc51300bb2527d5
    role: context
  - path: history/records/bacterial_type_flagellum_basal_body_ms_ring/2026-09-21T140304Z-codex-f0855d.yaml
    sha256: a3d836fbca846019906a7cd4a358ba3b7bd1be53f84972e392d43074e04bd283
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
- target_id: GO:0009431
  path: data/structures/appendage/bacterial_type_flagellum_basal_body_ms_ring.yaml
  label: bacterial-type flagellum basal body, MS ring
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_basal_body_ms_ring.yaml
    role: maintained scientific record
scope:
  description: One complete maintained record, all present scientific fields and both
    history surfaces; scientific inputs unchanged.
  selection: 'Next sequential unassessed record in the all-record worklist: data/structures/appendage/bacterial_type_flagellum_basal_body_ms_ring.yaml'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0009431
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - GO:0009431
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/appendage/bacterial_type_flagellum_basal_body_ms_ring.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Documented check completed successfully; biological support was assessed
    separately.
  scope_note: 2026-10-10T21:02:08Z to 2026-10-10T21:02:11Z; log /private/tmp/csm-review-20261010T210100Z/bacterial_type_flagellum_basal_body_ms_ring-schema.log;
    SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - GO:0009431
  command: .venv/bin/python scripts/validate_strict.py data/structures/appendage/bacterial_type_flagellum_basal_body_ms_ring.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Documented check completed successfully; biological support was assessed
    separately.
  scope_note: 2026-10-10T21:02:11Z to 2026-10-10T21:02:15Z; log /private/tmp/csm-review-20261010T210100Z/bacterial_type_flagellum_basal_body_ms_ring-strict.log;
    SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:0009431
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
  - GO:0009431
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
  - GO:0009431
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
  - GO:0009431
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
  - GO:0009431
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
  - GO:0009431
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  exit_code: 0
  expected_exit_code: 0
  summary: 'Structured adapter consulted: exact Salmonella core gene matches, no iModulon
    hits. Gene identity context only.'
  scope_note: 2026-10-10T21:03:59Z to 2026-10-10T21:04:01Z; log SHA-256 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- check_id: imodulondb-flif
  name: imodulondb-flif
  status: passed
  required: false
  target_ids:
  - GO:0009431
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism s_enterica --dataset core --query fliF
  exit_code: 0
  expected_exit_code: 0
  summary: 'Structured adapter consulted: exact Salmonella core gene matches, no iModulon
    hits. Gene identity context only.'
  scope_note: 2026-10-10T21:04:07Z to 2026-10-10T21:04:08Z; log SHA-256 0980650a86ff58ca243c0930e8d6e7a5415b7058c2416abe0683d785534b6f44
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/appendage/bacterial_type_flagellum_basal_body_ms_ring.yaml
  locator: Entire native YAML, schema enums, and recorded repository histories
  accessed_at: '2026-10-10T21:21:50Z'
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
- evidence_id: paper-02
  kind: primary_source
  reference: DOI:10.1038/s41467-021-24507-9
  locator: 'Full text: Results native basal-body symmetry, Fig. 1, export-gate core,
    Discussion and strain methods'
  accessed_at: '2026-10-10T21:02:15Z'
  snapshot_sha256: 602f3eb50f5f81de1ffa522838f21c064653d23f5bf5e86553ee6c0213017a43
  support: supports
  summary: The studied native Salmonella MS ring contains 34 FliF subunits. This supports
    the explicitly organism-bound count, scaffold and export-gate accommodation claims.
- evidence_id: paper-07
  kind: primary_source
  reference: DOI:10.1128/jb.171.7.3890-3900.1989
  locator: Primary abstract
  accessed_at: '2026-10-10T21:02:23Z'
  snapshot_sha256: b8d262114b3343f311d435327dce3ed4d55150bce26ae5da088ba883efd6971a
  support: supports
  summary: The sequenced Salmonella flgH, flgI and fliF genes encode L-, P- and M-ring
    proteins, respectively.
- evidence_id: paper-08
  kind: primary_source
  reference: DOI:10.1146/annurev.micro.57.030502.090832
  locator: Review abstract and publisher access page only
  accessed_at: '2026-10-10T21:02:25Z'
  snapshot_sha256: 68caf42cabe3749c93733a366e2bda96e3fb414eb0f71a846df6d91eb67b7f58
  support: supports
  summary: General axial export and distal assembly context; no unseen measurements
    or detailed mechanisms are certified.
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
- evidence_id: go-0009425
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0009425
  locator: Exact identifier, active status, identity, and relevant source metadata
  accessed_at: '2026-10-10T21:02:15Z'
  snapshot_sha256: ba237444d9aaed5133ec4da342e0d2d5392ac51591dcbc7fe9f7e8db9127df26
  support: supports
  summary: Authority identity checked; protein examples are gene/taxon identity context,
    not independent proof of structure membership.
- evidence_id: go-0009431
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0009431
  locator: Exact identifier, active status, identity, and relevant source metadata
  accessed_at: '2026-10-10T21:02:18Z'
  snapshot_sha256: 1c0feba8fb18a5f38d973f630108f3ebff0eaccbcf85356e4b7bdc78b8b11042
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
- evidence_id: go-0120102
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0120102
  locator: Exact identifier, active status, identity, and relevant source metadata
  accessed_at: '2026-10-10T21:02:20Z'
  snapshot_sha256: 596ac50eaf899440c439197ad0331598639a68e4acef60eb4fd5909e02bdc4b8
  support: supports
  summary: Authority identity checked; protein examples are gene/taxon identity context,
    not independent proof of structure membership.
- evidence_id: interpro-ipr000067
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000067/
  locator: Exact identifier, active status, identity, and relevant source metadata
  accessed_at: '2026-10-10T21:02:20Z'
  snapshot_sha256: 0ada2578399bc7e99d40388171ebd3e4351de6fa2941f7ff54d2d02b2cbedc43
  support: supports
  summary: Authority identity checked; protein examples are gene/taxon identity context,
    not independent proof of structure membership.
- evidence_id: uniprotkb-p15928
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P15928.json
  locator: Exact identifier, active status, identity, and relevant source metadata
  accessed_at: '2026-10-10T21:02:29Z'
  snapshot_sha256: 3568c3da24f10b41e809c072456c5572d4da6064483ca700635a09fcc3006562
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
- evidence_id: prior-search
  kind: search
  reference: reviews/
  locator: Recursive structured target-ID inspection
  accessed_at: '2026-10-10T21:21:51Z'
  support: context_only
  search_scope: All reviews/**/review.yaml, including hidden and ignored files, parsed
    for exact target ID GO:0009431; 28 canonical bundles inspected.
  summary: No previous canonical target review for this record. Prior bibliography
    mentions are not target assessments.
assessments:
- assessment_id: identity
  area: identity
  topic: Structure identity, synonyms, hierarchy and parthood
  outcome: supported
  target_ids:
  - GO:0009431
  evidence_ids:
  - record
  - synonym-scopes
  - go-0009431
  summary: Exact active GO cellular component denotes the named polymer/ring, not
    an individual protein. Native definitions and synonyms agree; rod segments belong
    to the rod and the rod/MS ring to the basal body.
- assessment_id: composition
  area: evidence
  topic: Every listed constituent, role, essentiality and protein example
  outcome: supported
  target_ids:
  - GO:0009431
  evidence_ids:
  - record
  - assembly
  - paper-02
  - paper-07
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
    - paper-02
    - paper-07
- assessment_id: grounding
  area: grounding
  topic: Constituent family scope
  outcome: supported
  target_ids:
  - GO:0009431
  evidence_ids:
  - record
  - interpro-ipr000067
  summary: Current exact constituent-family grounding is consistent with the native
    protein example and does not substitute a broader rod/hook family.
- assessment_id: taxonomy
  area: scope
  topic: All distribution rows and organism exemplars
  outcome: concern
  target_ids:
  - GO:0009431
  evidence_ids:
  - record
  - paper-09
  - distribution
  - paper-02
  - paper-07
  summary: The Salmonella exemplar and bacterial/archaellum distinction are supported.
    COMMON overstates prevalence at the Bacteria denominator. Use a defensible patchy/lineage-dependent
    category and retain genomic-proxy limits instead of turning marker frequency into
    observed anatomy.
- assessment_id: functions-graph
  area: graph
  topic: Both functions, all graph nodes and every edge
  outcome: supported
  target_ids:
  - GO:0009431
  evidence_ids:
  - record
  - paper-02
  - paper-00
  summary: Checked all 6 edges. Axial adjacency, constituent assembly, envelope bushing
    topology and mechanical coupling are supported in the cited model system. Spatial
    composition is not interpreted as a directly observed dynamic assembly trajectory.
    No unsupported stator rotation model is asserted here.
- assessment_id: quantities
  area: quantity
  topic: Stoichiometry and physical properties
  outcome: supported
  target_ids:
  - GO:0009431
  evidence_ids:
  - record
  - paper-02
  summary: The 34-subunit value is explicitly native Salmonella and supported by Kawamoto
    2021; it is not generalized to every species or isolated/recombinant construct.
- assessment_id: provenance
  area: provenance
  topic: Discussions, histories, status and omitted optional sections
  outcome: supported
  target_ids:
  - GO:0009431
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
  issue_key: flagellar-ms-ring-bacterial-prevalence-common
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
  - GO:0009431
  field_paths:
  - taxonomic_distribution[0].presence
  - taxonomic_distribution[0].reference
  evidence_ids:
  - record
  - distribution
  - paper-01
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_basal_body_ms_ring.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#evidence
  native_severity: major
  normalization_reason: Material taxonomic scope inflation under the native rubric.
actions:
- action_id: A1
  description: Curate the maintained occurrence row to VARIABLE or a narrower evidence-backed
    taxonomic statement; cite inspected support and retain the distinction between
    marker-bearing genomes and observed structures. Preserve archaellum distinction
    and native PROPOSED status.
  finding_ids:
  - F1
  target_ids:
  - GO:0009431
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_basal_body_ms_ring.yaml
    role: maintained scientific record
  acceptance_checks:
  - The row no longer asserts majority bacterial prevalence without appropriate evidence.
  - Schema/strict validation, identifier/label and history checks pass; regenerate
    maintained-derived products through repository commands if scientific content
    changes.
  generator: Guarded record writer, curation event, append-only history, text embedding/map
    refresh as required, and just render.
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
