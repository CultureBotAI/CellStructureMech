# Organelle identity, composition and evidence review

- Review: 20261021T110755Z-chloroplast-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T10:40:28Z
- Finished UTC: 2026-10-21T11:07:55Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The exact identity, structural boundaries, scoped composition and descriptive graph are coherent. No concrete curation finding was established; source-access and individual assembly-necessity limits remain explicit.

## Scope And Provenance

Entire single record with exact authority identities, declared source-reading scopes, protein checks where applicable and component/function/graph boundaries.

Selection: Target 7 in batch twenty-one; exact sorted uncovered path at frozen fresh-main revision.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0009507 | data/structures/membrane_organelle/chloroplast.yaml | maintained | chloroplast |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native protein verify | passed | True | GO:0009507 | Focused native command passed; identity/coverage result is distinct from scientific membership. |
| Native protein causal-graphs | passed | True | GO:0009507 | Focused native command passed; identity/coverage result is distinct from scientific membership. |
| Focused native schema | passed | True | GO:0009507 | Focused validator passed. |
| Focused native strict | passed | True | GO:0009507 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0009507 | 17 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | GO:0009507 | No expression-module or transcriptomic inference is made by this structural review. |
| Claim-level scientific review | passed | True | GO:0009507 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0009507 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0009507 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0009507 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0009507 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0009507 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Exact identity and adjacent structure boundaries

identity: supported. Targets: GO:0009507.

Native identifiers and source descriptions distinguish the complete organelle, its double-membrane envelope including the intervening space, individual inner bilayer, and enclosed intermembrane region. Asserted is_a parents and physical parts are coherent. The source-neutral GO definition is not silently expanded to make every plastid photosynthetic.

### Green lineage and model-organism context

scope: supported. Targets: GO:0009507.

The two native taxa are Viridiplantae and Chlamydomonas reinhardtii. The record describes widespread occurrence in photosynthetic green algae/plants and the established chloroplast of the experimental green alga; COMMON does not mean every tissue or every nonphotosynthetic plastid is a chloroplast. Keeling explicitly discusses plastid loss and nonphotosynthetic forms. The Jin abstract supplies direct Chlamydomonas envelope-spanning structure context without identifying a strain. No numerical prevalence estimate is inferred.

### Membrane parts and a bounded import complex

grounding: supported. Targets: GO:0009507.

The membrane rows identify actual organelle parts through exact GO membrane terms; these are not claimed as chemical identifiers for individual lipids. Toc/Tic subcomplexes are valid has_part structures. The composite TOC-TIC row is appropriately label-only because the checked classic GO supercomplex has a different required composition. The source supports14 identified components but neither an accession for the entire complex nor a mandatory exhaustive chloroplast inventory is inferred.

### Assembly requirements remain unknown

evidence: unknown. Targets: GO:0009507.

All four listed component essentialities are UNKNOWN. Photosynthetic activity, protein-import importance and recovery of a structural complex do not establish whole-chloroplast assembly failure after loss of each component class. No universal requirement is inferred from the primary abstract calling translocons essential.

### Photosynthesis and precursor import

evidence: supported. Targets: GO:0009507.

The inspected2011 review passages support chloroplast photosynthetic electron transfer and carbon assimilation. The native process identities and2022 primary abstract support the envelope-spanning precursor-import route. Exact transport kinetics, a substrate-bound trajectory and a molecular assembly sequence are not asserted.

### Eight descriptive topology and import edges

graph: supported. Targets: GO:0009507.

All eight edges retain their NONMECHANISTIC scope: envelope and membrane topology, thylakoid placement and the TOC-TIC import route. The native definitions support the spatial relations. The primary abstract directly describes the structure spanning both membranes and an IMS scaffold/pathway; these coarse edges do not claim experimentally demonstrated motion through every proposed pore.

### Accurate citation identities and bounded access

provenance: supported. Targets: GO:0009507.

The cited bibliography matches native MED metadata. The current source checks preserve HTTP errors and distinguish challenge/error documents from article bodies. No historical source-reading statement, status or history is rewritten. The model-organism example is supported at its declared scope; no new image, raw dataset or verbatim snippet is asserted.

### Bounded record-level coverage

completeness: supported. Targets: GO:0009507.

