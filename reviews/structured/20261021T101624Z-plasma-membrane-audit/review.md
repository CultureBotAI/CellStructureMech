# Plasma membrane identity, examples and bounded evidence review

- Review: 20261021T101624Z-plasma-membrane-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T09:59:50Z
- Finished UTC: 2026-10-21T10:16:24Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The plasma-membrane identity, material boundaries, examples and descriptive graph are supported with explicit access and formation-necessity limits. One minor correction is needed to the unqualified cytoplasmic membrane synonym scope.

## Scope And Provenance

Entire maintained target; fresh native GO/taxon/UniProt and exact-gene checks, full Calamia scans, specified bacterial review sections, limited archaeal/fungal review evidence and contextual archaeal review sections.

Selection: Eighth selected target in batch eighteen, fixed maintained-path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0005886 | data/structures/envelope/plasma_membrane.yaml | maintained | plasma membrane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native UniProt verify | passed | False | GO:0005886 | Native command passed; scientific membership and graph scope assessed independently. |
| Native UniProt causal-graphs | passed | False | GO:0005886 | Native command passed; scientific membership and graph scope assessed independently. |
| Focused native schema | passed | True | GO:0005886 | Focused validator passed. |
| Focused native strict | passed | True | GO:0005886 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0005886 | 19 identifiers OK; 4 transport/skipped residuals independently resolved. |
| Claim-level scientific review | passed | True | GO:0005886 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0005886 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0005886 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0005886 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0005886 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0005886 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Cell boundary distinct from outer membrane and compartments

identity: concern. Targets: GO:0005886.

Exact GO identity, membrane parent and cell-periphery parthood agree. The unqualified cytoplasmic membrane synonym is incorrectly typed NARROW although native GO treats it as exact and the maintained discussion calls it the same cell-bounding structure. The separately qualified bacterial inner membrane synonym remains appropriately narrow. Lipid-boundary wording avoids imposing a bilayer on archaeal examples.

### Mixed lipids and unrelated integral proteins

grounding: supported. Targets: GO:0005886.

The component rows denote a topology-defined lipid cohort and unrelated integral proteins, not one identified lipid species or homologous protein family. Label-only representation preserves that boundary. Collective lipid material constitutes the defined membrane; this identity conclusion does not establish formation necessity for each lipid species or integral protein.

### Formation necessity remains separate from identity and activity

evidence: unknown. Targets: GO:0005886.

The integral-protein cohort is marked CONDITIONAL, but the inspected localization, transport and fusion studies do not independently establish the conditions under which the whole plasma membrane fails to form without that cohort. ESSENTIAL for collective lipid material expresses the defining lipid-boundary constitution; no individual lipid-species necessity is demonstrated. This uncertainty does not justify replacing assembly necessity with function or viability, and does not establish a contrary biological result.

### Verified identities and separated localization evidence

evidence: supported. Targets: GO:0005886.

All four reviewed accessions, genes and paired taxa resolve exactly, with native verify and graph coverage passing. LacY experimental PubMed links match the entry and Calamia body. SecY is independently placed in the inner membrane by Silhavy. Pma1 membrane location and Hxt1 GO plasma-membrane annotations are database-level corroboration; the example notes appropriately limit their UniProt citations to identity, without turning gene-query uniqueness into membership proof.

### Occurrence and model-organism context

scope: supported. Targets: GO:0005886.

Taxon receipts identify each named species, strain, kingdom or domain only. UNIVERSAL refers to possession of a cell-bounding membrane, not a universal MCC architecture, lipid headgroup or respiratory chain. Douglas/Konopka abstract supports the fungal membrane-domain context and S.cerevisiae example; exact domain prevalence and every fungal lineage were not surveyed.

### Permeability, transport and energy functions

evidence: supported. Targets: GO:0005886.

Bacterial inner-membrane transport and energy roles are directly described in the read review, while fungal domain/transport context is supported at review-abstract tier. Archaeal ether-lipid boundary and embedded transport are corroborated at stated review scopes. Bioenergetics is retained as a class-level activity description, not proof that every bacterium or archaeon has all named complexes in this location; exact Albers body attribution remains access-limited.

### Explicitly descriptive boundary organization

graph: supported. Targets: GO:0005886.

The NONMECHANISTIC graph captures lipid-boundary assembly, enclosure and protein embedding/transport without specifying a universal biosynthetic pathway or lipid topology. A GENE_OR_PROTEIN cohort may inherit the four concrete examples without equating each accession to the entire class.

### Bounded review result with source access limits

completeness: supported. Targets: GO:0005886.

One bounded synonym-scope correction was established. No additional issue follows from optional chemical or protein inventories. Review abstracts, native database evidence and inspected primary scans retain distinct tiers. No existing quote or image requires reuse-license assessment; historical actions and PROPOSED state remain unchanged.

## Findings

### F1: Use exact scope for the unqualified cytoplasmic membrane synonym

minor / open / confirmed; issue key: plasma-membrane-cytoplasmic-synonym-scope.

The bare cytoplasmic membrane synonym is typed NARROW, but native GO0005886 lists it as EXACT and the maintained resolved discussion describes the same cell-bounding structure. Its bacterial review citation does not by itself restrict the unqualified name to a biologically narrower class. The distinct bacterial inner membrane row is already explicitly qualified and can remain narrow.

## Recommended Actions And Acceptance Checks

### A1

Type unqualified cytoplasmic membrane as EXACT_SYNONYM and cite GO0005886, or explicitly qualify the synonym text if a narrower bacterial name is intended. Retain bacterial inner membrane as NARROW_SYNONYM.

