# Scientific review of nitroplast

- Review: 20261022T025104Z-nitroplast-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T02:36:19Z
- Finished UTC: 2026-10-22T02:51:04Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Nitroplast identity, restricted FR21/host scope, observed membranes, nitrogenase activity and cautious import evidence are supported. No concrete issue observed; mechanistic and formation limits remain explicit.

## Scope And Provenance

Entire single maintained target at frozen f97b1abe; exact source identities, taxonomy, component/formation distinctions, function, evidence placement, completeness and all asserted graph/image fields.

Selection: Batch35 fixed strict path-order selection, position 1; one maintained record only. Initial focused inspect/schema/strict all passed before review.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:nitroplast | data/structures/membrane_organelle/nitroplast.yaml | maintained | nitroplast |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | cellstructuremech:nitroplast | Focused validator passed. |
| Focused native strict | passed | True | cellstructuremech:nitroplast | Focused validator passed. |
| Graph check applicability | not_applicable | False | cellstructuremech:nitroplast | No causal graph is asserted in the entire target. |
| Individual protein verification applicability | not_applicable | False | cellstructuremech:nitroplast | No structured individual protein example, gene-symbol field or UniProt protein accession is asserted. Named source proteins are checked against the actual primary passage; optional instance enrichment is not required. |
| Expression-module applicability | not_applicable | False | cellstructuremech:nitroplast | No expression-module/regulon claim or covered strain transcriptomic inference is made. |
| Claim-level scientific review | passed | True | cellstructuremech:nitroplast | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | cellstructuremech:nitroplast | 8 of 9 collected target identifiers returned OK. cellstructuremech:nitroplast: SKIPPED; Unique exact locally minted identifier verified in the complete frozen target and gitignore-independent corpus search; source evidence supports the bounded named structure. Local identity is not an external authority resolution. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | cellstructuremech:nitroplast | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | cellstructuremech:nitroplast | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | cellstructuremech:nitroplast | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | cellstructuremech:nitroplast | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | cellstructuremech:nitroplast | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Local identity and structural hierarchy

identity: supported. Targets: cellstructuremech:nitroplast.

Nitroplast is the UCYN-A-derived intracellular nitrogen-fixing organelle, distinct from the host taxon and other nitrogen-fixing symbionts. Broad intracellular-organelle parentage avoids an unsupported exact membrane-count assertion. Related spheroid-body synonym is appropriately qualified.

### Verified host and strain boundaries

scope: supported. Targets: cellstructuremech:nitroplast.

Host taxon is exact. The distribution note accurately narrows to genotypeIII and distinguishes bearing FR12/FR21 from culture loss in KC1-P2, rather than asserting wild-population frequency. The canonical FR21/NIES4399 and UCYN-A2 context agree with the primary paper and supplement.

### Membrane and nitrogenase constituents

grounding: supported. Targets: cellstructuremech:nitroplast.

The membrane system is accurately labeled OTHER and GO0016020, with UNKNOWN necessity; repository tests explicitly permit structural OTHER constituents. This is not a claim that a whole membrane is one lipid molecule. Nitrogenase complex identity is exact and supported by NifH enrichment plus activity without invented subunit stoichiometry.

### Assembly necessity and molecular detail

grounding: unknown. Targets: cellstructuremech:nitroplast.

Neither membrane imaging nor enzyme activity establishes a specific molecular formation requirement. Both target components correctly remain UNKNOWN; detailed lipid/protein inventory, import machinery and exact membrane count are not established by this review.

### Nitrogen fixation and host protein import

evidence: supported. Targets: cellstructuremech:nitroplast.

The primary activity assay supports nitrogen fixation in the stated FR21 culture context; enrichment supports organelle-level host protein import. The target correctly separates detected proteins from predicted-only uTP candidates and does not claim proven cleavage, ATP transfer, translocon identity or a causal transport pathway.

### Link-only TEM provenance

evidence: supported. Targets: cellstructuremech:nitroplast.

The actual Table2 and Fig28–31 pixels were inspected. Label, modality, scale, strain distinction and PDF page locator match. The original copyright notice supports the link-only OTHER-license treatment; no redistribution permission is inferred.

### Complete bounded record review

completeness: supported. Targets: cellstructuremech:nitroplast.

