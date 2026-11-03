# Respiratory complex I arm composition, protein identity and coupling evidence review

- Review: 20261021T091350Z-respiratory-chain-complex-i-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T08:50:35Z
- Finished UTC: 2026-10-21T09:13:50Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The exact GO identity, arm-level components, fourteen protein mappings and nonmechanistic quinone/proton coupling graph are supported. No concrete curation issue was established; native quinone, accessory-subunit and structural-mechanism limits remain explicit.

## Scope And Provenance

Entire single target, all named proteins and stable identifiers, exact native PDB entry/assembly/polymer mappings, full main primary article and Methods, bounded arm-grounding candidates, and native protein/graph verification.

Selection: Sixth selected target in batch fourteen, following fixed repository path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0045271 | data/structures/energy_complex/respiratory_chain_complex_i.yaml | maintained | respiratory chain complex I |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0045271 | Focused validator passed. |
| Focused native strict | passed | True | GO:0045271 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0045271 | 19 identifiers OK; 2 transport/skipped residuals independently resolved. |
| Native UniProt example verification | passed | True | GO:0045271 | All fourteen protein examples verified. |
| Native graph protein coverage | passed | True | GO:0045271 | Both arm nodes COVERED; all other coverage categories zero. |
| Expression-module applicability | not_applicable | False | GO:0045271 | The record makes no expression-module or regulator claim used as structural evidence; no iModulon analysis is required. |
| Claim-level scientific review | passed | True | GO:0045271 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0045271 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0045271 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0045271 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0045271 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0045271 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Exact complex and synonym identity

identity: supported. Targets: GO:0045271.

The exact GO cellular-component identity, both exact synonyms, L-shaped architecture and multiprotein-complex kind agree with the native term and primary structure. The definition intentionally avoids treating the bacterial projecting arm as a mitochondrial matrix structure.

### Parent and molecular-function relations

scope: supported. Targets: GO:0045271.

GO:0045271 is explicitly an is_a child of respiratory chain complex GO:0098803. GO:0008137 is a molecular function possessed by the complex, not a structural parent or biological process. The target uses these relations in the correct places.

### Arm composition and conserved-core examples

evidence: supported. Targets: GO:0045271.

The membrane set nqo7/8/10–14 and peripheral set nqo1–6/9 exactly match primary Supplementary Table3. The examples cover fourteen conserved core subunits; they do not assert that the Thermus crystallization preparation contains only fourteen proteins. The primary text and PDB support sixteen proteins in that preparation, including extra hydrophilic constituents. This establishes the intact two-arm architecture; it does not establish formation or assembly necessity through arm-removal experiments.

### Architecture versus formation and assembly necessity

scope: unknown. Targets: GO:0045271.

The schema defines ESSENTIAL in terms of formation or assembly. Intact-complex structures and functional arm assignments establish presence and architecture, but the inspected sources do not test whether a structure can form after removing an entire arm. Assembly necessity remains unverified here and is not inferred from catalytic coupling, intact structural presence or cell viability.

### Whole-arm scope versus subunit/domain candidates

grounding: supported. Targets: GO:0045271.

Retaining REVIEWED_LABEL_ONLY for each whole arm is justified. The tempting mitochondrial segment GO terms are obsolete, and inspected InterPro candidates describe domains shared with other proteins rather than complete arms. Existing Nuo/Nqo family cross-references can inform finer future rows but do not automatically replace these component identities. Historical first-pass verification wording is preserved; no exhaustive cross-database absence claim is made.

### All fourteen taxon-paired examples

grounding: supported. Targets: GO:0045271.

Each accession, primary gene, recommended name, reviewed status and taxon300852 pair matches native UniProt and the corresponding deposited polymer mapping. All declared symbols are covered exactly once in their component cohorts. The identity-only evidence notes correctly distinguish accessions from membership proof.

### Species example and HB8 preparation

scope: supported. Targets: GO:0045271.

Thermus thermophilus species274 is the correct canonical example, while protein and PDB source entries specify HB8 taxon300852. The generic record does not project the Thermus sixteen-subunit inventory onto every bacterial or mitochondrial complex I. Crystallization temperatures and diffraction conditions are experimental preparation parameters, not organismal growth or physiological operating temperatures.

### Generic quinone coupling and native acceptor

evidence: supported. Targets: GO:0045271.

The generic complex-I molecular function and quinone-reduction/proton-translocation description agree with GO and the paper. The Thermus enzyme uses menaquinone-8 in vivo; the primary study explicitly reports activity with decyl-ubiquinone and structural analogue binding. The record's generic GO activity name does not assert that native Thermus uses ubiquinone exclusively. The graph's quinone-pool label remains appropriately broad.

### Nonmechanistic topology and mechanistic proposal

graph: supported. Targets: GO:0045271.

All six nodes and five edges were read. NADH input enters the peripheral arm, electrons reach the quinone site, and intact-enzyme quinone reduction couples to the membrane arm and PMF contribution. Both protein nodes resolve to their component examples. The graph is explicitly NONMECHANISTIC and its coupling-edge evidence notes say proposed; no free-quinone causal driver, observed conformational sequence or direct four-proton assay is claimed.

### Direct structural evidence versus inferred dynamics

scope: supported. Targets: GO:0045271.

The 2013 evidence directly resolves architecture, redox-center arrangement and analogue-binding density. Its long-range conformational coupling and proton-channel paths are structural proposals, with modeled waters and further redox-state/time-resolved studies explicitly required. Analogue-bound models are called preliminary in Methods S10. Introductory reaction stoichiometry summarizes earlier experiments; it is not a new stoichiometric measurement in this crystallographic study. Nqo16 activity dispensability is attributed to personal communication in Supplementary Discussion page2, not a displayed primary assay.

### Readable source and native authority tiers

provenance: supported. Targets: GO:0045271.

The primary author-manuscript JATS was read across all main claim-bearing text and Methods, and the supplementary PDF was read at its specified discussion/table passages. Native GO supplies term semantics; taxonomy/UniProt/PDB supply identity and deposited composition. All snapshots retain exact raw hashes, actual statuses/content types and original UTCZ access times. Failed HTTP200 download-preparation HTML is distinct from the successful Europe PMC ZIP and its separately hashed extracted PDF.

### Bounded inventory and open grounding discussion

completeness: supported. Targets: GO:0045271.

