# Methyl accepting chemotaxis protein complex scientific review

- Review: 20261022T082338Z-methyl-accepting-chemotaxis-protein-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T07:58:05Z
- Finished UTC: 2026-10-22T08:23:38Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The array identity and most signaling evidence are supported. Two majors correct core/ring architecture and unsupported cross-domain defining scope; two minors repair primary attribution and stale current phosphotransfer prose.

## Scope And Provenance

Exactly one complete maintained target plus frozen guidance and protein-example skill. Actual source-reading extents appear per evidence row; no unlisted primary experiments or assets are certified.

Selection: Target 9 of batch59, strict uncovered path order at unchanged f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0098561 | data/structures/other/methyl_accepting_chemotaxis_protein_complex.yaml | maintained | methyl accepting chemotaxis protein complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0098561 | Focused validator passed. |
| Focused native strict | passed | True | GO:0098561 | Focused validator passed. |
| Native causal-graphs | passed | True | GO:0098561 | Native focused check passed; biological claims assessed separately. |
| Native verify | passed | True | GO:0098561 | Native focused check passed; biological claims assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0098561 | No expression-module inference is used. |
| Claim-level scientific review | passed | True | GO:0098561 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0098561 | 20 of 25 collected target identifiers returned OK. METPO:1000702: SKIPPED; Exact METPO1000702 row in the complete published TraitMech index has label motile. This resolves the linked trait identifier; it does not by itself establish a causal mechanism.; PMID:15919996: UNREACHABLE; Native Europe PMC uniquely identifies MED15919996: Global topology analysis of the Escherichia coli inner membrane proteome. (2005); DOI10.1126/science.1109730. Identifier transport verification is distinct from separately scoped primary-source reading.; PMID:22380631: UNREACHABLE; Native Europe PMC uniquely identifies MED22380631: Isolation and identification of new inner membrane-associated proteins that localize to cell poles in Escherichia coli. (2012); DOI10.1111/j.1365-2958.2012.08021.x. Identifier transport verification is distinct from separately scoped primary-source reading.; Pfam:PF00015: SKIPPED; Native PfamPF00015 identifies Methyl-accepting chemotaxis protein (MCP) signalling domain, API type family, integrated into IPR004089. Native identity is distinct from treating a domain profile as an exact whole-protein family.; Pfam:PF01584: SKIPPED; Native PfamPF01584 identifies CheW-like domain, API type domain, integrated into IPR002545. Native identity is distinct from treating a domain profile as an exact whole-protein family. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0098561 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0098561 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0098561 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0098561 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0098561 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Array identity and native molecular examples

identity: supported. Targets: GO:0098561.

The exact GO transmembrane signaling-complex identity, E.coli proteins/aliases, CheY output xref, partial-domain xrefs, motile trait and nanometer unit are supported. The broader chemosensory-array literature also contains cytoplasmic arrays; no silent extension of this transmembrane GO class is inferred.

### Core-to-ring architecture

graph: concern. Targets: GO:0098561.

The ring-to-core edge reverses the source-defined size/assembly relationship: one minimal core contains two trimers, one CheA dimer and two CheW, whereas three cores can build a hexagonal ring unit. The source does not identify a completed ring as that minimal core.

### Measured bacterial architecture versus asserted archaeal invariance

scope: concern. Targets: GO:0098561.

Briegel2009 contains13 bacterial species, not archaeal experiments. Broad archaeal MCP occurrence has review support, but the cited study does not establish the exact cross-domain12nm claim repeated in the definition/property/Archaea row/assembly note. The definition also makes geometry the complete explanation of gain where the reviewed mechanisms remain qualified. COMMON keeps the schema majority/losses-exception meaning; no quantitative bacterial prevalence census was established.

### Signaling source support and current narrative

graph: concern. Targets: GO:0098561.

The six literal review snippets, E.coli gain/control context and Stewart1997 complete abstract support the functional sequence at their stated tiers. Pulsatile output is an inference, not direct measurement, as the evidence note acknowledges. The current description and output-edge note still say CheA-to-CheY is not drawn, despite the present directly cited edge; historical dated history and resolved discussion are not errors.

### Primary2014 source identity

evidence: concern. Targets: GO:0098561.

The exact DOI identifies a2014 primary article led by Briegel,Wong,Hodges, not the2012 Briegel,Li,Bilwes,Hughes,Jensen,Crane author list and not a review. The cited assembly model is present, but the attribution should identify its actual source.

### Constituent roles and unmeasured universal necessity

grounding: unknown. Targets: GO:0098561.

The three protein classes define the canonical functional core and normal array architecture. Non-native receptor zippers are not counterexamples to formation of that same complex. The inspected conditions do not establish universal individual formation necessity across the full bacterial/archaeal scope; this is retained as unknown rather than a forced omission finding.

### Whole maintained target and declared source coverage

completeness: supported. Targets: GO:0098561.

Every maintained field, source note, graph and discussion was inspected at the declared extents. Optional inventory/contact enrichment and acknowledged unknowns alone do not create findings.

## Findings

### F1: Correct the reversed core-unit and ring relationship

major / open / confirmed; issue key: mcp-core-ring-hierarchy.

The ASSEMBLY edge from alternating CheA/CheW ring to core signaling unit assigns the larger ring to the minimal repeated core. Li2011 and Briegel2014 define the core first as two trimers+one CheA dimer+two CheW, then combine cores into rings/arrays. The edge’s own note describes the opposite order.

### F2: Bound the cross-domain architecture claim to its evidence

major / open / confirmed; issue key: mcp-cross-domain-architecture-scope.

The defining12nm claim, physical-property context, Archaea row and assembly evidence attribute bacterial-plus-archaeal conservation to a study of13 bacterial species. The inspected review supports archaeal MCP occurrence but not this asserted measurement. A bacterial source cannot independently establish the maintained universal cross-domain defining property.

### F3: Correct the 2014 primary-paper attribution

minor / open / confirmed; issue key: mcp-2014-primary-attribution.

The ring/core edge uses the correct2014 DOI but names the2012 author roster and calls the article a review. Its actual primary author list begins Briegel,Wong,Hodges; the article contains the proposed assembly model.

### F4: Synchronize the current phosphotransfer narrative

minor / open / confirmed; issue key: mcp-current-phosphotransfer-narrative.

The functional graph currently contains the Stewart1997 CheA-to-CheY edge, while its description and output-edge evidence note say that step is not drawn. The resolved historical discussion already records the addition.

## Recommended Actions And Acceptance Checks

### A1

Represent the minimal core before higher-order rings/arrays, with labels and directed edges matching the cited assembly model; retain the supported trimer geometry and variable array occupancy.

- Do not equate a completed alternating ring with one minimal core; distinguish experimentally measured stoichiometry from proposed sequential assembly.
- Preserve supported source-specific claims and pass applicable native gates.

### A2

Restrict measured12nm conservation and its citation to the sampled bacterial scope, or add an actually inspected archaeal architecture source before retaining the broader claim. Separate qualified mechanistic interpretation of gain from the geometry measurement.

- Do not declare archaeal arrays absent or biologically different merely from this source mismatch; retain exact ontology identity and correct bacterial measurements.
- Preserve supported source-specific claims and pass applicable native gates.

### A3

Correct the author attribution and identify the source as a primary experimental study with a proposed assembly model.

- Retain the exact DOI and distinguish the model from directly observed sequential assembly.
- Preserve supported source-specific claims and pass applicable native gates.

### A4

Update only current graph prose to acknowledge the present directly sourced phosphotransfer edge; preserve the dated historical record and resolved discussion.