All target fields and discussions were assessed. No causal graph or individual protein accession is asserted. Open mechanistic questions and conservative mapping status are retained; historical source-access statements are not contradicted merely by current retrieval differences.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/nitroplast.yaml; Entire maintained target, including all history, graph nodes/edges, evidence notes and discussions | context_only | All target bytes read; no maintained scientific content changed. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent and grounding; ComponentTypeEnum; EssentialityEnum and PresenceEnum | context_only | OTHER is expressly allowed without a chemical description. LIPID groundings concern a molecular lipid identity; a whole anatomical membrane is a distinct entity. Essentiality means whether the structure forms without the constituent, not cell survival or catalytic function. |
| other-test | tests/test_trypanosome_structure_evidence.py; test_faz1_rnai_does_not_establish_null_assembly_essentiality, assertion for faz_filament component_type OTHER | context_only | Repository contract explicitly retains a structural filament constituent as OTHER. This supports distinguishing accurate structural OTHER entries from chemical LIPID-to-location mismatches; no other FAZ biology is assessed. |
| nitroplast-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043229,GO:0016020,GO:0016610,GO:0009399; Complete QuickGO results: GO0043229/0016020/0016610/0009399; exact names, definitions, obsolete flags | supports | Four active terms correctly identify intracellular organelle, membrane, nitrogenase complex and nitrogen fixation. The membrane term denotes a lipid/protein sheet, not a chemical lipid; the target uses OTHER. Nitrogenase is a named subcomplex. |
| nitroplast-agent-go-search-nitroplast | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=nitroplast&amp;limit=100; Complete native response for query=nitroplast, limit=100 | context_only | The bounded current native query returns zero results for nitroplast. It supports retaining this local identifier without claiming an exhaustive ontology synonym or future-term absence. |
| nitroplast-agent-tax373042 | https://rest.uniprot.org/taxonomy/373042.json; Complete JSON taxonId, scientificName, active, rank and lineage | supports | Active species taxon373042 is Braarudosphaera bigelowii under Haptophyta/Prymnesiophyceae. The native entry alone does not encode the 2026 sensu-stricto strain revision or a population frequency. |
| nitroplast-agent-coale2024-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1126/science.adk1075; Unique result identity and complete abstractText | supports | Exact DOI, PMID38603509, title, authors/year and complete abstract match the 2024 primary study. |
| nitroplast-agent-coale2024-main-page1 | https://html.scribdassets.com/5pd08as4w0cdtz4x/pages/1-6ee1ae9510.jsonp; Printed217, page1; title/abstract, introduction and architecture Results; genuine publicly rendered page content, gzip-compressed JSONP bytes retained; decoded text is only a derivative | supports | The primary paper defines the early-stage nitrogen-fixing organelle and its membrane enclosure in cultured coastal UCYN-A2/B. bigelowii; SXT examines its cell architecture and coordinated division. |
| nitroplast-agent-coale2024-main-page3 | https://html.scribdassets.com/5pd08as4w0cdtz4x/pages/3-56a5ec096d.jsonp; Printed219, page3; nuclear-encoded protein import Results and Fig2 caption; genuine publicly rendered page content, gzip-compressed JSONP bytes retained; decoded text is only a derivative | supports | Fractionation and proteomics show NifH enrichment and host-encoded proteins enriched in isolated UCYN-A; this supports the record's cautious organelle-level import statement, not individual candidate validation or stoichiometry. |
| nitroplast-agent-coale2024-main-page4 | https://html.scribdassets.com/5pd08as4w0cdtz4x/pages/4-3a12e3746a.jsonp; Printed220, page4; uTP Results and Fig3 caption; genuine publicly rendered page content, gzip-compressed JSONP bytes retained; decoded text is only a derivative | supports | Detected/enriched host proteins are distinguished from HMM-only predictions; absent peptides from the C-terminal extension allow cleavage OR lack of translation, rather than proving cleavage or a translocon. |
| nitroplast-agent-coale2024-main-page5 | https://html.scribdassets.com/5pd08as4w0cdtz4x/pages/5-c1a70e6f2c.jsonp; Printed221, page5; concluding Results and UCYN-A as a nitrogen-fixing organelle; genuine publicly rendered page content, gzip-compressed JSONP bytes retained; decoded text is only a derivative | supports | The concluding primary discussion interprets integration/import as organellogenesis while several biochemical assignments remain proposed. The target does not convert these candidate roles into mechanistic edges. |
| nitroplast-agent-coale2024-supp-page2 | https://html.scribdassets.com/4a1aolh8hsce62xa/pages/2-349cb1d046.jsonp; Supplement p2: isolation, cell culture and diel sampling; public unblurred page JSONP, original gzip bytes and source provenance retained | supports | Supplementary Methods explicitly identify FR-21 as NIES-4399 and distinguish N-deplete proteomic cultures from N-replete diel SXT cultures. |
| nitroplast-agent-coale2024-supp-page7 | https://html.scribdassets.com/4a1aolh8hsce62xa/pages/7-952a50e37b.jsonp; Supplement p7: Nitrogen fixation rates, with adjacent protocol context; public unblurred page JSONP, original gzip bytes and source provenance retained | supports | Triplicate exponentially growing N-replete/deplete cultures were assayed during the light period by acetylene reduction and hourly ethylene measurement. This is a nitrogenase-activity assay, not direct nitrogen flux imaging. |
| nitroplast-agent-coale2024-supp-page11 | https://html.scribdassets.com/4a1aolh8hsce62xa/pages/11-ca621b2751.jsonp; Supplement p11: complete FigS3 caption; quantitative plotted pixels not inspected; public unblurred page JSONP, original gzip bytes and source provenance retained | supports | FigS3C caption identifies nitrogenase activity, growth and photosynthetic efficiency comparisons with/without added nitrate; no significant between-treatment difference is claimed. |
| nitroplast-agent-hagino2026-author | https://wakemanlaboratory.com/wp-content/uploads/2026/07/taxonomic-re-evaluation-of-the-braarudosphaera-bigelowii-species-complex-prymnesiophyceae-_compressed.pdf; Cover/title/copyright, printed5 Ultrastructure Methods, printed8 cell structure Results, printed12 Table2/Discussion and printed16 culture-loss discussion; PDFpages13–14 visually inspected Table2 and Fig28–31 pixels/captions | supports | The final author-hosted article identifies genotypeIII as B.bigelowii sensu stricto. Table2 separates FR12/FR21 with nitroplasts from KC1-P2 without; Fig28–29 are FR21, whereas30–31 are OTR22-B/typeI. The thin-section TEM images show one/two Nit bodies and internal lamellae, with 1 micrometer scale. Copyright belongs to International Phycological Society; the record links the PDF rather than hosting an image. |
| nitroplast-agent-li2026-pmc | https://pmc.ncbi.nlm.nih.gov/articles/13104995/; PMC article header; Discussion S10/S11/S12, especially Limitations of structural inference; preprint authority, not a peer-reviewed mechanistic demonstration | supports | Exact DOI/title and Version1 preprint status are present. Discussion explicitly leaves vesicle cargo/direction unresolved and labels static structural evidence as circumstantial for regulated exchange. The record preserves these limits and does not name unidentified densities as constituents. |
| access-coale2024-publisher | https://doi.org/10.1126/science.adk1075; Retained original HTTP response 403, 5561 bytes | context_only | Publisher route returned403; genuine page content was independently recovered from the public reproduction, not from this blocked response. |
| access-coale2024-supp | https://www.science.org/doi/suppl/10.1126/science.adk1075/suppl_file/science.adk1075_sm.pdf; Retained original HTTP response 403, 5745 bytes | context_only | Publisher supplement returned403; separate public page assets carry the protocol evidence. |
| access-hagino2026-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1080/00318884.2026.2660260; Retained original HTTP response 200, 196 bytes | context_only | EuropePMC DOI search returned200 with zero results; bibliographic identity is verified from the final author PDF, not this empty search response. |
| schema-result | just validate data/structures/membrane_organelle/nitroplast.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/nitroplast.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/nitroplast.yaml --out /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/nitroplast-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/nitroplast.yaml --out /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/nitroplast-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch35-20261022-5cl5i1x7/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/nitroplast-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/nitroplast.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 8 of 9 collected target identifiers returned OK. cellstructuremech:nitroplast: SKIPPED; Unique exact locally minted identifier verified in the complete frozen target and gitignore-independent corpus search; source evidence supports the bounded named structure. Local identity is not an external authority resolution. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Coale main pages1/3/4/5 and supplement pages2/7/11 were directly read from a public reproduction with exact page-asset receipts; the publisher returned403. Other downloaded pages and raw omics/supplement data were not treated as inspected evidence.
- Hagino Table2 and Fig28–31 were visually inspected; Coale FigS3 was read as caption/protocol only. No raw microscopy/omics reanalysis, population prevalence estimate or candidate-specific import experiment was performed.
- Li2026 is explicitly a version1 preprint. Its static architecture does not resolve vesicle cargo, directionality, translocon identity, or causal nitrogen-fixation control. OTHER membrane granularity is accepted under the explicit enum and repository test, without treating a location as a chemical lipid identity.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T025104Z-nitroplast-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Scientific review of nitroplast
started_at: '2026-10-22T02:36:19Z'
finished_at: '2026-10-22T02:51:04Z'
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
summary: Nitroplast identity, restricted FR21/host scope, observed membranes, nitrogenase
  activity and cautious import evidence are supported. No concrete issue observed;
  mechanistic and formation limits remain explicit.
