# Bacterial-type flagellum: evidence and scope audit

- Review: 20261010T201901Z-flagellum-whole
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-10T20:03:37Z
- Finished UTC: 2026-10-10T20:19:01Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Issue-bearing claim-level audit of this record. All sections inspected, but the diameter citation remains unverified; this is not complete scientific coverage.

## Scope And Provenance

Single maintained structure, all present fields and both history surfaces. No native edits, generators or GitHub mutations.

Selection: Next sequential unassessed target in the all-record operational worklist: data/structures/appendage/bacterial_type_flagellum.yaml
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 49e9ce6b5cbdabce9787d1f51ff09702f306eb61.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0009288 | data/structures/appendage/bacterial_type_flagellum.yaml | maintained | bacterial-type flagellum |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Fresh focused schema | passed | True | GO:0009288 | The unchanged target passed. |
| Fresh focused strict | passed | True | GO:0009288 | The unchanged target passed. |
| subtiwiki verification | passed | True | GO:0009288 | Dry run verified all 17 curated SubtiWiki/UniProt outlinks; no --apply and no native write. |
| traits verification | passed | True | GO:0009288 | Live published index contains 477 traits; all 10 corpus links match. This target has two links. |
| ci verification | passed | True | GO:0009288 | Reused successful exact-revision CI at 49e9ce6b: full QC 38081538245, labels 38081538303, identifier-liveness 38081538327, vendored sync 38081538243, merge integrity 38081538330. Native inputs are unchanged; not newly executed local full QC. |
| Verify diameter at its attached reference | unavailable | True | GO:0009288 | The source abstract does not contain the diameter and the tried publisher full-text routes were inaccessible. This preserves partial completion; access failure alone is not a finding. |

## Scientific And Domain Assessments

### Identity, hierarchy and boundary

identity: supported. Targets: GO:0009288.

The record denotes the bacterial flagellum, with filament, cap, junction, hook and basal body as named parts; archaella and cilia are distinguished. The conventional bacterial-flagellum synonym is equivalent although not listed as a current GO exact synonym.

### Every component, assembly essentiality and quantities

evidence: concern. Targets: GO:0009288.

Membership, MS-ring scaffold, axial rod, LP bushing, five-protein membrane gate and dispensable stator are supported. C-ring ESSENTIAL needs a condition-bound assembly qualification. Approximate flagellin count and nonuniversal protofilament count retain explicit evidence caveats; the hook is not replaced by its broader rod/hook family.

### Both distribution rows and canonical examples

scope: concern. Targets: GO:0009288.

Examples and the bacterial/archaellum distinction are supported. COMMON means most members under the native schema, stronger than the evidence supports; VARIABLE is the conservative correction.

### Protein examples and family decisions

grounding: supported. Targets: GO:0009288.

Twenty examples retain verified accession/gene/taxon identities; all 17 SubtiWiki mappings pass dry-run checks, including historical FlgE/FlgG and MotP/MotS aliases. FliY replacement is documented. FlgE broad-family rejection remains justified for the two inspected UniProt entries.

### Physical properties and exact source support

quantity: concern. Targets: GO:0009288.

Length lower bound is explicitly unsourced. Rotation-speed context and units are supported, with no hard low-load maximum inferred. The approximate diameter remains unverified at Macnab 2003; this required check keeps the review partial.

### Hosted TEM image and attribution

provenance: supported. Targets: GO:0009288.

Local bitmap visually inspected; cell and peritrichous filaments are visible. Hashes, public-domain metadata, photographer/provider, original CDC source and depicted O157:H7 taxon agree. No new measurement is inferred from the colorized image.

### Functions and every causal edge

graph: concern. Targets: GO:0009288.

All five edges checked: ion input, stator/FliG torque, coupled rotor rotation, hook transmission and propulsion. The PMF node improperly includes sodium flux, and proposed stator rotation is promoted to unqualified mechanism.

### Discussions, lifecycle and optional fields

provenance: concern. Targets: GO:0009288.

PROPOSED and append-only history are appropriate. No optional absent image, dataset, trait, pathway or composition field is treated as a defect. The grounding TODO still asks to assign an already assigned flagellin family and to redo an already documented hook decision.

## Findings

### F1: Remove or source the 5-micrometer lower bound

major / open / confirmed; issue key: bacterial-flagellum-length-lower-bound.

physical_properties[1] states 5-20 micrometers while its own evidence says the lower bound is unsourced. The inspected cited section supports up to 20, not a minimum of 5.

### F2: Keep proposed stator rotation labeled as a model

major / open / confirmed; issue key: bacterial-flagellum-stator-model-evidence-strength.

The prose asserts MotA/PomA-subunit rotation as an established mechanical step. The cited 2020 structural studies propose this trajectory; Deme also permits an oscillating ratchet. Preserve the resolved A5B2 architecture and experimentally supported torque coupling without upgrading the dynamic model.

### F3: Distinguish proton and sodium motive forces

major / open / confirmed; issue key: bacterial-flagellum-pmf-sodium-conflation.

The graph source node is proton motive force, but its outgoing description includes sodium flux. The source distinguishes ion-specific gradients; sodium-driven motors cannot be encoded as proton-driven merely because both are ion powered.

### F4: Use a supported bacterial prevalence category

major / open / confirmed; issue key: bacterial-flagellum-bacterial-presence-common.

COMMON encodes presence in most bacteria, while the note is only conditional/widespread. The inspected genomic survey does not support a majority. Use VARIABLE with its evidence limits.

### F5: Qualify C-ring assembly essentiality

major / open / confirmed; issue key: bacterial-flagellum-c-ring-assembly-condition.

Unqualified ESSENTIAL omits the experimentally demonstrated FliI-overproduction bypass. Encode condition-dependent assembly, preserving mutant and partial-structure scope and the lack of restored motility.

### F6: Narrow the completed portions of the grounding TODO

minor / open / confirmed; issue key: bacterial-flagellum-grounding-todo-stale.

The open prompt still requests a flagellin grounding already supplied as IPR001492 and repeats a FlgE decision already documented in grounding_notes. This directs future curation toward completed work.

## Recommended Actions And Acceptance Checks

### A1

Remove or source the 5-micrometer lower bound

- Use only a source-supported range or upper bound, with organism/measurement context; do not infer a minimum from an upper limit.
- Use guarded writer and append both histories; preserve PROPOSED and unrelated content. Run strict, labels, traits, history, QC and review-contract gates.

### A2

Keep proposed stator rotation labeled as a model

- Qualify the dynamic model in the claim-bearing description itself, or attach and inspect primary evidence that directly establishes that stronger claim. Do not imply that stator torque or A5B2 stoichiometry is merely hypothetical.
- Use guarded writer and append both histories; preserve PROPOSED and unrelated content. Run strict, labels, traits, history, QC and review-contract gates.

### A3

Distinguish proton and sodium motive forces

- Use ion motive force with explicit ion-coupling scope, or split proton and sodium branches. Preserve the verified stator variants.
- Use guarded writer and append both histories; preserve PROPOSED and unrelated content. Run strict, labels, traits, history, QC and review-contract gates.

### A4

Use a supported bacterial prevalence category

- Preserve patchy taxon/strain scope; do not turn a genomic proxy into direct observation or absence proof.
- Use guarded writer and append both histories; preserve PROPOSED and unrelated content. Run strict, labels, traits, history, QC and review-contract gates.

### A5

Qualify C-ring assembly essentiality

- Prefer CONDITIONAL with explicit bypass context. Do not equate defective flagella with a functional motor or automatically reclassify every component of the separate C-ring record.
- Use guarded writer and append both histories; preserve PROPOSED and unrelated content. Run strict, labels, traits, history, QC and review-contract gates.

### A6

Narrow the completed portions of the grounding TODO

