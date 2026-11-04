# Source-backed review of bam protein complex

- Review: 20261022T044323Z-bam-protein-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T04:25:38Z
- Finished UTC: 2026-10-22T04:43:23Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The BAM identity, five exact constituent families/proteins, E. coli experimental example, approximate mass and nonmechanistic folding/insertion outline are supported. No concrete curation defect was found; unknown formation necessity, model/state boundaries and reading limits remain explicit.

## Scope And Provenance

Exactly one complete target; no neighboring scientific-record verdict is imported. Exact authority, all current component/function/graph/source placements, taxonomic scope, formation semantics, history and discussions were reviewed.

Selection: Batch45 fixed strict path order, index 7; exactly one maintained target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:1990063 | data/structures/other/bam_protein_complex.yaml | maintained | Bam protein complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:1990063 | Focused validator passed. |
| Focused native strict | passed | True | GO:1990063 | Focused validator passed. |
| Focused native proteins | passed | True | GO:1990063 | Read-only native check passed; claim-level protein/edge support evaluated separately. |
| Focused native graphs | passed | True | GO:1990063 | Read-only native check passed; claim-level protein/edge support evaluated separately. |
| Claim-level scientific review | passed | True | GO:1990063 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:1990063 | 22 of 29 collected target identifiers returned OK. PMID:15851030: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:16079137: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:17404237: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:23882017: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:24619089: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:26900875: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:26901871: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:1990063 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:1990063 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:1990063 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:1990063 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:1990063 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### BAM identity and membrane hierarchy

identity: supported. Targets: GO:1990063.

The five-protein E. coli BAM example fits GO:1990063. Outer-membrane protein complex is a correct definition-based parent interpretation, while the fresh native is_a-only response does not assert that particular edge. Outer-membrane parthood is supported separately. No wrong sibling, chaperone or standalone protein replaces the assembly.

### Five exact constituent families and subcomplexes

grounding: supported. Targets: GO:1990063.

BamA/B/C/D/E are supported mature constituents, with five exact family CURIEs. The E. coli BamAB and BamCDE purification, ACDE crystal specimen and intact-five laterally open cryoEM are kept distinct. Accessory roles and periplasmic lipoprotein-ring wording are supported; SurA remains associated folding machinery outside the stable five-member component inventory.

### Native protein identities, gene queries and evidence references

grounding: supported. Targets: GO:1990063.

All five reviewed accessions resolve to their named Bam proteins in taxon83333 with matching gene symbols/aliases and exact family cross-references. Full native location/evidence joins plus the cited PMID identities/abstracts support the annotation notes. BamB/BamC one-hit reviewed-query statements match the current exact responses. Direct study findings, native annotation assertions and by-similarity/proposed interpretations are not collapsed into one evidence tier.

### Formation necessity remains unknown

scope: unknown. Targets: GO:1990063.

All five components retain UNKNOWN, appropriately avoiding conversion of viability, folding efficiency or activity defects into proof of complex-formation necessity. Native essential/accessory descriptions and the all-five efficient-OmpT assay do not by themselves answer the schema assembly-necessity question for every lineage.

### Diderm bacterial scope and recombinant contexts

scope: supported. Targets: GO:1990063.

The Bacteria VARIABLE row explicitly distinguishes diderm presence from monoderm absence rather than claiming every bacterium has BAM. Canonical E. coli species562 and reference K-12 strain83333 are correct. The Hagan2011 complete review abstract supports broad Gram-negative function; detailed primary systems are E. coli-derived purified/recombinant contexts, with BL21(DE3),HDB150 and plasmid-host details not replaced by the reference accession strain.

### Beta-barrel folding and insertion

evidence: supported. Targets: GO:1990063.

The purified proteoliposome experiment directly supports OmpT assembly by BAM with SurA and LPS assay requirements. Subsequent structures and crosslink experiments support the bounded functional model and conformational flexibility. The record does not claim a universally proven atomic trajectory, ATP-driven reaction or SurA membership.

### Approximate203kDa intact E. coli complex

quantity: supported. Targets: GO:1990063.

The reported molecular_mass203kDa is appropriately approximate and tied to the intact E. coli five-subunit example. Iadanza native MS supports the predominant observed mass and composition; minor two-BamE species and detergent/recombinant context prevent treating this as an invariant mass for all bacterial BAM systems.

### Explicitly nonmechanistic functional outline

graph: supported. Targets: GO:1990063.

All seven nodes/edges were read. Family/cohort actors, complex, substrate/product and membrane remain distinct; the graph summarizes organization, folding/insertion and a sampled laterally open state without claiming a complete experimentally resolved pathway. The accessory cohort xrefs are examples, not an exhaustive-every-member promise. Gu four-subunit and Iadanza intact-five observations are not conflated.

### Full target and source placement

completeness: supported. Targets: GO:1990063.

