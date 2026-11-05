# Basal-body cartwheel identity, composition and measurement review

- Review: 20261020T065955Z-basal-body-cartwheel-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-20T06:54:48Z
- Finished UTC: 2026-10-20T06:59:55Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Identity, two constituents and protein examples, three microbial specimens, three measurements and the hosted figure are supported. No concrete defect was found in the assessed record.

## Scope And Provenance

Entire maintained record and image; three primary full-text sources, native protein/family/taxon/ontology records and neighboring-deposit metadata.

Selection: Third unreviewed path of batch4.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:basal_body_cartwheel | data/structures/cytoskeleton/basal_body_cartwheel.yaml | maintained | basal body cartwheel |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | cellstructuremech:basal_body_cartwheel | Focused validator passed. |
| Focused native strict | passed | True | cellstructuremech:basal_body_cartwheel | Focused validator passed. |
| Target resolver slice | passed | True | cellstructuremech:basal_body_cartwheel | 15 identifiers OK; 1 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | cellstructuremech:basal_body_cartwheel | No expression-derived membership or matching microbial expression dataset is asserted; primary localization and structural sources establish the evidence. |
| Claim-level scientific review | passed | True | cellstructuremech:basal_body_cartwheel | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | cellstructuremech:basal_body_cartwheel | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | cellstructuremech:basal_body_cartwheel | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | cellstructuremech:basal_body_cartwheel | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | cellstructuremech:basal_body_cartwheel | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | cellstructuremech:basal_body_cartwheel | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Hub-and-spoke assembly

identity: supported. Targets: cellstructuremech:basal_body_cartwheel.

The record denotes a named multiprotein subassembly. Basal and pro-basal bodies are parents by parthood; neighboring densities and the narrower2017 core preparation are distinguished.

### Two supported constituents

evidence: supported. Targets: cellstructuremech:basal_body_cartwheel.

Native localization and reconstitution support SAS-6 and Bld10 membership without claiming a complete proteome or resolving all density assignments. Null-mutant phenotypes are not treated as selective cartwheel loss.

### Native protein identities

provenance: supported. Targets: cellstructuremech:basal_body_cartwheel.

Both taxon-paired examples match native names, gene symbols and reviewed status; BLD12 nomenclature is explicit in the2017 source.

### Conservative class grounding

grounding: supported. Targets: cellstructuremech:basal_body_cartwheel.

SAS-6 search matches are domains/superfamilies. Reviewed CEP135 and TSGA10 both map to the proposed broader family, so neither component is overgrounded.

### Three scoped specimens

scope: supported. Targets: cellstructuremech:basal_body_cartwheel.

The2020 sample Methods support mat3-4 Chlamydomonas, isolated Paramecium d4-2/delta-CenBP1 cortical units and differentiated Naegleria NEG flagellates, including preparation damage limits.

### Three source-specific numerical fields

evidence: supported. Targets: cellstructuremech:basal_body_cartwheel.

The2017 hub diameter and2020 mature Chlamydomonas hub/CID spacings match captions, sample counts and uncertainty labels. They are not recast as whole-cartwheel size, universal repeat or kinetic data.

### Radial scaffold

evidence: supported. Targets: cellstructuremech:basal_body_cartwheel.

Native morphology supports the grounded organization role. The source limits make a kinetic graph or universal essentiality assertion unwarranted; neither is supplied.

### Explicit open molecular follow-up

completeness: supported. Targets: cellstructuremech:basal_body_cartwheel.

The2026 source is explicitly context only, with no model or deposit claims adopted. Existing claims are supported by the inspected2017/2020 sources; the follow-up remains unassessed full text.

### Neighboring reconstructions

provenance: supported. Targets: cellstructuremech:basal_body_cartwheel.

The four neighboring deposits do not describe an isolated cartwheel; the record correctly avoids treating them as exact datasets.

### Native figure and licence

evidence: supported. Targets: cellstructuremech:basal_body_cartwheel.

The image bytes, graphic panel labels, species, processed-view qualification and CCBY4.0 provenance match the inspected source.

### Qualified proposed record

completeness: supported. Targets: cellstructuremech:basal_body_cartwheel.

