# Cytochrome bd-I identity, composition and respiratory-function evidence review

- Review: 20261021T090552Z-cytochrome-bd-i-ubiquinol-oxidase-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T08:41:34Z
- Finished UTC: 2026-10-21T09:05:52Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The E. coli bd-I identity, four deposited subunits, protein-example mappings and nonmechanistic reaction graph are supported. No concrete curation issue was established; primary full-text access, strain and mechanistic limits remain explicit.

## Scope And Provenance

Entire single maintained target and all claim-bearing references, including native GO/InterPro/taxon/UniProt projections, PDB6RKO and 7NKZ entries/entities/assemblies, three cited primary papers at their readable tiers, and native protein/graph gates.

Selection: Sixth selected target in batch thirteen, following fixed repository path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex | data/structures/energy_complex/cytochrome_bd_i_ubiquinol_oxidase_complex.yaml | maintained | cytochrome bd-I ubiquinol oxidase complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex | Focused validator passed. |
| Focused native strict | passed | True | cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex | Focused validator passed. |
| Target resolver slice | passed | True | cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex | 14 identifiers OK; 6 transport/skipped residuals independently resolved. |
| Native UniProt example verification | passed | True | cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex | All examples verified. |
| Native graph protein coverage | passed | True | cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex | Both graph protein nodes COVERED; every other coverage category zero. |
| Expression-module applicability | not_applicable | False | cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex | No expression-module, regulator or condition-specific expression claim is used to establish structural membership; iModulon evidence is not required. |
| Claim-level scientific review | passed | True | cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Named bd-I identity and ontology boundaries

identity: supported. Targets: cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex.

The local identifier, synonym, membrane-bound terminal-oxidase definition and multiprotein-complex kind match the E. coli bd-I entry. The two parent GO classes are valid broader is-a classifications, not parthood assertions. Cytochrome o/bo3 candidates denote another oxidase. The historical statement that no exact bd activity term was found is not contradicted by a generic reaction term.

### Four deposited constituent proteins

evidence: supported. Targets: cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex.

6RKO independently maps all four component rows to the stated polymer entities and accessions, with one instance of each in the global biological assembly. CydA and CydB are the named core constituents. Their membership is supported; assembly necessity is assessed separately below. The two small-subunit roles remain limited to the resolved E. coli example and essentiality UNKNOWN.

### Family versus protein identity

grounding: supported. Targets: cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex.

The four InterPro entries are genuine protein families matching the stated subunit identities. IPR047743 explicitly includes the CydH NCBIfam model, while A5A618 remains primary gene ynhF. Older tentative membership or cofactor descriptions are not allowed to override the separately deposited four-polymer architecture or introduce a detailed heme model.

### Taxon-paired protein examples and aliases

grounding: supported. Targets: cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex.

All four example names, primary genes, reviewed statuses and K-12 taxon pairs agree with native UniProt. Exact reviewed-gene queries return the expected entries, and cydX/ybgT is one accession. The target explicitly restricts protein examples to identity evidence; PDB supplies membership. Both graph protein nodes resolve to the correct components and verified examples.

### Experimental citation attribution and strain precision

evidence: supported. Targets: cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex.

The target notes correctly say that UniProt cites Zhang2004 and Stenberg2005 as ECO:0000269 evidence for CydA/B inner-membrane location. Stenberg body passages directly identify CydA/B in a membrane-complex preparation from BL21(DE3)pLysS, while the representative UniProt identities are K-12. These are distinct provenance statements, not a demonstrated record error. Abstract-only Zhang access cannot establish every tested construct or exclude CydB participation.

### Species example, strain and comparison

scope: supported. Targets: cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex.

The canonical E. coli species label agrees with taxon562; 6RKO polymer source and protein examples specify K-12 taxon83333. The separate 7NKZ comparison has M. tuberculosis H37Rv source taxon83332 and a distinct expression host. The record does not assert that every bd oxidase or strain has the E. coli accessory-subunit set.

### Reaction and PMF contribution

evidence: supported. Targets: cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex.

Ubiquinol oxidation, oxygen reduction, ubiquinone/water products and a bd architecture distinct from heme-copper oxidases are supported at the reaction/annotation level. RCSB EC7.1.1.7 annotations and UniProt function/reaction comments support the stated PMF contribution. Neither the target nor this review claims that bd-I actively pumps protons or that a newly inspected functional assay measured proton stoichiometry.

### Nonmechanistic functional topology

graph: supported. Targets: cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex.

All nine nodes and eight edges were checked. CydA/B component references and the self-structure reference resolve within this target; the graph correctly keeps ubiquinone and water as products and oxygen as terminal acceptor. Its NONMECHANISTIC scope excludes a detailed heme sequence or proton-channel mechanism. Structure/contribution edges rest on deposited entities and function annotation, not direct kinetic proof from the coordinate entry.

### Open cross-lineage boundary

scope: supported. Targets: cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex.

The existing discussion accurately contrasts four-polymer E. coli 6RKO with two-polymer M. tuberculosis 7NKZ. This supports retaining the open bd-I/bd-II/two-subunit boundary without projecting small subunits universally. The older tentative YhcB association is a separate hypothesis, not a mandatory fifth structural component or a synonym for YnhF.

### Exact source tiers and access limits

provenance: supported. Targets: cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex.

Native database responses establish identifier, family, taxon, entity and annotation facts. Safarian2019 and Zhang2004 were readable only as primary abstracts. Stenberg2005 was readable as discontinuous indexed primary-body passages with explicit locators, not a complete native article. All raw/meta snapshots preserve original UTCZ timestamps and hashes, including failed access attempts and reused metadata. No browser response is presented as HTTP status evidence.

### Bounded scope and maintained ownership

completeness: supported. Targets: cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex.

The record supplies a supported four-component example, taxon-paired identity evidence, a reaction graph and an explicit small-subunit scope TODO. Optional images, physical properties, detailed cofactor chemistry or additional generic reaction identifiers are not automatic defects. No exact structural misidentification, wrong protein mapping, unsupported universal subunit claim or graph-direction error was established; native PROPOSED status and historical curation remain unchanged.

### Assembly necessity versus constituent membership

evidence: unknown. Targets: cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex.

