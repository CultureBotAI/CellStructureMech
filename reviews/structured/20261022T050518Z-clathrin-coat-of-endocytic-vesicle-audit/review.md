# Source-backed review of clathrin coat of endocytic vesicle

- Review: 20261022T050518Z-clathrin-coat-of-endocytic-vesicle-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T04:47:14Z
- Finished UTC: 2026-10-22T05:05:18Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The coat identity, yeast examples and descriptive graph are supported at the declared source tiers. One bounded minor resolves the exact triskelion-complex grounding.

## Scope And Provenance

Exactly one complete target; no neighboring scientific-record verdict is imported. Exact authority, all current component/function/graph/source placements, taxonomic scope, formation semantics, history and discussions were reviewed.

Selection: Batch47 fixed strict path order, index 5; exactly one maintained target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0030128 | data/structures/other/clathrin_coat_of_endocytic_vesicle.yaml | maintained | clathrin coat of endocytic vesicle |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0030128 | Focused validator passed. |
| Focused native strict | passed | True | GO:0030128 | Focused validator passed. |
| Focused native proteins | passed | True | GO:0030128 | Read-only native check passed; claim-level protein/edge support evaluated separately. |
| Focused native graphs | passed | True | GO:0030128 | Read-only native check passed; claim-level protein/edge support evaluated separately. |
| Claim-level scientific review | passed | True | GO:0030128 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0030128 | 20 of 22 collected target identifiers returned OK. PMID:14562095: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:9531549: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0030128 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0030128 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0030128 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0030128 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0030128 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact coat identity and topology

identity: supported. Targets: GO:0030128.

The exact active GO identity, definition and declared topology are supported. Specific coat-to-membrane part_of and is_a links are native typed relations; broad coat-to-whole-vesicle parthood is definition-supported rather than an exposed direct edge in this response. The proteinaceous coat remains distinct from a lipid membrane and from the whole vesicle. The endocytic and TGN terms are specific children of the broad vesicle-coat class.

### Species, strain and prevalence meaning

scope: supported. Targets: GO:0030128.

Species4932 and strain559292 identities are correct. COMMON means present in most species members with exceptional losses; ordinary yeast experiments provide qualitative support, not a measured prevalence denominator. Experimental strain/condition details are not silently replaced by the reference accession taxon.

### Native examples and query claims

grounding: supported. Targets: GO:0030128.

All retained accession/gene/status/taxon pairs are correct. Exact reviewed S288C queries support the current single-hit claims. Identity-only examples remain identity evidence; primary membership and localization are assessed separately. P27351 is the APL1 beta subunit of AP2; its member example does not replace the complex identity GO0030122.

### Formation necessity

grounding: unknown. Targets: GO:0030128.

The component essentiality values are already UNKNOWN. The inspected localization, association and trafficking data do not establish a single universal requirement for formation of every coat represented by this class. No unsupported ESSENTIAL claim is introduced.

### Exact triskelion versus heterogeneous adaptor cohort

grounding: concern. Targets: GO:0030128.

Triskelion and adaptor membership is supported. The explicit PROTEIN_COMPLEX triskelion row has an exact native GO0071439 identity and should no longer remain REVIEWED_LABEL_ONLY. This grounds the triskelion building block, not the entire polymerized coat. The broader adaptor/cargo-selection cohort is not equivalent to AP2 or GO0030131, so its label-only representation remains bounded and no forced single-family mapping is proposed.

### Exact localization evidence placement

evidence: supported. Targets: GO:0030128.

Wendland1998 supports the stated Bud annotation, and the native P38856 Cytoplasm citation joins PMID14562095. Huh2003 was read only at complete abstract tier; the exact YAP1801 annotation is verified in native UniProt rather than an unread primary table. Newpher supplies independently read adaptor/cortical-clathrin context; Sla2 involvement is not called an obligatory initial recruitment factor.

### Coarse endocytic coat graph

graph: supported. Targets: GO:0030128.

The seven-node/seven-edge NONMECHANISTIC FUNCTION graph separates triskelion polymerization, adaptor association, AP2 part-of, coat/membrane/vesicle topology and endocytosis participation. Its scope expressly excludes a complete assembly/scission mechanism. Initial recruitment and later actin dynamics are not conflated with directly observed vesicle release.

### Whole-target coverage and bounded enrichment

completeness: supported. Targets: GO:0030128.

The entire target, all current components/examples, source placements, graph, discussions and history were reviewed. The supported exact mapping issue is distinct from optional inventory expansion. No exhaustive absence claim is made for future broader-adaptor families; no local-neighbor scientific verdict is imported.

## Findings

### F1: Use the verified exact clathrin-triskelion complex grounding

minor / open / confirmed; issue key: clathrin.clathrin_coat_of_endocytic_vesicle.exact_triskelion_grounding.

The component explicitly denotes the source-neutral clathrin triskelion complex and declares REVIEWED_LABEL_ONLY. Active GO0071439 has the exact synonym clathrin triskelion and matching three-heavy/three-light complex definition. The current review can resolve this bounded grounding gap without equating the complete coat with one triskelion. The dated statement that no term was curated in an earlier pass is not judged as a false historical search report.

## Recommended Actions And Acceptance Checks

### A1

Ground the triskelion component to GO:0071439, update its label-only status/notes and linked node consistently, retain component IDs and the distinction between triskelion units and polymerized coat. Preserve heterogeneous adaptor scope.