The open family and molecular questions are acknowledged scientific limits, not invented missing required facts. PROPOSED status is appropriate.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| tusk-paper | https://pmc-oa-opendata.s3.amazonaws.com/PMC7667884.1/PMC7667884.1.xml; Cartwheel Results, Figure1 caption, Discussion and sample Methods | supports | Native cartwheels, hub/CID measurements and species-specific organization are directly described. Discussion treats SAS-5 and precise density assignments as hypotheses and distinguishes static polarity from assembly chronology. |
| cartwheel-guichard | https://pmc-oa-opendata.s3.amazonaws.com/PMC5376648.1/PMC5376648.1.xml; Results, Discussion, Figure1/2 captions and Introduction BLD12 nomenclature | supports | Native core morphology and Bld10/SAS-6 localization support membership. Reconstitution distinguishes full-length protein plus fragment from truncated arrays; height distributions support a model rather than live chronology. Hub diameter22.4±1.3nm is measured10 times across5tomograms; the caption does not name the error statistic. |
| cartwheel-matsuura | https://pmc-oa-opendata.s3.amazonaws.com/PMC2172387.1/PMC2172387.1.xml; Localization Results, Figure7 and Discussion | supports | Immunogold localizes Bld10 to cartwheel radial fibers in basal and pro-basal bodies. Null-mutant loss is broader than a cartwheel-specific phenotype. |
| cartwheel-proteins | https://rest.uniprot.org/uniprotkb/search?query=accession:A9CQL4%20OR%20accession:A8ID55&amp;format=json; Both native entries: names, genes, organisms, status and references | supports | A9CQL4 is unreviewed Chlamydomonas CrSAS-6 with submitted name Centriole protein; A8ID55 is reviewed BLD10 Basal body protein10. The SAS-6 sequence reference identifies the original study. |
| cartwheel-sas6-search | https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=SAS-6&amp;page_size=200; Full native search response | supports | All six returned SAS-6 matches are domains or domain homologous superfamilies; next is null. No exact whole-protein family is established by this bounded search. |
| cartwheel-IPR051877 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051877; Native type/name fields | supports | The entry is a family, but the broader membership is established independently using reviewed sequence entries rather than its unchecked generated description. |
| cartwheel-human-paralogs | https://rest.uniprot.org/uniprotkb/search?query=(gene_exact:CEP135%20OR%20gene_exact:TSGA10)%20AND%20organism_id:9606%20AND%20reviewed:true&amp;format=json; Both reviewed entries; genes and InterPro cross-references | supports | Reviewed human CEP135 Q66GS9 and TSGA10 Q9BZW7 both cross-reference IPR051877, confirming that it is broader than Bld10/Cep135. |
| cartwheel-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032991,GO:0036064,GO:0120280,GO:0032053; Exact GO definitions | supports | The three hierarchy terms and basal-body organization function are active with matching meanings. |
| cartwheel-cartwheel-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=cartwheel&amp;limit=100; Native search response | supports | The exact cartwheel query returned no GO search matches. This bounded native search supports retaining the local identity, not an exhaustive ontology absence claim. |
| cartwheel-taxon | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=5762; Taxon name and rank | supports | NCBITaxon5762 is Naegleria gruberi at species rank. |
| tusk-taxon | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=5888; Taxon identity | supports | NCBITaxon5888 identifies Paramecium tetraurelia. |
| sheath-taxon | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=3055; Taxon identity | supports | NCBITaxon3055 identifies Chlamydomonas reinhardtii. |
| cartwheel-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1038/ncomms14813%20OR%20DOI:10.1083/jcb.200402022%20OR%20DOI:10.1073/pnas.2612170123&amp;format=json&amp;resultType=core; Exact publication metadata and2026 abstract | supports | The2017 and2004 source identities match their DOI/PMID pairs. The2026 Trichonympha publication identity and abstract are verified as context only; its full molecular model is not assessed or adopted. |
| tusk-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.15252/embj.2020106246&amp;format=json&amp;resultType=core; Exact article metadata | supports | PMID32954513 and the2020 DOI identify the same architectural study. |
| tusk-uo | https://www.ebi.ac.uk/ols4/api/ontologies/uo/terms?obo_id=UO:0000018; Native unit definition | supports | UO0000018 denotes nanometer. |
| cartwheel-figure1 | https://pmc-oa-opendata.s3.amazonaws.com/PMC7667884.1/EMBJ-39-e106246-g002.jpg; Complete Figure1 graphic, byte comparison and visual inspection | supports | Source and maintained image have identical SHA256c25cd15b6042c4631df0e30c2ce5bfa6e7b2fca1467bd035aec57879ddef7453. Visual inspection confirms G cross sections, H spacing plot and I-J serial projections, consistent with the curated caption. |
| cartwheel-guichard-fig1 | https://pmc-oa-opendata.s3.amazonaws.com/PMC5376648.1/ncomms14813-f1.jpg; Complete Figure1 visually inspected | supports | Figure1 distinguishes hub from D1/D2 and graphically labels the hub22.4nm. |
| tusk-paper-meta | https://pmc-oa-opendata.s3.amazonaws.com/PMC7667884.1/PMC7667884.1.json; Media MD5 and article licence metadata | supports | Official PMC media metadata checksum matches the figure; article JATS gives the explicit CCBY4.0 licence. |
| tusk-emdb10726 | https://www.ebi.ac.uk/emdb/api/entry/EMD-10726; Native title, source and primary citation | supports | Native title and citation describe a Paramecium linker or triplet reconstruction, supporting exclusion as an exact isolated-cartwheel dataset. |
| tusk-emdb10727 | https://www.ebi.ac.uk/emdb/api/entry/EMD-10727; Native title, source and primary citation | supports | Native title and citation describe a Paramecium linker or triplet reconstruction, supporting exclusion as an exact isolated-cartwheel dataset. |
| tusk-emdb10728 | https://www.ebi.ac.uk/emdb/api/entry/EMD-10728; Native title, source and primary citation | supports | Native title and citation describe a Paramecium linker or triplet reconstruction, supporting exclusion as an exact isolated-cartwheel dataset. |
| tusk-emdb10729 | https://www.ebi.ac.uk/emdb/api/entry/EMD-10729; Native title, source and primary citation | supports | Native title and citation describe a Paramecium linker or triplet reconstruction, supporting exclusion as an exact isolated-cartwheel dataset. |
| record | data/structures/cytoskeleton/basal_body_cartwheel.yaml; Entire target and maintained image | context_only | The record maintains source-specific measurements, three microbial examples, two components and explicit model/deposition limitations. No causal chronology or fixed stoichiometry is asserted. |
| local-id | data/structures/cytoskeleton/basal_body_cartwheel.yaml; Exact identifier search across data/structures including hidden and ignored files | context_only | The exact local identifier is declared by this target; a locally minted structural identity is not an external accession. |
| schema-result | just validate data/structures/cytoskeleton/basal_body_cartwheel.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/basal_body_cartwheel.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/basal_body_cartwheel.yaml --out /private/tmp/cellstructure-batch4-20261019-QtBQNE/basal_body_cartwheel-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/basal_body_cartwheel.yaml --out /private/tmp/cellstructure-batch4-20261019-QtBQNE/basal_body_cartwheel-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch4-20261019-QtBQNE/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch4-20261019-QtBQNE/basal_body_cartwheel-strict.tsv |
| target-curies | just check-curies-strict; data/structures/cytoskeleton/basal_body_cartwheel.yaml; exact collect() scope | supports | 15 of16 collected target identifiers returned OK at the unchanged base. Residuals: cellstructuremech:basal_body_cartwheel: SKIPPED; resolved by evidence local-id. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- The2026 Trichonympha paper was checked at metadata/abstract level only, as an explicitly excluded molecular follow-up; its full model remains unassessed.
- Full native composition, exact whole-protein family grounding and universal stoichiometry remain unresolved.
- Map volumes were not reprocessed. Static architecture and reconstitution models do not establish a live assembly time course.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Only the review bundle is saved. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T065955Z-basal-body-cartwheel-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Basal-body cartwheel identity, composition and measurement review
started_at: '2026-10-20T06:54:48Z'
finished_at: '2026-10-20T06:59:55Z'
reviewer:
  identity: Codex
  kind: agent
  independence: unknown
  independence_basis: Current source review does not establish independent historical
    authorship.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Identity, two constituents and protein examples, three microbial specimens,
  three measurements and the hosted figure are supported. No concrete defect was found
  in the assessed record.
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
  - path: data/images/cytoskeleton/basal_body_cartwheel/pmc7667884_embj2020106246_fig_0001.jpg
    sha256: c25cd15b6042c4631df0e30c2ce5bfa6e7b2fca1467bd035aec57879ddef7453
    role: context
  - path: data/structures/cytoskeleton/basal_body_cartwheel.yaml
    sha256: ad4e6fcf7639e0fffc00b553b0ab2e0e2a8eac5981b87ae9da1ee783ba942957
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
- target_id: cellstructuremech:basal_body_cartwheel
  path: data/structures/cytoskeleton/basal_body_cartwheel.yaml
  label: basal body cartwheel
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/basal_body_cartwheel.yaml
    role: maintained scientific record
