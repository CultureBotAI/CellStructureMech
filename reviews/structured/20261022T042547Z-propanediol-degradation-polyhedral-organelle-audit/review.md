# Source-backed review of propanediol degradation polyhedral organelle

- Review: 20261022T042547Z-propanediol-degradation-polyhedral-organelle-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T03:58:32Z
- Finished UTC: 2026-10-22T04:25:47Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Two major corrections address PduU shell-class identity and the mechanistic cargo-binding partner; one minor correction supplies the verified PduM family. Other identity, taxon and metabolic claims are supported within stated limits.

## Scope And Provenance

Exactly one complete target; no neighboring scientific-record verdict is imported. Exact authority, all current component/function/graph/source placements, taxonomic scope, formation semantics, history and discussions were reviewed.

Selection: Batch43 fixed strict path order, index 1; exactly one maintained target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0031472 | data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml | maintained | propanediol degradation polyhedral organelle |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0031472 | Focused validator passed. |
| Focused native strict | passed | True | GO:0031472 | Focused validator passed. |
| Focused native proteins | passed | True | GO:0031472 | Read-only native check passed; claim-level protein/edge support evaluated separately. |
| Focused native graphs | passed | True | GO:0031472 | Read-only native check passed; claim-level protein/edge support evaluated separately. |
| Claim-level scientific review | passed | True | GO:0031472 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0031472 | 27 of 34 collected target identifiers returned OK. PMID:10498708: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were reviewed after the bulk eutils414 transport failure. Biological support remains bounded by the separately recorded abstract or primary-body sections; identity resolution alone is not confirmation of every attached claim.; PMID:11844753: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were reviewed after the bulk eutils414 transport failure. Biological support remains bounded by the separately recorded abstract or primary-body sections; identity resolution alone is not confirmation of every attached claim.; PMID:12923081: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were reviewed after the bulk eutils414 transport failure. Biological support remains bounded by the separately recorded abstract or primary-body sections; identity resolution alone is not confirmation of every attached claim.; PMID:21239588: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were reviewed after the bulk eutils414 transport failure. Biological support remains bounded by the separately recorded abstract or primary-body sections; identity resolution alone is not confirmation of every attached claim.; PMID:22343294: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were reviewed after the bulk eutils414 transport failure. Biological support remains bounded by the separately recorded abstract or primary-body sections; identity resolution alone is not confirmation of every attached claim.; PMID:24747050: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were reviewed after the bulk eutils414 transport failure. Biological support remains bounded by the separately recorded abstract or primary-body sections; identity resolution alone is not confirmation of every attached claim.; PMID:27063436: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were reviewed after the bulk eutils414 transport failure. Biological support remains bounded by the separately recorded abstract or primary-body sections; identity resolution alone is not confirmation of every attached claim. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0031472 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0031472 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0031472 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0031472 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0031472 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Pdu identity, hierarchy and metabolic boundary

identity: supported. Targets: GO:0031472.

Exact GO identity, protein-shell class and BMC parent are supported; the activity GO is correctly withheld as a PduCDE-complex grounding.

### Protein cohorts and exact family gaps

grounding: concern. Targets: GO:0031472.

Membership and native structural/cargo roles are supported, but PduU is a hexameric BMC-H member placed in the BMC-T cohort. PduM has a verified exact family available. Other narrower Pdu-specific cohorts are not forced into broad domain families.

### Formation versus catalysis

grounding: unknown. Targets: GO:0031472.

PduCDE DISPENSABLE is supported by recovered MCPs from its deletion background. UNKNOWN PduM/PduN avoids overstating necessity. CONDITIONAL shell-cohort labels lack a complete condition-by-member necessity matrix; PduA phenotypes differ between the cited 2002 and 2020 contexts. No individual member is inferred essential from intact structure.

### Exact native gene identities and annotation provenance

grounding: supported. Targets: GO:0031472.

All eleven accessions, LT2 taxon, reviewed status and gene aliases agree, including the native PduU BMC-H name. Localization-evidence notes match native citation joins. Held2016 attribution is treated as native annotation provenance; its recombinant Eut work does not independently establish every native Pdu placement.

### Taxa and induction contexts

scope: supported. Targets: GO:0031472.

VARIABLE Bacteria and the native LT2 canonical example are supported. Genomic potential, induced laboratory organelles, deletion strains and fusion reporters remain distinct.

### Propanediol catalysis and aldehyde protection

evidence: supported. Targets: GO:0031472.

The retained native abstracts and direct studies support PduCDE chemistry, compartmentalization and protection from propionaldehyde-associated damage. Sampson2008 is abstract-only in this review; detailed damage assays were not inspected.

### Convergent model and unsupported binding partner

graph: concern. Targets: GO:0031472.

The Yang2022 convergence and proposed PduM/PduB bridge are accurately model-scoped; PduN geometry is a homologous-family inference supported by later native context. The separate enzyme-core→BMC-T binding edge assigns a specific receptor class beyond Fan2010/2011 targeting evidence. Fan2012’s directly reported PduP receptor is PduA/PduJ, not a general BMC-T cohort. Three CDE xrefs are examples within the broader core and are not treated as an exhaustive equality.

### Whole-record coverage and source limits

completeness: supported. Targets: GO:0031472.

All current fields, two synonyms, protein examples, graph, source notes and history were reviewed. No maintained image or verbatim snippet is present. Optional accessory enzymes and family candidates broader than the exact curated subsets do not create automatic findings.

## Findings

### F1: Separate PduU from the tandem-domain BMC-T cohort

major / open / confirmed; issue key: pdu-pduu-shell-class.

The component explicitly declares PduB, PduT and PduU to be BMC-T proteins and treats circular permutation as sufficient for that class. The cited quantitative study distinguishes trimeric PduT from hexameric PduU; native PduU and domain metadata identify the single-domain BMC-H architecture. Correct organelle membership does not repair the wrong molecular subclass.

### F2: Do not infer a general BMC-T receptor from cargo-targeting experiments

major / open / confirmed; issue key: pdu-targeting-bmc-t-partner.

The MECHANISTIC edge directly binds the lumen enzyme core to the BMC-T cohort. Fan2010/2011 establish terminal-sequence targeting, not that specific receptor class. The separately verified Fan2012 abstract reports PduP binding to PduA/PduJ, and the Yang2022 PduM/PduB model is a different, explicitly qualified coupling mechanism. The existing edge conflates these cargo and interaction contexts.

### F3: Ground PduM to its verified protein family

minor / open / confirmed; issue key: pdu-pdum-family-grounding.

The label-only PduM component now has an exact source-neutral family, IPR030992, whose native description and citation match the curated structural protein. This is a current resolvable gap, not a claim that a historical search was dishonest.

## Recommended Actions And Acceptance Checks

### A1

In authorized curation, move or separately represent PduU in its supported single-domain circularly permuted BMC-H class. Retain PduB/PduT in the properly scoped BMC-T cohort and update dependent node membership without losing supported PduU occurrence.

- Preserve exact supported identity, experimental organism and native versus recombinant context.
- Attach source-specific evidence to each changed claim and retain historical provenance.
- Native schema, strict, CURIE, protein and graph checks pass as applicable.

### A2

Replace the edge with the directly supported targeting relation or a specifically identified, source-qualified cargo/receptor interaction. If representing PduP–PduA/PduJ, preserve that distinct cargo identity and cite its actual interaction study; do not reassign PduD/CDE binding merely by analogy.

- Preserve exact supported identity, experimental organism and native versus recombinant context.
- Attach source-specific evidence to each changed claim and retain historical provenance.
- Native schema, strict, CURIE, protein and graph checks pass as applicable.

### A3

Use the verified PduM family grounding and reconcile the label-only note, preserving organism-specific examples and the model-qualified assembly role.

