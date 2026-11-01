# Radial spoke stalk identity, protein cohort and topology review

- Review: 20261021T080800Z-radial-spoke-stalk-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T07:54:07Z
- Finished UTC: 2026-10-21T08:08:00Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact stalk identity, topology and protein cohort are supported. One minor overstatement remains in the discussion of individual density assignment.

## Scope And Provenance

Entire single target, native ontology and sequence identities, relevant primary claim-bearing text, all component/graph/evidence assertions and open discussions.

Selection: Selected unreviewed path 9 in batch ten, in repository path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0001536 | data/structures/cytoskeleton/radial_spoke_stalk.yaml | maintained | radial spoke stalk |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0001536 | Focused validator passed. |
| Focused native strict | passed | True | GO:0001536 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0001536 | 13 identifiers OK; 1 transport/skipped residuals independently resolved. |
| Claim-level scientific review | passed | True | GO:0001536 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0001536 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0001536 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0001536 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0001536 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0001536 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Exact regional identity and parthood

identity: supported. Targets: GO:0001536.

The identifier, definition, protein-complex parent and whole-radial-spoke parthood agree with native GO. Head, neck, stalk, base, central-pair context and complete spoke are not interchangeable.

### Regional cohort and sequence identities

grounding: supported. Targets: GO:0001536.

The declared RSP3, RSP5, RSP7, RSP8, RSP11 and RSP12 belong to the source's established stalk cohort. Concrete examples agree with native accession identities; membership is assessed separately through the regional literature. The list is not asserted to be exhaustive, to define universal stoichiometry, or to prove each paralog essential.

### Heterogeneous cohort and narrower families

grounding: supported. Targets: GO:0001536.

This aggregate encompasses multiple distinct RSP families. A candidate for one subunit cannot ground the entire component. Splitting into separately sourced family components remains optional enrichment; no verified whole-cohort accession is established by the bounded searches.

### Chlamydomonas reference and experimental scope

scope: supported. Targets: GO:0001536.

The common species example is supported by the axonemal studies. The target does not transfer its named protein cohort to all ciliated taxa or identify reference sequences with the distinct engineered experimental strains.

### Every topology edge

graph: supported. Targets: GO:0001536.

Four edges correctly record protein contribution, spoke parthood and connections to base and neck. The ungrounded base node is an explicit topological region; the graph does not replace it with a direct stalk-to-A-tubule edge.

### Coarse architectural contribution

evidence: supported. Targets: GO:0001536.

The function describes the region's anatomical contribution. Motility transduction is apparatus-level context; no calibrated mechanical output, ordered recruitment pathway or per-protein catalytic mechanism is claimed.

### Primary model and actual access

evidence: supported. Targets: GO:0001536.

Full claim-bearing Poghosyan and Nicastro browser-rendered primary text and Yang native HTML were inspected. Source-specific snapshots retain transport/access limits. Structure and biochemical constraints are distinguished from hypothesized subunit positions and biochemical regulation.

### Inventory, dimensions and data-source scope

completeness: supported. Targets: GO:0001536.

Exact copy numbers, exhaustive associated proteins, detailed cross-species boundaries and complete assembly mechanism remain unresolved. No figures, physical dimensions, trait links or pathway relations occur in this target; their omission is not an unsupported claim.

### Individual stalk-density assignment

evidence: concern. Targets: GO:0001536.

The current open discussion overstates the primary paper's assignment scope. The Introduction lists the established stalk cohort, but individual segmented-density assignments are head/neck-specific; the stalk is represented as a coarse region.

## Findings

### F1: The open discussion overstates individual stalk-density assignment

minor / open / confirmed; issue key: radial-spoke-stalk-individual-density-overstatement.

The discussion credits Poghosyan2020 with assigning individual RSP densities to the stalk. Its Introduction summarizes the established stalk cohort, while its individual density assignments and segmentation methods concern head/neck proteins. Replace that claim with regional architectural refinement and established stalk composition; retain the supported stalk genes and distinguish the source's proposed model from direct subunit mapping.

## Recommended Actions And Acceptance Checks

### A1

Under separately authorized curation, correct the individual stalk-density claim and clarify the broader assignment notes to distinguish established membership from the2020 head/neck density model.

