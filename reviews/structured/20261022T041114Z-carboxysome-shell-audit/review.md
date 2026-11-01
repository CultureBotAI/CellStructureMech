# Source-backed review of carboxysome shell

- Review: 20261022T041114Z-carboxysome-shell-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T03:47:00Z
- Finished UTC: 2026-10-22T04:11:14Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

One major formation-label correction and one minor structural-source correction are required; shell identity, protein cohorts, taxon-paired examples and qualified permeability biology are supported.

## Scope And Provenance

One complete target, with the other three BMC/carboxysome/shell/Eut records frozen as boundary context. Exact authority, all current component/function/graph/source placements, taxonomic scope, formation semantics, history and discussions were reviewed.

Selection: Batch42 fixed strict path order, index 8; exactly one maintained target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:carboxysome_shell | data/structures/microcompartment/carboxysome_shell.yaml | maintained | carboxysome shell |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | cellstructuremech:carboxysome_shell | Focused validator passed. |
| Focused native strict | passed | True | cellstructuremech:carboxysome_shell | Focused validator passed. |
| Focused native proteins | passed | True | cellstructuremech:carboxysome_shell | Read-only native check passed; claim-level protein/edge support evaluated separately. |
| Focused native graphs | passed | True | cellstructuremech:carboxysome_shell | Read-only native check passed; claim-level protein/edge support evaluated separately. |
| Claim-level scientific review | passed | True | cellstructuremech:carboxysome_shell | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | cellstructuremech:carboxysome_shell | 20 of 32 collected target identifiers returned OK. PMID:17675289: UNREACHABLE; Exact native MED identity/title/DOI and returned PMC field were reviewed after bulk eutils414 transport failure. Resolving an identifier does not certify attached biology; the unrelated Ras PMID20080631 remains an explicit wrong-source finding.; PMID:18258595: UNREACHABLE; Exact native MED identity/title/DOI and returned PMC field were reviewed after bulk eutils414 transport failure. Resolving an identifier does not certify attached biology; the unrelated Ras PMID20080631 remains an explicit wrong-source finding.; PMID:18292340: UNREACHABLE; Exact native MED identity/title/DOI and returned PMC field were reviewed after bulk eutils414 transport failure. Resolving an identifier does not certify attached biology; the unrelated Ras PMID20080631 remains an explicit wrong-source finding.; PMID:19844578: UNREACHABLE; Exact native MED identity/title/DOI and returned PMC field were reviewed after bulk eutils414 transport failure. Resolving an identifier does not certify attached biology; the unrelated Ras PMID20080631 remains an explicit wrong-source finding.; PMID:20304968: UNREACHABLE; Exact native MED identity/title/DOI and returned PMC field were reviewed after bulk eutils414 transport failure. Resolving an identifier does not certify attached biology; the unrelated Ras PMID20080631 remains an explicit wrong-source finding.; PMID:22928045: UNREACHABLE; Exact native MED identity/title/DOI and returned PMC field were reviewed after bulk eutils414 transport failure. Resolving an identifier does not certify attached biology; the unrelated Ras PMID20080631 remains an explicit wrong-source finding.; PMID:23572529: UNREACHABLE; Exact native MED identity/title/DOI and returned PMC field were reviewed after bulk eutils414 transport failure. Resolving an identifier does not certify attached biology; the unrelated Ras PMID20080631 remains an explicit wrong-source finding.; PMID:24267892: UNREACHABLE; Exact native MED identity/title/DOI and returned PMC field were reviewed after bulk eutils414 transport failure. Resolving an identifier does not certify attached biology; the unrelated Ras PMID20080631 remains an explicit wrong-source finding.; PMID:28616951: UNREACHABLE; Exact native MED identity/title/DOI and returned PMC field were reviewed after bulk eutils414 transport failure. Resolving an identifier does not certify attached biology; the unrelated Ras PMID20080631 remains an explicit wrong-source finding.; PMID:31048338: UNREACHABLE; Exact native MED identity/title/DOI and returned PMC field were reviewed after bulk eutils414 transport failure. Resolving an identifier does not certify attached biology; the unrelated Ras PMID20080631 remains an explicit wrong-source finding.; PMID:7934888: UNREACHABLE; Exact native MED identity/title/DOI and returned PMC field were reviewed after bulk eutils414 transport failure. Resolving an identifier does not certify attached biology; the unrelated Ras PMID20080631 remains an explicit wrong-source finding.; cellstructuremech:carboxysome_shell: SKIPPED; Exact current local shell identity occurs once in an ignored-inclusive maintained-corpus identifier search and is a frozen reviewed input. This does not infer exhaustive ontology absence. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | cellstructuremech:carboxysome_shell | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | cellstructuremech:carboxysome_shell | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | cellstructuremech:carboxysome_shell | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | cellstructuremech:carboxysome_shell | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | cellstructuremech:carboxysome_shell | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Shell structural identity and local identifier

identity: supported. Targets: cellstructuremech:carboxysome_shell.

The protein shell is distinct from the complete enzyme-loaded carboxysome, correctly part of GO0031470. The local exact identifier is valid; GO0043886 is a molecular function, and neither it nor the whole-carboxysome term should replace the shell identity.

### H/T/P architectural cohorts

grounding: supported. Targets: cellstructuremech:carboxysome_shell.

The shell-only constituent boundary and three protein classes are supported. Verified native domain/family scopes justify withholding a single exact grounding for these carboxysome-only combined cohorts; the broader BMC-P family appropriate to generic BMC cannot be forced here.

### Vertex closure versus structure formation

grounding: concern. Targets: cellstructuremech:carboxysome_shell.

The unqualified BMC-P ESSENTIAL label conflicts with native csoS4AB mutant carboxysomes that still form, mostly normal-looking but physiologically compromised. This does not deny a requirement for normal closure or beta-specific CcmL roles.

### Other grouped formation dependencies

grounding: unknown. Targets: cellstructuremech:carboxysome_shell.

H is the principal facet material; T roles differ among CcmO, CcmP and CsoS1D. CONDITIONAL does not establish a necessity condition for every T paralog across taxa, and intact-particle structure alone is insufficient for such an inference.

### Exact accession and source-organism joins

grounding: supported. Targets: cellstructuremech:carboxysome_shell.

All named examples resolve to their correct reviewed proteins/taxa and annotation references. The H. neapolitanus CsoS1D example is explicitly an identity example; Roberts2012 directly tests Prochlorococcus, and the native annotation distinction is preserved.

### Distribution, examples and barrier function

scope: supported. Targets: cellstructuremech:carboxysome_shell.

Bacterial occurrence is qualified; native H. neapolitanus and Syn7942 studies support the examples and vertex/CO2 barrier mechanism. Pore size, sulfate binding, computational fitting and inferred gating remain distinguished from direct transport-rate measurement.

### Coarse construction and permeability model

graph: concern. Targets: cellstructuremech:carboxysome_shell.

H facets, T incorporation, P capping and permeability form a source-supported coarse model. One edge citation overstates isolated CcmP crystallography as resolution inside the native shell; membership is separately supported by native colocalization.

### Whole target, history and excluded lumen cargo

completeness: supported. Targets: cellstructuremech:carboxysome_shell.

The complete target and histories were read. Excluding Rubisco/CA/internal scaffolds from the shell-only molecular inventory is justified. No image or verbatim snippet occurs here; optional exhaustive paralog inventories do not constitute findings.

## Findings

### F1: Do not equate vertex closure with obligatory shell formation

major / open / confirmed; issue key: carboxysome-shell-vertex-formation-essentiality.

The BMC-P cohort has ESSENTIAL formation status, but cited Cai2009 csoS4AB double mutants still produce mostly normal-looking carboxysomes and some elongated shells. Their poor ambient-CO2 growth and leakage barrier defect establish physiological importance rather than complete inability to form the structure.

### F2: Separate isolated CcmP structure from in-shell placement

minor / open / confirmed; issue key: carboxysome-shell-ccmp-structure-context.

The graph source note says Cai2013 resolved CcmP as stacked trimers in the beta-carboxysome shell. The crystal structures are of recombinant isolated CcmP; native colocalization supports membership, while docking models placement in the shell.

## Recommended Actions And Acceptance Checks

### A1

Use a condition/taxon-qualified formation label and preserve closure/CO2-barrier roles. Do not infer that surviving mutant particles are fully normal or fully functional.

- Preserve exact supported identity, experimental organism and native versus recombinant context.
- Attach source-specific evidence to each changed claim and retain historical provenance.
- Native schema, strict, CURIE, protein and graph checks pass as applicable.

### A2

State isolated recombinant CcmP crystallography, native colocalization and modelled shell incorporation separately while retaining the supported architecture.