- Preserve exact supported identity, experimental organism and native versus recombinant context.
- Attach source-specific evidence to each changed claim and retain historical provenance.
- Native schema, strict, CURIE, protein and graph checks pass as applicable.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml; Complete maintained YAML; all components, source notes, graphs, discussions and historical entries | context_only | The entire maintained target was read; no scientific record was changed. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent; ComponentTypeEnum; EssentialityEnum; graph scopes | context_only | Protein-family identity is distinct from an assembled complex. ESSENTIAL concerns failure of structure formation, not merely loss of catalytic or transport function. |
| curation | docs/CURATION.md; Components; groundings; associated machinery and chaperone boundaries | context_only | Components are taxon-agnostic molecular families/classes; exact family grounding is preferred when verified. Mature constituents and assembled-structure maintenance machinery differ from transient preassembly chaperones. |
| micro43-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000148,GO:0003843,GO:0009277,GO:0031469,GO:0031472,GO:0042910,GO:0050215,GO:0051144,GO:0071970,GO:1990281; Requested entries GO0031472/0031469/0051144/0050215: complete names, definitions, typed children and active status. | supports | GO0031472 exactly denotes the protein-coated propanediol-degradation organelle and is an is_a child of GO0031469. GO0051144 denotes propanediol catabolism; GO0050215 is an enzyme activity, not a source-neutral PduCDE complex identity. |
| micro43-tax2 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2; Complete taxId/scientificName/rank/lineage/otherNames. | supports | ENA taxId 2 identifies Bacteria at rank domain; aliases and lineage match the record. Identity alone is not prevalence or experimental-condition evidence. |
| micro43-tax99287 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/99287; Complete taxId/scientificName/rank/lineage/otherNames. | supports | ENA taxId 99287 identifies Salmonella enterica subsp. enterica serovar Typhimurium str. LT2 at rank strain; aliases and lineage match the record. Identity alone is not prevalence or experimental-condition evidence. |
| micro43-doi-1 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1002%2Fpro.2246&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED23456886: Bacterial microcompartment shells of diverse functional types possess pentameric vertex proteins. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro43-doi-2 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fs41467-020-15888-4&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED32332738: Decoding the stoichiometric composition and organisation of bacterial metabolosomes. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro43-doi-3 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fs41467-021-24126-4&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED34155212: A catalog of the diversity and ubiquity of bacterial microcompartments. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro43-doi-4 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fs41467-022-30608-w&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED35614058: Biogenesis of a bacterial metabolosome for propanediol utilization. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro43-doi-5 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1073%2Fpnas.0913199107&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED20308536: Short N-terminal sequences package proteins into bacterial microcompartments. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro43-doi-9 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FJB.01925-07&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED18296526: Microcompartments for B12-dependent 1,2-propanediol degradation provide protection from DNA and cellular damage by a reactive metabolic intermediate. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro43-doi-10 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FJB.05661-11&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED21821773: The N-terminal region of the medium subunit (PduD) packages adenosylcobalamin-dependent diol dehydratase (PduCDE) into the Pdu microcompartment. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro43-doi-11 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FJB.06529-11&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED22343294: The PduM protein is a structural component of the microcompartments involved in coenzyme B(12)-dependent 1,2-propanediol degradation by Salmonella enterica. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro43-doi-12 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FJB.179.21.6633-6639.1997&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED9352910: Propanediol utilization genes (pdu) of Salmonella typhimurium: three genes for the propanediol dehydratase. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro43-doi-13 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FJB.184.5.1253-1261.2002&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED11844753: PduA is a shell protein of polyhedral organelles involved in coenzyme B(12)-dependent degradation of 1,2-propanediol in Salmonella enterica serovar typhimurium LT2. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro43-doi-14 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FJB.185.17.5086-5095.2003&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED12923081: Protein content of polyhedral organelles involved in coenzyme B12-dependent degradation of 1,2-propanediol in Salmonella enterica serovar Typhimurium LT2. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro43-doi6 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1073/pnas.1207516109%22&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED22927404: Interactions between the termini of lumen enzymes and shell proteins mediate enzyme encapsulation into bacterial microcompartments. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro43-pmid10498708 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10498708+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED10498708: The propanediol utilization (pdu) operon of Salmonella enterica serovar Typhimurium LT2 includes genes necessary for formation of polyhedral organelles involved in coenzyme B(12)-dependent 1, 2-propanediol degradation. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro43-pmid11844753 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11844753+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED11844753: PduA is a shell protein of polyhedral organelles involved in coenzyme B(12)-dependent degradation of 1,2-propanediol in Salmonella enterica serovar typhimurium LT2. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro43-pmid12923081 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12923081+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED12923081: Protein content of polyhedral organelles involved in coenzyme B12-dependent degradation of 1,2-propanediol in Salmonella enterica serovar Typhimurium LT2. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro43-pmid21239588 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21239588+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED21239588: Genetic analysis of the protein shell of the microcompartments involved in coenzyme B12-dependent 1,2-propanediol degradation by Salmonella. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro43-pmid22343294 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22343294+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED22343294: The PduM protein is a structural component of the microcompartments involved in coenzyme B(12)-dependent 1,2-propanediol degradation by Salmonella enterica. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro43-pmid24747050 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A24747050+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED24747050: Alanine scanning mutagenesis identifies an asparagine-arginine-lysine triad essential to assembly of the shell of the Pdu microcompartment. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro43-pmid27063436 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A27063436%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED27063436: Engineering formation of multiple recombinant Eut protein nanocompartments in E. coli. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro43-legacy-PMC7181861 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7181861/; Genuine primary HTML; all direct paragraphs of Sec1, Sec3, Sec4, Sec7, Sec9, Sec12 and Sec16 independently read. Class distinction: Sec4 paragraph 5. No figure pixels or supplementary data inspected. | supports | Native LT2-derived Pdu organelles were isolated and quantitatively characterized. The article distinguishes trimeric PduT from hexameric PduU. Its abundance estimates assume 60 PduN copies; they are not an independent direct vertex count. Functional organelles were recovered from its pduA-deletion condition, unlike a blanket extrapolation from earlier loss phenotypes. |
| micro43-legacy-PMC9132943 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9132943/; Genuine primary HTML; complete direct paragraphs in Sec1,3,4,5,6,8,9,12,16,21,22. Sec8 compares shell-first/cargo-first trajectories; Sec12 gives the model; Sec16/21/22 provide strain, growth and imaging context. No figure pixels or supplements. | supports | LT2-derived tagged-protein imaging and deletion studies support independent shell/cargo assemblies and convergent pathways, with PduCDE driving core recruitment and a proposed PduM/PduB link. Colocalization/deletion phenotypes support the hierarchical model; they do not directly measure a purified PduM–PduD binding interaction. Imaging cultures and fluorescent fusions remain distinct from an unmodified organelle. |
| micro43-legacy-PMC3187188 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3187188/; Genuine primary HTML; complete Results sec11–14 and Discussion sec15; Methods sec4/5/7/9 including Table1 strain context. Native source shows growth on succinate plus 1,2-PD and plasmid/IPTG constructs. No microscopy pixels or supplementary data. | supports | PduD N-terminal targeting is necessary/sufficient for packaging tested PduCDE and reporter constructs into LT2-derived MCPs. PduCDE deletion still permits MCP purification. Results and Discussion do not assign a BMC-T shell receptor. Intact-versus-broken immunoprecipitation supports internal packaging, while the Discussion distinguishes Salmonella and Citrobacter targeting observations. |
| micro43-body-PMC3318458 | https://pmc.ncbi.nlm.nih.gov/articles/3318458/; Genuine primary HTML; complete sec3,7,12,16,17,20,21: strain/purification/EM methods, sequence analysis, deletion phenotype, MS/Western and Discussion. No raw figure pixels. | supports | PduM is a native MCP structural constituent; deletion produces predominantly abnormal organelles rather than proving all formation impossible. The paper supports the PduM identity and structural role used by its exact InterPro family. |
| micro43-legacy-PMC134856 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC134856/; Genuine primary HTML; sec3,19,20,21,22 completely read: growth, immunogold, DDH localization, deletion and complementation. | supports | Immunogold identifies PduA at the shell and diol dehydratase internally in LT2-derived bodies; the tested pduA deletion disrupted normal organelle formation and complementation restored it. This experiment is not exported to every later strain/condition. |
| micro43-legacy-PMC180998 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC180998/; Genuine primary HTML; sec3,15,18,21,22,24,25 completely read, including purification, EM, immunoblot, sequence/MS, abundance and Discussion. | supports | Purified LT2-derived organelles contain the reported shell and enzyme proteins, with native EM, Western, N-terminal and MS characterization. Cultures used succinate plus propanediol without B12; isolation is not itself a simultaneous physiological degradation-rate assay. PduA was directly established as shell protein, while several other placements were inferred in this 2003 study. |
| micro43-body-PMC3649267 | https://pmc.ncbi.nlm.nih.gov/articles/3649267/; Genuine primary HTML reused with unchanged receipt; Abstract, Introduction sec1, all Results sec2 paragraphs1–8 and Methods sec4–7 independently read. No figure pixels. | supports | Primary crystallography directly examines Rhodospirillum GrpN and solution measurements examine E. coli EutN. PduN vertex assignment belongs to the homologous BMC-P inference, not a PduN crystal structure produced in this study. This distinction qualifies the record’s shorthand without rejecting the supported PduN role. |
| micro43-legacy-PMC8217296 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8217296/; Genuine primary HTML reused unchanged; Sec1 paragraph1, Sec3 paragraph2, Sec6 paragraph1, Sec8 paragraph4, Sec9 paragraphs1–2 independently read. Other body text is not certified by this row. | supports | The primary genomic catalog supports patchy PDU loci across bacterial lineages and conserved BMC shell classes. Locus calls are genomic potential, not microscopy-confirmed organelles or expression in every genome. |
| micro43-ipr-IPR030992 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR030992/; Complete metadata accession/type/name/description/member databases/hierarchy and literature identity. | supports | IPR030992 is the exact Bacterial microcompartment assembly protein PduM family, with the PduM structural role and Sinha2012 reference. It resolves the currently label-only PduM component without substituting a single organism accession for a family. |
| micro43-ipr-IPR044870 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR044870/; metadata accession/type/name, complete description and hierarchy; no claim that this domain is the exact PduU-only family. | supports | This circularly permuted BMC domain description distinguishes single-domain hexameric BMC-H from tandem-domain trimeric BMC-T. Circular permutation alone is not tandem architecture. |
| micro43-ipr-IPR009307 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR009307/; metadata name/type/complete description and hierarchy. | supports | The EutS/PduU/CutR family spans more than the Pdu-specific subset and supports the circularly permuted PduU class; it is not an exact identity for every Pdu BMC-T protein. |
| micro43-up-P0A1C7 | https://rest.uniprot.org/uniprotkb/P0A1C7.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. | supports | P0A1C7 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['pduA']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro43-up-H9L478 | https://rest.uniprot.org/uniprotkb/H9L478.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. | supports | H9L478 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['pduJ']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro43-up-Q9XDN6 | https://rest.uniprot.org/uniprotkb/Q9XDN6.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. | supports | Q9XDN6 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['pduK']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro43-up-P37449 | https://rest.uniprot.org/uniprotkb/P37449.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. | supports | P37449 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['pduB']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro43-up-Q9XDM8 | https://rest.uniprot.org/uniprotkb/Q9XDM8.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. | supports | Q9XDM8 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['pduT']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro43-up-P0A1D1 | https://rest.uniprot.org/uniprotkb/P0A1D1.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. | supports | P0A1D1 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['pduU']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro43-up-Q9XDN3 | https://rest.uniprot.org/uniprotkb/Q9XDN3.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. | supports | Q9XDN3 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['pduN']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro43-up-Q9XDN4 | https://rest.uniprot.org/uniprotkb/Q9XDN4.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. | supports | Q9XDN4 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['pduM']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro43-up-P37450 | https://rest.uniprot.org/uniprotkb/P37450.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. | supports | P37450 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['pduC']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro43-up-O31041 | https://rest.uniprot.org/uniprotkb/O31041.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. | supports | O31041 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['pduD']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro43-up-O31042 | https://rest.uniprot.org/uniprotkb/O31042.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. | supports | O31042 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['pduE']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro43-pdu-unique | https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A99287+AND+%28gene_exact%3ApduA+OR+gene_exact%3ApduB+OR+gene_exact%3ApduC+OR+gene_exact%3ApduD+OR+gene_exact%3ApduE+OR+gene_exact%3ApduJ+OR+gene_exact%3ApduK+OR+gene_exact%3ApduM+OR+gene_exact%3ApduN+OR+gene_exact%3ApduT+OR+gene_exact%3ApduU%29&amp;format=json&amp;size=100&amp;fields=accession%2Cid%2Cgene_names%2Corganism_id%2Cprotein_name; Complete public UniProt results; exact reviewed/taxon/gene query retained in source URL; result count below page size 100. | supports | The bounded reviewed LT2 query returns exactly the eleven declared gene identities, one accession per requested symbol. This verifies current resolution, not the historical retrieval date or every localization experiment. |
| micro43-legacy-PMC2867708 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2867708/; Exact retained response bytes; access/readability evidence only, not primary article results. | context_only | HTTP 200: challenge HTML rather than Fan2010 article body; complete native MED abstract was readable separately. |
| micro43-legacy-PMC2293232 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2293232/; Exact retained response bytes; access/readability evidence only, not primary article results. | context_only | HTTP 200: challenge HTML rather than Sampson2008 article body; complete native MED abstract supports the stated protective function at abstract tier. |
| schema-result | just validate data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml |
| strict-result | just validate-strict data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml --out /private/tmp/cellstructure-batch43-20261022-u_vlughs/propanediol_degradation_polyhedral_organelle-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml --out /private/tmp/cellstructure-batch43-20261022-u_vlughs/propanediol_degradation_polyhedral_organelle-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch43-20261022-u_vlughs/propanediol_degradation_polyhedral_organelle-strict.tsv |
| native-proteins | /private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml; Complete read-only focused native proteins log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-graphs | /private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml; Complete read-only focused native graphs log | supports | data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml  (GO:0031472)<br>  pdu_shell_cargo_convergent_biogenesis	pdu_bmc_h_shell_proteins	COVERED	-&gt;pdu_bmc_h_shell_proteins (UniProtKB:P0A1C7, UniProtKB:H9L478, UniProtKB:Q9XDN6)<br>  pdu_shell_cargo_convergent_biogenesis	pdu_bmc_t_shell_proteins	COVERED	-&gt;pdu_bmc_t_shell_proteins (UniProtKB:P37449, UniProtKB:Q9XDM8, UniProtKB:P0A1D1)<br>  pdu_shell_cargo_convergent_biogenesis	pdun_vertex_shell_protein	COVERED	-&gt;pdun_vertex_shell_protein (UniProtKB:Q9XDN3)<br>  pdu_shell_cargo_convergent_biogenesis	pducde_diol_dehydratase	COVERED	-&gt;pducde_diol_dehydratase (UniProtKB:P37450, UniProtKB:O31041, UniProtKB:O31042)<br>  pdu_shell_cargo_convergent_biogenesis	pdu_lumen_enzyme_core	UNANCHORED_WITH_UNIPROT	Pdu lumen enzyme core (UniProtKB:P37450, UniProtKB:O31041, UniProtKB:O31042)<br>  pdu_shell_cargo_convergent_biogenesis	pdum_structural_protein	COVERED	-&gt;pdum_structural_protein (UniProtKB:Q9XDN4)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     5  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     1  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     6  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 27 of 34 collected target identifiers returned OK. PMID:10498708: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were reviewed after the bulk eutils414 transport failure. Biological support remains bounded by the separately recorded abstract or primary-body sections; identity resolution alone is not confirmation of every attached claim.; PMID:11844753: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were reviewed after the bulk eutils414 transport failure. Biological support remains bounded by the separately recorded abstract or primary-body sections; identity resolution alone is not confirmation of every attached claim.; PMID:12923081: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were reviewed after the bulk eutils414 transport failure. Biological support remains bounded by the separately recorded abstract or primary-body sections; identity resolution alone is not confirmation of every attached claim.; PMID:21239588: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were reviewed after the bulk eutils414 transport failure. Biological support remains bounded by the separately recorded abstract or primary-body sections; identity resolution alone is not confirmation of every attached claim.; PMID:22343294: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were reviewed after the bulk eutils414 transport failure. Biological support remains bounded by the separately recorded abstract or primary-body sections; identity resolution alone is not confirmation of every attached claim.; PMID:24747050: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were reviewed after the bulk eutils414 transport failure. Biological support remains bounded by the separately recorded abstract or primary-body sections; identity resolution alone is not confirmation of every attached claim.; PMID:27063436: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were reviewed after the bulk eutils414 transport failure. Biological support remains bounded by the separately recorded abstract or primary-body sections; identity resolution alone is not confirmation of every attached claim. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Fan2010 and Sampson2008 primary bodies were inaccessible through the retained challenge routes; only their complete native abstracts are certified. Bobik1997 was also read at native-abstract tier, not scanned-page tier.
- No raw microscopy pixels, supplementary datasets or new proteomics reanalysis were inspected. Exact body sections are enumerated in each evidence row; copied source receipts preserve original access times.
- PduN pentamer/vertex support in Wheatley2013 is a family inference from GrpN/EutN, not a PduN structure measured there. Yang2022 molecular contacts remain a proposed model based on genetic/imaging evidence.
- Shell-cohort CONDITIONAL labels do not establish every individual member’s formation requirement; PduA phenotypes must retain experimental context. The three CDE node xrefs are not an exhaustive whole-core inventory.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User expressly requests one review for every unreviewed record, including scientifically clean records.
- iModulonDB is not applicable to these complex identity, protein family, assembly and enzyme or transport claims.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T042547Z-propanediol-degradation-polyhedral-organelle-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-backed review of propanediol degradation polyhedral organelle
started_at: '2026-10-22T03:58:32Z'
finished_at: '2026-10-22T04:25:47Z'
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
summary: Two major corrections address PduU shell-class identity and the mechanistic
  cargo-binding partner; one minor correction supplies the verified PduM family. Other
  identity, taxon and metabolic claims are supported within stated limits.
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
  - path: data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml
    sha256: 6be0e75f5fb1ffa1081869af24522c1c2864d31090832eacb2f920b3dec3d443
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
- target_id: GO:0031472
  path: data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml
  label: propanediol degradation polyhedral organelle
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete target; no neighboring scientific-record verdict
    is imported. Exact authority, all current component/function/graph/source placements,
    taxonomic scope, formation semantics, history and discussions were reviewed.
  selection: Batch43 fixed strict path order, index 1; exactly one maintained target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0031472
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0031472
  command: just validate data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0031472
  command: just validate-strict data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml
    --out /private/tmp/cellstructure-batch43-20261022-u_vlughs/propanediol_degradation_polyhedral_organelle-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-proteins
  name: Focused native proteins
  status: passed
  required: true
  target_ids:
  - GO:0031472
  command: /private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml
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
  - GO:0031472
  command: /private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml
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
  - GO:0031472
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - micro43-go
  - micro43-tax2
  - micro43-tax99287
  - micro43-doi-1
  - micro43-doi-2
  - micro43-doi-3
  - micro43-doi-4
  - micro43-doi-5
  - micro43-doi-9
  - micro43-doi-10
  - micro43-doi-11
  - micro43-doi-12
  - micro43-doi-13
  - micro43-doi-14
  - micro43-doi6
  - micro43-pmid10498708
  - micro43-pmid11844753
  - micro43-pmid12923081
  - micro43-pmid21239588
  - micro43-pmid22343294
  - micro43-pmid24747050
  - micro43-pmid27063436
  - micro43-legacy-PMC7181861
  - micro43-legacy-PMC9132943
  - micro43-legacy-PMC3187188
  - micro43-body-PMC3318458
  - micro43-legacy-PMC134856
  - micro43-legacy-PMC180998
  - micro43-body-PMC3649267
  - micro43-legacy-PMC8217296
  - micro43-ipr-IPR030992
  - micro43-ipr-IPR044870
  - micro43-ipr-IPR009307
  - micro43-up-P0A1C7
  - micro43-up-H9L478
  - micro43-up-Q9XDN6
  - micro43-up-P37449
  - micro43-up-Q9XDM8
  - micro43-up-P0A1D1
  - micro43-up-Q9XDN3
  - micro43-up-Q9XDN4
  - micro43-up-P37450
  - micro43-up-O31041
  - micro43-up-O31042
  - micro43-pdu-unique
  - micro43-legacy-PMC2867708
  - micro43-legacy-PMC2293232
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0031472
  summary: '27 of 34 collected target identifiers returned OK. PMID:10498708: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were reviewed after the
    bulk eutils414 transport failure. Biological support remains bounded by the separately
    recorded abstract or primary-body sections; identity resolution alone is not confirmation
    of every attached claim.; PMID:11844753: UNREACHABLE; Exact native Europe PMC
    MED identifier, title and DOI were reviewed after the bulk eutils414 transport
    failure. Biological support remains bounded by the separately recorded abstract
    or primary-body sections; identity resolution alone is not confirmation of every
    attached claim.; PMID:12923081: UNREACHABLE; Exact native Europe PMC MED identifier,
    title and DOI were reviewed after the bulk eutils414 transport failure. Biological
    support remains bounded by the separately recorded abstract or primary-body sections;
    identity resolution alone is not confirmation of every attached claim.; PMID:21239588:
    UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were reviewed
    after the bulk eutils414 transport failure. Biological support remains bounded
    by the separately recorded abstract or primary-body sections; identity resolution
    alone is not confirmation of every attached claim.; PMID:22343294: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were reviewed after the
    bulk eutils414 transport failure. Biological support remains bounded by the separately
    recorded abstract or primary-body sections; identity resolution alone is not confirmation
    of every attached claim.; PMID:24747050: UNREACHABLE; Exact native Europe PMC
    MED identifier, title and DOI were reviewed after the bulk eutils414 transport
    failure. Biological support remains bounded by the separately recorded abstract
    or primary-body sections; identity resolution alone is not confirmation of every
    attached claim.; PMID:27063436: UNREACHABLE; Exact native Europe PMC MED identifier,
    title and DOI were reviewed after the bulk eutils414 transport failure. Biological
    support remains bounded by the separately recorded abstract or primary-body sections;
    identity resolution alone is not confirmation of every attached claim. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.'
  evidence_ids:
  - target-curies
  - micro43-pmid10498708
  - micro43-pmid11844753
  - micro43-pmid12923081
  - micro43-pmid21239588
  - micro43-pmid22343294
  - micro43-pmid24747050
  - micro43-pmid27063436
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0031472
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch43 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0031472
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch43 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0031472
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch43 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0031472
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch43 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0031472
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
    and current batch43 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml
  locator: Complete maintained YAML; all components, source notes, graphs, discussions
    and historical entries
  accessed_at: '2026-10-22T04:16:47Z'
  support: context_only
  summary: The entire maintained target was read; no scientific record was changed.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent; ComponentTypeEnum; EssentialityEnum; graph scopes
  accessed_at: '2026-10-22T04:16:47Z'
  support: context_only
  summary: Protein-family identity is distinct from an assembled complex. ESSENTIAL
    concerns failure of structure formation, not merely loss of catalytic or transport
    function.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Components; groundings; associated machinery and chaperone boundaries
  accessed_at: '2026-10-22T04:16:47Z'
  support: context_only
  summary: Components are taxon-agnostic molecular families/classes; exact family
    grounding is preferred when verified. Mature constituents and assembled-structure
    maintenance machinery differ from transient preassembly chaperones.