The record supports the two-arm abstraction, conserved-core examples and broad functional topology. A complete list of Thermus accessory proteins, all family-level rows, images, physical properties or each redox cofactor is not mandatory. The existing finer-grounding discussion is a reasonable unresolved curation task. No concrete identity, protein-mapping, relation or evidence-placement defect was established.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/energy_complex/respiratory_chain_complex_i.yaml; Entire maintained YAML: definition, synonym scopes, parent, both arm components and fourteen protein examples, taxon example, function, every graph node/edge, discussion and history. | context_only | The entire record was read. It describes generic respiratory complex I using two arm-level components, conserved-core Thermus examples and a nonmechanistic coupling graph. Native PROPOSED status and historical notes are unchanged. |
| policy | docs/CURATION.md; Identifiers, components, protein examples, causal graphs, discussions and status; review and UniProt guidance in source.inputs. | context_only | An arm-level protein complex must not be grounded to a single subunit/domain. Protein accessions establish the stated identities, with structural membership checked separately. Optional omissions and historical first-pass search notes do not automatically establish defects. |
| complex-i-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0045271%2CGO%3A0098803%2CGO%3A0008137; All three native results: id, isObsolete, name, definition, synonyms, comment, aspect and children relation values. | supports | Active GO:0045271 exactly identifies respiratory chain complex I and lists both recorded synonyms as exact. GO:0098803 explicitly lists GO:0045271 as an is_a child. GO:0008137 is the molecular function NADH dehydrogenase (ubiquinone) activity, with an NADH/ubiquinone-to-NAD+/ubiquinol reaction coupled to proton translocation; its relation to GO:0045271 is capable_of. The CC definition uses mitochondrial matrix language, whereas the target appropriately generalizes the projecting arm for bacteria. |
| complex-i-agent-go-arm-candidates | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0042652%2CGO%3A0042653; Both exact results: id, isObsolete, name, definition, comment and synonym scope. | context_only | GO:0042652 and GO:0042653 describe the mitochondrial complex-I peripheral and membrane segments, respectively, and are both explicitly obsolete. The native comments state that these subcomplexes are out of GO scope. Neither is an active source-neutral grounding for the record's bacterial/mitochondrial arm-level component. |
| complex-i-agent-go-peripheral-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=peripheral%20arm&amp;limit=100; numberOfHits, pageInfo and result identifiers/names; exact query and page in URL. | context_only | QuickGO candidate search for 'peripheral arm'. All 96 returned hits; one complete page. Relevant obsolete arm candidates were then inspected through their exact native term records. |
| complex-i-agent-go-membrane-arm-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=membrane%20arm&amp;limit=100; numberOfHits, pageInfo and result identifiers/names; exact query and page in URL. | context_only | QuickGO candidate search for 'membrane arm'. First 100 of 1643 reported hits, page1 of17; intentionally bounded candidate screening, not an exhaustive search. Relevant obsolete arm candidates were then inspected through their exact native term records. |
| complex-i-agent-tax-274 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/274; taxId, scientificName, rank and otherNames. | supports | NCBITaxon:274 is Thermus thermophilus at species rank, matching the canonical structural example. |
| complex-i-agent-tax-300852 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/300852; taxId, scientificName, rank and otherNames. | supports | NCBITaxon:300852 is Thermus thermophilus HB8 at strain rank, with Thermus thermophilus ATCC27634 as a synonym. It matches all fourteen protein examples and the deposited source organism. |
| complex-i-agent-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A23417064%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; resultList.result[0]: PMID, PMCID, DOI, title, authors, publication details and abstractText. | supports | The exact Europe PMC result identifies Baradaran et al.2013, Crystal structure of the entire respiratory complex I, PMID23417064, PMCIDPMC3672946, DOI10.1038/nature11871. Metadata and abstract report a 3.3 A, sixteen-subunit Thermus structure; detailed assessment uses the separately retrieved primary body. |
| complex-i-agent-baradaran2013-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3672946/fullTextXML; Native Europe PMC JATS PMC3672946. Complete abstract, introductory P3–P10/FD1, main S1–S4 and Methods S6/S7–S11 read; all main Figure1–5 captions read. Key locators: S1 composition, S3 native substrate/analogue distinction, S4 proposed coupling and final limitation paragraph, S7 purification, S8 crystallization, S9 diffraction and S10 refinement. Figure pixels and raw coordinates not reanalyzed. | supports | The full primary author manuscript resolves intact T. thermophilus complex I with nine hydrophilic and seven membrane subunits, FMN/Fe-S centers and the quinone chamber. S1 lists membrane Nqo7/8/10–14 and identifies Nqo16 as crystallization-associated. S3 distinguishes native menaquinone-8 from active decyl-ubiquinone and reports quinone-analogue binding. S4/Figure5 explicitly propose long-range coupling; the main text does not directly observe a catalytic conformational cycle. Methods describe separated Nqo16-containing and lacking preparations, detergent purification, intact-complex crystallization at23 C, diffraction at100 K, molecular replacement and preliminary analogue-bound models. General reaction and stoichiometry context cites earlier work. |
| complex-i-agent-baradaran2013-supplement-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3672946/supplementaryFiles; HTTP200 Europe PMC supplementaryFiles ZIP; member NIHMS50981-supplement-1.pdf extracted with SHA256 0fc0c25b63a69c6342d45bc7432b982ac7d4e68047779635da6382313da4e426. Read PDF pages2–10 Supplementary Discussion, page13 Table3 and page14 Table4a/b. Table3 exactly resolves both seven-protein cohorts. Other supplementary tables, figure pixels and references were not independently audited. Evidence hash identifies the original ZIP response; extraction provenance is in supplement-extraction.json. | supports | The recovered primary supplementary PDF explicitly assigns Nqo1–6/9 to the hydrophilic domain and Nqo7/8/10–14 to the membrane domain in Table3, matching both example cohorts. It identifies Nqo15 and Nqo16 as extra hydrophilic proteins. Discussion identifies Nqo16 as TTHA1528 and proposes an assembly/chaperone role; its dispensability for oxidoreductase/proton-pumping activity is attributed to personal communication, not a displayed assay. The coupling discussion retains alternatives and model uncertainty. Table4 interaction estimates are computational PISA analysis, not an independent binding experiment. |
| complex-i-agent-pdb-4HEA | https://data.rcsb.org/rest/v1/core/entry/4HEA; struct, exptl, rcsb_entry_container_identifiers, rcsb_entry_info, rcsb_primary_citation and diffraction resolution fields. | supports | PDB4HEA is the entire Thermus thermophilus complex-I X-ray structure linked to the exact Baradaran2013 citation. It has sixteen distinct protein polymer entities, with two copies in the asymmetric-unit deposition and an overall resolution near3.3 A. The thirty-two deposited polymer instances are not thirty-two distinct enzyme subunits. |
| complex-i-agent-assembly-4HEA | https://data.rcsb.org/rest/v1/core/assembly/4HEA/1; pdbx_struct_assembly, rcsb_assembly_info and rcsb_struct_symmetry entries distinguished by kind. | supports | Biological assembly1 is an author/software-defined hexadecamer containing sixteen protein entities and sixteen instances. Its Global Symmetry entry lists one of each A–P. Pseudo-symmetry groups homologous subunits and does not change the biological copy number. |
| complex-i-agent-4HEA-entity-1 | https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/1; rcsb_polymer_entity.pdbx_description, rcsb_polymer_entity_container_identifiers.uniprot_ids, rcsb_polymer_entity_align and rcsb_entity_source_organism. Only this entity response is attested. | supports | 4HEA polymer entity1 is NADH-quinone oxidoreductase subunit 1, mapped to UniProtKB:Q56222, with source Thermus thermophilus HB8 (taxon300852). It corresponds to one of the fourteen conserved-core protein examples. |
| complex-i-agent-4HEA-entity-2 | https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/2; rcsb_polymer_entity.pdbx_description, rcsb_polymer_entity_container_identifiers.uniprot_ids, rcsb_polymer_entity_align and rcsb_entity_source_organism. Only this entity response is attested. | supports | 4HEA polymer entity2 is NADH-quinone oxidoreductase subunit 2, mapped to UniProtKB:Q56221, with source Thermus thermophilus HB8 (taxon300852). It corresponds to one of the fourteen conserved-core protein examples. |
| complex-i-agent-4HEA-entity-3 | https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/3; rcsb_polymer_entity.pdbx_description, rcsb_polymer_entity_container_identifiers.uniprot_ids, rcsb_polymer_entity_align and rcsb_entity_source_organism. Only this entity response is attested. | supports | 4HEA polymer entity3 is NADH-quinone oxidoreductase subunit 3, mapped to UniProtKB:Q56223, with source Thermus thermophilus HB8 (taxon300852). It corresponds to one of the fourteen conserved-core protein examples. |
| complex-i-agent-4HEA-entity-4 | https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/4; rcsb_polymer_entity.pdbx_description, rcsb_polymer_entity_container_identifiers.uniprot_ids, rcsb_polymer_entity_align and rcsb_entity_source_organism. Only this entity response is attested. | supports | 4HEA polymer entity4 is NADH-quinone oxidoreductase subunit 4, mapped to UniProtKB:Q56220, with source Thermus thermophilus HB8 (taxon300852). It corresponds to one of the fourteen conserved-core protein examples. |
| complex-i-agent-4HEA-entity-5 | https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/5; rcsb_polymer_entity.pdbx_description, rcsb_polymer_entity_container_identifiers.uniprot_ids, rcsb_polymer_entity_align and rcsb_entity_source_organism. Only this entity response is attested. | supports | 4HEA polymer entity5 is NADH-quinone oxidoreductase subunit 5, mapped to UniProtKB:Q56219, with source Thermus thermophilus HB8 (taxon300852). It corresponds to one of the fourteen conserved-core protein examples. |
| complex-i-agent-4HEA-entity-6 | https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/6; rcsb_polymer_entity.pdbx_description, rcsb_polymer_entity_container_identifiers.uniprot_ids, rcsb_polymer_entity_align and rcsb_entity_source_organism. Only this entity response is attested. | supports | 4HEA polymer entity6 is NADH-quinone oxidoreductase subunit 6, mapped to UniProtKB:Q56218, with source Thermus thermophilus HB8 (taxon300852). It corresponds to one of the fourteen conserved-core protein examples. |
| complex-i-agent-4HEA-entity-7 | https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/7; rcsb_polymer_entity.pdbx_description, rcsb_polymer_entity_container_identifiers.uniprot_ids, rcsb_polymer_entity_align and rcsb_entity_source_organism. Only this entity response is attested. | supports | 4HEA polymer entity7 is NADH-quinone oxidoreductase subunit 9, mapped to UniProtKB:Q56224, with source Thermus thermophilus HB8 (taxon300852). It corresponds to one of the fourteen conserved-core protein examples. |
| complex-i-agent-4HEA-entity-8 | https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/8; rcsb_polymer_entity.pdbx_description, rcsb_polymer_entity_container_identifiers.uniprot_ids, rcsb_polymer_entity_align and rcsb_entity_source_organism. Only this entity response is attested. | supports | 4HEA polymer entity8 is NADH-quinone oxidoreductase subunit 15, mapped to UniProtKB:Q5SKZ7, with source Thermus thermophilus HB8 (taxon300852). This is one of the two additional deposited proteins beyond the record's fourteen conserved-core examples; an exhaustive example inventory is not asserted. |
| complex-i-agent-4HEA-entity-9 | https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/9; rcsb_polymer_entity.pdbx_description, rcsb_polymer_entity_container_identifiers.uniprot_ids, rcsb_polymer_entity_align and rcsb_entity_source_organism. Only this entity response is attested. | supports | 4HEA polymer entity9 is Putative uncharacterized protein TTHA1528, mapped to UniProtKB:Q5SI52, with source Thermus thermophilus HB8 (taxon300852). This is one of the two additional deposited proteins beyond the record's fourteen conserved-core examples; an exhaustive example inventory is not asserted. |
| complex-i-agent-4HEA-entity-10 | https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/10; rcsb_polymer_entity.pdbx_description, rcsb_polymer_entity_container_identifiers.uniprot_ids, rcsb_polymer_entity_align and rcsb_entity_source_organism. Only this entity response is attested. | supports | 4HEA polymer entity10 is NADH-quinone oxidoreductase subunit 7, mapped to UniProtKB:Q56217, with source Thermus thermophilus HB8 (taxon300852). It corresponds to one of the fourteen conserved-core protein examples. |
| complex-i-agent-4HEA-entity-11 | https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/11; rcsb_polymer_entity.pdbx_description, rcsb_polymer_entity_container_identifiers.uniprot_ids, rcsb_polymer_entity_align and rcsb_entity_source_organism. Only this entity response is attested. | supports | 4HEA polymer entity11 is NADH-quinone oxidoreductase subunit 10, mapped to UniProtKB:Q56225, with source Thermus thermophilus HB8 (taxon300852). It corresponds to one of the fourteen conserved-core protein examples. |
| complex-i-agent-4HEA-entity-12 | https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/12; rcsb_polymer_entity.pdbx_description, rcsb_polymer_entity_container_identifiers.uniprot_ids, rcsb_polymer_entity_align and rcsb_entity_source_organism. Only this entity response is attested. | supports | 4HEA polymer entity12 is NADH-quinone oxidoreductase subunit 11, mapped to UniProtKB:Q56226, with source Thermus thermophilus HB8 (taxon300852). It corresponds to one of the fourteen conserved-core protein examples. |
| complex-i-agent-4HEA-entity-13 | https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/13; rcsb_polymer_entity.pdbx_description, rcsb_polymer_entity_container_identifiers.uniprot_ids, rcsb_polymer_entity_align and rcsb_entity_source_organism. Only this entity response is attested. | supports | 4HEA polymer entity13 is NADH-quinone oxidoreductase subunit 12, mapped to UniProtKB:Q56227, with source Thermus thermophilus HB8 (taxon300852). It corresponds to one of the fourteen conserved-core protein examples. |
| complex-i-agent-4HEA-entity-14 | https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/14; rcsb_polymer_entity.pdbx_description, rcsb_polymer_entity_container_identifiers.uniprot_ids, rcsb_polymer_entity_align and rcsb_entity_source_organism. Only this entity response is attested. | supports | 4HEA polymer entity14 is NADH-quinone oxidoreductase subunit 13, mapped to UniProtKB:Q56228, with source Thermus thermophilus HB8 (taxon300852). It corresponds to one of the fourteen conserved-core protein examples. |
| complex-i-agent-4HEA-entity-15 | https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/15; rcsb_polymer_entity.pdbx_description, rcsb_polymer_entity_container_identifiers.uniprot_ids, rcsb_polymer_entity_align and rcsb_entity_source_organism. Only this entity response is attested. | supports | 4HEA polymer entity15 is NADH-quinone oxidoreductase subunit 14, mapped to UniProtKB:Q56229, with source Thermus thermophilus HB8 (taxon300852). It corresponds to one of the fourteen conserved-core protein examples. |
| complex-i-agent-4HEA-entity-16 | https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/16; rcsb_polymer_entity.pdbx_description, rcsb_polymer_entity_container_identifiers.uniprot_ids, rcsb_polymer_entity_align and rcsb_entity_source_organism. Only this entity response is attested. | supports | 4HEA polymer entity16 is NADH-quinone oxidoreductase subunit 8, mapped to UniProtKB:Q60019, with source Thermus thermophilus HB8 (taxon300852). It corresponds to one of the fourteen conserved-core protein examples. |
| complex-i-agent-Q56222 | https://rest.uniprot.org/uniprotkb/Q56222.json; primaryAccession, entryType, proteinDescription.recommendedName, genes, organism, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT/SUBCELLULAR LOCATION/COFACTOR comments where present, and InterPro/Pfam/NCBIfam cross-references. | supports | Reviewed UniProtKB:Q56222 has the recorded name NADH-quinone oxidoreductase subunit1, primary gene nqo1, and HB8 taxon300852. Its SUBUNIT/location annotations support the peripheral assignment. Native annotations use menaquinone as the species' immediate acceptor and describe a fifteen-subunit enzyme, distinct from the sixteen-subunit crystallization preparation. The function/cofactor comments place NADH binding, FMN and cluster N3 in Nqo1. Protein-family cross-references describe particular subunits/domains, not a complete arm. |
| complex-i-agent-Q56221 | https://rest.uniprot.org/uniprotkb/Q56221.json; primaryAccession, entryType, proteinDescription.recommendedName, genes, organism, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT/SUBCELLULAR LOCATION/COFACTOR comments where present, and InterPro/Pfam/NCBIfam cross-references. | supports | Reviewed UniProtKB:Q56221 has the recorded name NADH-quinone oxidoreductase subunit2, primary gene nqo2, and HB8 taxon300852. Its SUBUNIT/location annotations support the peripheral assignment. Native annotations use menaquinone as the species' immediate acceptor and describe a fifteen-subunit enzyme, distinct from the sixteen-subunit crystallization preparation. The cofactor comment identifies cluster N1a. Protein-family cross-references describe particular subunits/domains, not a complete arm. |
| complex-i-agent-Q56223 | https://rest.uniprot.org/uniprotkb/Q56223.json; primaryAccession, entryType, proteinDescription.recommendedName, genes, organism, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT/SUBCELLULAR LOCATION/COFACTOR comments where present, and InterPro/Pfam/NCBIfam cross-references. | supports | Reviewed UniProtKB:Q56223 has the recorded name NADH-quinone oxidoreductase subunit3, primary gene nqo3, and HB8 taxon300852. Its SUBUNIT/location annotations support the peripheral assignment. Native annotations use menaquinone as the species' immediate acceptor and describe a fifteen-subunit enzyme, distinct from the sixteen-subunit crystallization preparation. The cofactor comments distinguish N1b and N5/N4/N7, and describe N7 as distant from the main electron-transfer chain. Protein-family cross-references describe particular subunits/domains, not a complete arm. |
| complex-i-agent-Q56220 | https://rest.uniprot.org/uniprotkb/Q56220.json; primaryAccession, entryType, proteinDescription.recommendedName, genes, organism, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT/SUBCELLULAR LOCATION/COFACTOR comments where present, and InterPro/Pfam/NCBIfam cross-references. | supports | Reviewed UniProtKB:Q56220 has the recorded name NADH-quinone oxidoreductase subunit4, primary gene nqo4, and HB8 taxon300852. Its SUBUNIT/location annotations support the peripheral assignment. Native annotations use menaquinone as the species' immediate acceptor and describe a fifteen-subunit enzyme, distinct from the sixteen-subunit crystallization preparation. Protein-family cross-references describe particular subunits/domains, not a complete arm. |
| complex-i-agent-Q56219 | https://rest.uniprot.org/uniprotkb/Q56219.json; primaryAccession, entryType, proteinDescription.recommendedName, genes, organism, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT/SUBCELLULAR LOCATION/COFACTOR comments where present, and InterPro/Pfam/NCBIfam cross-references. | supports | Reviewed UniProtKB:Q56219 has the recorded name NADH-quinone oxidoreductase subunit5, primary gene nqo5, and HB8 taxon300852. Its SUBUNIT/location annotations support the peripheral assignment. Native annotations use menaquinone as the species' immediate acceptor and describe a fifteen-subunit enzyme, distinct from the sixteen-subunit crystallization preparation. Protein-family cross-references describe particular subunits/domains, not a complete arm. |
| complex-i-agent-Q56218 | https://rest.uniprot.org/uniprotkb/Q56218.json; primaryAccession, entryType, proteinDescription.recommendedName, genes, organism, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT/SUBCELLULAR LOCATION/COFACTOR comments where present, and InterPro/Pfam/NCBIfam cross-references. | supports | Reviewed UniProtKB:Q56218 has the recorded name NADH-quinone oxidoreductase subunit6, primary gene nqo6, and HB8 taxon300852. Its SUBUNIT/location annotations support the peripheral assignment. Native annotations use menaquinone as the species' immediate acceptor and describe a fifteen-subunit enzyme, distinct from the sixteen-subunit crystallization preparation. The cofactor comment identifies terminal cluster N2. Protein-family cross-references describe particular subunits/domains, not a complete arm. |
| complex-i-agent-Q56224 | https://rest.uniprot.org/uniprotkb/Q56224.json; primaryAccession, entryType, proteinDescription.recommendedName, genes, organism, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT/SUBCELLULAR LOCATION/COFACTOR comments where present, and InterPro/Pfam/NCBIfam cross-references. | supports | Reviewed UniProtKB:Q56224 has the recorded name NADH-quinone oxidoreductase subunit9, primary gene nqo9, and HB8 taxon300852. Its SUBUNIT/location annotations support the peripheral assignment. Native annotations use menaquinone as the species' immediate acceptor and describe a fifteen-subunit enzyme, distinct from the sixteen-subunit crystallization preparation. The cofactor comments identify N6a/N6b. Protein-family cross-references describe particular subunits/domains, not a complete arm. |
| complex-i-agent-Q56217 | https://rest.uniprot.org/uniprotkb/Q56217.json; primaryAccession, entryType, proteinDescription.recommendedName, genes, organism, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT/SUBCELLULAR LOCATION/COFACTOR comments where present, and InterPro/Pfam/NCBIfam cross-references. | supports | Reviewed UniProtKB:Q56217 has the recorded name NADH-quinone oxidoreductase subunit7, primary gene nqo7, and HB8 taxon300852. Its SUBUNIT/location annotations support the membrane assignment. Native annotations use menaquinone as the species' immediate acceptor and describe a fifteen-subunit enzyme, distinct from the sixteen-subunit crystallization preparation. Protein-family cross-references describe particular subunits/domains, not a complete arm. |
| complex-i-agent-Q56225 | https://rest.uniprot.org/uniprotkb/Q56225.json; primaryAccession, entryType, proteinDescription.recommendedName, genes, organism, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT/SUBCELLULAR LOCATION/COFACTOR comments where present, and InterPro/Pfam/NCBIfam cross-references. | supports | Reviewed UniProtKB:Q56225 has the recorded name NADH-quinone oxidoreductase subunit10, primary gene nqo10, and HB8 taxon300852. Its SUBUNIT/location annotations support the membrane assignment. Native annotations use menaquinone as the species' immediate acceptor and describe a fifteen-subunit enzyme, distinct from the sixteen-subunit crystallization preparation. Protein-family cross-references describe particular subunits/domains, not a complete arm. |
| complex-i-agent-Q56226 | https://rest.uniprot.org/uniprotkb/Q56226.json; primaryAccession, entryType, proteinDescription.recommendedName, genes, organism, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT/SUBCELLULAR LOCATION/COFACTOR comments where present, and InterPro/Pfam/NCBIfam cross-references. | supports | Reviewed UniProtKB:Q56226 has the recorded name NADH-quinone oxidoreductase subunit11, primary gene nqo11, and HB8 taxon300852. Its SUBUNIT/location annotations support the membrane assignment. Native annotations use menaquinone as the species' immediate acceptor and describe a fifteen-subunit enzyme, distinct from the sixteen-subunit crystallization preparation. Protein-family cross-references describe particular subunits/domains, not a complete arm. |
| complex-i-agent-Q56227 | https://rest.uniprot.org/uniprotkb/Q56227.json; primaryAccession, entryType, proteinDescription.recommendedName, genes, organism, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT/SUBCELLULAR LOCATION/COFACTOR comments where present, and InterPro/Pfam/NCBIfam cross-references. | supports | Reviewed UniProtKB:Q56227 has the recorded name NADH-quinone oxidoreductase subunit12, primary gene nqo12, and HB8 taxon300852. Its SUBUNIT/location annotations support the membrane assignment. Native annotations use menaquinone as the species' immediate acceptor and describe a fifteen-subunit enzyme, distinct from the sixteen-subunit crystallization preparation. Protein-family cross-references describe particular subunits/domains, not a complete arm. |
| complex-i-agent-Q56228 | https://rest.uniprot.org/uniprotkb/Q56228.json; primaryAccession, entryType, proteinDescription.recommendedName, genes, organism, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT/SUBCELLULAR LOCATION/COFACTOR comments where present, and InterPro/Pfam/NCBIfam cross-references. | supports | Reviewed UniProtKB:Q56228 has the recorded name NADH-quinone oxidoreductase subunit13, primary gene nqo13, and HB8 taxon300852. Its SUBUNIT/location annotations support the membrane assignment. Native annotations use menaquinone as the species' immediate acceptor and describe a fifteen-subunit enzyme, distinct from the sixteen-subunit crystallization preparation. Protein-family cross-references describe particular subunits/domains, not a complete arm. |
| complex-i-agent-Q56229 | https://rest.uniprot.org/uniprotkb/Q56229.json; primaryAccession, entryType, proteinDescription.recommendedName, genes, organism, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT/SUBCELLULAR LOCATION/COFACTOR comments where present, and InterPro/Pfam/NCBIfam cross-references. | supports | Reviewed UniProtKB:Q56229 has the recorded name NADH-quinone oxidoreductase subunit14, primary gene nqo14, and HB8 taxon300852. Its SUBUNIT/location annotations support the membrane assignment. Native annotations use menaquinone as the species' immediate acceptor and describe a fifteen-subunit enzyme, distinct from the sixteen-subunit crystallization preparation. Protein-family cross-references describe particular subunits/domains, not a complete arm. |
| complex-i-agent-Q60019 | https://rest.uniprot.org/uniprotkb/Q60019.json; primaryAccession, entryType, proteinDescription.recommendedName, genes, organism, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT/SUBCELLULAR LOCATION/COFACTOR comments where present, and InterPro/Pfam/NCBIfam cross-references. | supports | Reviewed UniProtKB:Q60019 has the recorded name NADH-quinone oxidoreductase subunit8, primary gene nqo8, and HB8 taxon300852. Its SUBUNIT/location annotations support the membrane assignment. Native annotations use menaquinone as the species' immediate acceptor and describe a fifteen-subunit enzyme, distinct from the sixteen-subunit crystallization preparation. Protein-family cross-references describe particular subunits/domains, not a complete arm. |
| complex-i-agent-query-nqo | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene%3Anqo%2A%29%20AND%20%28organism_id%3A300852%29%20AND%20%28reviewed%3Atrue%29; Entire results array: primaryAccession, entryType, genes, organism; native response headers X-Total-Results=15 and no Link continuation captured in metadata. | supports | The complete reviewed UniProt gene:nqo* query in taxon300852 returns fifteen entries: one for each nqo1–nqo15. Each of the target's fourteen declared primary genes maps uniquely to its recorded accession. Nqo15 is an additional result, not a duplicate or replacement for a listed core gene. |
| complex-i-agent-ipr-001750 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001750/; metadata.accession/type=domain/name/description/member_databases; PF00361 integration. | context_only | IPR001750 is a transmembrane domain shared by NuoL/M/N (ND5/4/2), Mrp antiporter subunits and other membrane redox complexes. It is not an exact grounding for the whole complex-I membrane arm. |
| complex-i-agent-ipr-006137 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006137/; metadata.accession/type=domain/name/description/member_databases; PF01058 integration. | context_only | IPR006137 is a Rossmann-fold-type domain found in the complex-I20kDa subunit and hydrogenase-related proteins. It does not identify the complete peripheral electron-transfer arm. |
| schema-result | just validate data/structures/energy_complex/respiratory_chain_complex_i.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/energy_complex/respiratory_chain_complex_i.yaml |
| strict-result | just validate-strict data/structures/energy_complex/respiratory_chain_complex_i.yaml --out /private/tmp/cellstructure-batch14-20261021-g0felisv/respiratory_chain_complex_i-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/energy_complex/respiratory_chain_complex_i.yaml --out /private/tmp/cellstructure-batch14-20261021-g0felisv/respiratory_chain_complex_i-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch14-20261021-g0felisv/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch14-20261021-g0felisv/respiratory_chain_complex_i-strict.tsv |
| target-curies | just check-curies-strict; data/structures/energy_complex/respiratory_chain_complex_i.yaml; exact collect() scope; hash identifies the entire original resolver TSV; original /private/tmp/cellstructure-record-reviews-UhRFh7/repo/reports/curie_check.tsv, not resolver-slice.json | supports | 19 of 21 collected target identifiers returned OK at the unchanged base. Residuals: PDB:4HEA: SKIPPED; resolved by evidence complex-i-agent-pdb-4HEA; PMID:23417064: UNREACHABLE; resolved by evidence complex-i-agent-epmc. Source-native identity checked separately. |
| native-verify | uv run python scripts/uniprot_genes.py --verify --record data/structures/energy_complex/respiratory_chain_complex_i.yaml; Captured focused native gate log; exact command/start/end UTC in matching receipt. | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | uv run python scripts/uniprot_genes.py --causal-graphs --record data/structures/energy_complex/respiratory_chain_complex_i.yaml; Captured focused native gate log; exact command/start/end UTC in matching receipt. | supports | data/structures/energy_complex/respiratory_chain_complex_i.yaml  (GO:0045271)<br>  complex_i_nadh_quinone_proton_coupling	peripheral_arm	COVERED	-&gt;peripheral_electron_transfer_arm (UniProtKB:Q56222, UniProtKB:Q56221, UniProtKB:Q56223, UniProtKB:Q56220, UniProtKB:Q56219, UniProtKB:Q56218, UniProtKB:Q56224)<br>  complex_i_nadh_quinone_proton_coupling	membrane_arm	COVERED	-&gt;membrane_proton_pumping_arm (UniProtKB:Q56217, UniProtKB:Q60019, UniProtKB:Q56225, UniProtKB:Q56226, UniProtKB:Q56227, UniProtKB:Q56228, UniProtKB:Q56229)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     2  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- The ESSENTIAL labels on the two arms concern formation or assembly under the schema. The inspected intact structures and catalytic context do not test arm-removal assembly necessity; this remains unknown in the review and is not established by the two-arm architecture alone.
- The full primary author-manuscript body and main Methods were read, including all main figure captions. Figure pixels, raw diffraction data, electron-density maps and coordinates were not independently reanalyzed.
- The supplementary PDF was recovered from the native Europe PMC ZIP. Supplementary Discussion pages2–10, Table3 page13 and Table4a/b page14 were read. The remaining supplementary tables and image pixels were not independently audited. The earlier main-PDF/CDN404 and PMC HTTP200 download-preparation responses remain preserved as failed access receipts.
- The 2013 long-range conformational mechanism and proton pathways remain proposals inferred from a static structure; modeled waters and analogue-bound preliminary models do not establish observed dynamic proton transfer. The record itself confines the graph to NONMECHANISTIC topology and qualifies the underlying proposal.
- The primary text cites earlier work for general four-proton stoichiometry and some electron-transfer context; this review does not claim that those older experiments were independently read or newly repeated.
- Thermus uses menaquinone-8 in vivo, while the generic GO molecular-function term names ubiquinone and the structure study uses decyl-ubiquinone as an active analogue. Native quinone identity is not generalized across all complex-I examples.
- The fourteen protein examples cover conserved-core identities, not every member of the sixteen-subunit Thermus crystallization preparation. The main text reports that the Nqo16-containing preparation crystallized; Supplementary Discussion page2 attributes Nqo16 activity dispensability to personal communication. No independently read activity assay or universal accessory-subunit essentiality is inferred.
- The peripheral-arm GO search covered all96 hits, while the membrane-arm search screened only the first100 of1643 hits. Exact obsolete arm terms and two domain candidates were inspected. No exhaustive absence assertion is made across GO, Complex Portal, InterPro, Pfam or NCBIfam.
- Native UniProt annotations still describe a fifteen-subunit Thermus enzyme. Their identity and arm-assignment claims are used at their database tier; the sixteen-protein deposited crystallization composition is established separately by the primary paper and PDB.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Native inspect/schema/strict completed before assessment. UniProt guidance was added by native re-inspection, and all thirteen input hashes match unchanged base99692a3d5f16a7dcd6db7e3811344c299a977b81. No neighboring maintained record was required.
- The authorized batch task requests an unsaved draft including clean outcomes. No finding is invented to justify saving; root retains final review and save responsibility.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T091350Z-respiratory-chain-complex-i-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Respiratory complex I arm composition, protein identity and coupling evidence
  review
