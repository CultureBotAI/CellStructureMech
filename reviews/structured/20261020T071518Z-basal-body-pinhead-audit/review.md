# Basal-body pinhead morphology and source-boundary review

- Review: 20261020T071518Z-basal-body-pinhead-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-20T07:11:44Z
- Finished UTC: 2026-10-20T07:15:18Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Pinhead identity, Chlamydomonas morphology,8nm repeat, deposit and image are supported. Bld10 membership is supported only at the explicitly stated primary-abstract level; no concrete defect was found within that scope.

## Scope And Provenance

Entire maintained record and image; Li2019 full-text morphology/controls, Klena2020 boundary statements, native authority records and explicitly abstract-level Hiraki2007/Noga2022 evidence.

Selection: Eighth unreviewed path of batch4.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:basal_body_pinhead | data/structures/cytoskeleton/basal_body_pinhead.yaml | maintained | basal body pinhead |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | cellstructuremech:basal_body_pinhead | Focused validator passed. |
| Focused native strict | passed | True | cellstructuremech:basal_body_pinhead | Focused validator passed. |
| Target resolver slice | passed | True | cellstructuremech:basal_body_pinhead | 12 identifiers OK; 2 transport/skipped residuals independently resolved. |
| Full-text expansion beyond abstract-scoped molecular claims | unavailable | False | cellstructuremech:basal_body_pinhead | Hiraki2007 and Noga2022 full text remained inaccessible through attempted public routes. No detailed molecular/experimental claims from those unread sections are assessed or adopted. |
| Expression-module applicability | not_applicable | False | cellstructuremech:basal_body_pinhead | No matching expression dataset or expression-derived constituent assignment is asserted. |
| Claim-level scientific review | passed | True | cellstructuremech:basal_body_pinhead | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | cellstructuremech:basal_body_pinhead | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | cellstructuremech:basal_body_pinhead | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | cellstructuremech:basal_body_pinhead | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | cellstructuremech:basal_body_pinhead | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | cellstructuremech:basal_body_pinhead | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Peripheral cartwheel-to-A-tubule connection

identity: supported. Targets: cellstructuremech:basal_body_pinhead.

The named complex is distinct from hub, spokes, D2, triplet base, linker and axonemal radial spokes. Parent/parthood and morphological subdivision are appropriate.

### Explicit abstract-level Bld10 membership

evidence: supported. Targets: cellstructuremech:basal_body_pinhead.

The inspected primary abstract supports the exact limited spoke-tip membership claim. It does not establish PinB/PinF sequence identities or exclusive pinhead localization; the record does not assert those.

### Broader family and regional matches

grounding: supported. Targets: cellstructuremech:basal_body_pinhead.

IPR051877 spans CEP135/TSGA10 and the Pfam entries are regional coiled-coil matches. The label-only class avoids false exact grounding.

### Native Chlamydomonas material

scope: supported. Targets: cellstructuremech:basal_body_pinhead.

Species and proximal mother/pro-basal material match the primary reconstruction; the record does not claim whole-length occupancy or cross-species repeat conservation.

### Controlled8nm periodicity

evidence: supported. Targets: cellstructuremech:basal_body_pinhead.

The source morphology, Figure2D and explicit periodicity-control tests support the8nm repeat. Reconstruction window, resolution and subvolume count are correctly kept separate from dimensions and molecule numbers.

### Structural connection without kinetic extrapolation

graph: supported. Targets: cellstructuremech:basal_body_pinhead.

The observed connection supports the organization function. Static twist classes and low-resolution tips do not establish force constants, growth kinetics or a causal assembly time course.

### Exact broader map linkage

provenance: supported. Targets: cellstructuremech:basal_body_pinhead.

Table3 and native annotation agree on the pinhead-associated map. Its partial A-tubule prevents treating it as exact isolated-pinhead identity.

### Native licensed density rendering

evidence: supported. Targets: cellstructuremech:basal_body_pinhead.