The schema defines essentiality by whether the structure forms without the component. The inspected sources establish constituent membership and functions, but those observations alone do not establish this assembly-necessity assertion. No subunit-deletion/assembly experiment was independently checked here; catalytic necessity, organismal viability and intact structural membership are distinct questions.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/energy_complex/cytochrome_bd_i_ubiquinol_oxidase_complex.yaml; Entire maintained YAML, including definition, synonym, parents, four components and protein examples, canonical example, function, every graph node/edge, discussion and history. | context_only | The entire target was read. It describes the E. coli four-subunit bd-I example and explicitly leaves broader small-subunit scope unresolved; its native status is PROPOSED. |
| policy | docs/CURATION.md; Identifiers, components, protein examples, causal graphs, discussions and status; also the review and UniProt guidance captured in source.inputs. | context_only | Family and accession identity are distinct from structural membership. Optional empty slots and historical access/search annotations do not automatically establish curation defects. The explicitly authorized output is an unsaved review draft. |
| bdi-prep-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0016682,GO:0070069,GO:0098803; All three results: exact id, name, isObsolete, aspect, definition, synonyms and children relation values. | supports | GO:0098803 respiratory chain complex and GO:0070069 cytochrome complex are active cellular-component classes with definitions broad enough for bd-I. GO:0016682 is an active, broader molecular-function class for diphenol-related donors and oxygen acceptor; it is not an exact bd-I identity. |
| bdI-agent-go-candidates | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0009319%2CGO%3A0009486%2CGO%3A0009916; Exact three results: id/name/definition/synonyms/aspect; no equivalence to bd-I inferred. | context_only | GO:0009319 is the cytochrome o ubiquinol oxidase complex, and GO:0009486 is cytochrome bo3 ubiquinol oxidase activity; neither is the bd-I identity. GO:0009916 describes alternative oxidase activity without a bd-specific identity. |
| bdI-agent-go-0102721 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0102721; results[0]: id, isObsolete, name, definition and RHEA:30255 cross-reference. | context_only | GO:0102721 is an active molecular-function term for ubiquinol:oxygen oxidoreductase activity, specifying ubiquinol and oxygen conversion to ubiquinone and water. It is a possible generic reaction grounding, not a bd-specific complex or architecture identifier; the record already expresses this reaction without claiming this identifier is unavailable. |
| bdI-agent-go-bd-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=cytochrome%20bd&amp;limit=100; numberOfHits, pageInfo and all returned result identifiers/names; exact query and page retained in URL. | context_only | QuickGO query 'cytochrome bd', page 1 of 2, reports 183 hits across all pages. This snapshot was screened for relevant identity/reaction candidates; it is a bounded search result, not proof of absence throughout every ontology. |
| bdI-agent-go-bd-search-page2 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=cytochrome%20bd&amp;limit=100&amp;page=2; numberOfHits, pageInfo and all returned result identifiers/names; exact query and page retained in URL. | context_only | QuickGO query 'cytochrome bd', page 2 of 2, reports 183 hits across all pages. This snapshot was screened for relevant identity/reaction candidates; it is a bounded search result, not proof of absence throughout every ontology. |
| bdI-agent-go-ubiquinol-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=ubiquinol%20oxidase&amp;limit=100; numberOfHits, pageInfo and all returned result identifiers/names; exact query and page retained in URL. | context_only | QuickGO query 'ubiquinol oxidase', page 1 of 3, reports 277 hits across all pages. This snapshot was screened for relevant identity/reaction candidates; it is a bounded search result, not proof of absence throughout every ontology. |
| bdI-agent-go-ubiquinol-search-page2 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=ubiquinol%20oxidase&amp;limit=100&amp;page=2; numberOfHits, pageInfo and all returned result identifiers/names; exact query and page retained in URL. | context_only | QuickGO query 'ubiquinol oxidase', page 2 of 3, reports 277 hits across all pages. This snapshot was screened for relevant identity/reaction candidates; it is a bounded search result, not proof of absence throughout every ontology. |
| bdI-agent-go-ubiquinol-search-page3 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=ubiquinol%20oxidase&amp;limit=100&amp;page=3; numberOfHits, pageInfo and all returned result identifiers/names; exact query and page retained in URL. | context_only | QuickGO query 'ubiquinol oxidase', page 3 of 3, reports 277 hits across all pages. This snapshot was screened for relevant identity/reaction candidates; it is a bounded search result, not proof of absence throughout every ontology. |
| bdi-prep-tax-562 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562; taxId, scientificName, rank and otherNames; this source establishes only its own taxon identity. | supports | NCBITaxon:562 is Escherichia coli at species rank, matching the canonical example. |
| bdi-prep-tax-83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; taxId, scientificName, rank and otherNames; this source establishes only its own taxon identity. | supports | NCBITaxon:83333 is Escherichia coli K-12 at strain rank, with K12 as an alternate name, matching all four protein examples. |
| bdI-agent-tax-83332 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83332; taxId, scientificName, rank and otherNames; this source establishes only its own taxon identity. | supports | NCBITaxon:83332 is Mycobacterium tuberculosis H37Rv at strain rank, identifying the biological source of the comparative 7NKZ polymers. |
| bdi-prep-IPR002585 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002585/; metadata.accession, type=family, name, full description and member_databases; only this family response is attested. | supports | The cytochrome ubiquinol oxidase subunit-1 family includes the P0ABJ9 CydA example and describes bacterial ubiquinol oxidation coupled to oxygen reduction. Its older cofactor-placement wording is not used to infer a new residue-level or subunit-specific heme mechanism. |
| bdi-prep-IPR003317 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR003317/; metadata.accession, type=family, name, full description and member_databases; only this family response is attested. | supports | The cytochrome ubiquinol oxidase subunit-2 family describes integral membrane proteins in bd-type quinol-dependent oxygen uptake. Its TIGR00203 member model supports CydB family identity; older cofactor text is not imported into this review. |
| bdi-prep-IPR011724 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR011724/; metadata.accession, type=family, name, full description and member_databases; only this family response is attested. | supports | The Cyd operon protein YbgT family names P56100 as its E. coli example and describes a small membrane-spanning protein. Its TIGR02106 member model is named cytochrome bd-I oxidase subunit CydX; older tentative membership wording is supplemented by separately inspected 6RKO structural metadata. |
| bdi-prep-IPR047743 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR047743/; metadata.accession, type=family, name, full description and member_databases; only this family response is attested. | supports | The Membrane protein YnhF-like family describes small, approximately 29-residue gammaproteobacterial membrane proteins and includes NF033411, named cytochrome bd-I oxidase subunit CydH. This supports the target's bounded YnhF-like/CydH-model wording, not a forced rename of the UniProt primary gene. |
| bdi-prep-P0ABJ9 | https://rest.uniprot.org/uniprotkb/P0ABJ9.json; primaryAccession, entryType, proteinDescription, genes, organism, complete comments (FUNCTION, CATALYTIC ACTIVITY, COFACTOR, SUBUNIT and SUBCELLULAR LOCATION where present), features and uniProtKBCrossReferences. | supports | Reviewed P0ABJ9 is cytochrome bd-I ubiquinol oxidase subunit 1, gene cydA, taxon83333, with IPR002585. Its native inner-membrane annotation explicitly cites PMID:15013751 and PMID:16079137 with ECO:0000269, as the target notes state. Function and catalytic-activity annotations support electrogenic quinol oxidation and PMF contribution; cofactor annotations support heme association without independently rechecking an assay. |
| bdi-prep-P0ABK2 | https://rest.uniprot.org/uniprotkb/P0ABK2.json; primaryAccession, entryType, proteinDescription, genes, organism, complete comments (FUNCTION, CATALYTIC ACTIVITY, COFACTOR, SUBUNIT and SUBCELLULAR LOCATION where present), features and uniProtKBCrossReferences. | supports | Reviewed P0ABK2 is cytochrome bd-I ubiquinol oxidase subunit 2, gene cydB, taxon83333, with IPR003317. Its native inner-membrane annotation explicitly cites PMID:15013751 and PMID:16079137 with ECO:0000269. Its topology note also cites Zhang2004; the abstract-only paper access does not justify declaring that study irrelevant to CydB. Catalytic-activity annotations include EC7.1.1.7. |
| bdi-prep-P56100 | https://rest.uniprot.org/uniprotkb/P56100.json; primaryAccession, entryType, proteinDescription, genes, organism, complete comments (FUNCTION, CATALYTIC ACTIVITY, COFACTOR, SUBUNIT and SUBCELLULAR LOCATION where present), features and uniProtKBCrossReferences. | supports | Reviewed P56100 is cytochrome bd-I ubiquinol oxidase subunit X, primary gene cydX and synonym ybgT, taxon83333, with IPR011724. The target accurately uses the accession as identity evidence and separately grounds membership in 6RKO. Database localization and older tentative subunit comments are not treated as direct structural proof. |
| bdi-prep-A5A618 | https://rest.uniprot.org/uniprotkb/A5A618.json; primaryAccession, entryType, proteinDescription, genes, organism, complete comments (FUNCTION, CATALYTIC ACTIVITY, COFACTOR, SUBUNIT and SUBCELLULAR LOCATION where present), features and uniProtKBCrossReferences. | supports | Reviewed A5A618 retains the recommended name Uncharacterized protein YnhF, primary gene ynhF, taxon83333, and IPR047743. Its membrane/topology annotations support the bounded single-pass description. The record correctly keeps this native protein identity distinct from the associated CydH family-model name. |
| bdi-prep-query-cydA | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AcydA%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; Exact query in URL; entire results array and each result primaryAccession, entryType, genes and organism. No result-total HTTP header is attested by this receipt. | supports | The native exact-gene, reviewed-entry query restricted to taxon83333 returns one result, P0ABJ9, for cydA. This supports the recorded symbol/accession pairing; cydX and ybgT resolve to the same protein, not distinct subunits. |
| bdi-prep-query-cydB | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AcydB%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; Exact query in URL; entire results array and each result primaryAccession, entryType, genes and organism. No result-total HTTP header is attested by this receipt. | supports | The native exact-gene, reviewed-entry query restricted to taxon83333 returns one result, P0ABK2, for cydB. This supports the recorded symbol/accession pairing; cydX and ybgT resolve to the same protein, not distinct subunits. |
| bdi-prep-query-cydX | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AcydX%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; Exact query in URL; entire results array and each result primaryAccession, entryType, genes and organism. No result-total HTTP header is attested by this receipt. | supports | The native exact-gene, reviewed-entry query restricted to taxon83333 returns one result, P56100, for cydX. This supports the recorded symbol/accession pairing; cydX and ybgT resolve to the same protein, not distinct subunits. |
| bdi-prep-query-ybgT | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AybgT%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; Exact query in URL; entire results array and each result primaryAccession, entryType, genes and organism. No result-total HTTP header is attested by this receipt. | supports | The native exact-gene, reviewed-entry query restricted to taxon83333 returns one result, P56100, for ybgT. This supports the recorded symbol/accession pairing; cydX and ybgT resolve to the same protein, not distinct subunits. |
| bdi-prep-query-ynhF | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AynhF%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; Exact query in URL; entire results array and each result primaryAccession, entryType, genes and organism. No result-total HTTP header is attested by this receipt. | supports | The native exact-gene, reviewed-entry query restricted to taxon83333 returns one result, A5A618, for ynhF. This supports the recorded symbol/accession pairing; cydX and ybgT resolve to the same protein, not distinct subunits. |
| bdi-prep-pdb-6RKO | https://data.rcsb.org/rest/v1/core/entry/6RKO; struct, exptl, rcsb_entry_info, rcsb_entry_container_identifiers, rcsb_primary_citation and EM metadata. | supports | 6RKO is an experimental E. coli cytochrome bd-I cryo-EM structure, 2.68 A in the native entry, with four protein polymer entities. Its primary citation is Safarian2019, DOI:10.1126/science.aay0967, PMID:31604309. Entry metadata establishes the deposited structural identity; no coordinate or map reanalysis is claimed. |
| bdi-prep-assembly-6RKO | https://data.rcsb.org/rest/v1/core/assembly/6RKO/1; pdbx_struct_assembly, rcsb_assembly_info and rcsb_struct_symmetry entries distinguished by kind. | supports | Assembly1 is a tetramer with four distinct protein entities and four instances. Global symmetry lists A1B1C1D1. The separate A2B1C1 pseudo-symmetry grouping must not be interpreted as biological duplication of an individual subunit. |
| bdi-prep-6RKO-entity-1 | https://data.rcsb.org/rest/v1/core/polymer_entity/6RKO/1; entity_poly, entity_src_gen, rcsb_polymer_entity, rcsb_polymer_entity_container_identifiers, rcsb_polymer_entity_align, rcsb_entity_source_organism and rcsb_entity_host_organism; EC lineage where present. | supports | 6RKO polymer entity 1 is CydB, mapped to UniProtKB:P0ABK2, with genetically engineered source E. coli K-12 (taxon83333) and E. coli expression host. Its native EC lineage includes 7.1.1.7, quinol oxidase (electrogenic, proton-motive force generating); this is a database annotation rather than a new PMF assay. |
| bdi-prep-6RKO-entity-2 | https://data.rcsb.org/rest/v1/core/polymer_entity/6RKO/2; entity_poly, entity_src_gen, rcsb_polymer_entity, rcsb_polymer_entity_container_identifiers, rcsb_polymer_entity_align, rcsb_entity_source_organism and rcsb_entity_host_organism; EC lineage where present. | supports | 6RKO polymer entity 2 is CydA, mapped to UniProtKB:P0ABJ9, with genetically engineered source E. coli K-12 (taxon83333) and E. coli expression host. Its native EC lineage includes 7.1.1.7, quinol oxidase (electrogenic, proton-motive force generating); this is a database annotation rather than a new PMF assay. |
| bdi-prep-6RKO-entity-3 | https://data.rcsb.org/rest/v1/core/polymer_entity/6RKO/3; entity_poly, entity_src_gen, rcsb_polymer_entity, rcsb_polymer_entity_container_identifiers, rcsb_polymer_entity_align, rcsb_entity_source_organism and rcsb_entity_host_organism; EC lineage where present. | supports | 6RKO polymer entity 3 is YnhF, mapped to UniProtKB:A5A618, with genetically engineered source E. coli K-12 (taxon83333) and E. coli expression host. This entity does not carry the EC lineage used for the PMF edge; its membership rests on the deposited polymer and assembly records. |
| bdi-prep-6RKO-entity-4 | https://data.rcsb.org/rest/v1/core/polymer_entity/6RKO/4; entity_poly, entity_src_gen, rcsb_polymer_entity, rcsb_polymer_entity_container_identifiers, rcsb_polymer_entity_align, rcsb_entity_source_organism and rcsb_entity_host_organism; EC lineage where present. | supports | 6RKO polymer entity 4 is CydX, mapped to UniProtKB:P56100, with genetically engineered source E. coli K-12 (taxon83333) and E. coli expression host. Its native EC lineage includes 7.1.1.7, quinol oxidase (electrogenic, proton-motive force generating); this is a database annotation rather than a new PMF assay. |
| bdi-prep-pdb-7NKZ | https://data.rcsb.org/rest/v1/core/entry/7NKZ; struct, exptl, rcsb_entry_info, rcsb_entry_container_identifiers and rcsb_primary_citation. | supports | 7NKZ is an experimental M. tuberculosis bd-oxidase cryo-EM entry at 2.5 A, with two protein polymer entities and primary citation DOI:10.1038/s41467-021-25537-z. The comparison is limited to native deposited composition; that primary paper was not independently read. |
| bdi-prep-assembly-7NKZ | https://data.rcsb.org/rest/v1/core/assembly/7NKZ/1; pdbx_struct_assembly, rcsb_assembly_info and Global Symmetry entry in rcsb_struct_symmetry. | supports | Assembly1 is an author-defined heterodimer with two protein entities, two instances and global A1B1 stoichiometry. It supports the record's bounded two-polymer comparison, not universal absence of accessory proteins from every mycobacterial bd complex. |
| bdi-prep-7NKZ-entity-1 | https://data.rcsb.org/rest/v1/core/polymer_entity/7NKZ/1; rcsb_polymer_entity, rcsb_polymer_entity_container_identifiers, rcsb_entity_source_organism, rcsb_entity_host_organism and entity_src_gen. | supports | 7NKZ polymer entity 1 is CydB, UniProtKB:O06139, with M. tuberculosis H37Rv source taxon83332. The separately listed expression host is Mycolicibacterium smegmatis MC2 155, taxon246196, and is not substituted for the biological source. |
| bdi-prep-7NKZ-entity-2 | https://data.rcsb.org/rest/v1/core/polymer_entity/7NKZ/2; rcsb_polymer_entity, rcsb_polymer_entity_container_identifiers, rcsb_entity_source_organism, rcsb_entity_host_organism and entity_src_gen. | supports | 7NKZ polymer entity 2 is CydA, UniProtKB:L7N662, with M. tuberculosis H37Rv source taxon83332. The separately listed expression host is Mycolicibacterium smegmatis MC2 155, taxon246196, and is not substituted for the biological source. |
| bdi-prep-safarian-pmid-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A31604309%20AND%20SRC%3AMED; resultList.result[0]: exact PMID31604309, DOI, title, authors, publication details and entire abstractText. | supports | The exact primary-article abstract identifies E. coli bd-I cryo-EM structure determination and previously unknown CydH, and states oxygen-to-water reduction and structural divergence from mitochondrial cytochrome c oxidases. Readable tier is the abstract plus citation metadata, not the main text, Methods or supplementary material. |
| bdi-prep-zhang2004-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A15013751%20AND%20SRC%3AMED; resultList.result[0]: exact PMID15013751, DOI10.1016/S0014-5793(04)00125-5, title, authors and entire abstractText. | supports | The exact Zhang2004 primary abstract reports experimental beta-lactamase fusion tests supporting the revised nine-transmembrane-helix CydA topology and periplasmic-side oxygen-reactive site. Full methods, strain details and individual fusion results were not read. Native UniProt citation attribution was checked separately for both CydA and CydB. |
| bdi-prep-stenberg2005-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A16079137%20AND%20SRC%3AMED; resultList.result[0]: PMID16079137, DOI10.1074/jbc.M506479200, title, authors and entire abstractText. | supports | The Stenberg2005 primary abstract describes membrane-complex BN-PAGE, second-dimension SDS-PAGE and mass spectrometry. Its YhcB subunit assignment is explicitly tentative; YhcB is not the YnhF/CydH small protein in the target. Detailed localization and model scope are assessed from separately captured body passages. |
| bdI-agent-bdi-browser5 | https://doi.org/10.1074/jbc.M506479200; First JBC/DOI result only: Results &gt; Protein Complexes in the Inner Membrane &gt; Bioenergetic Complexes, cytochrome bd paragraph; Figure3 caption; Discussion YhcB paragraph. Other search results, including a later review, are not used. Figure pixels not inspected. | supports | Stenberg2005 primary Results identify CydA and CydB in the inner-membrane preparation and tentatively associate YhcB; Discussion retains that tentative scope. The Figure3 caption distinguishes proteins identified by mass spectrometry from inferred bands. This supports localization/association, not the modern four-subunit inventory or a newly verified PMF mechanism. The snapshot is a web.run indexed publisher extraction, not an attested HTTP200 response or complete-article download. |
| bdI-agent-bdi-stenberg-methods-search2 | https://doi.org/10.1074/jbc.M506479200; First JBC/DOI result only: Materials and Methods &gt; Preparation of Membrane Vesicles; One-dimensional BN-PAGE; initial Two-dimensional SDS-PAGE paragraph; Results &gt; Purification of Membrane Protein Complexes and Protein Identification. Table1 is truncated before Cyd rows; full MS methods, complete table and supplementary figures were not read. | supports | Stenberg2005 used BL21(DE3)pLysS grown at 37 C in LB and harvested in late log phase; sucrose-gradient membrane vesicles were solubilized for BN-PAGE using 0.5% DDM. The extracted Methods and Results explain the membrane separation and protein-identification workflow. This is direct experimental context for BL21, not a claim that the experiment used K-12. The snapshot is a web.run indexed publisher extraction, not an attested HTTP200 response or complete-article download. |
| schema-result | just validate data/structures/energy_complex/cytochrome_bd_i_ubiquinol_oxidase_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/energy_complex/cytochrome_bd_i_ubiquinol_oxidase_complex.yaml |
| strict-result | just validate-strict data/structures/energy_complex/cytochrome_bd_i_ubiquinol_oxidase_complex.yaml --out /private/tmp/cellstructure-batch13-20261021-vud60b4w/cytochrome_bd_i_ubiquinol_oxidase_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/energy_complex/cytochrome_bd_i_ubiquinol_oxidase_complex.yaml --out /private/tmp/cellstructure-batch13-20261021-vud60b4w/cytochrome_bd_i_ubiquinol_oxidase_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch13-20261021-vud60b4w/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch13-20261021-vud60b4w/cytochrome_bd_i_ubiquinol_oxidase_complex-strict.tsv |
| target-curies | just check-curies-strict; data/structures/energy_complex/cytochrome_bd_i_ubiquinol_oxidase_complex.yaml; exact collect() scope; hash identifies the entire original resolver TSV; original /private/tmp/cellstructure-record-reviews-UhRFh7/repo/reports/curie_check.tsv, not the generated resolver-slice.json | supports | 14 of 20 collected target identifiers returned OK at the unchanged base. Residuals: PDB:6RKO: SKIPPED; resolved by evidence bdi-prep-pdb-6RKO; PDB:7NKZ: SKIPPED; resolved by evidence bdi-prep-pdb-7NKZ; PMID:15013751: UNREACHABLE; resolved by evidence bdi-prep-zhang2004-meta; PMID:16079137: UNREACHABLE; resolved by evidence bdi-prep-stenberg2005-meta; PMID:31604309: UNREACHABLE; resolved by evidence bdi-prep-safarian-pmid-meta; cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex: SKIPPED; resolved by evidence record. Source-native identity checked separately. |
| native-verify | uv run python scripts/uniprot_genes.py --verify --record data/structures/energy_complex/cytochrome_bd_i_ubiquinol_oxidase_complex.yaml; Captured native gate log; command and start/end UTC in matching receipt. | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | uv run python scripts/uniprot_genes.py --causal-graphs --record data/structures/energy_complex/cytochrome_bd_i_ubiquinol_oxidase_complex.yaml; Captured native gate log; command and start/end UTC in matching receipt. | supports | data/structures/energy_complex/cytochrome_bd_i_ubiquinol_oxidase_complex.yaml  (cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex)<br>  cytochrome_bd_i_quinol_oxygen_coupling	cydA	COVERED	-&gt;cytochrome_bd_i_subunit_i (UniProtKB:P0ABJ9)<br>  cytochrome_bd_i_quinol_oxygen_coupling	cydB	COVERED	-&gt;cytochrome_bd_i_subunit_ii (UniProtKB:P0ABK2)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     2  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Safarian2019 main text, full Methods and supplementary material were not recovered. The exact primary abstract and RCSB entry/entity/assembly metadata support the claims at their stated tiers; no atomic coordinates, cryo-EM density, image pixels or newly retrieved PMF assay were independently analyzed.
- Zhang2004 was read as metadata and complete primary abstract only. Full experimental strain details, construct positions and individual topology results remain unread. Both UniProt entries directly attest the citation attribution made by the record.
- Stenberg2005 primary body access consists of the two indexed publisher extracts identified in evidence locators. Complete mass-spectrometry methods, Cyd rows of Table1, supplementary figures and figure pixels were not read. Native Elsevier API access returned metadata rather than a complete body; browser metadata has null HTTP status.
- Stenberg2005 experiments used BL21(DE3)pLysS; the target protein examples identify K-12 reference entries. Citation attribution is verified without asserting an exact experimental-strain match or an unqualified transfer of every measured property.
- PMF contribution is supported by native functional annotations and the bounded terminal-oxidase reaction. This review does not independently establish proton/electron stoichiometry, active proton pumping, catalytic kinetics or physiological essentiality under specified conditions.
- InterPro family descriptions contain older tentative subunit and cofactor wording. They are used for exact family identity and bounded reaction context, not as modern proof of heme placement or universal accessory-subunit composition.
- The 7NKZ comparison is restricted to native deposited entity and assembly metadata. Its associated 2021 primary paper was not independently read; two deposited polymers do not prove absence of accessory proteins in all mycobacterial preparations.
- Both QuickGO searches were fully paginated, but their failure to return a bd-specific identity is limited to those queries. GO:0102721 supplies a generic reaction candidate; no universal ontology-absence claim or automatic optional-grounding finding is made.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The schema defines essentiality by whether the structure forms without the component. The inspected sources establish constituent membership and functions, but those observations alone do not establish this assembly-necessity assertion. No subunit-deletion/assembly experiment was independently checked here; catalytic necessity, organismal viability and intact structural membership are distinct questions.
- Native inspect and focused schema/strict checks completed before assessment. All thirteen native input hashes were independently checked at unchanged base99692a3d5f16a7dcd6db7e3811344c299a977b81. No neighboring maintained record was needed.
- The user-authorized batch task explicitly requests an unsaved draft even for a clean outcome. No issue is manufactured to justify a saved review; root retains finalization and save responsibility.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T090552Z-cytochrome-bd-i-ubiquinol-oxidase-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Cytochrome bd-I identity, composition and respiratory-function evidence review
started_at: '2026-10-21T08:41:34Z'
finished_at: '2026-10-21T09:05:52Z'
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
summary: The E. coli bd-I identity, four deposited subunits, protein-example mappings
  and nonmechanistic reaction graph are supported. No concrete curation issue was
  established; primary full-text access, strain and mechanistic limits remain explicit.
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
  - path: .claude/skills/uniprot-protein-examples/SKILL.md
    sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
    role: context
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/energy_complex/cytochrome_bd_i_ubiquinol_oxidase_complex.yaml
    sha256: 1a71d5c7e8f417d2e943dfea2657d5be85bebad9786cccc4fee4fa39fa66f825
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
- target_id: cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex
  path: data/structures/energy_complex/cytochrome_bd_i_ubiquinol_oxidase_complex.yaml
  label: cytochrome bd-I ubiquinol oxidase complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/cytochrome_bd_i_ubiquinol_oxidase_complex.yaml
    role: maintained scientific record