- Preserve exact supported identity, experimental organism and native versus recombinant context.
- Attach source-specific evidence to each changed claim and retain historical provenance.
- Native schema, strict, CURIE, protein and graph checks pass as applicable.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/clathrin_coat_of_endocytic_vesicle.yaml; Complete maintained YAML; all components, source notes, graphs, discussions and historical entries | context_only | The entire maintained target was read; no scientific record was changed. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent; ComponentTypeEnum; EssentialityEnum; graph scopes | context_only | ComponentTypeEnum distinguishes LIPID from the permitted OTHER composite class. ESSENTIAL concerns failure of structure formation, not merely loss of catalytic or transport function. |
| curation | docs/CURATION.md; Components; groundings; associated machinery and chaperone boundaries | context_only | Components are taxon-agnostic molecular families/classes; exact family grounding is preferred when verified. Mature constituents and assembled-structure maintenance machinery differ from transient preassembly chaperones. |
| micro47-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005768,GO:0005802,GO:0005905,GO:0012510,GO:0016020,GO:0030117,GO:0030118,GO:0030119,GO:0030120,GO:0030121,GO:0030122,GO:0030125,GO:0030128,GO:0030130,GO:0030132,GO:0030136,GO:0030140,GO:0030669,GO:0045334,GO:0072583; Complete exact entries GO0030128/0030130/0030125/0030120/0030118/0030117/0030119/0030121/0030122/0030669/0012510/0030140/0045334/0030136/0005768/0005802/0072583: id,name,definition,isObsolete,typed children and synonyms; shared response also includes pit/membrane entries. | supports | GO0030128 is an active exact clathrin-coat identity, distinct from the membrane and whole vesicle it coats. The combined native response verifies the maintained is_a relations, the two specific coat-to-membrane part_of links, AP1/AP2 boundaries and GO0072583 endocytosis. The broad coat-to-vesicle parthood is definition-supported; a direct GO0030125 part_of GO0030136 edge is not exposed in this response. GO0030118 describes polymerized heavy/light-chain triskelions linked to membranes by adaptors. No exhaustive future inventory is inferred. |
| micro47-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete taxId/scientificName/rank/lineage/otherNames. | supports | ENA taxId 4932 identifies Saccharomyces cerevisiae at rank species; aliases and lineage match the record. Identity alone is not prevalence or experimental-condition evidence. |
| micro47-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete taxId/scientificName/rank/lineage/otherNames. | supports | ENA taxId 559292 identifies Saccharomyces cerevisiae S288C at rank strain; aliases and lineage match the record. Identity alone is not prevalence or experimental-condition evidence. |
| micro47-protein-P22137 | https://rest.uniprot.org/uniprotkb/P22137.json; primaryAccession/entryType; organism; proteinDescription; genes; full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their evidence joins. | supports | P22137 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['CHC1']. Recommended identity, gene aliases, full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their evidence codes/PMIDs were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro47-protein-P17891 | https://rest.uniprot.org/uniprotkb/P17891.json; primaryAccession/entryType; organism; proteinDescription; genes; full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their evidence joins. | supports | P17891 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['CLC1']. Recommended identity, gene aliases, full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their evidence codes/PMIDs were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro47-protein-Q12518 | https://rest.uniprot.org/uniprotkb/Q12518.json; primaryAccession/entryType; organism; proteinDescription; genes; full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their evidence joins. | supports | Q12518 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['ENT1']. Recommended identity, gene aliases, full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their evidence codes/PMIDs were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro47-protein-Q05785 | https://rest.uniprot.org/uniprotkb/Q05785.json; primaryAccession/entryType; organism; proteinDescription; genes; full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their evidence joins. | supports | Q05785 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['ENT2']. Recommended identity, gene aliases, full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their evidence codes/PMIDs were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro47-protein-P33338 | https://rest.uniprot.org/uniprotkb/P33338.json; primaryAccession/entryType; organism; proteinDescription; genes; full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their evidence joins. | supports | P33338 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['SLA2']. Recommended identity, gene aliases, full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their evidence codes/PMIDs were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro47-protein-P38856 | https://rest.uniprot.org/uniprotkb/P38856.json; primaryAccession/entryType; organism; proteinDescription; genes; full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their evidence joins. | supports | P38856 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['YAP1801']. Recommended identity, gene aliases, full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their evidence codes/PMIDs were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro47-protein-P27351 | https://rest.uniprot.org/uniprotkb/P27351.json; primaryAccession/entryType; organism; proteinDescription; genes; full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their evidence joins. | supports | P27351 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['APL1']. Recommended identity, gene aliases, full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their evidence codes/PMIDs were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro47-gene-CHC1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACHC1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete results of the retained exact gene/reviewed/taxon559292 URL. | supports | The exact reviewed S288C query for CHC1 returned 1 entry: P22137. Identity and primary gene symbol match; no current uniqueness discrepancy was observed. |
| micro47-gene-CLC1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACLC1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete results of the retained exact gene/reviewed/taxon559292 URL. | supports | The exact reviewed S288C query for CLC1 returned 1 entry: P17891. Identity and primary gene symbol match; no current uniqueness discrepancy was observed. |
| micro47-gene-ENT1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AENT1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete results of the retained exact gene/reviewed/taxon559292 URL. | supports | The exact reviewed S288C query for ENT1 returned 1 entry: Q12518. Identity and primary gene symbol match; no current uniqueness discrepancy was observed. |
| micro47-gene-ENT2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AENT2%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete results of the retained exact gene/reviewed/taxon559292 URL. | supports | The exact reviewed S288C query for ENT2 returned 1 entry: Q05785. Identity and primary gene symbol match; no current uniqueness discrepancy was observed. |
| micro47-gene-SLA2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASLA2%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete results of the retained exact gene/reviewed/taxon559292 URL. | supports | The exact reviewed S288C query for SLA2 returned 1 entry: P33338. Identity and primary gene symbol match; no current uniqueness discrepancy was observed. |
| micro47-gene-YAP1801 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AYAP1801%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete results of the retained exact gene/reviewed/taxon559292 URL. | supports | The exact reviewed S288C query for YAP1801 returned 1 entry: P38856. Identity and primary gene symbol match; no current uniqueness discrepancy was observed. |
| micro47-newpher2005-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.devcel.2005.04.014; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED15992543: In vivo dynamics of clathrin and its adaptor-dependent recruitment to the actin-based endocytic machinery in yeast. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro47-kaksonen2005-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.cell.2005.09.024; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED16239147: A modular design for the clathrin- and actin-mediated endocytosis machinery. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro47-newpher2005-duke | https://dukespace.lib.duke.edu/server/api/core/bitstreams/e3c70c30-e4a1-4ba0-8ea6-c50af4ba491e/content; Complete printed pp87–96: Summary/Introduction, Table1, all main Results/Discussion and Experimental Procedures, including Fig1–6 captions. Original Duke primary PDF; reading derivative only, no pixels, videos or supplements. | supports | Newpher2005 directly images cortical clathrin and endocytic factors in budding yeast. WT TIRFM places clathrin before Abp1; extensive adaptor colocalization/recruitment tests use sla2Δ or LAT-A and multi-adaptor perturbations. Sla2/End3/Pan1 affect progression or release rather than being required for initial cortical recruitment. The authors explicitly cannot distinguish clathrin disassembly from a coated vesicle/bud leaving the TIRF field; no direct scission claim follows. |
| micro47-go-triskelion-candidates | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0071439,GO:0030131; Complete exact GO0071439 and GO0030131 results, definitions, synonyms and typed child relations. | supports | GO0071439 is active clathrin complex, with exact synonym clathrin triskelion and definition of three heavy plus three light chains that polymerize into a vesicle-associated scaffold. GO0030131 is an AP-type clathrin adaptor complex, not an exact identity for the full heterogeneous endocytic epsin/Sla2/AP180 cohort in this target. |
| micro47-pmid9531549 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:9531549%20AND%20SRC:MED&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED9531549: Pan1p, yeast eps15, functions as a multivalent adaptor that coordinates protein-protein interactions essential for endocytosis. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro47-pmid14562095 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:14562095%20AND%20SRC:MED&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED14562095: Global analysis of protein localization in budding yeast. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro47-wendland1998-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2132731/; Complete Methods sec8 and sec10; Results sec17 and sec18 with Fig5 caption. Native journal HTML; no figure pixels inspected. | supports | Wendland1998 directly observes GFP-yAP180 puncta near the cell surface, concentrated in small buds and cytokinesis necks. Differential centrifugation supports membrane association but cannot precisely assign the smaller P100 pool. Cortical-actin colocalization is an inference: simultaneous GFP/actin imaging was unsuccessful. This supports the narrow native Bud annotation without inventing purified coat membership or direct actin colocalization. |
| schema-result | just validate data/structures/other/clathrin_coat_of_endocytic_vesicle.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/clathrin_coat_of_endocytic_vesicle.yaml |
| strict-result | just validate-strict data/structures/other/clathrin_coat_of_endocytic_vesicle.yaml --out /private/tmp/cellstructure-batch47-20261022-cz2022xg/clathrin_coat_of_endocytic_vesicle-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/clathrin_coat_of_endocytic_vesicle.yaml --out /private/tmp/cellstructure-batch47-20261022-cz2022xg/clathrin_coat_of_endocytic_vesicle-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch47-20261022-cz2022xg/clathrin_coat_of_endocytic_vesicle-strict.tsv |
| native-proteins | /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/other/clathrin_coat_of_endocytic_vesicle.yaml; Complete read-only focused native proteins log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-graphs | /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/clathrin_coat_of_endocytic_vesicle.yaml; Complete read-only focused native graphs log | supports | data/structures/other/clathrin_coat_of_endocytic_vesicle.yaml  (GO:0030128)<br>  endocytic_clathrin_coat_topology	clathrin_triskelion_scaffold	COVERED	-&gt;clathrin_triskelion_scaffold (UniProtKB:P22137, UniProtKB:P17891)<br>  endocytic_clathrin_coat_topology	endocytic_clathrin_adaptors	COVERED	-&gt;endocytic_clathrin_adaptors (UniProtKB:Q12518, UniProtKB:Q05785, UniProtKB:P33338, UniProtKB:P38856)<br>  endocytic_clathrin_coat_topology	ap2_adaptor_complex	UNANCHORED_WITH_UNIPROT	AP-2 adaptor complex (UniProtKB:P27351)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     2  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     1  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     3  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/other/clathrin_coat_of_endocytic_vesicle.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 20 of 22 collected target identifiers returned OK. PMID:14562095: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:9531549: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- COMMON retains its schema meaning present in most members with exceptional losses. The cited yeast studies support ordinary species-level occurrence qualitatively; they do not measure a species-wide prevalence census.
- No primary microscopy pixels, supplemental files or videos were inspected. Text, Methods and embedded figure captions were read only within the stated source extents.
- S288C reference-entry identity is distinct from the particular strains, mutants, tagged constructs and drug-treated cells in the primary studies.
- UNKNOWN formation necessity is retained; localization, cargo-traffic phenotypes, functional loss and formation of an entire coat are not interchangeable.
- Kaksonen2005 was read at complete native abstract tier only. It supports the modular endocytosis and initiation interpretation but detailed unseen experiments are not certified. Newpher itself leaves coat release versus vesicle departure unresolved.
- Huh2003 was read at complete native abstract tier only; its protein-specific primary table/pixels were not inspected. Native UniProt independently confirms the cited annotation join.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User expressly requests one review for every unreviewed record, including scientifically clean records.
- iModulonDB is not applicable to these clathrin-coat identity, molecular-family, localization and formation claims.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T050518Z-clathrin-coat-of-endocytic-vesicle-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-backed review of clathrin coat of endocytic vesicle
started_at: '2026-10-22T04:47:14Z'
finished_at: '2026-10-22T05:05:18Z'
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
summary: The coat identity, yeast examples and descriptive graph are supported at
  the declared source tiers. One bounded minor resolves the exact triskelion-complex
  grounding.
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
  - path: .claude/skills/uniprot-protein-examples/SKILL.md
    sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
    role: context
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/other/clathrin_coat_of_endocytic_vesicle.yaml
    sha256: 1c156e9a910b42e01f74505011a1f24644ca3ad0a8eeb48d438b3b8eeb7ed372
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
- target_id: GO:0030128
  path: data/structures/other/clathrin_coat_of_endocytic_vesicle.yaml
  label: clathrin coat of endocytic vesicle
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/clathrin_coat_of_endocytic_vesicle.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete target; no neighboring scientific-record verdict
    is imported. Exact authority, all current component/function/graph/source placements,
    taxonomic scope, formation semantics, history and discussions were reviewed.
  selection: Batch47 fixed strict path order, index 5; exactly one maintained target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0030128
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0030128
  command: just validate data/structures/other/clathrin_coat_of_endocytic_vesicle.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0030128
  command: just validate-strict data/structures/other/clathrin_coat_of_endocytic_vesicle.yaml
    --out /private/tmp/cellstructure-batch47-20261022-cz2022xg/clathrin_coat_of_endocytic_vesicle-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-proteins
  name: Focused native proteins
  status: passed
  required: true
  target_ids:
  - GO:0030128
  command: /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/clathrin_coat_of_endocytic_vesicle.yaml
  exit_code: 0
  summary: Read-only native check passed; claim-level protein/edge support evaluated
    separately.
  evidence_ids:
  - native-proteins
