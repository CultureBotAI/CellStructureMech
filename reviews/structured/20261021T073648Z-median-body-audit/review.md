# Median body identity, microtubule dynamics and functional-scope review

- Review: 20261021T073648Z-median-body-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T07:27:33Z
- Finished UTC: 2026-10-21T07:36:48Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Median-body identity, topology, tubulin composition and scoped Kinesin-13 localization/perturbation claims are supported. No material finding was identified. Source access, species/strain boundaries, cell-cycle effects and reservoir-function inference remain qualified.

## Scope And Provenance

Entire single target, native GO relation graph and taxonomy; relevant Friend1966 primary text/PDF, Piva2004 abstract, Dawson2007 body, 2020 review section 5 and Hardin2017 primary reservoir/imaging passages.

Selection: Ninth target in batch eight, in repository path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0097568 | data/structures/cytoskeleton/median_body.yaml | maintained | median body |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0097568 | Focused validator passed. |
| Focused native strict | passed | True | GO:0097568 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0097568 | 8 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | GO:0097568 | Physical microtubule-array composition, localization and dominant-negative perturbation claims; no transcriptional regulator or expression-module mechanism asserted. |
| Claim-level scientific review | passed | True | GO:0097568 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0097568 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0097568 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0097568 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0097568 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0097568 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Giardia median-body identity and morphology

identity: supported. Targets: GO:0097568.

Active GO0097568 exactly supplies the nonmembranous semi-organized microtubule-array definition, position and related parabasal-body synonym. Friend1966 supports a curved aggregate in G.muris; Piva2004 abstract and the later review support the distinct array without importing a fixed count, dimension, orientation or universal absence of connections across species.

### Cytoskeleton parthood and microtubule parts

representation: supported. Targets: GO:0097568.

Native OLS graph explicitly gives BFO0000050 part_of cytoskeleton and BFO0000051 has_part microtubule, with the term as relation source. QuickGO corroborates the part_of edge. The failed has_part-path query and ambiguous OLS traversal are not treated as relation absence or typed target evidence.

### Tubulin constituents versus associated regulator

evidence: supported. Targets: GO:0097568.

GO0005874 explicitly grounds alpha/beta-tubulin polymer composition; anti-tubulin reactivity in Piva and anti-alpha-tubulin imaging in Dawson support the array. Kinesin-13 GFP localization supports associated machinery, distinct from the structural constituent. Beta-giardin antibody reactivity is retained as a boundary TODO and is not converted to an exact accession, stoichiometry or experimentally complete inventory.

### Label-only classes and unresolved exact protein mappings

grounding: supported. Targets: GO:0097568.

No unsupported accession is supplied for the alpha/beta class or Giardia Kinesin-13. A generic tubulin superclass or kinesin motor domain would not, by itself, establish an exact match to these component classes. The primary study reports a sole Giardia Kinesin-13 homolog; no modern exhaustive family mapping was performed here. Historical no-exact-mapping notes and the explicit TODO do not alone establish a curation defect.

### Kinesin-13 and EB1 localization scope

graph: supported. Targets: GO:0097568.

Dawson GFP fusions localize Kinesin-13 and EB1 to the median body and other dynamic microtubule arrays. The target captures Kinesin-13 localization and acknowledges EB1 in prose; it does not claim exclusive residence, indispensability, direct binding to a defined plus end within every median body, or a complete regulator inventory.

### Condition-specific S280N volume response

graph: supported. Targets: GO:0097568.

Dawson compares WBC6/ATCC50803 cells with or without 48 h induction of an ectopic GFP-tagged S280N rigor construct by doxycycline withdrawal, using anti-alpha-tubulin and 3D volume analysis. The induced comparison gives smaller median-body volumes, while early-mitotic mutant arrays can elongate and persist. The record describes changes/modulation of volume and cites the decrease from the assay; this does not assert that every cell-cycle state responds in the same direction or that isolated motor activity was reconstituted.

### Reservoir evidence and unresolved physiological function

scope: supported. Targets: GO:0097568.

The current GO definition and 2020 review retain uncertain/enigmatic function. Hardin2017 provides primary live mNeonGreen-beta-tubulin imaging in which median-body signal decreases as spindles, discs and nascent flagella assemble; the authors interpret this as reservoir support. That evidence strengthens the reservoir hypothesis but does not directly trace isolated tubulin transfer, specifically ablate/rescue median-body function, or resolve competing proposals. Leaving a settled biological-process function unasserted is defensible.

### Species synonyms, experimental strain and cell state

scope: supported. Targets: GO:0097568.

Native taxon5741 currently prefers Giardia duodenalis and explicitly includes Giardia intestinalis and Giardia lamblia as synonyms. The maintained label therefore denotes the same species. Dawson uses WBC6/ATCC50803 trophozoites, whereas Friend describes G.muris; their detailed experimental observations are not conflated. Common trophozoite occurrence does not mean presence at every cell-cycle stage or a universal fixed number.

### Actual source readability and native bytes

provenance: supported. Targets: GO:0097568.

Relevant Friend historical primary text/PDF and Dawson article HTML are readable. The2020 source is a readable public author manuscript, and Hardin is a public coauthor-hosted PDF; their content and roles are distinguished. Piva remains abstract-only, with failed publisher routes preserved. Native MD5 confirms Friend XML/PDF and review XML bytes. No target image is present and no image license is inferred from public text accessibility.