scope:
  description: Entire single maintained target and all claim-bearing references, including
    native GO/InterPro/taxon/UniProt projections, PDB6RKO and 7NKZ entries/entities/assemblies,
    three cited primary papers at their readable tiers, and native protein/graph gates.
  selection: Sixth selected target in batch thirteen, following fixed repository path
    order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex
  command: just validate data/structures/energy_complex/cytochrome_bd_i_ubiquinol_oxidase_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex
  command: just validate-strict data/structures/energy_complex/cytochrome_bd_i_ubiquinol_oxidase_complex.yaml
    --out /private/tmp/cellstructure-batch13-20261021-vud60b4w/cytochrome_bd_i_ubiquinol_oxidase_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex
  summary: 14 identifiers OK; 6 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - bdi-prep-zhang2004-meta
  - bdi-prep-stenberg2005-meta
  - bdi-prep-safarian-pmid-meta
  - bdi-prep-pdb-6RKO
  - bdi-prep-pdb-7NKZ
  - record
- check_id: native-verify
  name: Native UniProt example verification
  status: passed
  required: true
  target_ids:
  - cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex
  command: uv run python scripts/uniprot_genes.py --verify --record data/structures/energy_complex/cytochrome_bd_i_ubiquinol_oxidase_complex.yaml
  exit_code: 0
  summary: All examples verified.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Native graph protein coverage
  status: passed
  required: true
  target_ids:
  - cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex
  command: uv run python scripts/uniprot_genes.py --causal-graphs --record data/structures/energy_complex/cytochrome_bd_i_ubiquinol_oxidase_complex.yaml
  exit_code: 0
  summary: Both graph protein nodes COVERED; every other coverage category zero.
  evidence_ids:
  - native-causal-graphs
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex
  summary: No expression-module, regulator or condition-specific expression claim
    is used to establish structural membership; iModulon evidence is not required.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - bdi-prep-go
  - bdI-agent-go-candidates
  - bdI-agent-go-0102721
  - bdI-agent-go-bd-search
  - bdI-agent-go-bd-search-page2
  - bdI-agent-go-ubiquinol-search
  - bdI-agent-go-ubiquinol-search-page2
  - bdI-agent-go-ubiquinol-search-page3
  - bdi-prep-tax-562
  - bdi-prep-tax-83333
  - bdI-agent-tax-83332
  - bdi-prep-IPR002585
  - bdi-prep-IPR003317
  - bdi-prep-IPR011724
  - bdi-prep-IPR047743
  - bdi-prep-P0ABJ9
  - bdi-prep-P0ABK2
  - bdi-prep-P56100
  - bdi-prep-A5A618
  - bdi-prep-query-cydA
  - bdi-prep-query-cydB
  - bdi-prep-query-cydX
  - bdi-prep-query-ybgT
  - bdi-prep-query-ynhF
  - bdi-prep-pdb-6RKO
  - bdi-prep-assembly-6RKO
  - bdi-prep-6RKO-entity-1
  - bdi-prep-6RKO-entity-2
  - bdi-prep-6RKO-entity-3
  - bdi-prep-6RKO-entity-4
  - bdi-prep-pdb-7NKZ
  - bdi-prep-assembly-7NKZ
  - bdi-prep-7NKZ-entity-1
  - bdi-prep-7NKZ-entity-2
  - bdi-prep-safarian-pmid-meta
  - bdi-prep-zhang2004-meta
  - bdi-prep-stenberg2005-meta
  - bdI-agent-bdi-browser5
  - bdI-agent-bdi-stenberg-methods-search2
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch13 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch13 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch13 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch13 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch13 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/energy_complex/cytochrome_bd_i_ubiquinol_oxidase_complex.yaml
  locator: Entire maintained YAML, including definition, synonym, parents, four components
    and protein examples, canonical example, function, every graph node/edge, discussion
    and history.
  accessed_at: '2026-10-21T08:54:46Z'
  support: context_only
  summary: The entire target was read. It describes the E. coli four-subunit bd-I
    example and explicitly leaves broader small-subunit scope unresolved; its native
    status is PROPOSED.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Identifiers, components, protein examples, causal graphs, discussions and
    status; also the review and UniProt guidance captured in source.inputs.
  accessed_at: '2026-10-21T08:54:46Z'
  support: context_only
  summary: Family and accession identity are distinct from structural membership.
    Optional empty slots and historical access/search annotations do not automatically
    establish curation defects. The explicitly authorized output is an unsaved review
    draft.