Image bytes, panel meanings, scales, taxon and CCBY4.0 provenance match the source. Rendered colors are not protein sequence assignments.

### Unsuccessful full-text follow-ups retained

completeness: supported. Targets: cellstructuremech:basal_body_pinhead.

Current lawful public attempts did not yield the2007/2022 full text. The record accurately restricts its adopted molecular evidence to the inspected abstract; additional molecular locations remain unassessed.

### Open native composition

completeness: supported. Targets: cellstructuremech:basal_body_pinhead.

PROPOSED and unresolved proteome, essentiality and exact family identity are justified. No concrete contradiction was found within the asserted evidence scope.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bc-li2019 | https://pmc-oa-opendata.s3.amazonaws.com/PMC6384029.1/PMC6384029.1.xml; Pinhead Results, periodicity-control Methods, Figure2 and Table3 | supports | Pinhead Results identify A3 attachment, bent PinB and two pinfeet, repeating8nm. Periodicity Methods test segment length, overlap, masking, initial references and mother/pro-basal sampling. Table3 identifies map9171 as the pinhead plus partial A-tubule from4763subtomograms at23.1angstrom. |
| tusk-paper | https://pmc-oa-opendata.s3.amazonaws.com/PMC7667884.1/PMC7667884.1.xml; Discussion, Figure5 caption and proximal triplet averaging Methods | supports | The2020 source distinguishes D2-rod, triplet base and pinhead. The triplet-base Bld10 assignment is hypothetical. Figure5 warns that8.5nm picking imposed an incorrect pinhead periodicity in that reconstruction. |
| pinhead-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/j.cub.2007.09.021%20OR%20DOI:10.15252/embj.2020104582&amp;format=json&amp;resultType=core; Exact DOI/PMID metadata and both primary abstracts | supports | The inspected Hiraki2007 primary abstract directly reports Bld10 spoke-tip membership from immuno-EM and truncation morphology. Its detailed Results/Methods remain unread. Noga2022 abstract concerns Bld10 intertriplet crosslinks and does not equate them with pinhead identity. |
| bc-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1083/jcb.202311104%20OR%20DOI:10.7554/eLife.43434&amp;format=json&amp;resultType=core; Exact bibliographic identity | supports | The Li2019 DOI and PMID30741631 identify the inspected structural paper. |
| cartwheel-proteins | https://rest.uniprot.org/uniprotkb/search?query=accession:A9CQL4%20OR%20accession:A8ID55&amp;format=json; Native A8ID55 name, gene, taxon and status | supports | A8ID55 is reviewed Chlamydomonas Basal body protein10 with primary BLD10 gene symbol; sequence identity is distinct from localization evidence. |
| cartwheel-human-paralogs | https://rest.uniprot.org/uniprotkb/search?query=(gene_exact:CEP135%20OR%20gene_exact:TSGA10)%20AND%20organism_id:9606%20AND%20reviewed:true&amp;format=json; Both gene identities and cross-references | supports | Reviewed human CEP135 and TSGA10 both cross-reference IPR051877, establishing its broader membership. |
| cartwheel-IPR051877 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051877; Entry name/type | supports | The native entry is a broader structural-protein family; its generated description is not used as primary membership proof. |
| pinhead-PF30381 | https://www.ebi.ac.uk/interpro/api/entry/pfam/PF30381; Native type and name | supports | Native entry is typed coiled_coil and names a CEP135 N-terminal or CEP135/TSGA10 region, not an exact whole-protein family. |
| pinhead-PF30378 | https://www.ebi.ac.uk/interpro/api/entry/pfam/PF30378; Native type and name | supports | Native entry is typed coiled_coil and names a CEP135 N-terminal or CEP135/TSGA10 region, not an exact whole-protein family. |
| cartwheel-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032991,GO:0036064,GO:0120280,GO:0032053; Native term definitions | supports | The broader protein-complex parent, basal/pro-basal parthood and basal-body organization function match their active GO terms. |
| pinhead-go-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=pinhead&amp;limit=100; Complete native response | supports | The native pinhead query returns zero matches. This is a bounded exact-name search, not an exhaustive absence assertion under all synonyms. |
| sheath-taxon | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=3055; Native taxonomy | supports | NCBITaxon3055 identifies Chlamydomonas reinhardtii. |
| tusk-uo | https://www.ebi.ac.uk/ols4/api/ontologies/uo/terms?obo_id=UO:0000018; Native unit definition | supports | UO0000018 denotes nanometer. |
| pinhead-emdb9171 | https://www.ebi.ac.uk/emdb/api/entry/EMD-9171; Map annotation, release status, natural source, reconstruction and citation | supports | Native released entry has generic title but map.annotation_details explicitly identifies the pinhead/A-tubule reconstruction. Source is Chlamydomonas3055 strainCC849; final reconstruction lists4763subtomograms and23.1angstrom with exact Li DOI/PMID. |
| bc-li-fig2 | https://pmc-oa-opendata.s3.amazonaws.com/PMC6384029.1/elife-43434-fig2.jpg; Complete Figure2 and byte comparison | supports | Visual inspection confirms panelD PinB/PinF1/PinF2 labels and8nm repeat, and10nm scale bars by row. Source bytes match the maintained image SHA2569be52fd2803806b6eba0a9907365734ffef10776ceae64386b31f566479bcecb. |
| pinhead-li-meta | https://pmc-oa-opendata.s3.amazonaws.com/PMC6384029.1/PMC6384029.1.json; XML/media checksums and licence | supports | Official PMC article and image MD5 values match captured sources; JATS explicitly identifies CCBY4.0. |
| access-hiraki-pdf | https://www.cell.com/article/S096098220701980X/pdf; Public full-text access attempt | context_only | Publisher PDF returned403. No full text inspected. |
| access-paper | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9574746/fullTextXML; Public full-text access attempt | context_only | XML endpoint returned500 after retry with XML content type. |
| access-noga-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC9574746.1/PMC9574746.1.xml; Public full-text access attempt | context_only | Public archive returned404. |
| access-noga-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC9574746/; Public full-text access attempt | context_only | HTTP200 response was a reCAPTCHA challenge, not article content; no challenge was bypassed. |
| record | data/structures/cytoskeleton/basal_body_pinhead.yaml; Entire maintained record and image | context_only | The component’s support is explicitly restricted to a primary abstract; no detailed mutant dimensions, residue assignments or unread full-text claims are imported. |
| local-id | data/structures/cytoskeleton/basal_body_pinhead.yaml; Exact identifier search across data/structures including hidden and ignored files | context_only | Only this target declares the exact local pinhead identity. |
| schema-result | just validate data/structures/cytoskeleton/basal_body_pinhead.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/basal_body_pinhead.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/basal_body_pinhead.yaml --out /private/tmp/cellstructure-batch4-20261019-QtBQNE/basal_body_pinhead-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/basal_body_pinhead.yaml --out /private/tmp/cellstructure-batch4-20261019-QtBQNE/basal_body_pinhead-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch4-20261019-QtBQNE/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch4-20261019-QtBQNE/basal_body_pinhead-strict.tsv |
| target-curies | just check-curies-strict; data/structures/cytoskeleton/basal_body_pinhead.yaml; exact collect() scope | supports | 12 of14 collected target identifiers returned OK at the unchanged base. Residuals: EMDB:EMD-9171: SKIPPED; resolved by evidence pinhead-emdb9171; cellstructuremech:basal_body_pinhead: SKIPPED; resolved by evidence local-id. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- The2007 and2022 full texts were not obtained; detailed molecular localization, mutant measurements and additional assignments remain unassessed.
- Bld10 spoke-tip membership is supported at primary-abstract level, not by an independently inspected full experimental report.
- No map volume was reprocessed; PinB/PinF protein identities and full composition remain unknown.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Only the review bundle is saved. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T071518Z-basal-body-pinhead-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Basal-body pinhead morphology and source-boundary review
started_at: '2026-10-20T07:11:44Z'
finished_at: '2026-10-20T07:15:18Z'
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
summary: Pinhead identity, Chlamydomonas morphology,8nm repeat, deposit and image
  are supported. Bld10 membership is supported only at the explicitly stated primary-abstract
  level; no concrete defect was found within that scope.
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
  - path: data/images/cytoskeleton/basal_body_pinhead/pmc6384029_fig2.jpg
    sha256: 9be52fd2803806b6eba0a9907365734ffef10776ceae64386b31f566479bcecb
    role: context
  - path: data/structures/cytoskeleton/basal_body_pinhead.yaml
    sha256: ef3da1eee8d7e92150c0bf3ab1c6e2c67a410aa366416ab03454e3929e25bff2
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
- target_id: cellstructuremech:basal_body_pinhead
  path: data/structures/cytoskeleton/basal_body_pinhead.yaml
  label: basal body pinhead
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/basal_body_pinhead.yaml
    role: maintained scientific record