scope:
  description: Entire maintained record and image; three primary full-text sources,
    native protein/family/taxon/ontology records and neighboring-deposit metadata.
  selection: Third unreviewed path of batch4.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:basal_body_cartwheel
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_cartwheel
  command: just validate data/structures/cytoskeleton/basal_body_cartwheel.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_cartwheel
  command: just validate-strict data/structures/cytoskeleton/basal_body_cartwheel.yaml
    --out /private/tmp/cellstructure-batch4-20261019-QtBQNE/basal_body_cartwheel-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_cartwheel
  summary: 15 identifiers OK; 1 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - local-id
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - cellstructuremech:basal_body_cartwheel
  summary: No expression-derived membership or matching microbial expression dataset
    is asserted; primary localization and structural sources establish the evidence.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_cartwheel
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - tusk-paper
  - cartwheel-guichard
  - cartwheel-matsuura
  - cartwheel-proteins
  - cartwheel-sas6-search
  - cartwheel-IPR051877
  - cartwheel-human-paralogs
  - cartwheel-go
  - cartwheel-cartwheel-search
  - cartwheel-taxon
  - tusk-taxon
  - sheath-taxon
  - cartwheel-epmc
  - tusk-epmc
  - tusk-uo
  - cartwheel-figure1
  - cartwheel-guichard-fig1
  - tusk-paper-meta
  - tusk-emdb10726
  - tusk-emdb10727
  - tusk-emdb10728
  - tusk-emdb10729
  - record
  - local-id
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_cartwheel
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
  - cellstructuremech:basal_body_cartwheel
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
  - cellstructuremech:basal_body_cartwheel
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
  - cellstructuremech:basal_body_cartwheel
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
  - cellstructuremech:basal_body_cartwheel
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
- evidence_id: tusk-paper
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC7667884.1/PMC7667884.1.xml
  locator: Cartwheel Results, Figure1 caption, Discussion and sample Methods
  accessed_at: '2026-10-20T04:07:36.772127Z'
  support: supports
  summary: Native cartwheels, hub/CID measurements and species-specific organization
    are directly described. Discussion treats SAS-5 and precise density assignments
    as hypotheses and distinguishes static polarity from assembly chronology.
  snapshot_sha256: 5116fa9428a3a69c7a3baca7e80ad82dc6d050ed8db9d88b37982136407d6184