started_at: '2026-10-21T08:50:35Z'
finished_at: '2026-10-21T09:13:50Z'
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
summary: The exact GO identity, arm-level components, fourteen protein mappings and
  nonmechanistic quinone/proton coupling graph are supported. No concrete curation
  issue was established; native quinone, accessory-subunit and structural-mechanism
  limits remain explicit.
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
  - path: data/structures/energy_complex/respiratory_chain_complex_i.yaml
    sha256: 412f85b2aeb446f9635a89f69cef1dc90c124dbade5bc41f1c5b568461a31e4a
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
- target_id: GO:0045271
  path: data/structures/energy_complex/respiratory_chain_complex_i.yaml
  label: respiratory chain complex I
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/respiratory_chain_complex_i.yaml
    role: maintained scientific record
scope:
  description: Entire single target, all named proteins and stable identifiers, exact
    native PDB entry/assembly/polymer mappings, full main primary article and Methods,
    bounded arm-grounding candidates, and native protein/graph verification.
  selection: Sixth selected target in batch fourteen, following fixed repository path
    order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0045271
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0045271
  command: just validate data/structures/energy_complex/respiratory_chain_complex_i.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0045271
  command: just validate-strict data/structures/energy_complex/respiratory_chain_complex_i.yaml
    --out /private/tmp/cellstructure-batch14-20261021-g0felisv/respiratory_chain_complex_i-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0045271
  summary: 19 identifiers OK; 2 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - complex-i-agent-epmc
  - complex-i-agent-pdb-4HEA