- check_id: native-graphs
  name: Focused native graphs
  status: passed
  required: true
  target_ids:
  - GO:0030128
  command: /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/clathrin_coat_of_endocytic_vesicle.yaml
  exit_code: 0
  summary: Read-only native check passed; claim-level protein/edge support evaluated
    separately.
  evidence_ids:
  - native-graphs
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0030128
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - micro47-go
  - micro47-tax4932
  - micro47-tax559292
  - micro47-protein-P22137
  - micro47-protein-P17891
  - micro47-protein-Q12518
  - micro47-protein-Q05785
  - micro47-protein-P33338
  - micro47-protein-P38856
  - micro47-protein-P27351
  - micro47-gene-CHC1
  - micro47-gene-CLC1
  - micro47-gene-ENT1
  - micro47-gene-ENT2
  - micro47-gene-SLA2
  - micro47-gene-YAP1801
  - micro47-newpher2005-meta
  - micro47-kaksonen2005-meta
  - micro47-newpher2005-duke
  - micro47-go-triskelion-candidates
  - micro47-pmid9531549
  - micro47-pmid14562095
  - micro47-wendland1998-legacy
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0030128
  summary: '20 of 22 collected target identifiers returned OK. PMID:14562095: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force.; PMID:9531549:
    UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected
    after the bulk eutils414 transport failure. Identity resolution does not certify
    every attached biological claim; declared abstract/body reading scope remains
    in force. Native source checks are separately scoped; skipped or unreachable identifiers
    are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - micro47-pmid14562095
  - micro47-pmid9531549
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0030128
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch47 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0030128
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch47 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0030128
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch47 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0030128
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch47 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0030128
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
    and current batch47 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/clathrin_coat_of_endocytic_vesicle.yaml
  locator: Complete maintained YAML; all components, source notes, graphs, discussions
    and historical entries
  accessed_at: '2026-10-22T04:59:22Z'
  support: context_only
  summary: The entire maintained target was read; no scientific record was changed.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent; ComponentTypeEnum; EssentialityEnum; graph scopes
  accessed_at: '2026-10-22T04:59:22Z'
  support: context_only
  summary: ComponentTypeEnum distinguishes LIPID from the permitted OTHER composite
    class. ESSENTIAL concerns failure of structure formation, not merely loss of catalytic
    or transport function.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Components; groundings; associated machinery and chaperone boundaries
  accessed_at: '2026-10-22T04:59:22Z'
  support: context_only
  summary: Components are taxon-agnostic molecular families/classes; exact family
    grounding is preferred when verified. Mature constituents and assembled-structure
    maintenance machinery differ from transient preassembly chaperones.