- evidence_id: cartwheel-guichard
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5376648.1/PMC5376648.1.xml
  locator: Results, Discussion, Figure1/2 captions and Introduction BLD12 nomenclature
  accessed_at: '2026-10-20T06:55:12.312759Z'
  support: supports
  summary: Native core morphology and Bld10/SAS-6 localization support membership.
    Reconstitution distinguishes full-length protein plus fragment from truncated
    arrays; height distributions support a model rather than live chronology. Hub
    diameter22.4±1.3nm is measured10 times across5tomograms; the caption does not
    name the error statistic.
  snapshot_sha256: 34c181266963f3a0f4a7a5839a5fefe950e2213b324b1dcb058340d17d46f8a9
- evidence_id: cartwheel-matsuura
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2172387.1/PMC2172387.1.xml
  locator: Localization Results, Figure7 and Discussion
  accessed_at: '2026-10-20T06:55:15.198279Z'
  support: supports
  summary: Immunogold localizes Bld10 to cartwheel radial fibers in basal and pro-basal
    bodies. Null-mutant loss is broader than a cartwheel-specific phenotype.
  snapshot_sha256: 5c397de0020904b247df8e98a8eb23868406edc6ba37172c44b983e5a45a0632
- evidence_id: cartwheel-proteins
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?query=accession:A9CQL4%20OR%20accession:A8ID55&format=json
  locator: 'Both native entries: names, genes, organisms, status and references'
  accessed_at: '2026-10-20T06:55:14.426725Z'
  support: supports
  summary: A9CQL4 is unreviewed Chlamydomonas CrSAS-6 with submitted name Centriole
    protein; A8ID55 is reviewed BLD10 Basal body protein10. The SAS-6 sequence reference
    identifies the original study.
  snapshot_sha256: 8a56b3bb6260c7af9fc0ef791ac0c2ae82c459f81c9dd18a24b174d15bce65fe