scope:
  description: Entire maintained record and image; Li2019 full-text morphology/controls,
    Klena2020 boundary statements, native authority records and explicitly abstract-level
    Hiraki2007/Noga2022 evidence.
  selection: Eighth unreviewed path of batch4.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:basal_body_pinhead
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_pinhead
  command: just validate data/structures/cytoskeleton/basal_body_pinhead.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_pinhead
  command: just validate-strict data/structures/cytoskeleton/basal_body_pinhead.yaml
    --out /private/tmp/cellstructure-batch4-20261019-QtBQNE/basal_body_pinhead-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_pinhead
  summary: 12 identifiers OK; 2 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - pinhead-emdb9171
  - local-id
- check_id: additional-full-text
  name: Full-text expansion beyond abstract-scoped molecular claims
  status: unavailable
  required: false
  target_ids:
  - cellstructuremech:basal_body_pinhead
  summary: Hiraki2007 and Noga2022 full text remained inaccessible through attempted
    public routes. No detailed molecular/experimental claims from those unread sections
    are assessed or adopted.
  evidence_ids:
  - access-hiraki-pdf
  - access-paper
  - access-noga-s3
  - access-noga-pmc
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - cellstructuremech:basal_body_pinhead
  summary: No matching expression dataset or expression-derived constituent assignment
    is asserted.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_pinhead
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - bc-li2019
  - tusk-paper
  - pinhead-epmc
  - bc-epmc
  - cartwheel-proteins
  - cartwheel-human-paralogs
  - cartwheel-IPR051877
  - pinhead-PF30381
  - pinhead-PF30378
  - cartwheel-go
  - pinhead-go-search
  - sheath-taxon
  - tusk-uo
  - pinhead-emdb9171
  - bc-li-fig2
  - pinhead-li-meta
  - access-hiraki-pdf
  - access-paper
  - access-noga-s3
  - access-noga-pmc
  - record
  - local-id
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_pinhead
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
  - cellstructuremech:basal_body_pinhead
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
  - cellstructuremech:basal_body_pinhead
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
  - cellstructuremech:basal_body_pinhead
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
  - cellstructuremech:basal_body_pinhead
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
- evidence_id: bc-li2019
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6384029.1/PMC6384029.1.xml
  locator: Pinhead Results, periodicity-control Methods, Figure2 and Table3
  accessed_at: '2026-10-20T04:10:07.604636Z'
  support: supports
  summary: Pinhead Results identify A3 attachment, bent PinB and two pinfeet, repeating8nm.
    Periodicity Methods test segment length, overlap, masking, initial references
    and mother/pro-basal sampling. Table3 identifies map9171 as the pinhead plus partial
    A-tubule from4763subtomograms at23.1angstrom.
  snapshot_sha256: 2965143460a98de85b7b6525bea14596791bbf9a32094484b54e42b74794af7a