- Narrow the prompt to remaining unresolved components; preserve posed_date and original rationale, appending current notes rather than deleting provenance.
- Use guarded writer and append both histories; preserve PROPOSED and unrelated content. Run strict, labels, traits, history, QC and review-contract gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/bacterial_type_flagellum.yaml; Entire YAML; native schema enums; append-only histories; full hidden/ignored review search | context_only | Input hashes captured before assessment; all present sections and history entries read; status PROPOSED retained. No earlier structured bundle for this target found in the searched reviews/reports roots, including ignored files. |
| paper-00 | DOI:10.1016/0022-2836(92)90958-m; Primary abstract | supports | Salmonella assembly intermediates establish autonomous MS-ring formation and cooperative FliE/FlgB/FlgC/FlgF/FlgG rod assembly. |
| paper-01 | DOI:10.1016/j.cell.2020.08.016; Primary abstract; author PDF pp. 251-253, rotational model and bidirectional rotation sections | supports | A5B2 architecture is experimentally resolved; detailed torque steps are proposed from structures and functional data, not directly filmed stator rotation. |
| paper-03 | DOI:10.1016/j.jmb.2005.07.030; Primary abstract | supports | B. subtilis MotAB and MotPS have distinct H+/Na+ coupling; stator-deficient cells retain flagella. Supports the curated MotP/MotS placements. |
| paper-04 | DOI:10.1016/j.tim.2014.12.011; Review abstract only | supports | The cited review covers conserved MS ring, C ring, rod and export apparatus, ion-powered motors, and Salmonella/Vibrio structural diversity; detailed unseen text is not certified. |
| paper-07 | DOI:10.1038/nrmicro1887; Review abstract only | supports | The article concerns coupling flagellar gene regulation and assembly in Gram-negative bacteria; its abstract is not a denominator-bearing bacterial prevalence survey. |
| paper-08 | DOI:10.1038/s41467-021-24507-9; Primary full text: introduction, native MS/C-ring results, Fig. 1, discussion and strain methods | supports | Native Salmonella MS ring has 34 FliF subunits in the studied preparation; C-ring symmetry varies. MS-ring scaffold and export-gate housing are supported. |
| paper-10 | DOI:10.1038/s41564-020-0788-8; Primary full text: stator architecture, Coupling of ion-flow to flagellar rotation, discussion and methods | supports | A5B2 structures support torque models. The authors explicitly allow either processive rotation or oscillating ratchet motion; geometry does not directly establish one dynamic trajectory. |
| paper-12 | DOI:10.1038/s41598-019-51440-1; Primary full text: introduction and Kurthia filament results | supports | Supports the recorded 11-protofilament statement together with its explicit Campylobacter exception; the exception is already retained in native evidence notes. |
| paper-16 | DOI:10.1093/nar/gkae957; Source-database paper abstract | supports | SubtiWiki is the maintained B. subtilis reference resource with an API. Individual protein outlinks were separately verified by the repository dry-run adapter. |
| paper-18 | DOI:10.1128/jb.00626-18; Primary abstract | supports | B. subtilis uses FliY in place of FliN and reverses the CheY-P rotational response relative to E. coli. The native record already acknowledges the lineage variant. |
| paper-19 | DOI:10.1128/jb.00353-25; Primary full text: introduction and motor-load paragraph | supports | The quoted source gives about 125 Hz with filament/high load and 300 Hz or faster at low load; the native context preserves these conditions. The approximate summary range is not a hard maximum. |
| paper-20 | DOI:10.1128/jcm.26.7.1367-1372.1988; Primary abstract | supports | Purification, TEM, H7 immunoassay and immunogold characterize O157:H7 strain CL-56 flagellin; supports the bounded taxon example, not identification of the separate CDC specimen. |
| paper-22 | DOI:10.1146/annurev.biochem.72.121801.161737; Review abstract only | supports | E. coli swimming uses reversible ion-driven motors and helical filaments; supports the broad definition, function and swimming edges, not a precise filament diameter. |
| paper-23 | DOI:10.1146/annurev.micro.57.030502.090832; Review abstract only | supports | Axial proteins are exported by a flagellar type III pathway and assemble distally. Its accessible abstract does not verify the native ~20 nm diameter. |
| paper-24 | DOI:10.3389/fmicb.2015.00023; Review full text: historical structural comparison and archaellum distinction | supports | Archaella have a distinct type-IV-filament-related architecture, not the bacterial flagellar apparatus; supports the bounded structural distinction, not an exhaustive new archaeal survey. |
| paper-25 | DOI:10.3390/biom11020186; Review full text: core export gate and Model for High-Speed Secretion of Flagellin | supports | The source states about 20,000 flagellin subunits and growth up to 20 micrometers; it does not establish a 5-micrometer minimum. Export-gate composition and FliK context are corroborated. |
| paper-26 | DOI:10.7554/elife.48979; Primary full text: stator-deletion results, Fig. 1, tomography comparison | supports | Borrelia motA/motB mutants retain paralyzed flagella and motor substructures; supports assembly dispensability of the stator, not normal motor function. |
| go-0009288 | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0009288; Exact OLS GO identifier, definition, synonyms, obsolete flag | supports | Exact active structure or process identity checked. GO:0120101 retains an outdated A4B2 definition upstream; the native record does not adopt that stoichiometry. |
| go-0009420 | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0009420; Exact OLS GO identifier, definition, synonyms, obsolete flag | supports | Exact active structure or process identity checked. GO:0120101 retains an outdated A4B2 definition upstream; the native record does not adopt that stoichiometry. |
| go-0009421 | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0009421; Exact OLS GO identifier, definition, synonyms, obsolete flag | supports | Exact active structure or process identity checked. GO:0120101 retains an outdated A4B2 definition upstream; the native record does not adopt that stoichiometry. |
| go-0009422 | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0009422; Exact OLS GO identifier, definition, synonyms, obsolete flag | supports | Exact active structure or process identity checked. GO:0120101 retains an outdated A4B2 definition upstream; the native record does not adopt that stoichiometry. |
| go-0009424 | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0009424; Exact OLS GO identifier, definition, synonyms, obsolete flag | supports | Exact active structure or process identity checked. GO:0120101 retains an outdated A4B2 definition upstream; the native record does not adopt that stoichiometry. |
| go-0009425 | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0009425; Exact OLS GO identifier, definition, synonyms, obsolete flag | supports | Exact active structure or process identity checked. GO:0120101 retains an outdated A4B2 definition upstream; the native record does not adopt that stoichiometry. |
| go-0071973 | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0071973; Exact OLS GO identifier, definition, synonyms, obsolete flag | supports | Exact active structure or process identity checked. GO:0120101 retains an outdated A4B2 definition upstream; the native record does not adopt that stoichiometry. |
| ipr001492 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001492/; InterPro metadata accession/name/type/description | supports | Family identity inspected; FliN entry explicitly notes the longer FliY form. Family/domain overlap is not proof that whole proteins are equivalent. |
| ipr012835 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012835/; InterPro metadata accession/name/type/description | supports | Family identity inspected; FliN entry explicitly notes the longer FliY form. Family/domain overlap is not proof that whole proteins are equivalent. |
| ipr020013 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020013/; InterPro metadata accession/name/type/description | supports | Family identity inspected; FliN entry explicitly notes the longer FliY form. Family/domain overlap is not proof that whole proteins are equivalent. |
| p02968 | https://rest.uniprot.org/uniprotkb/P02968.json; Reviewed status, recommended name, genes, taxon, InterPro matches and localization annotations | supports | Accession, gene and taxon match the native protein example. Identity-only examples remain identity-only; source annotation is not upgraded to direct localization. |
| p06179 | https://rest.uniprot.org/uniprotkb/P06179.json; Reviewed status, recommended name, genes, taxon, InterPro matches and localization annotations | supports | Accession, gene and taxon match the native protein example. Identity-only examples remain identity-only; source annotation is not upgraded to direct localization. |
| p52616 | https://rest.uniprot.org/uniprotkb/P52616.json; Reviewed status, recommended name, genes, taxon, InterPro matches and localization annotations | supports | Accession, gene and taxon match the native protein example. Identity-only examples remain identity-only; source annotation is not upgraded to direct localization. |
| p0a1j1 | https://rest.uniprot.org/uniprotkb/P0A1J1.json; Reviewed status, recommended name, genes, taxon, InterPro matches and localization annotations | supports | Accession, gene and taxon match the native protein example. Identity-only examples remain identity-only; source annotation is not upgraded to direct localization. |
| p23447 | https://rest.uniprot.org/uniprotkb/P23447.json; Reviewed status, recommended name, genes, taxon, InterPro matches and localization annotations | supports | Accession, gene and taxon match the native protein example. Identity-only examples remain identity-only; source annotation is not upgraded to direct localization. |
| p23448 | https://rest.uniprot.org/uniprotkb/P23448.json; Reviewed status, recommended name, genes, taxon, InterPro matches and localization annotations | supports | Accession, gene and taxon match the native protein example. Identity-only examples remain identity-only; source annotation is not upgraded to direct localization. |
| p23453 | https://rest.uniprot.org/uniprotkb/P23453.json; Reviewed status, recommended name, genes, taxon, InterPro matches and localization annotations | supports | Accession, gene and taxon match the native protein example. Identity-only examples remain identity-only; source annotation is not upgraded to direct localization. |
| p24073 | https://rest.uniprot.org/uniprotkb/P24073.json; Reviewed status, recommended name, genes, taxon, InterPro matches and localization annotations | supports | Accession, gene and taxon match the native protein example. Identity-only examples remain identity-only; source annotation is not upgraded to direct localization. |
| p28611 | https://rest.uniprot.org/uniprotkb/P28611.json; Reviewed status, recommended name, genes, taxon, InterPro matches and localization annotations | supports | Accession, gene and taxon match the native protein example. Identity-only examples remain identity-only; source annotation is not upgraded to direct localization. |
| p28612 | https://rest.uniprot.org/uniprotkb/P28612.json; Reviewed status, recommended name, genes, taxon, InterPro matches and localization annotations | supports | Accession, gene and taxon match the native protein example. Identity-only examples remain identity-only; source annotation is not upgraded to direct localization. |
| p39063 | https://rest.uniprot.org/uniprotkb/P39063.json; Reviewed status, recommended name, genes, taxon, InterPro matches and localization annotations | supports | Accession, gene and taxon match the native protein example. Identity-only examples remain identity-only; source annotation is not upgraded to direct localization. |
| p39064 | https://rest.uniprot.org/uniprotkb/P39064.json; Reviewed status, recommended name, genes, taxon, InterPro matches and localization annotations | supports | Accession, gene and taxon match the native protein example. Identity-only examples remain identity-only; source annotation is not upgraded to direct localization. |
| p23446 | https://rest.uniprot.org/uniprotkb/P23446.json; Reviewed status, recommended name, genes, taxon, InterPro matches and localization annotations | supports | Accession, gene and taxon match the native protein example. Identity-only examples remain identity-only; source annotation is not upgraded to direct localization. |
| p24500 | https://rest.uniprot.org/uniprotkb/P24500.json; Reviewed status, recommended name, genes, taxon, InterPro matches and localization annotations | supports | Accession, gene and taxon match the native protein example. Identity-only examples remain identity-only; source annotation is not upgraded to direct localization. |
| p24501 | https://rest.uniprot.org/uniprotkb/P24501.json; Reviewed status, recommended name, genes, taxon, InterPro matches and localization annotations | supports | Accession, gene and taxon match the native protein example. Identity-only examples remain identity-only; source annotation is not upgraded to direct localization. |
| p35620 | https://rest.uniprot.org/uniprotkb/P35620.json; Reviewed status, recommended name, genes, taxon, InterPro matches and localization annotations | supports | Accession, gene and taxon match the native protein example. Identity-only examples remain identity-only; source annotation is not upgraded to direct localization. |
| p35538 | https://rest.uniprot.org/uniprotkb/P35538.json; Reviewed status, recommended name, genes, taxon, InterPro matches and localization annotations | supports | Accession, gene and taxon match the native protein example. Identity-only examples remain identity-only; source annotation is not upgraded to direct localization. |
| p35528 | https://rest.uniprot.org/uniprotkb/P35528.json; Reviewed status, recommended name, genes, taxon, InterPro matches and localization annotations | supports | Accession, gene and taxon match the native protein example. Identity-only examples remain identity-only; source annotation is not upgraded to direct localization. |
| p35535 | https://rest.uniprot.org/uniprotkb/P35535.json; Reviewed status, recommended name, genes, taxon, InterPro matches and localization annotations | supports | Accession, gene and taxon match the native protein example. Identity-only examples remain identity-only; source annotation is not upgraded to direct localization. |
| p35537 | https://rest.uniprot.org/uniprotkb/P35537.json; Reviewed status, recommended name, genes, taxon, InterPro matches and localization annotations | supports | Accession, gene and taxon match the native protein example. Identity-only examples remain identity-only; source annotation is not upgraded to direct localization. |
| taxon-2 | https://rest.uniprot.org/taxonomy/2.json; Active taxonomy identity, rank and parent | supports | Authority identity and exemplar/lineage relationship inspected; authority metadata is not experimental evidence of occurrence. |
| taxon-2157 | https://rest.uniprot.org/taxonomy/2157.json; Active taxonomy identity, rank and parent | supports | Authority identity and exemplar/lineage relationship inspected; authority metadata is not experimental evidence of occurrence. |
| taxon-224308 | https://rest.uniprot.org/taxonomy/224308.json; Active taxonomy identity, rank and parent | supports | Authority identity and exemplar/lineage relationship inspected; authority metadata is not experimental evidence of occurrence. |
| taxon-83333 | https://rest.uniprot.org/taxonomy/83333.json; Active taxonomy identity, rank and parent | supports | Authority identity and exemplar/lineage relationship inspected; authority metadata is not experimental evidence of occurrence. |
| taxon-83334 | https://rest.uniprot.org/taxonomy/83334.json; Active taxonomy identity, rank and parent | supports | Authority identity and exemplar/lineage relationship inspected; authority metadata is not experimental evidence of occurrence. |
| taxon-90371 | https://rest.uniprot.org/taxonomy/90371.json; Active taxonomy identity, rank and parent | supports | Authority identity and exemplar/lineage relationship inspected; authority metadata is not experimental evidence of occurrence. |
| taxon-99287 | https://rest.uniprot.org/taxonomy/99287.json; Active taxonomy identity, rank and parent | supports | Authority identity and exemplar/lineage relationship inspected; authority metadata is not experimental evidence of occurrence. |
| sl | https://rest.uniprot.org/locations/SL-0307.json; Name, definition, synonyms, GO cross-reference and parthood | supports | Exact flagellum/basal-body equivalence and component topology supported. |
| distribution | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12403147/fullTextXML; Results phyletic distribution; Methods GTDB v95 and HMM search | refutes | A 30,238-genome survey across 131 phyla infers flagellar capacity in about 40% from FliPQR markers; not a direct microscopy census. |
| bypass | DOI:10.1128/JB.00601-09; Publisher full text, Results and Discussion, Figs. 3-4, Table 1 | refutes | Salmonella SJW1103-derived C-ring deletion mutants overproducing FliI assemble rare paralyzed flagella and partial basal structures. Normal function is not restored. |
| uo-0000017 | https://www.ebi.ac.uk/ols4/api/ontologies/uo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUO_0000017; Identifier, label and definition | supports | Micrometers, nanometers and turns per second agree with their property dimensions. |
| uo-0000018 | https://www.ebi.ac.uk/ols4/api/ontologies/uo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUO_0000018; Identifier, label and definition | supports | Micrometers, nanometers and turns per second agree with their property dimensions. |
| uo-0000092 | https://www.ebi.ac.uk/ols4/api/ontologies/uo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUO_0000092; Identifier, label and definition | supports | Micrometers, nanometers and turns per second agree with their property dimensions. |
| ro | https://www.ebi.ac.uk/ols4/api/ontologies/ro/properties?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FRO_0002327; Relation identifier and definition | supports | RO:0002327 resolves to enables. |
| image | https://commons.wikimedia.org/w/api.php?action=query&amp;format=json&amp;titles=File%3AEscherichia+coli+flagella+TEM.png&amp;prop=imageinfo&amp;iiprop=url%7Csha1%7Cextmetadata; Commons imageinfo SHA1, source description, artist, credit and licence metadata | supports | Local image SHA1 matches Commons and SHA256 matches YAML; public-domain source identifies O157:H7 TEM and White/Hayes credits. |
| cdc | https://phil.cdc.gov/Details.aspx?pid=9995; PHIL 9995 description, content provider, photographer and rights statement | supports | Original source confirms digitally colorized pseudo-replica EM with peritrichous flagella. Attribution/CDC provenance are retained in the native entry and notes. |
| imodulondb | https://imodulondb.org/; Official kg-microbe-sources datasets and fliG searches | context_only | The 28-dataset inventory includes all three model organisms. fliG hits: s_enterica/core/STM1970, b_subtilis/modulome/BSU_16220, e_coli/precise_mg1655/b1939. No iModulon hit; gene identity context only, not assembly or localization evidence. |

