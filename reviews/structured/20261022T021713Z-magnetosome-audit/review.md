# Magnetosome identity, composition and source-scope review

- Review: 20261022T021713Z-magnetosome-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T01:50:53Z
- Finished UTC: 2026-10-22T02:17:13Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Two major findings concern universal magnetite necessity and neutral-atom transport grounding; two minor findings update a stale current localization-gap interpretation and the MamJ-deletion phenotype wording. The supported organelle identity, protein examples and chain biology remain intact.

## Scope And Provenance

Entire single target, exact identities, hierarchy/boundaries, composition, formation necessity, native protein evidence, taxonomic and experimental scope, function, all graph claims and discussions.

Selection: Target 8 of batch31 in strict uncovered path order; frozen native inspection/schema/strict completed before scientific assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0110143 | data/structures/membrane_organelle/magnetosome.yaml | maintained | magnetosome |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0110143 | Focused validator passed. |
| Focused native strict | passed | True | GO:0110143 | Focused validator passed. |
| Focused native verify | passed | True | GO:0110143 | Native read-only check passed; reporting coverage classes is not itself a scientific finding. |
| Focused native causal-graphs | passed | True | GO:0110143 | Native read-only check passed; reporting coverage classes is not itself a scientific finding. |
| Expression-module applicability | not_applicable | False | GO:0110143 | No regulatory expression-module assertion is used. |
| Claim-level scientific review | passed | True | GO:0110143 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0110143 | 24 of 33 collected target identifiers returned OK. PMID:11571158: UNREACHABLE; The bulk transport returned414; the independently retrieved exact MED identity confirms PMID11571158, DOI10.1128/aem.67.10.4573-4582.2001 and A large gene cluster encoding several magnetosome proteins is conserved in different species of magnetotactic bacteria. Scientific scope remains limited to the separately documented inspections.; PMID:14766587: UNREACHABLE; The bulk transport returned414; the independently retrieved exact MED identity confirms PMID14766587, DOI10.1128/aem.70.2.1040-1050.2004 and Biochemical and proteomic analysis of the magnetosome membrane in Magnetospirillum gryphiswaldense. Scientific scope remains limited to the separately documented inspections.; PMID:17601786: UNREACHABLE; The bulk transport returned414; the independently retrieved exact MED identity confirms PMID17601786, DOI10.1128/jb.00421-07 and The acidic repetitive domain of the Magnetospirillum gryphiswaldense MamJ protein displays hypervariability but is not required for magnetosome chain assembly. Scientific scope remains limited to the separately documented inspections.; PMID:20212111: UNREACHABLE; The bulk transport returned414; the independently retrieved exact MED identity confirms PMID20212111, DOI10.1073/pnas.0914439107 and Comprehensive genetic dissection of the magnetosome gene island reveals the step-wise assembly of a prokaryotic organelle. Scientific scope remains limited to the separately documented inspections.; PMID:20487281: UNREACHABLE; The bulk transport returned414; the independently retrieved exact MED identity confirms PMID20487281, DOI10.1111/j.1365-2958.2010.07202.x and Loss of the actin-like protein MamK has pleiotropic effects on magnetosome formation and chain assembly in Magnetospirillum gryphiswaldense. Scientific scope remains limited to the separately documented inspections.; PMID:22007638: UNREACHABLE; The bulk transport returned414; the independently retrieved exact MED identity confirms PMID22007638, DOI10.1111/j.1365-2958.2011.07863.x and The cation diffusion facilitator proteins MamB and MamM of Magnetospirillum gryphiswaldense have distinct and complex functions, and are involved in magnetite biomineralization and magnetosome membrane assembly. Scientific scope remains limited to the separately documented inspections.; PMID:27481925: UNREACHABLE; The bulk transport returned414; the independently retrieved exact MED identity confirms PMID27481925, DOI10.1128/jb.00280-16 and Comparative Subcellular Localization Analysis of Magnetosome Proteins Reveals a Unique Localization Behavior of Mms6 Protein onto Magnetite Crystals. Scientific scope remains limited to the separately documented inspections.; cellstructuremech:mamk_filament: SKIPPED; The repository-minted identifier uniquely resolves to the frozen maintained MamK filament record at data/structures/cytoskeleton/mamk_filament.yaml. An anchored hidden/ignored-inclusive corpus search and exact input hash confirm reference identity, not all biological assertions.; traitmech:000071: SKIPPED; The exact native TraitMech index row resolves traitmech:000071 to magnetosome, morphology category. This verifies identifier/label linkage, not the mechanistic meaning of a trait. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0110143 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0110143 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0110143 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0110143 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0110143 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact organelle, lumen and membrane boundaries

identity: supported. Targets: GO:0110143.

The target matches the active GO and UniProt location identities. Native hierarchy and parthood distinguish the membrane-enclosed organelle, surrounding bilayer and enclosed volume. The whole record’s MICRO cross-reference is identity-level context where applicable.

### Native taxonomy and experimental conditions

scope: supported. Targets: GO:0110143.

Taxon identities and model strains are correct, including the current Paramagnetospirillum name for AMB-1 where present. Source experiments are assigned to MSR-1 or AMB-1, not exported as identical gene requirements across all bacteria. RARE/VARIABLE are broad qualitative occurrence statements, not a quantitative survey. The whole-record Archaea absence assertion is assessed separately as unknown.

### Material, mineral alternatives and protein cohort

grounding: concern. Targets: GO:0110143.

The membrane material, Mam/Mms cohort and separate MamK/MamJ associated machinery have source support. No single family is forced onto the multifamily cohort. The membrane row is interpreted as generic boundary material without an asserted chemical CURIE; it would benefit from explicit material wording, but no unsupported whole-GO molecular grounding is present. Magnetite and greigite are distinct alternatives, making the universal magnetite essentiality assertion a concrete concern in F1.

### Grouped necessity versus individual requirements

grounding: unknown. Targets: GO:0110143.

Murat and Uebe distinguish membrane-formation defects from biomineralization defects, with redundancy and strain dependence. A collective Mam/Mms ESSENTIAL row is not expanded into a claim that every listed member is independently necessary. Exact formation necessity for the complete taxon-agnostic cohort remains unresolved; no new per-protein necessity finding is inferred from dispensable members. A bilayer is constitutive of the named membrane-bounded class.

### Nine accessions, family and localization evidence

grounding: concern. Targets: GO:0110143.

All nine reviewed example identities, gene/taxon pairs and native evidence annotations match. MamJ family IPR060787 matches both examples. Direct biochemical localization, fluorescence localization and two-hybrid interaction are not conflated. The current six Mam/Mms examples each retain experimental localization annotations, contrary to the still-open present-tense localization-gap discussion addressed in F3.

### Chain function and transported chemical identity

graph: concern. Targets: GO:0110143.

The graph provides a source-backed overview of invagination, mineralization and chain-dependent magnetic alignment, rather than exact kinetics or a reconstituted pathway. MamK phenotypes differ between MSR-1 and AMB-1; the broad scatter shorthand is not a claim that every mutant particle is isolated. MamJ linkage is supported with the stated interaction-model limits; F4 separately qualifies the graph note describing the deletion phenotype. The exact neutral iron atom actor in its transport/mineralization edges is inconsistent with the source-described ion substrate, as bounded in F2.

### Unverified literature-absence attribution

scope: unknown. Targets: GO:0110143.

ENA verifies Archaea identity but cannot establish the biological absence statement. The readable Uebe2016 Key Points/Abstract do not independently establish that no magnetotactic archaeon has been described, and no exhaustive contemporary search was performed. This assertion remains unverified rather than confirmed or refuted.

### Trait linkage and size range access limit

scope: unknown. Targets: GO:0110143.

TraitMech000071 resolves to magnetosome and the chain’s orientation role is supported. UO0000018 resolves to nanometer. The exact35–120nm DIAMETER statement was not verified against the unread Uebe main body; the inspected independent review gives an approximate30–120nm crystal-size range. This remains an access/measurement-convention limitation, not proof the record’s range is false.

### Complete target with bounded optional enrichments

completeness: supported. Targets: GO:0110143.

Every target field, source placement, history and discussion was inspected. No tracked image asset or verbatim snippet is asserted. Generic membrane lipid chemistry, optional inventories and historical image/TODO searches are not automatic defects. Local boundary records and the MamK record where applicable are frozen context only.

## Findings

### F1: Qualify magnetite necessity for alternative-mineral magnetosomes

major / open / confirmed; issue key: magnetosome-magnetite-universal-necessity.

The component specifically denotes magnetite CHEBI46726 and is ESSENTIAL, but both the target definition/role and the inspected review explicitly allow greigite instead. Essentiality means the structure cannot form without that component; a magnetite-only requirement therefore excludes an acknowledged valid mineral alternative. This does not concern merely incomplete vesicle precursors or individual Mam-protein necessity.

### F2: Use an ion-compatible identity for transported iron

major / open / confirmed; issue key: magnetosome-neutral-iron-transport-actor.

The CHEMICAL node is explicitly labelled iron atom and grounded to CHEBI18248, whose native charge annotation is0. It is the object of transporter action and source of mineralization, while the inspected review and primary context describe iron/metal-ion transport. A neutral atom identity is not a charge-unspecified iron-ion substrate. The finding does not prescribe a single oxidation state or prove a detailed MamB/MamM transport mechanism.

### F3: Update the open localization-gap interpretation

minor / open / confirmed; issue key: magnetosome-localization-gap-current-example-conflict.

The open discussion currently says most magnetosome proteins have no experimental UniProt localization support and that only MamJ produced an example. The same maintained target now contains six Mam/Mms examples with the source-specific ECO0000269 localization annotations verified in current native records and supported by the inspected primary studies. The old SL0510 query may have been accurate at its recorded scope; the error is leaving its broad present-tense interpretation as an unresolved current gap.

### F4: Distinguish MamJ-deficient clustering from scattering

minor / open / confirmed; issue key: magnetosome-mamj-deletion-phenotype-wording.

The evidence note on the MamK-aligns-chain edge says mamJ deletion scatters magnetosomes. The inspected MSR-1 primary experiment reports predominantly aggregated clusters, occasional rings or imperfect short chains, and altered particle segregation. Its supported conclusion is loss of normal linear organization, not a uniform dispersed-particle phenotype. This does not refute MamJ-dependent attachment or the graph alignment edge.

## Recommended Actions And Acceptance Checks

### A1

In separately authorized curation, condition magnetite necessity on magnetite-producing lineages or represent the supported magnetic-mineral alternatives without asserting universal magnetite dependence. Preserve exact chemical identities and avoid claiming greigite is a subtype of magnetite.

- Retain source-specific organism, condition and chemical identity boundaries.
- Confirm the amended assertion matches the frozen essentiality/grounding contracts.
- Run focused native schema, strict and graph checks after separately authorized scientific curation.

### A2

In separately authorized curation, identify the transported iron at the ionic scope actually supported by the source, using verified appropriate chemistry grounding or a bounded label if oxidation-state specificity remains unresolved. Keep the downstream mineral identity distinct.

- Retain source-specific organism, condition and chemical identity boundaries.
- Confirm the amended assertion matches the frozen essentiality/grounding contracts.
- Run focused native schema, strict and graph checks after separately authorized scientific curation.

### A3

In separately authorized curation, preserve the historical query result but update or resolve the present-tense discussion to distinguish whole-magnetosome SL0510 from membrane SL0512 annotations and the current experimentally supported examples.

- Retain source-specific organism, condition and chemical identity boundaries.
- Confirm the amended assertion matches the frozen essentiality/grounding contracts.
- Run focused native schema, strict and graph checks after separately authorized scientific curation.

### A4

In separately authorized curation, describe the loss of normal linear organization and the source-specific MSR-1 clustering phenotype, and preserve distinctions from MamK mutants and AMB-1 genetic redundancy.