The entire maintained record and cited claim contexts were inspected at the stated source scopes. Additional exhaustive component inventories, numerical properties, images, traits and expanded mechanisms are optional. No verbatim quotation requires repair, and no status or history rewrite is proposed. This bounded review does not assert exhaustive literature completeness.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/chloroplast.yaml; Entire maintained YAML including history, all evidence notes, components, functions, graph edges and discussions | context_only | All maintained fields were read. No scientific edit or mapping-status promotion is made. |
| policy | docs/CURATION.md; Exact identity, claim-level evidence, material versus localization grounding, and component assembly-essentiality contract | context_only | Family identity, concrete protein examples and structure membership are separate; activity and viability are not by themselves formation assays. Optional inventories are not mandatory. |
| neighbor-chloroplast_envelope | data/structures/membrane_organelle/chloroplast_envelope.yaml; Entire adjacent record, including components, graph and discussions | context_only | Read to check the boundary between whole chloroplast, enclosing envelope, individual inner bilayer and intervening volume. This dependency is not a second review target. |
| neighbor-chloroplast_inner_membrane | data/structures/membrane_organelle/chloroplast_inner_membrane.yaml; Entire adjacent record, including components, graph and discussions | context_only | Read to check the boundary between whole chloroplast, enclosing envelope, individual inner bilayer and intervening volume. This dependency is not a second review target. |
| neighbor-chloroplast_intermembrane_space | data/structures/membrane_organelle/chloroplast_intermembrane_space.yaml; Entire adjacent record, including components, graph and discussions | context_only | Read to check the boundary between whole chloroplast, enclosing envelope, individual inner bilayer and intervening volume. This dependency is not a second review target. |
| root21-sources-chloroplast-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009507,GO:0009534,GO:0009535,GO:0009536,GO:0009570,GO:0009706,GO:0009707,GO:0009941,GO:0010006,GO:0015979,GO:0031897,GO:0045037,GO:0061927; All returned identifiers, names, definitions, aspect, obsolete status and relevant children | supports | Active native GO terms distinguish chloroplast, plastid, envelope, bilayers, stroma and intermembrane space. Definitions and returned child relations support the asserted structural boundaries; process terms are not substituted for organelle identities. |
| root21-sources-ancestors-0009507 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009507/ancestors?relations=is_a,part_of; Complete ancestor response with explicit is_a,part_of query | supports | The native ancestor response identifies the broader structural context of this term. Combined is_a/part_of closure is not used to erase the distinction between type and physical inclusion; exact parent relations are separately checked in returned term children and definitions. |
| root21-sources-NCBITaxon-33090 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/33090; Exact taxId, scientificName, rank, lineage and relevant alternative names | supports | Native ENA taxonomy identifies Viridiplantae at kingdom rank. Only this taxon's identity and names are asserted by this row, not occurrence or experimental stock identity. |
| root21-sources-NCBITaxon-3055 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055; Exact taxId, scientificName, rank, lineage and relevant alternative names | supports | Native ENA taxonomy identifies Chlamydomonas reinhardtii at species rank. Only this taxon's identity and names are asserted by this row, not occurrence or experimental stock identity. |
| root21-sources-doi-10.1098_rstb.2009.0103 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1098/rstb.2009.0103; Complete native bibliography and abstract | supports | Native MED identifies The endosymbiotic origin, diversification and fate of plastids. (Keeling PJ., 2010), PMID 20124341, DOI 10.1098/rstb.2009.0103. Exact bibliography and complete returned abstract were read; any body coverage is separately declared. |
| root21-sources-doi-10.1016_j.cell.2022.10.030 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.cell.2022.10.030; Complete native bibliography and abstract | supports | Native MED identifies Structure of a TOC-TIC supercomplex spanning two chloroplast envelope membranes. (Jin Z, Wan L, Zhang Y, Li X, Cao Y, Liu H, Fan S, Cao D, Wang Z, Li X, Pan J, Dong MQ, Wu J, Yan Z., 2022), PMID 36413996, DOI 10.1016/j.cell.2022.10.030. Exact bibliography and complete returned abstract were read; any body coverage is separately declared. |
| root21-sources-keeling2010-pmc | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2817223/; Actual source-access response, not article content | context_only | Native legacy PMC returned a recaptcha challenge with HTTP200, not article content. It is not treated as a full-text read. |
| root21-sources-keeling2010-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2817223/fullTextXML; Actual source-access response, not article content | context_only | Europe PMC fullTextXML returned500; no article body was obtained from this response. |
| root21-sources-keeling2010-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2817223.1/PMC2817223.1.xml; Actual source-access response, not article content | context_only | The attempted public OA version1 XML key returned404; this says nothing about the validity or scientific support of the cited paper. |
| root21-sources-keeling2010-repository | https://marinebiology.pt/beu/files/bib/Keeling2010.pdf; Actual source-access response, not article content | context_only | The independently discovered repository PDF route returned403; no PDF was read. |
| root21-sources-keeling2010-bioc | https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC2817223/unicode; Actual source-access response, not article content | context_only | The public NCBI BioC route returned an error document with HTTP200 and no article result, not a usable body. |
| root21-sources-jin2022-publisher | https://www.sciencedirect.com/science/article/pii/S0092867422013769; Actual source-access response, not article content | context_only | The native ScienceDirect route returned403; source-specific TOC-TIC support in this review is limited to the complete native primary abstract. |
| root21-sources-jin2022-author-publications | https://lifesciences.westlake.edu.cn/labs/zhen-yan/structural-biology-laboratory/publications/; Actual source-access response, not article content | context_only | The corresponding author laboratory publications page returned403. No full-paper access is inferred. |
| root21-sources-doi-10.1007_s00294-011-0339-1 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1007/s00294-011-0339-1; Complete native bibliography and abstract | supports | Native MED identifies The chloroplast proteome: a survey from the Chlamydomonas reinhardtii perspective with a focus on distinctive features. (Terashima M, Specht M, Hippler M., 2011), PMID 21533645, DOI 10.1007/s00294-011-0339-1. Exact bibliography and complete returned abstract were read; any body coverage is separately declared. |
| root21-sources-terashima2011-pdf | https://link.springer.com/content/pdf/10.1007/s00294-011-0339-1.pdf; Published pages151–152 Abstract/Introduction and initial proteomics/contamination discussion; Photosynthesis section from heading through LHCSR/CAS discussion on pages154–156; Carbon metabolism section on pages156–157 through its final paragraph. Figure pixels, supplements and the full remaining review were not read. | supports | The publisher PDF reviews the experimental Chlamydomonas chloroplast proteome and comparison with higher plants, emphasizing contamination control and the difference between predicted and experimental localization. Read passages support thylakoid photosynthetic machinery and chloroplast carbon assimilation without turning the list into a complete native inventory. |
| root21-sources-GO0061927 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0061927; Exact identifier, definition, active status and aspect | supports | Active GO0061927 is TOC-TIC supercomplex I and its definition requires a classic constituent set including Tic110. The Jin2022 abstract instead reports Tic20/YlmG architecture and Toc120/Toc75; this candidate cannot be adopted solely because its name resembles the grouped component. |
| native-verify | /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast.yaml --verify; Exact focused native output | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast.yaml --causal-graphs; Exact focused native output | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/membrane_organelle/chloroplast.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/chloroplast.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/chloroplast.yaml --out /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/chloroplast-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/chloroplast.yaml --out /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/chloroplast-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch21-20261021-jc4u1a6u/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/chloroplast-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/chloroplast.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 17 of17 collected target identifiers returned OK in this fresh base resolver run. Residuals: none. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Jin2022 and Keeling2010 were read through complete native abstracts and bibliographic metadata only; multiple legitimate full-text routes failed or returned challenge/error documents. No full-body, Methods, figure-pixel or supplement audit of those papers is claimed.
- Taxon-wide occurrence is assessed qualitatively at the maintained scope, not as a measured prevalence percentage. The review does not assert every cell of Viridiplantae carries chlorophyll-containing chloroplasts.
- The separate neighboring records were read only for boundaries; this review has exactly one target. No exhaustive family/ontology absence search or new molecular inventory is claimed.
- Terashima2011 publisher PDF was read only at the specified proteome, photosynthesis and carbon-metabolism passages. Its full protein table, figures, supplements and underlying raw proteomics were not reanalysed.
- No raw microscopy or quantitative datasets were reanalysed. Historical curator searches and independent historical authorship are not certified.
- The completed fresh-base batch15 global gates are attached only at finalization; identifier transport and label-adapter limits remain explicit.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The user explicitly authorized one review for every uncovered target, including a review with no findings. Only this review bundle is intended for persistence.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T110755Z-chloroplast-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Organelle identity, composition and evidence review
started_at: '2026-10-21T10:40:28Z'
finished_at: '2026-10-21T11:07:55Z'
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
summary: The exact identity, structural boundaries, scoped composition and descriptive
  graph are coherent. No concrete curation finding was established; source-access
  and individual assembly-necessity limits remain explicit.
