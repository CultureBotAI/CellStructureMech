# Basal-body B-C junction regional composition and evidence review

- Review: 20261020T065433Z-basal-body-b-c-inner-junction-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-20T04:09:55Z
- Finished UTC: 2026-10-20T06:54:33Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Regional composition, two species examples, four proximal contact edges, six deposits and hosted image are supported. One minor issue mislabels the POC1 example’s UniProt ORF field.

## Scope And Provenance

Entire record; all components, graph, datasets, discussions and image; four structural studies and the original Poc1 localization source.

Selection: Second unreviewed path of batch4.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:basal_body_b_c_inner_junction | data/structures/cytoskeleton/basal_body_b_c_inner_junction.yaml | maintained | basal body B-C inner junction |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | cellstructuremech:basal_body_b_c_inner_junction | Focused validator passed. |
| Focused native strict | passed | True | cellstructuremech:basal_body_b_c_inner_junction | Focused validator passed. |
| Target resolver slice | passed | True | cellstructuremech:basal_body_b_c_inner_junction | 11 identifiers OK; 8 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | cellstructuremech:basal_body_b_c_inner_junction | No expression dataset or expression-derived membership is asserted. Protein provenance is assessed from native sequence records and primary structural studies. |
| Claim-level scientific review | passed | True | cellstructuremech:basal_body_b_c_inner_junction | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | cellstructuremech:basal_body_b_c_inner_junction | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | cellstructuremech:basal_body_b_c_inner_junction | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | cellstructuremech:basal_body_b_c_inner_junction | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | cellstructuremech:basal_body_b_c_inner_junction | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | cellstructuremech:basal_body_b_c_inner_junction | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### B-C protein network

identity: supported. Targets: cellstructuremech:basal_body_b_c_inner_junction.

The named multiprotein interface is distinct from A-B, the outer junction, A-C linker and inner scaffold. Parent and parthood are appropriate.

### Proximal components and unknown core

evidence: supported. Targets: cellstructuremech:basal_body_b_c_inner_junction.

POC1 and I7LY02 have source-supported proximal assignments at the stated evidence levels. Core bridging proteins and the additional proximal WD40 density remain unassigned, with no forced equivalence between species.

### POC1 accession versus gene-name field

provenance: concern. Targets: cellstructuremech:basal_body_b_c_inner_junction.

The accession itself is directly supported as Poc1 by Ruehle’s model-fitting Results. UniProt lists the TTHERM identifier as an ORF name, not a primary name; this is a nonblocking wording/source-attribution defect.

### Label-only classes

grounding: supported. Targets: cellstructuremech:basal_body_b_c_inner_junction.

The broader family and domain/repeat annotations do not justify exact class grounding. The ladder’s integrated-entry no-match remains bounded.

### Two species and regional maturity

scope: supported. Targets: cellstructuremech:basal_body_b_c_inner_junction.

Tetrahymena proximal/core and wild-type/mutant observations remain distinct. Chlamydomonas pooled mother/procentriole averages are correctly described. Reference sequences are not silently paired with experimental strains.

### Structural connection

evidence: supported. Targets: cellstructuremech:basal_body_b_c_inner_junction.

Sources support luminal B-C connection and core scaffold attachment without proving a unique force threshold or attributing all Poc1 phenotypes to this junction.

### Four proximal fitted-model contacts

graph: supported. Targets: cellstructuremech:basal_body_b_c_inner_junction.

POC1 contacts B08/C10 and the ladder contacts B07/C10 in Cai Figure4. The graph explicitly describes structural-model contacts, not biochemical binding or temporal recruitment.

### Preserved contradictory source details

evidence: supported. Targets: cellstructuremech:basal_body_b_c_inner_junction.

The4nm/8nm MIP9 conflict and46438 regional-label conflict are real and correctly retained. Neither is silently converted into a record measurement or unsupported dataset identity.

### Six bounded native deposits

provenance: supported. Targets: cellstructuremech:basal_body_b_c_inner_junction.

Titles, genotypes, species and citations match the linked reconstructions; the focused WD40 map does not identify the unassigned protein.

### Hosted representative figure

evidence: supported. Targets: cellstructuremech:basal_body_b_c_inner_junction.

The image bytes, depositor attribution, taxonomy, caption and copyright policy match the native source. Inspected article figures are not copied into the corpus.

### Open composition and native status

completeness: supported. Targets: cellstructuremech:basal_body_b_c_inner_junction.

PROPOSED and the open family/core composition questions are appropriate. The record avoids universal stoichiometry, prevalence and essentiality claims.

## Findings

### F1: POC1 example calls an ORF name a UniProt primary gene name

minor / open / confirmed; issue key: basal-body-b-c-inner-junction-poc1-gene-field.

Q229Z6 provides TTHERM_01308010 in orfNames and no primary geneName. Ruehle2024 independently identifies the accession as Poc1. Describe the native field accurately and attribute the symbol mapping to the structural source; the accession and protein-family assignment are supported.

## Recommended Actions And Acceptance Checks

### A1

Call TTHERM_01308010 an ORF/locus name and cite the Ruehle2024 Q229Z6-to-Poc1 assignment while retaining the reference-strain limitation.