## Limits And Additional Notes

- This is one record, not corpus-wide scientific approval. Native records, histories and generated pages were not edited; no GitHub issue was created by this audit.
- Full deterministic gates reuse verified successful CI at the unchanged durable main commit. Focused schema/strict and live trait checks were rerun; passing them does not establish biological truth.
- All cited DOI metadata and applicable authority identities were checked. Several older papers were accessible only as primary/review abstracts. Narrow claims supported there are assessed; unseen experimental detail is not certified.
- Review articles are explicitly labeled in evidence locators despite the shared schema having no separate secondary-source enum. They are not new experimental observations.
- Initial sandbox requests failed DNS. Some Europe PMC XML routes returned HTTP 500, some BioC requests returned a no-result body despite HTTP 200, and some publisher web routes failed. Actual readable publisher HTML, author manuscripts/PDF and abstracts were distinguished from failures.
- The first SubtiWiki/trait tool outputs were truncated; their processes were confirmed finished before a captured rerun. The captured dry-run and trait results passed. The PDF text extractor emitted font warnings; no verbatim new quotation or measurement relies on an ambiguous glyph.
- The iModulonDB adapter found gene identity hits but no module hit for the three explicit fliG searches. It supplies no direct evidence of cell-structure assembly or localization.
- The native target-kind scratch metadata was corrected from an invalid label to maintained. All original input hashes and the original durable Git base were rechecked unchanged; no scientific byte attestation was silently refreshed.
- Macnab 2003 full text and its diameter assertion remain unverified; this review is partial. Access failure itself did not generate a finding. The length lower-bound finding is independently established by inspected source text and the native acknowledgement.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T201901Z-flagellum-whole
kind: record
repository: CultureBotAI/CellStructureMech
title: 'Bacterial-type flagellum: evidence and scope audit'
started_at: '2026-10-10T20:03:37Z'
finished_at: '2026-10-10T20:19:01Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent scientific audit; not independent human review or
    native status promotion.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: Issue-bearing claim-level audit of this record. All sections inspected, but
  the diameter citation remains unverified; this is not complete scientific coverage.
source:
  git_revision: 49e9ce6b5cbdabce9787d1f51ff09702f306eb61
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
    role: context
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/images/appendage/bacterial_type_flagellum/escherichia_coli_flagella_tem.png
    sha256: 370078e7879241342df889b048aaaea27468ae7ed2a8c9509e1f1b16fbdb465e
    role: context
  - path: data/structures/appendage/bacterial_type_flagellum.yaml
    sha256: 64e054b6fa8ae3087745f6c16f65741e7567efa2c3d77205d77c862763d18b76
    role: target
  - path: docs/CURATION.md
    sha256: c3e482fbf381edcf0238e579648b779c3a8803a1d888b89397ad6fc8808dd07d
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
  - path: history/records/bacterial_type_flagellum/2026-08-30T194359Z-codex-e62f9c.yaml
    sha256: fc231f12920ea3a8f81152480c5a04dbf04b19a1447e3c4ccd772bae53773ddd
    role: context
  - path: history/records/bacterial_type_flagellum/2026-09-03T003923Z-claude-code-e5302e.yaml
    sha256: 0badefa41efdbf808e139d8024bb1992ba3d9a9790491986235050bbc1156db7
    role: context
  - path: history/records/bacterial_type_flagellum/2026-09-03T073851Z-claude-code-d38ae5.yaml
    sha256: 4ec7af7841a3adff1f426adc49401710718d7a2f0fa7aa0c7c080eef03222693
    role: context
  - path: history/records/bacterial_type_flagellum/2026-09-04T014136Z-codex-b18360.yaml
    sha256: b654b69e653e68c1b744252a6001a861f79bfcf6a7878ab735cb081276d47f21
    role: context
  - path: history/records/bacterial_type_flagellum/2026-09-08T065716Z-claude-340f8f.yaml
    sha256: 18313874cff78001e0f882fd684edc2facb73d19c39b64b635b4d08c590b9064
    role: context
  - path: history/records/bacterial_type_flagellum/2026-09-09T023556Z-claude-49d259.yaml
    sha256: 0bbc5786f9d7f49576685ca809b49fdfe6059a14b09f9f872b495f0665c7f34e
    role: context
  - path: history/records/bacterial_type_flagellum/2026-09-09T042811Z-claude-e740a7.yaml
    sha256: a9a7a7438bccfe39d214006c94ea5f105190e8e73c08b09739e7ca3286191936
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
targets:
- target_id: GO:0009288
  path: data/structures/appendage/bacterial_type_flagellum.yaml
  label: bacterial-type flagellum
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum.yaml
    role: maintained scientific record