- Retain the exact stalk identity, base-to-neck topology and supported gene cohort.
- Describe the study as refining regional architecture and summarizing established stalk proteins; do not claim individual stalk-density mapping.
- Preserve model, stoichiometry and regional-overlap limits; use guarded curation/history and required native checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| radial-prep-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0001535,GO:0001536,GO:0120343,GO:0032991,GO:0001534,GO:0097540; All six term identities/definitions; GO0032991 and GO0001534 children with relation types | supports | Native active exact head, neck and stalk definitions; the protein-containing-complex parent includes all three as is-a children, and the radial-spoke term includes them as part-of children. The central-pair identifier is verified as a distinct context structure. |
| radial-prep-taxon | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055; taxId, scientificName, rank and lineage | supports | Taxon3055 is Chlamydomonas reinhardtii at species rank. The reference accession taxon does not identify every experimental stock. |
| radial-prep-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=100&amp;query=DOI%3A%2210.1242/jcs.245233%22%20OR%20DOI%3A%2210.1126/science.1128618%22%20OR%20EXT_ID%3A16507594%20OR%20EXT_ID%3A1508197; Exact DOI/PMID results, authors/title/year and abstract | supports | Exact native records verify Poghosyan2020 DOI10.1242/jcs.245233/PMID32694165, Nicastro2006 DOI10.1126/science.1128618/PMID16917055, Yang2006 DOI10.1242/jcs.02811/PMID16507594, and Curry1992 DOI10.1128/mcb.12.9.3967-3977.1992/PMID1508197. Metadata and abstracts are distinguished from actual body access. |
| radial-prep-poghosyan-intro-browser | https://www.researchgate.net/publication/343123729_The_structure_and_symmetry_of_the_radial_spoke_protein_complex_in_Chlamydomonas_flagella; Publisher-supplied full-text preview; Introduction lines138-259, especially162-169; exact browser response JSON, no tool-supplied HTTP status or native PDF assertion | supports | The Introduction explicitly lists the established head, neck and stalk RSP cohorts. The study uses Chlamydomonas and combines purified-spoke structure with complementary biochemical information. |
| radial-prep-poghosyan-browser | https://www.researchgate.net/publication/343123729_The_structure_and_symmetry_of_the_radial_spoke_protein_complex_in_Chlamydomonas_flagella; Primary Results/Discussion pp2-6, lines341-923, Fig2/3/5 legends and explicit model limitations; browser response JSON | supports | The study resolves regional architecture and proposes head/neck subunit positions using cross-linking and biochemical constraints; it does not provide an atomic assignment for every spoke protein. |
| radial-prep-poghosyan-methods-browser | https://www.researchgate.net/publication/343123729_The_structure_and_symmetry_of_the_radial_spoke_protein_complex_in_Chlamydomonas_flagella; Primary Methods pp7-8, lines994-1415; Discussion lines931-992; browser response JSON | supports | WT137c tomography is distinct from pf28pf30 conventional purification and a transgenic His-RSP3 optimized preparation. Segmentation, cross-linking and recombinant-protein assays constrain the model. |
| radial-prep-nicastro-browser | https://www.researchgate.net/publication/6871150_The_Molecular_Architecture_of_Axonemes_Revealed_by_Cryoelectron_Tomography; Author-uploaded primary body and Fig1F-G/Fig5C-D context; original retrieval retained; exact browser response JSON | supports | Chlamydomonas axonemal tomography provides whole-spoke architectural context. It is not a region-specific protein inventory or atomic subunit assignment. |
| radial-prep-nicastro-methods-browser | https://www.researchgate.net/publication/6871150_The_Molecular_Architecture_of_Axonemes_Revealed_by_Cryoelectron_Tomography; Primary supporting-material methods lines1562-1652; separate browser response hash and original retrieval timestamp | supports | Supplemental methods distinguish Chlamydomonas137c and pf9-3 preparations from sea-urchin sperm; no strain identity is inferred from species-level reference proteins. |
| radial-prep-yang-html | https://pmc.ncbi.nlm.nih.gov/articles/PMC1973137/?report=xml; Actual PMC1973137 HTML sectionsS3-S5,S8-S10,S12-S19, Table1 and Fig1/3/6 legends; distinct from failed JATS route | supports | Primary purification, peptide identification and immunoblot controls establish RSP identities; head/stalk assignments use mutant and biochemical context. Motifs and detailed organization remain models where stated. |
| radial-prep-protein-P12759 | https://rest.uniprot.org/uniprotkb/P12759.json; primaryAccession, entryType, proteinDescription, genes, organism, relevant citation/localization attribution | supports | Native P12759 is REVIEWED, gene RSP3, taxon3055; accession name, status and gene/taxon pairing match. Accession identity alone is not region-specific membership evidence. |
| radial-prep-protein-Q27YU7 | https://rest.uniprot.org/uniprotkb/Q27YU7.json; primaryAccession, entryType, proteinDescription, genes, organism, relevant citation/localization attribution | supports | Native Q27YU7 is REVIEWED, gene RSP5, taxon3055; accession name, status and gene/taxon pairing match. Accession identity alone is not region-specific membership evidence. |
| radial-prep-protein-Q27YT9 | https://rest.uniprot.org/uniprotkb/Q27YT9.json; primaryAccession, entryType, proteinDescription, genes, organism, relevant citation/localization attribution | supports | Native Q27YT9 is UNREVIEWED, gene RSP7, taxon3055; accession name, status and gene/taxon pairing match. Accession identity alone is not region-specific membership evidence. |
| radial-prep-protein-Q27YU6 | https://rest.uniprot.org/uniprotkb/Q27YU6.json; primaryAccession, entryType, proteinDescription, genes, organism, relevant citation/localization attribution | supports | Native Q27YU6 is UNREVIEWED, gene RSP8, taxon3055; accession name, status and gene/taxon pairing match. Accession identity alone is not region-specific membership evidence. |
| radial-prep-protein-Q27YU2 | https://rest.uniprot.org/uniprotkb/Q27YU2.json; primaryAccession, entryType, proteinDescription, genes, organism, relevant citation/localization attribution | supports | Native Q27YU2 is UNREVIEWED, gene RSP12, taxon3055; accession name, status and gene/taxon pairing match. Accession identity alone is not region-specific membership evidence. |
| radial-prep-reviewed-symbols | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28taxonomy_id%3A3055%29%20AND%20%28reviewed%3Atrue%29%20AND%20%28gene_exact%3ARSP1%20OR%20gene_exact%3ARSP2%20OR%20gene_exact%3ARSP3%20OR%20gene_exact%3ARSP4%20OR%20gene_exact%3ARSP5%20OR%20gene_exact%3ARSP6%29; Exact six-symbol query and all returned entries; one result per exact gene token | context_only | The bounded native taxon3055 reviewed query returns one matching entry for each requested exact symbol RSP1,RSP2,RSP3,RSP4,RSP5,RSP6, matching the stated reviewed examples. Unreviewed examples are not relabeled. |
| radial-prep-family-search-head | https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=radial%20spoke%20head&amp;page_size=200; InterPro entry search=radial spoke head, page_size200, count1 and next=null | context_only | The exact phrase search returns one RSP9 homolog family, not a family encompassing the full multi-protein cohort. This bounded search is not a global absence proof. |
| radial-prep-rsp9-family | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR055316/; Native family type, name, hierarchy and description | context_only | IPR055316 denotes the RSP9 homolog family; its member scope does not cover all head/neck/stalk proteins. It is not an exact grounding for the target aggregate. |
| radial-prep-family-search-stalk | https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=radial%20spoke%20stalk&amp;page_size=200; Exact phrase query; HTTP204 empty body | context_only | This endpoint returned no content for the narrow phrase search. It does not establish universal absence of all relevant families. |
| record | data/structures/cytoskeleton/radial_spoke_stalk.yaml; Entire target, history, component and examples, every graph edge and both discussions | context_only | Complete maintained target read; PROPOSED status retained, and the graph explicitly records nonmechanistic topology. |
| policy | docs/CURATION.md; Components and source evidence rules | context_only | Source-neutral component classes, exact taxon-paired identities and independent membership support are distinct requirements. |
| schema-result | just validate data/structures/cytoskeleton/radial_spoke_stalk.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/radial_spoke_stalk.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/radial_spoke_stalk.yaml --out /private/tmp/cellstructure-batch10-20261021-giynduuy/radial_spoke_stalk-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/radial_spoke_stalk.yaml --out /private/tmp/cellstructure-batch10-20261021-giynduuy/radial_spoke_stalk-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch10-20261021-giynduuy/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch10-20261021-giynduuy/radial_spoke_stalk-strict.tsv |
| target-curies | just check-curies-strict; data/structures/cytoskeleton/radial_spoke_stalk.yaml; exact collect() scope; hash identifies the entire original strict-resolver TSV, not the derived target slice | supports | 13 of 14 collected target identifiers returned OK at the unchanged base. Residuals: PMID:16507594: UNREACHABLE; resolved by evidence radial-prep-epmc. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Browser-rendered primary text and legends were inspected; native publisher/institution PDF routes were blocked. Browser snapshots carry no native HTTP status, and no independent microscopy-pixel, raw-map, movie or complete supplemental-data reanalysis is claimed.
- The2020 head/neck arrangement is an experimentally constrained model, including possible overlap of regional protein positions. Exact copy numbers and exclusive spatial membership are not adopted.
- The family searches are bounded to the stated queries. An empty HTTP204 response is an access/result limit, not proof that no exact family exists anywhere.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Root personally read each full target and the stated source sections. Only this target receives scientific coverage.
- Only the review bundle is saved. Maintained scientific content, native status, history and generated pages remain unchanged.
- A separate reviewer independently read the target and primary Introduction, Results/Discussion and segmentation Methods and agreed with the bounded source-overstatement finding.
- Only this target receives scientific review coverage. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T080800Z-radial-spoke-stalk-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Radial spoke stalk identity, protein cohort and topology review
started_at: '2026-10-21T07:54:07Z'
finished_at: '2026-10-21T08:08:00Z'
reviewer:
  identity: Codex
  kind: agent
  independence: unknown
  independence_basis: Current source review does not establish independent historical
    authorship.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Exact stalk identity, topology and protein cohort are supported. One minor
  overstatement remains in the discussion of individual density assignment.