- The wording matches UniProt genes.orfNames rather than asserting a primary geneName.
- The named Poc1 mapping remains traceable to the primary source.
- After separately authorized curation, run native record/history and generated-page checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bc-ruehle | https://pmc-oa-opendata.s3.amazonaws.com/PMC11094743.1/PMC11094743.1.xml; Poc1 junction Results, Figure2, FigureS4 and strain Methods | supports | The2024 study localizes Poc1 to proximal B-C using model fit and loss of corresponding density in complete mutant triplets. The core bridge is morphologically different and retained without Poc1; it is distinct from the lost scaffold attachment. |
| bc-li2019 | https://pmc-oa-opendata.s3.amazonaws.com/PMC6384029.1/PMC6384029.1.xml; MIP Results, Table1, Figure2/supplement12, pooling Methods and author response | supports | The Chlamydomonas study identifies B-C MIP9-11 densities without gene assignments. Main averages combine mother proximal segments and attached procentrioles. Results/author response give4nm for MIP9, while Table1 gives8nm; the record preserves the conflict. |
| basal-cai | https://pmc-oa-opendata.s3.amazonaws.com/PMC12506977.1/PMC12506977.1.xml; Junction Results, Figure4 and assignment/sample Methods | supports | The later study traces POC1’s B08-C10 bridge and I7LY02’s B07-C10 ladder. The additional WD40 density is unassigned; TBC1D31A is a hypothesis. Structural sample preparation names SB715. |
| basal-li | https://pmc-oa-opendata.s3.amazonaws.com/PMC11961760.1/PMC11961760.1.xml; Proximal Results, Table2 and Methods | supports | The earlier ladder assignment is unresolved in this source. Table2 calls46438 core B-C while Methods exclude detailed B-C analysis; the later molecular assignment comes from Cai. |
| bc-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1083/jcb.202311104%20OR%20DOI:10.7554/eLife.43434&amp;format=json&amp;resultType=core; Exact article identities | supports | The two additional structural DOIs resolve to the exact Ruehle2024 and Li2019 papers. |
| basal-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1038/s44318-025-00392-6%20OR%20DOI:10.1126/sciadv.ady3689%20OR%20EXT_ID:20008567&amp;format=json&amp;resultType=core; Three exact article metadata results | supports | The Cai/Li2025 papers and PMID20008567 match exact primary identities. |
| basal-proteins | https://rest.uniprot.org/uniprotkb/search?query=accession:Q229Z6%20OR%20accession:Q22ZH2%20OR%20accession:I7LU20%20OR%20accession:W7XCX2%20OR%20accession:W7XDG5%20OR%20accession:Q23EX8%20OR%20accession:I7M9T0%20OR%20accession:I7LY02%20OR%20accession:I7MJ23%20OR%20accession:Q24C92%20OR%20accession:I7MLQ3%20OR%20accession:Q22N53&amp;format=json; Q229Z6 and I7LY02 entries; genes and annotations | context_only | Q229Z6 is reviewed POC1 protein from SB210 with locusTTHERM_01308010 only in orfNames. Its localization annotation cites PMID20008567 exactly. I7LY02 is the unreviewed ladder reference and lacks listed InterPro/Pfam cross-references. |
| basal-poc1-paper | https://pmc-oa-opendata.s3.amazonaws.com/PMC2806327.1/PMC2806327.1.xml; GFP-Poc1 localization Results | supports | Original Poc1 localization results support basal-body localization, as attributed through UniProt. |
| basal-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0140535,GO:0036064,GO:0160113; Exact three GO definitions | supports | The intracellular-complex parent and basal-body part are valid; the axonemal A-B term denotes a different structural context. |
| outer-junction-taxa | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=5911,312017; Native taxonomy records | supports | Tetrahymena species5911 and reference strain312017 match their recorded names. |
| sheath-taxon | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=3055; Native species identity | supports | NCBITaxon3055 identifies Chlamydomonas reinhardtii. |
| basal-IPR050505 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050505; Entry name/type/definition | supports | The cited POC1-related family is broader than POC1, and the other annotations are repeats/domains. No exact replacement family is established. |
| basal-IPR020472 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020472; Entry name/type/definition | supports | The cited POC1-related family is broader than POC1, and the other annotations are repeats/domains. No exact replacement family is established. |
| basal-IPR056551 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR056551; Entry name/type/definition | supports | The cited POC1-related family is broader than POC1, and the other annotations are repeats/domains. No exact replacement family is established. |
| basal-pdb9qzc8 | https://data.rcsb.org/rest/v1/core/polymer_entity/9QZC/8; Exact entity mapping | supports | 9QZC entity8 maps exactly to I7LY02; this establishes the sequence model identity. |
| ladder-interpro | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/I7LY02/; Integrated InterPro entries for I7LY02 | context_only | The native endpoint returned HTTP204. This bounded absence of an integrated entry is not taxonomic absence of the structure. |
| bc-emdb42781 | https://www.ebi.ac.uk/emdb/api/entry/EMD-42781; Admin title/status/authors, source taxon and primary citation | supports | The released entry’s title, source taxon and primary citation match the record’s region, genotype and focused-reconstruction description. The42781 title typo is corrected by native natural-source metadata. |
| bc-emdb42777 | https://www.ebi.ac.uk/emdb/api/entry/EMD-42777; Admin title/status/authors, source taxon and primary citation | supports | The released entry’s title, source taxon and primary citation match the record’s region, genotype and focused-reconstruction description. The42781 title typo is corrected by native natural-source metadata. |
| bc-emdb42783 | https://www.ebi.ac.uk/emdb/api/entry/EMD-42783; Admin title/status/authors, source taxon and primary citation | supports | The released entry’s title, source taxon and primary citation match the record’s region, genotype and focused-reconstruction description. The42781 title typo is corrected by native natural-source metadata. |
| bc-emdb42784 | https://www.ebi.ac.uk/emdb/api/entry/EMD-42784; Admin title/status/authors, source taxon and primary citation | supports | The released entry’s title, source taxon and primary citation match the record’s region, genotype and focused-reconstruction description. The42781 title typo is corrected by native natural-source metadata. |
| bc-emdb53982 | https://www.ebi.ac.uk/emdb/api/entry/EMD-53982; Admin title/status/authors, source taxon and primary citation | supports | The released entry’s title, source taxon and primary citation match the record’s region, genotype and focused-reconstruction description. The42781 title typo is corrected by native natural-source metadata. |
| bc-emdb53983 | https://www.ebi.ac.uk/emdb/api/entry/EMD-53983; Admin title/status/authors, source taxon and primary citation | supports | The released entry’s title, source taxon and primary citation match the record’s region, genotype and focused-reconstruction description. The42781 title typo is corrected by native natural-source metadata. |
| basal-emdb46438 | https://www.ebi.ac.uk/emdb/api/entry/EMD-46438; Entry title and source | supports | The native title says proximal B-C, confirming the retained discrepancy with the Li2025 table. |
| bc-image | https://ftp.ebi.ac.uk/pub/databases/emdb/structures/EMD-42781/images/emd_42781.png; Complete PNG, byte comparison and visual inspection | supports | Source PNG and maintained image both have SHA256df7ed8e6da1d20a19522b82a1c2b0afc590de9c802972628beb22fabd0951860. Visual inspection confirms an unlabeled density rendering without a scale bar. |
| basal-policy | https://www.ebi.ac.uk/emdb/policies.html; Section3.1.2 | supports | EMDB policy3.1.2 requires representative figures free of copyright restrictions; the record explicitly states its licence convention. |
| bc-ruehle-fig2 | https://pmc-oa-opendata.s3.amazonaws.com/PMC11094743.1/JCB_202311104_Fig2.jpg; Complete primary figure | supports | Figure visually inspected for the claimed density assignments, mutant/core distinctions and unresolved MIP9 interpretation. |
| bc-ruehle-s4 | https://pmc-oa-opendata.s3.amazonaws.com/PMC11094743.1/JCB_202311104_FigS4.jpg; Complete primary figure | supports | Figure visually inspected for the claimed density assignments, mutant/core distinctions and unresolved MIP9 interpretation. |
| bc-li-fig2 | https://pmc-oa-opendata.s3.amazonaws.com/PMC6384029.1/elife-43434-fig2.jpg; Complete primary figure | supports | Figure visually inspected for the claimed density assignments, mutant/core distinctions and unresolved MIP9 interpretation. |
| bc-li-s12 | https://pmc-oa-opendata.s3.amazonaws.com/PMC6384029.1/elife-43434-fig2-figsupp12.jpg; Complete primary figure | supports | Figure visually inspected for the claimed density assignments, mutant/core distinctions and unresolved MIP9 interpretation. |
| basal-cai-fig4 | https://pmc-oa-opendata.s3.amazonaws.com/PMC12506977.1/sciadv.ady3689-f4.jpg; Figure4A-C; visual inspection | supports | Figure4A-C distinguishes the POC1 bridge, I7LY02 ladder and unassigned WD40 density at the proximal B-C interface. |
| record | data/structures/cytoskeleton/basal_body_b_c_inner_junction.yaml; Entire target, two components, one example, four edges, six datasets, discussions and image | context_only | The scientific claims preserve regional, species, genotype and model-fitting scope. The POC1 example inaccurately calls a UniProt ORF identifier a primary gene name. |
| local-id | data/structures/cytoskeleton/basal_body_b_c_inner_junction.yaml; Hidden/ignored-inclusive exact-identifier rg across data/structures | context_only | Only the target declares this local identifier; its local namespace is not an externally resolvable accession. |
| schema-result | just validate data/structures/cytoskeleton/basal_body_b_c_inner_junction.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/basal_body_b_c_inner_junction.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/basal_body_b_c_inner_junction.yaml --out /private/tmp/cellstructure-batch4-20261019-QtBQNE/basal_body_b_c_inner_junction-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/basal_body_b_c_inner_junction.yaml --out /private/tmp/cellstructure-batch4-20261019-QtBQNE/basal_body_b_c_inner_junction-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch4-20261019-QtBQNE/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch4-20261019-QtBQNE/basal_body_b_c_inner_junction-strict.tsv |
| target-curies | just check-curies-strict; data/structures/cytoskeleton/basal_body_b_c_inner_junction.yaml; exact collect() scope | supports | 11 of19 collected target identifiers returned OK at the unchanged base. Residuals: EMDB:EMD-42777: SKIPPED; resolved by evidence bc-emdb42777; EMDB:EMD-42781: SKIPPED; resolved by evidence bc-emdb42781; EMDB:EMD-42783: SKIPPED; resolved by evidence bc-emdb42783; EMDB:EMD-42784: SKIPPED; resolved by evidence bc-emdb42784; EMDB:EMD-53982: SKIPPED; resolved by evidence bc-emdb53982; EMDB:EMD-53983: SKIPPED; resolved by evidence bc-emdb53983; PMID:20008567: UNREACHABLE; resolved by evidence basal-epmc; cellstructuremech:basal_body_b_c_inner_junction: SKIPPED; resolved by evidence local-id. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Exact core and additional WD40 protein identities remain unresolved.
- The Chlamydomonas density labels do not establish a molecular crosswalk to Tetrahymena proteins.
- Conflicting MIP9 repeat and46438 region labels are retained rather than adjudicated beyond the available evidence.
- Map volumes were not reprocessed; native metadata, primary interpretations and figures were inspected.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Only the review bundle is saved. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T065433Z-basal-body-b-c-inner-junction-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Basal-body B-C junction regional composition and evidence review
started_at: '2026-10-20T04:09:55Z'
finished_at: '2026-10-20T06:54:33Z'
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
summary: Regional composition, two species examples, four proximal contact edges,
  six deposits and hosted image are supported. One minor issue mislabels the POC1
  example’s UniProt ORF field.
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
  - path: data/images/cytoskeleton/basal_body_b_c_inner_junction/emd_42781.png
    sha256: df7ed8e6da1d20a19522b82a1c2b0afc590de9c802972628beb22fabd0951860
    role: context
  - path: data/structures/cytoskeleton/basal_body_b_c_inner_junction.yaml
    sha256: 9c4967f2edcd2ccc044157dd3bc03ed3f066d5bcd7205e2f5cc30da20e858ea1
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
- target_id: cellstructuremech:basal_body_b_c_inner_junction
  path: data/structures/cytoskeleton/basal_body_b_c_inner_junction.yaml
  label: basal body B-C inner junction
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/basal_body_b_c_inner_junction.yaml
    role: maintained scientific record