- Retain source-specific organism, condition and chemical identity boundaries.
- Confirm the amended assertion matches the frozen essentiality/grounding contracts.
- Run focused native schema, strict and graph checks after separately authorized scientific curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/magnetosome.yaml; Entire maintained target including history, discussions, evidence and every graph node/edge | context_only | The entire single target was read; its maintained scientific bytes remain unchanged. |
| policy | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent; molecular grounding; essentiality; EssentialityEnum; CausalNode.component_ref | context_only | Essentiality states whether the structure forms without a component. Molecular species, material constituents, complete membranes and enclosed volumes remain distinct. |
| graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Frozen actor-identity, evidence and graph-scope guidance | context_only | A graph actor must retain its chemical or structural identity; descriptive topology is not a complete molecular mechanism. |
| boundaries | data/structures/membrane_organelle/magnetosome_lumen.yaml; Entire frozen neighboring whole/lumen/membrane records as listed in expanded inspection inputs | context_only | All three boundary records were read as context. Only this target receives a review; neighboring prose is not independent biological proof. |
| magnetosome-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0110143,GO:0110145,GO:0110146,GO:0043231,GO:0043233,GO:0016020; All requested IDs, names, definitions, obsolete flags and typed returned child relations | supports | All six requested GO identities are active. GO0110143 denotes the magnetic-mineral organelle and directly has the lumen0110145 and membrane0110146 as part_of children; it is an is_a child of0043231. Lumen and membrane retain distinct native definitions. A subtype or contained-part relation is not converted into a universal subclass assertion. |
| magnetosome-agent-SL0510 | https://rest.uniprot.org/locations/SL-0510.json; Native subcellular-location ID, entry name, definition, GO cross-reference and typed hierarchy | supports | SL0510 identifies Magnetosome and maps exactly to GO0110143. |
| magnetosome-agent-SL0511 | https://rest.uniprot.org/locations/SL-0511.json; Native subcellular-location ID, entry name, definition, GO cross-reference and typed hierarchy | supports | SL0511 identifies Magnetosome lumen, maps exactly to GO0110145 and gives Magnetosome as its containing location. |
| magnetosome-agent-SL0512 | https://rest.uniprot.org/locations/SL-0512.json; Native subcellular-location ID, entry name, definition, GO cross-reference and typed hierarchy | supports | SL0512 identifies Magnetosome membrane, maps exactly to GO0110146 and gives its membrane classification and magnetosome parthood. |
| magnetosome-agent-micro0000216 | https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000216; Exact term identity, definition and active flag | supports | The active MICRO0000216 identity is magnetosome, supporting the cross-reference. Historical descriptive details in that ontology entry are not adopted as new universal biological claims. |
| magnetosome-agent-tax28211 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/28211; Complete exact taxId, scientificName, rank, lineage and alternative-name fields | supports | ENA verifies the exact taxonomy identity, scientific name and rank for 28211. This is identity evidence, not measured prevalence or a biological absence experiment. |
| magnetosome-agent-tax1236 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1236; Complete exact taxId, scientificName, rank, lineage and alternative-name fields | supports | ENA verifies the exact taxonomy identity, scientific name and rank for 1236. This is identity evidence, not measured prevalence or a biological absence experiment. |
| magnetosome-agent-tax2157 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2157; Complete exact taxId, scientificName, rank, lineage and alternative-name fields | supports | ENA verifies the exact taxonomy identity, scientific name and rank for 2157. This is identity evidence, not measured prevalence or a biological absence experiment. |
| magnetosome-agent-tax431944 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/431944; Complete exact taxId, scientificName, rank, lineage and alternative-name fields | supports | ENA verifies the exact taxonomy identity, scientific name and rank for 431944. This is identity evidence, not measured prevalence or a biological absence experiment. |
| magnetosome-agent-tax342108 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/342108; Complete exact taxId, scientificName, rank, lineage and alternative-name fields | supports | ENA verifies the exact taxonomy identity, scientific name and rank for 342108. This is identity evidence, not measured prevalence or a biological absence experiment. |
| magnetosome-agent-uebe2016-publisher | https://www.nature.com/articles/nrmicro.2016.99; Complete Key Points and Abstract only; Access options boundary inspected; not a complete main article | supports | The genuine publisher response exposes Key Points and Abstract for Uebe and Schuler2016. These support membrane-enclosed magnetic crystals, genetic model strains, and the overview of invagination, protein recruitment, iron transport, redox biomineralization and chain positioning. The subscription main body is not readable here. |
| magnetosome-agent-uebe2016-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038/nrmicro.2016.99; Exact title/authors/DOI/PMID and complete abstractText | supports | The exact native MED record identifies Uebe and Schuler2016, Magnetosome biogenesis in magnetotactic bacteria, DOI10.1038/nrmicro.2016.99, PMID27620945. Its complete abstract matches the publisher abstract. |
| magnetosome-agent-barber2015-pmc | https://pmc.ncbi.nlm.nih.gov/articles/4815348/; Complete scientific review sections pro2827-sec-0001–pro2827-sec-0007, Table1 and Fig1–2 captions; no image pixels or supplements | supports | This fully inspected review distinguishes magnetite from greigite producers, strain-dependent membrane biogenesis, MamA/Mms6 dispensability in particular experiments, proposed MamB/MamM metal-ion transport, and distinct MamK/MamJ chain functions. Its approximate crystal-size range is30–120nm; it does not independently verify the target exact35–120nm diameter range. |
| magnetosome-agent-barber2015-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1002/pro.2827; Exact native title/authors/DOI/PMID/publication dates and complete abstractText | supports | The native record identifies Barber-Zucker, Keren-Khadmy and Zarivach, DOI10.1002/pro.2827, PMID26457474;2015 online publication and2016 issue dates coexist. The abbreviated target author wording does not change source identity. |
| magnetosome-agent-PMID11571158 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A11571158%20AND%20SRC%3AMED; Exact MED id/source, title, DOI, authorString and complete abstractText | supports | The exact native MED record verifies PMID11571158, title “A large gene cluster encoding several magnetosome proteins is conserved in different species of magnetotactic bacteria.”, DOI and authors. Complete abstract read; its experiment is retained at the stated organism/strain and assay scope. This separately resolves the full-corpus eutils414 transport result. |
| magnetosome-agent-PMID14766587 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A14766587%20AND%20SRC%3AMED; Exact MED id/source, title, DOI, authorString and complete abstractText | supports | The exact native MED record verifies PMID14766587, title “Biochemical and proteomic analysis of the magnetosome membrane in Magnetospirillum gryphiswaldense.”, DOI and authors. Complete abstract read; its experiment is retained at the stated organism/strain and assay scope. This separately resolves the full-corpus eutils414 transport result. |
| magnetosome-agent-PMID17601786 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A17601786%20AND%20SRC%3AMED; Exact MED id/source, title, DOI, authorString and complete abstractText | supports | The exact native MED record verifies PMID17601786, title “The acidic repetitive domain of the Magnetospirillum gryphiswaldense MamJ protein displays hypervariability but is not required for magnetosome chain assembly.”, DOI and authors. Complete abstract read; its experiment is retained at the stated organism/strain and assay scope. This separately resolves the full-corpus eutils414 transport result. |
| magnetosome-agent-PMID20212111 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A20212111%20AND%20SRC%3AMED; Exact MED id/source, title, DOI, authorString and complete abstractText | supports | The exact native MED record verifies PMID20212111, title “Comprehensive genetic dissection of the magnetosome gene island reveals the step-wise assembly of a prokaryotic organelle.”, DOI and authors. Complete abstract read; its experiment is retained at the stated organism/strain and assay scope. This separately resolves the full-corpus eutils414 transport result. |
| magnetosome-agent-PMID20487281 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A20487281%20AND%20SRC%3AMED; Exact MED id/source, title, DOI, authorString and complete abstractText | supports | The exact native MED record verifies PMID20487281, title “Loss of the actin-like protein MamK has pleiotropic effects on magnetosome formation and chain assembly in Magnetospirillum gryphiswaldense.”, DOI and authors. Complete abstract read; its experiment is retained at the stated organism/strain and assay scope. This separately resolves the full-corpus eutils414 transport result. |
| magnetosome-agent-PMID22007638 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A22007638%20AND%20SRC%3AMED; Exact MED id/source, title, DOI, authorString and complete abstractText | supports | The exact native MED record verifies PMID22007638, title “The cation diffusion facilitator proteins MamB and MamM of Magnetospirillum gryphiswaldense have distinct and complex functions, and are involved in magnetite biomineralization and magnetosome membrane assembly.”, DOI and authors. Complete abstract read; its experiment is retained at the stated organism/strain and assay scope. This separately resolves the full-corpus eutils414 transport result. |
| magnetosome-agent-PMID27481925 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A27481925%20AND%20SRC%3AMED; Exact MED id/source, title, DOI, authorString and complete abstractText | supports | The exact native MED record verifies PMID27481925, title “Comparative Subcellular Localization Analysis of Magnetosome Proteins Reveals a Unique Localization Behavior of Mms6 Protein onto Magnetite Crystals.”, DOI and authors. Complete abstract read; its experiment is retained at the stated organism/strain and assay scope. This separately resolves the full-corpus eutils414 transport result. |
| magnetosome-agent-grunberg2004-pmc | https://pmc.ncbi.nlm.nih.gov/articles/348919/; Complete Methods sec1, Results sec13 including subsections14–25 and Tables1–3, complete Discussion sec26; Fig1–7 captions read, no pixels | supports | Direct primary evidence from MSR-1 magnetosome isolation, lipid analysis, gels, sequencing and mass spectrometry supports a membrane with a distinct protein complement and the named Mam/Mms constituents. Table2 separates bona fide assignments from Table3 putative contaminants; binding, transient association and contamination limitations remain explicit. The paper does not establish formation necessity by depletion of each protein or lipid. |
| magnetosome-agent-grunberg2001-pmc | https://pmc.ncbi.nlm.nih.gov/articles/93205/; Complete Methods sec1, Results sec12 with Tables1–3 and Fig1–5 captions, complete Discussion sec23; no figure pixels | supports | MSR-1 purification, electrophoresis, N-terminal sequences and gene analyses identify MamA/B/C/D/E-associated material, with additional homologs and candidate functions distinguished from experiments. CDF-mediated iron transport was hypothesized, not directly measured in this source. |
| magnetosome-agent-murat2010-correct-pmc | https://pmc.ncbi.nlm.nih.gov/articles/2851823/; Complete Results s1 including Table1/Fig1–5 captions, Discussion s2/Fig6 caption and main Methods s3. Unsectioned introduction, supplements and image pixels were not independently inspected. | supports | AMB-1 genetic dissection directly separates membrane formation, protein localization, positioning and crystal production. MamJ-GFP localizes with the wild-type chain and redistributes in selected mutants; membrane-deficient mutants differ from crystal-deficient mutants. MamL mostly labels the cell membrane, with chain-like signal in a minority. Four required genes are not sufficient to restore compartments. |
| magnetosome-agent-scheffel2007-pmc | https://pmc.ncbi.nlm.nih.gov/articles/1951895/; Complete Methods sec1, Results sec9 and Discussion sec15; Fig1–6 captions. Unsectioned introduction, supplements and image pixels were not independently inspected. | supports | MSR-1 complementation and localization support MamK filament localization and MamJ chain organization; E.coli two-hybrid experiments support MamJ–MamK interaction, with explicit need for orthogonal confirmation. MamJ deletion leaves mineral particles but alters distribution, aggregation and chain geometry. |
| magnetosome-agent-arakaki2016-pmc | https://pmc.ncbi.nlm.nih.gov/articles/5038011/; Complete Introduction sec1, Methods sec2, Results sec3 including Tables1–2 and Discussion sec4; Fig1–6 captions, no pixels or supplements | supports | GFP-fusion experiments in AMB-1 show distinct protein-localization patterns. MamJ/MamK form longer linear patterns than crystal-growth proteins; Mms6 recruitment changes between aerobic and microaerobic conditions and correlates with crystals. MamL is predominantly cell-membrane localized with a minority chain-like pattern. The spatial model remains hypothetical. |
| magnetosome-agent-chebi46726 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_46726; Exact active OLS identity, label, definition, formula/charge annotations | supports | CHEBI46726 denotes magnetite Fe3O4. |
| magnetosome-agent-chebi86238 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86238; Exact active OLS identity, label, definition, formula/charge annotations | supports | CHEBI86238 denotes greigite Fe3S4, a distinct alternative magnetic mineral. |
| magnetosome-agent-chebi18248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18248; Exact active OLS identity, label, definition, formula/charge annotations | supports | CHEBI18248 denotes an iron atom with charge0, not a transported iron cation. |
| magnetosome-agent-uo0000018 | https://www.ebi.ac.uk/ols4/api/ontologies/uo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUO_0000018; Exact active term identity and definition | supports | UO0000018 is the active nanometer unit. This verifies the unit, not the exact numerical range or diameter convention. |
| magnetosome-agent-trait-index | https://culturebotai.github.io/TraitMech/pages/data/trait_graph.json; Exact index row with id traitmech:000071; label/category/match_method fields | supports | The public TraitMech index contains exactly the inspected row traitmech:000071, label magnetosome, category morphology. The index supplies identifier/label linkage; the biological orientation mechanism comes from the literature. |
| mamk-record | data/structures/cytoskeleton/mamk_filament.yaml; Entire frozen MamK filament record; exact local identifier and structural boundary | context_only | The local minted CURIE cellstructuremech:mamk_filament resolves to the MamK filament record. This is identity/context support, not an independent experiment. |
| magnetosome-agent-IPR060787 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR060787/; Metadata accession/name/type, member database and integrated family identity | supports | Native InterPro metadata identifies family IPR060787 as Magnetosome protein MamJ. Both retained MamJ UniProt records independently cross-reference that same family; no domain is promoted to a family. |
| magnetosome-agent-protein-Q93DY9 | https://rest.uniprot.org/uniprotkb/Q93DY9.json; Exact accession/review status, recommended name, primary gene, taxon, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their cited evidence; MamJ InterPro cross-reference where applicable | supports | The reviewed entry Q93DY9 identifies mamA in taxon431944. Localization is interpreted at the source-specific location and evidence code, not as proof of assembly necessity or exclusive residence. |
| magnetosome-agent-protein-V6F510 | https://rest.uniprot.org/uniprotkb/V6F510.json; Exact accession/review status, recommended name, primary gene, taxon, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their cited evidence; MamJ InterPro cross-reference where applicable | supports | The reviewed entry V6F510 identifies mamB in taxon431944. Localization is interpreted at the source-specific location and evidence code, not as proof of assembly necessity or exclusive residence. |
| magnetosome-agent-protein-V6F2B6 | https://rest.uniprot.org/uniprotkb/V6F2B6.json; Exact accession/review status, recommended name, primary gene, taxon, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their cited evidence; MamJ InterPro cross-reference where applicable | supports | The reviewed entry V6F2B6 identifies mamE in taxon431944. Localization is interpreted at the source-specific location and evidence code, not as proof of assembly necessity or exclusive residence. |
| magnetosome-agent-protein-V6F235 | https://rest.uniprot.org/uniprotkb/V6F235.json; Exact accession/review status, recommended name, primary gene, taxon, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their cited evidence; MamJ InterPro cross-reference where applicable | supports | The reviewed entry V6F235 identifies mamM in taxon431944. Localization is interpreted at the source-specific location and evidence code, not as proof of assembly necessity or exclusive residence. |
| magnetosome-agent-protein-Q93DZ1 | https://rest.uniprot.org/uniprotkb/Q93DZ1.json; Exact accession/review status, recommended name, primary gene, taxon, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their cited evidence; MamJ InterPro cross-reference where applicable | supports | The reviewed entry Q93DZ1 identifies mamO in taxon431944. Localization is interpreted at the source-specific location and evidence code, not as proof of assembly necessity or exclusive residence. |
| magnetosome-agent-protein-Q6NE76 | https://rest.uniprot.org/uniprotkb/Q6NE76.json; Exact accession/review status, recommended name, primary gene, taxon, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their cited evidence; MamJ InterPro cross-reference where applicable | supports | The reviewed entry Q6NE76 identifies mms6 in taxon431944. Localization is interpreted at the source-specific location and evidence code, not as proof of assembly necessity or exclusive residence. |
| magnetosome-agent-protein-Q6NE59 | https://rest.uniprot.org/uniprotkb/Q6NE59.json; Exact accession/review status, recommended name, primary gene, taxon, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their cited evidence; MamJ InterPro cross-reference where applicable | supports | The reviewed entry Q6NE59 identifies mamK in taxon431944. Localization is interpreted at the source-specific location and evidence code, not as proof of assembly necessity or exclusive residence. |
| magnetosome-agent-protein-V6F519 | https://rest.uniprot.org/uniprotkb/V6F519.json; Exact accession/review status, recommended name, primary gene, taxon, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their cited evidence; MamJ InterPro cross-reference where applicable | supports | The reviewed entry V6F519 identifies mamJ in taxon431944. Localization is interpreted at the source-specific location and evidence code, not as proof of assembly necessity or exclusive residence. |
| magnetosome-agent-protein-Q2W8Q7 | https://rest.uniprot.org/uniprotkb/Q2W8Q7.json; Exact accession/review status, recommended name, primary gene, taxon, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their cited evidence; MamJ InterPro cross-reference where applicable | supports | The reviewed entry Q2W8Q7 identifies mamJ in taxon342108. Localization is interpreted at the source-specific location and evidence code, not as proof of assembly necessity or exclusive residence. |
| magnetosome-agent-reviewed-uniqueness | https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue%20AND%20%28%28organism_id%3A431944%20AND%20%28gene_exact%3AmamA%20OR%20gene_exact%3AmamB%20OR%20gene_exact%3AmamE%20OR%20gene_exact%3AmamM%20OR%20gene_exact%3AmamO%20OR%20gene_exact%3Amms6%20OR%20gene_exact%3AmamK%20OR%20gene_exact%3AmamJ%29%29%20OR%20%28organism_id%3A342108%20AND%20gene_exact%3AmamJ%29%29&amp;format=json&amp;size=100; Entire returned results for the literal retained URL query, size100; nine records | supports | The bounded exact-gene/taxon reviewed query returns nine entries, one for each of the eight named MSR-1 genes and one AMB-1 mamJ. Each returned primary gene/taxon was independently compared with the target examples; no broader exclusivity is claimed. |
| schema-result | just validate data/structures/membrane_organelle/magnetosome.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/magnetosome.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/magnetosome.yaml --out /private/tmp/cellstructure-batch31-20261022-ag46a4d4/magnetosome-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/magnetosome.yaml --out /private/tmp/cellstructure-batch31-20261022-ag46a4d4/magnetosome-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch31-20261022-ag46a4d4/magnetosome-strict.tsv |
| native-verify | /private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/membrane_organelle/magnetosome.yaml; Exact retained native read-only log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/magnetosome.yaml; Exact retained native read-only log | supports | data/structures/membrane_organelle/magnetosome.yaml  (GO:0110143)<br>  magnetosome_chain_alignment	mam	COVERED	-&gt;mam_proteins (UniProtKB:Q93DY9, UniProtKB:V6F510, UniProtKB:V6F2B6, UniProtKB:V6F235, UniProtKB:Q93DZ1, UniProtKB:Q6NE76)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     1  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/magnetosome.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 24 of 33 collected target identifiers returned OK. PMID:11571158: UNREACHABLE; The bulk transport returned414; the independently retrieved exact MED identity confirms PMID11571158, DOI10.1128/aem.67.10.4573-4582.2001 and A large gene cluster encoding several magnetosome proteins is conserved in different species of magnetotactic bacteria. Scientific scope remains limited to the separately documented inspections.; PMID:14766587: UNREACHABLE; The bulk transport returned414; the independently retrieved exact MED identity confirms PMID14766587, DOI10.1128/aem.70.2.1040-1050.2004 and Biochemical and proteomic analysis of the magnetosome membrane in Magnetospirillum gryphiswaldense. Scientific scope remains limited to the separately documented inspections.; PMID:17601786: UNREACHABLE; The bulk transport returned414; the independently retrieved exact MED identity confirms PMID17601786, DOI10.1128/jb.00421-07 and The acidic repetitive domain of the Magnetospirillum gryphiswaldense MamJ protein displays hypervariability but is not required for magnetosome chain assembly. Scientific scope remains limited to the separately documented inspections.; PMID:20212111: UNREACHABLE; The bulk transport returned414; the independently retrieved exact MED identity confirms PMID20212111, DOI10.1073/pnas.0914439107 and Comprehensive genetic dissection of the magnetosome gene island reveals the step-wise assembly of a prokaryotic organelle. Scientific scope remains limited to the separately documented inspections.; PMID:20487281: UNREACHABLE; The bulk transport returned414; the independently retrieved exact MED identity confirms PMID20487281, DOI10.1111/j.1365-2958.2010.07202.x and Loss of the actin-like protein MamK has pleiotropic effects on magnetosome formation and chain assembly in Magnetospirillum gryphiswaldense. Scientific scope remains limited to the separately documented inspections.; PMID:22007638: UNREACHABLE; The bulk transport returned414; the independently retrieved exact MED identity confirms PMID22007638, DOI10.1111/j.1365-2958.2011.07863.x and The cation diffusion facilitator proteins MamB and MamM of Magnetospirillum gryphiswaldense have distinct and complex functions, and are involved in magnetite biomineralization and magnetosome membrane assembly. Scientific scope remains limited to the separately documented inspections.; PMID:27481925: UNREACHABLE; The bulk transport returned414; the independently retrieved exact MED identity confirms PMID27481925, DOI10.1128/jb.00280-16 and Comparative Subcellular Localization Analysis of Magnetosome Proteins Reveals a Unique Localization Behavior of Mms6 Protein onto Magnetite Crystals. Scientific scope remains limited to the separately documented inspections.; cellstructuremech:mamk_filament: SKIPPED; The repository-minted identifier uniquely resolves to the frozen maintained MamK filament record at data/structures/cytoskeleton/mamk_filament.yaml. An anchored hidden/ignored-inclusive corpus search and exact input hash confirm reference identity, not all biological assertions.; traitmech:000071: SKIPPED; The exact native TraitMech index row resolves traitmech:000071 to magnetosome, morphology category. This verifies identifier/label linkage, not the mechanistic meaning of a trait. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- The fresh target-resolver slice and all five corpus receipt/manifest checks are integrated in this completed review.
- Uebe2016 publisher and nominal-PDF responses contain Key Points/Abstract and access options, not a complete main body. Uebe2011 is native abstract only; its publisher response is403. No unread source passage is certified.
- The Barber review is secondary authority. Its complete scientific main body was read, as were Grünberg2004 Methods/Results/Discussion. No paper image pixels, supplements or raw assay data were inspected.
- Strain-specific mutants, membrane formation, crystal formation and chain organization remain distinct. Collective constituents are not taken as proof that every individual member is required for structure formation.
- Qualitative taxon occurrence and literature-bounded absence are not an exhaustive contemporary prevalence survey. Historical retrieval/search statements are not re-certified or declared false merely because newer evidence exists.
- Grünberg2001, Murat2010 and Scheffel2007 Methods/Results/Discussion and Arakaki2016 Introduction/Methods/Results/Discussion were read, including main captions/tables. Murat/Scheffel unsectioned introductions, all supplements and all figure pixels were not inspected. Katzmann2010 remains complete native abstract only.
- The failed guessed Murat numeric-PMC locator returned an unrelated insulin article; it is retained as rejected access evidence, never used scientifically. The correct PMC2851823 body is separately retained.
- The exact35–120nm diameter range remains unverified against the unread Uebe body; the independent review supplies an approximate30–120nm crystal-size range. MamB/MamM transport details and MamJ linkage retain the qualification of the cited experiments/models.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User explicitly authorizes one review per uncovered record, including clean pass_with_limitations, overriding the local issue-only output restriction.
- Only unsaved support/review artifacts are written outside the maintained repository; no scientific record, save/index, Git or publication mutation.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T021713Z-magnetosome-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Magnetosome identity, composition and source-scope review
started_at: '2026-10-22T01:50:53Z'
finished_at: '2026-10-22T02:17:13Z'
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
summary: Two major findings concern universal magnetite necessity and neutral-atom
  transport grounding; two minor findings update a stale current localization-gap
  interpretation and the MamJ-deletion phenotype wording. The supported organelle
  identity, protein examples and chain biology remain intact.
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
  - path: data/structures/cytoskeleton/mamk_filament.yaml
    sha256: fb273942dd11b99a71c61834f5ca331829a340b6a271e0f73e050c1b0128ca64
    role: context
  - path: data/structures/membrane_organelle/magnetosome.yaml
    sha256: dd4f1d27b520b8e0b00bc379f6adbac38204d45bed6c1cc9e27a5f3b37f6f4d3
    role: target
  - path: data/structures/membrane_organelle/magnetosome_lumen.yaml
    sha256: 6e777efa5c662d732dad014690fca690f9cad0ec08d9990e907ec04112e059c6
    role: context
  - path: data/structures/membrane_organelle/magnetosome_membrane.yaml
    sha256: 2c4667f86bae65f60cb8aa414079523e0b5f38a940b192e858d5a76f143c6ed4
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
- target_id: GO:0110143
  path: data/structures/membrane_organelle/magnetosome.yaml
  label: magnetosome
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/magnetosome.yaml
    role: maintained scientific record