source:
  git_revision: 99692a3d5f16a7dcd6db7e3811344c299a977b81
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
    role: context
  - path: .claude/skills/literature-evidence/SKILL.md
    sha256: f7c3c594b5fb2cd7d4d700844fce3b97c91cc382d4fdca8b2e2a96cf16abd41b
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
    role: context
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/cytoskeleton/radial_spoke_stalk.yaml
    sha256: 8747c08b214590fd435efacd64ee8fb09e56cf9e693fa193df256716c2703936
    role: target
  - path: docs/CURATION.md
    sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
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
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: GO:0001536
  path: data/structures/cytoskeleton/radial_spoke_stalk.yaml
  label: radial spoke stalk
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/radial_spoke_stalk.yaml
    role: maintained scientific record
scope:
  description: Entire single target, native ontology and sequence identities, relevant
    primary claim-bearing text, all component/graph/evidence assertions and open discussions.
  selection: Selected unreviewed path 9 in batch ten, in repository path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0001536
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0001536
  command: just validate data/structures/cytoskeleton/radial_spoke_stalk.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0001536
  command: just validate-strict data/structures/cytoskeleton/radial_spoke_stalk.yaml
    --out /private/tmp/cellstructure-batch10-20261021-giynduuy/radial_spoke_stalk-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0001536
  summary: 13 identifiers OK; 1 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - radial-prep-epmc
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0001536
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - radial-prep-go
  - radial-prep-taxon
  - radial-prep-epmc
  - radial-prep-poghosyan-intro-browser
  - radial-prep-poghosyan-browser
  - radial-prep-poghosyan-methods-browser
  - radial-prep-nicastro-browser
  - radial-prep-nicastro-methods-browser
  - radial-prep-yang-html
  - radial-prep-protein-P12759
  - radial-prep-protein-Q27YU7
  - radial-prep-protein-Q27YT9
  - radial-prep-protein-Q27YU6
  - radial-prep-protein-Q27YU2
  - radial-prep-reviewed-symbols
  - radial-prep-family-search-head
  - radial-prep-rsp9-family
  - radial-prep-family-search-stalk
  - record
  - policy
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0001536
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch10 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0001536
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch10 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0001536
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch10 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0001536
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch10 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0001536
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch10 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: radial-prep-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0001535,GO:0001536,GO:0120343,GO:0032991,GO:0001534,GO:0097540
  locator: All six term identities/definitions; GO0032991 and GO0001534 children with
    relation types
  accessed_at: '2026-10-21T07:55:47.868383Z'
  support: supports
  summary: Native active exact head, neck and stalk definitions; the protein-containing-complex
    parent includes all three as is-a children, and the radial-spoke term includes
    them as part-of children. The central-pair identifier is verified as a distinct
    context structure.
  snapshot_sha256: b3b9e98f1e3009e80442af24caa6e6e593a70c19c4650a758752e36f9b003dde
