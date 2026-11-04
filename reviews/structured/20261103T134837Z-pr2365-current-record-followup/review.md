# PR 2365: current-input review of ten records and adversarial follow-up

- Review: 20261103T134837Z-pr2365-current-record-followup
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-11-03T13:37:13.889656Z
- Finished UTC: 2026-11-03T13:48:37Z
- Reviewer: Codex root synthesis with three independent read-only adversarial reviewers (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Current-input reassessment of all ten records in PR2365. One stale eyespot-apparatus review is substantively refreshed and eight structured-source applicability exclusions are corrected. Three inherited minor scientific findings remain open for separate record curation; no records are edited.

## Scope And Provenance

Exact ten-record PR cohort reassessed against current main 948585dbdfa24febd7412aa677c2251ac88c9cff. Changed inputs are substantively reassessed. Scientific records remain unchanged.

Selection: Complete cohort of ten maintained records reviewed in original PR head 6a8478248be0609ee4c6b873ba243b0105311365.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base 5c140efd0be92d341410aa3024d677d5daf8bc1e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0031904 | data/structures/membrane_organelle/endosome_lumen.yaml | maintained | endosome lumen |
| GO:0010008 | data/structures/membrane_organelle/endosome_membrane.yaml | maintained | endosome membrane |
| GO:7770040 | data/structures/membrane_organelle/epiplastidial_membrane.yaml | maintained | epiplastidial membrane |
| GO:0012507 | data/structures/membrane_organelle/er_to_golgi_transport_vesicle_membrane.yaml | maintained | ER to Golgi transport vesicle membrane |
| GO:0033117 | data/structures/membrane_organelle/esterosome.yaml | maintained | esterosome |
| GO:0034467 | data/structures/membrane_organelle/esterosome_lumen.yaml | maintained | esterosome lumen |
| GO:0033118 | data/structures/membrane_organelle/esterosome_membrane.yaml | maintained | esterosome membrane |
| GO:0044311 | data/structures/membrane_organelle/exoneme.yaml | maintained | exoneme |
| GO:1990413 | data/structures/membrane_organelle/eyespot_apparatus.yaml | maintained | eyespot apparatus |
| cellstructuremech:ferrosome | data/structures/membrane_organelle/ferrosome.yaml | maintained | ferrosome |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full native QC | passed | True | GO:0031904, GO:0010008, GO:7770040, GO:0012507, GO:0033117, GO:0034467, GO:0033118, GO:0044311, GO:1990413, cellstructuremech:ferrosome | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| Native label correspondence | passed | True | GO:0031904, GO:0010008, GO:7770040, GO:0012507, GO:0033117, GO:0034467, GO:0033118, GO:0044311, GO:1990413, cellstructuremech:ferrosome | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| TraitMech references | passed | True | GO:0031904, GO:0010008, GO:7770040, GO:0012507, GO:0033117, GO:0034467, GO:0033118, GO:0044311, GO:1990413, cellstructuremech:ferrosome | Native TraitMech link check passed. |
| Pinned governed files | passed | True | GO:0031904, GO:0010008, GO:7770040, GO:0012507, GO:0033117, GO:0034467, GO:0033118, GO:0044311, GO:1990413, cellstructuremech:ferrosome | Pinned governed files match; native vendored check passed. |
| Native identifier resolver | passed | True | GO:0031904, GO:0010008, GO:7770040, GO:0012507, GO:0033117, GO:0034467, GO:0033118, GO:0044311, GO:1990413, cellstructuremech:ferrosome | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| validate GO:0031904 | passed | True | GO:0031904 | Documented focused command passed. |
| validate-strict GO:0031904 | passed | True | GO:0031904 | Documented focused command passed. |
| validate GO:0010008 | passed | True | GO:0010008 | Documented focused command passed. |
| validate-strict GO:0010008 | passed | True | GO:0010008 | Documented focused command passed. |
| validate GO:7770040 | passed | True | GO:7770040 | Documented focused command passed. |
| validate-strict GO:7770040 | passed | True | GO:7770040 | Documented focused command passed. |
| validate GO:0012507 | passed | True | GO:0012507 | Documented focused command passed. |
| validate-strict GO:0012507 | passed | True | GO:0012507 | Documented focused command passed. |
| validate GO:0033117 | passed | True | GO:0033117 | Documented focused command passed. |
| validate-strict GO:0033117 | passed | True | GO:0033117 | Documented focused command passed. |
| validate GO:0034467 | passed | True | GO:0034467 | Documented focused command passed. |
| validate-strict GO:0034467 | passed | True | GO:0034467 | Documented focused command passed. |
| validate GO:0033118 | passed | True | GO:0033118 | Documented focused command passed. |
| validate-strict GO:0033118 | passed | True | GO:0033118 | Documented focused command passed. |
| validate GO:0044311 | passed | True | GO:0044311 | Documented focused command passed. |
| validate-strict GO:0044311 | passed | True | GO:0044311 | Documented focused command passed. |
| validate GO:1990413 | passed | True | GO:1990413 | Documented focused command passed. |
| validate-strict GO:1990413 | passed | True | GO:1990413 | Documented focused command passed. |
| validate cellstructuremech:ferrosome | passed | True | cellstructuremech:ferrosome | Documented focused command passed. |
| validate-strict cellstructuremech:ferrosome | passed | True | cellstructuremech:ferrosome | Documented focused command passed. |
| Supplemental bounded PMID authority checks | passed | True | GO:0031904, GO:0010008, GO:7770040, GO:0012507, GO:0033117, GO:0034467, GO:0033118, GO:0044311, GO:1990413, cellstructuremech:ferrosome | 909 PMIDs all OK in bounded native requests; full-command limitations remain separate. |
| Official structured-source applicability and covered-dataset cross-checks | passed | False | GO:0031904, GO:0010008, GO:7770040, GO:0012507, GO:0033117, GO:0034467, GO:0033118, GO:0044311, GO:1990413, cellstructuremech:ferrosome | Eight explicit narrow exclusions are corrected after inspecting positive molecular and pathway assertions. Official catalogue responses and bounded organism/strain searches found no matching datasets for the reviewed native hosts; heterologous expression and unrelated-organism datasets are not substituted. Epiplastidial membrane and esterosome membrane remain genuinely excluded by their limited material/topology claims. Catalogue noncoverage is not biological absence. Historical runner unavailability retains its actual date and is not a fresh invocation. |
| Independent claim-level source review | passed | True | GO:0031904, GO:0010008, GO:7770040, GO:0012507, GO:0033117, GO:0034467, GO:0033118, GO:0044311, GO:1990413, cellstructuremech:ferrosome | Three read-only reviewers covered the complete ten-record cohort, including changed inputs, with explicit scientific findings and source-access limits. Final artifact/head acceptance occurs after saving. |
| Retained historical adapter runner availability | unavailable | False | GO:0031904, GO:0010008, GO:7770040, GO:0012507, GO:0033117, GO:0034467, GO:0033118, GO:0044311, GO:1990413, cellstructuremech:ferrosome | Historical 00:49Z invocation unavailable due to OS access restriction. Official catalogue source fallback was inspected separately; no current invocation or successful adapter execution is claimed. The actual historical exit code 1 is retained in the evidence receipt, since the native unavailable-check model has no execution exit-code field. |
| Native endosome lumen UniProt verify check | passed | True | GO:0031904 | Read-only native command returned zero. Represented protein inventory and typed molecular-node coverage are empty; narrative claims remain separately assessed. |
| Native endosome lumen UniProt causal check | passed | True | GO:0031904 | Read-only native command returned zero. Represented protein inventory and typed molecular-node coverage are empty; narrative claims remain separately assessed. |
| Native endosome membrane UniProt verify check | passed | True | GO:0010008 | Read-only native command returned zero. The Vps27 P40343 xref is verified; one UNANCHORED_WITH_UNIPROT node is an allowed transient actor without component_ref, not a dangling component. |
| Native endosome membrane UniProt causal check | passed | True | GO:0010008 | Read-only native command returned zero. The Vps27 P40343 xref is verified; one UNANCHORED_WITH_UNIPROT node is an allowed transient actor without component_ref, not a dangling component. |
| Native epiplastidial membrane UniProt verify check | passed | True | GO:7770040 | Read-only native command returned zero. Represented protein inventory and typed molecular-node coverage are empty; narrative claims remain separately assessed. |
| Native epiplastidial membrane UniProt causal check | passed | True | GO:7770040 | Read-only native command returned zero. Represented protein inventory and typed molecular-node coverage are empty; narrative claims remain separately assessed. |
| Native ER to Golgi transport vesicle membrane UniProt verify check | passed | True | GO:0012507 | Read-only native command returned zero. Represented protein inventory and typed molecular-node coverage are empty; named COPII narrative actors remain separately assessed. |
| Native ER to Golgi transport vesicle membrane UniProt causal check | passed | True | GO:0012507 | Read-only native command returned zero. Represented protein inventory and typed molecular-node coverage are empty; named COPII narrative actors remain separately assessed. |
| Native esterosome UniProt verify check | passed | True | GO:0033117 | Read-only native command returned zero. Two reviewed Dictyostelium examples cryS/P21837 and D2/P18142 are represented and verified; one typed node is COVERED. Primary localization remains separate from identity checks. |
| Native esterosome UniProt causal check | passed | True | GO:0033117 | Read-only native command returned zero. Two reviewed Dictyostelium examples cryS/P21837 and D2/P18142 are represented and verified; one typed node is COVERED. Primary localization remains separate from identity checks. |
| Native esterosome lumen UniProt verify check | passed | True | GO:0034467 | Read-only native command returned zero. Represented protein inventory and typed molecular-node coverage are empty; lumenal cargo assertions remain separately assessed. |
| Native esterosome lumen UniProt causal check | passed | True | GO:0034467 | Read-only native command returned zero. Represented protein inventory and typed molecular-node coverage are empty; lumenal cargo assertions remain separately assessed. |
| Native esterosome membrane UniProt verify check | passed | True | GO:0033118 | Read-only native command returned zero. Represented protein inventory and typed molecular-node coverage are empty; limited morphology/boundary claims remain separately assessed. |
| Native esterosome membrane UniProt causal check | passed | True | GO:0033118 | Read-only native command returned zero. Represented protein inventory and typed molecular-node coverage are empty; limited morphology/boundary claims remain separately assessed. |
| Native exoneme UniProt verify check | passed | True | GO:0044311 | Read-only native command returned zero. Two reviewed component examples SUB1/O61142 and PMX/Q8IAS0 plus substrate xrefs Q9TY95/Q8I0U8 are verified. Three typed nodes comprise two COVERED and one UNANCHORED_WITH_UNIPROT substrate-cohort actor; this is not proof of all mechanism or assembly necessity. |
| Native exoneme UniProt causal check | passed | True | GO:0044311 | Read-only native command returned zero. Two reviewed component examples SUB1/O61142 and PMX/Q8IAS0 plus substrate xrefs Q9TY95/Q8I0U8 are verified. Three typed nodes comprise two COVERED and one UNANCHORED_WITH_UNIPROT substrate-cohort actor; this is not proof of all mechanism or assembly necessity. |
| Native eyespot apparatus UniProt verify check | passed | True | GO:1990413 | Read-only native command returned zero. Two unreviewed Chlamydomonas examples Q8RUT8/cop4 and Q93WP2/acop1 are verified; one typed node is COVERED. The primary nomenclature bridge and membership scope are assessed separately. |
| Native eyespot apparatus UniProt causal check | passed | True | GO:1990413 | Read-only native command returned zero. Two unreviewed Chlamydomonas examples Q8RUT8/cop4 and Q93WP2/acop1 are verified; one typed node is COVERED. The primary nomenclature bridge and membership scope are assessed separately. |
| Native ferrosome UniProt verify check | passed | True | cellstructuremech:ferrosome | Read-only native command returned zero. Three unreviewed RS-1 DMR/Fez examples C4XH20, C4XH21 and C4XH22 are verified; one typed node is COVERED. Identity checks do not establish individual necessity or a universal fitness phenotype. |
| Native ferrosome UniProt causal check | passed | True | cellstructuremech:ferrosome | Read-only native command returned zero. Three unreviewed RS-1 DMR/Fez examples C4XH20, C4XH21 and C4XH22 are verified; one typed node is COVERED. Identity checks do not establish individual necessity or a universal fitness phenotype. |

## Scientific And Domain Assessments

### Represented protein inventory and graph actor coverage

schema: supported. Targets: GO:0031904.

No component protein_examples and zero GENE_OR_PROTEIN nodes in the complete current target; mechanical checks are empty-inventory scope. Both commands return0. Actual source identity/localization and narrative pathway scope are separately reviewed.

### Original immutable pair and frozen-input currentness

provenance: supported. Targets: GO:0031904.

Current target unchanged; original pair validates/renders and all 18 historical inputs match their source commit. No stale refresh or record correction claimed. Exact two EpM finding predecessors are preserved, without terminally resolving other historical issues.

### Complete current fields and optional inventories

completeness: supported. Targets: GO:0031904.

Whole maintained target, history, evidence, discussions and graph arrays read. No target image assets, verbatim snippets, trait links or quantitative properties to audit. No optional molecular inventory or guessed family/chemical identifier is manufactured. PROPOSED unchanged.

### Represented protein inventory and graph actor coverage

schema: supported. Targets: GO:0010008.

No component protein_examples; one GENE_OR_PROTEIN node is UNANCHORED_WITH_UNIPROT, carrying verified P40343 for external Vps27. This is permitted and does not require a fabricated component. Both commands return0. Actual source identity/localization and narrative pathway scope are separately reviewed.

### Original immutable pair and frozen-input currentness

provenance: supported. Targets: GO:0010008.

Current target unchanged; original pair validates/renders and all 17 historical inputs match their source commit. No stale refresh or record correction claimed. Exact two EpM finding predecessors are preserved, without terminally resolving other historical issues.

### Complete current fields and optional inventories

completeness: supported. Targets: GO:0010008.

Whole maintained target, history, evidence, discussions and graph arrays read. No target image assets, verbatim snippets, trait links or quantitative properties to audit. No optional molecular inventory or guessed family/chemical identifier is manufactured. PROPOSED unchanged.

### Represented protein inventory and graph actor coverage

schema: supported. Targets: GO:7770040.

No component protein_examples and zero GENE_OR_PROTEIN nodes in the complete current target; mechanical checks are empty-inventory scope. Both commands return0. Actual source identity/localization and narrative pathway scope are separately reviewed.

### Original immutable pair and frozen-input currentness

provenance: supported. Targets: GO:7770040.

Current target unchanged; original pair validates/renders and all 14 historical inputs match their source commit. No stale refresh or record correction claimed. Exact two EpM finding predecessors are preserved, without terminally resolving other historical issues.

### Complete current fields and optional inventories

completeness: supported. Targets: GO:7770040.

Whole maintained target, history, evidence, discussions and graph arrays read. No target image assets, verbatim snippets, trait links or quantitative properties to audit. No optional molecular inventory or guessed family/chemical identifier is manufactured. PROPOSED unchanged.

### Lumen versus membrane and MVB specialization

identity: supported. Targets: GO:0031904.

Exact GO target definition and kind agree; lumen and limiting membrane are distinct parts of endosome. MVB lumen is a specialized endosome lumen and local ILV denotes a whole internal vesicle. Supported specialized MVB context does not assert that every endosome contains ILVs.

### Yeast species and experimental strains

scope: supported. Targets: GO:0031904.

NCBITaxon4932 is S. cerevisiae. Primary abstract/body evidence supports the yeast MVB context. COMMON is qualitative, not measured prevalence. Katzmann2003 uses SEY6210 derivatives; P40343 S288C identity is a reference-strain accession, not a claim the experiments used S288C.

### Scoped ubiquitin-dependent MVB cargo sorting

evidence: supported. Targets: GO:0031904.

GO0071985, Katzmann2001 complete abstract and Katzmann2003 body support ubiquitinated membrane cargo entry into MVB internal vesicles. Henne is a secondary review, not an additional primary assay. The narrow function is not silently extended to every endosomal sorting route or universal molecular sequence.

### Actual pathway trigger and catalogue noncoverage

scope: supported. Targets: GO:0031904.

ESCRT-dependent MVB sorting is an explicit pathway assertion; membrane also names VPS27/P40343. The original check explicitly excludes iModulonDB for lack of expression inference, without coverage evidence. Current complete catalogue has no relevant yeast host, so no matched downstream query applies. Primary/authority fallback is completed; historical runner remains separately dated unavailable.

### Lumen versus membrane and MVB specialization

identity: supported. Targets: GO:0010008.

Exact GO target definition and kind agree; lumen and limiting membrane are distinct parts of endosome. MVB lumen is a specialized endosome lumen and local ILV denotes a whole internal vesicle. Supported specialized MVB context does not assert that every endosome contains ILVs.

### Yeast species and experimental strains

scope: supported. Targets: GO:0010008.

NCBITaxon4932 is S. cerevisiae. Primary abstract/body evidence supports the yeast MVB context. COMMON is qualitative, not measured prevalence. Katzmann2003 uses SEY6210 derivatives; P40343 S288C identity is a reference-strain accession, not a claim the experiments used S288C.

### Scoped ubiquitin-dependent MVB cargo sorting

evidence: supported. Targets: GO:0010008.

GO0071985, Katzmann2001 complete abstract and Katzmann2003 body support ubiquitinated membrane cargo entry into MVB internal vesicles. Henne is a secondary review, not an additional primary assay. The narrow function is not silently extended to every endosomal sorting route or universal molecular sequence.

### Actual pathway trigger and catalogue noncoverage

scope: supported. Targets: GO:0010008.

ESCRT-dependent MVB sorting is an explicit pathway assertion; membrane also names VPS27/P40343. The original check explicitly excludes iModulonDB for lack of expression inference, without coverage evidence. Current complete catalogue has no relevant yeast host, so no matched downstream query applies. Primary/authority fallback is completed; historical runner remains separately dated unavailable.

### Lumen as an internal region

grounding: supported. Targets: GO:0031904.

Empty constituent inventory is appropriate for the internal region. Enclosing membrane and ILVs are represented as boundary/content graph entities, not falsely made constitutive lipid/protein components of the lumen. Resolved local discussion agrees with actual membrane boundary node.

### All five NONMECHANISTIC topology edges

graph: supported. Targets: GO:0031904.

Lumen part_of endosome, MVB lumen is_a endosome lumen, endosome membrane bounds lumen, MVB is_a endosome, and ILV contained in MVB lumen are supported. Full ESCRT reaction or mandatory universal ILVs are not claimed.

### Beyond the scoped lumen topology

evidence: unknown. Targets: GO:0031904.

Detailed scission chemistry, exhaustive lumen cargo composition and primary2001 full-body experimental detail are not independently established by this bounded review.

### Collective lipid and transient external actors

grounding: supported. Targets: GO:0010008.

Generic lipid-bilayer constituent is REVIEWED_LABEL_ONLY with an explicit unresolved chemical grounding discussion; ESSENTIAL is collective defining constitution, not individual-lipid knockout necessity. Vps27/ESCRT actors remain graph nodes rather than invented stable membrane constituents. P40343 matches VPS27.

### All seven scoped membrane-topology and sorting edges

graph: supported. Targets: GO:0010008.

Parthood/enclosure and ILV formation/containment agree with authority definitions. Katzmann2003 supports Vps27 recruiting ESCRT-I; Katzmann2001 supports cargo sorting. Babst2002 abstract supports ESCRT-III membrane recruitment/oligomerization/sorting; Henne review and modern GO support broad membrane remodeling. NONMECHANISTIC scope does not assert precise scission chemistry or the full ESCRT cycle.

### Molecular necessity and scission detail

evidence: unknown. Targets: GO:0010008.

Exact lipid composition, necessity of every constituent and detailed ESCRT scission chemistry are outside the inspected evidence. The mechanical verifier and generic bilayer ESSENTIAL row do not establish those claims.

### Exact outermost complex-plastid membrane

identity: supported. Targets: GO:7770040.

GO7770040 exactly matches definition and five synonyms; plastid-membrane parentage and plastid parthood are supported. EpM/cERM is distinct from second-outer PPM7770041 and plastid-envelope outer membrane0009527. Native definition reproduced accurately; primary sources qualify diatom ER continuity and discuss other lineage differences.

### Diatom primary imaging context

scope: supported. Targets: GO:7770040.

Taxon2850 is P. tricornutum. Flori2016 Pt1 CCAP1055/3 FIB-SEM supports canonical ultrastructure; intact/disrupted cells are distinguished. Gueguen2024 uses Pt1 Strain8.6 CCAP1055/1. COMMON remains qualitative; distinct culture-collection designations are not silently equated.

### Unspecified collective epiplastidial lipid bilayer

grounding: supported. Targets: GO:7770040.

The generic LIPID row is defining collective bilayer material, intentionally REVIEWED_LABEL_ONLY. Exact mixture/individual lipid necessity is not asserted. Gueguen source title names MGD enzymes but the record does not positively assert specific enzymes, transport machinery or stress-response pathways.

### Immediate membrane interface versus nested enclosure

evidence: concern. Targets: GO:7770040.

The function says EpM separates PPC from the host endomembrane system. Primary topology places the PPC between PPM and oEM, and EpM is itself continuous with host ER/outer nuclear membrane. An outer membrane can indirectly enclose PPC, so the wording is not treated as a proven false enclosure claim; it needs the adjacent spaces specified to avoid attributing the PPM interface to EpM.

### Descriptive bilayer forms boundary graph

graph: concern. Targets: GO:7770040.

The graph consists of collective bilayer formation of the named membrane and outer-boundary maintenance. These relations describe identity and topology; the cited sources do not establish a molecular causal sequence represented by the current nodes and edges.

### Genuine material/topology exclusion

scope: not_applicable. Targets: GO:7770040.

Complete maintained record asserts lipid constitution, nested compartment boundaries, host-derived origin and ER continuity, without a positive gene/regulator/pathway/stress/transcriptomic assertion. Merely citing the MGD paper title does not import all its molecular claims into the record. This is a genuine scope exclusion, not an additional adapter defect; fresh catalogue also has no P. tricornutum match.

### Specific lipid necessity and evolutionary scope

evidence: unknown. Targets: GO:7770040.

Exact lipid pools/formation necessities and molecular maintenance mechanism remain unresolved. MGDgamma localization in ER/periphery is qualified; no exact EpM composition is inferred. Diatom ER continuity is not extrapolated to all secondary-plastid lineages, and source evolutionary alternatives remain hypotheses.

### Exoneme organelle and apical-complex relation

identity: supported. Targets: GO:0044311.

The native class/parent/parthood match. The maintained functions correctly describe discharge of soluble protease cargo into PV rather than assuming an entire stable organelle is released intact; full-record interpretation preserves this distinction.

### P. falciparum blood-stage evidence

scope: supported. Targets: GO:0044311.

The directly evidenced species, schizont/merozoite stages and canonical discharge/egress example match the primary abstract and later primary main text. COMMON is qualitative occurrence, not a counted frequency or all-apicomplexan claim. The record explicitly narrowed broader historical taxonomy.

### SUB1 and PMX components versus representative identity metadata

grounding: supported. Targets: GO:0044311.

Primary literature supports PfSUB1 exoneme cargo and PMX localization/dependence. Native examples and graph xrefs identify the exact species/isolate proteins and SERA5/MSP1 exemplars; xrefs do not equate the entire substrate cohort with just those two proteins. Native by-similarity annotations and historical dense-granule descriptions are not counted as independent direct exoneme experiments.

### Resolvable SUB1 family and unresolved exact PMX family

grounding: concern. Targets: GO:0044311.

IPR017314 is a verified whole-SUB1 family and O61142 directly carries it. The component’s unresolved-family rationale is stale for SUB1. IPR034204 is a domain and IPR001461 is broader than PMX, so neither is forced as an exact substitute for the remaining component.

### Protease activity requirement versus organelle formation

grounding: unknown. Targets: GO:0044311.

The studies establish important protease maturation, egress and invasion effects, but do not establish that loss of each cargo enzyme prevents formation of the exoneme compartment. Both UNKNOWN assembly-necessity entries are appropriate; catalytic essentiality is not silently converted to organelle-assembly necessity.

### Eight qualified egress pathway edges

graph: supported. Targets: GO:0044311.

Localization/storage, discharge into PV, PMX-supported SUB1 processing, downstream SERA/MSP processing and contributions to egress/invasion are supported at the stated evidence tiers. Nasamu directly supports the dependence, while its in-vivo direct-cleavage uncertainty is preserved by “supports maturation.” Withers provides reviewed background for discharge and substrate processing inside a primary structural paper, not an independent new discharge experiment. This graph represents a causal proteolytic sequence and its MECHANISTIC classification is justified within those limits.

### Full maintained record and bounded scientific coverage

completeness: supported. Targets: GO:0044311.

Every maintained claim, graph edge and discussion was inspected. No quantitative physical-property field, maintained image/licence asset or verbatim evidence snippet is present. Existing PROPOSED status and history remain unchanged. No finding is invented from optional unresolved molecular inventory or unavailable full-text routes alone.

### Immutable original and current native coverage

schema: supported. Targets: GO:0044311.

Original validates/renders identically and historical frozen input verified. Current root native protein commands exit0 with actual inventory limits; no scientific inference from status alone.

### Molecular/pathway applicability and exact catalogue coverage

evidence: not_applicable. Targets: GO:0044311.

Existing expression-only N/A rationale is deficient: this target asserts named proteins/pathways. Fresh official catalogue has no target organism/strain match; no downstream module keys or unmatched proxy invented. Historical runner unavailability is separately dated; this is a bounded source applicability result, not biological negative evidence.

### Eyespot apparatus across membrane systems

identity: supported. Targets: GO:1990413.

Exact GO1990413 definition and two RELATED synonyms agree. OTHER kind avoids misrepresenting the apparatus as one isolated membrane-bounded compartment: original sources place plasma-membrane photoreceptors over chloroplast-associated pigment granules. An empty optional parent/parthood slot is not an identity defect.

### Chlamydomonas scope and study contexts

scope: supported. Targets: GO:1990413.

Species3055 label and canonical/distribution scope agree. Lamb full abstract supports assembly/positioning mutant context; Schmidt cw15 fraction purification supports proteomics example. Mittelmeier uses137c/CC125 and specific mutants; Awasthi uses conditional IFT strains. COMMON is qualitative occurrence, not a prevalence count or all-algae claim.

### Pigment and photoreceptor cohorts

grounding: supported. Targets: GO:1990413.

Current Q8RUT8/cop4 and newly added Q93WP2/acop1 are unreviewed tax3055 examples. Schmidt Table1 bridges COP3/CHOP1/CSRA/Acop1 and COP4/CHOP2/CSRB/Acop2; primary fraction peptides support the represented cohort, with contamination limits. Empty literal COP3 query does not contradict the literature alias. Broad IPR001425 opsin family does not exactly resolve the channelrhodopsin cohort.

### Plural cohort versus directly imaged member

evidence: supported. Targets: GO:1990413.

Mittelmeier directly localizes ChR1; Awasthi provides ChR1/Cop8 trafficking and background COP3/4 identity. The already cited record-level Schmidt paper detects both COP3 and COP4, preserving support for the plural cohort. The review does not claim a direct ChR2 localization experiment in the first two papers or transfer all IFT controls to ChR2.

### Shielding and directional phototactic sign

evidence: supported. Targets: GO:1990413.

Ueki mutant/rescue, redox-biased assays and directly observed cellular lens effect support carotenoid-layer shielding and correct phototactic sign. Eyeless cells can retain photoreception and show strong responses under the tested conditions; the target uses supports/directional detection and UNKNOWN essentiality, rather than claiming all phototaxis requires a pigmented eyespot.

### All four descriptive light-detection edges

graph: supported. Targets: GO:1990413.

Pigment concentration, photoreceptor localization, shielding and support for directional detection are supported at the broad Chlamydomonas cohort level. The direct localization example is ChR1, and Ueki Fig6 is a model integrating the mutant and lens observations. NONMECHANISTIC scope does not claim a complete ion-channel/flagellar signaling cascade.

### Unknown formation requirements and proteome completeness

evidence: unknown. Targets: GO:1990413.

UNKNOWN component essentiality is appropriate: phototactic defects and reduced pigment do not establish a general absence-of-each-component structure-formation test. Whole-cell carotenoid HPLC does not resolve all eyespot-stored chemical species; fraction proteomics allows contamination. Optional family groundings and candidate constituents remain an explicit curation TODO, not a proof that all candidates are absent.

### Full maintained target and honest scope

completeness: supported. Targets: GO:1990413.

Entire target and every graph edge were read. There are no target image assets, measurements, trait links or verbatim evidence snippets to verify. Optional molecular inventories and family groundings remain acknowledged; no finding is invented from an empty optional slot. PROPOSED status and historical events are retained.

### Immutable original and current native coverage

schema: supported. Targets: GO:1990413.

Original validates/renders identically and historical frozen input verified. Current root native protein commands exit0 with actual inventory limits; no scientific inference from status alone.

### Molecular/pathway applicability and exact catalogue coverage

evidence: not_applicable. Targets: GO:1990413.

Existing expression-only N/A rationale is deficient: this target asserts named proteins/pathways. Fresh official catalogue has no target organism/strain match; no downstream module keys or unmatched proxy invented. Historical runner unavailability is separately dated; this is a bounded source applicability result, not biological negative evidence.

### Minted ferrosome versus magnetosome

identity: supported. Targets: cellstructuremech:ferrosome.

Exact local identifier uniquely denotes lipid-bounded amorphous iron-storage organelle, distinct from bullet-shaped magnetite crystals. Parent GO0043231 is compatible with the physical organelle, without claiming a native GO ferrosome child. Bounded exact search returned zero, not worldwide ontology absence.

### Exact Fez locus bridges and family/cohort limits

grounding: supported. Targets: cellstructuremech:ferrosome.

Grant explicitly bridges FezA/B/C to DMR28320/30/40, matching the three native RS-1 entries and their unreviewed statuses. Their grouped representation is a cohort, not one proven stoichiometric protein complex. Broad P-typeATPase or HMA-domain descriptions cannot exactly ground all three unrelated proteins. The acknowledged family/component-boundary TODO remains justified.

### Membrane and unresolved amorphous core chemistry

grounding: supported. Targets: cellstructuremech:ferrosome.

Byrne directly reports membrane-surrounded amorphous granules with Fe/P/O enrichment. This supports collective lipid boundary and chemically unresolved storage material; it does not identify a single mineral, free ion or molecular formula suitable for an exact CHEBI substitution. The existing label-only states and chemistry TODO preserve that uncertainty.

### Collective formation dependence versus individual requirements

grounding: unknown. Targets: cellstructuremech:ferrosome.

FezBC deletion/complementation supports the represented cohort-level dependence, but individual requirements for all three unrelated proteins are not separately demonstrated. UNKNOWN is retained for the cohort and exact core chemistry. The ESSENTIAL lipid row denotes the complete boundary material; individual lipid-species necessity or removal/substitution requirements are not measured. No catalytic or stoichiometric inference is substituted for formation necessity.

### RS-1 taxon and canonical ultrastructure

scope: supported. Targets: cellstructuremech:ferrosome.

The current strain name and historical Desulfovibrio name are natively bridged. RS-1 supplies Fez proteomics/genetics and Byrne ultrastructure, while the listed iron-rich growth/iron-transition context matters: COMMON is qualitative capacity/occurrence, not constitutive granules in every cell. The taxon note connects the RS-1 formation work to the study-level storage interpretation; it does not expressly claim that RS-1 supplied the iron-starvation fitness assay.

### Supported iron-storage interpretation with species-specific direct tests

evidence: supported. Targets: cellstructuremech:ferrosome.

The class-level storage function is supported by Grant’s iron accumulation/genetics and S. putrefaciens anaerobic iron-limitation growth/rescue assays, together with RS-1 structural storage evidence. Direct anaerobic fitness benefit was not measured for every ferrosome-producing species. The record’s generic function is read within this evidence scope, not as a quantified universal phenotype or demonstrated FezB transport substrate.

### Four explicitly NONMECHANISTIC formation/storage edges

graph: supported. Targets: cellstructuremech:ferrosome.

The graph preserves observed Fez-dependent formation, lipid enclosure, core accumulation and storage function without claiming a resolved molecular membrane-biogenesis mechanism, iron-transport reaction or core chemical species. This matches the primary results and their uncertainties.

### Full maintained record and bounded scientific coverage

completeness: supported. Targets: cellstructuremech:ferrosome.

Every maintained claim, graph edge and discussion was inspected. No quantitative physical-property field, maintained image/licence asset or verbatim evidence snippet is present. Existing PROPOSED status and history remain unchanged. No finding is invented from optional unresolved molecular inventory or unavailable full-text routes alone.

### Immutable original and current native coverage

schema: supported. Targets: cellstructuremech:ferrosome.

Original validates/renders identically and historical frozen input verified. Current root native protein commands exit0 with actual inventory limits; no scientific inference from status alone.

### Molecular/pathway applicability and exact catalogue coverage

evidence: not_applicable. Targets: cellstructuremech:ferrosome.

Existing expression-only N/A rationale is deficient: this target asserts named proteins/pathways. Fresh official catalogue has no target organism/strain match; no downstream module keys or unmatched proxy invented. Historical runner unavailability is separately dated; this is a bounded source applicability result, not biological negative evidence.

### Substantive reassessment of added acop1 example

evidence: supported. Targets: GO:1990413.

New Q93WP2/acop1, unreviewed tax3055, is correct by current native authority. Literature Table1 explicitly bridges COP3 to Acop1; current deterministic coverage moves the single node to COVERED. Accession identity is separate from apparatus association: direct ChR1 localization and proteomic COP3 detection supply that scope. No source claim transferred from ChR1 to all ChR2 or Cop8 experiments.

### Original schema/render and unchanged frozen target

schema: supported. Targets: GO:0012507.

Original native validation and deterministic rendering pass; original frozen, historical-source and current target bytes agree. None of these four targets is stale.

### Represented protein inventory and typed graph coverage

provenance: supported. Targets: GO:0012507.

No protein_examples, protein UniProtKB graph xrefs or GENE_OR_PROTEIN nodes are represented. Exit zero validates this empty represented inventory only, not narrative named molecules, pathway behavior, source localization or completeness.

### Target images, measurements, traits and snippets

scope: not_applicable. Targets: GO:0012507.

No target image, quantitative property, trait link or verbatim snippet is declared. Source OCR/caption inspection is not source figure-pixel, sequence-alignment or raw-data reanalysis.

### Scientific status and previous findings

provenance: supported. Targets: GO:0012507.

PROPOSED status and histories remain unchanged. Original findings/actions are empty; no prior finding identity or severity normalization is invented. Existing discussion resolutions explain scope, not a current terminal disposition of historical or neighboring issues.

### Original schema/render and unchanged frozen target

schema: supported. Targets: GO:0033117.

Original native validation and deterministic rendering pass; original frozen, historical-source and current target bytes agree. None of these four targets is stale.

### Represented protein inventory and typed graph coverage

provenance: supported. Targets: GO:0033117.

Two exact reviewed protein examples P21837/cryS and P18142/D2 validate; the one GENE_OR_PROTEIN node is COVERED through its component_ref. This covers declared identifiers and symbols, not exact family grounding, source localization, stoichiometry, necessity or completeness.

### Target images, measurements, traits and snippets

scope: not_applicable. Targets: GO:0033117.

No target image, quantitative property, trait link or verbatim snippet is declared. Source OCR/caption inspection is not source figure-pixel, sequence-alignment or raw-data reanalysis.

### Scientific status and previous findings

provenance: supported. Targets: GO:0033117.

PROPOSED status and histories remain unchanged. Original findings/actions are empty; no prior finding identity or severity normalization is invented. Existing discussion resolutions explain scope, not a current terminal disposition of historical or neighboring issues.

### Original schema/render and unchanged frozen target

schema: supported. Targets: GO:0034467.

Original native validation and deterministic rendering pass; original frozen, historical-source and current target bytes agree. None of these four targets is stale.

### Represented protein inventory and typed graph coverage

provenance: supported. Targets: GO:0034467.

No protein_examples, protein UniProtKB graph xrefs or GENE_OR_PROTEIN nodes are represented. Exit zero validates this empty represented inventory only, not narrative named molecules, pathway behavior, source localization or completeness.

### Target images, measurements, traits and snippets

scope: not_applicable. Targets: GO:0034467.

No target image, quantitative property, trait link or verbatim snippet is declared. Source OCR/caption inspection is not source figure-pixel, sequence-alignment or raw-data reanalysis.

### Scientific status and previous findings

provenance: supported. Targets: GO:0034467.

PROPOSED status and histories remain unchanged. Original findings/actions are empty; no prior finding identity or severity normalization is invented. Existing discussion resolutions explain scope, not a current terminal disposition of historical or neighboring issues.

### Original schema/render and unchanged frozen target

schema: supported. Targets: GO:0033118.

Original native validation and deterministic rendering pass; original frozen, historical-source and current target bytes agree. None of these four targets is stale.

### Represented protein inventory and typed graph coverage

provenance: supported. Targets: GO:0033118.

No protein_examples, protein UniProtKB graph xrefs or GENE_OR_PROTEIN nodes are represented. Exit zero validates this empty represented inventory only, not narrative named molecules, pathway behavior, source localization or completeness.

### Target images, measurements, traits and snippets

scope: not_applicable. Targets: GO:0033118.

No target image, quantitative property, trait link or verbatim snippet is declared. Source OCR/caption inspection is not source figure-pixel, sequence-alignment or raw-data reanalysis.

### Scientific status and previous findings

provenance: supported. Targets: GO:0033118.

PROPOSED status and histories remain unchanged. Original findings/actions are empty; no prior finding identity or severity normalization is invented. Existing discussion resolutions explain scope, not a current terminal disposition of historical or neighboring issues.

### Complete-record molecular applicability and target-host catalogue coverage

scope: not_applicable. Targets: GO:0012507.

Named molecular/pathway assertions trigger applicability assessment despite descriptive topology. Fresh complete official catalogue lacks the actual yeast/Dictyostelium host, so downstream queries are not applicable. Correct the original unsupported exemption in the review successor; preserve the actual historical runner failure and avoid negative-biology or unrelated-host claims.

### Complete-record molecular applicability and target-host catalogue coverage

scope: not_applicable. Targets: GO:0033117.

Named molecular/pathway assertions trigger applicability assessment despite descriptive topology. Fresh complete official catalogue lacks the actual yeast/Dictyostelium host, so downstream queries are not applicable. Correct the original unsupported exemption in the review successor; preserve the actual historical runner failure and avoid negative-biology or unrelated-host claims.

### Complete-record molecular applicability and target-host catalogue coverage

scope: not_applicable. Targets: GO:0034467.

Named molecular/pathway assertions trigger applicability assessment despite descriptive topology. Fresh complete official catalogue lacks the actual yeast/Dictyostelium host, so downstream queries are not applicable. Correct the original unsupported exemption in the review successor; preserve the actual historical runner failure and avoid negative-biology or unrelated-host claims.

### Genuine material and boundary-morphology exclusion

scope: not_applicable. Targets: GO:0033118.

The complete record asserts a generic lipid bilayer, crystal-filled lumen, RER-like boundary morphology and descriptive parthood. It names no cryS/D2 accession or gene and explicitly avoids ER-trafficking/nucleation mechanisms. This supports genuine molecular-query exclusion. Clarify the older generic rationale without manufacturing an extra bundle defect; the sparse scope, rather than a lack of expression claims, is the basis.

### Exact bilayer identity, synonym, parentage and containing carrier

identity: supported. Targets: GO:0012507.

GO0012507 exactly defines the surrounding ER-to-Golgi transport-vesicle lipid bilayer; its COPII synonym, transport/coated-membrane parents and COPII whole-vesicle parthood are verified by native typed GO entries.

### Generic bilayer component and coat boundary

grounding: supported. Targets: GO:0012507.

REVIEWED_LABEL_ONLY explicitly leaves chemical specificity open while correctly identifying collective lipid-bilayer constitution. Sar1/Sec complexes are coat machinery, not automatically direct bilayer constituents. GO coat parthood does not require treating that associated protein coat as the lipid material itself. No exact chemical-ontology absence is claimed.

### Yeast COPII model and actual source tiers

scope: supported. Targets: GO:0012507.

Exact S.cerevisiae identity and the yeast COPII ER-derived vesicle example are supported by GO and the complete Barlowe abstract. Matsuoka explicitly names purified Sar1, Sec13/31 and Sec23/24. COMMON is qualitative occurrence, not measured population prevalence; no uninspected full methods, detailed strains or figure-panel inference is certified.

### Three descriptive parthood, boundary and ER-donor relations

graph: supported. Targets: GO:0012507.

Part_of and bounds follow GO identity. ER membrane donation is supported by GO0090114 evagination and Barlowe ER-membrane budding; Matsuoka supplies complementary synthetic-liposome reconstitution, not a direct native-ER composition measurement. NONMECHANISTIC scope does not duplicate coat assembly or assert every lipid is necessary.

### Collective bilayer versus molecular requirement

grounding: unknown. Targets: GO:0012507.

ESSENTIAL applies to the defining collective bilayer. Specific lipid removal/substitution necessity in native membranes is not established by the cited source tiers, and no such individual requirement is asserted.

### Dictyostelium stage/strain and morphology context

scope: supported. Targets: GO:0033117.

Exact D.discoideum identity is current. Bomblies directly examines aggregation-stage crystals and membrane morphology, mostly AX2-214, with AX3 used for specified sequence/transcript work. The maintained qualitative COMMON/example wording is stage-bounded and does not assert pan-amoebal distribution, uniform abundance or live trafficking.

### Morphology and protein association versus unresolved physiology

evidence: supported. Targets: GO:0033117.

The paper supports membrane-enclosed crystals and RER-like boundary morphology. It explicitly leaves co-crystallization detail/ratio, ER sorting, nucleation, crystal fate and physiological function unresolved. OCR prose and caption text were inspected; raw data, alignment calculations and figure pixels were not reanalyzed.

### Dictyostelium stage/strain and morphology context

scope: supported. Targets: GO:0034467.

Exact D.discoideum identity is current. Bomblies directly examines aggregation-stage crystals and membrane morphology, mostly AX2-214, with AX3 used for specified sequence/transcript work. The maintained qualitative COMMON/example wording is stage-bounded and does not assert pan-amoebal distribution, uniform abundance or live trafficking.

### Morphology and protein association versus unresolved physiology

evidence: supported. Targets: GO:0034467.

The paper supports membrane-enclosed crystals and RER-like boundary morphology. It explicitly leaves co-crystallization detail/ratio, ER sorting, nucleation, crystal fate and physiological function unresolved. OCR prose and caption text were inspected; raw data, alignment calculations and figure pixels were not reanalyzed.

### Dictyostelium stage/strain and morphology context

scope: supported. Targets: GO:0033118.

Exact D.discoideum identity is current. Bomblies directly examines aggregation-stage crystals and membrane morphology, mostly AX2-214, with AX3 used for specified sequence/transcript work. The maintained qualitative COMMON/example wording is stage-bounded and does not assert pan-amoebal distribution, uniform abundance or live trafficking.

### Morphology and protein association versus unresolved physiology

evidence: supported. Targets: GO:0033118.

The paper supports membrane-enclosed crystals and RER-like boundary morphology. It explicitly leaves co-crystallization detail/ratio, ER sorting, nucleation, crystal fate and physiological function unresolved. OCR prose and caption text were inspected; raw data, alignment calculations and figure pixels were not reanalyzed.

### Exact whole organelle and its two parts

identity: supported. Targets: GO:0033117.

GO0033117 and SL0109 identify the whole esterosome as a cytoplasmic vesicle with crystalline esterase-like protein. GO/UniProt separately identify lumen and membrane; direct exact matches are distinguished from nested parental location mappings.

### Two exact reviewed protein examples

grounding: supported. Targets: GO:0033117.

Current P21837/cryS Crystal protein and P18142/D2 cAMP-regulated D2 protein are reviewed D.discoideum entries. These exact identities agree with the maintained examples and native coverage. Identity checks do not alone establish localization or necessity.

### Primary crystal cargo evidence and authority annotation granularity

evidence: supported. Targets: GO:0033117.

Purification, N-terminal/cDNA identity, protein-specific antibodies, serial sections and double-gold immunolabeling support cryS and D2 as major crystal-associated constituents. The paper explicitly describes lumenal rather than membrane-associated proteins. UniProt location SL0108 is therefore retained as coarse annotation context, not reassigned as direct bilayer membership. No exhaustive minor-protein inventory is asserted.

### Reviewed label-only family scope

grounding: supported. Targets: GO:0033117.

The complete current exact-protein InterPro responses contain a domain, conserved site, active site and homologous superfamily, but no integrated family-typed entry. Native guidance does not promote these types as a family consensus. Existing broad hydrolase similarity, exact verified proteins and the explicit family-grounding TODO do not establish an actionable deferred-family error here. The bounded response does not establish universal ontology absence.

### Observed crystal association and enclosing topology

graph: supported. Targets: GO:0033117.

The crystallize-in predicate is explicitly constrained by its co-fractionation/immunolabeling description and NONMECHANISTIC scope. It represents observed mature crystalline cargo, not purified binary co-crystallization, a fixed protein ratio, ER trafficking or a nucleation sequence. Membrane bounds lumen and membrane part_of whole are independently supported by exact identities and microscopy prose.

### Constitution versus protein formation necessity

grounding: unknown. Targets: GO:0033117.

Collective bounding membrane is essential by organelle definition; individual crystal-protein necessity remains UNKNOWN. Antibody localization, developmentally regulated abundance and cited D2 antisense phenotypes do not prove necessity for esterosome formation, and the paper discusses future genetic tests.

### Exact enclosed volume, broad is_a ancestry and parthood

identity: supported. Targets: GO:0034467.

GO0034467 and SL0328 identify the volume enclosed by esterosome membrane, provide the esterosomal-lumen synonym and whole-organelle parthood. The explicit is_a-only ancestor response verifies broad GO0043233, without falsely representing it as the direct native parent.

### Descriptive crystal storage versus unresolved biological role

evidence: supported. Targets: GO:0034467.

The storage function description states only that the internal compartment is occupied by crystalline esterase-like cargo. Bomblies supports that observed sequestration and cryS/D2 cargo context, but not a defined physiological storage purpose, catalysis or release route. Empty direct components are consistent with region identity and the maintained whole-organelle cargo model.

### Two descriptive lumen and boundary edges

graph: supported. Targets: GO:0034467.

Lumen part_of esterosome and membrane encloses lumen follow exact GO/UniProt identities and the source membrane-enclosed crystals. The boundary membrane is not a lumen constituent; no unobserved molecular transport or nucleation step is added.

### Exact membrane identity, synonym, parent and parthood

identity: supported. Targets: GO:0033118.

GO0033118 and SL0108 identify the surrounding bilayer, esterosomal-membrane synonym, cytoplasmic-vesicle-membrane parent and esterosome parthood. This is the boundary structure, not its crystal cargo or whole organelle.

### Collective lipid bilayer and RER-like morphology

grounding: supported. Targets: GO:0033118.

Generic bilayer constitution and RER-like boundary are supported by native definition and the primary microscopy prose. Reviewed-label-only chemical specificity is explicitly acknowledged. No exact lipid species, membrane-protein inventory, biochemical ER identity or trafficking continuity is claimed.

### Boundary function and two topological edges

graph: supported. Targets: GO:0033118.

The function and graph specify membrane parthood and lumen enclosure, supported by exact definitions and the membrane-enclosed crystal observations. NONMECHANISTIC scope explicitly excludes ER-trafficking and nucleation.

### Individual molecular requirements

grounding: unknown. Targets: GO:0033118.

ESSENTIAL denotes the defining collective bilayer, not an experimentally required lipid species or named protein. No individual molecular formation requirement is established or asserted.

### Qualified scientific acceptance with explicit access and inference limits

evidence: supported. Targets: GO:0012507.

No concrete scientific record correction was established for this complete assigned target. Preserve exact source tiers, authority/primary distinctions, experimental scope, unknown necessity and represented-inventory limits. Three actual applicability defects are transmitted separately; the sparse esterosome membrane is genuinely excluded. No scientific finding, predecessor identity or historical issue resolution is invented.

### Qualified scientific acceptance with explicit access and inference limits

evidence: supported. Targets: GO:0033117.

No concrete scientific record correction was established for this complete assigned target. Preserve exact source tiers, authority/primary distinctions, experimental scope, unknown necessity and represented-inventory limits. Three actual applicability defects are transmitted separately; the sparse esterosome membrane is genuinely excluded. No scientific finding, predecessor identity or historical issue resolution is invented.

### Qualified scientific acceptance with explicit access and inference limits

evidence: supported. Targets: GO:0034467.

No concrete scientific record correction was established for this complete assigned target. Preserve exact source tiers, authority/primary distinctions, experimental scope, unknown necessity and represented-inventory limits. Three actual applicability defects are transmitted separately; the sparse esterosome membrane is genuinely excluded. No scientific finding, predecessor identity or historical issue resolution is invented.

### Qualified scientific acceptance with explicit access and inference limits

evidence: supported. Targets: GO:0033118.

No concrete scientific record correction was established for this complete assigned target. Preserve exact source tiers, authority/primary distinctions, experimental scope, unknown necessity and represented-inventory limits. Three actual applicability defects are transmitted separately; the sparse esterosome membrane is genuinely excluded. No scientific finding, predecessor identity or historical issue resolution is invented.

### Complete frozen-input comparison and bounded refresh

provenance: supported. Targets: GO:0031904, GO:0010008, GO:7770040, GO:0012507, GO:0033117, GO:0034467, GO:0033118, GO:0044311, GO:1990413, cellstructuremech:ferrosome.

1 of ten original target hashes differ from current main. The changed content is substantively reassessed in the target-specific assessments; original observations remain historical and unchanged. All current target and used context bytes are frozen.

## Findings

### plaque-t2-F1: Clarify the membrane interface rather than compressing nested boundaries

minor / open / confirmed; issue key: epiplastidial-adjacent-interface-wording.

The function says EpM separates PPC from the host endomembrane system. Primary topology places the PPC between PPM and oEM, and EpM is itself continuous with host ER/outer nuclear membrane. An outer membrane can indirectly enclose PPC, so the wording is not treated as a proven false enclosure claim; it needs the adjacent spaces specified to avoid attributing the PPM interface to EpM.

### plaque-t2-F2: Classify the two-edge boundary graph as descriptive

minor / open / confirmed; issue key: epiplastidial-descriptive-graph-mechanistic-label.

The graph consists of collective bilayer formation of the named membrane and outer-boundary maintenance. These relations describe identity and topology; the cited sources do not establish a molecular causal sequence represented by the current nodes and edges.

### micro-F1: Resolve the verified SUB1 family instead of retaining an unresolved-family rationale

minor / open / confirmed; issue key: exoneme-sub1-family-grounding-gap.

Current InterPro IPR017314 is the exact Plasmodium SUB1 family, directly linked by current O61142. The unchanged component/discussion still says no exact family was resolved. Grounding can be repaired without treating family membership as independent exoneme localization. IPR034204 is a catalytic domain and broad PMX-family IPR001461 does not settle PMX.

## Recommended Actions And Acceptance Checks

### plaque-t2-A1

In a separately authorized curation change, clarify EpM as the outer boundary against host cytosol, enclosing the ER/cER lumen before the intervening PPM and deeper PPC; retain supported indirect enclosure and diatom ER continuity.

- Keep EpM, PPM and oEM distinct; name the actual adjacent compartments wherever a direct boundary is meant.
- Retain correct native identity and supported Phaeodactylum context; do not claim the source directly measured a new transport mechanism.
- Run focused schema and strict checks after the separately authorized edit.

### plaque-t2-A2

In a separately authorized curation change, use NONMECHANISTIC with a scope note for this descriptive topology, or add a genuinely source-backed mechanism only if independently established.

- Preserve supported topology while documenting the molecular mechanism is not represented.
- Do not invent transport machinery or lipid requirements to satisfy a graph label.
- Run the native graph and focused validation checks.

### micro-A1

In a separately authorized curation change, ground SUB1 to the verified IPR017314 family and narrow the TODO to unresolved PMX or other genuinely open identity questions; retain primary membership evidence and UNKNOWN assembly necessity.

- Verify the exact family ID/label pair against current native InterPro and run product/schema/strict checks.
- Keep the existing accession/taxon pairing and primary membership evidence; a family mapping alone does not prove exoneme localization.
- Do not replace PMX with a broad A1 family or use a catalytic domain as whole-protein identity.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| current-record-0 | data/structures/membrane_organelle/endosome_lumen.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 7522ffb363729241f2263bef6ebf96cb135a807c677df546e0b4ae92fe2bc604; current SHA256 7522ffb363729241f2263bef6ebf96cb135a807c677df546e0b4ae92fe2bc604. Record bytes unchanged since the original review. |
| original-review-0 | reviews/structured/20261022T013714Z-endosome-lumen-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-1 | data/structures/membrane_organelle/endosome_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 564b0ecf02448e0dab2210a213597b20b57ebfe09bf7637dfe2bed79a1b95270; current SHA256 564b0ecf02448e0dab2210a213597b20b57ebfe09bf7637dfe2bed79a1b95270. Record bytes unchanged since the original review. |
| original-review-1 | reviews/structured/20261022T013715Z-endosome-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-2 | data/structures/membrane_organelle/epiplastidial_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 15876d75b2efb4115edcf9f6ffa44a5254fcf104c9f543d7eb07b78a5f06db8a; current SHA256 15876d75b2efb4115edcf9f6ffa44a5254fcf104c9f543d7eb07b78a5f06db8a. Record bytes unchanged since the original review. |
| original-review-2 | reviews/structured/20261022T013716Z-epiplastidial-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-3 | data/structures/membrane_organelle/er_to_golgi_transport_vesicle_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 5cdd951707eead318295ce7ceb64c16bdc0c85b465374678d564878481f04a9c; current SHA256 5cdd951707eead318295ce7ceb64c16bdc0c85b465374678d564878481f04a9c. Record bytes unchanged since the original review. |
| original-review-3 | reviews/structured/20261022T013717Z-er-to-golgi-transport-vesicle-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-4 | data/structures/membrane_organelle/esterosome.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 c5779634687c3e16478f4782e24897bc8df7939f14eddfd26ec4715c6de3c95a; current SHA256 c5779634687c3e16478f4782e24897bc8df7939f14eddfd26ec4715c6de3c95a. Record bytes unchanged since the original review. |
| original-review-4 | reviews/structured/20261022T013717Z-esterosome-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-5 | data/structures/membrane_organelle/esterosome_lumen.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 6891a8c551bc57b8ab1ce07357d050e40b46303debc2de0b81132b54424b53a4; current SHA256 6891a8c551bc57b8ab1ce07357d050e40b46303debc2de0b81132b54424b53a4. Record bytes unchanged since the original review. |
| original-review-5 | reviews/structured/20261022T013718Z-esterosome-lumen-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-6 | data/structures/membrane_organelle/esterosome_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 b29aff5dceea8ed56348277d76f1c3658da2f304baa1b8e9858bf64cea5f4e5a; current SHA256 b29aff5dceea8ed56348277d76f1c3658da2f304baa1b8e9858bf64cea5f4e5a. Record bytes unchanged since the original review. |
| original-review-6 | reviews/structured/20261022T013719Z-esterosome-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-7 | data/structures/membrane_organelle/exoneme.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 2e32d7ca2f38ab39d5e1eb57cf683833fed5fdf18337191a3302689058d3b4b4; current SHA256 2e32d7ca2f38ab39d5e1eb57cf683833fed5fdf18337191a3302689058d3b4b4. Record bytes unchanged since the original review. |
| original-review-7 | reviews/structured/20261022T013720Z-exoneme-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-8 | data/structures/membrane_organelle/eyespot_apparatus.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 726e6433186bbdaf4cb318269e7369e07bd49d4b9d464590f0740ac5e156f36a; current SHA256 46c34aa696b5a0672d295e04dd475009d79c5c51b22aebe5afd541ccb97bc248. Changed record reassessed against current sources. |
| original-review-8 | reviews/structured/20261022T013720Z-eyespot-apparatus-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-9 | data/structures/membrane_organelle/ferrosome.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 a8350e9f852acd4d6cb753caba52b5f70ba3002f73f48e083ac047d0db405a6f; current SHA256 a8350e9f852acd4d6cb753caba52b5f70ba3002f73f48e083ac047d0db405a6f. Record bytes unchanged since the original review. |
| original-review-9 | reviews/structured/20261022T013721Z-ferrosome-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| plaque-current-0 | data/structures/membrane_organelle/endosome_lumen.yaml; Entire maintained record at source 5c140efd0be92d341410aa3024d677d5daf8bc1e; all fields, histories, discussions and graphs | supports | Entire current target independently read. Hash unchanged from original frozen target; PROPOSED unchanged. No scientific record curation performed. |
| plaque-original-0 | reviews/structured/20261022T013714Z-endosome-lumen-audit/review.yaml; Exact staleness-listed original authoritative YAML/Markdown, input hashes, checks, assessments, findings/actions and limitations | supports | Original pair validates and renders byte-exactly; all 18 historical frozen input hashes match. Scientific verdict independently reassessed; no other similarly named review is used. |
| plaque-current-1 | data/structures/membrane_organelle/endosome_membrane.yaml; Entire maintained record at source 5c140efd0be92d341410aa3024d677d5daf8bc1e; all fields, histories, discussions and graphs | supports | Entire current target independently read. Hash unchanged from original frozen target; PROPOSED unchanged. No scientific record curation performed. |
| plaque-original-1 | reviews/structured/20261022T013715Z-endosome-membrane-audit/review.yaml; Exact staleness-listed original authoritative YAML/Markdown, input hashes, checks, assessments, findings/actions and limitations | supports | Original pair validates and renders byte-exactly; all 17 historical frozen input hashes match. Scientific verdict independently reassessed; no other similarly named review is used. |
| plaque-current-2 | data/structures/membrane_organelle/epiplastidial_membrane.yaml; Entire maintained record at source 5c140efd0be92d341410aa3024d677d5daf8bc1e; all fields, histories, discussions and graphs | supports | Entire current target independently read. Hash unchanged from original frozen target; PROPOSED unchanged. No scientific record curation performed. |
| plaque-original-2 | reviews/structured/20261022T013716Z-epiplastidial-membrane-audit/review.yaml; Exact staleness-listed original authoritative YAML/Markdown, input hashes, checks, assessments, findings/actions and limitations | supports | Original pair validates and renders byte-exactly; all 14 historical frozen input hashes match. Scientific verdict independently reassessed; no other similarly named review is used. |
| plaque-policy | .claude/skills/review-yaml-record/SKILL.md; Frozen native contract and relevant definitions | context_only | Named genes/proteins/regulators/pathways/stress responses/traits trigger structured-source assessment. Empty accession inventories do not waive narrative pathway claims. |
| plaque-rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Frozen native contract and relevant definitions | context_only | Exact identity, source scope, grounding, taxonomy and necessity must be assessed; missing optional inventories alone are not findings. |
| plaque-graph-rubric | .claude/skills/curate-causal-graphs/SKILL.md; Frozen native contract and relevant definitions | context_only | Mechanistic claims require inspected primary support; descriptive identity/topology alone is not a molecular causal sequence. |
| plaque-protein-contract | .claude/skills/uniprot-protein-examples/SKILL.md; Frozen native contract and relevant definitions | context_only | External protein actors may carry verified causal-node xrefs rather than invented constituent component rows. |
| plaque-schema-policy | src/cellstructuremech/schema/cellstructuremech.yaml; Frozen native contract and relevant definitions | context_only | Whole compartment, subcellular lumen, membrane and generic collective lipid material retain their distinct granularity. |
| plaque-neighbor-mvb-lumen | data/structures/membrane_organelle/multivesicular_body_lumen.yaml; Entire frozen neighbor read for identity/boundary context only | context_only | Local MVB lumen is a specialized endosome lumen, distinct from its enclosing membrane and whole MVB. No independent review of unrelated neighbor claims or terminal historical disposition. |
| plaque-neighbor-ilv | data/structures/membrane_organelle/multivesicular_body_intraluminal_vesicle.yaml; Entire frozen neighbor read for identity/boundary context only | context_only | Local intraluminal vesicle denotes a whole vesicle inside an MVB; it is distinct from MVB lumen and limiting membrane. No independent review of unrelated neighbor claims or terminal historical disposition. |
| plaque-neighbor-ppm | data/structures/membrane_organelle/periplastidial_membrane.yaml; Entire frozen neighbor read for identity/boundary context only | context_only | PPM is the second outermost complex-plastid membrane, distinct from outermost EpM and plastid oEM. No independent review of unrelated neighbor claims or terminal historical disposition. |
| plaque-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031904,GO:0070013,GO:0005768,GO:0010008,GO:0005771,GO:0071985,GO:0016020,GO:0000813,GO:0000815,GO:7770040,GO:7770041,GO:0042170,GO:0009536,GO:0009527; All14 exact active term names/definitions/synonyms and relevant typed children; complete returned JSON | supports | Exact endosome lumen0031904 and membrane0010008 match target definitions; lumen is_a0070013 and both part_of0005768. MVB0005771 denotes an endosome with invaginated internal vesicles.0071985 describes MVB cargo sorting;0000813/0000815 identify ESCRT complexes, with modern III definition describing scission.7770040 matches full EpM definition and five synonyms;0042170 lists it is_a, and plastid0009536 lists plastid membrane part_of.7770041 puts PPC between PPM and outer plastid envelope0009527. Authority text is not a new experiment or universal strain-specific mechanism. |
| plaque-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete native taxId/scientificName/rank/lineage | supports | Species4932 is Saccharomyces cerevisiae. Native taxon identity is not an empirical prevalence or culture-collection strain assignment. |
| plaque-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete native taxId/scientificName/rank/lineage | supports | Strain559292 is S. cerevisiae S288C; this does not relabel SEY6210-derived experiments. Native taxon identity is not an empirical prevalence or culture-collection strain assignment. |
| plaque-tax2850 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2850; Complete native taxId/scientificName/rank/lineage | supports | Species2850 is Phaeodactylum tricornutum, a diatom. Native taxon identity is not an empirical prevalence or culture-collection strain assignment. |
| plaque-sl0340 | https://rest.uniprot.org/locations/SL-0340.json; Top-level identity/definition/synonyms and isA Endosome lumen SL0327/GO0031904, partOf MVB SL0174/GO0005771 | supports | MVB lumen is explicitly the compartment bounded by the MVB membrane and a subtype of endosome lumen. This validates local boundary/specialization context without treating ILVs as mandatory in every endosome. |
| plaque-protein-P40343 | https://rest.uniprot.org/uniprotkb/P40343.json; Primary accession, reviewed entry type, genes/protein names/organism and FUNCTION/SUBCELLULAR LOCATION comments with linked evidence | supports | Reviewed P40343 is VPS27/YNR006W, vacuolar protein sorting-associated protein27, in S288C559292. Annotation identifies ESCRT-0 actor recruiting ESCRT-I to endosomal membranes and links PMID12900393. It supports exact graph xref identity; primary experiments and strain scope are assessed separately. |
| plaque-katzmann2001-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A11511343%20AND%20SRC%3AMED; Exact EuropePMC native core bibliographic entry and complete abstract; body tier explicitly separate | supports | Katzmann/Babst/Emr2001 PMID11511343 DOI10.1016/s0092-8674(01)00434-2. Complete abstract identifies yeast ESCRT-I and ubiquitin-dependent cargo sorting into MVB vesicles; no full body or figure inspection. |
| plaque-katzmann2003-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1083/jcb.200302136; Exact EuropePMC native core bibliographic entry and complete abstract; body tier explicitly separate | supports | Katzmann/Stefan/Babst/Emr2003 PMID12900393 DOI10.1083/jcb.200302136; exact article identity and abstract support Vps27-dependent ESCRT-I recruitment; body inspected separately. |
| plaque-babst2002-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A12194857%20AND%20SRC%3AMED; Exact EuropePMC native core bibliographic entry and complete abstract; body tier explicitly separate | supports | Babst et al.2002 PMID12194857 DOI10.1016/s1534-5807(02)00220-4. Complete abstract supports cytoplasmic ESCRT-III recruitment, membrane oligomerization, subcomplex association and cargo sorting/concentration. It does not independently establish precise scission chemistry; no full body read. |
| plaque-henne2011-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.devcel.2011.05.015; Exact EuropePMC native core bibliographic entry and complete abstract; body tier explicitly separate | supports | Henne/Buchkovich/Emr2011 PMID21763610 DOI10.1016/j.devcel.2011.05.015 is explicitly a review. Complete abstract describes ESCRT cargo recognition and membrane sculpting; secondary context, not a primary intervention or full-body inspection. |
| plaque-flori2016-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.protis.2016.04.001; Exact EuropePMC native core bibliographic entry and complete abstract; body tier explicitly separate | supports | Flori/Jouneau/Finazzi/Marechal/Falconet2016 PMID27179349 DOI10.1016/j.protis.2016.04.001, Ultrastructure of the Periplastidial Compartment of the Diatom Phaeodactylum tricornutum. Primary FIB-SEM identity/abstract; detailed boundary claims assessed in PDF. |
| plaque-gueguen2024-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1093/plcell/koae275; Exact EuropePMC native core bibliographic entry and complete abstract; body tier explicitly separate | supports | Gueguen et al.2024 PMID39383259 DOI10.1093/plcell/koae275, Monogalactosyldiacylglycerol synthase isoforms play diverse roles inside and outside the diatom plastid. Primary identity/abstract; detailed scope assessed in JATS. |
| plaque-hashimoto2005-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1007/s10265-005-0214-6; Exact EuropePMC native core bibliographic entry and complete abstract; body tier explicitly separate | supports | Hashimoto2005 PMID15937721 DOI10.1007/s10265-005-0214-6 is a review. Complete abstract distinguishes secondary-plastid lineages and ER/outer-nuclear continuity in heterokonts/cryptophytes/haptophytes. Secondary abstract-only context; no primary experimental or full-body claim. |
| plaque-katzmann2003-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC2172707/; Genuine primary PMC HTML complete Resultssec5/sec6 and Methodssec12; Figure3/4 captions as text; no figure pixels or raw-data reanalysis | supports | Vps23-GFP redistribution in vps27 deletion and reciprocal localization, plus membrane-fraction copurification, support Vps27-dependent ESCRT-I recruitment/association on yeast endosomes. Methods list SEY6210-derived strains. Reference S288C UniProt identity is not substituted for study strain. These experiments support the narrow canonical example, not every ESCRT step or obligatory constituents of all endosome membranes. |
| plaque-flori2016-oceanomics-pdf | https://www.oceanomics.eu/sites/default/files/documents/oceanomics-flori-et-al-protist-2016-484.pdf; Published PDF p255 text and Fig1 caption/pixels; Results opening p256 and full p261; Discussion/Methods pp263–264 and associated Fig5/6 caption text. Other figure pixels, supplements and raw measurements not audited | supports | Primary P. tricornutum Pt1 CCAP1055/3 study distinguishes outer cERM/EpM continuous with outer nuclear envelope, PPM beneath it and PPC between PPM/oEM. Fig1 pixels show an intervening cERM–PPM space, not PPC immediately inside EpM. FIB-SEM compares disrupted cells and intact cells. Authors mark molecular machinery/lipid compositions unresolved and evolutionary alternatives as hypotheses. Indirect outer enclosure is valid; immediate-interface wording remains ambiguous. |
| plaque-gueguen2024-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11638560/fullTextXML; Introductionkoae275-s1 with Fig1 caption; Resultss2.4 with Fig2/3 captions; Discussions3.2/s3.8; Methodss4.4/s4.13; no figure-pixel, supplement or other-section audit | supports | P. tricornutum Pt1 Strain8.6 CCAP1055/1 study preserves EpM/PPM/oEM/iEM boundaries. MGDgamma-GFP fluorescence in ER/plastid periphery supports qualified possible EpM localization, while exact extraplastidial lipid pools/functions remain uncertain. Source-localization information is not a record assertion of exact lipid mixture or formation necessity. Evolutionary membrane-origin alternatives remain explicit in source. |
| plaque-catalogue | https://imodulondb.org/api/datasets; Complete fresh official /api/datasets response; every organism/dataset row read, no pagination | supports | Returned catalogue has no Saccharomyces cerevisiae or Phaeodactylum tricornutum host match. ESCRT/MVB pathway and VPS27 claims trigger assessment but no matched downstream gene/module query applies. Bacterial/archaeal datasets are not proxies for these eukaryotic hosts. Noncoverage is not biological absence; no generated module prose is used. |
| plaque-historical-runner | /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources imodulondb datasets; Historical00:49Z receipt with stdout/stderr reread and hashes verified | context_only | Historical runner failed before dataset retrieval with PermissionError reading pyvenv.cfg. No current invocation or success claimed; fresh official catalogue and scoped primary/authority sources are the permitted fallback. |
| plaque-original-checks | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/adversary-plaque/original-checks.json; All three original native validation/render results and historical-source input hashes | supports | Three original pairs validate/render exactly; historical input counts18/17/14 all match. All three target hashes unchanged. EpM two scientific findings remain independently confirmed. |
| plaque-native-endosome_lumen-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/endosome_lumen.yaml --verify; Root-owned actual command receipt/stdout independently read and hash-verified | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok Scope: No component protein_examples and zero GENE_OR_PROTEIN nodes in the complete current target; mechanical checks are empty-inventory scope. |
| plaque-native-endosome_lumen-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/endosome_lumen.yaml --causal-graphs; Root-owned actual command receipt/stdout independently read and hash-verified | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes Scope: No component protein_examples and zero GENE_OR_PROTEIN nodes in the complete current target; mechanical checks are empty-inventory scope. |
| plaque-native-endosome_membrane-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/endosome_membrane.yaml --verify; Root-owned actual command receipt/stdout independently read and hash-verified | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok Scope: No component protein_examples; one GENE_OR_PROTEIN node is UNANCHORED_WITH_UNIPROT, carrying verified P40343 for external Vps27. This is permitted and does not require a fabricated component. |
| plaque-native-endosome_membrane-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/endosome_membrane.yaml --causal-graphs; Root-owned actual command receipt/stdout independently read and hash-verified | supports | data/structures/membrane_organelle/endosome_membrane.yaml  (GO:0010008)<br>  endosome_membrane_mvb_sorting	vps27_endosomal_recruiter	UNANCHORED_WITH_UNIPROT	Vps27 endosomal ESCRT-I recruiter (UniProtKB:P40343)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     1  total GENE_OR_PROTEIN causal nodes Scope: No component protein_examples; one GENE_OR_PROTEIN node is UNANCHORED_WITH_UNIPROT, carrying verified P40343 for external Vps27. This is permitted and does not require a fabricated component. |
| plaque-native-epiplastidial_membrane-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/epiplastidial_membrane.yaml --verify; Root-owned actual command receipt/stdout independently read and hash-verified | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok Scope: No component protein_examples and zero GENE_OR_PROTEIN nodes in the complete current target; mechanical checks are empty-inventory scope. |
| plaque-native-epiplastidial_membrane-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/epiplastidial_membrane.yaml --causal-graphs; Root-owned actual command receipt/stdout independently read and hash-verified | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes Scope: No component protein_examples and zero GENE_OR_PROTEIN nodes in the complete current target; mechanical checks are empty-inventory scope. |
| micro-policy | .claude/skills/review-yaml-record/SKILL.md; Current complete native review skill/profile/config and checklist reread; remaining frozen common contracts retained at identical hashes, exact scope in policy-hash-check.json | context_only | Structure/protein/phenotype, membership/necessity and exact-family/domain scopes remain distinct. Named gene/locus/pathway claims trigger structured-source applicability even without an expression claim. All17 common instructions/schema/verifier inputs equal the preceding reviewed bytes. |
| micro-protein-contract | .claude/skills/uniprot-protein-examples/SKILL.md; Entire current skill reread: identity-only examples, exact native tokens, canonical taxa, reviewed/unreviewed status and allowed external-actor xrefs | context_only | An alias may be bridged by actual literature while gene_symbol retains the native entry token. Unreviewed status is explicit. Verified external substrates need not be invented as stable organelle constituents. |
| micro-record-exoneme | data/structures/membrane_organelle/exoneme.yaml; Entire current maintained YAML: all fields, history, components/examples, taxonomy, functions, evidence, graph and discussions | supports | Entire target independently read at 5c140efd0be92d341410aa3024d677d5daf8bc1e. Current bytes equal original frozen target. |
| micro-prior-exoneme | reviews/structured/20261022T013720Z-exoneme-audit/review.yaml; Original authoritative YAML plus paired deterministic Markdown; source hash, checks, all assessments/findings/actions/limitations | context_only | Original needs_curation; one inherited minor SUB1 family finding retains exact lineage. Existing expression-only adapter exclusion is reassessed; historical executions are not claimed current. |
| micro-native-exoneme-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/exoneme-uniprot-verify-receipt.json; Actual .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/exoneme.yaml --verify; complete stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/exoneme-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual source-head exit0. Two protein examples O61142/Q8IAS0 and two graph xrefs Q9TY95/Q8I0U8. Three typed nodes:2COVERED and1UNANCHORED_WITH_UNIPROT external SERA/MSP substrate cohort; the permitted external-actor route is not a dangling constituent. |
| micro-native-exoneme-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/exoneme-uniprot-causal-receipt.json; Actual .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/exoneme.yaml --causal-graphs; complete stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/exoneme-uniprot-causal.log SHA256 511b80633418ceaf902b70422e104017ea024ac612753acc164a8ceed3612398 | supports | Actual source-head exit0. Two protein examples O61142/Q8IAS0 and two graph xrefs Q9TY95/Q8I0U8. Three typed nodes:2COVERED and1UNANCHORED_WITH_UNIPROT external SERA/MSP substrate cohort; the permitted external-actor route is not a dangling constituent. |
| micro-record-eyespot_apparatus | data/structures/membrane_organelle/eyespot_apparatus.yaml; Entire current maintained YAML: all fields, history, components/examples, taxonomy, functions, evidence, graph and discussions | supports | Entire target independently read at 5c140efd0be92d341410aa3024d677d5daf8bc1e. Stale eyespot adds Q93WP2/acop1 protein example and corresponding history; substantively reassessed below. |
| micro-prior-eyespot_apparatus | reviews/structured/20261022T013720Z-eyespot-apparatus-audit/review.yaml; Original authoritative YAML plus paired deterministic Markdown; source hash, checks, all assessments/findings/actions/limitations | context_only | Original pass_with_limitations; no original findings/actions. Existing expression-only adapter exclusion is reassessed; historical executions are not claimed current. |
| micro-native-eyespot_apparatus-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/eyespot_apparatus-uniprot-verify-receipt.json; Actual .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/eyespot_apparatus.yaml --verify; complete stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/eyespot_apparatus-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual source-head exit0. Two unreviewed examples Q8RUT8/Q93WP2 and one COVERED typed node. Native success does not prove apparatus membership or make the literal COP3 query return a result. |
| micro-native-eyespot_apparatus-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/eyespot_apparatus-uniprot-causal-receipt.json; Actual .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/eyespot_apparatus.yaml --causal-graphs; complete stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/eyespot_apparatus-uniprot-causal.log SHA256 da5a05917d67e5d9fea5b655a99f994074cd657a4a40e6673c8e6d6bfb0bee5b | supports | Actual source-head exit0. Two unreviewed examples Q8RUT8/Q93WP2 and one COVERED typed node. Native success does not prove apparatus membership or make the literal COP3 query return a result. |
| micro-record-ferrosome | data/structures/membrane_organelle/ferrosome.yaml; Entire current maintained YAML: all fields, history, components/examples, taxonomy, functions, evidence, graph and discussions | supports | Entire target independently read at 5c140efd0be92d341410aa3024d677d5daf8bc1e. Current bytes equal original frozen target. |
| micro-prior-ferrosome | reviews/structured/20261022T013721Z-ferrosome-audit/review.yaml; Original authoritative YAML plus paired deterministic Markdown; source hash, checks, all assessments/findings/actions/limitations | context_only | Original pass_with_limitations; no original findings/actions. Existing expression-only adapter exclusion is reassessed; historical executions are not claimed current. |
| micro-native-ferrosome-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/ferrosome-uniprot-verify-receipt.json; Actual .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/ferrosome.yaml --verify; complete stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/ferrosome-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual source-head exit0. Three unreviewed locus examples C4XH20/C4XH21/C4XH22 and one COVERED typed Fez cohort node. Literature aliases and biological membership require separate primary evidence. |
| micro-native-ferrosome-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/ferrosome-uniprot-causal-receipt.json; Actual .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/ferrosome.yaml --causal-graphs; complete stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/ferrosome-uniprot-causal.log SHA256 d45e581edff9b488306b1c92b87a02fcd2a425cd7d85646a32d55d964924c28b | supports | Actual source-head exit0. Three unreviewed locus examples C4XH20/C4XH21/C4XH22 and one COVERED typed Fez cohort node. Literature aliases and biological membership require separate primary evidence. |
| micro-original-pairs | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/adversary-microtubule/original-validation.json; Three actual native validate and three render --content executions, all byte-equal; frozen historical record inputs checked through git show | supports | All three retained bundles are schema-valid and Markdown equals renderer output. Historical target hashes match source f97b1abe; only eyespot differs from current record. |
| micro-eyespot-delta | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/adversary-microtubule/eyespot-stale.diff; Exact original-frozen-source versus current-head diff for eyespot only | context_only | Only new Q93WP2/acop1 example and October23 curation event; no graph/definition/other component changes. |
| micro-exo-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044311,GO:0043231,GO:0020007; All three exact identifiers, definitions, active flags and relevant child relations | supports | Active GO0044311 matches the exoneme definition; GO0043231 lists it as an is_a child and GO0020007 lists it as part_of the apical complex. |
| micro-exo-tax5833 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5833; Exact taxId, scientificName, rank, lineage and alternate names | supports | ENA identifies tax5833 as Plasmodium falciparum, species. |
| micro-exo-tax36329 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/36329; Exact taxId, scientificName, rank, lineage and alternate names | supports | ENA identifies tax36329 as Plasmodium falciparum3D7, isolate rank. |
| micro-exo-yeoh2007-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.cell.2007.10.049; Exact Europe PMC DOI/PMID core lookup; complete MED bibliographic record and complete abstract only; full-body reading separately scoped | supports | PMID18083098, DOI10.1016/j.cell.2007.10.049: Subcellular discharge of a serine protease mediates release of invasive malaria parasites from host erythrocytes. Complete abstract inspected; no full-body access implied by metadata. |
| micro-exo-blackman1998-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A9722575%20AND%20SRC%3AMED; Exact Europe PMC DOI/PMID core lookup; complete MED bibliographic record and complete abstract only; full-body reading separately scoped | supports | PMID9722575, DOI10.1074/jbc.273.36.23398: A subtilisin-like protein in secretory organelles of Plasmodium falciparum merozoites. Complete abstract inspected; no full-body access implied by metadata. |
| micro-exo-blackman2008-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1111/j.1462-5822.2008.01176.x; Exact Europe PMC DOI/PMID core lookup; complete MED bibliographic record and complete abstract only; full-body reading separately scoped | context_only | PMID18503638, DOI10.1111/j.1462-5822.2008.01176.x: Malarial proteases and host cell egress: an 'emerging' cascade. Complete abstract inspected; no full-body access implied by metadata. |
| micro-exo-withers2014-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038/ncomms4726; Exact Europe PMC DOI/PMID core lookup; complete MED bibliographic record and complete abstract only; full-body reading separately scoped | supports | PMID24785947, DOI10.1038/ncomms4726: The malaria parasite egress protease SUB1 is a calcium-dependent redox switch subtilisin. Complete abstract inspected; no full-body access implied by metadata. |
| micro-exo-nasamu2017-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1126/science.aan1478; Exact Europe PMC DOI/PMID core lookup; complete MED bibliographic record and complete abstract only; full-body reading separately scoped | supports | PMID29074774, DOI10.1126/science.aan1478: Plasmepsins IX and X are essential and druggable mediators of malaria parasite egress and invasion. Complete abstract inspected; no full-body access implied by metadata. |
| micro-exo-blackman2008-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2610400/fullTextXML; Complete subsection SERA processing by SUB1: an activation event?; extracted body rows19–22; review-tier text, not new experiments | context_only | Secondary review explicitly attributes soluble PfSUB1 discharge into PV and SERA processing to Yeoh2007; proposed SERA activation and cross-stage extensions remain hypotheses. |
| micro-exo-withers2014-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4024747/fullTextXML; All five introductory paragraphs and complete Discussion; extracted body rows0–4,23–27. Results/Methods/figure pixels not inspected | supports | Primary structural paper background describes exoneme storage and PV discharge minutes before egress; Discussion makes reducing exoneme environment hypothetical. Used for attributed discharge context, not a new live-cell secretion experiment or verified in-vivo redox switch. |
| micro-exo-nasamu2017-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5928414/fullTextXML; Entire scientific main text and Fig1–4 captions, extracted body rows0–14; separate supplementary Methods and figure pixels not inspected | supports | Immuno-EM and colocalization place PMX in exonemes; knockdown and catalytic rescue support final SUB1 maturation, SERA5/MSP1 processing and egress/invasion effects. Direct final cleavage versus prodomain-relief in vivo remains explicitly unresolved. Fig4 parental NF54 is not relabeled as3D7. |
| micro-exo-O61142 | https://rest.uniprot.org/uniprotkb/O61142.json; Accession, reviewed status, recommended name, gene/ORF tokens, organism and relevant localization evidence/InterPro cross-references | supports | Native reviewed entry O61142 is Subtilisin-like protease 1, taxon5833; exact gene/ORF tokens and entry status match the maintained example or graph cross-reference. Secreted localization cites PMID9722575 with ECO0000269; PV lumen is by similarity to Q8I0V0. IPR017314 is a native family cross-reference. |
| micro-exo-Q8IAS0 | https://rest.uniprot.org/uniprotkb/Q8IAS0.json; Accession, reviewed status, recommended name, gene/ORF tokens, organism and relevant localization evidence/InterPro cross-references | supports | Native reviewed entry Q8IAS0 is Plasmepsin X, taxon36329; exact gene/ORF tokens and entry status match the maintained example or graph cross-reference. Secretory-vesicle localization is by similarity to W7JWW5, not an additional direct experiment in this metadata. |
| micro-exo-Q9TY95 | https://rest.uniprot.org/uniprotkb/Q9TY95.json; Accession, reviewed status, recommended name, gene/ORF tokens, organism and relevant localization evidence/InterPro cross-references | supports | Native reviewed entry Q9TY95 is Serine-repeat antigen protein 5, taxon36329; exact gene/ORF tokens and entry status match the maintained example or graph cross-reference. |
| micro-exo-Q8I0U8 | https://rest.uniprot.org/uniprotkb/Q8I0U8.json; Accession, reviewed status, recommended name, gene/ORF tokens, organism and relevant localization evidence/InterPro cross-references | supports | Native reviewed entry Q8I0U8 is Merozoite surface protein 1, taxon36329; exact gene/ORF tokens and entry status match the maintained example or graph cross-reference. |
| micro-exo-sub1-query | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Asub1%29%20AND%20%28taxonomy_id%3A5833%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Exact query and all three returned reviewed accession/taxon/gene rows | supports | The returned reviewed SUB1 entries are O61142 at species5833, Q8I0V0 at3D7/36329 and W7K9M0 atNF54/5843. Exactly one result is at the maintained species taxon; descendant-isolate entries are not falsely excluded. |
| micro-exo-pmx-query | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Apmx%29%20AND%20%28taxonomy_id%3A36329%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Exact query and complete single returned accession/taxon/gene row | supports | The exact reviewed PMX query for3D7 returns Q8IAS0, supporting the record’s uniqueness note at that taxon. |
| micro-exo-IPR017314 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017314/; metadata accession, type=family, name and complete non-LLM description | supports | InterPro explicitly types IPR017314 as a protein family for Plasmodium subtilisin-like peptidase1/SUB1. This matches the complete SUB1 molecular identity represented by the component; it is not merely an exoneme-location ontology term. |
| micro-exo-IPR034204 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR034204/; metadata accession, type=domain, name, description and listed scope | supports | IPR034204 is a catalytic domain, including related non-Plasmodium proteins, and is not an exact whole-SUB1 family substitute. |
| micro-exo-IPR001461 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001461/; metadata accession, family name/type and description | supports | IPR001461 is the broad pepsin/A1 family; its scope is wider than the exact PMX component. No exact PMX-family grounding is established by this candidate. |
| micro-eye-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031904,GO:0070013,GO:0005768,GO:0010008,GO:0005771,GO:0071985,GO:0016020,GO:0000813,GO:0000815,GO:0012507,GO:0030658,GO:0030662,GO:0030134,GO:0005789,GO:0090114,GO:0030127,GO:1990413; Exact GO1990413 active ID/name/definition/two RELATED synonyms within returned17-term packet; unrelated packet terms not assessed | supports | GO1990413 matches small pigmented light-detection organelle; eyespot and stigma are RELATED synonyms. OTHER kind preserves the cross-membrane apparatus boundary. |
| micro-eye-tax3055 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055; Exact taxId, scientificName, rank, lineage and alternate names | supports | Native ENA exact species identity and lineage agree with Chlamydomonas reinhardtii3055. This is taxonomic identity, not a measured population prevalence or an experimental strain assignment. |
| micro-eye-lamb1999-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A10511552%20AND%20SRC%3AMED; Exact Europe PMC DOI/PMID core lookup; complete MED bibliographic record and complete abstract only; full-body reading separately scoped | supports | PMID10511552, DOI10.1093/genetics/153.2.721: Eyespot-assembly mutants in Chlamydomonas reinhardtii. Complete abstract inspected; no full-body access implied by metadata. |
| micro-eye-schmidt2006-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A16798888%20AND%20SRC%3AMED; Exact Europe PMC DOI/PMID core lookup; complete MED bibliographic record and complete abstract only; full-body reading separately scoped | supports | PMID16798888, DOI10.1105/tpc.106.041749: Proteomic analysis of the eyespot of Chlamydomonas reinhardtii provides novel insights into its components and tactic movements. Complete abstract inspected; no full-body access implied by metadata. |
| micro-eye-mittelmeier2011-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A21555459%20AND%20SRC%3AMED; Exact Europe PMC DOI/PMID core lookup; complete MED bibliographic record and complete abstract only; full-body reading separately scoped | supports | PMID21555459, DOI10.1083/jcb.201009131: Asymmetric properties of the Chlamydomonas reinhardtii cytoskeleton direct rhodopsin photoreceptor localization. Complete abstract inspected; no full-body access implied by metadata. |
| micro-eye-awasthi2016-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1038/srep34646%22; Exact Europe PMC DOI/PMID core lookup; complete MED bibliographic record and complete abstract only; full-body reading separately scoped | supports | PMID27694882, DOI10.1038/srep34646: The trafficking of bacterial type rhodopsins into the Chlamydomonas eyespot and flagella is IFT mediated. Complete abstract inspected; no full-body access implied by metadata. |
| micro-eye-ueki2016-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A27122315%20AND%20SRC%3AMED; Exact Europe PMC DOI/PMID core lookup; complete MED bibliographic record and complete abstract only; full-body reading separately scoped | supports | PMID27122315, DOI10.1073/pnas.1525538113: Eyespot-dependent determination of the phototactic sign in Chlamydomonas reinhardtii. Complete abstract inspected; no full-body access implied by metadata. |
| micro-eye-protein-Q8RUT8 | https://rest.uniprot.org/uniprotkb/Q8RUT8.json; Exact primary accession, protein names, cop4/acop2/CSOB tokens,taxon3055,TrEMBL status and broad opsin-family crossref | supports | Q8RUT8 is unreviewed archaeal-type opsin2/cop4 at tax3055; broad IPR001425 and automated location do not independently prove eyespot membership. |
| micro-eye-query-COP3-true | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=gene_exact%3ACOP3%20AND%20taxonomy_id%3A3055%20AND%20reviewed%3Atrue; Full returned results at size500, exact query and entry identities | supports | The complete gene_exact:COP3, taxonomy_id:3055, reviewed:true query returns 0 entries. This bounded query result is not proof that the gene or an accession does not exist under other names. |
| micro-eye-query-COP3-false | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=gene_exact%3ACOP3%20AND%20taxonomy_id%3A3055%20AND%20reviewed%3Afalse; Full returned results at size500, exact query and entry identities | supports | The complete gene_exact:COP3, taxonomy_id:3055, reviewed:false query returns 0 entries. This bounded query result is not proof that the gene or an accession does not exist under other names. |
| micro-eye-query-COP4-true | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=gene_exact%3ACOP4%20AND%20taxonomy_id%3A3055%20AND%20reviewed%3Atrue; Full returned results at size500, exact query and entry identities | supports | The complete gene_exact:COP4, taxonomy_id:3055, reviewed:true query returns 0 entries. This bounded query result is not proof that the gene or an accession does not exist under other names. |
| micro-eye-query-COP4-false | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=gene_exact%3ACOP4%20AND%20taxonomy_id%3A3055%20AND%20reviewed%3Afalse; Full returned results at size500, exact query and entry identities | supports | The complete gene_exact:COP4, taxonomy_id:3055, reviewed:false query returns 1 entries (Q8RUT8). This bounded query result is not proof that the gene or an accession does not exist under other names. |
| micro-eye-schmidt2006-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC1533972/; Introduction paragraph on COP3/COP4 aliases; Table1 photoreceptor rows; complete paragraphs indexed32,54,55,67,74,77,89 and cw15 purification Methods145 in extracted text. Other Table1 rows only contextual, not individually recertified | supports | Table1 explicitly bridges COP3/CHOP1/CSRA/Acop1 (eight peptides) and COP4/CHOP2/CSRB/Acop2 (three peptides). Purified cw15 eyespot fractions support cohort association with explicit contaminant/loss limitations; reference identity and candidate detection do not automatically prove every proteome constituent or direct ChR2 localization. |
| micro-eye-mittelmeier2011-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC3166873/; Introduction paragraphs and Fig1 caption; first Results subsection ChR1 association with most extensively acetylated daughter rootlet and Fig2 caption; Strains and media. Extracted rows14–28,83–86; no figure pixels | supports | Direct ChR1 immunofluorescence shows equatorial patches adjacent to the D4 rootlet in wild type and altered patterns in mutants. Study distinguishes photoreceptor trafficking model from observations; reference strain137c/CC125 and mutant backgrounds are not all one generic strain. No direct ChR2 imaging claimed. |
| micro-eye-awasthi2016-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC5046144/; Introductory rhodopsin/IFT context, first Results localization paragraph, Strains and media and Antibodies Methods; extracted rows14–22,69–75. Other trafficking experiments and figure pixels not independently read | supports | Explicit COP3=ChR1 and COP4=ChR2 naming bridge. Principal experimentally trafficked proteins are ChR1 and Cop8, not both ChR1 and ChR2; source context does not export all IFT controls to ChR2. |
| micro-eye-ueki2016-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC4868408/; Complete Results subsections from lts1-211 carotenoid/eyespot deficiency through lens-effect/model discussion; Fig4–6/S3/S4 captions; complete Discussion and main Methods. Extracted rows55–77,98–106. No current figure-pixel/SI dataset inspection | supports | Mutant/rescue and redox-biased behavior plus cellular lens observations support pigment-layer shielding and phototactic sign; eyeless cells can still show strong phototaxis under tested conditions. Fig6 is an explanatory model. Whole-cell carotenoid HPLC is not an exhaustive eyespot chemical-species inventory. |
| micro-fer-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043231; Exact active ID/name/definition and returned children | supports | GO0043231 defines an intracellular membrane-bounded organelle, compatible with the experimentally described bacterial ferrosome. The minted record is not claimed to be a direct GO child. |
| micro-fer-tax573370 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/573370; Exact taxId, scientificName, rank, lineage and equivalent names | supports | ENA identifies tax573370 as Solidesulfovibrio magneticus RS-1, strain rank, with Desulfovibrio magneticus RS-1 and700980 as equivalent names. This directly bridges the current maintained name to the primary-paper nomenclature. |
| micro-fer-grant2022-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038/s41586-022-04741-x; Exact Europe PMC DOI/PMID core lookup; complete MED bibliographic record and complete abstract only; full-body reading separately scoped | supports | PMID35585231, DOI10.1038/s41586-022-04741-x: Distinct gene clusters drive formation of ferrosome organelles in bacteria. Complete abstract inspected; no full-body access implied by metadata. |
| micro-fer-byrne2010-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1073/pnas.1001290107; Exact Europe PMC DOI/PMID core lookup; complete MED bibliographic record and complete abstract only; full-body reading separately scoped | supports | PMID20566879, DOI10.1073/pnas.1001290107: Desulfovibrio magneticus RS-1 contains an iron- and phosphorus-rich organelle distinct from its bullet-shaped magnetosomes. Complete abstract inspected; no full-body access implied by metadata. |
| micro-fer-grant2022-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC10906721.1/PMC10906721.1.xml; Complete scientific main Introduction/Results/Discussion sections through S7, extracted rows0–16; independent fresh read. Methods, supplementary tables and figure pixels not read by this reviewer | supports | DMR_28320/28330/28340 map to FezA/B/C; fraction proteomics and RS-1 fezBC deletion plus fezABC complementation support cohort-dependent formation. Direct iron-starvation fitness/rescue is S.putrefaciens, not RS-1. E.coli heterologous fezSp and AMB-1 fezRp show engineered-host sufficiency; exact iron transport and membrane biogenesis remain open. |
| micro-fer-C4XH20 | https://rest.uniprot.org/uniprotkb/C4XH20.json; Accession, TrEMBL entry status, organism, protein description, genes.orderedLocusNames and InterPro cross-references | supports | Native unreviewed accession C4XH20, tax573370 and ordered-locus token DMR_28320 match the maintained example. The FezA alias bridge comes from Grant2022, not an independently indexed UniProt geneName. Automated protein-name annotations are not treated as measured substrate specificity. |
| micro-fer-C4XH21 | https://rest.uniprot.org/uniprotkb/C4XH21.json; Accession, TrEMBL entry status, organism, protein description, genes.orderedLocusNames and InterPro cross-references | supports | Native unreviewed accession C4XH21, tax573370 and ordered-locus token DMR_28330 match the maintained example. The FezB alias bridge comes from Grant2022, not an independently indexed UniProt geneName. Automated protein-name annotations are not treated as measured substrate specificity. |
| micro-fer-C4XH22 | https://rest.uniprot.org/uniprotkb/C4XH22.json; Accession, TrEMBL entry status, organism, protein description, genes.orderedLocusNames and InterPro cross-references | supports | Native unreviewed accession C4XH22, tax573370 and ordered-locus token DMR_28340 match the maintained example. The FezC alias bridge comes from Grant2022, not an independently indexed UniProt geneName. Automated protein-name annotations are not treated as measured substrate specificity. |
| micro-fer-IPR027256 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR027256/; metadata family/type/name and complete description | supports | IPR027256 covers broad subfamilyIB P-type metal ATPases. It is wider than FezB and cannot ground the unrelated FezA/B/C cohort as a single exact family. An annotated Zn transporter name is not direct evidence of FezB zinc specificity. |
| micro-fer-go-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=ferrosome&amp;limit=100; Native query and complete zero-result response | context_only | The exact bounded native query for ferrosome returned zero results. This is search context only, not an exhaustive claim that no ontology anywhere contains a matching concept. |
| micro-byrne-canonical | https://pmc.ncbi.nlm.nih.gov/articles/PMC2901430/; Complete Introduction, Results, Discussion, main Methods and Fig1–5 captions; extracted rows20–65. No image-pixel or separate supplementary Methods reanalysis | supports | RS-1 EDS finds Fe/P/O-rich amorphous granules; pulse-chase NanoSIMS and three imaging approaches distinguish membrane-enclosed granules from bullet-shaped crystals. Transient iron-influx response and proposed storage/sequestration do not directly test anaerobic fitness. Authors retain limits on magnetosome membrane visibility. |
| micro-eye-Q93WP2 | https://rest.uniprot.org/uniprotkb/Q93WP2.json; Exact primary accession, full submitted protein names, native geneName acop1, organism3055 and entryType; relevant broad family/location annotations | supports | New Q93WP2 is unreviewed archaeal-type opsin1/Channelopsin-1, primary gene acop1, tax3055. UniProt does not index literal COP3; freshly read Schmidt Table1 maps COP3 to Acop1, independently supporting the maintained alias role. Automated annotation alone is not eyespot membership. |
| micro-yeoh-pdf | https://www.cell.com/cell/pdf/S0092-8674(07)01403-1.pdf; Actual publisher access response only, HTTP403; not scientific full text | context_only | Primary body unavailable through this checked route. Complete native abstract remains the inspected tier; no full-body or figure claim. |
| micro-blackman1998-pdf | https://www.jbc.org/article/S0021925819750030/pdf; Actual publisher access response only, HTTP403; not scientific full text | context_only | Primary body unavailable through this checked route. Complete native abstract remains the inspected tier; no full-body or figure claim. |
| micro-source-access | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/adversary-microtubule/manifest.json; 49 current public-source responses; initial sandbox DNS failures separately archived; numeric Byrne response replaced by canonical PMC body | context_only | Authority/source fetch statuses are recorded. HTTP200 numeric Byrne route is not treated as body evidence; canonical article was separately fetched and read. Publisher403 responses for Yeoh/Blackman are explicit; original historic figures are not claimed freshly viewed. |
| micro-historical-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Actual historical adapter datasets invocation and PermissionError; reused receipt, no current invocation | context_only | Historical 00:49Z runner unavailable due interpreter-environment PermissionError; this is not a fresh failed run. Current applicability uses inspected official source catalogue. |
| micro-catalogue | https://imodulondb.org/api/datasets; Complete official /api/datasets response: all20 organism rows and28 organism/dataset pairs; names/IDs/descriptions/dataset lists read | context_only | No represented Plasmodium falciparum, Chlamydomonas reinhardtii or Solidesulfovibrio/Desulfovibrio magneticus RS-1 dataset. Three pathway-bearing targets require applicability assessment, but no matched module/gene query can be constructed from this catalogue. Foreign-host E.coli fez constructs are not an RS-1 proxy. |
| micro-local-ferrosome-id | rg --no-ignore --hidden -n ^identifier: cellstructuremech:ferrosome$ data/structures; Whole maintained data/structures exact identifier-line scan; ignored and hidden files included | context_only | Exactly one maintained identifier-line match, the frozen ferrosome target. No claim about every textual alias or external ontology. |
| septin-review-policy | .claude/skills/review-yaml-record/SKILL.md; Structured-source cross-checks and immutable review contract | supports | Assess actual named molecular or pathway assertions throughout the record. Expression-only exemptions are insufficient; material/morphology-only records may genuinely exclude molecular queries. Catalogue noncoverage is not negative biological evidence. |
| septin-curation-policy | docs/CURATION.md; Component grounding and family consensus; collective material and protein-example evidence | supports | Reviewed label-only components can document missing exact grounding. The automated InterPro policy promotes integrated entries typed family only, not domains, sites or homologous superfamilies. Exact protein identity is distinct from experimentally supported localization and necessity. |
| septin-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; NONMECHANISTIC topology and empirical association | supports | Parthood, boundaries and observed cargo association may remain descriptive. Cofractionation and colocalization do not establish purified co-crystallization, stoichiometry, nucleation or universal formation necessity. |
| septin-record-er_to_golgi_transport_vesicle_membrane | data/structures/membrane_organelle/er_to_golgi_transport_vesicle_membrane.yaml; Complete maintained record at 5c140efd0be92d341410aa3024d677d5daf8bc1e | supports | Read identity, definition, hierarchy/parthood, synonyms/xrefs, components, protein examples when present, taxon/example, functions, every evidence note and graph edge, discussions and history. No target images, quantitative properties, associated traits or verbatim snippets are declared. |
| septin-original-er_to_golgi_transport_vesicle_membrane | reviews/structured/20261022T013717Z-er-to-golgi-transport-vesicle-membrane-audit/review.yaml; Complete original YAML/Markdown; source inputs, checks, evidence tiers, assessments, empty findings/actions and limitations | supports | Original qualified positive scientific assessment has no findings/actions. It contains an explicit imodulondb exclusion, not an omitted row. Its historical checks/access dates remain historical; applicability is reassessed from the complete maintained record. |
| septin-original-validation-er_to_golgi_transport_vesicle_membrane | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/adversary-septin/original-checks.json; 20261022T013717Z-er-to-golgi-transport-vesicle-membrane-audit native validate/render and frozen input comparison | supports | Native validate and render exited zero; Markdown is byte-identical. Historical-source, original frozen and current target hashes agree. |
| septin-native-er_to_golgi_transport_vesicle_membrane-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/er_to_golgi_transport_vesicle_membrane-uniprot-verify-receipt.json; Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/er_to_golgi_transport_vesicle_membrane-uniprot-verify.log | supports | Exit zero. No protein_examples, protein UniProtKB graph xrefs or GENE_OR_PROTEIN nodes are represented. Exit zero validates this empty represented inventory only, not narrative named molecules, pathway behavior, source localization or completeness. |
| septin-native-er_to_golgi_transport_vesicle_membrane-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/er_to_golgi_transport_vesicle_membrane-uniprot-causal-receipt.json; Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/er_to_golgi_transport_vesicle_membrane-uniprot-causal.log | supports | Exit zero. No protein_examples, protein UniProtKB graph xrefs or GENE_OR_PROTEIN nodes are represented. Exit zero validates this empty represented inventory only, not narrative named molecules, pathway behavior, source localization or completeness. |
| septin-record-esterosome | data/structures/membrane_organelle/esterosome.yaml; Complete maintained record at 5c140efd0be92d341410aa3024d677d5daf8bc1e | supports | Read identity, definition, hierarchy/parthood, synonyms/xrefs, components, protein examples when present, taxon/example, functions, every evidence note and graph edge, discussions and history. No target images, quantitative properties, associated traits or verbatim snippets are declared. |
| septin-original-esterosome | reviews/structured/20261022T013717Z-esterosome-audit/review.yaml; Complete original YAML/Markdown; source inputs, checks, evidence tiers, assessments, empty findings/actions and limitations | supports | Original qualified positive scientific assessment has no findings/actions. It contains an explicit imodulondb exclusion, not an omitted row. Its historical checks/access dates remain historical; applicability is reassessed from the complete maintained record. |
| septin-original-validation-esterosome | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/adversary-septin/original-checks.json; 20261022T013717Z-esterosome-audit native validate/render and frozen input comparison | supports | Native validate and render exited zero; Markdown is byte-identical. Historical-source, original frozen and current target hashes agree. |
| septin-native-esterosome-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/esterosome-uniprot-verify-receipt.json; Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/esterosome-uniprot-verify.log | supports | Exit zero. Two exact reviewed protein examples P21837/cryS and P18142/D2 validate; the one GENE_OR_PROTEIN node is COVERED through its component_ref. This covers declared identifiers and symbols, not exact family grounding, source localization, stoichiometry, necessity or completeness. |
| septin-native-esterosome-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/esterosome-uniprot-causal-receipt.json; Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/esterosome-uniprot-causal.log | supports | Exit zero. Two exact reviewed protein examples P21837/cryS and P18142/D2 validate; the one GENE_OR_PROTEIN node is COVERED through its component_ref. This covers declared identifiers and symbols, not exact family grounding, source localization, stoichiometry, necessity or completeness. |
| septin-record-esterosome_lumen | data/structures/membrane_organelle/esterosome_lumen.yaml; Complete maintained record at 5c140efd0be92d341410aa3024d677d5daf8bc1e | supports | Read identity, definition, hierarchy/parthood, synonyms/xrefs, components, protein examples when present, taxon/example, functions, every evidence note and graph edge, discussions and history. No target images, quantitative properties, associated traits or verbatim snippets are declared. |
| septin-original-esterosome_lumen | reviews/structured/20261022T013718Z-esterosome-lumen-audit/review.yaml; Complete original YAML/Markdown; source inputs, checks, evidence tiers, assessments, empty findings/actions and limitations | supports | Original qualified positive scientific assessment has no findings/actions. It contains an explicit imodulondb exclusion, not an omitted row. Its historical checks/access dates remain historical; applicability is reassessed from the complete maintained record. |
| septin-original-validation-esterosome_lumen | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/adversary-septin/original-checks.json; 20261022T013718Z-esterosome-lumen-audit native validate/render and frozen input comparison | supports | Native validate and render exited zero; Markdown is byte-identical. Historical-source, original frozen and current target hashes agree. |
| septin-native-esterosome_lumen-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/esterosome_lumen-uniprot-verify-receipt.json; Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/esterosome_lumen-uniprot-verify.log | supports | Exit zero. No protein_examples, protein UniProtKB graph xrefs or GENE_OR_PROTEIN nodes are represented. Exit zero validates this empty represented inventory only, not narrative named molecules, pathway behavior, source localization or completeness. |
| septin-native-esterosome_lumen-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/esterosome_lumen-uniprot-causal-receipt.json; Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/esterosome_lumen-uniprot-causal.log | supports | Exit zero. No protein_examples, protein UniProtKB graph xrefs or GENE_OR_PROTEIN nodes are represented. Exit zero validates this empty represented inventory only, not narrative named molecules, pathway behavior, source localization or completeness. |
| septin-record-esterosome_membrane | data/structures/membrane_organelle/esterosome_membrane.yaml; Complete maintained record at 5c140efd0be92d341410aa3024d677d5daf8bc1e | supports | Read identity, definition, hierarchy/parthood, synonyms/xrefs, components, protein examples when present, taxon/example, functions, every evidence note and graph edge, discussions and history. No target images, quantitative properties, associated traits or verbatim snippets are declared. |
| septin-original-esterosome_membrane | reviews/structured/20261022T013719Z-esterosome-membrane-audit/review.yaml; Complete original YAML/Markdown; source inputs, checks, evidence tiers, assessments, empty findings/actions and limitations | supports | Original qualified positive scientific assessment has no findings/actions. It contains an explicit imodulondb exclusion, not an omitted row. Its historical checks/access dates remain historical; applicability is reassessed from the complete maintained record. |
| septin-original-validation-esterosome_membrane | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/adversary-septin/original-checks.json; 20261022T013719Z-esterosome-membrane-audit native validate/render and frozen input comparison | supports | Native validate and render exited zero; Markdown is byte-identical. Historical-source, original frozen and current target hashes agree. |
| septin-native-esterosome_membrane-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/esterosome_membrane-uniprot-verify-receipt.json; Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/esterosome_membrane-uniprot-verify.log | supports | Exit zero. No protein_examples, protein UniProtKB graph xrefs or GENE_OR_PROTEIN nodes are represented. Exit zero validates this empty represented inventory only, not narrative named molecules, pathway behavior, source localization or completeness. |
| septin-native-esterosome_membrane-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/esterosome_membrane-uniprot-causal-receipt.json; Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/esterosome_membrane-uniprot-causal.log | supports | Exit zero. No protein_examples, protein UniProtKB graph xrefs or GENE_OR_PROTEIN nodes are represented. Exit zero validates this empty represented inventory only, not narrative named molecules, pathway behavior, source localization or completeness. |
| septin-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0012507,GO:0030658,GO:0030662,GO:0030134,GO:0005789,GO:0090114,GO:0030127,GO:0033117,GO:0034467,GO:0033118,GO:0031410,GO:0043233,GO:0030659,GO:0060205; Fourteen exact active GO terms, definitions, synonyms and typed child edges | supports | GO0012507 denotes the ER-to-Golgi surrounding lipid bilayer and has the exact COPII-coated-vesicle-membrane synonym; GO0030658/0030662 are native parent classes and GO0030134 is the containing vesicle. GO0033117 esterosome is_a cytoplasmic vesicle GO0031410 and contains lumen GO0034467 and membrane GO0033118. Membrane is_a GO0030659; lumen directly is_a GO0060205. GO0090114 explicitly describes ER membrane evagination; coat GO0030127 is distinct from the lipid bilayer. |
| septin-lumen-is-a-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0034467/ancestors?relations=is_a; GO0034467 ancestors endpoint restricted to relations=is_a | supports | The returned transitive is_a ancestry includes GO0043233 organelle lumen and GO0060205 cytoplasmic vesicle lumen. The maintained broad parent is supported; no inference from a mixed part_of/is_a path or false direct-edge claim is needed. |
| septin-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Exact ENA taxId, scientificName, rank and lineage | supports | Current species identity is Saccharomyces cerevisiae. This authority check does not establish strain, condition, prevalence, localization or biological mechanism. |
| septin-tax44689 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/44689; Exact ENA taxId, scientificName, rank and lineage | supports | Current species identity is Dictyostelium discoideum. This authority check does not establish strain, condition, prevalence, localization or biological mechanism. |
| septin-SL-0108 | https://rest.uniprot.org/locations/SL-0108.json; Exact UniProt subcellular-location entry and relation-bearing parents | supports | Direct GO0033118 membrane mapping and esterosomal membrane synonym; is_a cytoplasmic vesicle membrane and part_of esterosome. Nested parent mappings are not exact identity matches. |
| septin-SL-0109 | https://rest.uniprot.org/locations/SL-0109.json; Exact UniProt subcellular-location entry and relation-bearing parents | supports | Direct GO0033117 whole-esterosome mapping; is_a cytoplasmic vesicle. Description recognizes crystal-filled vesicles and RER-like boundary. |
| septin-SL-0328 | https://rest.uniprot.org/locations/SL-0328.json; Exact UniProt subcellular-location entry and relation-bearing parents | supports | Direct GO0034467 lumen mapping and esterosomal lumen synonym; is_a cytoplasmic vesicle lumen and part_of esterosome. Protein-count fields are not a claim of biological absence. |
| septin-barlowe1994-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A8004676%20AND%20SRC%3AMED&amp;pageSize=25; Complete primary abstract and exact title/authors/year/DOI/PMID metadata | supports | Barlowe et al.1994, DOI10.1016/0092-8674(94)90138-4. Washed ER membranes plus Sar1, Sec13 complex and Sec23 complex produce COPII-coated vesicles; the abstract distinguishes GTP from GMP-PNP effects on coat retention and subsequent fusion. Supports yeast ER-derived coated-vesicle formation, without auditing full methods or figures. |
| septin-matsuoka1998-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A9568718%20AND%20SRC%3AMED&amp;pageSize=25; Complete primary abstract and exact title/authors/year/DOI/PMID metadata | supports | Matsuoka et al.1998, DOI10.1016/s0092-8674(00)81577-9. Purified Sar1, Sec13/31 and Sec23/24 reconstitute coat assembly and budding on chemically defined liposomes. Phosphoinositide requirements apply to this assay. Synthetic liposome donors do not themselves establish native ER lipid composition or an individual lipid requirement for every membrane. |
| septin-bomblies1990-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A2307702%20AND%20SRC%3AMED&amp;pageSize=25; Complete primary abstract and exact title/authors/year/DOI/PMID metadata | supports | Bomblies et al.1990, DOI10.1083/jcb.110.3.669, PMC2116030. Complete abstract identifies membrane-enclosed Dictyostelium crystals, cryS crystal protein and D2 protein, esterase-like sequence similarity, and stage-dependent accumulation. |
| septin-bomblies-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC2116030.1/PMC2116030.1.xml; Official PMC OA article XML, body preformat pmc-pdf-text: Introduction, Methods, Results and Discussion prose; TableI text and Fig1–11 caption text. Scanned-article OCR, not newly inspected figure pixels or sequence-alignment panels. | supports | Fresh genuine article OCR supports AX2-214/AX3 Dictyostelium experiments: purified crystals contain major69kD crystal protein and56kD D2, N-terminal/cDNA identification and antibodies label the same membrane-enclosed crystals in serial and double-gold sections. The paper explicitly places the proteins in the lumen rather than in the membrane. Ribosome-decorated boundary morphology is RER-like. Cofractionation and immunolabeling suggest co-crystallization but exact composition/ratio requires further recrystallization work. ER sorting, nucleation, physiological function and crystal fate remain hypotheses, and individual formation necessity is not demonstrated. Expression experiments are condition/strain specific; most work AX2, Fig11B cAMP transcripts AX3. |
| septin-bomblies-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC2116030/; Canonical PMC article URL returned an HTML recaptcha challenge despite HTTP200 | context_only | Access diagnostic only; these bytes are not article evidence. Genuine article prose was separately retrieved from the official PMC OA XML endpoint, whose DOI/PMID identity was verified. |
| septin-protein-P21837 | https://rest.uniprot.org/uniprotkb/P21837.json; Exact reviewed accession, recommended protein label, gene, organism, sequence-family similarity and location comments | supports | Current reviewed Crystal protein accession matches cryS and NCBITaxon44689. Location annotation uses SL0108 membrane with a membrane-enclosed-crystal note; this annotation granularity is not primary proof that the protein is a bilayer constituent. The original paper explicitly supports lumenal crystal cargo. Type-B carboxylesterase/lipase similarity does not alone establish esterosome membership, catalysis or necessity. |
| septin-protein-P18142 | https://rest.uniprot.org/uniprotkb/P18142.json; Exact reviewed accession, recommended protein label, gene, organism, sequence-family similarity and location comments | supports | Current reviewed cAMP-regulated D2 protein accession matches D2 and NCBITaxon44689. Location annotation uses SL0108 membrane with a membrane-enclosed-crystal note; this annotation granularity is not primary proof that the protein is a bilayer constituent. The original paper explicitly supports lumenal crystal cargo. Type-B carboxylesterase/lipase similarity does not alone establish esterosome membership, catalysis or necessity. |
| septin-interpro-P21837 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P21837/?page_size=100; Complete four-result exact-protein integrated InterPro response; metadata.type and member databases | supports | Returned IPR002018 is typed domain (member PF00135), IPR019819 conserved_site, IPR019826 active_site and IPR029058 homologous_superfamily. No integrated family-typed entry occurs in this complete exact-protein response. Under the native family-consensus policy these domain/site/superfamily entries do not establish an exact family-grounding correction. This bounded result does not prove that no ontology can ever supply a suitable class. |
| septin-interpro-P18142 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P18142/?page_size=100; Complete four-result exact-protein integrated InterPro response; metadata.type and member databases | supports | Returned IPR002018 is typed domain (member PF00135), IPR019819 conserved_site, IPR019826 active_site and IPR029058 homologous_superfamily. No integrated family-typed entry occurs in this complete exact-protein response. Under the native family-consensus policy these domain/site/superfamily entries do not establish an exact family-grounding correction. This bounded result does not prove that no ontology can ever supply a suitable class. |
| septin-catalogue | https://imodulondb.org/api/datasets; Complete official returned organism and dataset catalogue; actual target taxa and keys | supports | No matched Saccharomyces cerevisiae or Dictyostelium discoideum organism/dataset is returned. ER-to-Golgi membrane asserts named COPII machinery; whole esterosome and its lumen assert cryS/crystal protein and D2 context. Their applicability was assessed, but no matched-host downstream gene/module query is justified. The esterosome membrane has genuine material/topological scope. Noncoverage is not negative biological evidence. |
| septin-historical-adapter-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Actual historical datasets invocation00:49:00.848907Z–00:49:00.863225Z | context_only | Historical canary command exited1 with PermissionError reading pyvenv.cfg. This is a retained earlier unavailable-runner observation, not a fresh invocation or success. The present catalogue fallback is a distinct actual source retrieval. |
| septin-source-access | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/adversary-septin/source-receipts.json; Actual fresh URLs, access timestamps and hashes | supports | Current authorities, catalogue, exact-protein InterPro and three primary abstract responses were freshly fetched. Genuine Bomblies article OCR came from official PMC OA XML; canonical PMC HTML was a bot challenge. Barlowe/Matsuoka are complete-primary-abstract tiers only, with no full-body access claim. |
| septin-common-policy-reuse | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/adversary-septin/common-policy-hash-reuse.json; Seventeen previously read common policy/schema/native inputs checked against current freeze | supports | Current common input bytes match the prior read versions. Component-grounding and native family-consensus guidance additionally reread. No extra repository neighbor, prior category review or unfrozen script was used. |
| check-qc | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/qc.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| check-labels | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/labels.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| check-trait-links | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/trait-links.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Native TraitMech link check passed. |
| check-vendored | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/vendored.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Pinned governed files match; native vendored check passed. |
| check-curies | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/curies.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| focused | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/focused-results.json; All twenty actual target schema/strict command outputs | supports | Ten schema and ten strict commands returned exit zero. |
| supplemental-pmid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/pmid-chunks-receipt.json; Complete native-report PMID set checked with unchanged resolver in batches of at most fifty | supports | 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers remain unverified. |
| historical-adapter-runner-availability | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner invocation receipt, exact SHA256 reverified during PR2365 synthesis | context_only | Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS PermissionError reading the configured runner pyvenv.cfg. This is a retained historical availability observation, not a fresh attempt or a scientific validation failure. Native policy permits inspected source-catalogue fallback. |

## Limits And Additional Notes

- Endosome lumen/membrane and epiplastidial membrane independent subreview: Assigned endosome lumen/membrane and epiplastidial membrane only; all unchanged from original frozen hashes. Two inherited minor EpM findings retain exact keys, severities and repository/review/finding lineage. No historical neighbor/group/category resolution is implied.
- Endosome lumen/membrane and epiplastidial membrane independent subreview: Fresh Katzmann2001 and Babst2002 complete primary abstracts only. Henne2011 and Hashimoto2005 are secondary review abstracts only; no full bodies or figure pixels read for those four sources. Katzmann2003 genuine PMC Resultssec5/sec6 and Methodssec12 with Fig3/4 captions read; no quantitative or figure-pixel reanalysis.
- Endosome lumen/membrane and epiplastidial membrane independent subreview: Flori2016 published PDF p255 text/Fig1 caption and actual Fig1 pixels, Results opening p256/fullp261, Discussion/Methodspp263–264 and associated Fig5/6 caption text read. Other pixels, supplements/raw measurements and unlisted pages were not independently audited. Phaeodactylum Pt1 CCAP1055/3 disrupted/intact preparations remain distinct.
- Endosome lumen/membrane and epiplastidial membrane independent subreview: Gueguen2024 JATS scope: Introduction s1/Fig1caption, Results s2.4/Fig2–3captions, Discussion s3.2/s3.8, Methods s4.4/s4.13. No figure pixels, supplements or other sections. Pt1 Strain8.6 CCAP1055/1 is retained; qualified localization and uncertain lipid pools are not formation necessity.
- Endosome lumen/membrane and epiplastidial membrane independent subreview: Fresh GO definitions and broader/direct versus nested anatomy are distinguished. EpM definition is an exact authority quotation; diatom evidence does not experimentally establish ER continuity for all secondary-plastid lineages. F1 concerns adjacent-interface ambiguity, not denial of valid indirect PPC enclosure.
- Endosome lumen/membrane and epiplastidial membrane independent subreview: Whole bilayer ESSENTIAL is defining collective constitution; no individual-lipid necessity is proven. No missing optional protein/family inventory is fabricated. Empty protein inventory checks for lumen/EpM and one verified external VPS27 graph node for membrane have distinct scopes.
- Endosome lumen/membrane and epiplastidial membrane independent subreview: Both endosome records require molecular/pathway applicability assessment. Fresh official catalogue has no relevant eukaryotic host match; no downstream gene/module query or unrelated proxy applies. EpM is a genuine complete-record material/topology exclusion. Historical runner receipt remains actual00:49Z unavailable; no fresh invocation or success claimed.
- Endosome lumen/membrane and epiplastidial membrane independent subreview: Three frozen neighbor records were read only for identity/boundary context. Root owns global QC/issues/publication and all repository/GitHub writes; scientific records remain unchanged.
- Exoneme, eyespot apparatus and ferrosome independent subreview: Exoneme/eyespot/ferrosome slice: three entire current records and immutable original pairs read; no additional local neighbor used. Current eyespot example substantively refreshed, no original history overwritten or new scientific predecessor invented.
- Exoneme, eyespot apparatus and ferrosome independent subreview: Exoneme source tier: Yeoh2007 and Blackman1998 complete primary abstracts only; fresh publisher PDF403 retained. Blackman2008 is secondary review, one complete named subsection. Withers2014 Intro and Discussion provide attributed background, not independent discharge experiments; its Results/Methods/pixels not inspected. Nasamu2017 complete scientific main text/Fig1–4 captions read, no separate supplementary Methods/pixels; NF54 experiments are not recast as direct3D7 measurements.
- Exoneme, eyespot apparatus and ferrosome independent subreview: Eyespot source tier: Lamb1999 complete primary abstract only. Schmidt selected complete paragraphs, Table1 photoreceptor rows and cw15 purification Methods inspected; contamination and lost-soluble-protein limitations retained. Mittelmeier Intro/first Results/captions and strain/media Methods; Awasthi introductory and initial localization/strain/antibody scope; Ueki late Results, captions, Discussion/main Methods. No current source figure pixels, movies, raw proteomic data or complete supplemental datasets inspected. Original historical pixel inspection is not represented as current.
- Exoneme, eyespot apparatus and ferrosome independent subreview: Eyespot interpretation: literal COP3 UniProt index returns zero while native acop1 entry and primary alias mapping support Q93WP2; this is not absence of COP3. Direct ChR1 localization is distinct from COP4 fraction association and Cop8 trafficking. Unreviewed and automated annotations are not direct localization or exact-family groundings.
- Exoneme, eyespot apparatus and ferrosome independent subreview: Ferrosome source tier: Grant main scientific Introduction/Results/Discussion read; Methods, extended-data captions, supplementary tables and pixels not independently inspected in this pass. Byrne entire main scientific text/main Methods and Fig1–5 captions read without pixels/supplements. RS-1 supplies formation genetics/ultrastructure; direct anaerobic starvation-fitness/rescue is S.putrefaciens. Individual Fez necessity, transport substrate, exact core chemistry and universal function remain unresolved.
- Exoneme, eyespot apparatus and ferrosome independent subreview: Adapter/native limits: all three original rows are unsupported expression-only exclusions, corrected by a fresh official catalogue with no target-organism match. E.coli foreign-operon experimental host is not a matched native RS-1 proxy. Historical00:49Z runner failure retained honestly; current fetch DNS failures archived and numeric-PMC challenge excluded from body evidence. Actual protein inventories are exoneme2examples+2xrefs/3nodes,eyespot2examples/1node,ferrosome3examples/1node. No global gates, future CI or queue outcomes borrowed from root before actual receipts.
- Exoneme, eyespot apparatus and ferrosome independent subreview: Local inputs:17 common instructions/schema/verifier hashes equal preceding reviewed bytes; applicable skill/profile/config/checklist/protein guidance reread. Other retained instruction/schema reads are not represented as fresh full-file inspection. No repository/GitHub mutation; root authors successor and handles QC/issue publication.
- ER-to-Golgi transport-vesicle membrane and esterosome trio independent subreview: All four targets equal their original frozen and historical-source hashes; none is stale. Four original native validation/render checks pass and findings/actions are empty. No scientific predecessor, severity normalization or terminal historical disposition is invented.
- ER-to-Golgi transport-vesicle membrane and esterosome trio independent subreview: Barlowe and Matsuoka access is complete primary abstract plus exact metadata only. No full methods, detailed strain list, figure pixels or quantitative result reanalysis is certified. Matsuoka uses chemically defined liposome donors; native ER membrane donation also relies on GO and Barlowe.
- ER-to-Golgi transport-vesicle membrane and esterosome trio independent subreview: Bomblies evidence is fresh genuine official PMC OA XML containing scanned-article OCR. Introduction/Methods/Results/Discussion prose, TableI text and Fig1–11 caption text were read; sequence-alignment panels and source figure pixels/raw data were not reanalyzed. Canonical PMC HTML returned a challenge despite HTTP200 and was not article evidence.
- ER-to-Golgi transport-vesicle membrane and esterosome trio independent subreview: Bomblies supports stage-bounded membrane-enclosed crystals and major cryS/D2 constituents. Co-crystallization ratio, crystal sorting/nucleation/fate, physiological role, catalysis of purified proteins and individual formation necessity remain unresolved. The graph is explicitly NONMECHANISTIC; descriptive storage is not a proven physiological purpose.
- ER-to-Golgi transport-vesicle membrane and esterosome trio independent subreview: Reviewed UniProt protein entries carry membrane-location SL0108 annotation with membrane-enclosed-crystal notes. Primary prose explicitly places the proteins in the lumen; those authority annotations are not independent direct-bilayer membership evidence.
- ER-to-Golgi transport-vesicle membrane and esterosome trio independent subreview: Complete exact-protein InterPro responses return only domain/site/superfamily types, not integrated families. Native family-consensus policy excludes those types. This supports bounded label-only retention, not an exhaustive assertion that no exact term exists in any ontology.
- ER-to-Golgi transport-vesicle membrane and esterosome trio independent subreview: Three records trigger named molecular/pathway applicability; the fresh complete catalogue lacks their actual hosts. No unmatched-host gene/module query or negative biological inference is used. Esterosome membrane has genuine material/morphology-only scope and is excluded without a manufactured fourth bundle defect. Historical runner unavailability remains00:49Z, not a fresh execution.
- ER-to-Golgi transport-vesicle membrane and esterosome trio independent subreview: All eight current native protein commands passed. Whole esterosome has two validated examples and one COVERED typed molecular node; other three represented inventories are empty. Native checks do not certify narrative claims, complete composition, source localization or necessity.
- ER-to-Golgi transport-vesicle membrane and esterosome trio independent subreview: Only four assigned targets, eight original artifacts and seventeen byte-verified common policy/schema/native inputs were used locally. Other frozen cohort neighbors were not judged. No target image, quantitative property, trait link or verbatim snippet is declared.
- ER-to-Golgi transport-vesicle membrane and esterosome trio independent subreview: Root owns global gates, issue dedup/publication, repository/GitHub mutations and final-head/CI/queue checks. This report makes no future-gate or merge attestation and edits no records.
- Historical observations remain immutable; their old checks are not represented as current-head execution.
- The adapter runner was not rerun after the canary established OS access failure. Catalogue-based coverage is assessed directly; fresh and reused responses retain actual access timestamps.
- Native label checks include 923 no-adapter skips. Native identifier checks include 909 PMID transport failures and 254 skipped identifiers; bounded supplemental checks independently resolve the 909 PMIDs.
- Scientific record-curation findings stay in separate issues; no record is edited by this review PR.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after saving this immutable observation and are not represented here as already completed.
- All ten original YAML/Markdown pairs remain unchanged. Current main was merged normally and pushed without force.
- This explicit issue-bearing ten-record cohort follows the native persistence policy. All three inherited minor scientific findings retain stable keys and exact predecessor repository/review/finding identities.
- Issue #2690 tracks the stale eyespot-apparatus input. Current main adds Q93WP2/acop1, an unreviewed Chlamydomonas reinhardtii channelopsin-1 example, alongside Q8RUT8/cop4. Fresh UniProt identity and Schmidt2006 Table1 COP3/CHOP1/CSRA/Acop1 nomenclature with peptide support substantively establish the bounded bridge. Identity, apparatus membership and directional phototaxis claims remain separate evidence scopes.
- Issue #2691 tracks eight unsupported applicability exclusions. All ten original bundles contain an explicit imodulondb not_applicable row. Positive pathway or molecular assertions make the endosome lumen/membrane, ER-to-Golgi transport-vesicle membrane, esterosome/lumen, exoneme, eyespot and ferrosome records subject to a coverage check. Epiplastidial membrane and esterosome membrane retain genuine material/topology exclusions.
- Source commit 5c140efd0be92d341410aa3024d677d5daf8bc1e is retained by tag review-base/pr2365-current-record-followup-20261103.
- CLAUDE.md is an alias of AGENTS.md; canonical regular AGENTS.md bytes are frozen.
- All 50 local inputs were frozen before their assessment. The multivesicular-body lumen, intraluminal-vesicle and periplastidial-membrane records supply boundary context only; they are not additional review targets or dispositions of their findings.
- Fresh and reused source snapshots retain actual access timestamps and inspection tiers. Authority identity does not independently establish structure membership, mechanistic action, species-wide generalization or assembly necessity.
- All twenty native protein commands returned zero. Endosome membrane has one UNANCHORED_WITH_UNIPROT Vps27 node with verified P40343 xref. Esterosome has two reviewed examples, cryS/P21837 and D2/P18142, and one COVERED node. Exoneme has two reviewed component examples SUB1/O61142 and PMX/Q8IAS0 and three typed nodes: two COVERED plus an UNANCHORED_WITH_UNIPROT substrate-cohort node with Q9TY95/Q8I0U8 xrefs. Eyespot has two unreviewed examples and one COVERED node. Ferrosome has three unreviewed DMR/Fez examples and one COVERED node. The other five targets have empty represented inventories and zero typed molecular nodes. These checks do not certify all narrative claims or prove membership.
- Two inherited minor epiplastidial-membrane findings concern direct adjacent-space wording and a mechanistic label on a descriptive boundary graph. One inherited minor exoneme finding concerns an exact SUB1 family mapping now supported by IPR017314; a catalytic domain or broad PMX family does not resolve the same question.
- The two issue-bearing targets need curation; the other eight have qualified positive assessments. Native-validator issue #2514 is reused and remains open. Scientific findings remain separate from the bundle fixes.
- Ferrosome formation/genetic evidence in RS-1 is distinguished from the iron-starvation fitness result in Shewanella putrefaciens CN32. No universal fitness phenotype or individual Fez necessity is inferred. Heterologous expression in E. coli is not native matched-host expression-dataset coverage.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T134837Z-pr2365-current-record-followup
kind: batch
repository: CultureBotAI/CellStructureMech
title: 'PR 2365: current-input review of ten records and adversarial follow-up'
started_at: '2026-11-03T13:37:13.889656Z'
finished_at: '2026-11-03T13:48:37Z'
reviewer:
  identity: Codex root synthesis with three independent read-only adversarial reviewers
  kind: agent
  independence: self_review
  independence_basis: Root authors this synthesis of three separate read-only reviews.
    Independent reviewers inspected original bundles, current record bytes and primary/authority
    sources, and did not author or modify repository files. They independently re-review
    the final saved head before merge-queue admission. This is not human scientific
    sign-off.
skill: .claude/skills/review-yaml-record/SKILL.md; explicit batch route in docs/record-review-profile.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Current-input reassessment of all ten records in PR2365. One stale eyespot-apparatus
  review is substantively refreshed and eight structured-source applicability exclusions
  are corrected. Three inherited minor scientific findings remain open for separate
  record curation; no records are edited.
source:
  git_revision: 5c140efd0be92d341410aa3024d677d5daf8bc1e
  state: working_tree
  inputs:
  - path: .claude/skills/add-cell-structure/SKILL.md
    sha256: eee04ee51d2c82c05df98570674084bdce9001e5aa67d6230ac1ed50064a3175
    role: context
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
  - path: AGENTS.md
    sha256: ef74a980161b55cd24f1851e38d1c0b2e004fcf8837f1bc70da1874e4e8380f0
    role: context
  - path: conf/record_review.yaml
    sha256: d3334a12b8a616a7638f1195748085d2b543fba7df67ad4ff8fcc0ac18f2d3ee
    role: context
  - path: data/structures/membrane_organelle/endosome_lumen.yaml
    sha256: 7522ffb363729241f2263bef6ebf96cb135a807c677df546e0b4ae92fe2bc604
    role: target
  - path: data/structures/membrane_organelle/endosome_membrane.yaml
    sha256: 564b0ecf02448e0dab2210a213597b20b57ebfe09bf7637dfe2bed79a1b95270
    role: target
  - path: data/structures/membrane_organelle/epiplastidial_membrane.yaml
    sha256: 15876d75b2efb4115edcf9f6ffa44a5254fcf104c9f543d7eb07b78a5f06db8a
    role: target
  - path: data/structures/membrane_organelle/er_to_golgi_transport_vesicle_membrane.yaml
    sha256: 5cdd951707eead318295ce7ceb64c16bdc0c85b465374678d564878481f04a9c
    role: target
  - path: data/structures/membrane_organelle/esterosome.yaml
    sha256: c5779634687c3e16478f4782e24897bc8df7939f14eddfd26ec4715c6de3c95a
    role: target
  - path: data/structures/membrane_organelle/esterosome_lumen.yaml
    sha256: 6891a8c551bc57b8ab1ce07357d050e40b46303debc2de0b81132b54424b53a4
    role: target
  - path: data/structures/membrane_organelle/esterosome_membrane.yaml
    sha256: b29aff5dceea8ed56348277d76f1c3658da2f304baa1b8e9858bf64cea5f4e5a
    role: target
  - path: data/structures/membrane_organelle/exoneme.yaml
    sha256: 2e32d7ca2f38ab39d5e1eb57cf683833fed5fdf18337191a3302689058d3b4b4
    role: target
  - path: data/structures/membrane_organelle/eyespot_apparatus.yaml
    sha256: 46c34aa696b5a0672d295e04dd475009d79c5c51b22aebe5afd541ccb97bc248
    role: target
  - path: data/structures/membrane_organelle/ferrosome.yaml
    sha256: a8350e9f852acd4d6cb753caba52b5f70ba3002f73f48e083ac047d0db405a6f
    role: target
  - path: data/structures/membrane_organelle/multivesicular_body_intraluminal_vesicle.yaml
    sha256: 47e5f39198c321eb8e1df58ff20ac1a0a50ec731170ae0f9d07d22b299594916
    role: context
  - path: data/structures/membrane_organelle/multivesicular_body_lumen.yaml
    sha256: 6c67050e4fa82c1a03f0476a13be57741651c0ad9e1d4bfa241ca500525175f6
    role: context
  - path: data/structures/membrane_organelle/periplastidial_membrane.yaml
    sha256: 96374ff1877ac9701ca4104ebc8e7218aee2345b6d2170b35cf64e6c30f6188a
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
  - path: reviews/structured/20261022T013714Z-endosome-lumen-audit/review.md
    sha256: 65d9bf5d5e9e919cf89204e2981caadeeb9fe9070044299ab22094fd2bb72135
    role: context
  - path: reviews/structured/20261022T013714Z-endosome-lumen-audit/review.yaml
    sha256: f2bb53780f7d9b4bd704c73ba0222870690642380c53af8f72cff8a321ad40be
    role: context
  - path: reviews/structured/20261022T013715Z-endosome-membrane-audit/review.md
    sha256: eea93c592817f3292a2f8ef1e4c8e2e628a9a5d7f2086084e0fb7f227e92c921
    role: context
  - path: reviews/structured/20261022T013715Z-endosome-membrane-audit/review.yaml
    sha256: 7f72a4c56dfdf4ee7290a35ac5ec24a16649276574282b7fcf2bd8cafad48105
    role: context
  - path: reviews/structured/20261022T013716Z-epiplastidial-membrane-audit/review.md
    sha256: 140f3f6c70093b72691dd9159d117d6aab400af24842350e9b4a32cfc826622f
    role: context
  - path: reviews/structured/20261022T013716Z-epiplastidial-membrane-audit/review.yaml
    sha256: d1140ae276b9314ea234477f7dcb262ffe6d057c9b15d1b3fbfd31cd4af2535b
    role: context
  - path: reviews/structured/20261022T013717Z-er-to-golgi-transport-vesicle-membrane-audit/review.md
    sha256: b2fc37b6932920ace835fa9a2cdac11b932af54893a91c6f1db835e04a496a2c
    role: context
  - path: reviews/structured/20261022T013717Z-er-to-golgi-transport-vesicle-membrane-audit/review.yaml
    sha256: 443302a78569d841b938a4a245ed64efbb78f00364a5a238e5e99889992ccac5
    role: context
  - path: reviews/structured/20261022T013717Z-esterosome-audit/review.md
    sha256: 24f2e2096cedcb890a2bf82c3857ff2dfd36fc2be5b34b836bf14fec432a7beb
    role: context
  - path: reviews/structured/20261022T013717Z-esterosome-audit/review.yaml
    sha256: 3771f361702237469102a561833617eb0a3e6b5bb070204d184e8311067b20e9
    role: context
  - path: reviews/structured/20261022T013718Z-esterosome-lumen-audit/review.md
    sha256: c9e644158424bce2a5470b6ada7c7829a31c9a8db8e25e568a4dce7e7d5eb0d0
    role: context
  - path: reviews/structured/20261022T013718Z-esterosome-lumen-audit/review.yaml
    sha256: 95bb137bbc197c2b8e26c6b030050aa97f3dd20d330b6be25c6c8ec5a37345cc
    role: context
  - path: reviews/structured/20261022T013719Z-esterosome-membrane-audit/review.md
    sha256: a2bdc2bcae24055f813ec397831387be078e63491ffc268e5fc6dd97938a0e6d
    role: context
  - path: reviews/structured/20261022T013719Z-esterosome-membrane-audit/review.yaml
    sha256: 5caf336f1791fa5d7564ce6e976de292b62a9853d3f9728a37c9e665aa59e3d8
    role: context
  - path: reviews/structured/20261022T013720Z-exoneme-audit/review.md
    sha256: cafab6aa752f9d610062e1e2a4a98a94e04010bed5eb45e7ffe25a41d2658dfc
    role: context
  - path: reviews/structured/20261022T013720Z-exoneme-audit/review.yaml
    sha256: a8b4a809b8586315722ef09a34b458810a8f50d52a64fc026202f245a428cca5
    role: context
  - path: reviews/structured/20261022T013720Z-eyespot-apparatus-audit/review.md
    sha256: 0c5bb165faa01eec9721dfe45fe6d525772b65538056cd34342024ba227e6c47
    role: context
  - path: reviews/structured/20261022T013720Z-eyespot-apparatus-audit/review.yaml
    sha256: 30a96b63dbe341e4e627fee1d7f5c680ae5f9ec2640d854df3e9b1d375e8628d
    role: context
  - path: reviews/structured/20261022T013721Z-ferrosome-audit/review.md
    sha256: 38e0e601468ef08dfada70f90c06e7680db549f98c658a40cd2b57dfe2c5dbf8
    role: context
  - path: reviews/structured/20261022T013721Z-ferrosome-audit/review.yaml
    sha256: 6f0bbcd05a43e646ee0d4c07947151af79bee44a44eaa6185fe85b89e46149fc
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/uniprot_genes.py
    sha256: 8eaca44c9977fed92594e9bb2376d9e03a167546fd08932f2aa8b7d504605aa4
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: GO:0031904
  path: data/structures/membrane_organelle/endosome_lumen.yaml
  label: endosome lumen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/endosome_lumen.yaml
    role: maintained scientific record
- target_id: GO:0010008
  path: data/structures/membrane_organelle/endosome_membrane.yaml
  label: endosome membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/endosome_membrane.yaml
    role: maintained scientific record
- target_id: GO:7770040
  path: data/structures/membrane_organelle/epiplastidial_membrane.yaml
  label: epiplastidial membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/epiplastidial_membrane.yaml
    role: maintained scientific record
- target_id: GO:0012507
  path: data/structures/membrane_organelle/er_to_golgi_transport_vesicle_membrane.yaml
  label: ER to Golgi transport vesicle membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/er_to_golgi_transport_vesicle_membrane.yaml
    role: maintained scientific record
- target_id: GO:0033117
  path: data/structures/membrane_organelle/esterosome.yaml
  label: esterosome
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/esterosome.yaml
    role: maintained scientific record
- target_id: GO:0034467
  path: data/structures/membrane_organelle/esterosome_lumen.yaml
  label: esterosome lumen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/esterosome_lumen.yaml
    role: maintained scientific record
- target_id: GO:0033118
  path: data/structures/membrane_organelle/esterosome_membrane.yaml
  label: esterosome membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/esterosome_membrane.yaml
    role: maintained scientific record
- target_id: GO:0044311
  path: data/structures/membrane_organelle/exoneme.yaml
  label: exoneme
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/exoneme.yaml
    role: maintained scientific record
- target_id: GO:1990413
  path: data/structures/membrane_organelle/eyespot_apparatus.yaml
  label: eyespot apparatus
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/eyespot_apparatus.yaml
    role: maintained scientific record
- target_id: cellstructuremech:ferrosome
  path: data/structures/membrane_organelle/ferrosome.yaml
  label: ferrosome
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/ferrosome.yaml
    role: maintained scientific record
scope:
  description: Exact ten-record PR cohort reassessed against current main 948585dbdfa24febd7412aa677c2251ac88c9cff.
    Changed inputs are substantively reassessed. Scientific records remain unchanged.
  selection: Complete cohort of ten maintained records reviewed in original PR head
    6a8478248be0609ee4c6b873ba243b0105311365.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - GO:0031904
  - GO:0010008
  - GO:7770040
  - GO:0012507
  - GO:0033117
  - GO:0034467
  - GO:0033118
  - GO:0044311
  - GO:1990413
  - cellstructuremech:ferrosome
checks:
- check_id: qc
  name: Full native QC
  status: passed
  required: true
  target_ids:
  - GO:0031904
  - GO:0010008
  - GO:7770040
  - GO:0012507
  - GO:0033117
  - GO:0034467
  - GO:0033118
  - GO:0044311
  - GO:1990413
  - cellstructuremech:ferrosome
  command: just qc
  exit_code: 0
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  scope_note: Actual local execution at main-merge head 5c140efd0be92d341410aa3024d677d5daf8bc1e.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-qc
- check_id: labels
  name: Native label correspondence
  status: passed
  required: true
  target_ids:
  - GO:0031904
  - GO:0010008
  - GO:7770040
  - GO:0012507
  - GO:0033117
  - GO:0034467
  - GO:0033118
  - GO:0044311
  - GO:1990413
  - cellstructuremech:ferrosome
  command: just validate-products
  exit_code: 0
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  scope_note: Actual local execution at main-merge head 5c140efd0be92d341410aa3024d677d5daf8bc1e.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-labels
- check_id: trait-links
  name: TraitMech references
  status: passed
  required: true
  target_ids:
  - GO:0031904
  - GO:0010008
  - GO:7770040
  - GO:0012507
  - GO:0033117
  - GO:0034467
  - GO:0033118
  - GO:0044311
  - GO:1990413
  - cellstructuremech:ferrosome
  command: just check-trait-links --check
  exit_code: 0
  summary: Native TraitMech link check passed.
  scope_note: Actual local execution at main-merge head 5c140efd0be92d341410aa3024d677d5daf8bc1e.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-trait-links
- check_id: vendored
  name: Pinned governed files
  status: passed
  required: true
  target_ids:
  - GO:0031904
  - GO:0010008
  - GO:7770040
  - GO:0012507
  - GO:0033117
  - GO:0034467
  - GO:0033118
  - GO:0044311
  - GO:1990413
  - cellstructuremech:ferrosome
  command: just vendored-check
  exit_code: 0
  summary: Pinned governed files match; native vendored check passed.
  scope_note: Actual local execution at main-merge head 5c140efd0be92d341410aa3024d677d5daf8bc1e.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-vendored
- check_id: curies
  name: Native identifier resolver
  status: passed
  required: true
  target_ids:
  - GO:0031904
  - GO:0010008
  - GO:7770040
  - GO:0012507
  - GO:0033117
  - GO:0034467
  - GO:0033118
  - GO:0044311
  - GO:1990413
  - cellstructuremech:ferrosome
  command: just check-curies
  exit_code: 0
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  scope_note: Actual local execution at main-merge head 5c140efd0be92d341410aa3024d677d5daf8bc1e.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-curies
- check_id: focused-0
  name: validate GO:0031904
  status: passed
  required: true
  target_ids:
  - GO:0031904
  command: just validate data/structures/membrane_organelle/endosome_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-1
  name: validate-strict GO:0031904
  status: passed
  required: true
  target_ids:
  - GO:0031904
  command: just validate-strict data/structures/membrane_organelle/endosome_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-2
  name: validate GO:0010008
  status: passed
  required: true
  target_ids:
  - GO:0010008
  command: just validate data/structures/membrane_organelle/endosome_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-3
  name: validate-strict GO:0010008
  status: passed
  required: true
  target_ids:
  - GO:0010008
  command: just validate-strict data/structures/membrane_organelle/endosome_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-4
  name: validate GO:7770040
  status: passed
  required: true
  target_ids:
  - GO:7770040
  command: just validate data/structures/membrane_organelle/epiplastidial_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-5
  name: validate-strict GO:7770040
  status: passed
  required: true
  target_ids:
  - GO:7770040
  command: just validate-strict data/structures/membrane_organelle/epiplastidial_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-6
  name: validate GO:0012507
  status: passed
  required: true
  target_ids:
  - GO:0012507
  command: just validate data/structures/membrane_organelle/er_to_golgi_transport_vesicle_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-7
  name: validate-strict GO:0012507
  status: passed
  required: true
  target_ids:
  - GO:0012507
  command: just validate-strict data/structures/membrane_organelle/er_to_golgi_transport_vesicle_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-8
  name: validate GO:0033117
  status: passed
  required: true
  target_ids:
  - GO:0033117
  command: just validate data/structures/membrane_organelle/esterosome.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-9
  name: validate-strict GO:0033117
  status: passed
  required: true
  target_ids:
  - GO:0033117
  command: just validate-strict data/structures/membrane_organelle/esterosome.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-10
  name: validate GO:0034467
  status: passed
  required: true
  target_ids:
  - GO:0034467
  command: just validate data/structures/membrane_organelle/esterosome_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-11
  name: validate-strict GO:0034467
  status: passed
  required: true
  target_ids:
  - GO:0034467
  command: just validate-strict data/structures/membrane_organelle/esterosome_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-12
  name: validate GO:0033118
  status: passed
  required: true
  target_ids:
  - GO:0033118
  command: just validate data/structures/membrane_organelle/esterosome_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-13
  name: validate-strict GO:0033118
  status: passed
  required: true
  target_ids:
  - GO:0033118
  command: just validate-strict data/structures/membrane_organelle/esterosome_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-14
  name: validate GO:0044311
  status: passed
  required: true
  target_ids:
  - GO:0044311
  command: just validate data/structures/membrane_organelle/exoneme.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-15
  name: validate-strict GO:0044311
  status: passed
  required: true
  target_ids:
  - GO:0044311
  command: just validate-strict data/structures/membrane_organelle/exoneme.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-16
  name: validate GO:1990413
  status: passed
  required: true
  target_ids:
  - GO:1990413
  command: just validate data/structures/membrane_organelle/eyespot_apparatus.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-17
  name: validate-strict GO:1990413
  status: passed
  required: true
  target_ids:
  - GO:1990413
  command: just validate-strict data/structures/membrane_organelle/eyespot_apparatus.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-18
  name: validate cellstructuremech:ferrosome
  status: passed
  required: true
  target_ids:
  - cellstructuremech:ferrosome
  command: just validate data/structures/membrane_organelle/ferrosome.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-19
  name: validate-strict cellstructuremech:ferrosome
  status: passed
  required: true
  target_ids:
  - cellstructuremech:ferrosome
  command: just validate-strict data/structures/membrane_organelle/ferrosome.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: supplemental-pmid
  name: Supplemental bounded PMID authority checks
  status: passed
  required: true
  target_ids:
  - GO:0031904
  - GO:0010008
  - GO:7770040
  - GO:0012507
  - GO:0033117
  - GO:0034467
  - GO:0033118
  - GO:0044311
  - GO:1990413
  - cellstructuremech:ferrosome
  command: .venv/bin/python /private/tmp/cellstructure-batches-2346-2397-20261103/check_pmid_chunks.py
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365
  exit_code: 0
  summary: 909 PMIDs all OK in bounded native requests; full-command limitations remain
    separate.
  evidence_ids:
  - supplemental-pmid
- check_id: structured-source-applicability
  name: Official structured-source applicability and covered-dataset cross-checks
  status: passed
  required: false
  target_ids:
  - GO:0031904
  - GO:0010008
  - GO:7770040
  - GO:0012507
  - GO:0033117
  - GO:0034467
  - GO:0033118
  - GO:0044311
  - GO:1990413
  - cellstructuremech:ferrosome
  summary: Eight explicit narrow exclusions are corrected after inspecting positive
    molecular and pathway assertions. Official catalogue responses and bounded organism/strain
    searches found no matching datasets for the reviewed native hosts; heterologous
    expression and unrelated-organism datasets are not substituted. Epiplastidial
    membrane and esterosome membrane remain genuinely excluded by their limited material/topology
    claims. Catalogue noncoverage is not biological absence. Historical runner unavailability
    retains its actual date and is not a fresh invocation.
  evidence_ids:
  - plaque-catalogue
  - plaque-historical-runner
  - micro-catalogue
  - septin-catalogue
- check_id: independent-scientific-review
  name: Independent claim-level source review
  status: passed
  required: true
  target_ids:
  - GO:0031904
  - GO:0010008
  - GO:7770040
  - GO:0012507
  - GO:0033117
  - GO:0034467
  - GO:0033118
  - GO:0044311
  - GO:1990413
  - cellstructuremech:ferrosome
  summary: Three read-only reviewers covered the complete ten-record cohort, including
    changed inputs, with explicit scientific findings and source-access limits. Final
    artifact/head acceptance occurs after saving.
  evidence_ids:
  - plaque-policy
  - plaque-rubric
  - plaque-graph-rubric
  - plaque-protein-contract
  - plaque-schema-policy
  - plaque-go
  - plaque-tax4932
  - plaque-tax559292
  - plaque-tax2850
  - plaque-sl0340
  - plaque-protein-P40343
  - plaque-katzmann2001-meta
  - plaque-katzmann2003-meta
  - plaque-babst2002-meta
  - plaque-henne2011-meta
  - plaque-flori2016-meta
  - plaque-gueguen2024-meta
  - plaque-hashimoto2005-meta
  - plaque-katzmann2003-pmc
  - plaque-flori2016-oceanomics-pdf
  - plaque-gueguen2024-jats
  - plaque-catalogue
  - micro-policy
  - micro-protein-contract
  - micro-exo-go
  - micro-exo-tax5833
  - micro-exo-tax36329
  - micro-exo-yeoh2007-meta
  - micro-exo-blackman1998-meta
  - micro-exo-blackman2008-meta
  - micro-exo-withers2014-meta
  - micro-exo-nasamu2017-meta
  - micro-exo-blackman2008-jats
  - micro-exo-withers2014-jats
  - micro-exo-nasamu2017-jats
  - micro-exo-O61142
  - micro-exo-Q8IAS0
  - micro-exo-Q9TY95
  - micro-exo-Q8I0U8
  - micro-exo-sub1-query
  - micro-exo-pmx-query
  - micro-exo-IPR017314
  - micro-exo-IPR034204
  - micro-exo-IPR001461
  - micro-eye-go
  - micro-eye-tax3055
  - micro-eye-lamb1999-meta
  - micro-eye-schmidt2006-meta
  - micro-eye-mittelmeier2011-meta
  - micro-eye-awasthi2016-meta
  - micro-eye-ueki2016-meta
  - micro-eye-protein-Q8RUT8
  - micro-eye-query-COP3-true
  - micro-eye-query-COP3-false
  - micro-eye-query-COP4-true
  - micro-eye-query-COP4-false
  - micro-eye-schmidt2006-pmc
  - micro-eye-mittelmeier2011-pmc
  - micro-eye-awasthi2016-pmc
  - micro-eye-ueki2016-pmc
  - micro-fer-go
  - micro-fer-tax573370
  - micro-fer-grant2022-meta
  - micro-fer-byrne2010-meta
  - micro-fer-grant2022-s3
  - micro-fer-C4XH20
  - micro-fer-C4XH21
  - micro-fer-C4XH22
  - micro-fer-IPR027256
  - micro-byrne-canonical
  - micro-eye-Q93WP2
  - micro-yeoh-pdf
  - micro-blackman1998-pdf
  - septin-review-policy
  - septin-curation-policy
  - septin-graph-policy
  - septin-go
  - septin-lumen-is-a-ancestors
  - septin-tax4932
  - septin-tax44689
  - septin-SL-0108
  - septin-SL-0109
  - septin-SL-0328
  - septin-barlowe1994-meta
  - septin-matsuoka1998-meta
  - septin-bomblies1990-meta
  - septin-bomblies-jats
  - septin-bomblies-pmc
  - septin-protein-P21837
  - septin-protein-P18142
- check_id: historical-adapter-runner
  name: Retained historical adapter runner availability
  status: unavailable
  required: false
  target_ids:
  - GO:0031904
  - GO:0010008
  - GO:7770040
  - GO:0012507
  - GO:0033117
  - GO:0034467
  - GO:0033118
  - GO:0044311
  - GO:1990413
  - cellstructuremech:ferrosome
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  summary: Historical 00:49Z invocation unavailable due to OS access restriction.
    Official catalogue source fallback was inspected separately; no current invocation
    or successful adapter execution is claimed. The actual historical exit code 1
    is retained in the evidence receipt, since the native unavailable-check model
    has no execution exit-code field.
  scope_note: Prior canary execution receipt reread and hash-verified during this
    follow-up. A non-required capability observation; repository policy explicitly
    permits source-page fallback.
  evidence_ids:
  - historical-adapter-runner-availability
- check_id: endosome_lumen-uniprot-verify
  name: Native endosome lumen UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0031904
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/endosome_lumen.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed molecular-node coverage are empty; narrative claims remain separately assessed.
  scope_note: Actual execution at the current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-endosome_lumen-verify
- check_id: endosome_lumen-uniprot-causal
  name: Native endosome lumen UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0031904
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/endosome_lumen.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed molecular-node coverage are empty; narrative claims remain separately assessed.
  scope_note: Actual execution at the current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-endosome_lumen-causal
- check_id: endosome_membrane-uniprot-verify
  name: Native endosome membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0010008
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/endosome_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. The Vps27 P40343 xref is verified;
    one UNANCHORED_WITH_UNIPROT node is an allowed transient actor without component_ref,
    not a dangling component.
  scope_note: Actual execution at the current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-endosome_membrane-verify
- check_id: endosome_membrane-uniprot-causal
  name: Native endosome membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0010008
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/endosome_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. The Vps27 P40343 xref is verified;
    one UNANCHORED_WITH_UNIPROT node is an allowed transient actor without component_ref,
    not a dangling component.
  scope_note: Actual execution at the current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-endosome_membrane-causal
- check_id: epiplastidial_membrane-uniprot-verify
  name: Native epiplastidial membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:7770040
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/epiplastidial_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed molecular-node coverage are empty; narrative claims remain separately assessed.
  scope_note: Actual execution at the current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-epiplastidial_membrane-verify
- check_id: epiplastidial_membrane-uniprot-causal
  name: Native epiplastidial membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:7770040
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/epiplastidial_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed molecular-node coverage are empty; narrative claims remain separately assessed.
  scope_note: Actual execution at the current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-epiplastidial_membrane-causal
- check_id: er_to_golgi_transport_vesicle_membrane-uniprot-verify
  name: Native ER to Golgi transport vesicle membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0012507
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/er_to_golgi_transport_vesicle_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed molecular-node coverage are empty; named COPII narrative actors remain separately
    assessed.
  scope_note: Actual execution at the current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-er_to_golgi_transport_vesicle_membrane-verify
- check_id: er_to_golgi_transport_vesicle_membrane-uniprot-causal
  name: Native ER to Golgi transport vesicle membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0012507
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/er_to_golgi_transport_vesicle_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed molecular-node coverage are empty; named COPII narrative actors remain separately
    assessed.
  scope_note: Actual execution at the current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-er_to_golgi_transport_vesicle_membrane-causal
- check_id: esterosome-uniprot-verify
  name: Native esterosome UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0033117
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/esterosome.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Two reviewed Dictyostelium examples
    cryS/P21837 and D2/P18142 are represented and verified; one typed node is COVERED.
    Primary localization remains separate from identity checks.
  scope_note: Actual execution at the current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-esterosome-verify
- check_id: esterosome-uniprot-causal
  name: Native esterosome UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0033117
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/esterosome.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Two reviewed Dictyostelium examples
    cryS/P21837 and D2/P18142 are represented and verified; one typed node is COVERED.
    Primary localization remains separate from identity checks.
  scope_note: Actual execution at the current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-esterosome-causal
- check_id: esterosome_lumen-uniprot-verify
  name: Native esterosome lumen UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0034467
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/esterosome_lumen.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed molecular-node coverage are empty; lumenal cargo assertions remain separately
    assessed.
  scope_note: Actual execution at the current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-esterosome_lumen-verify
- check_id: esterosome_lumen-uniprot-causal
  name: Native esterosome lumen UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0034467
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/esterosome_lumen.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed molecular-node coverage are empty; lumenal cargo assertions remain separately
    assessed.
  scope_note: Actual execution at the current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-esterosome_lumen-causal
- check_id: esterosome_membrane-uniprot-verify
  name: Native esterosome membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0033118
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/esterosome_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed molecular-node coverage are empty; limited morphology/boundary claims remain
    separately assessed.
  scope_note: Actual execution at the current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-esterosome_membrane-verify
- check_id: esterosome_membrane-uniprot-causal
  name: Native esterosome membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0033118
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/esterosome_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed molecular-node coverage are empty; limited morphology/boundary claims remain
    separately assessed.
  scope_note: Actual execution at the current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-esterosome_membrane-causal
- check_id: exoneme-uniprot-verify
  name: Native exoneme UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0044311
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/exoneme.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Two reviewed component examples
    SUB1/O61142 and PMX/Q8IAS0 plus substrate xrefs Q9TY95/Q8I0U8 are verified. Three
    typed nodes comprise two COVERED and one UNANCHORED_WITH_UNIPROT substrate-cohort
    actor; this is not proof of all mechanism or assembly necessity.
  scope_note: Actual execution at the current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-exoneme-verify
- check_id: exoneme-uniprot-causal
  name: Native exoneme UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0044311
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/exoneme.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Two reviewed component examples
    SUB1/O61142 and PMX/Q8IAS0 plus substrate xrefs Q9TY95/Q8I0U8 are verified. Three
    typed nodes comprise two COVERED and one UNANCHORED_WITH_UNIPROT substrate-cohort
    actor; this is not proof of all mechanism or assembly necessity.
  scope_note: Actual execution at the current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-exoneme-causal
- check_id: eyespot_apparatus-uniprot-verify
  name: Native eyespot apparatus UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:1990413
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/eyespot_apparatus.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Two unreviewed Chlamydomonas examples
    Q8RUT8/cop4 and Q93WP2/acop1 are verified; one typed node is COVERED. The primary
    nomenclature bridge and membership scope are assessed separately.
  scope_note: Actual execution at the current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-eyespot_apparatus-verify
- check_id: eyespot_apparatus-uniprot-causal
  name: Native eyespot apparatus UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:1990413
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/eyespot_apparatus.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Two unreviewed Chlamydomonas examples
    Q8RUT8/cop4 and Q93WP2/acop1 are verified; one typed node is COVERED. The primary
    nomenclature bridge and membership scope are assessed separately.
  scope_note: Actual execution at the current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-eyespot_apparatus-causal
- check_id: ferrosome-uniprot-verify
  name: Native ferrosome UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:ferrosome
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/ferrosome.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Three unreviewed RS-1 DMR/Fez examples
    C4XH20, C4XH21 and C4XH22 are verified; one typed node is COVERED. Identity checks
    do not establish individual necessity or a universal fitness phenotype.
  scope_note: Actual execution at the current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-ferrosome-verify
- check_id: ferrosome-uniprot-causal
  name: Native ferrosome UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:ferrosome
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/ferrosome.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Three unreviewed RS-1 DMR/Fez examples
    C4XH20, C4XH21 and C4XH22 are verified; one typed node is COVERED. Identity checks
    do not establish individual necessity or a universal fitness phenotype.
  scope_note: Actual execution at the current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-ferrosome-causal
evidence:
- evidence_id: current-record-0
  kind: record_content
  reference: data/structures/membrane_organelle/endosome_lumen.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T13:48:37Z'
  support: context_only
  summary: Original frozen SHA256 7522ffb363729241f2263bef6ebf96cb135a807c677df546e0b4ae92fe2bc604;
    current SHA256 7522ffb363729241f2263bef6ebf96cb135a807c677df546e0b4ae92fe2bc604.
    Record bytes unchanged since the original review.
  snapshot_sha256: 7522ffb363729241f2263bef6ebf96cb135a807c677df546e0b4ae92fe2bc604
- evidence_id: original-review-0
  kind: prior_review
  reference: reviews/structured/20261022T013714Z-endosome-lumen-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T13:48:37Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: f2bb53780f7d9b4bd704c73ba0222870690642380c53af8f72cff8a321ad40be
- evidence_id: current-record-1
  kind: record_content
  reference: data/structures/membrane_organelle/endosome_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T13:48:37Z'
  support: context_only
  summary: Original frozen SHA256 564b0ecf02448e0dab2210a213597b20b57ebfe09bf7637dfe2bed79a1b95270;
    current SHA256 564b0ecf02448e0dab2210a213597b20b57ebfe09bf7637dfe2bed79a1b95270.
    Record bytes unchanged since the original review.
  snapshot_sha256: 564b0ecf02448e0dab2210a213597b20b57ebfe09bf7637dfe2bed79a1b95270
- evidence_id: original-review-1
  kind: prior_review
  reference: reviews/structured/20261022T013715Z-endosome-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T13:48:37Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 7f72a4c56dfdf4ee7290a35ac5ec24a16649276574282b7fcf2bd8cafad48105
- evidence_id: current-record-2
  kind: record_content
  reference: data/structures/membrane_organelle/epiplastidial_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T13:48:37Z'
  support: context_only
  summary: Original frozen SHA256 15876d75b2efb4115edcf9f6ffa44a5254fcf104c9f543d7eb07b78a5f06db8a;
    current SHA256 15876d75b2efb4115edcf9f6ffa44a5254fcf104c9f543d7eb07b78a5f06db8a.
    Record bytes unchanged since the original review.
  snapshot_sha256: 15876d75b2efb4115edcf9f6ffa44a5254fcf104c9f543d7eb07b78a5f06db8a
- evidence_id: original-review-2
  kind: prior_review
  reference: reviews/structured/20261022T013716Z-epiplastidial-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T13:48:37Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: d1140ae276b9314ea234477f7dcb262ffe6d057c9b15d1b3fbfd31cd4af2535b
- evidence_id: current-record-3
  kind: record_content
  reference: data/structures/membrane_organelle/er_to_golgi_transport_vesicle_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T13:48:37Z'
  support: context_only
  summary: Original frozen SHA256 5cdd951707eead318295ce7ceb64c16bdc0c85b465374678d564878481f04a9c;
    current SHA256 5cdd951707eead318295ce7ceb64c16bdc0c85b465374678d564878481f04a9c.
    Record bytes unchanged since the original review.
  snapshot_sha256: 5cdd951707eead318295ce7ceb64c16bdc0c85b465374678d564878481f04a9c
- evidence_id: original-review-3
  kind: prior_review
  reference: reviews/structured/20261022T013717Z-er-to-golgi-transport-vesicle-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T13:48:37Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 443302a78569d841b938a4a245ed64efbb78f00364a5a238e5e99889992ccac5
- evidence_id: current-record-4
  kind: record_content
  reference: data/structures/membrane_organelle/esterosome.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T13:48:37Z'
  support: context_only
  summary: Original frozen SHA256 c5779634687c3e16478f4782e24897bc8df7939f14eddfd26ec4715c6de3c95a;
    current SHA256 c5779634687c3e16478f4782e24897bc8df7939f14eddfd26ec4715c6de3c95a.
    Record bytes unchanged since the original review.
  snapshot_sha256: c5779634687c3e16478f4782e24897bc8df7939f14eddfd26ec4715c6de3c95a
- evidence_id: original-review-4
  kind: prior_review
  reference: reviews/structured/20261022T013717Z-esterosome-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T13:48:37Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 3771f361702237469102a561833617eb0a3e6b5bb070204d184e8311067b20e9
- evidence_id: current-record-5
  kind: record_content
  reference: data/structures/membrane_organelle/esterosome_lumen.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T13:48:37Z'
  support: context_only
  summary: Original frozen SHA256 6891a8c551bc57b8ab1ce07357d050e40b46303debc2de0b81132b54424b53a4;
    current SHA256 6891a8c551bc57b8ab1ce07357d050e40b46303debc2de0b81132b54424b53a4.
    Record bytes unchanged since the original review.
  snapshot_sha256: 6891a8c551bc57b8ab1ce07357d050e40b46303debc2de0b81132b54424b53a4
- evidence_id: original-review-5
  kind: prior_review
  reference: reviews/structured/20261022T013718Z-esterosome-lumen-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T13:48:37Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 95bb137bbc197c2b8e26c6b030050aa97f3dd20d330b6be25c6c8ec5a37345cc
- evidence_id: current-record-6
  kind: record_content
  reference: data/structures/membrane_organelle/esterosome_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T13:48:37Z'
  support: context_only
  summary: Original frozen SHA256 b29aff5dceea8ed56348277d76f1c3658da2f304baa1b8e9858bf64cea5f4e5a;
    current SHA256 b29aff5dceea8ed56348277d76f1c3658da2f304baa1b8e9858bf64cea5f4e5a.
    Record bytes unchanged since the original review.
  snapshot_sha256: b29aff5dceea8ed56348277d76f1c3658da2f304baa1b8e9858bf64cea5f4e5a
- evidence_id: original-review-6
  kind: prior_review
  reference: reviews/structured/20261022T013719Z-esterosome-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T13:48:37Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 5caf336f1791fa5d7564ce6e976de292b62a9853d3f9728a37c9e665aa59e3d8
- evidence_id: current-record-7
  kind: record_content
  reference: data/structures/membrane_organelle/exoneme.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T13:48:37Z'
  support: context_only
  summary: Original frozen SHA256 2e32d7ca2f38ab39d5e1eb57cf683833fed5fdf18337191a3302689058d3b4b4;
    current SHA256 2e32d7ca2f38ab39d5e1eb57cf683833fed5fdf18337191a3302689058d3b4b4.
    Record bytes unchanged since the original review.
  snapshot_sha256: 2e32d7ca2f38ab39d5e1eb57cf683833fed5fdf18337191a3302689058d3b4b4
- evidence_id: original-review-7
  kind: prior_review
  reference: reviews/structured/20261022T013720Z-exoneme-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T13:48:37Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: a8b4a809b8586315722ef09a34b458810a8f50d52a64fc026202f245a428cca5
- evidence_id: current-record-8
  kind: record_content
  reference: data/structures/membrane_organelle/eyespot_apparatus.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T13:48:37Z'
  support: context_only
  summary: Original frozen SHA256 726e6433186bbdaf4cb318269e7369e07bd49d4b9d464590f0740ac5e156f36a;
    current SHA256 46c34aa696b5a0672d295e04dd475009d79c5c51b22aebe5afd541ccb97bc248.
    Changed record reassessed against current sources.
  snapshot_sha256: 46c34aa696b5a0672d295e04dd475009d79c5c51b22aebe5afd541ccb97bc248
- evidence_id: original-review-8
  kind: prior_review
  reference: reviews/structured/20261022T013720Z-eyespot-apparatus-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T13:48:37Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 30a96b63dbe341e4e627fee1d7f5c680ae5f9ec2640d854df3e9b1d375e8628d
- evidence_id: current-record-9
  kind: record_content
  reference: data/structures/membrane_organelle/ferrosome.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T13:48:37Z'
  support: context_only
  summary: Original frozen SHA256 a8350e9f852acd4d6cb753caba52b5f70ba3002f73f48e083ac047d0db405a6f;
    current SHA256 a8350e9f852acd4d6cb753caba52b5f70ba3002f73f48e083ac047d0db405a6f.
    Record bytes unchanged since the original review.
  snapshot_sha256: a8350e9f852acd4d6cb753caba52b5f70ba3002f73f48e083ac047d0db405a6f
- evidence_id: original-review-9
  kind: prior_review
  reference: reviews/structured/20261022T013721Z-ferrosome-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T13:48:37Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 6f0bbcd05a43e646ee0d4c07947151af79bee44a44eaa6185fe85b89e46149fc
- evidence_id: plaque-current-0
  kind: record_content
  reference: data/structures/membrane_organelle/endosome_lumen.yaml
  locator: Entire maintained record at source 5c140efd0be92d341410aa3024d677d5daf8bc1e;
    all fields, histories, discussions and graphs
  summary: Entire current target independently read. Hash unchanged from original
    frozen target; PROPOSED unchanged. No scientific record curation performed.
  accessed_at: '2026-11-03T13:43:12.293571Z'
  support: supports
  snapshot_sha256: 7522ffb363729241f2263bef6ebf96cb135a807c677df546e0b4ae92fe2bc604
- evidence_id: plaque-original-0
  kind: prior_review
  reference: reviews/structured/20261022T013714Z-endosome-lumen-audit/review.yaml
  locator: Exact staleness-listed original authoritative YAML/Markdown, input hashes,
    checks, assessments, findings/actions and limitations
  summary: Original pair validates and renders byte-exactly; all 18 historical frozen
    input hashes match. Scientific verdict independently reassessed; no other similarly
    named review is used.
  accessed_at: '2026-11-03T13:43:12.293571Z'
  support: supports
  snapshot_sha256: f2bb53780f7d9b4bd704c73ba0222870690642380c53af8f72cff8a321ad40be
- evidence_id: plaque-current-1
  kind: record_content
  reference: data/structures/membrane_organelle/endosome_membrane.yaml
  locator: Entire maintained record at source 5c140efd0be92d341410aa3024d677d5daf8bc1e;
    all fields, histories, discussions and graphs
  summary: Entire current target independently read. Hash unchanged from original
    frozen target; PROPOSED unchanged. No scientific record curation performed.
  accessed_at: '2026-11-03T13:43:12.293571Z'
  support: supports
  snapshot_sha256: 564b0ecf02448e0dab2210a213597b20b57ebfe09bf7637dfe2bed79a1b95270
- evidence_id: plaque-original-1
  kind: prior_review
  reference: reviews/structured/20261022T013715Z-endosome-membrane-audit/review.yaml
  locator: Exact staleness-listed original authoritative YAML/Markdown, input hashes,
    checks, assessments, findings/actions and limitations
  summary: Original pair validates and renders byte-exactly; all 17 historical frozen
    input hashes match. Scientific verdict independently reassessed; no other similarly
    named review is used.
  accessed_at: '2026-11-03T13:43:12.293571Z'
  support: supports
  snapshot_sha256: 7f72a4c56dfdf4ee7290a35ac5ec24a16649276574282b7fcf2bd8cafad48105
- evidence_id: plaque-current-2
  kind: record_content
  reference: data/structures/membrane_organelle/epiplastidial_membrane.yaml
  locator: Entire maintained record at source 5c140efd0be92d341410aa3024d677d5daf8bc1e;
    all fields, histories, discussions and graphs
  summary: Entire current target independently read. Hash unchanged from original
    frozen target; PROPOSED unchanged. No scientific record curation performed.
  accessed_at: '2026-11-03T13:43:12.293571Z'
  support: supports
  snapshot_sha256: 15876d75b2efb4115edcf9f6ffa44a5254fcf104c9f543d7eb07b78a5f06db8a
- evidence_id: plaque-original-2
  kind: prior_review
  reference: reviews/structured/20261022T013716Z-epiplastidial-membrane-audit/review.yaml
  locator: Exact staleness-listed original authoritative YAML/Markdown, input hashes,
    checks, assessments, findings/actions and limitations
  summary: Original pair validates and renders byte-exactly; all 14 historical frozen
    input hashes match. Scientific verdict independently reassessed; no other similarly
    named review is used.
  accessed_at: '2026-11-03T13:43:12.293571Z'
  support: supports
  snapshot_sha256: d1140ae276b9314ea234477f7dcb262ffe6d057c9b15d1b3fbfd31cd4af2535b
- evidence_id: plaque-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Frozen native contract and relevant definitions
  summary: Named genes/proteins/regulators/pathways/stress responses/traits trigger
    structured-source assessment. Empty accession inventories do not waive narrative
    pathway claims.
  accessed_at: '2026-11-03T13:43:12.293571Z'
  support: context_only
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: plaque-rubric
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Frozen native contract and relevant definitions
  summary: Exact identity, source scope, grounding, taxonomy and necessity must be
    assessed; missing optional inventories alone are not findings.
  accessed_at: '2026-11-03T13:43:12.293571Z'
  support: context_only
  snapshot_sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
- evidence_id: plaque-graph-rubric
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Frozen native contract and relevant definitions
  summary: Mechanistic claims require inspected primary support; descriptive identity/topology
    alone is not a molecular causal sequence.
  accessed_at: '2026-11-03T13:43:12.293571Z'
  support: context_only
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: plaque-protein-contract
  kind: authority
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Frozen native contract and relevant definitions
  summary: External protein actors may carry verified causal-node xrefs rather than
    invented constituent component rows.
  accessed_at: '2026-11-03T13:43:12.293571Z'
  support: context_only
  snapshot_sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
- evidence_id: plaque-schema-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Frozen native contract and relevant definitions
  summary: Whole compartment, subcellular lumen, membrane and generic collective lipid
    material retain their distinct granularity.
  accessed_at: '2026-11-03T13:43:12.293571Z'
  support: context_only
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: plaque-neighbor-mvb-lumen
  kind: record_content
  reference: data/structures/membrane_organelle/multivesicular_body_lumen.yaml
  locator: Entire frozen neighbor read for identity/boundary context only
  summary: Local MVB lumen is a specialized endosome lumen, distinct from its enclosing
    membrane and whole MVB. No independent review of unrelated neighbor claims or
    terminal historical disposition.
  accessed_at: '2026-11-03T13:43:12.293571Z'
  support: context_only
  snapshot_sha256: 6c67050e4fa82c1a03f0476a13be57741651c0ad9e1d4bfa241ca500525175f6
- evidence_id: plaque-neighbor-ilv
  kind: record_content
  reference: data/structures/membrane_organelle/multivesicular_body_intraluminal_vesicle.yaml
  locator: Entire frozen neighbor read for identity/boundary context only
  summary: Local intraluminal vesicle denotes a whole vesicle inside an MVB; it is
    distinct from MVB lumen and limiting membrane. No independent review of unrelated
    neighbor claims or terminal historical disposition.
  accessed_at: '2026-11-03T13:43:12.293571Z'
  support: context_only
  snapshot_sha256: 47e5f39198c321eb8e1df58ff20ac1a0a50ec731170ae0f9d07d22b299594916
- evidence_id: plaque-neighbor-ppm
  kind: record_content
  reference: data/structures/membrane_organelle/periplastidial_membrane.yaml
  locator: Entire frozen neighbor read for identity/boundary context only
  summary: PPM is the second outermost complex-plastid membrane, distinct from outermost
    EpM and plastid oEM. No independent review of unrelated neighbor claims or terminal
    historical disposition.
  accessed_at: '2026-11-03T13:43:12.293571Z'
  support: context_only
  snapshot_sha256: 96374ff1877ac9701ca4104ebc8e7218aee2345b6d2170b35cf64e6c30f6188a
- evidence_id: plaque-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031904,GO:0070013,GO:0005768,GO:0010008,GO:0005771,GO:0071985,GO:0016020,GO:0000813,GO:0000815,GO:7770040,GO:7770041,GO:0042170,GO:0009536,GO:0009527
  locator: All14 exact active term names/definitions/synonyms and relevant typed children;
    complete returned JSON
  summary: Exact endosome lumen0031904 and membrane0010008 match target definitions;
    lumen is_a0070013 and both part_of0005768. MVB0005771 denotes an endosome with
    invaginated internal vesicles.0071985 describes MVB cargo sorting;0000813/0000815
    identify ESCRT complexes, with modern III definition describing scission.7770040
    matches full EpM definition and five synonyms;0042170 lists it is_a, and plastid0009536
    lists plastid membrane part_of.7770041 puts PPC between PPM and outer plastid
    envelope0009527. Authority text is not a new experiment or universal strain-specific
    mechanism.
  accessed_at: '2026-11-03T13:39:48.527866Z'
  support: supports
  snapshot_sha256: 060b6757157da6eb1c4791ae61f18c0976708ef6804cdce30fc4ae5e05272d84
- evidence_id: plaque-tax4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete native taxId/scientificName/rank/lineage
  summary: Species4932 is Saccharomyces cerevisiae. Native taxon identity is not an
    empirical prevalence or culture-collection strain assignment.
  accessed_at: '2026-11-03T13:39:48.528089Z'
  support: supports
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
- evidence_id: plaque-tax559292
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete native taxId/scientificName/rank/lineage
  summary: Strain559292 is S. cerevisiae S288C; this does not relabel SEY6210-derived
    experiments. Native taxon identity is not an empirical prevalence or culture-collection
    strain assignment.
  accessed_at: '2026-11-03T13:39:48.536549Z'
  support: supports
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: plaque-tax2850
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2850
  locator: Complete native taxId/scientificName/rank/lineage
  summary: Species2850 is Phaeodactylum tricornutum, a diatom. Native taxon identity
    is not an empirical prevalence or culture-collection strain assignment.
  accessed_at: '2026-11-03T13:39:49.168425Z'
  support: supports
  snapshot_sha256: b6d69eacb3d411eba55cf0cc28d869546514e6d8f84d90a0368382c63fa324d1
- evidence_id: plaque-sl0340
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0340.json
  locator: Top-level identity/definition/synonyms and isA Endosome lumen SL0327/GO0031904,
    partOf MVB SL0174/GO0005771
  summary: MVB lumen is explicitly the compartment bounded by the MVB membrane and
    a subtype of endosome lumen. This validates local boundary/specialization context
    without treating ILVs as mandatory in every endosome.
  accessed_at: '2026-11-03T13:39:48.528281Z'
  support: supports
  snapshot_sha256: 8e50a2ed2c762cf87ee99c3fdc6742225f4e9669f81b50640f776066000860ad
- evidence_id: plaque-protein-P40343
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P40343.json
  locator: Primary accession, reviewed entry type, genes/protein names/organism and
    FUNCTION/SUBCELLULAR LOCATION comments with linked evidence
  summary: Reviewed P40343 is VPS27/YNR006W, vacuolar protein sorting-associated protein27,
    in S288C559292. Annotation identifies ESCRT-0 actor recruiting ESCRT-I to endosomal
    membranes and links PMID12900393. It supports exact graph xref identity; primary
    experiments and strain scope are assessed separately.
  accessed_at: '2026-11-03T13:39:49.140515Z'
  support: supports
  snapshot_sha256: 9722b86a9641dd5d053f0babc34f530ea7656e19571069c2eb081537e836c344
- evidence_id: plaque-katzmann2001-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A11511343%20AND%20SRC%3AMED
  locator: Exact EuropePMC native core bibliographic entry and complete abstract;
    body tier explicitly separate
  summary: Katzmann/Babst/Emr2001 PMID11511343 DOI10.1016/s0092-8674(01)00434-2. Complete
    abstract identifies yeast ESCRT-I and ubiquitin-dependent cargo sorting into MVB
    vesicles; no full body or figure inspection.
  accessed_at: '2026-11-03T13:39:48.528151Z'
  support: supports
  snapshot_sha256: 7db9305a7cf288c30baa004d8fc4361b4e058b80a743d22f94264009ff9cf609
- evidence_id: plaque-katzmann2003-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1083/jcb.200302136
  locator: Exact EuropePMC native core bibliographic entry and complete abstract;
    body tier explicitly separate
  summary: Katzmann/Stefan/Babst/Emr2003 PMID12900393 DOI10.1083/jcb.200302136; exact
    article identity and abstract support Vps27-dependent ESCRT-I recruitment; body
    inspected separately.
  accessed_at: '2026-11-03T13:39:48.530267Z'
  support: supports
  snapshot_sha256: 563c8c33c8918c5c041e9a2566de99fd4fac9e291d54af2e82f4cdb3732bfe4a
- evidence_id: plaque-babst2002-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A12194857%20AND%20SRC%3AMED
  locator: Exact EuropePMC native core bibliographic entry and complete abstract;
    body tier explicitly separate
  summary: Babst et al.2002 PMID12194857 DOI10.1016/s1534-5807(02)00220-4. Complete
    abstract supports cytoplasmic ESCRT-III recruitment, membrane oligomerization,
    subcomplex association and cargo sorting/concentration. It does not independently
    establish precise scission chemistry; no full body read.
  accessed_at: '2026-11-03T13:39:48.536332Z'
  support: supports
  snapshot_sha256: 154c66e5c81005bcb646718e07a114e6c610e20c4a80803a5505061f4c107317
- evidence_id: plaque-henne2011-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.devcel.2011.05.015
  locator: Exact EuropePMC native core bibliographic entry and complete abstract;
    body tier explicitly separate
  summary: Henne/Buchkovich/Emr2011 PMID21763610 DOI10.1016/j.devcel.2011.05.015 is
    explicitly a review. Complete abstract describes ESCRT cargo recognition and membrane
    sculpting; secondary context, not a primary intervention or full-body inspection.
  accessed_at: '2026-11-03T13:39:48.528231Z'
  support: supports
  snapshot_sha256: 53f8c38ed00fbf480d0102c7025f98bda9b1750dc9731738bae41a1e4daaf611
- evidence_id: plaque-flori2016-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.protis.2016.04.001
  locator: Exact EuropePMC native core bibliographic entry and complete abstract;
    body tier explicitly separate
  summary: Flori/Jouneau/Finazzi/Marechal/Falconet2016 PMID27179349 DOI10.1016/j.protis.2016.04.001,
    Ultrastructure of the Periplastidial Compartment of the Diatom Phaeodactylum tricornutum.
    Primary FIB-SEM identity/abstract; detailed boundary claims assessed in PDF.
  accessed_at: '2026-11-03T13:39:49.168494Z'
  support: supports
  snapshot_sha256: b0d1f3a82b3c7ccfe807918a0ab4820af2bf8959d77c2b961b466fccc8b37a51
- evidence_id: plaque-gueguen2024-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1093/plcell/koae275
  locator: Exact EuropePMC native core bibliographic entry and complete abstract;
    body tier explicitly separate
  summary: Gueguen et al.2024 PMID39383259 DOI10.1093/plcell/koae275, Monogalactosyldiacylglycerol
    synthase isoforms play diverse roles inside and outside the diatom plastid. Primary
    identity/abstract; detailed scope assessed in JATS.
  accessed_at: '2026-11-03T13:39:49.171228Z'
  support: supports
  snapshot_sha256: b08f31cdb1c1f54505f232ad176837466d659b8b2603e746b6b8d064a98dd354
- evidence_id: plaque-hashimoto2005-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1007/s10265-005-0214-6
  locator: Exact EuropePMC native core bibliographic entry and complete abstract;
    body tier explicitly separate
  summary: Hashimoto2005 PMID15937721 DOI10.1007/s10265-005-0214-6 is a review. Complete
    abstract distinguishes secondary-plastid lineages and ER/outer-nuclear continuity
    in heterokonts/cryptophytes/haptophytes. Secondary abstract-only context; no primary
    experimental or full-body claim.
  accessed_at: '2026-11-03T13:39:49.193288Z'
  support: supports
  snapshot_sha256: 53585862732582c8319845c15dd54898911c31ef4f9baa8018b548b791b049b8
- evidence_id: plaque-katzmann2003-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2172707/
  locator: Genuine primary PMC HTML complete Resultssec5/sec6 and Methodssec12; Figure3/4
    captions as text; no figure pixels or raw-data reanalysis
  summary: Vps23-GFP redistribution in vps27 deletion and reciprocal localization,
    plus membrane-fraction copurification, support Vps27-dependent ESCRT-I recruitment/association
    on yeast endosomes. Methods list SEY6210-derived strains. Reference S288C UniProt
    identity is not substituted for study strain. These experiments support the narrow
    canonical example, not every ESCRT step or obligatory constituents of all endosome
    membranes.
  accessed_at: '2026-11-03T13:39:49.164129Z'
  support: supports
  snapshot_sha256: dd950faeb5738bc5819452db307891303223640a8d47a1d938976b6bde66c034
- evidence_id: plaque-flori2016-oceanomics-pdf
  kind: primary_source
  reference: https://www.oceanomics.eu/sites/default/files/documents/oceanomics-flori-et-al-protist-2016-484.pdf
  locator: Published PDF p255 text and Fig1 caption/pixels; Results opening p256 and
    full p261; Discussion/Methods pp263–264 and associated Fig5/6 caption text. Other
    figure pixels, supplements and raw measurements not audited
  summary: Primary P. tricornutum Pt1 CCAP1055/3 study distinguishes outer cERM/EpM
    continuous with outer nuclear envelope, PPM beneath it and PPC between PPM/oEM.
    Fig1 pixels show an intervening cERM–PPM space, not PPC immediately inside EpM.
    FIB-SEM compares disrupted cells and intact cells. Authors mark molecular machinery/lipid
    compositions unresolved and evolutionary alternatives as hypotheses. Indirect
    outer enclosure is valid; immediate-interface wording remains ambiguous.
  accessed_at: '2026-11-03T13:39:49.196858Z'
  support: supports
  snapshot_sha256: e2ca79ebda9c385dfc7a1a99b7b9e0227f615d4b4127b36efb616fc97170bf35
- evidence_id: plaque-gueguen2024-jats
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11638560/fullTextXML
  locator: Introductionkoae275-s1 with Fig1 caption; Resultss2.4 with Fig2/3 captions;
    Discussions3.2/s3.8; Methodss4.4/s4.13; no figure-pixel, supplement or other-section
    audit
  summary: P. tricornutum Pt1 Strain8.6 CCAP1055/1 study preserves EpM/PPM/oEM/iEM
    boundaries. MGDgamma-GFP fluorescence in ER/plastid periphery supports qualified
    possible EpM localization, while exact extraplastidial lipid pools/functions remain
    uncertain. Source-localization information is not a record assertion of exact
    lipid mixture or formation necessity. Evolutionary membrane-origin alternatives
    remain explicit in source.
  accessed_at: '2026-11-03T13:39:49.204958Z'
  support: supports
  snapshot_sha256: 0078d6a856bbf8cc5b6769112284c598a161cacf7a7508cfba3e18bac1f14ed0
- evidence_id: plaque-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete fresh official /api/datasets response; every organism/dataset
    row read, no pagination
  summary: Returned catalogue has no Saccharomyces cerevisiae or Phaeodactylum tricornutum
    host match. ESCRT/MVB pathway and VPS27 claims trigger assessment but no matched
    downstream gene/module query applies. Bacterial/archaeal datasets are not proxies
    for these eukaryotic hosts. Noncoverage is not biological absence; no generated
    module prose is used.
  accessed_at: '2026-11-03T13:39:49.513570Z'
  support: supports
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: plaque-historical-runner
  kind: validation
  reference: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  locator: Historical00:49Z receipt with stdout/stderr reread and hashes verified
  summary: Historical runner failed before dataset retrieval with PermissionError
    reading pyvenv.cfg. No current invocation or success claimed; fresh official catalogue
    and scoped primary/authority sources are the permitted fallback.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: plaque-original-checks
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/adversary-plaque/original-checks.json
  locator: All three original native validation/render results and historical-source
    input hashes
  summary: Three original pairs validate/render exactly; historical input counts18/17/14
    all match. All three target hashes unchanged. EpM two scientific findings remain
    independently confirmed.
  accessed_at: '2026-11-03T13:39:43.313835Z'
  support: supports
  snapshot_sha256: 6fd1ea217723224805c84a85eff602998787ccdaac8afb6bb530bca98ab69c76
- evidence_id: plaque-native-endosome_lumen-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/endosome_lumen.yaml
    --verify
  locator: Root-owned actual command receipt/stdout independently read and hash-verified
  summary: 'all UniProtKB protein_examples and causal_graphs xrefs verified ok Scope:
    No component protein_examples and zero GENE_OR_PROTEIN nodes in the complete current
    target; mechanical checks are empty-inventory scope.'
  accessed_at: '2026-11-03T13:38:19.102513Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-endosome_lumen-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/endosome_lumen.yaml
    --causal-graphs
  locator: Root-owned actual command receipt/stdout independently read and hash-verified
  summary: "causal_graphs GENE_OR_PROTEIN node summary:\n     0  COVERED         \
    \          component_ref target holds protein_examples covering all declared symbols\n\
    \     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     0\
    \  total GENE_OR_PROTEIN causal nodes Scope: No component protein_examples and\
    \ zero GENE_OR_PROTEIN nodes in the complete current target; mechanical checks\
    \ are empty-inventory scope."
  accessed_at: '2026-11-03T13:38:19.542747Z'
  support: supports
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: plaque-native-endosome_membrane-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/endosome_membrane.yaml
    --verify
  locator: Root-owned actual command receipt/stdout independently read and hash-verified
  summary: 'all UniProtKB protein_examples and causal_graphs xrefs verified ok Scope:
    No component protein_examples; one GENE_OR_PROTEIN node is UNANCHORED_WITH_UNIPROT,
    carrying verified P40343 for external Vps27. This is permitted and does not require
    a fabricated component.'
  accessed_at: '2026-11-03T13:38:20.569373Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-endosome_membrane-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/endosome_membrane.yaml
    --causal-graphs
  locator: Root-owned actual command receipt/stdout independently read and hash-verified
  summary: "data/structures/membrane_organelle/endosome_membrane.yaml  (GO:0010008)\n\
    \  endosome_membrane_mvb_sorting\tvps27_endosomal_recruiter\tUNANCHORED_WITH_UNIPROT\t\
    Vps27 endosomal ESCRT-I recruiter (UniProtKB:P40343)\n\ncausal_graphs GENE_OR_PROTEIN\
    \ node summary:\n     1  UNANCHORED_WITH_UNIPROT   no component_ref, but node\
    \ carries a UniProtKB grounding or xref\n     0  COVERED                   component_ref\
    \ target holds protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES\
    \          component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or\
    \ xref on the node\n     1  total GENE_OR_PROTEIN causal nodes Scope: No component\
    \ protein_examples; one GENE_OR_PROTEIN node is UNANCHORED_WITH_UNIPROT, carrying\
    \ verified P40343 for external Vps27. This is permitted and does not require a\
    \ fabricated component."
  accessed_at: '2026-11-03T13:38:21.002036Z'
  support: supports
  snapshot_sha256: 60d9577c6bd0ff53005e8d24b45f7e18b9e281ee0d37fa082241f0743244897d
- evidence_id: plaque-native-epiplastidial_membrane-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/epiplastidial_membrane.yaml
    --verify
  locator: Root-owned actual command receipt/stdout independently read and hash-verified
  summary: 'all UniProtKB protein_examples and causal_graphs xrefs verified ok Scope:
    No component protein_examples and zero GENE_OR_PROTEIN nodes in the complete current
    target; mechanical checks are empty-inventory scope.'
  accessed_at: '2026-11-03T13:38:21.431637Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-epiplastidial_membrane-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/epiplastidial_membrane.yaml
    --causal-graphs
  locator: Root-owned actual command receipt/stdout independently read and hash-verified
  summary: "causal_graphs GENE_OR_PROTEIN node summary:\n     0  COVERED         \
    \          component_ref target holds protein_examples covering all declared symbols\n\
    \     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     0\
    \  total GENE_OR_PROTEIN causal nodes Scope: No component protein_examples and\
    \ zero GENE_OR_PROTEIN nodes in the complete current target; mechanical checks\
    \ are empty-inventory scope."
  accessed_at: '2026-11-03T13:38:21.876714Z'
  support: supports
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: micro-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Current complete native review skill/profile/config and checklist reread;
    remaining frozen common contracts retained at identical hashes, exact scope in
    policy-hash-check.json
  accessed_at: '2026-11-03T13:43:24.002658Z'
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
  summary: Structure/protein/phenotype, membership/necessity and exact-family/domain
    scopes remain distinct. Named gene/locus/pathway claims trigger structured-source
    applicability even without an expression claim. All17 common instructions/schema/verifier
    inputs equal the preceding reviewed bytes.
  support: context_only
- evidence_id: micro-protein-contract
  kind: authority
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: 'Entire current skill reread: identity-only examples, exact native tokens,
    canonical taxa, reviewed/unreviewed status and allowed external-actor xrefs'
  accessed_at: '2026-11-03T13:43:24.002658Z'
  snapshot_sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
  summary: An alias may be bridged by actual literature while gene_symbol retains
    the native entry token. Unreviewed status is explicit. Verified external substrates
    need not be invented as stable organelle constituents.
  support: context_only
- evidence_id: micro-record-exoneme
  kind: record_content
  reference: data/structures/membrane_organelle/exoneme.yaml
  locator: 'Entire current maintained YAML: all fields, history, components/examples,
    taxonomy, functions, evidence, graph and discussions'
  accessed_at: '2026-11-03T13:43:24.002658Z'
  snapshot_sha256: 2e32d7ca2f38ab39d5e1eb57cf683833fed5fdf18337191a3302689058d3b4b4
  summary: Entire target independently read at 5c140efd0be92d341410aa3024d677d5daf8bc1e.
    Current bytes equal original frozen target.
  support: supports
- evidence_id: micro-prior-exoneme
  kind: prior_review
  reference: reviews/structured/20261022T013720Z-exoneme-audit/review.yaml
  locator: Original authoritative YAML plus paired deterministic Markdown; source
    hash, checks, all assessments/findings/actions/limitations
  accessed_at: '2026-11-03T13:43:24.002658Z'
  snapshot_sha256: a8b4a809b8586315722ef09a34b458810a8f50d52a64fc026202f245a428cca5
  summary: Original needs_curation; one inherited minor SUB1 family finding retains
    exact lineage. Existing expression-only adapter exclusion is reassessed; historical
    executions are not claimed current.
  support: context_only
- evidence_id: micro-native-exoneme-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/exoneme-uniprot-verify-receipt.json
  locator: Actual .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/exoneme.yaml
    --verify; complete stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/exoneme-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T13:38:27.413372Z'
  snapshot_sha256: 9afa0f0e9e07efe5fcf2c6c4b215ea9db28507503f9e198fe8dca90bd3179434
  summary: Actual source-head exit0. Two protein examples O61142/Q8IAS0 and two graph
    xrefs Q9TY95/Q8I0U8. Three typed nodes:2COVERED and1UNANCHORED_WITH_UNIPROT external
    SERA/MSP substrate cohort; the permitted external-actor route is not a dangling
    constituent.
  support: supports
- evidence_id: micro-native-exoneme-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/exoneme-uniprot-causal-receipt.json
  locator: Actual .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/exoneme.yaml
    --causal-graphs; complete stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/exoneme-uniprot-causal.log
    SHA256 511b80633418ceaf902b70422e104017ea024ac612753acc164a8ceed3612398
  accessed_at: '2026-11-03T13:38:27.849477Z'
  snapshot_sha256: e297612c2ab7f4d2b38d73c3a5dac584f9ec5ec007c96b8ad20bc989ec202270
  summary: Actual source-head exit0. Two protein examples O61142/Q8IAS0 and two graph
    xrefs Q9TY95/Q8I0U8. Three typed nodes:2COVERED and1UNANCHORED_WITH_UNIPROT external
    SERA/MSP substrate cohort; the permitted external-actor route is not a dangling
    constituent.
  support: supports
- evidence_id: micro-record-eyespot_apparatus
  kind: record_content
  reference: data/structures/membrane_organelle/eyespot_apparatus.yaml
  locator: 'Entire current maintained YAML: all fields, history, components/examples,
    taxonomy, functions, evidence, graph and discussions'
  accessed_at: '2026-11-03T13:43:24.002658Z'
  snapshot_sha256: 46c34aa696b5a0672d295e04dd475009d79c5c51b22aebe5afd541ccb97bc248
  summary: Entire target independently read at 5c140efd0be92d341410aa3024d677d5daf8bc1e.
    Stale eyespot adds Q93WP2/acop1 protein example and corresponding history; substantively
    reassessed below.
  support: supports
- evidence_id: micro-prior-eyespot_apparatus
  kind: prior_review
  reference: reviews/structured/20261022T013720Z-eyespot-apparatus-audit/review.yaml
  locator: Original authoritative YAML plus paired deterministic Markdown; source
    hash, checks, all assessments/findings/actions/limitations
  accessed_at: '2026-11-03T13:43:24.002658Z'
  snapshot_sha256: 30a96b63dbe341e4e627fee1d7f5c680ae5f9ec2640d854df3e9b1d375e8628d
  summary: Original pass_with_limitations; no original findings/actions. Existing
    expression-only adapter exclusion is reassessed; historical executions are not
    claimed current.
  support: context_only
- evidence_id: micro-native-eyespot_apparatus-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/eyespot_apparatus-uniprot-verify-receipt.json
  locator: Actual .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/eyespot_apparatus.yaml
    --verify; complete stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/eyespot_apparatus-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T13:38:29.070641Z'
  snapshot_sha256: 8005b71743f5624d3fa2c3ab748e94871e467defa01e499babe380e4ad69de9a
  summary: Actual source-head exit0. Two unreviewed examples Q8RUT8/Q93WP2 and one
    COVERED typed node. Native success does not prove apparatus membership or make
    the literal COP3 query return a result.
  support: supports
- evidence_id: micro-native-eyespot_apparatus-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/eyespot_apparatus-uniprot-causal-receipt.json
  locator: Actual .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/eyespot_apparatus.yaml
    --causal-graphs; complete stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/eyespot_apparatus-uniprot-causal.log
    SHA256 da5a05917d67e5d9fea5b655a99f994074cd657a4a40e6673c8e6d6bfb0bee5b
  accessed_at: '2026-11-03T13:38:29.509625Z'
  snapshot_sha256: a8751bcf1396d3abc0aea38e67e2406ac711556011c0ca075ea7de9ab1798dd1
  summary: Actual source-head exit0. Two unreviewed examples Q8RUT8/Q93WP2 and one
    COVERED typed node. Native success does not prove apparatus membership or make
    the literal COP3 query return a result.
  support: supports
- evidence_id: micro-record-ferrosome
  kind: record_content
  reference: data/structures/membrane_organelle/ferrosome.yaml
  locator: 'Entire current maintained YAML: all fields, history, components/examples,
    taxonomy, functions, evidence, graph and discussions'
  accessed_at: '2026-11-03T13:43:24.002658Z'
  snapshot_sha256: a8350e9f852acd4d6cb753caba52b5f70ba3002f73f48e083ac047d0db405a6f
  summary: Entire target independently read at 5c140efd0be92d341410aa3024d677d5daf8bc1e.
    Current bytes equal original frozen target.
  support: supports
- evidence_id: micro-prior-ferrosome
  kind: prior_review
  reference: reviews/structured/20261022T013721Z-ferrosome-audit/review.yaml
  locator: Original authoritative YAML plus paired deterministic Markdown; source
    hash, checks, all assessments/findings/actions/limitations
  accessed_at: '2026-11-03T13:43:24.002658Z'
  snapshot_sha256: 6f0bbcd05a43e646ee0d4c07947151af79bee44a44eaa6185fe85b89e46149fc
  summary: Original pass_with_limitations; no original findings/actions. Existing
    expression-only adapter exclusion is reassessed; historical executions are not
    claimed current.
  support: context_only
- evidence_id: micro-native-ferrosome-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/ferrosome-uniprot-verify-receipt.json
  locator: Actual .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/ferrosome.yaml
    --verify; complete stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/ferrosome-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T13:38:31.146405Z'
  snapshot_sha256: fcfa200c65141cc6a88d260eed4a7e21319012eac6a777fbd2c73e1718edad8c
  summary: Actual source-head exit0. Three unreviewed locus examples C4XH20/C4XH21/C4XH22
    and one COVERED typed Fez cohort node. Literature aliases and biological membership
    require separate primary evidence.
  support: supports
- evidence_id: micro-native-ferrosome-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/ferrosome-uniprot-causal-receipt.json
  locator: Actual .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/ferrosome.yaml
    --causal-graphs; complete stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/ferrosome-uniprot-causal.log
    SHA256 d45e581edff9b488306b1c92b87a02fcd2a425cd7d85646a32d55d964924c28b
  accessed_at: '2026-11-03T13:38:31.610984Z'
  snapshot_sha256: de4a2d74a46b0f12e8fbdb2d4bab1c4f72e66ad04eb179771993e252809d3ac5
  summary: Actual source-head exit0. Three unreviewed locus examples C4XH20/C4XH21/C4XH22
    and one COVERED typed Fez cohort node. Literature aliases and biological membership
    require separate primary evidence.
  support: supports
- evidence_id: micro-original-pairs
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/adversary-microtubule/original-validation.json
  locator: Three actual native validate and three render --content executions, all
    byte-equal; frozen historical record inputs checked through git show
  accessed_at: '2026-11-03T13:38:39.199504Z'
  snapshot_sha256: 69e948fb597b45fbdadab22d4f1e60930035c0351bd115af0692867501ab3301
  summary: All three retained bundles are schema-valid and Markdown equals renderer
    output. Historical target hashes match source f97b1abe; only eyespot differs from
    current record.
  support: supports
- evidence_id: micro-eyespot-delta
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/adversary-microtubule/eyespot-stale.diff
  locator: Exact original-frozen-source versus current-head diff for eyespot only
  accessed_at: '2026-11-03T13:43:24.002658Z'
  snapshot_sha256: 5136aaad48f6fed07339234dfcf96a4781e5f13cf1a123044f842a13054bdf05
  summary: Only new Q93WP2/acop1 example and October23 curation event; no graph/definition/other
    component changes.
  support: context_only
- evidence_id: micro-exo-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044311,GO:0043231,GO:0020007
  locator: All three exact identifiers, definitions, active flags and relevant child
    relations
  accessed_at: '2026-11-03T13:38:56.497740Z'
  snapshot_sha256: 0755406ae14f6287bd46e603298ec29a1dda850cb8aaee3f7251b9198b85cc33
  summary: Active GO0044311 matches the exoneme definition; GO0043231 lists it as
    an is_a child and GO0020007 lists it as part_of the apical complex.
  support: supports
- evidence_id: micro-exo-tax5833
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5833
  locator: Exact taxId, scientificName, rank, lineage and alternate names
  accessed_at: '2026-11-03T13:38:56.498086Z'
  snapshot_sha256: 47c9da135299ea0515b9cbddde80166e0e7256bcf1daac4cdf87f8ae3e0ecd11
  summary: ENA identifies tax5833 as Plasmodium falciparum, species.
  support: supports
- evidence_id: micro-exo-tax36329
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/36329
  locator: Exact taxId, scientificName, rank, lineage and alternate names
  accessed_at: '2026-11-03T13:38:56.498231Z'
  snapshot_sha256: 6d1389e6a3af3a09ef4bf23157b95ec8d94dac9b395b8f8ccf0d1952beddc306
  summary: ENA identifies tax36329 as Plasmodium falciparum3D7, isolate rank.
  support: supports
- evidence_id: micro-exo-yeoh2007-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.cell.2007.10.049
  locator: Exact Europe PMC DOI/PMID core lookup; complete MED bibliographic record
    and complete abstract only; full-body reading separately scoped
  accessed_at: '2026-11-03T13:38:56.498356Z'
  snapshot_sha256: 2dca392ec8fc4c79b9b6aad4415eb0fd226ea8c40d15159aa992a3ef96792da0
  summary: 'PMID18083098, DOI10.1016/j.cell.2007.10.049: Subcellular discharge of
    a serine protease mediates release of invasive malaria parasites from host erythrocytes.
    Complete abstract inspected; no full-body access implied by metadata.'
  support: supports
- evidence_id: micro-exo-blackman1998-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A9722575%20AND%20SRC%3AMED
  locator: Exact Europe PMC DOI/PMID core lookup; complete MED bibliographic record
    and complete abstract only; full-body reading separately scoped
  accessed_at: '2026-11-03T13:38:56.498478Z'
  snapshot_sha256: 7af93b27c231d3f3de663eab218765a5a8f728ac69842a3e262edd76a0cff066
  summary: 'PMID9722575, DOI10.1074/jbc.273.36.23398: A subtilisin-like protein in
    secretory organelles of Plasmodium falciparum merozoites. Complete abstract inspected;
    no full-body access implied by metadata.'
  support: supports
- evidence_id: micro-exo-blackman2008-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1111/j.1462-5822.2008.01176.x
  locator: Exact Europe PMC DOI/PMID core lookup; complete MED bibliographic record
    and complete abstract only; full-body reading separately scoped
  accessed_at: '2026-11-03T13:38:56.498637Z'
  snapshot_sha256: ee28ac5d67c61506bfb7bc47a5ef75e5b7abeb56a431524212f013760c00531e
  summary: 'PMID18503638, DOI10.1111/j.1462-5822.2008.01176.x: Malarial proteases
    and host cell egress: an ''emerging'' cascade. Complete abstract inspected; no
    full-body access implied by metadata.'
  support: context_only
- evidence_id: micro-exo-withers2014-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/ncomms4726
  locator: Exact Europe PMC DOI/PMID core lookup; complete MED bibliographic record
    and complete abstract only; full-body reading separately scoped
  accessed_at: '2026-11-03T13:38:57.117088Z'
  snapshot_sha256: 211dfd6bb92adff1ba446a93338a123f6f260fd8d0332959eac41d7ccac6160e
  summary: 'PMID24785947, DOI10.1038/ncomms4726: The malaria parasite egress protease
    SUB1 is a calcium-dependent redox switch subtilisin. Complete abstract inspected;
    no full-body access implied by metadata.'
  support: supports
- evidence_id: micro-exo-nasamu2017-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1126/science.aan1478
  locator: Exact Europe PMC DOI/PMID core lookup; complete MED bibliographic record
    and complete abstract only; full-body reading separately scoped
  accessed_at: '2026-11-03T13:38:57.119708Z'
  snapshot_sha256: caaee89580068dd014c1ed51c05c6a6f5693ce5073fa8f89073ec58d5e488e59
  summary: 'PMID29074774, DOI10.1126/science.aan1478: Plasmepsins IX and X are essential
    and druggable mediators of malaria parasite egress and invasion. Complete abstract
    inspected; no full-body access implied by metadata.'
  support: supports
- evidence_id: micro-exo-blackman2008-jats
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2610400/fullTextXML
  locator: 'Complete subsection SERA processing by SUB1: an activation event?; extracted
    body rows19–22; review-tier text, not new experiments'
  accessed_at: '2026-11-03T13:38:57.121495Z'
  snapshot_sha256: 899e36096d2da3dd306f447032b906fb28679042b098c4fbbc4f3b158508b496
  summary: Secondary review explicitly attributes soluble PfSUB1 discharge into PV
    and SERA processing to Yeoh2007; proposed SERA activation and cross-stage extensions
    remain hypotheses.
  support: context_only
- evidence_id: micro-exo-withers2014-jats
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4024747/fullTextXML
  locator: All five introductory paragraphs and complete Discussion; extracted body
    rows0–4,23–27. Results/Methods/figure pixels not inspected
  accessed_at: '2026-11-03T13:38:57.123744Z'
  snapshot_sha256: 1ce1e42f1c39c9a38ff32c749e6376a1f6053c91a6cd64f0163e2088197fc06f
  summary: Primary structural paper background describes exoneme storage and PV discharge
    minutes before egress; Discussion makes reducing exoneme environment hypothetical.
    Used for attributed discharge context, not a new live-cell secretion experiment
    or verified in-vivo redox switch.
  support: supports
- evidence_id: micro-exo-nasamu2017-jats
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5928414/fullTextXML
  locator: Entire scientific main text and Fig1–4 captions, extracted body rows0–14;
    separate supplementary Methods and figure pixels not inspected
  accessed_at: '2026-11-03T13:38:57.135863Z'
  snapshot_sha256: 563825583d6aea2dffda29e592f303e3a4d5c9302b79dd4d321e5c12e65f898b
  summary: Immuno-EM and colocalization place PMX in exonemes; knockdown and catalytic
    rescue support final SUB1 maturation, SERA5/MSP1 processing and egress/invasion
    effects. Direct final cleavage versus prodomain-relief in vivo remains explicitly
    unresolved. Fig4 parental NF54 is not relabeled as3D7.
  support: supports
- evidence_id: micro-exo-O61142
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/O61142.json
  locator: Accession, reviewed status, recommended name, gene/ORF tokens, organism
    and relevant localization evidence/InterPro cross-references
  accessed_at: '2026-11-03T13:38:57.167004Z'
  snapshot_sha256: fa8b17256b77645b179d2c7dc6153036699ddff8481bba0b2e070982d9d84424
  summary: Native reviewed entry O61142 is Subtilisin-like protease 1, taxon5833;
    exact gene/ORF tokens and entry status match the maintained example or graph cross-reference.
    Secreted localization cites PMID9722575 with ECO0000269; PV lumen is by similarity
    to Q8I0V0. IPR017314 is a native family cross-reference.
  support: supports
- evidence_id: micro-exo-Q8IAS0
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q8IAS0.json
  locator: Accession, reviewed status, recommended name, gene/ORF tokens, organism
    and relevant localization evidence/InterPro cross-references
  accessed_at: '2026-11-03T13:38:57.754242Z'
  snapshot_sha256: b63747f066b55dcfb3a4884cb8647fa390225373879da2a2ba107cc7da15101f
  summary: Native reviewed entry Q8IAS0 is Plasmepsin X, taxon36329; exact gene/ORF
    tokens and entry status match the maintained example or graph cross-reference.
    Secretory-vesicle localization is by similarity to W7JWW5, not an additional direct
    experiment in this metadata.
  support: supports
- evidence_id: micro-exo-Q9TY95
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q9TY95.json
  locator: Accession, reviewed status, recommended name, gene/ORF tokens, organism
    and relevant localization evidence/InterPro cross-references
  accessed_at: '2026-11-03T13:38:57.804119Z'
  snapshot_sha256: 09588e9def043b90658a1a3517fdca2750c2e2fb538a23b20d97eea0ef9b6471
  summary: Native reviewed entry Q9TY95 is Serine-repeat antigen protein 5, taxon36329;
    exact gene/ORF tokens and entry status match the maintained example or graph cross-reference.
  support: supports
- evidence_id: micro-exo-Q8I0U8
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q8I0U8.json
  locator: Accession, reviewed status, recommended name, gene/ORF tokens, organism
    and relevant localization evidence/InterPro cross-references
  accessed_at: '2026-11-03T13:38:58.045287Z'
  snapshot_sha256: 40831b7d4689247dc2f789bdb59dd82111e28978e9495d5a477c7d8816e8f6e2
  summary: Native reviewed entry Q8I0U8 is Merozoite surface protein 1, taxon36329;
    exact gene/ORF tokens and entry status match the maintained example or graph cross-reference.
  support: supports
- evidence_id: micro-exo-sub1-query
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Asub1%29%20AND%20%28taxonomy_id%3A5833%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100
  locator: Exact query and all three returned reviewed accession/taxon/gene rows
  accessed_at: '2026-11-03T13:38:58.371315Z'
  snapshot_sha256: 74f4dbfe3b78df7a5201dd97636e6d959cbe6fd510342ddc9adcc02397ec02e4
  summary: The returned reviewed SUB1 entries are O61142 at species5833, Q8I0V0 at3D7/36329
    and W7K9M0 atNF54/5843. Exactly one result is at the maintained species taxon;
    descendant-isolate entries are not falsely excluded.
  support: supports
- evidence_id: micro-exo-pmx-query
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Apmx%29%20AND%20%28taxonomy_id%3A36329%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100
  locator: Exact query and complete single returned accession/taxon/gene row
  accessed_at: '2026-11-03T13:38:58.544856Z'
  snapshot_sha256: 6a076771ec70cab9b0e882587c6ff30d9b5ead4bec9c34531bb21710d396d4f1
  summary: The exact reviewed PMX query for3D7 returns Q8IAS0, supporting the record’s
    uniqueness note at that taxon.
  support: supports
- evidence_id: micro-exo-IPR017314
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017314/
  locator: metadata accession, type=family, name and complete non-LLM description
  accessed_at: '2026-11-03T13:38:59.031368Z'
  snapshot_sha256: 00de8b05b5da0a21adef9fd1db82c9c36b0bed42093f921563b3a7733a91ba68
  summary: InterPro explicitly types IPR017314 as a protein family for Plasmodium
    subtilisin-like peptidase1/SUB1. This matches the complete SUB1 molecular identity
    represented by the component; it is not merely an exoneme-location ontology term.
  support: supports
- evidence_id: micro-exo-IPR034204
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR034204/
  locator: metadata accession, type=domain, name, description and listed scope
  accessed_at: '2026-11-03T13:38:59.102158Z'
  snapshot_sha256: 21b4d4ef4ab3318beff2031ec322b95f1468565b12628cec1c9d98652815a7c8
  summary: IPR034204 is a catalytic domain, including related non-Plasmodium proteins,
    and is not an exact whole-SUB1 family substitute.
  support: supports
- evidence_id: micro-exo-IPR001461
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001461/
  locator: metadata accession, family name/type and description
  accessed_at: '2026-11-03T13:38:59.643280Z'
  snapshot_sha256: 7919edb7b7f8dd8968ee8b4babe8743c81eae2e921932e1372a14a8d6f77bd09
  summary: IPR001461 is the broad pepsin/A1 family; its scope is wider than the exact
    PMX component. No exact PMX-family grounding is established by this candidate.
  support: supports
- evidence_id: micro-eye-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031904,GO:0070013,GO:0005768,GO:0010008,GO:0005771,GO:0071985,GO:0016020,GO:0000813,GO:0000815,GO:0012507,GO:0030658,GO:0030662,GO:0030134,GO:0005789,GO:0090114,GO:0030127,GO:1990413
  locator: Exact GO1990413 active ID/name/definition/two RELATED synonyms within returned17-term
    packet; unrelated packet terms not assessed
  accessed_at: '2026-11-03T13:38:59.747988Z'
  snapshot_sha256: 196c0eb6263923cb4c06c3050858f88ab320a65b4a9504075dfc5796e203a956
  summary: GO1990413 matches small pigmented light-detection organelle; eyespot and
    stigma are RELATED synonyms. OTHER kind preserves the cross-membrane apparatus
    boundary.
  support: supports
- evidence_id: micro-eye-tax3055
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055
  locator: Exact taxId, scientificName, rank, lineage and alternate names
  accessed_at: '2026-11-03T13:39:00.144558Z'
  snapshot_sha256: e3861fe6706cefe2e079e15c0178a65e95efaad3890f548f25e721553eaa93a0
  summary: Native ENA exact species identity and lineage agree with Chlamydomonas
    reinhardtii3055. This is taxonomic identity, not a measured population prevalence
    or an experimental strain assignment.
  support: supports
- evidence_id: micro-eye-lamb1999-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A10511552%20AND%20SRC%3AMED
  locator: Exact Europe PMC DOI/PMID core lookup; complete MED bibliographic record
    and complete abstract only; full-body reading separately scoped
  accessed_at: '2026-11-03T13:39:00.250744Z'
  snapshot_sha256: e1f246c780df2a89267bf5ca75d5bf8740c709ab7b2bef092e58b85c8551f53d
  summary: 'PMID10511552, DOI10.1093/genetics/153.2.721: Eyespot-assembly mutants
    in Chlamydomonas reinhardtii. Complete abstract inspected; no full-body access
    implied by metadata.'
  support: supports
- evidence_id: micro-eye-schmidt2006-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A16798888%20AND%20SRC%3AMED
  locator: Exact Europe PMC DOI/PMID core lookup; complete MED bibliographic record
    and complete abstract only; full-body reading separately scoped
  accessed_at: '2026-11-03T13:39:00.304421Z'
  snapshot_sha256: 850f4cc8cabfa09801d9c8b4e6f75d5d57eb23fdc230638b8e96f0d16fd0ac04
  summary: 'PMID16798888, DOI10.1105/tpc.106.041749: Proteomic analysis of the eyespot
    of Chlamydomonas reinhardtii provides novel insights into its components and tactic
    movements. Complete abstract inspected; no full-body access implied by metadata.'
  support: supports
- evidence_id: micro-eye-mittelmeier2011-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A21555459%20AND%20SRC%3AMED
  locator: Exact Europe PMC DOI/PMID core lookup; complete MED bibliographic record
    and complete abstract only; full-body reading separately scoped
  accessed_at: '2026-11-03T13:39:00.349095Z'
  snapshot_sha256: 2f766caa5745c29e75178d0f3a359bfd48e1d9aca542c3fcd47c01388c0560aa
  summary: 'PMID21555459, DOI10.1083/jcb.201009131: Asymmetric properties of the Chlamydomonas
    reinhardtii cytoskeleton direct rhodopsin photoreceptor localization. Complete
    abstract inspected; no full-body access implied by metadata.'
  support: supports
- evidence_id: micro-eye-awasthi2016-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1038/srep34646%22
  locator: Exact Europe PMC DOI/PMID core lookup; complete MED bibliographic record
    and complete abstract only; full-body reading separately scoped
  accessed_at: '2026-11-03T13:39:00.752874Z'
  snapshot_sha256: a743b5587fe994628934a068e7ae5c7a1a9b7267f04cad7ac5c63b9a4fe09431
  summary: 'PMID27694882, DOI10.1038/srep34646: The trafficking of bacterial type
    rhodopsins into the Chlamydomonas eyespot and flagella is IFT mediated. Complete
    abstract inspected; no full-body access implied by metadata.'
  support: supports
- evidence_id: micro-eye-ueki2016-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A27122315%20AND%20SRC%3AMED
  locator: Exact Europe PMC DOI/PMID core lookup; complete MED bibliographic record
    and complete abstract only; full-body reading separately scoped
  accessed_at: '2026-11-03T13:39:00.858445Z'
  snapshot_sha256: 76490f9cc73b3d10b63df0175e814cabd93099a3f02e0e545f99e3f4ae57846c
  summary: 'PMID27122315, DOI10.1073/pnas.1525538113: Eyespot-dependent determination
    of the phototactic sign in Chlamydomonas reinhardtii. Complete abstract inspected;
    no full-body access implied by metadata.'
  support: supports
- evidence_id: micro-eye-protein-Q8RUT8
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q8RUT8.json
  locator: Exact primary accession, protein names, cop4/acop2/CSOB tokens,taxon3055,TrEMBL
    status and broad opsin-family crossref
  accessed_at: '2026-11-03T13:39:00.926975Z'
  snapshot_sha256: 5576309014e3a4ed270d37783133413c0542b2274a515253521947c72acb5ac3
  summary: Q8RUT8 is unreviewed archaeal-type opsin2/cop4 at tax3055; broad IPR001425
    and automated location do not independently prove eyespot membership.
  support: supports
- evidence_id: micro-eye-query-COP3-true
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=gene_exact%3ACOP3%20AND%20taxonomy_id%3A3055%20AND%20reviewed%3Atrue
  locator: Full returned results at size500, exact query and entry identities
  accessed_at: '2026-11-03T13:39:00.965425Z'
  snapshot_sha256: 5021e624e752b001ce3e3846e8f158ed4aeb93a4c9a72fdb35a0c5b14a0eea84
  summary: The complete gene_exact:COP3, taxonomy_id:3055, reviewed:true query returns
    0 entries. This bounded query result is not proof that the gene or an accession
    does not exist under other names.
  support: supports
- evidence_id: micro-eye-query-COP3-false
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=gene_exact%3ACOP3%20AND%20taxonomy_id%3A3055%20AND%20reviewed%3Afalse
  locator: Full returned results at size500, exact query and entry identities
  accessed_at: '2026-11-03T13:39:01.383917Z'
  snapshot_sha256: 5021e624e752b001ce3e3846e8f158ed4aeb93a4c9a72fdb35a0c5b14a0eea84
  summary: The complete gene_exact:COP3, taxonomy_id:3055, reviewed:false query returns
    0 entries. This bounded query result is not proof that the gene or an accession
    does not exist under other names.
  support: supports
- evidence_id: micro-eye-query-COP4-true
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=gene_exact%3ACOP4%20AND%20taxonomy_id%3A3055%20AND%20reviewed%3Atrue
  locator: Full returned results at size500, exact query and entry identities
  accessed_at: '2026-11-03T13:39:01.460531Z'
  snapshot_sha256: 5021e624e752b001ce3e3846e8f158ed4aeb93a4c9a72fdb35a0c5b14a0eea84
  summary: The complete gene_exact:COP4, taxonomy_id:3055, reviewed:true query returns
    0 entries. This bounded query result is not proof that the gene or an accession
    does not exist under other names.
  support: supports
- evidence_id: micro-eye-query-COP4-false
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=gene_exact%3ACOP4%20AND%20taxonomy_id%3A3055%20AND%20reviewed%3Afalse
  locator: Full returned results at size500, exact query and entry identities
  accessed_at: '2026-11-03T13:39:01.480682Z'
  snapshot_sha256: 0bd25d61ad25cdfe1e9f616843cb530809a4a412398cc34d7b3787815b3ffe5e
  summary: The complete gene_exact:COP4, taxonomy_id:3055, reviewed:false query returns
    1 entries (Q8RUT8). This bounded query result is not proof that the gene or an
    accession does not exist under other names.
  support: supports
- evidence_id: micro-eye-schmidt2006-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1533972/
  locator: Introduction paragraph on COP3/COP4 aliases; Table1 photoreceptor rows;
    complete paragraphs indexed32,54,55,67,74,77,89 and cw15 purification Methods145
    in extracted text. Other Table1 rows only contextual, not individually recertified
  accessed_at: '2026-11-03T13:39:01.562717Z'
  snapshot_sha256: 1eb51b46030fb4a849f623ee9b587d011cc6defe9a223917b2622efc9c8a9c4b
  summary: Table1 explicitly bridges COP3/CHOP1/CSRA/Acop1 (eight peptides) and COP4/CHOP2/CSRB/Acop2
    (three peptides). Purified cw15 eyespot fractions support cohort association with
    explicit contaminant/loss limitations; reference identity and candidate detection
    do not automatically prove every proteome constituent or direct ChR2 localization.
  support: supports
- evidence_id: micro-eye-mittelmeier2011-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3166873/
  locator: Introduction paragraphs and Fig1 caption; first Results subsection ChR1
    association with most extensively acetylated daughter rootlet and Fig2 caption;
    Strains and media. Extracted rows14–28,83–86; no figure pixels
  accessed_at: '2026-11-03T13:39:01.592217Z'
  snapshot_sha256: d872a90219dc9dceb1060aff98ea6413dea3ec510c3a2fdcc80c87bf04b4677b
  summary: Direct ChR1 immunofluorescence shows equatorial patches adjacent to the
    D4 rootlet in wild type and altered patterns in mutants. Study distinguishes photoreceptor
    trafficking model from observations; reference strain137c/CC125 and mutant backgrounds
    are not all one generic strain. No direct ChR2 imaging claimed.
  support: supports
- evidence_id: micro-eye-awasthi2016-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC5046144/
  locator: Introductory rhodopsin/IFT context, first Results localization paragraph,
    Strains and media and Antibodies Methods; extracted rows14–22,69–75. Other trafficking
    experiments and figure pixels not independently read
  accessed_at: '2026-11-03T13:39:02.037813Z'
  snapshot_sha256: 2daa6112a146cda9fcb2465229d55fd36476b82729bbe2f73d730a774c7db87c
  summary: Explicit COP3=ChR1 and COP4=ChR2 naming bridge. Principal experimentally
    trafficked proteins are ChR1 and Cop8, not both ChR1 and ChR2; source context
    does not export all IFT controls to ChR2.
  support: supports
- evidence_id: micro-eye-ueki2016-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4868408/
  locator: Complete Results subsections from lts1-211 carotenoid/eyespot deficiency
    through lens-effect/model discussion; Fig4–6/S3/S4 captions; complete Discussion
    and main Methods. Extracted rows55–77,98–106. No current figure-pixel/SI dataset
    inspection
  accessed_at: '2026-11-03T13:39:02.052471Z'
  snapshot_sha256: a0babbea987a266785c233550bfd13026b171e0ca2007ff163295c21e07c8758
  summary: Mutant/rescue and redox-biased behavior plus cellular lens observations
    support pigment-layer shielding and phototactic sign; eyeless cells can still
    show strong phototaxis under tested conditions. Fig6 is an explanatory model.
    Whole-cell carotenoid HPLC is not an exhaustive eyespot chemical-species inventory.
  support: supports
- evidence_id: micro-fer-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043231
  locator: Exact active ID/name/definition and returned children
  accessed_at: '2026-11-03T13:39:02.065283Z'
  snapshot_sha256: 633262bf25df8960e37134d348c2a702c8886dbb7c352b683f5cf43c8058158b
  summary: GO0043231 defines an intracellular membrane-bounded organelle, compatible
    with the experimentally described bacterial ferrosome. The minted record is not
    claimed to be a direct GO child.
  support: supports
- evidence_id: micro-fer-tax573370
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/573370
  locator: Exact taxId, scientificName, rank, lineage and equivalent names
  accessed_at: '2026-11-03T13:39:02.123927Z'
  snapshot_sha256: 74b9f549ae8746720be051b2722a85b8ad84a130216a3fd1dc2c3fabf9d795b7
  summary: ENA identifies tax573370 as Solidesulfovibrio magneticus RS-1, strain rank,
    with Desulfovibrio magneticus RS-1 and700980 as equivalent names. This directly
    bridges the current maintained name to the primary-paper nomenclature.
  support: supports
- evidence_id: micro-fer-grant2022-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/s41586-022-04741-x
  locator: Exact Europe PMC DOI/PMID core lookup; complete MED bibliographic record
    and complete abstract only; full-body reading separately scoped
  accessed_at: '2026-11-03T13:39:02.445401Z'
  snapshot_sha256: 433637849520f94e2d38990bea87bff18b1f288d1167a116a11ea90c4baca0c6
  summary: 'PMID35585231, DOI10.1038/s41586-022-04741-x: Distinct gene clusters drive
    formation of ferrosome organelles in bacteria. Complete abstract inspected; no
    full-body access implied by metadata.'
  support: supports
- evidence_id: micro-fer-byrne2010-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1073/pnas.1001290107
  locator: Exact Europe PMC DOI/PMID core lookup; complete MED bibliographic record
    and complete abstract only; full-body reading separately scoped
  accessed_at: '2026-11-03T13:39:02.462422Z'
  snapshot_sha256: cf8359e17d8f95c09876a80d5c20bfe2b1ba37bf659e5e2d4b0656e306f25e15
  summary: 'PMID20566879, DOI10.1073/pnas.1001290107: Desulfovibrio magneticus RS-1
    contains an iron- and phosphorus-rich organelle distinct from its bullet-shaped
    magnetosomes. Complete abstract inspected; no full-body access implied by metadata.'
  support: supports
- evidence_id: micro-fer-grant2022-s3
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC10906721.1/PMC10906721.1.xml
  locator: Complete scientific main Introduction/Results/Discussion sections through
    S7, extracted rows0–16; independent fresh read. Methods, supplementary tables
    and figure pixels not read by this reviewer
  accessed_at: '2026-11-03T13:39:02.639156Z'
  snapshot_sha256: 015e012e12537c8f5efdb93825a0c5f01661ea60778b4973a415ac095fc6a49c
  summary: DMR_28320/28330/28340 map to FezA/B/C; fraction proteomics and RS-1 fezBC
    deletion plus fezABC complementation support cohort-dependent formation. Direct
    iron-starvation fitness/rescue is S.putrefaciens, not RS-1. E.coli heterologous
    fezSp and AMB-1 fezRp show engineered-host sufficiency; exact iron transport and
    membrane biogenesis remain open.
  support: supports
- evidence_id: micro-fer-C4XH20
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/C4XH20.json
  locator: Accession, TrEMBL entry status, organism, protein description, genes.orderedLocusNames
    and InterPro cross-references
  accessed_at: '2026-11-03T13:39:02.952227Z'
  snapshot_sha256: af7d7531a9c3a5fee7263b27181fd2816fb93702f6e5940cd240ef94d225ef08
  summary: Native unreviewed accession C4XH20, tax573370 and ordered-locus token DMR_28320
    match the maintained example. The FezA alias bridge comes from Grant2022, not
    an independently indexed UniProt geneName. Automated protein-name annotations
    are not treated as measured substrate specificity.
  support: supports
- evidence_id: micro-fer-C4XH21
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/C4XH21.json
  locator: Accession, TrEMBL entry status, organism, protein description, genes.orderedLocusNames
    and InterPro cross-references
  accessed_at: '2026-11-03T13:39:03.067197Z'
  snapshot_sha256: c8233fdce219a73c3b53b88e81214230172b9ece3c94288c921bef18460a1984
  summary: Native unreviewed accession C4XH21, tax573370 and ordered-locus token DMR_28330
    match the maintained example. The FezB alias bridge comes from Grant2022, not
    an independently indexed UniProt geneName. Automated protein-name annotations
    are not treated as measured substrate specificity.
  support: supports
- evidence_id: micro-fer-C4XH22
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/C4XH22.json
  locator: Accession, TrEMBL entry status, organism, protein description, genes.orderedLocusNames
    and InterPro cross-references
  accessed_at: '2026-11-03T13:39:03.077007Z'
  snapshot_sha256: a4e0dfe3e3c9c00b665bf808963e12704c0b5d7ac48545255cc70fd118f76ded
  summary: Native unreviewed accession C4XH22, tax573370 and ordered-locus token DMR_28340
    match the maintained example. The FezC alias bridge comes from Grant2022, not
    an independently indexed UniProt geneName. Automated protein-name annotations
    are not treated as measured substrate specificity.
  support: supports
- evidence_id: micro-fer-IPR027256
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR027256/
  locator: metadata family/type/name and complete description
  accessed_at: '2026-11-03T13:39:03.100539Z'
  snapshot_sha256: 9696e9d8ffd6ecca64086f65b83b2fa12cf1dde004155eadda4a635f5df4d3f4
  summary: IPR027256 covers broad subfamilyIB P-type metal ATPases. It is wider than
    FezB and cannot ground the unrelated FezA/B/C cohort as a single exact family.
    An annotated Zn transporter name is not direct evidence of FezB zinc specificity.
  support: supports
- evidence_id: micro-fer-go-search
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=ferrosome&limit=100
  locator: Native query and complete zero-result response
  accessed_at: '2026-11-03T13:39:03.185472Z'
  snapshot_sha256: f3a7dae9b1e9335291e3940cdf0e5f8dadf9335da7b9547710606b5106c63f86
  summary: The exact bounded native query for ferrosome returned zero results. This
    is search context only, not an exhaustive claim that no ontology anywhere contains
    a matching concept.
  support: context_only
  search_scope: Fresh QuickGO search at 2026-11-03T13:39:03.185472Z; literal query
    'ferrosome'; requested limit/size 100; inspected complete returned page (0 rows),
    total header None, next-page Link None. Bounded query result only; not worldwide
    gene/family/ontology absence.
- evidence_id: micro-byrne-canonical
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2901430/
  locator: Complete Introduction, Results, Discussion, main Methods and Fig1–5 captions;
    extracted rows20–65. No image-pixel or separate supplementary Methods reanalysis
  accessed_at: '2026-11-03T13:39:45.534806Z'
  snapshot_sha256: 25dcbaea33c0dc38dc78628d3eeeb3bf20cca90e88d08394352e59e3c32f5427
  summary: RS-1 EDS finds Fe/P/O-rich amorphous granules; pulse-chase NanoSIMS and
    three imaging approaches distinguish membrane-enclosed granules from bullet-shaped
    crystals. Transient iron-influx response and proposed storage/sequestration do
    not directly test anaerobic fitness. Authors retain limits on magnetosome membrane
    visibility.
  support: supports
- evidence_id: micro-eye-Q93WP2
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q93WP2.json
  locator: Exact primary accession, full submitted protein names, native geneName
    acop1, organism3055 and entryType; relevant broad family/location annotations
  accessed_at: '2026-11-03T13:39:03.564997Z'
  snapshot_sha256: ffcf1fd2492e36111dae0ca08dd2c6386c7ef05738b1eb01c43e45c737c71b1d
  summary: New Q93WP2 is unreviewed archaeal-type opsin1/Channelopsin-1, primary gene
    acop1, tax3055. UniProt does not index literal COP3; freshly read Schmidt Table1
    maps COP3 to Acop1, independently supporting the maintained alias role. Automated
    annotation alone is not eyespot membership.
  support: supports
- evidence_id: micro-yeoh-pdf
  kind: authority
  reference: https://www.cell.com/cell/pdf/S0092-8674(07)01403-1.pdf
  locator: Actual publisher access response only, HTTP403; not scientific full text
  accessed_at: '2026-11-03T13:39:45.535150Z'
  snapshot_sha256: 8ce0385c4cc3f85c7031e9648f7ae1fce8a539f49d0bcfafe918edca4147ec1b
  summary: Primary body unavailable through this checked route. Complete native abstract
    remains the inspected tier; no full-body or figure claim.
  support: context_only
- evidence_id: micro-blackman1998-pdf
  kind: authority
  reference: https://www.jbc.org/article/S0021925819750030/pdf
  locator: Actual publisher access response only, HTTP403; not scientific full text
  accessed_at: '2026-11-03T13:39:45.535292Z'
  snapshot_sha256: 990db20e747b87f95594b4940097480723bb34f2cd03ffc86121ad69a2734e73
  summary: Primary body unavailable through this checked route. Complete native abstract
    remains the inspected tier; no full-body or figure claim.
  support: context_only
- evidence_id: micro-source-access
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/adversary-microtubule/manifest.json
  locator: 49 current public-source responses; initial sandbox DNS failures separately
    archived; numeric Byrne response replaced by canonical PMC body
  accessed_at: '2026-11-03T13:43:24.002658Z'
  snapshot_sha256: 04a3e6c8bba617cd7f9316b915a7b14fa362ba982383b93c64fb529eed421e7e
  summary: Authority/source fetch statuses are recorded. HTTP200 numeric Byrne route
    is not treated as body evidence; canonical article was separately fetched and
    read. Publisher403 responses for Yeoh/Blackman are explicit; original historic
    figures are not claimed freshly viewed.
  support: context_only
- evidence_id: micro-historical-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Actual historical adapter datasets invocation and PermissionError; reused
    receipt, no current invocation
  accessed_at: '2026-11-03T00:49:00.863225Z'
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Historical 00:49Z runner unavailable due interpreter-environment PermissionError;
    this is not a fresh failed run. Current applicability uses inspected official
    source catalogue.
  support: context_only
- evidence_id: micro-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: 'Complete official /api/datasets response: all20 organism rows and28 organism/dataset
    pairs; names/IDs/descriptions/dataset lists read'
  accessed_at: '2026-11-03T13:39:03.691493Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  summary: No represented Plasmodium falciparum, Chlamydomonas reinhardtii or Solidesulfovibrio/Desulfovibrio
    magneticus RS-1 dataset. Three pathway-bearing targets require applicability assessment,
    but no matched module/gene query can be constructed from this catalogue. Foreign-host
    E.coli fez constructs are not an RS-1 proxy.
  support: context_only
  search_scope: Official iModulonDB /api/datasets API retrieved 2026-11-03T13:39:03.691493Z;
    no server query/filter/page parameter; complete20 returned organism rows/28 organism-dataset
    pairs inspected. Bounded case-insensitive checks for Plasmodium/falciparum/3D7/NF54,Chlamydomonas/reinhardtii,Solidesulfovibrio/Desulfovibrio/magneticus/RS-1/700980/13731
    and primary-model Shewanella/putrefaciens/Rhodopseudomonas/palustris. No catalogue
    match; absence is not negative biological evidence or an exhaustive transcriptomics
    search.
- evidence_id: micro-local-ferrosome-id
  kind: search
  reference: 'rg --no-ignore --hidden -n ^identifier: cellstructuremech:ferrosome$
    data/structures'
  locator: Whole maintained data/structures exact identifier-line scan; ignored and
    hidden files included
  accessed_at: '2026-11-03T13:41:32.029468Z'
  snapshot_sha256: e7be63b2cee53cd2f43532050544d070b54e93e1f2386b68534604fd0429b9a6
  summary: Exactly one maintained identifier-line match, the frozen ferrosome target.
    No claim about every textual alias or external ontology.
  support: context_only
  search_scope: rg --no-ignore --hidden -n with exact anchored identifier cellstructuremech:ferrosome
    across data/structures at current source head; ignored/hidden files included;
    one matching identifier line. 2026-11-03T13:41:32.029468Z
- evidence_id: septin-review-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Structured-source cross-checks and immutable review contract
  summary: Assess actual named molecular or pathway assertions throughout the record.
    Expression-only exemptions are insufficient; material/morphology-only records
    may genuinely exclude molecular queries. Catalogue noncoverage is not negative
    biological evidence.
  accessed_at: '2026-11-03T13:44:45.663261Z'
  support: supports
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: septin-curation-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Component grounding and family consensus; collective material and protein-example
    evidence
  summary: Reviewed label-only components can document missing exact grounding. The
    automated InterPro policy promotes integrated entries typed family only, not domains,
    sites or homologous superfamilies. Exact protein identity is distinct from experimentally
    supported localization and necessity.
  accessed_at: '2026-11-03T13:44:45.663261Z'
  support: supports
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: septin-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: NONMECHANISTIC topology and empirical association
  summary: Parthood, boundaries and observed cargo association may remain descriptive.
    Cofractionation and colocalization do not establish purified co-crystallization,
    stoichiometry, nucleation or universal formation necessity.
  accessed_at: '2026-11-03T13:44:45.663261Z'
  support: supports
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: septin-record-er_to_golgi_transport_vesicle_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/er_to_golgi_transport_vesicle_membrane.yaml
  locator: Complete maintained record at 5c140efd0be92d341410aa3024d677d5daf8bc1e
  summary: Read identity, definition, hierarchy/parthood, synonyms/xrefs, components,
    protein examples when present, taxon/example, functions, every evidence note and
    graph edge, discussions and history. No target images, quantitative properties,
    associated traits or verbatim snippets are declared.
  accessed_at: '2026-11-03T13:44:45.663261Z'
  support: supports
  snapshot_sha256: 5cdd951707eead318295ce7ceb64c16bdc0c85b465374678d564878481f04a9c
- evidence_id: septin-original-er_to_golgi_transport_vesicle_membrane
  kind: prior_review
  reference: reviews/structured/20261022T013717Z-er-to-golgi-transport-vesicle-membrane-audit/review.yaml
  locator: Complete original YAML/Markdown; source inputs, checks, evidence tiers,
    assessments, empty findings/actions and limitations
  summary: Original qualified positive scientific assessment has no findings/actions.
    It contains an explicit imodulondb exclusion, not an omitted row. Its historical
    checks/access dates remain historical; applicability is reassessed from the complete
    maintained record.
  accessed_at: '2026-11-03T13:44:45.663261Z'
  support: supports
  snapshot_sha256: 443302a78569d841b938a4a245ed64efbb78f00364a5a238e5e99889992ccac5
- evidence_id: septin-original-validation-er_to_golgi_transport_vesicle_membrane
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/adversary-septin/original-checks.json
  locator: 20261022T013717Z-er-to-golgi-transport-vesicle-membrane-audit native validate/render
    and frozen input comparison
  summary: Native validate and render exited zero; Markdown is byte-identical. Historical-source,
    original frozen and current target hashes agree.
  accessed_at: '2026-11-03T13:39:58.276305Z'
  support: supports
  snapshot_sha256: 87f7b45c99a6d36f646e3c59358c80dc2bd7ee0bf1c39f7d8a27e3105f13804a
- evidence_id: septin-native-er_to_golgi_transport_vesicle_membrane-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/er_to_golgi_transport_vesicle_membrane-uniprot-verify-receipt.json
  locator: Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/er_to_golgi_transport_vesicle_membrane-uniprot-verify.log
  summary: Exit zero. No protein_examples, protein UniProtKB graph xrefs or GENE_OR_PROTEIN
    nodes are represented. Exit zero validates this empty represented inventory only,
    not narrative named molecules, pathway behavior, source localization or completeness.
  accessed_at: '2026-11-03T13:38:22.312803Z'
  support: supports
  snapshot_sha256: d66f12a8a21de933d597ac0ffadb3530fde5e1bf8656a70b6225d739f6e503c9
- evidence_id: septin-native-er_to_golgi_transport_vesicle_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/er_to_golgi_transport_vesicle_membrane-uniprot-causal-receipt.json
  locator: Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/er_to_golgi_transport_vesicle_membrane-uniprot-causal.log
  summary: Exit zero. No protein_examples, protein UniProtKB graph xrefs or GENE_OR_PROTEIN
    nodes are represented. Exit zero validates this empty represented inventory only,
    not narrative named molecules, pathway behavior, source localization or completeness.
  accessed_at: '2026-11-03T13:38:22.762248Z'
  support: supports
  snapshot_sha256: 1069a7e99a64db57943038a64fd5d79932e27701873fd0164eab0a8a0472bb09
- evidence_id: septin-record-esterosome
  kind: record_content
  reference: data/structures/membrane_organelle/esterosome.yaml
  locator: Complete maintained record at 5c140efd0be92d341410aa3024d677d5daf8bc1e
  summary: Read identity, definition, hierarchy/parthood, synonyms/xrefs, components,
    protein examples when present, taxon/example, functions, every evidence note and
    graph edge, discussions and history. No target images, quantitative properties,
    associated traits or verbatim snippets are declared.
  accessed_at: '2026-11-03T13:44:45.663261Z'
  support: supports
  snapshot_sha256: c5779634687c3e16478f4782e24897bc8df7939f14eddfd26ec4715c6de3c95a
- evidence_id: septin-original-esterosome
  kind: prior_review
  reference: reviews/structured/20261022T013717Z-esterosome-audit/review.yaml
  locator: Complete original YAML/Markdown; source inputs, checks, evidence tiers,
    assessments, empty findings/actions and limitations
  summary: Original qualified positive scientific assessment has no findings/actions.
    It contains an explicit imodulondb exclusion, not an omitted row. Its historical
    checks/access dates remain historical; applicability is reassessed from the complete
    maintained record.
  accessed_at: '2026-11-03T13:44:45.663261Z'
  support: supports
  snapshot_sha256: 3771f361702237469102a561833617eb0a3e6b5bb070204d184e8311067b20e9
- evidence_id: septin-original-validation-esterosome
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/adversary-septin/original-checks.json
  locator: 20261022T013717Z-esterosome-audit native validate/render and frozen input
    comparison
  summary: Native validate and render exited zero; Markdown is byte-identical. Historical-source,
    original frozen and current target hashes agree.
  accessed_at: '2026-11-03T13:39:59.468332Z'
  support: supports
  snapshot_sha256: 87f7b45c99a6d36f646e3c59358c80dc2bd7ee0bf1c39f7d8a27e3105f13804a
- evidence_id: septin-native-esterosome-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/esterosome-uniprot-verify-receipt.json
  locator: Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/esterosome-uniprot-verify.log
  summary: Exit zero. Two exact reviewed protein examples P21837/cryS and P18142/D2
    validate; the one GENE_OR_PROTEIN node is COVERED through its component_ref. This
    covers declared identifiers and symbols, not exact family grounding, source localization,
    stoichiometry, necessity or completeness.
  accessed_at: '2026-11-03T13:38:24.012468Z'
  support: supports
  snapshot_sha256: e576125bc93861dc0262b38b0f41c5cfde9be13161236e47a212132d7b57a526
- evidence_id: septin-native-esterosome-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/esterosome-uniprot-causal-receipt.json
  locator: Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/esterosome-uniprot-causal.log
  summary: Exit zero. Two exact reviewed protein examples P21837/cryS and P18142/D2
    validate; the one GENE_OR_PROTEIN node is COVERED through its component_ref. This
    covers declared identifiers and symbols, not exact family grounding, source localization,
    stoichiometry, necessity or completeness.
  accessed_at: '2026-11-03T13:38:24.453612Z'
  support: supports
  snapshot_sha256: 3f1d928016d6688c94923393136670fd5fd1442a3a5b6d1104dd0efe7357c56e
- evidence_id: septin-record-esterosome_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/esterosome_lumen.yaml
  locator: Complete maintained record at 5c140efd0be92d341410aa3024d677d5daf8bc1e
  summary: Read identity, definition, hierarchy/parthood, synonyms/xrefs, components,
    protein examples when present, taxon/example, functions, every evidence note and
    graph edge, discussions and history. No target images, quantitative properties,
    associated traits or verbatim snippets are declared.
  accessed_at: '2026-11-03T13:44:45.663261Z'
  support: supports
  snapshot_sha256: 6891a8c551bc57b8ab1ce07357d050e40b46303debc2de0b81132b54424b53a4
- evidence_id: septin-original-esterosome_lumen
  kind: prior_review
  reference: reviews/structured/20261022T013718Z-esterosome-lumen-audit/review.yaml
  locator: Complete original YAML/Markdown; source inputs, checks, evidence tiers,
    assessments, empty findings/actions and limitations
  summary: Original qualified positive scientific assessment has no findings/actions.
    It contains an explicit imodulondb exclusion, not an omitted row. Its historical
    checks/access dates remain historical; applicability is reassessed from the complete
    maintained record.
  accessed_at: '2026-11-03T13:44:45.663261Z'
  support: supports
  snapshot_sha256: 95bb137bbc197c2b8e26c6b030050aa97f3dd20d330b6be25c6c8ec5a37345cc
- evidence_id: septin-original-validation-esterosome_lumen
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/adversary-septin/original-checks.json
  locator: 20261022T013718Z-esterosome-lumen-audit native validate/render and frozen
    input comparison
  summary: Native validate and render exited zero; Markdown is byte-identical. Historical-source,
    original frozen and current target hashes agree.
  accessed_at: '2026-11-03T13:40:00.643361Z'
  support: supports
  snapshot_sha256: 87f7b45c99a6d36f646e3c59358c80dc2bd7ee0bf1c39f7d8a27e3105f13804a
- evidence_id: septin-native-esterosome_lumen-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/esterosome_lumen-uniprot-verify-receipt.json
  locator: Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/esterosome_lumen-uniprot-verify.log
  summary: Exit zero. No protein_examples, protein UniProtKB graph xrefs or GENE_OR_PROTEIN
    nodes are represented. Exit zero validates this empty represented inventory only,
    not narrative named molecules, pathway behavior, source localization or completeness.
  accessed_at: '2026-11-03T13:38:24.894006Z'
  support: supports
  snapshot_sha256: 51bd744e98da3fc5e23ca41a70ba79c28090475ea19ab57d54512182fa3f9fda
- evidence_id: septin-native-esterosome_lumen-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/esterosome_lumen-uniprot-causal-receipt.json
  locator: Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/esterosome_lumen-uniprot-causal.log
  summary: Exit zero. No protein_examples, protein UniProtKB graph xrefs or GENE_OR_PROTEIN
    nodes are represented. Exit zero validates this empty represented inventory only,
    not narrative named molecules, pathway behavior, source localization or completeness.
  accessed_at: '2026-11-03T13:38:25.336962Z'
  support: supports
  snapshot_sha256: 29563b0104271e12248955b38fc9d1e79ec5739660d4569daa3d942c1352fa75
- evidence_id: septin-record-esterosome_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/esterosome_membrane.yaml
  locator: Complete maintained record at 5c140efd0be92d341410aa3024d677d5daf8bc1e
  summary: Read identity, definition, hierarchy/parthood, synonyms/xrefs, components,
    protein examples when present, taxon/example, functions, every evidence note and
    graph edge, discussions and history. No target images, quantitative properties,
    associated traits or verbatim snippets are declared.
  accessed_at: '2026-11-03T13:44:45.663261Z'
  support: supports
  snapshot_sha256: b29aff5dceea8ed56348277d76f1c3658da2f304baa1b8e9858bf64cea5f4e5a
- evidence_id: septin-original-esterosome_membrane
  kind: prior_review
  reference: reviews/structured/20261022T013719Z-esterosome-membrane-audit/review.yaml
  locator: Complete original YAML/Markdown; source inputs, checks, evidence tiers,
    assessments, empty findings/actions and limitations
  summary: Original qualified positive scientific assessment has no findings/actions.
    It contains an explicit imodulondb exclusion, not an omitted row. Its historical
    checks/access dates remain historical; applicability is reassessed from the complete
    maintained record.
  accessed_at: '2026-11-03T13:44:45.663261Z'
  support: supports
  snapshot_sha256: 5caf336f1791fa5d7564ce6e976de292b62a9853d3f9728a37c9e665aa59e3d8
- evidence_id: septin-original-validation-esterosome_membrane
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/adversary-septin/original-checks.json
  locator: 20261022T013719Z-esterosome-membrane-audit native validate/render and frozen
    input comparison
  summary: Native validate and render exited zero; Markdown is byte-identical. Historical-source,
    original frozen and current target hashes agree.
  accessed_at: '2026-11-03T13:40:01.800263Z'
  support: supports
  snapshot_sha256: 87f7b45c99a6d36f646e3c59358c80dc2bd7ee0bf1c39f7d8a27e3105f13804a
- evidence_id: septin-native-esterosome_membrane-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/esterosome_membrane-uniprot-verify-receipt.json
  locator: Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/esterosome_membrane-uniprot-verify.log
  summary: Exit zero. No protein_examples, protein UniProtKB graph xrefs or GENE_OR_PROTEIN
    nodes are represented. Exit zero validates this empty represented inventory only,
    not narrative named molecules, pathway behavior, source localization or completeness.
  accessed_at: '2026-11-03T13:38:25.789048Z'
  support: supports
  snapshot_sha256: ad53d9e3aafb79daa2275f020311c4a006538359e391dccd3b91523669cc11bf
- evidence_id: septin-native-esterosome_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/esterosome_membrane-uniprot-causal-receipt.json
  locator: Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/esterosome_membrane-uniprot-causal.log
  summary: Exit zero. No protein_examples, protein UniProtKB graph xrefs or GENE_OR_PROTEIN
    nodes are represented. Exit zero validates this empty represented inventory only,
    not narrative named molecules, pathway behavior, source localization or completeness.
  accessed_at: '2026-11-03T13:38:26.234839Z'
  support: supports
  snapshot_sha256: 1f8f25739aca01889c3b12a41ca614f60c3bb35ef77b6446bb11d90841512956
- evidence_id: septin-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0012507,GO:0030658,GO:0030662,GO:0030134,GO:0005789,GO:0090114,GO:0030127,GO:0033117,GO:0034467,GO:0033118,GO:0031410,GO:0043233,GO:0030659,GO:0060205
  locator: Fourteen exact active GO terms, definitions, synonyms and typed child edges
  summary: GO0012507 denotes the ER-to-Golgi surrounding lipid bilayer and has the
    exact COPII-coated-vesicle-membrane synonym; GO0030658/0030662 are native parent
    classes and GO0030134 is the containing vesicle. GO0033117 esterosome is_a cytoplasmic
    vesicle GO0031410 and contains lumen GO0034467 and membrane GO0033118. Membrane
    is_a GO0030659; lumen directly is_a GO0060205. GO0090114 explicitly describes
    ER membrane evagination; coat GO0030127 is distinct from the lipid bilayer.
  accessed_at: '2026-11-03T13:38:31.997293Z'
  support: supports
  snapshot_sha256: 90e48c2e38afa970a4e8c678a494cca4f043fb2801b9a0cbcebe07442e22965c
- evidence_id: septin-lumen-is-a-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0034467/ancestors?relations=is_a
  locator: GO0034467 ancestors endpoint restricted to relations=is_a
  summary: The returned transitive is_a ancestry includes GO0043233 organelle lumen
    and GO0060205 cytoplasmic vesicle lumen. The maintained broad parent is supported;
    no inference from a mixed part_of/is_a path or false direct-edge claim is needed.
  accessed_at: '2026-11-03T13:42:43.837559Z'
  support: supports
  snapshot_sha256: a94d190b8db0d4ef60e32b7baa06de4a39b6e35558cf388fbfddace78f451d58
- evidence_id: septin-tax4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Exact ENA taxId, scientificName, rank and lineage
  summary: Current species identity is Saccharomyces cerevisiae. This authority check
    does not establish strain, condition, prevalence, localization or biological mechanism.
  accessed_at: '2026-11-03T13:38:31.998360Z'
  support: supports
  snapshot_sha256: d930c884e1154be4c050977652c0d6baf3666d183a90fa17ead8d01cce2c770f
- evidence_id: septin-tax44689
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/44689
  locator: Exact ENA taxId, scientificName, rank and lineage
  summary: Current species identity is Dictyostelium discoideum. This authority check
    does not establish strain, condition, prevalence, localization or biological mechanism.
  accessed_at: '2026-11-03T13:38:32.129912Z'
  support: supports
  snapshot_sha256: f7bfea542a721125d862d08a5f8dd0986c1c19034b45f1fb92adf8c8d045efca
- evidence_id: septin-SL-0108
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0108.json
  locator: Exact UniProt subcellular-location entry and relation-bearing parents
  summary: Direct GO0033118 membrane mapping and esterosomal membrane synonym; is_a
    cytoplasmic vesicle membrane and part_of esterosome. Nested parent mappings are
    not exact identity matches.
  accessed_at: '2026-11-03T13:38:32.794480Z'
  support: supports
  snapshot_sha256: d09af7d2ae5dee175d331abbe865ca6f1c20cd5caceb6d3a85c9a4cd9a7e3c74
- evidence_id: septin-SL-0109
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0109.json
  locator: Exact UniProt subcellular-location entry and relation-bearing parents
  summary: Direct GO0033117 whole-esterosome mapping; is_a cytoplasmic vesicle. Description
    recognizes crystal-filled vesicles and RER-like boundary.
  accessed_at: '2026-11-03T13:38:32.862571Z'
  support: supports
  snapshot_sha256: 07e7e4afc37ebf1072119d97a830dd493ebe66aae619320a676ba90e01d73431
- evidence_id: septin-SL-0328
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0328.json
  locator: Exact UniProt subcellular-location entry and relation-bearing parents
  summary: Direct GO0034467 lumen mapping and esterosomal lumen synonym; is_a cytoplasmic
    vesicle lumen and part_of esterosome. Protein-count fields are not a claim of
    biological absence.
  accessed_at: '2026-11-03T13:38:33.391088Z'
  support: supports
  snapshot_sha256: da3ece8e78de178ff95a2aae89c72a0902b753ad05909f42f48612e0a6ea3373
- evidence_id: septin-barlowe1994-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A8004676%20AND%20SRC%3AMED&pageSize=25
  locator: Complete primary abstract and exact title/authors/year/DOI/PMID metadata
  summary: Barlowe et al.1994, DOI10.1016/0092-8674(94)90138-4. Washed ER membranes
    plus Sar1, Sec13 complex and Sec23 complex produce COPII-coated vesicles; the
    abstract distinguishes GTP from GMP-PNP effects on coat retention and subsequent
    fusion. Supports yeast ER-derived coated-vesicle formation, without auditing full
    methods or figures.
  accessed_at: '2026-11-03T13:38:33.688530Z'
  support: supports
  snapshot_sha256: 5cb877da5722be8060792d7c7e1c653fd91cb3c6e9338675e8e92762a7e2ec3e
  search_scope: Europe PMC exact query EXT_ID:8004676 AND SRC:MED; resultType=core,
    pageSize25, one matched result, no date filter; fetched 2026-11-03T13:38:33.688530Z.
    This is identifier-bounded retrieval, not an exhaustive literature search.
- evidence_id: septin-matsuoka1998-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A9568718%20AND%20SRC%3AMED&pageSize=25
  locator: Complete primary abstract and exact title/authors/year/DOI/PMID metadata
  summary: Matsuoka et al.1998, DOI10.1016/s0092-8674(00)81577-9. Purified Sar1, Sec13/31
    and Sec23/24 reconstitute coat assembly and budding on chemically defined liposomes.
    Phosphoinositide requirements apply to this assay. Synthetic liposome donors do
    not themselves establish native ER lipid composition or an individual lipid requirement
    for every membrane.
  accessed_at: '2026-11-03T13:38:33.735611Z'
  support: supports
  snapshot_sha256: 0cdaf91dc4f4bf9261f55530522a8ed41116b930c39ac656de0d729c318bf1c0
  search_scope: Europe PMC exact query EXT_ID:9568718 AND SRC:MED; resultType=core,
    pageSize25, one matched result, no date filter; fetched 2026-11-03T13:38:33.735611Z.
    This is identifier-bounded retrieval, not an exhaustive literature search.
- evidence_id: septin-bomblies1990-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A2307702%20AND%20SRC%3AMED&pageSize=25
  locator: Complete primary abstract and exact title/authors/year/DOI/PMID metadata
  summary: Bomblies et al.1990, DOI10.1083/jcb.110.3.669, PMC2116030. Complete abstract
    identifies membrane-enclosed Dictyostelium crystals, cryS crystal protein and
    D2 protein, esterase-like sequence similarity, and stage-dependent accumulation.
  accessed_at: '2026-11-03T13:38:33.488098Z'
  support: supports
  snapshot_sha256: 72114827208c9718ab044aa7bce78cf34a35c1067b95dab550d8466039338410
  search_scope: Europe PMC exact query EXT_ID:2307702 AND SRC:MED; resultType=core,
    pageSize25, one matched result, no date filter; fetched 2026-11-03T13:38:33.488098Z.
    This is identifier-bounded retrieval, not an exhaustive literature search.
- evidence_id: septin-bomblies-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2116030.1/PMC2116030.1.xml
  locator: 'Official PMC OA article XML, body preformat pmc-pdf-text: Introduction,
    Methods, Results and Discussion prose; TableI text and Fig1–11 caption text. Scanned-article
    OCR, not newly inspected figure pixels or sequence-alignment panels.'
  summary: 'Fresh genuine article OCR supports AX2-214/AX3 Dictyostelium experiments:
    purified crystals contain major69kD crystal protein and56kD D2, N-terminal/cDNA
    identification and antibodies label the same membrane-enclosed crystals in serial
    and double-gold sections. The paper explicitly places the proteins in the lumen
    rather than in the membrane. Ribosome-decorated boundary morphology is RER-like.
    Cofractionation and immunolabeling suggest co-crystallization but exact composition/ratio
    requires further recrystallization work. ER sorting, nucleation, physiological
    function and crystal fate remain hypotheses, and individual formation necessity
    is not demonstrated. Expression experiments are condition/strain specific; most
    work AX2, Fig11B cAMP transcripts AX3.'
  accessed_at: '2026-11-03T13:38:31.998181Z'
  support: supports
  snapshot_sha256: 1463d650050255ec3716b375b43bfd3fc988d082575e95c5a035034085846b3c
- evidence_id: septin-bomblies-pmc
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2116030/
  locator: Canonical PMC article URL returned an HTML recaptcha challenge despite
    HTTP200
  summary: Access diagnostic only; these bytes are not article evidence. Genuine article
    prose was separately retrieved from the official PMC OA XML endpoint, whose DOI/PMID
    identity was verified.
  accessed_at: '2026-11-03T13:38:31.998084Z'
  support: context_only
  snapshot_sha256: 8cea782aa56126352fcebec1558e1fef41287383a973e898cfd14af82645978e
- evidence_id: septin-protein-P21837
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P21837.json
  locator: Exact reviewed accession, recommended protein label, gene, organism, sequence-family
    similarity and location comments
  summary: Current reviewed Crystal protein accession matches cryS and NCBITaxon44689.
    Location annotation uses SL0108 membrane with a membrane-enclosed-crystal note;
    this annotation granularity is not primary proof that the protein is a bilayer
    constituent. The original paper explicitly supports lumenal crystal cargo. Type-B
    carboxylesterase/lipase similarity does not alone establish esterosome membership,
    catalysis or necessity.
  accessed_at: '2026-11-03T13:38:32.177266Z'
  support: supports
  snapshot_sha256: 6257114009b0abe20bee2d48f9242b16a8bc57316a58f8745bbe8c617f32c45b
- evidence_id: septin-protein-P18142
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P18142.json
  locator: Exact reviewed accession, recommended protein label, gene, organism, sequence-family
    similarity and location comments
  summary: Current reviewed cAMP-regulated D2 protein accession matches D2 and NCBITaxon44689.
    Location annotation uses SL0108 membrane with a membrane-enclosed-crystal note;
    this annotation granularity is not primary proof that the protein is a bilayer
    constituent. The original paper explicitly supports lumenal crystal cargo. Type-B
    carboxylesterase/lipase similarity does not alone establish esterosome membership,
    catalysis or necessity.
  accessed_at: '2026-11-03T13:38:32.787441Z'
  support: supports
  snapshot_sha256: ff367a9f99e92972c09afa1c92d0972bf3d7cbb77c51460d370a1599b21763bb
- evidence_id: septin-interpro-P21837
  kind: search
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P21837/?page_size=100
  locator: Complete four-result exact-protein integrated InterPro response; metadata.type
    and member databases
  summary: Returned IPR002018 is typed domain (member PF00135), IPR019819 conserved_site,
    IPR019826 active_site and IPR029058 homologous_superfamily. No integrated family-typed
    entry occurs in this complete exact-protein response. Under the native family-consensus
    policy these domain/site/superfamily entries do not establish an exact family-grounding
    correction. This bounded result does not prove that no ontology can ever supply
    a suitable class.
  accessed_at: '2026-11-03T13:38:32.497380Z'
  support: supports
  snapshot_sha256: f2e4bbb331fbb49cac0cc26c3c333bc4cfd318e4d0f57444a620e766a5105065
  search_scope: Official InterPro exact UniProt accession P21837 lookup, /entry/interpro/protein/uniprot/P21837/?page_size=100,
    four results, next=null, no taxon substitution or date filter; actual access 2026-11-03T13:38:32.497380Z.
    All returned integrated entry metadata/types independently inspected; no ontology-wide
    absence inference.
- evidence_id: septin-interpro-P18142
  kind: search
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P18142/?page_size=100
  locator: Complete four-result exact-protein integrated InterPro response; metadata.type
    and member databases
  summary: Returned IPR002018 is typed domain (member PF00135), IPR019819 conserved_site,
    IPR019826 active_site and IPR029058 homologous_superfamily. No integrated family-typed
    entry occurs in this complete exact-protein response. Under the native family-consensus
    policy these domain/site/superfamily entries do not establish an exact family-grounding
    correction. This bounded result does not prove that no ontology can ever supply
    a suitable class.
  accessed_at: '2026-11-03T13:38:32.789562Z'
  support: supports
  snapshot_sha256: 2c9d2dbe57f8683b5a1cb1ff39d82ac5920919411576b940ac190908912319d2
  search_scope: Official InterPro exact UniProt accession P18142 lookup, /entry/interpro/protein/uniprot/P18142/?page_size=100,
    four results, next=null, no taxon substitution or date filter; actual access 2026-11-03T13:38:32.789562Z.
    All returned integrated entry metadata/types independently inspected; no ontology-wide
    absence inference.
- evidence_id: septin-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Complete official returned organism and dataset catalogue; actual target
    taxa and keys
  summary: No matched Saccharomyces cerevisiae or Dictyostelium discoideum organism/dataset
    is returned. ER-to-Golgi membrane asserts named COPII machinery; whole esterosome
    and its lumen assert cryS/crystal protein and D2 context. Their applicability
    was assessed, but no matched-host downstream gene/module query is justified. The
    esterosome membrane has genuine material/topological scope. Noncoverage is not
    negative biological evidence.
  accessed_at: '2026-11-03T13:38:31.997771Z'
  support: supports
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: Official GET /api/datasets at 2026-11-03T13:38:31.997771Z; complete
    returned catalogue searched for Saccharomyces/cerevisiae/yeast and Dictyostelium/discoideum
    across organism names, IDs and dataset keys, no date filter. No unrelated-host
    proxy or downstream gene/module query. No global count is claimed.
- evidence_id: septin-historical-adapter-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Actual historical datasets invocation00:49:00.848907Z–00:49:00.863225Z
  summary: Historical canary command exited1 with PermissionError reading pyvenv.cfg.
    This is a retained earlier unavailable-runner observation, not a fresh invocation
    or success. The present catalogue fallback is a distinct actual source retrieval.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: septin-source-access
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/adversary-septin/source-receipts.json
  locator: Actual fresh URLs, access timestamps and hashes
  summary: Current authorities, catalogue, exact-protein InterPro and three primary
    abstract responses were freshly fetched. Genuine Bomblies article OCR came from
    official PMC OA XML; canonical PMC HTML was a bot challenge. Barlowe/Matsuoka
    are complete-primary-abstract tiers only, with no full-body access claim.
  accessed_at: '2026-11-03T13:44:45.663261Z'
  support: supports
  snapshot_sha256: 29fcba71635a9ee70fe0f7f61ed954fa9287c8e2cc3a94b3264a2c98b1c0813c
- evidence_id: septin-common-policy-reuse
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/adversary-septin/common-policy-hash-reuse.json
  locator: Seventeen previously read common policy/schema/native inputs checked against
    current freeze
  summary: Current common input bytes match the prior read versions. Component-grounding
    and native family-consensus guidance additionally reread. No extra repository
    neighbor, prior category review or unfrozen script was used.
  accessed_at: '2026-11-03T13:44:45.663261Z'
  support: supports
  snapshot_sha256: 97ffdac706b5dab06418690bf4bb0688ca8fa50f42f0c17b1bdd5c804f2c6161
- evidence_id: check-qc
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/qc.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T13:43:45.440682Z'
  support: supports
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  snapshot_sha256: b367065026807b63ad6eac32f115a4e71166ed33ec8f58535a148186ae82ef76
- evidence_id: check-labels
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/labels.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T13:38:32.288404Z'
  support: supports
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  snapshot_sha256: 6cdfb05df9a27194f05a5fd7f851783f817ac1523ca0bbfa54fe0e0d18775905
- evidence_id: check-trait-links
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/trait-links.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T13:38:09.008714Z'
  support: supports
  summary: Native TraitMech link check passed.
  snapshot_sha256: 8b336cdefbbd3daf6da8787990efdbe346c95e2c8361d50b7eb68a18f2d5a44a
- evidence_id: check-vendored
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/vendored.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T13:38:04.311566Z'
  support: supports
  summary: Pinned governed files match; native vendored check passed.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: check-curies
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/curies.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T13:38:08.782798Z'
  support: supports
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  snapshot_sha256: bc12b1285f5747707643f7a98e03dbb3a6c88fb062ad49f99db9cb42ececf3d2
- evidence_id: focused
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/focused-results.json
  locator: All twenty actual target schema/strict command outputs
  accessed_at: '2026-11-03T13:48:37Z'
  support: supports
  summary: Ten schema and ten strict commands returned exit zero.
  snapshot_sha256: b6a735dfb5b7352d26d66b0eba67c745803eb9f2a47faac6550fcf68809afe9a
- evidence_id: supplemental-pmid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2365/pmid-chunks-receipt.json
  locator: Complete native-report PMID set checked with unchanged resolver in batches
    of at most fifty
  accessed_at: '2026-11-03T13:39:29.530167Z'
  support: supports
  summary: 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers
    remain unverified.
  snapshot_sha256: dba9df7c57cbe5b9e2522a8647dd85bf91a976e39c0ccec8ec19584ee09c9a01
- evidence_id: historical-adapter-runner-availability
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner invocation receipt, exact SHA256 reverified during PR2365
    synthesis
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS
    PermissionError reading the configured runner pyvenv.cfg. This is a retained historical
    availability observation, not a fresh attempt or a scientific validation failure.
    Native policy permits inspected source-catalogue fallback.
assessments:
- assessment_id: plaque-t0-native
  area: schema
  topic: Represented protein inventory and graph actor coverage
  outcome: supported
  summary: No component protein_examples and zero GENE_OR_PROTEIN nodes in the complete
    current target; mechanical checks are empty-inventory scope. Both commands return0.
    Actual source identity/localization and narrative pathway scope are separately
    reviewed.
  target_ids:
  - GO:0031904
  evidence_ids:
  - plaque-current-0
  - plaque-native-endosome_lumen-verify
  - plaque-native-endosome_lumen-causal
  - plaque-protein-contract
- assessment_id: plaque-t0-provenance
  area: provenance
  topic: Original immutable pair and frozen-input currentness
  outcome: supported
  summary: Current target unchanged; original pair validates/renders and all 18 historical
    inputs match their source commit. No stale refresh or record correction claimed.
    Exact two EpM finding predecessors are preserved, without terminally resolving
    other historical issues.
  target_ids:
  - GO:0031904
  evidence_ids:
  - plaque-current-0
  - plaque-original-0
  - plaque-original-checks
- assessment_id: plaque-t0-coverage
  area: completeness
  topic: Complete current fields and optional inventories
  outcome: supported
  summary: Whole maintained target, history, evidence, discussions and graph arrays
    read. No target image assets, verbatim snippets, trait links or quantitative properties
    to audit. No optional molecular inventory or guessed family/chemical identifier
    is manufactured. PROPOSED unchanged.
  target_ids:
  - GO:0031904
  evidence_ids:
  - plaque-current-0
  - plaque-rubric
  - plaque-original-checks
- assessment_id: plaque-t1-native
  area: schema
  topic: Represented protein inventory and graph actor coverage
  outcome: supported
  summary: No component protein_examples; one GENE_OR_PROTEIN node is UNANCHORED_WITH_UNIPROT,
    carrying verified P40343 for external Vps27. This is permitted and does not require
    a fabricated component. Both commands return0. Actual source identity/localization
    and narrative pathway scope are separately reviewed.
  target_ids:
  - GO:0010008
  evidence_ids:
  - plaque-current-1
  - plaque-native-endosome_membrane-verify
  - plaque-native-endosome_membrane-causal
  - plaque-protein-contract
- assessment_id: plaque-t1-provenance
  area: provenance
  topic: Original immutable pair and frozen-input currentness
  outcome: supported
  summary: Current target unchanged; original pair validates/renders and all 17 historical
    inputs match their source commit. No stale refresh or record correction claimed.
    Exact two EpM finding predecessors are preserved, without terminally resolving
    other historical issues.
  target_ids:
  - GO:0010008
  evidence_ids:
  - plaque-current-1
  - plaque-original-1
  - plaque-original-checks
- assessment_id: plaque-t1-coverage
  area: completeness
  topic: Complete current fields and optional inventories
  outcome: supported
  summary: Whole maintained target, history, evidence, discussions and graph arrays
    read. No target image assets, verbatim snippets, trait links or quantitative properties
    to audit. No optional molecular inventory or guessed family/chemical identifier
    is manufactured. PROPOSED unchanged.
  target_ids:
  - GO:0010008
  evidence_ids:
  - plaque-current-1
  - plaque-rubric
  - plaque-original-checks
- assessment_id: plaque-t2-native
  area: schema
  topic: Represented protein inventory and graph actor coverage
  outcome: supported
  summary: No component protein_examples and zero GENE_OR_PROTEIN nodes in the complete
    current target; mechanical checks are empty-inventory scope. Both commands return0.
    Actual source identity/localization and narrative pathway scope are separately
    reviewed.
  target_ids:
  - GO:7770040
  evidence_ids:
  - plaque-current-2
  - plaque-native-epiplastidial_membrane-verify
  - plaque-native-epiplastidial_membrane-causal
  - plaque-protein-contract
- assessment_id: plaque-t2-provenance
  area: provenance
  topic: Original immutable pair and frozen-input currentness
  outcome: supported
  summary: Current target unchanged; original pair validates/renders and all 14 historical
    inputs match their source commit. No stale refresh or record correction claimed.
    Exact two EpM finding predecessors are preserved, without terminally resolving
    other historical issues.
  target_ids:
  - GO:7770040
  evidence_ids:
  - plaque-current-2
  - plaque-original-2
  - plaque-original-checks
- assessment_id: plaque-t2-coverage
  area: completeness
  topic: Complete current fields and optional inventories
  outcome: supported
  summary: Whole maintained target, history, evidence, discussions and graph arrays
    read. No target image assets, verbatim snippets, trait links or quantitative properties
    to audit. No optional molecular inventory or guessed family/chemical identifier
    is manufactured. PROPOSED unchanged.
  target_ids:
  - GO:7770040
  evidence_ids:
  - plaque-current-2
  - plaque-rubric
  - plaque-original-checks
- assessment_id: plaque-t0-identity
  area: identity
  topic: Lumen versus membrane and MVB specialization
  outcome: supported
  summary: Exact GO target definition and kind agree; lumen and limiting membrane
    are distinct parts of endosome. MVB lumen is a specialized endosome lumen and
    local ILV denotes a whole internal vesicle. Supported specialized MVB context
    does not assert that every endosome contains ILVs.
  target_ids:
  - GO:0031904
  evidence_ids:
  - plaque-current-0
  - plaque-go
  - plaque-sl0340
  - plaque-neighbor-mvb-lumen
  - plaque-neighbor-ilv
  - plaque-schema-policy
- assessment_id: plaque-t0-taxonomy
  area: scope
  topic: Yeast species and experimental strains
  outcome: supported
  summary: NCBITaxon4932 is S. cerevisiae. Primary abstract/body evidence supports
    the yeast MVB context. COMMON is qualitative, not measured prevalence. Katzmann2003
    uses SEY6210 derivatives; P40343 S288C identity is a reference-strain accession,
    not a claim the experiments used S288C.
  target_ids:
  - GO:0031904
  evidence_ids:
  - plaque-current-0
  - plaque-tax4932
  - plaque-tax559292
  - plaque-katzmann2001-meta
  - plaque-katzmann2003-pmc
  - plaque-protein-P40343
- assessment_id: plaque-t0-function
  area: evidence
  topic: Scoped ubiquitin-dependent MVB cargo sorting
  outcome: supported
  summary: GO0071985, Katzmann2001 complete abstract and Katzmann2003 body support
    ubiquitinated membrane cargo entry into MVB internal vesicles. Henne is a secondary
    review, not an additional primary assay. The narrow function is not silently extended
    to every endosomal sorting route or universal molecular sequence.
  target_ids:
  - GO:0031904
  evidence_ids:
  - plaque-current-0
  - plaque-go
  - plaque-katzmann2001-meta
  - plaque-katzmann2003-pmc
  - plaque-henne2011-meta
- assessment_id: plaque-t0-adapter
  area: scope
  topic: Actual pathway trigger and catalogue noncoverage
  outcome: supported
  summary: ESCRT-dependent MVB sorting is an explicit pathway assertion; membrane
    also names VPS27/P40343. The original check explicitly excludes iModulonDB for
    lack of expression inference, without coverage evidence. Current complete catalogue
    has no relevant yeast host, so no matched downstream query applies. Primary/authority
    fallback is completed; historical runner remains separately dated unavailable.
  target_ids:
  - GO:0031904
  evidence_ids:
  - plaque-current-0
  - plaque-original-0
  - plaque-policy
  - plaque-catalogue
  - plaque-historical-runner
  - plaque-katzmann2001-meta
  - plaque-katzmann2003-pmc
- assessment_id: plaque-t1-identity
  area: identity
  topic: Lumen versus membrane and MVB specialization
  outcome: supported
  summary: Exact GO target definition and kind agree; lumen and limiting membrane
    are distinct parts of endosome. MVB lumen is a specialized endosome lumen and
    local ILV denotes a whole internal vesicle. Supported specialized MVB context
    does not assert that every endosome contains ILVs.
  target_ids:
  - GO:0010008
  evidence_ids:
  - plaque-current-1
  - plaque-go
  - plaque-sl0340
  - plaque-neighbor-mvb-lumen
  - plaque-neighbor-ilv
  - plaque-schema-policy
- assessment_id: plaque-t1-taxonomy
  area: scope
  topic: Yeast species and experimental strains
  outcome: supported
  summary: NCBITaxon4932 is S. cerevisiae. Primary abstract/body evidence supports
    the yeast MVB context. COMMON is qualitative, not measured prevalence. Katzmann2003
    uses SEY6210 derivatives; P40343 S288C identity is a reference-strain accession,
    not a claim the experiments used S288C.
  target_ids:
  - GO:0010008
  evidence_ids:
  - plaque-current-1
  - plaque-tax4932
  - plaque-tax559292
  - plaque-katzmann2001-meta
  - plaque-katzmann2003-pmc
  - plaque-protein-P40343
- assessment_id: plaque-t1-function
  area: evidence
  topic: Scoped ubiquitin-dependent MVB cargo sorting
  outcome: supported
  summary: GO0071985, Katzmann2001 complete abstract and Katzmann2003 body support
    ubiquitinated membrane cargo entry into MVB internal vesicles. Henne is a secondary
    review, not an additional primary assay. The narrow function is not silently extended
    to every endosomal sorting route or universal molecular sequence.
  target_ids:
  - GO:0010008
  evidence_ids:
  - plaque-current-1
  - plaque-go
  - plaque-katzmann2001-meta
  - plaque-katzmann2003-pmc
  - plaque-henne2011-meta
- assessment_id: plaque-t1-adapter
  area: scope
  topic: Actual pathway trigger and catalogue noncoverage
  outcome: supported
  summary: ESCRT-dependent MVB sorting is an explicit pathway assertion; membrane
    also names VPS27/P40343. The original check explicitly excludes iModulonDB for
    lack of expression inference, without coverage evidence. Current complete catalogue
    has no relevant yeast host, so no matched downstream query applies. Primary/authority
    fallback is completed; historical runner remains separately dated unavailable.
  target_ids:
  - GO:0010008
  evidence_ids:
  - plaque-current-1
  - plaque-original-1
  - plaque-policy
  - plaque-catalogue
  - plaque-historical-runner
  - plaque-katzmann2001-meta
  - plaque-katzmann2003-pmc
- assessment_id: plaque-t0-composition
  area: grounding
  topic: Lumen as an internal region
  outcome: supported
  summary: Empty constituent inventory is appropriate for the internal region. Enclosing
    membrane and ILVs are represented as boundary/content graph entities, not falsely
    made constitutive lipid/protein components of the lumen. Resolved local discussion
    agrees with actual membrane boundary node.
  target_ids:
  - GO:0031904
  evidence_ids:
  - plaque-current-0
  - plaque-go
  - plaque-sl0340
  - plaque-neighbor-mvb-lumen
- assessment_id: plaque-t0-graph
  area: graph
  topic: All five NONMECHANISTIC topology edges
  outcome: supported
  summary: Lumen part_of endosome, MVB lumen is_a endosome lumen, endosome membrane
    bounds lumen, MVB is_a endosome, and ILV contained in MVB lumen are supported.
    Full ESCRT reaction or mandatory universal ILVs are not claimed.
  target_ids:
  - GO:0031904
  evidence_ids:
  - plaque-current-0
  - plaque-go
  - plaque-sl0340
  - plaque-neighbor-ilv
- assessment_id: plaque-t0-limits
  area: evidence
  topic: Beyond the scoped lumen topology
  outcome: unknown
  summary: Detailed scission chemistry, exhaustive lumen cargo composition and primary2001
    full-body experimental detail are not independently established by this bounded
    review.
  target_ids:
  - GO:0031904
  evidence_ids:
  - plaque-current-0
  - plaque-katzmann2001-meta
  - plaque-henne2011-meta
- assessment_id: plaque-t1-composition
  area: grounding
  topic: Collective lipid and transient external actors
  outcome: supported
  summary: Generic lipid-bilayer constituent is REVIEWED_LABEL_ONLY with an explicit
    unresolved chemical grounding discussion; ESSENTIAL is collective defining constitution,
    not individual-lipid knockout necessity. Vps27/ESCRT actors remain graph nodes
    rather than invented stable membrane constituents. P40343 matches VPS27.
  target_ids:
  - GO:0010008
  evidence_ids:
  - plaque-current-1
  - plaque-go
  - plaque-protein-contract
  - plaque-protein-P40343
- assessment_id: plaque-t1-graph
  area: graph
  topic: All seven scoped membrane-topology and sorting edges
  outcome: supported
  summary: Parthood/enclosure and ILV formation/containment agree with authority definitions.
    Katzmann2003 supports Vps27 recruiting ESCRT-I; Katzmann2001 supports cargo sorting.
    Babst2002 abstract supports ESCRT-III membrane recruitment/oligomerization/sorting;
    Henne review and modern GO support broad membrane remodeling. NONMECHANISTIC scope
    does not assert precise scission chemistry or the full ESCRT cycle.
  target_ids:
  - GO:0010008
  evidence_ids:
  - plaque-current-1
  - plaque-go
  - plaque-katzmann2001-meta
  - plaque-katzmann2003-pmc
  - plaque-babst2002-meta
  - plaque-henne2011-meta
- assessment_id: plaque-t1-limits
  area: evidence
  topic: Molecular necessity and scission detail
  outcome: unknown
  summary: Exact lipid composition, necessity of every constituent and detailed ESCRT
    scission chemistry are outside the inspected evidence. The mechanical verifier
    and generic bilayer ESSENTIAL row do not establish those claims.
  target_ids:
  - GO:0010008
  evidence_ids:
  - plaque-current-1
  - plaque-rubric
  - plaque-babst2002-meta
  - plaque-henne2011-meta
- assessment_id: plaque-t2-identity
  area: identity
  topic: Exact outermost complex-plastid membrane
  outcome: supported
  summary: GO7770040 exactly matches definition and five synonyms; plastid-membrane
    parentage and plastid parthood are supported. EpM/cERM is distinct from second-outer
    PPM7770041 and plastid-envelope outer membrane0009527. Native definition reproduced
    accurately; primary sources qualify diatom ER continuity and discuss other lineage
    differences.
  target_ids:
  - GO:7770040
  evidence_ids:
  - plaque-current-2
  - plaque-go
  - plaque-neighbor-ppm
  - plaque-flori2016-oceanomics-pdf
- assessment_id: plaque-t2-taxonomy
  area: scope
  topic: Diatom primary imaging context
  outcome: supported
  summary: Taxon2850 is P. tricornutum. Flori2016 Pt1 CCAP1055/3 FIB-SEM supports
    canonical ultrastructure; intact/disrupted cells are distinguished. Gueguen2024
    uses Pt1 Strain8.6 CCAP1055/1. COMMON remains qualitative; distinct culture-collection
    designations are not silently equated.
  target_ids:
  - GO:7770040
  evidence_ids:
  - plaque-current-2
  - plaque-tax2850
  - plaque-flori2016-oceanomics-pdf
  - plaque-gueguen2024-jats
- assessment_id: plaque-t2-composition
  area: grounding
  topic: Unspecified collective epiplastidial lipid bilayer
  outcome: supported
  summary: The generic LIPID row is defining collective bilayer material, intentionally
    REVIEWED_LABEL_ONLY. Exact mixture/individual lipid necessity is not asserted.
    Gueguen source title names MGD enzymes but the record does not positively assert
    specific enzymes, transport machinery or stress-response pathways.
  target_ids:
  - GO:7770040
  evidence_ids:
  - plaque-current-2
  - plaque-go
  - plaque-flori2016-oceanomics-pdf
  - plaque-gueguen2024-jats
  - plaque-rubric
- assessment_id: plaque-t2-function
  area: evidence
  topic: Immediate membrane interface versus nested enclosure
  outcome: concern
  summary: The function says EpM separates PPC from the host endomembrane system.
    Primary topology places the PPC between PPM and oEM, and EpM is itself continuous
    with host ER/outer nuclear membrane. An outer membrane can indirectly enclose
    PPC, so the wording is not treated as a proven false enclosure claim; it needs
    the adjacent spaces specified to avoid attributing the PPM interface to EpM.
  target_ids:
  - GO:7770040
  evidence_ids:
  - plaque-current-2
  - plaque-go
  - plaque-flori2016-oceanomics-pdf
  - plaque-gueguen2024-jats
  - plaque-neighbor-ppm
- assessment_id: plaque-t2-graph
  area: graph
  topic: Descriptive bilayer forms boundary graph
  outcome: concern
  summary: The graph consists of collective bilayer formation of the named membrane
    and outer-boundary maintenance. These relations describe identity and topology;
    the cited sources do not establish a molecular causal sequence represented by
    the current nodes and edges.
  target_ids:
  - GO:7770040
  evidence_ids:
  - plaque-current-2
  - plaque-graph-rubric
  - plaque-go
  - plaque-flori2016-oceanomics-pdf
- assessment_id: plaque-t2-adapter
  area: scope
  topic: Genuine material/topology exclusion
  outcome: not_applicable
  summary: Complete maintained record asserts lipid constitution, nested compartment
    boundaries, host-derived origin and ER continuity, without a positive gene/regulator/pathway/stress/transcriptomic
    assertion. Merely citing the MGD paper title does not import all its molecular
    claims into the record. This is a genuine scope exclusion, not an additional adapter
    defect; fresh catalogue also has no P. tricornutum match.
  target_ids:
  - GO:7770040
  evidence_ids:
  - plaque-current-2
  - plaque-policy
  - plaque-catalogue
  - plaque-gueguen2024-jats
- assessment_id: plaque-t2-limits
  area: evidence
  topic: Specific lipid necessity and evolutionary scope
  outcome: unknown
  summary: Exact lipid pools/formation necessities and molecular maintenance mechanism
    remain unresolved. MGDgamma localization in ER/periphery is qualified; no exact
    EpM composition is inferred. Diatom ER continuity is not extrapolated to all secondary-plastid
    lineages, and source evolutionary alternatives remain hypotheses.
  target_ids:
  - GO:7770040
  evidence_ids:
  - plaque-current-2
  - plaque-flori2016-oceanomics-pdf
  - plaque-gueguen2024-jats
  - plaque-hashimoto2005-meta
- assessment_id: micro-exoneme-identity
  area: identity
  topic: Exoneme organelle and apical-complex relation
  outcome: supported
  target_ids:
  - GO:0044311
  summary: The native class/parent/parthood match. The maintained functions correctly
    describe discharge of soluble protease cargo into PV rather than assuming an entire
    stable organelle is released intact; full-record interpretation preserves this
    distinction.
  evidence_ids:
  - micro-record-exoneme
  - micro-exo-go
  - micro-exo-yeoh2007-meta
  - micro-exo-blackman2008-jats
  - micro-exo-nasamu2017-jats
- assessment_id: micro-exoneme-scope
  area: scope
  topic: P. falciparum blood-stage evidence
  outcome: supported
  target_ids:
  - GO:0044311
  summary: The directly evidenced species, schizont/merozoite stages and canonical
    discharge/egress example match the primary abstract and later primary main text.
    COMMON is qualitative occurrence, not a counted frequency or all-apicomplexan
    claim. The record explicitly narrowed broader historical taxonomy.
  evidence_ids:
  - micro-record-exoneme
  - micro-exo-yeoh2007-meta
  - micro-exo-nasamu2017-jats
  - micro-exo-tax5833
  - micro-exo-tax36329
- assessment_id: micro-exoneme-membership
  area: grounding
  topic: SUB1 and PMX components versus representative identity metadata
  outcome: supported
  target_ids:
  - GO:0044311
  summary: Primary literature supports PfSUB1 exoneme cargo and PMX localization/dependence.
    Native examples and graph xrefs identify the exact species/isolate proteins and
    SERA5/MSP1 exemplars; xrefs do not equate the entire substrate cohort with just
    those two proteins. Native by-similarity annotations and historical dense-granule
    descriptions are not counted as independent direct exoneme experiments.
  evidence_ids:
  - micro-record-exoneme
  - micro-policy
  - micro-exo-yeoh2007-meta
  - micro-exo-blackman1998-meta
  - micro-exo-blackman2008-jats
  - micro-exo-nasamu2017-jats
  - micro-exo-O61142
  - micro-exo-Q8IAS0
  - micro-exo-Q9TY95
  - micro-exo-Q8I0U8
  - micro-exo-sub1-query
  - micro-exo-pmx-query
- assessment_id: micro-exoneme-family
  area: grounding
  topic: Resolvable SUB1 family and unresolved exact PMX family
  outcome: concern
  target_ids:
  - GO:0044311
  summary: IPR017314 is a verified whole-SUB1 family and O61142 directly carries it.
    The component’s unresolved-family rationale is stale for SUB1. IPR034204 is a
    domain and IPR001461 is broader than PMX, so neither is forced as an exact substitute
    for the remaining component.
  evidence_ids:
  - micro-record-exoneme
  - micro-policy
  - micro-exo-IPR017314
  - micro-exo-IPR034204
  - micro-exo-IPR001461
  - micro-exo-O61142
  - micro-exo-Q8IAS0
- assessment_id: micro-exoneme-necessity
  area: grounding
  topic: Protease activity requirement versus organelle formation
  outcome: unknown
  target_ids:
  - GO:0044311
  summary: The studies establish important protease maturation, egress and invasion
    effects, but do not establish that loss of each cargo enzyme prevents formation
    of the exoneme compartment. Both UNKNOWN assembly-necessity entries are appropriate;
    catalytic essentiality is not silently converted to organelle-assembly necessity.
  evidence_ids:
  - micro-record-exoneme
  - micro-policy
  - micro-exo-yeoh2007-meta
  - micro-exo-nasamu2017-jats
- assessment_id: micro-exoneme-function-graph
  area: graph
  topic: Eight qualified egress pathway edges
  outcome: supported
  target_ids:
  - GO:0044311
  summary: Localization/storage, discharge into PV, PMX-supported SUB1 processing,
    downstream SERA/MSP processing and contributions to egress/invasion are supported
    at the stated evidence tiers. Nasamu directly supports the dependence, while its
    in-vivo direct-cleavage uncertainty is preserved by “supports maturation.” Withers
    provides reviewed background for discharge and substrate processing inside a primary
    structural paper, not an independent new discharge experiment. This graph represents
    a causal proteolytic sequence and its MECHANISTIC classification is justified
    within those limits.
  evidence_ids:
  - micro-record-exoneme
  - micro-exo-yeoh2007-meta
  - micro-exo-blackman2008-jats
  - micro-exo-withers2014-jats
  - micro-exo-nasamu2017-jats
  - micro-exo-Q9TY95
  - micro-exo-Q8I0U8
- assessment_id: micro-exoneme-coverage
  area: completeness
  topic: Full maintained record and bounded scientific coverage
  outcome: supported
  target_ids:
  - GO:0044311
  summary: Every maintained claim, graph edge and discussion was inspected. No quantitative
    physical-property field, maintained image/licence asset or verbatim evidence snippet
    is present. Existing PROPOSED status and history remain unchanged. No finding
    is invented from optional unresolved molecular inventory or unavailable full-text
    routes alone.
  evidence_ids:
  - micro-record-exoneme
  - micro-policy
- assessment_id: micro-exoneme-schema
  area: schema
  topic: Immutable original and current native coverage
  outcome: supported
  summary: Original validates/renders identically and historical frozen input verified.
    Current root native protein commands exit0 with actual inventory limits; no scientific
    inference from status alone.
  target_ids:
  - GO:0044311
  evidence_ids:
  - micro-original-pairs
  - micro-prior-exoneme
  - micro-native-exoneme-verify
  - micro-native-exoneme-causal
- assessment_id: micro-exoneme-adapter
  area: evidence
  topic: Molecular/pathway applicability and exact catalogue coverage
  outcome: not_applicable
  summary: 'Existing expression-only N/A rationale is deficient: this target asserts
    named proteins/pathways. Fresh official catalogue has no target organism/strain
    match; no downstream module keys or unmatched proxy invented. Historical runner
    unavailability is separately dated; this is a bounded source applicability result,
    not biological negative evidence.'
  target_ids:
  - GO:0044311
  evidence_ids:
  - micro-record-exoneme
  - micro-prior-exoneme
  - micro-policy
  - micro-historical-runner
  - micro-catalogue
- assessment_id: micro-eyespot_apparatus-identity
  area: identity
  topic: Eyespot apparatus across membrane systems
  outcome: supported
  target_ids:
  - GO:1990413
  summary: 'Exact GO1990413 definition and two RELATED synonyms agree. OTHER kind
    avoids misrepresenting the apparatus as one isolated membrane-bounded compartment:
    original sources place plasma-membrane photoreceptors over chloroplast-associated
    pigment granules. An empty optional parent/parthood slot is not an identity defect.'
  evidence_ids:
  - micro-record-eyespot_apparatus
  - micro-eye-go
  - micro-policy
  - micro-eye-lamb1999-meta
  - micro-eye-schmidt2006-pmc
  - micro-eye-mittelmeier2011-pmc
  - micro-eye-awasthi2016-pmc
  - micro-eye-ueki2016-pmc
- assessment_id: micro-eyespot_apparatus-scope
  area: scope
  topic: Chlamydomonas scope and study contexts
  outcome: supported
  target_ids:
  - GO:1990413
  summary: Species3055 label and canonical/distribution scope agree. Lamb full abstract
    supports assembly/positioning mutant context; Schmidt cw15 fraction purification
    supports proteomics example. Mittelmeier uses137c/CC125 and specific mutants;
    Awasthi uses conditional IFT strains. COMMON is qualitative occurrence, not a
    prevalence count or all-algae claim.
  evidence_ids:
  - micro-record-eyespot_apparatus
  - micro-eye-tax3055
  - micro-eye-lamb1999-meta
  - micro-eye-schmidt2006-meta
  - micro-eye-mittelmeier2011-meta
  - micro-eye-awasthi2016-meta
  - micro-eye-ueki2016-meta
  - micro-eye-schmidt2006-pmc
  - micro-eye-mittelmeier2011-pmc
  - micro-eye-awasthi2016-pmc
  - micro-eye-ueki2016-pmc
- assessment_id: micro-eyespot_apparatus-composition
  area: grounding
  topic: Pigment and photoreceptor cohorts
  outcome: supported
  target_ids:
  - GO:1990413
  summary: Current Q8RUT8/cop4 and newly added Q93WP2/acop1 are unreviewed tax3055
    examples. Schmidt Table1 bridges COP3/CHOP1/CSRA/Acop1 and COP4/CHOP2/CSRB/Acop2;
    primary fraction peptides support the represented cohort, with contamination limits.
    Empty literal COP3 query does not contradict the literature alias. Broad IPR001425
    opsin family does not exactly resolve the channelrhodopsin cohort.
  evidence_ids:
  - micro-record-eyespot_apparatus
  - micro-eye-go
  - micro-protein-contract
  - micro-eye-protein-Q8RUT8
  - micro-eye-query-COP3-true
  - micro-eye-query-COP3-false
  - micro-eye-query-COP4-true
  - micro-eye-query-COP4-false
  - micro-eye-schmidt2006-pmc
  - micro-eye-mittelmeier2011-pmc
  - micro-eye-awasthi2016-pmc
  - micro-eye-ueki2016-pmc
  - micro-eye-Q93WP2
- assessment_id: micro-eyespot_apparatus-source-placement
  area: evidence
  topic: Plural cohort versus directly imaged member
  outcome: supported
  target_ids:
  - GO:1990413
  summary: Mittelmeier directly localizes ChR1; Awasthi provides ChR1/Cop8 trafficking
    and background COP3/4 identity. The already cited record-level Schmidt paper detects
    both COP3 and COP4, preserving support for the plural cohort. The review does
    not claim a direct ChR2 localization experiment in the first two papers or transfer
    all IFT controls to ChR2.
  evidence_ids:
  - micro-record-eyespot_apparatus
  - micro-eye-schmidt2006-pmc
  - micro-eye-mittelmeier2011-pmc
  - micro-eye-awasthi2016-pmc
  - micro-eye-ueki2016-pmc
  - micro-eye-lamb1999-meta
  - micro-eye-schmidt2006-meta
  - micro-eye-mittelmeier2011-meta
  - micro-eye-awasthi2016-meta
  - micro-eye-ueki2016-meta
- assessment_id: micro-eyespot_apparatus-function
  area: evidence
  topic: Shielding and directional phototactic sign
  outcome: supported
  target_ids:
  - GO:1990413
  summary: Ueki mutant/rescue, redox-biased assays and directly observed cellular
    lens effect support carotenoid-layer shielding and correct phototactic sign. Eyeless
    cells can retain photoreception and show strong responses under the tested conditions;
    the target uses supports/directional detection and UNKNOWN essentiality, rather
    than claiming all phototaxis requires a pigmented eyespot.
  evidence_ids:
  - micro-record-eyespot_apparatus
  - micro-eye-ueki2016-meta
  - micro-eye-schmidt2006-pmc
  - micro-eye-mittelmeier2011-pmc
  - micro-eye-awasthi2016-pmc
  - micro-eye-ueki2016-pmc
- assessment_id: micro-eyespot_apparatus-graph
  area: graph
  topic: All four descriptive light-detection edges
  outcome: supported
  target_ids:
  - GO:1990413
  summary: Pigment concentration, photoreceptor localization, shielding and support
    for directional detection are supported at the broad Chlamydomonas cohort level.
    The direct localization example is ChR1, and Ueki Fig6 is a model integrating
    the mutant and lens observations. NONMECHANISTIC scope does not claim a complete
    ion-channel/flagellar signaling cascade.
  evidence_ids:
  - micro-record-eyespot_apparatus
  - micro-eye-lamb1999-meta
  - micro-eye-schmidt2006-meta
  - micro-eye-mittelmeier2011-meta
  - micro-eye-awasthi2016-meta
  - micro-eye-ueki2016-meta
  - micro-eye-schmidt2006-pmc
  - micro-eye-mittelmeier2011-pmc
  - micro-eye-awasthi2016-pmc
  - micro-eye-ueki2016-pmc
- assessment_id: micro-eyespot_apparatus-necessity
  area: evidence
  topic: Unknown formation requirements and proteome completeness
  outcome: unknown
  target_ids:
  - GO:1990413
  summary: 'UNKNOWN component essentiality is appropriate: phototactic defects and
    reduced pigment do not establish a general absence-of-each-component structure-formation
    test. Whole-cell carotenoid HPLC does not resolve all eyespot-stored chemical
    species; fraction proteomics allows contamination. Optional family groundings
    and candidate constituents remain an explicit curation TODO, not a proof that
    all candidates are absent.'
  evidence_ids:
  - micro-record-eyespot_apparatus
  - micro-protein-contract
  - micro-eye-schmidt2006-pmc
  - micro-eye-mittelmeier2011-pmc
  - micro-eye-awasthi2016-pmc
  - micro-eye-ueki2016-pmc
- assessment_id: micro-eyespot_apparatus-coverage
  area: completeness
  topic: Full maintained target and honest scope
  outcome: supported
  target_ids:
  - GO:1990413
  summary: Entire target and every graph edge were read. There are no target image
    assets, measurements, trait links or verbatim evidence snippets to verify. Optional
    molecular inventories and family groundings remain acknowledged; no finding is
    invented from an empty optional slot. PROPOSED status and historical events are
    retained.
  evidence_ids:
  - micro-record-eyespot_apparatus
  - micro-policy
  - micro-eye-go
  - micro-eye-lamb1999-meta
  - micro-eye-schmidt2006-meta
  - micro-eye-mittelmeier2011-meta
  - micro-eye-awasthi2016-meta
  - micro-eye-ueki2016-meta
- assessment_id: micro-eyespot_apparatus-schema
  area: schema
  topic: Immutable original and current native coverage
  outcome: supported
  summary: Original validates/renders identically and historical frozen input verified.
    Current root native protein commands exit0 with actual inventory limits; no scientific
    inference from status alone.
  target_ids:
  - GO:1990413
  evidence_ids:
  - micro-original-pairs
  - micro-prior-eyespot_apparatus
  - micro-native-eyespot_apparatus-verify
  - micro-native-eyespot_apparatus-causal
- assessment_id: micro-eyespot_apparatus-adapter
  area: evidence
  topic: Molecular/pathway applicability and exact catalogue coverage
  outcome: not_applicable
  summary: 'Existing expression-only N/A rationale is deficient: this target asserts
    named proteins/pathways. Fresh official catalogue has no target organism/strain
    match; no downstream module keys or unmatched proxy invented. Historical runner
    unavailability is separately dated; this is a bounded source applicability result,
    not biological negative evidence.'
  target_ids:
  - GO:1990413
  evidence_ids:
  - micro-record-eyespot_apparatus
  - micro-prior-eyespot_apparatus
  - micro-policy
  - micro-historical-runner
  - micro-catalogue
- assessment_id: micro-ferrosome-identity
  area: identity
  topic: Minted ferrosome versus magnetosome
  outcome: supported
  target_ids:
  - cellstructuremech:ferrosome
  summary: Exact local identifier uniquely denotes lipid-bounded amorphous iron-storage
    organelle, distinct from bullet-shaped magnetite crystals. Parent GO0043231 is
    compatible with the physical organelle, without claiming a native GO ferrosome
    child. Bounded exact search returned zero, not worldwide ontology absence.
  evidence_ids:
  - micro-record-ferrosome
  - micro-local-ferrosome-id
  - micro-fer-go
  - micro-fer-go-search
  - micro-fer-grant2022-s3
  - micro-byrne-canonical
- assessment_id: micro-ferrosome-protein-identity
  area: grounding
  topic: Exact Fez locus bridges and family/cohort limits
  outcome: supported
  target_ids:
  - cellstructuremech:ferrosome
  summary: Grant explicitly bridges FezA/B/C to DMR28320/30/40, matching the three
    native RS-1 entries and their unreviewed statuses. Their grouped representation
    is a cohort, not one proven stoichiometric protein complex. Broad P-typeATPase
    or HMA-domain descriptions cannot exactly ground all three unrelated proteins.
    The acknowledged family/component-boundary TODO remains justified.
  evidence_ids:
  - micro-record-ferrosome
  - micro-policy
  - micro-fer-grant2022-s3
  - micro-fer-IPR027256
  - micro-fer-C4XH20
  - micro-fer-C4XH21
  - micro-fer-C4XH22
- assessment_id: micro-ferrosome-material
  area: grounding
  topic: Membrane and unresolved amorphous core chemistry
  outcome: supported
  target_ids:
  - cellstructuremech:ferrosome
  summary: Byrne directly reports membrane-surrounded amorphous granules with Fe/P/O
    enrichment. This supports collective lipid boundary and chemically unresolved
    storage material; it does not identify a single mineral, free ion or molecular
    formula suitable for an exact CHEBI substitution. The existing label-only states
    and chemistry TODO preserve that uncertainty.
  evidence_ids:
  - micro-record-ferrosome
  - micro-policy
  - micro-byrne-canonical
  - micro-fer-grant2022-s3
- assessment_id: micro-ferrosome-necessity
  area: grounding
  topic: Collective formation dependence versus individual requirements
  outcome: unknown
  target_ids:
  - cellstructuremech:ferrosome
  summary: FezBC deletion/complementation supports the represented cohort-level dependence,
    but individual requirements for all three unrelated proteins are not separately
    demonstrated. UNKNOWN is retained for the cohort and exact core chemistry. The
    ESSENTIAL lipid row denotes the complete boundary material; individual lipid-species
    necessity or removal/substitution requirements are not measured. No catalytic
    or stoichiometric inference is substituted for formation necessity.
  evidence_ids:
  - micro-record-ferrosome
  - micro-policy
  - micro-fer-grant2022-s3
  - micro-byrne-canonical
- assessment_id: micro-ferrosome-scope
  area: scope
  topic: RS-1 taxon and canonical ultrastructure
  outcome: supported
  target_ids:
  - cellstructuremech:ferrosome
  summary: 'The current strain name and historical Desulfovibrio name are natively
    bridged. RS-1 supplies Fez proteomics/genetics and Byrne ultrastructure, while
    the listed iron-rich growth/iron-transition context matters: COMMON is qualitative
    capacity/occurrence, not constitutive granules in every cell. The taxon note connects
    the RS-1 formation work to the study-level storage interpretation; it does not
    expressly claim that RS-1 supplied the iron-starvation fitness assay.'
  evidence_ids:
  - micro-record-ferrosome
  - micro-fer-tax573370
  - micro-fer-grant2022-s3
  - micro-byrne-canonical
- assessment_id: micro-ferrosome-function
  area: evidence
  topic: Supported iron-storage interpretation with species-specific direct tests
  outcome: supported
  target_ids:
  - cellstructuremech:ferrosome
  summary: The class-level storage function is supported by Grant’s iron accumulation/genetics
    and S. putrefaciens anaerobic iron-limitation growth/rescue assays, together with
    RS-1 structural storage evidence. Direct anaerobic fitness benefit was not measured
    for every ferrosome-producing species. The record’s generic function is read within
    this evidence scope, not as a quantified universal phenotype or demonstrated FezB
    transport substrate.
  evidence_ids:
  - micro-record-ferrosome
  - micro-fer-grant2022-s3
  - micro-byrne-canonical
- assessment_id: micro-ferrosome-graph
  area: graph
  topic: Four explicitly NONMECHANISTIC formation/storage edges
  outcome: supported
  target_ids:
  - cellstructuremech:ferrosome
  summary: The graph preserves observed Fez-dependent formation, lipid enclosure,
    core accumulation and storage function without claiming a resolved molecular membrane-biogenesis
    mechanism, iron-transport reaction or core chemical species. This matches the
    primary results and their uncertainties.
  evidence_ids:
  - micro-record-ferrosome
  - micro-policy
  - micro-fer-grant2022-s3
  - micro-byrne-canonical
- assessment_id: micro-ferrosome-coverage
  area: completeness
  topic: Full maintained record and bounded scientific coverage
  outcome: supported
  target_ids:
  - cellstructuremech:ferrosome
  summary: Every maintained claim, graph edge and discussion was inspected. No quantitative
    physical-property field, maintained image/licence asset or verbatim evidence snippet
    is present. Existing PROPOSED status and history remain unchanged. No finding
    is invented from optional unresolved molecular inventory or unavailable full-text
    routes alone.
  evidence_ids:
  - micro-record-ferrosome
  - micro-policy
- assessment_id: micro-ferrosome-schema
  area: schema
  topic: Immutable original and current native coverage
  outcome: supported
  summary: Original validates/renders identically and historical frozen input verified.
    Current root native protein commands exit0 with actual inventory limits; no scientific
    inference from status alone.
  target_ids:
  - cellstructuremech:ferrosome
  evidence_ids:
  - micro-original-pairs
  - micro-prior-ferrosome
  - micro-native-ferrosome-verify
  - micro-native-ferrosome-causal
- assessment_id: micro-ferrosome-adapter
  area: evidence
  topic: Molecular/pathway applicability and exact catalogue coverage
  outcome: not_applicable
  summary: 'Existing expression-only N/A rationale is deficient: this target asserts
    named proteins/pathways. Fresh official catalogue has no target organism/strain
    match; no downstream module keys or unmatched proxy invented. Historical runner
    unavailability is separately dated; this is a bounded source applicability result,
    not biological negative evidence.'
  target_ids:
  - cellstructuremech:ferrosome
  evidence_ids:
  - micro-record-ferrosome
  - micro-prior-ferrosome
  - micro-policy
  - micro-historical-runner
  - micro-catalogue
- assessment_id: micro-eyespot-refresh
  area: evidence
  topic: Substantive reassessment of added acop1 example
  outcome: supported
  summary: 'New Q93WP2/acop1, unreviewed tax3055, is correct by current native authority.
    Literature Table1 explicitly bridges COP3 to Acop1; current deterministic coverage
    moves the single node to COVERED. Accession identity is separate from apparatus
    association: direct ChR1 localization and proteomic COP3 detection supply that
    scope. No source claim transferred from ChR1 to all ChR2 or Cop8 experiments.'
  target_ids:
  - GO:1990413
  evidence_ids:
  - micro-eyespot-delta
  - micro-record-eyespot_apparatus
  - micro-prior-eyespot_apparatus
  - micro-eye-Q93WP2
  - micro-eye-schmidt2006-pmc
  - micro-eye-mittelmeier2011-pmc
  - micro-native-eyespot_apparatus-causal
- assessment_id: septin-er_to_golgi_transport_vesicle_membrane-schema
  area: schema
  topic: Original schema/render and unchanged frozen target
  outcome: supported
  summary: Original native validation and deterministic rendering pass; original frozen,
    historical-source and current target bytes agree. None of these four targets is
    stale.
  target_ids:
  - GO:0012507
  evidence_ids:
  - septin-record-er_to_golgi_transport_vesicle_membrane
  - septin-original-validation-er_to_golgi_transport_vesicle_membrane
- assessment_id: septin-er_to_golgi_transport_vesicle_membrane-native-scope
  area: provenance
  topic: Represented protein inventory and typed graph coverage
  outcome: supported
  summary: No protein_examples, protein UniProtKB graph xrefs or GENE_OR_PROTEIN nodes
    are represented. Exit zero validates this empty represented inventory only, not
    narrative named molecules, pathway behavior, source localization or completeness.
  target_ids:
  - GO:0012507
  evidence_ids:
  - septin-record-er_to_golgi_transport_vesicle_membrane
  - septin-native-er_to_golgi_transport_vesicle_membrane-verify
  - septin-native-er_to_golgi_transport_vesicle_membrane-causal
- assessment_id: septin-er_to_golgi_transport_vesicle_membrane-nonasserted-surfaces
  area: scope
  topic: Target images, measurements, traits and snippets
  outcome: not_applicable
  summary: No target image, quantitative property, trait link or verbatim snippet
    is declared. Source OCR/caption inspection is not source figure-pixel, sequence-alignment
    or raw-data reanalysis.
  target_ids:
  - GO:0012507
  evidence_ids:
  - septin-record-er_to_golgi_transport_vesicle_membrane
- assessment_id: septin-er_to_golgi_transport_vesicle_membrane-history
  area: provenance
  topic: Scientific status and previous findings
  outcome: supported
  summary: PROPOSED status and histories remain unchanged. Original findings/actions
    are empty; no prior finding identity or severity normalization is invented. Existing
    discussion resolutions explain scope, not a current terminal disposition of historical
    or neighboring issues.
  target_ids:
  - GO:0012507
  evidence_ids:
  - septin-record-er_to_golgi_transport_vesicle_membrane
  - septin-original-er_to_golgi_transport_vesicle_membrane
  - septin-curation-policy
- assessment_id: septin-esterosome-schema
  area: schema
  topic: Original schema/render and unchanged frozen target
  outcome: supported
  summary: Original native validation and deterministic rendering pass; original frozen,
    historical-source and current target bytes agree. None of these four targets is
    stale.
  target_ids:
  - GO:0033117
  evidence_ids:
  - septin-record-esterosome
  - septin-original-validation-esterosome
- assessment_id: septin-esterosome-native-scope
  area: provenance
  topic: Represented protein inventory and typed graph coverage
  outcome: supported
  summary: Two exact reviewed protein examples P21837/cryS and P18142/D2 validate;
    the one GENE_OR_PROTEIN node is COVERED through its component_ref. This covers
    declared identifiers and symbols, not exact family grounding, source localization,
    stoichiometry, necessity or completeness.
  target_ids:
  - GO:0033117
  evidence_ids:
  - septin-record-esterosome
  - septin-native-esterosome-verify
  - septin-native-esterosome-causal
- assessment_id: septin-esterosome-nonasserted-surfaces
  area: scope
  topic: Target images, measurements, traits and snippets
  outcome: not_applicable
  summary: No target image, quantitative property, trait link or verbatim snippet
    is declared. Source OCR/caption inspection is not source figure-pixel, sequence-alignment
    or raw-data reanalysis.
  target_ids:
  - GO:0033117
  evidence_ids:
  - septin-record-esterosome
- assessment_id: septin-esterosome-history
  area: provenance
  topic: Scientific status and previous findings
  outcome: supported
  summary: PROPOSED status and histories remain unchanged. Original findings/actions
    are empty; no prior finding identity or severity normalization is invented. Existing
    discussion resolutions explain scope, not a current terminal disposition of historical
    or neighboring issues.
  target_ids:
  - GO:0033117
  evidence_ids:
  - septin-record-esterosome
  - septin-original-esterosome
  - septin-curation-policy
- assessment_id: septin-esterosome_lumen-schema
  area: schema
  topic: Original schema/render and unchanged frozen target
  outcome: supported
  summary: Original native validation and deterministic rendering pass; original frozen,
    historical-source and current target bytes agree. None of these four targets is
    stale.
  target_ids:
  - GO:0034467
  evidence_ids:
  - septin-record-esterosome_lumen
  - septin-original-validation-esterosome_lumen
- assessment_id: septin-esterosome_lumen-native-scope
  area: provenance
  topic: Represented protein inventory and typed graph coverage
  outcome: supported
  summary: No protein_examples, protein UniProtKB graph xrefs or GENE_OR_PROTEIN nodes
    are represented. Exit zero validates this empty represented inventory only, not
    narrative named molecules, pathway behavior, source localization or completeness.
  target_ids:
  - GO:0034467
  evidence_ids:
  - septin-record-esterosome_lumen
  - septin-native-esterosome_lumen-verify
  - septin-native-esterosome_lumen-causal
- assessment_id: septin-esterosome_lumen-nonasserted-surfaces
  area: scope
  topic: Target images, measurements, traits and snippets
  outcome: not_applicable
  summary: No target image, quantitative property, trait link or verbatim snippet
    is declared. Source OCR/caption inspection is not source figure-pixel, sequence-alignment
    or raw-data reanalysis.
  target_ids:
  - GO:0034467
  evidence_ids:
  - septin-record-esterosome_lumen
- assessment_id: septin-esterosome_lumen-history
  area: provenance
  topic: Scientific status and previous findings
  outcome: supported
  summary: PROPOSED status and histories remain unchanged. Original findings/actions
    are empty; no prior finding identity or severity normalization is invented. Existing
    discussion resolutions explain scope, not a current terminal disposition of historical
    or neighboring issues.
  target_ids:
  - GO:0034467
  evidence_ids:
  - septin-record-esterosome_lumen
  - septin-original-esterosome_lumen
  - septin-curation-policy
- assessment_id: septin-esterosome_membrane-schema
  area: schema
  topic: Original schema/render and unchanged frozen target
  outcome: supported
  summary: Original native validation and deterministic rendering pass; original frozen,
    historical-source and current target bytes agree. None of these four targets is
    stale.
  target_ids:
  - GO:0033118
  evidence_ids:
  - septin-record-esterosome_membrane
  - septin-original-validation-esterosome_membrane
- assessment_id: septin-esterosome_membrane-native-scope
  area: provenance
  topic: Represented protein inventory and typed graph coverage
  outcome: supported
  summary: No protein_examples, protein UniProtKB graph xrefs or GENE_OR_PROTEIN nodes
    are represented. Exit zero validates this empty represented inventory only, not
    narrative named molecules, pathway behavior, source localization or completeness.
  target_ids:
  - GO:0033118
  evidence_ids:
  - septin-record-esterosome_membrane
  - septin-native-esterosome_membrane-verify
  - septin-native-esterosome_membrane-causal
- assessment_id: septin-esterosome_membrane-nonasserted-surfaces
  area: scope
  topic: Target images, measurements, traits and snippets
  outcome: not_applicable
  summary: No target image, quantitative property, trait link or verbatim snippet
    is declared. Source OCR/caption inspection is not source figure-pixel, sequence-alignment
    or raw-data reanalysis.
  target_ids:
  - GO:0033118
  evidence_ids:
  - septin-record-esterosome_membrane
- assessment_id: septin-esterosome_membrane-history
  area: provenance
  topic: Scientific status and previous findings
  outcome: supported
  summary: PROPOSED status and histories remain unchanged. Original findings/actions
    are empty; no prior finding identity or severity normalization is invented. Existing
    discussion resolutions explain scope, not a current terminal disposition of historical
    or neighboring issues.
  target_ids:
  - GO:0033118
  evidence_ids:
  - septin-record-esterosome_membrane
  - septin-original-esterosome_membrane
  - septin-curation-policy
- assessment_id: septin-er_to_golgi_transport_vesicle_membrane-adapter
  area: scope
  topic: Complete-record molecular applicability and target-host catalogue coverage
  outcome: not_applicable
  summary: Named molecular/pathway assertions trigger applicability assessment despite
    descriptive topology. Fresh complete official catalogue lacks the actual yeast/Dictyostelium
    host, so downstream queries are not applicable. Correct the original unsupported
    exemption in the review successor; preserve the actual historical runner failure
    and avoid negative-biology or unrelated-host claims.
  target_ids:
  - GO:0012507
  evidence_ids:
  - septin-record-er_to_golgi_transport_vesicle_membrane
  - septin-original-er_to_golgi_transport_vesicle_membrane
  - septin-review-policy
  - septin-catalogue
  - septin-historical-adapter-runner
- assessment_id: septin-esterosome-adapter
  area: scope
  topic: Complete-record molecular applicability and target-host catalogue coverage
  outcome: not_applicable
  summary: Named molecular/pathway assertions trigger applicability assessment despite
    descriptive topology. Fresh complete official catalogue lacks the actual yeast/Dictyostelium
    host, so downstream queries are not applicable. Correct the original unsupported
    exemption in the review successor; preserve the actual historical runner failure
    and avoid negative-biology or unrelated-host claims.
  target_ids:
  - GO:0033117
  evidence_ids:
  - septin-record-esterosome
  - septin-original-esterosome
  - septin-review-policy
  - septin-catalogue
  - septin-historical-adapter-runner
- assessment_id: septin-esterosome_lumen-adapter
  area: scope
  topic: Complete-record molecular applicability and target-host catalogue coverage
  outcome: not_applicable
  summary: Named molecular/pathway assertions trigger applicability assessment despite
    descriptive topology. Fresh complete official catalogue lacks the actual yeast/Dictyostelium
    host, so downstream queries are not applicable. Correct the original unsupported
    exemption in the review successor; preserve the actual historical runner failure
    and avoid negative-biology or unrelated-host claims.
  target_ids:
  - GO:0034467
  evidence_ids:
  - septin-record-esterosome_lumen
  - septin-original-esterosome_lumen
  - septin-review-policy
  - septin-catalogue
  - septin-historical-adapter-runner
- assessment_id: septin-esterosome_membrane-adapter
  area: scope
  topic: Genuine material and boundary-morphology exclusion
  outcome: not_applicable
  summary: The complete record asserts a generic lipid bilayer, crystal-filled lumen,
    RER-like boundary morphology and descriptive parthood. It names no cryS/D2 accession
    or gene and explicitly avoids ER-trafficking/nucleation mechanisms. This supports
    genuine molecular-query exclusion. Clarify the older generic rationale without
    manufacturing an extra bundle defect; the sparse scope, rather than a lack of
    expression claims, is the basis.
  target_ids:
  - GO:0033118
  evidence_ids:
  - septin-record-esterosome_membrane
  - septin-original-esterosome_membrane
  - septin-review-policy
  - septin-catalogue
- assessment_id: septin-er_to_golgi_transport_vesicle_membrane-identity
  area: identity
  topic: Exact bilayer identity, synonym, parentage and containing carrier
  outcome: supported
  summary: GO0012507 exactly defines the surrounding ER-to-Golgi transport-vesicle
    lipid bilayer; its COPII synonym, transport/coated-membrane parents and COPII
    whole-vesicle parthood are verified by native typed GO entries.
  target_ids:
  - GO:0012507
  evidence_ids:
  - septin-record-er_to_golgi_transport_vesicle_membrane
  - septin-go
- assessment_id: septin-er_to_golgi_transport_vesicle_membrane-material
  area: grounding
  topic: Generic bilayer component and coat boundary
  outcome: supported
  summary: REVIEWED_LABEL_ONLY explicitly leaves chemical specificity open while correctly
    identifying collective lipid-bilayer constitution. Sar1/Sec complexes are coat
    machinery, not automatically direct bilayer constituents. GO coat parthood does
    not require treating that associated protein coat as the lipid material itself.
    No exact chemical-ontology absence is claimed.
  target_ids:
  - GO:0012507
  evidence_ids:
  - septin-record-er_to_golgi_transport_vesicle_membrane
  - septin-go
  - septin-curation-policy
  - septin-barlowe1994-meta
  - septin-matsuoka1998-meta
- assessment_id: septin-er_to_golgi_transport_vesicle_membrane-taxon
  area: scope
  topic: Yeast COPII model and actual source tiers
  outcome: supported
  summary: Exact S.cerevisiae identity and the yeast COPII ER-derived vesicle example
    are supported by GO and the complete Barlowe abstract. Matsuoka explicitly names
    purified Sar1, Sec13/31 and Sec23/24. COMMON is qualitative occurrence, not measured
    population prevalence; no uninspected full methods, detailed strains or figure-panel
    inference is certified.
  target_ids:
  - GO:0012507
  evidence_ids:
  - septin-record-er_to_golgi_transport_vesicle_membrane
  - septin-tax4932
  - septin-go
  - septin-barlowe1994-meta
  - septin-matsuoka1998-meta
- assessment_id: septin-er_to_golgi_transport_vesicle_membrane-graph
  area: graph
  topic: Three descriptive parthood, boundary and ER-donor relations
  outcome: supported
  summary: Part_of and bounds follow GO identity. ER membrane donation is supported
    by GO0090114 evagination and Barlowe ER-membrane budding; Matsuoka supplies complementary
    synthetic-liposome reconstitution, not a direct native-ER composition measurement.
    NONMECHANISTIC scope does not duplicate coat assembly or assert every lipid is
    necessary.
  target_ids:
  - GO:0012507
  evidence_ids:
  - septin-record-er_to_golgi_transport_vesicle_membrane
  - septin-go
  - septin-barlowe1994-meta
  - septin-matsuoka1998-meta
  - septin-graph-policy
- assessment_id: septin-er_to_golgi_transport_vesicle_membrane-necessity
  area: grounding
  topic: Collective bilayer versus molecular requirement
  outcome: unknown
  summary: ESSENTIAL applies to the defining collective bilayer. Specific lipid removal/substitution
    necessity in native membranes is not established by the cited source tiers, and
    no such individual requirement is asserted.
  target_ids:
  - GO:0012507
  evidence_ids:
  - septin-record-er_to_golgi_transport_vesicle_membrane
  - septin-go
  - septin-matsuoka1998-meta
  - septin-curation-policy
- assessment_id: septin-esterosome-taxon
  area: scope
  topic: Dictyostelium stage/strain and morphology context
  outcome: supported
  summary: Exact D.discoideum identity is current. Bomblies directly examines aggregation-stage
    crystals and membrane morphology, mostly AX2-214, with AX3 used for specified
    sequence/transcript work. The maintained qualitative COMMON/example wording is
    stage-bounded and does not assert pan-amoebal distribution, uniform abundance
    or live trafficking.
  target_ids:
  - GO:0033117
  evidence_ids:
  - septin-record-esterosome
  - septin-tax44689
  - septin-bomblies1990-meta
  - septin-bomblies-jats
- assessment_id: septin-esterosome-source-limits
  area: evidence
  topic: Morphology and protein association versus unresolved physiology
  outcome: supported
  summary: The paper supports membrane-enclosed crystals and RER-like boundary morphology.
    It explicitly leaves co-crystallization detail/ratio, ER sorting, nucleation,
    crystal fate and physiological function unresolved. OCR prose and caption text
    were inspected; raw data, alignment calculations and figure pixels were not reanalyzed.
  target_ids:
  - GO:0033117
  evidence_ids:
  - septin-record-esterosome
  - septin-bomblies-jats
  - septin-source-access
- assessment_id: septin-esterosome_lumen-taxon
  area: scope
  topic: Dictyostelium stage/strain and morphology context
  outcome: supported
  summary: Exact D.discoideum identity is current. Bomblies directly examines aggregation-stage
    crystals and membrane morphology, mostly AX2-214, with AX3 used for specified
    sequence/transcript work. The maintained qualitative COMMON/example wording is
    stage-bounded and does not assert pan-amoebal distribution, uniform abundance
    or live trafficking.
  target_ids:
  - GO:0034467
  evidence_ids:
  - septin-record-esterosome_lumen
  - septin-tax44689
  - septin-bomblies1990-meta
  - septin-bomblies-jats
- assessment_id: septin-esterosome_lumen-source-limits
  area: evidence
  topic: Morphology and protein association versus unresolved physiology
  outcome: supported
  summary: The paper supports membrane-enclosed crystals and RER-like boundary morphology.
    It explicitly leaves co-crystallization detail/ratio, ER sorting, nucleation,
    crystal fate and physiological function unresolved. OCR prose and caption text
    were inspected; raw data, alignment calculations and figure pixels were not reanalyzed.
  target_ids:
  - GO:0034467
  evidence_ids:
  - septin-record-esterosome_lumen
  - septin-bomblies-jats
  - septin-source-access
- assessment_id: septin-esterosome_membrane-taxon
  area: scope
  topic: Dictyostelium stage/strain and morphology context
  outcome: supported
  summary: Exact D.discoideum identity is current. Bomblies directly examines aggregation-stage
    crystals and membrane morphology, mostly AX2-214, with AX3 used for specified
    sequence/transcript work. The maintained qualitative COMMON/example wording is
    stage-bounded and does not assert pan-amoebal distribution, uniform abundance
    or live trafficking.
  target_ids:
  - GO:0033118
  evidence_ids:
  - septin-record-esterosome_membrane
  - septin-tax44689
  - septin-bomblies1990-meta
  - septin-bomblies-jats
- assessment_id: septin-esterosome_membrane-source-limits
  area: evidence
  topic: Morphology and protein association versus unresolved physiology
  outcome: supported
  summary: The paper supports membrane-enclosed crystals and RER-like boundary morphology.
    It explicitly leaves co-crystallization detail/ratio, ER sorting, nucleation,
    crystal fate and physiological function unresolved. OCR prose and caption text
    were inspected; raw data, alignment calculations and figure pixels were not reanalyzed.
  target_ids:
  - GO:0033118
  evidence_ids:
  - septin-record-esterosome_membrane
  - septin-bomblies-jats
  - septin-source-access
- assessment_id: septin-esterosome-identity
  area: identity
  topic: Exact whole organelle and its two parts
  outcome: supported
  summary: GO0033117 and SL0109 identify the whole esterosome as a cytoplasmic vesicle
    with crystalline esterase-like protein. GO/UniProt separately identify lumen and
    membrane; direct exact matches are distinguished from nested parental location
    mappings.
  target_ids:
  - GO:0033117
  evidence_ids:
  - septin-record-esterosome
  - septin-go
  - septin-SL-0109
  - septin-SL-0108
  - septin-SL-0328
- assessment_id: septin-esterosome-protein-identity
  area: grounding
  topic: Two exact reviewed protein examples
  outcome: supported
  summary: Current P21837/cryS Crystal protein and P18142/D2 cAMP-regulated D2 protein
    are reviewed D.discoideum entries. These exact identities agree with the maintained
    examples and native coverage. Identity checks do not alone establish localization
    or necessity.
  target_ids:
  - GO:0033117
  evidence_ids:
  - septin-record-esterosome
  - septin-protein-P21837
  - septin-protein-P18142
  - septin-native-esterosome-verify
  - septin-native-esterosome-causal
- assessment_id: septin-esterosome-membership
  area: evidence
  topic: Primary crystal cargo evidence and authority annotation granularity
  outcome: supported
  summary: Purification, N-terminal/cDNA identity, protein-specific antibodies, serial
    sections and double-gold immunolabeling support cryS and D2 as major crystal-associated
    constituents. The paper explicitly describes lumenal rather than membrane-associated
    proteins. UniProt location SL0108 is therefore retained as coarse annotation context,
    not reassigned as direct bilayer membership. No exhaustive minor-protein inventory
    is asserted.
  target_ids:
  - GO:0033117
  evidence_ids:
  - septin-record-esterosome
  - septin-bomblies-jats
  - septin-protein-P21837
  - septin-protein-P18142
- assessment_id: septin-esterosome-family-grounding
  area: grounding
  topic: Reviewed label-only family scope
  outcome: supported
  summary: The complete current exact-protein InterPro responses contain a domain,
    conserved site, active site and homologous superfamily, but no integrated family-typed
    entry. Native guidance does not promote these types as a family consensus. Existing
    broad hydrolase similarity, exact verified proteins and the explicit family-grounding
    TODO do not establish an actionable deferred-family error here. The bounded response
    does not establish universal ontology absence.
  target_ids:
  - GO:0033117
  evidence_ids:
  - septin-record-esterosome
  - septin-interpro-P21837
  - septin-interpro-P18142
  - septin-curation-policy
  - septin-protein-P21837
  - septin-protein-P18142
- assessment_id: septin-esterosome-graph
  area: graph
  topic: Observed crystal association and enclosing topology
  outcome: supported
  summary: The crystallize-in predicate is explicitly constrained by its co-fractionation/immunolabeling
    description and NONMECHANISTIC scope. It represents observed mature crystalline
    cargo, not purified binary co-crystallization, a fixed protein ratio, ER trafficking
    or a nucleation sequence. Membrane bounds lumen and membrane part_of whole are
    independently supported by exact identities and microscopy prose.
  target_ids:
  - GO:0033117
  evidence_ids:
  - septin-record-esterosome
  - septin-bomblies-jats
  - septin-go
  - septin-graph-policy
- assessment_id: septin-esterosome-necessity
  area: grounding
  topic: Constitution versus protein formation necessity
  outcome: unknown
  summary: Collective bounding membrane is essential by organelle definition; individual
    crystal-protein necessity remains UNKNOWN. Antibody localization, developmentally
    regulated abundance and cited D2 antisense phenotypes do not prove necessity for
    esterosome formation, and the paper discusses future genetic tests.
  target_ids:
  - GO:0033117
  evidence_ids:
  - septin-record-esterosome
  - septin-bomblies-jats
  - septin-curation-policy
- assessment_id: septin-esterosome_lumen-identity
  area: identity
  topic: Exact enclosed volume, broad is_a ancestry and parthood
  outcome: supported
  summary: GO0034467 and SL0328 identify the volume enclosed by esterosome membrane,
    provide the esterosomal-lumen synonym and whole-organelle parthood. The explicit
    is_a-only ancestor response verifies broad GO0043233, without falsely representing
    it as the direct native parent.
  target_ids:
  - GO:0034467
  evidence_ids:
  - septin-record-esterosome_lumen
  - septin-go
  - septin-lumen-is-a-ancestors
  - septin-SL-0328
  - septin-SL-0109
- assessment_id: septin-esterosome_lumen-cargo-function
  area: evidence
  topic: Descriptive crystal storage versus unresolved biological role
  outcome: supported
  summary: The storage function description states only that the internal compartment
    is occupied by crystalline esterase-like cargo. Bomblies supports that observed
    sequestration and cryS/D2 cargo context, but not a defined physiological storage
    purpose, catalysis or release route. Empty direct components are consistent with
    region identity and the maintained whole-organelle cargo model.
  target_ids:
  - GO:0034467
  evidence_ids:
  - septin-record-esterosome_lumen
  - septin-bomblies-jats
  - septin-go
  - septin-curation-policy
- assessment_id: septin-esterosome_lumen-graph
  area: graph
  topic: Two descriptive lumen and boundary edges
  outcome: supported
  summary: Lumen part_of esterosome and membrane encloses lumen follow exact GO/UniProt
    identities and the source membrane-enclosed crystals. The boundary membrane is
    not a lumen constituent; no unobserved molecular transport or nucleation step
    is added.
  target_ids:
  - GO:0034467
  evidence_ids:
  - septin-record-esterosome_lumen
  - septin-go
  - septin-SL-0328
  - septin-bomblies-jats
  - septin-graph-policy
- assessment_id: septin-esterosome_membrane-identity
  area: identity
  topic: Exact membrane identity, synonym, parent and parthood
  outcome: supported
  summary: GO0033118 and SL0108 identify the surrounding bilayer, esterosomal-membrane
    synonym, cytoplasmic-vesicle-membrane parent and esterosome parthood. This is
    the boundary structure, not its crystal cargo or whole organelle.
  target_ids:
  - GO:0033118
  evidence_ids:
  - septin-record-esterosome_membrane
  - septin-go
  - septin-SL-0108
- assessment_id: septin-esterosome_membrane-material
  area: grounding
  topic: Collective lipid bilayer and RER-like morphology
  outcome: supported
  summary: Generic bilayer constitution and RER-like boundary are supported by native
    definition and the primary microscopy prose. Reviewed-label-only chemical specificity
    is explicitly acknowledged. No exact lipid species, membrane-protein inventory,
    biochemical ER identity or trafficking continuity is claimed.
  target_ids:
  - GO:0033118
  evidence_ids:
  - septin-record-esterosome_membrane
  - septin-go
  - septin-bomblies-jats
  - septin-curation-policy
- assessment_id: septin-esterosome_membrane-graph-function
  area: graph
  topic: Boundary function and two topological edges
  outcome: supported
  summary: The function and graph specify membrane parthood and lumen enclosure, supported
    by exact definitions and the membrane-enclosed crystal observations. NONMECHANISTIC
    scope explicitly excludes ER-trafficking and nucleation.
  target_ids:
  - GO:0033118
  evidence_ids:
  - septin-record-esterosome_membrane
  - septin-go
  - septin-SL-0108
  - septin-bomblies-jats
  - septin-graph-policy
- assessment_id: septin-esterosome_membrane-necessity
  area: grounding
  topic: Individual molecular requirements
  outcome: unknown
  summary: ESSENTIAL denotes the defining collective bilayer, not an experimentally
    required lipid species or named protein. No individual molecular formation requirement
    is established or asserted.
  target_ids:
  - GO:0033118
  evidence_ids:
  - septin-record-esterosome_membrane
  - septin-go
  - septin-curation-policy
- assessment_id: septin-er_to_golgi_transport_vesicle_membrane-verdict
  area: evidence
  topic: Qualified scientific acceptance with explicit access and inference limits
  outcome: supported
  summary: No concrete scientific record correction was established for this complete
    assigned target. Preserve exact source tiers, authority/primary distinctions,
    experimental scope, unknown necessity and represented-inventory limits. Three
    actual applicability defects are transmitted separately; the sparse esterosome
    membrane is genuinely excluded. No scientific finding, predecessor identity or
    historical issue resolution is invented.
  target_ids:
  - GO:0012507
  evidence_ids:
  - septin-record-er_to_golgi_transport_vesicle_membrane
  - septin-go
  - septin-catalogue
  - septin-curation-policy
  - septin-barlowe1994-meta
  - septin-matsuoka1998-meta
- assessment_id: septin-esterosome-verdict
  area: evidence
  topic: Qualified scientific acceptance with explicit access and inference limits
  outcome: supported
  summary: No concrete scientific record correction was established for this complete
    assigned target. Preserve exact source tiers, authority/primary distinctions,
    experimental scope, unknown necessity and represented-inventory limits. Three
    actual applicability defects are transmitted separately; the sparse esterosome
    membrane is genuinely excluded. No scientific finding, predecessor identity or
    historical issue resolution is invented.
  target_ids:
  - GO:0033117
  evidence_ids:
  - septin-record-esterosome
  - septin-go
  - septin-catalogue
  - septin-curation-policy
  - septin-bomblies-jats
- assessment_id: septin-esterosome_lumen-verdict
  area: evidence
  topic: Qualified scientific acceptance with explicit access and inference limits
  outcome: supported
  summary: No concrete scientific record correction was established for this complete
    assigned target. Preserve exact source tiers, authority/primary distinctions,
    experimental scope, unknown necessity and represented-inventory limits. Three
    actual applicability defects are transmitted separately; the sparse esterosome
    membrane is genuinely excluded. No scientific finding, predecessor identity or
    historical issue resolution is invented.
  target_ids:
  - GO:0034467
  evidence_ids:
  - septin-record-esterosome_lumen
  - septin-go
  - septin-catalogue
  - septin-curation-policy
  - septin-bomblies-jats
- assessment_id: septin-esterosome_membrane-verdict
  area: evidence
  topic: Qualified scientific acceptance with explicit access and inference limits
  outcome: supported
  summary: No concrete scientific record correction was established for this complete
    assigned target. Preserve exact source tiers, authority/primary distinctions,
    experimental scope, unknown necessity and represented-inventory limits. Three
    actual applicability defects are transmitted separately; the sparse esterosome
    membrane is genuinely excluded. No scientific finding, predecessor identity or
    historical issue resolution is invented.
  target_ids:
  - GO:0033118
  evidence_ids:
  - septin-record-esterosome_membrane
  - septin-go
  - septin-catalogue
  - septin-curation-policy
  - septin-bomblies-jats
- assessment_id: current-input-comparison
  area: provenance
  topic: Complete frozen-input comparison and bounded refresh
  outcome: supported
  summary: 1 of ten original target hashes differ from current main. The changed content
    is substantively reassessed in the target-specific assessments; original observations
    remain historical and unchanged. All current target and used context bytes are
    frozen.
  target_ids:
  - GO:0031904
  - GO:0010008
  - GO:7770040
  - GO:0012507
  - GO:0033117
  - GO:0034467
  - GO:0033118
  - GO:0044311
  - GO:1990413
  - cellstructuremech:ferrosome
  evidence_ids:
  - current-record-0
  - original-review-0
  - current-record-1
  - original-review-1
  - current-record-2
  - original-review-2
  - current-record-3
  - original-review-3
  - current-record-4
  - original-review-4
  - current-record-5
  - original-review-5
  - current-record-6
  - original-review-6
  - current-record-7
  - original-review-7
  - current-record-8
  - original-review-8
  - current-record-9
  - original-review-9
findings:
- finding_id: plaque-t2-F1
  issue_key: epiplastidial-adjacent-interface-wording
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Clarify the membrane interface rather than compressing nested boundaries
  description: The function says EpM separates PPC from the host endomembrane system.
    Primary topology places the PPC between PPM and oEM, and EpM is itself continuous
    with host ER/outer nuclear membrane. An outer membrane can indirectly enclose
    PPC, so the wording is not treated as a proven false enclosure claim; it needs
    the adjacent spaces specified to avoid attributing the PPM interface to EpM.
  target_ids:
  - GO:7770040
  field_paths:
  - functions#complex_plastid_outer_boundary.description
  - causal_graphs#epiplastidial_membrane_boundary.edges
  evidence_ids:
  - plaque-current-2
  - plaque-go
  - plaque-flori2016-oceanomics-pdf
  - plaque-gueguen2024-jats
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/epiplastidial_membrane.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:claim-level evidence and minor
    weak-wording/provenance rubric
  native_severity: minor
  normalization_reason: Minor weak wording because indirect enclosure remains valid
    and the text does not explicitly assert a single immediate interface. The correction
    removes ambiguity; it is not a major finding of demonstrably false whole-structure
    identity or universal biological function.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T013716Z-epiplastidial-membrane-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2692
- finding_id: plaque-t2-F2
  issue_key: epiplastidial-descriptive-graph-mechanistic-label
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Classify the two-edge boundary graph as descriptive
  description: The graph consists of collective bilayer formation of the named membrane
    and outer-boundary maintenance. These relations describe identity and topology;
    the cited sources do not establish a molecular causal sequence represented by
    the current nodes and edges.
  target_ids:
  - GO:7770040
  field_paths:
  - causal_graphs#epiplastidial_membrane_boundary.scope_status
  evidence_ids:
  - plaque-current-2
  - plaque-graph-rubric
  - plaque-go
  - plaque-flori2016-oceanomics-pdf
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/epiplastidial_membrane.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:claim-level evidence and minor
    weak-wording/provenance rubric
  native_severity: minor
  normalization_reason: 'Minor metadata overstatement: the constituent relations remain
    supported and no invented molecular interaction is present.'
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T013716Z-epiplastidial-membrane-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2693
- finding_id: micro-F1
  issue_key: exoneme-sub1-family-grounding-gap
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve the verified SUB1 family instead of retaining an unresolved-family
    rationale
  description: Current InterPro IPR017314 is the exact Plasmodium SUB1 family, directly
    linked by current O61142. The unchanged component/discussion still says no exact
    family was resolved. Grounding can be repaired without treating family membership
    as independent exoneme localization. IPR034204 is a catalytic domain and broad
    PMX-family IPR001461 does not settle PMX.
  target_ids:
  - GO:0044311
  field_paths:
  - components#pfsub1_exoneme_protease.grounding_status
  - components#pfsub1_exoneme_protease.grounding_notes
  - discussions#ground_exoneme_proteases
  evidence_ids:
  - micro-record-exoneme
  - micro-policy
  - micro-exo-IPR017314
  - micro-exo-IPR034204
  - micro-exo-O61142
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/exoneme.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:claim-level evidence and minor
    weak-wording/provenance rubric
  native_severity: minor
  normalization_reason: 'Minor grounding/provenance gap: the protein identity, membership
    and mechanism remain correct; a now-resolved family has been left label-only.'
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T013720Z-exoneme-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2694
actions:
- action_id: plaque-t2-A1
  finding_ids:
  - plaque-t2-F1
  target_ids:
  - GO:7770040
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/epiplastidial_membrane.yaml
    role: maintained scientific record
  description: In a separately authorized curation change, clarify EpM as the outer
    boundary against host cytosol, enclosing the ER/cER lumen before the intervening
    PPM and deeper PPC; retain supported indirect enclosure and diatom ER continuity.
  acceptance_checks:
  - Keep EpM, PPM and oEM distinct; name the actual adjacent compartments wherever
    a direct boundary is meant.
  - Retain correct native identity and supported Phaeodactylum context; do not claim
    the source directly measured a new transport mechanism.
  - Run focused schema and strict checks after the separately authorized edit.
- action_id: plaque-t2-A2
  finding_ids:
  - plaque-t2-F2
  target_ids:
  - GO:7770040
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/epiplastidial_membrane.yaml
    role: maintained scientific record
  description: In a separately authorized curation change, use NONMECHANISTIC with
    a scope note for this descriptive topology, or add a genuinely source-backed mechanism
    only if independently established.
  acceptance_checks:
  - Preserve supported topology while documenting the molecular mechanism is not represented.
  - Do not invent transport machinery or lipid requirements to satisfy a graph label.
  - Run the native graph and focused validation checks.
- action_id: micro-A1
  finding_ids:
  - micro-F1
  target_ids:
  - GO:0044311
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/exoneme.yaml
    role: maintained scientific record
  description: In a separately authorized curation change, ground SUB1 to the verified
    IPR017314 family and narrow the TODO to unresolved PMX or other genuinely open
    identity questions; retain primary membership evidence and UNKNOWN assembly necessity.
  acceptance_checks:
  - Verify the exact family ID/label pair against current native InterPro and run
    product/schema/strict checks.
  - Keep the existing accession/taxon pairing and primary membership evidence; a family
    mapping alone does not prove exoneme localization.
  - Do not replace PMX with a broad A1 family or use a catalytic domain as whole-protein
    identity.
limitations:
- 'Endosome lumen/membrane and epiplastidial membrane independent subreview: Assigned
  endosome lumen/membrane and epiplastidial membrane only; all unchanged from original
  frozen hashes. Two inherited minor EpM findings retain exact keys, severities and
  repository/review/finding lineage. No historical neighbor/group/category resolution
  is implied.'
- 'Endosome lumen/membrane and epiplastidial membrane independent subreview: Fresh
  Katzmann2001 and Babst2002 complete primary abstracts only. Henne2011 and Hashimoto2005
  are secondary review abstracts only; no full bodies or figure pixels read for those
  four sources. Katzmann2003 genuine PMC Resultssec5/sec6 and Methodssec12 with Fig3/4
  captions read; no quantitative or figure-pixel reanalysis.'
- 'Endosome lumen/membrane and epiplastidial membrane independent subreview: Flori2016
  published PDF p255 text/Fig1 caption and actual Fig1 pixels, Results opening p256/fullp261,
  Discussion/Methodspp263–264 and associated Fig5/6 caption text read. Other pixels,
  supplements/raw measurements and unlisted pages were not independently audited.
  Phaeodactylum Pt1 CCAP1055/3 disrupted/intact preparations remain distinct.'
- 'Endosome lumen/membrane and epiplastidial membrane independent subreview: Gueguen2024
  JATS scope: Introduction s1/Fig1caption, Results s2.4/Fig2–3captions, Discussion
  s3.2/s3.8, Methods s4.4/s4.13. No figure pixels, supplements or other sections.
  Pt1 Strain8.6 CCAP1055/1 is retained; qualified localization and uncertain lipid
  pools are not formation necessity.'
- 'Endosome lumen/membrane and epiplastidial membrane independent subreview: Fresh
  GO definitions and broader/direct versus nested anatomy are distinguished. EpM definition
  is an exact authority quotation; diatom evidence does not experimentally establish
  ER continuity for all secondary-plastid lineages. F1 concerns adjacent-interface
  ambiguity, not denial of valid indirect PPC enclosure.'
- 'Endosome lumen/membrane and epiplastidial membrane independent subreview: Whole
  bilayer ESSENTIAL is defining collective constitution; no individual-lipid necessity
  is proven. No missing optional protein/family inventory is fabricated. Empty protein
  inventory checks for lumen/EpM and one verified external VPS27 graph node for membrane
  have distinct scopes.'
- 'Endosome lumen/membrane and epiplastidial membrane independent subreview: Both
  endosome records require molecular/pathway applicability assessment. Fresh official
  catalogue has no relevant eukaryotic host match; no downstream gene/module query
  or unrelated proxy applies. EpM is a genuine complete-record material/topology exclusion.
  Historical runner receipt remains actual00:49Z unavailable; no fresh invocation
  or success claimed.'
- 'Endosome lumen/membrane and epiplastidial membrane independent subreview: Three
  frozen neighbor records were read only for identity/boundary context. Root owns
  global QC/issues/publication and all repository/GitHub writes; scientific records
  remain unchanged.'
- 'Exoneme, eyespot apparatus and ferrosome independent subreview: Exoneme/eyespot/ferrosome
  slice: three entire current records and immutable original pairs read; no additional
  local neighbor used. Current eyespot example substantively refreshed, no original
  history overwritten or new scientific predecessor invented.'
- 'Exoneme, eyespot apparatus and ferrosome independent subreview: Exoneme source
  tier: Yeoh2007 and Blackman1998 complete primary abstracts only; fresh publisher
  PDF403 retained. Blackman2008 is secondary review, one complete named subsection.
  Withers2014 Intro and Discussion provide attributed background, not independent
  discharge experiments; its Results/Methods/pixels not inspected. Nasamu2017 complete
  scientific main text/Fig1–4 captions read, no separate supplementary Methods/pixels;
  NF54 experiments are not recast as direct3D7 measurements.'
- 'Exoneme, eyespot apparatus and ferrosome independent subreview: Eyespot source
  tier: Lamb1999 complete primary abstract only. Schmidt selected complete paragraphs,
  Table1 photoreceptor rows and cw15 purification Methods inspected; contamination
  and lost-soluble-protein limitations retained. Mittelmeier Intro/first Results/captions
  and strain/media Methods; Awasthi introductory and initial localization/strain/antibody
  scope; Ueki late Results, captions, Discussion/main Methods. No current source figure
  pixels, movies, raw proteomic data or complete supplemental datasets inspected.
  Original historical pixel inspection is not represented as current.'
- 'Exoneme, eyespot apparatus and ferrosome independent subreview: Eyespot interpretation:
  literal COP3 UniProt index returns zero while native acop1 entry and primary alias
  mapping support Q93WP2; this is not absence of COP3. Direct ChR1 localization is
  distinct from COP4 fraction association and Cop8 trafficking. Unreviewed and automated
  annotations are not direct localization or exact-family groundings.'
- 'Exoneme, eyespot apparatus and ferrosome independent subreview: Ferrosome source
  tier: Grant main scientific Introduction/Results/Discussion read; Methods, extended-data
  captions, supplementary tables and pixels not independently inspected in this pass.
  Byrne entire main scientific text/main Methods and Fig1–5 captions read without
  pixels/supplements. RS-1 supplies formation genetics/ultrastructure; direct anaerobic
  starvation-fitness/rescue is S.putrefaciens. Individual Fez necessity, transport
  substrate, exact core chemistry and universal function remain unresolved.'
- 'Exoneme, eyespot apparatus and ferrosome independent subreview: Adapter/native
  limits: all three original rows are unsupported expression-only exclusions, corrected
  by a fresh official catalogue with no target-organism match. E.coli foreign-operon
  experimental host is not a matched native RS-1 proxy. Historical00:49Z runner failure
  retained honestly; current fetch DNS failures archived and numeric-PMC challenge
  excluded from body evidence. Actual protein inventories are exoneme2examples+2xrefs/3nodes,eyespot2examples/1node,ferrosome3examples/1node.
  No global gates, future CI or queue outcomes borrowed from root before actual receipts.'
- 'Exoneme, eyespot apparatus and ferrosome independent subreview: Local inputs:17
  common instructions/schema/verifier hashes equal preceding reviewed bytes; applicable
  skill/profile/config/checklist/protein guidance reread. Other retained instruction/schema
  reads are not represented as fresh full-file inspection. No repository/GitHub mutation;
  root authors successor and handles QC/issue publication.'
- 'ER-to-Golgi transport-vesicle membrane and esterosome trio independent subreview:
  All four targets equal their original frozen and historical-source hashes; none
  is stale. Four original native validation/render checks pass and findings/actions
  are empty. No scientific predecessor, severity normalization or terminal historical
  disposition is invented.'
- 'ER-to-Golgi transport-vesicle membrane and esterosome trio independent subreview:
  Barlowe and Matsuoka access is complete primary abstract plus exact metadata only.
  No full methods, detailed strain list, figure pixels or quantitative result reanalysis
  is certified. Matsuoka uses chemically defined liposome donors; native ER membrane
  donation also relies on GO and Barlowe.'
- 'ER-to-Golgi transport-vesicle membrane and esterosome trio independent subreview:
  Bomblies evidence is fresh genuine official PMC OA XML containing scanned-article
  OCR. Introduction/Methods/Results/Discussion prose, TableI text and Fig1–11 caption
  text were read; sequence-alignment panels and source figure pixels/raw data were
  not reanalyzed. Canonical PMC HTML returned a challenge despite HTTP200 and was
  not article evidence.'
- 'ER-to-Golgi transport-vesicle membrane and esterosome trio independent subreview:
  Bomblies supports stage-bounded membrane-enclosed crystals and major cryS/D2 constituents.
  Co-crystallization ratio, crystal sorting/nucleation/fate, physiological role, catalysis
  of purified proteins and individual formation necessity remain unresolved. The graph
  is explicitly NONMECHANISTIC; descriptive storage is not a proven physiological
  purpose.'
- 'ER-to-Golgi transport-vesicle membrane and esterosome trio independent subreview:
  Reviewed UniProt protein entries carry membrane-location SL0108 annotation with
  membrane-enclosed-crystal notes. Primary prose explicitly places the proteins in
  the lumen; those authority annotations are not independent direct-bilayer membership
  evidence.'
- 'ER-to-Golgi transport-vesicle membrane and esterosome trio independent subreview:
  Complete exact-protein InterPro responses return only domain/site/superfamily types,
  not integrated families. Native family-consensus policy excludes those types. This
  supports bounded label-only retention, not an exhaustive assertion that no exact
  term exists in any ontology.'
- 'ER-to-Golgi transport-vesicle membrane and esterosome trio independent subreview:
  Three records trigger named molecular/pathway applicability; the fresh complete
  catalogue lacks their actual hosts. No unmatched-host gene/module query or negative
  biological inference is used. Esterosome membrane has genuine material/morphology-only
  scope and is excluded without a manufactured fourth bundle defect. Historical runner
  unavailability remains00:49Z, not a fresh execution.'
- 'ER-to-Golgi transport-vesicle membrane and esterosome trio independent subreview:
  All eight current native protein commands passed. Whole esterosome has two validated
  examples and one COVERED typed molecular node; other three represented inventories
  are empty. Native checks do not certify narrative claims, complete composition,
  source localization or necessity.'
- 'ER-to-Golgi transport-vesicle membrane and esterosome trio independent subreview:
  Only four assigned targets, eight original artifacts and seventeen byte-verified
  common policy/schema/native inputs were used locally. Other frozen cohort neighbors
  were not judged. No target image, quantitative property, trait link or verbatim
  snippet is declared.'
- 'ER-to-Golgi transport-vesicle membrane and esterosome trio independent subreview:
  Root owns global gates, issue dedup/publication, repository/GitHub mutations and
  final-head/CI/queue checks. This report makes no future-gate or merge attestation
  and edits no records.'
- Historical observations remain immutable; their old checks are not represented as
  current-head execution.
- The adapter runner was not rerun after the canary established OS access failure.
  Catalogue-based coverage is assessed directly; fresh and reused responses retain
  actual access timestamps.
- Native label checks include 923 no-adapter skips. Native identifier checks include
  909 PMID transport failures and 254 skipped identifiers; bounded supplemental checks
  independently resolve the 909 PMIDs.
- Scientific record-curation findings stay in separate issues; no record is edited
  by this review PR.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head
  CI and merge-group CI occur after saving this immutable observation and are not
  represented here as already completed.
notes:
- All ten original YAML/Markdown pairs remain unchanged. Current main was merged normally
  and pushed without force.
- This explicit issue-bearing ten-record cohort follows the native persistence policy.
  All three inherited minor scientific findings retain stable keys and exact predecessor
  repository/review/finding identities.
- 'Issue #2690 tracks the stale eyespot-apparatus input. Current main adds Q93WP2/acop1,
  an unreviewed Chlamydomonas reinhardtii channelopsin-1 example, alongside Q8RUT8/cop4.
  Fresh UniProt identity and Schmidt2006 Table1 COP3/CHOP1/CSRA/Acop1 nomenclature
  with peptide support substantively establish the bounded bridge. Identity, apparatus
  membership and directional phototaxis claims remain separate evidence scopes.'
- 'Issue #2691 tracks eight unsupported applicability exclusions. All ten original
  bundles contain an explicit imodulondb not_applicable row. Positive pathway or molecular
  assertions make the endosome lumen/membrane, ER-to-Golgi transport-vesicle membrane,
  esterosome/lumen, exoneme, eyespot and ferrosome records subject to a coverage check.
  Epiplastidial membrane and esterosome membrane retain genuine material/topology
  exclusions.'
- Source commit 5c140efd0be92d341410aa3024d677d5daf8bc1e is retained by tag review-base/pr2365-current-record-followup-20261103.
- CLAUDE.md is an alias of AGENTS.md; canonical regular AGENTS.md bytes are frozen.
- All 50 local inputs were frozen before their assessment. The multivesicular-body
  lumen, intraluminal-vesicle and periplastidial-membrane records supply boundary
  context only; they are not additional review targets or dispositions of their findings.
- Fresh and reused source snapshots retain actual access timestamps and inspection
  tiers. Authority identity does not independently establish structure membership,
  mechanistic action, species-wide generalization or assembly necessity.
- 'All twenty native protein commands returned zero. Endosome membrane has one UNANCHORED_WITH_UNIPROT
  Vps27 node with verified P40343 xref. Esterosome has two reviewed examples, cryS/P21837
  and D2/P18142, and one COVERED node. Exoneme has two reviewed component examples
  SUB1/O61142 and PMX/Q8IAS0 and three typed nodes: two COVERED plus an UNANCHORED_WITH_UNIPROT
  substrate-cohort node with Q9TY95/Q8I0U8 xrefs. Eyespot has two unreviewed examples
  and one COVERED node. Ferrosome has three unreviewed DMR/Fez examples and one COVERED
  node. The other five targets have empty represented inventories and zero typed molecular
  nodes. These checks do not certify all narrative claims or prove membership.'
- Two inherited minor epiplastidial-membrane findings concern direct adjacent-space
  wording and a mechanistic label on a descriptive boundary graph. One inherited minor
  exoneme finding concerns an exact SUB1 family mapping now supported by IPR017314;
  a catalytic domain or broad PMX family does not resolve the same question.
- 'The two issue-bearing targets need curation; the other eight have qualified positive
  assessments. Native-validator issue #2514 is reused and remains open. Scientific
  findings remain separate from the bundle fixes.'
- Ferrosome formation/genetic evidence in RS-1 is distinguished from the iron-starvation
  fitness result in Shewanella putrefaciens CN32. No universal fitness phenotype or
  individual Fez necessity is inferred. Heterologous expression in E. coli is not
  native matched-host expression-dataset coverage.
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T013714Z-endosome-lumen-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T013715Z-endosome-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T013716Z-epiplastidial-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T013717Z-er-to-golgi-transport-vesicle-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T013717Z-esterosome-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T013718Z-esterosome-lumen-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T013719Z-esterosome-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T013720Z-exoneme-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T013720Z-eyespot-apparatus-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T013721Z-ferrosome-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
links:
- https://github.com/CultureBotAI/CellStructureMech/pull/2365
- https://github.com/CultureBotAI/CellStructureMech/issues/2514
- https://github.com/CultureBotAI/CellStructureMech/issues/2690
- https://github.com/CultureBotAI/CellStructureMech/issues/2691
- https://github.com/CultureBotAI/CellStructureMech/issues/2692
- https://github.com/CultureBotAI/CellStructureMech/issues/2693
- https://github.com/CultureBotAI/CellStructureMech/issues/2694
```