- evidence_id: micro43-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000148,GO:0003843,GO:0009277,GO:0031469,GO:0031472,GO:0042910,GO:0050215,GO:0051144,GO:0071970,GO:1990281
  locator: 'Requested entries GO0031472/0031469/0051144/0050215: complete names, definitions,
    typed children and active status.'
  accessed_at: '2026-10-22T04:09:03.496578Z'
  support: supports
  summary: GO0031472 exactly denotes the protein-coated propanediol-degradation organelle
    and is an is_a child of GO0031469. GO0051144 denotes propanediol catabolism; GO0050215
    is an enzyme activity, not a source-neutral PduCDE complex identity.
  snapshot_sha256: d40f3f203eaad9efb2ceba4c52209731a537cf62d0528a69af69d7b7d9c252f6
- evidence_id: micro43-tax2
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2
  locator: Complete taxId/scientificName/rank/lineage/otherNames.
  accessed_at: '2026-10-22T03:49:53.043115Z'
  support: supports
  summary: ENA taxId 2 identifies Bacteria at rank domain; aliases and lineage match
    the record. Identity alone is not prevalence or experimental-condition evidence.
  snapshot_sha256: 314bd7723b8dea04f1840809fb74e06c514664fba9c6a0619e8f12e2a6dceef1
- evidence_id: micro43-tax99287
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/99287
  locator: Complete taxId/scientificName/rank/lineage/otherNames.
  accessed_at: '2026-10-22T03:49:53.787584Z'
  support: supports
  summary: ENA taxId 99287 identifies Salmonella enterica subsp. enterica serovar
    Typhimurium str. LT2 at rank strain; aliases and lineage match the record. Identity
    alone is not prevalence or experimental-condition evidence.
  snapshot_sha256: a557fe03f1355059dd28424200acb7710f662743c0887e910746f8648fd83736