- check_id: native-verify
  name: Native UniProt example verification
  status: passed
  required: true
  target_ids:
  - GO:0045271
  command: uv run python scripts/uniprot_genes.py --verify --record data/structures/energy_complex/respiratory_chain_complex_i.yaml
  exit_code: 0
  summary: All fourteen protein examples verified.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Native graph protein coverage
  status: passed
  required: true
  target_ids:
  - GO:0045271
  command: uv run python scripts/uniprot_genes.py --causal-graphs --record data/structures/energy_complex/respiratory_chain_complex_i.yaml
  exit_code: 0
  summary: Both arm nodes COVERED; all other coverage categories zero.
  evidence_ids:
  - native-causal-graphs
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0045271
  summary: The record makes no expression-module or regulator claim used as structural
    evidence; no iModulon analysis is required.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0045271
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - complex-i-agent-go
  - complex-i-agent-go-arm-candidates
  - complex-i-agent-go-peripheral-search
  - complex-i-agent-go-membrane-arm-search
  - complex-i-agent-tax-274
  - complex-i-agent-tax-300852
  - complex-i-agent-epmc
  - complex-i-agent-baradaran2013-jats
  - complex-i-agent-baradaran2013-supplement-epmc
  - complex-i-agent-pdb-4HEA
  - complex-i-agent-assembly-4HEA
  - complex-i-agent-4HEA-entity-1
  - complex-i-agent-4HEA-entity-2
  - complex-i-agent-4HEA-entity-3
  - complex-i-agent-4HEA-entity-4
  - complex-i-agent-4HEA-entity-5
  - complex-i-agent-4HEA-entity-6
  - complex-i-agent-4HEA-entity-7
  - complex-i-agent-4HEA-entity-8
  - complex-i-agent-4HEA-entity-9
  - complex-i-agent-4HEA-entity-10
  - complex-i-agent-4HEA-entity-11
  - complex-i-agent-4HEA-entity-12
  - complex-i-agent-4HEA-entity-13
  - complex-i-agent-4HEA-entity-14
  - complex-i-agent-4HEA-entity-15
  - complex-i-agent-4HEA-entity-16
  - complex-i-agent-Q56222
  - complex-i-agent-Q56221
  - complex-i-agent-Q56223
  - complex-i-agent-Q56220
  - complex-i-agent-Q56219
  - complex-i-agent-Q56218
  - complex-i-agent-Q56224
  - complex-i-agent-Q56217
  - complex-i-agent-Q56225
  - complex-i-agent-Q56226
  - complex-i-agent-Q56227
  - complex-i-agent-Q56228
  - complex-i-agent-Q56229
  - complex-i-agent-Q60019
  - complex-i-agent-query-nqo
  - complex-i-agent-ipr-001750
  - complex-i-agent-ipr-006137
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0045271
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch14 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0045271
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch14 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0045271
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch14 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0045271
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch14 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0045271
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch14 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/energy_complex/respiratory_chain_complex_i.yaml
  locator: 'Entire maintained YAML: definition, synonym scopes, parent, both arm components
    and fourteen protein examples, taxon example, function, every graph node/edge,
    discussion and history.'
  accessed_at: '2026-10-21T09:03:44Z'
  support: context_only
  summary: The entire record was read. It describes generic respiratory complex I
    using two arm-level components, conserved-core Thermus examples and a nonmechanistic
    coupling graph. Native PROPOSED status and historical notes are unchanged.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Identifiers, components, protein examples, causal graphs, discussions and
    status; review and UniProt guidance in source.inputs.
  accessed_at: '2026-10-21T09:03:44Z'
  support: context_only
  summary: An arm-level protein complex must not be grounded to a single subunit/domain.
    Protein accessions establish the stated identities, with structural membership
    checked separately. Optional omissions and historical first-pass search notes
    do not automatically establish defects.
- evidence_id: complex-i-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0045271%2CGO%3A0098803%2CGO%3A0008137
  locator: 'All three native results: id, isObsolete, name, definition, synonyms,
    comment, aspect and children relation values.'
  accessed_at: '2026-10-21T08:56:13.900828Z'
  support: supports
  summary: Active GO:0045271 exactly identifies respiratory chain complex I and lists
    both recorded synonyms as exact. GO:0098803 explicitly lists GO:0045271 as an
    is_a child. GO:0008137 is the molecular function NADH dehydrogenase (ubiquinone)
    activity, with an NADH/ubiquinone-to-NAD+/ubiquinol reaction coupled to proton
    translocation; its relation to GO:0045271 is capable_of. The CC definition uses
    mitochondrial matrix language, whereas the target appropriately generalizes the
    projecting arm for bacteria.
  snapshot_sha256: f6470e88b26349bf06188cbe20c816cc0853c70629f5a5f81ad750d05f26d134
- evidence_id: complex-i-agent-go-arm-candidates
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0042652%2CGO%3A0042653
  locator: 'Both exact results: id, isObsolete, name, definition, comment and synonym
    scope.'
  accessed_at: '2026-10-21T08:56:55.763009Z'
  support: context_only
  summary: GO:0042652 and GO:0042653 describe the mitochondrial complex-I peripheral
    and membrane segments, respectively, and are both explicitly obsolete. The native
    comments state that these subcomplexes are out of GO scope. Neither is an active
    source-neutral grounding for the record's bacterial/mitochondrial arm-level component.
  snapshot_sha256: eb5f72a796b4605c79ad4d23b242d16fc0f4fe4a1593d721ee43d7e03df78715
- evidence_id: complex-i-agent-go-peripheral-search
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=peripheral%20arm&limit=100
  locator: numberOfHits, pageInfo and result identifiers/names; exact query and page
    in URL.
  accessed_at: '2026-10-21T08:56:14.735741Z'
  support: context_only
  summary: QuickGO candidate search for 'peripheral arm'. All 96 returned hits; one
    complete page. Relevant obsolete arm candidates were then inspected through their
    exact native term records.
  snapshot_sha256: e2ed242fc15aac7fe46b9adcf0677f9c93d3bebb09fb30415daed1ebb80cb42f
  search_scope: Native external QuickGO search 'peripheral arm', limit100. All 96
    returned hits; one complete page. No universal absence statement across GO, Complex
    Portal or protein-family databases is inferred. Local ignored-file inclusion is
    not applicable to this external search.
- evidence_id: complex-i-agent-go-membrane-arm-search
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=membrane%20arm&limit=100
  locator: numberOfHits, pageInfo and result identifiers/names; exact query and page
    in URL.
  accessed_at: '2026-10-21T08:56:14.798524Z'
  support: context_only
  summary: QuickGO candidate search for 'membrane arm'. First 100 of 1643 reported
    hits, page1 of17; intentionally bounded candidate screening, not an exhaustive
    search. Relevant obsolete arm candidates were then inspected through their exact
    native term records.
  snapshot_sha256: 8e299f1f143c36a4c03aa0d039a94a5c392923acba2b8d0810d05e3faa8bebfd
  search_scope: Native external QuickGO search 'membrane arm', limit100. First 100
    of 1643 reported hits, page1 of17; intentionally bounded candidate screening,
    not an exhaustive search. No universal absence statement across GO, Complex Portal
    or protein-family databases is inferred. Local ignored-file inclusion is not applicable
    to this external search.
- evidence_id: complex-i-agent-tax-274
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/274
  locator: taxId, scientificName, rank and otherNames.
  accessed_at: '2026-10-21T08:56:13.902806Z'
  support: supports
  summary: NCBITaxon:274 is Thermus thermophilus at species rank, matching the canonical
    structural example.
  snapshot_sha256: 4a02ca7d31d93e30ddc7b001c685fb75dfcb48c3ac0aa5d4f4d0908098a593c7
- evidence_id: complex-i-agent-tax-300852
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/300852
  locator: taxId, scientificName, rank and otherNames.
  accessed_at: '2026-10-21T08:56:13.896521Z'
  support: supports
  summary: NCBITaxon:300852 is Thermus thermophilus HB8 at strain rank, with Thermus
    thermophilus ATCC27634 as a synonym. It matches all fourteen protein examples
    and the deposited source organism.
  snapshot_sha256: 2fb71cef249a41d237c19ee3d31adbf884d0f2b35e4791cc7d8bd288f3d80c06
- evidence_id: complex-i-agent-epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A23417064%20AND%20SRC%3AMED&format=json&resultType=core
  locator: 'resultList.result[0]: PMID, PMCID, DOI, title, authors, publication details
    and abstractText.'
  accessed_at: '2026-10-21T08:56:13.924072Z'
  support: supports
  summary: The exact Europe PMC result identifies Baradaran et al.2013, Crystal structure
    of the entire respiratory complex I, PMID23417064, PMCIDPMC3672946, DOI10.1038/nature11871.
    Metadata and abstract report a 3.3 A, sixteen-subunit Thermus structure; detailed
    assessment uses the separately retrieved primary body.
  snapshot_sha256: f2ee6060fbc23dca8a5b2612288af4ba41b0d7052d70ae8f79b7fa375eada652
- evidence_id: complex-i-agent-baradaran2013-jats
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3672946/fullTextXML
  locator: 'Native Europe PMC JATS PMC3672946. Complete abstract, introductory P3–P10/FD1,
    main S1–S4 and Methods S6/S7–S11 read; all main Figure1–5 captions read. Key locators:
    S1 composition, S3 native substrate/analogue distinction, S4 proposed coupling
    and final limitation paragraph, S7 purification, S8 crystallization, S9 diffraction
    and S10 refinement. Figure pixels and raw coordinates not reanalyzed.'
  accessed_at: '2026-10-21T08:56:15.289398Z'
  support: supports
  summary: The full primary author manuscript resolves intact T. thermophilus complex
    I with nine hydrophilic and seven membrane subunits, FMN/Fe-S centers and the
    quinone chamber. S1 lists membrane Nqo7/8/10–14 and identifies Nqo16 as crystallization-associated.
    S3 distinguishes native menaquinone-8 from active decyl-ubiquinone and reports
    quinone-analogue binding. S4/Figure5 explicitly propose long-range coupling; the
    main text does not directly observe a catalytic conformational cycle. Methods
    describe separated Nqo16-containing and lacking preparations, detergent purification,
    intact-complex crystallization at23 C, diffraction at100 K, molecular replacement
    and preliminary analogue-bound models. General reaction and stoichiometry context
    cites earlier work.
  snapshot_sha256: 8e4a9762e39f0f334983f805c1d8c699a6e6abf719e7f93690412eddf7f365a2