- evidence_id: bdi-prep-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0016682,GO:0070069,GO:0098803
  locator: 'All three results: exact id, name, isObsolete, aspect, definition, synonyms
    and children relation values.'
  accessed_at: '2026-10-21T08:39:15.554567Z'
  support: supports
  summary: GO:0098803 respiratory chain complex and GO:0070069 cytochrome complex
    are active cellular-component classes with definitions broad enough for bd-I.
    GO:0016682 is an active, broader molecular-function class for diphenol-related
    donors and oxygen acceptor; it is not an exact bd-I identity.
  snapshot_sha256: f5c514e1b9e4fb267f3a5c65f256e7a92297abb518c9282b8dccbf949ab0249d
- evidence_id: bdI-agent-go-candidates
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0009319%2CGO%3A0009486%2CGO%3A0009916
  locator: 'Exact three results: id/name/definition/synonyms/aspect; no equivalence
    to bd-I inferred.'
  accessed_at: '2026-10-21T08:51:57.023319Z'
  support: context_only
  summary: GO:0009319 is the cytochrome o ubiquinol oxidase complex, and GO:0009486
    is cytochrome bo3 ubiquinol oxidase activity; neither is the bd-I identity. GO:0009916
    describes alternative oxidase activity without a bd-specific identity.
  snapshot_sha256: 4086e4fb43f0f0502116bf214bbb997cac19457501ff18363e0d97f33069cad1
- evidence_id: bdI-agent-go-0102721
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0102721
  locator: 'results[0]: id, isObsolete, name, definition and RHEA:30255 cross-reference.'
  accessed_at: '2026-10-21T08:52:25.116438Z'
  support: context_only
  summary: GO:0102721 is an active molecular-function term for ubiquinol:oxygen oxidoreductase
    activity, specifying ubiquinol and oxygen conversion to ubiquinone and water.
    It is a possible generic reaction grounding, not a bd-specific complex or architecture
    identifier; the record already expresses this reaction without claiming this identifier
    is unavailable.
  snapshot_sha256: 6af4743ce46e334031dcc24c4d57436cb70d31be78fb2997ece560855c11a46b
- evidence_id: bdI-agent-go-bd-search
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=cytochrome%20bd&limit=100
  locator: numberOfHits, pageInfo and all returned result identifiers/names; exact
    query and page retained in URL.
  accessed_at: '2026-10-21T08:49:23.696601Z'
  support: context_only
  summary: QuickGO query 'cytochrome bd', page 1 of 2, reports 183 hits across all
    pages. This snapshot was screened for relevant identity/reaction candidates; it
    is a bounded search result, not proof of absence throughout every ontology.
  snapshot_sha256: 3ac5a9ea50953abc917ef6aa806d76f956de2a8fd181f48b8cfba9c62edc4b2e
  search_scope: QuickGO native search, query 'cytochrome bd', limit=100, page 1/2;
    all pages of both queries were retrieved and screened. No exact bd-named identity
    emerged in these query results. GO:0009319, GO:0009486, GO:0009916 and GO:0102721
    were inspected separately. This is an external ontology search; local ignored-file
    inclusion is not applicable.
- evidence_id: bdI-agent-go-bd-search-page2
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=cytochrome%20bd&limit=100&page=2
  locator: numberOfHits, pageInfo and all returned result identifiers/names; exact
    query and page retained in URL.
  accessed_at: '2026-10-21T08:51:57.541607Z'
  support: context_only
  summary: QuickGO query 'cytochrome bd', page 2 of 2, reports 183 hits across all
    pages. This snapshot was screened for relevant identity/reaction candidates; it
    is a bounded search result, not proof of absence throughout every ontology.
  snapshot_sha256: ebd6cbb16f185549eda214433a88eb3e8b56666d2487f172e895f7a854d04673
  search_scope: QuickGO native search, query 'cytochrome bd', limit=100, page 2/2;
    all pages of both queries were retrieved and screened. No exact bd-named identity
    emerged in these query results. GO:0009319, GO:0009486, GO:0009916 and GO:0102721
    were inspected separately. This is an external ontology search; local ignored-file
    inclusion is not applicable.
- evidence_id: bdI-agent-go-ubiquinol-search
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=ubiquinol%20oxidase&limit=100
  locator: numberOfHits, pageInfo and all returned result identifiers/names; exact
    query and page retained in URL.
  accessed_at: '2026-10-21T08:49:23.718569Z'
  support: context_only
  summary: QuickGO query 'ubiquinol oxidase', page 1 of 3, reports 277 hits across
    all pages. This snapshot was screened for relevant identity/reaction candidates;
    it is a bounded search result, not proof of absence throughout every ontology.
  snapshot_sha256: dc75d71611dae5fa3938cc5ea26f7c5bba983305f3a10fa3860b7c5e15811c56
  search_scope: QuickGO native search, query 'ubiquinol oxidase', limit=100, page
    1/3; all pages of both queries were retrieved and screened. No exact bd-named
    identity emerged in these query results. GO:0009319, GO:0009486, GO:0009916 and
    GO:0102721 were inspected separately. This is an external ontology search; local
    ignored-file inclusion is not applicable.