- evidence_id: micro43-doi-1
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1002%2Fpro.2246&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:09:03.496077Z'
  support: supports
  summary: 'Unique MED23456886: Bacterial microcompartment shells of diverse functional
    types possess pentameric vertex proteins. Authors/year/DOI and the complete native
    abstract were inspected. This row establishes bibliographic identity and abstract-level
    content only; detailed experiments require separately specified body evidence.'
  snapshot_sha256: 27dc16b4e2591c0198a4d7ef311229c97ef74a1c64d6acf3337da7e940e5f8d5
- evidence_id: micro43-doi-2
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fs41467-020-15888-4&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:09:03.496605Z'
  support: supports
  summary: 'Unique MED32332738: Decoding the stoichiometric composition and organisation
    of bacterial metabolosomes. Authors/year/DOI and the complete native abstract
    were inspected. This row establishes bibliographic identity and abstract-level
    content only; detailed experiments require separately specified body evidence.'
  snapshot_sha256: ce82234970fed9c6d0575476a508e99eb58f3a2c288878de3a283db242e41fd9
- evidence_id: micro43-doi-3
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fs41467-021-24126-4&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:09:03.496855Z'
  support: supports
  summary: 'Unique MED34155212: A catalog of the diversity and ubiquity of bacterial
    microcompartments. Authors/year/DOI and the complete native abstract were inspected.
    This row establishes bibliographic identity and abstract-level content only; detailed
    experiments require separately specified body evidence.'
  snapshot_sha256: 3e4a4be9776bb45c6e2970def4b0e599d8948517bd45106a4f554408ebc4f985
- evidence_id: micro43-doi-4
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fs41467-022-30608-w&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:09:03.496526Z'
  support: supports
  summary: 'Unique MED35614058: Biogenesis of a bacterial metabolosome for propanediol
    utilization. Authors/year/DOI and the complete native abstract were inspected.
    This row establishes bibliographic identity and abstract-level content only; detailed
    experiments require separately specified body evidence.'
  snapshot_sha256: 455060b724021e28eae0ac87a713c018e3c03bf8495578f443b6758237b75d81
- evidence_id: micro43-doi-5
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1073%2Fpnas.0913199107&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:09:04.295247Z'
  support: supports
  summary: 'Unique MED20308536: Short N-terminal sequences package proteins into bacterial
    microcompartments. Authors/year/DOI and the complete native abstract were inspected.
    This row establishes bibliographic identity and abstract-level content only; detailed
    experiments require separately specified body evidence.'
  snapshot_sha256: 20b3b42dbc595108f1bd96635d8db1ceb24ad5e817baa68ca6c8aca9692b1c10
- evidence_id: micro43-doi-9
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FJB.01925-07&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:09:04.429373Z'
  support: supports
  summary: 'Unique MED18296526: Microcompartments for B12-dependent 1,2-propanediol
    degradation provide protection from DNA and cellular damage by a reactive metabolic
    intermediate. Authors/year/DOI and the complete native abstract were inspected.
    This row establishes bibliographic identity and abstract-level content only; detailed
    experiments require separately specified body evidence.'
  snapshot_sha256: 7ce317bd1dff691cd3607d0a8b5c7fba528ddf4d9d7ee1a0e22c8f059ab7f85c