- evidence_id: micro47-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005768,GO:0005802,GO:0005905,GO:0012510,GO:0016020,GO:0030117,GO:0030118,GO:0030119,GO:0030120,GO:0030121,GO:0030122,GO:0030125,GO:0030128,GO:0030130,GO:0030132,GO:0030136,GO:0030140,GO:0030669,GO:0045334,GO:0072583
  locator: 'Complete exact entries GO0030128/0030130/0030125/0030120/0030118/0030117/0030119/0030121/0030122/0030669/0012510/0030140/0045334/0030136/0005768/0005802/0072583:
    id,name,definition,isObsolete,typed children and synonyms; shared response also
    includes pit/membrane entries.'
  accessed_at: '2026-10-22T04:48:27.885977Z'
  support: supports
  summary: GO0030128 is an active exact clathrin-coat identity, distinct from the
    membrane and whole vesicle it coats. The combined native response verifies the
    maintained is_a relations, the two specific coat-to-membrane part_of links, AP1/AP2
    boundaries and GO0072583 endocytosis. The broad coat-to-vesicle parthood is definition-supported;
    a direct GO0030125 part_of GO0030136 edge is not exposed in this response. GO0030118
    describes polymerized heavy/light-chain triskelions linked to membranes by adaptors.
    No exhaustive future inventory is inferred.
  snapshot_sha256: d99cebcf37913222815e3282d94e35f6fa629e25ca25660703949d4f38893d30
- evidence_id: micro47-tax4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete taxId/scientificName/rank/lineage/otherNames.
  accessed_at: '2026-10-22T04:15:34.948894Z'
  support: supports
  summary: ENA taxId 4932 identifies Saccharomyces cerevisiae at rank species; aliases
    and lineage match the record. Identity alone is not prevalence or experimental-condition
    evidence.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: micro47-tax559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete taxId/scientificName/rank/lineage/otherNames.
  accessed_at: '2026-10-22T04:15:34.948991Z'
  support: supports
  summary: ENA taxId 559292 identifies Saccharomyces cerevisiae S288C at rank strain;
    aliases and lineage match the record. Identity alone is not prevalence or experimental-condition
    evidence.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: micro47-protein-P22137
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P22137.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION comments and their evidence joins.
  accessed_at: '2026-10-22T04:48:27.888375Z'
  support: supports
  summary: P22137 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['CHC1'].
    Recommended identity, gene aliases, full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION
    comments and their evidence codes/PMIDs were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 09d51b91c677526fa74c1513304fdd8c51215ce5c9511a6654355fbd16c61648