source:
  git_revision: f97b1abe2d78971b6f66b9083087d7a94cf3c0cc
  state: working_tree
  inputs:
  - path: .claude/skills/curate-causal-graphs/SKILL.md
    sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
    role: context
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
  - path: data/structures/membrane_organelle/nitroplast.yaml
    sha256: 3f7dc36b6c5e8389c881e64839227e1e5cdde49edb55277e245b180f0de8d6a8
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
  - path: tests/test_trypanosome_structure_evidence.py
    sha256: 7ce1dfa869f9295e836fff7a7956e62685ac291969283c5311e08c7fad5cf79b
    role: context
targets:
- target_id: cellstructuremech:nitroplast
  path: data/structures/membrane_organelle/nitroplast.yaml
  label: nitroplast
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/nitroplast.yaml
    role: maintained scientific record
scope:
  description: Entire single maintained target at frozen f97b1abe; exact source identities,
    taxonomy, component/formation distinctions, function, evidence placement, completeness
    and all asserted graph/image fields.
  selection: Batch35 fixed strict path-order selection, position 1; one maintained
    record only. Initial focused inspect/schema/strict all passed before review.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:nitroplast
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:nitroplast
  command: just validate data/structures/membrane_organelle/nitroplast.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:nitroplast
  command: just validate-strict data/structures/membrane_organelle/nitroplast.yaml
    --out /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/nitroplast-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: focused-causal
  name: Graph check applicability
  status: not_applicable
  required: false
  target_ids:
  - cellstructuremech:nitroplast
  summary: No causal graph is asserted in the entire target.