Every component, example, quantity, function, graph edge, discussion and historical entry was assessed. Five verified proteins/families cover the named component inventory. No automatic finding is assigned to generic substrate examples or optional images. Historical reviews and current source limitations are preserved; source notes do not require unavailable bodies to prove every cited annotation anew.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/bam_protein_complex.yaml; Complete maintained YAML; all components, source notes, graphs, discussions and historical entries | context_only | The entire maintained target was read; no scientific record was changed. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent; ComponentTypeEnum; EssentialityEnum; graph scopes | context_only | ComponentTypeEnum distinguishes LIPID from the permitted OTHER composite class. ESSENTIAL concerns failure of structure formation, not merely loss of catalytic or transport function. |
| curation | docs/CURATION.md; Components; groundings; associated machinery and chaperone boundaries | context_only | Components are taxon-agnostic molecular families/classes; exact family grounding is preferred when verified. Mature constituents and assembled-structure maintenance machinery differ from transient preassembly chaperones. |
| micro45-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097691,GO:0061701,GO:1903561,GO:0009279,GO:1990063,GO:0106234; Exact complete entries GO:1990063, GO:0106234 and GO:0009279: id/name/isObsolete/definition/synonyms/children; other returned vesicle terms not used. | supports | GO:1990063 is the active BAM cellular-component complex, with the E. coli five-protein definition and described BamAB/BamCDE organization. GO:0106234 denotes an outer-membrane protein complex and GO:0009279 the outer membrane. The proposed parent is definition-supported biological classification; this combined response does not establish a native is_a edge to GO:0106234. |
| micro45-bam-isa | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990063/ancestors?relations=is_a; Exact QuickGO ancestor response for GO:1990063, relations=is_a; inspected entire result. | supports | The returned is_a-only ancestry contains protein-containing-complex ancestors but does not contain GO:0106234. This is an ontology-relation limitation, not evidence that the outer-membrane-complex biological classification is false. |
| micro45-bam-partof | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990063/ancestors?relations=part_of; Exact QuickGO GO:1990063 ancestor response, requested relations=part_of; entire result. | supports | The native requested part_of ancestry includes GO:0009279, supporting outer-membrane containment; the response is a transitive ancestor list, not a claim that every listed relationship is direct. |
| micro45-tax2 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2; Complete taxId/scientificName/rank/lineage/otherNames. | supports | ENA taxId 2 identifies Bacteria at rank domain; aliases and lineage match the record. Identity alone is not prevalence or experimental-condition evidence. |
| micro45-tax562 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562; Complete taxId/scientificName/rank/lineage/otherNames. | supports | ENA taxId 562 identifies Escherichia coli at rank species; aliases and lineage match the record. Identity alone is not prevalence or experimental-condition evidence. |
| micro45-tax83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Complete taxId/scientificName/rank/lineage/otherNames. | supports | ENA taxId 83333 identifies Escherichia coli K-12 at rank strain; aliases and lineage match the record. Identity alone is not prevalence or experimental-condition evidence. |
| micro45-hagan2010-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1126%2Fscience.1188919%22&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED20378773: Reconstitution of outer membrane protein assembly from purified components. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro45-hagan2011-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1146%2Fannurev-biochem-061408-144611%22&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED21370981: β-Barrel membrane protein assembly by the Bam complex. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro45-gu2016-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fnature17199%22&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED26901871: Structural basis of outer membrane protein insertion by the BAM complex. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro45-iadanza2016-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fncomms12865%22&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED27686148: Lateral opening in the intact β-barrel assembly machinery captured by cryo-EM. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro45-bakelar2016-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1126%2Fscience.aad3460%22&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED26744406: The structure of the β-barrel assembly machinery complex. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro45-pmid16079137 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16079137+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED16079137: Protein complexes of the Escherichia coli cell envelope. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro45-pmid23882017 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A23882017+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED23882017: Receptor polymorphism restricts contact-dependent growth inhibition to members of the same species. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro45-pmid24619089 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A24619089+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED24619089: Structural and functional analysis of the β-barrel domain of BamA from Escherichia coli. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro45-pmid15851030 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15851030+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED15851030: Identification of a multicomponent complex required for outer membrane biogenesis in Escherichia coli. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro45-pmid26900875 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A26900875+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED26900875: Structure of the BAM complex and its implications for biogenesis of outer-membrane proteins. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro45-pmid17404237 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A17404237+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED17404237: Lipoprotein SmpA is a component of the YaeT complex that assembles outer membrane proteins in Escherichia coli. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro45-protein-P0A940 | https://rest.uniprot.org/uniprotkb/P0A940.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. Full FUNCTION and SUBUNIT comments also inspected. | supports | P0A940 is UniProtKB reviewed (Swiss-Prot), taxon 83333, genes ['bamA']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. Complete FUNCTION and SUBUNIT comments were read; these preserve accessory-subunit, proposed-gating and receptor-function distinctions. |
| micro45-protein-P77774 | https://rest.uniprot.org/uniprotkb/P77774.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. Full FUNCTION and SUBUNIT comments also inspected. | supports | P77774 is UniProtKB reviewed (Swiss-Prot), taxon 83333, genes ['bamB']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. Complete FUNCTION and SUBUNIT comments were read; these preserve accessory-subunit, proposed-gating and receptor-function distinctions. |
| micro45-protein-P0A903 | https://rest.uniprot.org/uniprotkb/P0A903.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. Full FUNCTION and SUBUNIT comments also inspected. | supports | P0A903 is UniProtKB reviewed (Swiss-Prot), taxon 83333, genes ['bamC']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. Complete FUNCTION and SUBUNIT comments were read; these preserve accessory-subunit, proposed-gating and receptor-function distinctions. |
| micro45-protein-P0AC02 | https://rest.uniprot.org/uniprotkb/P0AC02.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. Full FUNCTION and SUBUNIT comments also inspected. | supports | P0AC02 is UniProtKB reviewed (Swiss-Prot), taxon 83333, genes ['bamD']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. Complete FUNCTION and SUBUNIT comments were read; these preserve accessory-subunit, proposed-gating and receptor-function distinctions. |
| micro45-protein-P0A937 | https://rest.uniprot.org/uniprotkb/P0A937.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. Full FUNCTION and SUBUNIT comments also inspected. | supports | P0A937 is UniProtKB reviewed (Swiss-Prot), taxon 83333, genes ['bamE']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. Complete FUNCTION and SUBUNIT comments were read; these preserve accessory-subunit, proposed-gating and receptor-function distinctions. |
| micro45-ipr-IPR023707 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR023707/; Native InterPro metadata: accession/name/type/description; hierarchy and member_databases; description metadata. | supports | IPR023707 is the specific BamA family; exact accession/name/type/description and member-database metadata were inspected, consistent with the component and its native protein cross-reference. This family identity alone is not an assembly-necessity experiment. |
| micro45-ipr-IPR017687 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017687/; Native InterPro metadata: accession/name/type/description; hierarchy and member_databases; description metadata. | supports | IPR017687 is the specific BamB family; exact accession/name/type/description and member-database metadata were inspected, consistent with the component and its native protein cross-reference. This family identity alone is not an assembly-necessity experiment. |
| micro45-ipr-IPR014524 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014524/; Native InterPro metadata: accession/name/type/description; hierarchy and member_databases; description metadata. | supports | IPR014524 is the specific BamC family; exact accession/name/type/description and member-database metadata were inspected, consistent with the component and its native protein cross-reference. This family identity alone is not an assembly-necessity experiment. |
| micro45-ipr-IPR017689 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017689/; Native InterPro metadata: accession/name/type/description; hierarchy and member_databases; description metadata. | supports | IPR017689 is the specific BamD family; exact accession/name/type/description and member-database metadata were inspected, consistent with the component and its native protein cross-reference. This family identity alone is not an assembly-necessity experiment. |
| micro45-ipr-IPR026592 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR026592/; Native InterPro metadata: accession/name/type/description; hierarchy and member_databases; description metadata. | supports | IPR026592 is the specific BamE family; exact accession/name/type/description and member-database metadata were inspected, consistent with the component and its native protein cross-reference. This family identity alone is not an assembly-necessity experiment. |
| micro45-gene-bamA | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AbamA%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete retained reviewed gene_exact/taxon83333 native query response; scope is the exact URL request, not a local filesystem search. | supports | The exact reviewed gene/taxon83333 request returned one entry for bamA; all returned accession/gene-name/alias/taxon fields were inspected. Current single-hit claims for BamB and BamC are therefore supported. This bounded endpoint result is not a whole-UniProt absence statement. |
| micro45-gene-bamB | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AbamB%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete retained reviewed gene_exact/taxon83333 native query response; scope is the exact URL request, not a local filesystem search. | supports | The exact reviewed gene/taxon83333 request returned one entry for bamB; all returned accession/gene-name/alias/taxon fields were inspected. Current single-hit claims for BamB and BamC are therefore supported. This bounded endpoint result is not a whole-UniProt absence statement. |
| micro45-gene-bamC | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AbamC%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete retained reviewed gene_exact/taxon83333 native query response; scope is the exact URL request, not a local filesystem search. | supports | The exact reviewed gene/taxon83333 request returned one entry for bamC; all returned accession/gene-name/alias/taxon fields were inspected. Current single-hit claims for BamB and BamC are therefore supported. This bounded endpoint result is not a whole-UniProt absence statement. |
| micro45-gene-bamD | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AbamD%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete retained reviewed gene_exact/taxon83333 native query response; scope is the exact URL request, not a local filesystem search. | supports | The exact reviewed gene/taxon83333 request returned one entry for bamD; all returned accession/gene-name/alias/taxon fields were inspected. Current single-hit claims for BamB and BamC are therefore supported. This bounded endpoint result is not a whole-UniProt absence statement. |
| micro45-gene-bamE | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AbamE%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete retained reviewed gene_exact/taxon83333 native query response; scope is the exact URL request, not a local filesystem search. | supports | The exact reviewed gene/taxon83333 request returned one entry for bamE; all returned accession/gene-name/alias/taxon fields were inspected. Current single-hit claims for BamB and BamC are therefore supported. This bounded endpoint result is not a whole-UniProt absence statement. |
| micro45-hagan2010-legacy | https://pmc.ncbi.nlm.nih.gov/articles/PMC2873164/?report=xml; Genuine HTML complete main-text paragraphs P2–P10; abstract independently read in MED record. No figure pixels, full figure captions or supplementary Methods inspected. | supports | Purified E. coli BamAB and BamCDE were combined in proteoliposomes with SurA/OmpT; fluorescence, heat-modifiability and carbonate-resistance assays support folding and membrane insertion. All-five versus partial-complex controls are activity-context evidence. SurA is added separately and is not a sixth stable BAM constituent. The older inferred BamE copy number was unresolved1or2, not a universal stoichiometry claim. |
| micro45-bakelar2016-legacy | https://pmc.ncbi.nlm.nih.gov/articles/PMC4883095/?report=xml; Genuine HTML complete main-text paragraphs P5–P9. No remaining Results, full Methods, supplementary material or image pixels claimed. | supports | The crystallographic specimen lost BamB during prolonged incubation and was BamACDE; the text explicitly distinguishes the modeled/docked BamB context from the observed ACDE structure. BamC has unresolved globular domains. Direct A/D/E/C interaction descriptions support the bounded subcomplex note. |
| micro45-iadanza2016-legacy | https://pmc.ncbi.nlm.nih.gov/articles/PMC5056442/?report=xml; Genuine HTML complete sec2,sec3,sec8,sec11,sec12 and entire sec16 including sec17/18. Methods use pJH114/BL21(DE3), E. coli polar-lipid proteoliposomes and SurA/OmpT. No figure pixels, remaining Results/Discussion or supplementary tables inspected. | supports | Native MS gives a predominant1:1:1:1:1 ABCDE complex of203456±22Da (predicted203218Da), with minor two-BamE species. Intact-five cryoEM in detergent captures a laterally open conformation; partial BamC density and model assembly limits remain explicit. Crosslink/OmpT assays and BL21(DE3)expression/reconstitution methods are distinct from the K-12 reference-protein identities. |
| micro45-gu2016-author | https://ueaeprints.uea.ac.uk/id/eprint/57584/1/BAM_Nature_Gu_29012016_2_change_Figure_legends_3_revised_accepted.pdf; Genuine university-hosted accepted PDF printed pp1–8 (continuous main text through initial BamA–BamD interaction section); complete Methods Cloning, expression and purification of BAM complex, printed pp27–29. No figure pixels or later main-text/Methods sections claimed. SHA identifies full retained PDF, not derivative text. | supports | The accepted primary manuscript distinguishes inward-open five-subunit and laterally open four-subunit crystal complexes, periplasmic A/C/D/E ring organization and crosslink/function experiments. It does not establish that every observed conformation contains five subunits. The inspected cloning/purification method uses HDB150/pJH114, additional bamB expression and DH5alpha plasmid preparation, not an assumed match to the K-12 reference-protein taxon. |
| micro45-uo0000222 | https://www.ebi.ac.uk/ols4/api/ontologies/uo/terms?obo_id=UO:0000222; Complete OLS term identity/definition/obo_id/synonyms/is_obsolete. | supports | UO:0000222 is active kilodalton, symbol kDa, defined as1000daltons; it matches the recorded approximate203 molecular-mass unit. |
| micro45-hagan2011-publisher | https://doi.org/10.1146/annurev-biochem-061408-144611; Complete retained response; status/content inspected against receipt. | context_only | HTTP 403 returned an access-denied HTML response, not an inspected paper body. Metadata/abstract or a separately specified genuine body is used instead. |
| micro45-gu2016-publisher | https://doi.org/10.1038/nature17199; Complete retained response; status/content inspected against receipt. | context_only | HTTP 200 returned a 3038-byte Client Challenge HTML page, not the paper body. Metadata/abstract or a separately specified genuine body is used instead. |
| schema-result | just validate data/structures/other/bam_protein_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/bam_protein_complex.yaml |
| strict-result | just validate-strict data/structures/other/bam_protein_complex.yaml --out /private/tmp/cellstructure-batch45-20261022-mptgrq24/bam_protein_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/bam_protein_complex.yaml --out /private/tmp/cellstructure-batch45-20261022-mptgrq24/bam_protein_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch45-20261022-mptgrq24/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch45-20261022-mptgrq24/bam_protein_complex-strict.tsv |
| native-proteins | /private/tmp/cellstructure-batch45-20261022-mptgrq24/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/other/bam_protein_complex.yaml; Complete read-only focused native proteins log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-graphs | /private/tmp/cellstructure-batch45-20261022-mptgrq24/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/bam_protein_complex.yaml; Complete read-only focused native graphs log | supports | data/structures/other/bam_protein_complex.yaml  (GO:1990063)<br>  bam_omp_folding_and_insertion	unfolded_omp_substrate	UNANCHORED_NO_UNIPROT	unfolded outer-membrane beta-barrel protein substrate<br>  bam_omp_folding_and_insertion	bam_a	COVERED	-&gt;bam_a (UniProtKB:P0A940)<br>  bam_omp_folding_and_insertion	bam_b_to_e_lipoproteins	UNANCHORED_WITH_UNIPROT	BamB-E lipoproteins (UniProtKB:P77774, UniProtKB:P0A903, UniProtKB:P0AC02)<br>  bam_omp_folding_and_insertion	outer_membrane_beta_barrel	UNANCHORED_NO_UNIPROT	assembled outer-membrane beta-barrel protein<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     2  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     1  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     1  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     4  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/other/bam_protein_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 22 of 29 collected target identifiers returned OK. PMID:15851030: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:16079137: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:17404237: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:23882017: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:24619089: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:26900875: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:26901871: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Hagan2011 was read only through its complete native abstract; publisher returned403. Gu publisher returned HTTP200 Client Challenge, but a genuine accepted primary manuscript was separately recovered and read only at pp1–8 and cloning/expression/purification Methods pp27–29.
- Hagan2010 body P2–P10, Bakelar2016 P5–P9 and Iadanza2016 sec2/3/8/11/12/16 including17/18 define the actual primary-body scope. No raw structural pixels, figure panels, deposited maps, omitted Methods or supplementary tables were inspected.
- Six additional annotation papers were verified through complete native MED abstracts only; exact UniProt evidence joins are annotation evidence, not a claim that those complete paper bodies were read.
- The current is_a-only GO ancestry does not contain GO:0106234; that parent is retained as definition-supported biological classification. UNKNOWN formation necessity and cross-lineage stoichiometry are not resolved by activity or a predominant native-MS species.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User expressly requests one review for every unreviewed record, including scientifically clean records.
- iModulonDB is not applicable to these complex identity, protein family, assembly, vesicle carriage and enzyme or transport claims.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T044323Z-bam-protein-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-backed review of bam protein complex
started_at: '2026-10-22T04:25:38Z'
finished_at: '2026-10-22T04:43:23Z'
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
summary: The BAM identity, five exact constituent families/proteins, E. coli experimental
  example, approximate mass and nonmechanistic folding/insertion outline are supported.
  No concrete curation defect was found; unknown formation necessity, model/state
  boundaries and reading limits remain explicit.
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
  - path: data/structures/other/bam_protein_complex.yaml
    sha256: caa3620dc7868afb69744609d3f28450d13ce822789d33224fab2e805a49a8dd
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
- target_id: GO:1990063
  path: data/structures/other/bam_protein_complex.yaml
  label: Bam protein complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/bam_protein_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete target; no neighboring scientific-record verdict
    is imported. Exact authority, all current component/function/graph/source placements,
    taxonomic scope, formation semantics, history and discussions were reviewed.
  selection: Batch45 fixed strict path order, index 7; exactly one maintained target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:1990063
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:1990063
  command: just validate data/structures/other/bam_protein_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:1990063
  command: just validate-strict data/structures/other/bam_protein_complex.yaml --out
    /private/tmp/cellstructure-batch45-20261022-mptgrq24/bam_protein_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-proteins
  name: Focused native proteins
  status: passed
  required: true
  target_ids:
  - GO:1990063
  command: /private/tmp/cellstructure-batch45-20261022-mptgrq24/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/bam_protein_complex.yaml
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
  - GO:1990063
  command: /private/tmp/cellstructure-batch45-20261022-mptgrq24/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/bam_protein_complex.yaml
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
  - GO:1990063
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - micro45-go
  - micro45-bam-isa
  - micro45-bam-partof
  - micro45-tax2
  - micro45-tax562
  - micro45-tax83333
  - micro45-hagan2010-meta
  - micro45-hagan2011-meta
  - micro45-gu2016-meta
  - micro45-iadanza2016-meta
  - micro45-bakelar2016-meta
  - micro45-pmid16079137
  - micro45-pmid23882017
  - micro45-pmid24619089
  - micro45-pmid15851030
  - micro45-pmid26900875
  - micro45-pmid17404237
  - micro45-protein-P0A940
  - micro45-protein-P77774
  - micro45-protein-P0A903
  - micro45-protein-P0AC02
  - micro45-protein-P0A937
  - micro45-ipr-IPR023707
  - micro45-ipr-IPR017687
  - micro45-ipr-IPR014524
  - micro45-ipr-IPR017689
  - micro45-ipr-IPR026592
  - micro45-gene-bamA
  - micro45-gene-bamB
  - micro45-gene-bamC
  - micro45-gene-bamD
  - micro45-gene-bamE
  - micro45-hagan2010-legacy
  - micro45-bakelar2016-legacy
  - micro45-iadanza2016-legacy
  - micro45-gu2016-author
  - micro45-uo0000222
  - micro45-hagan2011-publisher
  - micro45-gu2016-publisher
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:1990063
  summary: '22 of 29 collected target identifiers returned OK. PMID:15851030: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force.; PMID:16079137:
    UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected
    after the bulk eutils414 transport failure. Identity resolution does not certify
    every attached biological claim; declared abstract/body reading scope remains
    in force.; PMID:17404237: UNREACHABLE; Exact native Europe PMC MED identifier,
    title and DOI were inspected after the bulk eutils414 transport failure. Identity
    resolution does not certify every attached biological claim; declared abstract/body
    reading scope remains in force.; PMID:23882017: UNREACHABLE; Exact native Europe
    PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport
    failure. Identity resolution does not certify every attached biological claim;
    declared abstract/body reading scope remains in force.; PMID:24619089: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force.; PMID:26900875:
    UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected
    after the bulk eutils414 transport failure. Identity resolution does not certify
    every attached biological claim; declared abstract/body reading scope remains
    in force.; PMID:26901871: UNREACHABLE; Exact native Europe PMC MED identifier,
    title and DOI were inspected after the bulk eutils414 transport failure. Identity
    resolution does not certify every attached biological claim; declared abstract/body
    reading scope remains in force. Native source checks are separately scoped; skipped
    or unreachable identifiers are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - micro45-pmid15851030
  - micro45-pmid16079137
  - micro45-pmid17404237
  - micro45-pmid23882017
  - micro45-pmid24619089
  - micro45-pmid26900875
  - micro45-gu2016-meta
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:1990063
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch45 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:1990063
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch45 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:1990063
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch45 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:1990063
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch45 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:1990063
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
    and current batch45 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/bam_protein_complex.yaml
  locator: Complete maintained YAML; all components, source notes, graphs, discussions
    and historical entries
  accessed_at: '2026-10-22T04:39:53Z'
  support: context_only
  summary: The entire maintained target was read; no scientific record was changed.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent; ComponentTypeEnum; EssentialityEnum; graph scopes
  accessed_at: '2026-10-22T04:39:53Z'
  support: context_only
  summary: ComponentTypeEnum distinguishes LIPID from the permitted OTHER composite
    class. ESSENTIAL concerns failure of structure formation, not merely loss of catalytic
    or transport function.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Components; groundings; associated machinery and chaperone boundaries
  accessed_at: '2026-10-22T04:39:53Z'
  support: context_only
  summary: Components are taxon-agnostic molecular families/classes; exact family
    grounding is preferred when verified. Mature constituents and assembled-structure
    maintenance machinery differ from transient preassembly chaperones.
