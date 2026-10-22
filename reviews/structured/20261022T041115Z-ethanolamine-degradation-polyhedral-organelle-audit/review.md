# Source-backed review of ethanolamine degradation polyhedral organelle

- Review: 20261022T041115Z-ethanolamine-degradation-polyhedral-organelle-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T03:47:05Z
- Finished UTC: 2026-10-22T04:11:15Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Two minor corrections address attached-study attribution and reporter-to-native-cargo graph scope. Exact identity, qualified shell composition, protein identities, variable distribution and the genetic confinement model are supported.

## Scope And Provenance

One complete target, with the other three BMC/carboxysome/shell/Eut records frozen as boundary context. Exact authority, all current component/function/graph/source placements, taxonomic scope, formation semantics, history and discussions were reviewed.

Selection: Batch42 fixed strict path order, index 10; exactly one maintained target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0031471 | data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml | maintained | ethanolamine degradation polyhedral organelle |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0031471 | Focused validator passed. |
| Focused native strict | passed | True | GO:0031471 | Focused validator passed. |
| Focused native proteins | passed | True | GO:0031471 | Read-only native check passed; claim-level protein/edge support evaluated separately. |
| Focused native graphs | passed | True | GO:0031471 | Read-only native check passed; claim-level protein/edge support evaluated separately. |
| Claim-level scientific review | passed | True | GO:0031471 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0031471 | 22 of 25 collected target identifiers returned OK. PMID:22428024: UNREACHABLE; Exact native MED identity/title/DOI and returned PMC field were reviewed after bulk eutils414 transport failure. Resolving an identifier does not certify attached biology; the unrelated Ras PMID20080631 remains an explicit wrong-source finding.; PMID:27063436: UNREACHABLE; Exact native MED identity/title/DOI and returned PMC field were reviewed after bulk eutils414 transport failure. Resolving an identifier does not certify attached biology; the unrelated Ras PMID20080631 remains an explicit wrong-source finding.; PMID:27450681: UNREACHABLE; Exact native MED identity/title/DOI and returned PMC field were reviewed after bulk eutils414 transport failure. Resolving an identifier does not certify attached biology; the unrelated Ras PMID20080631 remains an explicit wrong-source finding. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0031471 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0031471 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0031471 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0031471 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0031471 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact ethanolamine organelle class

identity: supported. Targets: GO:0031471.

The GO identity/definition, BMC parent and Eut synonyms are supported; this is a protein shell organelle, not a lipid membrane or merely an operon.

### Shell membership and family scopes

grounding: supported. Targets: GO:0031471.

The two shell cohorts and their oligomeric roles are supported at specified native/recombinant tiers. Exact Eut-only family withholding is justified; optional exhaustive enzyme or assembly-factor inventory is not required.

### Formation labels honestly unresolved

grounding: unknown. Targets: GO:0031471.

Both component rows use UNKNOWN. Native mutant and recombinant sufficiency results do not imply universal individual-protein formation necessity; EutQ multiplicity effects are not obligatory formation.

### Accession and localization qualifications

grounding: concern. Targets: GO:0031471.

All current example/graph accessions match reviewed Salmonella LT2 proteins and genes. EutN identity alone is not membership proof; its native location annotation is by similarity. EutB/C interior location remains probable/model dependent rather than directly established by reporter fusion.

### Variable Bacteria and experimental strains

scope: supported. Targets: GO:0031471.

Native taxon identities match. LT2 native cultures, E. coli recombinant expression and isolated E. coli shell-protein studies are distinguished. VARIABLE Bacteria is tied to the genomic catalog, not extrapolated from one host.

### Chemical routing and confinement

evidence: supported. Targets: GO:0031471.

The process identity and genetic cofactor/aldehyde model are supported. Notes correctly describe genetic evidence/model rather than direct permeability assays. Acetaldehyde restriction is incomplete and cofactor topology is mechanistic inference.

### Cargo targeting and source placement

graph: concern. Targets: GO:0031471.

Recombinant shell construction, EutC targeting and in-vitro EutQ–EutM binding are supported. Fan2012 is the wrong attached study for EutC/EutE–EutS binding; relevant Quin2016 occurs elsewhere. The lumen-enzyme node should not convert fused-reporter results into settled native EutB/C interior topology.

### Full record and canonical source scope

completeness: concern. Targets: GO:0031471.

All fields/history/graph annotations were read; no images or verbatim snippets occur. The canonical note combines Kofoid operon mapping and Huseby cofactor work but attaches only Kofoid. This is bounded provenance, not rejection of the Salmonella example.

## Findings

### F1: Attach the correct study to cargo binding and cofactor claims

minor / open / confirmed; issue key: eut-source-claim-placement.

Fan2012 directly studies PduP binding PduA/PduJ in the propanediol compartment, not EutC/EutE binding EutS. Relevant Quin2016 is already cited elsewhere and supports that biology. The canonical note also attributes private cofactor recycling to Huseby/Roth but attaches only Kofoid1999 operon mapping.

### F2: Distinguish reporter cargo from unsettled native EutBC topology

minor / open / confirmed; issue key: eut-reporter-native-cargo-graph-scope.

The Eut lumen enzymes node specifically xrefs EutB/EutC, while its incoming Choudhary edge demonstrates routing fused reporters by the EutC N-terminal peptide. The cited Huseby model places EutBC outside/on the shell and says localization was not tested; native UniProt interior annotation is probable. Reporter encapsulation does not settle native EutBC topology.

## Recommended Actions And Acceptance Checks

### A1

Attach Quin2016 to specific EutC/EutE–EutS binding and Huseby/Roth to cofactor modelling, retaining Kofoid for operon identity and each primary experimental context.

- Preserve exact supported identity, experimental organism and native versus recombinant context.
- Attach source-specific evidence to each changed claim and retain historical provenance.
- Native schema, strict, CURIE, protein and graph checks pass as applicable.

### A2

Represent demonstrated fused-reporter cargo or qualify the native-enzyme node and preserve competing models; do not claim EutBC is proven exterior or universally interior.