- Confirm the exact native GO synonym and revised text/source agree.
- Preserve archaeal-compatible lipid-boundary wording and the separate bacterial inner membrane row.
- Run focused schema and strict-reference validation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/envelope/plasma_membrane.yaml; Entire maintained YAML including definition, components, functions, hierarchy, examples, graph edges, discussions, image metadata and history | context_only | All fields were read after fresh native inspection; the maintained target and PROPOSED state are unchanged. |
| policy | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, CausalNode and source-specific ComplexComposition contracts; essentiality definition; docs/CURATION.md assembly-versus-function guidance and review checklist | context_only | Component family identity, concrete protein identity and source-specific assembly membership are separate. Essentiality asks whether the structure forms without the component; membership and activity do not establish it. Optional fields are not mandatory. CausalNode permits protein complexes; its xrefs contract does not inherit the top-level record equivalence restriction. |
| plasma-membrane-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0005886,GO%3A0016020,GO%3A0071944,GO%3A0005737,GO%3A0055085; All five native definitions, synonyms and relevant parent-child relationships | supports | GO0005886 identifies the cell-bounding membrane, GO0016020 its broader membrane class, and GO0071944 lists it as a part. GO0005737 identifies cytoplasm and GO0055085 transmembrane transport. Native GO also uses cytoplasmic membrane as an exact synonym; the maintained bacterial-source naming convention is assessed in its stated microbial context. |
| plasma-membrane-agent-tax-2 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2; Complete taxId, scientificName, rank, lineage and relevant synonyms | supports | Native ENA taxonomy identifies Bacteria, domain. This receipt attests that identity and rank only, not occurrence or the experimental strain. |
| plasma-membrane-agent-tax-2157 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2157; Complete taxId, scientificName, rank, lineage and relevant synonyms | supports | Native ENA taxonomy identifies Archaea, domain. This receipt attests that identity and rank only, not occurrence or the experimental strain. |
| plasma-membrane-agent-tax-4751 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4751; Complete taxId, scientificName, rank, lineage and relevant synonyms | supports | Native ENA taxonomy identifies Fungi, kingdom. This receipt attests that identity and rank only, not occurrence or the experimental strain. |
| plasma-membrane-agent-tax-562 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562; Complete taxId, scientificName, rank, lineage and relevant synonyms | supports | Native ENA taxonomy identifies Escherichia coli, species. This receipt attests that identity and rank only, not occurrence or the experimental strain. |
| plasma-membrane-agent-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete taxId, scientificName, rank, lineage and relevant synonyms | supports | Native ENA taxonomy identifies Saccharomyces cerevisiae, species. This receipt attests that identity and rank only, not occurrence or the experimental strain. |
| plasma-membrane-agent-tax-83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Complete taxId, scientificName, rank, lineage and relevant synonyms | supports | Native ENA taxonomy identifies Escherichia coli K-12, strain. This receipt attests that identity and rank only, not occurrence or the experimental strain. |
| plasma-membrane-agent-tax-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete taxId, scientificName, rank, lineage and relevant synonyms | supports | Native ENA taxonomy identifies Saccharomyces cerevisiae S288C, strain. This receipt attests that identity and rank only, not occurrence or the experimental strain. |
| plasma-membrane-agent-doi-cshperspect_a000414 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1101/cshperspect.a000414; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies The bacterial cell envelope. Authors: Silhavy TJ, Kahne D, Walker S.; PMID 20452953; DOI 10.1101/cshperspect.a000414. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| plasma-membrane-agent-doi-10.1093_femsre_fuv008 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1093/femsre/fuv008&amp;format=json&amp;resultType=core; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Bacterial membrane lipids: diversity in structures and pathways. Authors: Sohlenkamp C, Geiger O.; PMID 25862689; DOI 10.1093/femsre/fuv008. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| plasma-membrane-agent-doi-10.1038_nrmicro2576 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038/nrmicro2576&amp;format=json&amp;resultType=core; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies The archaeal cell envelope. Authors: Albers SV, Meyer BH.; PMID 21572458; DOI 10.1038/nrmicro2576. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| plasma-membrane-agent-pmid-25002088 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A25002088%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Fungal membrane organization: the eisosome concept. Authors: Douglas LM, Konopka JB.; PMID 25002088; DOI 10.1146/annurev-micro-091313-103507. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| plasma-membrane-agent-pmid-2164211 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A2164211%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies lac permease of Escherichia coli: topology and sequence elements promoting membrane insertion. Authors: Calamia J, Manoil C.; PMID 2164211; DOI 10.1073/pnas.87.13.4937. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| plasma-membrane-agent-pmid-7000781 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A7000781%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Solubilization and reconstitution of the lactose transport system from Escherichia coli. Authors: Newman MJ, Wilson TH.; PMID 7000781; DOI 10.1016/s0021-9258(19)70345-7. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| plasma-membrane-agent-pmid-7028742 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A7028742%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Purification and reconstitution of functional lactose carrier from Escherichia coli. Authors: Newman MJ, Foster DL, Wilson TH, Kaback HR.; PMID 7028742; DOI 10.1016/s0021-9258(19)68477-2. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| plasma-membrane-agent-silhavy2010-legacy-html | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2857177/; PMC2857177: section s1 opening, s1a Outer Membrane, s1b Peptidoglycan, s1c Periplasm, s1d Inner Membrane, s1e Transenvelope Machines; s1f paragraphs on SecYEG translocation, alternating signal/start-stop membrane insertion and YidC. Other biogenesis paragraphs and Gram-positive sections were not comprehensively audited here. | supports | Silhavy, Kahne and Walker2010 is review-tier synthesis. It distinguishes inner membrane, peptidoglycan, periplasm and outer membrane; identifies transport and energy functions of the inner membrane; and places SecYEG in that membrane. These are bacterial examples, not a universal lipid composition or protein inventory. |
| plasma-membrane-agent-sohlenkamp2016-html | https://oup.silverchair-cdn.com/article-minimal/2467617; Publisher full HTML: Abstract and complete Introduction; bibliographic issue2016 versus first-online2015 identity checked. Later pathway sections were not comprehensively audited. | supports | Sohlenkamp and Geiger is a review of bacterial membrane lipid structural diversity and biosynthesis. The introduction distinguishes bacterial inner/plasma and outer membranes and varied amphiphilic lipid classes; this does not identify one invariant plasma-membrane lipid species across taxa. |
| plasma-membrane-agent-albers2011-pdf | https://www.nature.com/articles/nrmicro2576.pdf; Publisher HTML Key Points, Abstract and access boundary; bibliography is not treated as read primary evidence | supports | Despite its filename and HTTP200, this response is a publisher HTML landing page, not the full PDF. The directly read Key Points identify archaeal ether rather than bacterial ester lipids; Abstract states the single-membrane pattern with one exception and common S-layers. Detailed body claims are access-limited. |
| plasma-membrane-agent-ellen2010-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI:10.1155/2010/608243; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Shaping the archaeal cell envelope. Authors: Ellen AF, Zolghadr B, Driessen AM, Albers SV.; PMID 20671907; DOI 10.1155/2010/608243. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| plasma-membrane-agent-ellen2010-browser | https://onlinelibrary.wiley.com/doi/10.1155/2010/608243; Displayed publisher review section1 and section2.1, including Figure1 caption; browser capture has no native HTTP status | supports | Supplemental review context from Ellen et al.2010 explicitly distinguishes diether bilayers and tetraether monolayers, and describes membrane-embedded archaeal Sec transport. It independently bounds the retained topology statement; it does not stand in for the unread Albers2011 body or establish a universal respiratory apparatus. |
| plasma-membrane-agent-douglas2014-pdf | https://www.annualreviews.org/doi/pdf/10.1146/annurev-micro-091313-103507; Actual response body and retrieval receipt | context_only | Publisher route returned403 HTML; the Douglas/Konopka2014 body was not recovered. The maintained claims are assessed from its verified review abstract, which describes fungal membrane domains and the S.cerevisiae MCC example. |
| plasma-membrane-agent-douglas2014-publisher | https://www.annualreviews.org/content/journals/10.1146/annurev-micro-091313-103507; Actual response body and retrieval receipt | context_only | Publisher route returned403 HTML; the Douglas/Konopka2014 body was not recovered. The maintained claims are assessed from its verified review abstract, which describes fungal membrane domains and the S.cerevisiae MCC example. |
| plasma-membrane-agent-P02920 | https://rest.uniprot.org/uniprotkb/P02920.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB P02920 identifies Lactose permease, gene lacY, taxon83333. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| plasma-membrane-agent-query-lacY | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AlacY%20AND%20organism_id%3A83333%20AND%20reviewed%3Atrue&amp;format=json&amp;size=500; All returned results for exact gene lacY, organism 83333, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns P02920. This checks identifier resolution only. |
| plasma-membrane-agent-P0AGA2 | https://rest.uniprot.org/uniprotkb/P0AGA2.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB P0AGA2 identifies Protein translocase subunit SecY, gene secY, taxon83333. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| plasma-membrane-agent-query-secY | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AsecY%20AND%20organism_id%3A83333%20AND%20reviewed%3Atrue&amp;format=json&amp;size=500; All returned results for exact gene secY, organism 83333, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns P0AGA2. This checks identifier resolution only. |
| plasma-membrane-agent-P05030 | https://rest.uniprot.org/uniprotkb/P05030.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB P05030 identifies Plasma membrane ATPase 1, gene PMA1, taxon559292. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| plasma-membrane-agent-query-PMA1 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3APMA1%20AND%20organism_id%3A559292%20AND%20reviewed%3Atrue&amp;format=json&amp;size=500; All returned results for exact gene PMA1, organism 559292, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns P05030. This checks identifier resolution only. |
| plasma-membrane-agent-P32465 | https://rest.uniprot.org/uniprotkb/P32465.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant; GO0005886 cross-reference and associated evidence records | supports | Native reviewed UniProtKB P32465 identifies Low-affinity glucose transporter HXT1, gene HXT1, taxon559292. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. Its GO0005886 cross-reference has SGD IDA annotations with PMID10377429/24124599; those papers were not independently read, so this remains database-level localization evidence. |
| plasma-membrane-agent-query-HXT1 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AHXT1%20AND%20organism_id%3A559292%20AND%20reviewed%3Atrue&amp;format=json&amp;size=500; All returned results for exact gene HXT1, organism 559292, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns P32465. This checks identifier resolution only. |
| plasma-membrane-agent-calamia1990-page1 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/35d7/54236/dc659e784616/pnas01038-0052.png; Native PMC54236 PNG scan. Printed p4937: title/authors, Abstract, Introduction, complete Materials and methods, and Results fusion-isolation opening. Entire scan visually read. | supports | This page introduces36 LacY-PhoA fusions and the12-versus14-transmembrane-model comparison. It specifies bacterial strains, growth/assay conditions, fusion construction and protein immunoprecipitation methods. Its Abstract states the study-level topology conclusion. |
| plasma-membrane-agent-calamia1990-page2 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/35d7/54236/957636ab68ea/pnas01038-0053.png; Native PMC54236 PNG scan. Printed p4938: Results fusion construction and alkaline-phosphatase activities; complete Table1 of hybrid-protein properties. Entire scan visually read. | supports | Fusion-junction activities are compared with competing topology models. Table1 records positions, activities and other hybrid-protein properties. The text explains why the central-region activities favor the12-helix model over the14-helix alternative. |
| plasma-membrane-agent-calamia1990-page3 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/35d7/54236/43af54c2f24c/pnas01038-0054.png; Native PMC54236 PNG scan. Printed p4939: Figures1-3 with complete captions; Results minimum-segment tests and protein production/stability opening. Entire scan visually read. | supports | Figure1 relates fusion activities to the two topology models; Figure2 maps junctions in segments3/5; Figure3 identifies hybrid proteins. Results report that short nonpolar stretches can promote PhoA translocation and begin the hybrid-protein stability analysis. |
| plasma-membrane-agent-calamia1990-page4 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/35d7/54236/9d8dc864b102/pnas01038-0055.png; Native PMC54236 PNG scan. Printed p4940: Figure4 pulse-chase stability; Results toxicity and lac activity; Discussion opening. Entire scan visually read. | supports | The page compares hybrid stability, toxicity and lactose-utilization effects. Discussion explains the topology evidence favoring12 helices and addresses fusions with intermediate activities. These measurements concern LacY topology and fusion behavior, not formation of the complete plasma membrane. |
| plasma-membrane-agent-calamia1990-page5 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/35d7/54236/56d268b65926/pnas01038-0056.png; Native PMC54236 PNG scan. Printed p4941: Discussion continuation, acknowledgments and references1-25. Entire scan visually read. | supports | Discussion interprets proteolytic stability and incoming-versus-outgoing segment fusion behavior. It distinguishes short export-promoting sequence stretches from additional residues potentially needed for stable membrane anchoring. The remaining page contains acknowledgments and references. |
| plasma-membrane-agent-newman1980-pdf | https://www.jbc.org/article/S0021-9258(19)70345-7/pdf; Actual response body and retrieval receipt | context_only | JBC PDF request returned403 HTML. Native metadata/abstract and exact UniProt experimental-reference linkage were checked, but this route did not provide readable full text. |
| plasma-membrane-agent-newman1981-pdf | https://www.jbc.org/article/S0021-9258(19)68477-2/pdf; Actual response body and retrieval receipt | context_only | JBC PDF request returned403 HTML. Native metadata/abstract and exact UniProt experimental-reference linkage were checked, but this route did not provide readable full text. |
| native-verify | /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/envelope/plasma_membrane.yaml --verify; Captured focused native verify log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/envelope/plasma_membrane.yaml --causal-graphs; Captured focused native causal-graphs log | supports | data/structures/envelope/plasma_membrane.yaml  (GO:0005886)<br>  lipid_membrane_boundary	integral_plasma_membrane_proteins	COVERED	-&gt;integral_plasma_membrane_proteins (UniProtKB:P02920, UniProtKB:P05030, UniProtKB:P32465, UniProtKB:P0AGA2)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     1  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/envelope/plasma_membrane.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/envelope/plasma_membrane.yaml |
| strict-result | just validate-strict data/structures/envelope/plasma_membrane.yaml --out /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/plasma_membrane-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/envelope/plasma_membrane.yaml --out /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/plasma_membrane-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch18-20261021-5wxxz5kh/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/plasma_membrane-strict.tsv |
| target-curies | just check-curies-strict; data/structures/envelope/plasma_membrane.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 19 of23 collected target identifiers returned OK in this fresh base resolver run. Residuals: PMID:2164211: UNREACHABLE; resolved by evidence plasma-membrane-agent-pmid-2164211; PMID:25002088: UNREACHABLE; resolved by evidence plasma-membrane-agent-pmid-25002088; PMID:7000781: UNREACHABLE; resolved by evidence plasma-membrane-agent-pmid-7000781; PMID:7028742: UNREACHABLE; resolved by evidence plasma-membrane-agent-pmid-7028742. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Albers and Meyer2011 is limited to verified native metadata, publisher Key Points and Abstract; its apparent PDF response is HTML. Douglas and Konopka2014 is limited to verified native metadata/abstract after publisher403 responses. These are reviews, not primary experiments.
- Sohlenkamp/Geiger Abstract and Introduction and named Silhavy sections were read, not every pathway or primary citation. Ellen2010 sections1/2.1 provide supplemental review context only and do not replace access to the maintained Albers citation.
- Calamia1990 all five genuine primary page scans were visually read. Newman1980/1981 full PDFs were unavailable; their exact native abstracts and UniProt reference links were verified. Pma1/Hxt1 annotation-source primary papers were not independently reviewed.
- No individual lipid or integral protein removal establishes whether the generic plasma membrane forms without it. Collective lipid material is defining; CONDITIONAL necessity of the broad protein cohort is not independently established and is not redefined as functional activity.
- Taxonomy authority is not occurrence evidence. This record-level audit does not survey every fungal domain arrangement, archaeal energy-localization exception or bacterial respiratory strategy.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T101624Z-plasma-membrane-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Plasma membrane identity, examples and bounded evidence review
started_at: '2026-10-21T09:59:50Z'
finished_at: '2026-10-21T10:16:24Z'
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
summary: The plasma-membrane identity, material boundaries, examples and descriptive
  graph are supported with explicit access and formation-necessity limits. One minor
  correction is needed to the unqualified cytoplasmic membrane synonym scope.
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
  - path: .claude/skills/uniprot-protein-examples/SKILL.md
    sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
    role: context
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/envelope/plasma_membrane.yaml
    sha256: 20619b6099645731d2a8ee641c76ec5130b747bac304fb61ccccfd0b5693d25d
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
  - path: scripts/uniprot_genes.py
    sha256: feb9042b212bc639bc2603c186c6e328fa142c2641e93fc1418ad5a14e1d5faf
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: GO:0005886
  path: data/structures/envelope/plasma_membrane.yaml
  label: plasma membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/envelope/plasma_membrane.yaml
    role: maintained scientific record