- evidence_id: micro45-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097691,GO:0061701,GO:1903561,GO:0009279,GO:1990063,GO:0106234
  locator: 'Exact complete entries GO:1990063, GO:0106234 and GO:0009279: id/name/isObsolete/definition/synonyms/children;
    other returned vesicle terms not used.'
  accessed_at: '2026-10-22T04:32:21.376534Z'
  support: supports
  summary: GO:1990063 is the active BAM cellular-component complex, with the E. coli
    five-protein definition and described BamAB/BamCDE organization. GO:0106234 denotes
    an outer-membrane protein complex and GO:0009279 the outer membrane. The proposed
    parent is definition-supported biological classification; this combined response
    does not establish a native is_a edge to GO:0106234.
  snapshot_sha256: 7039eee9ee3550641584f881c521a22795fc64a1b2b73b12b977d3eb9a8329ba
- evidence_id: micro45-bam-isa
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990063/ancestors?relations=is_a
  locator: Exact QuickGO ancestor response for GO:1990063, relations=is_a; inspected
    entire result.
  accessed_at: '2026-10-22T04:33:37.075192Z'
  support: supports
  summary: The returned is_a-only ancestry contains protein-containing-complex ancestors
    but does not contain GO:0106234. This is an ontology-relation limitation, not
    evidence that the outer-membrane-complex biological classification is false.
  snapshot_sha256: bd4dc08d6bd0f803e3f2eee8f0580914baf2237435a71fc14c81e05fafa5e80e