- evidence_id: bdI-agent-go-ubiquinol-search-page2
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=ubiquinol%20oxidase&limit=100&page=2
  locator: numberOfHits, pageInfo and all returned result identifiers/names; exact
    query and page retained in URL.
  accessed_at: '2026-10-21T08:51:57.130173Z'
  support: context_only
  summary: QuickGO query 'ubiquinol oxidase', page 2 of 3, reports 277 hits across
    all pages. This snapshot was screened for relevant identity/reaction candidates;
    it is a bounded search result, not proof of absence throughout every ontology.
  snapshot_sha256: 43dfcba448429a7a7cbfe0e005cdcfa08844f4bd02a89e144ecee981352e657e
  search_scope: QuickGO native search, query 'ubiquinol oxidase', limit=100, page
    2/3; all pages of both queries were retrieved and screened. No exact bd-named
    identity emerged in these query results. GO:0009319, GO:0009486, GO:0009916 and
    GO:0102721 were inspected separately. This is an external ontology search; local
    ignored-file inclusion is not applicable.
- evidence_id: bdI-agent-go-ubiquinol-search-page3
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=ubiquinol%20oxidase&limit=100&page=3
  locator: numberOfHits, pageInfo and all returned result identifiers/names; exact
    query and page retained in URL.
  accessed_at: '2026-10-21T08:51:57.450809Z'
  support: context_only
  summary: QuickGO query 'ubiquinol oxidase', page 3 of 3, reports 277 hits across
    all pages. This snapshot was screened for relevant identity/reaction candidates;
    it is a bounded search result, not proof of absence throughout every ontology.
  snapshot_sha256: 9f79325bd97198f56cd66e48738605b560a3250dd25aa1e2d84f152a0b6ec527
  search_scope: QuickGO native search, query 'ubiquinol oxidase', limit=100, page
    3/3; all pages of both queries were retrieved and screened. No exact bd-named
    identity emerged in these query results. GO:0009319, GO:0009486, GO:0009916 and
    GO:0102721 were inspected separately. This is an external ontology search; local
    ignored-file inclusion is not applicable.
- evidence_id: bdi-prep-tax-562
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562
  locator: taxId, scientificName, rank and otherNames; this source establishes only
    its own taxon identity.
  accessed_at: '2026-10-21T08:39:15.639383Z'
  support: supports
  summary: NCBITaxon:562 is Escherichia coli at species rank, matching the canonical
    example.
  snapshot_sha256: ea038c30da3aab3426b7df16ce7a137cf2985e73d6ad8281971b9c390a74d2a8
- evidence_id: bdi-prep-tax-83333
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: taxId, scientificName, rank and otherNames; this source establishes only
    its own taxon identity.
  accessed_at: '2026-10-21T08:39:15.629858Z'
  support: supports
  summary: NCBITaxon:83333 is Escherichia coli K-12 at strain rank, with K12 as an
    alternate name, matching all four protein examples.
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: bdI-agent-tax-83332
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83332
  locator: taxId, scientificName, rank and otherNames; this source establishes only
    its own taxon identity.
  accessed_at: '2026-10-21T08:49:23.533630Z'
  support: supports
  summary: NCBITaxon:83332 is Mycobacterium tuberculosis H37Rv at strain rank, identifying
    the biological source of the comparative 7NKZ polymers.
  snapshot_sha256: e180d1c39d308888c25a8f6d2e43fb0c344b5c126f49422d1d83d3a2946585d1
- evidence_id: bdi-prep-IPR002585
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002585/
  locator: metadata.accession, type=family, name, full description and member_databases;
    only this family response is attested.
  accessed_at: '2026-10-21T08:39:15.704411Z'
  support: supports
  summary: The cytochrome ubiquinol oxidase subunit-1 family includes the P0ABJ9 CydA
    example and describes bacterial ubiquinol oxidation coupled to oxygen reduction.
    Its older cofactor-placement wording is not used to infer a new residue-level
    or subunit-specific heme mechanism.
  snapshot_sha256: c8ed5edbfc8ea938600485c31b949142cee495e646ddaa13056449aba65563a5
- evidence_id: bdi-prep-IPR003317
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR003317/
  locator: metadata.accession, type=family, name, full description and member_databases;
    only this family response is attested.
  accessed_at: '2026-10-21T08:39:15.835798Z'
  support: supports
  summary: The cytochrome ubiquinol oxidase subunit-2 family describes integral membrane
    proteins in bd-type quinol-dependent oxygen uptake. Its TIGR00203 member model
    supports CydB family identity; older cofactor text is not imported into this review.
  snapshot_sha256: 5fd530dc8c367d9b48028d36009c8a7f75ae487657d4b4983ee5aebb37c2ffe1
- evidence_id: bdi-prep-IPR011724
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR011724/
  locator: metadata.accession, type=family, name, full description and member_databases;
    only this family response is attested.
  accessed_at: '2026-10-21T08:39:16.163017Z'
  support: supports
  summary: The Cyd operon protein YbgT family names P56100 as its E. coli example
    and describes a small membrane-spanning protein. Its TIGR02106 member model is
    named cytochrome bd-I oxidase subunit CydX; older tentative membership wording
    is supplemented by separately inspected 6RKO structural metadata.
  snapshot_sha256: d356eeb2c7c9fcb5b83d3dbbcafd763deaff4eb367264e5f8f33a7721a30c71d
- evidence_id: bdi-prep-IPR047743
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR047743/
  locator: metadata.accession, type=family, name, full description and member_databases;
    only this family response is attested.
  accessed_at: '2026-10-21T08:39:16.257612Z'
  support: supports
  summary: The Membrane protein YnhF-like family describes small, approximately 29-residue
    gammaproteobacterial membrane proteins and includes NF033411, named cytochrome
    bd-I oxidase subunit CydH. This supports the target's bounded YnhF-like/CydH-model
    wording, not a forced rename of the UniProt primary gene.
  snapshot_sha256: e6a229daacfe27a2b4fce35e6bbab8c1802247e8bc60ac971078dde8c57d0e2a
- evidence_id: bdi-prep-P0ABJ9
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0ABJ9.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism, complete
    comments (FUNCTION, CATALYTIC ACTIVITY, COFACTOR, SUBUNIT and SUBCELLULAR LOCATION
    where present), features and uniProtKBCrossReferences.
  accessed_at: '2026-10-21T08:39:16.475711Z'
  support: supports
  summary: Reviewed P0ABJ9 is cytochrome bd-I ubiquinol oxidase subunit 1, gene cydA,
    taxon83333, with IPR002585. Its native inner-membrane annotation explicitly cites
    PMID:15013751 and PMID:16079137 with ECO:0000269, as the target notes state. Function
    and catalytic-activity annotations support electrogenic quinol oxidation and PMF
    contribution; cofactor annotations support heme association without independently
    rechecking an assay.
  snapshot_sha256: af4e17ad29e0033c733789bd15ea9d8a63e2464519939bc2e408e0a6b256b370
- evidence_id: bdi-prep-P0ABK2
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0ABK2.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism, complete
    comments (FUNCTION, CATALYTIC ACTIVITY, COFACTOR, SUBUNIT and SUBCELLULAR LOCATION
    where present), features and uniProtKBCrossReferences.
  accessed_at: '2026-10-21T08:39:16.470673Z'
  support: supports
  summary: Reviewed P0ABK2 is cytochrome bd-I ubiquinol oxidase subunit 2, gene cydB,
    taxon83333, with IPR003317. Its native inner-membrane annotation explicitly cites
    PMID:15013751 and PMID:16079137 with ECO:0000269. Its topology note also cites
    Zhang2004; the abstract-only paper access does not justify declaring that study
    irrelevant to CydB. Catalytic-activity annotations include EC7.1.1.7.
  snapshot_sha256: ee684c6cd1e2d5a05f245df7bee5400d9fe60ce2664ef304a8020aece0ce94e5
- evidence_id: bdi-prep-P56100
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P56100.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism, complete
    comments (FUNCTION, CATALYTIC ACTIVITY, COFACTOR, SUBUNIT and SUBCELLULAR LOCATION
    where present), features and uniProtKBCrossReferences.
  accessed_at: '2026-10-21T08:39:16.864955Z'
  support: supports
  summary: Reviewed P56100 is cytochrome bd-I ubiquinol oxidase subunit X, primary
    gene cydX and synonym ybgT, taxon83333, with IPR011724. The target accurately
    uses the accession as identity evidence and separately grounds membership in 6RKO.
    Database localization and older tentative subunit comments are not treated as
    direct structural proof.
  snapshot_sha256: f77290062640434e0e471b8050d10359cec77cb91836e22632f319b494a37d4a
- evidence_id: bdi-prep-A5A618
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/A5A618.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism, complete
    comments (FUNCTION, CATALYTIC ACTIVITY, COFACTOR, SUBUNIT and SUBCELLULAR LOCATION
    where present), features and uniProtKBCrossReferences.
  accessed_at: '2026-10-21T08:39:16.272722Z'
  support: supports
  summary: Reviewed A5A618 retains the recommended name Uncharacterized protein YnhF,
    primary gene ynhF, taxon83333, and IPR047743. Its membrane/topology annotations
    support the bounded single-pass description. The record correctly keeps this native
    protein identity distinct from the associated CydH family-model name.
  snapshot_sha256: b2d8fb8ee434a3e6e92f8a691892391c484db043674277627f207f9fe47ea574
- evidence_id: bdi-prep-query-cydA
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AcydA%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: Exact query in URL; entire results array and each result primaryAccession,
    entryType, genes and organism. No result-total HTTP header is attested by this
    receipt.
  accessed_at: '2026-10-21T08:39:17.170771Z'
  support: supports
  summary: The native exact-gene, reviewed-entry query restricted to taxon83333 returns
    one result, P0ABJ9, for cydA. This supports the recorded symbol/accession pairing;
    cydX and ybgT resolve to the same protein, not distinct subunits.
  snapshot_sha256: 5c36aded5449f0aa0978d88f4abef4cf210718826f1d67051d45851853e6b792
- evidence_id: bdi-prep-query-cydB
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AcydB%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: Exact query in URL; entire results array and each result primaryAccession,
    entryType, genes and organism. No result-total HTTP header is attested by this
    receipt.
  accessed_at: '2026-10-21T08:39:17.292501Z'
  support: supports
  summary: The native exact-gene, reviewed-entry query restricted to taxon83333 returns
    one result, P0ABK2, for cydB. This supports the recorded symbol/accession pairing;
    cydX and ybgT resolve to the same protein, not distinct subunits.
  snapshot_sha256: d53ae35e596dca3ebd132db6760560222cf5485e5fd8b61b6b9b3f65f4d0066d