- evidence_id: micro43-doi-10
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FJB.05661-11&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:09:04.955397Z'
  support: supports
  summary: 'Unique MED21821773: The N-terminal region of the medium subunit (PduD)
    packages adenosylcobalamin-dependent diol dehydratase (PduCDE) into the Pdu microcompartment.
    Authors/year/DOI and the complete native abstract were inspected. This row establishes
    bibliographic identity and abstract-level content only; detailed experiments require
    separately specified body evidence.'
  snapshot_sha256: 0c71bba9b01d63c1c42d99d5840844a680702123402a77b1bc46d0b2f229d24d
- evidence_id: micro43-doi-11
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FJB.06529-11&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:09:05.031607Z'
  support: supports
  summary: 'Unique MED22343294: The PduM protein is a structural component of the
    microcompartments involved in coenzyme B(12)-dependent 1,2-propanediol degradation
    by Salmonella enterica. Authors/year/DOI and the complete native abstract were
    inspected. This row establishes bibliographic identity and abstract-level content
    only; detailed experiments require separately specified body evidence.'
  snapshot_sha256: ac28bc60707360259eb6697030075722e3df32caa7329b0127d6ae4b52a96e4d
- evidence_id: micro43-doi-12
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FJB.179.21.6633-6639.1997&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:09:05.158213Z'
  support: supports
  summary: 'Unique MED9352910: Propanediol utilization genes (pdu) of Salmonella typhimurium:
    three genes for the propanediol dehydratase. Authors/year/DOI and the complete
    native abstract were inspected. This row establishes bibliographic identity and
    abstract-level content only; detailed experiments require separately specified
    body evidence.'
  snapshot_sha256: b7215ecd2ea4d0b79c34989b14e06dd95aeff2210989477a6e10edcf7efc6d1f
- evidence_id: micro43-doi-13
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FJB.184.5.1253-1261.2002&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:09:05.164806Z'
  support: supports
  summary: 'Unique MED11844753: PduA is a shell protein of polyhedral organelles involved
    in coenzyme B(12)-dependent degradation of 1,2-propanediol in Salmonella enterica
    serovar typhimurium LT2. Authors/year/DOI and the complete native abstract were
    inspected. This row establishes bibliographic identity and abstract-level content
    only; detailed experiments require separately specified body evidence.'
  snapshot_sha256: ad138a828fede1b07038f0abf9eae9399e9f2f15e697c47c3f394de6c5fc67c0
- evidence_id: micro43-doi-14
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FJB.185.17.5086-5095.2003&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:09:05.181004Z'
  support: supports
  summary: 'Unique MED12923081: Protein content of polyhedral organelles involved
    in coenzyme B12-dependent degradation of 1,2-propanediol in Salmonella enterica
    serovar Typhimurium LT2. Authors/year/DOI and the complete native abstract were
    inspected. This row establishes bibliographic identity and abstract-level content
    only; detailed experiments require separately specified body evidence.'
  snapshot_sha256: 1c77eda653b08a3c077dd5ee5f5e02b7e0ed385b1cb7cd336a8b273563c288bb
- evidence_id: micro43-doi6
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1073/pnas.1207516109%22&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T03:49:45.287187Z'
  support: supports
  summary: 'Unique MED22927404: Interactions between the termini of lumen enzymes
    and shell proteins mediate enzyme encapsulation into bacterial microcompartments.
    Authors/year/DOI and the complete native abstract were inspected. This row establishes
    bibliographic identity and abstract-level content only; detailed experiments require
    separately specified body evidence.'
  snapshot_sha256: d5e58fe9bf17db4e9fb75eef26fb4b85e536764a8d02e4d0f95ca61c26d58274
- evidence_id: micro43-pmid10498708
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10498708+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:09:06.419716Z'
  support: supports
  summary: 'Unique MED10498708: The propanediol utilization (pdu) operon of Salmonella
    enterica serovar Typhimurium LT2 includes genes necessary for formation of polyhedral
    organelles involved in coenzyme B(12)-dependent 1, 2-propanediol degradation.
    Authors/year/DOI and the complete native abstract were inspected. This row establishes
    bibliographic identity and abstract-level content only; detailed experiments require
    separately specified body evidence.'
  snapshot_sha256: 7b0c3ed4f6f14054c611d26e019f45f47de45bb547814e18dc50c726294fa174
- evidence_id: micro43-pmid11844753
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11844753+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:09:06.467202Z'
  support: supports
  summary: 'Unique MED11844753: PduA is a shell protein of polyhedral organelles involved
    in coenzyme B(12)-dependent degradation of 1,2-propanediol in Salmonella enterica
    serovar typhimurium LT2. Authors/year/DOI and the complete native abstract were
    inspected. This row establishes bibliographic identity and abstract-level content
    only; detailed experiments require separately specified body evidence.'
  snapshot_sha256: 6a1f8071cd237876053c5ebfa07469201bb3524af1b6abfa7c628fee6cb9ef5d
- evidence_id: micro43-pmid12923081
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12923081+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:09:06.993608Z'
  support: supports
  summary: 'Unique MED12923081: Protein content of polyhedral organelles involved
    in coenzyme B12-dependent degradation of 1,2-propanediol in Salmonella enterica
    serovar Typhimurium LT2. Authors/year/DOI and the complete native abstract were
    inspected. This row establishes bibliographic identity and abstract-level content
    only; detailed experiments require separately specified body evidence.'
  snapshot_sha256: 8c6cb97680602dfd2f451235a9d8760948564e50e6069683df0cafcd01acf444
- evidence_id: micro43-pmid21239588
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21239588+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:09:07.084572Z'
  support: supports
  summary: 'Unique MED21239588: Genetic analysis of the protein shell of the microcompartments
    involved in coenzyme B12-dependent 1,2-propanediol degradation by Salmonella.
    Authors/year/DOI and the complete native abstract were inspected. This row establishes
    bibliographic identity and abstract-level content only; detailed experiments require
    separately specified body evidence.'
  snapshot_sha256: 719fc7d13ac32bc08322b53c954f3265243d1bd202d36c9fea1aca172068efb7
- evidence_id: micro43-pmid22343294
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22343294+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:09:07.178900Z'
  support: supports
  summary: 'Unique MED22343294: The PduM protein is a structural component of the
    microcompartments involved in coenzyme B(12)-dependent 1,2-propanediol degradation
    by Salmonella enterica. Authors/year/DOI and the complete native abstract were
    inspected. This row establishes bibliographic identity and abstract-level content
    only; detailed experiments require separately specified body evidence.'
  snapshot_sha256: a051a85f82a21ad0767674ab34ff7f9015402194aa7c33cf1e9ef68daee13198
- evidence_id: micro43-pmid24747050
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A24747050+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:09:07.286940Z'
  support: supports
  summary: 'Unique MED24747050: Alanine scanning mutagenesis identifies an asparagine-arginine-lysine
    triad essential to assembly of the shell of the Pdu microcompartment. Authors/year/DOI
    and the complete native abstract were inspected. This row establishes bibliographic
    identity and abstract-level content only; detailed experiments require separately
    specified body evidence.'
  snapshot_sha256: ad10be760cc57b8cf302605f5a59f230d6475a33a547df35006bf0f57f39063e
- evidence_id: micro43-pmid27063436
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A27063436%20AND%20SRC%3AMED&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T03:49:43.096342Z'
  support: supports
  summary: 'Unique MED27063436: Engineering formation of multiple recombinant Eut
    protein nanocompartments in E. coli. Authors/year/DOI and the complete native
    abstract were inspected. This row establishes bibliographic identity and abstract-level
    content only; detailed experiments require separately specified body evidence.'
  snapshot_sha256: c31546b5874f1edf0e471d32e6dcc2a871a6488bd984ee0b72c156a29e7d3944
- evidence_id: micro43-legacy-PMC7181861
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7181861/
  locator: 'Genuine primary HTML; all direct paragraphs of Sec1, Sec3, Sec4, Sec7,
    Sec9, Sec12 and Sec16 independently read. Class distinction: Sec4 paragraph 5.
    No figure pixels or supplementary data inspected.'
  accessed_at: '2026-10-22T04:10:07.438139Z'
  support: supports
  summary: Native LT2-derived Pdu organelles were isolated and quantitatively characterized.
    The article distinguishes trimeric PduT from hexameric PduU. Its abundance estimates
    assume 60 PduN copies; they are not an independent direct vertex count. Functional
    organelles were recovered from its pduA-deletion condition, unlike a blanket extrapolation
    from earlier loss phenotypes.
  snapshot_sha256: 1a8b6a0a797e29a5ffe5fbc93bb98075a66f7d1ba5218e54d4cabaa13584a79b
- evidence_id: micro43-legacy-PMC9132943
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9132943/
  locator: Genuine primary HTML; complete direct paragraphs in Sec1,3,4,5,6,8,9,12,16,21,22.
    Sec8 compares shell-first/cargo-first trajectories; Sec12 gives the model; Sec16/21/22
    provide strain, growth and imaging context. No figure pixels or supplements.
  accessed_at: '2026-10-22T04:10:07.698496Z'
  support: supports
  summary: LT2-derived tagged-protein imaging and deletion studies support independent
    shell/cargo assemblies and convergent pathways, with PduCDE driving core recruitment
    and a proposed PduM/PduB link. Colocalization/deletion phenotypes support the
    hierarchical model; they do not directly measure a purified PduM–PduD binding
    interaction. Imaging cultures and fluorescent fusions remain distinct from an
    unmodified organelle.
  snapshot_sha256: af5d24118f1e0e662b26c7df20bd534a28cbf94e9586ebf5e266f6a793cd0327