- evidence_id: micro45-bam-partof
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990063/ancestors?relations=part_of
  locator: Exact QuickGO GO:1990063 ancestor response, requested relations=part_of;
    entire result.
  accessed_at: '2026-10-22T04:33:37.075459Z'
  support: supports
  summary: The native requested part_of ancestry includes GO:0009279, supporting outer-membrane
    containment; the response is a transitive ancestor list, not a claim that every
    listed relationship is direct.
  snapshot_sha256: e33ff357e9e4e891ed09d7f96514fd289cd87e57fc4343acbff8406a1337d214
- evidence_id: micro45-tax2
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2
  locator: Complete taxId/scientificName/rank/lineage/otherNames.
  accessed_at: '2026-10-22T04:32:21.376961Z'
  support: supports
  summary: ENA taxId 2 identifies Bacteria at rank domain; aliases and lineage match
    the record. Identity alone is not prevalence or experimental-condition evidence.
  snapshot_sha256: 314bd7723b8dea04f1840809fb74e06c514664fba9c6a0619e8f12e2a6dceef1
- evidence_id: micro45-tax562
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562
  locator: Complete taxId/scientificName/rank/lineage/otherNames.
  accessed_at: '2026-10-22T04:32:21.378577Z'
  support: supports
  summary: ENA taxId 562 identifies Escherichia coli at rank species; aliases and
    lineage match the record. Identity alone is not prevalence or experimental-condition
    evidence.
  snapshot_sha256: ea038c30da3aab3426b7df16ce7a137cf2985e73d6ad8281971b9c390a74d2a8
- evidence_id: micro45-tax83333
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Complete taxId/scientificName/rank/lineage/otherNames.
  accessed_at: '2026-10-22T04:32:22.130624Z'
  support: supports
  summary: ENA taxId 83333 identifies Escherichia coli K-12 at rank strain; aliases
    and lineage match the record. Identity alone is not prevalence or experimental-condition
    evidence.
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: micro45-hagan2010-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1126%2Fscience.1188919%22&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:32:25.904046Z'
  support: supports
  summary: 'Unique MED20378773: Reconstitution of outer membrane protein assembly
    from purified components. Authors/year/DOI and the complete native abstract were
    inspected. This row establishes bibliographic identity and abstract-level content
    only; detailed experiments require separately specified body evidence.'
  snapshot_sha256: f2a970ca67236be079e274c050122ea916b89e926b632249ab06b2e858074187
- evidence_id: micro45-hagan2011-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1146%2Fannurev-biochem-061408-144611%22&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:32:25.689233Z'
  support: supports
  summary: 'Unique MED21370981: β-Barrel membrane protein assembly by the Bam complex.
    Authors/year/DOI and the complete native abstract were inspected. This row establishes
    bibliographic identity and abstract-level content only; detailed experiments require
    separately specified body evidence.'
  snapshot_sha256: 8a8eec2df3a67dc3701ad1c45291c387b95e637261b446afbcd44e9db95332ce
- evidence_id: micro45-gu2016-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fnature17199%22&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:32:25.925818Z'
  support: supports
  summary: 'Unique MED26901871: Structural basis of outer membrane protein insertion
    by the BAM complex. Authors/year/DOI and the complete native abstract were inspected.
    This row establishes bibliographic identity and abstract-level content only; detailed
    experiments require separately specified body evidence.'
  snapshot_sha256: 06101ac411e63d2c471d32e2ef0b3e6d2b18153b7fc90cf94cf497d71445dc52