- evidence_id: complex-i-agent-baradaran2013-supplement-epmc
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3672946/supplementaryFiles
  locator: HTTP200 Europe PMC supplementaryFiles ZIP; member NIHMS50981-supplement-1.pdf
    extracted with SHA256 0fc0c25b63a69c6342d45bc7432b982ac7d4e68047779635da6382313da4e426.
    Read PDF pages2–10 Supplementary Discussion, page13 Table3 and page14 Table4a/b.
    Table3 exactly resolves both seven-protein cohorts. Other supplementary tables,
    figure pixels and references were not independently audited. Evidence hash identifies
    the original ZIP response; extraction provenance is in supplement-extraction.json.
  accessed_at: '2026-10-21T08:59:40.048001Z'
  support: supports
  summary: The recovered primary supplementary PDF explicitly assigns Nqo1–6/9 to
    the hydrophilic domain and Nqo7/8/10–14 to the membrane domain in Table3, matching
    both example cohorts. It identifies Nqo15 and Nqo16 as extra hydrophilic proteins.
    Discussion identifies Nqo16 as TTHA1528 and proposes an assembly/chaperone role;
    its dispensability for oxidoreductase/proton-pumping activity is attributed to
    personal communication, not a displayed assay. The coupling discussion retains
    alternatives and model uncertainty. Table4 interaction estimates are computational
    PISA analysis, not an independent binding experiment.
  snapshot_sha256: 8a464c8e540194ad69fee747e18275401f92de81af96cdc0c4f139e30e3cbc9d
- evidence_id: complex-i-agent-pdb-4HEA
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/entry/4HEA
  locator: struct, exptl, rcsb_entry_container_identifiers, rcsb_entry_info, rcsb_primary_citation
    and diffraction resolution fields.
  accessed_at: '2026-10-21T08:56:13.968236Z'
  support: supports
  summary: PDB4HEA is the entire Thermus thermophilus complex-I X-ray structure linked
    to the exact Baradaran2013 citation. It has sixteen distinct protein polymer entities,
    with two copies in the asymmetric-unit deposition and an overall resolution near3.3
    A. The thirty-two deposited polymer instances are not thirty-two distinct enzyme
    subunits.
  snapshot_sha256: 1cd71f61f6c41d66dd33611cccc924cd814366e5bfd8189221030c069fa8c442
- evidence_id: complex-i-agent-assembly-4HEA
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/assembly/4HEA/1
  locator: pdbx_struct_assembly, rcsb_assembly_info and rcsb_struct_symmetry entries
    distinguished by kind.
  accessed_at: '2026-10-21T08:56:13.993515Z'
  support: supports
  summary: Biological assembly1 is an author/software-defined hexadecamer containing
    sixteen protein entities and sixteen instances. Its Global Symmetry entry lists
    one of each A–P. Pseudo-symmetry groups homologous subunits and does not change
    the biological copy number.
  snapshot_sha256: de39f0c8edd60408ebc712c38cbb5cf86479331c3935ef3415e931416092a96f
- evidence_id: complex-i-agent-4HEA-entity-1
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/1
  locator: rcsb_polymer_entity.pdbx_description, rcsb_polymer_entity_container_identifiers.uniprot_ids,
    rcsb_polymer_entity_align and rcsb_entity_source_organism. Only this entity response
    is attested.
  accessed_at: '2026-10-21T08:56:54.876252Z'
  support: supports
  summary: 4HEA polymer entity1 is NADH-quinone oxidoreductase subunit 1, mapped to
    UniProtKB:Q56222, with source Thermus thermophilus HB8 (taxon300852). It corresponds
    to one of the fourteen conserved-core protein examples.
  snapshot_sha256: c0d3dbff80f1b46de9f7264bed486f838598d7006831419d26121c345a7a74e0
- evidence_id: complex-i-agent-4HEA-entity-2
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/2
  locator: rcsb_polymer_entity.pdbx_description, rcsb_polymer_entity_container_identifiers.uniprot_ids,
    rcsb_polymer_entity_align and rcsb_entity_source_organism. Only this entity response
    is attested.
  accessed_at: '2026-10-21T08:56:54.871399Z'
  support: supports
  summary: 4HEA polymer entity2 is NADH-quinone oxidoreductase subunit 2, mapped to
    UniProtKB:Q56221, with source Thermus thermophilus HB8 (taxon300852). It corresponds
    to one of the fourteen conserved-core protein examples.
  snapshot_sha256: 79a4a75012d932e45862a9d90af011a7d43c402df855e45bffcb2254ee3552fb
- evidence_id: complex-i-agent-4HEA-entity-3
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/3
  locator: rcsb_polymer_entity.pdbx_description, rcsb_polymer_entity_container_identifiers.uniprot_ids,
    rcsb_polymer_entity_align and rcsb_entity_source_organism. Only this entity response
    is attested.
  accessed_at: '2026-10-21T08:56:54.874332Z'
  support: supports
  summary: 4HEA polymer entity3 is NADH-quinone oxidoreductase subunit 3, mapped to
    UniProtKB:Q56223, with source Thermus thermophilus HB8 (taxon300852). It corresponds
    to one of the fourteen conserved-core protein examples.
  snapshot_sha256: 81ed2b59b58f2c493679c6265865655b2c2b595e5fff9f0226fa620a92c44d24
- evidence_id: complex-i-agent-4HEA-entity-4
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/4
  locator: rcsb_polymer_entity.pdbx_description, rcsb_polymer_entity_container_identifiers.uniprot_ids,
    rcsb_polymer_entity_align and rcsb_entity_source_organism. Only this entity response
    is attested.
  accessed_at: '2026-10-21T08:56:54.884028Z'
  support: supports
  summary: 4HEA polymer entity4 is NADH-quinone oxidoreductase subunit 4, mapped to
    UniProtKB:Q56220, with source Thermus thermophilus HB8 (taxon300852). It corresponds
    to one of the fourteen conserved-core protein examples.
  snapshot_sha256: 7707b94ca538b57579ab84341e45bf0ccdb1a6db04c23e6ec55155381f00603e
- evidence_id: complex-i-agent-4HEA-entity-5
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/5
  locator: rcsb_polymer_entity.pdbx_description, rcsb_polymer_entity_container_identifiers.uniprot_ids,
    rcsb_polymer_entity_align and rcsb_entity_source_organism. Only this entity response
    is attested.
  accessed_at: '2026-10-21T08:56:54.985249Z'
  support: supports
  summary: 4HEA polymer entity5 is NADH-quinone oxidoreductase subunit 5, mapped to
    UniProtKB:Q56219, with source Thermus thermophilus HB8 (taxon300852). It corresponds
    to one of the fourteen conserved-core protein examples.
  snapshot_sha256: c6d947e714ac11a9710c5e86b76348842b5fb06c9685f92d26a9692783474080
- evidence_id: complex-i-agent-4HEA-entity-6
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/6
  locator: rcsb_polymer_entity.pdbx_description, rcsb_polymer_entity_container_identifiers.uniprot_ids,
    rcsb_polymer_entity_align and rcsb_entity_source_organism. Only this entity response
    is attested.
  accessed_at: '2026-10-21T08:56:54.973600Z'
  support: supports
  summary: 4HEA polymer entity6 is NADH-quinone oxidoreductase subunit 6, mapped to
    UniProtKB:Q56218, with source Thermus thermophilus HB8 (taxon300852). It corresponds
    to one of the fourteen conserved-core protein examples.
  snapshot_sha256: 0f9b17ea171e4b97bdd8a16ce03e1040d1bca43127d7df3476a10a8bc1a99430
- evidence_id: complex-i-agent-4HEA-entity-7
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/7
  locator: rcsb_polymer_entity.pdbx_description, rcsb_polymer_entity_container_identifiers.uniprot_ids,
    rcsb_polymer_entity_align and rcsb_entity_source_organism. Only this entity response
    is attested.
  accessed_at: '2026-10-21T08:56:55.021214Z'
  support: supports
  summary: 4HEA polymer entity7 is NADH-quinone oxidoreductase subunit 9, mapped to
    UniProtKB:Q56224, with source Thermus thermophilus HB8 (taxon300852). It corresponds
    to one of the fourteen conserved-core protein examples.
  snapshot_sha256: 8a16ae6837fffe4153a899486c34a5c67874f1b41eae4d0c3a90b32eccf18b94
- evidence_id: complex-i-agent-4HEA-entity-8
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/8
  locator: rcsb_polymer_entity.pdbx_description, rcsb_polymer_entity_container_identifiers.uniprot_ids,
    rcsb_polymer_entity_align and rcsb_entity_source_organism. Only this entity response
    is attested.
  accessed_at: '2026-10-21T08:56:55.016259Z'
  support: supports
  summary: 4HEA polymer entity8 is NADH-quinone oxidoreductase subunit 15, mapped
    to UniProtKB:Q5SKZ7, with source Thermus thermophilus HB8 (taxon300852). This
    is one of the two additional deposited proteins beyond the record's fourteen conserved-core
    examples; an exhaustive example inventory is not asserted.
  snapshot_sha256: f9e10ad75cc74a8607738c14ab444b831ba02e438f3ba99dec90f492b27c3791
- evidence_id: complex-i-agent-4HEA-entity-9
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/9
  locator: rcsb_polymer_entity.pdbx_description, rcsb_polymer_entity_container_identifiers.uniprot_ids,
    rcsb_polymer_entity_align and rcsb_entity_source_organism. Only this entity response
    is attested.
  accessed_at: '2026-10-21T08:56:55.063159Z'
  support: supports
  summary: 4HEA polymer entity9 is Putative uncharacterized protein TTHA1528, mapped
    to UniProtKB:Q5SI52, with source Thermus thermophilus HB8 (taxon300852). This
    is one of the two additional deposited proteins beyond the record's fourteen conserved-core
    examples; an exhaustive example inventory is not asserted.
  snapshot_sha256: 7da2a0060e41d40d4052d61d35226dddb4cdbbdecc8ea27563a81be8b9f45f3f
- evidence_id: complex-i-agent-4HEA-entity-10
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/10
  locator: rcsb_polymer_entity.pdbx_description, rcsb_polymer_entity_container_identifiers.uniprot_ids,
    rcsb_polymer_entity_align and rcsb_entity_source_organism. Only this entity response
    is attested.
  accessed_at: '2026-10-21T08:56:55.125162Z'
  support: supports
  summary: 4HEA polymer entity10 is NADH-quinone oxidoreductase subunit 7, mapped
    to UniProtKB:Q56217, with source Thermus thermophilus HB8 (taxon300852). It corresponds
    to one of the fourteen conserved-core protein examples.
  snapshot_sha256: 8c379e840f11ba4db4d079062fd2b7b968b91c9b07839d4775fbdde2c4169de5
- evidence_id: complex-i-agent-4HEA-entity-11
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/11
  locator: rcsb_polymer_entity.pdbx_description, rcsb_polymer_entity_container_identifiers.uniprot_ids,
    rcsb_polymer_entity_align and rcsb_entity_source_organism. Only this entity response
    is attested.
  accessed_at: '2026-10-21T08:56:55.143349Z'
  support: supports
  summary: 4HEA polymer entity11 is NADH-quinone oxidoreductase subunit 10, mapped
    to UniProtKB:Q56225, with source Thermus thermophilus HB8 (taxon300852). It corresponds
    to one of the fourteen conserved-core protein examples.
  snapshot_sha256: d51e00a4369b3c063be13efc3d687449118252b7df5624317e4dc6d05fcf38d7
- evidence_id: complex-i-agent-4HEA-entity-12
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/12
  locator: rcsb_polymer_entity.pdbx_description, rcsb_polymer_entity_container_identifiers.uniprot_ids,
    rcsb_polymer_entity_align and rcsb_entity_source_organism. Only this entity response
    is attested.
  accessed_at: '2026-10-21T08:56:55.162755Z'
  support: supports
  summary: 4HEA polymer entity12 is NADH-quinone oxidoreductase subunit 11, mapped
    to UniProtKB:Q56226, with source Thermus thermophilus HB8 (taxon300852). It corresponds
    to one of the fourteen conserved-core protein examples.
  snapshot_sha256: 271c72397f9139d85d381625f52cb297657c255472c3b3113e33d199ecb378e3
- evidence_id: complex-i-agent-4HEA-entity-13
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/13
  locator: rcsb_polymer_entity.pdbx_description, rcsb_polymer_entity_container_identifiers.uniprot_ids,
    rcsb_polymer_entity_align and rcsb_entity_source_organism. Only this entity response
    is attested.
  accessed_at: '2026-10-21T08:56:55.149324Z'
  support: supports
  summary: 4HEA polymer entity13 is NADH-quinone oxidoreductase subunit 12, mapped
    to UniProtKB:Q56227, with source Thermus thermophilus HB8 (taxon300852). It corresponds
    to one of the fourteen conserved-core protein examples.
  snapshot_sha256: bdd72bc7f463270cf0680685ddfa03e8eef15ee8fa34dbc7c864716042c61c95
- evidence_id: complex-i-agent-4HEA-entity-14
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/14
  locator: rcsb_polymer_entity.pdbx_description, rcsb_polymer_entity_container_identifiers.uniprot_ids,
    rcsb_polymer_entity_align and rcsb_entity_source_organism. Only this entity response
    is attested.
  accessed_at: '2026-10-21T08:56:55.241994Z'
  support: supports
  summary: 4HEA polymer entity14 is NADH-quinone oxidoreductase subunit 13, mapped
    to UniProtKB:Q56228, with source Thermus thermophilus HB8 (taxon300852). It corresponds
    to one of the fourteen conserved-core protein examples.
  snapshot_sha256: ce5d869ed45fd7d64209adb3e19b20fedfb34aaa7b853501e3a5499f677f1fe8