- evidence_id: radial-prep-taxon
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055
  locator: taxId, scientificName, rank and lineage
  accessed_at: '2026-10-21T07:55:47.869041Z'
  support: supports
  summary: Taxon3055 is Chlamydomonas reinhardtii at species rank. The reference accession
    taxon does not identify every experimental stock.
  snapshot_sha256: e3861fe6706cefe2e079e15c0178a65e95efaad3890f548f25e721553eaa93a0
- evidence_id: radial-prep-epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=100&query=DOI%3A%2210.1242/jcs.245233%22%20OR%20DOI%3A%2210.1126/science.1128618%22%20OR%20EXT_ID%3A16507594%20OR%20EXT_ID%3A1508197
  locator: Exact DOI/PMID results, authors/title/year and abstract
  accessed_at: '2026-10-21T07:55:47.869188Z'
  support: supports
  summary: Exact native records verify Poghosyan2020 DOI10.1242/jcs.245233/PMID32694165,
    Nicastro2006 DOI10.1126/science.1128618/PMID16917055, Yang2006 DOI10.1242/jcs.02811/PMID16507594,
    and Curry1992 DOI10.1128/mcb.12.9.3967-3977.1992/PMID1508197. Metadata and abstracts
    are distinguished from actual body access.
  snapshot_sha256: 0ba17bf3187e291a582389f4448411f393cdf4ca7c3c2036507e6f9a4c903b72
- evidence_id: radial-prep-poghosyan-intro-browser
  kind: primary_source
  reference: https://www.researchgate.net/publication/343123729_The_structure_and_symmetry_of_the_radial_spoke_protein_complex_in_Chlamydomonas_flagella
  locator: Publisher-supplied full-text preview; Introduction lines138-259, especially162-169;
    exact browser response JSON, no tool-supplied HTTP status or native PDF assertion
  accessed_at: '2026-10-21T08:00:49.582073Z'
  support: supports
  summary: The Introduction explicitly lists the established head, neck and stalk
    RSP cohorts. The study uses Chlamydomonas and combines purified-spoke structure
    with complementary biochemical information.
  snapshot_sha256: 211eac25b834f5548f141556b3a03bb2e1470da8f7387398659eef81936fe353