- Preserve exact supported identity, experimental organism and native versus recombinant context.
- Attach source-specific evidence to each changed claim and retain historical provenance.
- Native schema, strict, CURIE, protein and graph checks pass as applicable.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/microcompartment/carboxysome_shell.yaml; Complete maintained YAML; all components, source notes, graphs, discussions and historical entries | context_only | The entire maintained target was read; no scientific record was changed. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent; ComponentTypeEnum; EssentialityEnum; graph scopes | context_only | Protein-family identity is distinct from an assembled complex. ESSENTIAL concerns failure of structure formation, not loss of catalytic function or ambient-CO2 growth. |
| curation | docs/CURATION.md; Components; groundings; associated machinery and chaperone boundaries | context_only | Components are taxon-agnostic molecular families/classes; exact family grounding is preferred when verified. Mature constituents and assembled-structure maintenance machinery differ from transient preassembly chaperones. |
| neighbor-bacterial_microcompartment | data/structures/microcompartment/bacterial_microcompartment.yaml; Complete frozen BMC/carboxysome/shell/Eut boundary neighbor | context_only | Frozen neighboring record read for class, family and boundary context; its scientific verdict is not imported. |
| neighbor-carboxysome | data/structures/microcompartment/carboxysome.yaml; Complete frozen BMC/carboxysome/shell/Eut boundary neighbor | context_only | Frozen neighboring record read for class, family and boundary context; its scientific verdict is not imported. |
| neighbor-ethanolamine_degradation_polyhedral_organelle | data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml; Complete frozen BMC/carboxysome/shell/Eut boundary neighbor | context_only | Frozen neighboring record read for class, family and boundary context; its scientific verdict is not imported. |
| micro42-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0015977,GO:0031469,GO:0031470,GO:0031471,GO:0043232,GO:0046336; Complete requested term identities, definitions, obsolescence and typed child relations. | supports | The requested active GO entries distinguish the whole carboxysome GO0031470, its BMC parent GO0031469 and the carbon-fixation process GO0015977. Typed children were read; this is not an asserted exact GO shell term. |
| micro42-SL0034 | https://rest.uniprot.org/locations/SL-0034.json; Complete definition, GO mapping and isA object; native counts not used as completeness evidence. | supports | SL-0034 identifies the carboxysome, maps GO0031470 and places it under bacterial microcompartment SL-0544. Its definition supports protein coat, Rubisco and carbonic-anhydrase carbon concentration. |
| micro42-tax1140 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1140; Complete taxId/scientificName/rank/lineage/otherNames. | supports | ENA taxId 1140 identifies Synechococcus elongatus PCC 7942 = FACHB-805 at rank strain; aliases and lineage match the record. Identity alone is not prevalence or experimental-condition evidence. |
| micro42-tax2 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2; Complete taxId/scientificName/rank/lineage/otherNames. | supports | ENA taxId 2 identifies Bacteria at rank domain; aliases and lineage match the record. Identity alone is not prevalence or experimental-condition evidence. |
| micro42-tax555778 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/555778; Complete taxId/scientificName/rank/lineage/otherNames. | supports | ENA taxId 555778 identifies Halothiobacillus neapolitanus c2 at rank strain; aliases and lineage match the record. Identity alone is not prevalence or experimental-condition evidence. |
| micro42-tax927 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/927; Complete taxId/scientificName/rank/lineage/otherNames. | supports | ENA taxId 927 identifies Halothiobacillus neapolitanus at rank species; aliases and lineage match the record. Identity alone is not prevalence or experimental-condition evidence. |
| micro42-up-D0KZ73 | https://rest.uniprot.org/uniprotkb/D0KZ73.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. | supports | D0KZ73 is UniProtKB reviewed (Swiss-Prot), taxon 555778, genes ['csoS1D']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro42-up-O85043 | https://rest.uniprot.org/uniprotkb/O85043.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. | supports | O85043 is UniProtKB reviewed (Swiss-Prot), taxon 555778, genes ['csoS4A']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro42-up-O85044 | https://rest.uniprot.org/uniprotkb/O85044.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. | supports | O85044 is UniProtKB reviewed (Swiss-Prot), taxon 555778, genes ['csoS4B']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro42-up-P45689 | https://rest.uniprot.org/uniprotkb/P45689.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. | supports | P45689 is UniProtKB reviewed (Swiss-Prot), taxon 555778, genes ['csoS1A']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro42-up-P46205 | https://rest.uniprot.org/uniprotkb/P46205.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. | supports | P46205 is UniProtKB reviewed (Swiss-Prot), taxon 1140, genes ['ccmO']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro42-up-Q03511 | https://rest.uniprot.org/uniprotkb/Q03511.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. | supports | Q03511 is UniProtKB reviewed (Swiss-Prot), taxon 1140, genes ['ccmK2']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro42-up-Q03512 | https://rest.uniprot.org/uniprotkb/Q03512.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. | supports | Q03512 is UniProtKB reviewed (Swiss-Prot), taxon 1140, genes ['ccmL']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro42-up-Q31QW7 | https://rest.uniprot.org/uniprotkb/Q31QW7.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. | supports | Q31QW7 is UniProtKB reviewed (Swiss-Prot), taxon 1140, genes ['ccmP']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro42-pmid17675289 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A17675289%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED17675289: Analysis of carboxysomes from Synechococcus PCC7942 reveals multiple Rubisco complexes with carboxysomal proteins CcmM and CcaA. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro42-pmid18258595 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A18258595%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED18258595: CO2 fixation kinetics of Halothiobacillus neapolitanus mutant carboxysomes lacking carbonic anhydrase suggest the shell acts as a diffusional barrier for CO2. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro42-pmid18292340 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A18292340%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED18292340: Atomic-level models of the bacterial carboxysome shell. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro42-pmid19844578 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A19844578%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED19844578: The pentameric vertex proteins are necessary for the icosahedral carboxysome shell to function as a CO2 leakage barrier. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro42-pmid20304968 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A20304968%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED20304968: Functional cyanobacterial beta-carboxysomes have an absolute requirement for both long and short forms of the CcmM protein. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro42-pmid22928045 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22928045%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED22928045: Structural determinants of the outer shell of β-carboxysomes in Synechococcus elongatus PCC 7942: roles for CcmK2, K3-K4, CcmO, and CcmL. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro42-pmid23572529 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A23572529%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED23572529: The structure of CcmP, a tandem bacterial microcompartment domain protein from the β-carboxysome, forms a subcompartment within a microcompartment. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro42-pmid24267892 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A24267892%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED24267892: Biogenesis of a bacterial organelle: the carboxysome assembly pathway. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro42-pmid28616951 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A28616951%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED28616951: Direct characterization of the native structure and mechanics of cyanobacterial carboxysomes. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro42-pmid31048338 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A31048338%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED31048338: Single-Organelle Quantification Reveals Stoichiometric and Structural Variability of Carboxysomes Dependent on the Environment. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro42-pmid7934888 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A7934888%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED7934888: Isolation and characterization of a carboxysome shell gene from Thiobacillus neapolitanus. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro42-legacy-PMC6022854 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6022854/; Genuine review HTML: Introduction P1–6, timeline P8–46, shell/assembly/diversity P47–72 and associated main captions. | supports | This secondary synthesis supports H/T/P shell architecture, alpha/beta core organization and established carbon-concentrating function; it distinguishes shell/core assembly models and incomplete mechanistic knowledge. |
| micro42-legacy-PMC3811607 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3811607/; Genuine secondary full HTML; independently read sec3-2, sec3-4, sec3-5, sec3-7, sec8-1 and sec8-2; complete native abstract separately. | supports | The review distinguishes alpha and beta components and evolution; carbonic-anhydrase deletion can leave normal-looking carboxysomes while abolishing efficient ambient-CO2 function. CcmM chemistry and CcaA occurrence differ among beta lineages. Shell-permeability and evolutionary arguments remain models, not a directly measured universal oxygen-exclusion rate. |
| micro42-body-PMC2760150 | https://pmc.ncbi.nlm.nih.gov/articles/2760150/; Genuine primary HTML: complete Introduction s1, Results s2a–f, Discussion s3, Methods s4a–g and Fig1–7 captions. Native H. neapolitanus c2/ATCC23641; high-CO2 culture context preserved. No new pixel quantification. | supports | Native H. neapolitanus csoS4AB double mutants still form mostly normal-looking carboxysomes, with a minority elongated, yet require high CO2 and show a compromised CO2 barrier. Absence was checked immunologically; subtle geometric deviations were not excluded. This directly separates formation from functional closure. |
| micro42-legacy-PMC3425506 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3425506/; Genuine primary HTML: Results s2a/s2c/s2d; Discussion s3a; Methods s4a/s4d/s4e; complete native abstract. Enriched fractions and nonspecific CcmM carryover are explicitly distinguished. | supports | Native Syn7942 deletion/complementation, TEM and carboxysome-enriched fractions support distinct CcmK2/CcmO requirements and their interaction; K3/K4 deletions differ. The work does not establish every H/T/P individual as universally essential across alpha and beta carboxysomes. |
| micro42-legacy-PMC3668761 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3668761/; Genuine primary HTML: Methods sec3/sec4; Results sec13 (nested Results text through sec20, including Fig1–5 captions); complete Discussion direct paragraphs sec21. Supplemental figures/data were not independently read. | supports | Native Syn7942 colocalization establishes CcmP association. Recombinant E. coli-expressed purified CcmP crystallography resolves stacked trimers and open/closed pore states; docking proposes incorporation into shell models. It does not resolve CcmP within an intact native shell or measure dynamic passage directly. |
| micro42-body-PMC3272956 | https://pmc.ncbi.nlm.nih.gov/articles/3272956/; Genuine primary HTML: Methods sec3–6; Results sec10 and sec12, their Fig1/2/4/5 captions and Table1. | supports | Native P. marinus MED4 carboxysomes were isolated; CsoS1D copurified and remained in the shell-enriched fraction after disruption. This is direct Prochlorococcus membership evidence, not direct localization of the independently identified H. neapolitanus accession. Some other low-abundance bands could not be conclusively identified. |
| micro42-body-PMC1872035 | https://pmc.ncbi.nlm.nih.gov/articles/1872035/; Genuine primary HTML: Introduction s1; Results s2a–d; Discussion s3 direct paragraphs; Methods s4a/s4b/s4g; complete Fig1 caption. The maintained Fig1 image is independently viewed only for the whole target. | supports | The primary study resolves recombinant H. neapolitanus CsoS1A hexamers and crystal layers; pore electrostatics/sulfate binding and diffusion calculations motivate a selective-permeability model. It explicitly does not directly measure natural metabolite transport. Fig1 depicts native H. neapolitanus cells and isolated carboxysomes with 100-nm bars. |
| micro42-IPR000249 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000249/; Complete native metadata identity/type/member description and integration, cross-checked against the named protein entries. | supports | Native identity/type and member coverage were inspected. Domain/family scope is broader or narrower than the combined carboxysome architectural cohort; no single near-match is imposed as exact H/T/P identity. IPR050575 generated description is not treated as primary experimental evidence. |
| micro42-IPR004992 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004992/; Complete native metadata identity/type/member description and integration, cross-checked against the named protein entries. | supports | Native identity/type and member coverage were inspected. Domain/family scope is broader or narrower than the combined carboxysome architectural cohort; no single near-match is imposed as exact H/T/P identity. IPR050575 generated description is not treated as primary experimental evidence. |
| micro42-IPR014076 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014076/; Complete native metadata identity/type/member description and integration, cross-checked against the named protein entries. | supports | Native identity/type and member coverage were inspected. Domain/family scope is broader or narrower than the combined carboxysome architectural cohort; no single near-match is imposed as exact H/T/P identity. IPR050575 generated description is not treated as primary experimental evidence. |
| micro42-IPR014077 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014077/; Complete native metadata identity/type/member description and integration, cross-checked against the named protein entries. | supports | Native identity/type and member coverage were inspected. Domain/family scope is broader or narrower than the combined carboxysome architectural cohort; no single near-match is imposed as exact H/T/P identity. IPR050575 generated description is not treated as primary experimental evidence. |
| micro42-IPR046380 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR046380/; Complete native metadata identity/type/member description and integration, cross-checked against the named protein entries. | supports | Native identity/type and member coverage were inspected. Domain/family scope is broader or narrower than the combined carboxysome architectural cohort; no single near-match is imposed as exact H/T/P identity. IPR050575 generated description is not treated as primary experimental evidence. |
| micro42-IPR046387 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR046387/; Complete native metadata identity/type/member description and integration, cross-checked against the named protein entries. | supports | Native identity/type and member coverage were inspected. Domain/family scope is broader or narrower than the combined carboxysome architectural cohort; no single near-match is imposed as exact H/T/P identity. IPR050575 generated description is not treated as primary experimental evidence. |
| micro42-IPR050575 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050575/; Complete native metadata identity/type/member description and integration, cross-checked against the named protein entries. | supports | Native identity/type and member coverage were inspected. Domain/family scope is broader or narrower than the combined carboxysome architectural cohort; no single near-match is imposed as exact H/T/P identity. IPR050575 generated description is not treated as primary experimental evidence. |
| micro42-IPR044870 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR044870/; Complete native metadata identity/type/member description and integration, cross-checked against the named protein entries. | supports | Native identity/type and member coverage were inspected. Domain/family scope is broader or narrower than the combined carboxysome architectural cohort; no single near-match is imposed as exact H/T/P identity. IPR050575 generated description is not treated as primary experimental evidence. |
| micro42-PF00936 | https://www.ebi.ac.uk/interpro/api/entry/pfam/PF00936/; Complete native metadata identity/type/member description and integration, cross-checked against the named protein entries. | supports | Native identity/type and member coverage were inspected. Domain/family scope is broader or narrower than the combined carboxysome architectural cohort; no single near-match is imposed as exact H/T/P identity. IPR050575 generated description is not treated as primary experimental evidence. |
| micro42-PF03319 | https://www.ebi.ac.uk/interpro/api/entry/pfam/PF03319/; Complete native metadata identity/type/member description and integration, cross-checked against the named protein entries. | supports | Native identity/type and member coverage were inspected. Domain/family scope is broader or narrower than the combined carboxysome architectural cohort; no single near-match is imposed as exact H/T/P identity. IPR050575 generated description is not treated as primary experimental evidence. |
| micro42-doi2 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038/nrmicro.2018.10%22&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED29503457: Bacterial microcompartments. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro42-doi10 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1128/JB.06444-11%22&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED22155772: Isolation and characterization of the Prochlorococcus carboxysome reveal the presence of the novel shell protein CsoS1D. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro42-doi13 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1371/journal.pbio.0050144%22&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED17518518: Structural analysis of CsoS1A and the protein shell of the Halothiobacillus neapolitanus carboxysome. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro42-doi15 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1371/journal.pone.0007521%22&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED19844578: The pentameric vertex proteins are necessary for the icosahedral carboxysome shell to function as a CO2 leakage barrier. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro42-doi17 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1371/journal.pone.0043871%22&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED22928045: Structural determinants of the outer shell of β-carboxysomes in Synechococcus elongatus PCC 7942: roles for CcmK2, K3-K4, CcmO, and CcmL. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro42-go-shell-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=carboxysome%20shell&amp;limit=100; Exact query carboxysome shell, returned term list and paging metadata; remote query only. | supports | The bounded native QuickGO search returns the whole carboxysome and a molecular-function shell-constituent term, not an exact shell cellular component in these results. This does not establish global ontology absence; the maintained local ID remains an exact structural identity. |
| micro42-go-carboxysome-children | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031470/children; Complete requested GO0031470 children response with typed relations. | supports | The exact native carboxysome children response contains the shell-constituent molecular function linked by occurs_in; it does not supply an exact shell cellular-component identity in this child list. |
| schema-result | just validate data/structures/microcompartment/carboxysome_shell.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/microcompartment/carboxysome_shell.yaml |
| strict-result | just validate-strict data/structures/microcompartment/carboxysome_shell.yaml --out /private/tmp/cellstructure-batch42-20261022-q4522lvm/carboxysome_shell-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/microcompartment/carboxysome_shell.yaml --out /private/tmp/cellstructure-batch42-20261022-q4522lvm/carboxysome_shell-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch42-20261022-q4522lvm/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch42-20261022-q4522lvm/carboxysome_shell-strict.tsv |
| native-proteins | /private/tmp/cellstructure-batch42-20261022-q4522lvm/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/microcompartment/carboxysome_shell.yaml; Complete read-only focused native proteins log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-graphs | /private/tmp/cellstructure-batch42-20261022-q4522lvm/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/microcompartment/carboxysome_shell.yaml; Complete read-only focused native graphs log | supports | data/structures/microcompartment/carboxysome_shell.yaml  (cellstructuremech:carboxysome_shell)<br>  protein_shell_selective_barrier	bmc_h	COVERED	-&gt;bmc_h (UniProtKB:Q03511, UniProtKB:P45689)<br>  protein_shell_selective_barrier	bmc_t	COVERED	-&gt;bmc_t (UniProtKB:P46205, UniProtKB:Q31QW7, UniProtKB:D0KZ73)<br>  protein_shell_selective_barrier	bmc_p	COVERED	-&gt;bmc_p (UniProtKB:Q03512, UniProtKB:O85043, UniProtKB:O85044)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     3  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     3  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/microcompartment/carboxysome_shell.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 20 of 32 collected target identifiers returned OK. PMID:17675289: UNREACHABLE; Exact native MED identity/title/DOI and returned PMC field were reviewed after bulk eutils414 transport failure. Resolving an identifier does not certify attached biology; the unrelated Ras PMID20080631 remains an explicit wrong-source finding.; PMID:18258595: UNREACHABLE; Exact native MED identity/title/DOI and returned PMC field were reviewed after bulk eutils414 transport failure. Resolving an identifier does not certify attached biology; the unrelated Ras PMID20080631 remains an explicit wrong-source finding.; PMID:18292340: UNREACHABLE; Exact native MED identity/title/DOI and returned PMC field were reviewed after bulk eutils414 transport failure. Resolving an identifier does not certify attached biology; the unrelated Ras PMID20080631 remains an explicit wrong-source finding.; PMID:19844578: UNREACHABLE; Exact native MED identity/title/DOI and returned PMC field were reviewed after bulk eutils414 transport failure. Resolving an identifier does not certify attached biology; the unrelated Ras PMID20080631 remains an explicit wrong-source finding.; PMID:20304968: UNREACHABLE; Exact native MED identity/title/DOI and returned PMC field were reviewed after bulk eutils414 transport failure. Resolving an identifier does not certify attached biology; the unrelated Ras PMID20080631 remains an explicit wrong-source finding.; PMID:22928045: UNREACHABLE; Exact native MED identity/title/DOI and returned PMC field were reviewed after bulk eutils414 transport failure. Resolving an identifier does not certify attached biology; the unrelated Ras PMID20080631 remains an explicit wrong-source finding.; PMID:23572529: UNREACHABLE; Exact native MED identity/title/DOI and returned PMC field were reviewed after bulk eutils414 transport failure. Resolving an identifier does not certify attached biology; the unrelated Ras PMID20080631 remains an explicit wrong-source finding.; PMID:24267892: UNREACHABLE; Exact native MED identity/title/DOI and returned PMC field were reviewed after bulk eutils414 transport failure. Resolving an identifier does not certify attached biology; the unrelated Ras PMID20080631 remains an explicit wrong-source finding.; PMID:28616951: UNREACHABLE; Exact native MED identity/title/DOI and returned PMC field were reviewed after bulk eutils414 transport failure. Resolving an identifier does not certify attached biology; the unrelated Ras PMID20080631 remains an explicit wrong-source finding.; PMID:31048338: UNREACHABLE; Exact native MED identity/title/DOI and returned PMC field were reviewed after bulk eutils414 transport failure. Resolving an identifier does not certify attached biology; the unrelated Ras PMID20080631 remains an explicit wrong-source finding.; PMID:7934888: UNREACHABLE; Exact native MED identity/title/DOI and returned PMC field were reviewed after bulk eutils414 transport failure. Resolving an identifier does not certify attached biology; the unrelated Ras PMID20080631 remains an explicit wrong-source finding.; cellstructuremech:carboxysome_shell: SKIPPED; Exact current local shell identity occurs once in an ignored-inclusive maintained-corpus identifier search and is a frozen reviewed input. This does not infer exhaustive ontology absence. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Reading extents are specified per source. Several native annotation citations were checked at complete-abstract level without claiming unread article bodies or supplemental datasets.
- Cai2009 mutant particles retain assembly with defects; the result does not establish normal icosahedral geometry or functional closure. Specific beta-carboxysome CcmL requirements remain distinct.
- The exact native GO query is bounded, not proof that no future or unqueried shell term exists. Local identity is preserved; no molecular-function near-match is substituted.
- No raw figure pixels were reanalysed for this target. Crystal geometry, static conformers and shell docking do not establish dynamic transport rates in vivo.
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
review_id: 20261022T041114Z-carboxysome-shell-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-backed review of carboxysome shell
started_at: '2026-10-22T03:47:00Z'
finished_at: '2026-10-22T04:11:14Z'
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
summary: One major formation-label correction and one minor structural-source correction
  are required; shell identity, protein cohorts, taxon-paired examples and qualified
  permeability biology are supported.
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
    role: target
  - path: data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml
    sha256: 67b4280a4ef1837e40fe65ac0ed67e263b95339d1b364a976ee1110c2440029f
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
- target_id: cellstructuremech:carboxysome_shell
  path: data/structures/microcompartment/carboxysome_shell.yaml
  label: carboxysome shell
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/microcompartment/carboxysome_shell.yaml
    role: maintained scientific record