- evidence_id: bdi-prep-query-cydX
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AcydX%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: Exact query in URL; entire results array and each result primaryAccession,
    entryType, genes and organism. No result-total HTTP header is attested by this
    receipt.
  accessed_at: '2026-10-21T08:39:17.190475Z'
  support: supports
  summary: The native exact-gene, reviewed-entry query restricted to taxon83333 returns
    one result, P56100, for cydX. This supports the recorded symbol/accession pairing;
    cydX and ybgT resolve to the same protein, not distinct subunits.
  snapshot_sha256: 69fed7990fdb53427b92351fbeb3feb3187ac2dc1e7aec7b1ea7fe913f215040
- evidence_id: bdi-prep-query-ybgT
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AybgT%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: Exact query in URL; entire results array and each result primaryAccession,
    entryType, genes and organism. No result-total HTTP header is attested by this
    receipt.
  accessed_at: '2026-10-21T08:39:17.456321Z'
  support: supports
  summary: The native exact-gene, reviewed-entry query restricted to taxon83333 returns
    one result, P56100, for ybgT. This supports the recorded symbol/accession pairing;
    cydX and ybgT resolve to the same protein, not distinct subunits.
  snapshot_sha256: 69fed7990fdb53427b92351fbeb3feb3187ac2dc1e7aec7b1ea7fe913f215040
- evidence_id: bdi-prep-query-ynhF
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AynhF%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: Exact query in URL; entire results array and each result primaryAccession,
    entryType, genes and organism. No result-total HTTP header is attested by this
    receipt.
  accessed_at: '2026-10-21T08:39:18.052813Z'
  support: supports
  summary: The native exact-gene, reviewed-entry query restricted to taxon83333 returns
    one result, A5A618, for ynhF. This supports the recorded symbol/accession pairing;
    cydX and ybgT resolve to the same protein, not distinct subunits.
  snapshot_sha256: dfbe7897e738b6adc763360a1fa15ebc7ef8e0719b068cd1604a709c31495bd3
- evidence_id: bdi-prep-pdb-6RKO
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/entry/6RKO
  locator: struct, exptl, rcsb_entry_info, rcsb_entry_container_identifiers, rcsb_primary_citation
    and EM metadata.
  accessed_at: '2026-10-21T08:39:18.917897Z'
  support: supports
  summary: 6RKO is an experimental E. coli cytochrome bd-I cryo-EM structure, 2.68
    A in the native entry, with four protein polymer entities. Its primary citation
    is Safarian2019, DOI:10.1126/science.aay0967, PMID:31604309. Entry metadata establishes
    the deposited structural identity; no coordinate or map reanalysis is claimed.
  snapshot_sha256: b5650c369bb24ab1365fbbf469b689c030b291cd39ad9246ede47424e7a428ca
- evidence_id: bdi-prep-assembly-6RKO
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/assembly/6RKO/1
  locator: pdbx_struct_assembly, rcsb_assembly_info and rcsb_struct_symmetry entries
    distinguished by kind.
  accessed_at: '2026-10-21T08:39:18.993085Z'
  support: supports
  summary: Assembly1 is a tetramer with four distinct protein entities and four instances.
    Global symmetry lists A1B1C1D1. The separate A2B1C1 pseudo-symmetry grouping must
    not be interpreted as biological duplication of an individual subunit.
  snapshot_sha256: 03f0637af88edb0a6d1229ad521bffd1ed53bcae8f1229750dec5eae2055c6ad
- evidence_id: bdi-prep-6RKO-entity-1
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/6RKO/1
  locator: entity_poly, entity_src_gen, rcsb_polymer_entity, rcsb_polymer_entity_container_identifiers,
    rcsb_polymer_entity_align, rcsb_entity_source_organism and rcsb_entity_host_organism;
    EC lineage where present.
  accessed_at: '2026-10-21T08:39:19.068785Z'
  support: supports
  summary: 6RKO polymer entity 1 is CydB, mapped to UniProtKB:P0ABK2, with genetically
    engineered source E. coli K-12 (taxon83333) and E. coli expression host. Its native
    EC lineage includes 7.1.1.7, quinol oxidase (electrogenic, proton-motive force
    generating); this is a database annotation rather than a new PMF assay.
  snapshot_sha256: 7ad660ab4b7a83ea8cb28f2ef625de7a85f29b5c91181070a533a33da9e0ace2
- evidence_id: bdi-prep-6RKO-entity-2
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/6RKO/2
  locator: entity_poly, entity_src_gen, rcsb_polymer_entity, rcsb_polymer_entity_container_identifiers,
    rcsb_polymer_entity_align, rcsb_entity_source_organism and rcsb_entity_host_organism;
    EC lineage where present.
  accessed_at: '2026-10-21T08:39:19.218777Z'
  support: supports
  summary: 6RKO polymer entity 2 is CydA, mapped to UniProtKB:P0ABJ9, with genetically
    engineered source E. coli K-12 (taxon83333) and E. coli expression host. Its native
    EC lineage includes 7.1.1.7, quinol oxidase (electrogenic, proton-motive force
    generating); this is a database annotation rather than a new PMF assay.
  snapshot_sha256: 2360610b19b736ca6483c1d68658b2f3d3c8a0cc69bfcdbfa1daea086ec6d7cb
- evidence_id: bdi-prep-6RKO-entity-3
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/6RKO/3
  locator: entity_poly, entity_src_gen, rcsb_polymer_entity, rcsb_polymer_entity_container_identifiers,
    rcsb_polymer_entity_align, rcsb_entity_source_organism and rcsb_entity_host_organism;
    EC lineage where present.
  accessed_at: '2026-10-21T08:39:19.254081Z'
  support: supports
  summary: 6RKO polymer entity 3 is YnhF, mapped to UniProtKB:A5A618, with genetically
    engineered source E. coli K-12 (taxon83333) and E. coli expression host. This
    entity does not carry the EC lineage used for the PMF edge; its membership rests
    on the deposited polymer and assembly records.
  snapshot_sha256: da8b5fb422d60c44805dc378316f1a1b3555d7fc22955afd5ed16f4ba73a9e6d
- evidence_id: bdi-prep-6RKO-entity-4
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/6RKO/4
  locator: entity_poly, entity_src_gen, rcsb_polymer_entity, rcsb_polymer_entity_container_identifiers,
    rcsb_polymer_entity_align, rcsb_entity_source_organism and rcsb_entity_host_organism;
    EC lineage where present.
  accessed_at: '2026-10-21T08:39:19.303157Z'
  support: supports
  summary: 6RKO polymer entity 4 is CydX, mapped to UniProtKB:P56100, with genetically
    engineered source E. coli K-12 (taxon83333) and E. coli expression host. Its native
    EC lineage includes 7.1.1.7, quinol oxidase (electrogenic, proton-motive force
    generating); this is a database annotation rather than a new PMF assay.
  snapshot_sha256: 3c583d12d695e4c097d27a5991462831721fdf0e71665a3075bba38557f2a613
- evidence_id: bdi-prep-pdb-7NKZ
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/entry/7NKZ
  locator: struct, exptl, rcsb_entry_info, rcsb_entry_container_identifiers and rcsb_primary_citation.
  accessed_at: '2026-10-21T08:39:19.341974Z'
  support: supports
  summary: 7NKZ is an experimental M. tuberculosis bd-oxidase cryo-EM entry at 2.5
    A, with two protein polymer entities and primary citation DOI:10.1038/s41467-021-25537-z.
    The comparison is limited to native deposited composition; that primary paper
    was not independently read.
  snapshot_sha256: faadcd2aeb030bdea625b832fd0f4bba5fa93b3a7c9ea1cb01dcaa2ef62da08a
- evidence_id: bdi-prep-assembly-7NKZ
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/assembly/7NKZ/1
  locator: pdbx_struct_assembly, rcsb_assembly_info and Global Symmetry entry in rcsb_struct_symmetry.
  accessed_at: '2026-10-21T08:39:19.369036Z'
  support: supports
  summary: Assembly1 is an author-defined heterodimer with two protein entities, two
    instances and global A1B1 stoichiometry. It supports the record's bounded two-polymer
    comparison, not universal absence of accessory proteins from every mycobacterial
    bd complex.
  snapshot_sha256: d3f7140cba6f264f064f69a17ad06bbbd39350ea978cc963e8af6261e30f99b2
- evidence_id: bdi-prep-7NKZ-entity-1
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/7NKZ/1
  locator: rcsb_polymer_entity, rcsb_polymer_entity_container_identifiers, rcsb_entity_source_organism,
    rcsb_entity_host_organism and entity_src_gen.
  accessed_at: '2026-10-21T08:39:19.398925Z'
  support: supports
  summary: 7NKZ polymer entity 1 is CydB, UniProtKB:O06139, with M. tuberculosis H37Rv
    source taxon83332. The separately listed expression host is Mycolicibacterium
    smegmatis MC2 155, taxon246196, and is not substituted for the biological source.
  snapshot_sha256: 02c40a9e01b6a4984f05341a1a2642d43b6bd7bc58d7dd5820e0a98392bdadc4
- evidence_id: bdi-prep-7NKZ-entity-2
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/7NKZ/2
  locator: rcsb_polymer_entity, rcsb_polymer_entity_container_identifiers, rcsb_entity_source_organism,
    rcsb_entity_host_organism and entity_src_gen.
  accessed_at: '2026-10-21T08:39:19.415656Z'
  support: supports
  summary: 7NKZ polymer entity 2 is CydA, UniProtKB:L7N662, with M. tuberculosis H37Rv
    source taxon83332. The separately listed expression host is Mycolicibacterium
    smegmatis MC2 155, taxon246196, and is not substituted for the biological source.
  snapshot_sha256: 5e370b1e7987762c1d1124bb5fe5de140db8afa262f5fab9f78259b8a682d83a
- evidence_id: bdi-prep-safarian-pmid-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A31604309%20AND%20SRC%3AMED
  locator: 'resultList.result[0]: exact PMID31604309, DOI, title, authors, publication
    details and entire abstractText.'
  accessed_at: '2026-10-21T08:39:18.736907Z'
  support: supports
  summary: The exact primary-article abstract identifies E. coli bd-I cryo-EM structure
    determination and previously unknown CydH, and states oxygen-to-water reduction
    and structural divergence from mitochondrial cytochrome c oxidases. Readable tier
    is the abstract plus citation metadata, not the main text, Methods or supplementary
    material.
  snapshot_sha256: 5151ff576c237af1ffa4f2a770480115afbe6b32147f1618b8c025565638c25c