- evidence_id: micro47-protein-P17891
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P17891.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION comments and their evidence joins.
  accessed_at: '2026-10-22T04:48:27.888620Z'
  support: supports
  summary: P17891 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['CLC1'].
    Recommended identity, gene aliases, full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION
    comments and their evidence codes/PMIDs were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 1b6e6853470eea45530073217e5f1abcfbe6fba0fc5568df34d83a73130d25af
- evidence_id: micro47-protein-Q12518
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q12518.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION comments and their evidence joins.
  accessed_at: '2026-10-22T04:51:23.117258Z'
  support: supports
  summary: Q12518 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['ENT1'].
    Recommended identity, gene aliases, full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION
    comments and their evidence codes/PMIDs were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 6c1b9e5e450f9d1a6f201a1fad51481ea96cb126bab7636c94158944e6f86954
- evidence_id: micro47-protein-Q05785
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q05785.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION comments and their evidence joins.
  accessed_at: '2026-10-22T04:51:23.116748Z'
  support: supports
  summary: Q05785 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['ENT2'].
    Recommended identity, gene aliases, full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION
    comments and their evidence codes/PMIDs were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 9e7e2475c19be4b5cd8d487b8aa185ba320b6793d8ecc39d2d8484c779c16560
- evidence_id: micro47-protein-P33338
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P33338.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION comments and their evidence joins.
  accessed_at: '2026-10-22T04:51:23.117443Z'
  support: supports
  summary: P33338 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['SLA2'].
    Recommended identity, gene aliases, full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION
    comments and their evidence codes/PMIDs were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: abd3ba999d75341ae5d58e46264fc5e6ffb114f680cfa65616b1bba382ff68c0
- evidence_id: micro47-protein-P38856
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P38856.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION comments and their evidence joins.
  accessed_at: '2026-10-22T04:51:23.117664Z'
  support: supports
  summary: P38856 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['YAP1801'].
    Recommended identity, gene aliases, full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION
    comments and their evidence codes/PMIDs were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 3d662ceac8783551c22e55f006cb5a1de580a8e71ce4902c4d4dc0a93ef479d6
- evidence_id: micro47-protein-P27351
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P27351.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION comments and their evidence joins.
  accessed_at: '2026-10-22T04:51:23.117895Z'
  support: supports
  summary: P27351 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['APL1'].
    Recommended identity, gene aliases, full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION
    comments and their evidence codes/PMIDs were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 94c3684403a35815a55bfd797ef48e9d555810dfe5df628234f65e677f38aa3d
- evidence_id: micro47-gene-CHC1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACHC1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete results of the retained exact gene/reviewed/taxon559292 URL.
  accessed_at: '2026-10-22T04:48:28.846864Z'
  support: supports
  summary: 'The exact reviewed S288C query for CHC1 returned 1 entry: P22137. Identity
    and primary gene symbol match; no current uniqueness discrepancy was observed.'
  snapshot_sha256: 2a920614f72637e8dca08d8a782c81c920e1e8a01fd1b0b958f6d70602c68b89
  search_scope: Remote UniProt exact gene CHC1, reviewed entries, organism_id559292
    only; complete returned result set inspected. Local ignored files are not applicable
    to this remote query.
- evidence_id: micro47-gene-CLC1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACLC1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete results of the retained exact gene/reviewed/taxon559292 URL.
  accessed_at: '2026-10-22T04:48:28.900316Z'
  support: supports
  summary: 'The exact reviewed S288C query for CLC1 returned 1 entry: P17891. Identity
    and primary gene symbol match; no current uniqueness discrepancy was observed.'
  snapshot_sha256: 263ed77f230c390b1cf03ce642b609d8cff66ef219794d4c6bccab47942bbc69
  search_scope: Remote UniProt exact gene CLC1, reviewed entries, organism_id559292
    only; complete returned result set inspected. Local ignored files are not applicable
    to this remote query.
- evidence_id: micro47-gene-ENT1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AENT1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete results of the retained exact gene/reviewed/taxon559292 URL.
  accessed_at: '2026-10-22T04:51:24.293984Z'
  support: supports
  summary: 'The exact reviewed S288C query for ENT1 returned 1 entry: Q12518. Identity
    and primary gene symbol match; no current uniqueness discrepancy was observed.'
  snapshot_sha256: 50ee85d64650abf316f9c3e03047d6f4a28522ac960d03e1584f0a1a3d7e88af
  search_scope: Remote UniProt exact gene ENT1, reviewed entries, organism_id559292
    only; complete returned result set inspected. Local ignored files are not applicable
    to this remote query.
- evidence_id: micro47-gene-ENT2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AENT2%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete results of the retained exact gene/reviewed/taxon559292 URL.
  accessed_at: '2026-10-22T04:51:24.778706Z'
  support: supports
  summary: 'The exact reviewed S288C query for ENT2 returned 1 entry: Q05785. Identity
    and primary gene symbol match; no current uniqueness discrepancy was observed.'
  snapshot_sha256: b71661bde72762ae3f353e8308b496e3195c9a46831b5482461513ea3f6f38c9
  search_scope: Remote UniProt exact gene ENT2, reviewed entries, organism_id559292
    only; complete returned result set inspected. Local ignored files are not applicable
    to this remote query.