scope:
  description: Entire single target, exact identities, hierarchy/boundaries, composition,
    formation necessity, native protein evidence, taxonomic and experimental scope,
    function, all graph claims and discussions.
  selection: Target 8 of batch31 in strict uncovered path order; frozen native inspection/schema/strict
    completed before scientific assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0110143
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0110143
  command: just validate data/structures/membrane_organelle/magnetosome.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0110143
  command: just validate-strict data/structures/membrane_organelle/magnetosome.yaml
    --out /private/tmp/cellstructure-batch31-20261022-ag46a4d4/magnetosome-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - GO:0110143
  command: /private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/membrane_organelle/magnetosome.yaml
  exit_code: 0
  summary: Native read-only check passed; reporting coverage classes is not itself
    a scientific finding.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0110143
  command: /private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/magnetosome.yaml
  exit_code: 0
  summary: Native read-only check passed; reporting coverage classes is not itself
    a scientific finding.
  evidence_ids:
  - native-causal-graphs
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0110143
  summary: No regulatory expression-module assertion is used.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0110143
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - graph-policy
  - boundaries
  - magnetosome-agent-go
  - magnetosome-agent-SL0510
  - magnetosome-agent-SL0511
  - magnetosome-agent-SL0512
  - magnetosome-agent-micro0000216
  - magnetosome-agent-tax28211
  - magnetosome-agent-tax1236
  - magnetosome-agent-tax2157
  - magnetosome-agent-tax431944
  - magnetosome-agent-tax342108
  - magnetosome-agent-uebe2016-publisher
  - magnetosome-agent-uebe2016-meta
  - magnetosome-agent-barber2015-pmc
  - magnetosome-agent-barber2015-meta
  - magnetosome-agent-PMID11571158
  - magnetosome-agent-PMID14766587
  - magnetosome-agent-PMID17601786
  - magnetosome-agent-PMID20212111
  - magnetosome-agent-PMID20487281
  - magnetosome-agent-PMID22007638
  - magnetosome-agent-PMID27481925
  - magnetosome-agent-grunberg2004-pmc
  - magnetosome-agent-grunberg2001-pmc
  - magnetosome-agent-murat2010-correct-pmc
  - magnetosome-agent-scheffel2007-pmc
  - magnetosome-agent-arakaki2016-pmc
  - magnetosome-agent-chebi46726
  - magnetosome-agent-chebi86238
  - magnetosome-agent-chebi18248
  - magnetosome-agent-uo0000018
  - magnetosome-agent-trait-index
  - mamk-record
  - magnetosome-agent-IPR060787
  - magnetosome-agent-protein-Q93DY9
  - magnetosome-agent-protein-V6F510
  - magnetosome-agent-protein-V6F2B6
  - magnetosome-agent-protein-V6F235
  - magnetosome-agent-protein-Q93DZ1
  - magnetosome-agent-protein-Q6NE76
  - magnetosome-agent-protein-Q6NE59
  - magnetosome-agent-protein-V6F519
  - magnetosome-agent-protein-Q2W8Q7
  - magnetosome-agent-reviewed-uniqueness
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0110143
  summary: '24 of 33 collected target identifiers returned OK. PMID:11571158: UNREACHABLE;
    The bulk transport returned414; the independently retrieved exact MED identity
    confirms PMID11571158, DOI10.1128/aem.67.10.4573-4582.2001 and A large gene cluster
    encoding several magnetosome proteins is conserved in different species of magnetotactic
    bacteria. Scientific scope remains limited to the separately documented inspections.;
    PMID:14766587: UNREACHABLE; The bulk transport returned414; the independently
    retrieved exact MED identity confirms PMID14766587, DOI10.1128/aem.70.2.1040-1050.2004
    and Biochemical and proteomic analysis of the magnetosome membrane in Magnetospirillum
    gryphiswaldense. Scientific scope remains limited to the separately documented
    inspections.; PMID:17601786: UNREACHABLE; The bulk transport returned414; the
    independently retrieved exact MED identity confirms PMID17601786, DOI10.1128/jb.00421-07
    and The acidic repetitive domain of the Magnetospirillum gryphiswaldense MamJ
    protein displays hypervariability but is not required for magnetosome chain assembly.
    Scientific scope remains limited to the separately documented inspections.; PMID:20212111:
    UNREACHABLE; The bulk transport returned414; the independently retrieved exact
    MED identity confirms PMID20212111, DOI10.1073/pnas.0914439107 and Comprehensive
    genetic dissection of the magnetosome gene island reveals the step-wise assembly
    of a prokaryotic organelle. Scientific scope remains limited to the separately
    documented inspections.; PMID:20487281: UNREACHABLE; The bulk transport returned414;
    the independently retrieved exact MED identity confirms PMID20487281, DOI10.1111/j.1365-2958.2010.07202.x
    and Loss of the actin-like protein MamK has pleiotropic effects on magnetosome
    formation and chain assembly in Magnetospirillum gryphiswaldense. Scientific scope
    remains limited to the separately documented inspections.; PMID:22007638: UNREACHABLE;
    The bulk transport returned414; the independently retrieved exact MED identity
    confirms PMID22007638, DOI10.1111/j.1365-2958.2011.07863.x and The cation diffusion
    facilitator proteins MamB and MamM of Magnetospirillum gryphiswaldense have distinct
    and complex functions, and are involved in magnetite biomineralization and magnetosome
    membrane assembly. Scientific scope remains limited to the separately documented
    inspections.; PMID:27481925: UNREACHABLE; The bulk transport returned414; the
    independently retrieved exact MED identity confirms PMID27481925, DOI10.1128/jb.00280-16
    and Comparative Subcellular Localization Analysis of Magnetosome Proteins Reveals
    a Unique Localization Behavior of Mms6 Protein onto Magnetite Crystals. Scientific
    scope remains limited to the separately documented inspections.; cellstructuremech:mamk_filament:
    SKIPPED; The repository-minted identifier uniquely resolves to the frozen maintained
    MamK filament record at data/structures/cytoskeleton/mamk_filament.yaml. An anchored
    hidden/ignored-inclusive corpus search and exact input hash confirm reference
    identity, not all biological assertions.; traitmech:000071: SKIPPED; The exact
    native TraitMech index row resolves traitmech:000071 to magnetosome, morphology
    category. This verifies identifier/label linkage, not the mechanistic meaning
    of a trait. Native source checks are separately scoped; skipped or unreachable
    identifiers are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - magnetosome-agent-PMID11571158
  - magnetosome-agent-PMID14766587
  - magnetosome-agent-PMID17601786
  - magnetosome-agent-PMID20212111
  - magnetosome-agent-PMID20487281
  - magnetosome-agent-PMID22007638
  - magnetosome-agent-PMID27481925
  - mamk-record
  - magnetosome-agent-trait-index
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0110143
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch31 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0110143
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch31 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0110143
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch31 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0110143
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch31 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0110143
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
    and current batch31 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/magnetosome.yaml
  locator: Entire maintained target including history, discussions, evidence and every
    graph node/edge
  accessed_at: '2026-10-22T02:04:20Z'
  support: context_only
  summary: The entire single target was read; its maintained scientific bytes remain
    unchanged.