scope:
  description: One complete target, with the other three BMC/carboxysome/shell/Eut
    records frozen as boundary context. Exact authority, all current component/function/graph/source
    placements, taxonomic scope, formation semantics, history and discussions were
    reviewed.
  selection: Batch42 fixed strict path order, index 8; exactly one maintained target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:carboxysome_shell
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:carboxysome_shell
  command: just validate data/structures/microcompartment/carboxysome_shell.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:carboxysome_shell
  command: just validate-strict data/structures/microcompartment/carboxysome_shell.yaml
    --out /private/tmp/cellstructure-batch42-20261022-q4522lvm/carboxysome_shell-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-proteins
  name: Focused native proteins
  status: passed
  required: true
  target_ids:
  - cellstructuremech:carboxysome_shell
  command: /private/tmp/cellstructure-batch42-20261022-q4522lvm/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/microcompartment/carboxysome_shell.yaml
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
  - cellstructuremech:carboxysome_shell
  command: /private/tmp/cellstructure-batch42-20261022-q4522lvm/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/microcompartment/carboxysome_shell.yaml
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
  - cellstructuremech:carboxysome_shell
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - neighbor-bacterial_microcompartment
  - neighbor-carboxysome
  - neighbor-ethanolamine_degradation_polyhedral_organelle
  - micro42-go
  - micro42-SL0034
  - micro42-tax1140
  - micro42-tax2
  - micro42-tax555778
  - micro42-tax927
  - micro42-up-D0KZ73
  - micro42-up-O85043
  - micro42-up-O85044
  - micro42-up-P45689
  - micro42-up-P46205
  - micro42-up-Q03511
  - micro42-up-Q03512
  - micro42-up-Q31QW7
  - micro42-pmid17675289
  - micro42-pmid18258595
  - micro42-pmid18292340
  - micro42-pmid19844578
  - micro42-pmid20304968
  - micro42-pmid22928045
  - micro42-pmid23572529
  - micro42-pmid24267892
  - micro42-pmid28616951
  - micro42-pmid31048338
  - micro42-pmid7934888
  - micro42-legacy-PMC6022854
  - micro42-legacy-PMC3811607
  - micro42-body-PMC2760150
  - micro42-legacy-PMC3425506
  - micro42-legacy-PMC3668761
  - micro42-body-PMC3272956
  - micro42-body-PMC1872035
  - micro42-IPR000249
  - micro42-IPR004992
  - micro42-IPR014076
  - micro42-IPR014077
  - micro42-IPR046380
  - micro42-IPR046387
  - micro42-IPR050575
  - micro42-IPR044870
  - micro42-PF00936
  - micro42-PF03319
  - micro42-doi2
  - micro42-doi10
  - micro42-doi13
  - micro42-doi15
  - micro42-doi17
  - micro42-go-shell-search
  - micro42-go-carboxysome-children
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - cellstructuremech:carboxysome_shell
  summary: '20 of 32 collected target identifiers returned OK. PMID:17675289: UNREACHABLE;
    Exact native MED identity/title/DOI and returned PMC field were reviewed after
    bulk eutils414 transport failure. Resolving an identifier does not certify attached
    biology; the unrelated Ras PMID20080631 remains an explicit wrong-source finding.;
    PMID:18258595: UNREACHABLE; Exact native MED identity/title/DOI and returned PMC
    field were reviewed after bulk eutils414 transport failure. Resolving an identifier
    does not certify attached biology; the unrelated Ras PMID20080631 remains an explicit
    wrong-source finding.; PMID:18292340: UNREACHABLE; Exact native MED identity/title/DOI
    and returned PMC field were reviewed after bulk eutils414 transport failure. Resolving
    an identifier does not certify attached biology; the unrelated Ras PMID20080631
    remains an explicit wrong-source finding.; PMID:19844578: UNREACHABLE; Exact native
    MED identity/title/DOI and returned PMC field were reviewed after bulk eutils414
    transport failure. Resolving an identifier does not certify attached biology;
    the unrelated Ras PMID20080631 remains an explicit wrong-source finding.; PMID:20304968:
    UNREACHABLE; Exact native MED identity/title/DOI and returned PMC field were reviewed
    after bulk eutils414 transport failure. Resolving an identifier does not certify
    attached biology; the unrelated Ras PMID20080631 remains an explicit wrong-source
    finding.; PMID:22928045: UNREACHABLE; Exact native MED identity/title/DOI and
    returned PMC field were reviewed after bulk eutils414 transport failure. Resolving
    an identifier does not certify attached biology; the unrelated Ras PMID20080631
    remains an explicit wrong-source finding.; PMID:23572529: UNREACHABLE; Exact native
    MED identity/title/DOI and returned PMC field were reviewed after bulk eutils414
    transport failure. Resolving an identifier does not certify attached biology;
    the unrelated Ras PMID20080631 remains an explicit wrong-source finding.; PMID:24267892:
    UNREACHABLE; Exact native MED identity/title/DOI and returned PMC field were reviewed
    after bulk eutils414 transport failure. Resolving an identifier does not certify
    attached biology; the unrelated Ras PMID20080631 remains an explicit wrong-source
    finding.; PMID:28616951: UNREACHABLE; Exact native MED identity/title/DOI and
    returned PMC field were reviewed after bulk eutils414 transport failure. Resolving
    an identifier does not certify attached biology; the unrelated Ras PMID20080631
    remains an explicit wrong-source finding.; PMID:31048338: UNREACHABLE; Exact native
    MED identity/title/DOI and returned PMC field were reviewed after bulk eutils414
    transport failure. Resolving an identifier does not certify attached biology;
    the unrelated Ras PMID20080631 remains an explicit wrong-source finding.; PMID:7934888:
    UNREACHABLE; Exact native MED identity/title/DOI and returned PMC field were reviewed
    after bulk eutils414 transport failure. Resolving an identifier does not certify
    attached biology; the unrelated Ras PMID20080631 remains an explicit wrong-source
    finding.; cellstructuremech:carboxysome_shell: SKIPPED; Exact current local shell
    identity occurs once in an ignored-inclusive maintained-corpus identifier search
    and is a frozen reviewed input. This does not infer exhaustive ontology absence.
    Native source checks are separately scoped; skipped or unreachable identifiers
    are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - micro42-pmid17675289
  - micro42-pmid18258595
  - micro42-pmid18292340
  - micro42-doi15
  - micro42-pmid19844578
  - micro42-pmid20304968
  - micro42-doi17
  - micro42-pmid22928045
  - micro42-pmid23572529
  - micro42-pmid24267892
  - micro42-pmid28616951
  - micro42-pmid31048338
  - micro42-pmid7934888
  - record
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:carboxysome_shell
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
  - cellstructuremech:carboxysome_shell
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
  - cellstructuremech:carboxysome_shell
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
  - cellstructuremech:carboxysome_shell
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
  - cellstructuremech:carboxysome_shell
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
  reference: data/structures/microcompartment/carboxysome_shell.yaml
  locator: Complete maintained YAML; all components, source notes, graphs, discussions
    and historical entries
  accessed_at: '2026-10-22T04:02:35Z'
  support: context_only
  summary: The entire maintained target was read; no scientific record was changed.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent; ComponentTypeEnum; EssentialityEnum; graph scopes
  accessed_at: '2026-10-22T04:02:35Z'
  support: context_only
  summary: Protein-family identity is distinct from an assembled complex. ESSENTIAL
    concerns failure of structure formation, not loss of catalytic function or ambient-CO2
    growth.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Components; groundings; associated machinery and chaperone boundaries
  accessed_at: '2026-10-22T04:02:35Z'
  support: context_only
  summary: Components are taxon-agnostic molecular families/classes; exact family
    grounding is preferred when verified. Mature constituents and assembled-structure
    maintenance machinery differ from transient preassembly chaperones.