scope:
  description: Entire record; all components, graph, datasets, discussions and image;
    four structural studies and the original Poc1 localization source.
  selection: Second unreviewed path of batch4.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:basal_body_b_c_inner_junction
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_b_c_inner_junction
  command: just validate data/structures/cytoskeleton/basal_body_b_c_inner_junction.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_b_c_inner_junction
  command: just validate-strict data/structures/cytoskeleton/basal_body_b_c_inner_junction.yaml
    --out /private/tmp/cellstructure-batch4-20261019-QtBQNE/basal_body_b_c_inner_junction-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_b_c_inner_junction
  summary: 11 identifiers OK; 8 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - bc-emdb42781
  - basal-epmc
  - bc-emdb42784
  - bc-emdb53982
  - bc-emdb53983
  - bc-emdb42777
  - local-id
  - bc-emdb42783
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - cellstructuremech:basal_body_b_c_inner_junction
  summary: No expression dataset or expression-derived membership is asserted. Protein
    provenance is assessed from native sequence records and primary structural studies.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_b_c_inner_junction
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - bc-ruehle
  - bc-li2019
  - basal-cai
  - basal-li
  - bc-epmc
  - basal-epmc
  - basal-proteins
  - basal-poc1-paper
  - basal-go
  - outer-junction-taxa
  - sheath-taxon
  - basal-IPR050505
  - basal-IPR020472
  - basal-IPR056551
  - basal-pdb9qzc8
  - ladder-interpro
  - bc-emdb42781
  - bc-emdb42777
  - bc-emdb42783
  - bc-emdb42784
  - bc-emdb53982
  - bc-emdb53983
  - basal-emdb46438
  - bc-image
  - basal-policy
  - bc-ruehle-fig2
  - bc-ruehle-s4
  - bc-li-fig2
  - bc-li-s12
  - basal-cai-fig4
  - record
  - local-id
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_b_c_inner_junction
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch3 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_b_c_inner_junction
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch3 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_b_c_inner_junction
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch3 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_b_c_inner_junction
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch3 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_b_c_inner_junction
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch3 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: bc-ruehle
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC11094743.1/PMC11094743.1.xml
  locator: Poc1 junction Results, Figure2, FigureS4 and strain Methods
  accessed_at: '2026-10-20T04:10:07.463296Z'
  support: supports
  summary: The2024 study localizes Poc1 to proximal B-C using model fit and loss of
    corresponding density in complete mutant triplets. The core bridge is morphologically
    different and retained without Poc1; it is distinct from the lost scaffold attachment.
  snapshot_sha256: 85209722ca994d8f3d4a5d61e5ba1cb45c4a7953c6f265a0dd19be83ec75926d