scope:
  description: Entire maintained target; fresh native GO/taxon/UniProt and exact-gene
    checks, full Calamia scans, specified bacterial review sections, limited archaeal/fungal
    review evidence and contextual archaeal review sections.
  selection: Eighth selected target in batch eighteen, fixed maintained-path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0005886
checks:
- check_id: native-verify
  name: Native UniProt verify
  status: passed
  required: false
  target_ids:
  - GO:0005886
  command: /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/envelope/plasma_membrane.yaml
    --verify
  exit_code: 0
  summary: Native command passed; scientific membership and graph scope assessed independently.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Native UniProt causal-graphs
  status: passed
  required: false
  target_ids:
  - GO:0005886
  command: /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/envelope/plasma_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Native command passed; scientific membership and graph scope assessed independently.
  evidence_ids:
  - native-causal-graphs
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0005886
  command: just validate data/structures/envelope/plasma_membrane.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0005886
  command: just validate-strict data/structures/envelope/plasma_membrane.yaml --out
    /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/plasma_membrane-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0005886
  summary: 19 identifiers OK; 4 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - plasma-membrane-agent-pmid-2164211
  - plasma-membrane-agent-pmid-25002088
  - plasma-membrane-agent-pmid-7000781
  - plasma-membrane-agent-pmid-7028742
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0005886
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - plasma-membrane-agent-go
  - plasma-membrane-agent-tax-2
  - plasma-membrane-agent-tax-2157
  - plasma-membrane-agent-tax-4751
  - plasma-membrane-agent-tax-562
  - plasma-membrane-agent-tax-4932
  - plasma-membrane-agent-tax-83333
  - plasma-membrane-agent-tax-559292
  - plasma-membrane-agent-doi-cshperspect_a000414
  - plasma-membrane-agent-doi-10.1093_femsre_fuv008
  - plasma-membrane-agent-doi-10.1038_nrmicro2576
  - plasma-membrane-agent-pmid-25002088
  - plasma-membrane-agent-pmid-2164211
  - plasma-membrane-agent-pmid-7000781
  - plasma-membrane-agent-pmid-7028742
  - plasma-membrane-agent-silhavy2010-legacy-html
  - plasma-membrane-agent-sohlenkamp2016-html
  - plasma-membrane-agent-albers2011-pdf
  - plasma-membrane-agent-ellen2010-meta
  - plasma-membrane-agent-ellen2010-browser
  - plasma-membrane-agent-douglas2014-pdf
  - plasma-membrane-agent-douglas2014-publisher
  - plasma-membrane-agent-P02920
  - plasma-membrane-agent-query-lacY
  - plasma-membrane-agent-P0AGA2
  - plasma-membrane-agent-query-secY
  - plasma-membrane-agent-P05030
  - plasma-membrane-agent-query-PMA1
  - plasma-membrane-agent-P32465
  - plasma-membrane-agent-query-HXT1
  - plasma-membrane-agent-calamia1990-page1
  - plasma-membrane-agent-calamia1990-page2
  - plasma-membrane-agent-calamia1990-page3
  - plasma-membrane-agent-calamia1990-page4
  - plasma-membrane-agent-calamia1990-page5
  - plasma-membrane-agent-newman1980-pdf
  - plasma-membrane-agent-newman1981-pdf
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0005886
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
  - GO:0005886
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
  - GO:0005886
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
  - GO:0005886
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
  - GO:0005886
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
  reference: data/structures/envelope/plasma_membrane.yaml
  locator: Entire maintained YAML including definition, components, functions, hierarchy,
    examples, graph edges, discussions, image metadata and history
  accessed_at: '2026-10-21T10:11:23Z'
  support: context_only
  summary: All fields were read after fresh native inspection; the maintained target
    and PROPOSED state are unchanged.