### Bounded structural and dynamics representation

completeness: supported. Targets: GO:0097568.

The target represents the defining microtubule array, constituent class, experimentally localized regulator, canonical species and supported dynamics relationship. It explicitly leaves exact protein boundaries, further associated material and physiological function open. No exact family match or required complete inventory was established that would convert those optional omissions into a finding.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| median-body-agent-dawson-efetch | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&amp;id=2168246; PMC articleset front matter and publisher XML restriction comment | context_only | HTTP200 body explicitly says publisher does not allow downloading full text in XML form. No experimental body. |
| median-body-agent-dawson-europe | https://europepmc.org/articles/PMC2168246; HTTP403 response | unknown | Europe PMC HTML request unavailable. |
| median-body-agent-dawson-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2168246/fullTextXML; HTTP500 response | unknown | Full text not obtained by Europe PMC XML route. |
| median-body-agent-dawson-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2168246/; Methods strain/culture, cloning/GFP/S280N, immunostaining/measurement, drug treatments; Results Figs1–6/Table2; Discussion median-body subsection | supports | Actual PMC article HTML. All median-body Results/Discussion, relevant Methods and main captions read. See claim_scope. |
| median-body-agent-dawson-pdf | https://pmc.ncbi.nlm.nih.gov/articles/PMC2168246/pdf/0128-07.pdf; HTTP200 short HTML response | unknown | Not a PDF or article body; not used as scientific evidence. |
| median-body-agent-dawson-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2168246.1/PMC2168246.1.xml; HTTP404 XML response | unknown | Exact S3 object unavailable; does not prove paper lacks free full text elsewhere. |
| median-body-agent-dawson2007 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2168246/; HTML title/body | unknown | HTTP200 reCAPTCHA; not full text. |
| median-body-agent-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1083/jcb.29.2.317%20OR%20DOI:10.1016/j.biolcel.2004.05.006%20OR%20DOI:10.1128/EC.00128-07%20OR%20DOI:10.1016/bs.apar.2019.11.001&amp;format=json&amp;resultType=core; Four exact DOI results; all abstracts read | supports | Friend1966 PMID5961344/PMC2106914; Piva2004 PMID15567529; Dawson2007 PMID17766466/PMC2168246; Hagen2020 PMID32122531/PMC8086724. Piva abstract directly reports anti-tubulin and anti-beta-giardin reactivity and variable number/shape/position. |
| median-body-agent-friend-meta | https://pmc-oa-opendata.s3.amazonaws.com/PMC2106914.1/PMC2106914.1.json; DOI/PMID/title/version, XML/PDF native checksums | supports | Identity and downloaded-byte checks verified below. |
| median-body-agent-friend1966-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC2106914.1/PMC2106914.1.xml; Native article JATS body; abstract and median-body text | supports | Supports G.muris ultrastructure; native historical text corroborated against scanned PDF. |
| median-body-agent-friend1966-pdf | https://pmc-oa-opendata.s3.amazonaws.com/PMC2106914.1/PMC2106914.1.pdf; pp318–319 Methods and general configuration; p323 Median Body; p324 Figs12–13 caption; p328 Discussion Median Body | supports | G.muris trophozoites in mouse duodenum, in-situ chemical fixation and thin-section EM. Curved non-membrane-bound tubule aggregate described. No quantitative claim imported into target. |
| median-body-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097568,GO:0005856,GO:0005874; Three GO results: definition/synonym/aspect/isObsolete/children | supports | Exact median-body definition and RELATED parabasal-body synonym match current active CC term. Microtubule definition explicitly describes alpha/beta polymeric tubulin. Cytoskeleton lists median body as part_of child. |
| median-body-agent-go-graph | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FGO_0097568/graph; edges with source GO_0097568 | supports | Explicit BFO_0000050 part_of GO_0005856; BFO_0000051 has_part GO_0005874; RO_0002162 in_taxon NCBITaxon_5740. Strong direct relation evidence. |
| median-body-agent-go-haspart | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097568/paths/GO:0005874?relations=has_part; HTTP400 JSON response | unknown | QuickGO rejects has_part path parameter; not evidence that relation is absent. |
| median-body-agent-go-ols | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0097568; GO:0097568 term, definitions and relation-link URLs | context_only | Definition verified; links alone do not identify has_part target. |
| median-body-agent-go-ols-haspart | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FGO_0097568/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBFO_0000051; OLS relation-link response embedded terms | unknown | Returned multiple terms spanning different relations; not used alone as typed relation evidence. |
| median-body-agent-go-relations | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097568/paths/GO:0005575?relations=is_a,part_of; GO:0097568 paths to CC root | supports | Direct part_of GO:0005856; separate is_a GO:0110165. No is_a/cytoskeleton conflation. |
| median-body-agent-hardin-author-pdf | https://vnminin.github.io/papers/Hardin2017.pdf; Hardin et al2017 DOI10.1073/pnas.1705096114; pE5855 Results first subsection; Fig1 caption; pE5862 Materials and Methods | supports | Public coauthor-hosted article PDF. Relevant reservoir Results, Fig1 caption and imaging/strain Methods read; not a full-paper scientific audit. See claim_scope. |
| median-body-agent-hardin-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5530689/fullTextXML; Europe PMC XML HTTP500 | unknown | Not article text. |
| median-body-agent-hardin-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5530689/; HTTP200 HTML title/body | unknown | Not article text. |
| median-body-agent-hardin2017 | https://pmc-oa-opendata.s3.amazonaws.com/PMC5530689.1/PMC5530689.1.xml; Exact S3 XML HTTP404 | unknown | No source body recovered by this route. |
| median-body-agent-piva-html | https://onlinelibrary.wiley.com/doi/full/10.1016/j.biolcel.2004.05.006; Wiley full article HTTP403 | unknown | No body obtained. Browser full route unavailable; ScienceDirect browser403. No fulltext inferred from search snippets. |
| median-body-agent-piva2004 | https://onlinelibrary.wiley.com/doi/pdfdirect/10.1016/j.biolcel.2004.05.006; Wiley pdfdirect HTTP403 | unknown | No full PDF obtained from this route; source remains abstract-only in this preparation. |
| median-body-agent-review-meta | https://pmc-oa-opendata.s3.amazonaws.com/PMC8086724.1/PMC8086724.1.json; PMC8086724.1 DOI/PMID/title, manuscript and TDM license metadata | supports | Author manuscript NIHMS1664321; is_pmc_openaccess false; license_code TDM. Readable public native XML does not authorize corpus image hosting. XML native checksum verified. |
| median-body-agent-review-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC8086724.1/PMC8086724.1.xml; Section5 S5/P23–P24, reference R59; Table1 relevant rows | supports | Literature-review manuscript, not a new primary experiment. Median-body architecture/dynamics and competing function hypotheses read. Review calls function enigmatic while citing primary live-cell evidence supporting tubulin reservoir. Table1 is a source inventory, not new native family/accession grounding. |
| median-body-agent-review2020 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8086724/; HTML title/body | unknown | HTTP200 reCAPTCHA, not full text; later native S3 recovery succeeded. |
| median-body-agent-species | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5741; taxId5741, scientificName, rank, otherNames | supports | Current preferred name Giardia duodenalis, species; Giardia intestinalis and Giardia lamblia are explicit synonyms. Record uses recognized synonym of same taxon. |
| record | data/structures/cytoskeleton/median_body.yaml; Entire YAML: definition, synonymy, topology, two components, taxon rows, all graph edges and both discussions | context_only | The complete maintained record was read. It distinguishes tubulin constituents from associated Kinesin-13, leaves exact family/protein boundaries and physiological function unresolved, and does not assert a complete mechanistic pathway or invariant volume response. |
| schema-result | just validate data/structures/cytoskeleton/median_body.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/median_body.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/median_body.yaml --out /private/tmp/cellstructure-batch8-20261021-q561gvty/median_body-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/median_body.yaml --out /private/tmp/cellstructure-batch8-20261021-q561gvty/median_body-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch8-20261021-q561gvty/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch8-20261021-q561gvty/median_body-strict.tsv |
| target-curies | just check-curies-strict; data/structures/cytoskeleton/median_body.yaml; exact collect() scope; snapshot_sha256 identifies the entire original reports/curie_check.tsv, not the extracted resolver-slice.json | supports | 8 of 8 collected target identifiers returned OK at the unchanged base. Residuals: none. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Piva2004 was inspected at abstract tier only; publisher HTML and PDF retrieval returned 403. Original antibody methods, controls and detailed counts were not independently recovered.
- Friend1966 describes chemically fixed G.muris trophozoites from mouse duodenum. Its detailed dimensions, connections and incidence were not generalized to WBC6 or all Giardia species.
- Dawson volume effects depend on ectopic S280N induction and cell-cycle context. Smaller volumes at 48 h and elongated/persistent early-mitotic arrays are distinct observations; raw volumes and normalized ratios were not conflated.
- Hardin2017 reservoir inference comes from live fluorescent tubulin redistribution. Imaging used WBC6, albendazole pretreatment/washout, SB5050, 37°C and controlled hypoxia; drug-free DIC timing was a separate experiment. No isolated molecular-transfer, median-body depletion/rescue or purified reconstitution claim is made.
- Relevant body text and captions were read; microscopy pixels, movies and raw data were not independently reanalyzed. The Hardin paper was inspected only for the reservoir and relevant methods passages.
- No exhaustive family/accession enrichment was performed. Broad family or domain resemblance is not proof of an exact match to the recorded alpha/beta-tubulin or Giardia-specific Kinesin-13 classes.
- The2020 review is contextual literature, not an independent primary experiment. Its publicly readable native manuscript has TDM metadata and does not confer an image-reuse license.
- Current review does not reconstruct every historical curation decision or establish independent historical authorship.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The full median_body.yaml is the only substantive local scientific input used. No neighboring-record or previous-review scientific judgment informed the assessment. All native captured input hashes were rechecked.
- Native focused schema/strict checks passed before assessment. Shared unchanged-base gates are documented by the parent reviewer before finalization.
- The parent checked the source-scoped draft before finalization; no maintained scientific content was changed.
- Only the review bundle is saved. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T073648Z-median-body-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Median body identity, microtubule dynamics and functional-scope review
started_at: '2026-10-21T07:27:33Z'
finished_at: '2026-10-21T07:36:48Z'
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
summary: Median-body identity, topology, tubulin composition and scoped Kinesin-13
  localization/perturbation claims are supported. No material finding was identified.
  Source access, species/strain boundaries, cell-cycle effects and reservoir-function
  inference remain qualified.
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
  - path: data/structures/cytoskeleton/median_body.yaml
    sha256: d8acb0b396e2f02d12854bfcef95a7a2bc67b6be648058230971e38d1b7e757f
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
- target_id: GO:0097568
  path: data/structures/cytoskeleton/median_body.yaml
  label: median body
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/median_body.yaml
    role: maintained scientific record