- check_id: protein-verification
  name: Individual protein verification applicability
  status: not_applicable
  required: false
  target_ids:
  - cellstructuremech:nitroplast
  summary: No structured individual protein example, gene-symbol field or UniProt
    protein accession is asserted. Named source proteins are checked against the actual
    primary passage; optional instance enrichment is not required.
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - cellstructuremech:nitroplast
  summary: No expression-module/regulon claim or covered strain transcriptomic inference
    is made.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:nitroplast
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - other-test
  - nitroplast-agent-go
  - nitroplast-agent-go-search-nitroplast
  - nitroplast-agent-tax373042
  - nitroplast-agent-coale2024-meta
  - nitroplast-agent-coale2024-main-page1
  - nitroplast-agent-coale2024-main-page3
  - nitroplast-agent-coale2024-main-page4
  - nitroplast-agent-coale2024-main-page5
  - nitroplast-agent-coale2024-supp-page2
  - nitroplast-agent-coale2024-supp-page7
  - nitroplast-agent-coale2024-supp-page11
  - nitroplast-agent-hagino2026-author
  - nitroplast-agent-li2026-pmc
  - access-coale2024-publisher
  - access-coale2024-supp
  - access-hagino2026-meta
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - cellstructuremech:nitroplast
  summary: '8 of 9 collected target identifiers returned OK. cellstructuremech:nitroplast:
    SKIPPED; Unique exact locally minted identifier verified in the complete frozen
    target and gitignore-independent corpus search; source evidence supports the bounded
    named structure. Local identity is not an external authority resolution. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.'
  evidence_ids:
  - target-curies
  - record
  - nitroplast-agent-go-search-nitroplast
  - nitroplast-agent-coale2024-main-page1
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:nitroplast
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch35 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:nitroplast
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch35 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:nitroplast
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch35 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:nitroplast
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch35 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - cellstructuremech:nitroplast
  command: just check-curies-strict
  exit_code: 0
  summary: 'Exit0. Native resolver control: every resolver accepts a known id and
    rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE.
    Transport failures and skipped prefixes are not proof of identifier resolution;
    exact target residuals are assessed separately.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:34Z to
    2026-10-22T01:34:04Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch35 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/nitroplast.yaml
  locator: Entire maintained target, including all history, graph nodes/edges, evidence
    notes and discussions
  accessed_at: '2026-10-22T02:44:30Z'
  support: context_only
  summary: All target bytes read; no maintained scientific content changed.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent and grounding; ComponentTypeEnum; EssentialityEnum
    and PresenceEnum
  accessed_at: '2026-10-22T02:44:30Z'
  support: context_only
  summary: OTHER is expressly allowed without a chemical description. LIPID groundings
    concern a molecular lipid identity; a whole anatomical membrane is a distinct
    entity. Essentiality means whether the structure forms without the constituent,
    not cell survival or catalytic function.
- evidence_id: other-test
  kind: record_content
  reference: tests/test_trypanosome_structure_evidence.py
  locator: test_faz1_rnai_does_not_establish_null_assembly_essentiality, assertion
    for faz_filament component_type OTHER
  accessed_at: '2026-10-22T02:44:30Z'
  support: context_only
  summary: Repository contract explicitly retains a structural filament constituent
    as OTHER. This supports distinguishing accurate structural OTHER entries from
    chemical LIPID-to-location mismatches; no other FAZ biology is assessed.
- evidence_id: nitroplast-agent-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043229,GO:0016020,GO:0016610,GO:0009399
  locator: 'Complete QuickGO results: GO0043229/0016020/0016610/0009399; exact names,
    definitions, obsolete flags'
  accessed_at: '2026-10-22T02:37:49.488183Z'
  support: supports
  summary: Four active terms correctly identify intracellular organelle, membrane,
    nitrogenase complex and nitrogen fixation. The membrane term denotes a lipid/protein
    sheet, not a chemical lipid; the target uses OTHER. Nitrogenase is a named subcomplex.
  snapshot_sha256: 412df7210b18568e2aa11e4f7efec86a97394145b5ef53b33e3c8cf3a66946de