- evidence_id: radial-prep-poghosyan-browser
  kind: primary_source
  reference: https://www.researchgate.net/publication/343123729_The_structure_and_symmetry_of_the_radial_spoke_protein_complex_in_Chlamydomonas_flagella
  locator: Primary Results/Discussion pp2-6, lines341-923, Fig2/3/5 legends and explicit
    model limitations; browser response JSON
  accessed_at: '2026-10-21T08:00:08.095758Z'
  support: supports
  summary: The study resolves regional architecture and proposes head/neck subunit
    positions using cross-linking and biochemical constraints; it does not provide
    an atomic assignment for every spoke protein.
  snapshot_sha256: 2506cf11a1f4882708661846708ae8b214fa144c1f49751e2a4e6beec0746415
- evidence_id: radial-prep-poghosyan-methods-browser
  kind: primary_source
  reference: https://www.researchgate.net/publication/343123729_The_structure_and_symmetry_of_the_radial_spoke_protein_complex_in_Chlamydomonas_flagella
  locator: Primary Methods pp7-8, lines994-1415; Discussion lines931-992; browser
    response JSON
  accessed_at: '2026-10-21T08:00:20.822614Z'
  support: supports
  summary: WT137c tomography is distinct from pf28pf30 conventional purification and
    a transgenic His-RSP3 optimized preparation. Segmentation, cross-linking and recombinant-protein
    assays constrain the model.
  snapshot_sha256: b2a12db9e07db66c8086242c95ca447994e7787ef85b10f804f7ff18b5f83b47
- evidence_id: radial-prep-nicastro-browser
  kind: primary_source
  reference: https://www.researchgate.net/publication/6871150_The_Molecular_Architecture_of_Axonemes_Revealed_by_Cryoelectron_Tomography
  locator: Author-uploaded primary body and Fig1F-G/Fig5C-D context; original retrieval
    retained; exact browser response JSON
  accessed_at: '2026-10-21T07:38:16.675911Z'
  support: supports
  summary: Chlamydomonas axonemal tomography provides whole-spoke architectural context.
    It is not a region-specific protein inventory or atomic subunit assignment.
  snapshot_sha256: 0d28f5c7269d892d9ff78d7f8699840cf5ca9887d0b8967c9a2f8afbf12d8d11
- evidence_id: radial-prep-nicastro-methods-browser
  kind: primary_source
  reference: https://www.researchgate.net/publication/6871150_The_Molecular_Architecture_of_Axonemes_Revealed_by_Cryoelectron_Tomography
  locator: Primary supporting-material methods lines1562-1652; separate browser response
    hash and original retrieval timestamp
  accessed_at: '2026-10-21T07:38:38.502409Z'
  support: supports
  summary: Supplemental methods distinguish Chlamydomonas137c and pf9-3 preparations
    from sea-urchin sperm; no strain identity is inferred from species-level reference
    proteins.
  snapshot_sha256: 6a9ed325f07a171d0f956a008bddea206631151f957a0463f11d687f68dda60e
- evidence_id: radial-prep-yang-html
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1973137/?report=xml
  locator: Actual PMC1973137 HTML sectionsS3-S5,S8-S10,S12-S19, Table1 and Fig1/3/6
    legends; distinct from failed JATS route
  accessed_at: '2026-10-21T07:59:23.226696Z'
  support: supports
  summary: Primary purification, peptide identification and immunoblot controls establish
    RSP identities; head/stalk assignments use mutant and biochemical context. Motifs
    and detailed organization remain models where stated.
  snapshot_sha256: bdb7c5af8600183f68c00b2e080f13d0621e3184b7aea97c7db2e88c507f12b8
- evidence_id: radial-prep-protein-P12759
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P12759.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism, relevant
    citation/localization attribution
  accessed_at: '2026-10-21T07:55:48.720722Z'
  support: supports
  summary: Native P12759 is REVIEWED, gene RSP3, taxon3055; accession name, status
    and gene/taxon pairing match. Accession identity alone is not region-specific
    membership evidence.
  snapshot_sha256: 65b4c59781a111e35ecd8a2bc548d5ba2347dbc596f405bc9ba78cd08cd0f76d
- evidence_id: radial-prep-protein-Q27YU7
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q27YU7.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism, relevant
    citation/localization attribution
  accessed_at: '2026-10-21T07:55:48.735635Z'
  support: supports
  summary: Native Q27YU7 is REVIEWED, gene RSP5, taxon3055; accession name, status
    and gene/taxon pairing match. Accession identity alone is not region-specific
    membership evidence.
  snapshot_sha256: b90e96d4e0724d16701d068fb5676b6cd65d2266dbf6717e6bf922bc49714c92
- evidence_id: radial-prep-protein-Q27YT9
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q27YT9.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism, relevant
    citation/localization attribution
  accessed_at: '2026-10-21T07:55:49.013831Z'
  support: supports
  summary: Native Q27YT9 is UNREVIEWED, gene RSP7, taxon3055; accession name, status
    and gene/taxon pairing match. Accession identity alone is not region-specific
    membership evidence.
  snapshot_sha256: 5d35a20ee93ad5f1234225ff79a9a5d588e4eb1b2b35a45aa36f9c2fce9b6dfd