- evidence_id: policy
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent; molecular grounding; essentiality; EssentialityEnum;
    CausalNode.component_ref
  accessed_at: '2026-10-22T02:04:20Z'
  support: context_only
  summary: Essentiality states whether the structure forms without a component. Molecular
    species, material constituents, complete membranes and enclosed volumes remain
    distinct.
- evidence_id: graph-policy
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Frozen actor-identity, evidence and graph-scope guidance
  accessed_at: '2026-10-22T02:04:20Z'
  support: context_only
  summary: A graph actor must retain its chemical or structural identity; descriptive
    topology is not a complete molecular mechanism.
- evidence_id: boundaries
  kind: record_content
  reference: data/structures/membrane_organelle/magnetosome_lumen.yaml
  locator: Entire frozen neighboring whole/lumen/membrane records as listed in expanded
    inspection inputs
  accessed_at: '2026-10-22T02:04:20Z'
  support: context_only
  summary: All three boundary records were read as context. Only this target receives
    a review; neighboring prose is not independent biological proof.
- evidence_id: magnetosome-agent-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0110143,GO:0110145,GO:0110146,GO:0043231,GO:0043233,GO:0016020
  locator: All requested IDs, names, definitions, obsolete flags and typed returned
    child relations
  accessed_at: '2026-10-22T01:54:50.489778Z'
  support: supports
  summary: All six requested GO identities are active. GO0110143 denotes the magnetic-mineral
    organelle and directly has the lumen0110145 and membrane0110146 as part_of children;
    it is an is_a child of0043231. Lumen and membrane retain distinct native definitions.
    A subtype or contained-part relation is not converted into a universal subclass
    assertion.
  snapshot_sha256: fe60b747acb4743040bfafb812bd181bf6b2cac0a8f5ba821cb441ace1f051c8
- evidence_id: magnetosome-agent-SL0510
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0510.json
  locator: Native subcellular-location ID, entry name, definition, GO cross-reference
    and typed hierarchy
  accessed_at: '2026-10-22T01:54:52.525934Z'
  support: supports
  summary: SL0510 identifies Magnetosome and maps exactly to GO0110143.
  snapshot_sha256: aeb4bcf6878993c0447743c8c84901d5a4bacafbde8183dbd0cc4adc2dc3ea8a
- evidence_id: magnetosome-agent-SL0511
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0511.json
  locator: Native subcellular-location ID, entry name, definition, GO cross-reference
    and typed hierarchy
  accessed_at: '2026-10-22T01:54:53.425804Z'
  support: supports
  summary: SL0511 identifies Magnetosome lumen, maps exactly to GO0110145 and gives
    Magnetosome as its containing location.
  snapshot_sha256: bdd80959bf50571da2bace95c31b088edce4ef5ffdbc030ee008da2e8802fa9f
- evidence_id: magnetosome-agent-SL0512
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0512.json
  locator: Native subcellular-location ID, entry name, definition, GO cross-reference
    and typed hierarchy
  accessed_at: '2026-10-22T01:54:53.425483Z'
  support: supports
  summary: SL0512 identifies Magnetosome membrane, maps exactly to GO0110146 and gives
    its membrane classification and magnetosome parthood.
  snapshot_sha256: 1a5e2619ee57df8b04098c35c9768ec4ef04c4d511e4f0f5eccaed6141d65f19
- evidence_id: magnetosome-agent-micro0000216
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000216
  locator: Exact term identity, definition and active flag
  accessed_at: '2026-10-22T01:54:54.645796Z'
  support: supports
  summary: The active MICRO0000216 identity is magnetosome, supporting the cross-reference.
    Historical descriptive details in that ontology entry are not adopted as new universal
    biological claims.
  snapshot_sha256: aeb875c595890df066ada49288c837bffa719de820343694a76847c5d18a4f1c