- evidence_id: complex-i-agent-4HEA-entity-15
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/15
  locator: rcsb_polymer_entity.pdbx_description, rcsb_polymer_entity_container_identifiers.uniprot_ids,
    rcsb_polymer_entity_align and rcsb_entity_source_organism. Only this entity response
    is attested.
  accessed_at: '2026-10-21T08:56:55.241184Z'
  support: supports
  summary: 4HEA polymer entity15 is NADH-quinone oxidoreductase subunit 14, mapped
    to UniProtKB:Q56229, with source Thermus thermophilus HB8 (taxon300852). It corresponds
    to one of the fourteen conserved-core protein examples.
  snapshot_sha256: 2df64dfd30e9944461fd5144e1320b6bc866eb934daa96e46b524bbb2a7d13c7
- evidence_id: complex-i-agent-4HEA-entity-16
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/16
  locator: rcsb_polymer_entity.pdbx_description, rcsb_polymer_entity_container_identifiers.uniprot_ids,
    rcsb_polymer_entity_align and rcsb_entity_source_organism. Only this entity response
    is attested.
  accessed_at: '2026-10-21T08:56:55.231548Z'
  support: supports
  summary: 4HEA polymer entity16 is NADH-quinone oxidoreductase subunit 8, mapped
    to UniProtKB:Q60019, with source Thermus thermophilus HB8 (taxon300852). It corresponds
    to one of the fourteen conserved-core protein examples.
  snapshot_sha256: e9407ad52cd498fa9999f837f0fb328d16e9599b623dd513f6e1aa710a0d62a2
- evidence_id: complex-i-agent-Q56222
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q56222.json
  locator: primaryAccession, entryType, proteinDescription.recommendedName, genes,
    organism, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT/SUBCELLULAR LOCATION/COFACTOR comments
    where present, and InterPro/Pfam/NCBIfam cross-references.
  accessed_at: '2026-10-21T08:56:15.254483Z'
  support: supports
  summary: Reviewed UniProtKB:Q56222 has the recorded name NADH-quinone oxidoreductase
    subunit1, primary gene nqo1, and HB8 taxon300852. Its SUBUNIT/location annotations
    support the peripheral assignment. Native annotations use menaquinone as the species'
    immediate acceptor and describe a fifteen-subunit enzyme, distinct from the sixteen-subunit
    crystallization preparation. The function/cofactor comments place NADH binding,
    FMN and cluster N3 in Nqo1. Protein-family cross-references describe particular
    subunits/domains, not a complete arm.
  snapshot_sha256: 65d3f939390c7247952e7090232fceb6bc690ca1cfbb555b393e4eba54cdd018
- evidence_id: complex-i-agent-Q56221
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q56221.json
  locator: primaryAccession, entryType, proteinDescription.recommendedName, genes,
    organism, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT/SUBCELLULAR LOCATION/COFACTOR comments
    where present, and InterPro/Pfam/NCBIfam cross-references.
  accessed_at: '2026-10-21T08:56:15.357598Z'
  support: supports
  summary: Reviewed UniProtKB:Q56221 has the recorded name NADH-quinone oxidoreductase
    subunit2, primary gene nqo2, and HB8 taxon300852. Its SUBUNIT/location annotations
    support the peripheral assignment. Native annotations use menaquinone as the species'
    immediate acceptor and describe a fifteen-subunit enzyme, distinct from the sixteen-subunit
    crystallization preparation. The cofactor comment identifies cluster N1a. Protein-family
    cross-references describe particular subunits/domains, not a complete arm.
  snapshot_sha256: 7bc5943f43a587c683a10d9b7270b73b1f75c3bcb9b2a88fa6317c2feee9c8ea
- evidence_id: complex-i-agent-Q56223
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q56223.json
  locator: primaryAccession, entryType, proteinDescription.recommendedName, genes,
    organism, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT/SUBCELLULAR LOCATION/COFACTOR comments
    where present, and InterPro/Pfam/NCBIfam cross-references.
  accessed_at: '2026-10-21T08:56:15.502944Z'
  support: supports
  summary: Reviewed UniProtKB:Q56223 has the recorded name NADH-quinone oxidoreductase
    subunit3, primary gene nqo3, and HB8 taxon300852. Its SUBUNIT/location annotations
    support the peripheral assignment. Native annotations use menaquinone as the species'
    immediate acceptor and describe a fifteen-subunit enzyme, distinct from the sixteen-subunit
    crystallization preparation. The cofactor comments distinguish N1b and N5/N4/N7,
    and describe N7 as distant from the main electron-transfer chain. Protein-family
    cross-references describe particular subunits/domains, not a complete arm.
  snapshot_sha256: b6afcc94e603a5e6e59330d501cc9b5e551d6a8f75ae99f2a9970de2010ab2ff
- evidence_id: complex-i-agent-Q56220
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q56220.json
  locator: primaryAccession, entryType, proteinDescription.recommendedName, genes,
    organism, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT/SUBCELLULAR LOCATION/COFACTOR comments
    where present, and InterPro/Pfam/NCBIfam cross-references.
  accessed_at: '2026-10-21T08:56:16.288304Z'
  support: supports
  summary: Reviewed UniProtKB:Q56220 has the recorded name NADH-quinone oxidoreductase
    subunit4, primary gene nqo4, and HB8 taxon300852. Its SUBUNIT/location annotations
    support the peripheral assignment. Native annotations use menaquinone as the species'
    immediate acceptor and describe a fifteen-subunit enzyme, distinct from the sixteen-subunit
    crystallization preparation. Protein-family cross-references describe particular
    subunits/domains, not a complete arm.
  snapshot_sha256: fda7ee94d139ceed29ca6536ea2327f507089f8c38e4e57a3e17ee1798852f40
- evidence_id: complex-i-agent-Q56219
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q56219.json
  locator: primaryAccession, entryType, proteinDescription.recommendedName, genes,
    organism, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT/SUBCELLULAR LOCATION/COFACTOR comments
    where present, and InterPro/Pfam/NCBIfam cross-references.
  accessed_at: '2026-10-21T08:56:16.256986Z'
  support: supports
  summary: Reviewed UniProtKB:Q56219 has the recorded name NADH-quinone oxidoreductase
    subunit5, primary gene nqo5, and HB8 taxon300852. Its SUBUNIT/location annotations
    support the peripheral assignment. Native annotations use menaquinone as the species'
    immediate acceptor and describe a fifteen-subunit enzyme, distinct from the sixteen-subunit
    crystallization preparation. Protein-family cross-references describe particular
    subunits/domains, not a complete arm.
  snapshot_sha256: 558f1926ca287faa7c12df80990c104aefec4b6365361b4331f5acd513e308c4
- evidence_id: complex-i-agent-Q56218
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q56218.json
  locator: primaryAccession, entryType, proteinDescription.recommendedName, genes,
    organism, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT/SUBCELLULAR LOCATION/COFACTOR comments
    where present, and InterPro/Pfam/NCBIfam cross-references.
  accessed_at: '2026-10-21T08:56:16.333641Z'
  support: supports
  summary: Reviewed UniProtKB:Q56218 has the recorded name NADH-quinone oxidoreductase
    subunit6, primary gene nqo6, and HB8 taxon300852. Its SUBUNIT/location annotations
    support the peripheral assignment. Native annotations use menaquinone as the species'
    immediate acceptor and describe a fifteen-subunit enzyme, distinct from the sixteen-subunit
    crystallization preparation. The cofactor comment identifies terminal cluster
    N2. Protein-family cross-references describe particular subunits/domains, not
    a complete arm.
  snapshot_sha256: 46722f4c655b655775989329970613c904bd4e858ce9f5fe75966ac9c0799bde
- evidence_id: complex-i-agent-Q56224
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q56224.json
  locator: primaryAccession, entryType, proteinDescription.recommendedName, genes,
    organism, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT/SUBCELLULAR LOCATION/COFACTOR comments
    where present, and InterPro/Pfam/NCBIfam cross-references.
  accessed_at: '2026-10-21T08:56:16.274344Z'
  support: supports
  summary: Reviewed UniProtKB:Q56224 has the recorded name NADH-quinone oxidoreductase
    subunit9, primary gene nqo9, and HB8 taxon300852. Its SUBUNIT/location annotations
    support the peripheral assignment. Native annotations use menaquinone as the species'
    immediate acceptor and describe a fifteen-subunit enzyme, distinct from the sixteen-subunit
    crystallization preparation. The cofactor comments identify N6a/N6b. Protein-family
    cross-references describe particular subunits/domains, not a complete arm.
  snapshot_sha256: 49666b37f32e2ecb3d8d6fe41733347ed38eb8be989dca486f4bc535957838a7
- evidence_id: complex-i-agent-Q56217
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q56217.json
  locator: primaryAccession, entryType, proteinDescription.recommendedName, genes,
    organism, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT/SUBCELLULAR LOCATION/COFACTOR comments
    where present, and InterPro/Pfam/NCBIfam cross-references.
  accessed_at: '2026-10-21T08:56:17.173872Z'
  support: supports
  summary: Reviewed UniProtKB:Q56217 has the recorded name NADH-quinone oxidoreductase
    subunit7, primary gene nqo7, and HB8 taxon300852. Its SUBUNIT/location annotations
    support the membrane assignment. Native annotations use menaquinone as the species'
    immediate acceptor and describe a fifteen-subunit enzyme, distinct from the sixteen-subunit
    crystallization preparation. Protein-family cross-references describe particular
    subunits/domains, not a complete arm.
  snapshot_sha256: 1e95b26ed571fb3b93ae9a02cf1b654a8c1906426aed66c22d0494a2aa9effb6
- evidence_id: complex-i-agent-Q56225
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q56225.json
  locator: primaryAccession, entryType, proteinDescription.recommendedName, genes,
    organism, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT/SUBCELLULAR LOCATION/COFACTOR comments
    where present, and InterPro/Pfam/NCBIfam cross-references.
  accessed_at: '2026-10-21T08:56:18.047610Z'
  support: supports
  summary: Reviewed UniProtKB:Q56225 has the recorded name NADH-quinone oxidoreductase
    subunit10, primary gene nqo10, and HB8 taxon300852. Its SUBUNIT/location annotations
    support the membrane assignment. Native annotations use menaquinone as the species'
    immediate acceptor and describe a fifteen-subunit enzyme, distinct from the sixteen-subunit
    crystallization preparation. Protein-family cross-references describe particular
    subunits/domains, not a complete arm.
  snapshot_sha256: 5c166ed79a5e345a5b5476bf614f2117f07b2c1933c135415689793185c4b621
- evidence_id: complex-i-agent-Q56226
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q56226.json
  locator: primaryAccession, entryType, proteinDescription.recommendedName, genes,
    organism, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT/SUBCELLULAR LOCATION/COFACTOR comments
    where present, and InterPro/Pfam/NCBIfam cross-references.
  accessed_at: '2026-10-21T08:56:17.264083Z'
  support: supports
  summary: Reviewed UniProtKB:Q56226 has the recorded name NADH-quinone oxidoreductase
    subunit11, primary gene nqo11, and HB8 taxon300852. Its SUBUNIT/location annotations
    support the membrane assignment. Native annotations use menaquinone as the species'
    immediate acceptor and describe a fifteen-subunit enzyme, distinct from the sixteen-subunit
    crystallization preparation. Protein-family cross-references describe particular
    subunits/domains, not a complete arm.
  snapshot_sha256: e091cd1aa3a6e985e00e7f48b68c8569965c521df87424d6dba9c2e561c4dd99
- evidence_id: complex-i-agent-Q56227
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q56227.json
  locator: primaryAccession, entryType, proteinDescription.recommendedName, genes,
    organism, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT/SUBCELLULAR LOCATION/COFACTOR comments
    where present, and InterPro/Pfam/NCBIfam cross-references.
  accessed_at: '2026-10-21T08:56:18.083545Z'
  support: supports
  summary: Reviewed UniProtKB:Q56227 has the recorded name NADH-quinone oxidoreductase
    subunit12, primary gene nqo12, and HB8 taxon300852. Its SUBUNIT/location annotations
    support the membrane assignment. Native annotations use menaquinone as the species'
    immediate acceptor and describe a fifteen-subunit enzyme, distinct from the sixteen-subunit
    crystallization preparation. Protein-family cross-references describe particular
    subunits/domains, not a complete arm.
  snapshot_sha256: 9619291210f3795763fdfc70c2b846299f5a368664479325400dc1ae363fcd3e