- evidence_id: nitroplast-agent-go-search-nitroplast
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=nitroplast&limit=100
  locator: Complete native response for query=nitroplast, limit=100
  accessed_at: '2026-10-22T02:41:59.530541Z'
  support: context_only
  summary: The bounded current native query returns zero results for nitroplast. It
    supports retaining this local identifier without claiming an exhaustive ontology
    synonym or future-term absence.
  snapshot_sha256: f3a7dae9b1e9335291e3940cdf0e5f8dadf9335da7b9547710606b5106c63f86
  search_scope: One native QuickGO term-search endpoint query for nitroplast, limit100;
    complete response numberOfHits0. Ignored files not applicable to this remote query;
    no local-file or exhaustive synonym absence claim.
- evidence_id: nitroplast-agent-tax373042
  kind: database
  reference: https://rest.uniprot.org/taxonomy/373042.json
  locator: Complete JSON taxonId, scientificName, active, rank and lineage
  accessed_at: '2026-10-22T02:37:49.731553Z'
  support: supports
  summary: Active species taxon373042 is Braarudosphaera bigelowii under Haptophyta/Prymnesiophyceae.
    The native entry alone does not encode the 2026 sensu-stricto strain revision
    or a population frequency.
  snapshot_sha256: 6cdee90cb62ead292c1778ba3905353639b5217a8528339f2474849eed0c8441
- evidence_id: nitroplast-agent-coale2024-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1126/science.adk1075
  locator: Unique result identity and complete abstractText
  accessed_at: '2026-10-22T02:37:45.808883Z'
  support: supports
  summary: Exact DOI, PMID38603509, title, authors/year and complete abstract match
    the 2024 primary study.
  snapshot_sha256: ed61bdf32d42189f9daf860c29f2a58e29ebf09793bacc753f6a2dac52b122d3
- evidence_id: nitroplast-agent-coale2024-main-page1
  kind: primary_source
  reference: https://html.scribdassets.com/5pd08as4w0cdtz4x/pages/1-6ee1ae9510.jsonp
  locator: Printed217, page1; title/abstract, introduction and architecture Results;
    genuine publicly rendered page content, gzip-compressed JSONP bytes retained;
    decoded text is only a derivative
  accessed_at: '2026-10-22T02:40:32.534615Z'
  support: supports
  summary: The primary paper defines the early-stage nitrogen-fixing organelle and
    its membrane enclosure in cultured coastal UCYN-A2/B. bigelowii; SXT examines
    its cell architecture and coordinated division.
  snapshot_sha256: 13aaeaf28b4cc8c137e524e6a5f75339de16f2db242c3e8b75181fc61f63ac0e
- evidence_id: nitroplast-agent-coale2024-main-page3
  kind: primary_source
  reference: https://html.scribdassets.com/5pd08as4w0cdtz4x/pages/3-56a5ec096d.jsonp
  locator: Printed219, page3; nuclear-encoded protein import Results and Fig2 caption;
    genuine publicly rendered page content, gzip-compressed JSONP bytes retained;
    decoded text is only a derivative
  accessed_at: '2026-10-22T02:40:32.534777Z'
  support: supports
  summary: Fractionation and proteomics show NifH enrichment and host-encoded proteins
    enriched in isolated UCYN-A; this supports the record's cautious organelle-level
    import statement, not individual candidate validation or stoichiometry.
  snapshot_sha256: 5be8adecfe2e9b69c6a233bde074c621e4748bc075df694e43e6eb9a74c808a5
- evidence_id: nitroplast-agent-coale2024-main-page4
  kind: primary_source
  reference: https://html.scribdassets.com/5pd08as4w0cdtz4x/pages/4-3a12e3746a.jsonp
  locator: Printed220, page4; uTP Results and Fig3 caption; genuine publicly rendered
    page content, gzip-compressed JSONP bytes retained; decoded text is only a derivative
  accessed_at: '2026-10-22T02:40:32.534921Z'
  support: supports
  summary: Detected/enriched host proteins are distinguished from HMM-only predictions;
    absent peptides from the C-terminal extension allow cleavage OR lack of translation,
    rather than proving cleavage or a translocon.
  snapshot_sha256: f0ddd5bd80892e3cfb9455676e5b9b7c7ca83ed9b1798e263fd3c5a8fa613894
- evidence_id: nitroplast-agent-coale2024-main-page5
  kind: primary_source
  reference: https://html.scribdassets.com/5pd08as4w0cdtz4x/pages/5-c1a70e6f2c.jsonp
  locator: Printed221, page5; concluding Results and UCYN-A as a nitrogen-fixing organelle;
    genuine publicly rendered page content, gzip-compressed JSONP bytes retained;
    decoded text is only a derivative
  accessed_at: '2026-10-22T02:40:32.790287Z'
  support: supports
  summary: The concluding primary discussion interprets integration/import as organellogenesis
    while several biochemical assignments remain proposed. The target does not convert
    these candidate roles into mechanistic edges.
  snapshot_sha256: 1201951b6ca91e723644783b27d79d6b2cd5d56d9774d3db5f35dfb5a32e5010