scope:
  description: Single maintained structure, all present fields and both history surfaces.
    No native edits, generators or GitHub mutations.
  selection: 'Next sequential unassessed target in the all-record operational worklist:
    data/structures/appendage/bacterial_type_flagellum.yaml'
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - GO:0009288
  exclusions:
  - target: physical_properties[0].reference
    reason: Macnab 2003 full text unavailable through tried publisher/index routes;
      ~20 nm cannot be verified at its attached citation. No claim that the diameter
      is false.
checks:
- check_id: schema
  name: Fresh focused schema
  status: passed
  required: true
  target_ids:
  - GO:0009288
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/appendage/bacterial_type_flagellum.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: The unchanged target passed.
  scope_note: 2026-10-10T20:03:43Z to 2026-10-10T20:03:45Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: Fresh focused strict
  status: passed
  required: true
  target_ids:
  - GO:0009288
  command: .venv/bin/python scripts/validate_strict.py data/structures/appendage/bacterial_type_flagellum.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: The unchanged target passed.
  scope_note: 2026-10-10T20:03:45Z to 2026-10-10T20:03:48Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: subtiwiki
  name: subtiwiki verification
  status: passed
  required: true
  target_ids:
  - GO:0009288
  command: .venv/bin/python scripts/subtiwiki.py --record data/structures/appendage/bacterial_type_flagellum.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Dry run verified all 17 curated SubtiWiki/UniProt outlinks; no --apply
    and no native write.
  scope_note: 2026-10-10T20:08:32.681097+00:00 to 2026-10-10T20:08:54.932893+00:00;
    log SHA-256 8d420c5187c312d04d7dc3422db8fab92b182e200862a7c3584c7a06c0a6fb49
- check_id: traits
  name: traits verification
  status: passed
  required: true
  target_ids:
  - GO:0009288
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Live published index contains 477 traits; all 10 corpus links match. This
    target has two links.
  scope_note: 2026-10-10T20:08:54.933165+00:00 to 2026-10-10T20:09:17.745540+00:00;
    log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: ci
  name: ci verification
  status: passed
  required: true
  target_ids:
  - GO:0009288
  command: gh api 'repos/CultureBotAI/CellStructureMech/actions/runs?head_sha=49e9ce6b5cbdabce9787d1f51ff09702f306eb61&event=push&per_page=10'
  exit_code: 0
  expected_exit_code: 0
  summary: 'Reused successful exact-revision CI at 49e9ce6b: full QC 38081538245,
    labels 38081538303, identifier-liveness 38081538327, vendored sync 38081538243,
    merge integrity 38081538330. Native inputs are unchanged; not newly executed local
    full QC.'
  scope_note: 2026-10-10T20:09:17.745876+00:00 to 2026-10-10T20:09:18.295687+00:00;
    log SHA-256 ae2e01f6f7986856204e1ace507e79136878449550b537b4020f3e5244605a35
- check_id: diameter-source
  name: Verify diameter at its attached reference
  status: unavailable
  required: true
  target_ids:
  - GO:0009288
  summary: The source abstract does not contain the diameter and the tried publisher
    full-text routes were inaccessible. This preserves partial completion; access
    failure alone is not a finding.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/appendage/bacterial_type_flagellum.yaml
  locator: Entire YAML; native schema enums; append-only histories; full hidden/ignored
    review search
  accessed_at: '2026-10-10T20:14:58Z'
  support: context_only
  summary: Input hashes captured before assessment; all present sections and history
    entries read; status PROPOSED retained. No earlier structured bundle for this
    target found in the searched reviews/reports roots, including ignored files.
- evidence_id: paper-00
  kind: primary_source
  reference: DOI:10.1016/0022-2836(92)90958-m
  locator: Primary abstract
  accessed_at: '2026-10-10T20:04:42Z'
  snapshot_sha256: ed51549b0c8aba6074ccf23c7373a0e3b920cb77a35c5815e6719832e83f66a4
  support: supports
  summary: Salmonella assembly intermediates establish autonomous MS-ring formation
    and cooperative FliE/FlgB/FlgC/FlgF/FlgG rod assembly.
- evidence_id: paper-01
  kind: primary_source
  reference: DOI:10.1016/j.cell.2020.08.016
  locator: Primary abstract; author PDF pp. 251-253, rotational model and bidirectional
    rotation sections
  accessed_at: '2026-10-10T20:10:25Z'
  snapshot_sha256: 523d65ad14bfee062c9c8d7a687dd0838b56c7943b2f25212fb9a34f25c09d94
  support: supports
  summary: A5B2 architecture is experimentally resolved; detailed torque steps are
    proposed from structures and functional data, not directly filmed stator rotation.
- evidence_id: paper-03
  kind: primary_source
  reference: DOI:10.1016/j.jmb.2005.07.030
  locator: Primary abstract
  accessed_at: '2026-10-10T20:04:44Z'
  snapshot_sha256: 4a2f9c2a697475905e4f5faf59f098b83e929f124531d47f7e93a50ef6a1aea3
  support: supports
  summary: B. subtilis MotAB and MotPS have distinct H+/Na+ coupling; stator-deficient
    cells retain flagella. Supports the curated MotP/MotS placements.
- evidence_id: paper-04
  kind: primary_source
  reference: DOI:10.1016/j.tim.2014.12.011
  locator: Review abstract only
  accessed_at: '2026-10-10T20:04:45Z'
  snapshot_sha256: ad98d7055c7f2495697e3a5f0856dc19cc1d09131e19e34f31215db0b0238c43
  support: supports
  summary: The cited review covers conserved MS ring, C ring, rod and export apparatus,
    ion-powered motors, and Salmonella/Vibrio structural diversity; detailed unseen
    text is not certified.
- evidence_id: paper-07
  kind: primary_source
  reference: DOI:10.1038/nrmicro1887
  locator: Review abstract only
  accessed_at: '2026-10-10T20:04:49Z'
  snapshot_sha256: 648eac60aca511dba55bd983fcc746cd1c173f143b5259fa8bd78daa609ca3c6
  support: supports
  summary: The article concerns coupling flagellar gene regulation and assembly in
    Gram-negative bacteria; its abstract is not a denominator-bearing bacterial prevalence
    survey.
- evidence_id: paper-08
  kind: primary_source
  reference: DOI:10.1038/s41467-021-24507-9
  locator: 'Primary full text: introduction, native MS/C-ring results, Fig. 1, discussion
    and strain methods'
  accessed_at: '2026-10-10T20:04:51Z'
  snapshot_sha256: 602f3eb50f5f81de1ffa522838f21c064653d23f5bf5e86553ee6c0213017a43
  support: supports
  summary: Native Salmonella MS ring has 34 FliF subunits in the studied preparation;
    C-ring symmetry varies. MS-ring scaffold and export-gate housing are supported.
- evidence_id: paper-10
  kind: primary_source
  reference: DOI:10.1038/s41564-020-0788-8
  locator: 'Primary full text: stator architecture, Coupling of ion-flow to flagellar
    rotation, discussion and methods'
  accessed_at: '2026-10-10T20:04:55Z'
  snapshot_sha256: 2250b535735358b44b02046731afdf6ad1fac623468bfd82d7145248b1a6b072
  support: supports
  summary: A5B2 structures support torque models. The authors explicitly allow either
    processive rotation or oscillating ratchet motion; geometry does not directly
    establish one dynamic trajectory.
- evidence_id: paper-12
  kind: primary_source
  reference: DOI:10.1038/s41598-019-51440-1
  locator: 'Primary full text: introduction and Kurthia filament results'
  accessed_at: '2026-10-10T20:04:58Z'
  snapshot_sha256: 66f39520bc10a5b835715828e2a9938d8a8bdbc4205950e7b259531b705329e7
  support: supports
  summary: Supports the recorded 11-protofilament statement together with its explicit
    Campylobacter exception; the exception is already retained in native evidence
    notes.
- evidence_id: paper-16
  kind: primary_source
  reference: DOI:10.1093/nar/gkae957
  locator: Source-database paper abstract
  accessed_at: '2026-10-10T20:05:04Z'
  snapshot_sha256: 6312b1ab469126a4cdcb3a033d5223fe6ca9f27243f2ea0e65b4cb94270cd256
  support: supports
  summary: SubtiWiki is the maintained B. subtilis reference resource with an API.
    Individual protein outlinks were separately verified by the repository dry-run
    adapter.
- evidence_id: paper-18
  kind: primary_source
  reference: DOI:10.1128/jb.00626-18
  locator: Primary abstract
  accessed_at: '2026-10-10T20:05:07Z'
  snapshot_sha256: 7e62038b257d8f313145023b06de6fa732c6f3244c01e4c6daf85822cfabc74a
  support: supports
  summary: B. subtilis uses FliY in place of FliN and reverses the CheY-P rotational
    response relative to E. coli. The native record already acknowledges the lineage
    variant.