- evidence_id: micro43-legacy-PMC3187188
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3187188/
  locator: Genuine primary HTML; complete Results sec11–14 and Discussion sec15; Methods
    sec4/5/7/9 including Table1 strain context. Native source shows growth on succinate
    plus 1,2-PD and plasmid/IPTG constructs. No microscopy pixels or supplementary
    data.
  accessed_at: '2026-10-22T04:10:06.746811Z'
  support: supports
  summary: PduD N-terminal targeting is necessary/sufficient for packaging tested
    PduCDE and reporter constructs into LT2-derived MCPs. PduCDE deletion still permits
    MCP purification. Results and Discussion do not assign a BMC-T shell receptor.
    Intact-versus-broken immunoprecipitation supports internal packaging, while the
    Discussion distinguishes Salmonella and Citrobacter targeting observations.
  snapshot_sha256: ebe369816ef17eba6ca40039de07e87658f36736963949a2516a98c5f9ac4c0d
- evidence_id: micro43-body-PMC3318458
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/3318458/
  locator: 'Genuine primary HTML; complete sec3,7,12,16,17,20,21: strain/purification/EM
    methods, sequence analysis, deletion phenotype, MS/Western and Discussion. No
    raw figure pixels.'
  accessed_at: '2026-10-22T04:09:48.836961Z'
  support: supports
  summary: PduM is a native MCP structural constituent; deletion produces predominantly
    abnormal organelles rather than proving all formation impossible. The paper supports
    the PduM identity and structural role used by its exact InterPro family.
  snapshot_sha256: de9fc62766880c5704d9927dd3cdb51e17ba4f900b5f89359acecc56c086dbee
- evidence_id: micro43-legacy-PMC134856
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC134856/
  locator: 'Genuine primary HTML; sec3,19,20,21,22 completely read: growth, immunogold,
    DDH localization, deletion and complementation.'
  accessed_at: '2026-10-22T04:10:06.747377Z'
  support: supports
  summary: Immunogold identifies PduA at the shell and diol dehydratase internally
    in LT2-derived bodies; the tested pduA deletion disrupted normal organelle formation
    and complementation restored it. This experiment is not exported to every later
    strain/condition.
  snapshot_sha256: 0b4fdad12b3ac907de1b805cf28d218102853be5c782ee97426535a39e4b2c39
- evidence_id: micro43-legacy-PMC180998
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC180998/
  locator: Genuine primary HTML; sec3,15,18,21,22,24,25 completely read, including
    purification, EM, immunoblot, sequence/MS, abundance and Discussion.
  accessed_at: '2026-10-22T04:10:06.747597Z'
  support: supports
  summary: Purified LT2-derived organelles contain the reported shell and enzyme proteins,
    with native EM, Western, N-terminal and MS characterization. Cultures used succinate
    plus propanediol without B12; isolation is not itself a simultaneous physiological
    degradation-rate assay. PduA was directly established as shell protein, while
    several other placements were inferred in this 2003 study.
  snapshot_sha256: 6092bf2feed496f06fc5469638554e53ee993c37e9fb7ba6878a527fe8b257a8
- evidence_id: micro43-body-PMC3649267
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/3649267/
  locator: Genuine primary HTML reused with unchanged receipt; Abstract, Introduction
    sec1, all Results sec2 paragraphs1–8 and Methods sec4–7 independently read. No
    figure pixels.
  accessed_at: '2026-10-22T03:50:10.258988Z'
  support: supports
  summary: Primary crystallography directly examines Rhodospirillum GrpN and solution
    measurements examine E. coli EutN. PduN vertex assignment belongs to the homologous
    BMC-P inference, not a PduN crystal structure produced in this study. This distinction
    qualifies the record’s shorthand without rejecting the supported PduN role.
  snapshot_sha256: 22f974a401d2a905f82dce70ece1b7d6a774f66a9fb70220ce14b01c8f657709
- evidence_id: micro43-legacy-PMC8217296
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8217296/
  locator: Genuine primary HTML reused unchanged; Sec1 paragraph1, Sec3 paragraph2,
    Sec6 paragraph1, Sec8 paragraph4, Sec9 paragraphs1–2 independently read. Other
    body text is not certified by this row.
  accessed_at: '2026-10-22T03:50:50.267128Z'
  support: supports
  summary: The primary genomic catalog supports patchy PDU loci across bacterial lineages
    and conserved BMC shell classes. Locus calls are genomic potential, not microscopy-confirmed
    organelles or expression in every genome.
  snapshot_sha256: 3e1fe21fcf3ef391a378e1db66831851b09ac1e77e9c0483891831304e36b8f9
- evidence_id: micro43-ipr-IPR030992
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR030992/
  locator: Complete metadata accession/type/name/description/member databases/hierarchy
    and literature identity.
  accessed_at: '2026-10-22T04:09:49.407540Z'
  support: supports
  summary: IPR030992 is the exact Bacterial microcompartment assembly protein PduM
    family, with the PduM structural role and Sinha2012 reference. It resolves the
    currently label-only PduM component without substituting a single organism accession
    for a family.
  snapshot_sha256: 721b07d44b115a0cb2e00f4dd63ad061d2c2d0d0ab0d5957fd125752419020c9
- evidence_id: micro43-ipr-IPR044870
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR044870/
  locator: metadata accession/type/name, complete description and hierarchy; no claim
    that this domain is the exact PduU-only family.
  accessed_at: '2026-10-22T04:09:50.088520Z'
  support: supports
  summary: This circularly permuted BMC domain description distinguishes single-domain
    hexameric BMC-H from tandem-domain trimeric BMC-T. Circular permutation alone
    is not tandem architecture.
  snapshot_sha256: ea9d3be2d8b421f5fe80535a4a43a5e82b164a6761578d282c3bc7d962f4b62e
- evidence_id: micro43-ipr-IPR009307
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR009307/
  locator: metadata name/type/complete description and hierarchy.
  accessed_at: '2026-10-22T04:09:50.109292Z'
  support: supports
  summary: The EutS/PduU/CutR family spans more than the Pdu-specific subset and supports
    the circularly permuted PduU class; it is not an exact identity for every Pdu
    BMC-T protein.
  snapshot_sha256: ada00a2253578257905e3f5290867b3c9e7854eb38aa0d6f1b157c0eb5c461b1