- The current graph description must agree with its nodes/edges and retain the distinction between direct phosphotransfer kinetics and inferred pulsatile output.
- Preserve supported source-specific claims and pass applicable native gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/methyl_accepting_chemotaxis_protein_complex.yaml; Entire maintained record, all examples, evidence, graphs, properties, images, history and discussions | context_only | Every maintained field was read. Historical curation statements are context, not independent biological evidence. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; Component/ProteinExample, EssentialityEnum, PresenceEnum and graph-scope contracts | context_only | Formation necessity differs from function, viability and membership. COMMON means most members with losses the exception; VARIABLE means lineage- or strain-level patchiness, not cell-type-specific visibility. |
| curation | docs/CURATION.md; Component grounding and REVIEWED_LABEL_ONLY at159–160 | context_only | Exact full-family mappings differ from shared domains or broader paralog classes. Label-only is not merely uncurated in this pass. |
| complex59-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0001401,GO:0005743,GO:0006935,GO:0015191,GO:0030117,GO:0030118,GO:0030119,GO:0030120,GO:0033232,GO:0061617,GO:0098561,GO:0098796,GO:0098800,GO:0140275,GO:1902495,GO:1990197; Complete target-relevant native definitions/synonyms and typed relationships; unrelated combined entries not attributed to this target | supports | GO0098561 defines a transmembrane MCP/kinase/connector complex regulating flagellar motor activity; it does not itself define a universal12nm geometry. GO0006935 identifies chemotaxis. |
| complex59-agent-go-0098561-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0098561/ancestors?relations=is_a; Complete is_a-only ancestor response | supports | The is_a-only closure supplies classification ancestry for this exact target. It does not establish parthood, experimental assembly necessity or prevalence. |
| complex59-agent-tax-2 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2; Complete ENA identity/names/lineage | supports | Taxon2: Bacteria, rank domain; exact native names and lineage inspected. |
| complex59-agent-tax-2157 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2157; Complete ENA identity/names/lineage | supports | Taxon2157: Archaea, rank domain; exact native names and lineage inspected. |
| complex59-agent-tax-83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Complete ENA identity/names/lineage | supports | Taxon83333: Escherichia coli K-12, rank strain; exact native names and lineage inspected. |
| complex59-agent-protein-P02942 | https://rest.uniprot.org/uniprotkb/P02942.json; Accession/status/name/all gene tokens/organism, relevant function/subunit/localization/similarity comments and family cross-references | supports | UniProtKB reviewed (Swiss-Prot): P02942, Methyl-accepting chemotaxis protein I; primary genes tsr, synonyms cheD, taxon83333. Its own native comments and family cross-references were inspected with their original evidence qualifiers. |
| complex59-agent-protein-P05704 | https://rest.uniprot.org/uniprotkb/P05704.json; Accession/status/name/all gene tokens/organism, relevant function/subunit/localization/similarity comments and family cross-references | supports | UniProtKB reviewed (Swiss-Prot): P05704, Methyl-accepting chemotaxis protein III; primary genes trg, synonyms none, taxon83333. Its own native comments and family cross-references were inspected with their original evidence qualifiers. |
| complex59-agent-protein-P07017 | https://rest.uniprot.org/uniprotkb/P07017.json; Accession/status/name/all gene tokens/organism, relevant function/subunit/localization/similarity comments and family cross-references | supports | UniProtKB reviewed (Swiss-Prot): P07017, Methyl-accepting chemotaxis protein II; primary genes tar, synonyms cheM, taxon83333. Its own native comments and family cross-references were inspected with their original evidence qualifiers. |
| complex59-agent-protein-P07018 | https://rest.uniprot.org/uniprotkb/P07018.json; Accession/status/name/all gene tokens/organism, relevant function/subunit/localization/similarity comments and family cross-references | supports | UniProtKB reviewed (Swiss-Prot): P07018, Methyl-accepting chemotaxis protein IV; primary genes tap, synonyms none, taxon83333. Its own native comments and family cross-references were inspected with their original evidence qualifiers. |
| complex59-agent-protein-P07363 | https://rest.uniprot.org/uniprotkb/P07363.json; Accession/status/name/all gene tokens/organism, relevant function/subunit/localization/similarity comments and family cross-references | supports | UniProtKB reviewed (Swiss-Prot): P07363, Chemotaxis protein CheA; primary genes cheA, synonyms none, taxon83333. Its own native comments and family cross-references were inspected with their original evidence qualifiers. |
| complex59-agent-protein-P0A964 | https://rest.uniprot.org/uniprotkb/P0A964.json; Accession/status/name/all gene tokens/organism, relevant function/subunit/localization/similarity comments and family cross-references | supports | UniProtKB reviewed (Swiss-Prot): P0A964, Chemotaxis protein CheW; primary genes cheW, synonyms none, taxon83333. Its own native comments and family cross-references were inspected with their original evidence qualifiers. |
| complex59-agent-protein-P0AE67 | https://rest.uniprot.org/uniprotkb/P0AE67.json; Accession/status/name/all gene tokens/organism, relevant function/subunit/localization/similarity comments and family cross-references | supports | UniProtKB reviewed (Swiss-Prot): P0AE67, Chemotaxis protein CheY; primary genes cheY, synonyms none, taxon83333. Its own native comments and family cross-references were inspected with their original evidence qualifiers. |
| complex59-agent-query-cheA | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AcheA%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete query results | supports | Exact native query returns 1 entry: P07363. Every returned identity/gene/organism was read. |
| complex59-agent-query-cheW | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AcheW%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete query results | supports | Exact native query returns 1 entry: P0A964. Every returned identity/gene/organism was read. |
| complex59-agent-query-tap | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Atap%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete query results | supports | Exact native query returns 1 entry: P07018. Every returned identity/gene/organism was read. |
| complex59-agent-query-tar | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Atar%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete query results | supports | Exact native query returns 1 entry: P07017. Every returned identity/gene/organism was read. |
| complex59-agent-query-trg | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Atrg%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete query results | supports | Exact native query returns 1 entry: P05704. Every returned identity/gene/organism was read. |
| complex59-agent-query-tsr | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Atsr%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete query results | supports | Exact native query returns 1 entry: P02942. Every returned identity/gene/organism was read. |
| complex59-agent-pmid-15919996 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15919996+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native identity and available abstract | supports | MED15919996: Global topology analysis of the Escherichia coli inner membrane proteome. Daley DO, Rapp M, Granseth E, Melén K, Drew D, von Heijne G. (2005), DOI10.1126/science.1109730. Exact metadata and complete available abstract read; this does not claim body access.  |
| complex59-agent-pmid-22380631 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22380631+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native identity and available abstract | supports | MED22380631: Isolation and identification of new inner membrane-associated proteins that localize to cell poles in Escherichia coli. Li G, Young KD. (2012), DOI10.1111/j.1365-2958.2012.08021.x. Exact metadata and complete available abstract read; this does not claim body access.  |
| complex59-agent-doi-10.1016_j.tim.2015.03.003 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.tim.2015.03.003%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native identity and abstract | supports | Exact native DOI/MED identity: Signaling and sensory adaptation in Escherichia coli chemoreceptors: 2015 update. Parkinson JS, Hazelbauer GL, Falke JJ. (2015), PMID25834953. Complete available abstract read. |
| complex59-agent-doi-10.1021_bi5000614 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1021%2Fbi5000614%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native identity and abstract | supports | Exact native DOI/MED identity: New insights into bacterial chemoreceptor array structure and assembly from electron cryotomography. Briegel A, Wong ML, Hodges HL, Oikonomou CM, Piasta KN, Harris MJ, Fowler DJ, Thompson LK, Falke JJ, Kiessling LL, Jensen GJ. (2014), PMID24580139. Complete available abstract read. |
| complex59-agent-doi-10.1021_bi962261k | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1021%2Fbi962261k%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native identity and abstract | supports | Exact native DOI/MED identity: Kinetic characterization of phosphotransfer between CheA and CheY in the bacterial chemotaxis signal transduction pathway. Stewart RC. (1997), PMID9047301. Complete available abstract read. |
| complex59-agent-doi-10.1073_pnas.0905181106 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1073%2Fpnas.0905181106%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native identity and abstract | supports | Exact native DOI/MED identity: Universal architecture of bacterial chemoreceptor arrays. Briegel A, Ortega DR, Tocheva EI, Wuichet K, Li Z, Chen S, Müller A, Iancu CV, Murphy GE, Dobro MJ, Zhulin IB, Jensen GJ. (2009), PMID19805102. Complete available abstract read. |
| complex59-agent-doi-10.1073_pnas.1104824108 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1073%2Fpnas.1104824108%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native identity and abstract | supports | Exact native DOI/MED identity: Core unit of chemotaxis signaling complexes. Li M, Hazelbauer GL. (2011), PMID21606342. Complete available abstract read. |
| complex59-agent-doi-10.1073_pnas.1115719109 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1073%2Fpnas.1115719109%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native identity and abstract | supports | Exact native DOI/MED identity: Bacterial chemoreceptor arrays are hexagonally packed trimers of receptor dimers networked by rings of kinase and coupling proteins. Briegel A, Li X, Bilwes AM, Hughes KT, Jensen GJ, Crane BR. (2012), PMID22355139. Complete available abstract read. |
| complex59-agent-doi-10.1146_annurev-biophys-070816-033555 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1146%2Fannurev-biophys-070816-033555%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native identity and abstract | supports | Exact native DOI/MED identity: Progress and Potential of Electron Cryotomography as Illustrated by Its Application to Bacterial Chemoreceptor Arrays. Briegel A, Jensen G. (2017), PMID28301773. Complete available abstract read. |
| complex59-agent-briegel2009-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2761316/; Complete Results/Discussion sec1–4 including Table1/Fig1–4 captions, Conclusion sec5 and Methods sec6–9; no Introduction, pixels or supplements. | supports | Briegel2009 examines13 bacterial species and finds12nm hexagonal order in accessible top views. It does not include archaeal specimens. Architectural conservation suggests related bacterial mechanisms, rather than directly proving the entire causal basis of gain. |
| complex59-agent-li2011-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3111312/; Results sec6 including Fig8 caption; complete Discussion SEC3 and Methods sec12. No other sections or pixels. | supports | Purified nanodisc core units comprise two receptor trimers, one CheA dimer and two CheW; hexagons are proposed to combine three such cores. Quantitative corrections account for extra nonparticipating Tar dimers. |
| complex59-agent-briegel2012-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3309718/; Complete Results/Discussion SEC1 including Table1/Fig1–4 captions; Methods sec3 growth/preparation and sec8 modeling. No pixels/supplements. | supports | Native-array cryotomography and Thermotoga ternary crystallography support alternating CheA-P5/CheW rings linked by CheA dimers. Minimal core units span two trimers; ring occupancy and CheW substitution vary. |
| complex59-agent-briegel2014-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3985956/fullTextXML; Complete unsectioned Introduction, Results sec3.1–3.6 and Discussion sec4 with Fig1–7 captions. Methods and pixels/supplements not read. | supports | Briegel,Wong,Hodges and colleagues2014 present primary array experiments. Their proposed assembly sequence forms minimal cores first, then rings/superlattices. Native, overexpression, membrane reconstitution and soluble-fragment arrays have distinct outcomes. |
| complex59-agent-parkinson2015-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4417406/; Complete abstract and sections S1/S4/S5/S6/S7 including Box1–3 and embedded captions; six snippet comparisons after whitespace normalization. Original cited experiments were not independently read unless separately listed. | supports | Parkinson2015 is a secondary review. It distinguishes minimal core units from higher-order rings/arrays and describes cooperative gain and inferred pulsatile output. All six maintained snippets match the normalized full text exactly, including the source’s mechanistic qualifiers. |
| complex59-agent-pfam-PF00015 | https://www.ebi.ac.uk/interpro/api/entry/pfam/PF00015/; Native name/type, description and curation flags/signatures; example membership is independently supplied by UniProt | supports | PF00015 is the MCP signaling-region profile; its API type is family but its named biological scope is a signaling domain. |
| complex59-agent-pfam-PF01584 | https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01584/; Native name/type, description and curation flags/signatures; example membership is independently supplied by UniProt | supports | PF01584 is the CheW-like domain, shared with related chemotaxis proteins. Partial-domain xrefs are not exact whole-component grounding. |
| complex59-agent-interpro-IPR004090 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004090/; Native name/type, description and curation flags/signatures; example membership is independently supplied by UniProt | supports | IPR004090 describes the MCP protein family with broader related prokaryotic signaling context. |
| complex59-agent-interpro-IPR051315 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051315/; Native name/type, description and curation flags/signatures; example membership is independently supplied by UniProt | supports | IPR051315 is the bacterial CheA family; unchecked machine-generated prose is not independent primary evidence. |
| complex59-agent-interpro-IPR039315 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR039315/; Native name/type, description and curation flags/signatures; example membership is independently supplied by UniProt | supports | IPR039315 identifies the CheW protein family, distinct from the broader CheW-like domain. |
| complex59-agent-traitmech-index | https://culturebotai.github.io/TraitMech/pages/data/trait_graph.json; Exact METPO1000702 row in complete published trait index | supports | The published TraitMech index contains METPO1000702 with exact label motile. |
| complex59-agent-uo-0000018 | https://www.ebi.ac.uk/ols4/api/ontologies/uo/terms?obo_id=UO:0000018; Exact OLS term identity and definition | supports | UO0000018 is nanometer,10^-9 meter. |
| schema-result | just validate data/structures/other/methyl_accepting_chemotaxis_protein_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/methyl_accepting_chemotaxis_protein_complex.yaml |
| strict-result | just validate-strict data/structures/other/methyl_accepting_chemotaxis_protein_complex.yaml --out /private/tmp/cellstructure-batch59-20261022-t3ere5ku/methyl_accepting_chemotaxis_protein_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/methyl_accepting_chemotaxis_protein_complex.yaml --out /private/tmp/cellstructure-batch59-20261022-t3ere5ku/methyl_accepting_chemotaxis_protein_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch59-20261022-t3ere5ku/methyl_accepting_chemotaxis_protein_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/methyl_accepting_chemotaxis_protein_complex.yaml --causal-graphs; Complete native focused report | supports | data/structures/other/methyl_accepting_chemotaxis_protein_complex.yaml  (GO:0098561)<br>  chea_chew_hexagonal_array_assembly	mcp	COVERED	-&gt;mcp (UniProtKB:P07017, UniProtKB:P02942, UniProtKB:P05704, UniProtKB:P07018)<br>  chea_chew_hexagonal_array_assembly	chea	COVERED	-&gt;chea (UniProtKB:P07363)<br>  chea_chew_hexagonal_array_assembly	chew	COVERED	-&gt;chew (UniProtKB:P0A964)<br>  chemoreceptor_array_signalling	mcp	COVERED	-&gt;mcp (UniProtKB:P07017, UniProtKB:P02942, UniProtKB:P05704, UniProtKB:P07018)<br>  chemoreceptor_array_signalling	chew	COVERED	-&gt;chew (UniProtKB:P0A964)<br>  chemoreceptor_array_signalling	chea	COVERED	-&gt;chea (UniProtKB:P07363)<br>  chemoreceptor_array_signalling	phospho_chey	UNANCHORED_WITH_UNIPROT	phospho-CheY (UniProtKB:P0AE67)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     6  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     1  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     7  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/methyl_accepting_chemotaxis_protein_complex.yaml --verify; Complete native focused report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/methyl_accepting_chemotaxis_protein_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 20 of 25 collected target identifiers returned OK. METPO:1000702: SKIPPED; Exact METPO1000702 row in the complete published TraitMech index has label motile. This resolves the linked trait identifier; it does not by itself establish a causal mechanism.; PMID:15919996: UNREACHABLE; Native Europe PMC uniquely identifies MED15919996: Global topology analysis of the Escherichia coli inner membrane proteome. (2005); DOI10.1126/science.1109730. Identifier transport verification is distinct from separately scoped primary-source reading.; PMID:22380631: UNREACHABLE; Native Europe PMC uniquely identifies MED22380631: Isolation and identification of new inner membrane-associated proteins that localize to cell poles in Escherichia coli. (2012); DOI10.1111/j.1365-2958.2012.08021.x. Identifier transport verification is distinct from separately scoped primary-source reading.; Pfam:PF00015: SKIPPED; Native PfamPF00015 identifies Methyl-accepting chemotaxis protein (MCP) signalling domain, API type family, integrated into IPR004089. Native identity is distinct from treating a domain profile as an exact whole-protein family.; Pfam:PF01584: SKIPPED; Native PfamPF01584 identifies CheW-like domain, API type domain, integrated into IPR002545. Native identity is distinct from treating a domain profile as an exact whole-protein family. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five completed same-base batch26 global gates are integrated with exact manifest/input/log hashes verified; no fresh full-site QC is claimed from this sparse checkout.
- Only the explicitly listed source sections/assets were inspected. No unlisted supplements, atomic coordinates or raw experimental data were analyzed.
- Briegel/Jensen2017 and Stewart1997 were inspected at complete native metadata/abstract scope only; the2017publisher PDF returned403. Briegel2009/2012/2014, Li2011 and Parkinson2015 were read only at the explicit extents above. No figure pixels or supplements were inspected.
- The six quotations were verified exactly after whitespace normalization; this verifies wording, not independent replication of the review’s cited primary experiments. No archaeal architecture primary was inspected.
- Whole-protein family candidates are retained as bounded context rather than forced mappings for unqualified cross-domain cohorts; the existing Pfam xrefs describe partial regions.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The explicit all-record goal authorizes both clean and issue-bearing reviews.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T082338Z-methyl-accepting-chemotaxis-protein-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Methyl accepting chemotaxis protein complex scientific review
started_at: '2026-10-22T07:58:05Z'
finished_at: '2026-10-22T08:23:38Z'
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
summary: The array identity and most signaling evidence are supported. Two majors
  correct core/ring architecture and unsupported cross-domain defining scope; two
  minors repair primary attribution and stale current phosphotransfer prose.