- evidence_id: policy
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, CausalNode and source-specific ComplexComposition
    contracts; essentiality definition; docs/CURATION.md assembly-versus-function
    guidance and review checklist
  accessed_at: '2026-10-21T10:11:23Z'
  support: context_only
  summary: Component family identity, concrete protein identity and source-specific
    assembly membership are separate. Essentiality asks whether the structure forms
    without the component; membership and activity do not establish it. Optional fields
    are not mandatory. CausalNode permits protein complexes; its xrefs contract does
    not inherit the top-level record equivalence restriction.
- evidence_id: plasma-membrane-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0005886,GO%3A0016020,GO%3A0071944,GO%3A0005737,GO%3A0055085
  locator: All five native definitions, synonyms and relevant parent-child relationships
  accessed_at: '2026-10-21T10:00:23.966336Z'
  support: supports
  summary: GO0005886 identifies the cell-bounding membrane, GO0016020 its broader
    membrane class, and GO0071944 lists it as a part. GO0005737 identifies cytoplasm
    and GO0055085 transmembrane transport. Native GO also uses cytoplasmic membrane
    as an exact synonym; the maintained bacterial-source naming convention is assessed
    in its stated microbial context.
  snapshot_sha256: cb8ac6d93b058b92d034bf5dfaf5aceb5289bed150037a336be4b68f4cc62a97
- evidence_id: plasma-membrane-agent-tax-2
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2
  locator: Complete taxId, scientificName, rank, lineage and relevant synonyms
  accessed_at: '2026-10-21T10:00:24.635222Z'
  support: supports
  summary: Native ENA taxonomy identifies Bacteria, domain. This receipt attests that
    identity and rank only, not occurrence or the experimental strain.
  snapshot_sha256: 314bd7723b8dea04f1840809fb74e06c514664fba9c6a0619e8f12e2a6dceef1
- evidence_id: plasma-membrane-agent-tax-2157
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2157
  locator: Complete taxId, scientificName, rank, lineage and relevant synonyms
  accessed_at: '2026-10-21T10:00:24.696056Z'
  support: supports
  summary: Native ENA taxonomy identifies Archaea, domain. This receipt attests that
    identity and rank only, not occurrence or the experimental strain.
  snapshot_sha256: c6e652011b95e43e933983bf5f3f5cec9508c1925adae00dc55e46cd4e816b19
- evidence_id: plasma-membrane-agent-tax-4751
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4751
  locator: Complete taxId, scientificName, rank, lineage and relevant synonyms
  accessed_at: '2026-10-21T10:00:24.713691Z'
  support: supports
  summary: Native ENA taxonomy identifies Fungi, kingdom. This receipt attests that
    identity and rank only, not occurrence or the experimental strain.
  snapshot_sha256: a7bab59bce650c0d29732327d4e7e342f1b648747f7f9635958f923b4a6089e6
- evidence_id: plasma-membrane-agent-tax-562
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562
  locator: Complete taxId, scientificName, rank, lineage and relevant synonyms
  accessed_at: '2026-10-21T10:00:24.725326Z'
  support: supports
  summary: Native ENA taxonomy identifies Escherichia coli, species. This receipt
    attests that identity and rank only, not occurrence or the experimental strain.
  snapshot_sha256: ea038c30da3aab3426b7df16ce7a137cf2985e73d6ad8281971b9c390a74d2a8
- evidence_id: plasma-membrane-agent-tax-4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete taxId, scientificName, rank, lineage and relevant synonyms
  accessed_at: '2026-10-21T10:00:24.802401Z'
  support: supports
  summary: Native ENA taxonomy identifies Saccharomyces cerevisiae, species. This
    receipt attests that identity and rank only, not occurrence or the experimental
    strain.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: plasma-membrane-agent-tax-83333
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Complete taxId, scientificName, rank, lineage and relevant synonyms
  accessed_at: '2026-10-21T10:00:25.237026Z'
  support: supports
  summary: Native ENA taxonomy identifies Escherichia coli K-12, strain. This receipt
    attests that identity and rank only, not occurrence or the experimental strain.
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: plasma-membrane-agent-tax-559292
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete taxId, scientificName, rank, lineage and relevant synonyms
  accessed_at: '2026-10-21T10:00:25.319191Z'
  support: supports
  summary: Native ENA taxonomy identifies Saccharomyces cerevisiae S288C, strain.
    This receipt attests that identity and rank only, not occurrence or the experimental
    strain.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: plasma-membrane-agent-doi-cshperspect_a000414
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1101/cshperspect.a000414
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:01:39.409675Z'
  support: supports
  summary: 'Native metadata identifies The bacterial cell envelope. Authors: Silhavy
    TJ, Kahne D, Walker S.; PMID 20452953; DOI 10.1101/cshperspect.a000414. Bibliographic
    identity and available abstract only; not a substitute for inspected article body.'
  snapshot_sha256: 6dbe4b87edaa5c136c12c86c9d1dd160a184f8e75b68e56095dcffb08d567992