- evidence_id: bc-li2019
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6384029.1/PMC6384029.1.xml
  locator: MIP Results, Table1, Figure2/supplement12, pooling Methods and author response
  accessed_at: '2026-10-20T04:10:07.604636Z'
  support: supports
  summary: The Chlamydomonas study identifies B-C MIP9-11 densities without gene assignments.
    Main averages combine mother proximal segments and attached procentrioles. Results/author
    response give4nm for MIP9, while Table1 gives8nm; the record preserves the conflict.
  snapshot_sha256: 2965143460a98de85b7b6525bea14596791bbf9a32094484b54e42b74794af7a
- evidence_id: basal-cai
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC12506977.1/PMC12506977.1.xml
  locator: Junction Results, Figure4 and assignment/sample Methods
  accessed_at: '2026-10-20T04:01:04.096242Z'
  support: supports
  summary: The later study traces POC1’s B08-C10 bridge and I7LY02’s B07-C10 ladder.
    The additional WD40 density is unassigned; TBC1D31A is a hypothesis. Structural
    sample preparation names SB715.
  snapshot_sha256: ab8bf23b7821eaa514f3eebd1c4f281e1eb1c2af9ef4dc429aced2fe5dfcb04a
- evidence_id: basal-li
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC11961760.1/PMC11961760.1.xml
  locator: Proximal Results, Table2 and Methods
  accessed_at: '2026-10-20T04:01:03.411389Z'
  support: supports
  summary: The earlier ladder assignment is unresolved in this source. Table2 calls46438
    core B-C while Methods exclude detailed B-C analysis; the later molecular assignment
    comes from Cai.
  snapshot_sha256: d1bfd06b3f2d20e19d7118186aee0d8333391748546a179f0694a9611c29bd61