- evidence_id: neighbor-bacterial_microcompartment
  kind: record_content
  reference: data/structures/microcompartment/bacterial_microcompartment.yaml
  locator: Complete frozen BMC/carboxysome/shell/Eut boundary neighbor
  accessed_at: '2026-10-22T04:02:35Z'
  support: context_only
  summary: Frozen neighboring record read for class, family and boundary context;
    its scientific verdict is not imported.
- evidence_id: neighbor-carboxysome
  kind: record_content
  reference: data/structures/microcompartment/carboxysome.yaml
  locator: Complete frozen BMC/carboxysome/shell/Eut boundary neighbor
  accessed_at: '2026-10-22T04:02:35Z'
  support: context_only
  summary: Frozen neighboring record read for class, family and boundary context;
    its scientific verdict is not imported.
- evidence_id: neighbor-ethanolamine_degradation_polyhedral_organelle
  kind: record_content
  reference: data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml
  locator: Complete frozen BMC/carboxysome/shell/Eut boundary neighbor
  accessed_at: '2026-10-22T04:02:35Z'
  support: context_only
  summary: Frozen neighboring record read for class, family and boundary context;
    its scientific verdict is not imported.
- evidence_id: micro42-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0015977,GO:0031469,GO:0031470,GO:0031471,GO:0043232,GO:0046336
  locator: Complete requested term identities, definitions, obsolescence and typed
    child relations.
  accessed_at: '2026-10-22T03:50:27.488533Z'
  support: supports
  summary: The requested active GO entries distinguish the whole carboxysome GO0031470,
    its BMC parent GO0031469 and the carbon-fixation process GO0015977. Typed children
    were read; this is not an asserted exact GO shell term.
  snapshot_sha256: 7d520adef79917ad67a8d84c30d00d98c1bd17c20957615036f09416a50f15a1
- evidence_id: micro42-SL0034
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0034.json
  locator: Complete definition, GO mapping and isA object; native counts not used
    as completeness evidence.
  accessed_at: '2026-10-22T03:50:28.112492Z'
  support: supports
  summary: SL-0034 identifies the carboxysome, maps GO0031470 and places it under
    bacterial microcompartment SL-0544. Its definition supports protein coat, Rubisco
    and carbonic-anhydrase carbon concentration.
  snapshot_sha256: 29e0329bec73c800ab336f0676f35834dc67a4f7a6e19d2bb81ad19a9f40d6bd
- evidence_id: micro42-tax1140
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1140
  locator: Complete taxId/scientificName/rank/lineage/otherNames.
  accessed_at: '2026-10-22T03:49:52.867893Z'
  support: supports
  summary: ENA taxId 1140 identifies Synechococcus elongatus PCC 7942 = FACHB-805
    at rank strain; aliases and lineage match the record. Identity alone is not prevalence
    or experimental-condition evidence.
  snapshot_sha256: 70bf02b8ca783e9afbd060d6c098a79cec71954ea2d64a270fc130481a63cb2b