- evidence_id: cartwheel-sas6-search
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=SAS-6&page_size=200
  locator: Full native search response
  accessed_at: '2026-10-20T06:55:15.367712Z'
  support: supports
  summary: All six returned SAS-6 matches are domains or domain homologous superfamilies;
    next is null. No exact whole-protein family is established by this bounded search.
  snapshot_sha256: fce60aba70b506a318791f4351c3a7b20bdd83b860b4d002f11c61564cfb60bf
- evidence_id: cartwheel-IPR051877
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051877
  locator: Native type/name fields
  accessed_at: '2026-10-20T06:55:13.619866Z'
  support: supports
  summary: The entry is a family, but the broader membership is established independently
    using reviewed sequence entries rather than its unchecked generated description.
  snapshot_sha256: ef5b481674874d1e56d39f6808f575fbee42919f894ad36b3aef1ea0d1b1645e
- evidence_id: cartwheel-human-paralogs
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?query=(gene_exact:CEP135%20OR%20gene_exact:TSGA10)%20AND%20organism_id:9606%20AND%20reviewed:true&format=json
  locator: Both reviewed entries; genes and InterPro cross-references
  accessed_at: '2026-10-20T06:56:05.105046Z'
  support: supports
  summary: Reviewed human CEP135 Q66GS9 and TSGA10 Q9BZW7 both cross-reference IPR051877,
    confirming that it is broader than Bld10/Cep135.
  snapshot_sha256: 0796a565c2224aaea2b8c6b1cc1311b2f8d561cae1c21876707f430e8bb8fcd8
- evidence_id: cartwheel-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032991,GO:0036064,GO:0120280,GO:0032053
  locator: Exact GO definitions
  accessed_at: '2026-10-20T06:55:12.197440Z'
  support: supports
  summary: The three hierarchy terms and basal-body organization function are active
    with matching meanings.
  snapshot_sha256: 3b763f8154d823f7eb174cd748438843c3ed9723272033a93957a481877a3316
- evidence_id: cartwheel-cartwheel-search
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=cartwheel&limit=100
  locator: Native search response
  accessed_at: '2026-10-20T06:55:16.021017Z'
  support: supports
  summary: The exact cartwheel query returned no GO search matches. This bounded native
    search supports retaining the local identity, not an exhaustive ontology absence
    claim.
  snapshot_sha256: f3a7dae9b1e9335291e3940cdf0e5f8dadf9335da7b9547710606b5106c63f86
- evidence_id: cartwheel-taxon
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=5762
  locator: Taxon name and rank
  accessed_at: '2026-10-20T06:55:12.769665Z'
  support: supports
  summary: NCBITaxon5762 is Naegleria gruberi at species rank.
  snapshot_sha256: e8bbe4d5488d28b2d48e10a08a246e676765cabef625e087e24b8f1af67abce1