scope:
  description: Entire single target, native GO relation graph and taxonomy; relevant
    Friend1966 primary text/PDF, Piva2004 abstract, Dawson2007 body, 2020 review section
    5 and Hardin2017 primary reservoir/imaging passages.
  selection: Ninth target in batch eight, in repository path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0097568
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0097568
  command: just validate data/structures/cytoskeleton/median_body.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0097568
  command: just validate-strict data/structures/cytoskeleton/median_body.yaml --out
    /private/tmp/cellstructure-batch8-20261021-q561gvty/median_body-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0097568
  summary: 8 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0097568
  summary: Physical microtubule-array composition, localization and dominant-negative
    perturbation claims; no transcriptional regulator or expression-module mechanism
    asserted.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0097568
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - median-body-agent-dawson-efetch
  - median-body-agent-dawson-europe
  - median-body-agent-dawson-jats
  - median-body-agent-dawson-legacy
  - median-body-agent-dawson-pdf
  - median-body-agent-dawson-s3
  - median-body-agent-dawson2007
  - median-body-agent-epmc
  - median-body-agent-friend-meta
  - median-body-agent-friend1966-jats
  - median-body-agent-friend1966-pdf
  - median-body-agent-go
  - median-body-agent-go-graph
  - median-body-agent-go-haspart
  - median-body-agent-go-ols
  - median-body-agent-go-ols-haspart
  - median-body-agent-go-relations
  - median-body-agent-hardin-author-pdf
  - median-body-agent-hardin-jats
  - median-body-agent-hardin-legacy
  - median-body-agent-hardin2017
  - median-body-agent-piva-html
  - median-body-agent-piva2004
  - median-body-agent-review-meta
  - median-body-agent-review-s3
  - median-body-agent-review2020
  - median-body-agent-species
  - record
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0097568
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch8 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0097568
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch8 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0097568
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch8 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0097568
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch8 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0097568
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch8 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: median-body-agent-dawson-efetch
  kind: primary_source
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=2168246
  locator: PMC articleset front matter and publisher XML restriction comment
  accessed_at: '2026-10-21T07:30:33.790969Z'
  support: context_only
  summary: HTTP200 body explicitly says publisher does not allow downloading full
    text in XML form. No experimental body.
  snapshot_sha256: f9b16c8cb261e014de8456a2e07f321e5c00148db57091d86e8ae710f67e7383