- evidence_id: magnetosome-agent-tax28211
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/28211
  locator: Complete exact taxId, scientificName, rank, lineage and alternative-name
    fields
  accessed_at: '2026-10-22T01:54:50.505577Z'
  support: supports
  summary: ENA verifies the exact taxonomy identity, scientific name and rank for
    28211. This is identity evidence, not measured prevalence or a biological absence
    experiment.
  snapshot_sha256: eb9d44c1e2cf0944eb4414649c09418a757a87de66fc01f51cc6c980ef68e802
- evidence_id: magnetosome-agent-tax1236
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1236
  locator: Complete exact taxId, scientificName, rank, lineage and alternative-name
    fields
  accessed_at: '2026-10-22T01:54:50.528267Z'
  support: supports
  summary: ENA verifies the exact taxonomy identity, scientific name and rank for
    1236. This is identity evidence, not measured prevalence or a biological absence
    experiment.
  snapshot_sha256: 3b797338ad9a40408789392bddda40d0323f87c30760a754e45b88d02ec8888a
- evidence_id: magnetosome-agent-tax2157
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2157
  locator: Complete exact taxId, scientificName, rank, lineage and alternative-name
    fields
  accessed_at: '2026-10-22T01:54:51.147545Z'
  support: supports
  summary: ENA verifies the exact taxonomy identity, scientific name and rank for
    2157. This is identity evidence, not measured prevalence or a biological absence
    experiment.
  snapshot_sha256: c6e652011b95e43e933983bf5f3f5cec9508c1925adae00dc55e46cd4e816b19
- evidence_id: magnetosome-agent-tax431944
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/431944
  locator: Complete exact taxId, scientificName, rank, lineage and alternative-name
    fields
  accessed_at: '2026-10-22T01:54:51.109038Z'
  support: supports
  summary: ENA verifies the exact taxonomy identity, scientific name and rank for
    431944. This is identity evidence, not measured prevalence or a biological absence
    experiment.
  snapshot_sha256: 8e6916672afb4c32a2a99e2dcc07f5a14b4ba7b0969243ce89646042ce60476d
- evidence_id: magnetosome-agent-tax342108
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/342108
  locator: Complete exact taxId, scientificName, rank, lineage and alternative-name
    fields
  accessed_at: '2026-10-22T01:54:51.123891Z'
  support: supports
  summary: ENA verifies the exact taxonomy identity, scientific name and rank for
    342108. This is identity evidence, not measured prevalence or a biological absence
    experiment.
  snapshot_sha256: 23ab2a141de441b18fc4edcd456c3cf95d789c0c017cd9e58cb8bda73a5ae365
- evidence_id: magnetosome-agent-uebe2016-publisher
  kind: authority
  reference: https://www.nature.com/articles/nrmicro.2016.99
  locator: Complete Key Points and Abstract only; Access options boundary inspected;
    not a complete main article
  accessed_at: '2026-10-22T01:55:29.602449Z'
  support: supports
  summary: The genuine publisher response exposes Key Points and Abstract for Uebe
    and Schuler2016. These support membrane-enclosed magnetic crystals, genetic model
    strains, and the overview of invagination, protein recruitment, iron transport,
    redox biomineralization and chain positioning. The subscription main body is not
    readable here.
  snapshot_sha256: 068e5eea78b8f17c89b712fb2777cfebe58c6b78f2b83707d8c554273a8e9359
- evidence_id: magnetosome-agent-uebe2016-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/nrmicro.2016.99
  locator: Exact title/authors/DOI/PMID and complete abstractText
  accessed_at: '2026-10-22T01:54:53.760632Z'
  support: supports
  summary: The exact native MED record identifies Uebe and Schuler2016, Magnetosome
    biogenesis in magnetotactic bacteria, DOI10.1038/nrmicro.2016.99, PMID27620945.
    Its complete abstract matches the publisher abstract.
  snapshot_sha256: aafc33cb7d6402c95ed55eda17b01e3ef154db512917948d8161ed5bd3ac945e
- evidence_id: magnetosome-agent-barber2015-pmc
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/4815348/
  locator: Complete scientific review sections pro2827-sec-0001–pro2827-sec-0007,
    Table1 and Fig1–2 captions; no image pixels or supplements
  accessed_at: '2026-10-22T01:55:28.453057Z'
  support: supports
  summary: This fully inspected review distinguishes magnetite from greigite producers,
    strain-dependent membrane biogenesis, MamA/Mms6 dispensability in particular experiments,
    proposed MamB/MamM metal-ion transport, and distinct MamK/MamJ chain functions.
    Its approximate crystal-size range is30–120nm; it does not independently verify
    the target exact35–120nm diameter range.
  snapshot_sha256: a052d6b82e120fa4f253f6aa7abeaf5c9a5080f7748fbbe35cfd2150c3713934
- evidence_id: magnetosome-agent-barber2015-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1002/pro.2827
  locator: Exact native title/authors/DOI/PMID/publication dates and complete abstractText
  accessed_at: '2026-10-22T01:54:54.045286Z'
  support: supports
  summary: The native record identifies Barber-Zucker, Keren-Khadmy and Zarivach,
    DOI10.1002/pro.2827, PMID26457474;2015 online publication and2016 issue dates
    coexist. The abbreviated target author wording does not change source identity.
  snapshot_sha256: 2fbe01feb61de63ae0641fcb7d783622f8e45a56acbb420948f5bb24612f50e1
- evidence_id: magnetosome-agent-PMID11571158
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A11571158%20AND%20SRC%3AMED
  locator: Exact MED id/source, title, DOI, authorString and complete abstractText
  accessed_at: '2026-10-22T01:54:53.073079Z'
  support: supports
  summary: The exact native MED record verifies PMID11571158, title “A large gene
    cluster encoding several magnetosome proteins is conserved in different species
    of magnetotactic bacteria.”, DOI and authors. Complete abstract read; its experiment
    is retained at the stated organism/strain and assay scope. This separately resolves
    the full-corpus eutils414 transport result.
  snapshot_sha256: 064539a207607d7753e1f0abbe893f69f71384bc5c282433b620e7b237ed41a0
- evidence_id: magnetosome-agent-PMID14766587
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A14766587%20AND%20SRC%3AMED
  locator: Exact MED id/source, title, DOI, authorString and complete abstractText
  accessed_at: '2026-10-22T01:54:53.146827Z'
  support: supports
  summary: The exact native MED record verifies PMID14766587, title “Biochemical and
    proteomic analysis of the magnetosome membrane in Magnetospirillum gryphiswaldense.”,
    DOI and authors. Complete abstract read; its experiment is retained at the stated
    organism/strain and assay scope. This separately resolves the full-corpus eutils414
    transport result.
  snapshot_sha256: 58b737f08ab3ed694909eba9351656b618908df49ab83cd7d6a72fb030650b66
- evidence_id: magnetosome-agent-PMID17601786
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A17601786%20AND%20SRC%3AMED
  locator: Exact MED id/source, title, DOI, authorString and complete abstractText
  accessed_at: '2026-10-22T01:54:53.136886Z'
  support: supports
  summary: The exact native MED record verifies PMID17601786, title “The acidic repetitive
    domain of the Magnetospirillum gryphiswaldense MamJ protein displays hypervariability
    but is not required for magnetosome chain assembly.”, DOI and authors. Complete
    abstract read; its experiment is retained at the stated organism/strain and assay
    scope. This separately resolves the full-corpus eutils414 transport result.
  snapshot_sha256: fa5bfd11cc6cf401c20b18ce15f815d12ec12070bad0bfe9c19494805dce1c64
- evidence_id: magnetosome-agent-PMID20212111
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A20212111%20AND%20SRC%3AMED
  locator: Exact MED id/source, title, DOI, authorString and complete abstractText
  accessed_at: '2026-10-22T01:54:53.741964Z'
  support: supports
  summary: The exact native MED record verifies PMID20212111, title “Comprehensive
    genetic dissection of the magnetosome gene island reveals the step-wise assembly
    of a prokaryotic organelle.”, DOI and authors. Complete abstract read; its experiment
    is retained at the stated organism/strain and assay scope. This separately resolves
    the full-corpus eutils414 transport result.
  snapshot_sha256: 06ce8585bb7cb69dd53a3b68d9fe052076f434cb66505982d0a0b0fe419b3cd7
- evidence_id: magnetosome-agent-PMID20487281
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A20487281%20AND%20SRC%3AMED
  locator: Exact MED id/source, title, DOI, authorString and complete abstractText
  accessed_at: '2026-10-22T01:54:53.732742Z'
  support: supports
  summary: The exact native MED record verifies PMID20487281, title “Loss of the actin-like
    protein MamK has pleiotropic effects on magnetosome formation and chain assembly
    in Magnetospirillum gryphiswaldense.”, DOI and authors. Complete abstract read;
    its experiment is retained at the stated organism/strain and assay scope. This
    separately resolves the full-corpus eutils414 transport result.
  snapshot_sha256: b8fa27e3b78c3f50d4a1d8feb89ed482986677420d9dc39af84c32038056efe9
- evidence_id: magnetosome-agent-PMID22007638
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A22007638%20AND%20SRC%3AMED
  locator: Exact MED id/source, title, DOI, authorString and complete abstractText
  accessed_at: '2026-10-22T01:54:53.139745Z'
  support: supports
  summary: The exact native MED record verifies PMID22007638, title “The cation diffusion
    facilitator proteins MamB and MamM of Magnetospirillum gryphiswaldense have distinct
    and complex functions, and are involved in magnetite biomineralization and magnetosome
    membrane assembly.”, DOI and authors. Complete abstract read; its experiment is
    retained at the stated organism/strain and assay scope. This separately resolves
    the full-corpus eutils414 transport result.
  snapshot_sha256: 6b934aea8d05333a872fb1f27da9983ec1df9ab275b18c735518a15ea1278fe6
- evidence_id: magnetosome-agent-PMID27481925
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A27481925%20AND%20SRC%3AMED
  locator: Exact MED id/source, title, DOI, authorString and complete abstractText
  accessed_at: '2026-10-22T01:54:53.748712Z'
  support: supports
  summary: The exact native MED record verifies PMID27481925, title “Comparative Subcellular
    Localization Analysis of Magnetosome Proteins Reveals a Unique Localization Behavior
    of Mms6 Protein onto Magnetite Crystals.”, DOI and authors. Complete abstract
    read; its experiment is retained at the stated organism/strain and assay scope.
    This separately resolves the full-corpus eutils414 transport result.
  snapshot_sha256: 6674788db85978b761503f20d0a5aeb56a83f21b4952fe54c58c252b0af2995d
- evidence_id: magnetosome-agent-grunberg2004-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/348919/
  locator: Complete Methods sec1, Results sec13 including subsections14–25 and Tables1–3,
    complete Discussion sec26; Fig1–7 captions read, no pixels
  accessed_at: '2026-10-22T01:55:28.245268Z'
  support: supports
  summary: Direct primary evidence from MSR-1 magnetosome isolation, lipid analysis,
    gels, sequencing and mass spectrometry supports a membrane with a distinct protein
    complement and the named Mam/Mms constituents. Table2 separates bona fide assignments
    from Table3 putative contaminants; binding, transient association and contamination
    limitations remain explicit. The paper does not establish formation necessity
    by depletion of each protein or lipid.
  snapshot_sha256: ca7ae2f19185633cd778e9550909b7f68bb2ea18c80f4c0a7a65aa7c59527485
- evidence_id: magnetosome-agent-grunberg2001-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/93205/
  locator: Complete Methods sec1, Results sec12 with Tables1–3 and Fig1–5 captions,
    complete Discussion sec23; no figure pixels
  accessed_at: '2026-10-22T01:55:28.231919Z'
  support: supports
  summary: MSR-1 purification, electrophoresis, N-terminal sequences and gene analyses
    identify MamA/B/C/D/E-associated material, with additional homologs and candidate
    functions distinguished from experiments. CDF-mediated iron transport was hypothesized,
    not directly measured in this source.
  snapshot_sha256: 4c92051e5e7ac09949304aeab0f462e67b3fa7af91c720b289c5bcc41a85ca64