- evidence_id: complex-i-agent-Q56228
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q56228.json
  locator: primaryAccession, entryType, proteinDescription.recommendedName, genes,
    organism, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT/SUBCELLULAR LOCATION/COFACTOR comments
    where present, and InterPro/Pfam/NCBIfam cross-references.
  accessed_at: '2026-10-21T08:56:18.147450Z'
  support: supports
  summary: Reviewed UniProtKB:Q56228 has the recorded name NADH-quinone oxidoreductase
    subunit13, primary gene nqo13, and HB8 taxon300852. Its SUBUNIT/location annotations
    support the membrane assignment. Native annotations use menaquinone as the species'
    immediate acceptor and describe a fifteen-subunit enzyme, distinct from the sixteen-subunit
    crystallization preparation. Protein-family cross-references describe particular
    subunits/domains, not a complete arm.
  snapshot_sha256: 0a371f8f1ecaed6e9123c7e42e47932234b50159751f98a1886d587528a0bbd5
- evidence_id: complex-i-agent-Q56229
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q56229.json
  locator: primaryAccession, entryType, proteinDescription.recommendedName, genes,
    organism, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT/SUBCELLULAR LOCATION/COFACTOR comments
    where present, and InterPro/Pfam/NCBIfam cross-references.
  accessed_at: '2026-10-21T08:56:18.030204Z'
  support: supports
  summary: Reviewed UniProtKB:Q56229 has the recorded name NADH-quinone oxidoreductase
    subunit14, primary gene nqo14, and HB8 taxon300852. Its SUBUNIT/location annotations
    support the membrane assignment. Native annotations use menaquinone as the species'
    immediate acceptor and describe a fifteen-subunit enzyme, distinct from the sixteen-subunit
    crystallization preparation. Protein-family cross-references describe particular
    subunits/domains, not a complete arm.
  snapshot_sha256: 7bbaeb9eed0029cbfdf9e53c21c2bd20956910320e42caf45ebb2260a9d6be68
- evidence_id: complex-i-agent-Q60019
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q60019.json
  locator: primaryAccession, entryType, proteinDescription.recommendedName, genes,
    organism, FUNCTION/CATALYTIC ACTIVITY/SUBUNIT/SUBCELLULAR LOCATION/COFACTOR comments
    where present, and InterPro/Pfam/NCBIfam cross-references.
  accessed_at: '2026-10-21T08:56:17.065442Z'
  support: supports
  summary: Reviewed UniProtKB:Q60019 has the recorded name NADH-quinone oxidoreductase
    subunit8, primary gene nqo8, and HB8 taxon300852. Its SUBUNIT/location annotations
    support the membrane assignment. Native annotations use menaquinone as the species'
    immediate acceptor and describe a fifteen-subunit enzyme, distinct from the sixteen-subunit
    crystallization preparation. Protein-family cross-references describe particular
    subunits/domains, not a complete arm.
  snapshot_sha256: d2c6eeb6c4cef280a32ab4be2bbee457fbbd771bf9f6e3b1967ce085dfd51764
- evidence_id: complex-i-agent-query-nqo
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene%3Anqo%2A%29%20AND%20%28organism_id%3A300852%29%20AND%20%28reviewed%3Atrue%29
  locator: 'Entire results array: primaryAccession, entryType, genes, organism; native
    response headers X-Total-Results=15 and no Link continuation captured in metadata.'
  accessed_at: '2026-10-21T08:56:19.898719Z'
  support: supports
  summary: 'The complete reviewed UniProt gene:nqo* query in taxon300852 returns fifteen
    entries: one for each nqo1–nqo15. Each of the target''s fourteen declared primary
    genes maps uniquely to its recorded accession. Nqo15 is an additional result,
    not a duplicate or replacement for a listed core gene.'
  snapshot_sha256: 1a49d555d0e684de6a1dee4efd0711b5a3e39b1a8f2c8ce23315ff94b78f4348
- evidence_id: complex-i-agent-ipr-001750
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001750/
  locator: metadata.accession/type=domain/name/description/member_databases; PF00361
    integration.
  accessed_at: '2026-10-21T08:57:38.386769Z'
  support: context_only
  summary: IPR001750 is a transmembrane domain shared by NuoL/M/N (ND5/4/2), Mrp antiporter
    subunits and other membrane redox complexes. It is not an exact grounding for
    the whole complex-I membrane arm.
  snapshot_sha256: 750b245da5231826a6c4423122008e35d4d7460f51fbfa18754cca952021149b
- evidence_id: complex-i-agent-ipr-006137
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006137/
  locator: metadata.accession/type=domain/name/description/member_databases; PF01058
    integration.
  accessed_at: '2026-10-21T08:57:38.711793Z'
  support: context_only
  summary: IPR006137 is a Rossmann-fold-type domain found in the complex-I20kDa subunit
    and hydrogenase-related proteins. It does not identify the complete peripheral
    electron-transfer arm.
  snapshot_sha256: 3b1cb07da540d4be40dd91a3669d8645931474c55adec9684d911276cd4ac9fc
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/energy_complex/respiratory_chain_complex_i.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:50:38Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/energy_complex/respiratory_chain_complex_i.yaml'
  snapshot_sha256: fcca39656bd0822a83acedbfddf04162c5bb1b18eb75c819f2d5220a493033d9
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/energy_complex/respiratory_chain_complex_i.yaml
    --out /private/tmp/cellstructure-batch14-20261021-g0felisv/respiratory_chain_complex_i-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:50:42Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/energy_complex/respiratory_chain_complex_i.yaml\
    \ --out /private/tmp/cellstructure-batch14-20261021-g0felisv/respiratory_chain_complex_i-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch14-20261021-g0felisv/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch14-20261021-g0felisv/respiratory_chain_complex_i-strict.tsv"
  snapshot_sha256: 1d257ec7ab11a8f773ea1b802f9aae19f0b415e232dcc26579d91532690efdad
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/energy_complex/respiratory_chain_complex_i.yaml; exact
    collect() scope; hash identifies the entire original resolver TSV; original /private/tmp/cellstructure-record-reviews-UhRFh7/repo/reports/curie_check.tsv,
    not resolver-slice.json
  accessed_at: '2026-10-21T09:03:45Z'
  support: supports
  summary: '19 of 21 collected target identifiers returned OK at the unchanged base.
    Residuals: PDB:4HEA: SKIPPED; resolved by evidence complex-i-agent-pdb-4HEA; PMID:23417064:
    UNREACHABLE; resolved by evidence complex-i-agent-epmc. Source-native identity
    checked separately.'
  snapshot_sha256: 68d64e4e86437df228658f43be4d47b41054fe882fedf357e660293691a0a061
- evidence_id: native-verify
  kind: validation
  reference: uv run python scripts/uniprot_genes.py --verify --record data/structures/energy_complex/respiratory_chain_complex_i.yaml
  locator: Captured focused native gate log; exact command/start/end UTC in matching
    receipt.
  accessed_at: '2026-10-21T08:56:20.208670Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: uv run python scripts/uniprot_genes.py --causal-graphs --record data/structures/energy_complex/respiratory_chain_complex_i.yaml
  locator: Captured focused native gate log; exact command/start/end UTC in matching
    receipt.
  accessed_at: '2026-10-21T08:56:20.832697Z'
  support: supports
  summary: "data/structures/energy_complex/respiratory_chain_complex_i.yaml  (GO:0045271)\n\
    \  complex_i_nadh_quinone_proton_coupling\tperipheral_arm\tCOVERED\t->peripheral_electron_transfer_arm\
    \ (UniProtKB:Q56222, UniProtKB:Q56221, UniProtKB:Q56223, UniProtKB:Q56220, UniProtKB:Q56219,\
    \ UniProtKB:Q56218, UniProtKB:Q56224)\n  complex_i_nadh_quinone_proton_coupling\t\
    membrane_arm\tCOVERED\t->membrane_proton_pumping_arm (UniProtKB:Q56217, UniProtKB:Q60019,\
    \ UniProtKB:Q56225, UniProtKB:Q56226, UniProtKB:Q56227, UniProtKB:Q56228, UniProtKB:Q56229)\n\
    \ncausal_graphs GENE_OR_PROTEIN node summary:\n     2  COVERED               \
    \    component_ref target holds protein_examples covering all declared symbols\n\
    \     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     2\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 633f42f63c3f46c078be270a8917a0d33c4e99bf9677469acf36fd3061d11a35
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
  topic: Exact complex and synonym identity
  outcome: supported
  target_ids:
  - GO:0045271
  summary: The exact GO cellular-component identity, both exact synonyms, L-shaped
    architecture and multiprotein-complex kind agree with the native term and primary
    structure. The definition intentionally avoids treating the bacterial projecting
    arm as a mitochondrial matrix structure.
  evidence_ids:
  - complex-i-agent-go
  - complex-i-agent-baradaran2013-jats
  - complex-i-agent-pdb-4HEA
  - record
- assessment_id: hierarchy
  area: scope
  topic: Parent and molecular-function relations
  outcome: supported
  target_ids:
  - GO:0045271
  summary: GO:0045271 is explicitly an is_a child of respiratory chain complex GO:0098803.
    GO:0008137 is a molecular function possessed by the complex, not a structural
    parent or biological process. The target uses these relations in the correct places.
  evidence_ids:
  - complex-i-agent-go
  - record
- assessment_id: composition
  area: evidence
  topic: Arm composition and conserved-core examples
  outcome: supported
  target_ids:
  - GO:0045271
  summary: The membrane set nqo7/8/10–14 and peripheral set nqo1–6/9 exactly match
    primary Supplementary Table3. The examples cover fourteen conserved core subunits;
    they do not assert that the Thermus crystallization preparation contains only
    fourteen proteins. The primary text and PDB support sixteen proteins in that preparation,
    including extra hydrophilic constituents. This establishes the intact two-arm
    architecture; it does not establish formation or assembly necessity through arm-removal
    experiments.
  evidence_ids:
  - complex-i-agent-baradaran2013-jats
  - complex-i-agent-baradaran2013-supplement-epmc
  - complex-i-agent-pdb-4HEA
  - complex-i-agent-assembly-4HEA
  - complex-i-agent-query-nqo
  - complex-i-agent-4HEA-entity-1
  - complex-i-agent-4HEA-entity-2
  - complex-i-agent-4HEA-entity-3
  - complex-i-agent-4HEA-entity-4
  - complex-i-agent-4HEA-entity-5
  - complex-i-agent-4HEA-entity-6
  - complex-i-agent-4HEA-entity-7
  - complex-i-agent-4HEA-entity-8
  - complex-i-agent-4HEA-entity-9
  - complex-i-agent-4HEA-entity-10
  - complex-i-agent-4HEA-entity-11
  - complex-i-agent-4HEA-entity-12
  - complex-i-agent-4HEA-entity-13
  - complex-i-agent-4HEA-entity-14
  - complex-i-agent-4HEA-entity-15
  - complex-i-agent-4HEA-entity-16
  - complex-i-agent-Q56222
  - complex-i-agent-Q56221
  - complex-i-agent-Q56223
  - complex-i-agent-Q56220
  - complex-i-agent-Q56219
  - complex-i-agent-Q56218
  - complex-i-agent-Q56224
  - complex-i-agent-Q56217
  - complex-i-agent-Q56225
  - complex-i-agent-Q56226
  - complex-i-agent-Q56227
  - complex-i-agent-Q56228
  - complex-i-agent-Q56229
  - complex-i-agent-Q60019
  - record
- assessment_id: essentiality
  area: scope
  topic: Architecture versus formation and assembly necessity
  outcome: unknown
  target_ids:
  - GO:0045271
  summary: The schema defines ESSENTIAL in terms of formation or assembly. Intact-complex
    structures and functional arm assignments establish presence and architecture,
    but the inspected sources do not test whether a structure can form after removing
    an entire arm. Assembly necessity remains unverified here and is not inferred
    from catalytic coupling, intact structural presence or cell viability.
  evidence_ids:
  - complex-i-agent-baradaran2013-jats
  - complex-i-agent-baradaran2013-supplement-epmc
  - record
  - policy
- assessment_id: grounding
  area: grounding
  topic: Whole-arm scope versus subunit/domain candidates
  outcome: supported
  target_ids:
  - GO:0045271
  summary: Retaining REVIEWED_LABEL_ONLY for each whole arm is justified. The tempting
    mitochondrial segment GO terms are obsolete, and inspected InterPro candidates
    describe domains shared with other proteins rather than complete arms. Existing
    Nuo/Nqo family cross-references can inform finer future rows but do not automatically
    replace these component identities. Historical first-pass verification wording
    is preserved; no exhaustive cross-database absence claim is made.
  evidence_ids:
  - complex-i-agent-go-arm-candidates
  - complex-i-agent-ipr-001750
  - complex-i-agent-ipr-006137
  - complex-i-agent-go-peripheral-search
  - complex-i-agent-go-membrane-arm-search
  - complex-i-agent-Q56222
  - complex-i-agent-Q56221
  - complex-i-agent-Q56223
  - complex-i-agent-Q56220
  - complex-i-agent-Q56219
  - complex-i-agent-Q56218
  - complex-i-agent-Q56224
  - complex-i-agent-Q56217
  - complex-i-agent-Q56225
  - complex-i-agent-Q56226
  - complex-i-agent-Q56227
  - complex-i-agent-Q56228
  - complex-i-agent-Q56229
  - complex-i-agent-Q60019
  - record
  - policy