- evidence_id: paper-19
  kind: primary_source
  reference: DOI:10.1128/jb.00353-25
  locator: 'Primary full text: introduction and motor-load paragraph'
  accessed_at: '2026-10-10T20:05:09Z'
  snapshot_sha256: 97fe62fb23009cda264e055feb1c12bf354cb3f55a08f91467b8960c59b74da4
  support: supports
  summary: The quoted source gives about 125 Hz with filament/high load and 300 Hz
    or faster at low load; the native context preserves these conditions. The approximate
    summary range is not a hard maximum.
- evidence_id: paper-20
  kind: primary_source
  reference: DOI:10.1128/jcm.26.7.1367-1372.1988
  locator: Primary abstract
  accessed_at: '2026-10-10T20:05:10Z'
  snapshot_sha256: 6af1b9c29e4e754c21205be354e7e195096126d7ffcb895124581b8544382536
  support: supports
  summary: Purification, TEM, H7 immunoassay and immunogold characterize O157:H7 strain
    CL-56 flagellin; supports the bounded taxon example, not identification of the
    separate CDC specimen.
- evidence_id: paper-22
  kind: primary_source
  reference: DOI:10.1146/annurev.biochem.72.121801.161737
  locator: Review abstract only
  accessed_at: '2026-10-10T20:05:13Z'
  snapshot_sha256: 4c2938da11aeddedf2691f6bca3667182d4a49446eaf8bc12de59bf84c81ac9a
  support: supports
  summary: E. coli swimming uses reversible ion-driven motors and helical filaments;
    supports the broad definition, function and swimming edges, not a precise filament
    diameter.
- evidence_id: paper-23
  kind: primary_source
  reference: DOI:10.1146/annurev.micro.57.030502.090832
  locator: Review abstract only
  accessed_at: '2026-10-10T20:05:14Z'
  snapshot_sha256: 68caf42cabe3749c93733a366e2bda96e3fb414eb0f71a846df6d91eb67b7f58
  support: supports
  summary: Axial proteins are exported by a flagellar type III pathway and assemble
    distally. Its accessible abstract does not verify the native ~20 nm diameter.
- evidence_id: paper-24
  kind: primary_source
  reference: DOI:10.3389/fmicb.2015.00023
  locator: 'Review full text: historical structural comparison and archaellum distinction'
  accessed_at: '2026-10-10T20:05:15Z'
  snapshot_sha256: c2cec0461a17865f7242ef36df178bfc68d00c1f1e292b75f9682a6ba5461464
  support: supports
  summary: Archaella have a distinct type-IV-filament-related architecture, not the
    bacterial flagellar apparatus; supports the bounded structural distinction, not
    an exhaustive new archaeal survey.
- evidence_id: paper-25
  kind: primary_source
  reference: DOI:10.3390/biom11020186
  locator: 'Review full text: core export gate and Model for High-Speed Secretion
    of Flagellin'
  accessed_at: '2026-10-10T20:05:19Z'
  snapshot_sha256: 2f4a7d1f075cdd8f454d354c31192a07f9373119e2cfd15a8d24fe2aaca7e911
  support: supports
  summary: The source states about 20,000 flagellin subunits and growth up to 20 micrometers;
    it does not establish a 5-micrometer minimum. Export-gate composition and FliK
    context are corroborated.
- evidence_id: paper-26
  kind: primary_source
  reference: DOI:10.7554/elife.48979
  locator: 'Primary full text: stator-deletion results, Fig. 1, tomography comparison'
  accessed_at: '2026-10-10T20:05:22Z'
  snapshot_sha256: bf6a96bd205a6cbaea786a35c1c2c68367f8d7f97ddddea875c45760113e1b68
  support: supports
  summary: Borrelia motA/motB mutants retain paralyzed flagella and motor substructures;
    supports assembly dispensability of the stator, not normal motor function.
- evidence_id: go-0009288
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0009288
  locator: Exact OLS GO identifier, definition, synonyms, obsolete flag
  accessed_at: '2026-10-10T20:05:35Z'
  snapshot_sha256: d92c7515a86c21f7570660976b4f66561598d312ef830aae7d4b6dfdd328cf21
  support: supports
  summary: Exact active structure or process identity checked. GO:0120101 retains
    an outdated A4B2 definition upstream; the native record does not adopt that stoichiometry.
- evidence_id: go-0009420
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0009420
  locator: Exact OLS GO identifier, definition, synonyms, obsolete flag
  accessed_at: '2026-10-10T20:05:36Z'
  snapshot_sha256: 5842cfd41cc8b5d02d7ba10b43c0de1b563dc724ad0861e38cab6a4765454199
  support: supports
  summary: Exact active structure or process identity checked. GO:0120101 retains
    an outdated A4B2 definition upstream; the native record does not adopt that stoichiometry.
- evidence_id: go-0009421
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0009421
  locator: Exact OLS GO identifier, definition, synonyms, obsolete flag
  accessed_at: '2026-10-10T20:05:36Z'
  snapshot_sha256: a5149d00ede2f5f8930d6d35888bf248b3d9d2abc72f5c8b78aa1a64be24b68e
  support: supports
  summary: Exact active structure or process identity checked. GO:0120101 retains
    an outdated A4B2 definition upstream; the native record does not adopt that stoichiometry.
- evidence_id: go-0009422
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0009422
  locator: Exact OLS GO identifier, definition, synonyms, obsolete flag
  accessed_at: '2026-10-10T20:05:37Z'
  snapshot_sha256: 2173f58d0e4237c7365e2953b3334a6325f5607a6f61992e24d69492cb87e93f
  support: supports
  summary: Exact active structure or process identity checked. GO:0120101 retains
    an outdated A4B2 definition upstream; the native record does not adopt that stoichiometry.
- evidence_id: go-0009424
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0009424
  locator: Exact OLS GO identifier, definition, synonyms, obsolete flag
  accessed_at: '2026-10-10T20:05:38Z'
  snapshot_sha256: 0ea0c99c4cc0f3538a77323eb000284f8e030f65cc83bc8aadf9f89b67d35dd3
  support: supports
  summary: Exact active structure or process identity checked. GO:0120101 retains
    an outdated A4B2 definition upstream; the native record does not adopt that stoichiometry.
- evidence_id: go-0009425
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0009425
  locator: Exact OLS GO identifier, definition, synonyms, obsolete flag
  accessed_at: '2026-10-10T20:05:38Z'
  snapshot_sha256: ba237444d9aaed5133ec4da342e0d2d5392ac51591dcbc7fe9f7e8db9127df26
  support: supports
  summary: Exact active structure or process identity checked. GO:0120101 retains
    an outdated A4B2 definition upstream; the native record does not adopt that stoichiometry.
- evidence_id: go-0071973
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0071973
  locator: Exact OLS GO identifier, definition, synonyms, obsolete flag
  accessed_at: '2026-10-10T20:05:40Z'
  snapshot_sha256: 1445397d323fd0ccae50b29e2271e0f87ba81af0185bfcc7707ad6355f4b97b8
  support: supports
  summary: Exact active structure or process identity checked. GO:0120101 retains
    an outdated A4B2 definition upstream; the native record does not adopt that stoichiometry.
- evidence_id: ipr001492
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001492/
  locator: InterPro metadata accession/name/type/description
  accessed_at: '2026-10-10T20:05:42Z'
  snapshot_sha256: 412be2b849def6075db63e78f069de9051b598d879399e454c2211a5e061816c
  support: supports
  summary: Family identity inspected; FliN entry explicitly notes the longer FliY
    form. Family/domain overlap is not proof that whole proteins are equivalent.
- evidence_id: ipr012835
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012835/
  locator: InterPro metadata accession/name/type/description
  accessed_at: '2026-10-10T20:08:36Z'
  snapshot_sha256: 4dd654200d0e65e518424ba3acb2e02e3f3de33f3f4bb8b4da1718efa678e04d
  support: supports
  summary: Family identity inspected; FliN entry explicitly notes the longer FliY
    form. Family/domain overlap is not proof that whole proteins are equivalent.
- evidence_id: ipr020013
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020013/
  locator: InterPro metadata accession/name/type/description
  accessed_at: '2026-10-10T20:08:37Z'
  snapshot_sha256: edb69e1603a4fc1dcbf4cfa68c1a7d8a1298965e9adc73fb85731123c63a648d
  support: supports
  summary: Family identity inspected; FliN entry explicitly notes the longer FliY
    form. Family/domain overlap is not proof that whole proteins are equivalent.
- evidence_id: p02968
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P02968.json
  locator: Reviewed status, recommended name, genes, taxon, InterPro matches and localization
    annotations
  accessed_at: '2026-10-10T20:05:50Z'
  snapshot_sha256: 0f1fbe5112078f6dc85f3f32e7c4e06d6e6ca5f26cf23d64ec7a8ced8cc723f2
  support: supports
  summary: Accession, gene and taxon match the native protein example. Identity-only
    examples remain identity-only; source annotation is not upgraded to direct localization.
- evidence_id: p06179
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P06179.json
  locator: Reviewed status, recommended name, genes, taxon, InterPro matches and localization
    annotations
  accessed_at: '2026-10-10T20:05:51Z'
  snapshot_sha256: d7581a1c33bae41b8a5cad7676fd290f48e49b783f129bf544ac125d5801a450
  support: supports
  summary: Accession, gene and taxon match the native protein example. Identity-only
    examples remain identity-only; source annotation is not upgraded to direct localization.
- evidence_id: p52616
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P52616.json
  locator: Reviewed status, recommended name, genes, taxon, InterPro matches and localization
    annotations
  accessed_at: '2026-10-10T20:06:04Z'
  snapshot_sha256: 795005e3625a12dbc336b1a68b72ede793ade300c94abb8335cae3db9c5219b0
  support: supports
  summary: Accession, gene and taxon match the native protein example. Identity-only
    examples remain identity-only; source annotation is not upgraded to direct localization.