- evidence_id: bc-epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1083/jcb.202311104%20OR%20DOI:10.7554/eLife.43434&format=json&resultType=core
  locator: Exact article identities
  accessed_at: '2026-10-20T04:10:07.568353Z'
  support: supports
  summary: The two additional structural DOIs resolve to the exact Ruehle2024 and
    Li2019 papers.
  snapshot_sha256: f0ab2357cbfb307cd5527ea3ff914c1ac8eac0a9699276c5e493b36d57f28b05
- evidence_id: basal-epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1038/s44318-025-00392-6%20OR%20DOI:10.1126/sciadv.ady3689%20OR%20EXT_ID:20008567&format=json&resultType=core
  locator: Three exact article metadata results
  accessed_at: '2026-10-20T04:01:03.594222Z'
  support: supports
  summary: The Cai/Li2025 papers and PMID20008567 match exact primary identities.
  snapshot_sha256: 20208f5249e6f4ec1ec9f51c8e8ee7844c4b2541d27c7492dd7ea833b8afba11
- evidence_id: basal-proteins
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?query=accession:Q229Z6%20OR%20accession:Q22ZH2%20OR%20accession:I7LU20%20OR%20accession:W7XCX2%20OR%20accession:W7XDG5%20OR%20accession:Q23EX8%20OR%20accession:I7M9T0%20OR%20accession:I7LY02%20OR%20accession:I7MJ23%20OR%20accession:Q24C92%20OR%20accession:I7MLQ3%20OR%20accession:Q22N53&format=json
  locator: Q229Z6 and I7LY02 entries; genes and annotations
  accessed_at: '2026-10-20T04:01:03.753057Z'
  support: context_only
  summary: Q229Z6 is reviewed POC1 protein from SB210 with locusTTHERM_01308010 only
    in orfNames. Its localization annotation cites PMID20008567 exactly. I7LY02 is
    the unreviewed ladder reference and lacks listed InterPro/Pfam cross-references.
  snapshot_sha256: 94cf7783b68cce4d2db5f1af3ba8a5a505723d6f83bee53e8da1c6e2bed8a6ae
- evidence_id: basal-poc1-paper
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2806327.1/PMC2806327.1.xml
  locator: GFP-Poc1 localization Results
  accessed_at: '2026-10-20T04:03:32.503253Z'
  support: supports
  summary: Original Poc1 localization results support basal-body localization, as
    attributed through UniProt.
  snapshot_sha256: f4c5df75072c24ca64f8b73b93f84cb7b3bead5b31ef02eedaf3f320f0c0ad0a
- evidence_id: basal-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0140535,GO:0036064,GO:0160113
  locator: Exact three GO definitions
  accessed_at: '2026-10-20T04:01:03.550318Z'
  support: supports
  summary: The intracellular-complex parent and basal-body part are valid; the axonemal
    A-B term denotes a different structural context.
  snapshot_sha256: ff1bf3e7d1d0d44fa46e41651fb0d225bf35375d06cbce944ec49e86868ba509
- evidence_id: outer-junction-taxa
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=5911,312017
  locator: Native taxonomy records
  accessed_at: '2026-10-20T03:52:55.154591Z'
  support: supports
  summary: Tetrahymena species5911 and reference strain312017 match their recorded
    names.
  snapshot_sha256: fda62743792eecc892116e6d58703350304a02ea34bd536d666e735750142c2a
- evidence_id: sheath-taxon
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=3055
  locator: Native species identity
  accessed_at: '2026-10-20T03:38:20.199537Z'
  support: supports
  summary: NCBITaxon3055 identifies Chlamydomonas reinhardtii.
  snapshot_sha256: a17bc1c97fea9112288574ef15727ed7e37c42787a430ef074ae5fc654547e6b
- evidence_id: basal-IPR050505
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050505
  locator: Entry name/type/definition
  accessed_at: '2026-10-20T04:01:05.136709Z'
  support: supports
  summary: The cited POC1-related family is broader than POC1, and the other annotations
    are repeats/domains. No exact replacement family is established.
  snapshot_sha256: a441faeaa7da8487b8e14015dcc322403b37d7620dc71a539ed189b411dac195
- evidence_id: basal-IPR020472
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020472
  locator: Entry name/type/definition
  accessed_at: '2026-10-20T04:01:05.207719Z'
  support: supports
  summary: The cited POC1-related family is broader than POC1, and the other annotations
    are repeats/domains. No exact replacement family is established.
  snapshot_sha256: f5ceeddc437713cad39c49c699d92bf1b9a5bb9ef18d46e036338a736f24f673
- evidence_id: basal-IPR056551
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR056551
  locator: Entry name/type/definition
  accessed_at: '2026-10-20T04:01:47.989671Z'
  support: supports
  summary: The cited POC1-related family is broader than POC1, and the other annotations
    are repeats/domains. No exact replacement family is established.
  snapshot_sha256: 0d4fad01d608cfc20b180d46f26792250befd95a1930d7615e3a832db3169936
- evidence_id: basal-pdb9qzc8
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/9QZC/8
  locator: Exact entity mapping
  accessed_at: '2026-10-20T04:01:04.567570Z'
  support: supports
  summary: 9QZC entity8 maps exactly to I7LY02; this establishes the sequence model
    identity.
  snapshot_sha256: be57ff9ae430382d536725916de77efb95bc96f36666065dfc1716c06d2a25aa