source:
  git_revision: 9c0446c4c0dd4b458787c43a499e4ceab5e179a6
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
  - path: data/structures/membrane_organelle/chloroplast.yaml
    sha256: 4c13f5dadaeb23a88fabfc2b5ec65034ed0ac83cbca9d45143793618acf2e727
    role: target
  - path: data/structures/membrane_organelle/chloroplast_envelope.yaml
    sha256: 29da363489107536342db1782001be534ea54605039b80c201cba0a46de9468e
    role: context
  - path: data/structures/membrane_organelle/chloroplast_inner_membrane.yaml
    sha256: 05283f5252a6354d26bef1ff196b3a9e10fbd6e72e9a6ec17014330f7a28dbb3
    role: context
  - path: data/structures/membrane_organelle/chloroplast_intermembrane_space.yaml
    sha256: 7ab90f4d2f4c41c466e100d589fb1f1d42bf90ded515dea6db5575d54119d43a
    role: context
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
- target_id: GO:0009507
  path: data/structures/membrane_organelle/chloroplast.yaml
  label: chloroplast
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/chloroplast.yaml
    role: maintained scientific record
scope:
  description: Entire single record with exact authority identities, declared source-reading
    scopes, protein checks where applicable and component/function/graph boundaries.
  selection: Target 7 in batch twenty-one; exact sorted uncovered path at frozen fresh-main
    revision.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0009507