- Preserve exact supported identity, experimental organism and native versus recombinant context.
- Attach source-specific evidence to each changed claim and retain historical provenance.
- Native schema, strict, CURIE, protein and graph checks pass as applicable.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml; Complete maintained YAML; all components, source notes, graphs, discussions and historical entries | context_only | The entire maintained target was read; no scientific record was changed. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent; ComponentTypeEnum; EssentialityEnum; graph scopes | context_only | Protein-family identity is distinct from an assembled complex. ESSENTIAL concerns failure of structure formation, not loss of catalytic function or ambient-CO2 growth. |
| curation | docs/CURATION.md; Components; groundings; associated machinery and chaperone boundaries | context_only | Components are taxon-agnostic molecular families/classes; exact family grounding is preferred when verified. Mature constituents and assembled-structure maintenance machinery differ from transient preassembly chaperones. |
| neighbor-bacterial_microcompartment | data/structures/microcompartment/bacterial_microcompartment.yaml; Complete frozen BMC/carboxysome/shell/Eut boundary neighbor | context_only | Frozen neighboring record read for class, family and boundary context; its scientific verdict is not imported. |
| neighbor-carboxysome | data/structures/microcompartment/carboxysome.yaml; Complete frozen BMC/carboxysome/shell/Eut boundary neighbor | context_only | Frozen neighboring record read for class, family and boundary context; its scientific verdict is not imported. |
| neighbor-carboxysome_shell | data/structures/microcompartment/carboxysome_shell.yaml; Complete frozen BMC/carboxysome/shell/Eut boundary neighbor | context_only | Frozen neighboring record read for class, family and boundary context; its scientific verdict is not imported. |
| micro42-doi0 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1002/pro.2246%22&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED23456886: Bacterial microcompartment shells of diverse functional types possess pentameric vertex proteins. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro42-doi4 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038/s41467-021-24126-4%22&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED34155212: A catalog of the diversity and ubiquity of bacterial microcompartments. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro42-doi5 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038/srep24359%22&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED27063436: Engineering formation of multiple recombinant Eut protein nanocompartments in E. coli. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro42-doi6 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1073/pnas.1207516109%22&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED22927404: Interactions between the termini of lumen enzymes and shell proteins mediate enzyme encapsulation into bacterial microcompartments. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro42-doi8 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1128/JB.00652-10%22&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED20851901: Crystallographic insights into the pore structures and mechanisms of the EutL and EutM shell proteins of the ethanolamine-utilizing microcompartment of Escherichia coli. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro42-doi9 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1128/JB.02179-12%22&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED23585538: Evidence that a metabolic microcompartment contains and recycles private cofactor pools. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro42-doi11 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1128/jb.181.17.5317-5329.1999%22&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED10464203: The 17-gene ethanolamine (eut) operon of Salmonella typhimurium encodes five homologues of carboxysome shell proteins. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro42-doi12 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1128/mbio.00066-18%22&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED29463652: Ethanolamine Utilization in Bacteria. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro42-doi16 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1371/journal.pone.0033342%22&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED22428024: Engineered protein nano-compartments for targeted enzyme localization. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro42-pmid22428024 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22428024%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED22428024: Engineered protein nano-compartments for targeted enzyme localization. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro42-pmid27063436 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A27063436%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED27063436: Engineering formation of multiple recombinant Eut protein nanocompartments in E. coli. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro42-pmid27450681 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A27450681%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED27450681: Encapsulation of multiple cargo proteins within recombinant Eut nanocompartments. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro42-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0015977,GO:0031469,GO:0031470,GO:0031471,GO:0043232,GO:0046336; Exact GO0031471/GO0031469/GO0046336 identity, definition, obsolescence and typed relations. | supports | Native GO0031471 defines the protein-coated ethanolamine-catabolic organelle and its BMC parent; GO0046336 is the ethanolamine catabolic process. The record definition and hierarchy match these exact entries. |
| micro42-tax2 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2; Complete taxId/scientificName/rank/lineage/otherNames. | supports | ENA taxId 2 identifies Bacteria at rank domain; aliases and lineage match the record. Identity alone is not prevalence or experimental-condition evidence. |
| micro42-tax99287 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/99287; Complete taxId/scientificName/rank/lineage/otherNames. | supports | ENA taxId 99287 identifies Salmonella enterica subsp. enterica serovar Typhimurium str. LT2 at rank strain; aliases and lineage match the record. Identity alone is not prevalence or experimental-condition evidence. |
| micro42-up-P0A1C9 | https://rest.uniprot.org/uniprotkb/P0A1C9.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. | supports | P0A1C9 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['eutL']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro42-up-P19264 | https://rest.uniprot.org/uniprotkb/P19264.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. | supports | P19264 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['eutB']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro42-up-P19265 | https://rest.uniprot.org/uniprotkb/P19265.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. | supports | P19265 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['eutC']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro42-up-P41791 | https://rest.uniprot.org/uniprotkb/P41791.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. | supports | P41791 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['eutM']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro42-up-P41792 | https://rest.uniprot.org/uniprotkb/P41792.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. | supports | P41792 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['eutN']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro42-up-Q9ZFU8 | https://rest.uniprot.org/uniprotkb/Q9ZFU8.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. | supports | Q9ZFU8 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['eutK']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro42-up-Q9ZFV5 | https://rest.uniprot.org/uniprotkb/Q9ZFV5.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. | supports | Q9ZFV5 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['eutQ']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro42-up-Q9ZFV7 | https://rest.uniprot.org/uniprotkb/Q9ZFV7.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. | supports | Q9ZFV7 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['eutS']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro42-xml-PMC4827028 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4827028/fullTextXML; Genuine primary JATS: Results sec3/sec4/sec6/sec7, Discussion sec8, Methods sec10–15. Figure-caption information in these sections; no supplementary movies/data or raw-pixel reanalysis. | supports | Salmonella shell proteins form recombinant E. coli C2566 nanocompartments; EutQ alters number and interacts with EutM in vitro. Native LT2 deletion and heterologous constructs are distinct. EutQ-mediated nucleation and specific in-vivo binding remain hypotheses; EutQ is not absolutely required for a single recombinant shell. |
| micro42-xml-PMC3299773 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3299773/fullTextXML; Genuine primary JATS: Results s2b/s2c/s2d/s2e/s2h; Methods s4a/s4c/s4f; complete native abstract. Supplements and movies not independently read. | supports | The study directly demonstrates EutC1–19-mediated reporter targeting in native Salmonella and recombinant E. coli Eut shells, with antibody-accessibility/immunogold controls. It does not establish full native EutB/EutC topology from reporter-fusion encapsulation alone. EutS sufficiency is restricted to the engineered system. |
| micro42-legacy-PMC3697265 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3697265/; Genuine primary HTML: complete model sec17 and Discussion sec22, including inference versus untested topology; complete native abstract. Earlier detailed Results/Methods were not independently read. | supports | Genetic growth/suppression and excreted-metabolite observations motivate private cofactor recycling and restricted aldehyde diffusion. The model explicitly proposes EutBC outside/on the shell and states that positioning was not tested. This competes with interior depictions; it does not prove exterior localization. |
| micro42-body-PMC3649267 | https://pmc.ncbi.nlm.nih.gov/articles/3649267/; Genuine primary HTML: complete main Introduction sec1, Results/Discussion sec2 and Methods sec4–7; Fig1/2 captions. | supports | The primary E. coli EutN work identifies predominantly pentameric solution assembly despite older hexamer crystal arrangements. It supports a vertex-protein lineage, without being an intact native Salmonella shell vertex map. |
| micro42-legacy-PMC2976447 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2976447/; Genuine primary HTML: Methods sec2; Results sec6/sec8 and sec7 except its truncated tail sentence; complete Discussion sec10. No supplement or new structural-data analysis. | supports | Recombinant E. coli EutL/EutM structures reveal shell-like layers and distinct pores; zinc-associated EutL opening motivates gating hypotheses. Native mixed-facet assembly and physiological zinc gating were not established. |
| micro42-body-PMC5821096 | https://pmc.ncbi.nlm.nih.gov/articles/5821096/; Genuine secondary review HTML: sec1.1 Catabolic reactions and sec1.2 Microcompartment formation; complete native abstract. | supports | The secondary review supports ethanolamine catabolism, Eut shell cohorts, variable gene content and proposed cofactor pools. Detailed chemistry/localization models are not universal to all bacteria carrying only core eut genes. |
| micro42-legacy-PMC8217296 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8217296/; Genuine primary HTML: complete abstract/Introduction Par1–6, Results Par7–10 and Fig1–4 captions. | supports | The genomic catalog supports patchy BMC locus distributions, including ethanolamine-associated types. Locus presence is not direct microscopic observation or expression in every bacterium. |
| micro42-PF00936 | https://www.ebi.ac.uk/interpro/api/entry/pfam/PF00936/; Complete native identity/type/description and integration scope. | supports | The native domain/family is broader than the exact Eut-only protein cohort and includes other BMC lineages; no near-match is imposed. |
| micro42-PF03319 | https://www.ebi.ac.uk/interpro/api/entry/pfam/PF03319/; Complete native identity/type/description and integration scope. | supports | The native domain/family is broader than the exact Eut-only protein cohort and includes other BMC lineages; no near-match is imposed. |
| micro42-IPR000249 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000249/; Complete native identity/type/description and integration scope. | supports | The native domain/family is broader than the exact Eut-only protein cohort and includes other BMC lineages; no near-match is imposed. |
| micro42-IPR004992 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004992/; Complete native identity/type/description and integration scope. | supports | The native domain/family is broader than the exact Eut-only protein cohort and includes other BMC lineages; no near-match is imposed. |
| schema-result | just validate data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml |
| strict-result | just validate-strict data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml --out /private/tmp/cellstructure-batch42-20261022-q4522lvm/ethanolamine_degradation_polyhedral_organelle-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml --out /private/tmp/cellstructure-batch42-20261022-q4522lvm/ethanolamine_degradation_polyhedral_organelle-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch42-20261022-q4522lvm/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch42-20261022-q4522lvm/ethanolamine_degradation_polyhedral_organelle-strict.tsv |
| native-proteins | /private/tmp/cellstructure-batch42-20261022-q4522lvm/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml; Complete read-only focused native proteins log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-graphs | /private/tmp/cellstructure-batch42-20261022-q4522lvm/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml; Complete read-only focused native graphs log | supports | data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml  (GO:0031471)<br>  eut_shell_assembly_and_cargo_targeting	eut_bmc_domain_shell_proteins	COVERED	-&gt;eut_bmc_domain_shell_proteins (UniProtKB:Q9ZFV7, UniProtKB:P41791, UniProtKB:P0A1C9, UniProtKB:Q9ZFU8)<br>  eut_shell_assembly_and_cargo_targeting	eutn_vertex_shell_protein	COVERED	-&gt;eutn_vertex_shell_protein (UniProtKB:P41792)<br>  eut_shell_assembly_and_cargo_targeting	eutc_targeting_peptide	UNANCHORED_WITH_UNIPROT	EutC N-terminal targeting sequence (UniProtKB:P19265)<br>  eut_shell_assembly_and_cargo_targeting	eut_lumen_enzymes	UNANCHORED_WITH_UNIPROT	Eut lumen enzymes (UniProtKB:P19264, UniProtKB:P19265)<br>  eut_shell_assembly_and_cargo_targeting	eutq	UNANCHORED_WITH_UNIPROT	EutQ assembly factor (UniProtKB:Q9ZFV5)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     3  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     2  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     5  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 22 of 25 collected target identifiers returned OK. PMID:22428024: UNREACHABLE; Exact native MED identity/title/DOI and returned PMC field were reviewed after bulk eutils414 transport failure. Resolving an identifier does not certify attached biology; the unrelated Ras PMID20080631 remains an explicit wrong-source finding.; PMID:27063436: UNREACHABLE; Exact native MED identity/title/DOI and returned PMC field were reviewed after bulk eutils414 transport failure. Resolving an identifier does not certify attached biology; the unrelated Ras PMID20080631 remains an explicit wrong-source finding.; PMID:27450681: UNREACHABLE; Exact native MED identity/title/DOI and returned PMC field were reviewed after bulk eutils414 transport failure. Resolving an identifier does not certify attached biology; the unrelated Ras PMID20080631 remains an explicit wrong-source finding. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Fan2012 and Kofoid1999 are complete-native-abstract only; canonical/legacy PMC responses were browser-check challenges and EPMC XML attempts failed. Quin2016 is complete-native-abstract support; no unread body is certified.
- Other body reading is confined to the specified sections. No supplement, movie, raw-image or crystallographic-data reanalysis was performed.
- EutB/C topology remains contested/inferred. Reporter fusions demonstrate targeting without settling full native enzyme orientation. EutQ nucleation remains a hypothesis despite direct in-vitro interaction and number effects.
- Identity/annotations do not establish every protein as essential or all eut-bearing bacteria as microcompartment-forming.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User expressly requests one review for every unreviewed record, including scientifically clean records.
- iModulonDB is not applicable to these protein-shell identity, assembly and compartmentalized-enzyme claims.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T041115Z-ethanolamine-degradation-polyhedral-organelle-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-backed review of ethanolamine degradation polyhedral organelle
started_at: '2026-10-22T03:47:05Z'
finished_at: '2026-10-22T04:11:15Z'
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
summary: Two minor corrections address attached-study attribution and reporter-to-native-cargo
  graph scope. Exact identity, qualified shell composition, protein identities, variable
  distribution and the genetic confinement model are supported.
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
  - path: data/structures/microcompartment/bacterial_microcompartment.yaml
    sha256: 744baee4509a2d6c59e951bf107ec3730a2576b7c084d239569913389b1a3321
    role: context
  - path: data/structures/microcompartment/carboxysome.yaml
    sha256: cdb55020f01fc187a13bdecb69c982a747dfb27fd2fa2e341c288a0cb56bdcd6
    role: context
  - path: data/structures/microcompartment/carboxysome_shell.yaml
    sha256: a732afb9239cc57b69ff7d4ca75700b4f2b3fb682837b1be799376d12acb7762
    role: context
  - path: data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml
    sha256: 67b4280a4ef1837e40fe65ac0ed67e263b95339d1b364a976ee1110c2440029f
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
- target_id: GO:0031471
  path: data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml
  label: ethanolamine degradation polyhedral organelle
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml
    role: maintained scientific record