- evidence_id: micro42-tax2
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2
  locator: Complete taxId/scientificName/rank/lineage/otherNames.
  accessed_at: '2026-10-22T03:49:53.043115Z'
  support: supports
  summary: ENA taxId 2 identifies Bacteria at rank domain; aliases and lineage match
    the record. Identity alone is not prevalence or experimental-condition evidence.
  snapshot_sha256: 314bd7723b8dea04f1840809fb74e06c514664fba9c6a0619e8f12e2a6dceef1
- evidence_id: micro42-tax555778
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/555778
  locator: Complete taxId/scientificName/rank/lineage/otherNames.
  accessed_at: '2026-10-22T03:49:53.064797Z'
  support: supports
  summary: ENA taxId 555778 identifies Halothiobacillus neapolitanus c2 at rank strain;
    aliases and lineage match the record. Identity alone is not prevalence or experimental-condition
    evidence.
  snapshot_sha256: 8f62a0778e6500581adfb9880ed654a7c8bf642e9c12d9cb0948a1423069ea1f
- evidence_id: micro42-tax927
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/927
  locator: Complete taxId/scientificName/rank/lineage/otherNames.
  accessed_at: '2026-10-22T03:49:53.728108Z'
  support: supports
  summary: ENA taxId 927 identifies Halothiobacillus neapolitanus at rank species;
    aliases and lineage match the record. Identity alone is not prevalence or experimental-condition
    evidence.
  snapshot_sha256: 90c2235cf96f6b99ac73674d561b86090ac8e059e4d6981ed09ca244ab67bd90