- evidence_id: nitroplast-agent-coale2024-supp-page2
  kind: primary_source
  reference: https://html.scribdassets.com/4a1aolh8hsce62xa/pages/2-349cb1d046.jsonp
  locator: 'Supplement p2: isolation, cell culture and diel sampling; public unblurred
    page JSONP, original gzip bytes and source provenance retained'
  accessed_at: '2026-10-22T02:40:32.838998Z'
  support: supports
  summary: Supplementary Methods explicitly identify FR-21 as NIES-4399 and distinguish
    N-deplete proteomic cultures from N-replete diel SXT cultures.
  snapshot_sha256: f374344d9a46cc2b263d4500baac89a72a34ef5a1274875111c96a699786f57d
- evidence_id: nitroplast-agent-coale2024-supp-page7
  kind: primary_source
  reference: https://html.scribdassets.com/4a1aolh8hsce62xa/pages/7-952a50e37b.jsonp
  locator: 'Supplement p7: Nitrogen fixation rates, with adjacent protocol context;
    public unblurred page JSONP, original gzip bytes and source provenance retained'
  accessed_at: '2026-10-22T02:40:33.068621Z'
  support: supports
  summary: Triplicate exponentially growing N-replete/deplete cultures were assayed
    during the light period by acetylene reduction and hourly ethylene measurement.
    This is a nitrogenase-activity assay, not direct nitrogen flux imaging.
  snapshot_sha256: 7869472ee2ac9289480b322b3a265e6a9363e7c7986694ed69b26fff15d523fe
- evidence_id: nitroplast-agent-coale2024-supp-page11
  kind: primary_source
  reference: https://html.scribdassets.com/4a1aolh8hsce62xa/pages/11-ca621b2751.jsonp
  locator: 'Supplement p11: complete FigS3 caption; quantitative plotted pixels not
    inspected; public unblurred page JSONP, original gzip bytes and source provenance
    retained'
  accessed_at: '2026-10-22T02:40:33.199743Z'
  support: supports
  summary: FigS3C caption identifies nitrogenase activity, growth and photosynthetic
    efficiency comparisons with/without added nitrate; no significant between-treatment
    difference is claimed.
  snapshot_sha256: 9dc4929fd5dde857496109a7d6595f0db51f38fc17acd35726147d57706ef344
- evidence_id: nitroplast-agent-hagino2026-author
  kind: primary_source
  reference: https://wakemanlaboratory.com/wp-content/uploads/2026/07/taxonomic-re-evaluation-of-the-braarudosphaera-bigelowii-species-complex-prymnesiophyceae-_compressed.pdf
  locator: Cover/title/copyright, printed5 Ultrastructure Methods, printed8 cell structure
    Results, printed12 Table2/Discussion and printed16 culture-loss discussion; PDFpages13–14
    visually inspected Table2 and Fig28–31 pixels/captions
  accessed_at: '2026-10-22T02:37:50.707909Z'
  support: supports
  summary: The final author-hosted article identifies genotypeIII as B.bigelowii sensu
    stricto. Table2 separates FR12/FR21 with nitroplasts from KC1-P2 without; Fig28–29
    are FR21, whereas30–31 are OTR22-B/typeI. The thin-section TEM images show one/two
    Nit bodies and internal lamellae, with 1 micrometer scale. Copyright belongs to
    International Phycological Society; the record links the PDF rather than hosting
    an image.
  snapshot_sha256: 8ba2e99a97d10cf23220f0d80dcc3ed3aac1ee1e6b22260036c7cea4544813ac
- evidence_id: nitroplast-agent-li2026-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/13104995/
  locator: PMC article header; Discussion S10/S11/S12, especially Limitations of structural
    inference; preprint authority, not a peer-reviewed mechanistic demonstration
  accessed_at: '2026-10-22T02:37:50.746949Z'
  support: supports
  summary: Exact DOI/title and Version1 preprint status are present. Discussion explicitly
    leaves vesicle cargo/direction unresolved and labels static structural evidence
    as circumstantial for regulated exchange. The record preserves these limits and
    does not name unidentified densities as constituents.
  snapshot_sha256: 6bac37e98a7f2b04dc31623c2a7d39a430c89af942bdecd3bf745069d39c55ca
- evidence_id: access-coale2024-publisher
  kind: authority
  reference: https://doi.org/10.1126/science.adk1075
  locator: Retained original HTTP response 403, 5561 bytes
  accessed_at: '2026-10-22T02:37:45.810080Z'
  support: context_only
  summary: Publisher route returned403; genuine page content was independently recovered
    from the public reproduction, not from this blocked response.
  snapshot_sha256: d93d78eb9d5c96d683985c02cc8569b6194f11b955431191fd80ae764bd96944