- evidence_id: tusk-taxon
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=5888
  locator: Taxon identity
  accessed_at: '2026-10-20T04:07:36.781682Z'
  support: supports
  summary: NCBITaxon5888 identifies Paramecium tetraurelia.
  snapshot_sha256: 596cc922f484502eb5c3608ed45943d1486fb9b2e620d7805a76f2984ec0ad6b
- evidence_id: sheath-taxon
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=3055
  locator: Taxon identity
  accessed_at: '2026-10-20T03:38:20.199537Z'
  support: supports
  summary: NCBITaxon3055 identifies Chlamydomonas reinhardtii.
  snapshot_sha256: a17bc1c97fea9112288574ef15727ed7e37c42787a430ef074ae5fc654547e6b
- evidence_id: cartwheel-epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1038/ncomms14813%20OR%20DOI:10.1083/jcb.200402022%20OR%20DOI:10.1073/pnas.2612170123&format=json&resultType=core
  locator: Exact publication metadata and2026 abstract
  accessed_at: '2026-10-20T06:55:11.189899Z'
  support: supports
  summary: The2017 and2004 source identities match their DOI/PMID pairs. The2026 Trichonympha
    publication identity and abstract are verified as context only; its full molecular
    model is not assessed or adopted.
  snapshot_sha256: d5fbeff1379410a18b63a9c2fe024b585b812f25a57681288616fa5f13656dd9
- evidence_id: tusk-epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.15252/embj.2020106246&format=json&resultType=core
  locator: Exact article metadata
  accessed_at: '2026-10-20T04:07:37.473964Z'
  support: supports
  summary: PMID32954513 and the2020 DOI identify the same architectural study.
  snapshot_sha256: fc5be273d2b5b8a6a8e0508133e82627d15be3c057345cafce1b51fd4fb1c685
- evidence_id: tusk-uo
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uo/terms?obo_id=UO:0000018
  locator: Native unit definition
  accessed_at: '2026-10-20T04:07:37.417486Z'
  support: supports
  summary: UO0000018 denotes nanometer.
  snapshot_sha256: 4c7db9c8cb664724cfeb7ded951492cac50dd7c8bdc275363486b3e34df94bf8
- evidence_id: cartwheel-figure1
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC7667884.1/EMBJ-39-e106246-g002.jpg
  locator: Complete Figure1 graphic, byte comparison and visual inspection
  accessed_at: '2026-10-20T06:55:14.977499Z'
  support: supports
  summary: Source and maintained image have identical SHA256c25cd15b6042c4631df0e30c2ce5bfa6e7b2fca1467bd035aec57879ddef7453.
    Visual inspection confirms G cross sections, H spacing plot and I-J serial projections,
    consistent with the curated caption.
  snapshot_sha256: c25cd15b6042c4631df0e30c2ce5bfa6e7b2fca1467bd035aec57879ddef7453
- evidence_id: cartwheel-guichard-fig1
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5376648.1/ncomms14813-f1.jpg
  locator: Complete Figure1 visually inspected
  accessed_at: '2026-10-20T06:56:05.021744Z'
  support: supports
  summary: Figure1 distinguishes hub from D1/D2 and graphically labels the hub22.4nm.
  snapshot_sha256: 50a63f5c43b225e40950c425b3c32b6c8e728c051a543a2d0277d898ee5712da
- evidence_id: tusk-paper-meta
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC7667884.1/PMC7667884.1.json
  locator: Media MD5 and article licence metadata
  accessed_at: '2026-10-20T04:07:36.562450Z'
  support: supports
  summary: Official PMC media metadata checksum matches the figure; article JATS gives
    the explicit CCBY4.0 licence.
  snapshot_sha256: 0ec250e461c0b021eff66c3668b7b0dc5701968e9102faeabd16bfa5e902c65b
- evidence_id: tusk-emdb10726
  kind: authority
  reference: https://www.ebi.ac.uk/emdb/api/entry/EMD-10726
  locator: Native title, source and primary citation
  accessed_at: '2026-10-20T04:07:37.620588Z'
  support: supports
  summary: Native title and citation describe a Paramecium linker or triplet reconstruction,
    supporting exclusion as an exact isolated-cartwheel dataset.
  snapshot_sha256: 58cebaeacbb0aa96022d51cc2e575167dbc7b53c9d1f1473a8cc5fe2ebac19d4