- evidence_id: tusk-paper
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC7667884.1/PMC7667884.1.xml
  locator: Discussion, Figure5 caption and proximal triplet averaging Methods
  accessed_at: '2026-10-20T04:07:36.772127Z'
  support: supports
  summary: The2020 source distinguishes D2-rod, triplet base and pinhead. The triplet-base
    Bld10 assignment is hypothetical. Figure5 warns that8.5nm picking imposed an incorrect
    pinhead periodicity in that reconstruction.
  snapshot_sha256: 5116fa9428a3a69c7a3baca7e80ad82dc6d050ed8db9d88b37982136407d6184
- evidence_id: pinhead-epmc
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/j.cub.2007.09.021%20OR%20DOI:10.15252/embj.2020104582&format=json&resultType=core
  locator: Exact DOI/PMID metadata and both primary abstracts
  accessed_at: '2026-10-20T07:12:05.917499Z'
  support: supports
  summary: The inspected Hiraki2007 primary abstract directly reports Bld10 spoke-tip
    membership from immuno-EM and truncation morphology. Its detailed Results/Methods
    remain unread. Noga2022 abstract concerns Bld10 intertriplet crosslinks and does
    not equate them with pinhead identity.
  snapshot_sha256: 60b872f66ea1c0ec093e26079306a389ca21fd59016cf7d9b5cbdc524c1eb2ca