- evidence_id: median-body-agent-dawson-europe
  kind: primary_source
  reference: https://europepmc.org/articles/PMC2168246
  locator: HTTP403 response
  accessed_at: '2026-10-21T07:31:00.210249Z'
  support: unknown
  summary: Europe PMC HTML request unavailable.
  snapshot_sha256: 885701c3aded994941c58b07bd5bdec9065c92418b62153aa560e6eba0da5399
- evidence_id: median-body-agent-dawson-jats
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2168246/fullTextXML
  locator: HTTP500 response
  accessed_at: '2026-10-21T07:29:37.622859Z'
  support: unknown
  summary: Full text not obtained by Europe PMC XML route.
  snapshot_sha256: 6de75c3d7d30f3386b4a9491c7ad7b782a5e4f46fe9836d28f05cd88232a5ef2
- evidence_id: median-body-agent-dawson-legacy
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2168246/
  locator: Methods strain/culture, cloning/GFP/S280N, immunostaining/measurement,
    drug treatments; Results Figs1–6/Table2; Discussion median-body subsection
  accessed_at: '2026-10-21T07:31:00.528835Z'
  support: supports
  summary: Actual PMC article HTML. All median-body Results/Discussion, relevant Methods
    and main captions read. See claim_scope.
  snapshot_sha256: 62c2fa4d97c94fbc4a1f7545496d334e40704d6fe17c9f6dac21825bf66aa297
- evidence_id: median-body-agent-dawson-pdf
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2168246/pdf/0128-07.pdf
  locator: HTTP200 short HTML response
  accessed_at: '2026-10-21T07:31:00.322905Z'
  support: unknown
  summary: Not a PDF or article body; not used as scientific evidence.
  snapshot_sha256: 2b6e42ade1fb692f53fbec452e3f8802047752d1308fd5455e067a15d501bcc7
- evidence_id: median-body-agent-dawson-s3
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2168246.1/PMC2168246.1.xml
  locator: HTTP404 XML response
  accessed_at: '2026-10-21T07:30:33.686254Z'
  support: unknown
  summary: Exact S3 object unavailable; does not prove paper lacks free full text
    elsewhere.
  snapshot_sha256: f13695f0c880abcdd757a9114c60eaa04dbb9ba6cc0d7361806955b37725a749
- evidence_id: median-body-agent-dawson2007
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2168246/
  locator: HTML title/body
  accessed_at: '2026-10-21T07:29:36.992414Z'
  support: unknown
  summary: HTTP200 reCAPTCHA; not full text.
  snapshot_sha256: a7822632733306e99163658f5a5272cc104c7ad5adea5ae4b53bf2de3cd93df8