- evidence_id: bdi-prep-zhang2004-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A15013751%20AND%20SRC%3AMED
  locator: 'resultList.result[0]: exact PMID15013751, DOI10.1016/S0014-5793(04)00125-5,
    title, authors and entire abstractText.'
  accessed_at: '2026-10-21T08:39:19.127884Z'
  support: supports
  summary: The exact Zhang2004 primary abstract reports experimental beta-lactamase
    fusion tests supporting the revised nine-transmembrane-helix CydA topology and
    periplasmic-side oxygen-reactive site. Full methods, strain details and individual
    fusion results were not read. Native UniProt citation attribution was checked
    separately for both CydA and CydB.
  snapshot_sha256: 13cb5d944dac26fc217c91dcbea739938715faff12d1101c938f0b41c38a841e
- evidence_id: bdi-prep-stenberg2005-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A16079137%20AND%20SRC%3AMED
  locator: 'resultList.result[0]: PMID16079137, DOI10.1074/jbc.M506479200, title,
    authors and entire abstractText.'
  accessed_at: '2026-10-21T08:39:19.271342Z'
  support: supports
  summary: The Stenberg2005 primary abstract describes membrane-complex BN-PAGE, second-dimension
    SDS-PAGE and mass spectrometry. Its YhcB subunit assignment is explicitly tentative;
    YhcB is not the YnhF/CydH small protein in the target. Detailed localization and
    model scope are assessed from separately captured body passages.
  snapshot_sha256: 0c8a782dd1022fdd5016d2f9b2ca9cdb04e46072105f4233ec07edeff9af1d38
- evidence_id: bdI-agent-bdi-browser5
  kind: primary_source
  reference: https://doi.org/10.1074/jbc.M506479200
  locator: 'First JBC/DOI result only: Results > Protein Complexes in the Inner Membrane
    > Bioenergetic Complexes, cytochrome bd paragraph; Figure3 caption; Discussion
    YhcB paragraph. Other search results, including a later review, are not used.
    Figure pixels not inspected.'
  accessed_at: '2026-10-21T08:42:51.281Z'
  support: supports
  summary: Stenberg2005 primary Results identify CydA and CydB in the inner-membrane
    preparation and tentatively associate YhcB; Discussion retains that tentative
    scope. The Figure3 caption distinguishes proteins identified by mass spectrometry
    from inferred bands. This supports localization/association, not the modern four-subunit
    inventory or a newly verified PMF mechanism. The snapshot is a web.run indexed
    publisher extraction, not an attested HTTP200 response or complete-article download.
  snapshot_sha256: 1359a24816b54519a127f7c3c2fe0e188ecccb08eb898acadc88b2860e985162
- evidence_id: bdI-agent-bdi-stenberg-methods-search2
  kind: primary_source
  reference: https://doi.org/10.1074/jbc.M506479200
  locator: 'First JBC/DOI result only: Materials and Methods > Preparation of Membrane
    Vesicles; One-dimensional BN-PAGE; initial Two-dimensional SDS-PAGE paragraph;
    Results > Purification of Membrane Protein Complexes and Protein Identification.
    Table1 is truncated before Cyd rows; full MS methods, complete table and supplementary
    figures were not read.'
  accessed_at: '2026-10-21T08:43:22.725Z'
  support: supports
  summary: Stenberg2005 used BL21(DE3)pLysS grown at 37 C in LB and harvested in late
    log phase; sucrose-gradient membrane vesicles were solubilized for BN-PAGE using
    0.5% DDM. The extracted Methods and Results explain the membrane separation and
    protein-identification workflow. This is direct experimental context for BL21,
    not a claim that the experiment used K-12. The snapshot is a web.run indexed publisher
    extraction, not an attested HTTP200 response or complete-article download.
  snapshot_sha256: 9cb13cd4e0ee40b1493ce919ebc6ba74b467ea5adc5849fc0a92a4b394aa2e0d
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/energy_complex/cytochrome_bd_i_ubiquinol_oxidase_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:41:37Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/energy_complex/cytochrome_bd_i_ubiquinol_oxidase_complex.yaml'
  snapshot_sha256: 1d18f6d9ec091bedb62f16279fac83fedd613a91e8d3699de63069a30fd95715
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/energy_complex/cytochrome_bd_i_ubiquinol_oxidase_complex.yaml
    --out /private/tmp/cellstructure-batch13-20261021-vud60b4w/cytochrome_bd_i_ubiquinol_oxidase_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:41:40Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/energy_complex/cytochrome_bd_i_ubiquinol_oxidase_complex.yaml\
    \ --out /private/tmp/cellstructure-batch13-20261021-vud60b4w/cytochrome_bd_i_ubiquinol_oxidase_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch13-20261021-vud60b4w/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch13-20261021-vud60b4w/cytochrome_bd_i_ubiquinol_oxidase_complex-strict.tsv"
  snapshot_sha256: 15cc46c7e846781aa8f6a650baad0b4cc04cd6ecde1099128a1468287af1b8ff
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/energy_complex/cytochrome_bd_i_ubiquinol_oxidase_complex.yaml;
    exact collect() scope; hash identifies the entire original resolver TSV; original
    /private/tmp/cellstructure-record-reviews-UhRFh7/repo/reports/curie_check.tsv,
    not the generated resolver-slice.json
  accessed_at: '2026-10-21T08:54:46Z'
  support: supports
  summary: '14 of 20 collected target identifiers returned OK at the unchanged base.
    Residuals: PDB:6RKO: SKIPPED; resolved by evidence bdi-prep-pdb-6RKO; PDB:7NKZ:
    SKIPPED; resolved by evidence bdi-prep-pdb-7NKZ; PMID:15013751: UNREACHABLE; resolved
    by evidence bdi-prep-zhang2004-meta; PMID:16079137: UNREACHABLE; resolved by evidence
    bdi-prep-stenberg2005-meta; PMID:31604309: UNREACHABLE; resolved by evidence bdi-prep-safarian-pmid-meta;
    cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex: SKIPPED; resolved
    by evidence record. Source-native identity checked separately.'
  snapshot_sha256: 68d64e4e86437df228658f43be4d47b41054fe882fedf357e660293691a0a061
- evidence_id: native-verify
  kind: validation
  reference: uv run python scripts/uniprot_genes.py --verify --record data/structures/energy_complex/cytochrome_bd_i_ubiquinol_oxidase_complex.yaml
  locator: Captured native gate log; command and start/end UTC in matching receipt.
  accessed_at: '2026-10-21T08:48:40.563085Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: uv run python scripts/uniprot_genes.py --causal-graphs --record data/structures/energy_complex/cytochrome_bd_i_ubiquinol_oxidase_complex.yaml
  locator: Captured native gate log; command and start/end UTC in matching receipt.
  accessed_at: '2026-10-21T08:48:41.206159Z'
  support: supports
  summary: "data/structures/energy_complex/cytochrome_bd_i_ubiquinol_oxidase_complex.yaml\
    \  (cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex)\n  cytochrome_bd_i_quinol_oxygen_coupling\t\
    cydA\tCOVERED\t->cytochrome_bd_i_subunit_i (UniProtKB:P0ABJ9)\n  cytochrome_bd_i_quinol_oxygen_coupling\t\
    cydB\tCOVERED\t->cytochrome_bd_i_subunit_ii (UniProtKB:P0ABK2)\n\ncausal_graphs\
    \ GENE_OR_PROTEIN node summary:\n     2  COVERED                   component_ref\
    \ target holds protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES\
    \          component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     2  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: 2b1a2521bf3fe54b2b6378d53eb1f62efc250910532198b8248a140c60e933d2
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
  topic: Named bd-I identity and ontology boundaries
  outcome: supported
  target_ids:
  - cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex
  summary: The local identifier, synonym, membrane-bound terminal-oxidase definition
    and multiprotein-complex kind match the E. coli bd-I entry. The two parent GO
    classes are valid broader is-a classifications, not parthood assertions. Cytochrome
    o/bo3 candidates denote another oxidase. The historical statement that no exact
    bd activity term was found is not contradicted by a generic reaction term.
  evidence_ids:
  - bdi-prep-go
  - bdI-agent-go-candidates
  - bdI-agent-go-0102721
  - bdi-prep-pdb-6RKO
  - bdi-prep-safarian-pmid-meta
  - record
  - bdI-agent-go-bd-search
  - bdI-agent-go-bd-search-page2
  - bdI-agent-go-ubiquinol-search
  - bdI-agent-go-ubiquinol-search-page2
  - bdI-agent-go-ubiquinol-search-page3
- assessment_id: composition
  area: evidence
  topic: Four deposited constituent proteins
  outcome: supported
  target_ids:
  - cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex
  summary: 6RKO independently maps all four component rows to the stated polymer entities
    and accessions, with one instance of each in the global biological assembly. CydA
    and CydB are the named core constituents. Their membership is supported; assembly
    necessity is assessed separately below. The two small-subunit roles remain limited
    to the resolved E. coli example and essentiality UNKNOWN.
  evidence_ids:
  - bdi-prep-pdb-6RKO
  - bdi-prep-assembly-6RKO
  - bdi-prep-6RKO-entity-1
  - bdi-prep-6RKO-entity-2
  - bdi-prep-6RKO-entity-3
  - bdi-prep-6RKO-entity-4
  - bdi-prep-P0ABJ9
  - bdi-prep-P0ABK2
  - bdi-prep-P56100
  - bdi-prep-A5A618
  - record
- assessment_id: families
  area: grounding
  topic: Family versus protein identity
  outcome: supported
  target_ids:
  - cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex
  summary: The four InterPro entries are genuine protein families matching the stated
    subunit identities. IPR047743 explicitly includes the CydH NCBIfam model, while
    A5A618 remains primary gene ynhF. Older tentative membership or cofactor descriptions
    are not allowed to override the separately deposited four-polymer architecture
    or introduce a detailed heme model.
  evidence_ids:
  - bdi-prep-IPR002585
  - bdi-prep-IPR003317
  - bdi-prep-IPR011724
  - bdi-prep-IPR047743
  - bdi-prep-P0ABJ9
  - bdi-prep-P0ABK2
  - bdi-prep-P56100
  - bdi-prep-A5A618
  - bdi-prep-6RKO-entity-1
  - bdi-prep-6RKO-entity-2
  - bdi-prep-6RKO-entity-3
  - bdi-prep-6RKO-entity-4
  - record