- evidence_id: magnetosome-agent-murat2010-correct-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/2851823/
  locator: Complete Results s1 including Table1/Fig1–5 captions, Discussion s2/Fig6
    caption and main Methods s3. Unsectioned introduction, supplements and image pixels
    were not independently inspected.
  accessed_at: '2026-10-22T02:01:12.318453Z'
  support: supports
  summary: AMB-1 genetic dissection directly separates membrane formation, protein
    localization, positioning and crystal production. MamJ-GFP localizes with the
    wild-type chain and redistributes in selected mutants; membrane-deficient mutants
    differ from crystal-deficient mutants. MamL mostly labels the cell membrane, with
    chain-like signal in a minority. Four required genes are not sufficient to restore
    compartments.
  snapshot_sha256: b2d328e8eb33d389e302d9d417b76df4d1e192601ae39cc9a3726c5409f0cb6e
- evidence_id: magnetosome-agent-scheffel2007-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/1951895/
  locator: Complete Methods sec1, Results sec9 and Discussion sec15; Fig1–6 captions.
    Unsectioned introduction, supplements and image pixels were not independently
    inspected.
  accessed_at: '2026-10-22T02:01:12.342219Z'
  support: supports
  summary: MSR-1 complementation and localization support MamK filament localization
    and MamJ chain organization; E.coli two-hybrid experiments support MamJ–MamK interaction,
    with explicit need for orthogonal confirmation. MamJ deletion leaves mineral particles
    but alters distribution, aggregation and chain geometry.
  snapshot_sha256: f97eb3fb4c1d31bf2f5b110fd149ea9a4a1244ca2d082dd3808c3bf0c710f427
- evidence_id: magnetosome-agent-arakaki2016-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/5038011/
  locator: Complete Introduction sec1, Methods sec2, Results sec3 including Tables1–2
    and Discussion sec4; Fig1–6 captions, no pixels or supplements
  accessed_at: '2026-10-22T01:55:28.278615Z'
  support: supports
  summary: GFP-fusion experiments in AMB-1 show distinct protein-localization patterns.
    MamJ/MamK form longer linear patterns than crystal-growth proteins; Mms6 recruitment
    changes between aerobic and microaerobic conditions and correlates with crystals.
    MamL is predominantly cell-membrane localized with a minority chain-like pattern.
    The spatial model remains hypothetical.
  snapshot_sha256: 7ced9ec58bbcc676dd7fd517dd7f3d4c93fa9a23ca27053668cafe7840f914ab
- evidence_id: magnetosome-agent-chebi46726
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_46726
  locator: Exact active OLS identity, label, definition, formula/charge annotations
  accessed_at: '2026-10-22T01:54:54.474223Z'
  support: supports
  summary: CHEBI46726 denotes magnetite Fe3O4.
  snapshot_sha256: 0abc845119f9fdaa12a29c2a3cd76bf6de785b2b5009ff76a38f36709ea60213
- evidence_id: magnetosome-agent-chebi86238
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86238
  locator: Exact active OLS identity, label, definition, formula/charge annotations
  accessed_at: '2026-10-22T01:54:54.397513Z'
  support: supports
  summary: CHEBI86238 denotes greigite Fe3S4, a distinct alternative magnetic mineral.
  snapshot_sha256: 7dcd024053e2086928174c71ff2981d86855f92975fa2a219462554e136a6176
- evidence_id: magnetosome-agent-chebi18248
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18248
  locator: Exact active OLS identity, label, definition, formula/charge annotations
  accessed_at: '2026-10-22T01:54:54.474860Z'
  support: supports
  summary: CHEBI18248 denotes an iron atom with charge0, not a transported iron cation.
  snapshot_sha256: 8b382aa1dc3cdaedba15e69b40a2b75133d1c67f88cb75341932a8bce2595af5
- evidence_id: magnetosome-agent-uo0000018
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUO_0000018
  locator: Exact active term identity and definition
  accessed_at: '2026-10-22T01:54:54.392049Z'
  support: supports
  summary: UO0000018 is the active nanometer unit. This verifies the unit, not the
    exact numerical range or diameter convention.
  snapshot_sha256: 5aa4d11cd0f398ac65be12b58f91295efae620bb2e5c345bd0fd81c6f0e09c5c
- evidence_id: magnetosome-agent-trait-index
  kind: database
  reference: https://culturebotai.github.io/TraitMech/pages/data/trait_graph.json
  locator: Exact index row with id traitmech:000071; label/category/match_method fields
  accessed_at: '2026-10-22T01:56:53.833323Z'
  support: supports
  summary: The public TraitMech index contains exactly the inspected row traitmech:000071,
    label magnetosome, category morphology. The index supplies identifier/label linkage;
    the biological orientation mechanism comes from the literature.
  snapshot_sha256: bdd3ee3c4f3db4e6b73aa25d87da7dfeb179d056154e491a7abc3d643c6847d8
- evidence_id: mamk-record
  kind: record_content
  reference: data/structures/cytoskeleton/mamk_filament.yaml
  locator: Entire frozen MamK filament record; exact local identifier and structural
    boundary
  accessed_at: '2026-10-22T02:04:20Z'
  support: context_only
  summary: The local minted CURIE cellstructuremech:mamk_filament resolves to the
    MamK filament record. This is identity/context support, not an independent experiment.
- evidence_id: magnetosome-agent-IPR060787
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR060787/
  locator: Metadata accession/name/type, member database and integrated family identity
  accessed_at: '2026-10-22T01:54:54.475971Z'
  support: supports
  summary: Native InterPro metadata identifies family IPR060787 as Magnetosome protein
    MamJ. Both retained MamJ UniProt records independently cross-reference that same
    family; no domain is promoted to a family.
  snapshot_sha256: 30bea264adde7bd7af90b512f677882c4f08d4ada31a0bda8df269035e729217
- evidence_id: magnetosome-agent-protein-Q93DY9
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q93DY9.json
  locator: Exact accession/review status, recommended name, primary gene, taxon, FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION comments and their cited evidence; MamJ InterPro cross-reference where
    applicable
  accessed_at: '2026-10-22T01:54:51.333535Z'
  support: supports
  summary: The reviewed entry Q93DY9 identifies mamA in taxon431944. Localization
    is interpreted at the source-specific location and evidence code, not as proof
    of assembly necessity or exclusive residence.
  snapshot_sha256: d0806f93bc6b1b2c700e6d781028aded4bb2194d74302a4cb4074f45dadb9580
- evidence_id: magnetosome-agent-protein-V6F510
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/V6F510.json
  locator: Exact accession/review status, recommended name, primary gene, taxon, FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION comments and their cited evidence; MamJ InterPro cross-reference where
    applicable
  accessed_at: '2026-10-22T01:54:51.327522Z'
  support: supports
  summary: The reviewed entry V6F510 identifies mamB in taxon431944. Localization
    is interpreted at the source-specific location and evidence code, not as proof
    of assembly necessity or exclusive residence.
  snapshot_sha256: 526814c66af4b8bbf66cd0f3399455f2537c025fe9045475737b4e5293e75212
- evidence_id: magnetosome-agent-protein-V6F2B6
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/V6F2B6.json
  locator: Exact accession/review status, recommended name, primary gene, taxon, FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION comments and their cited evidence; MamJ InterPro cross-reference where
    applicable
  accessed_at: '2026-10-22T01:54:51.327132Z'
  support: supports
  summary: The reviewed entry V6F2B6 identifies mamE in taxon431944. Localization
    is interpreted at the source-specific location and evidence code, not as proof
    of assembly necessity or exclusive residence.
  snapshot_sha256: c0857c461389e7e5650d783f3169b2f1b49a835cc405b55421133883164f3e7e
- evidence_id: magnetosome-agent-protein-V6F235
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/V6F235.json
  locator: Exact accession/review status, recommended name, primary gene, taxon, FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION comments and their cited evidence; MamJ InterPro cross-reference where
    applicable
  accessed_at: '2026-10-22T01:54:52.105347Z'
  support: supports
  summary: The reviewed entry V6F235 identifies mamM in taxon431944. Localization
    is interpreted at the source-specific location and evidence code, not as proof
    of assembly necessity or exclusive residence.
  snapshot_sha256: 1e87ed2625ca608d68e069dbff2376d2b08f269da840189abf695e91b2b1c3d6
- evidence_id: magnetosome-agent-protein-Q93DZ1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q93DZ1.json
  locator: Exact accession/review status, recommended name, primary gene, taxon, FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION comments and their cited evidence; MamJ InterPro cross-reference where
    applicable
  accessed_at: '2026-10-22T01:54:51.853654Z'
  support: supports
  summary: The reviewed entry Q93DZ1 identifies mamO in taxon431944. Localization
    is interpreted at the source-specific location and evidence code, not as proof
    of assembly necessity or exclusive residence.
  snapshot_sha256: 3754220ec9946babcb7dd8c36611e5e7e0eefdb0b744cb45f8509112c97d6976
- evidence_id: magnetosome-agent-protein-Q6NE76
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q6NE76.json
  locator: Exact accession/review status, recommended name, primary gene, taxon, FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION comments and their cited evidence; MamJ InterPro cross-reference where
    applicable
  accessed_at: '2026-10-22T01:54:51.904548Z'
  support: supports
  summary: The reviewed entry Q6NE76 identifies mms6 in taxon431944. Localization
    is interpreted at the source-specific location and evidence code, not as proof
    of assembly necessity or exclusive residence.
  snapshot_sha256: 4bdaae8944c2f60830514481d846baf51e91fd39fcb5288d13fab7d526fe52a8
- evidence_id: magnetosome-agent-protein-Q6NE59
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q6NE59.json
  locator: Exact accession/review status, recommended name, primary gene, taxon, FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION comments and their cited evidence; MamJ InterPro cross-reference where
    applicable
  accessed_at: '2026-10-22T01:54:52.069220Z'
  support: supports
  summary: The reviewed entry Q6NE59 identifies mamK in taxon431944. Localization
    is interpreted at the source-specific location and evidence code, not as proof
    of assembly necessity or exclusive residence.
  snapshot_sha256: 12f0f9719e4395404b26dee6039de9834b8d17f6019884b8430479d69502a40c
- evidence_id: magnetosome-agent-protein-V6F519
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/V6F519.json
  locator: Exact accession/review status, recommended name, primary gene, taxon, FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION comments and their cited evidence; MamJ InterPro cross-reference where
    applicable
  accessed_at: '2026-10-22T01:54:52.526287Z'
  support: supports
  summary: The reviewed entry V6F519 identifies mamJ in taxon431944. Localization
    is interpreted at the source-specific location and evidence code, not as proof
    of assembly necessity or exclusive residence.
  snapshot_sha256: 2657edfba0fa2a6bdbb0a1322dac09158b64255ee47545829a25b11b412c0a64
- evidence_id: magnetosome-agent-protein-Q2W8Q7
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q2W8Q7.json
  locator: Exact accession/review status, recommended name, primary gene, taxon, FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION comments and their cited evidence; MamJ InterPro cross-reference where
    applicable
  accessed_at: '2026-10-22T01:54:52.413476Z'
  support: supports
  summary: The reviewed entry Q2W8Q7 identifies mamJ in taxon342108. Localization
    is interpreted at the source-specific location and evidence code, not as proof
    of assembly necessity or exclusive residence.
  snapshot_sha256: ebcc9714aa62e720336a1d0b1ebd4fce22017535ffd137e0786ca76d44227818