- evidence_id: median-body-agent-epmc
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1083/jcb.29.2.317%20OR%20DOI:10.1016/j.biolcel.2004.05.006%20OR%20DOI:10.1128/EC.00128-07%20OR%20DOI:10.1016/bs.apar.2019.11.001&format=json&resultType=core
  locator: Four exact DOI results; all abstracts read
  accessed_at: '2026-10-21T07:29:12.841538Z'
  support: supports
  summary: Friend1966 PMID5961344/PMC2106914; Piva2004 PMID15567529; Dawson2007 PMID17766466/PMC2168246;
    Hagen2020 PMID32122531/PMC8086724. Piva abstract directly reports anti-tubulin
    and anti-beta-giardin reactivity and variable number/shape/position.
  snapshot_sha256: bdbfcb512af7c0bd1b03a79b1d27d4db2805c74cbe67ffa9317e925a46c2ee05
  search_scope: Europe PMC core lookup restricted to the four explicitly listed DOI
    values; all four returned records and abstracts inspected. This is a bounded citation
    lookup, not a comprehensive literature search. Ignored local files are not applicable
    to this remote query.
- evidence_id: median-body-agent-friend-meta
  kind: database
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2106914.1/PMC2106914.1.json
  locator: DOI/PMID/title/version, XML/PDF native checksums
  accessed_at: '2026-10-21T07:31:51.787159Z'
  support: supports
  summary: Identity and downloaded-byte checks verified below.
  snapshot_sha256: c8fb3899ced543805b343707967e8e25f1e6fe9c45e064a2b312706badfed083
- evidence_id: median-body-agent-friend1966-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2106914.1/PMC2106914.1.xml
  locator: Native article JATS body; abstract and median-body text
  accessed_at: '2026-10-21T07:29:37.206603Z'
  support: supports
  summary: Supports G.muris ultrastructure; native historical text corroborated against
    scanned PDF.
  snapshot_sha256: 31658a6fe24a8d21770d9abbf89c02a2ad12fa1e191d1744488625948a904298
- evidence_id: median-body-agent-friend1966-pdf
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2106914.1/PMC2106914.1.pdf
  locator: pp318–319 Methods and general configuration; p323 Median Body; p324 Figs12–13
    caption; p328 Discussion Median Body
  accessed_at: '2026-10-21T07:29:37.638211Z'
  support: supports
  summary: G.muris trophozoites in mouse duodenum, in-situ chemical fixation and thin-section
    EM. Curved non-membrane-bound tubule aggregate described. No quantitative claim
    imported into target.
  snapshot_sha256: a5564e57c80223abcab7f374a88dc059dab11f6481f596609da95f21b2ba2668
- evidence_id: median-body-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097568,GO:0005856,GO:0005874
  locator: 'Three GO results: definition/synonym/aspect/isObsolete/children'
  accessed_at: '2026-10-21T07:29:12.637119Z'
  support: supports
  summary: Exact median-body definition and RELATED parabasal-body synonym match current
    active CC term. Microtubule definition explicitly describes alpha/beta polymeric
    tubulin. Cytoskeleton lists median body as part_of child.
  snapshot_sha256: b9dbeda1272971811afcd7fc1f2ecff99c4f7eb0ef62f8499765a67ee6325c7b
- evidence_id: median-body-agent-go-graph
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FGO_0097568/graph
  locator: edges with source GO_0097568
  accessed_at: '2026-10-21T07:31:00.721876Z'
  support: supports
  summary: Explicit BFO_0000050 part_of GO_0005856; BFO_0000051 has_part GO_0005874;
    RO_0002162 in_taxon NCBITaxon_5740. Strong direct relation evidence.
  snapshot_sha256: add88681db421767de0a28dd9e4c8f77d708e7173f029b7c88c4947b2cd1d529
- evidence_id: median-body-agent-go-haspart
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097568/paths/GO:0005874?relations=has_part
  locator: HTTP400 JSON response
  accessed_at: '2026-10-21T07:29:37.467697Z'
  support: unknown
  summary: QuickGO rejects has_part path parameter; not evidence that relation is
    absent.
  snapshot_sha256: 973138444d0b8caef26e8168afcec5acdb53ec45a4b7e9a2a6651c53d8e25f86
- evidence_id: median-body-agent-go-ols
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0097568
  locator: GO:0097568 term, definitions and relation-link URLs
  accessed_at: '2026-10-21T07:29:37.674585Z'
  support: context_only
  summary: Definition verified; links alone do not identify has_part target.
  snapshot_sha256: fb538f83b0cabc892eaa90c21caf1ced8a50ec007c9c7842f464f6903fb1ce07
- evidence_id: median-body-agent-go-ols-haspart
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FGO_0097568/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBFO_0000051
  locator: OLS relation-link response embedded terms
  accessed_at: '2026-10-21T07:30:34.410844Z'
  support: unknown
  summary: Returned multiple terms spanning different relations; not used alone as
    typed relation evidence.
  snapshot_sha256: b57758a5dde7ca06ae3e702ca51552f7fecd532870006ea107026d60c63dc552