checks:
- check_id: native-verify
  name: Native protein verify
  status: passed
  required: true
  target_ids:
  - GO:0009507
  command: /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast.yaml
    --verify
  exit_code: 0
  summary: Focused native command passed; identity/coverage result is distinct from
    scientific membership.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Native protein causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0009507
  command: /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast.yaml
    --causal-graphs
  exit_code: 0
  summary: Focused native command passed; identity/coverage result is distinct from
    scientific membership.
  evidence_ids:
  - native-causal-graphs
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0009507
  command: just validate data/structures/membrane_organelle/chloroplast.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0009507
  command: just validate-strict data/structures/membrane_organelle/chloroplast.yaml
    --out /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/chloroplast-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0009507
  summary: 17 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0009507
  summary: No expression-module or transcriptomic inference is made by this structural
    review.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0009507
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - neighbor-chloroplast_envelope
  - neighbor-chloroplast_inner_membrane
  - neighbor-chloroplast_intermembrane_space
  - root21-sources-chloroplast-go
  - root21-sources-ancestors-0009507
  - root21-sources-NCBITaxon-33090
  - root21-sources-NCBITaxon-3055
  - root21-sources-doi-10.1098_rstb.2009.0103
  - root21-sources-doi-10.1016_j.cell.2022.10.030
  - root21-sources-keeling2010-pmc
  - root21-sources-keeling2010-jats
  - root21-sources-keeling2010-s3
  - root21-sources-keeling2010-repository
  - root21-sources-keeling2010-bioc
  - root21-sources-jin2022-publisher
  - root21-sources-jin2022-author-publications
  - root21-sources-doi-10.1007_s00294-011-0339-1
  - root21-sources-terashima2011-pdf
  - root21-sources-GO0061927
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0009507
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:53Z to
    2026-10-21T09:12:21Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0009507
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1828 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:53Z to
    2026-10-21T09:05:00Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0009507
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:57Z to
    2026-10-21T09:05:46Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0009507
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:57Z to
    2026-10-21T09:05:06Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0009507
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE.
    Transport failures and skipped prefixes are not evidence of resolution. Exact
    target identifiers are assessed separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:57Z to
    2026-10-21T09:45:43Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/chloroplast.yaml
  locator: Entire maintained YAML including history, all evidence notes, components,
    functions, graph edges and discussions
  accessed_at: '2026-10-21T10:46:07Z'
  support: context_only
  summary: All maintained fields were read. No scientific edit or mapping-status promotion
    is made.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact identity, claim-level evidence, material versus localization grounding,
    and component assembly-essentiality contract
  accessed_at: '2026-10-21T10:46:07Z'
  support: context_only
  summary: Family identity, concrete protein examples and structure membership are
    separate; activity and viability are not by themselves formation assays. Optional
    inventories are not mandatory.
- evidence_id: neighbor-chloroplast_envelope
  kind: record_content
  reference: data/structures/membrane_organelle/chloroplast_envelope.yaml
  locator: Entire adjacent record, including components, graph and discussions
  accessed_at: '2026-10-21T10:46:07Z'
  support: context_only
  summary: Read to check the boundary between whole chloroplast, enclosing envelope,
    individual inner bilayer and intervening volume. This dependency is not a second
    review target.
- evidence_id: neighbor-chloroplast_inner_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/chloroplast_inner_membrane.yaml
  locator: Entire adjacent record, including components, graph and discussions
  accessed_at: '2026-10-21T10:46:07Z'
  support: context_only
  summary: Read to check the boundary between whole chloroplast, enclosing envelope,
    individual inner bilayer and intervening volume. This dependency is not a second
    review target.
- evidence_id: neighbor-chloroplast_intermembrane_space
  kind: record_content
  reference: data/structures/membrane_organelle/chloroplast_intermembrane_space.yaml
  locator: Entire adjacent record, including components, graph and discussions
  accessed_at: '2026-10-21T10:46:07Z'
  support: context_only
  summary: Read to check the boundary between whole chloroplast, enclosing envelope,
    individual inner bilayer and intervening volume. This dependency is not a second
    review target.
- evidence_id: root21-sources-chloroplast-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009507,GO:0009534,GO:0009535,GO:0009536,GO:0009570,GO:0009706,GO:0009707,GO:0009941,GO:0010006,GO:0015979,GO:0031897,GO:0045037,GO:0061927
  locator: All returned identifiers, names, definitions, aspect, obsolete status and
    relevant children
  accessed_at: '2026-10-21T10:41:48.043820Z'
  support: supports
  summary: Active native GO terms distinguish chloroplast, plastid, envelope, bilayers,
    stroma and intermembrane space. Definitions and returned child relations support
    the asserted structural boundaries; process terms are not substituted for organelle
    identities.
  snapshot_sha256: d3e445f547c0b77756cd784b474abddbcef716d647264ff4e3ffcad643ff4ed8
- evidence_id: root21-sources-ancestors-0009507
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009507/ancestors?relations=is_a,part_of
  locator: Complete ancestor response with explicit is_a,part_of query
  accessed_at: '2026-10-21T10:41:48.746953Z'
  support: supports
  summary: The native ancestor response identifies the broader structural context
    of this term. Combined is_a/part_of closure is not used to erase the distinction
    between type and physical inclusion; exact parent relations are separately checked
    in returned term children and definitions.
  snapshot_sha256: cbdf5fc49c2b7c9425aece03659961b04336046658ec04870b356ee0ef3a97cf
- evidence_id: root21-sources-NCBITaxon-33090
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/33090
  locator: Exact taxId, scientificName, rank, lineage and relevant alternative names
  accessed_at: '2026-10-21T10:41:48.003081Z'
  support: supports
  summary: Native ENA taxonomy identifies Viridiplantae at kingdom rank. Only this
    taxon's identity and names are asserted by this row, not occurrence or experimental
    stock identity.
  snapshot_sha256: 5edd98868e71b65ad827c23592102272c4e9e3ce6f29421e9263dcff0a3410f4