- evidence_id: micro47-gene-SLA2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASLA2%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete results of the retained exact gene/reviewed/taxon559292 URL.
  accessed_at: '2026-10-22T04:51:24.809750Z'
  support: supports
  summary: 'The exact reviewed S288C query for SLA2 returned 1 entry: P33338. Identity
    and primary gene symbol match; no current uniqueness discrepancy was observed.'
  snapshot_sha256: 005f936651f5f6aca8806f3f26d72923a9ef0c272babade1957ac2a02ad03bd8
  search_scope: Remote UniProt exact gene SLA2, reviewed entries, organism_id559292
    only; complete returned result set inspected. Local ignored files are not applicable
    to this remote query.
- evidence_id: micro47-gene-YAP1801
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AYAP1801%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete results of the retained exact gene/reviewed/taxon559292 URL.
  accessed_at: '2026-10-22T04:51:24.826460Z'
  support: supports
  summary: 'The exact reviewed S288C query for YAP1801 returned 1 entry: P38856. Identity
    and primary gene symbol match; no current uniqueness discrepancy was observed.'
  snapshot_sha256: 9819c85ed82ad1607aa044c4343e87826481991d11124be2e79f001a62bbb308
  search_scope: Remote UniProt exact gene YAP1801, reviewed entries, organism_id559292
    only; complete returned result set inspected. Local ignored files are not applicable
    to this remote query.
- evidence_id: micro47-newpher2005-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.devcel.2005.04.014
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-21T10:57:50.523144Z'
  support: supports
  summary: 'Unique MED15992543: In vivo dynamics of clathrin and its adaptor-dependent
    recruitment to the actin-based endocytic machinery in yeast. Authors/year/DOI
    and the complete native abstract were inspected. This row establishes bibliographic
    identity and abstract-level content only; detailed experiments require separately
    specified body evidence.'
  snapshot_sha256: c99ec084fa3f65e3b5107699c30f42b09489dbc49d6be518d71ff9352d5a199c
- evidence_id: micro47-kaksonen2005-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.cell.2005.09.024
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-21T11:04:40.023205Z'
  support: supports
  summary: 'Unique MED16239147: A modular design for the clathrin- and actin-mediated
    endocytosis machinery. Authors/year/DOI and the complete native abstract were
    inspected. This row establishes bibliographic identity and abstract-level content
    only; detailed experiments require separately specified body evidence.'
  snapshot_sha256: b21f04a2ca620468ebafa02936207fe7e04553d44f862f3f18d72a85b6c4aba2
- evidence_id: micro47-newpher2005-duke
  kind: primary_source
  reference: https://dukespace.lib.duke.edu/server/api/core/bitstreams/e3c70c30-e4a1-4ba0-8ea6-c50af4ba491e/content
  locator: 'Complete printed pp87–96: Summary/Introduction, Table1, all main Results/Discussion
    and Experimental Procedures, including Fig1–6 captions. Original Duke primary
    PDF; reading derivative only, no pixels, videos or supplements.'
  accessed_at: '2026-10-21T11:00:52.091438Z'
  support: supports
  summary: Newpher2005 directly images cortical clathrin and endocytic factors in
    budding yeast. WT TIRFM places clathrin before Abp1; extensive adaptor colocalization/recruitment
    tests use sla2Δ or LAT-A and multi-adaptor perturbations. Sla2/End3/Pan1 affect
    progression or release rather than being required for initial cortical recruitment.
    The authors explicitly cannot distinguish clathrin disassembly from a coated vesicle/bud
    leaving the TIRF field; no direct scission claim follows.
  snapshot_sha256: c848e911372b9afb9902e4a74e3cb3dd66ef90eb5e102024cc95fff648bb6c21
- evidence_id: micro47-go-triskelion-candidates
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0071439,GO:0030131
  locator: Complete exact GO0071439 and GO0030131 results, definitions, synonyms and
    typed child relations.
  accessed_at: '2026-10-22T04:48:54.266838Z'
  support: supports
  summary: GO0071439 is active clathrin complex, with exact synonym clathrin triskelion
    and definition of three heavy plus three light chains that polymerize into a vesicle-associated
    scaffold. GO0030131 is an AP-type clathrin adaptor complex, not an exact identity
    for the full heterogeneous endocytic epsin/Sla2/AP180 cohort in this target.
  snapshot_sha256: a425c7a31777f7b3c4b24ac1e05fc89fcc459966ef577607175f719c142e4e80
- evidence_id: micro47-pmid9531549
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:9531549%20AND%20SRC:MED&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:51:26.423083Z'
  support: supports
  summary: 'Unique MED9531549: Pan1p, yeast eps15, functions as a multivalent adaptor
    that coordinates protein-protein interactions essential for endocytosis. Authors/year/DOI
    and the complete native abstract were inspected. This row establishes bibliographic
    identity and abstract-level content only; detailed experiments require separately
    specified body evidence.'
  snapshot_sha256: def7139cee8721c3dd7929a259ef330c34599d4dc92cc5c4eca4a1715339fd99
- evidence_id: micro47-pmid14562095
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:14562095%20AND%20SRC:MED&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:51:26.516975Z'
  support: supports
  summary: 'Unique MED14562095: Global analysis of protein localization in budding
    yeast. Authors/year/DOI and the complete native abstract were inspected. This
    row establishes bibliographic identity and abstract-level content only; detailed
    experiments require separately specified body evidence.'
  snapshot_sha256: 8bbeed3381c96852db4221aac079da00e1bf5c50630629c24d4d9136e1645c21