- evidence_id: access-coale2024-supp
  kind: authority
  reference: https://www.science.org/doi/suppl/10.1126/science.adk1075/suppl_file/science.adk1075_sm.pdf
  locator: Retained original HTTP response 403, 5745 bytes
  accessed_at: '2026-10-22T02:37:50.718525Z'
  support: context_only
  summary: Publisher supplement returned403; separate public page assets carry the
    protocol evidence.
  snapshot_sha256: 30a1c07c0cd33010831bb35852205fd48c3a59cceb257f21204392f2172e0f5d
- evidence_id: access-hagino2026-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1080/00318884.2026.2660260
  locator: Retained original HTTP response 200, 196 bytes
  accessed_at: '2026-10-22T02:37:45.810342Z'
  support: context_only
  summary: EuropePMC DOI search returned200 with zero results; bibliographic identity
    is verified from the final author PDF, not this empty search response.
  snapshot_sha256: f071b9a66f812235662bc783cbb206244640c7d60e2c732361717801857ccb3b
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/nitroplast.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:36:20Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/nitroplast.yaml'
  snapshot_sha256: be6f6c705331d7dd439537e4b4cfb605847333170c46ecf0d5c33e26a446926b
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/nitroplast.yaml
    --out /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/nitroplast-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:36:21Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/nitroplast.yaml\
    \ --out /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/nitroplast-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch35-20261022-5cl5i1x7/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/nitroplast-strict.tsv"
  snapshot_sha256: a80454cd19b4fe9858005723e533a993d8b8c388181c4f5df43bd88fda12e4d7
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/nitroplast.yaml; native collect() exact
    identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '8 of 9 collected target identifiers returned OK. cellstructuremech:nitroplast:
    SKIPPED; Unique exact locally minted identifier verified in the complete frozen
    target and gitignore-independent corpus search; source evidence supports the bounded
    named structure. Local identity is not an external authority resolution. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.'
  snapshot_sha256: 173c367ec1621e2a96027e149b5cad9f4db0a86f0a3c916455ce192a9aa5f428
- evidence_id: global-qc-result
  kind: validation
  reference: just qc
  locator: Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02
  accessed_at: '2026-10-22T01:05:35Z'
  support: supports
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  snapshot_sha256: 8696c0d603149cee93ac200eaa3ed26c84320204285cd22cca542eb1ae7ba572
- evidence_id: global-history-result
  kind: validation
  reference: just validate-history
  locator: Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02
  accessed_at: '2026-10-22T00:58:37Z'
  support: supports
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  snapshot_sha256: 98a7952c42add0416633f4dee73ff64331e5c6c4c4c8d707e98a152f04fc5b6d
- evidence_id: global-products-result
  kind: validation
  reference: just validate-products
  locator: Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02
  accessed_at: '2026-10-22T00:59:14Z'
  support: supports
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  snapshot_sha256: b5cc67214f5627a654e75cfc335d77d42113d057091884a12094aa1a71447a5e
- evidence_id: global-traits-result
  kind: validation
  reference: just check-trait-links --check
  locator: Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02
  accessed_at: '2026-10-22T00:58:40Z'
  support: supports
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  snapshot_sha256: 6eab64b59433928ec8e0df9b0046dbccf479c84bb0911c315feebc344d536007
- evidence_id: global-curies-result
  kind: validation
  reference: just check-curies-strict
  locator: Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 'Exit0. Native resolver control: every resolver accepts a known id and
    rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE.
    Transport failures and skipped prefixes are not proof of identifier resolution;
    exact target residuals are assessed separately.'
  snapshot_sha256: 00cc5664a9143235d28fb9885fc5c43a8a78c9a9c9f47603b1232e1eddddeac1
assessments:
- assessment_id: identity
  area: identity
  topic: Local identity and structural hierarchy
  outcome: supported
  target_ids:
  - cellstructuremech:nitroplast
  summary: Nitroplast is the UCYN-A-derived intracellular nitrogen-fixing organelle,
    distinct from the host taxon and other nitrogen-fixing symbionts. Broad intracellular-organelle
    parentage avoids an unsupported exact membrane-count assertion. Related spheroid-body
    synonym is appropriately qualified.
  evidence_ids:
  - nitroplast-agent-go
  - nitroplast-agent-go-search-nitroplast
  - nitroplast-agent-coale2024-main-page1
  - record