scope:
  description: One complete target, with the other three BMC/carboxysome/shell/Eut
    records frozen as boundary context. Exact authority, all current component/function/graph/source
    placements, taxonomic scope, formation semantics, history and discussions were
    reviewed.
  selection: Batch42 fixed strict path order, index 10; exactly one maintained target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0031471
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0031471
  command: just validate data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0031471
  command: just validate-strict data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml
    --out /private/tmp/cellstructure-batch42-20261022-q4522lvm/ethanolamine_degradation_polyhedral_organelle-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-proteins
  name: Focused native proteins
  status: passed
  required: true
  target_ids:
  - GO:0031471
  command: /private/tmp/cellstructure-batch42-20261022-q4522lvm/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml
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
  - GO:0031471
  command: /private/tmp/cellstructure-batch42-20261022-q4522lvm/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml
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
  - GO:0031471
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - neighbor-bacterial_microcompartment
  - neighbor-carboxysome
  - neighbor-carboxysome_shell
  - micro42-doi0
  - micro42-doi4
  - micro42-doi5
  - micro42-doi6
  - micro42-doi8
  - micro42-doi9
  - micro42-doi11
  - micro42-doi12
  - micro42-doi16
  - micro42-pmid22428024
  - micro42-pmid27063436
  - micro42-pmid27450681
  - micro42-go
  - micro42-tax2
  - micro42-tax99287
  - micro42-up-P0A1C9
  - micro42-up-P19264
  - micro42-up-P19265
  - micro42-up-P41791
  - micro42-up-P41792
  - micro42-up-Q9ZFU8
  - micro42-up-Q9ZFV5
  - micro42-up-Q9ZFV7
  - micro42-xml-PMC4827028
  - micro42-xml-PMC3299773
  - micro42-legacy-PMC3697265
  - micro42-body-PMC3649267
  - micro42-legacy-PMC2976447
  - micro42-body-PMC5821096
  - micro42-legacy-PMC8217296
  - micro42-PF00936
  - micro42-PF03319
  - micro42-IPR000249
  - micro42-IPR004992
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0031471
  summary: '22 of 25 collected target identifiers returned OK. PMID:22428024: UNREACHABLE;
    Exact native MED identity/title/DOI and returned PMC field were reviewed after
    bulk eutils414 transport failure. Resolving an identifier does not certify attached
    biology; the unrelated Ras PMID20080631 remains an explicit wrong-source finding.;
    PMID:27063436: UNREACHABLE; Exact native MED identity/title/DOI and returned PMC
    field were reviewed after bulk eutils414 transport failure. Resolving an identifier
    does not certify attached biology; the unrelated Ras PMID20080631 remains an explicit
    wrong-source finding.; PMID:27450681: UNREACHABLE; Exact native MED identity/title/DOI
    and returned PMC field were reviewed after bulk eutils414 transport failure. Resolving
    an identifier does not certify attached biology; the unrelated Ras PMID20080631
    remains an explicit wrong-source finding. Native source checks are separately
    scoped; skipped or unreachable identifiers are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - micro42-doi16
  - micro42-pmid22428024
  - micro42-doi5
  - micro42-pmid27063436
  - micro42-pmid27450681
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0031471
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch42 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0031471
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch42 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0031471
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch42 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0031471
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch42 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0031471
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
    and current batch42 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml
  locator: Complete maintained YAML; all components, source notes, graphs, discussions
    and historical entries
  accessed_at: '2026-10-22T04:04:36Z'
  support: context_only
  summary: The entire maintained target was read; no scientific record was changed.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent; ComponentTypeEnum; EssentialityEnum; graph scopes
  accessed_at: '2026-10-22T04:04:36Z'
  support: context_only
  summary: Protein-family identity is distinct from an assembled complex. ESSENTIAL
    concerns failure of structure formation, not loss of catalytic function or ambient-CO2
    growth.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Components; groundings; associated machinery and chaperone boundaries
  accessed_at: '2026-10-22T04:04:36Z'
  support: context_only
  summary: Components are taxon-agnostic molecular families/classes; exact family
    grounding is preferred when verified. Mature constituents and assembled-structure
    maintenance machinery differ from transient preassembly chaperones.