- evidence_id: root21-sources-NCBITaxon-3055
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055
  locator: Exact taxId, scientificName, rank, lineage and relevant alternative names
  accessed_at: '2026-10-21T10:41:48.009244Z'
  support: supports
  summary: Native ENA taxonomy identifies Chlamydomonas reinhardtii at species rank.
    Only this taxon's identity and names are asserted by this row, not occurrence
    or experimental stock identity.
  snapshot_sha256: a24c8f85014097148d9e865ea324b01b8d04f6bae27e893834f8abb5bd8b6a1f
- evidence_id: root21-sources-doi-10.1098_rstb.2009.0103
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1098/rstb.2009.0103
  locator: Complete native bibliography and abstract
  accessed_at: '2026-10-21T10:41:48.128898Z'
  support: supports
  summary: Native MED identifies The endosymbiotic origin, diversification and fate
    of plastids. (Keeling PJ., 2010), PMID 20124341, DOI 10.1098/rstb.2009.0103. Exact
    bibliography and complete returned abstract were read; any body coverage is separately
    declared.
  snapshot_sha256: cb4b9f46ce9002adf2521e02ef9aa676bb65af752c0b025c4015b37a21d9aa0b
- evidence_id: root21-sources-doi-10.1016_j.cell.2022.10.030
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.cell.2022.10.030
  locator: Complete native bibliography and abstract
  accessed_at: '2026-10-21T10:41:48.146550Z'
  support: supports
  summary: Native MED identifies Structure of a TOC-TIC supercomplex spanning two
    chloroplast envelope membranes. (Jin Z, Wan L, Zhang Y, Li X, Cao Y, Liu H, Fan
    S, Cao D, Wang Z, Li X, Pan J, Dong MQ, Wu J, Yan Z., 2022), PMID 36413996, DOI
    10.1016/j.cell.2022.10.030. Exact bibliography and complete returned abstract
    were read; any body coverage is separately declared.
  snapshot_sha256: f4fc2108c3825f4a38c42eb7d109ac334b6e4d413ff1216d0d013925a2780061
- evidence_id: root21-sources-keeling2010-pmc
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2817223/
  locator: Actual source-access response, not article content
  accessed_at: '2026-10-21T10:41:49.525235Z'
  support: context_only
  summary: Native legacy PMC returned a recaptcha challenge with HTTP200, not article
    content. It is not treated as a full-text read.
  snapshot_sha256: b16bf621eb2a3f358f1f623288ece9340e27da9dbb1cf7d86cbfbe75ce8fbff6
- evidence_id: root21-sources-keeling2010-jats
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2817223/fullTextXML
  locator: Actual source-access response, not article content
  accessed_at: '2026-10-21T10:41:53.762849Z'
  support: context_only
  summary: Europe PMC fullTextXML returned500; no article body was obtained from this
    response.
  snapshot_sha256: e6403bb63596b669f29df052d5f58bb6300bdc53798b238391b33d8931a1c4de
- evidence_id: root21-sources-keeling2010-s3
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2817223.1/PMC2817223.1.xml
  locator: Actual source-access response, not article content
  accessed_at: '2026-10-21T10:43:00.841136Z'
  support: context_only
  summary: The attempted public OA version1 XML key returned404; this says nothing
    about the validity or scientific support of the cited paper.
  snapshot_sha256: 0c113dcd4c04302e28fff991a7589cd3cde942d6178c6c36ca7d3203a0e09180
- evidence_id: root21-sources-keeling2010-repository
  kind: authority
  reference: https://marinebiology.pt/beu/files/bib/Keeling2010.pdf
  locator: Actual source-access response, not article content
  accessed_at: '2026-10-21T10:43:01.449137Z'
  support: context_only
  summary: The independently discovered repository PDF route returned403; no PDF was
    read.
  snapshot_sha256: 5e08fb869bdfd099766860b8fb11bef1632adb7085f7a9d0c82568913ab2c966
- evidence_id: root21-sources-keeling2010-bioc
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC2817223/unicode
  locator: Actual source-access response, not article content
  accessed_at: '2026-10-21T10:44:31.891198Z'
  support: context_only
  summary: The public NCBI BioC route returned an error document with HTTP200 and
    no article result, not a usable body.
  snapshot_sha256: 478f38e0765ee9c406831bb2fc27e8019ac5227c20c6b28ca0de582d8449354a
- evidence_id: root21-sources-jin2022-publisher
  kind: authority
  reference: https://www.sciencedirect.com/science/article/pii/S0092867422013769
  locator: Actual source-access response, not article content
  accessed_at: '2026-10-21T10:41:48.872483Z'
  support: context_only
  summary: The native ScienceDirect route returned403; source-specific TOC-TIC support
    in this review is limited to the complete native primary abstract.
  snapshot_sha256: bba6b4a3d80f9dc3bde89c33f536c9d5a98a33e25ce7baf49f5d0cb668b46677