- assessment_id: taxa
  area: scope
  topic: Verified host and strain boundaries
  outcome: supported
  target_ids:
  - cellstructuremech:nitroplast
  summary: Host taxon is exact. The distribution note accurately narrows to genotypeIII
    and distinguishes bearing FR12/FR21 from culture loss in KC1-P2, rather than asserting
    wild-population frequency. The canonical FR21/NIES4399 and UCYN-A2 context agree
    with the primary paper and supplement.
  evidence_ids:
  - nitroplast-agent-tax373042
  - nitroplast-agent-hagino2026-author
  - nitroplast-agent-coale2024-main-page1
  - nitroplast-agent-coale2024-supp-page2
- assessment_id: composition
  area: grounding
  topic: Membrane and nitrogenase constituents
  outcome: supported
  target_ids:
  - cellstructuremech:nitroplast
  summary: The membrane system is accurately labeled OTHER and GO0016020, with UNKNOWN
    necessity; repository tests explicitly permit structural OTHER constituents. This
    is not a claim that a whole membrane is one lipid molecule. Nitrogenase complex
    identity is exact and supported by NifH enrichment plus activity without invented
    subunit stoichiometry.
  evidence_ids:
  - nitroplast-agent-go
  - nitroplast-agent-hagino2026-author
  - nitroplast-agent-coale2024-main-page3
  - nitroplast-agent-coale2024-supp-page7
  - other-test
  - schema
- assessment_id: formation
  area: grounding
  topic: Assembly necessity and molecular detail
  outcome: unknown
  target_ids:
  - cellstructuremech:nitroplast
  summary: Neither membrane imaging nor enzyme activity establishes a specific molecular
    formation requirement. Both target components correctly remain UNKNOWN; detailed
    lipid/protein inventory, import machinery and exact membrane count are not established
    by this review.
  evidence_ids:
  - nitroplast-agent-hagino2026-author
  - nitroplast-agent-coale2024-main-page3
  - nitroplast-agent-coale2024-supp-page7
  - schema
- assessment_id: function
  area: evidence
  topic: Nitrogen fixation and host protein import
  outcome: supported
  target_ids:
  - cellstructuremech:nitroplast
  summary: The primary activity assay supports nitrogen fixation in the stated FR21
    culture context; enrichment supports organelle-level host protein import. The
    target correctly separates detected proteins from predicted-only uTP candidates
    and does not claim proven cleavage, ATP transfer, translocon identity or a causal
    transport pathway.
  evidence_ids:
  - nitroplast-agent-coale2024-main-page3
  - nitroplast-agent-coale2024-main-page4
  - nitroplast-agent-coale2024-main-page5
  - nitroplast-agent-coale2024-supp-page2
  - nitroplast-agent-coale2024-supp-page7
  - nitroplast-agent-coale2024-supp-page11
  - nitroplast-agent-li2026-pmc
- assessment_id: image
  area: evidence
  topic: Link-only TEM provenance
  outcome: supported
  target_ids:
  - cellstructuremech:nitroplast
  summary: The actual Table2 and Fig28–31 pixels were inspected. Label, modality,
    scale, strain distinction and PDF page locator match. The original copyright notice
    supports the link-only OTHER-license treatment; no redistribution permission is
    inferred.
  evidence_ids:
  - nitroplast-agent-hagino2026-author
  - record
- assessment_id: coverage
  area: completeness
  topic: Complete bounded record review
  outcome: supported
  target_ids:
  - cellstructuremech:nitroplast
  summary: All target fields and discussions were assessed. No causal graph or individual
    protein accession is asserted. Open mechanistic questions and conservative mapping
    status are retained; historical source-access statements are not contradicted
    merely by current retrieval differences.
  evidence_ids:
  - nitroplast-agent-go
  - nitroplast-agent-go-search-nitroplast
  - nitroplast-agent-tax373042
  - nitroplast-agent-coale2024-meta
  - nitroplast-agent-coale2024-main-page1
  - nitroplast-agent-coale2024-main-page3
  - nitroplast-agent-coale2024-main-page4
  - nitroplast-agent-coale2024-main-page5
  - nitroplast-agent-coale2024-supp-page2
  - nitroplast-agent-coale2024-supp-page7
  - nitroplast-agent-coale2024-supp-page11
  - nitroplast-agent-hagino2026-author
  - nitroplast-agent-li2026-pmc
  - record
findings: []
actions: []
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Coale main pages1/3/4/5 and supplement pages2/7/11 were directly read from a public
  reproduction with exact page-asset receipts; the publisher returned403. Other downloaded
  pages and raw omics/supplement data were not treated as inspected evidence.
- Hagino Table2 and Fig28–31 were visually inspected; Coale FigS3 was read as caption/protocol
  only. No raw microscopy/omics reanalysis, population prevalence estimate or candidate-specific
  import experiment was performed.
- Li2026 is explicitly a version1 preprint. Its static architecture does not resolve
  vesicle cargo, directionality, translocon identity, or causal nitrogen-fixation
  control. OTHER membrane granularity is accepted under the explicit enum and repository
  test, without treating a location as a chemical lipid identity.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