- evidence_id: p0a1j1
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0A1J1.json
  locator: Reviewed status, recommended name, genes, taxon, InterPro matches and localization
    annotations
  accessed_at: '2026-10-10T20:05:51Z'
  snapshot_sha256: d38958f6bab34260fde99a0597b66dbca9ceb127a06edc6287965aed4daa146d
  support: supports
  summary: Accession, gene and taxon match the native protein example. Identity-only
    examples remain identity-only; source annotation is not upgraded to direct localization.
- evidence_id: p23447
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P23447.json
  locator: Reviewed status, recommended name, genes, taxon, InterPro matches and localization
    annotations
  accessed_at: '2026-10-10T20:05:53Z'
  snapshot_sha256: 7956d9d7d0320dbedd3ac4d771672e55d4810b12ad5c171f9b570d1aa6abee90
  support: supports
  summary: Accession, gene and taxon match the native protein example. Identity-only
    examples remain identity-only; source annotation is not upgraded to direct localization.
- evidence_id: p23448
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P23448.json
  locator: Reviewed status, recommended name, genes, taxon, InterPro matches and localization
    annotations
  accessed_at: '2026-10-10T20:05:54Z'
  snapshot_sha256: 35e60b262aaf9e1b5e5d2da63e0ac8fb7769d4d6481c48db30fed8496548ec10
  support: supports
  summary: Accession, gene and taxon match the native protein example. Identity-only
    examples remain identity-only; source annotation is not upgraded to direct localization.
- evidence_id: p23453
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P23453.json
  locator: Reviewed status, recommended name, genes, taxon, InterPro matches and localization
    annotations
  accessed_at: '2026-10-10T20:05:55Z'
  snapshot_sha256: 0bec9dc4de1d2436f99fca01394ec30357b747454d2c2038dbfb17c6d1194f58
  support: supports
  summary: Accession, gene and taxon match the native protein example. Identity-only
    examples remain identity-only; source annotation is not upgraded to direct localization.
- evidence_id: p24073
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P24073.json
  locator: Reviewed status, recommended name, genes, taxon, InterPro matches and localization
    annotations
  accessed_at: '2026-10-10T20:05:55Z'
  snapshot_sha256: fdec67f72bcd246fb0d2bed16f72340f49ddbec5c34a071e23753e8f549543c0
  support: supports
  summary: Accession, gene and taxon match the native protein example. Identity-only
    examples remain identity-only; source annotation is not upgraded to direct localization.
- evidence_id: p28611
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P28611.json
  locator: Reviewed status, recommended name, genes, taxon, InterPro matches and localization
    annotations
  accessed_at: '2026-10-10T20:05:59Z'
  snapshot_sha256: ba60bdd6dc6fef5d0b3cf64895e967613f274a3f9128b2d02fb723aa744a3b86
  support: supports
  summary: Accession, gene and taxon match the native protein example. Identity-only
    examples remain identity-only; source annotation is not upgraded to direct localization.
- evidence_id: p28612
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P28612.json
  locator: Reviewed status, recommended name, genes, taxon, InterPro matches and localization
    annotations
  accessed_at: '2026-10-10T20:05:59Z'
  snapshot_sha256: 698561a1ec0bb831cb199878ae8afcc1ef266f4cff32cab57e16eafa7e5fb6be
  support: supports
  summary: Accession, gene and taxon match the native protein example. Identity-only
    examples remain identity-only; source annotation is not upgraded to direct localization.
- evidence_id: p39063
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P39063.json
  locator: Reviewed status, recommended name, genes, taxon, InterPro matches and localization
    annotations
  accessed_at: '2026-10-10T20:06:03Z'
  snapshot_sha256: 0991ed03821dfbd7e9c3ad841728fb056dc4100f079b875996d37e58edce4ea3
  support: supports
  summary: Accession, gene and taxon match the native protein example. Identity-only
    examples remain identity-only; source annotation is not upgraded to direct localization.
- evidence_id: p39064
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P39064.json
  locator: Reviewed status, recommended name, genes, taxon, InterPro matches and localization
    annotations
  accessed_at: '2026-10-10T20:06:04Z'
  snapshot_sha256: 5eb6c87f9bfbcc9dc4c4fc9a5f5bfa656bd1e361084b16495d5a6a2f16a6a44e
  support: supports
  summary: Accession, gene and taxon match the native protein example. Identity-only
    examples remain identity-only; source annotation is not upgraded to direct localization.
- evidence_id: p23446
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P23446.json
  locator: Reviewed status, recommended name, genes, taxon, InterPro matches and localization
    annotations
  accessed_at: '2026-10-10T20:05:53Z'
  snapshot_sha256: 052d5e1518e70c0c25d20dcb5405de7398a75809f4115eea8ee05ada05facd60
  support: supports
  summary: Accession, gene and taxon match the native protein example. Identity-only
    examples remain identity-only; source annotation is not upgraded to direct localization.
- evidence_id: p24500
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P24500.json
  locator: Reviewed status, recommended name, genes, taxon, InterPro matches and localization
    annotations
  accessed_at: '2026-10-10T20:05:56Z'
  snapshot_sha256: ff0bb5ab65adcdb391317a655b5aa048a5d500c9f50f17d3c5d4eca0a79537a3
  support: supports
  summary: Accession, gene and taxon match the native protein example. Identity-only
    examples remain identity-only; source annotation is not upgraded to direct localization.
- evidence_id: p24501
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P24501.json
  locator: Reviewed status, recommended name, genes, taxon, InterPro matches and localization
    annotations
  accessed_at: '2026-10-10T20:05:57Z'
  snapshot_sha256: 2a9950594b1fbbd4b6f54213395dce09138703a45b12cc05e7cb7f2eb302a8fd
  support: supports
  summary: Accession, gene and taxon match the native protein example. Identity-only
    examples remain identity-only; source annotation is not upgraded to direct localization.
- evidence_id: p35620
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P35620.json
  locator: Reviewed status, recommended name, genes, taxon, InterPro matches and localization
    annotations
  accessed_at: '2026-10-10T20:06:02Z'
  snapshot_sha256: 2354a42e0ffad5f1841265cf11878e6839a922f80e3552931e5707c19da5fef5
  support: supports
  summary: Accession, gene and taxon match the native protein example. Identity-only
    examples remain identity-only; source annotation is not upgraded to direct localization.
- evidence_id: p35538
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P35538.json
  locator: Reviewed status, recommended name, genes, taxon, InterPro matches and localization
    annotations
  accessed_at: '2026-10-10T20:06:02Z'
  snapshot_sha256: 96863b9a2c6d314295b1c033cacd3f1d1c432ab69e34b63c4eaa45a1bcb3cf30
  support: supports
  summary: Accession, gene and taxon match the native protein example. Identity-only
    examples remain identity-only; source annotation is not upgraded to direct localization.
- evidence_id: p35528
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P35528.json
  locator: Reviewed status, recommended name, genes, taxon, InterPro matches and localization
    annotations
  accessed_at: '2026-10-10T20:06:00Z'
  snapshot_sha256: 78e8fcce710ad863b71ab25b057bb9116d29af44dc4efdec105fb1b4d23475d6
  support: supports
  summary: Accession, gene and taxon match the native protein example. Identity-only
    examples remain identity-only; source annotation is not upgraded to direct localization.
- evidence_id: p35535
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P35535.json
  locator: Reviewed status, recommended name, genes, taxon, InterPro matches and localization
    annotations
  accessed_at: '2026-10-10T20:06:00Z'
  snapshot_sha256: 05409f7ddb2eb7b92750673b4a7d6fdfd58bd717fdd9674ad9d945bec2d85e21
  support: supports
  summary: Accession, gene and taxon match the native protein example. Identity-only
    examples remain identity-only; source annotation is not upgraded to direct localization.
- evidence_id: p35537
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P35537.json
  locator: Reviewed status, recommended name, genes, taxon, InterPro matches and localization
    annotations
  accessed_at: '2026-10-10T20:06:01Z'
  snapshot_sha256: f068a8ada8afb73a276c19019a0a8b3bc4613225a124941f6985aa872ace58b4
  support: supports
  summary: Accession, gene and taxon match the native protein example. Identity-only
    examples remain identity-only; source annotation is not upgraded to direct localization.
- evidence_id: taxon-2
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/2.json
  locator: Active taxonomy identity, rank and parent
  accessed_at: '2026-10-10T20:05:44Z'
  snapshot_sha256: 8074c9bcd59cd4da1da4bc9ec98c040bbecd52ef5c91c4c4bb9bed0f3a7cb5a9
  support: supports
  summary: Authority identity and exemplar/lineage relationship inspected; authority
    metadata is not experimental evidence of occurrence.
- evidence_id: taxon-2157
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/2157.json
  locator: Active taxonomy identity, rank and parent
  accessed_at: '2026-10-10T20:05:44Z'
  snapshot_sha256: 14f5852a1db0f9f5ef8d60e4a11c1916bf005bf549c57dd4bc860d39194a1799
  support: supports
  summary: Authority identity and exemplar/lineage relationship inspected; authority
    metadata is not experimental evidence of occurrence.
- evidence_id: taxon-224308
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/224308.json
  locator: Active taxonomy identity, rank and parent
  accessed_at: '2026-10-10T20:05:45Z'
  snapshot_sha256: 67c51a9882fd6b4b39580518be53faece835e0c31b0e347a0345bd248a70c9fa
  support: supports
  summary: Authority identity and exemplar/lineage relationship inspected; authority
    metadata is not experimental evidence of occurrence.