- evidence_id: plasma-membrane-agent-doi-10.1093_femsre_fuv008
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1093/femsre/fuv008&format=json&resultType=core
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T10:00:26.577299Z'
  support: supports
  summary: 'Native metadata identifies Bacterial membrane lipids: diversity in structures
    and pathways. Authors: Sohlenkamp C, Geiger O.; PMID 25862689; DOI 10.1093/femsre/fuv008.
    Bibliographic identity and available abstract only; not a substitute for inspected
    article body.'
  snapshot_sha256: 53fb76acf59bd8d6bd054dd470dd5c324822fe7ab9484c5908c9aae08c869d06
- evidence_id: plasma-membrane-agent-doi-10.1038_nrmicro2576
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038/nrmicro2576&format=json&resultType=core
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T10:00:26.639873Z'
  support: supports
  summary: 'Native metadata identifies The archaeal cell envelope. Authors: Albers
    SV, Meyer BH.; PMID 21572458; DOI 10.1038/nrmicro2576. Bibliographic identity
    and available abstract only; not a substitute for inspected article body.'
  snapshot_sha256: 204718d66e280a9f75c1f3242abcf74068d69a1466deb71ade85b43257574671
- evidence_id: plasma-membrane-agent-pmid-25002088
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A25002088%20AND%20SRC%3AMED&format=json&resultType=core
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T10:00:26.007714Z'
  support: supports
  summary: 'Native metadata identifies Fungal membrane organization: the eisosome
    concept. Authors: Douglas LM, Konopka JB.; PMID 25002088; DOI 10.1146/annurev-micro-091313-103507.
    Bibliographic identity and available abstract only; not a substitute for inspected
    article body.'
  snapshot_sha256: 71ecfd6a977ea4cf9b0a84f6d66894714be936e2e3b070bf44dff7d6e2139e1f
- evidence_id: plasma-membrane-agent-pmid-2164211
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A2164211%20AND%20SRC%3AMED&format=json&resultType=core
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T10:00:26.466796Z'
  support: supports
  summary: 'Native metadata identifies lac permease of Escherichia coli: topology
    and sequence elements promoting membrane insertion. Authors: Calamia J, Manoil
    C.; PMID 2164211; DOI 10.1073/pnas.87.13.4937. Bibliographic identity and available
    abstract only; not a substitute for inspected article body.'
  snapshot_sha256: 66773061a0f8aa9ac6333238ac47b6dcc95dd3d8050de3e364b975fab17d61c9
- evidence_id: plasma-membrane-agent-pmid-7000781
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A7000781%20AND%20SRC%3AMED&format=json&resultType=core
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T10:00:26.530625Z'
  support: supports
  summary: 'Native metadata identifies Solubilization and reconstitution of the lactose
    transport system from Escherichia coli. Authors: Newman MJ, Wilson TH.; PMID 7000781;
    DOI 10.1016/s0021-9258(19)70345-7. Bibliographic identity and available abstract
    only; not a substitute for inspected article body.'
  snapshot_sha256: d6c554697bbb39ca9394a47e9539339f2ccd119214c6819bd739b18d7e1fa48a
- evidence_id: plasma-membrane-agent-pmid-7028742
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A7028742%20AND%20SRC%3AMED&format=json&resultType=core
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T10:00:26.552097Z'
  support: supports
  summary: 'Native metadata identifies Purification and reconstitution of functional
    lactose carrier from Escherichia coli. Authors: Newman MJ, Foster DL, Wilson TH,
    Kaback HR.; PMID 7028742; DOI 10.1016/s0021-9258(19)68477-2. Bibliographic identity
    and available abstract only; not a substitute for inspected article body.'
  snapshot_sha256: 032ec39eccd829307dfec072d68a87e20516c7377b1fcc65209c2a087915ef14
- evidence_id: plasma-membrane-agent-silhavy2010-legacy-html
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2857177/
  locator: 'PMC2857177: section s1 opening, s1a Outer Membrane, s1b Peptidoglycan,
    s1c Periplasm, s1d Inner Membrane, s1e Transenvelope Machines; s1f paragraphs
    on SecYEG translocation, alternating signal/start-stop membrane insertion and
    YidC. Other biogenesis paragraphs and Gram-positive sections were not comprehensively
    audited here.'
  accessed_at: '2026-10-21T09:03:55.797283Z'
  support: supports
  summary: Silhavy, Kahne and Walker2010 is review-tier synthesis. It distinguishes
    inner membrane, peptidoglycan, periplasm and outer membrane; identifies transport
    and energy functions of the inner membrane; and places SecYEG in that membrane.
    These are bacterial examples, not a universal lipid composition or protein inventory.
  snapshot_sha256: 734e73fa7aafdfe44d5c447f32a07431c543b374d715a519947ee42c6b388c28
- evidence_id: plasma-membrane-agent-sohlenkamp2016-html
  kind: authority
  reference: https://oup.silverchair-cdn.com/article-minimal/2467617
  locator: 'Publisher full HTML: Abstract and complete Introduction; bibliographic
    issue2016 versus first-online2015 identity checked. Later pathway sections were
    not comprehensively audited.'
  accessed_at: '2026-10-21T10:01:37.763603Z'
  support: supports
  summary: Sohlenkamp and Geiger is a review of bacterial membrane lipid structural
    diversity and biosynthesis. The introduction distinguishes bacterial inner/plasma
    and outer membranes and varied amphiphilic lipid classes; this does not identify
    one invariant plasma-membrane lipid species across taxa.
  snapshot_sha256: a0e2e277435e67ac022544173d5ffc200f23879a77b5ad94932bdd0c4a39de6e
- evidence_id: plasma-membrane-agent-albers2011-pdf
  kind: authority
  reference: https://www.nature.com/articles/nrmicro2576.pdf
  locator: Publisher HTML Key Points, Abstract and access boundary; bibliography is
    not treated as read primary evidence
  accessed_at: '2026-10-21T10:01:37.833188Z'
  support: supports
  summary: Despite its filename and HTTP200, this response is a publisher HTML landing
    page, not the full PDF. The directly read Key Points identify archaeal ether rather
    than bacterial ester lipids; Abstract states the single-membrane pattern with
    one exception and common S-layers. Detailed body claims are access-limited.
  snapshot_sha256: 575694926a5792d5cbad6c67ce12e70ea4c590154f41d52b64999b885246cb65
- evidence_id: plasma-membrane-agent-ellen2010-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI:10.1155/2010/608243
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T10:08:08.674949Z'
  support: supports
  summary: 'Native metadata identifies Shaping the archaeal cell envelope. Authors:
    Ellen AF, Zolghadr B, Driessen AM, Albers SV.; PMID 20671907; DOI 10.1155/2010/608243.
    Bibliographic identity and available abstract only; not a substitute for inspected
    article body.'
  snapshot_sha256: 7e3a2f4f1d8389b08de62bb2b90fdb0c3d39a80cf981a4cbec8fe4a6c2df4d68
- evidence_id: plasma-membrane-agent-ellen2010-browser
  kind: authority
  reference: https://onlinelibrary.wiley.com/doi/10.1155/2010/608243
  locator: Displayed publisher review section1 and section2.1, including Figure1 caption;
    browser capture has no native HTTP status
  accessed_at: '2026-10-21T10:09:00Z'
  support: supports
  summary: Supplemental review context from Ellen et al.2010 explicitly distinguishes
    diether bilayers and tetraether monolayers, and describes membrane-embedded archaeal
    Sec transport. It independently bounds the retained topology statement; it does
    not stand in for the unread Albers2011 body or establish a universal respiratory
    apparatus.
  snapshot_sha256: 221dd9f93ced227cd64463bbcfaa100114a0e0fd94ec161bc2c76bf63bc3776b