- evidence_id: tusk-emdb10727
  kind: authority
  reference: https://www.ebi.ac.uk/emdb/api/entry/EMD-10727
  locator: Native title, source and primary citation
  accessed_at: '2026-10-20T04:07:38.078163Z'
  support: supports
  summary: Native title and citation describe a Paramecium linker or triplet reconstruction,
    supporting exclusion as an exact isolated-cartwheel dataset.
  snapshot_sha256: 6fb33d249a0bed05c662904d275357c2352d338887a56427b11bb166c7bffab9
- evidence_id: tusk-emdb10728
  kind: authority
  reference: https://www.ebi.ac.uk/emdb/api/entry/EMD-10728
  locator: Native title, source and primary citation
  accessed_at: '2026-10-20T04:07:38.108046Z'
  support: supports
  summary: Native title and citation describe a Paramecium linker or triplet reconstruction,
    supporting exclusion as an exact isolated-cartwheel dataset.
  snapshot_sha256: 720aaa30a6a1551795a4bc2c314ae33df53be46e29e411a3b441d9b097cb5dc3
- evidence_id: tusk-emdb10729
  kind: authority
  reference: https://www.ebi.ac.uk/emdb/api/entry/EMD-10729
  locator: Native title, source and primary citation
  accessed_at: '2026-10-20T04:07:38.169902Z'
  support: supports
  summary: Native title and citation describe a Paramecium linker or triplet reconstruction,
    supporting exclusion as an exact isolated-cartwheel dataset.
  snapshot_sha256: 29cd3ebac1c41715ca0bfa7254842b6ce3b5e591e1dd9b9c165607eba2a8032d
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/basal_body_cartwheel.yaml
  locator: Entire target and maintained image
  accessed_at: '2026-10-20T06:59:54Z'
  support: context_only
  summary: The record maintains source-specific measurements, three microbial examples,
    two components and explicit model/deposition limitations. No causal chronology
    or fixed stoichiometry is asserted.
- evidence_id: local-id
  kind: record_content
  reference: data/structures/cytoskeleton/basal_body_cartwheel.yaml
  locator: Exact identifier search across data/structures including hidden and ignored
    files
  accessed_at: '2026-10-20T06:59:54Z'
  support: context_only
  summary: The exact local identifier is declared by this target; a locally minted
    structural identity is not an external accession.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/basal_body_cartwheel.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-20T06:54:49Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/basal_body_cartwheel.yaml'
  snapshot_sha256: f7b1918ab8c792520feeccda3fbee56109f3a93b7a0f88a81d2b80e2ab32422c
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/basal_body_cartwheel.yaml
    --out /private/tmp/cellstructure-batch4-20261019-QtBQNE/basal_body_cartwheel-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-20T06:54:50Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/basal_body_cartwheel.yaml\
    \ --out /private/tmp/cellstructure-batch4-20261019-QtBQNE/basal_body_cartwheel-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch4-20261019-QtBQNE/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch4-20261019-QtBQNE/basal_body_cartwheel-strict.tsv"
  snapshot_sha256: 356374e00613d0822d1b7b32403ffb81d49764c7300c072773161f82379c6746
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/basal_body_cartwheel.yaml; exact collect()
    scope
  accessed_at: '2026-10-20T06:59:54Z'
  support: supports
  summary: '15 of16 collected target identifiers returned OK at the unchanged base.
    Residuals: cellstructuremech:basal_body_cartwheel: SKIPPED; resolved by evidence
    local-id. Source-native identity checked separately.'
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
  topic: Hub-and-spoke assembly
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_cartwheel
  summary: The record denotes a named multiprotein subassembly. Basal and pro-basal
    bodies are parents by parthood; neighboring densities and the narrower2017 core
    preparation are distinguished.
  evidence_ids:
  - cartwheel-go
  - cartwheel-cartwheel-search
  - tusk-paper
  - cartwheel-guichard
  - record
- assessment_id: components
  area: evidence
  topic: Two supported constituents
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_cartwheel
  summary: Native localization and reconstitution support SAS-6 and Bld10 membership
    without claiming a complete proteome or resolving all density assignments. Null-mutant
    phenotypes are not treated as selective cartwheel loss.
  evidence_ids:
  - tusk-paper
  - cartwheel-guichard
  - cartwheel-matsuura
  - record