- evidence_id: magnetosome-agent-reviewed-uniqueness
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue%20AND%20%28%28organism_id%3A431944%20AND%20%28gene_exact%3AmamA%20OR%20gene_exact%3AmamB%20OR%20gene_exact%3AmamE%20OR%20gene_exact%3AmamM%20OR%20gene_exact%3AmamO%20OR%20gene_exact%3Amms6%20OR%20gene_exact%3AmamK%20OR%20gene_exact%3AmamJ%29%29%20OR%20%28organism_id%3A342108%20AND%20gene_exact%3AmamJ%29%29&format=json&size=100
  locator: Entire returned results for the literal retained URL query, size100; nine
    records
  accessed_at: '2026-10-22T01:54:55.678220Z'
  support: supports
  summary: The bounded exact-gene/taxon reviewed query returns nine entries, one for
    each of the eight named MSR-1 genes and one AMB-1 mamJ. Each returned primary
    gene/taxon was independently compared with the target examples; no broader exclusivity
    is claimed.
  snapshot_sha256: a72bd89facaa4cc2ee75fbf32a07aac5d176273ada312af13e14193aa9776ead
  search_scope: 'Remote UniProtKB query only: reviewed:true AND either organism_id431944
    with gene_exact mamA/mamB/mamE/mamM/mamO/mms6/mamK/mamJ, or organism_id342108
    with gene_exact mamJ; size100; all nine results inspected. Ignored-file coverage
    is not applicable to this remote query; no local absence claim.'
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/magnetosome.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T01:50:55Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/magnetosome.yaml'
  snapshot_sha256: 509c642ec5ba951100f982d6b5bb926ca77a2cd2d3dc0b2bead3760d9ff4951b
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/magnetosome.yaml
    --out /private/tmp/cellstructure-batch31-20261022-ag46a4d4/magnetosome-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T01:50:56Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/magnetosome.yaml\
    \ --out /private/tmp/cellstructure-batch31-20261022-ag46a4d4/magnetosome-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch31-20261022-ag46a4d4/magnetosome-strict.tsv"
  snapshot_sha256: e7e2499dbfff56547c8e2fc2f90463bc6132d75a0bb0b595dca7405a00fc81d6
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/membrane_organelle/magnetosome.yaml
  locator: Exact retained native read-only log
  accessed_at: '2026-10-22T01:56:49.777579Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/magnetosome.yaml
  locator: Exact retained native read-only log
  accessed_at: '2026-10-22T02:00:45.614546Z'
  support: supports
  summary: "data/structures/membrane_organelle/magnetosome.yaml  (GO:0110143)\n  magnetosome_chain_alignment\t\
    mam\tCOVERED\t->mam_proteins (UniProtKB:Q93DY9, UniProtKB:V6F510, UniProtKB:V6F2B6,\
    \ UniProtKB:V6F235, UniProtKB:Q93DZ1, UniProtKB:Q6NE76)\n\ncausal_graphs GENE_OR_PROTEIN\
    \ node summary:\n     1  COVERED                   component_ref target holds\
    \ protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES   \
    \       component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     1  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: 7c62711f405aafe46942c9e80b9c07332fe08abbfbe6c1975d8efa98ca1cf5c4
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/magnetosome.yaml; native collect() exact
    identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '24 of 33 collected target identifiers returned OK. PMID:11571158: UNREACHABLE;
    The bulk transport returned414; the independently retrieved exact MED identity
    confirms PMID11571158, DOI10.1128/aem.67.10.4573-4582.2001 and A large gene cluster
    encoding several magnetosome proteins is conserved in different species of magnetotactic
    bacteria. Scientific scope remains limited to the separately documented inspections.;
    PMID:14766587: UNREACHABLE; The bulk transport returned414; the independently
    retrieved exact MED identity confirms PMID14766587, DOI10.1128/aem.70.2.1040-1050.2004
    and Biochemical and proteomic analysis of the magnetosome membrane in Magnetospirillum
    gryphiswaldense. Scientific scope remains limited to the separately documented
    inspections.; PMID:17601786: UNREACHABLE; The bulk transport returned414; the
    independently retrieved exact MED identity confirms PMID17601786, DOI10.1128/jb.00421-07
    and The acidic repetitive domain of the Magnetospirillum gryphiswaldense MamJ
    protein displays hypervariability but is not required for magnetosome chain assembly.
    Scientific scope remains limited to the separately documented inspections.; PMID:20212111:
    UNREACHABLE; The bulk transport returned414; the independently retrieved exact
    MED identity confirms PMID20212111, DOI10.1073/pnas.0914439107 and Comprehensive
    genetic dissection of the magnetosome gene island reveals the step-wise assembly
    of a prokaryotic organelle. Scientific scope remains limited to the separately
    documented inspections.; PMID:20487281: UNREACHABLE; The bulk transport returned414;
    the independently retrieved exact MED identity confirms PMID20487281, DOI10.1111/j.1365-2958.2010.07202.x
    and Loss of the actin-like protein MamK has pleiotropic effects on magnetosome
    formation and chain assembly in Magnetospirillum gryphiswaldense. Scientific scope
    remains limited to the separately documented inspections.; PMID:22007638: UNREACHABLE;
    The bulk transport returned414; the independently retrieved exact MED identity
    confirms PMID22007638, DOI10.1111/j.1365-2958.2011.07863.x and The cation diffusion
    facilitator proteins MamB and MamM of Magnetospirillum gryphiswaldense have distinct
    and complex functions, and are involved in magnetite biomineralization and magnetosome
    membrane assembly. Scientific scope remains limited to the separately documented
    inspections.; PMID:27481925: UNREACHABLE; The bulk transport returned414; the
    independently retrieved exact MED identity confirms PMID27481925, DOI10.1128/jb.00280-16
    and Comparative Subcellular Localization Analysis of Magnetosome Proteins Reveals
    a Unique Localization Behavior of Mms6 Protein onto Magnetite Crystals. Scientific
    scope remains limited to the separately documented inspections.; cellstructuremech:mamk_filament:
    SKIPPED; The repository-minted identifier uniquely resolves to the frozen maintained
    MamK filament record at data/structures/cytoskeleton/mamk_filament.yaml. An anchored
    hidden/ignored-inclusive corpus search and exact input hash confirm reference
    identity, not all biological assertions.; traitmech:000071: SKIPPED; The exact
    native TraitMech index row resolves traitmech:000071 to magnetosome, morphology
    category. This verifies identifier/label linkage, not the mechanistic meaning
    of a trait. Native source checks are separately scoped; skipped or unreachable
    identifiers are not silently counted as resolved.'
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
  topic: Exact organelle, lumen and membrane boundaries
  outcome: supported
  target_ids:
  - GO:0110143
  summary: The target matches the active GO and UniProt location identities. Native
    hierarchy and parthood distinguish the membrane-enclosed organelle, surrounding
    bilayer and enclosed volume. The whole record’s MICRO cross-reference is identity-level
    context where applicable.
  evidence_ids:
  - record
  - boundaries
  - magnetosome-agent-go
  - magnetosome-agent-SL0510
  - magnetosome-agent-SL0511
  - magnetosome-agent-SL0512
- assessment_id: taxon-scope
  area: scope
  topic: Native taxonomy and experimental conditions
  outcome: supported
  target_ids:
  - GO:0110143
  summary: Taxon identities and model strains are correct, including the current Paramagnetospirillum
    name for AMB-1 where present. Source experiments are assigned to MSR-1 or AMB-1,
    not exported as identical gene requirements across all bacteria. RARE/VARIABLE
    are broad qualitative occurrence statements, not a quantitative survey. The whole-record
    Archaea absence assertion is assessed separately as unknown.
  evidence_ids:
  - record
  - magnetosome-agent-tax28211
  - magnetosome-agent-tax1236
  - magnetosome-agent-tax2157
  - magnetosome-agent-tax431944
  - magnetosome-agent-tax342108
  - magnetosome-agent-uebe2016-publisher
  - magnetosome-agent-uebe2016-meta
  - magnetosome-agent-barber2015-pmc
  - magnetosome-agent-barber2015-meta
  - magnetosome-agent-grunberg2004-pmc
  - magnetosome-agent-PMID11571158
  - magnetosome-agent-PMID14766587
  - magnetosome-agent-PMID17601786
  - magnetosome-agent-PMID20212111
  - magnetosome-agent-PMID20487281
  - magnetosome-agent-PMID22007638
  - magnetosome-agent-PMID27481925
  - magnetosome-agent-grunberg2001-pmc
  - magnetosome-agent-murat2010-correct-pmc
  - magnetosome-agent-scheffel2007-pmc
  - magnetosome-agent-arakaki2016-pmc
- assessment_id: composition
  area: grounding
  topic: Material, mineral alternatives and protein cohort
  outcome: concern
  target_ids:
  - GO:0110143
  summary: The membrane material, Mam/Mms cohort and separate MamK/MamJ associated
    machinery have source support. No single family is forced onto the multifamily
    cohort. The membrane row is interpreted as generic boundary material without an
    asserted chemical CURIE; it would benefit from explicit material wording, but
    no unsupported whole-GO molecular grounding is present. Magnetite and greigite
    are distinct alternatives, making the universal magnetite essentiality assertion
    a concrete concern in F1.
  evidence_ids:
  - record
  - policy
  - magnetosome-agent-go
  - magnetosome-agent-chebi46726
  - magnetosome-agent-chebi86238
  - magnetosome-agent-chebi18248
  - magnetosome-agent-barber2015-pmc
  - magnetosome-agent-grunberg2004-pmc
  - magnetosome-agent-IPR060787
- assessment_id: formation-necessity
  area: grounding
  topic: Grouped necessity versus individual requirements
  outcome: unknown
  target_ids:
  - GO:0110143
  summary: Murat and Uebe distinguish membrane-formation defects from biomineralization
    defects, with redundancy and strain dependence. A collective Mam/Mms ESSENTIAL
    row is not expanded into a claim that every listed member is independently necessary.
    Exact formation necessity for the complete taxon-agnostic cohort remains unresolved;
    no new per-protein necessity finding is inferred from dispensable members. A bilayer
    is constitutive of the named membrane-bounded class.
  evidence_ids:
  - record
  - policy
  - magnetosome-agent-murat2010-correct-pmc
  - magnetosome-agent-PMID22007638
  - magnetosome-agent-barber2015-pmc
- assessment_id: proteins
  area: grounding
  topic: Nine accessions, family and localization evidence
  outcome: concern
  target_ids:
  - GO:0110143
  summary: All nine reviewed example identities, gene/taxon pairs and native evidence
    annotations match. MamJ family IPR060787 matches both examples. Direct biochemical
    localization, fluorescence localization and two-hybrid interaction are not conflated.
    The current six Mam/Mms examples each retain experimental localization annotations,
    contrary to the still-open present-tense localization-gap discussion addressed
    in F3.
  evidence_ids:
  - record
  - magnetosome-agent-IPR060787
  - magnetosome-agent-reviewed-uniqueness
  - magnetosome-agent-protein-Q93DY9
  - magnetosome-agent-protein-V6F510
  - magnetosome-agent-protein-V6F2B6
  - magnetosome-agent-protein-V6F235
  - magnetosome-agent-protein-Q93DZ1
  - magnetosome-agent-protein-Q6NE76
  - magnetosome-agent-protein-Q6NE59
  - magnetosome-agent-protein-V6F519
  - magnetosome-agent-protein-Q2W8Q7
  - magnetosome-agent-grunberg2001-pmc
  - magnetosome-agent-grunberg2004-pmc
  - magnetosome-agent-murat2010-correct-pmc
  - magnetosome-agent-scheffel2007-pmc
  - magnetosome-agent-arakaki2016-pmc
- assessment_id: function-graph
  area: graph
  topic: Chain function and transported chemical identity
  outcome: concern
  target_ids:
  - GO:0110143
  summary: The graph provides a source-backed overview of invagination, mineralization
    and chain-dependent magnetic alignment, rather than exact kinetics or a reconstituted
    pathway. MamK phenotypes differ between MSR-1 and AMB-1; the broad scatter shorthand
    is not a claim that every mutant particle is isolated. MamJ linkage is supported
    with the stated interaction-model limits; F4 separately qualifies the graph note
    describing the deletion phenotype. The exact neutral iron atom actor in its transport/mineralization
    edges is inconsistent with the source-described ion substrate, as bounded in F2.
  evidence_ids:
  - record
  - graph-policy
  - magnetosome-agent-chebi46726
  - magnetosome-agent-chebi86238
  - magnetosome-agent-chebi18248
  - magnetosome-agent-barber2015-pmc
  - magnetosome-agent-murat2010-correct-pmc
  - magnetosome-agent-scheffel2007-pmc
  - magnetosome-agent-PMID20487281