- assessment_id: proteins
  area: grounding
  topic: All fourteen taxon-paired examples
  outcome: supported
  target_ids:
  - GO:0045271
  summary: Each accession, primary gene, recommended name, reviewed status and taxon300852
    pair matches native UniProt and the corresponding deposited polymer mapping. All
    declared symbols are covered exactly once in their component cohorts. The identity-only
    evidence notes correctly distinguish accessions from membership proof.
  evidence_ids:
  - complex-i-agent-tax-300852
  - complex-i-agent-query-nqo
  - complex-i-agent-Q56222
  - complex-i-agent-Q56221
  - complex-i-agent-Q56223
  - complex-i-agent-Q56220
  - complex-i-agent-Q56219
  - complex-i-agent-Q56218
  - complex-i-agent-Q56224
  - complex-i-agent-Q56217
  - complex-i-agent-Q56225
  - complex-i-agent-Q56226
  - complex-i-agent-Q56227
  - complex-i-agent-Q56228
  - complex-i-agent-Q56229
  - complex-i-agent-Q60019
  - complex-i-agent-4HEA-entity-1
  - complex-i-agent-4HEA-entity-2
  - complex-i-agent-4HEA-entity-3
  - complex-i-agent-4HEA-entity-4
  - complex-i-agent-4HEA-entity-5
  - complex-i-agent-4HEA-entity-6
  - complex-i-agent-4HEA-entity-7
  - complex-i-agent-4HEA-entity-8
  - complex-i-agent-4HEA-entity-9
  - complex-i-agent-4HEA-entity-10
  - complex-i-agent-4HEA-entity-11
  - complex-i-agent-4HEA-entity-12
  - complex-i-agent-4HEA-entity-13
  - complex-i-agent-4HEA-entity-14
  - complex-i-agent-4HEA-entity-15
  - complex-i-agent-4HEA-entity-16
  - record
- assessment_id: taxonomy
  area: scope
  topic: Species example and HB8 preparation
  outcome: supported
  target_ids:
  - GO:0045271
  summary: Thermus thermophilus species274 is the correct canonical example, while
    protein and PDB source entries specify HB8 taxon300852. The generic record does
    not project the Thermus sixteen-subunit inventory onto every bacterial or mitochondrial
    complex I. Crystallization temperatures and diffraction conditions are experimental
    preparation parameters, not organismal growth or physiological operating temperatures.
  evidence_ids:
  - complex-i-agent-tax-274
  - complex-i-agent-tax-300852
  - complex-i-agent-baradaran2013-jats
  - complex-i-agent-pdb-4HEA
  - complex-i-agent-4HEA-entity-1
  - complex-i-agent-4HEA-entity-2
  - complex-i-agent-4HEA-entity-3
  - complex-i-agent-4HEA-entity-4
  - complex-i-agent-4HEA-entity-5
  - complex-i-agent-4HEA-entity-6
  - complex-i-agent-4HEA-entity-7
  - complex-i-agent-4HEA-entity-8
  - complex-i-agent-4HEA-entity-9
  - complex-i-agent-4HEA-entity-10
  - complex-i-agent-4HEA-entity-11
  - complex-i-agent-4HEA-entity-12
  - complex-i-agent-4HEA-entity-13
  - complex-i-agent-4HEA-entity-14
  - complex-i-agent-4HEA-entity-15
  - complex-i-agent-4HEA-entity-16
  - record
- assessment_id: reaction
  area: evidence
  topic: Generic quinone coupling and native acceptor
  outcome: supported
  target_ids:
  - GO:0045271
  summary: The generic complex-I molecular function and quinone-reduction/proton-translocation
    description agree with GO and the paper. The Thermus enzyme uses menaquinone-8
    in vivo; the primary study explicitly reports activity with decyl-ubiquinone and
    structural analogue binding. The record's generic GO activity name does not assert
    that native Thermus uses ubiquinone exclusively. The graph's quinone-pool label
    remains appropriately broad.
  evidence_ids:
  - complex-i-agent-go
  - complex-i-agent-baradaran2013-jats
  - complex-i-agent-query-nqo
  - complex-i-agent-Q56222
  - complex-i-agent-Q56221
  - complex-i-agent-Q56223
  - complex-i-agent-Q56220
  - complex-i-agent-Q56219
  - complex-i-agent-Q56218
  - complex-i-agent-Q56224
  - complex-i-agent-Q56217
  - complex-i-agent-Q56225
  - complex-i-agent-Q56226
  - complex-i-agent-Q56227
  - complex-i-agent-Q56228
  - complex-i-agent-Q56229
  - complex-i-agent-Q60019
  - record
- assessment_id: graph
  area: graph
  topic: Nonmechanistic topology and mechanistic proposal
  outcome: supported
  target_ids:
  - GO:0045271
  summary: All six nodes and five edges were read. NADH input enters the peripheral
    arm, electrons reach the quinone site, and intact-enzyme quinone reduction couples
    to the membrane arm and PMF contribution. Both protein nodes resolve to their
    component examples. The graph is explicitly NONMECHANISTIC and its coupling-edge
    evidence notes say proposed; no free-quinone causal driver, observed conformational
    sequence or direct four-proton assay is claimed.
  evidence_ids:
  - complex-i-agent-go
  - complex-i-agent-baradaran2013-jats
  - complex-i-agent-pdb-4HEA
  - complex-i-agent-Q56222
  - complex-i-agent-Q56221
  - complex-i-agent-Q56223
  - complex-i-agent-Q56220
  - complex-i-agent-Q56219
  - complex-i-agent-Q56218
  - complex-i-agent-Q56224
  - complex-i-agent-Q56217
  - complex-i-agent-Q56225
  - complex-i-agent-Q56226
  - complex-i-agent-Q56227
  - complex-i-agent-Q56228
  - complex-i-agent-Q56229
  - complex-i-agent-Q60019
  - record
- assessment_id: methods
  area: scope
  topic: Direct structural evidence versus inferred dynamics
  outcome: supported
  target_ids:
  - GO:0045271
  summary: The 2013 evidence directly resolves architecture, redox-center arrangement
    and analogue-binding density. Its long-range conformational coupling and proton-channel
    paths are structural proposals, with modeled waters and further redox-state/time-resolved
    studies explicitly required. Analogue-bound models are called preliminary in Methods
    S10. Introductory reaction stoichiometry summarizes earlier experiments; it is
    not a new stoichiometric measurement in this crystallographic study. Nqo16 activity
    dispensability is attributed to personal communication in Supplementary Discussion
    page2, not a displayed primary assay.
  evidence_ids:
  - complex-i-agent-baradaran2013-jats
  - complex-i-agent-baradaran2013-supplement-epmc
  - record
- assessment_id: provenance
  area: provenance
  topic: Readable source and native authority tiers
  outcome: supported
  target_ids:
  - GO:0045271
  summary: The primary author-manuscript JATS was read across all main claim-bearing
    text and Methods, and the supplementary PDF was read at its specified discussion/table
    passages. Native GO supplies term semantics; taxonomy/UniProt/PDB supply identity
    and deposited composition. All snapshots retain exact raw hashes, actual statuses/content
    types and original UTCZ access times. Failed HTTP200 download-preparation HTML
    is distinct from the successful Europe PMC ZIP and its separately hashed extracted
    PDF.
  evidence_ids:
  - complex-i-agent-go
  - complex-i-agent-baradaran2013-jats
  - complex-i-agent-baradaran2013-supplement-epmc
  - complex-i-agent-epmc
  - complex-i-agent-pdb-4HEA
  - complex-i-agent-assembly-4HEA
  - complex-i-agent-query-nqo
  - complex-i-agent-tax-274
  - complex-i-agent-tax-300852
  - complex-i-agent-Q56222
  - complex-i-agent-Q56221
  - complex-i-agent-Q56223
  - complex-i-agent-Q56220
  - complex-i-agent-Q56219
  - complex-i-agent-Q56218
  - complex-i-agent-Q56224
  - complex-i-agent-Q56217
  - complex-i-agent-Q56225
  - complex-i-agent-Q56226
  - complex-i-agent-Q56227
  - complex-i-agent-Q56228
  - complex-i-agent-Q56229
  - complex-i-agent-Q60019
  - complex-i-agent-4HEA-entity-1
  - complex-i-agent-4HEA-entity-2
  - complex-i-agent-4HEA-entity-3
  - complex-i-agent-4HEA-entity-4
  - complex-i-agent-4HEA-entity-5
  - complex-i-agent-4HEA-entity-6
  - complex-i-agent-4HEA-entity-7
  - complex-i-agent-4HEA-entity-8
  - complex-i-agent-4HEA-entity-9
  - complex-i-agent-4HEA-entity-10
  - complex-i-agent-4HEA-entity-11
  - complex-i-agent-4HEA-entity-12
  - complex-i-agent-4HEA-entity-13
  - complex-i-agent-4HEA-entity-14
  - complex-i-agent-4HEA-entity-15
  - complex-i-agent-4HEA-entity-16
- assessment_id: completeness
  area: completeness
  topic: Bounded inventory and open grounding discussion
  outcome: supported
  target_ids:
  - GO:0045271
  summary: The record supports the two-arm abstraction, conserved-core examples and
    broad functional topology. A complete list of Thermus accessory proteins, all
    family-level rows, images, physical properties or each redox cofactor is not mandatory.
    The existing finer-grounding discussion is a reasonable unresolved curation task.
    No concrete identity, protein-mapping, relation or evidence-placement defect was
    established.
  evidence_ids:
  - complex-i-agent-baradaran2013-jats
  - complex-i-agent-pdb-4HEA
  - complex-i-agent-assembly-4HEA
  - complex-i-agent-go-arm-candidates
  - complex-i-agent-ipr-001750
  - complex-i-agent-ipr-006137
  - record
  - policy
findings: []
actions: []
limitations:
- The ESSENTIAL labels on the two arms concern formation or assembly under the schema.
  The inspected intact structures and catalytic context do not test arm-removal assembly
  necessity; this remains unknown in the review and is not established by the two-arm
  architecture alone.
- The full primary author-manuscript body and main Methods were read, including all
  main figure captions. Figure pixels, raw diffraction data, electron-density maps
  and coordinates were not independently reanalyzed.
- The supplementary PDF was recovered from the native Europe PMC ZIP. Supplementary
  Discussion pages2–10, Table3 page13 and Table4a/b page14 were read. The remaining
  supplementary tables and image pixels were not independently audited. The earlier
  main-PDF/CDN404 and PMC HTTP200 download-preparation responses remain preserved
  as failed access receipts.
- The 2013 long-range conformational mechanism and proton pathways remain proposals
  inferred from a static structure; modeled waters and analogue-bound preliminary
  models do not establish observed dynamic proton transfer. The record itself confines
  the graph to NONMECHANISTIC topology and qualifies the underlying proposal.
- The primary text cites earlier work for general four-proton stoichiometry and some
  electron-transfer context; this review does not claim that those older experiments
  were independently read or newly repeated.
- Thermus uses menaquinone-8 in vivo, while the generic GO molecular-function term
  names ubiquinone and the structure study uses decyl-ubiquinone as an active analogue.
  Native quinone identity is not generalized across all complex-I examples.
- The fourteen protein examples cover conserved-core identities, not every member
  of the sixteen-subunit Thermus crystallization preparation. The main text reports
  that the Nqo16-containing preparation crystallized; Supplementary Discussion page2
  attributes Nqo16 activity dispensability to personal communication. No independently
  read activity assay or universal accessory-subunit essentiality is inferred.
- The peripheral-arm GO search covered all96 hits, while the membrane-arm search screened
  only the first100 of1643 hits. Exact obsolete arm terms and two domain candidates
  were inspected. No exhaustive absence assertion is made across GO, Complex Portal,
  InterPro, Pfam or NCBIfam.
- Native UniProt annotations still describe a fifteen-subunit Thermus enzyme. Their
  identity and arm-assignment claims are used at their database tier; the sixteen-protein
  deposited crystallization composition is established separately by the primary paper
  and PDB.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- Native inspect/schema/strict completed before assessment. UniProt guidance was added
  by native re-inspection, and all thirteen input hashes match unchanged base99692a3d5f16a7dcd6db7e3811344c299a977b81.
  No neighboring maintained record was required.
- The authorized batch task requests an unsaved draft including clean outcomes. No
  finding is invented to justify saving; root retains final review and save responsibility.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