source:
  git_revision: f97b1abe2d78971b6f66b9083087d7a94cf3c0cc
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
  - path: data/structures/other/methyl_accepting_chemotaxis_protein_complex.yaml
    sha256: 9f67d7f92daa2bb5c36c906457c0f507cd529c925a934af10661cfd33cb8c819
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
- target_id: GO:0098561
  path: data/structures/other/methyl_accepting_chemotaxis_protein_complex.yaml
  label: methyl accepting chemotaxis protein complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/methyl_accepting_chemotaxis_protein_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete maintained target plus frozen guidance and protein-example
    skill. Actual source-reading extents appear per evidence row; no unlisted primary
    experiments or assets are certified.
  selection: Target 9 of batch59, strict uncovered path order at unchanged f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0098561
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0098561
  command: just validate data/structures/other/methyl_accepting_chemotaxis_protein_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0098561
  command: just validate-strict data/structures/other/methyl_accepting_chemotaxis_protein_complex.yaml
    --out /private/tmp/cellstructure-batch59-20261022-t3ere5ku/methyl_accepting_chemotaxis_protein_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0098561
  command: /private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/methyl_accepting_chemotaxis_protein_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Native focused check passed; biological claims assessed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Native verify
  status: passed
  required: true
  target_ids:
  - GO:0098561
  command: /private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/methyl_accepting_chemotaxis_protein_complex.yaml
    --verify
  exit_code: 0
  summary: Native focused check passed; biological claims assessed separately.
  evidence_ids:
  - native-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0098561
  summary: No expression-module inference is used.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0098561
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - complex59-agent-go
  - complex59-agent-go-0098561-ancestors
  - complex59-agent-tax-2
  - complex59-agent-tax-2157
  - complex59-agent-tax-83333
  - complex59-agent-protein-P02942
  - complex59-agent-protein-P05704
  - complex59-agent-protein-P07017
  - complex59-agent-protein-P07018
  - complex59-agent-protein-P07363
  - complex59-agent-protein-P0A964
  - complex59-agent-protein-P0AE67
  - complex59-agent-query-cheA
  - complex59-agent-query-cheW
  - complex59-agent-query-tap
  - complex59-agent-query-tar
  - complex59-agent-query-trg
  - complex59-agent-query-tsr
  - complex59-agent-pmid-15919996
  - complex59-agent-pmid-22380631
  - complex59-agent-doi-10.1016_j.tim.2015.03.003
  - complex59-agent-doi-10.1021_bi5000614
  - complex59-agent-doi-10.1021_bi962261k
  - complex59-agent-doi-10.1073_pnas.0905181106
  - complex59-agent-doi-10.1073_pnas.1104824108
  - complex59-agent-doi-10.1073_pnas.1115719109
  - complex59-agent-doi-10.1146_annurev-biophys-070816-033555
  - complex59-agent-briegel2009-legacy
  - complex59-agent-li2011-legacy
  - complex59-agent-briegel2012-legacy
  - complex59-agent-briegel2014-xml
  - complex59-agent-parkinson2015-legacy
  - complex59-agent-pfam-PF00015
  - complex59-agent-pfam-PF01584
  - complex59-agent-interpro-IPR004090
  - complex59-agent-interpro-IPR051315
  - complex59-agent-interpro-IPR039315
  - complex59-agent-traitmech-index
  - complex59-agent-uo-0000018
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0098561
  summary: '20 of 25 collected target identifiers returned OK. METPO:1000702: SKIPPED;
    Exact METPO1000702 row in the complete published TraitMech index has label motile.
    This resolves the linked trait identifier; it does not by itself establish a causal
    mechanism.; PMID:15919996: UNREACHABLE; Native Europe PMC uniquely identifies
    MED15919996: Global topology analysis of the Escherichia coli inner membrane proteome.
    (2005); DOI10.1126/science.1109730. Identifier transport verification is distinct
    from separately scoped primary-source reading.; PMID:22380631: UNREACHABLE; Native
    Europe PMC uniquely identifies MED22380631: Isolation and identification of new
    inner membrane-associated proteins that localize to cell poles in Escherichia
    coli. (2012); DOI10.1111/j.1365-2958.2012.08021.x. Identifier transport verification
    is distinct from separately scoped primary-source reading.; Pfam:PF00015: SKIPPED;
    Native PfamPF00015 identifies Methyl-accepting chemotaxis protein (MCP) signalling
    domain, API type family, integrated into IPR004089. Native identity is distinct
    from treating a domain profile as an exact whole-protein family.; Pfam:PF01584:
    SKIPPED; Native PfamPF01584 identifies CheW-like domain, API type domain, integrated
    into IPR002545. Native identity is distinct from treating a domain profile as
    an exact whole-protein family. Native source checks are separately scoped; skipped
    or unreachable identifiers are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - complex59-agent-traitmech-index
  - complex59-agent-pmid-15919996
  - complex59-agent-pmid-22380631
  - complex59-agent-pfam-PF00015
  - complex59-agent-pfam-PF01584
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0098561
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch59 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0098561
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch59 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0098561
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch59 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0098561
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch59 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0098561
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
    and current batch59 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/methyl_accepting_chemotaxis_protein_complex.yaml
  locator: Entire maintained record, all examples, evidence, graphs, properties, images,
    history and discussions
  accessed_at: '2026-10-22T08:10:34Z'
  support: context_only
  summary: Every maintained field was read. Historical curation statements are context,
    not independent biological evidence.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Component/ProteinExample, EssentialityEnum, PresenceEnum and graph-scope
    contracts
  accessed_at: '2026-10-22T08:10:34Z'
  support: context_only
  summary: Formation necessity differs from function, viability and membership. COMMON
    means most members with losses the exception; VARIABLE means lineage- or strain-level
    patchiness, not cell-type-specific visibility.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Component grounding and REVIEWED_LABEL_ONLY at159–160
  accessed_at: '2026-10-22T08:10:34Z'
  support: context_only
  summary: Exact full-family mappings differ from shared domains or broader paralog
    classes. Label-only is not merely uncurated in this pass.