- evidence_id: micro45-iadanza2016-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fncomms12865%22&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:32:25.952756Z'
  support: supports
  summary: 'Unique MED27686148: Lateral opening in the intact β-barrel assembly machinery
    captured by cryo-EM. Authors/year/DOI and the complete native abstract were inspected.
    This row establishes bibliographic identity and abstract-level content only; detailed
    experiments require separately specified body evidence.'
  snapshot_sha256: c613d34226da1d2e49d9dd076e137abfe7383c9e2eb7812c74a45b4cda78cf0f
- evidence_id: micro45-bakelar2016-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1126%2Fscience.aad3460%22&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:32:26.072279Z'
  support: supports
  summary: 'Unique MED26744406: The structure of the β-barrel assembly machinery complex.
    Authors/year/DOI and the complete native abstract were inspected. This row establishes
    bibliographic identity and abstract-level content only; detailed experiments require
    separately specified body evidence.'
  snapshot_sha256: 6f4257edae6040ed740b701099fca691dc6c3f8ee37b4dc2f2f3fd9216c86e19
- evidence_id: micro45-pmid16079137
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16079137+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:32:26.334684Z'
  support: supports
  summary: 'Unique MED16079137: Protein complexes of the Escherichia coli cell envelope.
    Authors/year/DOI and the complete native abstract were inspected. This row establishes
    bibliographic identity and abstract-level content only; detailed experiments require
    separately specified body evidence.'
  snapshot_sha256: cf1c57d1a5343edc60d65a0b5d128f9d7b78f0006ac9526b7a31be6d9945918a
- evidence_id: micro45-pmid23882017
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A23882017+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:32:26.536466Z'
  support: supports
  summary: 'Unique MED23882017: Receptor polymorphism restricts contact-dependent
    growth inhibition to members of the same species. Authors/year/DOI and the complete
    native abstract were inspected. This row establishes bibliographic identity and
    abstract-level content only; detailed experiments require separately specified
    body evidence.'
  snapshot_sha256: d1fc76a41efb3d14a5349774a16b7033c4200c9fb052b648065a170ed65738a5
- evidence_id: micro45-pmid24619089
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A24619089+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:32:26.589269Z'
  support: supports
  summary: 'Unique MED24619089: Structural and functional analysis of the β-barrel
    domain of BamA from Escherichia coli. Authors/year/DOI and the complete native
    abstract were inspected. This row establishes bibliographic identity and abstract-level
    content only; detailed experiments require separately specified body evidence.'
  snapshot_sha256: 3bf39231ef314853e692c8623395a61975e81ced049781a81fa178ed3ef25824
- evidence_id: micro45-pmid15851030
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15851030+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:32:26.591545Z'
  support: supports
  summary: 'Unique MED15851030: Identification of a multicomponent complex required
    for outer membrane biogenesis in Escherichia coli. Authors/year/DOI and the complete
    native abstract were inspected. This row establishes bibliographic identity and
    abstract-level content only; detailed experiments require separately specified
    body evidence.'
  snapshot_sha256: fcac0ce0679ddc997acdb7a4dd20bc4fc3487e9879f5f7f993f9135fbd800203
- evidence_id: micro45-pmid26900875
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A26900875+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:32:26.700035Z'
  support: supports
  summary: 'Unique MED26900875: Structure of the BAM complex and its implications
    for biogenesis of outer-membrane proteins. Authors/year/DOI and the complete native
    abstract were inspected. This row establishes bibliographic identity and abstract-level
    content only; detailed experiments require separately specified body evidence.'
  snapshot_sha256: 21c4853857d79e7ca3112664d71a095f0314a09b39cdf403b5a33531904ed6ae
- evidence_id: micro45-pmid17404237
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A17404237+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:32:26.965890Z'
  support: supports
  summary: 'Unique MED17404237: Lipoprotein SmpA is a component of the YaeT complex
    that assembles outer membrane proteins in Escherichia coli. Authors/year/DOI and
    the complete native abstract were inspected. This row establishes bibliographic
    identity and abstract-level content only; detailed experiments require separately
    specified body evidence.'
  snapshot_sha256: 697aece3a60f7f95c8b7253d69d98310ce075dabba1af9eb1617f88b66e89cbe