- assessment_id: archaea-absence
  area: scope
  topic: Unverified literature-absence attribution
  outcome: unknown
  target_ids:
  - GO:0110143
  summary: ENA verifies Archaea identity but cannot establish the biological absence
    statement. The readable Uebe2016 Key Points/Abstract do not independently establish
    that no magnetotactic archaeon has been described, and no exhaustive contemporary
    search was performed. This assertion remains unverified rather than confirmed
    or refuted.
  evidence_ids:
  - record
  - magnetosome-agent-uebe2016-publisher
  - magnetosome-agent-uebe2016-meta
  - magnetosome-agent-tax28211
  - magnetosome-agent-tax1236
  - magnetosome-agent-tax2157
  - magnetosome-agent-tax431944
  - magnetosome-agent-tax342108
- assessment_id: trait-size
  area: scope
  topic: Trait linkage and size range access limit
  outcome: unknown
  target_ids:
  - GO:0110143
  summary: TraitMech000071 resolves to magnetosome and the chain’s orientation role
    is supported. UO0000018 resolves to nanometer. The exact35–120nm DIAMETER statement
    was not verified against the unread Uebe main body; the inspected independent
    review gives an approximate30–120nm crystal-size range. This remains an access/measurement-convention
    limitation, not proof the record’s range is false.
  evidence_ids:
  - record
  - magnetosome-agent-trait-index
  - magnetosome-agent-uo0000018
  - magnetosome-agent-uebe2016-publisher
  - magnetosome-agent-barber2015-pmc
- assessment_id: completeness
  area: completeness
  topic: Complete target with bounded optional enrichments
  outcome: supported
  target_ids:
  - GO:0110143
  summary: Every target field, source placement, history and discussion was inspected.
    No tracked image asset or verbatim snippet is asserted. Generic membrane lipid
    chemistry, optional inventories and historical image/TODO searches are not automatic
    defects. Local boundary records and the MamK record where applicable are frozen
    context only.
  evidence_ids:
  - record
  - policy
  - magnetosome-agent-go
  - magnetosome-agent-uebe2016-publisher
  - magnetosome-agent-uebe2016-meta
  - magnetosome-agent-barber2015-pmc
  - magnetosome-agent-barber2015-meta
  - magnetosome-agent-grunberg2004-pmc
  - magnetosome-agent-PMID11571158
  - magnetosome-agent-PMID14766587
  - magnetosome-agent-PMID17601786
  - magnetosome-agent-PMID20212111
  - magnetosome-agent-PMID20487281
  - magnetosome-agent-PMID22007638
  - magnetosome-agent-PMID27481925
  - magnetosome-agent-grunberg2001-pmc
  - magnetosome-agent-murat2010-correct-pmc
  - magnetosome-agent-scheffel2007-pmc
  - magnetosome-agent-arakaki2016-pmc
findings:
- finding_id: F1
  issue_key: magnetosome-magnetite-universal-necessity
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Qualify magnetite necessity for alternative-mineral magnetosomes
  description: The component specifically denotes magnetite CHEBI46726 and is ESSENTIAL,
    but both the target definition/role and the inspected review explicitly allow
    greigite instead. Essentiality means the structure cannot form without that component;
    a magnetite-only requirement therefore excludes an acknowledged valid mineral
    alternative. This does not concern merely incomplete vesicle precursors or individual
    Mam-protein necessity.
  target_ids:
  - GO:0110143
  field_paths:
  - components#magnetite.essentiality
  evidence_ids:
  - record
  - policy
  - magnetosome-agent-chebi46726
  - magnetosome-agent-chebi86238
  - magnetosome-agent-barber2015-pmc
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/magnetosome.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:claim support, exact grounding
    and internal consistency
  native_severity: major
  normalization_reason: Major material scope contradiction between an unconditional
    structure-formation requirement and an explicitly acknowledged alternative constituent.
- finding_id: F2
  issue_key: magnetosome-neutral-iron-transport-actor
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Use an ion-compatible identity for transported iron
  description: The CHEMICAL node is explicitly labelled iron atom and grounded to
    CHEBI18248, whose native charge annotation is0. It is the object of transporter
    action and source of mineralization, while the inspected review and primary context
    describe iron/metal-ion transport. A neutral atom identity is not a charge-unspecified
    iron-ion substrate. The finding does not prescribe a single oxidation state or
    prove a detailed MamB/MamM transport mechanism.
  target_ids:
  - GO:0110143
  field_paths:
  - causal_graphs#magnetosome_chain_alignment.nodes#iron
  - causal_graphs#magnetosome_chain_alignment.edges[1].object
  - causal_graphs#magnetosome_chain_alignment.edges[2].subject
  evidence_ids:
  - record
  - policy
  - graph-policy
  - magnetosome-agent-chebi18248
  - magnetosome-agent-barber2015-pmc
  - magnetosome-agent-murat2010-correct-pmc
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/magnetosome.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:claim support, exact grounding
    and internal consistency
  native_severity: major
  normalization_reason: 'Major exact chemical-actor mismatch: a neutral atomic species
    is formally assigned a source-supported ion-transport role; the general fact of
    iron supply is not disputed.'
- finding_id: F3
  issue_key: magnetosome-localization-gap-current-example-conflict
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  title: Update the open localization-gap interpretation
  description: The open discussion currently says most magnetosome proteins have no
    experimental UniProt localization support and that only MamJ produced an example.
    The same maintained target now contains six Mam/Mms examples with the source-specific
    ECO0000269 localization annotations verified in current native records and supported
    by the inspected primary studies. The old SL0510 query may have been accurate
    at its recorded scope; the error is leaving its broad present-tense interpretation
    as an unresolved current gap.
  target_ids:
  - GO:0110143
  field_paths:
  - discussions#localisation_evidence_is_thin
  evidence_ids:
  - record
  - magnetosome-agent-protein-Q93DY9
  - magnetosome-agent-protein-V6F510
  - magnetosome-agent-protein-V6F2B6
  - magnetosome-agent-protein-V6F235
  - magnetosome-agent-protein-Q93DZ1
  - magnetosome-agent-protein-Q6NE76
  - magnetosome-agent-protein-Q6NE59
  - magnetosome-agent-protein-V6F519
  - magnetosome-agent-protein-Q2W8Q7
  - magnetosome-agent-grunberg2001-pmc
  - magnetosome-agent-grunberg2004-pmc
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/magnetosome.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:claim support, exact grounding
    and internal consistency
  native_severity: minor
  normalization_reason: Minor stale current interpretation; no historical query count,
    retrieval date or genuine biological knowledge gap is declared false.
- finding_id: F4
  issue_key: magnetosome-mamj-deletion-phenotype-wording
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Distinguish MamJ-deficient clustering from scattering
  description: The evidence note on the MamK-aligns-chain edge says mamJ deletion
    scatters magnetosomes. The inspected MSR-1 primary experiment reports predominantly
    aggregated clusters, occasional rings or imperfect short chains, and altered particle
    segregation. Its supported conclusion is loss of normal linear organization, not
    a uniform dispersed-particle phenotype. This does not refute MamJ-dependent attachment
    or the graph alignment edge.
  target_ids:
  - GO:0110143
  field_paths:
  - causal_graphs#magnetosome_chain_alignment.edges[3].evidence[0].notes
  evidence_ids:
  - record
  - magnetosome-agent-scheffel2007-pmc
  - magnetosome-agent-barber2015-pmc
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/magnetosome.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:claim support, exact grounding
    and internal consistency
  native_severity: minor
  normalization_reason: Minor source/phenotype wording overstatement; the overall
    chain-organization mechanism and associated-machinery status remain supported.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0110143
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/magnetosome.yaml
    role: maintained scientific record
  description: In separately authorized curation, condition magnetite necessity on
    magnetite-producing lineages or represent the supported magnetic-mineral alternatives
    without asserting universal magnetite dependence. Preserve exact chemical identities
    and avoid claiming greigite is a subtype of magnetite.
  acceptance_checks:
  - Retain source-specific organism, condition and chemical identity boundaries.
  - Confirm the amended assertion matches the frozen essentiality/grounding contracts.
  - Run focused native schema, strict and graph checks after separately authorized
    scientific curation.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0110143
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/magnetosome.yaml
    role: maintained scientific record
  description: In separately authorized curation, identify the transported iron at
    the ionic scope actually supported by the source, using verified appropriate chemistry
    grounding or a bounded label if oxidation-state specificity remains unresolved.
    Keep the downstream mineral identity distinct.
  acceptance_checks:
  - Retain source-specific organism, condition and chemical identity boundaries.
  - Confirm the amended assertion matches the frozen essentiality/grounding contracts.
  - Run focused native schema, strict and graph checks after separately authorized
    scientific curation.
- action_id: A3
  finding_ids:
  - F3
  target_ids:
  - GO:0110143
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/magnetosome.yaml
    role: maintained scientific record
  description: In separately authorized curation, preserve the historical query result
    but update or resolve the present-tense discussion to distinguish whole-magnetosome
    SL0510 from membrane SL0512 annotations and the current experimentally supported
    examples.
  acceptance_checks:
  - Retain source-specific organism, condition and chemical identity boundaries.
  - Confirm the amended assertion matches the frozen essentiality/grounding contracts.
  - Run focused native schema, strict and graph checks after separately authorized
    scientific curation.
- action_id: A4
  finding_ids:
  - F4
  target_ids:
  - GO:0110143
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/magnetosome.yaml
    role: maintained scientific record
  description: In separately authorized curation, describe the loss of normal linear
    organization and the source-specific MSR-1 clustering phenotype, and preserve
    distinctions from MamK mutants and AMB-1 genetic redundancy.
  acceptance_checks:
  - Retain source-specific organism, condition and chemical identity boundaries.
  - Confirm the amended assertion matches the frozen essentiality/grounding contracts.
  - Run focused native schema, strict and graph checks after separately authorized
    scientific curation.
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- The fresh target-resolver slice and all five corpus receipt/manifest checks are
  integrated in this completed review.
- Uebe2016 publisher and nominal-PDF responses contain Key Points/Abstract and access
  options, not a complete main body. Uebe2011 is native abstract only; its publisher
  response is403. No unread source passage is certified.
- The Barber review is secondary authority. Its complete scientific main body was
  read, as were Grünberg2004 Methods/Results/Discussion. No paper image pixels, supplements
  or raw assay data were inspected.
- Strain-specific mutants, membrane formation, crystal formation and chain organization
  remain distinct. Collective constituents are not taken as proof that every individual
  member is required for structure formation.
- Qualitative taxon occurrence and literature-bounded absence are not an exhaustive
  contemporary prevalence survey. Historical retrieval/search statements are not re-certified
  or declared false merely because newer evidence exists.
- Grünberg2001, Murat2010 and Scheffel2007 Methods/Results/Discussion and Arakaki2016
  Introduction/Methods/Results/Discussion were read, including main captions/tables.
  Murat/Scheffel unsectioned introductions, all supplements and all figure pixels
  were not inspected. Katzmann2010 remains complete native abstract only.
- The failed guessed Murat numeric-PMC locator returned an unrelated insulin article;
  it is retained as rejected access evidence, never used scientifically. The correct
  PMC2851823 body is separately retained.
- The exact35–120nm diameter range remains unverified against the unread Uebe body;
  the independent review supplies an approximate30–120nm crystal-size range. MamB/MamM
  transport details and MamJ linkage retain the qualification of the cited experiments/models.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User explicitly authorizes one review per uncovered record, including clean pass_with_limitations,
  overriding the local issue-only output restriction.
- Only unsaved support/review artifacts are written outside the maintained repository;
  no scientific record, save/index, Git or publication mutation.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