- evidence_id: complex59-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0001401,GO:0005743,GO:0006935,GO:0015191,GO:0030117,GO:0030118,GO:0030119,GO:0030120,GO:0033232,GO:0061617,GO:0098561,GO:0098796,GO:0098800,GO:0140275,GO:1902495,GO:1990197
  locator: Complete target-relevant native definitions/synonyms and typed relationships;
    unrelated combined entries not attributed to this target
  accessed_at: '2026-10-22T07:52:24.329077Z'
  support: supports
  summary: GO0098561 defines a transmembrane MCP/kinase/connector complex regulating
    flagellar motor activity; it does not itself define a universal12nm geometry.
    GO0006935 identifies chemotaxis.
  snapshot_sha256: dbd460ba253a79f76308983bfbf11d984337e32c973e044f3f1b30f1394901af
- evidence_id: complex59-agent-go-0098561-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0098561/ancestors?relations=is_a
  locator: Complete is_a-only ancestor response
  accessed_at: '2026-10-22T07:52:40.619546Z'
  support: supports
  summary: The is_a-only closure supplies classification ancestry for this exact target.
    It does not establish parthood, experimental assembly necessity or prevalence.
  snapshot_sha256: b849157559d939ea1d1fca84307d1cefbe63ad2bf58db1bd43c55dc53a401ceb
- evidence_id: complex59-agent-tax-2
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2
  locator: Complete ENA identity/names/lineage
  accessed_at: '2026-10-22T07:52:30.361183Z'
  support: supports
  summary: 'Taxon2: Bacteria, rank domain; exact native names and lineage inspected.'
  snapshot_sha256: 314bd7723b8dea04f1840809fb74e06c514664fba9c6a0619e8f12e2a6dceef1
- evidence_id: complex59-agent-tax-2157
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2157
  locator: Complete ENA identity/names/lineage
  accessed_at: '2026-10-22T07:52:30.470114Z'
  support: supports
  summary: 'Taxon2157: Archaea, rank domain; exact native names and lineage inspected.'
  snapshot_sha256: 9ddd1001f0c607eb9b7582ecd9e83d3d18a89ddf8e540ec75da7dc4c9939c6ae
- evidence_id: complex59-agent-tax-83333
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Complete ENA identity/names/lineage
  accessed_at: '2026-10-22T07:52:31.662631Z'
  support: supports
  summary: 'Taxon83333: Escherichia coli K-12, rank strain; exact native names and
    lineage inspected.'
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: complex59-agent-protein-P02942
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P02942.json
  locator: Accession/status/name/all gene tokens/organism, relevant function/subunit/localization/similarity
    comments and family cross-references
  accessed_at: '2026-10-22T07:52:24.328842Z'
  support: supports
  summary: 'UniProtKB reviewed (Swiss-Prot): P02942, Methyl-accepting chemotaxis protein
    I; primary genes tsr, synonyms cheD, taxon83333. Its own native comments and family
    cross-references were inspected with their original evidence qualifiers.'
  snapshot_sha256: 6bb916220eca63fc72fabed9ad27d98e3afd1c5a623dcd4f75c5447325983b62
- evidence_id: complex59-agent-protein-P05704
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P05704.json
  locator: Accession/status/name/all gene tokens/organism, relevant function/subunit/localization/similarity
    comments and family cross-references
  accessed_at: '2026-10-22T07:52:24.330244Z'
  support: supports
  summary: 'UniProtKB reviewed (Swiss-Prot): P05704, Methyl-accepting chemotaxis protein
    III; primary genes trg, synonyms none, taxon83333. Its own native comments and
    family cross-references were inspected with their original evidence qualifiers.'
  snapshot_sha256: b2312a33bb224aa15f07608736af4673ad4ad40de29a1fbd71ff5d3f25666375
- evidence_id: complex59-agent-protein-P07017
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P07017.json
  locator: Accession/status/name/all gene tokens/organism, relevant function/subunit/localization/similarity
    comments and family cross-references
  accessed_at: '2026-10-22T07:52:25.049219Z'
  support: supports
  summary: 'UniProtKB reviewed (Swiss-Prot): P07017, Methyl-accepting chemotaxis protein
    II; primary genes tar, synonyms cheM, taxon83333. Its own native comments and
    family cross-references were inspected with their original evidence qualifiers.'
  snapshot_sha256: 6a7230205b55972ea1d693a8ed41e985afbe497f8754ec1502abd63bdbe8073f