- evidence_id: micro45-protein-P0A940
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0A940.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references. Full
    FUNCTION and SUBUNIT comments also inspected.
  accessed_at: '2026-10-22T04:32:22.133425Z'
  support: supports
  summary: P0A940 is UniProtKB reviewed (Swiss-Prot), taxon 83333, genes ['bamA'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge. Complete FUNCTION and SUBUNIT comments
    were read; these preserve accessory-subunit, proposed-gating and receptor-function
    distinctions.
  snapshot_sha256: 2ff846ae12669c4bab0ccd5ee26ee045bc2c77b2c49c18bfcf90adaee3a2296d
- evidence_id: micro45-protein-P77774
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P77774.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references. Full
    FUNCTION and SUBUNIT comments also inspected.
  accessed_at: '2026-10-22T04:32:22.136451Z'
  support: supports
  summary: P77774 is UniProtKB reviewed (Swiss-Prot), taxon 83333, genes ['bamB'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge. Complete FUNCTION and SUBUNIT comments
    were read; these preserve accessory-subunit, proposed-gating and receptor-function
    distinctions.
  snapshot_sha256: 2ef03b2f0a01756551013ff513ba85409096bdb8d13b57be1991bd465d1376e1
- evidence_id: micro45-protein-P0A903
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0A903.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references. Full
    FUNCTION and SUBUNIT comments also inspected.
  accessed_at: '2026-10-22T04:32:22.167376Z'
  support: supports
  summary: P0A903 is UniProtKB reviewed (Swiss-Prot), taxon 83333, genes ['bamC'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge. Complete FUNCTION and SUBUNIT comments
    were read; these preserve accessory-subunit, proposed-gating and receptor-function
    distinctions.
  snapshot_sha256: 584c056225b866005264ce4b2288722d06ff5adf60d6f217a65b59e6b0c22c60
- evidence_id: micro45-protein-P0AC02
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0AC02.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references. Full
    FUNCTION and SUBUNIT comments also inspected.
  accessed_at: '2026-10-22T04:32:22.179814Z'
  support: supports
  summary: P0AC02 is UniProtKB reviewed (Swiss-Prot), taxon 83333, genes ['bamD'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge. Complete FUNCTION and SUBUNIT comments
    were read; these preserve accessory-subunit, proposed-gating and receptor-function
    distinctions.
  snapshot_sha256: 97262e786c9e1d055dd17acbcc26d085df95a8e0206f10d3ad247dc545a4902b
- evidence_id: micro45-protein-P0A937
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0A937.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references. Full
    FUNCTION and SUBUNIT comments also inspected.
  accessed_at: '2026-10-22T04:32:22.778928Z'
  support: supports
  summary: P0A937 is UniProtKB reviewed (Swiss-Prot), taxon 83333, genes ['bamE'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge. Complete FUNCTION and SUBUNIT comments
    were read; these preserve accessory-subunit, proposed-gating and receptor-function
    distinctions.
  snapshot_sha256: 4a0d6c264c3eaa5fbb921ec2c0abd09825d2085e08bb12556cce6c15677e5d03
- evidence_id: micro45-ipr-IPR023707
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR023707/
  locator: 'Native InterPro metadata: accession/name/type/description; hierarchy and
    member_databases; description metadata.'
  accessed_at: '2026-10-22T04:32:23.021598Z'
  support: supports
  summary: IPR023707 is the specific BamA family; exact accession/name/type/description
    and member-database metadata were inspected, consistent with the component and
    its native protein cross-reference. This family identity alone is not an assembly-necessity
    experiment.
  snapshot_sha256: 6332e23f488ba575c9b64f72ca33529ea7708cbc683ce6ea8c92d5be517ebda4
- evidence_id: micro45-ipr-IPR017687
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017687/
  locator: 'Native InterPro metadata: accession/name/type/description; hierarchy and
    member_databases; description metadata.'
  accessed_at: '2026-10-22T04:32:23.038803Z'
  support: supports
  summary: IPR017687 is the specific BamB family; exact accession/name/type/description
    and member-database metadata were inspected, consistent with the component and
    its native protein cross-reference. This family identity alone is not an assembly-necessity
    experiment.
  snapshot_sha256: 4a1e68d606e1300e5d42418dc06954d330eea3f450edd6de5feb2edb0d8e091a
- evidence_id: micro45-ipr-IPR014524
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014524/
  locator: 'Native InterPro metadata: accession/name/type/description; hierarchy and
    member_databases; description metadata.'
  accessed_at: '2026-10-22T04:32:23.129882Z'
  support: supports
  summary: IPR014524 is the specific BamC family; exact accession/name/type/description
    and member-database metadata were inspected, consistent with the component and
    its native protein cross-reference. This family identity alone is not an assembly-necessity
    experiment.
  snapshot_sha256: e628a709adce13480ab5a3280fbffc7b8e8af5b546acd438be423992354b0164
- evidence_id: micro45-ipr-IPR017689
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017689/
  locator: 'Native InterPro metadata: accession/name/type/description; hierarchy and
    member_databases; description metadata.'
  accessed_at: '2026-10-22T04:32:23.375371Z'
  support: supports
  summary: IPR017689 is the specific BamD family; exact accession/name/type/description
    and member-database metadata were inspected, consistent with the component and
    its native protein cross-reference. This family identity alone is not an assembly-necessity
    experiment.
  snapshot_sha256: 0f8fe8ba57b5271c42ba4a610111c9a46e8a0731f8c4fb661b1763d36939434e
- evidence_id: micro45-ipr-IPR026592
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR026592/
  locator: 'Native InterPro metadata: accession/name/type/description; hierarchy and
    member_databases; description metadata.'
  accessed_at: '2026-10-22T04:32:23.608980Z'
  support: supports
  summary: IPR026592 is the specific BamE family; exact accession/name/type/description
    and member-database metadata were inspected, consistent with the component and
    its native protein cross-reference. This family identity alone is not an assembly-necessity
    experiment.
  snapshot_sha256: 042bb194391df3d7402d2cce4e49dde1b549d3430d435dfa2a12b49e0b96239d
- evidence_id: micro45-gene-bamA
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AbamA%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete retained reviewed gene_exact/taxon83333 native query response;
    scope is the exact URL request, not a local filesystem search.
  accessed_at: '2026-10-22T04:32:23.613408Z'
  support: supports
  summary: The exact reviewed gene/taxon83333 request returned one entry for bamA;
    all returned accession/gene-name/alias/taxon fields were inspected. Current single-hit
    claims for BamB and BamC are therefore supported. This bounded endpoint result
    is not a whole-UniProt absence statement.
  snapshot_sha256: eedefca132b33d6adebab88357ec41c7c549af0160a80fe342ec9c5c2ed76809
- evidence_id: micro45-gene-bamB
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AbamB%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete retained reviewed gene_exact/taxon83333 native query response;
    scope is the exact URL request, not a local filesystem search.
  accessed_at: '2026-10-22T04:32:23.635420Z'
  support: supports
  summary: The exact reviewed gene/taxon83333 request returned one entry for bamB;
    all returned accession/gene-name/alias/taxon fields were inspected. Current single-hit
    claims for BamB and BamC are therefore supported. This bounded endpoint result
    is not a whole-UniProt absence statement.
  snapshot_sha256: a5fb6bdb8a6d22d3789192420f7891e4f381de850cf4cc724acdffe4383b890e
- evidence_id: micro45-gene-bamC
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AbamC%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete retained reviewed gene_exact/taxon83333 native query response;
    scope is the exact URL request, not a local filesystem search.
  accessed_at: '2026-10-22T04:32:23.714080Z'
  support: supports
  summary: The exact reviewed gene/taxon83333 request returned one entry for bamC;
    all returned accession/gene-name/alias/taxon fields were inspected. Current single-hit
    claims for BamB and BamC are therefore supported. This bounded endpoint result
    is not a whole-UniProt absence statement.
  snapshot_sha256: 073444923c46fbd03e5e35ea4c1d56f51a2e76205a35aee6e9b0d426378fd5f4
- evidence_id: micro45-gene-bamD
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AbamD%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete retained reviewed gene_exact/taxon83333 native query response;
    scope is the exact URL request, not a local filesystem search.
  accessed_at: '2026-10-22T04:32:23.965032Z'
  support: supports
  summary: The exact reviewed gene/taxon83333 request returned one entry for bamD;
    all returned accession/gene-name/alias/taxon fields were inspected. Current single-hit
    claims for BamB and BamC are therefore supported. This bounded endpoint result
    is not a whole-UniProt absence statement.
  snapshot_sha256: 3863cd5db0a7c555cf2dba77d3a52ae3a8ebd3681a6821e8628e854c010497ca
- evidence_id: micro45-gene-bamE
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AbamE%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete retained reviewed gene_exact/taxon83333 native query response;
    scope is the exact URL request, not a local filesystem search.
  accessed_at: '2026-10-22T04:32:24.202578Z'
  support: supports
  summary: The exact reviewed gene/taxon83333 request returned one entry for bamE;
    all returned accession/gene-name/alias/taxon fields were inspected. Current single-hit
    claims for BamB and BamC are therefore supported. This bounded endpoint result
    is not a whole-UniProt absence statement.
  snapshot_sha256: 2c3d1d8bec5ecedd19c04c83b35c47c779714bbbb1ffb76af766770cff82d765
- evidence_id: micro45-hagan2010-legacy
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2873164/?report=xml
  locator: Genuine HTML complete main-text paragraphs P2–P10; abstract independently
    read in MED record. No figure pixels, full figure captions or supplementary Methods
    inspected.
  accessed_at: '2026-10-22T04:32:50.333092Z'
  support: supports
  summary: Purified E. coli BamAB and BamCDE were combined in proteoliposomes with
    SurA/OmpT; fluorescence, heat-modifiability and carbonate-resistance assays support
    folding and membrane insertion. All-five versus partial-complex controls are activity-context
    evidence. SurA is added separately and is not a sixth stable BAM constituent.
    The older inferred BamE copy number was unresolved1or2, not a universal stoichiometry
    claim.
  snapshot_sha256: 6379382404aac3c45c0f2d36a65aa8a99cc6860e4f6b1ddc79b1f46e577d90b9
- evidence_id: micro45-bakelar2016-legacy
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4883095/?report=xml
  locator: Genuine HTML complete main-text paragraphs P5–P9. No remaining Results,
    full Methods, supplementary material or image pixels claimed.
  accessed_at: '2026-10-22T04:32:50.332997Z'
  support: supports
  summary: The crystallographic specimen lost BamB during prolonged incubation and
    was BamACDE; the text explicitly distinguishes the modeled/docked BamB context
    from the observed ACDE structure. BamC has unresolved globular domains. Direct
    A/D/E/C interaction descriptions support the bounded subcomplex note.
  snapshot_sha256: f187ddc575421cebe98fcfb69186185ccad796cb60e972bc7f6b7882879fa197
- evidence_id: micro45-iadanza2016-legacy
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC5056442/?report=xml
  locator: Genuine HTML complete sec2,sec3,sec8,sec11,sec12 and entire sec16 including
    sec17/18. Methods use pJH114/BL21(DE3), E. coli polar-lipid proteoliposomes and
    SurA/OmpT. No figure pixels, remaining Results/Discussion or supplementary tables
    inspected.
  accessed_at: '2026-10-22T04:32:50.333061Z'
  support: supports
  summary: Native MS gives a predominant1:1:1:1:1 ABCDE complex of203456±22Da (predicted203218Da),
    with minor two-BamE species. Intact-five cryoEM in detergent captures a laterally
    open conformation; partial BamC density and model assembly limits remain explicit.
    Crosslink/OmpT assays and BL21(DE3)expression/reconstitution methods are distinct
    from the K-12 reference-protein identities.
  snapshot_sha256: 6053a1d9753cb9645ee0ca7a1d195a9b781ef4aba05af3c010ef6c2a3d20042b
- evidence_id: micro45-gu2016-author
  kind: primary_source
  reference: https://ueaeprints.uea.ac.uk/id/eprint/57584/1/BAM_Nature_Gu_29012016_2_change_Figure_legends_3_revised_accepted.pdf
  locator: Genuine university-hosted accepted PDF printed pp1–8 (continuous main text
    through initial BamA–BamD interaction section); complete Methods Cloning, expression
    and purification of BAM complex, printed pp27–29. No figure pixels or later main-text/Methods
    sections claimed. SHA identifies full retained PDF, not derivative text.
  accessed_at: '2026-10-22T04:33:37.074664Z'
  support: supports
  summary: The accepted primary manuscript distinguishes inward-open five-subunit
    and laterally open four-subunit crystal complexes, periplasmic A/C/D/E ring organization
    and crosslink/function experiments. It does not establish that every observed
    conformation contains five subunits. The inspected cloning/purification method
    uses HDB150/pJH114, additional bamB expression and DH5alpha plasmid preparation,
    not an assumed match to the K-12 reference-protein taxon.
  snapshot_sha256: e032a8e60fdd821e5e00f33268f9b232a0dc3970e6f65db4faa804bbbc71ec23
- evidence_id: micro45-uo0000222
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uo/terms?obo_id=UO:0000222
  locator: Complete OLS term identity/definition/obo_id/synonyms/is_obsolete.
  accessed_at: '2026-10-22T04:33:37.075406Z'
  support: supports
  summary: UO:0000222 is active kilodalton, symbol kDa, defined as1000daltons; it
    matches the recorded approximate203 molecular-mass unit.
  snapshot_sha256: 76b2847684bc23e048e4930291a2496762989586108c42140ecb256d72a1e74c
- evidence_id: micro45-hagan2011-publisher
  kind: authority
  reference: https://doi.org/10.1146/annurev-biochem-061408-144611
  locator: Complete retained response; status/content inspected against receipt.
  accessed_at: '2026-10-22T04:32:51.072873Z'
  support: context_only
  summary: HTTP 403 returned an access-denied HTML response, not an inspected paper
    body. Metadata/abstract or a separately specified genuine body is used instead.
  snapshot_sha256: fb5a84b01f627628badcbc676c1780e4f0c662e00846b621e4ce6cc46fff8daa
- evidence_id: micro45-gu2016-publisher
  kind: authority
  reference: https://doi.org/10.1038/nature17199
  locator: Complete retained response; status/content inspected against receipt.
  accessed_at: '2026-10-22T04:32:51.109843Z'
  support: context_only
  summary: HTTP 200 returned a 3038-byte Client Challenge HTML page, not the paper
    body. Metadata/abstract or a separately specified genuine body is used instead.
  snapshot_sha256: 32ed63159c77e21ee19ca1b9aa3213ccf0218eb59539560b132a8e68ef0e18ea
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/bam_protein_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:25:39Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/bam_protein_complex.yaml'
  snapshot_sha256: 47aad2b82ea6cd6c2219c28eff3657725ad5b6fa30409bbec302181b054d5bdf
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/bam_protein_complex.yaml --out
    /private/tmp/cellstructure-batch45-20261022-mptgrq24/bam_protein_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:25:41Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/bam_protein_complex.yaml\
    \ --out /private/tmp/cellstructure-batch45-20261022-mptgrq24/bam_protein_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch45-20261022-mptgrq24/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch45-20261022-mptgrq24/bam_protein_complex-strict.tsv"
  snapshot_sha256: 66614278bf2a2560826701a86d7c8f51b0acbc7db74c491f741f898475b41d23
- evidence_id: native-proteins
  kind: validation
  reference: /private/tmp/cellstructure-batch45-20261022-mptgrq24/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/bam_protein_complex.yaml
  locator: Complete read-only focused native proteins log
  accessed_at: '2026-10-22T04:33:00.301171Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch45-20261022-mptgrq24/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/bam_protein_complex.yaml
  locator: Complete read-only focused native graphs log
  accessed_at: '2026-10-22T04:33:00.839808Z'
  support: supports
  summary: "data/structures/other/bam_protein_complex.yaml  (GO:1990063)\n  bam_omp_folding_and_insertion\t\
    unfolded_omp_substrate\tUNANCHORED_NO_UNIPROT\tunfolded outer-membrane beta-barrel\
    \ protein substrate\n  bam_omp_folding_and_insertion\tbam_a\tCOVERED\t->bam_a\
    \ (UniProtKB:P0A940)\n  bam_omp_folding_and_insertion\tbam_b_to_e_lipoproteins\t\
    UNANCHORED_WITH_UNIPROT\tBamB-E lipoproteins (UniProtKB:P77774, UniProtKB:P0A903,\
    \ UniProtKB:P0AC02)\n  bam_omp_folding_and_insertion\touter_membrane_beta_barrel\t\
    UNANCHORED_NO_UNIPROT\tassembled outer-membrane beta-barrel protein\n\ncausal_graphs\
    \ GENE_OR_PROTEIN node summary:\n     2  UNANCHORED_NO_UNIPROT     no component_ref\
    \ and no UniProtKB grounding or xref on the node\n     1  COVERED            \
    \       component_ref target holds protein_examples covering all declared symbols\n\
    \     1  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  PARTIAL_EXAMPLES          component_ref target holds\
    \ protein_examples but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES\
    \   component_ref target declares gene_symbols but holds no protein_examples\n\
    \     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols\
    \ and holds no protein_examples\n     0  DANGLING_COMPONENT_REF    component_ref\
    \ names a component_id that does not exist on the record\n     4  total GENE_OR_PROTEIN\
    \ causal nodes"
  snapshot_sha256: f4f275b1a9b744191948d61e4aeade2b7ed53269aa3327f29a7819a1a12a6c55
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/bam_protein_complex.yaml; native collect() exact
    identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '22 of 29 collected target identifiers returned OK. PMID:15851030: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force.; PMID:16079137:
    UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected
    after the bulk eutils414 transport failure. Identity resolution does not certify
    every attached biological claim; declared abstract/body reading scope remains
    in force.; PMID:17404237: UNREACHABLE; Exact native Europe PMC MED identifier,
    title and DOI were inspected after the bulk eutils414 transport failure. Identity
    resolution does not certify every attached biological claim; declared abstract/body
    reading scope remains in force.; PMID:23882017: UNREACHABLE; Exact native Europe
    PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport
    failure. Identity resolution does not certify every attached biological claim;
    declared abstract/body reading scope remains in force.; PMID:24619089: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force.; PMID:26900875:
    UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected
    after the bulk eutils414 transport failure. Identity resolution does not certify
    every attached biological claim; declared abstract/body reading scope remains
    in force.; PMID:26901871: UNREACHABLE; Exact native Europe PMC MED identifier,
    title and DOI were inspected after the bulk eutils414 transport failure. Identity
    resolution does not certify every attached biological claim; declared abstract/body
    reading scope remains in force. Native source checks are separately scoped; skipped
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
  topic: BAM identity and membrane hierarchy
  outcome: supported
  target_ids:
  - GO:1990063
  summary: The five-protein E. coli BAM example fits GO:1990063. Outer-membrane protein
    complex is a correct definition-based parent interpretation, while the fresh native
    is_a-only response does not assert that particular edge. Outer-membrane parthood
    is supported separately. No wrong sibling, chaperone or standalone protein replaces
    the assembly.
  evidence_ids:
  - micro45-go
  - micro45-bam-isa
  - micro45-bam-partof
  - micro45-hagan2010-legacy
  - micro45-gu2016-author
  - micro45-iadanza2016-legacy
  - record
- assessment_id: components
  area: grounding
  topic: Five exact constituent families and subcomplexes
  outcome: supported
  target_ids:
  - GO:1990063
  summary: BamA/B/C/D/E are supported mature constituents, with five exact family
    CURIEs. The E. coli BamAB and BamCDE purification, ACDE crystal specimen and intact-five
    laterally open cryoEM are kept distinct. Accessory roles and periplasmic lipoprotein-ring
    wording are supported; SurA remains associated folding machinery outside the stable
    five-member component inventory.
  evidence_ids:
  - micro45-ipr-IPR023707
  - micro45-ipr-IPR017687
  - micro45-ipr-IPR014524
  - micro45-ipr-IPR017689
  - micro45-ipr-IPR026592
  - micro45-go
  - micro45-hagan2010-legacy
  - micro45-bakelar2016-legacy
  - micro45-iadanza2016-legacy
  - micro45-gu2016-author
  - curation
  - record
- assessment_id: proteins
  area: grounding
  topic: Native protein identities, gene queries and evidence references
  outcome: supported
  target_ids:
  - GO:1990063
  summary: All five reviewed accessions resolve to their named Bam proteins in taxon83333
    with matching gene symbols/aliases and exact family cross-references. Full native
    location/evidence joins plus the cited PMID identities/abstracts support the annotation
    notes. BamB/BamC one-hit reviewed-query statements match the current exact responses.
    Direct study findings, native annotation assertions and by-similarity/proposed
    interpretations are not collapsed into one evidence tier.
  evidence_ids:
  - micro45-protein-P0A940
  - micro45-protein-P77774
  - micro45-protein-P0A903
  - micro45-protein-P0AC02
  - micro45-protein-P0A937
  - micro45-gene-bamA
  - micro45-gene-bamB
  - micro45-gene-bamC
  - micro45-gene-bamD
  - micro45-gene-bamE
  - micro45-pmid16079137
  - micro45-pmid23882017
  - micro45-pmid24619089
  - micro45-pmid15851030
  - micro45-pmid26900875
  - micro45-pmid17404237
  - micro45-gu2016-meta
- assessment_id: necessity
  area: scope
  topic: Formation necessity remains unknown
  outcome: unknown
  target_ids:
  - GO:1990063
  summary: All five components retain UNKNOWN, appropriately avoiding conversion of
    viability, folding efficiency or activity defects into proof of complex-formation
    necessity. Native essential/accessory descriptions and the all-five efficient-OmpT
    assay do not by themselves answer the schema assembly-necessity question for every
    lineage.
  evidence_ids:
  - micro45-hagan2010-legacy
  - micro45-iadanza2016-legacy
  - schema
  - record
  - micro45-protein-P0A940
  - micro45-protein-P77774
  - micro45-protein-P0A903
  - micro45-protein-P0AC02
  - micro45-protein-P0A937
- assessment_id: taxa
  area: scope
  topic: Diderm bacterial scope and recombinant contexts
  outcome: supported
  target_ids:
  - GO:1990063
  summary: The Bacteria VARIABLE row explicitly distinguishes diderm presence from
    monoderm absence rather than claiming every bacterium has BAM. Canonical E. coli
    species562 and reference K-12 strain83333 are correct. The Hagan2011 complete
    review abstract supports broad Gram-negative function; detailed primary systems
    are E. coli-derived purified/recombinant contexts, with BL21(DE3),HDB150 and plasmid-host
    details not replaced by the reference accession strain.
  evidence_ids:
  - micro45-tax2
  - micro45-tax562
  - micro45-tax83333
  - micro45-hagan2011-meta
  - micro45-hagan2010-legacy
  - micro45-gu2016-author
  - micro45-iadanza2016-legacy
- assessment_id: function
  area: evidence
  topic: Beta-barrel folding and insertion
  outcome: supported
  target_ids:
  - GO:1990063
  summary: The purified proteoliposome experiment directly supports OmpT assembly
    by BAM with SurA and LPS assay requirements. Subsequent structures and crosslink
    experiments support the bounded functional model and conformational flexibility.
    The record does not claim a universally proven atomic trajectory, ATP-driven reaction
    or SurA membership.
  evidence_ids:
  - micro45-hagan2010-legacy
  - micro45-gu2016-author
  - micro45-iadanza2016-legacy
  - micro45-hagan2011-meta
  - record
- assessment_id: mass
  area: quantity
  topic: Approximate203kDa intact E. coli complex
  outcome: supported
  target_ids:
  - GO:1990063
  summary: The reported molecular_mass203kDa is appropriately approximate and tied
    to the intact E. coli five-subunit example. Iadanza native MS supports the predominant
    observed mass and composition; minor two-BamE species and detergent/recombinant
    context prevent treating this as an invariant mass for all bacterial BAM systems.
  evidence_ids:
  - micro45-iadanza2016-legacy
  - micro45-uo0000222
  - record
- assessment_id: graph
  area: graph
  topic: Explicitly nonmechanistic functional outline
  outcome: supported
  target_ids:
  - GO:1990063
  summary: All seven nodes/edges were read. Family/cohort actors, complex, substrate/product
    and membrane remain distinct; the graph summarizes organization, folding/insertion
    and a sampled laterally open state without claiming a complete experimentally
    resolved pathway. The accessory cohort xrefs are examples, not an exhaustive-every-member
    promise. Gu four-subunit and Iadanza intact-five observations are not conflated.
  evidence_ids:
  - micro45-go
  - micro45-hagan2010-legacy
  - micro45-bakelar2016-legacy
  - micro45-gu2016-author
  - micro45-iadanza2016-legacy
  - record
  - micro45-protein-P0A940
  - micro45-protein-P77774
  - micro45-protein-P0A903
  - micro45-protein-P0AC02
  - micro45-protein-P0A937
- assessment_id: coverage
  area: completeness
  topic: Full target and source placement
  outcome: supported
  target_ids:
  - GO:1990063
  summary: Every component, example, quantity, function, graph edge, discussion and
    historical entry was assessed. Five verified proteins/families cover the named
    component inventory. No automatic finding is assigned to generic substrate examples
    or optional images. Historical reviews and current source limitations are preserved;
    source notes do not require unavailable bodies to prove every cited annotation
    anew.
  evidence_ids:
  - micro45-go
  - micro45-hagan2010-legacy
  - micro45-bakelar2016-legacy
  - micro45-gu2016-author
  - micro45-iadanza2016-legacy
  - record
  - micro45-hagan2010-meta
  - micro45-hagan2011-meta
  - micro45-gu2016-meta
  - micro45-iadanza2016-meta
  - micro45-bakelar2016-meta
  - micro45-pmid16079137
  - micro45-pmid23882017
  - micro45-pmid24619089
  - micro45-pmid15851030
  - micro45-pmid26900875
  - micro45-pmid17404237
findings: []
actions: []
limitations:
- Hagan2011 was read only through its complete native abstract; publisher returned403.
  Gu publisher returned HTTP200 Client Challenge, but a genuine accepted primary manuscript
  was separately recovered and read only at pp1–8 and cloning/expression/purification
  Methods pp27–29.
- Hagan2010 body P2–P10, Bakelar2016 P5–P9 and Iadanza2016 sec2/3/8/11/12/16 including17/18
  define the actual primary-body scope. No raw structural pixels, figure panels, deposited
  maps, omitted Methods or supplementary tables were inspected.
- Six additional annotation papers were verified through complete native MED abstracts
  only; exact UniProt evidence joins are annotation evidence, not a claim that those
  complete paper bodies were read.
- The current is_a-only GO ancestry does not contain GO:0106234; that parent is retained
  as definition-supported biological classification. UNKNOWN formation necessity and
  cross-lineage stoichiometry are not resolved by activity or a predominant native-MS
  species.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User expressly requests one review for every unreviewed record, including scientifically
  clean records.
- iModulonDB is not applicable to these complex identity, protein family, assembly,
  vesicle carriage and enzyme or transport claims.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