- evidence_id: root21-sources-jin2022-author-publications
  kind: authority
  reference: https://lifesciences.westlake.edu.cn/labs/zhen-yan/structural-biology-laboratory/publications/
  locator: Actual source-access response, not article content
  accessed_at: '2026-10-21T10:43:01.857288Z'
  support: context_only
  summary: The corresponding author laboratory publications page returned403. No full-paper
    access is inferred.
  snapshot_sha256: 11112b4a5aec6ac320e00d8e7129abc97d562d7135808114e7994dcad1d1f585
- evidence_id: root21-sources-doi-10.1007_s00294-011-0339-1
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1007/s00294-011-0339-1
  locator: Complete native bibliography and abstract
  accessed_at: '2026-10-21T10:41:48.103033Z'
  support: supports
  summary: 'Native MED identifies The chloroplast proteome: a survey from the Chlamydomonas
    reinhardtii perspective with a focus on distinctive features. (Terashima M, Specht
    M, Hippler M., 2011), PMID 21533645, DOI 10.1007/s00294-011-0339-1. Exact bibliography
    and complete returned abstract were read; any body coverage is separately declared.'
  snapshot_sha256: aec76518f370734a76392741bffd319ac61df223c77fad628910ec04da56412e
- evidence_id: root21-sources-terashima2011-pdf
  kind: authority
  reference: https://link.springer.com/content/pdf/10.1007/s00294-011-0339-1.pdf
  locator: Published pages151–152 Abstract/Introduction and initial proteomics/contamination
    discussion; Photosynthesis section from heading through LHCSR/CAS discussion on
    pages154–156; Carbon metabolism section on pages156–157 through its final paragraph.
    Figure pixels, supplements and the full remaining review were not read.
  accessed_at: '2026-10-21T10:41:52.689991Z'
  support: supports
  summary: The publisher PDF reviews the experimental Chlamydomonas chloroplast proteome
    and comparison with higher plants, emphasizing contamination control and the difference
    between predicted and experimental localization. Read passages support thylakoid
    photosynthetic machinery and chloroplast carbon assimilation without turning the
    list into a complete native inventory.
  snapshot_sha256: e42edb346d375e4e083e2eb79c6d9eff9fc217513e1ae9ecf808acb143129c6b
- evidence_id: root21-sources-GO0061927
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0061927
  locator: Exact identifier, definition, active status and aspect
  accessed_at: '2026-10-21T10:41:49.305769Z'
  support: supports
  summary: Active GO0061927 is TOC-TIC supercomplex I and its definition requires
    a classic constituent set including Tic110. The Jin2022 abstract instead reports
    Tic20/YlmG architecture and Toc120/Toc75; this candidate cannot be adopted solely
    because its name resembles the grouped component.
  snapshot_sha256: c396141ec6b3ee096330ffd7050a629e09efdbb06839c03e0ea67a546cf389d2
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast.yaml
    --verify
  locator: Exact focused native output
  accessed_at: '2026-10-21T10:42:58.568963Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast.yaml
    --causal-graphs
  locator: Exact focused native output
  accessed_at: '2026-10-21T10:42:59.251312Z'
  support: supports
  summary: "causal_graphs GENE_OR_PROTEIN node summary:\n     0  COVERED         \
    \          component_ref target holds protein_examples covering all declared symbols\n\
    \     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     0\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/chloroplast.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:40:31Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/chloroplast.yaml'
  snapshot_sha256: 3c06516b9ce178893db8cb91c14e9080d7d37ab6ac1bb33e6dc0da8576caa631
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/chloroplast.yaml
    --out /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/chloroplast-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:40:33Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/chloroplast.yaml\
    \ --out /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/chloroplast-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch21-20261021-jc4u1a6u/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/chloroplast-strict.tsv"
  snapshot_sha256: aff6dc099d2de47cbc932d48bec39d9f03583ed716252eb34694f1cee2e69611
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/chloroplast.yaml; exact collect() scope;
    hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T10:46:07Z'
  support: supports
  summary: '17 of17 collected target identifiers returned OK in this fresh base resolver
    run. Residuals: none. Source-native identity checked separately.'
  snapshot_sha256: d428d95fd13ac608f3786bcf74a032c768ac80e494b9673013e1e4d27de9ad66
- evidence_id: global-qc-result
  kind: validation
  reference: just qc
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82
  accessed_at: '2026-10-21T09:12:21Z'
  support: supports
  summary: 'Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  snapshot_sha256: 2cf77f0998cf42f98e103ee00a0f23cd610d5fcfd4814d7438d3e76bc9ef3d6d
- evidence_id: global-history-result
  kind: validation
  reference: just validate-history
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0
  accessed_at: '2026-10-21T09:05:00Z'
  support: supports
  summary: Exit 0. All 1828 history records validated; URI precheck reported zero
    invalid references.
  snapshot_sha256: 793664cc55dee807ad6725ace8cbdeb817e07c968f017af7ab0b5183a67b3df0
- evidence_id: global-products-result
  kind: validation
  reference: just validate-products
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26
  accessed_at: '2026-10-21T09:05:46Z'
  support: supports
  summary: 'Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  snapshot_sha256: dd07915effbb88aa88c56f6c102542b3cea4d9c70f381d943a664796a79c6917