- evidence_id: neighbor-bacterial_microcompartment
  kind: record_content
  reference: data/structures/microcompartment/bacterial_microcompartment.yaml
  locator: Complete frozen BMC/carboxysome/shell/Eut boundary neighbor
  accessed_at: '2026-10-22T04:04:36Z'
  support: context_only
  summary: Frozen neighboring record read for class, family and boundary context;
    its scientific verdict is not imported.
- evidence_id: neighbor-carboxysome
  kind: record_content
  reference: data/structures/microcompartment/carboxysome.yaml
  locator: Complete frozen BMC/carboxysome/shell/Eut boundary neighbor
  accessed_at: '2026-10-22T04:04:36Z'
  support: context_only
  summary: Frozen neighboring record read for class, family and boundary context;
    its scientific verdict is not imported.
- evidence_id: neighbor-carboxysome_shell
  kind: record_content
  reference: data/structures/microcompartment/carboxysome_shell.yaml
  locator: Complete frozen BMC/carboxysome/shell/Eut boundary neighbor
  accessed_at: '2026-10-22T04:04:36Z'
  support: context_only
  summary: Frozen neighboring record read for class, family and boundary context;
    its scientific verdict is not imported.
- evidence_id: micro42-doi0
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1002/pro.2246%22&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T03:49:44.560896Z'
  support: supports
  summary: 'Unique MED23456886: Bacterial microcompartment shells of diverse functional
    types possess pentameric vertex proteins. Authors/year/DOI and the complete native
    abstract were inspected. This row establishes bibliographic identity and abstract-level
    content only; detailed experiments require separately specified body evidence.'
  snapshot_sha256: d9ceebb6c28f663ab15b6c0b9becef57da37b3ab8d2260e198e12b9a1056c7a7
- evidence_id: micro42-doi4
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038/s41467-021-24126-4%22&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T03:49:44.657511Z'
  support: supports
  summary: 'Unique MED34155212: A catalog of the diversity and ubiquity of bacterial
    microcompartments. Authors/year/DOI and the complete native abstract were inspected.
    This row establishes bibliographic identity and abstract-level content only; detailed
    experiments require separately specified body evidence.'
  snapshot_sha256: 4ef9237d799acf8c34a54a2ad911d8c1355d6d6949d0cb18e0d8aa61cce9b9f7
- evidence_id: micro42-doi5
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038/srep24359%22&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T03:49:45.241904Z'
  support: supports
  summary: 'Unique MED27063436: Engineering formation of multiple recombinant Eut
    protein nanocompartments in E. coli. Authors/year/DOI and the complete native
    abstract were inspected. This row establishes bibliographic identity and abstract-level
    content only; detailed experiments require separately specified body evidence.'
  snapshot_sha256: 3a32e2eae31cea1b5db9f3399f9a509767cdac76e7253fcf11272d891a0d6942