- evidence_id: plasma-membrane-agent-douglas2014-pdf
  kind: authority
  reference: https://www.annualreviews.org/doi/pdf/10.1146/annurev-micro-091313-103507
  locator: Actual response body and retrieval receipt
  accessed_at: '2026-10-21T10:01:29.741344Z'
  support: context_only
  summary: Publisher route returned403 HTML; the Douglas/Konopka2014 body was not
    recovered. The maintained claims are assessed from its verified review abstract,
    which describes fungal membrane domains and the S.cerevisiae MCC example.
  snapshot_sha256: e94aa7d0fa76107936007effb3e0160e6c98ae0c915e5d2fb9ec9140842720d5
- evidence_id: plasma-membrane-agent-douglas2014-publisher
  kind: authority
  reference: https://www.annualreviews.org/content/journals/10.1146/annurev-micro-091313-103507
  locator: Actual response body and retrieval receipt
  accessed_at: '2026-10-21T10:00:34.701299Z'
  support: context_only
  summary: Publisher route returned403 HTML; the Douglas/Konopka2014 body was not
    recovered. The maintained claims are assessed from its verified review abstract,
    which describes fungal membrane domains and the S.cerevisiae MCC example.
  snapshot_sha256: b1f4711f6f03e0c79150315105c200a454323178003dcc32b35f9bb6d4e03e1d
- evidence_id: plasma-membrane-agent-P02920
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P02920.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T10:00:27.776517Z'
  support: supports
  summary: Native reviewed UniProtKB P02920 identifies Lactose permease, gene lacY,
    taxon83333. Concrete identity is checked independently of membership; relevant
    subunit/cofactor/location comments retain their own evidence scope.
  snapshot_sha256: dc9f2caffe4fad652b136c61b634acfd7586af9b5170f8841b2ae5fe73d30630
- evidence_id: plasma-membrane-agent-query-lacY
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AlacY%20AND%20organism_id%3A83333%20AND%20reviewed%3Atrue&format=json&size=500
  locator: All returned results for exact gene lacY, organism 83333, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T10:00:27.865676Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns P02920. This checks identifier
    resolution only.
  snapshot_sha256: 9e535c157927ff536c6580fedafaaaa2dad374766695630ba8f3b221e4d045a7
  search_scope: UniProtKB query gene_exact:lacY AND organism_id:83333 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: plasma-membrane-agent-P0AGA2
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0AGA2.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T10:00:28.847950Z'
  support: supports
  summary: Native reviewed UniProtKB P0AGA2 identifies Protein translocase subunit
    SecY, gene secY, taxon83333. Concrete identity is checked independently of membership;
    relevant subunit/cofactor/location comments retain their own evidence scope.
  snapshot_sha256: 5fe9bfda47ab90303ecfc2f9b03197d28e32e6b2cf67b467280882c149f64c65
- evidence_id: plasma-membrane-agent-query-secY
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AsecY%20AND%20organism_id%3A83333%20AND%20reviewed%3Atrue&format=json&size=500
  locator: All returned results for exact gene secY, organism 83333, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T10:00:28.900168Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns P0AGA2. This checks identifier
    resolution only.
  snapshot_sha256: ae87004d0b0fed75ec157a730ace426adf991eb37be3d161ecae0225eabf153b
  search_scope: UniProtKB query gene_exact:secY AND organism_id:83333 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: plasma-membrane-agent-P05030
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P05030.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T10:00:28.044491Z'
  support: supports
  summary: Native reviewed UniProtKB P05030 identifies Plasma membrane ATPase 1, gene
    PMA1, taxon559292. Concrete identity is checked independently of membership; relevant
    subunit/cofactor/location comments retain their own evidence scope.
  snapshot_sha256: 8d6bf727c345c1316e73f4f4556bee120df8e71ccea998da4d77228f5a2bcb66
- evidence_id: plasma-membrane-agent-query-PMA1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3APMA1%20AND%20organism_id%3A559292%20AND%20reviewed%3Atrue&format=json&size=500
  locator: All returned results for exact gene PMA1, organism 559292, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T10:00:28.046881Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns P05030. This checks identifier
    resolution only.
  snapshot_sha256: e4cfa702daf0bd8f33057050be18c0f2bae67bdb790a46ddc10bddd5dfd7e846
  search_scope: UniProtKB query gene_exact:PMA1 AND organism_id:559292 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: plasma-membrane-agent-P32465
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P32465.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant; GO0005886 cross-reference
    and associated evidence records
  accessed_at: '2026-10-21T10:00:28.483539Z'
  support: supports
  summary: Native reviewed UniProtKB P32465 identifies Low-affinity glucose transporter
    HXT1, gene HXT1, taxon559292. Concrete identity is checked independently of membership;
    relevant subunit/cofactor/location comments retain their own evidence scope. Its
    GO0005886 cross-reference has SGD IDA annotations with PMID10377429/24124599;
    those papers were not independently read, so this remains database-level localization
    evidence.
  snapshot_sha256: 3696a15cf29561ab7c51d1707c32a6436a0a36e6671950d0bf75ca1eb855a41f
- evidence_id: plasma-membrane-agent-query-HXT1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AHXT1%20AND%20organism_id%3A559292%20AND%20reviewed%3Atrue&format=json&size=500
  locator: All returned results for exact gene HXT1, organism 559292, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T10:00:28.687868Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns P32465. This checks identifier
    resolution only.
  snapshot_sha256: a03e9e0d84871aecf2e2d994d2800e40c1cd63972d7f53906a0ed60ad4b4a995
  search_scope: UniProtKB query gene_exact:HXT1 AND organism_id:559292 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: plasma-membrane-agent-calamia1990-page1
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/35d7/54236/dc659e784616/pnas01038-0052.png
  locator: 'Native PMC54236 PNG scan. Printed p4937: title/authors, Abstract, Introduction,
    complete Materials and methods, and Results fusion-isolation opening. Entire scan
    visually read.'
  accessed_at: '2026-10-21T10:06:32.751148Z'
  support: supports
  summary: This page introduces36 LacY-PhoA fusions and the12-versus14-transmembrane-model
    comparison. It specifies bacterial strains, growth/assay conditions, fusion construction
    and protein immunoprecipitation methods. Its Abstract states the study-level topology
    conclusion.
  snapshot_sha256: 6f70b84078c642c7687b132365bc5d5a492a91e2f1bf212c15811feabfd26ba9
- evidence_id: plasma-membrane-agent-calamia1990-page2
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/35d7/54236/957636ab68ea/pnas01038-0053.png
  locator: 'Native PMC54236 PNG scan. Printed p4938: Results fusion construction and
    alkaline-phosphatase activities; complete Table1 of hybrid-protein properties.
    Entire scan visually read.'
  accessed_at: '2026-10-21T10:06:32.767767Z'
  support: supports
  summary: Fusion-junction activities are compared with competing topology models.
    Table1 records positions, activities and other hybrid-protein properties. The
    text explains why the central-region activities favor the12-helix model over the14-helix
    alternative.
  snapshot_sha256: 9180062e28c5de73cb62c3d4ec7b530ce2543576af26400af7f4ab2890ceb8d4
- evidence_id: plasma-membrane-agent-calamia1990-page3
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/35d7/54236/43af54c2f24c/pnas01038-0054.png
  locator: 'Native PMC54236 PNG scan. Printed p4939: Figures1-3 with complete captions;
    Results minimum-segment tests and protein production/stability opening. Entire
    scan visually read.'
  accessed_at: '2026-10-21T10:06:32.817794Z'
  support: supports
  summary: Figure1 relates fusion activities to the two topology models; Figure2 maps
    junctions in segments3/5; Figure3 identifies hybrid proteins. Results report that
    short nonpolar stretches can promote PhoA translocation and begin the hybrid-protein
    stability analysis.
  snapshot_sha256: 29c2bf94669b041532b0e8498f2d6251a2a3e3ccbcd6febc7def9776fcf8ac37