- evidence_id: ladder-interpro
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/I7LY02/
  locator: Integrated InterPro entries for I7LY02
  accessed_at: '2026-10-20T04:01:48.149997Z'
  support: context_only
  summary: The native endpoint returned HTTP204. This bounded absence of an integrated
    entry is not taxonomic absence of the structure.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: bc-emdb42781
  kind: authority
  reference: https://www.ebi.ac.uk/emdb/api/entry/EMD-42781
  locator: Admin title/status/authors, source taxon and primary citation
  accessed_at: '2026-10-20T04:10:08.231265Z'
  support: supports
  summary: The released entry’s title, source taxon and primary citation match the
    record’s region, genotype and focused-reconstruction description. The42781 title
    typo is corrected by native natural-source metadata.
  snapshot_sha256: 053e4afb7dd053cb62e970365d8621ef245c76468d4a53722b9f87dc44980507
- evidence_id: bc-emdb42777
  kind: authority
  reference: https://www.ebi.ac.uk/emdb/api/entry/EMD-42777
  locator: Admin title/status/authors, source taxon and primary citation
  accessed_at: '2026-10-20T04:10:08.302928Z'
  support: supports
  summary: The released entry’s title, source taxon and primary citation match the
    record’s region, genotype and focused-reconstruction description. The42781 title
    typo is corrected by native natural-source metadata.
  snapshot_sha256: b36e20e7da7684fcfa2488cf6c2f7d9ec95ef267ee3c56360b17711fe5d8ef73
- evidence_id: bc-emdb42783
  kind: authority
  reference: https://www.ebi.ac.uk/emdb/api/entry/EMD-42783
  locator: Admin title/status/authors, source taxon and primary citation
  accessed_at: '2026-10-20T04:10:08.332600Z'
  support: supports
  summary: The released entry’s title, source taxon and primary citation match the
    record’s region, genotype and focused-reconstruction description. The42781 title
    typo is corrected by native natural-source metadata.
  snapshot_sha256: cea865ab741c1e83593e0d9c28107629365b67822b007e31440cf40089af991e
- evidence_id: bc-emdb42784
  kind: authority
  reference: https://www.ebi.ac.uk/emdb/api/entry/EMD-42784
  locator: Admin title/status/authors, source taxon and primary citation
  accessed_at: '2026-10-20T04:10:08.365667Z'
  support: supports
  summary: The released entry’s title, source taxon and primary citation match the
    record’s region, genotype and focused-reconstruction description. The42781 title
    typo is corrected by native natural-source metadata.
  snapshot_sha256: 12fcfa6e95cbdd54fa8d6a9ee96b9e694efca702ad58b1c021326ca595f897f4
- evidence_id: bc-emdb53982
  kind: authority
  reference: https://www.ebi.ac.uk/emdb/api/entry/EMD-53982
  locator: Admin title/status/authors, source taxon and primary citation
  accessed_at: '2026-10-20T04:10:09.055238Z'
  support: supports
  summary: The released entry’s title, source taxon and primary citation match the
    record’s region, genotype and focused-reconstruction description. The42781 title
    typo is corrected by native natural-source metadata.
  snapshot_sha256: d8d3d93ead3f0fc432948edb33d72cfce9adec84d875fe2224ecec6e0ce7f3cc
- evidence_id: bc-emdb53983
  kind: authority
  reference: https://www.ebi.ac.uk/emdb/api/entry/EMD-53983
  locator: Admin title/status/authors, source taxon and primary citation
  accessed_at: '2026-10-20T04:10:09.099730Z'
  support: supports
  summary: The released entry’s title, source taxon and primary citation match the
    record’s region, genotype and focused-reconstruction description. The42781 title
    typo is corrected by native natural-source metadata.
  snapshot_sha256: c809200023c59f35b07592452a71f08b9dc3e2179e2e022ba7398e68d34130d3
- evidence_id: basal-emdb46438
  kind: authority
  reference: https://www.ebi.ac.uk/emdb/api/entry/EMD-46438
  locator: Entry title and source
  accessed_at: '2026-10-20T04:01:48.162691Z'
  support: supports
  summary: The native title says proximal B-C, confirming the retained discrepancy
    with the Li2025 table.
  snapshot_sha256: 11925ad540168876c8c998de753acdaab8447261fec3d279d7f0b0e6bb6a0dae
- evidence_id: bc-image
  kind: authority
  reference: https://ftp.ebi.ac.uk/pub/databases/emdb/structures/EMD-42781/images/emd_42781.png
  locator: Complete PNG, byte comparison and visual inspection
  accessed_at: '2026-10-20T04:10:07.509702Z'
  support: supports
  summary: Source PNG and maintained image both have SHA256df7ed8e6da1d20a19522b82a1c2b0afc590de9c802972628beb22fabd0951860.
    Visual inspection confirms an unlabeled density rendering without a scale bar.
  snapshot_sha256: df7ed8e6da1d20a19522b82a1c2b0afc590de9c802972628beb22fabd0951860
- evidence_id: basal-policy
  kind: authority
  reference: https://www.ebi.ac.uk/emdb/policies.html
  locator: Section3.1.2
  accessed_at: '2026-10-20T04:01:05.425069Z'
  support: supports
  summary: EMDB policy3.1.2 requires representative figures free of copyright restrictions;
    the record explicitly states its licence convention.
  snapshot_sha256: 20723befa3d18968826e22b70ae9c6679c4b41cdf6bb08b6001f0b412c281a00
- evidence_id: bc-ruehle-fig2
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC11094743.1/JCB_202311104_Fig2.jpg
  locator: Complete primary figure
  accessed_at: '2026-10-20T06:53:11.515329Z'
  support: supports
  summary: Figure visually inspected for the claimed density assignments, mutant/core
    distinctions and unresolved MIP9 interpretation.
  snapshot_sha256: f69ad0192c513abdff855fd41910456e1a5d155929f1255ee5b1d30b387956b9