- evidence_id: micro42-doi6
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
- evidence_id: micro42-doi8
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1128/JB.00652-10%22&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T03:49:45.432180Z'
  support: supports
  summary: 'Unique MED20851901: Crystallographic insights into the pore structures
    and mechanisms of the EutL and EutM shell proteins of the ethanolamine-utilizing
    microcompartment of Escherichia coli. Authors/year/DOI and the complete native
    abstract were inspected. This row establishes bibliographic identity and abstract-level
    content only; detailed experiments require separately specified body evidence.'
  snapshot_sha256: acbdc03648f98b68e0336eb864804dad8c5f5408ed3dd2b642b3f044badb0bd6
- evidence_id: micro42-doi9
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1128/JB.02179-12%22&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T03:49:45.857747Z'
  support: supports
  summary: 'Unique MED23585538: Evidence that a metabolic microcompartment contains
    and recycles private cofactor pools. Authors/year/DOI and the complete native
    abstract were inspected. This row establishes bibliographic identity and abstract-level
    content only; detailed experiments require separately specified body evidence.'
  snapshot_sha256: 4e1d2bc19ac7b667575da75b0cef0e45dd4db994be69bfc0b6fb366ba648c6b7
- evidence_id: micro42-doi11
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1128/jb.181.17.5317-5329.1999%22&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T03:49:46.125528Z'
  support: supports
  summary: 'Unique MED10464203: The 17-gene ethanolamine (eut) operon of Salmonella
    typhimurium encodes five homologues of carboxysome shell proteins. Authors/year/DOI
    and the complete native abstract were inspected. This row establishes bibliographic
    identity and abstract-level content only; detailed experiments require separately
    specified body evidence.'
  snapshot_sha256: 415e817fc2937531c04234492a5a36bf4ec0359a6ccd79ce11ea07d751ccd187
- evidence_id: micro42-doi12
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1128/mbio.00066-18%22&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T03:49:46.243468Z'
  support: supports
  summary: 'Unique MED29463652: Ethanolamine Utilization in Bacteria. Authors/year/DOI
    and the complete native abstract were inspected. This row establishes bibliographic
    identity and abstract-level content only; detailed experiments require separately
    specified body evidence.'
  snapshot_sha256: ec5428e4417e38fb53dc6295075ff97474d14de479ac99dd8ac13759d4eb6f66
- evidence_id: micro42-doi16
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1371/journal.pone.0033342%22&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T03:49:46.898409Z'
  support: supports
  summary: 'Unique MED22428024: Engineered protein nano-compartments for targeted
    enzyme localization. Authors/year/DOI and the complete native abstract were inspected.
    This row establishes bibliographic identity and abstract-level content only; detailed
    experiments require separately specified body evidence.'
  snapshot_sha256: a32a3bd9eefc7ea1671260cbe1f86dcc940bd3fc7940498f2f303fcc07181f00
- evidence_id: micro42-pmid22428024
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22428024%20AND%20SRC%3AMED&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T03:49:41.544173Z'
  support: supports
  summary: 'Unique MED22428024: Engineered protein nano-compartments for targeted
    enzyme localization. Authors/year/DOI and the complete native abstract were inspected.
    This row establishes bibliographic identity and abstract-level content only; detailed
    experiments require separately specified body evidence.'
  snapshot_sha256: acded31e3e8a8ca87cc4d83b8a166bfe151b4a2be46075a115ad91ebe218cc14
- evidence_id: micro42-pmid27063436
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
- evidence_id: micro42-pmid27450681
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A27450681%20AND%20SRC%3AMED&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T03:49:43.106424Z'
  support: supports
  summary: 'Unique MED27450681: Encapsulation of multiple cargo proteins within recombinant
    Eut nanocompartments. Authors/year/DOI and the complete native abstract were inspected.
    This row establishes bibliographic identity and abstract-level content only; detailed
    experiments require separately specified body evidence.'
  snapshot_sha256: 3cf9a5d668f82f9f92ac951f9207d2889283bf7a18557dc904019f00ce5346fb
- evidence_id: micro42-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0015977,GO:0031469,GO:0031470,GO:0031471,GO:0043232,GO:0046336
  locator: Exact GO0031471/GO0031469/GO0046336 identity, definition, obsolescence
    and typed relations.
  accessed_at: '2026-10-22T03:50:27.488533Z'
  support: supports
  summary: Native GO0031471 defines the protein-coated ethanolamine-catabolic organelle
    and its BMC parent; GO0046336 is the ethanolamine catabolic process. The record
    definition and hierarchy match these exact entries.
  snapshot_sha256: 7d520adef79917ad67a8d84c30d00d98c1bd17c20957615036f09416a50f15a1
- evidence_id: micro42-tax2
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2
  locator: Complete taxId/scientificName/rank/lineage/otherNames.
  accessed_at: '2026-10-22T03:49:53.043115Z'
  support: supports
  summary: ENA taxId 2 identifies Bacteria at rank domain; aliases and lineage match
    the record. Identity alone is not prevalence or experimental-condition evidence.
  snapshot_sha256: 314bd7723b8dea04f1840809fb74e06c514664fba9c6a0619e8f12e2a6dceef1
- evidence_id: micro42-tax99287
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/99287
  locator: Complete taxId/scientificName/rank/lineage/otherNames.
  accessed_at: '2026-10-22T03:49:53.787584Z'
  support: supports
  summary: ENA taxId 99287 identifies Salmonella enterica subsp. enterica serovar
    Typhimurium str. LT2 at rank strain; aliases and lineage match the record. Identity
    alone is not prevalence or experimental-condition evidence.
  snapshot_sha256: a557fe03f1355059dd28424200acb7710f662743c0887e910746f8648fd83736