- evidence_id: median-body-agent-go-relations
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097568/paths/GO:0005575?relations=is_a,part_of
  locator: GO:0097568 paths to CC root
  accessed_at: '2026-10-21T07:29:12.632606Z'
  support: supports
  summary: Direct part_of GO:0005856; separate is_a GO:0110165. No is_a/cytoskeleton
    conflation.
  snapshot_sha256: b9e0e6b842023bd23a013710ab29204484039def1b45c9c8e3ee062aa351d2c5
- evidence_id: median-body-agent-hardin-author-pdf
  kind: primary_source
  reference: https://vnminin.github.io/papers/Hardin2017.pdf
  locator: Hardin et al2017 DOI10.1073/pnas.1705096114; pE5855 Results first subsection;
    Fig1 caption; pE5862 Materials and Methods
  accessed_at: '2026-10-21T07:32:31.303225Z'
  support: supports
  summary: Public coauthor-hosted article PDF. Relevant reservoir Results, Fig1 caption
    and imaging/strain Methods read; not a full-paper scientific audit. See claim_scope.
  snapshot_sha256: f0899ad47d697c588f90c7a1cea03c790705d97e772de9646c31fe9e69418c45
- evidence_id: median-body-agent-hardin-jats
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5530689/fullTextXML
  locator: Europe PMC XML HTTP500
  accessed_at: '2026-10-21T07:32:09.495115Z'
  support: unknown
  summary: Not article text.
  snapshot_sha256: 1795d28285af73cf00a46ec842492cd685462a756933e4868f9aa6b668be3625
- evidence_id: median-body-agent-hardin-legacy
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5530689/
  locator: HTTP200 HTML title/body
  accessed_at: '2026-10-21T07:32:08.716630Z'
  support: unknown
  summary: Not article text.
  snapshot_sha256: 039c474467a8555fc6e5bddeb267cac683a6b1b16e7c555029c6775f5ff02ad9
- evidence_id: median-body-agent-hardin2017
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5530689.1/PMC5530689.1.xml
  locator: Exact S3 XML HTTP404
  accessed_at: '2026-10-21T07:31:51.699809Z'
  support: unknown
  summary: No source body recovered by this route.
  snapshot_sha256: 926029daa8c2c939de3f840d9c54b1396938d41b2110e065ad6719d6a7b6b7ba
- evidence_id: median-body-agent-piva-html
  kind: primary_source
  reference: https://onlinelibrary.wiley.com/doi/full/10.1016/j.biolcel.2004.05.006
  locator: Wiley full article HTTP403
  accessed_at: '2026-10-21T07:30:33.828103Z'
  support: unknown
  summary: No body obtained. Browser full route unavailable; ScienceDirect browser403.
    No fulltext inferred from search snippets.
  snapshot_sha256: 97fbc15f583e0cc60adbe0df2575f9dd1513a30bc5b8c6a5d4415405d8a9a2f1
- evidence_id: median-body-agent-piva2004
  kind: primary_source
  reference: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1016/j.biolcel.2004.05.006
  locator: Wiley pdfdirect HTTP403
  accessed_at: '2026-10-21T07:29:36.856797Z'
  support: unknown
  summary: No full PDF obtained from this route; source remains abstract-only in this
    preparation.
  snapshot_sha256: 759a094e27ec5937818a2ee472a9e7ff8c6218d131f575dc1787276537b74538
- evidence_id: median-body-agent-review-meta
  kind: database
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC8086724.1/PMC8086724.1.json
  locator: PMC8086724.1 DOI/PMID/title, manuscript and TDM license metadata
  accessed_at: '2026-10-21T07:30:33.756110Z'
  support: supports
  summary: Author manuscript NIHMS1664321; is_pmc_openaccess false; license_code TDM.
    Readable public native XML does not authorize corpus image hosting. XML native
    checksum verified.
  snapshot_sha256: a3f177987076cf229d3c0dd499b9f31b30e7e9db0d1c4aca6885dbbcc3f663ce
- evidence_id: median-body-agent-review-s3
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC8086724.1/PMC8086724.1.xml
  locator: Section5 S5/P23–P24, reference R59; Table1 relevant rows
  accessed_at: '2026-10-21T07:30:34.071674Z'
  support: supports
  summary: Literature-review manuscript, not a new primary experiment. Median-body
    architecture/dynamics and competing function hypotheses read. Review calls function
    enigmatic while citing primary live-cell evidence supporting tubulin reservoir.
    Table1 is a source inventory, not new native family/accession grounding.
  snapshot_sha256: e94a97234e02daf25a3a3de12b4f6f86f8bcacd85629b39202fd195c4b7c8894
- evidence_id: median-body-agent-review2020
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC8086724/
  locator: HTML title/body
  accessed_at: '2026-10-21T07:29:36.972551Z'
  support: unknown
  summary: HTTP200 reCAPTCHA, not full text; later native S3 recovery succeeded.
  snapshot_sha256: 3bb51ef712dc0e511eb951850537645ac1422faabd780c46b61281ef70ada05b