- evidence_id: micro47-wendland1998-legacy
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2132731/
  locator: Complete Methods sec8 and sec10; Results sec17 and sec18 with Fig5 caption.
    Native journal HTML; no figure pixels inspected.
  accessed_at: '2026-10-22T04:52:20.414819Z'
  support: supports
  summary: 'Wendland1998 directly observes GFP-yAP180 puncta near the cell surface,
    concentrated in small buds and cytokinesis necks. Differential centrifugation
    supports membrane association but cannot precisely assign the smaller P100 pool.
    Cortical-actin colocalization is an inference: simultaneous GFP/actin imaging
    was unsuccessful. This supports the narrow native Bud annotation without inventing
    purified coat membership or direct actin colocalization.'
  snapshot_sha256: 98649cd0d7aacc29892e9444b89ea98e50c47cd452a0a737f1626db2881b42fa
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/clathrin_coat_of_endocytic_vesicle.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:47:16Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/clathrin_coat_of_endocytic_vesicle.yaml'
  snapshot_sha256: 1007ba6ba1213d9132bac1b554413321a39975cb4246a58bd8917d3a989b8ae9
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/clathrin_coat_of_endocytic_vesicle.yaml
    --out /private/tmp/cellstructure-batch47-20261022-cz2022xg/clathrin_coat_of_endocytic_vesicle-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:47:17Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/clathrin_coat_of_endocytic_vesicle.yaml\
    \ --out /private/tmp/cellstructure-batch47-20261022-cz2022xg/clathrin_coat_of_endocytic_vesicle-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch47-20261022-cz2022xg/clathrin_coat_of_endocytic_vesicle-strict.tsv"
  snapshot_sha256: e9027dc8c52af706dcc324a3048574a6adc2d71daf8eceef6819cfb8ce36040f
- evidence_id: native-proteins
  kind: validation
  reference: /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/clathrin_coat_of_endocytic_vesicle.yaml
  locator: Complete read-only focused native proteins log
  accessed_at: '2026-10-22T04:51:48.197948Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/clathrin_coat_of_endocytic_vesicle.yaml
  locator: Complete read-only focused native graphs log
  accessed_at: '2026-10-22T04:51:48.665461Z'
  support: supports
  summary: "data/structures/other/clathrin_coat_of_endocytic_vesicle.yaml  (GO:0030128)\n\
    \  endocytic_clathrin_coat_topology\tclathrin_triskelion_scaffold\tCOVERED\t->clathrin_triskelion_scaffold\
    \ (UniProtKB:P22137, UniProtKB:P17891)\n  endocytic_clathrin_coat_topology\tendocytic_clathrin_adaptors\t\
    COVERED\t->endocytic_clathrin_adaptors (UniProtKB:Q12518, UniProtKB:Q05785, UniProtKB:P33338,\
    \ UniProtKB:P38856)\n  endocytic_clathrin_coat_topology\tap2_adaptor_complex\t\
    UNANCHORED_WITH_UNIPROT\tAP-2 adaptor complex (UniProtKB:P27351)\n\ncausal_graphs\
    \ GENE_OR_PROTEIN node summary:\n     2  COVERED                   component_ref\
    \ target holds protein_examples covering all declared symbols\n     1  UNANCHORED_WITH_UNIPROT\
    \   no component_ref, but node carries a UniProtKB grounding or xref\n     0 \
    \ PARTIAL_EXAMPLES          component_ref target holds protein_examples but has\
    \ unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target\
    \ declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_NO_UNIPROT     no component_ref\
    \ and no UniProtKB grounding or xref on the node\n     3  total GENE_OR_PROTEIN\
    \ causal nodes"
  snapshot_sha256: 1bf6cb8dbcdcbe48050a08158541982b39a2d419670c0e758b79c64c3b2feb27
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/clathrin_coat_of_endocytic_vesicle.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '20 of 22 collected target identifiers returned OK. PMID:14562095: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force.; PMID:9531549:
    UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected
    after the bulk eutils414 transport failure. Identity resolution does not certify
    every attached biological claim; declared abstract/body reading scope remains
    in force. Native source checks are separately scoped; skipped or unreachable identifiers
    are not silently counted as resolved.'
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
  topic: Exact coat identity and topology
  outcome: supported
  target_ids:
  - GO:0030128
  summary: The exact active GO identity, definition and declared topology are supported.
    Specific coat-to-membrane part_of and is_a links are native typed relations; broad
    coat-to-whole-vesicle parthood is definition-supported rather than an exposed
    direct edge in this response. The proteinaceous coat remains distinct from a lipid
    membrane and from the whole vesicle. The endocytic and TGN terms are specific
    children of the broad vesicle-coat class.
  evidence_ids:
  - micro47-go
  - record
- assessment_id: scope
  area: scope
  topic: Species, strain and prevalence meaning
  outcome: supported
  target_ids:
  - GO:0030128
  summary: Species4932 and strain559292 identities are correct. COMMON means present
    in most species members with exceptional losses; ordinary yeast experiments provide
    qualitative support, not a measured prevalence denominator. Experimental strain/condition
    details are not silently replaced by the reference accession taxon.
  evidence_ids:
  - micro47-tax4932
  - micro47-tax559292
  - schema
  - micro47-newpher2005-meta
  - micro47-newpher2005-duke
  - micro47-kaksonen2005-meta
- assessment_id: proteins
  area: grounding
  topic: Native examples and query claims
  outcome: supported
  target_ids:
  - GO:0030128
  summary: All retained accession/gene/status/taxon pairs are correct. Exact reviewed
    S288C queries support the current single-hit claims. Identity-only examples remain
    identity evidence; primary membership and localization are assessed separately.
    P27351 is the APL1 beta subunit of AP2; its member example does not replace the
    complex identity GO0030122.
  evidence_ids:
  - micro47-protein-P22137
  - micro47-protein-P17891
  - micro47-protein-Q12518
  - micro47-protein-Q05785
  - micro47-protein-P33338
  - micro47-protein-P38856
  - micro47-protein-P27351
  - micro47-gene-CHC1
  - micro47-gene-CLC1
  - micro47-gene-ENT1
  - micro47-gene-ENT2
  - micro47-gene-SLA2
  - micro47-gene-YAP1801
- assessment_id: necessity
  area: grounding
  topic: Formation necessity
  outcome: unknown
  target_ids:
  - GO:0030128
  summary: The component essentiality values are already UNKNOWN. The inspected localization,
    association and trafficking data do not establish a single universal requirement
    for formation of every coat represented by this class. No unsupported ESSENTIAL
    claim is introduced.
  evidence_ids:
  - micro47-go
  - schema
  - record
  - micro47-newpher2005-meta
  - micro47-newpher2005-duke
  - micro47-kaksonen2005-meta