- evidence_id: plasma-membrane-agent-calamia1990-page4
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/35d7/54236/9d8dc864b102/pnas01038-0055.png
  locator: 'Native PMC54236 PNG scan. Printed p4940: Figure4 pulse-chase stability;
    Results toxicity and lac activity; Discussion opening. Entire scan visually read.'
  accessed_at: '2026-10-21T10:06:32.823892Z'
  support: supports
  summary: The page compares hybrid stability, toxicity and lactose-utilization effects.
    Discussion explains the topology evidence favoring12 helices and addresses fusions
    with intermediate activities. These measurements concern LacY topology and fusion
    behavior, not formation of the complete plasma membrane.
  snapshot_sha256: 40d2e6a8684fe9f540576d3d356ffbb602531f7da4f78e2c0da93f010c7537e5
- evidence_id: plasma-membrane-agent-calamia1990-page5
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/35d7/54236/56d268b65926/pnas01038-0056.png
  locator: 'Native PMC54236 PNG scan. Printed p4941: Discussion continuation, acknowledgments
    and references1-25. Entire scan visually read.'
  accessed_at: '2026-10-21T10:06:32.828632Z'
  support: supports
  summary: Discussion interprets proteolytic stability and incoming-versus-outgoing
    segment fusion behavior. It distinguishes short export-promoting sequence stretches
    from additional residues potentially needed for stable membrane anchoring. The
    remaining page contains acknowledgments and references.
  snapshot_sha256: b5b5f0f93b19939fab7909476ed411f6aab9921670dc1658db42fd07883ccb11
- evidence_id: plasma-membrane-agent-newman1980-pdf
  kind: authority
  reference: https://www.jbc.org/article/S0021-9258(19)70345-7/pdf
  locator: Actual response body and retrieval receipt
  accessed_at: '2026-10-21T10:08:08.674700Z'
  support: context_only
  summary: JBC PDF request returned403 HTML. Native metadata/abstract and exact UniProt
    experimental-reference linkage were checked, but this route did not provide readable
    full text.
  snapshot_sha256: 569649acbb02fcd77ec0e0bf8cb08c157f80c0c36103871323bca2dba0d1cb80
- evidence_id: plasma-membrane-agent-newman1981-pdf
  kind: authority
  reference: https://www.jbc.org/article/S0021-9258(19)68477-2/pdf
  locator: Actual response body and retrieval receipt
  accessed_at: '2026-10-21T10:08:08.674842Z'
  support: context_only
  summary: JBC PDF request returned403 HTML. Native metadata/abstract and exact UniProt
    experimental-reference linkage were checked, but this route did not provide readable
    full text.
  snapshot_sha256: 8f91c524dcfc48f3ff057c628f34af61f0b9ed6aef005f5a5c959a4f99cfd3f4
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/envelope/plasma_membrane.yaml
    --verify
  locator: Captured focused native verify log
  accessed_at: '2026-10-21T10:01:15.820778Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/envelope/plasma_membrane.yaml
    --causal-graphs
  locator: Captured focused native causal-graphs log
  accessed_at: '2026-10-21T10:01:16.438571Z'
  support: supports
  summary: "data/structures/envelope/plasma_membrane.yaml  (GO:0005886)\n  lipid_membrane_boundary\t\
    integral_plasma_membrane_proteins\tCOVERED\t->integral_plasma_membrane_proteins\
    \ (UniProtKB:P02920, UniProtKB:P05030, UniProtKB:P32465, UniProtKB:P0AGA2)\n\n\
    causal_graphs GENE_OR_PROTEIN node summary:\n     1  COVERED                 \
    \  component_ref target holds protein_examples covering all declared symbols\n\
    \     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     1\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 02376b0fd2cb51f5730901b0383efb67c81a8ea43f54386adc259ba1ad729e2d
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/envelope/plasma_membrane.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:59:52Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/envelope/plasma_membrane.yaml'
  snapshot_sha256: 9422192b026ce72b93a954675a092524d1787df55d697c3ee76b4d3d991a64e8
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/envelope/plasma_membrane.yaml --out
    /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/plasma_membrane-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:59:54Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/envelope/plasma_membrane.yaml\
    \ --out /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/plasma_membrane-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch18-20261021-5wxxz5kh/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/plasma_membrane-strict.tsv"
  snapshot_sha256: 8a4573e289dbf928e818225ea6c46481713f92c9994b3cb69e23d9b8be321c89
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/envelope/plasma_membrane.yaml; exact collect() scope; hash
    identifies the entire original resolver TSV
  accessed_at: '2026-10-21T10:11:23Z'
  support: supports
  summary: '19 of23 collected target identifiers returned OK in this fresh base resolver
    run. Residuals: PMID:2164211: UNREACHABLE; resolved by evidence plasma-membrane-agent-pmid-2164211;
    PMID:25002088: UNREACHABLE; resolved by evidence plasma-membrane-agent-pmid-25002088;
    PMID:7000781: UNREACHABLE; resolved by evidence plasma-membrane-agent-pmid-7000781;
    PMID:7028742: UNREACHABLE; resolved by evidence plasma-membrane-agent-pmid-7028742.
    Source-native identity checked separately.'
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
  topic: Cell boundary distinct from outer membrane and compartments
  outcome: concern
  target_ids:
  - GO:0005886
  summary: Exact GO identity, membrane parent and cell-periphery parthood agree. The
    unqualified cytoplasmic membrane synonym is incorrectly typed NARROW although
    native GO treats it as exact and the maintained discussion calls it the same cell-bounding
    structure. The separately qualified bacterial inner membrane synonym remains appropriately
    narrow. Lipid-boundary wording avoids imposing a bilayer on archaeal examples.
  evidence_ids:
  - plasma-membrane-agent-go
  - plasma-membrane-agent-silhavy2010-legacy-html
  - plasma-membrane-agent-albers2011-pdf
  - plasma-membrane-agent-ellen2010-browser
  - record
- assessment_id: materials
  area: grounding
  topic: Mixed lipids and unrelated integral proteins
  outcome: supported
  target_ids:
  - GO:0005886
  summary: The component rows denote a topology-defined lipid cohort and unrelated
    integral proteins, not one identified lipid species or homologous protein family.
    Label-only representation preserves that boundary. Collective lipid material constitutes
    the defined membrane; this identity conclusion does not establish formation necessity
    for each lipid species or integral protein.
  evidence_ids:
  - plasma-membrane-agent-sohlenkamp2016-html
  - plasma-membrane-agent-albers2011-pdf
  - plasma-membrane-agent-ellen2010-browser
  - plasma-membrane-agent-P02920
  - plasma-membrane-agent-P0AGA2
  - plasma-membrane-agent-P05030
  - plasma-membrane-agent-P32465
  - record
  - policy
- assessment_id: formation-necessity
  area: evidence
  topic: Formation necessity remains separate from identity and activity
  outcome: unknown
  target_ids:
  - GO:0005886
  summary: The integral-protein cohort is marked CONDITIONAL, but the inspected localization,
    transport and fusion studies do not independently establish the conditions under
    which the whole plasma membrane fails to form without that cohort. ESSENTIAL for
    collective lipid material expresses the defining lipid-boundary constitution;
    no individual lipid-species necessity is demonstrated. This uncertainty does not
    justify replacing assembly necessity with function or viability, and does not
    establish a contrary biological result.
  evidence_ids:
  - record
  - policy
  - plasma-membrane-agent-silhavy2010-legacy-html
  - plasma-membrane-agent-sohlenkamp2016-html
  - plasma-membrane-agent-calamia1990-page1
  - plasma-membrane-agent-calamia1990-page2
  - plasma-membrane-agent-calamia1990-page3
  - plasma-membrane-agent-calamia1990-page4
  - plasma-membrane-agent-calamia1990-page5