- evidence_id: bc-ruehle-s4
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC11094743.1/JCB_202311104_FigS4.jpg
  locator: Complete primary figure
  accessed_at: '2026-10-20T06:53:03.130453Z'
  support: supports
  summary: Figure visually inspected for the claimed density assignments, mutant/core
    distinctions and unresolved MIP9 interpretation.
  snapshot_sha256: 42e976b5b9736701455fc99fe5527786ba95b7cee16c53523242ef0c3dea7714
- evidence_id: bc-li-fig2
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6384029.1/elife-43434-fig2.jpg
  locator: Complete primary figure
  accessed_at: '2026-10-20T06:53:09.065225Z'
  support: supports
  summary: Figure visually inspected for the claimed density assignments, mutant/core
    distinctions and unresolved MIP9 interpretation.
  snapshot_sha256: 9be52fd2803806b6eba0a9907365734ffef10776ceae64386b31f566479bcecb
- evidence_id: bc-li-s12
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6384029.1/elife-43434-fig2-figsupp12.jpg
  locator: Complete primary figure
  accessed_at: '2026-10-20T06:53:03.519740Z'
  support: supports
  summary: Figure visually inspected for the claimed density assignments, mutant/core
    distinctions and unresolved MIP9 interpretation.
  snapshot_sha256: 0ed217ca26c4b4d44616b3d1e8534d1aef5333caeb5c153ac38080de3f5dab93
- evidence_id: basal-cai-fig4
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC12506977.1/sciadv.ady3689-f4.jpg
  locator: Figure4A-C; visual inspection
  accessed_at: '2026-10-20T04:02:19.314075Z'
  support: supports
  summary: Figure4A-C distinguishes the POC1 bridge, I7LY02 ladder and unassigned
    WD40 density at the proximal B-C interface.
  snapshot_sha256: 1db3325f905ae3d30234a23b6184ebfac416f2b1fd56a63ca9e84c63c1094fd7
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/basal_body_b_c_inner_junction.yaml
  locator: Entire target, two components, one example, four edges, six datasets, discussions
    and image
  accessed_at: '2026-10-20T06:54:32Z'
  support: context_only
  summary: The scientific claims preserve regional, species, genotype and model-fitting
    scope. The POC1 example inaccurately calls a UniProt ORF identifier a primary
    gene name.
- evidence_id: local-id
  kind: record_content
  reference: data/structures/cytoskeleton/basal_body_b_c_inner_junction.yaml
  locator: Hidden/ignored-inclusive exact-identifier rg across data/structures
  accessed_at: '2026-10-20T06:54:32Z'
  support: context_only
  summary: Only the target declares this local identifier; its local namespace is
    not an externally resolvable accession.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/basal_body_b_c_inner_junction.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-20T04:09:57Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/basal_body_b_c_inner_junction.yaml'
  snapshot_sha256: b738506f24b8387c78bc6156dfd5e80bded2db895bb2f52d456051dbc69dda21
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/basal_body_b_c_inner_junction.yaml
    --out /private/tmp/cellstructure-batch4-20261019-QtBQNE/basal_body_b_c_inner_junction-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-20T04:09:59Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/basal_body_b_c_inner_junction.yaml\
    \ --out /private/tmp/cellstructure-batch4-20261019-QtBQNE/basal_body_b_c_inner_junction-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch4-20261019-QtBQNE/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch4-20261019-QtBQNE/basal_body_b_c_inner_junction-strict.tsv"
  snapshot_sha256: ef51679507d2966a9987d9c8e522cc6c2305c468c388f867920f90e0bcd74f37
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/basal_body_b_c_inner_junction.yaml; exact
    collect() scope
  accessed_at: '2026-10-20T06:54:32Z'
  support: supports
  summary: '11 of19 collected target identifiers returned OK at the unchanged base.
    Residuals: EMDB:EMD-42777: SKIPPED; resolved by evidence bc-emdb42777; EMDB:EMD-42781:
    SKIPPED; resolved by evidence bc-emdb42781; EMDB:EMD-42783: SKIPPED; resolved
    by evidence bc-emdb42783; EMDB:EMD-42784: SKIPPED; resolved by evidence bc-emdb42784;
    EMDB:EMD-53982: SKIPPED; resolved by evidence bc-emdb53982; EMDB:EMD-53983: SKIPPED;
    resolved by evidence bc-emdb53983; PMID:20008567: UNREACHABLE; resolved by evidence
    basal-epmc; cellstructuremech:basal_body_b_c_inner_junction: SKIPPED; resolved
    by evidence local-id. Source-native identity checked separately.'
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
  topic: B-C protein network
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_b_c_inner_junction
  summary: The named multiprotein interface is distinct from A-B, the outer junction,
    A-C linker and inner scaffold. Parent and parthood are appropriate.
  evidence_ids:
  - basal-go
  - bc-ruehle
  - bc-li2019
  - basal-cai
  - record
- assessment_id: composition
  area: evidence
  topic: Proximal components and unknown core
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_b_c_inner_junction
  summary: POC1 and I7LY02 have source-supported proximal assignments at the stated
    evidence levels. Core bridging proteins and the additional proximal WD40 density
    remain unassigned, with no forced equivalence between species.
  evidence_ids:
  - bc-ruehle
  - bc-li2019
  - basal-cai
  - basal-pdb9qzc8
  - record