- evidence_id: median-body-agent-species
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5741
  locator: taxId5741, scientificName, rank, otherNames
  accessed_at: '2026-10-21T07:29:12.640114Z'
  support: supports
  summary: Current preferred name Giardia duodenalis, species; Giardia intestinalis
    and Giardia lamblia are explicit synonyms. Record uses recognized synonym of same
    taxon.
  snapshot_sha256: 1dcdc380972a71a0a24c80755d8bbacdcb0b6d9988bb5fb1e05ba43f50580dd3
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/median_body.yaml
  locator: 'Entire YAML: definition, synonymy, topology, two components, taxon rows,
    all graph edges and both discussions'
  accessed_at: '2026-10-21T07:35:52Z'
  support: context_only
  summary: The complete maintained record was read. It distinguishes tubulin constituents
    from associated Kinesin-13, leaves exact family/protein boundaries and physiological
    function unresolved, and does not assert a complete mechanistic pathway or invariant
    volume response.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/median_body.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T07:27:40Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/median_body.yaml'
  snapshot_sha256: cdd733b9640add9ba66edf2f3a1c8f52344903b0a1b45c6cf337b92d075dedb3
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/median_body.yaml --out
    /private/tmp/cellstructure-batch8-20261021-q561gvty/median_body-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T07:27:48Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/median_body.yaml\
    \ --out /private/tmp/cellstructure-batch8-20261021-q561gvty/median_body-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch8-20261021-q561gvty/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch8-20261021-q561gvty/median_body-strict.tsv"
  snapshot_sha256: d136bf9c5b649d78741dea7d0302ccce8edbdf6f4cf77d507a927603d883288b
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/median_body.yaml; exact collect() scope; snapshot_sha256
    identifies the entire original reports/curie_check.tsv, not the extracted resolver-slice.json
  accessed_at: '2026-10-21T07:35:52Z'
  support: supports
  summary: '8 of 8 collected target identifiers returned OK at the unchanged base.
    Residuals: none. Source-native identity checked separately.'
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
  topic: Giardia median-body identity and morphology
  outcome: supported
  target_ids:
  - GO:0097568
  summary: Active GO0097568 exactly supplies the nonmembranous semi-organized microtubule-array
    definition, position and related parabasal-body synonym. Friend1966 supports a
    curved aggregate in G.muris; Piva2004 abstract and the later review support the
    distinct array without importing a fixed count, dimension, orientation or universal
    absence of connections across species.
  evidence_ids:
  - median-body-agent-go
  - median-body-agent-friend1966-jats
  - median-body-agent-friend1966-pdf
  - median-body-agent-epmc
  - median-body-agent-review-s3
  - record
- assessment_id: topology
  area: representation
  topic: Cytoskeleton parthood and microtubule parts
  outcome: supported
  target_ids:
  - GO:0097568
  summary: Native OLS graph explicitly gives BFO0000050 part_of cytoskeleton and BFO0000051
    has_part microtubule, with the term as relation source. QuickGO corroborates the
    part_of edge. The failed has_part-path query and ambiguous OLS traversal are not
    treated as relation absence or typed target evidence.
  evidence_ids:
  - median-body-agent-go
  - median-body-agent-go-graph
  - median-body-agent-go-relations
  - median-body-agent-go-haspart
  - median-body-agent-go-ols
  - median-body-agent-go-ols-haspart
  - record
- assessment_id: composition
  area: evidence
  topic: Tubulin constituents versus associated regulator
  outcome: supported
  target_ids:
  - GO:0097568
  summary: GO0005874 explicitly grounds alpha/beta-tubulin polymer composition; anti-tubulin
    reactivity in Piva and anti-alpha-tubulin imaging in Dawson support the array.
    Kinesin-13 GFP localization supports associated machinery, distinct from the structural
    constituent. Beta-giardin antibody reactivity is retained as a boundary TODO and
    is not converted to an exact accession, stoichiometry or experimentally complete
    inventory.
  evidence_ids:
  - median-body-agent-go
  - median-body-agent-epmc
  - median-body-agent-dawson-legacy
  - record
- assessment_id: grounding
  area: grounding
  topic: Label-only classes and unresolved exact protein mappings
  outcome: supported
  target_ids:
  - GO:0097568
  summary: No unsupported accession is supplied for the alpha/beta class or Giardia
    Kinesin-13. A generic tubulin superclass or kinesin motor domain would not, by
    itself, establish an exact match to these component classes. The primary study
    reports a sole Giardia Kinesin-13 homolog; no modern exhaustive family mapping
    was performed here. Historical no-exact-mapping notes and the explicit TODO do
    not alone establish a curation defect.
  evidence_ids:
  - median-body-agent-go
  - median-body-agent-dawson-legacy
  - median-body-agent-review-s3
  - record
- assessment_id: localization
  area: graph
  topic: Kinesin-13 and EB1 localization scope
  outcome: supported
  target_ids:
  - GO:0097568
  summary: Dawson GFP fusions localize Kinesin-13 and EB1 to the median body and other
    dynamic microtubule arrays. The target captures Kinesin-13 localization and acknowledges
    EB1 in prose; it does not claim exclusive residence, indispensability, direct
    binding to a defined plus end within every median body, or a complete regulator
    inventory.
  evidence_ids:
  - median-body-agent-dawson-legacy
  - record
- assessment_id: perturbation
  area: graph
  topic: Condition-specific S280N volume response
  outcome: supported
  target_ids:
  - GO:0097568
  summary: Dawson compares WBC6/ATCC50803 cells with or without 48 h induction of
    an ectopic GFP-tagged S280N rigor construct by doxycycline withdrawal, using anti-alpha-tubulin
    and 3D volume analysis. The induced comparison gives smaller median-body volumes,
    while early-mitotic mutant arrays can elongate and persist. The record describes
    changes/modulation of volume and cites the decrease from the assay; this does
    not assert that every cell-cycle state responds in the same direction or that
    isolated motor activity was reconstituted.
  evidence_ids:
  - median-body-agent-dawson-legacy
  - record