- evidence_id: bc-epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1083/jcb.202311104%20OR%20DOI:10.7554/eLife.43434&format=json&resultType=core
  locator: Exact bibliographic identity
  accessed_at: '2026-10-20T04:10:07.568353Z'
  support: supports
  summary: The Li2019 DOI and PMID30741631 identify the inspected structural paper.
  snapshot_sha256: f0ab2357cbfb307cd5527ea3ff914c1ac8eac0a9699276c5e493b36d57f28b05
- evidence_id: cartwheel-proteins
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?query=accession:A9CQL4%20OR%20accession:A8ID55&format=json
  locator: Native A8ID55 name, gene, taxon and status
  accessed_at: '2026-10-20T06:55:14.426725Z'
  support: supports
  summary: A8ID55 is reviewed Chlamydomonas Basal body protein10 with primary BLD10
    gene symbol; sequence identity is distinct from localization evidence.
  snapshot_sha256: 8a56b3bb6260c7af9fc0ef791ac0c2ae82c459f81c9dd18a24b174d15bce65fe
- evidence_id: cartwheel-human-paralogs
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?query=(gene_exact:CEP135%20OR%20gene_exact:TSGA10)%20AND%20organism_id:9606%20AND%20reviewed:true&format=json
  locator: Both gene identities and cross-references
  accessed_at: '2026-10-20T06:56:05.105046Z'
  support: supports
  summary: Reviewed human CEP135 and TSGA10 both cross-reference IPR051877, establishing
    its broader membership.
  snapshot_sha256: 0796a565c2224aaea2b8c6b1cc1311b2f8d561cae1c21876707f430e8bb8fcd8
- evidence_id: cartwheel-IPR051877
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051877
  locator: Entry name/type
  accessed_at: '2026-10-20T06:55:13.619866Z'
  support: supports
  summary: The native entry is a broader structural-protein family; its generated
    description is not used as primary membership proof.
  snapshot_sha256: ef5b481674874d1e56d39f6808f575fbee42919f894ad36b3aef1ea0d1b1645e
- evidence_id: pinhead-PF30381
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF30381
  locator: Native type and name
  accessed_at: '2026-10-20T07:14:13.796151Z'
  support: supports
  summary: Native entry is typed coiled_coil and names a CEP135 N-terminal or CEP135/TSGA10
    region, not an exact whole-protein family.
  snapshot_sha256: aaef0f53c13d953f94499f529b6e932af9a99c16c8ed282585715d144da68580