- evidence_id: complex59-agent-protein-P07018
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P07018.json
  locator: Accession/status/name/all gene tokens/organism, relevant function/subunit/localization/similarity
    comments and family cross-references
  accessed_at: '2026-10-22T07:52:25.090400Z'
  support: supports
  summary: 'UniProtKB reviewed (Swiss-Prot): P07018, Methyl-accepting chemotaxis protein
    IV; primary genes tap, synonyms none, taxon83333. Its own native comments and
    family cross-references were inspected with their original evidence qualifiers.'
  snapshot_sha256: eadad20ead8121f293674201bccb1000b41f2fc4aa0a28d032a611dc4944b07b
- evidence_id: complex59-agent-protein-P07363
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P07363.json
  locator: Accession/status/name/all gene tokens/organism, relevant function/subunit/localization/similarity
    comments and family cross-references
  accessed_at: '2026-10-22T07:52:25.165089Z'
  support: supports
  summary: 'UniProtKB reviewed (Swiss-Prot): P07363, Chemotaxis protein CheA; primary
    genes cheA, synonyms none, taxon83333. Its own native comments and family cross-references
    were inspected with their original evidence qualifiers.'
  snapshot_sha256: 48174af095d79ede49f4acbed42295ca16133fe8e75f3f6ea2930774200bbeac
- evidence_id: complex59-agent-protein-P0A964
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0A964.json
  locator: Accession/status/name/all gene tokens/organism, relevant function/subunit/localization/similarity
    comments and family cross-references
  accessed_at: '2026-10-22T07:52:25.719482Z'
  support: supports
  summary: 'UniProtKB reviewed (Swiss-Prot): P0A964, Chemotaxis protein CheW; primary
    genes cheW, synonyms none, taxon83333. Its own native comments and family cross-references
    were inspected with their original evidence qualifiers.'
  snapshot_sha256: accde71f7c3dff08c8ba4b7fa37992491e9253dafd9738c6600fa41b737da333
- evidence_id: complex59-agent-protein-P0AE67
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0AE67.json
  locator: Accession/status/name/all gene tokens/organism, relevant function/subunit/localization/similarity
    comments and family cross-references
  accessed_at: '2026-10-22T07:52:25.792031Z'
  support: supports
  summary: 'UniProtKB reviewed (Swiss-Prot): P0AE67, Chemotaxis protein CheY; primary
    genes cheY, synonyms none, taxon83333. Its own native comments and family cross-references
    were inspected with their original evidence qualifiers.'
  snapshot_sha256: 5fbb1eac2f6d91b1af3219813bb8b2221ea258f9843085c2bd51a3df7fde6c42
- evidence_id: complex59-agent-query-cheA
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AcheA%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete query results
  accessed_at: '2026-10-22T07:57:27.749530Z'
  support: supports
  summary: 'Exact native query returns 1 entry: P07363. Every returned identity/gene/organism
    was read.'
  snapshot_sha256: 08361384d93bf123c1adc0e6285ee763dc6b092ed98fc409dfef125a7efc15be
  search_scope: Exact retained UniProt request https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AcheA%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    all returned identities inspected.
- evidence_id: complex59-agent-query-cheW
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AcheW%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete query results
  accessed_at: '2026-10-22T07:57:27.912298Z'
  support: supports
  summary: 'Exact native query returns 1 entry: P0A964. Every returned identity/gene/organism
    was read.'
  snapshot_sha256: dcf7e640bac188b844806dda81bece7e28197923ddc4a0345eb21a81657fe341
  search_scope: Exact retained UniProt request https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AcheW%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    all returned identities inspected.
- evidence_id: complex59-agent-query-tap
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Atap%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete query results
  accessed_at: '2026-10-22T07:57:27.427344Z'
  support: supports
  summary: 'Exact native query returns 1 entry: P07018. Every returned identity/gene/organism
    was read.'
  snapshot_sha256: 453bebe567440f3d398fd08ed294f37f4d0af619da1c0773c2e00aff8f7c2935
  search_scope: Exact retained UniProt request https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Atap%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    all returned identities inspected.
- evidence_id: complex59-agent-query-tar
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Atar%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete query results
  accessed_at: '2026-10-22T07:57:26.580156Z'
  support: supports
  summary: 'Exact native query returns 1 entry: P07017. Every returned identity/gene/organism
    was read.'
  snapshot_sha256: 8235e3d78438859bb4efdaa1eae081ba5e0dd2423596387fcdf4ee29acbb7bbb
  search_scope: Exact retained UniProt request https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Atar%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    all returned identities inspected.
- evidence_id: complex59-agent-query-trg
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Atrg%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete query results
  accessed_at: '2026-10-22T07:57:27.111274Z'
  support: supports
  summary: 'Exact native query returns 1 entry: P05704. Every returned identity/gene/organism
    was read.'
  snapshot_sha256: f290ff7cfc305eb69500d7bec028ad2dd9fb477e1c757d6fa3d8c65278599616
  search_scope: Exact retained UniProt request https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Atrg%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    all returned identities inspected.
- evidence_id: complex59-agent-query-tsr
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Atsr%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete query results
  accessed_at: '2026-10-22T07:57:26.894288Z'
  support: supports
  summary: 'Exact native query returns 1 entry: P02942. Every returned identity/gene/organism
    was read.'
  snapshot_sha256: d52be1a47cd764c63d7254b8c86b99925ac39a648c72b731d9e90f2e963b754a
  search_scope: Exact retained UniProt request https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Atsr%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    all returned identities inspected.
- evidence_id: complex59-agent-pmid-15919996
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15919996+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native identity and available abstract
  accessed_at: '2026-10-22T07:52:34.177675Z'
  support: supports
  summary: 'MED15919996: Global topology analysis of the Escherichia coli inner membrane
    proteome. Daley DO, Rapp M, Granseth E, Melén K, Drew D, von Heijne G. (2005),
    DOI10.1126/science.1109730. Exact metadata and complete available abstract read;
    this does not claim body access. '
  snapshot_sha256: 7c83fcb28f68a14cbc566904fbd32091121999b45f87b73b013e0396826b0102
- evidence_id: complex59-agent-pmid-22380631
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22380631+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native identity and available abstract
  accessed_at: '2026-10-22T07:52:34.794620Z'
  support: supports
  summary: 'MED22380631: Isolation and identification of new inner membrane-associated
    proteins that localize to cell poles in Escherichia coli. Li G, Young KD. (2012),
    DOI10.1111/j.1365-2958.2012.08021.x. Exact metadata and complete available abstract
    read; this does not claim body access. '
  snapshot_sha256: af75f2a1ed289f1dcaf4322ea47b8d025f98cbbbf3681fca5c700bcf08097aa3
- evidence_id: complex59-agent-doi-10.1016_j.tim.2015.03.003
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.tim.2015.03.003%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native identity and abstract
  accessed_at: '2026-10-22T07:52:37.319637Z'
  support: supports
  summary: 'Exact native DOI/MED identity: Signaling and sensory adaptation in Escherichia
    coli chemoreceptors: 2015 update. Parkinson JS, Hazelbauer GL, Falke JJ. (2015),
    PMID25834953. Complete available abstract read.'
  snapshot_sha256: 97dd46efbdc021bdb3b686dac15e0fb6ab250d53010f27d4acc43dc0134c3ff4
- evidence_id: complex59-agent-doi-10.1021_bi5000614
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1021%2Fbi5000614%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native identity and abstract
  accessed_at: '2026-10-22T07:52:37.397914Z'
  support: supports
  summary: 'Exact native DOI/MED identity: New insights into bacterial chemoreceptor
    array structure and assembly from electron cryotomography. Briegel A, Wong ML,
    Hodges HL, Oikonomou CM, Piasta KN, Harris MJ, Fowler DJ, Thompson LK, Falke JJ,
    Kiessling LL, Jensen GJ. (2014), PMID24580139. Complete available abstract read.'
  snapshot_sha256: 9642ea49e1ae9974c8a4dcd3a4c2bc525906857ebf5ccc28052a860e2cccc044
- evidence_id: complex59-agent-doi-10.1021_bi962261k
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1021%2Fbi962261k%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native identity and abstract
  accessed_at: '2026-10-22T07:52:37.991837Z'
  support: supports
  summary: 'Exact native DOI/MED identity: Kinetic characterization of phosphotransfer
    between CheA and CheY in the bacterial chemotaxis signal transduction pathway.
    Stewart RC. (1997), PMID9047301. Complete available abstract read.'
  snapshot_sha256: 455b9ba4508beee286dd95451fe94e5d47ba382ce7b709c2c1042cd629beb2d7
- evidence_id: complex59-agent-doi-10.1073_pnas.0905181106
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1073%2Fpnas.0905181106%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native identity and abstract
  accessed_at: '2026-10-22T07:52:38.033616Z'
  support: supports
  summary: 'Exact native DOI/MED identity: Universal architecture of bacterial chemoreceptor
    arrays. Briegel A, Ortega DR, Tocheva EI, Wuichet K, Li Z, Chen S, Müller A, Iancu
    CV, Murphy GE, Dobro MJ, Zhulin IB, Jensen GJ. (2009), PMID19805102. Complete
    available abstract read.'
  snapshot_sha256: 3107773a3a3b44d376fb2a8b53914d5f35f503392df321a7e2d83ddbcda25b38