- evidence_id: radial-prep-protein-Q27YU6
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q27YU6.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism, relevant
    citation/localization attribution
  accessed_at: '2026-10-21T07:55:49.341520Z'
  support: supports
  summary: Native Q27YU6 is UNREVIEWED, gene RSP8, taxon3055; accession name, status
    and gene/taxon pairing match. Accession identity alone is not region-specific
    membership evidence.
  snapshot_sha256: ed7a558ca5a0ff032612dcb83d6bab3e6ad8890962b236350397d7955a9d021c
- evidence_id: radial-prep-protein-Q27YU2
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q27YU2.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism, relevant
    citation/localization attribution
  accessed_at: '2026-10-21T07:55:49.664083Z'
  support: supports
  summary: Native Q27YU2 is UNREVIEWED, gene RSP12, taxon3055; accession name, status
    and gene/taxon pairing match. Accession identity alone is not region-specific
    membership evidence.
  snapshot_sha256: 5fbb70dafde75059a161530daed7c8fb486b8e21e5f9d98cb165c5de47e87986
- evidence_id: radial-prep-reviewed-symbols
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28taxonomy_id%3A3055%29%20AND%20%28reviewed%3Atrue%29%20AND%20%28gene_exact%3ARSP1%20OR%20gene_exact%3ARSP2%20OR%20gene_exact%3ARSP3%20OR%20gene_exact%3ARSP4%20OR%20gene_exact%3ARSP5%20OR%20gene_exact%3ARSP6%29
  locator: Exact six-symbol query and all returned entries; one result per exact gene
    token
  accessed_at: '2026-10-21T08:02:19.747361Z'
  support: context_only
  summary: The bounded native taxon3055 reviewed query returns one matching entry
    for each requested exact symbol RSP1,RSP2,RSP3,RSP4,RSP5,RSP6, matching the stated
    reviewed examples. Unreviewed examples are not relabeled.
  snapshot_sha256: fe08d114681674b2a6e635031f9af337065fc3756923619408edfdda91a8f4ac
- evidence_id: radial-prep-family-search-head
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=radial%20spoke%20head&page_size=200
  locator: InterPro entry search=radial spoke head, page_size200, count1 and next=null
  accessed_at: '2026-10-21T07:55:49.678389Z'
  support: context_only
  summary: The exact phrase search returns one RSP9 homolog family, not a family encompassing
    the full multi-protein cohort. This bounded search is not a global absence proof.
  snapshot_sha256: 4088fa1ce575b768e2c591d095c32454ee8577e70aba7f39bf932930836d04e9
- evidence_id: radial-prep-rsp9-family
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR055316/
  locator: Native family type, name, hierarchy and description
  accessed_at: '2026-10-21T08:00:41.296303Z'
  support: context_only
  summary: IPR055316 denotes the RSP9 homolog family; its member scope does not cover
    all head/neck/stalk proteins. It is not an exact grounding for the target aggregate.
  snapshot_sha256: 8e972a4ad66b3215025f8b07f521fab3a62d60a0f3a6b40c7be23de5dde9c2fa
- evidence_id: radial-prep-family-search-stalk
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=radial%20spoke%20stalk&page_size=200
  locator: Exact phrase query; HTTP204 empty body
  accessed_at: '2026-10-21T07:55:49.761881Z'
  support: context_only
  summary: This endpoint returned no content for the narrow phrase search. It does
    not establish universal absence of all relevant families.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/radial_spoke_stalk.yaml
  locator: Entire target, history, component and examples, every graph edge and both
    discussions
  accessed_at: '2026-10-21T08:03:28Z'
  support: context_only
  summary: Complete maintained target read; PROPOSED status retained, and the graph
    explicitly records nonmechanistic topology.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Components and source evidence rules
  accessed_at: '2026-10-21T08:03:28Z'
  support: context_only
  summary: Source-neutral component classes, exact taxon-paired identities and independent
    membership support are distinct requirements.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/radial_spoke_stalk.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T07:54:08Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/radial_spoke_stalk.yaml'
  snapshot_sha256: 4e8145831ac4943be1412ba05183f70b4e9ffdd3e750c24b7af62e21923b223c
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/radial_spoke_stalk.yaml
    --out /private/tmp/cellstructure-batch10-20261021-giynduuy/radial_spoke_stalk-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T07:54:10Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/radial_spoke_stalk.yaml\
    \ --out /private/tmp/cellstructure-batch10-20261021-giynduuy/radial_spoke_stalk-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch10-20261021-giynduuy/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch10-20261021-giynduuy/radial_spoke_stalk-strict.tsv"
  snapshot_sha256: 8b90b835132750aec00e0e1f0fd5db65d83f8a105949f3cb8acb2c03c84686c5
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/radial_spoke_stalk.yaml; exact collect() scope;
    hash identifies the entire original strict-resolver TSV, not the derived target
    slice
  accessed_at: '2026-10-21T08:03:28Z'
  support: supports
  summary: '13 of 14 collected target identifiers returned OK at the unchanged base.
    Residuals: PMID:16507594: UNREACHABLE; resolved by evidence radial-prep-epmc.
    Source-native identity checked separately.'
  snapshot_sha256: 68d64e4e86437df228658f43be4d47b41054fe882fedf357e660293691a0a061