- evidence_id: pinhead-PF30378
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF30378
  locator: Native type and name
  accessed_at: '2026-10-20T07:14:14.368578Z'
  support: supports
  summary: Native entry is typed coiled_coil and names a CEP135 N-terminal or CEP135/TSGA10
    region, not an exact whole-protein family.
  snapshot_sha256: dbd17fc2ed4eec8c32cdbdf7ef08f92b492531850c97793cc7b462d8b1a6fa2f
- evidence_id: cartwheel-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032991,GO:0036064,GO:0120280,GO:0032053
  locator: Native term definitions
  accessed_at: '2026-10-20T06:55:12.197440Z'
  support: supports
  summary: The broader protein-complex parent, basal/pro-basal parthood and basal-body
    organization function match their active GO terms.
  snapshot_sha256: 3b763f8154d823f7eb174cd748438843c3ed9723272033a93957a481877a3316
- evidence_id: pinhead-go-search
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=pinhead&limit=100
  locator: Complete native response
  accessed_at: '2026-10-20T07:12:06.381819Z'
  support: supports
  summary: The native pinhead query returns zero matches. This is a bounded exact-name
    search, not an exhaustive absence assertion under all synonyms.
  snapshot_sha256: f3a7dae9b1e9335291e3940cdf0e5f8dadf9335da7b9547710606b5106c63f86
- evidence_id: sheath-taxon
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=3055
  locator: Native taxonomy
  accessed_at: '2026-10-20T03:38:20.199537Z'
  support: supports
  summary: NCBITaxon3055 identifies Chlamydomonas reinhardtii.
  snapshot_sha256: a17bc1c97fea9112288574ef15727ed7e37c42787a430ef074ae5fc654547e6b
- evidence_id: tusk-uo
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uo/terms?obo_id=UO:0000018
  locator: Native unit definition
  accessed_at: '2026-10-20T04:07:37.417486Z'
  support: supports
  summary: UO0000018 denotes nanometer.
  snapshot_sha256: 4c7db9c8cb664724cfeb7ded951492cac50dd7c8bdc275363486b3e34df94bf8
- evidence_id: pinhead-emdb9171
  kind: authority
  reference: https://www.ebi.ac.uk/emdb/api/entry/EMD-9171
  locator: Map annotation, release status, natural source, reconstruction and citation
  accessed_at: '2026-10-20T07:12:07.603805Z'
  support: supports
  summary: Native released entry has generic title but map.annotation_details explicitly
    identifies the pinhead/A-tubule reconstruction. Source is Chlamydomonas3055 strainCC849;
    final reconstruction lists4763subtomograms and23.1angstrom with exact Li DOI/PMID.
  snapshot_sha256: 22538bcad530612264dbce7758708ac04d4c47fff175f51a17a472e0f2177034
- evidence_id: bc-li-fig2
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6384029.1/elife-43434-fig2.jpg
  locator: Complete Figure2 and byte comparison
  accessed_at: '2026-10-20T06:53:09.065225Z'
  support: supports
  summary: Visual inspection confirms panelD PinB/PinF1/PinF2 labels and8nm repeat,
    and10nm scale bars by row. Source bytes match the maintained image SHA2569be52fd2803806b6eba0a9907365734ffef10776ceae64386b31f566479bcecb.
  snapshot_sha256: 9be52fd2803806b6eba0a9907365734ffef10776ceae64386b31f566479bcecb
- evidence_id: pinhead-li-meta
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6384029.1/PMC6384029.1.json
  locator: XML/media checksums and licence
  accessed_at: '2026-10-20T07:12:05.610868Z'
  support: supports
  summary: Official PMC article and image MD5 values match captured sources; JATS
    explicitly identifies CCBY4.0.
  snapshot_sha256: c60fe2231d7b88fcdf6ccaf8adae4a478747905d3c6072048983714495cb9eb8