- evidence_id: taxon-83333
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/83333.json
  locator: Active taxonomy identity, rank and parent
  accessed_at: '2026-10-10T20:05:46Z'
  snapshot_sha256: 83c59ae9694d1874b8a175d7ce7608f77f5688d35adf307a0859dbb20f9e1c17
  support: supports
  summary: Authority identity and exemplar/lineage relationship inspected; authority
    metadata is not experimental evidence of occurrence.
- evidence_id: taxon-83334
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/83334.json
  locator: Active taxonomy identity, rank and parent
  accessed_at: '2026-10-10T20:05:46Z'
  snapshot_sha256: 8a22ae71ff5a8b8fac877f045fcd02598ec70eb7de80210bffb02068293a7de9
  support: supports
  summary: Authority identity and exemplar/lineage relationship inspected; authority
    metadata is not experimental evidence of occurrence.
- evidence_id: taxon-90371
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/90371.json
  locator: Active taxonomy identity, rank and parent
  accessed_at: '2026-10-10T20:05:47Z'
  snapshot_sha256: 46c958747209e78a835996643e63aafb6d1e94a8a632f0094dba733eb1bd3dee
  support: supports
  summary: Authority identity and exemplar/lineage relationship inspected; authority
    metadata is not experimental evidence of occurrence.
- evidence_id: taxon-99287
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/99287.json
  locator: Active taxonomy identity, rank and parent
  accessed_at: '2026-10-10T20:05:47Z'
  snapshot_sha256: 107ebfece75c5a7147abe7547dec9166f87ff267e6cbc3f67bea9ab9df694a59
  support: supports
  summary: Authority identity and exemplar/lineage relationship inspected; authority
    metadata is not experimental evidence of occurrence.
- evidence_id: sl
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0307.json
  locator: Name, definition, synonyms, GO cross-reference and parthood
  accessed_at: '2026-10-10T20:06:06Z'
  snapshot_sha256: e55524af529f132e7dd82e9ceb96e6165f3177fcf7fed385cce9bb4be064a70b
  support: supports
  summary: Exact flagellum/basal-body equivalence and component topology supported.
- evidence_id: distribution
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12403147/fullTextXML
  locator: Results phyletic distribution; Methods GTDB v95 and HMM search
  accessed_at: '2026-10-10T20:11:14Z'
  snapshot_sha256: 6cedc1bf8fd502b010e3123a8cd40e566506804de364f6d959a52120457af9f6
  support: refutes
  summary: A 30,238-genome survey across 131 phyla infers flagellar capacity in about
    40% from FliPQR markers; not a direct microscopy census.
- evidence_id: bypass
  kind: primary_source
  reference: DOI:10.1128/JB.00601-09
  accessed_at: '2026-10-10T20:14:58Z'
  locator: Publisher full text, Results and Discussion, Figs. 3-4, Table 1
  support: refutes
  summary: Salmonella SJW1103-derived C-ring deletion mutants overproducing FliI assemble
    rare paralyzed flagella and partial basal structures. Normal function is not restored.
- evidence_id: uo-0000017
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUO_0000017
  locator: Identifier, label and definition
  accessed_at: '2026-10-10T20:05:48Z'
  snapshot_sha256: 786ed7f6d5b07e4ec6f0a105ced79a4e4b5f025329b403c7ffc7e1d0566e2951
  support: supports
  summary: Micrometers, nanometers and turns per second agree with their property
    dimensions.
- evidence_id: uo-0000018
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUO_0000018
  locator: Identifier, label and definition
  accessed_at: '2026-10-10T20:05:49Z'
  snapshot_sha256: 5aa4d11cd0f398ac65be12b58f91295efae620bb2e5c345bd0fd81c6f0e09c5c
  support: supports
  summary: Micrometers, nanometers and turns per second agree with their property
    dimensions.
- evidence_id: uo-0000092
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUO_0000092
  locator: Identifier, label and definition
  accessed_at: '2026-10-10T20:05:49Z'
  snapshot_sha256: bb7288236129e5f267f8bb9f25fd3233e32e6958020ebc732634ff0ec4d9235d
  support: supports
  summary: Micrometers, nanometers and turns per second agree with their property
    dimensions.
- evidence_id: ro
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/ro/properties?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FRO_0002327
  locator: Relation identifier and definition
  accessed_at: '2026-10-10T20:11:16Z'
  snapshot_sha256: 5bbceaccdeae417c68a2344aac455d7a7607b3f29b5295d909a16de496b49419
  support: supports
  summary: RO:0002327 resolves to enables.
- evidence_id: image
  kind: authority
  reference: https://commons.wikimedia.org/w/api.php?action=query&format=json&titles=File%3AEscherichia+coli+flagella+TEM.png&prop=imageinfo&iiprop=url%7Csha1%7Cextmetadata
  locator: Commons imageinfo SHA1, source description, artist, credit and licence
    metadata
  accessed_at: '2026-10-10T20:08:38Z'
  snapshot_sha256: bbf5d0ff8daa9cba8efd98d429ebbde048b32af1e8297cef9f1f22921c7bf640
  support: supports
  summary: Local image SHA1 matches Commons and SHA256 matches YAML; public-domain
    source identifies O157:H7 TEM and White/Hayes credits.
- evidence_id: cdc
  kind: authority
  reference: https://phil.cdc.gov/Details.aspx?pid=9995
  locator: PHIL 9995 description, content provider, photographer and rights statement
  accessed_at: '2026-10-10T20:08:38Z'
  snapshot_sha256: 98a589f1c5e56833f966f84da76d218a3ee3a8319fedd0b3f33e8897df212891
  support: supports
  summary: Original source confirms digitally colorized pseudo-replica EM with peritrichous
    flagella. Attribution/CDC provenance are retained in the native entry and notes.
- evidence_id: imodulondb
  kind: database
  reference: https://imodulondb.org/
  locator: Official kg-microbe-sources datasets and fliG searches
  accessed_at: '2026-10-10T20:14:58Z'
  support: context_only
  summary: 'The 28-dataset inventory includes all three model organisms. fliG hits:
    s_enterica/core/STM1970, b_subtilis/modulome/BSU_16220, e_coli/precise_mg1655/b1939.
    No iModulon hit; gene identity context only, not assembly or localization evidence.'
assessments:
- assessment_id: identity
  area: identity
  topic: Identity, hierarchy and boundary
  outcome: supported
  target_ids:
  - GO:0009288
  evidence_ids:
  - record
  - go-0009288
  - go-0009420
  - go-0009421
  - go-0009422
  - go-0009424
  - go-0009425
  - go-0071973
  summary: The record denotes the bacterial flagellum, with filament, cap, junction,
    hook and basal body as named parts; archaella and cilia are distinguished. The
    conventional bacterial-flagellum synonym is equivalent although not listed as
    a current GO exact synonym.
- assessment_id: composition
  area: evidence
  topic: Every component, assembly essentiality and quantities
  outcome: concern
  target_ids:
  - GO:0009288
  evidence_ids:
  - record
  - paper-00
  - paper-08
  - paper-10
  - paper-26
  - bypass
  - paper-25
  - paper-12
  - paper-03
  summary: Membership, MS-ring scaffold, axial rod, LP bushing, five-protein membrane
    gate and dispensable stator are supported. C-ring ESSENTIAL needs a condition-bound
    assembly qualification. Approximate flagellin count and nonuniversal protofilament
    count retain explicit evidence caveats; the hook is not replaced by its broader
    rod/hook family.
- assessment_id: taxonomy
  area: scope
  topic: Both distribution rows and canonical examples
  outcome: concern
  target_ids:
  - GO:0009288
  evidence_ids:
  - record
  - distribution
  - paper-24
  - paper-20
  - paper-16
  summary: Examples and the bacterial/archaellum distinction are supported. COMMON
    means most members under the native schema, stronger than the evidence supports;
    VARIABLE is the conservative correction.
  dimensions:
  - name: survey-method
    value: Genomic proxy, not observed flagellation
    definition: Limits on interpreting population evidence
    evidence_ids:
    - distribution
- assessment_id: examples
  area: grounding
  topic: Protein examples and family decisions
  outcome: supported
  target_ids:
  - GO:0009288
  evidence_ids:
  - record
  - ipr001492
  - ipr012835
  - ipr020013
  - paper-03
  - paper-18
  - imodulondb
  summary: Twenty examples retain verified accession/gene/taxon identities; all 17
    SubtiWiki mappings pass dry-run checks, including historical FlgE/FlgG and MotP/MotS
    aliases. FliY replacement is documented. FlgE broad-family rejection remains justified
    for the two inspected UniProt entries.
- assessment_id: quantities
  area: quantity
  topic: Physical properties and exact source support
  outcome: concern
  target_ids:
  - GO:0009288
  evidence_ids:
  - record
  - paper-19
  - paper-23
  - paper-25
  - uo-0000017
  - uo-0000018
  - uo-0000092
  summary: Length lower bound is explicitly unsourced. Rotation-speed context and
    units are supported, with no hard low-load maximum inferred. The approximate diameter
    remains unverified at Macnab 2003; this required check keeps the review partial.
- assessment_id: image
  area: provenance
  topic: Hosted TEM image and attribution
  outcome: supported
  target_ids:
  - GO:0009288
  evidence_ids:
  - image
  - cdc
  - record
  summary: Local bitmap visually inspected; cell and peritrichous filaments are visible.
    Hashes, public-domain metadata, photographer/provider, original CDC source and
    depicted O157:H7 taxon agree. No new measurement is inferred from the colorized
    image.