- evidence_id: global-traits-result
  kind: validation
  reference: just check-trait-links --check
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad
  accessed_at: '2026-10-21T09:05:06Z'
  support: supports
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  snapshot_sha256: 6eab64b59433928ec8e0df9b0046dbccf479c84bb0911c315feebc344d536007
- evidence_id: global-curies-result
  kind: validation
  reference: just check-curies-strict
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d
  accessed_at: '2026-10-21T09:45:43Z'
  support: supports
  summary: Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE.
    Transport failures and skipped prefixes are not evidence of resolution. Exact
    target identifiers are assessed separately in this review.
  snapshot_sha256: 4b17ccc07b33ceab3eeb8631b1cf075f5f750c5a6f4820455b1930e3aa165286
assessments:
- assessment_id: identity
  area: identity
  topic: Exact identity and adjacent structure boundaries
  outcome: supported
  target_ids:
  - GO:0009507
  summary: Native identifiers and source descriptions distinguish the complete organelle,
    its double-membrane envelope including the intervening space, individual inner
    bilayer, and enclosed intermembrane region. Asserted is_a parents and physical
    parts are coherent. The source-neutral GO definition is not silently expanded
    to make every plastid photosynthetic.
  evidence_ids:
  - root21-sources-chloroplast-go
  - root21-sources-ancestors-0009507
  - root21-sources-NCBITaxon-33090
  - root21-sources-NCBITaxon-3055
  - root21-sources-doi-10.1098_rstb.2009.0103
  - root21-sources-doi-10.1016_j.cell.2022.10.030
  - record
  - policy
  - root21-sources-doi-10.1007_s00294-011-0339-1
  - root21-sources-terashima2011-pdf
  - root21-sources-GO0061927
- assessment_id: scope
  area: scope
  topic: Green lineage and model-organism context
  outcome: supported
  target_ids:
  - GO:0009507
  summary: The two native taxa are Viridiplantae and Chlamydomonas reinhardtii. The
    record describes widespread occurrence in photosynthetic green algae/plants and
    the established chloroplast of the experimental green alga; COMMON does not mean
    every tissue or every nonphotosynthetic plastid is a chloroplast. Keeling explicitly
    discusses plastid loss and nonphotosynthetic forms. The Jin abstract supplies
    direct Chlamydomonas envelope-spanning structure context without identifying a
    strain. No numerical prevalence estimate is inferred.
  evidence_ids:
  - root21-sources-chloroplast-go
  - root21-sources-ancestors-0009507
  - root21-sources-NCBITaxon-33090
  - root21-sources-NCBITaxon-3055
  - root21-sources-doi-10.1098_rstb.2009.0103
  - root21-sources-doi-10.1016_j.cell.2022.10.030
  - record
  - policy
  - root21-sources-doi-10.1007_s00294-011-0339-1
  - root21-sources-terashima2011-pdf
  - root21-sources-GO0061927
- assessment_id: composition
  area: grounding
  topic: Membrane parts and a bounded import complex
  outcome: supported
  target_ids:
  - GO:0009507
  summary: The membrane rows identify actual organelle parts through exact GO membrane
    terms; these are not claimed as chemical identifiers for individual lipids. Toc/Tic
    subcomplexes are valid has_part structures. The composite TOC-TIC row is appropriately
    label-only because the checked classic GO supercomplex has a different required
    composition. The source supports14 identified components but neither an accession
    for the entire complex nor a mandatory exhaustive chloroplast inventory is inferred.
  evidence_ids:
  - root21-sources-chloroplast-go
  - root21-sources-ancestors-0009507
  - root21-sources-NCBITaxon-33090
  - root21-sources-NCBITaxon-3055
  - root21-sources-doi-10.1098_rstb.2009.0103
  - root21-sources-doi-10.1016_j.cell.2022.10.030
  - record
  - policy
  - root21-sources-doi-10.1007_s00294-011-0339-1
  - root21-sources-terashima2011-pdf
  - root21-sources-GO0061927
- assessment_id: necessity
  area: evidence
  topic: Assembly requirements remain unknown
  outcome: unknown
  target_ids:
  - GO:0009507
  summary: All four listed component essentialities are UNKNOWN. Photosynthetic activity,
    protein-import importance and recovery of a structural complex do not establish
    whole-chloroplast assembly failure after loss of each component class. No universal
    requirement is inferred from the primary abstract calling translocons essential.
  evidence_ids:
  - root21-sources-chloroplast-go
  - root21-sources-ancestors-0009507
  - root21-sources-NCBITaxon-33090
  - root21-sources-NCBITaxon-3055
  - root21-sources-doi-10.1098_rstb.2009.0103
  - root21-sources-doi-10.1016_j.cell.2022.10.030
  - record
  - policy
  - root21-sources-doi-10.1007_s00294-011-0339-1
  - root21-sources-terashima2011-pdf
  - root21-sources-GO0061927