- evidence_id: access-hiraki-pdf
  kind: primary_source
  reference: https://www.cell.com/article/S096098220701980X/pdf
  locator: Public full-text access attempt
  accessed_at: '2026-10-20T07:12:27.073662Z'
  support: context_only
  summary: Publisher PDF returned403. No full text inspected.
  snapshot_sha256: 221f0312ba5ce8059318140146ea77ee6dbfa09a6ac5b742c53e05f27511435d
- evidence_id: access-paper
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9574746/fullTextXML
  locator: Public full-text access attempt
  accessed_at: '2026-10-20T07:12:57.778123Z'
  support: context_only
  summary: XML endpoint returned500 after retry with XML content type.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: access-noga-s3
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC9574746.1/PMC9574746.1.xml
  locator: Public full-text access attempt
  accessed_at: '2026-10-20T07:12:57.077151Z'
  support: context_only
  summary: Public archive returned404.
  snapshot_sha256: 2a699eed3e6322e01cfe87b61362174e1aee187f40853cd5e003e46ec73b3a61
- evidence_id: access-noga-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC9574746/
  locator: Public full-text access attempt
  accessed_at: '2026-10-20T07:12:27.204812Z'
  support: context_only
  summary: HTTP200 response was a reCAPTCHA challenge, not article content; no challenge
    was bypassed.
  snapshot_sha256: cc2ea96c6fe11e232acdba42cffb2cdc8c5729cc2b81258a6ba82efa44e204ed
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/basal_body_pinhead.yaml
  locator: Entire maintained record and image
  accessed_at: '2026-10-20T07:15:18Z'
  support: context_only
  summary: The component’s support is explicitly restricted to a primary abstract;
    no detailed mutant dimensions, residue assignments or unread full-text claims
    are imported.
- evidence_id: local-id
  kind: record_content
  reference: data/structures/cytoskeleton/basal_body_pinhead.yaml
  locator: Exact identifier search across data/structures including hidden and ignored
    files
  accessed_at: '2026-10-20T07:15:18Z'
  support: context_only
  summary: Only this target declares the exact local pinhead identity.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/basal_body_pinhead.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-20T07:11:46Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/basal_body_pinhead.yaml'
  snapshot_sha256: b27fbffa591760432c68f59593638d9ecfd24763a1af84eebc1aa9948afb6e99
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/basal_body_pinhead.yaml
    --out /private/tmp/cellstructure-batch4-20261019-QtBQNE/basal_body_pinhead-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-20T07:11:47Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/basal_body_pinhead.yaml\
    \ --out /private/tmp/cellstructure-batch4-20261019-QtBQNE/basal_body_pinhead-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch4-20261019-QtBQNE/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch4-20261019-QtBQNE/basal_body_pinhead-strict.tsv"
  snapshot_sha256: 62b7ab582c7d0a5c52b15fa33a7d39816bd9732b668fc032fb21a1aba1de7a4f
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/basal_body_pinhead.yaml; exact collect() scope
  accessed_at: '2026-10-20T07:15:18Z'
  support: supports
  summary: '12 of14 collected target identifiers returned OK at the unchanged base.
    Residuals: EMDB:EMD-9171: SKIPPED; resolved by evidence pinhead-emdb9171; cellstructuremech:basal_body_pinhead:
    SKIPPED; resolved by evidence local-id. Source-native identity checked separately.'
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
  topic: Peripheral cartwheel-to-A-tubule connection
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_pinhead
  summary: The named complex is distinct from hub, spokes, D2, triplet base, linker
    and axonemal radial spokes. Parent/parthood and morphological subdivision are
    appropriate.
  evidence_ids:
  - bc-li2019
  - tusk-paper
  - cartwheel-go
  - pinhead-go-search
  - record