- evidence_id: complex59-agent-doi-10.1073_pnas.1104824108
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1073%2Fpnas.1104824108%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native identity and abstract
  accessed_at: '2026-10-22T07:52:38.610604Z'
  support: supports
  summary: 'Exact native DOI/MED identity: Core unit of chemotaxis signaling complexes.
    Li M, Hazelbauer GL. (2011), PMID21606342. Complete available abstract read.'
  snapshot_sha256: b56205423842386615393232ea137b2875ea36edb364c2a750edd187c66bb263
- evidence_id: complex59-agent-doi-10.1073_pnas.1115719109
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1073%2Fpnas.1115719109%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native identity and abstract
  accessed_at: '2026-10-22T07:52:38.691205Z'
  support: supports
  summary: 'Exact native DOI/MED identity: Bacterial chemoreceptor arrays are hexagonally
    packed trimers of receptor dimers networked by rings of kinase and coupling proteins.
    Briegel A, Li X, Bilwes AM, Hughes KT, Jensen GJ, Crane BR. (2012), PMID22355139.
    Complete available abstract read.'
  snapshot_sha256: e11101bb43b0c817acdda2b387322525e5a8a3e19666e6b04bf833aa4a92e9ea
- evidence_id: complex59-agent-doi-10.1146_annurev-biophys-070816-033555
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1146%2Fannurev-biophys-070816-033555%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native identity and abstract
  accessed_at: '2026-10-22T07:52:39.970717Z'
  support: supports
  summary: 'Exact native DOI/MED identity: Progress and Potential of Electron Cryotomography
    as Illustrated by Its Application to Bacterial Chemoreceptor Arrays. Briegel A,
    Jensen G. (2017), PMID28301773. Complete available abstract read.'
  snapshot_sha256: b0886a3f82dd25f5c571e69cd554cb6a28d0e93c9b1aaa61c3d51a990df9c0f1
- evidence_id: complex59-agent-briegel2009-legacy
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2761316/
  locator: Complete Results/Discussion sec1–4 including Table1/Fig1–4 captions, Conclusion
    sec5 and Methods sec6–9; no Introduction, pixels or supplements.
  accessed_at: '2026-10-22T07:59:45.597927Z'
  support: supports
  summary: Briegel2009 examines13 bacterial species and finds12nm hexagonal order
    in accessible top views. It does not include archaeal specimens. Architectural
    conservation suggests related bacterial mechanisms, rather than directly proving
    the entire causal basis of gain.
  snapshot_sha256: 9b59c7206a0d903d1179d0afdee682b6bc8362045f52b44b7895b919cc958e31
- evidence_id: complex59-agent-li2011-legacy
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3111312/
  locator: Results sec6 including Fig8 caption; complete Discussion SEC3 and Methods
    sec12. No other sections or pixels.
  accessed_at: '2026-10-22T07:58:00.648062Z'
  support: supports
  summary: Purified nanodisc core units comprise two receptor trimers, one CheA dimer
    and two CheW; hexagons are proposed to combine three such cores. Quantitative
    corrections account for extra nonparticipating Tar dimers.
  snapshot_sha256: 2ec14e1b22c4aa236d07d1abe347cee3718df82165c9c954964acaf591de4124
- evidence_id: complex59-agent-briegel2012-legacy
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3309718/
  locator: Complete Results/Discussion SEC1 including Table1/Fig1–4 captions; Methods
    sec3 growth/preparation and sec8 modeling. No pixels/supplements.
  accessed_at: '2026-10-22T07:58:02.388094Z'
  support: supports
  summary: Native-array cryotomography and Thermotoga ternary crystallography support
    alternating CheA-P5/CheW rings linked by CheA dimers. Minimal core units span
    two trimers; ring occupancy and CheW substitution vary.
  snapshot_sha256: da178bd8ce08a69bcd5da4c69cbe40fbb141a9affc4ac1fb65a0729f740dbc1b
- evidence_id: complex59-agent-briegel2014-xml
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3985956/fullTextXML
  locator: Complete unsectioned Introduction, Results sec3.1–3.6 and Discussion sec4
    with Fig1–7 captions. Methods and pixels/supplements not read.
  accessed_at: '2026-10-22T07:57:19.717982Z'
  support: supports
  summary: Briegel,Wong,Hodges and colleagues2014 present primary array experiments.
    Their proposed assembly sequence forms minimal cores first, then rings/superlattices.
    Native, overexpression, membrane reconstitution and soluble-fragment arrays have
    distinct outcomes.
  snapshot_sha256: 8694403ad1d9b5dae30550c47f21ad269bcb6bea602966de3791a47d3424f858
- evidence_id: complex59-agent-parkinson2015-legacy
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4417406/
  locator: Complete abstract and sections S1/S4/S5/S6/S7 including Box1–3 and embedded
    captions; six snippet comparisons after whitespace normalization. Original cited
    experiments were not independently read unless separately listed.
  accessed_at: '2026-10-22T07:58:00.155281Z'
  support: supports
  summary: Parkinson2015 is a secondary review. It distinguishes minimal core units
    from higher-order rings/arrays and describes cooperative gain and inferred pulsatile
    output. All six maintained snippets match the normalized full text exactly, including
    the source’s mechanistic qualifiers.
  snapshot_sha256: dee17c8d6cf4af960df4bd8de58d2f52b49b19c0255935b5182f149618419f25
- evidence_id: complex59-agent-pfam-PF00015
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF00015/
  locator: Native name/type, description and curation flags/signatures; example membership
    is independently supplied by UniProt
  accessed_at: '2026-10-22T07:52:29.466843Z'
  support: supports
  summary: PF00015 is the MCP signaling-region profile; its API type is family but
    its named biological scope is a signaling domain.
  snapshot_sha256: 408b01fef86898cc6c79c46307e72ae896dab42de53f2e42606591946dea1f25
- evidence_id: complex59-agent-pfam-PF01584
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01584/
  locator: Native name/type, description and curation flags/signatures; example membership
    is independently supplied by UniProt
  accessed_at: '2026-10-22T07:52:29.963787Z'
  support: supports
  summary: PF01584 is the CheW-like domain, shared with related chemotaxis proteins.
    Partial-domain xrefs are not exact whole-component grounding.
  snapshot_sha256: 0eee54cb954a957a02a0878fb5c0ef52ac1ee74fa7e1e8eeb4f0100e669720fa
- evidence_id: complex59-agent-interpro-IPR004090
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004090/
  locator: Native name/type, description and curation flags/signatures; example membership
    is independently supplied by UniProt
  accessed_at: '2026-10-22T07:57:28.697355Z'
  support: supports
  summary: IPR004090 describes the MCP protein family with broader related prokaryotic
    signaling context.
  snapshot_sha256: abaa321b6371ccad4d0b0270ef5f4cb5e956547867435615eddb4cbebea7b401
- evidence_id: complex59-agent-interpro-IPR051315
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051315/
  locator: Native name/type, description and curation flags/signatures; example membership
    is independently supplied by UniProt
  accessed_at: '2026-10-22T07:57:28.816024Z'
  support: supports
  summary: IPR051315 is the bacterial CheA family; unchecked machine-generated prose
    is not independent primary evidence.
  snapshot_sha256: f3e80b36131759867ab82696c9d08d07b5918c874ea09c59a47dd3f332413c4d
- evidence_id: complex59-agent-interpro-IPR039315
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR039315/
  locator: Native name/type, description and curation flags/signatures; example membership
    is independently supplied by UniProt
  accessed_at: '2026-10-22T07:57:28.855651Z'
  support: supports
  summary: IPR039315 identifies the CheW protein family, distinct from the broader
    CheW-like domain.
  snapshot_sha256: 38d7a0174f343f9def66b3a79898e33150bf11cdd6a6a681b9b908cfc359c18f
- evidence_id: complex59-agent-traitmech-index
  kind: database
  reference: https://culturebotai.github.io/TraitMech/pages/data/trait_graph.json
  locator: Exact METPO1000702 row in complete published trait index
  accessed_at: '2026-10-22T08:06:36.628289Z'
  support: supports
  summary: The published TraitMech index contains METPO1000702 with exact label motile.
  snapshot_sha256: bdd3ee3c4f3db4e6b73aa25d87da7dfeb179d056154e491a7abc3d643c6847d8