- evidence_id: micro43-up-P0A1C7
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0A1C7.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references.
  accessed_at: '2026-10-22T04:09:08.554584Z'
  support: supports
  summary: P0A1C7 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['pduA'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 389718a823a5a31aeff4e117b5c2a3af6c95e95647de047e52a9c0745dd5f064
- evidence_id: micro43-up-H9L478
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/H9L478.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references.
  accessed_at: '2026-10-22T04:09:07.791474Z'
  support: supports
  summary: H9L478 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['pduJ'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 36333b80883cffc9e16691c1a00cb20786510cc6827b59b953e701172ea78c53
- evidence_id: micro43-up-Q9XDN6
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q9XDN6.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references.
  accessed_at: '2026-10-22T04:09:10.652838Z'
  support: supports
  summary: Q9XDN6 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['pduK'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 7078fab3c550ef1d2bef2004939cec6072992dacb1c6d7e9f82907f499577eb5
- evidence_id: micro43-up-P37449
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P37449.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references.
  accessed_at: '2026-10-22T04:09:09.352766Z'
  support: supports
  summary: P37449 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['pduB'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 4c43b72065c16c776a492d6ffafacc3bf9348b1bd54bd5164b67a16a09980ed0
- evidence_id: micro43-up-Q9XDM8
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q9XDM8.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references.
  accessed_at: '2026-10-22T04:09:10.232357Z'
  support: supports
  summary: Q9XDM8 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['pduT'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 805112b48c5200721328c2a87ee11a81aa36e9c9864afc22e0262ef5f677cf1c
- evidence_id: micro43-up-P0A1D1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0A1D1.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references.
  accessed_at: '2026-10-22T04:09:08.951264Z'
  support: supports
  summary: P0A1D1 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['pduU'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 77369d0ed03be3e2c5b5d655dc9451a709e79dea816a98fa564f6d026e7d3796
- evidence_id: micro43-up-Q9XDN3
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q9XDN3.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references.
  accessed_at: '2026-10-22T04:09:10.447834Z'
  support: supports
  summary: Q9XDN3 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['pduN'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 0b1f46044a456550bd908272a2b76536d36d59146da0295d7113948452fe2907
- evidence_id: micro43-up-Q9XDN4
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q9XDN4.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references.
  accessed_at: '2026-10-22T04:09:10.485541Z'
  support: supports
  summary: Q9XDN4 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['pduM'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 4fe5c228010e17183e28a56db12e6eedaaf515089cfe4e7458ab754c6a5a56d6
- evidence_id: micro43-up-P37450
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P37450.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references.
  accessed_at: '2026-10-22T04:09:09.477938Z'
  support: supports
  summary: P37450 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['pduC'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: c53413b5403dc092d117c68da0b59e6dfaaebfae9e3e1c50c7fb0d9fe2a58ade
- evidence_id: micro43-up-O31041
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/O31041.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references.
  accessed_at: '2026-10-22T04:09:07.928613Z'
  support: supports
  summary: O31041 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['pduD'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 269ad4332be19430e7c7584d14764c257523f85397d87cf421cf45e7e63bef6d
- evidence_id: micro43-up-O31042
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/O31042.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references.
  accessed_at: '2026-10-22T04:09:08.304104Z'
  support: supports
  summary: O31042 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['pduE'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 069d7e39a2dc26608992b9ae88e8ec89578fc94c513543471f83ce31becb1f5d
- evidence_id: micro43-pdu-unique
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A99287+AND+%28gene_exact%3ApduA+OR+gene_exact%3ApduB+OR+gene_exact%3ApduC+OR+gene_exact%3ApduD+OR+gene_exact%3ApduE+OR+gene_exact%3ApduJ+OR+gene_exact%3ApduK+OR+gene_exact%3ApduM+OR+gene_exact%3ApduN+OR+gene_exact%3ApduT+OR+gene_exact%3ApduU%29&format=json&size=100&fields=accession%2Cid%2Cgene_names%2Corganism_id%2Cprotein_name
  locator: Complete public UniProt results; exact reviewed/taxon/gene query retained
    in source URL; result count below page size 100.
  accessed_at: '2026-10-22T04:14:23.968243Z'
  support: supports
  summary: The bounded reviewed LT2 query returns exactly the eleven declared gene
    identities, one accession per requested symbol. This verifies current resolution,
    not the historical retrieval date or every localization experiment.
  snapshot_sha256: 66d3f6116ebf246ac24a96145d1064bc4aca8a3abbd672153656609262a6fdad
  search_scope: reviewed:true AND organism_id:99287 AND exact pduA/B/C/D/E/J/K/M/N/T/U
    genes; all eleven results inspected. Remote native query only; gitignored-file
    inclusion is not applicable, and this is not a local absence search.
- evidence_id: micro43-legacy-PMC2867708
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2867708/
  locator: Exact retained response bytes; access/readability evidence only, not primary
    article results.
  accessed_at: '2026-10-22T04:10:08.065095Z'
  support: context_only
  summary: 'HTTP 200: challenge HTML rather than Fan2010 article body; complete native
    MED abstract was readable separately.'
  snapshot_sha256: cb89e08fa51b5201238fd8d97ee8d0c28a25a34db34d915c982cf0a31a2d66ea
- evidence_id: micro43-legacy-PMC2293232
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2293232/
  locator: Exact retained response bytes; access/readability evidence only, not primary
    article results.
  accessed_at: '2026-10-22T04:10:08.555952Z'
  support: context_only
  summary: 'HTTP 200: challenge HTML rather than Sampson2008 article body; complete
    native MED abstract supports the stated protective function at abstract tier.'
  snapshot_sha256: 48cceae8009f0a4c8c8b50b89a16b531c3d30086ecc83d4d89a49224c9c7365e
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:58:33Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml'
  snapshot_sha256: 32aabf55ac88d6d9294cd73378a6646d32020f85845c59f32c1eba8e2d8199bb
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml
    --out /private/tmp/cellstructure-batch43-20261022-u_vlughs/propanediol_degradation_polyhedral_organelle-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:58:34Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml\
    \ --out /private/tmp/cellstructure-batch43-20261022-u_vlughs/propanediol_degradation_polyhedral_organelle-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch43-20261022-u_vlughs/propanediol_degradation_polyhedral_organelle-strict.tsv"
  snapshot_sha256: b11c9c381e7c1e4be98003a736802a7bfb23e86a33d66c7a36c6be7558fbf49a
- evidence_id: native-proteins
  kind: validation
  reference: /private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml
  locator: Complete read-only focused native proteins log
  accessed_at: '2026-10-22T04:09:27.058093Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml
  locator: Complete read-only focused native graphs log
  accessed_at: '2026-10-22T04:09:27.486743Z'
  support: supports
  summary: "data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml\
    \  (GO:0031472)\n  pdu_shell_cargo_convergent_biogenesis\tpdu_bmc_h_shell_proteins\t\
    COVERED\t->pdu_bmc_h_shell_proteins (UniProtKB:P0A1C7, UniProtKB:H9L478, UniProtKB:Q9XDN6)\n\
    \  pdu_shell_cargo_convergent_biogenesis\tpdu_bmc_t_shell_proteins\tCOVERED\t\
    ->pdu_bmc_t_shell_proteins (UniProtKB:P37449, UniProtKB:Q9XDM8, UniProtKB:P0A1D1)\n\
    \  pdu_shell_cargo_convergent_biogenesis\tpdun_vertex_shell_protein\tCOVERED\t\
    ->pdun_vertex_shell_protein (UniProtKB:Q9XDN3)\n  pdu_shell_cargo_convergent_biogenesis\t\
    pducde_diol_dehydratase\tCOVERED\t->pducde_diol_dehydratase (UniProtKB:P37450,\
    \ UniProtKB:O31041, UniProtKB:O31042)\n  pdu_shell_cargo_convergent_biogenesis\t\
    pdu_lumen_enzyme_core\tUNANCHORED_WITH_UNIPROT\tPdu lumen enzyme core (UniProtKB:P37450,\
    \ UniProtKB:O31041, UniProtKB:O31042)\n  pdu_shell_cargo_convergent_biogenesis\t\
    pdum_structural_protein\tCOVERED\t->pdum_structural_protein (UniProtKB:Q9XDN4)\n\
    \ncausal_graphs GENE_OR_PROTEIN node summary:\n     5  COVERED               \
    \    component_ref target holds protein_examples covering all declared symbols\n\
    \     1  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  PARTIAL_EXAMPLES          component_ref target holds\
    \ protein_examples but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES\
    \   component_ref target declares gene_symbols but holds no protein_examples\n\
    \     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols\
    \ and holds no protein_examples\n     0  DANGLING_COMPONENT_REF    component_ref\
    \ names a component_id that does not exist on the record\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     6\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: b89131a25336ff922cc4345e348943880ecafc1cb064b4867ac156090e0eaab0
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml;
    native collect() exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '27 of 34 collected target identifiers returned OK. PMID:10498708: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were reviewed after the
    bulk eutils414 transport failure. Biological support remains bounded by the separately
    recorded abstract or primary-body sections; identity resolution alone is not confirmation
    of every attached claim.; PMID:11844753: UNREACHABLE; Exact native Europe PMC
    MED identifier, title and DOI were reviewed after the bulk eutils414 transport
    failure. Biological support remains bounded by the separately recorded abstract
    or primary-body sections; identity resolution alone is not confirmation of every
    attached claim.; PMID:12923081: UNREACHABLE; Exact native Europe PMC MED identifier,
    title and DOI were reviewed after the bulk eutils414 transport failure. Biological
    support remains bounded by the separately recorded abstract or primary-body sections;
    identity resolution alone is not confirmation of every attached claim.; PMID:21239588:
    UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were reviewed
    after the bulk eutils414 transport failure. Biological support remains bounded
    by the separately recorded abstract or primary-body sections; identity resolution
    alone is not confirmation of every attached claim.; PMID:22343294: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were reviewed after the
    bulk eutils414 transport failure. Biological support remains bounded by the separately
    recorded abstract or primary-body sections; identity resolution alone is not confirmation
    of every attached claim.; PMID:24747050: UNREACHABLE; Exact native Europe PMC
    MED identifier, title and DOI were reviewed after the bulk eutils414 transport
    failure. Biological support remains bounded by the separately recorded abstract
    or primary-body sections; identity resolution alone is not confirmation of every
    attached claim.; PMID:27063436: UNREACHABLE; Exact native Europe PMC MED identifier,
    title and DOI were reviewed after the bulk eutils414 transport failure. Biological
    support remains bounded by the separately recorded abstract or primary-body sections;
    identity resolution alone is not confirmation of every attached claim. Native
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
  topic: Pdu identity, hierarchy and metabolic boundary
  outcome: supported
  target_ids:
  - GO:0031472
  summary: Exact GO identity, protein-shell class and BMC parent are supported; the
    activity GO is correctly withheld as a PduCDE-complex grounding.
  evidence_ids:
  - record
  - micro43-go
- assessment_id: composition
  area: grounding
  topic: Protein cohorts and exact family gaps
  outcome: concern
  target_ids:
  - GO:0031472
  summary: Membership and native structural/cargo roles are supported, but PduU is
    a hexameric BMC-H member placed in the BMC-T cohort. PduM has a verified exact
    family available. Other narrower Pdu-specific cohorts are not forced into broad
    domain families.
  evidence_ids:
  - record
  - curation
  - micro43-legacy-PMC7181861
  - micro43-legacy-PMC9132943
  - micro43-legacy-PMC180998
  - micro43-ipr-IPR044870
  - micro43-ipr-IPR009307
  - micro43-ipr-IPR030992
- assessment_id: necessity
  area: grounding
  topic: Formation versus catalysis
  outcome: unknown
  target_ids:
  - GO:0031472
  summary: PduCDE DISPENSABLE is supported by recovered MCPs from its deletion background.
    UNKNOWN PduM/PduN avoids overstating necessity. CONDITIONAL shell-cohort labels
    lack a complete condition-by-member necessity matrix; PduA phenotypes differ between
    the cited 2002 and 2020 contexts. No individual member is inferred essential from
    intact structure.
  evidence_ids:
  - record
  - schema
  - micro43-legacy-PMC3187188
  - micro43-body-PMC3318458
  - micro43-legacy-PMC134856
  - micro43-legacy-PMC7181861
- assessment_id: proteins
  area: grounding
  topic: Exact native gene identities and annotation provenance
  outcome: supported
  target_ids:
  - GO:0031472
  summary: All eleven accessions, LT2 taxon, reviewed status and gene aliases agree,
    including the native PduU BMC-H name. Localization-evidence notes match native
    citation joins. Held2016 attribution is treated as native annotation provenance;
    its recombinant Eut work does not independently establish every native Pdu placement.
  evidence_ids:
  - record
  - micro43-pdu-unique
  - micro43-up-P0A1C7
  - micro43-up-H9L478
  - micro43-up-Q9XDN6
  - micro43-up-P37449
  - micro43-up-Q9XDM8
  - micro43-up-P0A1D1
  - micro43-up-Q9XDN3
  - micro43-up-Q9XDN4
  - micro43-up-P37450
  - micro43-up-O31041
  - micro43-up-O31042
  - micro43-pmid27063436
- assessment_id: scope
  area: scope
  topic: Taxa and induction contexts
  outcome: supported
  target_ids:
  - GO:0031472
  summary: VARIABLE Bacteria and the native LT2 canonical example are supported. Genomic
    potential, induced laboratory organelles, deletion strains and fusion reporters
    remain distinct.
  evidence_ids:
  - record
  - micro43-legacy-PMC8217296
  - micro43-legacy-PMC180998
  - micro43-legacy-PMC9132943
  - micro43-tax2
  - micro43-tax99287
- assessment_id: functions
  area: evidence
  topic: Propanediol catalysis and aldehyde protection
  outcome: supported
  target_ids:
  - GO:0031472
  summary: The retained native abstracts and direct studies support PduCDE chemistry,
    compartmentalization and protection from propionaldehyde-associated damage. Sampson2008
    is abstract-only in this review; detailed damage assays were not inspected.
  evidence_ids:
  - record
  - micro43-go
  - micro43-doi-9
  - micro43-doi-12
  - micro43-legacy-PMC134856
  - micro43-legacy-PMC180998
- assessment_id: graph
  area: graph
  topic: Convergent model and unsupported binding partner
  outcome: concern
  target_ids:
  - GO:0031472
  summary: The Yang2022 convergence and proposed PduM/PduB bridge are accurately model-scoped;
    PduN geometry is a homologous-family inference supported by later native context.
    The separate enzyme-core→BMC-T binding edge assigns a specific receptor class
    beyond Fan2010/2011 targeting evidence. Fan2012’s directly reported PduP receptor
    is PduA/PduJ, not a general BMC-T cohort. Three CDE xrefs are examples within
    the broader core and are not treated as an exhaustive equality.
  evidence_ids:
  - record
  - micro43-legacy-PMC9132943
  - micro43-legacy-PMC3187188
  - micro43-body-PMC3649267
  - micro43-legacy-PMC7181861
  - micro43-doi-5
  - micro43-doi6
- assessment_id: coverage
  area: completeness
  topic: Whole-record coverage and source limits
  outcome: supported
  target_ids:
  - GO:0031472
  summary: All current fields, two synonyms, protein examples, graph, source notes
    and history were reviewed. No maintained image or verbatim snippet is present.
    Optional accessory enzymes and family candidates broader than the exact curated
    subsets do not create automatic findings.
  evidence_ids:
  - record
  - micro43-go
  - micro43-legacy-PMC8217296
  - micro43-ipr-IPR030992
  - micro43-ipr-IPR009307
findings:
- finding_id: F1
  issue_key: pdu-pduu-shell-class
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Separate PduU from the tandem-domain BMC-T cohort
  description: The component explicitly declares PduB, PduT and PduU to be BMC-T proteins
    and treats circular permutation as sufficient for that class. The cited quantitative
    study distinguishes trimeric PduT from hexameric PduU; native PduU and domain
    metadata identify the single-domain BMC-H architecture. Correct organelle membership
    does not repair the wrong molecular subclass.
  target_ids:
  - GO:0031472
  field_paths:
  - components[1].label
  - components[1].gene_symbols
  - components[1].role
  - components[1].grounding_notes
  - causal_graphs[0].nodes[1]
  evidence_ids:
  - record
  - micro43-legacy-PMC7181861
  - micro43-ipr-IPR044870
  - micro43-up-P0A1D1
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml
    role: maintained scientific record
  rule_id: Exact source scope, protein grounding and formation-specific essentiality
  native_severity: major
  normalization_reason: This is a material protein-class assignment error propagated
    into a mechanistic actor, not an optional annotation or terminology preference.
- finding_id: F2
  issue_key: pdu-targeting-bmc-t-partner
  category: graph
  severity: major
  status: open
  certainty: confirmed
  title: Do not infer a general BMC-T receptor from cargo-targeting experiments
  description: The MECHANISTIC edge directly binds the lumen enzyme core to the BMC-T
    cohort. Fan2010/2011 establish terminal-sequence targeting, not that specific
    receptor class. The separately verified Fan2012 abstract reports PduP binding
    to PduA/PduJ, and the Yang2022 PduM/PduB model is a different, explicitly qualified
    coupling mechanism. The existing edge conflates these cargo and interaction contexts.
  target_ids:
  - GO:0031472
  field_paths:
  - causal_graphs[0].edges[2]
  evidence_ids:
  - record
  - micro43-legacy-PMC3187188
  - micro43-doi-5
  - micro43-doi6
  - micro43-legacy-PMC9132943
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml
    role: maintained scientific record
  rule_id: Exact source scope, protein grounding and formation-specific essentiality
  native_severity: major
  normalization_reason: The endpoint and binding predicate assert a specific causal
    molecular relation unsupported by their cited experiments; generic encapsulation
    remains correct. This is independent of the PduU classification correction.
- finding_id: F3
  issue_key: pdu-pdum-family-grounding
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground PduM to its verified protein family
  description: The label-only PduM component now has an exact source-neutral family,
    IPR030992, whose native description and citation match the curated structural
    protein. This is a current resolvable gap, not a claim that a historical search
    was dishonest.
  target_ids:
  - GO:0031472
  field_paths:
  - components[3].grounding
  - components[3].grounding_status
  - components[3].grounding_notes
  evidence_ids:
  - record
  - curation
  - micro43-ipr-IPR030992
  - micro43-body-PMC3318458
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml
    role: maintained scientific record
  rule_id: Exact source scope, protein grounding and formation-specific essentiality
  native_severity: minor
  normalization_reason: Identity and biological role are correct; only the exact available
    family grounding remains unresolved.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0031472
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml
    role: maintained scientific record
  description: In authorized curation, move or separately represent PduU in its supported
    single-domain circularly permuted BMC-H class. Retain PduB/PduT in the properly
    scoped BMC-T cohort and update dependent node membership without losing supported
    PduU occurrence.
  acceptance_checks:
  - Preserve exact supported identity, experimental organism and native versus recombinant
    context.
  - Attach source-specific evidence to each changed claim and retain historical provenance.
  - Native schema, strict, CURIE, protein and graph checks pass as applicable.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0031472
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml
    role: maintained scientific record
  description: Replace the edge with the directly supported targeting relation or
    a specifically identified, source-qualified cargo/receptor interaction. If representing
    PduP–PduA/PduJ, preserve that distinct cargo identity and cite its actual interaction
    study; do not reassign PduD/CDE binding merely by analogy.
  acceptance_checks:
  - Preserve exact supported identity, experimental organism and native versus recombinant
    context.
  - Attach source-specific evidence to each changed claim and retain historical provenance.
  - Native schema, strict, CURIE, protein and graph checks pass as applicable.
- action_id: A3
  finding_ids:
  - F3
  target_ids:
  - GO:0031472
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml
    role: maintained scientific record
  description: Use the verified PduM family grounding and reconcile the label-only
    note, preserving organism-specific examples and the model-qualified assembly role.
  acceptance_checks:
  - Preserve exact supported identity, experimental organism and native versus recombinant
    context.
  - Attach source-specific evidence to each changed claim and retain historical provenance.
  - Native schema, strict, CURIE, protein and graph checks pass as applicable.
limitations:
- Fan2010 and Sampson2008 primary bodies were inaccessible through the retained challenge
  routes; only their complete native abstracts are certified. Bobik1997 was also read
  at native-abstract tier, not scanned-page tier.
- No raw microscopy pixels, supplementary datasets or new proteomics reanalysis were
  inspected. Exact body sections are enumerated in each evidence row; copied source
  receipts preserve original access times.
- PduN pentamer/vertex support in Wheatley2013 is a family inference from GrpN/EutN,
  not a PduN structure measured there. Yang2022 molecular contacts remain a proposed
  model based on genetic/imaging evidence.
- Shell-cohort CONDITIONAL labels do not establish every individual member’s formation
  requirement; PduA phenotypes must retain experimental context. The three CDE node
  xrefs are not an exhaustive whole-core inventory.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User expressly requests one review for every unreviewed record, including scientifically
  clean records.
- iModulonDB is not applicable to these complex identity, protein family, assembly
  and enzyme or transport claims.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