- assessment_id: component
  area: evidence
  topic: Explicit abstract-level Bld10 membership
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_pinhead
  summary: The inspected primary abstract supports the exact limited spoke-tip membership
    claim. It does not establish PinB/PinF sequence identities or exclusive pinhead
    localization; the record does not assert those.
  evidence_ids:
  - pinhead-epmc
  - cartwheel-proteins
  - record
- assessment_id: grounding
  area: grounding
  topic: Broader family and regional matches
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_pinhead
  summary: IPR051877 spans CEP135/TSGA10 and the Pfam entries are regional coiled-coil
    matches. The label-only class avoids false exact grounding.
  evidence_ids:
  - cartwheel-IPR051877
  - cartwheel-human-paralogs
  - pinhead-PF30381
  - pinhead-PF30378
  - record
- assessment_id: scope
  area: scope
  topic: Native Chlamydomonas material
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_pinhead
  summary: Species and proximal mother/pro-basal material match the primary reconstruction;
    the record does not claim whole-length occupancy or cross-species repeat conservation.
  evidence_ids:
  - bc-li2019
  - sheath-taxon
  - pinhead-emdb9171
  - record
- assessment_id: measurement
  area: evidence
  topic: Controlled8nm periodicity
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_pinhead
  summary: The source morphology, Figure2D and explicit periodicity-control tests
    support the8nm repeat. Reconstruction window, resolution and subvolume count are
    correctly kept separate from dimensions and molecule numbers.
  evidence_ids:
  - bc-li2019
  - tusk-uo
  - bc-li-fig2
  - pinhead-emdb9171
  - record
- assessment_id: function
  area: graph
  topic: Structural connection without kinetic extrapolation
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_pinhead
  summary: The observed connection supports the organization function. Static twist
    classes and low-resolution tips do not establish force constants, growth kinetics
    or a causal assembly time course.
  evidence_ids:
  - bc-li2019
  - tusk-paper
  - cartwheel-go
  - record
- assessment_id: dataset
  area: provenance
  topic: Exact broader map linkage
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_pinhead
  summary: Table3 and native annotation agree on the pinhead-associated map. Its partial
    A-tubule prevents treating it as exact isolated-pinhead identity.
  evidence_ids:
  - bc-li2019
  - pinhead-emdb9171
  - record
- assessment_id: image
  area: evidence
  topic: Native licensed density rendering
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_pinhead
  summary: Image bytes, panel meanings, scales, taxon and CCBY4.0 provenance match
    the source. Rendered colors are not protein sequence assignments.
  evidence_ids:
  - bc-li-fig2
  - pinhead-li-meta
  - bc-li2019
  - record
- assessment_id: source-boundary
  area: completeness
  topic: Unsuccessful full-text follow-ups retained
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_pinhead
  summary: Current lawful public attempts did not yield the2007/2022 full text. The
    record accurately restricts its adopted molecular evidence to the inspected abstract;
    additional molecular locations remain unassessed.
  evidence_ids:
  - pinhead-epmc
  - access-hiraki-pdf
  - access-paper
  - access-noga-s3
  - access-noga-pmc
  - record
- assessment_id: status
  area: completeness
  topic: Open native composition
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_pinhead
  summary: PROPOSED and unresolved proteome, essentiality and exact family identity
    are justified. No concrete contradiction was found within the asserted evidence
    scope.
  evidence_ids:
  - bc-li2019
  - pinhead-epmc
  - cartwheel-human-paralogs
  - record
findings: []
actions: []
limitations:
- The2007 and2022 full texts were not obtained; detailed molecular localization, mutant
  measurements and additional assignments remain unassessed.
- Bld10 spoke-tip membership is supported at primary-abstract level, not by an independently
  inspected full experimental report.
- No map volume was reprocessed; PinB/PinF protein identities and full composition
  remain unknown.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- Only the review bundle is saved. Maintained scientific content, native status, history
  and generated pages remain unchanged.
```