- evidence_id: complex59-agent-uo-0000018
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uo/terms?obo_id=UO:0000018
  locator: Exact OLS term identity and definition
  accessed_at: '2026-10-22T08:06:36.628042Z'
  support: supports
  summary: UO0000018 is nanometer,10^-9 meter.
  snapshot_sha256: 4c7db9c8cb664724cfeb7ded951492cac50dd7c8bdc275363486b3e34df94bf8
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/methyl_accepting_chemotaxis_protein_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T07:58:06Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/methyl_accepting_chemotaxis_protein_complex.yaml'
  snapshot_sha256: ad614672e65221377fd429fb0aa1ffc69df19b873c208577cdb110d4b7a3901c
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/methyl_accepting_chemotaxis_protein_complex.yaml
    --out /private/tmp/cellstructure-batch59-20261022-t3ere5ku/methyl_accepting_chemotaxis_protein_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T07:58:07Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/methyl_accepting_chemotaxis_protein_complex.yaml\
    \ --out /private/tmp/cellstructure-batch59-20261022-t3ere5ku/methyl_accepting_chemotaxis_protein_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch59-20261022-t3ere5ku/methyl_accepting_chemotaxis_protein_complex-strict.tsv"
  snapshot_sha256: c52f8789c39da2600ae71f9639fb8be5459388c19b5f10d5eea1a26023558e0c
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/methyl_accepting_chemotaxis_protein_complex.yaml
    --causal-graphs
  locator: Complete native focused report
  accessed_at: '2026-10-22T08:00:14.609369Z'
  support: supports
  summary: "data/structures/other/methyl_accepting_chemotaxis_protein_complex.yaml\
    \  (GO:0098561)\n  chea_chew_hexagonal_array_assembly\tmcp\tCOVERED\t->mcp (UniProtKB:P07017,\
    \ UniProtKB:P02942, UniProtKB:P05704, UniProtKB:P07018)\n  chea_chew_hexagonal_array_assembly\t\
    chea\tCOVERED\t->chea (UniProtKB:P07363)\n  chea_chew_hexagonal_array_assembly\t\
    chew\tCOVERED\t->chew (UniProtKB:P0A964)\n  chemoreceptor_array_signalling\tmcp\t\
    COVERED\t->mcp (UniProtKB:P07017, UniProtKB:P02942, UniProtKB:P05704, UniProtKB:P07018)\n\
    \  chemoreceptor_array_signalling\tchew\tCOVERED\t->chew (UniProtKB:P0A964)\n\
    \  chemoreceptor_array_signalling\tchea\tCOVERED\t->chea (UniProtKB:P07363)\n\
    \  chemoreceptor_array_signalling\tphospho_chey\tUNANCHORED_WITH_UNIPROT\tphospho-CheY\
    \ (UniProtKB:P0AE67)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n     6  COVERED\
    \                   component_ref target holds protein_examples covering all declared\
    \ symbols\n     1  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries\
    \ a UniProtKB grounding or xref\n     0  PARTIAL_EXAMPLES          component_ref\
    \ target holds protein_examples but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES\
    \   component_ref target declares gene_symbols but holds no protein_examples\n\
    \     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols\
    \ and holds no protein_examples\n     0  DANGLING_COMPONENT_REF    component_ref\
    \ names a component_id that does not exist on the record\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     7\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 452e2d76229c8a377576f3bc9a4c574f49cf751f7efa096d7666b7615079f862
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/methyl_accepting_chemotaxis_protein_complex.yaml
    --verify
  locator: Complete native focused report
  accessed_at: '2026-10-22T08:00:15.790064Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/methyl_accepting_chemotaxis_protein_complex.yaml;
    native collect() exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '20 of 25 collected target identifiers returned OK. METPO:1000702: SKIPPED;
    Exact METPO1000702 row in the complete published TraitMech index has label motile.
    This resolves the linked trait identifier; it does not by itself establish a causal
    mechanism.; PMID:15919996: UNREACHABLE; Native Europe PMC uniquely identifies
    MED15919996: Global topology analysis of the Escherichia coli inner membrane proteome.
    (2005); DOI10.1126/science.1109730. Identifier transport verification is distinct
    from separately scoped primary-source reading.; PMID:22380631: UNREACHABLE; Native
    Europe PMC uniquely identifies MED22380631: Isolation and identification of new
    inner membrane-associated proteins that localize to cell poles in Escherichia
    coli. (2012); DOI10.1111/j.1365-2958.2012.08021.x. Identifier transport verification
    is distinct from separately scoped primary-source reading.; Pfam:PF00015: SKIPPED;
    Native PfamPF00015 identifies Methyl-accepting chemotaxis protein (MCP) signalling
    domain, API type family, integrated into IPR004089. Native identity is distinct
    from treating a domain profile as an exact whole-protein family.; Pfam:PF01584:
    SKIPPED; Native PfamPF01584 identifies CheW-like domain, API type domain, integrated
    into IPR002545. Native identity is distinct from treating a domain profile as
    an exact whole-protein family. Native source checks are separately scoped; skipped
    or unreachable identifiers are not silently counted as resolved.'
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
  topic: Array identity and native molecular examples
  outcome: supported
  target_ids:
  - GO:0098561
  summary: The exact GO transmembrane signaling-complex identity, E.coli proteins/aliases,
    CheY output xref, partial-domain xrefs, motile trait and nanometer unit are supported.
    The broader chemosensory-array literature also contains cytoplasmic arrays; no
    silent extension of this transmembrane GO class is inferred.
  evidence_ids:
  - record
  - complex59-agent-go
  - complex59-agent-go-0098561-ancestors
  - complex59-agent-traitmech-index
  - complex59-agent-uo-0000018
  - complex59-agent-protein-P02942
  - complex59-agent-protein-P05704
  - complex59-agent-protein-P07017
  - complex59-agent-protein-P07018
  - complex59-agent-protein-P07363
  - complex59-agent-protein-P0A964
  - complex59-agent-protein-P0AE67
  - complex59-agent-query-cheA
  - complex59-agent-query-cheW
  - complex59-agent-query-tap
  - complex59-agent-query-tar
  - complex59-agent-query-trg
  - complex59-agent-query-tsr
  - complex59-agent-tax-2
  - complex59-agent-tax-2157
  - complex59-agent-tax-83333
  - complex59-agent-pfam-PF00015
  - complex59-agent-pfam-PF01584
  - complex59-agent-interpro-IPR004090
  - complex59-agent-interpro-IPR051315
  - complex59-agent-interpro-IPR039315
- assessment_id: assembly
  area: graph
  topic: Core-to-ring architecture
  outcome: concern
  target_ids:
  - GO:0098561
  summary: 'The ring-to-core edge reverses the source-defined size/assembly relationship:
    one minimal core contains two trimers, one CheA dimer and two CheW, whereas three
    cores can build a hexagonal ring unit. The source does not identify a completed
    ring as that minimal core.'
  evidence_ids:
  - record
  - complex59-agent-li2011-legacy
  - complex59-agent-briegel2012-legacy
  - complex59-agent-briegel2014-xml
  - complex59-agent-parkinson2015-legacy
- assessment_id: scope
  area: scope
  topic: Measured bacterial architecture versus asserted archaeal invariance
  outcome: concern
  target_ids:
  - GO:0098561
  summary: Briegel2009 contains13 bacterial species, not archaeal experiments. Broad
    archaeal MCP occurrence has review support, but the cited study does not establish
    the exact cross-domain12nm claim repeated in the definition/property/Archaea row/assembly
    note. The definition also makes geometry the complete explanation of gain where
    the reviewed mechanisms remain qualified. COMMON keeps the schema majority/losses-exception
    meaning; no quantitative bacterial prevalence census was established.
  evidence_ids:
  - record
  - schema
  - complex59-agent-briegel2009-legacy
  - complex59-agent-parkinson2015-legacy
  - complex59-agent-tax-2
  - complex59-agent-tax-2157
  - complex59-agent-tax-83333
- assessment_id: function
  area: graph
  topic: Signaling source support and current narrative
  outcome: concern
  target_ids:
  - GO:0098561
  summary: The six literal review snippets, E.coli gain/control context and Stewart1997
    complete abstract support the functional sequence at their stated tiers. Pulsatile
    output is an inference, not direct measurement, as the evidence note acknowledges.
    The current description and output-edge note still say CheA-to-CheY is not drawn,
    despite the present directly cited edge; historical dated history and resolved
    discussion are not errors.
  evidence_ids:
  - record
  - complex59-agent-parkinson2015-legacy
  - complex59-agent-doi-10.1016_j.tim.2015.03.003
  - complex59-agent-doi-10.1021_bi5000614
  - complex59-agent-doi-10.1021_bi962261k
  - complex59-agent-doi-10.1073_pnas.0905181106
  - complex59-agent-doi-10.1073_pnas.1104824108
  - complex59-agent-doi-10.1073_pnas.1115719109
  - complex59-agent-doi-10.1146_annurev-biophys-070816-033555
- assessment_id: citation
  area: evidence
  topic: Primary2014 source identity
  outcome: concern
  target_ids:
  - GO:0098561
  summary: The exact DOI identifies a2014 primary article led by Briegel,Wong,Hodges,
    not the2012 Briegel,Li,Bilwes,Hughes,Jensen,Crane author list and not a review.
    The cited assembly model is present, but the attribution should identify its actual
    source.
  evidence_ids:
  - record
  - complex59-agent-briegel2014-xml
  - complex59-agent-doi-10.1016_j.tim.2015.03.003
  - complex59-agent-doi-10.1021_bi5000614
  - complex59-agent-doi-10.1021_bi962261k
  - complex59-agent-doi-10.1073_pnas.0905181106
  - complex59-agent-doi-10.1073_pnas.1104824108
  - complex59-agent-doi-10.1073_pnas.1115719109
  - complex59-agent-doi-10.1146_annurev-biophys-070816-033555