- assessment_id: examples
  area: provenance
  topic: Native protein identities
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_cartwheel
  summary: Both taxon-paired examples match native names, gene symbols and reviewed
    status; BLD12 nomenclature is explicit in the2017 source.
  evidence_ids:
  - cartwheel-proteins
  - cartwheel-guichard
  - sheath-taxon
  - record
- assessment_id: grounding
  area: grounding
  topic: Conservative class grounding
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_cartwheel
  summary: SAS-6 search matches are domains/superfamilies. Reviewed CEP135 and TSGA10
    both map to the proposed broader family, so neither component is overgrounded.
  evidence_ids:
  - cartwheel-sas6-search
  - cartwheel-IPR051877
  - cartwheel-human-paralogs
  - record
- assessment_id: taxa
  area: scope
  topic: Three scoped specimens
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_cartwheel
  summary: The2020 sample Methods support mat3-4 Chlamydomonas, isolated Paramecium
    d4-2/delta-CenBP1 cortical units and differentiated Naegleria NEG flagellates,
    including preparation damage limits.
  evidence_ids:
  - tusk-paper
  - cartwheel-taxon
  - tusk-taxon
  - sheath-taxon
  - record
- assessment_id: measurements
  area: evidence
  topic: Three source-specific numerical fields
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_cartwheel
  summary: The2017 hub diameter and2020 mature Chlamydomonas hub/CID spacings match
    captions, sample counts and uncertainty labels. They are not recast as whole-cartwheel
    size, universal repeat or kinetic data.
  evidence_ids:
  - cartwheel-guichard
  - tusk-paper
  - tusk-uo
  - cartwheel-figure1
  - record
- assessment_id: function
  area: evidence
  topic: Radial scaffold
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_cartwheel
  summary: Native morphology supports the grounded organization role. The source limits
    make a kinetic graph or universal essentiality assertion unwarranted; neither
    is supplied.
  evidence_ids:
  - tusk-paper
  - cartwheel-guichard
  - cartwheel-go
  - record
- assessment_id: followup
  area: completeness
  topic: Explicit open molecular follow-up
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_cartwheel
  summary: The2026 source is explicitly context only, with no model or deposit claims
    adopted. Existing claims are supported by the inspected2017/2020 sources; the
    follow-up remains unassessed full text.
  evidence_ids:
  - cartwheel-epmc
  - tusk-paper
  - cartwheel-guichard
  - record
- assessment_id: deposits
  area: provenance
  topic: Neighboring reconstructions
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_cartwheel
  summary: The four neighboring deposits do not describe an isolated cartwheel; the
    record correctly avoids treating them as exact datasets.
  evidence_ids:
  - tusk-emdb10726
  - tusk-emdb10727
  - tusk-emdb10728
  - tusk-emdb10729
  - record
- assessment_id: image
  area: evidence
  topic: Native figure and licence
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_cartwheel
  summary: The image bytes, graphic panel labels, species, processed-view qualification
    and CCBY4.0 provenance match the inspected source.
  evidence_ids:
  - cartwheel-figure1
  - tusk-paper-meta
  - tusk-paper
  - record
- assessment_id: status
  area: completeness
  topic: Qualified proposed record
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_cartwheel
  summary: The open family and molecular questions are acknowledged scientific limits,
    not invented missing required facts. PROPOSED status is appropriate.
  evidence_ids:
  - cartwheel-sas6-search
  - cartwheel-human-paralogs
  - tusk-paper
  - record
findings: []
actions: []
limitations:
- The2026 Trichonympha paper was checked at metadata/abstract level only, as an explicitly
  excluded molecular follow-up; its full model remains unassessed.
- Full native composition, exact whole-protein family grounding and universal stoichiometry
  remain unresolved.
- Map volumes were not reprocessed. Static architecture and reconstitution models
  do not establish a live assembly time course.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- Only the review bundle is saved. Maintained scientific content, native status, history
  and generated pages remain unchanged.
```