- evidence_id: global-qc-result
  kind: validation
  reference: just qc
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec
  accessed_at: '2026-10-19T07:38:12Z'
  support: supports
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  snapshot_sha256: 7b6165ba8532d080a336f7a5a4c29b456fdf7182dd596410b700dfe60af61a06
- evidence_id: global-history-result
  kind: validation
  reference: just validate-history
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0
  accessed_at: '2026-10-19T07:29:37Z'
  support: supports
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  snapshot_sha256: b98e3eecd58a81fa46033e6baca6977811a439f119b943fd5d9931964adb2680
- evidence_id: global-products-result
  kind: validation
  reference: just validate-products
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad
  accessed_at: '2026-10-19T07:32:39Z'
  support: supports
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  snapshot_sha256: 2a1330c26aac5bd248a2fd3a3a7b9c882d2b3bb202365c555e5d6415d1c2203d
- evidence_id: global-traits-result
  kind: validation
  reference: just check-trait-links --check
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad
  accessed_at: '2026-10-19T07:29:45Z'
  support: supports
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  snapshot_sha256: 6eab64b59433928ec8e0df9b0046dbccf479c84bb0911c315feebc344d536007
- evidence_id: global-curies-result
  kind: validation
  reference: just check-curies-strict
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4
  accessed_at: '2026-10-19T08:04:01Z'
  support: supports
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  snapshot_sha256: 7cb413edccc92ee6ce79a32cd2b96a59bc4da37f2cb7b326eaca51a64f723cfb
assessments:
- assessment_id: identity
  area: identity
  topic: Exact regional identity and parthood
  outcome: supported
  target_ids:
  - GO:0001536
  summary: The identifier, definition, protein-complex parent and whole-radial-spoke
    parthood agree with native GO. Head, neck, stalk, base, central-pair context and
    complete spoke are not interchangeable.
  evidence_ids:
  - radial-prep-go
  - record
- assessment_id: composition
  area: grounding
  topic: Regional cohort and sequence identities
  outcome: supported
  target_ids:
  - GO:0001536
  summary: The declared RSP3, RSP5, RSP7, RSP8, RSP11 and RSP12 belong to the source's
    established stalk cohort. Concrete examples agree with native accession identities;
    membership is assessed separately through the regional literature. The list is
    not asserted to be exhaustive, to define universal stoichiometry, or to prove
    each paralog essential.
  evidence_ids:
  - radial-prep-poghosyan-intro-browser
  - radial-prep-poghosyan-browser
  - radial-prep-yang-html
  - radial-prep-protein-P12759
  - radial-prep-protein-Q27YU7
  - radial-prep-protein-Q27YT9
  - radial-prep-protein-Q27YU6
  - radial-prep-protein-Q27YU2
  - radial-prep-reviewed-symbols
  - record
- assessment_id: family
  area: grounding
  topic: Heterogeneous cohort and narrower families
  outcome: supported
  target_ids:
  - GO:0001536
  summary: This aggregate encompasses multiple distinct RSP families. A candidate
    for one subunit cannot ground the entire component. Splitting into separately
    sourced family components remains optional enrichment; no verified whole-cohort
    accession is established by the bounded searches.
  evidence_ids:
  - radial-prep-family-search-head
  - radial-prep-rsp9-family
  - record
  - policy
- assessment_id: scope
  area: scope
  topic: Chlamydomonas reference and experimental scope
  outcome: supported
  target_ids:
  - GO:0001536
  summary: The common species example is supported by the axonemal studies. The target
    does not transfer its named protein cohort to all ciliated taxa or identify reference
    sequences with the distinct engineered experimental strains.
  evidence_ids:
  - radial-prep-taxon
  - radial-prep-poghosyan-intro-browser
  - radial-prep-poghosyan-methods-browser
  - radial-prep-nicastro-browser
  - radial-prep-nicastro-methods-browser
  - radial-prep-protein-P12759
  - radial-prep-protein-Q27YU7
  - radial-prep-protein-Q27YT9
  - radial-prep-protein-Q27YU6
  - radial-prep-protein-Q27YU2
  - record
- assessment_id: graph
  area: graph
  topic: Every topology edge
  outcome: supported
  target_ids:
  - GO:0001536
  summary: Four edges correctly record protein contribution, spoke parthood and connections
    to base and neck. The ungrounded base node is an explicit topological region;
    the graph does not replace it with a direct stalk-to-A-tubule edge.
  evidence_ids:
  - radial-prep-go
  - radial-prep-poghosyan-browser
  - radial-prep-nicastro-browser
  - record