- evidence_id: micro42-up-P0A1C9
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0A1C9.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references.
  accessed_at: '2026-10-22T03:49:47.756115Z'
  support: supports
  summary: P0A1C9 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['eutL'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 57753c195b2361203b9486c4a2cd8b30122d42f828fb5353ef487aeb8d9b5ad7
- evidence_id: micro42-up-P19264
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P19264.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references.
  accessed_at: '2026-10-22T03:49:47.776547Z'
  support: supports
  summary: P19264 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['eutB'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 5e401f34f61e17d72b3b2e260b87a6c729a41213b34b14a9dcbc02bc36eb2e70
- evidence_id: micro42-up-P19265
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P19265.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references.
  accessed_at: '2026-10-22T03:49:48.081798Z'
  support: supports
  summary: P19265 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['eutC'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 4e7b89f5b5f777de07de439c5ef635dadf2153b0d031ce1219fc34537b16a4ae
- evidence_id: micro42-up-P41791
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P41791.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references.
  accessed_at: '2026-10-22T03:49:48.473401Z'
  support: supports
  summary: P41791 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['eutM'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 1314821aa5369f8e58642a7d2a514dc3874af5622d2d2b0fdc6c2a67d639ab04
- evidence_id: micro42-up-P41792
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P41792.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references.
  accessed_at: '2026-10-22T03:49:48.495502Z'
  support: supports
  summary: P41792 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['eutN'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 22a0d585cec14eaa689767c91865f15404a42b532d14e6fb93555d16fa0b54ae
- evidence_id: micro42-up-Q9ZFU8
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q9ZFU8.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references.
  accessed_at: '2026-10-22T03:49:51.940572Z'
  support: supports
  summary: Q9ZFU8 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['eutK'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 5c3fda58489c611e7a5402629f500dfeea795c0915732ee25e703fdd1ac0728e
- evidence_id: micro42-up-Q9ZFV5
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q9ZFV5.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references.
  accessed_at: '2026-10-22T03:49:51.948293Z'
  support: supports
  summary: Q9ZFV5 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['eutQ'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 900441c5b49834d3d932b69661990092728248b42ede8ff7f958ae53cba61480
- evidence_id: micro42-up-Q9ZFV7
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q9ZFV7.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references.
  accessed_at: '2026-10-22T03:49:51.977933Z'
  support: supports
  summary: Q9ZFV7 is UniProtKB reviewed (Swiss-Prot), taxon 99287, genes ['eutS'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 08a2fde02fba424292d9aadd28196d0fd5a28e026079f564ec96f54ad16e1516
- evidence_id: micro42-xml-PMC4827028
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4827028/fullTextXML
  locator: 'Genuine primary JATS: Results sec3/sec4/sec6/sec7, Discussion sec8, Methods
    sec10–15. Figure-caption information in these sections; no supplementary movies/data
    or raw-pixel reanalysis.'
  accessed_at: '2026-10-22T03:52:07.953615Z'
  support: supports
  summary: Salmonella shell proteins form recombinant E. coli C2566 nanocompartments;
    EutQ alters number and interacts with EutM in vitro. Native LT2 deletion and heterologous
    constructs are distinct. EutQ-mediated nucleation and specific in-vivo binding
    remain hypotheses; EutQ is not absolutely required for a single recombinant shell.
  snapshot_sha256: cafd67767856801045fd864d5a220db1b8a4d18e07b0f5162e6fba15ecae9fbe
- evidence_id: micro42-xml-PMC3299773
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3299773/fullTextXML
  locator: 'Genuine primary JATS: Results s2b/s2c/s2d/s2e/s2h; Methods s4a/s4c/s4f;
    complete native abstract. Supplements and movies not independently read.'
  accessed_at: '2026-10-22T03:52:08.419507Z'
  support: supports
  summary: The study directly demonstrates EutC1–19-mediated reporter targeting in
    native Salmonella and recombinant E. coli Eut shells, with antibody-accessibility/immunogold
    controls. It does not establish full native EutB/EutC topology from reporter-fusion
    encapsulation alone. EutS sufficiency is restricted to the engineered system.
  snapshot_sha256: 80bed3dc78ff03883e126ff5c26c33dc041a5cac796fc9d628fbeb4a0c9f5268
- evidence_id: micro42-legacy-PMC3697265
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3697265/
  locator: 'Genuine primary HTML: complete model sec17 and Discussion sec22, including
    inference versus untested topology; complete native abstract. Earlier detailed
    Results/Methods were not independently read.'
  accessed_at: '2026-10-22T03:50:50.787622Z'
  support: supports
  summary: Genetic growth/suppression and excreted-metabolite observations motivate
    private cofactor recycling and restricted aldehyde diffusion. The model explicitly
    proposes EutBC outside/on the shell and states that positioning was not tested.
    This competes with interior depictions; it does not prove exterior localization.
  snapshot_sha256: 4e6676759a814cf96d8973c15e8c87c22b150a062ac1352ef3a678fc1b1cb5b3
- evidence_id: micro42-body-PMC3649267
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/3649267/
  locator: 'Genuine primary HTML: complete main Introduction sec1, Results/Discussion
    sec2 and Methods sec4–7; Fig1/2 captions.'
  accessed_at: '2026-10-22T03:50:10.258988Z'
  support: supports
  summary: The primary E. coli EutN work identifies predominantly pentameric solution
    assembly despite older hexamer crystal arrangements. It supports a vertex-protein
    lineage, without being an intact native Salmonella shell vertex map.
  snapshot_sha256: 22f974a401d2a905f82dce70ece1b7d6a774f66a9fb70220ce14b01c8f657709
- evidence_id: micro42-legacy-PMC2976447
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2976447/
  locator: 'Genuine primary HTML: Methods sec2; Results sec6/sec8 and sec7 except
    its truncated tail sentence; complete Discussion sec10. No supplement or new structural-data
    analysis.'
  accessed_at: '2026-10-22T03:50:49.598664Z'
  support: supports
  summary: Recombinant E. coli EutL/EutM structures reveal shell-like layers and distinct
    pores; zinc-associated EutL opening motivates gating hypotheses. Native mixed-facet
    assembly and physiological zinc gating were not established.
  snapshot_sha256: 099ae35e7560dc9dbc0bda4fa5eb444a81c6385d4246ad3aa6423a4a5b1fd1f8
- evidence_id: micro42-body-PMC5821096
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/5821096/
  locator: 'Genuine secondary review HTML: sec1.1 Catabolic reactions and sec1.2 Microcompartment
    formation; complete native abstract.'
  accessed_at: '2026-10-22T03:50:10.283204Z'
  support: supports
  summary: The secondary review supports ethanolamine catabolism, Eut shell cohorts,
    variable gene content and proposed cofactor pools. Detailed chemistry/localization
    models are not universal to all bacteria carrying only core eut genes.
  snapshot_sha256: 461082b397364e2a10ff7adf7eda320e8542e4a3211251bb979740746dbe7032
- evidence_id: micro42-legacy-PMC8217296
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8217296/
  locator: 'Genuine primary HTML: complete abstract/Introduction Par1–6, Results Par7–10
    and Fig1–4 captions.'
  accessed_at: '2026-10-22T03:50:50.267128Z'
  support: supports
  summary: The genomic catalog supports patchy BMC locus distributions, including
    ethanolamine-associated types. Locus presence is not direct microscopic observation
    or expression in every bacterium.
  snapshot_sha256: 3e1fe21fcf3ef391a378e1db66831851b09ac1e77e9c0483891831304e36b8f9
- evidence_id: micro42-PF00936
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF00936/
  locator: Complete native identity/type/description and integration scope.
  accessed_at: '2026-10-22T03:50:12.001189Z'
  support: supports
  summary: The native domain/family is broader than the exact Eut-only protein cohort
    and includes other BMC lineages; no near-match is imposed.
  snapshot_sha256: 88a3c70d733d57424d141f6922140d963d8b905db3c6195b6ff0966a5174aca5
- evidence_id: micro42-PF03319
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF03319/
  locator: Complete native identity/type/description and integration scope.
  accessed_at: '2026-10-22T03:50:11.940521Z'
  support: supports
  summary: The native domain/family is broader than the exact Eut-only protein cohort
    and includes other BMC lineages; no near-match is imposed.
  snapshot_sha256: ad23273fdf50fc94344313209a5b93f784650f2cc77658c99ccae660b546c569
- evidence_id: micro42-IPR000249
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000249/
  locator: Complete native identity/type/description and integration scope.
  accessed_at: '2026-10-22T03:49:53.814276Z'
  support: supports
  summary: The native domain/family is broader than the exact Eut-only protein cohort
    and includes other BMC lineages; no near-match is imposed.
  snapshot_sha256: a803c78897d7650014ec5c4b3404b8ea98b98c7e6879286566526675fb0bf103
- evidence_id: micro42-IPR004992
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004992/
  locator: Complete native identity/type/description and integration scope.
  accessed_at: '2026-10-22T03:49:54.003619Z'
  support: supports
  summary: The native domain/family is broader than the exact Eut-only protein cohort
    and includes other BMC lineages; no near-match is imposed.
  snapshot_sha256: e74c5aa30d022cec998d439ed5406764b62db0f8572dbda2a505255421d76c88
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:47:06Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml'
  snapshot_sha256: 7897efc4afa50b5d40daafe2c4f85ccef365f7e7e03cb887e548ecd71bbe4e82
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml
    --out /private/tmp/cellstructure-batch42-20261022-q4522lvm/ethanolamine_degradation_polyhedral_organelle-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:47:07Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml\
    \ --out /private/tmp/cellstructure-batch42-20261022-q4522lvm/ethanolamine_degradation_polyhedral_organelle-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch42-20261022-q4522lvm/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch42-20261022-q4522lvm/ethanolamine_degradation_polyhedral_organelle-strict.tsv"
  snapshot_sha256: eceb03642b9c1366465030f036b47db9c64fc4934395d19907178fd87b4128be
- evidence_id: native-proteins
  kind: validation
  reference: /private/tmp/cellstructure-batch42-20261022-q4522lvm/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml
  locator: Complete read-only focused native proteins log
  accessed_at: '2026-10-22T03:50:37.196037Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch42-20261022-q4522lvm/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml
  locator: Complete read-only focused native graphs log
  accessed_at: '2026-10-22T03:50:38.067509Z'
  support: supports
  summary: "data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml\
    \  (GO:0031471)\n  eut_shell_assembly_and_cargo_targeting\teut_bmc_domain_shell_proteins\t\
    COVERED\t->eut_bmc_domain_shell_proteins (UniProtKB:Q9ZFV7, UniProtKB:P41791,\
    \ UniProtKB:P0A1C9, UniProtKB:Q9ZFU8)\n  eut_shell_assembly_and_cargo_targeting\t\
    eutn_vertex_shell_protein\tCOVERED\t->eutn_vertex_shell_protein (UniProtKB:P41792)\n\
    \  eut_shell_assembly_and_cargo_targeting\teutc_targeting_peptide\tUNANCHORED_WITH_UNIPROT\t\
    EutC N-terminal targeting sequence (UniProtKB:P19265)\n  eut_shell_assembly_and_cargo_targeting\t\
    eut_lumen_enzymes\tUNANCHORED_WITH_UNIPROT\tEut lumen enzymes (UniProtKB:P19264,\
    \ UniProtKB:P19265)\n  eut_shell_assembly_and_cargo_targeting\teutq\tUNANCHORED_WITH_UNIPROT\t\
    EutQ assembly factor (UniProtKB:Q9ZFV5)\n\ncausal_graphs GENE_OR_PROTEIN node\
    \ summary:\n     3  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries\
    \ a UniProtKB grounding or xref\n     2  COVERED                   component_ref\
    \ target holds protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES\
    \          component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or\
    \ xref on the node\n     5  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 63d7f4bebe41a565bdb8dd398fa61a5e65b832949ae26d0b83e9a729f7946921
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml;
    native collect() exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '22 of 25 collected target identifiers returned OK. PMID:22428024: UNREACHABLE;
    Exact native MED identity/title/DOI and returned PMC field were reviewed after
    bulk eutils414 transport failure. Resolving an identifier does not certify attached
    biology; the unrelated Ras PMID20080631 remains an explicit wrong-source finding.;
    PMID:27063436: UNREACHABLE; Exact native MED identity/title/DOI and returned PMC
    field were reviewed after bulk eutils414 transport failure. Resolving an identifier
    does not certify attached biology; the unrelated Ras PMID20080631 remains an explicit
    wrong-source finding.; PMID:27450681: UNREACHABLE; Exact native MED identity/title/DOI
    and returned PMC field were reviewed after bulk eutils414 transport failure. Resolving
    an identifier does not certify attached biology; the unrelated Ras PMID20080631
    remains an explicit wrong-source finding. Native source checks are separately
    scoped; skipped or unreachable identifiers are not silently counted as resolved.'
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
  topic: Exact ethanolamine organelle class
  outcome: supported
  target_ids:
  - GO:0031471
  summary: The GO identity/definition, BMC parent and Eut synonyms are supported;
    this is a protein shell organelle, not a lipid membrane or merely an operon.
  evidence_ids:
  - record
  - micro42-go
  - micro42-body-PMC5821096
  - micro42-xml-PMC4827028
- assessment_id: composition
  area: grounding
  topic: Shell membership and family scopes
  outcome: supported
  target_ids:
  - GO:0031471
  summary: The two shell cohorts and their oligomeric roles are supported at specified
    native/recombinant tiers. Exact Eut-only family withholding is justified; optional
    exhaustive enzyme or assembly-factor inventory is not required.
  evidence_ids:
  - record
  - curation
  - micro42-body-PMC3649267
  - micro42-legacy-PMC2976447
  - micro42-xml-PMC3299773
  - micro42-xml-PMC4827028
  - micro42-PF00936
  - micro42-PF03319
  - micro42-IPR000249
  - micro42-IPR004992
- assessment_id: necessity
  area: grounding
  topic: Formation labels honestly unresolved
  outcome: unknown
  target_ids:
  - GO:0031471
  summary: Both component rows use UNKNOWN. Native mutant and recombinant sufficiency
    results do not imply universal individual-protein formation necessity; EutQ multiplicity
    effects are not obligatory formation.
  evidence_ids:
  - record
  - schema
  - micro42-xml-PMC3299773
  - micro42-xml-PMC4827028
  - micro42-legacy-PMC3697265
- assessment_id: proteins
  area: grounding
  topic: Accession and localization qualifications
  outcome: concern
  target_ids:
  - GO:0031471
  summary: All current example/graph accessions match reviewed Salmonella LT2 proteins
    and genes. EutN identity alone is not membership proof; its native location annotation
    is by similarity. EutB/C interior location remains probable/model dependent rather
    than directly established by reporter fusion.
  evidence_ids:
  - record
  - micro42-legacy-PMC3697265
  - micro42-xml-PMC3299773
  - micro42-up-P0A1C9
  - micro42-up-P19264
  - micro42-up-P19265
  - micro42-up-P41791
  - micro42-up-P41792
  - micro42-up-Q9ZFU8
  - micro42-up-Q9ZFV5
  - micro42-up-Q9ZFV7
- assessment_id: scope
  area: scope
  topic: Variable Bacteria and experimental strains
  outcome: supported
  target_ids:
  - GO:0031471
  summary: Native taxon identities match. LT2 native cultures, E. coli recombinant
    expression and isolated E. coli shell-protein studies are distinguished. VARIABLE
    Bacteria is tied to the genomic catalog, not extrapolated from one host.
  evidence_ids:
  - record
  - micro42-legacy-PMC8217296
  - micro42-xml-PMC4827028
  - micro42-xml-PMC3299773
  - micro42-legacy-PMC2976447
  - micro42-tax2
  - micro42-tax99287
- assessment_id: functions
  area: evidence
  topic: Chemical routing and confinement
  outcome: supported
  target_ids:
  - GO:0031471
  summary: The process identity and genetic cofactor/aldehyde model are supported.
    Notes correctly describe genetic evidence/model rather than direct permeability
    assays. Acetaldehyde restriction is incomplete and cofactor topology is mechanistic
    inference.
  evidence_ids:
  - record
  - micro42-go
  - micro42-legacy-PMC3697265
  - micro42-body-PMC5821096
- assessment_id: graph
  area: graph
  topic: Cargo targeting and source placement
  outcome: concern
  target_ids:
  - GO:0031471
  summary: Recombinant shell construction, EutC targeting and in-vitro EutQ–EutM binding
    are supported. Fan2012 is the wrong attached study for EutC/EutE–EutS binding;
    relevant Quin2016 occurs elsewhere. The lumen-enzyme node should not convert fused-reporter
    results into settled native EutB/C interior topology.
  evidence_ids:
  - record
  - micro42-xml-PMC4827028
  - micro42-xml-PMC3299773
  - micro42-legacy-PMC3697265
  - micro42-doi6
  - micro42-pmid27450681
- assessment_id: coverage
  area: completeness
  topic: Full record and canonical source scope
  outcome: concern
  target_ids:
  - GO:0031471
  summary: All fields/history/graph annotations were read; no images or verbatim snippets
    occur. The canonical note combines Kofoid operon mapping and Huseby cofactor work
    but attaches only Kofoid. This is bounded provenance, not rejection of the Salmonella
    example.
  evidence_ids:
  - record
  - micro42-doi11
  - micro42-legacy-PMC3697265
findings:
- finding_id: F1
  issue_key: eut-source-claim-placement
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Attach the correct study to cargo binding and cofactor claims
  description: Fan2012 directly studies PduP binding PduA/PduJ in the propanediol
    compartment, not EutC/EutE binding EutS. Relevant Quin2016 is already cited elsewhere
    and supports that biology. The canonical note also attributes private cofactor
    recycling to Huseby/Roth but attaches only Kofoid1999 operon mapping.
  target_ids:
  - GO:0031471
  field_paths:
  - causal_graphs[0].edges[2].evidence[0].reference
  - causal_graphs[0].edges[2].evidence[0].notes
  - canonical_examples[0].reference
  - canonical_examples[0].note
  evidence_ids:
  - record
  - micro42-doi6
  - micro42-pmid27450681
  - micro42-doi11
  - micro42-legacy-PMC3697265
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml
    role: maintained scientific record
  rule_id: Exact source scope, protein grounding and formation-specific essentiality
  native_severity: minor
  normalization_reason: Local source-placement errors with independently supported
    biology and correct organism; not proof that the mechanism or example is false.
- finding_id: F2
  issue_key: eut-reporter-native-cargo-graph-scope
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Distinguish reporter cargo from unsettled native EutBC topology
  description: The Eut lumen enzymes node specifically xrefs EutB/EutC, while its
    incoming Choudhary edge demonstrates routing fused reporters by the EutC N-terminal
    peptide. The cited Huseby model places EutBC outside/on the shell and says localization
    was not tested; native UniProt interior annotation is probable. Reporter encapsulation
    does not settle native EutBC topology.
  target_ids:
  - GO:0031471
  field_paths:
  - causal_graphs[0].nodes[4].label
  - causal_graphs[0].nodes[4].xrefs
  - causal_graphs[0].edges[3].object
  evidence_ids:
  - record
  - micro42-xml-PMC3299773
  - micro42-legacy-PMC3697265
  - micro42-up-P19264
  - micro42-up-P19265
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml
    role: maintained scientific record
  rule_id: Exact source scope, protein grounding and formation-specific essentiality
  native_severity: minor
  normalization_reason: The targeting sequence and recombinant encapsulation experiment
    remain correct; a bounded graph-object/accession join overstates native topology
    amid unresolved competing models.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0031471
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml
    role: maintained scientific record
  description: Attach Quin2016 to specific EutC/EutE–EutS binding and Huseby/Roth
    to cofactor modelling, retaining Kofoid for operon identity and each primary experimental
    context.
  acceptance_checks:
  - Preserve exact supported identity, experimental organism and native versus recombinant
    context.
  - Attach source-specific evidence to each changed claim and retain historical provenance.
  - Native schema, strict, CURIE, protein and graph checks pass as applicable.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0031471
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml
    role: maintained scientific record
  description: Represent demonstrated fused-reporter cargo or qualify the native-enzyme
    node and preserve competing models; do not claim EutBC is proven exterior or universally
    interior.
  acceptance_checks:
  - Preserve exact supported identity, experimental organism and native versus recombinant
    context.
  - Attach source-specific evidence to each changed claim and retain historical provenance.
  - Native schema, strict, CURIE, protein and graph checks pass as applicable.
limitations:
- Fan2012 and Kofoid1999 are complete-native-abstract only; canonical/legacy PMC responses
  were browser-check challenges and EPMC XML attempts failed. Quin2016 is complete-native-abstract
  support; no unread body is certified.
- Other body reading is confined to the specified sections. No supplement, movie,
  raw-image or crystallographic-data reanalysis was performed.
- EutB/C topology remains contested/inferred. Reporter fusions demonstrate targeting
  without settling full native enzyme orientation. EutQ nucleation remains a hypothesis
  despite direct in-vitro interaction and number effects.
- Identity/annotations do not establish every protein as essential or all eut-bearing
  bacteria as microcompartment-forming.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User expressly requests one review for every unreviewed record, including scientifically
  clean records.
- iModulonDB is not applicable to these protein-shell identity, assembly and compartmentalized-enzyme
  claims.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