- assessment_id: function
  area: evidence
  topic: Photosynthesis and precursor import
  outcome: supported
  target_ids:
  - GO:0009507
  summary: The inspected2011 review passages support chloroplast photosynthetic electron
    transfer and carbon assimilation. The native process identities and2022 primary
    abstract support the envelope-spanning precursor-import route. Exact transport
    kinetics, a substrate-bound trajectory and a molecular assembly sequence are not
    asserted.
  evidence_ids:
  - root21-sources-chloroplast-go
  - root21-sources-ancestors-0009507
  - root21-sources-NCBITaxon-33090
  - root21-sources-NCBITaxon-3055
  - root21-sources-doi-10.1098_rstb.2009.0103
  - root21-sources-doi-10.1016_j.cell.2022.10.030
  - record
  - policy
  - root21-sources-doi-10.1007_s00294-011-0339-1
  - root21-sources-terashima2011-pdf
  - root21-sources-GO0061927
- assessment_id: graph
  area: graph
  topic: Eight descriptive topology and import edges
  outcome: supported
  target_ids:
  - GO:0009507
  summary: 'All eight edges retain their NONMECHANISTIC scope: envelope and membrane
    topology, thylakoid placement and the TOC-TIC import route. The native definitions
    support the spatial relations. The primary abstract directly describes the structure
    spanning both membranes and an IMS scaffold/pathway; these coarse edges do not
    claim experimentally demonstrated motion through every proposed pore.'
  evidence_ids:
  - root21-sources-chloroplast-go
  - root21-sources-ancestors-0009507
  - root21-sources-NCBITaxon-33090
  - root21-sources-NCBITaxon-3055
  - root21-sources-doi-10.1098_rstb.2009.0103
  - root21-sources-doi-10.1016_j.cell.2022.10.030
  - record
  - policy
  - root21-sources-doi-10.1007_s00294-011-0339-1
  - root21-sources-terashima2011-pdf
  - root21-sources-GO0061927
- assessment_id: provenance
  area: provenance
  topic: Accurate citation identities and bounded access
  outcome: supported
  target_ids:
  - GO:0009507
  summary: The cited bibliography matches native MED metadata. The current source
    checks preserve HTTP errors and distinguish challenge/error documents from article
    bodies. No historical source-reading statement, status or history is rewritten.
    The model-organism example is supported at its declared scope; no new image, raw
    dataset or verbatim snippet is asserted.
  evidence_ids:
  - root21-sources-chloroplast-go
  - root21-sources-ancestors-0009507
  - root21-sources-NCBITaxon-33090
  - root21-sources-NCBITaxon-3055
  - root21-sources-doi-10.1098_rstb.2009.0103
  - root21-sources-doi-10.1016_j.cell.2022.10.030
  - record
  - policy
  - root21-sources-doi-10.1007_s00294-011-0339-1
  - root21-sources-terashima2011-pdf
  - root21-sources-GO0061927
- assessment_id: coverage
  area: completeness
  topic: Bounded record-level coverage
  outcome: supported
  target_ids:
  - GO:0009507
  summary: The entire maintained record and cited claim contexts were inspected at
    the stated source scopes. Additional exhaustive component inventories, numerical
    properties, images, traits and expanded mechanisms are optional. No verbatim quotation
    requires repair, and no status or history rewrite is proposed. This bounded review
    does not assert exhaustive literature completeness.
  evidence_ids:
  - record
  - policy
  - neighbor-chloroplast_envelope
  - neighbor-chloroplast_inner_membrane
  - neighbor-chloroplast_intermembrane_space
  - root21-sources-chloroplast-go
  - root21-sources-ancestors-0009507
  - root21-sources-NCBITaxon-33090
  - root21-sources-NCBITaxon-3055
  - root21-sources-doi-10.1098_rstb.2009.0103
  - root21-sources-doi-10.1016_j.cell.2022.10.030
  - root21-sources-keeling2010-pmc
  - root21-sources-keeling2010-jats
  - root21-sources-keeling2010-s3
  - root21-sources-keeling2010-repository
  - root21-sources-keeling2010-bioc
  - root21-sources-jin2022-publisher
  - root21-sources-jin2022-author-publications
  - root21-sources-doi-10.1007_s00294-011-0339-1
  - root21-sources-terashima2011-pdf
  - root21-sources-GO0061927
findings: []
actions: []
limitations:
- Jin2022 and Keeling2010 were read through complete native abstracts and bibliographic
  metadata only; multiple legitimate full-text routes failed or returned challenge/error
  documents. No full-body, Methods, figure-pixel or supplement audit of those papers
  is claimed.
- Taxon-wide occurrence is assessed qualitatively at the maintained scope, not as
  a measured prevalence percentage. The review does not assert every cell of Viridiplantae
  carries chlorophyll-containing chloroplasts.
- The separate neighboring records were read only for boundaries; this review has
  exactly one target. No exhaustive family/ontology absence search or new molecular
  inventory is claimed.
- Terashima2011 publisher PDF was read only at the specified proteome, photosynthesis
  and carbon-metabolism passages. Its full protein table, figures, supplements and
  underlying raw proteomics were not reanalysed.
- No raw microscopy or quantitative datasets were reanalysed. Historical curator searches
  and independent historical authorship are not certified.
- The completed fresh-base batch15 global gates are attached only at finalization;
  identifier transport and label-adapter limits remain explicit.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- The user explicitly authorized one review for every uncovered target, including
  a review with no findings. Only this review bundle is intended for persistence.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