- assessment_id: function
  area: evidence
  topic: Coarse architectural contribution
  outcome: supported
  target_ids:
  - GO:0001536
  summary: The function describes the region's anatomical contribution. Motility transduction
    is apparatus-level context; no calibrated mechanical output, ordered recruitment
    pathway or per-protein catalytic mechanism is claimed.
  evidence_ids:
  - radial-prep-go
  - radial-prep-poghosyan-browser
  - radial-prep-poghosyan-methods-browser
  - radial-prep-yang-html
  - record
- assessment_id: evidence
  area: evidence
  topic: Primary model and actual access
  outcome: supported
  target_ids:
  - GO:0001536
  summary: Full claim-bearing Poghosyan and Nicastro browser-rendered primary text
    and Yang native HTML were inspected. Source-specific snapshots retain transport/access
    limits. Structure and biochemical constraints are distinguished from hypothesized
    subunit positions and biochemical regulation.
  evidence_ids:
  - radial-prep-poghosyan-intro-browser
  - radial-prep-poghosyan-browser
  - radial-prep-poghosyan-methods-browser
  - radial-prep-nicastro-browser
  - radial-prep-nicastro-methods-browser
  - radial-prep-yang-html
  - radial-prep-epmc
  - record
- assessment_id: completeness
  area: completeness
  topic: Inventory, dimensions and data-source scope
  outcome: supported
  target_ids:
  - GO:0001536
  summary: Exact copy numbers, exhaustive associated proteins, detailed cross-species
    boundaries and complete assembly mechanism remain unresolved. No figures, physical
    dimensions, trait links or pathway relations occur in this target; their omission
    is not an unsupported claim.
  evidence_ids:
  - radial-prep-go
  - radial-prep-poghosyan-browser
  - radial-prep-yang-html
  - record
- assessment_id: source-overstatement
  area: evidence
  topic: Individual stalk-density assignment
  outcome: concern
  target_ids:
  - GO:0001536
  summary: The current open discussion overstates the primary paper's assignment scope.
    The Introduction lists the established stalk cohort, but individual segmented-density
    assignments are head/neck-specific; the stalk is represented as a coarse region.
  evidence_ids:
  - radial-prep-poghosyan-intro-browser
  - radial-prep-poghosyan-browser
  - radial-prep-poghosyan-methods-browser
  - radial-prep-yang-html
  - record
findings:
- finding_id: F1
  issue_key: radial-spoke-stalk-individual-density-overstatement
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: The open discussion overstates individual stalk-density assignment
  description: The discussion credits Poghosyan2020 with assigning individual RSP
    densities to the stalk. Its Introduction summarizes the established stalk cohort,
    while its individual density assignments and segmentation methods concern head/neck
    proteins. Replace that claim with regional architectural refinement and established
    stalk composition; retain the supported stalk genes and distinguish the source's
    proposed model from direct subunit mapping.
  target_ids:
  - GO:0001536
  field_paths:
  - discussions[discussion_id=resolve_radial_spoke_stalk_proteins].rationale
  - components[component_id=radial_spoke_stalk_proteins].evidence
  - functions[function_id=radial_spoke_stalk_outer_doublet_linkage].evidence
  evidence_ids:
  - radial-prep-poghosyan-intro-browser
  - radial-prep-poghosyan-browser
  - radial-prep-poghosyan-methods-browser
  - radial-prep-yang-html
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/radial_spoke_stalk.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:Evidence Rules
  native_severity: minor
  normalization_reason: Bounded overstatement of what the cited study assigned; regional
    identity and the established protein cohort remain supported.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0001536
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/radial_spoke_stalk.yaml
    role: maintained scientific record
  description: Under separately authorized curation, correct the individual stalk-density
    claim and clarify the broader assignment notes to distinguish established membership
    from the2020 head/neck density model.
  acceptance_checks:
  - Retain the exact stalk identity, base-to-neck topology and supported gene cohort.
  - Describe the study as refining regional architecture and summarizing established
    stalk proteins; do not claim individual stalk-density mapping.
  - Preserve model, stoichiometry and regional-overlap limits; use guarded curation/history
    and required native checks.
  generator: Maintained structure YAML; pages derive through just render.
limitations:
- Browser-rendered primary text and legends were inspected; native publisher/institution
  PDF routes were blocked. Browser snapshots carry no native HTTP status, and no independent
  microscopy-pixel, raw-map, movie or complete supplemental-data reanalysis is claimed.
- The2020 head/neck arrangement is an experimentally constrained model, including
  possible overlap of regional protein positions. Exact copy numbers and exclusive
  spatial membership are not adopted.
- The family searches are bounded to the stated queries. An empty HTTP204 response
  is an access/result limit, not proof that no exact family exists anywhere.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- Root personally read each full target and the stated source sections. Only this
  target receives scientific coverage.
- Only the review bundle is saved. Maintained scientific content, native status, history
  and generated pages remain unchanged.
- A separate reviewer independently read the target and primary Introduction, Results/Discussion
  and segmentation Methods and agreed with the bounded source-overstatement finding.
- Only this target receives scientific review coverage. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