- assessment_id: components
  area: grounding
  topic: Exact triskelion versus heterogeneous adaptor cohort
  outcome: concern
  target_ids:
  - GO:0030128
  summary: Triskelion and adaptor membership is supported. The explicit PROTEIN_COMPLEX
    triskelion row has an exact native GO0071439 identity and should no longer remain
    REVIEWED_LABEL_ONLY. This grounds the triskelion building block, not the entire
    polymerized coat. The broader adaptor/cargo-selection cohort is not equivalent
    to AP2 or GO0030131, so its label-only representation remains bounded and no forced
    single-family mapping is proposed.
  evidence_ids:
  - micro47-go
  - micro47-go-triskelion-candidates
  - micro47-newpher2005-meta
  - micro47-newpher2005-duke
  - micro47-kaksonen2005-meta
  - record
  - curation
- assessment_id: sources
  area: evidence
  topic: Exact localization evidence placement
  outcome: supported
  target_ids:
  - GO:0030128
  summary: Wendland1998 supports the stated Bud annotation, and the native P38856
    Cytoplasm citation joins PMID14562095. Huh2003 was read only at complete abstract
    tier; the exact YAP1801 annotation is verified in native UniProt rather than an
    unread primary table. Newpher supplies independently read adaptor/cortical-clathrin
    context; Sla2 involvement is not called an obligatory initial recruitment factor.
  evidence_ids:
  - micro47-pmid9531549
  - micro47-pmid14562095
  - micro47-wendland1998-legacy
  - micro47-newpher2005-duke
  - micro47-protein-P38856
  - record
- assessment_id: graph
  area: graph
  topic: Coarse endocytic coat graph
  outcome: supported
  target_ids:
  - GO:0030128
  summary: The seven-node/seven-edge NONMECHANISTIC FUNCTION graph separates triskelion
    polymerization, adaptor association, AP2 part-of, coat/membrane/vesicle topology
    and endocytosis participation. Its scope expressly excludes a complete assembly/scission
    mechanism. Initial recruitment and later actin dynamics are not conflated with
    directly observed vesicle release.
  evidence_ids:
  - micro47-go
  - micro47-newpher2005-duke
  - micro47-go-triskelion-candidates
  - record
- assessment_id: coverage
  area: completeness
  topic: Whole-target coverage and bounded enrichment
  outcome: supported
  target_ids:
  - GO:0030128
  summary: The entire target, all current components/examples, source placements,
    graph, discussions and history were reviewed. The supported exact mapping issue
    is distinct from optional inventory expansion. No exhaustive absence claim is
    made for future broader-adaptor families; no local-neighbor scientific verdict
    is imported.
  evidence_ids:
  - micro47-go
  - record
  - curation
  - micro47-newpher2005-meta
  - micro47-newpher2005-duke
  - micro47-kaksonen2005-meta
findings:
- finding_id: F1
  issue_key: clathrin.clathrin_coat_of_endocytic_vesicle.exact_triskelion_grounding
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Use the verified exact clathrin-triskelion complex grounding
  description: The component explicitly denotes the source-neutral clathrin triskelion
    complex and declares REVIEWED_LABEL_ONLY. Active GO0071439 has the exact synonym
    clathrin triskelion and matching three-heavy/three-light complex definition. The
    current review can resolve this bounded grounding gap without equating the complete
    coat with one triskelion. The dated statement that no term was curated in an earlier
    pass is not judged as a false historical search report.
  target_ids:
  - GO:0030128
  field_paths:
  - components[0].grounding
  - components[0].grounding_status
  - components[0].grounding_notes
  evidence_ids:
  - micro47-go-triskelion-candidates
  - micro47-go
  - schema
  - curation
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/clathrin_coat_of_endocytic_vesicle.yaml
    role: maintained scientific record
  rule_id: Exact source scope, protein grounding and formation-specific essentiality
  native_severity: minor
  normalization_reason: 'Minor: biological identity and membership are already correct;
    the exact available sub-complex mapping resolves a non-blocking curation gap under
    the explicit label-only contract.'
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0030128
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/clathrin_coat_of_endocytic_vesicle.yaml
    role: maintained scientific record
  description: Ground the triskelion component to GO:0071439, update its label-only
    status/notes and linked node consistently, retain component IDs and the distinction
    between triskelion units and polymerized coat. Preserve heterogeneous adaptor
    scope.
  acceptance_checks:
  - Preserve exact supported identity, experimental organism and native versus recombinant
    context.
  - Attach source-specific evidence to each changed claim and retain historical provenance.
  - Native schema, strict, CURIE, protein and graph checks pass as applicable.
limitations:
- COMMON retains its schema meaning present in most members with exceptional losses.
  The cited yeast studies support ordinary species-level occurrence qualitatively;
  they do not measure a species-wide prevalence census.
- No primary microscopy pixels, supplemental files or videos were inspected. Text,
  Methods and embedded figure captions were read only within the stated source extents.
- S288C reference-entry identity is distinct from the particular strains, mutants,
  tagged constructs and drug-treated cells in the primary studies.
- UNKNOWN formation necessity is retained; localization, cargo-traffic phenotypes,
  functional loss and formation of an entire coat are not interchangeable.
- Kaksonen2005 was read at complete native abstract tier only. It supports the modular
  endocytosis and initiation interpretation but detailed unseen experiments are not
  certified. Newpher itself leaves coat release versus vesicle departure unresolved.
- Huh2003 was read at complete native abstract tier only; its protein-specific primary
  table/pixels were not inspected. Native UniProt independently confirms the cited
  annotation join.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User expressly requests one review for every unreviewed record, including scientifically
  clean records.
- iModulonDB is not applicable to these clathrin-coat identity, molecular-family,
  localization and formation claims.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