- assessment_id: proteins
  area: grounding
  topic: Taxon-paired protein examples and aliases
  outcome: supported
  target_ids:
  - cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex
  summary: All four example names, primary genes, reviewed statuses and K-12 taxon
    pairs agree with native UniProt. Exact reviewed-gene queries return the expected
    entries, and cydX/ybgT is one accession. The target explicitly restricts protein
    examples to identity evidence; PDB supplies membership. Both graph protein nodes
    resolve to the correct components and verified examples.
  evidence_ids:
  - bdi-prep-P0ABJ9
  - bdi-prep-P0ABK2
  - bdi-prep-P56100
  - bdi-prep-A5A618
  - bdi-prep-query-cydA
  - bdi-prep-query-cydB
  - bdi-prep-query-cydX
  - bdi-prep-query-ybgT
  - bdi-prep-query-ynhF
  - bdi-prep-tax-83333
  - record
- assessment_id: localization
  area: evidence
  topic: Experimental citation attribution and strain precision
  outcome: supported
  target_ids:
  - cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex
  summary: The target notes correctly say that UniProt cites Zhang2004 and Stenberg2005
    as ECO:0000269 evidence for CydA/B inner-membrane location. Stenberg body passages
    directly identify CydA/B in a membrane-complex preparation from BL21(DE3)pLysS,
    while the representative UniProt identities are K-12. These are distinct provenance
    statements, not a demonstrated record error. Abstract-only Zhang access cannot
    establish every tested construct or exclude CydB participation.
  evidence_ids:
  - bdi-prep-P0ABJ9
  - bdi-prep-P0ABK2
  - bdi-prep-zhang2004-meta
  - bdi-prep-stenberg2005-meta
  - bdI-agent-bdi-browser5
  - bdI-agent-bdi-stenberg-methods-search2
  - record
- assessment_id: taxonomy
  area: scope
  topic: Species example, strain and comparison
  outcome: supported
  target_ids:
  - cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex
  summary: The canonical E. coli species label agrees with taxon562; 6RKO polymer
    source and protein examples specify K-12 taxon83333. The separate 7NKZ comparison
    has M. tuberculosis H37Rv source taxon83332 and a distinct expression host. The
    record does not assert that every bd oxidase or strain has the E. coli accessory-subunit
    set.
  evidence_ids:
  - bdi-prep-tax-562
  - bdi-prep-tax-83333
  - bdI-agent-tax-83332
  - bdi-prep-pdb-6RKO
  - bdi-prep-pdb-7NKZ
  - bdi-prep-assembly-7NKZ
  - bdi-prep-6RKO-entity-1
  - bdi-prep-6RKO-entity-2
  - bdi-prep-6RKO-entity-3
  - bdi-prep-6RKO-entity-4
  - bdi-prep-7NKZ-entity-1
  - bdi-prep-7NKZ-entity-2
  - record
- assessment_id: function
  area: evidence
  topic: Reaction and PMF contribution
  outcome: supported
  target_ids:
  - cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex
  summary: Ubiquinol oxidation, oxygen reduction, ubiquinone/water products and a
    bd architecture distinct from heme-copper oxidases are supported at the reaction/annotation
    level. RCSB EC7.1.1.7 annotations and UniProt function/reaction comments support
    the stated PMF contribution. Neither the target nor this review claims that bd-I
    actively pumps protons or that a newly inspected functional assay measured proton
    stoichiometry.
  evidence_ids:
  - bdi-prep-IPR002585
  - bdi-prep-safarian-pmid-meta
  - bdI-agent-go-0102721
  - bdi-prep-P0ABJ9
  - bdi-prep-P0ABK2
  - bdi-prep-6RKO-entity-1
  - bdi-prep-6RKO-entity-2
  - bdi-prep-6RKO-entity-3
  - bdi-prep-6RKO-entity-4
  - record
- assessment_id: graph
  area: graph
  topic: Nonmechanistic functional topology
  outcome: supported
  target_ids:
  - cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex
  summary: All nine nodes and eight edges were checked. CydA/B component references
    and the self-structure reference resolve within this target; the graph correctly
    keeps ubiquinone and water as products and oxygen as terminal acceptor. Its NONMECHANISTIC
    scope excludes a detailed heme sequence or proton-channel mechanism. Structure/contribution
    edges rest on deposited entities and function annotation, not direct kinetic proof
    from the coordinate entry.
  evidence_ids:
  - bdi-prep-pdb-6RKO
  - bdi-prep-assembly-6RKO
  - bdi-prep-safarian-pmid-meta
  - bdi-prep-IPR002585
  - bdI-agent-go-0102721
  - bdi-prep-6RKO-entity-1
  - bdi-prep-6RKO-entity-2
  - bdi-prep-6RKO-entity-3
  - bdi-prep-6RKO-entity-4
  - bdi-prep-P0ABJ9
  - bdi-prep-P0ABK2
  - record
- assessment_id: small-subunits
  area: scope
  topic: Open cross-lineage boundary
  outcome: supported
  target_ids:
  - cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex
  summary: The existing discussion accurately contrasts four-polymer E. coli 6RKO
    with two-polymer M. tuberculosis 7NKZ. This supports retaining the open bd-I/bd-II/two-subunit
    boundary without projecting small subunits universally. The older tentative YhcB
    association is a separate hypothesis, not a mandatory fifth structural component
    or a synonym for YnhF.
  evidence_ids:
  - bdi-prep-pdb-6RKO
  - bdi-prep-assembly-6RKO
  - bdi-prep-pdb-7NKZ
  - bdi-prep-assembly-7NKZ
  - bdi-prep-stenberg2005-meta
  - bdI-agent-bdi-browser5
  - bdi-prep-7NKZ-entity-1
  - bdi-prep-7NKZ-entity-2
  - record
- assessment_id: provenance
  area: provenance
  topic: Exact source tiers and access limits
  outcome: supported
  target_ids:
  - cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex
  summary: Native database responses establish identifier, family, taxon, entity and
    annotation facts. Safarian2019 and Zhang2004 were readable only as primary abstracts.
    Stenberg2005 was readable as discontinuous indexed primary-body passages with
    explicit locators, not a complete native article. All raw/meta snapshots preserve
    original UTCZ timestamps and hashes, including failed access attempts and reused
    metadata. No browser response is presented as HTTP status evidence.
  evidence_ids:
  - bdi-prep-safarian-pmid-meta
  - bdi-prep-zhang2004-meta
  - bdi-prep-stenberg2005-meta
  - bdI-agent-bdi-browser5
  - bdI-agent-bdi-stenberg-methods-search2
  - bdi-prep-pdb-6RKO
  - bdi-prep-P0ABJ9
  - bdi-prep-P0ABK2
  - bdi-prep-P56100
  - bdi-prep-A5A618
  - record
- assessment_id: completeness
  area: completeness
  topic: Bounded scope and maintained ownership
  outcome: supported
  target_ids:
  - cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex
  summary: The record supplies a supported four-component example, taxon-paired identity
    evidence, a reaction graph and an explicit small-subunit scope TODO. Optional
    images, physical properties, detailed cofactor chemistry or additional generic
    reaction identifiers are not automatic defects. No exact structural misidentification,
    wrong protein mapping, unsupported universal subunit claim or graph-direction
    error was established; native PROPOSED status and historical curation remain unchanged.
  evidence_ids:
  - bdi-prep-pdb-6RKO
  - bdi-prep-assembly-6RKO
  - bdi-prep-pdb-7NKZ
  - bdI-agent-go-0102721
  - record
  - policy
- assessment_id: assembly-necessity
  area: evidence
  topic: Assembly necessity versus constituent membership
  outcome: unknown
  target_ids:
  - cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex
  summary: The schema defines essentiality by whether the structure forms without
    the component. The inspected sources establish constituent membership and functions,
    but those observations alone do not establish this assembly-necessity assertion.
    No subunit-deletion/assembly experiment was independently checked here; catalytic
    necessity, organismal viability and intact structural membership are distinct
    questions.
  evidence_ids:
  - bdi-prep-pdb-6RKO
  - bdi-prep-assembly-6RKO
  - bdi-prep-6RKO-entity-1
  - bdi-prep-6RKO-entity-2
  - bdi-prep-6RKO-entity-3
  - bdi-prep-6RKO-entity-4
  - bdi-prep-P0ABJ9
  - bdi-prep-P0ABK2
  - bdi-prep-P56100
  - bdi-prep-A5A618
  - record
  - policy
findings: []
actions: []
limitations:
- Safarian2019 main text, full Methods and supplementary material were not recovered.
  The exact primary abstract and RCSB entry/entity/assembly metadata support the claims
  at their stated tiers; no atomic coordinates, cryo-EM density, image pixels or newly
  retrieved PMF assay were independently analyzed.
- Zhang2004 was read as metadata and complete primary abstract only. Full experimental
  strain details, construct positions and individual topology results remain unread.
  Both UniProt entries directly attest the citation attribution made by the record.
- Stenberg2005 primary body access consists of the two indexed publisher extracts
  identified in evidence locators. Complete mass-spectrometry methods, Cyd rows of
  Table1, supplementary figures and figure pixels were not read. Native Elsevier API
  access returned metadata rather than a complete body; browser metadata has null
  HTTP status.
- Stenberg2005 experiments used BL21(DE3)pLysS; the target protein examples identify
  K-12 reference entries. Citation attribution is verified without asserting an exact
  experimental-strain match or an unqualified transfer of every measured property.
- PMF contribution is supported by native functional annotations and the bounded terminal-oxidase
  reaction. This review does not independently establish proton/electron stoichiometry,
  active proton pumping, catalytic kinetics or physiological essentiality under specified
  conditions.
- InterPro family descriptions contain older tentative subunit and cofactor wording.
  They are used for exact family identity and bounded reaction context, not as modern
  proof of heme placement or universal accessory-subunit composition.
- The 7NKZ comparison is restricted to native deposited entity and assembly metadata.
  Its associated 2021 primary paper was not independently read; two deposited polymers
  do not prove absence of accessory proteins in all mycobacterial preparations.
- Both QuickGO searches were fully paginated, but their failure to return a bd-specific
  identity is limited to those queries. GO:0102721 supplies a generic reaction candidate;
  no universal ontology-absence claim or automatic optional-grounding finding is made.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
- The schema defines essentiality by whether the structure forms without the component.
  The inspected sources establish constituent membership and functions, but those
  observations alone do not establish this assembly-necessity assertion. No subunit-deletion/assembly
  experiment was independently checked here; catalytic necessity, organismal viability
  and intact structural membership are distinct questions.
notes:
- Native inspect and focused schema/strict checks completed before assessment. All
  thirteen native input hashes were independently checked at unchanged base99692a3d5f16a7dcd6db7e3811344c299a977b81.
  No neighboring maintained record was needed.
- The user-authorized batch task explicitly requests an unsaved draft even for a clean
  outcome. No issue is manufactured to justify a saved review; root retains finalization
  and save responsibility.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