- evidence_id: micro42-up-D0KZ73
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/D0KZ73.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references.
  accessed_at: '2026-10-22T03:49:47.051030Z'
  support: supports
  summary: D0KZ73 is UniProtKB reviewed (Swiss-Prot), taxon 555778, genes ['csoS1D'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 107ef8fef5ffc5d3654c2d57dbce06770395ea235e6f0cc03d8131229cb4c45b
- evidence_id: micro42-up-O85043
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/O85043.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references.
  accessed_at: '2026-10-22T03:49:47.659953Z'
  support: supports
  summary: O85043 is UniProtKB reviewed (Swiss-Prot), taxon 555778, genes ['csoS4A'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 9fee67e162991078ba3a2bf368848b0afb508579c0a96092e2279b0bbc7780b4
- evidence_id: micro42-up-O85044
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/O85044.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references.
  accessed_at: '2026-10-22T03:49:47.694333Z'
  support: supports
  summary: O85044 is UniProtKB reviewed (Swiss-Prot), taxon 555778, genes ['csoS4B'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 3046156a1f38423ccd917475f4694ab42231bc7bc1e8e22d197268ec3d5792c9
- evidence_id: micro42-up-P45689
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P45689.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references.
  accessed_at: '2026-10-22T03:49:48.943404Z'
  support: supports
  summary: P45689 is UniProtKB reviewed (Swiss-Prot), taxon 555778, genes ['csoS1A'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 72e1c7f661583c36b401d51f42d203de0a8dd988eb90428b7ae83bee6f5ec7c0
- evidence_id: micro42-up-P46205
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P46205.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references.
  accessed_at: '2026-10-22T03:49:49.053396Z'
  support: supports
  summary: P46205 is UniProtKB reviewed (Swiss-Prot), taxon 1140, genes ['ccmO'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 483d0e740d1701ec0ecd17fedf2cd27a2d89724108efd1956f1197207317f6c1
- evidence_id: micro42-up-Q03511
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q03511.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references.
  accessed_at: '2026-10-22T03:49:49.209838Z'
  support: supports
  summary: Q03511 is UniProtKB reviewed (Swiss-Prot), taxon 1140, genes ['ccmK2'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: e03170ddd15e23f7594be9c1f46838487b1855624aa39763a58d405ef7061bbb
- evidence_id: micro42-up-Q03512
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q03512.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references.
  accessed_at: '2026-10-22T03:49:49.937278Z'
  support: supports
  summary: Q03512 is UniProtKB reviewed (Swiss-Prot), taxon 1140, genes ['ccmL'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 1237cf2534382c045d3fd7ef1952c7457fde8296980a23f8102f3a0a5885f5f7
- evidence_id: micro42-up-Q31QW7
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q31QW7.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references.
  accessed_at: '2026-10-22T03:49:50.934653Z'
  support: supports
  summary: Q31QW7 is UniProtKB reviewed (Swiss-Prot), taxon 1140, genes ['ccmP'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: fb89b777434d141599507638b7349cba93af480f0809db802e6325b8f5716af6
- evidence_id: micro42-pmid17675289
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A17675289%20AND%20SRC%3AMED&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T03:49:40.714107Z'
  support: supports
  summary: 'Unique MED17675289: Analysis of carboxysomes from Synechococcus PCC7942
    reveals multiple Rubisco complexes with carboxysomal proteins CcmM and CcaA. Authors/year/DOI
    and the complete native abstract were inspected. This row establishes bibliographic
    identity and abstract-level content only; detailed experiments require separately
    specified body evidence.'
  snapshot_sha256: ef9469b046197d96f494b9830367d27dbb1a53ed8c5419291e4cf8b0b49a3141
- evidence_id: micro42-pmid18258595
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A18258595%20AND%20SRC%3AMED&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T03:49:40.713839Z'
  support: supports
  summary: 'Unique MED18258595: CO2 fixation kinetics of Halothiobacillus neapolitanus
    mutant carboxysomes lacking carbonic anhydrase suggest the shell acts as a diffusional
    barrier for CO2. Authors/year/DOI and the complete native abstract were inspected.
    This row establishes bibliographic identity and abstract-level content only; detailed
    experiments require separately specified body evidence.'
  snapshot_sha256: 1b8fad2f552448cbbb4f25fead285cd9c1561a79fc810794ea129b9482f52e6c
- evidence_id: micro42-pmid18292340
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A18292340%20AND%20SRC%3AMED&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T03:49:40.714199Z'
  support: supports
  summary: 'Unique MED18292340: Atomic-level models of the bacterial carboxysome shell.
    Authors/year/DOI and the complete native abstract were inspected. This row establishes
    bibliographic identity and abstract-level content only; detailed experiments require
    separately specified body evidence.'
  snapshot_sha256: 29e5bb00c81adb3f97faa2fc0c0b1d8e087dd9fb53d251fd5d72ee157a474fb2
- evidence_id: micro42-pmid19844578
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A19844578%20AND%20SRC%3AMED&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T03:49:40.714381Z'
  support: supports
  summary: 'Unique MED19844578: The pentameric vertex proteins are necessary for the
    icosahedral carboxysome shell to function as a CO2 leakage barrier. Authors/year/DOI
    and the complete native abstract were inspected. This row establishes bibliographic
    identity and abstract-level content only; detailed experiments require separately
    specified body evidence.'
  snapshot_sha256: 796d432f24f46f3130a9c4038afa6412ee060a7e8c1ebdc4a2dc16ce25de52ba
- evidence_id: micro42-pmid20304968
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A20304968%20AND%20SRC%3AMED&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T03:49:41.484071Z'
  support: supports
  summary: 'Unique MED20304968: Functional cyanobacterial beta-carboxysomes have an
    absolute requirement for both long and short forms of the CcmM protein. Authors/year/DOI
    and the complete native abstract were inspected. This row establishes bibliographic
    identity and abstract-level content only; detailed experiments require separately
    specified body evidence.'
  snapshot_sha256: 3ae3717b15e082d0fae56431455bc913eb0c8d59e3c783b0b93b1b0460a98e7a
- evidence_id: micro42-pmid22928045
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22928045%20AND%20SRC%3AMED&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T03:49:41.558423Z'
  support: supports
  summary: 'Unique MED22928045: Structural determinants of the outer shell of β-carboxysomes
    in Synechococcus elongatus PCC 7942: roles for CcmK2, K3-K4, CcmO, and CcmL. Authors/year/DOI
    and the complete native abstract were inspected. This row establishes bibliographic
    identity and abstract-level content only; detailed experiments require separately
    specified body evidence.'
  snapshot_sha256: df7ba5ed9c21d3f19f06d9e13fe6fbee677b6450a341bd580c1d6fb3789bf809
- evidence_id: micro42-pmid23572529
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A23572529%20AND%20SRC%3AMED&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T03:49:42.095327Z'
  support: supports
  summary: 'Unique MED23572529: The structure of CcmP, a tandem bacterial microcompartment
    domain protein from the β-carboxysome, forms a subcompartment within a microcompartment.
    Authors/year/DOI and the complete native abstract were inspected. This row establishes
    bibliographic identity and abstract-level content only; detailed experiments require
    separately specified body evidence.'
  snapshot_sha256: 3b5bfa6a4c08941b1c66d45d1bcfc1cd7158749018b26c21c185bef29e3eaa5f
- evidence_id: micro42-pmid24267892
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A24267892%20AND%20SRC%3AMED&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T03:49:42.196543Z'
  support: supports
  summary: 'Unique MED24267892: Biogenesis of a bacterial organelle: the carboxysome
    assembly pathway. Authors/year/DOI and the complete native abstract were inspected.
    This row establishes bibliographic identity and abstract-level content only; detailed
    experiments require separately specified body evidence.'
  snapshot_sha256: 6605b1a2d8fce06e213eaefdc19a68e81b0cd1962062180fcfd2408763bb715b
- evidence_id: micro42-pmid28616951
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A28616951%20AND%20SRC%3AMED&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T03:49:43.188137Z'
  support: supports
  summary: 'Unique MED28616951: Direct characterization of the native structure and
    mechanics of cyanobacterial carboxysomes. Authors/year/DOI and the complete native
    abstract were inspected. This row establishes bibliographic identity and abstract-level
    content only; detailed experiments require separately specified body evidence.'
  snapshot_sha256: 0cc0255449a6983017f13fa10a4820c7b09dbe75250328dbcbe04b3af5cb479f
- evidence_id: micro42-pmid31048338
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A31048338%20AND%20SRC%3AMED&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T03:49:43.926450Z'
  support: supports
  summary: 'Unique MED31048338: Single-Organelle Quantification Reveals Stoichiometric
    and Structural Variability of Carboxysomes Dependent on the Environment. Authors/year/DOI
    and the complete native abstract were inspected. This row establishes bibliographic
    identity and abstract-level content only; detailed experiments require separately
    specified body evidence.'
  snapshot_sha256: dd02a54f554c0d21eb014d0f204e2dff5126713fd4c51d69eb3cd86ab01ee827
- evidence_id: micro42-pmid7934888
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A7934888%20AND%20SRC%3AMED&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T03:49:43.975037Z'
  support: supports
  summary: 'Unique MED7934888: Isolation and characterization of a carboxysome shell
    gene from Thiobacillus neapolitanus. Authors/year/DOI and the complete native
    abstract were inspected. This row establishes bibliographic identity and abstract-level
    content only; detailed experiments require separately specified body evidence.'
  snapshot_sha256: 3fe182a5b1309bf9e99409562f6cd217d08d95b893b18a92060624a424117e39
- evidence_id: micro42-legacy-PMC6022854
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6022854/
  locator: 'Genuine review HTML: Introduction P1–6, timeline P8–46, shell/assembly/diversity
    P47–72 and associated main captions.'
  accessed_at: '2026-10-22T03:50:50.533150Z'
  support: supports
  summary: This secondary synthesis supports H/T/P shell architecture, alpha/beta
    core organization and established carbon-concentrating function; it distinguishes
    shell/core assembly models and incomplete mechanistic knowledge.
  snapshot_sha256: 4d4c6458a485c328fdf9f64c005c464dbcb2c9866cd8236374995ece391db05d
- evidence_id: micro42-legacy-PMC3811607
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3811607/
  locator: Genuine secondary full HTML; independently read sec3-2, sec3-4, sec3-5,
    sec3-7, sec8-1 and sec8-2; complete native abstract separately.
  accessed_at: '2026-10-22T03:50:51.119229Z'
  support: supports
  summary: The review distinguishes alpha and beta components and evolution; carbonic-anhydrase
    deletion can leave normal-looking carboxysomes while abolishing efficient ambient-CO2
    function. CcmM chemistry and CcaA occurrence differ among beta lineages. Shell-permeability
    and evolutionary arguments remain models, not a directly measured universal oxygen-exclusion
    rate.
  snapshot_sha256: 025eef543848d674ea088d5f94e210c6011ddd2abe7bd957ed2e7c233e9c8c54
- evidence_id: micro42-body-PMC2760150
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/2760150/
  locator: 'Genuine primary HTML: complete Introduction s1, Results s2a–f, Discussion
    s3, Methods s4a–g and Fig1–7 captions. Native H. neapolitanus c2/ATCC23641; high-CO2
    culture context preserved. No new pixel quantification.'
  accessed_at: '2026-10-22T03:50:10.723977Z'
  support: supports
  summary: Native H. neapolitanus csoS4AB double mutants still form mostly normal-looking
    carboxysomes, with a minority elongated, yet require high CO2 and show a compromised
    CO2 barrier. Absence was checked immunologically; subtle geometric deviations
    were not excluded. This directly separates formation from functional closure.
  snapshot_sha256: ed4b9e04cbf950a05dff636695de32a84046abbe5d24fce85360c72e375311c6
- evidence_id: micro42-legacy-PMC3425506
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3425506/
  locator: 'Genuine primary HTML: Results s2a/s2c/s2d; Discussion s3a; Methods s4a/s4d/s4e;
    complete native abstract. Enriched fractions and nonspecific CcmM carryover are
    explicitly distinguished.'
  accessed_at: '2026-10-22T03:50:50.875597Z'
  support: supports
  summary: Native Syn7942 deletion/complementation, TEM and carboxysome-enriched fractions
    support distinct CcmK2/CcmO requirements and their interaction; K3/K4 deletions
    differ. The work does not establish every H/T/P individual as universally essential
    across alpha and beta carboxysomes.
  snapshot_sha256: 90c0f1ec81ae14a57b002a6af10ce5cfe8764eccc8be5216943372db0c673e26
- evidence_id: micro42-legacy-PMC3668761
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3668761/
  locator: 'Genuine primary HTML: Methods sec3/sec4; Results sec13 (nested Results
    text through sec20, including Fig1–5 captions); complete Discussion direct paragraphs
    sec21. Supplemental figures/data were not independently read.'
  accessed_at: '2026-10-22T03:50:49.599660Z'
  support: supports
  summary: Native Syn7942 colocalization establishes CcmP association. Recombinant
    E. coli-expressed purified CcmP crystallography resolves stacked trimers and open/closed
    pore states; docking proposes incorporation into shell models. It does not resolve
    CcmP within an intact native shell or measure dynamic passage directly.
  snapshot_sha256: a33e5646bf7d4c78e0d0db45dd065b23557649aedd670a52f8ddf9100807c8d8
- evidence_id: micro42-body-PMC3272956
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/3272956/
  locator: 'Genuine primary HTML: Methods sec3–6; Results sec10 and sec12, their Fig1/2/4/5
    captions and Table1.'
  accessed_at: '2026-10-22T03:50:10.281127Z'
  support: supports
  summary: Native P. marinus MED4 carboxysomes were isolated; CsoS1D copurified and
    remained in the shell-enriched fraction after disruption. This is direct Prochlorococcus
    membership evidence, not direct localization of the independently identified H.
    neapolitanus accession. Some other low-abundance bands could not be conclusively
    identified.
  snapshot_sha256: 2c111dcf86c1916859514e858651c5f276217f3b7626cf14ac84aac15e1125ff
- evidence_id: micro42-body-PMC1872035
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/1872035/
  locator: 'Genuine primary HTML: Introduction s1; Results s2a–d; Discussion s3 direct
    paragraphs; Methods s4a/s4b/s4g; complete Fig1 caption. The maintained Fig1 image
    is independently viewed only for the whole target.'
  accessed_at: '2026-10-22T03:50:10.689644Z'
  support: supports
  summary: The primary study resolves recombinant H. neapolitanus CsoS1A hexamers
    and crystal layers; pore electrostatics/sulfate binding and diffusion calculations
    motivate a selective-permeability model. It explicitly does not directly measure
    natural metabolite transport. Fig1 depicts native H. neapolitanus cells and isolated
    carboxysomes with 100-nm bars.
  snapshot_sha256: 8d2fad5081043094b5468996d1f643cd4791c07950c825cd2451507faa709c93
- evidence_id: micro42-IPR000249
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000249/
  locator: Complete native metadata identity/type/member description and integration,
    cross-checked against the named protein entries.
  accessed_at: '2026-10-22T03:49:53.814276Z'
  support: supports
  summary: Native identity/type and member coverage were inspected. Domain/family
    scope is broader or narrower than the combined carboxysome architectural cohort;
    no single near-match is imposed as exact H/T/P identity. IPR050575 generated description
    is not treated as primary experimental evidence.
  snapshot_sha256: a803c78897d7650014ec5c4b3404b8ea98b98c7e6879286566526675fb0bf103
- evidence_id: micro42-IPR004992
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004992/
  locator: Complete native metadata identity/type/member description and integration,
    cross-checked against the named protein entries.
  accessed_at: '2026-10-22T03:49:54.003619Z'
  support: supports
  summary: Native identity/type and member coverage were inspected. Domain/family
    scope is broader or narrower than the combined carboxysome architectural cohort;
    no single near-match is imposed as exact H/T/P identity. IPR050575 generated description
    is not treated as primary experimental evidence.
  snapshot_sha256: e74c5aa30d022cec998d439ed5406764b62db0f8572dbda2a505255421d76c88
- evidence_id: micro42-IPR014076
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014076/
  locator: Complete native metadata identity/type/member description and integration,
    cross-checked against the named protein entries.
  accessed_at: '2026-10-22T03:49:55.279151Z'
  support: supports
  summary: Native identity/type and member coverage were inspected. Domain/family
    scope is broader or narrower than the combined carboxysome architectural cohort;
    no single near-match is imposed as exact H/T/P identity. IPR050575 generated description
    is not treated as primary experimental evidence.
  snapshot_sha256: 950ab813aa5719021e2979c6c2284b461fb57abe9e987ab38ff437c701626fbb
- evidence_id: micro42-IPR014077
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014077/
  locator: Complete native metadata identity/type/member description and integration,
    cross-checked against the named protein entries.
  accessed_at: '2026-10-22T03:50:08.757861Z'
  support: supports
  summary: Native identity/type and member coverage were inspected. Domain/family
    scope is broader or narrower than the combined carboxysome architectural cohort;
    no single near-match is imposed as exact H/T/P identity. IPR050575 generated description
    is not treated as primary experimental evidence.
  snapshot_sha256: a512302003b951a71d4c914811d84fddd2fb9b8d6f2f5b151a8da9d05bd4a65f
- evidence_id: micro42-IPR046380
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR046380/
  locator: Complete native metadata identity/type/member description and integration,
    cross-checked against the named protein entries.
  accessed_at: '2026-10-22T03:50:18.504332Z'
  support: supports
  summary: Native identity/type and member coverage were inspected. Domain/family
    scope is broader or narrower than the combined carboxysome architectural cohort;
    no single near-match is imposed as exact H/T/P identity. IPR050575 generated description
    is not treated as primary experimental evidence.
  snapshot_sha256: a37c31f836716d4e799ff63bd53449e76187812dac10bf92f1b678fd155b79a2
- evidence_id: micro42-IPR046387
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR046387/
  locator: Complete native metadata identity/type/member description and integration,
    cross-checked against the named protein entries.
  accessed_at: '2026-10-22T03:50:22.103532Z'
  support: supports
  summary: Native identity/type and member coverage were inspected. Domain/family
    scope is broader or narrower than the combined carboxysome architectural cohort;
    no single near-match is imposed as exact H/T/P identity. IPR050575 generated description
    is not treated as primary experimental evidence.
  snapshot_sha256: f1643b74366e1266370860d8e04318897616bc329ee5f97863437226d4079079
- evidence_id: micro42-IPR050575
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050575/
  locator: Complete native metadata identity/type/member description and integration,
    cross-checked against the named protein entries.
  accessed_at: '2026-10-22T03:50:23.719950Z'
  support: supports
  summary: Native identity/type and member coverage were inspected. Domain/family
    scope is broader or narrower than the combined carboxysome architectural cohort;
    no single near-match is imposed as exact H/T/P identity. IPR050575 generated description
    is not treated as primary experimental evidence.
  snapshot_sha256: c10a875a9b33d2ea782ada989c7d0e4047cf5a90fd2cb68a77430189eb130d12
- evidence_id: micro42-IPR044870
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR044870/
  locator: Complete native metadata identity/type/member description and integration,
    cross-checked against the named protein entries.
  accessed_at: '2026-10-22T03:50:12.244909Z'
  support: supports
  summary: Native identity/type and member coverage were inspected. Domain/family
    scope is broader or narrower than the combined carboxysome architectural cohort;
    no single near-match is imposed as exact H/T/P identity. IPR050575 generated description
    is not treated as primary experimental evidence.
  snapshot_sha256: ea9d3be2d8b421f5fe80535a4a43a5e82b164a6761578d282c3bc7d962f4b62e
- evidence_id: micro42-PF00936
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF00936/
  locator: Complete native metadata identity/type/member description and integration,
    cross-checked against the named protein entries.
  accessed_at: '2026-10-22T03:50:12.001189Z'
  support: supports
  summary: Native identity/type and member coverage were inspected. Domain/family
    scope is broader or narrower than the combined carboxysome architectural cohort;
    no single near-match is imposed as exact H/T/P identity. IPR050575 generated description
    is not treated as primary experimental evidence.
  snapshot_sha256: 88a3c70d733d57424d141f6922140d963d8b905db3c6195b6ff0966a5174aca5
- evidence_id: micro42-PF03319
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF03319/
  locator: Complete native metadata identity/type/member description and integration,
    cross-checked against the named protein entries.
  accessed_at: '2026-10-22T03:50:11.940521Z'
  support: supports
  summary: Native identity/type and member coverage were inspected. Domain/family
    scope is broader or narrower than the combined carboxysome architectural cohort;
    no single near-match is imposed as exact H/T/P identity. IPR050575 generated description
    is not treated as primary experimental evidence.
  snapshot_sha256: ad23273fdf50fc94344313209a5b93f784650f2cc77658c99ccae660b546c569
- evidence_id: micro42-doi2
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038/nrmicro.2018.10%22&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T03:49:44.622347Z'
  support: supports
  summary: 'Unique MED29503457: Bacterial microcompartments. Authors/year/DOI and
    the complete native abstract were inspected. This row establishes bibliographic
    identity and abstract-level content only; detailed experiments require separately
    specified body evidence.'
  snapshot_sha256: 2a201c7ad09e400058b0e169914d5d0b828ef4af6d8ec642fcb41e1d373b42e6
- evidence_id: micro42-doi10
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1128/JB.06444-11%22&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T03:49:46.121669Z'
  support: supports
  summary: 'Unique MED22155772: Isolation and characterization of the Prochlorococcus
    carboxysome reveal the presence of the novel shell protein CsoS1D. Authors/year/DOI
    and the complete native abstract were inspected. This row establishes bibliographic
    identity and abstract-level content only; detailed experiments require separately
    specified body evidence.'
  snapshot_sha256: d304c8b65d3076f95ee6abe2bc4d6c8db280044f50d7ccf337de6a5c47c3aea8
- evidence_id: micro42-doi13
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1371/journal.pbio.0050144%22&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T03:49:46.395617Z'
  support: supports
  summary: 'Unique MED17518518: Structural analysis of CsoS1A and the protein shell
    of the Halothiobacillus neapolitanus carboxysome. Authors/year/DOI and the complete
    native abstract were inspected. This row establishes bibliographic identity and
    abstract-level content only; detailed experiments require separately specified
    body evidence.'
  snapshot_sha256: d0d776049743f73c89410d29a3e312cf939c2cc5b17ea52d5bc7bb903be3fd53
- evidence_id: micro42-doi15
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1371/journal.pone.0007521%22&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T03:49:46.876168Z'
  support: supports
  summary: 'Unique MED19844578: The pentameric vertex proteins are necessary for the
    icosahedral carboxysome shell to function as a CO2 leakage barrier. Authors/year/DOI
    and the complete native abstract were inspected. This row establishes bibliographic
    identity and abstract-level content only; detailed experiments require separately
    specified body evidence.'
  snapshot_sha256: 9ef0efb805d53e74ddb993f9afc934aa8ed25f01844311df6fe9da2bed3a0c5c
- evidence_id: micro42-doi17
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1371/journal.pone.0043871%22&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T03:49:46.899168Z'
  support: supports
  summary: 'Unique MED22928045: Structural determinants of the outer shell of β-carboxysomes
    in Synechococcus elongatus PCC 7942: roles for CcmK2, K3-K4, CcmO, and CcmL. Authors/year/DOI
    and the complete native abstract were inspected. This row establishes bibliographic
    identity and abstract-level content only; detailed experiments require separately
    specified body evidence.'
  snapshot_sha256: db5f61ea3024085db917f36a1b523e65707dc187b58d4ca151788a963d6718e7
- evidence_id: micro42-go-shell-search
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=carboxysome%20shell&limit=100
  locator: Exact query carboxysome shell, returned term list and paging metadata;
    remote query only.
  accessed_at: '2026-10-22T03:50:12.029353Z'
  support: supports
  summary: The bounded native QuickGO search returns the whole carboxysome and a molecular-function
    shell-constituent term, not an exact shell cellular component in these results.
    This does not establish global ontology absence; the maintained local ID remains
    an exact structural identity.
  snapshot_sha256: 87bfffb18a01262c533e3d7fd385a573300f9d01ef11579c1063e8422c58dc70
  search_scope: Native remote QuickGO search for carboxysome shell, first/only response
    page, limit100; all returned entries and result count read. Ignored-file inclusion
    is not applicable to a remote query; no local absence inferred.
- evidence_id: micro42-go-carboxysome-children
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031470/children
  locator: Complete requested GO0031470 children response with typed relations.
  accessed_at: '2026-10-22T03:50:12.247375Z'
  support: supports
  summary: The exact native carboxysome children response contains the shell-constituent
    molecular function linked by occurs_in; it does not supply an exact shell cellular-component
    identity in this child list.
  snapshot_sha256: 687ba3097972a240459a720669b958335888300f64987665aa8fcf3aeb1ab470
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/microcompartment/carboxysome_shell.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:47:01Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/microcompartment/carboxysome_shell.yaml'
  snapshot_sha256: 9956809412a847e888766fd6e9d69227c9241c11d6cbc27a96eeef4254ee617c
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/microcompartment/carboxysome_shell.yaml
    --out /private/tmp/cellstructure-batch42-20261022-q4522lvm/carboxysome_shell-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:47:03Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/microcompartment/carboxysome_shell.yaml\
    \ --out /private/tmp/cellstructure-batch42-20261022-q4522lvm/carboxysome_shell-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch42-20261022-q4522lvm/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch42-20261022-q4522lvm/carboxysome_shell-strict.tsv"
  snapshot_sha256: 76ba6197d7b2f7442d1d10d898a8c6732f527c5adb91b34d8a8069ec8188d612
- evidence_id: native-proteins
  kind: validation
  reference: /private/tmp/cellstructure-batch42-20261022-q4522lvm/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/microcompartment/carboxysome_shell.yaml
  locator: Complete read-only focused native proteins log
  accessed_at: '2026-10-22T03:50:33.713066Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch42-20261022-q4522lvm/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/microcompartment/carboxysome_shell.yaml
  locator: Complete read-only focused native graphs log
  accessed_at: '2026-10-22T03:50:34.670673Z'
  support: supports
  summary: "data/structures/microcompartment/carboxysome_shell.yaml  (cellstructuremech:carboxysome_shell)\n\
    \  protein_shell_selective_barrier\tbmc_h\tCOVERED\t->bmc_h (UniProtKB:Q03511,\
    \ UniProtKB:P45689)\n  protein_shell_selective_barrier\tbmc_t\tCOVERED\t->bmc_t\
    \ (UniProtKB:P46205, UniProtKB:Q31QW7, UniProtKB:D0KZ73)\n  protein_shell_selective_barrier\t\
    bmc_p\tCOVERED\t->bmc_p (UniProtKB:Q03512, UniProtKB:O85043, UniProtKB:O85044)\n\
    \ncausal_graphs GENE_OR_PROTEIN node summary:\n     3  COVERED               \
    \    component_ref target holds protein_examples covering all declared symbols\n\
    \     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     3\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: d5abdebec9f8d73685b62b2b47cc0db710171a10b8479a827128d1ab1fa6f9c2
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/microcompartment/carboxysome_shell.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '20 of 32 collected target identifiers returned OK. PMID:17675289: UNREACHABLE;
    Exact native MED identity/title/DOI and returned PMC field were reviewed after
    bulk eutils414 transport failure. Resolving an identifier does not certify attached
    biology; the unrelated Ras PMID20080631 remains an explicit wrong-source finding.;
    PMID:18258595: UNREACHABLE; Exact native MED identity/title/DOI and returned PMC
    field were reviewed after bulk eutils414 transport failure. Resolving an identifier
    does not certify attached biology; the unrelated Ras PMID20080631 remains an explicit
    wrong-source finding.; PMID:18292340: UNREACHABLE; Exact native MED identity/title/DOI
    and returned PMC field were reviewed after bulk eutils414 transport failure. Resolving
    an identifier does not certify attached biology; the unrelated Ras PMID20080631
    remains an explicit wrong-source finding.; PMID:19844578: UNREACHABLE; Exact native
    MED identity/title/DOI and returned PMC field were reviewed after bulk eutils414
    transport failure. Resolving an identifier does not certify attached biology;
    the unrelated Ras PMID20080631 remains an explicit wrong-source finding.; PMID:20304968:
    UNREACHABLE; Exact native MED identity/title/DOI and returned PMC field were reviewed
    after bulk eutils414 transport failure. Resolving an identifier does not certify
    attached biology; the unrelated Ras PMID20080631 remains an explicit wrong-source
    finding.; PMID:22928045: UNREACHABLE; Exact native MED identity/title/DOI and
    returned PMC field were reviewed after bulk eutils414 transport failure. Resolving
    an identifier does not certify attached biology; the unrelated Ras PMID20080631
    remains an explicit wrong-source finding.; PMID:23572529: UNREACHABLE; Exact native
    MED identity/title/DOI and returned PMC field were reviewed after bulk eutils414
    transport failure. Resolving an identifier does not certify attached biology;
    the unrelated Ras PMID20080631 remains an explicit wrong-source finding.; PMID:24267892:
    UNREACHABLE; Exact native MED identity/title/DOI and returned PMC field were reviewed
    after bulk eutils414 transport failure. Resolving an identifier does not certify
    attached biology; the unrelated Ras PMID20080631 remains an explicit wrong-source
    finding.; PMID:28616951: UNREACHABLE; Exact native MED identity/title/DOI and
    returned PMC field were reviewed after bulk eutils414 transport failure. Resolving
    an identifier does not certify attached biology; the unrelated Ras PMID20080631
    remains an explicit wrong-source finding.; PMID:31048338: UNREACHABLE; Exact native
    MED identity/title/DOI and returned PMC field were reviewed after bulk eutils414
    transport failure. Resolving an identifier does not certify attached biology;
    the unrelated Ras PMID20080631 remains an explicit wrong-source finding.; PMID:7934888:
    UNREACHABLE; Exact native MED identity/title/DOI and returned PMC field were reviewed
    after bulk eutils414 transport failure. Resolving an identifier does not certify
    attached biology; the unrelated Ras PMID20080631 remains an explicit wrong-source
    finding.; cellstructuremech:carboxysome_shell: SKIPPED; Exact current local shell
    identity occurs once in an ignored-inclusive maintained-corpus identifier search
    and is a frozen reviewed input. This does not infer exhaustive ontology absence.
    Native source checks are separately scoped; skipped or unreachable identifiers
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
  topic: Shell structural identity and local identifier
  outcome: supported
  target_ids:
  - cellstructuremech:carboxysome_shell
  summary: The protein shell is distinct from the complete enzyme-loaded carboxysome,
    correctly part of GO0031470. The local exact identifier is valid; GO0043886 is
    a molecular function, and neither it nor the whole-carboxysome term should replace
    the shell identity.
  evidence_ids:
  - record
  - micro42-go
  - micro42-SL0034
  - micro42-go-shell-search
  - micro42-go-carboxysome-children
  - micro42-legacy-PMC6022854
  - micro42-body-PMC1872035
- assessment_id: components
  area: grounding
  topic: H/T/P architectural cohorts
  outcome: supported
  target_ids:
  - cellstructuremech:carboxysome_shell
  summary: The shell-only constituent boundary and three protein classes are supported.
    Verified native domain/family scopes justify withholding a single exact grounding
    for these carboxysome-only combined cohorts; the broader BMC-P family appropriate
    to generic BMC cannot be forced here.
  evidence_ids:
  - record
  - micro42-legacy-PMC6022854
  - micro42-legacy-PMC3668761
  - micro42-body-PMC3272956
  - micro42-IPR000249
  - micro42-IPR004992
  - micro42-IPR014076
  - micro42-IPR014077
  - micro42-IPR046380
  - micro42-IPR046387
  - micro42-IPR050575
  - micro42-IPR044870
  - micro42-PF00936
  - micro42-PF03319
- assessment_id: necessity
  area: grounding
  topic: Vertex closure versus structure formation
  outcome: concern
  target_ids:
  - cellstructuremech:carboxysome_shell
  summary: The unqualified BMC-P ESSENTIAL label conflicts with native csoS4AB mutant
    carboxysomes that still form, mostly normal-looking but physiologically compromised.
    This does not deny a requirement for normal closure or beta-specific CcmL roles.
  evidence_ids:
  - record
  - schema
  - micro42-body-PMC2760150
  - micro42-legacy-PMC3425506
- assessment_id: remaining-necessity
  area: grounding
  topic: Other grouped formation dependencies
  outcome: unknown
  target_ids:
  - cellstructuremech:carboxysome_shell
  summary: H is the principal facet material; T roles differ among CcmO, CcmP and
    CsoS1D. CONDITIONAL does not establish a necessity condition for every T paralog
    across taxa, and intact-particle structure alone is insufficient for such an inference.
  evidence_ids:
  - record
  - schema
  - micro42-legacy-PMC6022854
  - micro42-legacy-PMC3425506
  - micro42-legacy-PMC3668761
  - micro42-body-PMC3272956
- assessment_id: proteins
  area: grounding
  topic: Exact accession and source-organism joins
  outcome: supported
  target_ids:
  - cellstructuremech:carboxysome_shell
  summary: All named examples resolve to their correct reviewed proteins/taxa and
    annotation references. The H. neapolitanus CsoS1D example is explicitly an identity
    example; Roberts2012 directly tests Prochlorococcus, and the native annotation
    distinction is preserved.
  evidence_ids:
  - record
  - micro42-body-PMC3272956
  - micro42-up-D0KZ73
  - micro42-up-O85043
  - micro42-up-O85044
  - micro42-up-P45689
  - micro42-up-P46205
  - micro42-up-Q03511
  - micro42-up-Q03512
  - micro42-up-Q31QW7
  - micro42-pmid17675289
  - micro42-pmid18258595
  - micro42-pmid18292340
  - micro42-pmid19844578
  - micro42-pmid20304968
  - micro42-pmid22928045
  - micro42-pmid23572529
  - micro42-pmid24267892
  - micro42-pmid28616951
  - micro42-pmid31048338
  - micro42-pmid7934888
- assessment_id: scope-function
  area: scope
  topic: Distribution, examples and barrier function
  outcome: supported
  target_ids:
  - cellstructuremech:carboxysome_shell
  summary: Bacterial occurrence is qualified; native H. neapolitanus and Syn7942 studies
    support the examples and vertex/CO2 barrier mechanism. Pore size, sulfate binding,
    computational fitting and inferred gating remain distinguished from direct transport-rate
    measurement.
  evidence_ids:
  - record
  - micro42-legacy-PMC6022854
  - micro42-legacy-PMC3811607
  - micro42-body-PMC2760150
  - micro42-body-PMC1872035
  - micro42-legacy-PMC3668761
  - micro42-tax1140
  - micro42-tax2
  - micro42-tax555778
  - micro42-tax927
- assessment_id: graph
  area: graph
  topic: Coarse construction and permeability model
  outcome: concern
  target_ids:
  - cellstructuremech:carboxysome_shell
  summary: H facets, T incorporation, P capping and permeability form a source-supported
    coarse model. One edge citation overstates isolated CcmP crystallography as resolution
    inside the native shell; membership is separately supported by native colocalization.
  evidence_ids:
  - record
  - micro42-legacy-PMC6022854
  - micro42-body-PMC1872035
  - micro42-legacy-PMC3668761
  - micro42-body-PMC2760150
- assessment_id: coverage
  area: completeness
  topic: Whole target, history and excluded lumen cargo
  outcome: supported
  target_ids:
  - cellstructuremech:carboxysome_shell
  summary: The complete target and histories were read. Excluding Rubisco/CA/internal
    scaffolds from the shell-only molecular inventory is justified. No image or verbatim
    snippet occurs here; optional exhaustive paralog inventories do not constitute
    findings.
  evidence_ids:
  - record
  - micro42-legacy-PMC6022854
  - micro42-legacy-PMC3811607
findings:
- finding_id: F1
  issue_key: carboxysome-shell-vertex-formation-essentiality
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Do not equate vertex closure with obligatory shell formation
  description: The BMC-P cohort has ESSENTIAL formation status, but cited Cai2009
    csoS4AB double mutants still produce mostly normal-looking carboxysomes and some
    elongated shells. Their poor ambient-CO2 growth and leakage barrier defect establish
    physiological importance rather than complete inability to form the structure.
  target_ids:
  - cellstructuremech:carboxysome_shell
  field_paths:
  - components[2].essentiality
  evidence_ids:
  - record
  - schema
  - micro42-body-PMC2760150
  - micro42-legacy-PMC3425506
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/microcompartment/carboxysome_shell.yaml
    role: maintained scientific record
  rule_id: Exact source scope, protein grounding and formation-specific essentiality
  native_severity: major
  normalization_reason: This formal universal assembly dependency is directly contradicted
    by native retained structures, not just missing deletion evidence; subtle geometric
    and functional defects remain acknowledged.
- finding_id: F2
  issue_key: carboxysome-shell-ccmp-structure-context
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Separate isolated CcmP structure from in-shell placement
  description: The graph source note says Cai2013 resolved CcmP as stacked trimers
    in the beta-carboxysome shell. The crystal structures are of recombinant isolated
    CcmP; native colocalization supports membership, while docking models placement
    in the shell.
  target_ids:
  - cellstructuremech:carboxysome_shell
  field_paths:
  - causal_graphs[0].edges[1].evidence[0].notes
  evidence_ids:
  - record
  - micro42-legacy-PMC3668761
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/microcompartment/carboxysome_shell.yaml
    role: maintained scientific record
  rule_id: Exact source scope, protein grounding and formation-specific essentiality
  native_severity: minor
  normalization_reason: The stacked-trimer architecture and shell membership are supported;
    the error is a bounded inflation of the experimental structural context.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - cellstructuremech:carboxysome_shell
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/microcompartment/carboxysome_shell.yaml
    role: maintained scientific record
  description: Use a condition/taxon-qualified formation label and preserve closure/CO2-barrier
    roles. Do not infer that surviving mutant particles are fully normal or fully
    functional.
  acceptance_checks:
  - Preserve exact supported identity, experimental organism and native versus recombinant
    context.
  - Attach source-specific evidence to each changed claim and retain historical provenance.
  - Native schema, strict, CURIE, protein and graph checks pass as applicable.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - cellstructuremech:carboxysome_shell
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/microcompartment/carboxysome_shell.yaml
    role: maintained scientific record
  description: State isolated recombinant CcmP crystallography, native colocalization
    and modelled shell incorporation separately while retaining the supported architecture.
  acceptance_checks:
  - Preserve exact supported identity, experimental organism and native versus recombinant
    context.
  - Attach source-specific evidence to each changed claim and retain historical provenance.
  - Native schema, strict, CURIE, protein and graph checks pass as applicable.
limitations:
- Reading extents are specified per source. Several native annotation citations were
  checked at complete-abstract level without claiming unread article bodies or supplemental
  datasets.
- Cai2009 mutant particles retain assembly with defects; the result does not establish
  normal icosahedral geometry or functional closure. Specific beta-carboxysome CcmL
  requirements remain distinct.
- The exact native GO query is bounded, not proof that no future or unqueried shell
  term exists. Local identity is preserved; no molecular-function near-match is substituted.
- No raw figure pixels were reanalysed for this target. Crystal geometry, static conformers
  and shell docking do not establish dynamic transport rates in vivo.
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