- assessment_id: proteins
  area: evidence
  topic: Verified identities and separated localization evidence
  outcome: supported
  target_ids:
  - GO:0005886
  summary: All four reviewed accessions, genes and paired taxa resolve exactly, with
    native verify and graph coverage passing. LacY experimental PubMed links match
    the entry and Calamia body. SecY is independently placed in the inner membrane
    by Silhavy. Pma1 membrane location and Hxt1 GO plasma-membrane annotations are
    database-level corroboration; the example notes appropriately limit their UniProt
    citations to identity, without turning gene-query uniqueness into membership proof.
  evidence_ids:
  - plasma-membrane-agent-P02920
  - plasma-membrane-agent-P0AGA2
  - plasma-membrane-agent-P05030
  - plasma-membrane-agent-P32465
  - plasma-membrane-agent-calamia1990-page1
  - plasma-membrane-agent-calamia1990-page2
  - plasma-membrane-agent-calamia1990-page3
  - plasma-membrane-agent-calamia1990-page4
  - plasma-membrane-agent-calamia1990-page5
  - plasma-membrane-agent-pmid-2164211
  - plasma-membrane-agent-pmid-7000781
  - plasma-membrane-agent-pmid-7028742
  - plasma-membrane-agent-silhavy2010-legacy-html
  - record
- assessment_id: taxa
  area: scope
  topic: Occurrence and model-organism context
  outcome: supported
  target_ids:
  - GO:0005886
  summary: Taxon receipts identify each named species, strain, kingdom or domain only.
    UNIVERSAL refers to possession of a cell-bounding membrane, not a universal MCC
    architecture, lipid headgroup or respiratory chain. Douglas/Konopka abstract supports
    the fungal membrane-domain context and S.cerevisiae example; exact domain prevalence
    and every fungal lineage were not surveyed.
  evidence_ids:
  - plasma-membrane-agent-tax-2
  - plasma-membrane-agent-tax-2157
  - plasma-membrane-agent-tax-4751
  - plasma-membrane-agent-tax-562
  - plasma-membrane-agent-tax-4932
  - plasma-membrane-agent-tax-83333
  - plasma-membrane-agent-tax-559292
  - plasma-membrane-agent-silhavy2010-legacy-html
  - plasma-membrane-agent-sohlenkamp2016-html
  - plasma-membrane-agent-albers2011-pdf
  - plasma-membrane-agent-pmid-25002088
  - record
- assessment_id: functions
  area: evidence
  topic: Permeability, transport and energy functions
  outcome: supported
  target_ids:
  - GO:0005886
  summary: Bacterial inner-membrane transport and energy roles are directly described
    in the read review, while fungal domain/transport context is supported at review-abstract
    tier. Archaeal ether-lipid boundary and embedded transport are corroborated at
    stated review scopes. Bioenergetics is retained as a class-level activity description,
    not proof that every bacterium or archaeon has all named complexes in this location;
    exact Albers body attribution remains access-limited.
  evidence_ids:
  - plasma-membrane-agent-silhavy2010-legacy-html
  - plasma-membrane-agent-sohlenkamp2016-html
  - plasma-membrane-agent-albers2011-pdf
  - plasma-membrane-agent-ellen2010-browser
  - plasma-membrane-agent-pmid-25002088
  - plasma-membrane-agent-calamia1990-page1
  - plasma-membrane-agent-calamia1990-page2
  - plasma-membrane-agent-calamia1990-page3
  - plasma-membrane-agent-calamia1990-page4
  - plasma-membrane-agent-calamia1990-page5
  - record
- assessment_id: graph
  area: graph
  topic: Explicitly descriptive boundary organization
  outcome: supported
  target_ids:
  - GO:0005886
  summary: The NONMECHANISTIC graph captures lipid-boundary assembly, enclosure and
    protein embedding/transport without specifying a universal biosynthetic pathway
    or lipid topology. A GENE_OR_PROTEIN cohort may inherit the four concrete examples
    without equating each accession to the entire class.
  evidence_ids:
  - plasma-membrane-agent-go
  - plasma-membrane-agent-silhavy2010-legacy-html
  - plasma-membrane-agent-sohlenkamp2016-html
  - plasma-membrane-agent-ellen2010-browser
  - plasma-membrane-agent-P02920
  - plasma-membrane-agent-P0AGA2
  - plasma-membrane-agent-P05030
  - plasma-membrane-agent-P32465
  - record
  - policy
- assessment_id: coverage
  area: completeness
  topic: Bounded review result with source access limits
  outcome: supported
  target_ids:
  - GO:0005886
  summary: One bounded synonym-scope correction was established. No additional issue
    follows from optional chemical or protein inventories. Review abstracts, native
    database evidence and inspected primary scans retain distinct tiers. No existing
    quote or image requires reuse-license assessment; historical actions and PROPOSED
    state remain unchanged.
  evidence_ids:
  - plasma-membrane-agent-go
  - plasma-membrane-agent-silhavy2010-legacy-html
  - plasma-membrane-agent-sohlenkamp2016-html
  - plasma-membrane-agent-albers2011-pdf
  - plasma-membrane-agent-pmid-25002088
  - plasma-membrane-agent-calamia1990-page1
  - plasma-membrane-agent-calamia1990-page2
  - plasma-membrane-agent-calamia1990-page3
  - plasma-membrane-agent-calamia1990-page4
  - plasma-membrane-agent-calamia1990-page5
  - record
  - policy
findings:
- finding_id: F1
  issue_key: plasma-membrane-cytoplasmic-synonym-scope
  category: scope
  severity: minor
  status: open
  certainty: confirmed
  title: Use exact scope for the unqualified cytoplasmic membrane synonym
  description: The bare cytoplasmic membrane synonym is typed NARROW, but native GO0005886
    lists it as EXACT and the maintained resolved discussion describes the same cell-bounding
    structure. Its bacterial review citation does not by itself restrict the unqualified
    name to a biologically narrower class. The distinct bacterial inner membrane row
    is already explicitly qualified and can remain narrow.
  target_ids:
  - GO:0005886
  field_paths:
  - synonyms[synonym_text=cytoplasmic membrane].synonym_type
  - synonyms[synonym_text=cytoplasmic membrane].source
  evidence_ids:
  - plasma-membrane-agent-go
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/envelope/plasma_membrane.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Identity
    and scope
  native_severity: minor
  normalization_reason: The underlying plasma-membrane identity is correct; this is
    a bounded machine-readable synonym-scope correction.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0005886
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/envelope/plasma_membrane.yaml
    role: maintained scientific record
  description: Type unqualified cytoplasmic membrane as EXACT_SYNONYM and cite GO0005886,
    or explicitly qualify the synonym text if a narrower bacterial name is intended.
    Retain bacterial inner membrane as NARROW_SYNONYM.
  acceptance_checks:
  - Confirm the exact native GO synonym and revised text/source agree.
  - Preserve archaeal-compatible lipid-boundary wording and the separate bacterial
    inner membrane row.
  - Run focused schema and strict-reference validation.
limitations:
- Albers and Meyer2011 is limited to verified native metadata, publisher Key Points
  and Abstract; its apparent PDF response is HTML. Douglas and Konopka2014 is limited
  to verified native metadata/abstract after publisher403 responses. These are reviews,
  not primary experiments.
- Sohlenkamp/Geiger Abstract and Introduction and named Silhavy sections were read,
  not every pathway or primary citation. Ellen2010 sections1/2.1 provide supplemental
  review context only and do not replace access to the maintained Albers citation.
- Calamia1990 all five genuine primary page scans were visually read. Newman1980/1981
  full PDFs were unavailable; their exact native abstracts and UniProt reference links
  were verified. Pma1/Hxt1 annotation-source primary papers were not independently
  reviewed.
- No individual lipid or integral protein removal establishes whether the generic
  plasma membrane forms without it. Collective lipid material is defining; CONDITIONAL
  necessity of the broad protein cohort is not independently established and is not
  redefined as functional activity.
- Taxonomy authority is not occurrence evidence. This record-level audit does not
  survey every fungal domain arrangement, archaeal energy-localization exception or
  bacterial respiratory strategy.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