- assessment_id: examples
  area: provenance
  topic: POC1 accession versus gene-name field
  outcome: concern
  target_ids:
  - cellstructuremech:basal_body_b_c_inner_junction
  summary: The accession itself is directly supported as Poc1 by Ruehle’s model-fitting
    Results. UniProt lists the TTHERM identifier as an ORF name, not a primary name;
    this is a nonblocking wording/source-attribution defect.
  evidence_ids:
  - basal-proteins
  - bc-ruehle
  - basal-poc1-paper
  - record
- assessment_id: families
  area: grounding
  topic: Label-only classes
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_b_c_inner_junction
  summary: The broader family and domain/repeat annotations do not justify exact class
    grounding. The ladder’s integrated-entry no-match remains bounded.
  evidence_ids:
  - basal-IPR050505
  - basal-IPR020472
  - basal-IPR056551
  - basal-proteins
  - ladder-interpro
  - record
- assessment_id: scope
  area: scope
  topic: Two species and regional maturity
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_b_c_inner_junction
  summary: Tetrahymena proximal/core and wild-type/mutant observations remain distinct.
    Chlamydomonas pooled mother/procentriole averages are correctly described. Reference
    sequences are not silently paired with experimental strains.
  evidence_ids:
  - outer-junction-taxa
  - sheath-taxon
  - bc-ruehle
  - bc-li2019
  - basal-cai
  - basal-proteins
  - record
- assessment_id: function
  area: evidence
  topic: Structural connection
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_b_c_inner_junction
  summary: Sources support luminal B-C connection and core scaffold attachment without
    proving a unique force threshold or attributing all Poc1 phenotypes to this junction.
  evidence_ids:
  - bc-ruehle
  - bc-li2019
  - record
- assessment_id: graph
  area: graph
  topic: Four proximal fitted-model contacts
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_b_c_inner_junction
  summary: POC1 contacts B08/C10 and the ladder contacts B07/C10 in Cai Figure4. The
    graph explicitly describes structural-model contacts, not biochemical binding
    or temporal recruitment.
  evidence_ids:
  - basal-cai
  - basal-cai-fig4
  - record
- assessment_id: conflicts
  area: evidence
  topic: Preserved contradictory source details
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_b_c_inner_junction
  summary: The4nm/8nm MIP9 conflict and46438 regional-label conflict are real and
    correctly retained. Neither is silently converted into a record measurement or
    unsupported dataset identity.
  evidence_ids:
  - bc-li2019
  - basal-li
  - basal-emdb46438
  - record
- assessment_id: datasets
  area: provenance
  topic: Six bounded native deposits
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_b_c_inner_junction
  summary: Titles, genotypes, species and citations match the linked reconstructions;
    the focused WD40 map does not identify the unassigned protein.
  evidence_ids:
  - bc-emdb42781
  - bc-emdb42777
  - bc-emdb42783
  - bc-emdb42784
  - bc-emdb53982
  - bc-emdb53983
  - bc-ruehle
  - basal-cai
  - record
- assessment_id: image
  area: evidence
  topic: Hosted representative figure
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_b_c_inner_junction
  summary: The image bytes, depositor attribution, taxonomy, caption and copyright
    policy match the native source. Inspected article figures are not copied into
    the corpus.
  evidence_ids:
  - bc-image
  - basal-policy
  - bc-emdb42781
  - record
- assessment_id: status
  area: completeness
  topic: Open composition and native status
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_b_c_inner_junction
  summary: PROPOSED and the open family/core composition questions are appropriate.
    The record avoids universal stoichiometry, prevalence and essentiality claims.
  evidence_ids:
  - bc-ruehle
  - bc-li2019
  - basal-cai
  - record
findings:
- finding_id: F1
  issue_key: basal-body-b-c-inner-junction-poc1-gene-field
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: POC1 example calls an ORF name a UniProt primary gene name
  description: Q229Z6 provides TTHERM_01308010 in orfNames and no primary geneName.
    Ruehle2024 independently identifies the accession as Poc1. Describe the native
    field accurately and attribute the symbol mapping to the structural source; the
    accession and protein-family assignment are supported.
  target_ids:
  - cellstructuremech:basal_body_b_c_inner_junction
  field_paths:
  - components[component_id=poc1].protein_examples[0].role
  evidence_ids:
  - basal-proteins
  - bc-ruehle
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/basal_body_b_c_inner_junction.yaml
    role: maintained scientific record
  rule_id: review-checklist:Evidence standard and Components
  native_severity: minor
  normalization_reason: The underlying Poc1 accession is supported; inaccurate source-field
    wording is bounded provenance.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - cellstructuremech:basal_body_b_c_inner_junction
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/basal_body_b_c_inner_junction.yaml
    role: maintained scientific record
  description: Call TTHERM_01308010 an ORF/locus name and cite the Ruehle2024 Q229Z6-to-Poc1
    assignment while retaining the reference-strain limitation.
  acceptance_checks:
  - The wording matches UniProt genes.orfNames rather than asserting a primary geneName.
  - The named Poc1 mapping remains traceable to the primary source.
  - After separately authorized curation, run native record/history and generated-page
    checks.
  generator: Maintained YAML; just render derives pages.
limitations:
- Exact core and additional WD40 protein identities remain unresolved.
- The Chlamydomonas density labels do not establish a molecular crosswalk to Tetrahymena
  proteins.
- Conflicting MIP9 repeat and46438 region labels are retained rather than adjudicated
  beyond the available evidence.
- Map volumes were not reprocessed; native metadata, primary interpretations and figures
  were inspected.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- Only the review bundle is saved. Maintained scientific content, native status, history
  and generated pages remain unchanged.
```