- assessment_id: formation
  area: grounding
  topic: Constituent roles and unmeasured universal necessity
  outcome: unknown
  target_ids:
  - GO:0098561
  summary: The three protein classes define the canonical functional core and normal
    array architecture. Non-native receptor zippers are not counterexamples to formation
    of that same complex. The inspected conditions do not establish universal individual
    formation necessity across the full bacterial/archaeal scope; this is retained
    as unknown rather than a forced omission finding.
  evidence_ids:
  - record
  - schema
  - complex59-agent-briegel2009-legacy
  - complex59-agent-li2011-legacy
  - complex59-agent-briegel2012-legacy
  - complex59-agent-briegel2014-xml
- assessment_id: coverage
  area: completeness
  topic: Whole maintained target and declared source coverage
  outcome: supported
  target_ids:
  - GO:0098561
  summary: Every maintained field, source note, graph and discussion was inspected
    at the declared extents. Optional inventory/contact enrichment and acknowledged
    unknowns alone do not create findings.
  evidence_ids:
  - record
  - schema
  - curation
  - complex59-agent-go
findings:
- finding_id: F1
  issue_key: mcp-core-ring-hierarchy
  category: graph
  severity: major
  status: open
  certainty: confirmed
  title: Correct the reversed core-unit and ring relationship
  description: The ASSEMBLY edge from alternating CheA/CheW ring to core signaling
    unit assigns the larger ring to the minimal repeated core. Li2011 and Briegel2014
    define the core first as two trimers+one CheA dimer+two CheW, then combine cores
    into rings/arrays. The edge’s own note describes the opposite order.
  target_ids:
  - GO:0098561
  field_paths:
  - causal_graphs#chea_chew_hexagonal_array_assembly.edges
  evidence_ids:
  - record
  - complex59-agent-li2011-legacy
  - complex59-agent-briegel2012-legacy
  - complex59-agent-briegel2014-xml
  - complex59-agent-parkinson2015-legacy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/methyl_accepting_chemotaxis_protein_complex.yaml
    role: maintained scientific record
  rule_id: Source-backed identity, grounding and claim scope
  native_severity: major
  normalization_reason: A materially wrong assembly hierarchy or unsupported defining
    biological scope requires correction.
- finding_id: F2
  issue_key: mcp-cross-domain-architecture-scope
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Bound the cross-domain architecture claim to its evidence
  description: The defining12nm claim, physical-property context, Archaea row and
    assembly evidence attribute bacterial-plus-archaeal conservation to a study of13
    bacterial species. The inspected review supports archaeal MCP occurrence but not
    this asserted measurement. A bacterial source cannot independently establish the
    maintained universal cross-domain defining property.
  target_ids:
  - GO:0098561
  field_paths:
  - definition
  - physical_properties
  - taxonomic_distribution
  - causal_graphs#chea_chew_hexagonal_array_assembly.edges
  evidence_ids:
  - record
  - complex59-agent-briegel2009-legacy
  - complex59-agent-parkinson2015-legacy
  - complex59-agent-tax-2
  - complex59-agent-tax-2157
  - complex59-agent-tax-83333
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/methyl_accepting_chemotaxis_protein_complex.yaml
    role: maintained scientific record
  rule_id: Source-backed identity, grounding and claim scope
  native_severity: major
  normalization_reason: A materially wrong assembly hierarchy or unsupported defining
    biological scope requires correction.
- finding_id: F3
  issue_key: mcp-2014-primary-attribution
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the 2014 primary-paper attribution
  description: The ring/core edge uses the correct2014 DOI but names the2012 author
    roster and calls the article a review. Its actual primary author list begins Briegel,Wong,Hodges;
    the article contains the proposed assembly model.
  target_ids:
  - GO:0098561
  field_paths:
  - causal_graphs#chea_chew_hexagonal_array_assembly.edges.evidence
  evidence_ids:
  - record
  - complex59-agent-briegel2014-xml
  - complex59-agent-doi-10.1016_j.tim.2015.03.003
  - complex59-agent-doi-10.1021_bi5000614
  - complex59-agent-doi-10.1021_bi962261k
  - complex59-agent-doi-10.1073_pnas.0905181106
  - complex59-agent-doi-10.1073_pnas.1104824108
  - complex59-agent-doi-10.1073_pnas.1115719109
  - complex59-agent-doi-10.1146_annurev-biophys-070816-033555
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/methyl_accepting_chemotaxis_protein_complex.yaml
    role: maintained scientific record
  rule_id: Source-backed identity, grounding and claim scope
  native_severity: minor
  normalization_reason: A bounded correction preserves the supported complex identity
    and principal biological function.
- finding_id: F4
  issue_key: mcp-current-phosphotransfer-narrative
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Synchronize the current phosphotransfer narrative
  description: The functional graph currently contains the Stewart1997 CheA-to-CheY
    edge, while its description and output-edge evidence note say that step is not
    drawn. The resolved historical discussion already records the addition.
  target_ids:
  - GO:0098561
  field_paths:
  - causal_graphs#chemoreceptor_array_signalling.description
  - causal_graphs#chemoreceptor_array_signalling.edges.evidence.notes
  evidence_ids:
  - record
  - complex59-agent-parkinson2015-legacy
  - complex59-agent-doi-10.1016_j.tim.2015.03.003
  - complex59-agent-doi-10.1021_bi5000614
  - complex59-agent-doi-10.1021_bi962261k
  - complex59-agent-doi-10.1073_pnas.0905181106
  - complex59-agent-doi-10.1073_pnas.1104824108
  - complex59-agent-doi-10.1073_pnas.1115719109
  - complex59-agent-doi-10.1146_annurev-biophys-070816-033555
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/methyl_accepting_chemotaxis_protein_complex.yaml
    role: maintained scientific record
  rule_id: Source-backed identity, grounding and claim scope
  native_severity: minor
  normalization_reason: A bounded correction preserves the supported complex identity
    and principal biological function.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0098561
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/methyl_accepting_chemotaxis_protein_complex.yaml
    role: maintained scientific record
  description: Represent the minimal core before higher-order rings/arrays, with labels
    and directed edges matching the cited assembly model; retain the supported trimer
    geometry and variable array occupancy.
  acceptance_checks:
  - Do not equate a completed alternating ring with one minimal core; distinguish
    experimentally measured stoichiometry from proposed sequential assembly.
  - Preserve supported source-specific claims and pass applicable native gates.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0098561
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/methyl_accepting_chemotaxis_protein_complex.yaml
    role: maintained scientific record
  description: Restrict measured12nm conservation and its citation to the sampled
    bacterial scope, or add an actually inspected archaeal architecture source before
    retaining the broader claim. Separate qualified mechanistic interpretation of
    gain from the geometry measurement.
  acceptance_checks:
  - Do not declare archaeal arrays absent or biologically different merely from this
    source mismatch; retain exact ontology identity and correct bacterial measurements.
  - Preserve supported source-specific claims and pass applicable native gates.
- action_id: A3
  finding_ids:
  - F3
  target_ids:
  - GO:0098561
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/methyl_accepting_chemotaxis_protein_complex.yaml
    role: maintained scientific record
  description: Correct the author attribution and identify the source as a primary
    experimental study with a proposed assembly model.
  acceptance_checks:
  - Retain the exact DOI and distinguish the model from directly observed sequential
    assembly.
  - Preserve supported source-specific claims and pass applicable native gates.
- action_id: A4
  finding_ids:
  - F4
  target_ids:
  - GO:0098561
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/methyl_accepting_chemotaxis_protein_complex.yaml
    role: maintained scientific record
  description: Update only current graph prose to acknowledge the present directly
    sourced phosphotransfer edge; preserve the dated historical record and resolved
    discussion.
  acceptance_checks:
  - The current graph description must agree with its nodes/edges and retain the distinction
    between direct phosphotransfer kinetics and inferred pulsatile output.
  - Preserve supported source-specific claims and pass applicable native gates.
limitations:
- All five completed same-base batch26 global gates are integrated with exact manifest/input/log
  hashes verified; no fresh full-site QC is claimed from this sparse checkout.
- Only the explicitly listed source sections/assets were inspected. No unlisted supplements,
  atomic coordinates or raw experimental data were analyzed.
- Briegel/Jensen2017 and Stewart1997 were inspected at complete native metadata/abstract
  scope only; the2017publisher PDF returned403. Briegel2009/2012/2014, Li2011 and
  Parkinson2015 were read only at the explicit extents above. No figure pixels or
  supplements were inspected.
- The six quotations were verified exactly after whitespace normalization; this verifies
  wording, not independent replication of the review’s cited primary experiments.
  No archaeal architecture primary was inspected.
- Whole-protein family candidates are retained as bounded context rather than forced
  mappings for unqualified cross-domain cohorts; the existing Pfam xrefs describe
  partial regions.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The explicit all-record goal authorizes both clean and issue-bearing reviews.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