- assessment_id: function
  area: scope
  topic: Reservoir evidence and unresolved physiological function
  outcome: supported
  target_ids:
  - GO:0097568
  summary: The current GO definition and 2020 review retain uncertain/enigmatic function.
    Hardin2017 provides primary live mNeonGreen-beta-tubulin imaging in which median-body
    signal decreases as spindles, discs and nascent flagella assemble; the authors
    interpret this as reservoir support. That evidence strengthens the reservoir hypothesis
    but does not directly trace isolated tubulin transfer, specifically ablate/rescue
    median-body function, or resolve competing proposals. Leaving a settled biological-process
    function unasserted is defensible.
  evidence_ids:
  - median-body-agent-go
  - median-body-agent-review-s3
  - median-body-agent-hardin-author-pdf
  - record
- assessment_id: taxon
  area: scope
  topic: Species synonyms, experimental strain and cell state
  outcome: supported
  target_ids:
  - GO:0097568
  summary: Native taxon5741 currently prefers Giardia duodenalis and explicitly includes
    Giardia intestinalis and Giardia lamblia as synonyms. The maintained label therefore
    denotes the same species. Dawson uses WBC6/ATCC50803 trophozoites, whereas Friend
    describes G.muris; their detailed experimental observations are not conflated.
    Common trophozoite occurrence does not mean presence at every cell-cycle stage
    or a universal fixed number.
  evidence_ids:
  - median-body-agent-species
  - median-body-agent-epmc
  - median-body-agent-dawson-legacy
  - median-body-agent-friend1966-pdf
  - record
- assessment_id: access
  area: provenance
  topic: Actual source readability and native bytes
  outcome: supported
  target_ids:
  - GO:0097568
  summary: Relevant Friend historical primary text/PDF and Dawson article HTML are
    readable. The2020 source is a readable public author manuscript, and Hardin is
    a public coauthor-hosted PDF; their content and roles are distinguished. Piva
    remains abstract-only, with failed publisher routes preserved. Native MD5 confirms
    Friend XML/PDF and review XML bytes. No target image is present and no image license
    is inferred from public text accessibility.
  evidence_ids:
  - median-body-agent-epmc
  - median-body-agent-friend-meta
  - median-body-agent-friend1966-jats
  - median-body-agent-friend1966-pdf
  - median-body-agent-dawson-legacy
  - median-body-agent-review-meta
  - median-body-agent-review-s3
  - median-body-agent-hardin-author-pdf
  - median-body-agent-piva-html
  - median-body-agent-piva2004
  - record
- assessment_id: completeness
  area: completeness
  topic: Bounded structural and dynamics representation
  outcome: supported
  target_ids:
  - GO:0097568
  summary: The target represents the defining microtubule array, constituent class,
    experimentally localized regulator, canonical species and supported dynamics relationship.
    It explicitly leaves exact protein boundaries, further associated material and
    physiological function open. No exact family match or required complete inventory
    was established that would convert those optional omissions into a finding.
  evidence_ids:
  - median-body-agent-go
  - median-body-agent-epmc
  - median-body-agent-dawson-legacy
  - median-body-agent-review-s3
  - median-body-agent-hardin-author-pdf
  - record
findings: []
actions: []
limitations:
- Piva2004 was inspected at abstract tier only; publisher HTML and PDF retrieval returned
  403. Original antibody methods, controls and detailed counts were not independently
  recovered.
- Friend1966 describes chemically fixed G.muris trophozoites from mouse duodenum.
  Its detailed dimensions, connections and incidence were not generalized to WBC6
  or all Giardia species.
- Dawson volume effects depend on ectopic S280N induction and cell-cycle context.
  Smaller volumes at 48 h and elongated/persistent early-mitotic arrays are distinct
  observations; raw volumes and normalized ratios were not conflated.
- Hardin2017 reservoir inference comes from live fluorescent tubulin redistribution.
  Imaging used WBC6, albendazole pretreatment/washout, SB5050, 37°C and controlled
  hypoxia; drug-free DIC timing was a separate experiment. No isolated molecular-transfer,
  median-body depletion/rescue or purified reconstitution claim is made.
- Relevant body text and captions were read; microscopy pixels, movies and raw data
  were not independently reanalyzed. The Hardin paper was inspected only for the reservoir
  and relevant methods passages.
- No exhaustive family/accession enrichment was performed. Broad family or domain
  resemblance is not proof of an exact match to the recorded alpha/beta-tubulin or
  Giardia-specific Kinesin-13 classes.
- The2020 review is contextual literature, not an independent primary experiment.
  Its publicly readable native manuscript has TDM metadata and does not confer an
  image-reuse license.
- Current review does not reconstruct every historical curation decision or establish
  independent historical authorship.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- The full median_body.yaml is the only substantive local scientific input used. No
  neighboring-record or previous-review scientific judgment informed the assessment.
  All native captured input hashes were rechecked.
- Native focused schema/strict checks passed before assessment. Shared unchanged-base
  gates are documented by the parent reviewer before finalization.
- The parent checked the source-scoped draft before finalization; no maintained scientific
  content was changed.
- Only the review bundle is saved. Maintained scientific content, native status, history
  and generated pages remain unchanged.
```