- assessment_id: function-graph
  area: graph
  topic: Functions and every causal edge
  outcome: concern
  target_ids:
  - GO:0009288
  evidence_ids:
  - record
  - paper-10
  - paper-01
  - paper-22
  - paper-19
  - ro
  summary: 'All five edges checked: ion input, stator/FliG torque, coupled rotor rotation,
    hook transmission and propulsion. The PMF node improperly includes sodium flux,
    and proposed stator rotation is promoted to unqualified mechanism.'
- assessment_id: status
  area: provenance
  topic: Discussions, lifecycle and optional fields
  outcome: concern
  target_ids:
  - GO:0009288
  evidence_ids:
  - record
  summary: PROPOSED and append-only history are appropriate. No optional absent image,
    dataset, trait, pathway or composition field is treated as a defect. The grounding
    TODO still asks to assign an already assigned flagellin family and to redo an
    already documented hook decision.
findings:
- finding_id: F1
  issue_key: bacterial-flagellum-length-lower-bound
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Remove or source the 5-micrometer lower bound
  description: physical_properties[1] states 5-20 micrometers while its own evidence
    says the lower bound is unsourced. The inspected cited section supports up to
    20, not a minimum of 5.
  target_ids:
  - GO:0009288
  field_paths:
  - physical_properties[1]
  evidence_ids:
  - record
  - paper-25
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#evidence
  native_severity: major
  normalization_reason: Material evidence/scope defect under the native rubric.
- finding_id: F2
  issue_key: bacterial-flagellum-stator-model-evidence-strength
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Keep proposed stator rotation labeled as a model
  description: The prose asserts MotA/PomA-subunit rotation as an established mechanical
    step. The cited 2020 structural studies propose this trajectory; Deme also permits
    an oscillating ratchet. Preserve the resolved A5B2 architecture and experimentally
    supported torque coupling without upgrading the dynamic model.
  target_ids:
  - GO:0009288
  field_paths:
  - components[4].evidence[0].notes
  - causal_graphs[0].edges[0:2]
  evidence_ids:
  - record
  - paper-10
  - paper-01
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#evidence
  native_severity: major
  normalization_reason: Material evidence/scope defect under the native rubric.
- finding_id: F3
  issue_key: bacterial-flagellum-pmf-sodium-conflation
  category: graph
  severity: major
  status: open
  certainty: confirmed
  title: Distinguish proton and sodium motive forces
  description: The graph source node is proton motive force, but its outgoing description
    includes sodium flux. The source distinguishes ion-specific gradients; sodium-driven
    motors cannot be encoded as proton-driven merely because both are ion powered.
  target_ids:
  - GO:0009288
  field_paths:
  - causal_graphs[0].nodes[0]
  - causal_graphs[0].edges[0].description
  evidence_ids:
  - record
  - paper-03
  - paper-10
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#causal-graphs
  native_severity: major
  normalization_reason: Material evidence/scope defect under the native rubric.
- finding_id: F4
  issue_key: bacterial-flagellum-bacterial-presence-common
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Use a supported bacterial prevalence category
  description: COMMON encodes presence in most bacteria, while the note is only conditional/widespread.
    The inspected genomic survey does not support a majority. Use VARIABLE with its
    evidence limits.
  target_ids:
  - GO:0009288
  field_paths:
  - taxonomic_distribution[0].presence
  - taxonomic_distribution[0].reference
  evidence_ids:
  - record
  - distribution
  - paper-07
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum.yaml
    role: maintained scientific record
  rule_id: src/cellstructuremech/schema/cellstructuremech.yaml#PresenceEnum
  native_severity: major
  normalization_reason: Material evidence/scope defect under the native rubric.
- finding_id: F5
  issue_key: bacterial-flagellum-c-ring-assembly-condition
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Qualify C-ring assembly essentiality
  description: Unqualified ESSENTIAL omits the experimentally demonstrated FliI-overproduction
    bypass. Encode condition-dependent assembly, preserving mutant and partial-structure
    scope and the lack of restored motility.
  target_ids:
  - GO:0009288
  field_paths:
  - components[3].essentiality
  evidence_ids:
  - record
  - bypass
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#components
  native_severity: major
  normalization_reason: Material evidence/scope defect under the native rubric.
- finding_id: F6
  issue_key: bacterial-flagellum-grounding-todo-stale
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Narrow the completed portions of the grounding TODO
  description: The open prompt still requests a flagellin grounding already supplied
    as IPR001492 and repeats a FlgE decision already documented in grounding_notes.
    This directs future curation toward completed work.
  target_ids:
  - GO:0009288
  field_paths:
  - discussions[0].prompt
  - discussions[0].attaches_to
  evidence_ids:
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#discussions
  native_severity: minor
  normalization_reason: Bounded misleading curation guidance; native structure identity
    remains valid.
actions:
- action_id: A1
  description: Remove or source the 5-micrometer lower bound
  finding_ids:
  - F1
  target_ids:
  - GO:0009288
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum.yaml
    role: maintained scientific record
  generator: just text-embeddings-refresh; just render
  acceptance_checks:
  - Use only a source-supported range or upper bound, with organism/measurement context;
    do not infer a minimum from an upper limit.
  - Use guarded writer and append both histories; preserve PROPOSED and unrelated
    content. Run strict, labels, traits, history, QC and review-contract gates.
- action_id: A2
  description: Keep proposed stator rotation labeled as a model
  finding_ids:
  - F2
  target_ids:
  - GO:0009288
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum.yaml
    role: maintained scientific record
  generator: just text-embeddings-refresh; just render
  acceptance_checks:
  - Qualify the dynamic model in the claim-bearing description itself, or attach and
    inspect primary evidence that directly establishes that stronger claim. Do not
    imply that stator torque or A5B2 stoichiometry is merely hypothetical.
  - Use guarded writer and append both histories; preserve PROPOSED and unrelated
    content. Run strict, labels, traits, history, QC and review-contract gates.
- action_id: A3
  description: Distinguish proton and sodium motive forces
  finding_ids:
  - F3
  target_ids:
  - GO:0009288
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum.yaml
    role: maintained scientific record
  generator: just text-embeddings-refresh; just render
  acceptance_checks:
  - Use ion motive force with explicit ion-coupling scope, or split proton and sodium
    branches. Preserve the verified stator variants.
  - Use guarded writer and append both histories; preserve PROPOSED and unrelated
    content. Run strict, labels, traits, history, QC and review-contract gates.
- action_id: A4
  description: Use a supported bacterial prevalence category
  finding_ids:
  - F4
  target_ids:
  - GO:0009288
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum.yaml
    role: maintained scientific record
  generator: just text-embeddings-refresh; just render
  acceptance_checks:
  - Preserve patchy taxon/strain scope; do not turn a genomic proxy into direct observation
    or absence proof.
  - Use guarded writer and append both histories; preserve PROPOSED and unrelated
    content. Run strict, labels, traits, history, QC and review-contract gates.
- action_id: A5
  description: Qualify C-ring assembly essentiality
  finding_ids:
  - F5
  target_ids:
  - GO:0009288
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum.yaml
    role: maintained scientific record
  generator: just text-embeddings-refresh; just render
  acceptance_checks:
  - Prefer CONDITIONAL with explicit bypass context. Do not equate defective flagella
    with a functional motor or automatically reclassify every component of the separate
    C-ring record.
  - Use guarded writer and append both histories; preserve PROPOSED and unrelated
    content. Run strict, labels, traits, history, QC and review-contract gates.
- action_id: A6
  description: Narrow the completed portions of the grounding TODO
  finding_ids:
  - F6
  target_ids:
  - GO:0009288
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum.yaml
    role: maintained scientific record
  generator: just text-embeddings-refresh; just render
  acceptance_checks:
  - Narrow the prompt to remaining unresolved components; preserve posed_date and
    original rationale, appending current notes rather than deleting provenance.
  - Use guarded writer and append both histories; preserve PROPOSED and unrelated
    content. Run strict, labels, traits, history, QC and review-contract gates.
limitations:
- This is one record, not corpus-wide scientific approval. Native records, histories
  and generated pages were not edited; no GitHub issue was created by this audit.
- Full deterministic gates reuse verified successful CI at the unchanged durable main
  commit. Focused schema/strict and live trait checks were rerun; passing them does
  not establish biological truth.
- All cited DOI metadata and applicable authority identities were checked. Several
  older papers were accessible only as primary/review abstracts. Narrow claims supported
  there are assessed; unseen experimental detail is not certified.
- Review articles are explicitly labeled in evidence locators despite the shared schema
  having no separate secondary-source enum. They are not new experimental observations.
- Initial sandbox requests failed DNS. Some Europe PMC XML routes returned HTTP 500,
  some BioC requests returned a no-result body despite HTTP 200, and some publisher
  web routes failed. Actual readable publisher HTML, author manuscripts/PDF and abstracts
  were distinguished from failures.
- The first SubtiWiki/trait tool outputs were truncated; their processes were confirmed
  finished before a captured rerun. The captured dry-run and trait results passed.
  The PDF text extractor emitted font warnings; no verbatim new quotation or measurement
  relies on an ambiguous glyph.
- The iModulonDB adapter found gene identity hits but no module hit for the three
  explicit fliG searches. It supplies no direct evidence of cell-structure assembly
  or localization.
- The native target-kind scratch metadata was corrected from an invalid label to maintained.
  All original input hashes and the original durable Git base were rechecked unchanged;
  no scientific byte attestation was silently refreshed.
- Macnab 2003 full text and its diameter assertion remain unverified; this review
  is partial. Access failure itself did not generate a finding. The length lower-bound
  finding is independently established by inspected source text and the native acknowledgement.
```
