# PR 2362: current-input review of ten records and adversarial follow-up

- Review: 20261103T115912Z-pr2362-current-record-followup
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-11-03T11:50:42.116655Z
- Finished UTC: 2026-11-03T11:59:12Z
- Reviewer: Codex root synthesis with three independent read-only adversarial reviewers (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Current-input reassessment of all ten records in PR2362. One stale cyanelle review is substantively refreshed and four structured-source applicability assessments are corrected. Independent source review identifies one minor new cyanelle GO-provenance finding for separate curation; no records are edited.

## Scope And Provenance

Exact ten-record PR cohort reassessed against current main 41d0d30a456e5f1af1417f23afa89bc4fa0674ba. Changed inputs are substantively reassessed. Scientific records remain unchanged.

Selection: Complete cohort of ten maintained records reviewed in original PR head 1d0845adece5711c9a194abadaf80aeec1eb8b50.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base ed8281f2fc915349c8ce429e7103e42b256c0533.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0033107 | data/structures/membrane_organelle/cvt_vesicle.yaml | maintained | Cvt vesicle |
| cellstructuremech:cvt_vesicle_lumen | data/structures/membrane_organelle/cvt_vesicle_lumen.yaml | maintained | Cvt vesicle lumen |
| GO:0033110 | data/structures/membrane_organelle/cvt_vesicle_membrane.yaml | maintained | Cvt vesicle membrane |
| GO:0009842 | data/structures/membrane_organelle/cyanelle.yaml | maintained | cyanelle |
| GO:0033112 | data/structures/membrane_organelle/cyanelle_envelope.yaml | maintained | cyanelle envelope |
| GO:0036012 | data/structures/membrane_organelle/cyanelle_inner_membrane.yaml | maintained | cyanelle inner membrane |
| GO:0036014 | data/structures/membrane_organelle/cyanelle_intermembrane_space.yaml | maintained | cyanelle intermembrane space |
| GO:0033113 | data/structures/membrane_organelle/cyanelle_membrane.yaml | maintained | cyanelle membrane |
| GO:0036013 | data/structures/membrane_organelle/cyanelle_outer_membrane.yaml | maintained | cyanelle outer membrane |
| GO:0034060 | data/structures/membrane_organelle/cyanelle_stroma.yaml | maintained | cyanelle stroma |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full native QC | passed | True | GO:0033107, cellstructuremech:cvt_vesicle_lumen, GO:0033110, GO:0009842, GO:0033112, GO:0036012, GO:0036014, GO:0033113, GO:0036013, GO:0034060 | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| Native label correspondence | passed | True | GO:0033107, cellstructuremech:cvt_vesicle_lumen, GO:0033110, GO:0009842, GO:0033112, GO:0036012, GO:0036014, GO:0033113, GO:0036013, GO:0034060 | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| TraitMech references | passed | True | GO:0033107, cellstructuremech:cvt_vesicle_lumen, GO:0033110, GO:0009842, GO:0033112, GO:0036012, GO:0036014, GO:0033113, GO:0036013, GO:0034060 | Native TraitMech link check passed. |
| Pinned governed files | passed | True | GO:0033107, cellstructuremech:cvt_vesicle_lumen, GO:0033110, GO:0009842, GO:0033112, GO:0036012, GO:0036014, GO:0033113, GO:0036013, GO:0034060 | Pinned governed files match; native vendored check passed. |
| Native identifier resolver | passed | True | GO:0033107, cellstructuremech:cvt_vesicle_lumen, GO:0033110, GO:0009842, GO:0033112, GO:0036012, GO:0036014, GO:0033113, GO:0036013, GO:0034060 | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| validate GO:0033107 | passed | True | GO:0033107 | Documented focused command passed. |
| validate-strict GO:0033107 | passed | True | GO:0033107 | Documented focused command passed. |
| validate cellstructuremech:cvt_vesicle_lumen | passed | True | cellstructuremech:cvt_vesicle_lumen | Documented focused command passed. |
| validate-strict cellstructuremech:cvt_vesicle_lumen | passed | True | cellstructuremech:cvt_vesicle_lumen | Documented focused command passed. |
| validate GO:0033110 | passed | True | GO:0033110 | Documented focused command passed. |
| validate-strict GO:0033110 | passed | True | GO:0033110 | Documented focused command passed. |
| validate GO:0009842 | passed | True | GO:0009842 | Documented focused command passed. |
| validate-strict GO:0009842 | passed | True | GO:0009842 | Documented focused command passed. |
| validate GO:0033112 | passed | True | GO:0033112 | Documented focused command passed. |
| validate-strict GO:0033112 | passed | True | GO:0033112 | Documented focused command passed. |
| validate GO:0036012 | passed | True | GO:0036012 | Documented focused command passed. |
| validate-strict GO:0036012 | passed | True | GO:0036012 | Documented focused command passed. |
| validate GO:0036014 | passed | True | GO:0036014 | Documented focused command passed. |
| validate-strict GO:0036014 | passed | True | GO:0036014 | Documented focused command passed. |
| validate GO:0033113 | passed | True | GO:0033113 | Documented focused command passed. |
| validate-strict GO:0033113 | passed | True | GO:0033113 | Documented focused command passed. |
| validate GO:0036013 | passed | True | GO:0036013 | Documented focused command passed. |
| validate-strict GO:0036013 | passed | True | GO:0036013 | Documented focused command passed. |
| validate GO:0034060 | passed | True | GO:0034060 | Documented focused command passed. |
| validate-strict GO:0034060 | passed | True | GO:0034060 | Documented focused command passed. |
| Supplemental bounded PMID authority checks | passed | True | GO:0033107, cellstructuremech:cvt_vesicle_lumen, GO:0033110, GO:0009842, GO:0033112, GO:0036012, GO:0036014, GO:0033113, GO:0036013, GO:0034060 | 909 PMIDs all OK in bounded native requests; full-command limitations remain separate. |
| Official structured-source applicability and covered-dataset cross-checks | passed | False | GO:0033107, cellstructuremech:cvt_vesicle_lumen, GO:0033110, GO:0009842, GO:0033112, GO:0036012, GO:0036014, GO:0033113, GO:0036013, GO:0034060 | Four unsupported expression-only applicability exclusions are corrected: the three Cvt carrier/lumen/membrane records name Cvt or early-secretory pathway and molecular context, and whole cyanelle asserts photosynthesis. Six cyanelle boundary/material records remain genuine exclusions after full-claim inspection. Complete official catalogue coverage has no matching relevant yeast or Cyanophora dataset; no unrelated organism or downstream module query substitutes for noncoverage. Resource noncoverage is not biological absence. The retained historical runner failure is not a fresh invocation. |
| Independent claim-level source review | passed | True | GO:0033107, cellstructuremech:cvt_vesicle_lumen, GO:0033110, GO:0009842, GO:0033112, GO:0036012, GO:0036014, GO:0033113, GO:0036013, GO:0034060 | Three read-only reviewers covered the complete ten-record cohort, including changed inputs, with explicit scientific findings and source-access limits. Final artifact/head acceptance occurs after saving. |
| Retained historical adapter runner availability | unavailable | False | GO:0033107, cellstructuremech:cvt_vesicle_lumen, GO:0033110, GO:0009842 | Historical 00:49Z invocation unavailable due to OS access restriction. Official catalogue source fallback was inspected separately; no current invocation or successful adapter execution is claimed. The actual historical exit code 1 is retained in the evidence receipt, since the native unavailable-check model has no execution exit-code field. |
| Native cvt vesicle UniProt verify check | passed | True | GO:0033107 | Read-only native command returned zero on an empty represented protein inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native cvt vesicle UniProt causal check | passed | True | GO:0033107 | Read-only native command returned zero on an empty represented protein inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native cvt vesicle lumen UniProt verify check | passed | True | cellstructuremech:cvt_vesicle_lumen | Read-only native command returned zero on an empty represented protein inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native cvt vesicle lumen UniProt causal check | passed | True | cellstructuremech:cvt_vesicle_lumen | Read-only native command returned zero on an empty represented protein inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native cvt vesicle membrane UniProt verify check | passed | True | GO:0033110 | Read-only native command returned zero on an empty represented protein inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native cvt vesicle membrane UniProt causal check | passed | True | GO:0033110 | Read-only native command returned zero on an empty represented protein inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native cyanelle UniProt verify check | passed | True | GO:0009842 | Read-only native command returned zero on an empty represented protein inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native cyanelle UniProt causal check | passed | True | GO:0009842 | Read-only native command returned zero on an empty represented protein inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native cyanelle envelope UniProt verify check | passed | True | GO:0033112 | Read-only native command returned zero on an empty represented protein inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native cyanelle envelope UniProt causal check | passed | True | GO:0033112 | Read-only native command returned zero on an empty represented protein inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native cyanelle inner membrane UniProt verify check | passed | True | GO:0036012 | Read-only native command returned zero on an empty represented protein inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native cyanelle inner membrane UniProt causal check | passed | True | GO:0036012 | Read-only native command returned zero on an empty represented protein inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native cyanelle intermembrane space UniProt verify check | passed | True | GO:0036014 | Read-only native command returned zero on an empty represented protein inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native cyanelle intermembrane space UniProt causal check | passed | True | GO:0036014 | Read-only native command returned zero on an empty represented protein inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native cyanelle membrane UniProt verify check | passed | True | GO:0033113 | Read-only native command returned zero on an empty represented protein inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native cyanelle membrane UniProt causal check | passed | True | GO:0033113 | Read-only native command returned zero on an empty represented protein inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native cyanelle outer membrane UniProt verify check | passed | True | GO:0036013 | Read-only native command returned zero on an empty represented protein inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native cyanelle outer membrane UniProt causal check | passed | True | GO:0036013 | Read-only native command returned zero on an empty represented protein inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native cyanelle stroma UniProt verify check | passed | True | GO:0034060 | Read-only native command returned zero on an empty represented protein inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native cyanelle stroma UniProt causal check | passed | True | GO:0034060 | Read-only native command returned zero on an empty represented protein inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |

## Scientific And Domain Assessments

### Native protein and graph inventories

schema: supported. Targets: GO:0036012.

Both commands pass empty represented protein inventories and zero GENE_OR_PROTEIN nodes. These are mechanical checks, not independent certification of paper biology or an exhaustive membrane proteome.

### Original lineage and unchanged frozen record

provenance: supported. Targets: GO:0036012.

Original validates/renders exactly and all historical input hashes match. Current target is unchanged; no stale input requires refresh. Original findings/actions are empty. Historical record issues are context only, not reclosed or recertified.

### Entire maintained record and bounded science

completeness: supported. Targets: GO:0036012.

All maintained fields, histories, discussions and graph edges read. No images, snippets, quantitative properties or named protein examples are represented. Optional protein inventories are not fabricated and no scientific curation defect established at declared evidence tiers.

### Exact organism/class and qualitative occurrence

scope: supported. Targets: GO:0036012.

ENA verifies C.paradoxa2762 and Glaucocystophyceae38254 including Glaucophyta synonym. COMMON is qualitative defining organization, not a sampled numerical prevalence or identical composition in every life stage. Primary culture observations remain strain-specific.

### Collective material versus particular molecule necessity

evidence: unknown. Targets: GO:0036012.

Morphology and localization do not establish that an individual lipid species, PG modification or protein is necessary for formation. Such claims are not made here. ESSENTIAL bilayer entries are constitutional collective material; IMS PG essentiality is explicitly UNKNOWN.

### Primary scans and limited biochemical evidence

provenance: supported. Targets: GO:0036012.

Fresh Giddings scans409/414/416/417 were independently viewed, including source text and figures; no full-paper or raw-image reanalysis. Pfanzagl primary-structure evidence is complete abstract only. Historical presumed PG/LPS chemistry and endosymbiont wording are not generalized into new molecular or evolutionary claims.

### Native protein and graph inventories

schema: supported. Targets: GO:0036014.

Both commands pass empty represented protein inventories and zero GENE_OR_PROTEIN nodes. These are mechanical checks, not independent certification of paper biology or an exhaustive membrane proteome.

### Original lineage and unchanged frozen record

provenance: supported. Targets: GO:0036014.

Original validates/renders exactly and all historical input hashes match. Current target is unchanged; no stale input requires refresh. Original findings/actions are empty. Historical record issues are context only, not reclosed or recertified.

### Entire maintained record and bounded science

completeness: supported. Targets: GO:0036014.

All maintained fields, histories, discussions and graph edges read. No images, snippets, quantitative properties or named protein examples are represented. Optional protein inventories are not fabricated and no scientific curation defect established at declared evidence tiers.

### Exact organism/class and qualitative occurrence

scope: supported. Targets: GO:0036014.

ENA verifies C.paradoxa2762 and Glaucocystophyceae38254 including Glaucophyta synonym. COMMON is qualitative defining organization, not a sampled numerical prevalence or identical composition in every life stage. Primary culture observations remain strain-specific.

### Collective material versus particular molecule necessity

evidence: unknown. Targets: GO:0036014.

Morphology and localization do not establish that an individual lipid species, PG modification or protein is necessary for formation. Such claims are not made here. ESSENTIAL bilayer entries are constitutional collective material; IMS PG essentiality is explicitly UNKNOWN.

### Primary scans and limited biochemical evidence

provenance: supported. Targets: GO:0036014.

Fresh Giddings scans409/414/416/417 were independently viewed, including source text and figures; no full-paper or raw-image reanalysis. Pfanzagl primary-structure evidence is complete abstract only. Historical presumed PG/LPS chemistry and endosymbiont wording are not generalized into new molecular or evolutionary claims.

### Native protein and graph inventories

schema: supported. Targets: GO:0033113.

Both commands pass empty represented protein inventories and zero GENE_OR_PROTEIN nodes. These are mechanical checks, not independent certification of paper biology or an exhaustive membrane proteome.

### Original lineage and unchanged frozen record

provenance: supported. Targets: GO:0033113.

Original validates/renders exactly and all historical input hashes match. Current target is unchanged; no stale input requires refresh. Original findings/actions are empty. Historical record issues are context only, not reclosed or recertified.

### Entire maintained record and bounded science

completeness: supported. Targets: GO:0033113.

All maintained fields, histories, discussions and graph edges read. No images, snippets, quantitative properties or named protein examples are represented. Optional protein inventories are not fabricated and no scientific curation defect established at declared evidence tiers.

### Exact organism/class and qualitative occurrence

scope: supported. Targets: GO:0033113.

ENA verifies C.paradoxa2762 and Glaucocystophyceae38254 including Glaucophyta synonym. COMMON is qualitative defining organization, not a sampled numerical prevalence or identical composition in every life stage. Primary culture observations remain strain-specific.

### Collective material versus particular molecule necessity

evidence: unknown. Targets: GO:0033113.

Morphology and localization do not establish that an individual lipid species, PG modification or protein is necessary for formation. Such claims are not made here. ESSENTIAL bilayer entries are constitutional collective material; IMS PG essentiality is explicitly UNKNOWN.

### Primary scans and limited biochemical evidence

provenance: supported. Targets: GO:0033113.

Fresh Giddings scans409/414/416/417 were independently viewed, including source text and figures; no full-paper or raw-image reanalysis. Pfanzagl primary-structure evidence is complete abstract only. Historical presumed PG/LPS chemistry and endosymbiont wording are not generalized into new molecular or evolutionary claims.

### Native protein and graph inventories

schema: supported. Targets: GO:0036013.

Both commands pass empty represented protein inventories and zero GENE_OR_PROTEIN nodes. These are mechanical checks, not independent certification of paper biology or an exhaustive membrane proteome.

### Original lineage and unchanged frozen record

provenance: supported. Targets: GO:0036013.

Original validates/renders exactly and all historical input hashes match. Current target is unchanged; no stale input requires refresh. Original findings/actions are empty. Historical record issues are context only, not reclosed or recertified.

### Entire maintained record and bounded science

completeness: supported. Targets: GO:0036013.

All maintained fields, histories, discussions and graph edges read. No images, snippets, quantitative properties or named protein examples are represented. Optional protein inventories are not fabricated and no scientific curation defect established at declared evidence tiers.

### Exact organism/class and qualitative occurrence

scope: supported. Targets: GO:0036013.

ENA verifies C.paradoxa2762 and Glaucocystophyceae38254 including Glaucophyta synonym. COMMON is qualitative defining organization, not a sampled numerical prevalence or identical composition in every life stage. Primary culture observations remain strain-specific.

### Collective material versus particular molecule necessity

evidence: unknown. Targets: GO:0036013.

Morphology and localization do not establish that an individual lipid species, PG modification or protein is necessary for formation. Such claims are not made here. ESSENTIAL bilayer entries are constitutional collective material; IMS PG essentiality is explicitly UNKNOWN.

### Primary scans and limited biochemical evidence

provenance: supported. Targets: GO:0036013.

Fresh Giddings scans409/414/416/417 were independently viewed, including source text and figures; no full-paper or raw-image reanalysis. Pfanzagl primary-structure evidence is complete abstract only. Historical presumed PG/LPS chemistry and endosymbiont wording are not generalized into new molecular or evolutionary claims.

### Exact compartment, parentage and source scope

identity: supported. Targets: GO:0036012.

Exact GO0036012/SL0480 identify the stroma-facing inner envelope membrane, exact inner-envelope synonym, plastid-inner and generic cyanelle-membrane parents and envelope parthood.

### Exact compartment, parentage and source scope

identity: supported. Targets: GO:0036014.

Exact GO0036014/SL0481 identify the PG-containing intermembrane region; both GO synonyms are exact. Plastid-IMS is is_a and envelope is the containing structure; region is distinct from its boundaries and stroma.

### Exact compartment, parentage and source scope

identity: supported. Targets: GO:0033113.

GO0033113 identifies either envelope bilayer, with plastid-membrane parent and envelope parthood. SL0083 has broader unresolved outer/inner/thylakoid localization scope; maintained evidence explicitly caveats this and correctly omits an exact xref.

### Exact compartment, parentage and source scope

identity: supported. Targets: GO:0036013.

Exact GO0036013/SL0482 identify the cytoplasm-facing outer membrane; generic cyanelle/plastid-outer parents and envelope parthood agree. Native source definitions distinguish outer membrane from whole envelope, PG layer and IMS.

### Material constituent and honest unresolved grounding

grounding: supported. Targets: GO:0036012.

Collective inner lipid bilayer is defining membrane material, not a single chemical species. REVIEWED_LABEL_ONLY and the existing grounding TODO retain specificity honestly; the whole-membrane GO identifier is not misused as an exact chemical ID.

### Material constituent and honest unresolved grounding

grounding: supported. Targets: GO:0036014.

PG is a structural layer in the IMS, not a single muropeptide or a membrane-bounded compartment. Direct GO/SL placement and primary chemistry support its presence. UNKNOWN essentiality and explicit material-layer grounding TODO avoid guessed IDs or implied biogenesis necessity.

### Material constituent and honest unresolved grounding

grounding: supported. Targets: GO:0033113.

Generic collective envelope lipid bilayer is constitutional material when inner/outer identity is unspecified. GO envelope-only scope excludes thylakoid membrane; broader SL fallback is not treated as exact constituent identity.

### Material constituent and honest unresolved grounding

grounding: supported. Targets: GO:0036013.

The outer lipid bilayer is collective material. Kojima protein localization is bounded contextual support for the exterior membrane boundary, not identification of a specific lipid or evidence that CppS/F is universally required to form it.

### Complete descriptive graph

graph: supported. Targets: GO:0036012.

All three NONMECHANISTIC edges represent envelope parthood and the stroma/IMS boundaries. Exact GO/SL and inspected envelope ultrastructure support the geometry; no import machinery or photosystem mechanism is asserted.

### Complete descriptive graph

graph: supported. Targets: GO:0036014.

Outer and inner membrane delimit the region; structural PG resides within it. component_ref points to the actual PG material, not a gene/protein. All three NONMECHANISTIC relations agree with GO/SL and chemistry, without transport or PG-remodeling mechanisms.

### Complete descriptive graph

graph: supported. Targets: GO:0033113.

Three descriptive relations state generic membrane partOf envelope and inner/outer is_a generic membrane. Direct typed GO children support them; component_ref identifies collective material without substituting a protein identity. Thylakoid is explicitly excluded.

### Complete descriptive graph

graph: supported. Targets: GO:0036013.

Envelope parthood, cytoplasm-facing orientation and outer boundary of the IMS are source-supported. GO/SL geometry plus Kojima exterior localization agree, without equating membrane with PG or claiming transport kinetics.

### PG distribution across the named genera

evidence: supported. Targets: GO:0036014.

PMID8955325 primary abstract directly reports Glaucocystis nostochinearum and Cyanoptyche gloeocystis PG analysis with prior Cyanophora comparison. This supports the three named genera in the class-level note, not every glaucophyte strain or a universal quantified chemical recipe. C.paradoxa canonical example is the separate primary-structure study.

### Exterior protein localization and distinct experimental assays

evidence: supported. Targets: GO:0036013.

Kojima NIES547 fractionation, PG/protein preparations, microscopy/pigment support and separate outer-membrane preparation support the record’s narrow localization note. Primary proteoliposome channel assays are separate from live-cell rates or formation necessity. The record does not assert a complete CppS/F inventory or import mechanistic/evolutionary title claims wholesale.

### Genuine material and topology applicability exclusion

scope: not_applicable. Targets: GO:0036012.

Inner membrane describes collective lipid material and stroma/IMS topology; no named molecular identity, regulator, pathway, stress response, trait or dataset is asserted. Its absent original adapter row does not create a defect when applicability is genuinely absent. Fresh complete catalogue also has no Cyanophora/glaucophyte host. No unmatched bacterial/cyanobacterial dataset, missing inventory or biological absence is inferred; historical runner remains separately dated.

### Genuine material and topology applicability exclusion

scope: not_applicable. Targets: GO:0036014.

IMS describes PG as a material layer and comparative structural occurrence, not PG biosynthesis/remodeling machinery, a regulator or stress-response trait. No positive molecular/pathway trigger is asserted; the absent original row alone is not a defect. Fresh complete catalogue also has no Cyanophora/glaucophyte host. No unmatched bacterial/cyanobacterial dataset, missing inventory or biological absence is inferred; historical runner remains separately dated.

### Genuine material and topology applicability exclusion

scope: not_applicable. Targets: GO:0033113.

Generic membrane describes envelope lipid material and localization-class boundaries. The broader SL fallback mentions unresolved protein locations but asserts no named protein or pathway. Retain genuine N/A with this concrete scope rationale; do not count its earlier expression-only wording as a defect when no trigger exists. Fresh complete catalogue also has no Cyanophora/glaucophyte host. No unmatched bacterial/cyanobacterial dataset, missing inventory or biological absence is inferred; historical runner remains separately dated.

### Genuine material and topology applicability exclusion

scope: not_applicable. Targets: GO:0036013.

Outer membrane cites generic protein-localization experiments as topology context but names no constituent gene/protein, regulator, pathway or stress-response mechanism. A paper title mentioning diffusion channels is bibliographic context, not a target assertion of channel machinery. Genuine N/A is retained with this scope rationale. Fresh complete catalogue also has no Cyanophora/glaucophyte host. No unmatched bacterial/cyanobacterial dataset, missing inventory or biological absence is inferred; historical runner remains separately dated.

### Exact structure and boundary identity

identity: supported. Targets: GO:0009842.

GO0009842 denotes the whole glaucophyte photosynthetic plastid, with valid plastid is-a and envelope/stroma/thylakoid parthood; exact synonyms and native status are preserved.

### Qualitative occurrence versus experimental scope

scope: supported. Targets: GO:0009842.

Species2762 and class38254 are current verified authorities. COMMON is characteristic qualitative anatomy, not measured prevalence; canonical C.paradoxa is species-level illustration of paper-specific experimental material. Giddings used UTEX LB555; Kojima NIES547; Price genome study CCMP329. Native authorities support defining glaucophyte anatomy; no claim of every species being experimentally tested.

### Constituents, optional content and necessity

completeness: supported. Targets: GO:0009842.

Three lipid-bilayer rows identify constituent membranes; PG sheet is reviewed-label-only with an explicit unresolved exact-grounding discussion. UNKNOWN essentiality is not a missing knockout assertion. The record does not promise a complete molecular stoichiometry/inventory.

### Empty native protein checks

schema: supported. Targets: GO:0009842.

Both actual native commands exited0 on the current source. Empty declared accession inventories and zero GENE_OR_PROTEIN nodes make this a bounded representation check, not an exhaustive protein search, identity verification, biochemical-membership or assembly-necessity finding.

### Original hashes, native pair integrity and lineage

provenance: supported. Targets: GO:0009842.

Only this target is stale in my slice: original source hash24275c8050ca5d13c66d563c7aa697a4de65766f87499f876fc94c41cd2f0db7 changed to5ebb2c3b4cc2d9364dc08ac335c793409014f30f0ca009ee3b4aeafb860371b6. A new history event and three topological edges were fully reassessed; original five-edge review remains historical. Original native validation/render match; all three original scientific findings/actions were empty, so no predecessor finding or historical issue is terminally resolved by this review.

### Claim support and source-access limits

evidence: supported. Targets: GO:0009842.

Current source review uses native authority definitions, six visually inspected Giddings scans, Pfanzagl primary-structure and comparative abstracts, bounded genuine Kojima body, and bounded Price JATS. Price and GO support photosynthetic function; Giddings morphology alone is not used as the sole proof of physiological function. Historical terminology, microscopy preparation effects, literature-cited context and actual strain scopes remain qualified; no new molecular necessity or universal prevalence claims are made.

### Images, measurements and verbatim snippets

evidence: not_applicable. Targets: GO:0009842.

The entire current target has no image entry or measured property needing verification and no verbatim snippet asserted. Source scans were nonetheless visually inspected where morphology was assessed; no new measurements or image attribution are imputed to the record.

### Status and curation ownership

provenance: supported. Targets: GO:0009842.

Record remains PROPOSED. History is treated as context, not certification of old correctness or automatic closure of another issue/category. This read-only review edits no record or history; any scientific correction belongs to a separate guarded-writer curation change.

### Exact structure and boundary identity

identity: supported. Targets: GO:0033112.

GO0033112 denotes the complete double-membrane envelope including IMS, with plastid-envelope is-a and cyanelle parthood; distinct from either single bilayer.

### Qualitative occurrence versus experimental scope

scope: supported. Targets: GO:0033112.

Species2762 and class38254 are current verified authorities. COMMON is characteristic qualitative anatomy, not measured prevalence; canonical C.paradoxa is species-level illustration of paper-specific experimental material. Giddings used UTEX LB555; Kojima NIES547; Price genome study CCMP329. The envelope explicitly names Glaucocystis/Cyanoptyche/Cyanophora, supported by PMID8955325 abstract, not extrapolated from a single species.

### Constituents, optional content and necessity

completeness: supported. Targets: GO:0033112.

Outer/inner bilayers and PG sheet are material components, not proteins; broad IMS is not substituted for PG-sheet identity. UNKNOWN essentiality avoids inferring assembly necessity from occurrence or biochemical localization. The envelope record does not assert an unrecorded named transport mechanism.

### Empty native protein checks

schema: supported. Targets: GO:0033112.

Both actual native commands exited0 on the current source. Empty declared accession inventories and zero GENE_OR_PROTEIN nodes make this a bounded representation check, not an exhaustive protein search, identity verification, biochemical-membership or assembly-necessity finding.

### Original hashes, native pair integrity and lineage

provenance: supported. Targets: GO:0033112.

Current target bytes match the original frozen input. Original native validation/render match; all three original scientific findings/actions were empty, so no predecessor finding or historical issue is terminally resolved by this review.

### Claim support and source-access limits

evidence: supported. Targets: GO:0033112.

Current source review uses native authority definitions, six visually inspected Giddings scans, Pfanzagl primary-structure and comparative abstracts, bounded genuine Kojima body, and bounded Price JATS. Historical terminology, microscopy preparation effects, literature-cited context and actual strain scopes remain qualified; no new molecular necessity or universal prevalence claims are made.

### Images, measurements and verbatim snippets

evidence: not_applicable. Targets: GO:0033112.

The entire current target has no image entry or measured property needing verification and no verbatim snippet asserted. Source scans were nonetheless visually inspected where morphology was assessed; no new measurements or image attribution are imputed to the record.

### Status and curation ownership

provenance: supported. Targets: GO:0033112.

Record remains PROPOSED. History is treated as context, not certification of old correctness or automatic closure of another issue/category. This read-only review edits no record or history; any scientific correction belongs to a separate guarded-writer curation change.

### Exact structure and boundary identity

identity: supported. Targets: GO:0034060.

GO0034060 and SL0350 denote the stromal compartment excluding thylakoid lumen, with plastid-stroma is-a and cyanelle parthood. It is a region, not a protein or membrane.

### Qualitative occurrence versus experimental scope

scope: supported. Targets: GO:0034060.

Species2762 and class38254 are current verified authorities. COMMON is characteristic qualitative anatomy, not measured prevalence; canonical C.paradoxa is species-level illustration of paper-specific experimental material. Giddings used UTEX LB555; Kojima NIES547; Price genome study CCMP329. Native authorities support defining glaucophyte anatomy; no claim of every species being experimentally tested.

### Constituents, optional content and necessity

completeness: supported. Targets: GO:0034060.

No component or protein inventory is declared. Its resolved discussion explicitly distinguishes DNA/ribosomes/photosynthetic products as possible compartment contents and withholds inventory expansion; omission of optional content-level slots is not a consequential defect.

### Empty native protein checks

schema: supported. Targets: GO:0034060.

Both actual native commands exited0 on the current source. Empty declared accession inventories and zero GENE_OR_PROTEIN nodes make this a bounded representation check, not an exhaustive protein search, identity verification, biochemical-membership or assembly-necessity finding.

### Original hashes, native pair integrity and lineage

provenance: supported. Targets: GO:0034060.

Current target bytes match the original frozen input. Original native validation/render match; all three original scientific findings/actions were empty, so no predecessor finding or historical issue is terminally resolved by this review.

### Claim support and source-access limits

evidence: supported. Targets: GO:0034060.

Current source review uses native authority definitions, six visually inspected Giddings scans, Pfanzagl primary-structure and comparative abstracts, bounded genuine Kojima body, and bounded Price JATS. Historical terminology, microscopy preparation effects, literature-cited context and actual strain scopes remain qualified; no new molecular necessity or universal prevalence claims are made.

### Images, measurements and verbatim snippets

evidence: not_applicable. Targets: GO:0034060.

The entire current target has no image entry or measured property needing verification and no verbatim snippet asserted. Source scans were nonetheless visually inspected where morphology was assessed; no new measurements or image attribution are imputed to the record.

### Status and curation ownership

provenance: supported. Targets: GO:0034060.

Record remains PROPOSED. History is treated as context, not certification of old correctness or automatic closure of another issue/category. This read-only review edits no record or history; any scientific correction belongs to a separate guarded-writer curation change.

### Eight topological edges and stale three-edge refresh

graph: concern. Targets: GO:0009842.

The retained outer-facing/inner-stroma boundary, PG-in-IMS, thylakoid-membrane parthood and photosynthesis support remain bounded NONMECHANISTIC topology. Newly added stroma→cyanelle parthood is a direct GO relation; thylakoid→stroma residency is supported by GO context and Giddings/Price morphology. Newly added IMS→cyanelle parthood is valid transitively through envelope. Its evidence note wrongly labels that GO relationship direct: F1 is a minor attribution correction, not rejection of the anatomical edge.

### Six NONMECHANISTIC envelope edges

graph: supported. Targets: GO:0033112.

Whole/envelope parthood, outer/inner subdivision, inner boundary to stroma, IMS within envelope and PG within IMS agree with exact authorities and scoped primary evidence. No gene/protein necessity, direct molecular interaction or transport mechanism is asserted.

### Two NONMECHANISTIC stromal edges

graph: supported. Targets: GO:0034060.

Stroma part_of whole cyanelle and inner membrane bounds stroma are supported by current GO and SL0480. The inner membrane separates stroma from IMS, and thylakoid lumen is excluded. No arbitrary composition or biochemical causal mechanism is inferred.

### Named pathway triggers actual structured-source assessment

evidence: concern. Targets: GO:0009842.

Whole cyanelle explicitly names photosynthesisGO0015979, so the original no-transcriptomic-inference rationale is insufficient. Current real catalogue inspection finds no matching glaucophyte organism/dataset; bacterial Synechococcus is not a proxy. Native runner historical unavailability and current public-source fallback are distinguished. No applicable matched dataset remains to search/summarize; no biological inference follows from this catalogue absence.

### Genuine structural/material applicability exclusion

evidence: not_applicable. Targets: GO:0033112.

The reviewed current content asserts material identity, compartment boundaries and qualitative occurrence, not a named gene/locus/accession/regulator/pathway/stress/trait/transcriptomics claim requiring a gene-module query. Bibliographic titles, localization evidence and expressly deferred stromal contents do not create an asserted molecular mechanism. No separate omission finding is warranted merely because the original N/A wording mentioned expression. Whole cyanelle pathway applicability is assessed separately.

### Genuine structural/material applicability exclusion

evidence: not_applicable. Targets: GO:0034060.

The reviewed current content asserts material identity, compartment boundaries and qualitative occurrence, not a named gene/locus/accession/regulator/pathway/stress/trait/transcriptomics claim requiring a gene-module query. Bibliographic titles, localization evidence and expressly deferred stromal contents do not create an asserted molecular mechanism. No separate omission finding is warranted merely because the original N/A wording mentioned expression. Whole cyanelle pathway applicability is assessed separately.

### Original schema/render and unchanged frozen targets

schema: supported. Targets: GO:0033107.

Original native validate/render succeeds with deterministic Markdown and matching historical/current target hashes. No record change is needed to refresh this assessment.

### Actual empty protein inventory limits

provenance: supported. Targets: GO:0033107.

No protein examples or UniProtKB graph xrefs and zero GENE_OR_PROTEIN graph nodes. Execution success verifies only this empty represented inventory; it does not establish narrative Ape1/Ams1/Atg identity, localization, mechanism, complete composition or formation necessity.

### Images, measurements, traits and snippets

scope: not_applicable. Targets: GO:0033107.

The maintained record asserts none of these optional surfaces. Textual primary figure-caption inspection is not pixel inspection or raw-data reanalysis; no image-rights attestation is needed for absent target images.

### Original schema/render and unchanged frozen targets

schema: supported. Targets: cellstructuremech:cvt_vesicle_lumen.

Original native validate/render succeeds with deterministic Markdown and matching historical/current target hashes. No record change is needed to refresh this assessment.

### Actual empty protein inventory limits

provenance: supported. Targets: cellstructuremech:cvt_vesicle_lumen.

No protein examples or UniProtKB graph xrefs and zero GENE_OR_PROTEIN graph nodes. Execution success verifies only this empty represented inventory; it does not establish narrative Ape1/Ams1/Atg identity, localization, mechanism, complete composition or formation necessity.

### Images, measurements, traits and snippets

scope: not_applicable. Targets: cellstructuremech:cvt_vesicle_lumen.

The maintained record asserts none of these optional surfaces. Textual primary figure-caption inspection is not pixel inspection or raw-data reanalysis; no image-rights attestation is needed for absent target images.

### Original schema/render and unchanged frozen targets

schema: supported. Targets: GO:0033110.

Original native validate/render succeeds with deterministic Markdown and matching historical/current target hashes. No record change is needed to refresh this assessment.

### Actual empty protein inventory limits

provenance: supported. Targets: GO:0033110.

No protein examples or UniProtKB graph xrefs and zero GENE_OR_PROTEIN graph nodes. Execution success verifies only this empty represented inventory; it does not establish narrative Ape1/Ams1/Atg identity, localization, mechanism, complete composition or formation necessity.

### Images, measurements, traits and snippets

scope: not_applicable. Targets: GO:0033110.

The maintained record asserts none of these optional surfaces. Textual primary figure-caption inspection is not pixel inspection or raw-data reanalysis; no image-rights attestation is needed for absent target images.

### Yeast model and condition-bounded occurrence

scope: supported. Targets: GO:0033107.

ENA validates S.cerevisiae identity. Reggiori and Shintani establish carrier context in named budding-yeast strains; COMMON is qualitative, not a measured prevalence or a claim of constant visible vesicles in every cell. Nutrient-rich Cvt transport, nitrogen-starvation/rapamycin autophagy and temperature-sensitive perturbations remain distinct.

### Actual structured-source applicability and unmatched host

scope: not_applicable. Targets: GO:0033107.

Affirmative Cvt/early-secretory pathway assertions trigger applicability inspection even though a graph is nonmechanistic or omits proteins. The complete current catalogue lacks a matching S.cerevisiae dataset, so downstream gene/module checks are not applicable. Historical runner failure is separate; catalogue noncoverage is not negative biology.

### Maintained status and original history

provenance: supported. Targets: GO:0033107.

PROPOSED status and all prior curation/history text remain unchanged. A fresh qualified review neither retrospectively certifies old execution/authorship nor terminally resolves historical issue references or the neighbor cargo record.

### Yeast model and condition-bounded occurrence

scope: supported. Targets: cellstructuremech:cvt_vesicle_lumen.

ENA validates S.cerevisiae identity. Reggiori and Shintani establish carrier context in named budding-yeast strains; COMMON is qualitative, not a measured prevalence or a claim of constant visible vesicles in every cell. Nutrient-rich Cvt transport, nitrogen-starvation/rapamycin autophagy and temperature-sensitive perturbations remain distinct.

### Actual structured-source applicability and unmatched host

scope: not_applicable. Targets: cellstructuremech:cvt_vesicle_lumen.

Affirmative Cvt/early-secretory pathway assertions trigger applicability inspection even though a graph is nonmechanistic or omits proteins. The complete current catalogue lacks a matching S.cerevisiae dataset, so downstream gene/module checks are not applicable. Historical runner failure is separate; catalogue noncoverage is not negative biology.

### Maintained status and original history

provenance: supported. Targets: cellstructuremech:cvt_vesicle_lumen.

PROPOSED status and all prior curation/history text remain unchanged. A fresh qualified review neither retrospectively certifies old execution/authorship nor terminally resolves historical issue references or the neighbor cargo record.

### Yeast model and condition-bounded occurrence

scope: supported. Targets: GO:0033110.

ENA validates S.cerevisiae identity. Reggiori and Shintani establish carrier context in named budding-yeast strains; COMMON is qualitative, not a measured prevalence or a claim of constant visible vesicles in every cell. Nutrient-rich Cvt transport, nitrogen-starvation/rapamycin autophagy and temperature-sensitive perturbations remain distinct.

### Actual structured-source applicability and unmatched host

scope: not_applicable. Targets: GO:0033110.

Affirmative Cvt/early-secretory pathway assertions trigger applicability inspection even though a graph is nonmechanistic or omits proteins. The complete current catalogue lacks a matching S.cerevisiae dataset, so downstream gene/module checks are not applicable. Historical runner failure is separate; catalogue noncoverage is not negative biology.

### Maintained status and original history

provenance: supported. Targets: GO:0033110.

PROPOSED status and all prior curation/history text remain unchanged. A fresh qualified review neither retrospectively certifies old execution/authorship nor terminally resolves historical issue references or the neighbor cargo record.

### Whole double-membrane carrier, cargo and bilayers

identity: supported. Targets: GO:0033107.

Exact GO0033107 definition and synonyms, cytoplasmic-vesicle parent and SL0080 mapping denote the complete carrier. GO0033110 is either individual bilayer; GO0034270 is the protein cargo complex. Whole enclosure is not attributed to a single bilayer.

### Membrane part and incorporated cargo complex

grounding: supported. Targets: GO:0033107.

The membrane row denotes a complete structural bilayer part; its LIPID type is collective material, not an asserted single lipid species. The Cvt-complex constituent is explicitly sequestered cargo, not a coat or a full assembly-machine census. GO exact identities and primary cargo inclusion support these bounded rows; species-specific complexes and transient actors are not silently conflated.

### Constitution versus empirical formation necessity

grounding: unknown. Targets: GO:0033107.

ESSENTIAL refers to the defining membrane material of the double-membrane carrier, not a named phospholipid removal experiment. Cargo UNKNOWN avoids upgrading conditional APE1/ATG19 deletion phenotypes into universal formation necessity. Molecular requirements and complete stoichiometry are not established by this descriptive record.

### Selective hydrolase cargo delivery

evidence: supported. Targets: GO:0033107.

GO0032258 and primary studies support selective cytoplasmic hydrolase enclosure and eventual fungal-vacuole delivery. Scott directly supports the Cvt19 receptor/prAPI binding context; Shintani explicitly supplies Atg19/Cvt19 nomenclature. The word review in one maintained Shintani note is treated as a verb, not a source-type claim: this is a primary experiment.

### Four descriptive edges at carrier scope

graph: supported. Targets: GO:0033107.

Membrane part_of whole carrier, cargo complex enclosed_by whole carrier, carrier supports Cvt pathway, and carrier delivers cargo_to fungal vacuole are supported. Bulk-cytoplasm exclusion is source-supported selective enclosure; no measured exclusion coefficient, universal size or complete receptor/scaffold/fusion mechanism is asserted.

### Explicitly incomplete Atg inventory

completeness: supported. Targets: GO:0033107.

The TODO distinguishes unrepresented Atg19/Atg11/Atg8/Atg9 machinery from the already represented membrane and cargo complex. The primary papers establish named actors and context; exact family uncertainty is not uncertainty that they exist. A descriptive carrier record does not assert exhaustive machinery or mechanism, and adding all transient actors as constituents would be unjustified. No consequential missing-required-representation defect is established in this review.

### Positive SL lumen identity with bounded GO candidates

identity: supported. Targets: cellstructuremech:cvt_vesicle_lumen.

SL0323 directly supports the local Cvt lumen definition, cytoplasmic-vesicle-lumen parent and carrier parthood. Bounded current GO candidates did not establish a conflicting exact mapping; no exhaustive absence claim is made. The ignored-inclusive exact-id search finds one maintained local record.

### Two mature-compartment relations

graph: supported. Targets: cellstructuremech:cvt_vesicle_lumen.

The mature cargo-containing compartment is part of the whole carrier and is bounded by its surrounding membrane at the source location scope. This describes the interior rather than asserting that either outer bilayer individually directly contacts cargo, or equating it with the intermembrane space/post-fusion Cvt body. No fusion, receptor/scaffold mechanism or soluble inventory is asserted.

### Canonical early-secretory requirement without invented molecular steps

scope: supported. Targets: cellstructuremech:cvt_vesicle_lumen.

The canonical example positively cites early-secretory requirements; Reggiori sec12/sec7 results support this condition-bounded pathway context. The graph expressly declines the receptor/scaffold/expansion mechanism. Its geometry-focused content does not erase that affirmative pathway assertion for adapter applicability.

### No declared molecular necessity

grounding: not_applicable. Targets: cellstructuremech:cvt_vesicle_lumen.

No molecular component or essentiality row is declared in this region record. The primary carrier evidence does not establish an independent lumen-assembly molecular inventory. No missing optional component row is treated as a defect.

### Either bilayer of the double-membrane carrier

identity: supported. Targets: GO:0033110.

GO0033110 and SL0081 denote either surrounding bilayer, with cytoplasmic-vesicle-membrane parentage and Cvt-carrier parthood. The maintained definition and pair-of-membranes graph preserve the double-membrane structure.

### Collective bilayer and limited chemical specificity

grounding: supported. Targets: GO:0033110.

The reviewed-label-only LIPID row describes collective bilayer material. Its notes and TODO acknowledge that no separate exact chemical constituent was curated; the membrane location is not falsely assigned as a molecular lipid identity. This review does not establish exhaustive chemical ontology absence or an exact species/abundance inventory.

### Unresolved individual lipid requirements

grounding: unknown. Targets: GO:0033110.

A bilayer is constitutive of the membrane definition, while empirical necessity of individual lipids or composition ratios is unassessed. Neither current primary article supplies a species-specific lipid removal/substitution assay; logical material constitution is not such an assay.

### Membrane contribution to selective carrier function

evidence: supported. Targets: GO:0033110.

The membrane surrounds the selective hydrolase carrier; it is not described as an enzyme or independent receptor. GO0032258 and primary cargo experiments support carrier context. A unique ER/Golgi membrane donor is explicitly not inferred from early-secretory perturbations.

### Three descriptive carrier-context edges

graph: supported. Targets: GO:0033110.

The graph specifies a pair of membranes and only individual membrane parthood, enclosure of Cvt complex by the complete vesicle, and carrier participation in targeting. Every edge has relevant authority/primary support; it does not collapse two bilayers or invent molecular membrane-expansion steps.

### Qualified positive scientific assessment

evidence: supported. Targets: GO:0033107.

No concrete scientific curation finding was established in this complete assigned-record scope. Original findings/actions were empty and remain so; qualified support retains source-body boundaries, incomplete molecular composition, conditional experiments, empty native inventories and dataset noncoverage. The identified adapter defect belongs to the original review bundle and is corrected through a successor.

### Qualified positive scientific assessment

evidence: supported. Targets: cellstructuremech:cvt_vesicle_lumen.

No concrete scientific curation finding was established in this complete assigned-record scope. Original findings/actions were empty and remain so; qualified support retains source-body boundaries, incomplete molecular composition, conditional experiments, empty native inventories and dataset noncoverage. The identified adapter defect belongs to the original review bundle and is corrected through a successor.

### Qualified positive scientific assessment

evidence: supported. Targets: GO:0033110.

No concrete scientific curation finding was established in this complete assigned-record scope. Original findings/actions were empty and remain so; qualified support retains source-body boundaries, incomplete molecular composition, conditional experiments, empty native inventories and dataset noncoverage. The identified adapter defect belongs to the original review bundle and is corrected through a successor.

### Complete frozen-input comparison and bounded refresh

provenance: supported. Targets: GO:0033107, cellstructuremech:cvt_vesicle_lumen, GO:0033110, GO:0009842, GO:0033112, GO:0036012, GO:0036014, GO:0033113, GO:0036013, GO:0034060.

1 of ten original target hashes differ from current main. The changed content is substantively reassessed in the target-specific assessments; original observations remain historical and unchanged. All current target and used context bytes are frozen.

## Findings

### micro-F1: Cyanelle IMS evidence note overstates direct GO parthood

minor / open / confirmed; issue key: cyanelle-ims-direct-go-parthood-overstatement.

The newly added edge correctly states cyanelle intermembrane space is part of the whole cyanelle. However, its evidence note says GO0036014 places it as a direct part of GO0009842. The current authority asserts GO0036014 part_of GO0033112 (envelope), and GO0033112 part_of GO0009842; the direct stroma relation is a separate case. Correct the note to distinguish transitive parthood through envelope while retaining the supported anatomical edge.

## Recommended Actions And Acceptance Checks

### micro-A1

In a separately authorized curation change, revise only the IMS-to-cyanelle edge evidence note to say GO supports parthood transitively through GO0033112, retaining the biologically valid edge. Recheck live authority paths before editing.

- Evidence note distinguishes GO0036014 part_of GO0033112 part_of GO0009842 from a direct asserted ontology relationship.
- Retained anatomical edge is not deleted merely because ontology parthood is transitive.
- Use guarded validated writer, curation event and repository history in the separate curation change; focused native checks pass.
- No scientific record changes in this review PR.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| current-record-0 | data/structures/membrane_organelle/cvt_vesicle.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 cf6eb5075a057a0b8b104cbacb61cdf895298eb4b018945a08b46bcb939c8b0c; current SHA256 cf6eb5075a057a0b8b104cbacb61cdf895298eb4b018945a08b46bcb939c8b0c. Record bytes unchanged since the original review. |
| original-review-0 | reviews/structured/20261022T010353Z-cvt-vesicle-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-1 | data/structures/membrane_organelle/cvt_vesicle_lumen.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 3bb8cb5c3f751ec93619bb4658fb51a2c6e6a94e4e0b16aa0ea8a0833a28c243; current SHA256 3bb8cb5c3f751ec93619bb4658fb51a2c6e6a94e4e0b16aa0ea8a0833a28c243. Record bytes unchanged since the original review. |
| original-review-1 | reviews/structured/20261022T010357Z-cvt-vesicle-lumen-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-2 | data/structures/membrane_organelle/cvt_vesicle_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 679cdeb18f93b2ecf38916c132f8461121e7067f0db52e4b24842559b39dbb67; current SHA256 679cdeb18f93b2ecf38916c132f8461121e7067f0db52e4b24842559b39dbb67. Record bytes unchanged since the original review. |
| original-review-2 | reviews/structured/20261022T010402Z-cvt-vesicle-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-3 | data/structures/membrane_organelle/cyanelle.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 24275c8050ca5d13c66d563c7aa697a4de65766f87499f876fc94c41cd2f0db7; current SHA256 5ebb2c3b4cc2d9364dc08ac335c793409014f30f0ca009ee3b4aeafb860371b6. Changed record reassessed against current sources. |
| original-review-3 | reviews/structured/20261022T010406Z-cyanelle-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-4 | data/structures/membrane_organelle/cyanelle_envelope.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 4a25594b3a26541401976d3ab78f271bc8726951462af9073fafc0eff2389a67; current SHA256 4a25594b3a26541401976d3ab78f271bc8726951462af9073fafc0eff2389a67. Record bytes unchanged since the original review. |
| original-review-4 | reviews/structured/20261022T010409Z-cyanelle-envelope-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-5 | data/structures/membrane_organelle/cyanelle_inner_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 f10bb4f3ff44fb6d0b23e67379861768a590eb6d3da75686e296a0a5b3b26970; current SHA256 f10bb4f3ff44fb6d0b23e67379861768a590eb6d3da75686e296a0a5b3b26970. Record bytes unchanged since the original review. |
| original-review-5 | reviews/structured/20261022T010413Z-cyanelle-inner-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-6 | data/structures/membrane_organelle/cyanelle_intermembrane_space.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 aba8ad62f544ec82bea2f4767a8c79cc45d3fe117423163fc1ce1211a2527f8c; current SHA256 aba8ad62f544ec82bea2f4767a8c79cc45d3fe117423163fc1ce1211a2527f8c. Record bytes unchanged since the original review. |
| original-review-6 | reviews/structured/20261022T010416Z-cyanelle-intermembrane-space-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-7 | data/structures/membrane_organelle/cyanelle_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 b95c9fcb293bd9f434df3ccf9ecaa7c9bf04e1f83a95a2cd19673441a537a20b; current SHA256 b95c9fcb293bd9f434df3ccf9ecaa7c9bf04e1f83a95a2cd19673441a537a20b. Record bytes unchanged since the original review. |
| original-review-7 | reviews/structured/20261022T010419Z-cyanelle-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-8 | data/structures/membrane_organelle/cyanelle_outer_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 2f058b25ce3bf1b49d52bc03391ee46d6e26376860035469f037d27c52234047; current SHA256 2f058b25ce3bf1b49d52bc03391ee46d6e26376860035469f037d27c52234047. Record bytes unchanged since the original review. |
| original-review-8 | reviews/structured/20261022T010421Z-cyanelle-outer-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-9 | data/structures/membrane_organelle/cyanelle_stroma.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 13d83e3dadca9cafaa6550a7bf84cd8066bf1539ccaacd3627ec23aa5b08e118; current SHA256 13d83e3dadca9cafaa6550a7bf84cd8066bf1539ccaacd3627ec23aa5b08e118. Record bytes unchanged since the original review. |
| original-review-9 | reviews/structured/20261022T010425Z-cyanelle-stroma-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| plaque-current-5 | data/structures/membrane_organelle/cyanelle_inner_membrane.yaml; Entire maintained record at source ed8281f2fc915349c8ce429e7103e42b256c0533; all fields, histories, discussions and graphs | supports | Entire current target independently read. Hash remains unchanged from original frozen target; PROPOSED status unchanged and no record curation performed. |
| plaque-original-5 | reviews/structured/20261022T010413Z-cyanelle-inner-membrane-audit/review.yaml; Original authoritative YAML/Markdown, source inputs, checks, assessments, findings/actions and limitations | supports | Original native validate/render passes and all original historical input hashes match. Verdict pass_with_limitations, no findings or actions; no original scientific finding exists to terminally dispose of. |
| plaque-current-6 | data/structures/membrane_organelle/cyanelle_intermembrane_space.yaml; Entire maintained record at source ed8281f2fc915349c8ce429e7103e42b256c0533; all fields, histories, discussions and graphs | supports | Entire current target independently read. Hash remains unchanged from original frozen target; PROPOSED status unchanged and no record curation performed. |
| plaque-original-6 | reviews/structured/20261022T010416Z-cyanelle-intermembrane-space-audit/review.yaml; Original authoritative YAML/Markdown, source inputs, checks, assessments, findings/actions and limitations | supports | Original native validate/render passes and all original historical input hashes match. Verdict pass_with_limitations, no findings or actions; no original scientific finding exists to terminally dispose of. |
| plaque-current-7 | data/structures/membrane_organelle/cyanelle_membrane.yaml; Entire maintained record at source ed8281f2fc915349c8ce429e7103e42b256c0533; all fields, histories, discussions and graphs | supports | Entire current target independently read. Hash remains unchanged from original frozen target; PROPOSED status unchanged and no record curation performed. |
| plaque-original-7 | reviews/structured/20261022T010419Z-cyanelle-membrane-audit/review.yaml; Original authoritative YAML/Markdown, source inputs, checks, assessments, findings/actions and limitations | supports | Original native validate/render passes and all original historical input hashes match. Verdict pass_with_limitations, no findings or actions; no original scientific finding exists to terminally dispose of. |
| plaque-current-8 | data/structures/membrane_organelle/cyanelle_outer_membrane.yaml; Entire maintained record at source ed8281f2fc915349c8ce429e7103e42b256c0533; all fields, histories, discussions and graphs | supports | Entire current target independently read. Hash remains unchanged from original frozen target; PROPOSED status unchanged and no record curation performed. |
| plaque-original-8 | reviews/structured/20261022T010421Z-cyanelle-outer-membrane-audit/review.yaml; Original authoritative YAML/Markdown, source inputs, checks, assessments, findings/actions and limitations | supports | Original native validate/render passes and all original historical input hashes match. Verdict pass_with_limitations, no findings or actions; no original scientific finding exists to terminally dispose of. |
| plaque-policy | .claude/skills/review-yaml-record/SKILL.md; Frozen native review, material identity, component, graph and structured-source applicability contract | context_only | Actual named genes/proteins/regulators/pathways/stress responses/traits trigger structured-source assessment. Generic material/topology or explicitly withheld molecular assignments are genuine exclusions. No missing molecular inventory is fabricated merely because a membrane contains proteins. |
| plaque-rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Frozen native review, material identity, component, graph and structured-source applicability contract | context_only | Actual named genes/proteins/regulators/pathways/stress responses/traits trigger structured-source assessment. Generic material/topology or explicitly withheld molecular assignments are genuine exclusions. No missing molecular inventory is fabricated merely because a membrane contains proteins. |
| plaque-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Frozen native review, material identity, component, graph and structured-source applicability contract | context_only | Actual named genes/proteins/regulators/pathways/stress responses/traits trigger structured-source assessment. Generic material/topology or explicitly withheld molecular assignments are genuine exclusions. No missing molecular inventory is fabricated merely because a membrane contains proteins. |
| plaque-schema-policy | src/cellstructuremech/schema/cellstructuremech.yaml; Frozen native review, material identity, component, graph and structured-source applicability contract | context_only | Actual named genes/proteins/regulators/pathways/stress responses/traits trigger structured-source assessment. Generic material/topology or explicitly withheld molecular assignments are genuine exclusions. No missing molecular inventory is fabricated merely because a membrane contains proteins. |
| plaque-shared-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009842,GO:0009536,GO:0033112,GO:0036012,GO:0036013,GO:0036014,GO:0034060,GO:0009843,GO:0033114,GO:0033115,GO:0033113,GO:0042170,GO:0009527,GO:0009532,GO:0005737,GO:0015979,GO:0009526; Exact identities/active definitions/synonyms of represented cyanelle/plastid/cytoplasm terms; typed child relations for0042170,0033113,0033112,0009527 and0034060 context | supports | Inner0036012 and outer0036013 are is_a children of generic envelope membrane0033113, which is part_of envelope0033112. Envelope also has IMS0036014 as part_of. Plastid outer0009527 has outer cyanelle membrane as is_a child. Inner/outer direct envelope parthood is additionally explicit in UniProt; no missing direct GO relation is invented. Envelope membranes, stroma and thylakoids remain distinct. Same-PR public snapshot independently read with original fetch timestamp retained. |
| plaque-cyanelle-boundary-parents | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009528,GO:0009529; Complete exact0009528/0009529 definitions, active status and direct typed child relations | supports | Plastid inner membrane0009528 has cyanelle inner0036012 as is_a child; plastid IMS0009529 has cyanelle IMS0036014 as is_a child. This verifies exact parent types rather than inferring them from mixed ancestry. |
| plaque-cyanelle-SL-0480 | https://rest.uniprot.org/locations/SL-0480.json; Complete top-level definition, synonyms, direct GO correspondence, immediate isA/partOf; nested objects distinguished | supports | SL0480 defines the stroma/IMS separator, directly maps toGO0036012, has generic cyanelle/plastid-inner isA and envelope partOf. Protein-count statistics are not structural prevalence or constituent necessity evidence. |
| plaque-cyanelle-SL-0481 | https://rest.uniprot.org/locations/SL-0481.json; Complete top-level definition, synonyms, direct GO correspondence, immediate isA/partOf; nested objects distinguished | supports | SL0481 defines the region between inner/outer membranes including the vestigial PG layer, directly mapsGO0036014, has plastid-IMS parent and envelope partOf. Protein-count statistics are not structural prevalence or constituent necessity evidence. |
| plaque-cyanelle-SL-0482 | https://rest.uniprot.org/locations/SL-0482.json; Complete top-level definition, synonyms, direct GO correspondence, immediate isA/partOf; nested objects distinguished | supports | SL0482 defines the cytoplasm-facing cyanelle membrane, mapsGO0036013, has generic cyanelle/plastid-outer parents and envelope partOf. Protein-count statistics are not structural prevalence or constituent necessity evidence. |
| plaque-cyanelle-SL-0083 | https://rest.uniprot.org/locations/SL-0083.json; Complete top-level definition, synonyms, direct GO correspondence, immediate isA/partOf; nested objects distinguished | supports | SL0083 mapsGO0033113 but explicitly permits unresolved outer/inner/thylakoid protein localization. The maintained generic record correctly treats this as broader fallback, not an exact xref or expansion of GO envelope-only scope. Protein-count statistics are not structural prevalence or constituent necessity evidence. |
| plaque-shared-tax2762 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2762; Complete native taxId/scientificName/rank/lineage/alternative names | supports | Native ENA verifies Cyanophora paradoxa 2762. Species belongs to Glaucocystophyceae. Identity does not establish experimental strain or quantitative prevalence; same-PR snapshot independently reread. |
| plaque-shared-tax38254 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/38254; Complete native taxId/scientificName/rank/lineage/alternative names | supports | Native ENA verifies Glaucocystophyceae 38254. Glaucophyta and Glaucophyceae are synonyms of class Glaucocystophyceae. Identity does not establish experimental strain or quantitative prevalence; same-PR snapshot independently reread. |
| plaque-shared-giddings1983-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1104%2Fpp.71.2.409; Complete primary abstract and exact title/authors/year/DOI/PMID metadata | supports | Giddings/Wasmann/Staehelin1983 distinguishes inner envelope membrane and two exterior layers by thin sections/freeze fracture. Presumptive PG/LPS assignment and historical symbiont interpretation are not upgraded to current molecular certainty. The separate fresh source scans support inspected body scope. |
| plaque-shared-giddings1983-page409 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/6ed041edd2c7/plntphys00558-0203.png; Complete scanned page409 visually inspected: title/authors, abstract, Introduction and culture/initial isolation Methods | supports | Source identifies C.paradoxa UTEX LB555,26C,modified CY-II medium and continuous illumination. Historical endosymbiont terminology is not imposed on modern GO organelle identity. Public scan independently viewed from same-PR shared snapshot at actual retained fetch time; not a full-paper claim. |
| plaque-shared-giddings1983-page414 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/9d4d067999da/plntphys00558-0208.png; Complete scanned page414 visually inspected: Envelope Membranes Results opening, Figure11/12 images and captions | supports | Envelope Results distinguish inner membrane and wall layer. Figure12 identifies inner-membrane P-face and thickened wall at cleavage furrow; Figure11 is thylakoid context, not envelope. Public scan independently viewed from same-PR shared snapshot at actual retained fetch time; not a full-paper claim. |
| plaque-shared-giddings1983-page416 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/c329334d81e0/plntphys00558-0210.png; Complete scanned page416 visually inspected: Envelope Results continuation, Figure15 histogram/caption and Discussion opening | supports | Outer-envelope fracture faces occur exterior to presumed PG; isolation can produce membrane blisters/peeling, exposing underlying smooth wall. No raw histogram or microscopy measurement reanalysis. Public scan independently viewed from same-PR shared snapshot at actual retained fetch time; not a full-paper claim. |
| plaque-shared-giddings1983-page417 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/7694ed6a7a74/plntphys00558-0211.png; Complete scanned page417 visually inspected: envelope Discussion and Figure16–18 images/captions plus adjacent text | supports | Inner membrane is distinct from thylakoids, with no observed continuity. Figure17 shows outer-envelope membrane detached from PG; Figure18 shows exposed layer after membrane removal. Historical chemical and organelle-status interpretations remain qualified. Public scan independently viewed from same-PR shared snapshot at actual retained fetch time; not a full-paper claim. |
| plaque-shared-pfanzagl1996-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1128%2Fjb.178.2.332-339.1996; Complete primary abstract and exact title/authors/year/DOI and PMID8550450 metadata | supports | Pfanzagl1996 primary-structure study biochemically characterizes C.paradoxa cyanelle PG using separated muropeptides and mass spectrometry. This supports material presence, not every reported chemical measurement, all glaucophyte species, a complete protein inventory or individual formation necessity. Abstract tier only in this reviewer. |
| plaque-pfanzagl-comparative-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID:8955325%20AND%20SRC:MED; Complete primary abstract, precise PMID8955325/DOI10.1128/jb.178.23.6994-6997.1996 and title/authors/year | supports | Comparative study directly analyzes Glaucocystis nostochinearum and Cyanoptyche gloeocystis cyanelle PG with chromatography/mass spectrometry, in comparison with prior Cyanophora evidence. The named genera in the IMS taxon note are supported; no universal recipe or numerical prevalence follows. |
| plaque-pfanzagl-comparative-body | https://pmc.ncbi.nlm.nih.gov/articles/178604/; Genuine PMC title/byline/abstract and PDF-only full-text landing surface | context_only | This successful HTML retrieval supplies the same complete abstract and a link to PDF, not the article body. No full comparative-body or underlying measurement reanalysis is claimed. |
| plaque-kojima2016-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI:%2210.1074/jbc.M116.746131%22; Exact DOI query result: title/authors/year/PMID27502278/PMC5025702 and complete abstract | supports | Kojima/Muramoto/Kusano2016 bibliography and primary abstract verified. CppS/F localization and channel assays are described in the genuine primary body separately; outer target does not assert a full molecular inventory or measured in-vivo transport rate. |
| plaque-kojima2016-canonical | https://pmc.ncbi.nlm.nih.gov/articles/PMC5025702/; Genuine primary HTML Abstract/Introduction, complete Results subsections Isolation and Sequence Analysis(sec5/6), channel subsection8, complete Discussion9; Methods13–21 and32; included captions as text | supports | C.paradoxa NIES547 cultures at24C supplied isolated cyanelle membranes. Co-fractionation, detergent-resistant PG/protein preparations, microscopy, pigments and independent outer-membrane isolation support the narrow exterior localization context. Channel measurements use reconstituted proteoliposomes; they do not prove membrane formation necessity or in-vivo rates. No complete-paper, Table1 audit, figure-pixel, supplementary or raw-data reanalysis claim; current target withholds named molecular assignments. |
| plaque-kojima2016-body | https://pmc.ncbi.nlm.nih.gov/articles/5025702/; Actual HTTP response inspected solely for source-access tier | context_only | HTTP200. Numeric PMC returned a challenge, S3 guessed version404, EuropePMC XML500. None supplies inspected full text; canonical PMC route separately succeeds. |
| plaque-kojima2016-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC5025702.1/PMC5025702.1.xml; Actual HTTP response inspected solely for source-access tier | context_only | HTTP404. Numeric PMC returned a challenge, S3 guessed version404, EuropePMC XML500. None supplies inspected full text; canonical PMC route separately succeeds. |
| plaque-kojima2016-epmcxml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5025702/fullTextXML; Actual HTTP response inspected solely for source-access tier | context_only | HTTP500. Numeric PMC returned a challenge, S3 guessed version404, EuropePMC XML500. None supplies inspected full text; canonical PMC route separately succeeds. |
| plaque-catalogue | https://imodulondb.org/api/datasets; Complete fresh /api/datasets response; all20 organism rows and their dataset entries inspected, no pagination | supports | No current organism row covers Cyanophora or another glaucophyte. No downstream matched gene/module query applies, and no bacterial/cyanobacterial analogue is substituted. Catalogue noncoverage is not evidence of biological absence. |
| plaque-historical-runner | /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources imodulondb datasets; Original historical00:49Z receipt and exact stdout/stderr independently reread/hash-verified | context_only | Historical runner exited1 before datasets due OS PermissionError on pyvenv.cfg; not a new invocation or successful execution. Official current catalogue is the permitted source fallback. |
| plaque-original-checks | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/adversary-plaque/original-checks.json; Four read-only native original validate/render executions; every frozen input at its historical source commit | supports | All four originals validate/render exactly.19/19/12/12 historical source hashes match; all four current target hashes unchanged. Original findings/actions empty. |
| plaque-native-cyanelle_inner_membrane-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_inner_membrane.yaml --verify; Actual root-owned native command receipt and exact stdout independently read/hash-verified | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| plaque-native-cyanelle_inner_membrane-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_inner_membrane.yaml --causal-graphs; Actual root-owned native command receipt and exact stdout independently read/hash-verified | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| plaque-native-cyanelle_intermembrane_space-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_intermembrane_space.yaml --verify; Actual root-owned native command receipt and exact stdout independently read/hash-verified | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| plaque-native-cyanelle_intermembrane_space-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_intermembrane_space.yaml --causal-graphs; Actual root-owned native command receipt and exact stdout independently read/hash-verified | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| plaque-native-cyanelle_membrane-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_membrane.yaml --verify; Actual root-owned native command receipt and exact stdout independently read/hash-verified | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| plaque-native-cyanelle_membrane-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_membrane.yaml --causal-graphs; Actual root-owned native command receipt and exact stdout independently read/hash-verified | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| plaque-native-cyanelle_outer_membrane-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_outer_membrane.yaml --verify; Actual root-owned native command receipt and exact stdout independently read/hash-verified | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| plaque-native-cyanelle_outer_membrane-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_outer_membrane.yaml --causal-graphs; Actual root-owned native command receipt and exact stdout independently read/hash-verified | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| micro-policy | .claude/skills/review-yaml-record/SKILL.md; Evidence Rules; Structured Source Cross-Checks; native checklist; profile and shared lineage contract; applicable common inputs frozen by native inspect before assessment | context_only | Native review requires narrow source scope, actual input hashes and command results, bounded searches, explicit applicability for named pathways, and separate record curation. All 17 retained common policy/schema/verifier inputs remain byte-identical to the previous reviewed common set; route/profile/config/checklist/shared contract reread in this audit. |
| micro-record-cyanelle | data/structures/membrane_organelle/cyanelle.yaml; Entire maintained YAML: definition, history, hierarchy, components, distribution/examples, functions, evidence, graph and discussions | supports | Entire current record independently read at ed8281f2fc915349c8ce429e7103e42b256c0533; PROPOSED status retained; current SHA matches native inspect and current main. Changed record reassessed substantively; original frozen version retained. |
| micro-prior-cyanelle | reviews/structured/20261022T010406Z-cyanelle-audit/review.yaml; Entire authoritative original YAML and paired Markdown, especially source.inputs, scientific assessments, verdict, checks[id=imodulondb], limitations and empty findings/actions | context_only | Original qualified pass had no scientific finding or request-curation action. Original validation/render and historical input hash independently checked; original observation is retained, not rewritten or recertified as current. |
| micro-native-cyanelle-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cyanelle-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle.yaml --verify; adjacent stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cyanelle-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Root executed at exact reviewed source; exit 0. The declared UniProt protein-example/xref inventory is empty, so this is not independent proof of protein identity, membership or necessity. |
| micro-native-cyanelle-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cyanelle-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle.yaml --causal-graphs; adjacent stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cyanelle-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Root executed at exact reviewed source; exit 0. All GENE_OR_PROTEIN categories and total are zero; this checks no biochemical gene/protein node and does not validate topology or biology. |
| micro-record-cyanelle_envelope | data/structures/membrane_organelle/cyanelle_envelope.yaml; Entire maintained YAML: definition, history, hierarchy, components, distribution/examples, functions, evidence, graph and discussions | supports | Entire current record independently read at ed8281f2fc915349c8ce429e7103e42b256c0533; PROPOSED status retained; current SHA matches native inspect and current main. Current bytes match original frozen scientific input. |
| micro-prior-cyanelle_envelope | reviews/structured/20261022T010409Z-cyanelle-envelope-audit/review.yaml; Entire authoritative original YAML and paired Markdown, especially source.inputs, scientific assessments, verdict, checks[id=imodulondb], limitations and empty findings/actions | context_only | Original qualified pass had no scientific finding or request-curation action. Original validation/render and historical input hash independently checked; original observation is retained, not rewritten or recertified as current. |
| micro-native-cyanelle_envelope-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cyanelle_envelope-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_envelope.yaml --verify; adjacent stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cyanelle_envelope-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Root executed at exact reviewed source; exit 0. The declared UniProt protein-example/xref inventory is empty, so this is not independent proof of protein identity, membership or necessity. |
| micro-native-cyanelle_envelope-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cyanelle_envelope-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_envelope.yaml --causal-graphs; adjacent stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cyanelle_envelope-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Root executed at exact reviewed source; exit 0. All GENE_OR_PROTEIN categories and total are zero; this checks no biochemical gene/protein node and does not validate topology or biology. |
| micro-record-cyanelle_stroma | data/structures/membrane_organelle/cyanelle_stroma.yaml; Entire maintained YAML: definition, history, hierarchy, components, distribution/examples, functions, evidence, graph and discussions | supports | Entire current record independently read at ed8281f2fc915349c8ce429e7103e42b256c0533; PROPOSED status retained; current SHA matches native inspect and current main. Current bytes match original frozen scientific input. |
| micro-prior-cyanelle_stroma | reviews/structured/20261022T010425Z-cyanelle-stroma-audit/review.yaml; Entire authoritative original YAML and paired Markdown, especially source.inputs, scientific assessments, verdict, checks[id=imodulondb], limitations and empty findings/actions | context_only | Original qualified pass had no scientific finding or request-curation action. Original validation/render and historical input hash independently checked; original observation is retained, not rewritten or recertified as current. |
| micro-native-cyanelle_stroma-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cyanelle_stroma-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_stroma.yaml --verify; adjacent stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cyanelle_stroma-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Root executed at exact reviewed source; exit 0. The declared UniProt protein-example/xref inventory is empty, so this is not independent proof of protein identity, membership or necessity. |
| micro-native-cyanelle_stroma-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cyanelle_stroma-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_stroma.yaml --causal-graphs; adjacent stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cyanelle_stroma-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Root executed at exact reviewed source; exit 0. All GENE_OR_PROTEIN categories and total are zero; this checks no biochemical gene/protein node and does not validate topology or biology. |
| micro-original-validation-inputs | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/adversary-microtubule/original-validation-inputs.json; All three original validate + render --content executions and original-source versus current-target SHA256 comparisons | supports | Three native original validations exit 0, three deterministic Markdown comparisons match. Frozen source revision 9c0446c4c0dd4b458787c43a499e4ceab5e179a6 verified. Only whole cyanelle changed: old24275c8050ca5d13c66d563c7aa697a4de65766f87499f876fc94c41cd2f0db7 versus current5ebb2c3b4cc2d9364dc08ac335c793409014f30f0ca009ee3b4aeafb860371b6. |
| micro-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009842,GO:0009536,GO:0033112,GO:0036012,GO:0036013,GO:0036014,GO:0034060,GO:0009843,GO:0033114,GO:0033115,GO:0033113,GO:0042170,GO:0009527,GO:0009532,GO:0005737,GO:0015979,GO:0009526; Exact 17-ID QuickGO term response: definitions, synonyms, native child relations for whole cyanelle, envelope, inner/outer membranes, IMS, stroma, thylakoid/lumen/membrane, plastid parents and photosynthesis | supports | Exact identities and typed parthood/is-a relationships support the retained anatomy. Whole cyanelle explicitly has stroma as a part; IMS is a child of envelope, itself a part of cyanelle. Definition and synonyms remain compatible with current taxonomic terminology. |
| micro-ims-go-path | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0036014/paths/GO:0009842; Complete QuickGO paths response from GO:0036014 to GO:0009842; one returned path of two part_of edges | refutes | The only returned path is GO:0036014 → GO:0033112 → GO:0009842. Supports transitive IMS parthood in cyanelle while refuting the record note that GO asserts this as a direct relationship. |
| micro-SL-0082 | https://rest.uniprot.org/locations/SL-0082.json; Native UniProt Subcellular Location JSON: definition, GO mapping and hierarchy; protein-count metadata not treated as inventory | supports | Exact Cyanelle entry maps GO0009842, gives cyanoplast/muroplast synonyms and describes photosynthetic glaucophyte organelle with double membrane and PG. |
| micro-SL-0479 | https://rest.uniprot.org/locations/SL-0479.json; Native UniProt Subcellular Location JSON: definition, GO mapping and hierarchy; protein-count metadata not treated as inventory | supports | Exact envelope entry maps GO0033112 and explicitly includes both membranes, IMS and PG; it is not a single bilayer. |
| micro-SL-0350 | https://rest.uniprot.org/locations/SL-0350.json; Native UniProt Subcellular Location JSON: definition, GO mapping and hierarchy; protein-count metadata not treated as inventory | supports | Exact stroma entry maps GO0034060, excludes thylakoid space, and lists DNA/ribosomes/photosynthetic products as contents, not mandatory identities of the compartment. |
| micro-cyanelle-SL-0480 | https://rest.uniprot.org/locations/SL-0480.json; Native UniProt definition and hierarchy; independently read supplied response, preserving plaque fetch timestamp | supports | The inner membrane separates stroma from IMS; this supports the graph boundary without treating either compartment as a membrane or protein. |
| micro-tax2762 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2762; Exact ENA taxonomy tax-id response: scientific name, rank, lineage and other names | supports | ENA taxon2762 is species Cyanophora paradoxa. |
| micro-tax38254 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/38254; Exact ENA taxonomy tax-id response: scientific name, rank, lineage and other names | supports | ENA taxon38254 is class Glaucocystophyceae, with Glaucophyta and Glaucophyceae listed as alternative names. |
| micro-giddings1983-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1104%2Fpp.71.2.409; Europe PMC exact DOI core result PMID16662839: bibliographic identity and complete primary abstract | supports | Primary microscopy of Cyanophora paradoxa cyanelles and thylakoids; presumptive PSII/contact assignments remain qualified. This is abstract metadata, supplemented by the separately viewed scanned pages. |
| micro-giddings1983-page409 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/6ed041edd2c7/plntphys00558-0203.png; Giddings et al.1983 DOI10.1104/pp.71.2.409, printed page409; source scan visually viewed as pixels, text and stated figures/captions | supports | Title, abstract, Introduction and opening Methods inspected in pixels: Cyanophora paradoxa UTEX LB555 culture/isolation; photosynthetically active cyanelles, phycobilisomes, and qualified historic envelope/PG interpretation. |
| micro-giddings1983-page410 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/8d99de19802c/plntphys00558-0204.png; Giddings et al.1983 DOI10.1104/pp.71.2.409, printed page410; source scan visually viewed as pixels, text and stated figures/captions | supports | Figures1–3 pixels and captions inspected: whole-cell cyanelle, isolated cyanelle and thylakoid faces; curved lamellae within the organelle, not a numerical or universal concentricity measurement. Isolation continuation and thylakoid preparation also read. |
| micro-giddings1983-page412 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/392b5bf89308/plntphys00558-0206.png; Giddings et al.1983 DOI10.1104/pp.71.2.409, printed page412; source scan visually viewed as pixels, text and stated figures/captions | supports | Results opening states dense cyanelle stroma; thylakoid/phycobilisome results and Methods continuation read, Figure6 pixels/caption inspected. Morphology is not a universal assembly-necessity test. |
| micro-giddings1983-page414 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/9d4d067999da/plntphys00558-0208.png; Giddings et al.1983 DOI10.1104/pp.71.2.409, printed page414; source scan visually viewed as pixels, text and stated figures/captions | supports | Envelope Membranes Results opening and Figures11–12 pixels/captions read: inner membrane, wall layer and isolated cyanelle organization distinguish envelope from internal thylakoids. |
| micro-giddings1983-page416 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/c329334d81e0/plntphys00558-0210.png; Giddings et al.1983 DOI10.1104/pp.71.2.409, printed page416; source scan visually viewed as pixels, text and stated figures/captions | supports | Envelope Results continuation and Discussion opening read with Figure15 histogram pixels/caption: outer layer exterior to PG and preparation-associated blistering/peeling are explicitly distinguished. |
| micro-giddings1983-page417 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/7694ed6a7a74/plntphys00558-0211.png; Giddings et al.1983 DOI10.1104/pp.71.2.409, printed page417; source scan visually viewed as pixels, text and stated figures/captions | supports | Complete envelope Discussion and Figures16–18 pixels/captions read: distinct inner and outer envelope structure, PG layer and no observed continuity between inner envelope and thylakoids; historical endosymbiont terminology is not current taxonomy. |
| micro-pfanzagl1996-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1128%2Fjb.178.2.332-339.1996; Europe PMC exact DOI core result PMID8550450: complete primary abstract and bibliographic identity; no full-body Methods/Results inspection claimed | supports | Primary biochemical characterization of Cyanophora paradoxa cyanelle PG by separation and mass spectrometry supports the material claim. Abstract-only scope is adequate for the record broad biochemical attribution, not a new claim about detailed experimental conditions or necessity. |
| micro-pfanzagl-comparative-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID:8955325%20AND%20SRC:MED; Complete Europe PMC primary abstract for PMID8955325 plus metadata; independently read supplied response, original fetch time retained | supports | HPLC/mass-spectrometric study identifies cyanelle PG in Glaucocystis nostochinearum and Cyanoptyche gloeocystis and compares earlier Cyanophora paradoxa chemistry. Supports the envelope note about those three named genera without universal species prevalence or full-body inspection. |
| micro-kojima2016-canonical | https://pmc.ncbi.nlm.nih.gov/articles/PMC5025702/; Genuine PMC5025702 canonical HTML: Abstract, Introduction, Results first subsection Isolation of CppS/F (sec5), Experimental Procedures Strains/Culture, Cyanelle Isolation, CppS/F Isolation, PG detection/binding, EM and PG preparation (sec13–19); text/captions only, not figure-pixel inspection | supports | Independent bounded body read confirms C.paradoxa NIES547 biochemical fractionation and PG-associated proteins/outer membrane preparation; direct localization support has appropriate experimental scope. No claim of reading all Results, all Methods, sequence analyses or supplementary data; article is not a universal necessity experiment. |
| micro-price2019-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A31098614%20AND%20SRC%3AMED; Europe PMC exact PMID31098614 core metadata and complete primary abstract | supports | Price et al.2019 DOI10.1093/dnares/dsz009 is a Cyanophora genome/ultrastructure study, supporting the reference identity and scoped glaucophyte context. |
| micro-price2019-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC6704402.1/PMC6704402.1.xml; Genuine PMC6704402.1 JATS: Introduction, Methods2.1, Results3.4 including3.4.1–5 and3.5; Figure2 and referenced supplement captions/prose only, no pixel inspection | supports | Primary QFDE microscopy and C.paradoxa CCMP329 genome context support plastid/thylakoid/PG anatomy. Results3.4.3 describes apparent concentric/spiral architecture with occasional termini/bifurcations, so the stale thylakoid-in-stroma edge is supported as bounded morphology, not a universal closed-onion claim. Introduction and cited historical conclusions are secondary context; no reanalysis or exhaustive genome audit claimed. |
| micro-pg-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=cyanelle%20peptidoglycan&amp;limit=100&amp;page=1; Complete QuickGO query response with literal query cyanelle peptidoglycan, page1, limit100 | supports | Returned64 results, including broader PG-wall and cyanelle anatomical terms, do not establish a unique cyanelle PG-sheet identity. The existing reviewed-label-only component and explicit open grounding discussion remain appropriate; no universal absence conclusion. |
| micro-catalogue | https://imodulondb.org/api/datasets; Complete public iModulonDB /api/datasets response; organism IDs/names and dataset arrays inspected | supports | No organism/dataset entry matches Cyanophora paradoxa, Glaucocystophyceae/Glaucophyta, Cyanoptyche or Glaucocystis. Synechococcus elongatus is a different bacterial organism and is not substituted for a glaucophyte plastid. No matched dataset means downstream gene/module queries cannot inform this record; absence is not biological negative evidence. |
| micro-historical-adapter-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Retained actual native imodulondb datasets attempt, exit1 / operating-system PermissionError reading runner pyvenv.cfg; receipt reviewed as historical evidence | context_only | This runner failure occurred at00:49:00Z in the earlier canary session, not a fresh invocation for PR2362. Current applicability uses the independently fetched catalogue fallback. Unavailability does not imply absent biology. |
| septin-review-policy | .claude/skills/review-yaml-record/SKILL.md; Structured Source Cross-Checks and immutable review contract | supports | Named molecular and pathway assertions trigger applicability assessment, including affirmative canonical-example pathway claims. Expression-only non-inference is not an exemption. No covered organism is a resource limit, not negative biology. |
| septin-curation-policy | docs/CURATION.md; Identity, components, material constitution, source scope and evidence | supports | A structure, its constituent bilayer, cargo complex and associated transient assembly machinery remain distinct. Molecular identity does not establish localization or formation necessity. |
| septin-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; NONMECHANISTIC graphs and scoped molecular evidence | supports | Descriptive topology and supported delivery endpoints may be nonmechanistic. Empty protein-node inventories do not prove narrative molecular assertions. |
| septin-record-cvt_vesicle | data/structures/membrane_organelle/cvt_vesicle.yaml; Entire current maintained YAML at ed8281f2fc915349c8ce429e7103e42b256c0533 | supports | Read identity/definition, history, hierarchy, components, taxon and canonical context, function, every graph edge, evidence and discussion. No target image, quantitative property, trait link, verbatim snippet or individual protein accession is declared. |
| septin-original-cvt_vesicle | reviews/structured/20261022T010353Z-cvt-vesicle-audit/review.yaml; Original YAML plus deterministic Markdown; frozen inputs, checks, source tiers, assessments and limitations | supports | Original qualified pass has no scientific findings or request-curation actions. Its target bytes remain current. Its expression-only iModulonDB rationale is insufficient; historical source times and global checks remain historical. |
| septin-original-validation-cvt_vesicle | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/adversary-septin/original-checks.json; 20261022T010353Z-cvt-vesicle-audit actual validate/render plus original-source/current hash comparison | supports | Both native commands exited zero; Markdown matches byte-for-byte and target hashes match original historical source, original frozen input and current record. |
| septin-native-cvt_vesicle-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cvt_vesicle-uniprot-verify-receipt.json; Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cvt_vesicle-uniprot-verify.log | supports | Exit zero. No protein examples or UniProtKB graph xrefs and zero GENE_OR_PROTEIN graph nodes. Execution success verifies only this empty represented inventory; it does not establish narrative Ape1/Ams1/Atg identity, localization, mechanism, complete composition or formation necessity. |
| septin-native-cvt_vesicle-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cvt_vesicle-uniprot-causal-receipt.json; Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cvt_vesicle-uniprot-causal.log | supports | Exit zero. No protein examples or UniProtKB graph xrefs and zero GENE_OR_PROTEIN graph nodes. Execution success verifies only this empty represented inventory; it does not establish narrative Ape1/Ams1/Atg identity, localization, mechanism, complete composition or formation necessity. |
| septin-record-cvt_vesicle_lumen | data/structures/membrane_organelle/cvt_vesicle_lumen.yaml; Entire current maintained YAML at ed8281f2fc915349c8ce429e7103e42b256c0533 | supports | Read identity/definition, history, hierarchy, components, taxon and canonical context, function, every graph edge, evidence and discussion. No target image, quantitative property, trait link, verbatim snippet or individual protein accession is declared. |
| septin-original-cvt_vesicle_lumen | reviews/structured/20261022T010357Z-cvt-vesicle-lumen-audit/review.yaml; Original YAML plus deterministic Markdown; frozen inputs, checks, source tiers, assessments and limitations | supports | Original qualified pass has no scientific findings or request-curation actions. Its target bytes remain current. Its expression-only iModulonDB rationale is insufficient; historical source times and global checks remain historical. |
| septin-original-validation-cvt_vesicle_lumen | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/adversary-septin/original-checks.json; 20261022T010357Z-cvt-vesicle-lumen-audit actual validate/render plus original-source/current hash comparison | supports | Both native commands exited zero; Markdown matches byte-for-byte and target hashes match original historical source, original frozen input and current record. |
| septin-native-cvt_vesicle_lumen-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cvt_vesicle_lumen-uniprot-verify-receipt.json; Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cvt_vesicle_lumen-uniprot-verify.log | supports | Exit zero. No protein examples or UniProtKB graph xrefs and zero GENE_OR_PROTEIN graph nodes. Execution success verifies only this empty represented inventory; it does not establish narrative Ape1/Ams1/Atg identity, localization, mechanism, complete composition or formation necessity. |
| septin-native-cvt_vesicle_lumen-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cvt_vesicle_lumen-uniprot-causal-receipt.json; Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cvt_vesicle_lumen-uniprot-causal.log | supports | Exit zero. No protein examples or UniProtKB graph xrefs and zero GENE_OR_PROTEIN graph nodes. Execution success verifies only this empty represented inventory; it does not establish narrative Ape1/Ams1/Atg identity, localization, mechanism, complete composition or formation necessity. |
| septin-record-cvt_vesicle_membrane | data/structures/membrane_organelle/cvt_vesicle_membrane.yaml; Entire current maintained YAML at ed8281f2fc915349c8ce429e7103e42b256c0533 | supports | Read identity/definition, history, hierarchy, components, taxon and canonical context, function, every graph edge, evidence and discussion. No target image, quantitative property, trait link, verbatim snippet or individual protein accession is declared. |
| septin-original-cvt_vesicle_membrane | reviews/structured/20261022T010402Z-cvt-vesicle-membrane-audit/review.yaml; Original YAML plus deterministic Markdown; frozen inputs, checks, source tiers, assessments and limitations | supports | Original qualified pass has no scientific findings or request-curation actions. Its target bytes remain current. Its expression-only iModulonDB rationale is insufficient; historical source times and global checks remain historical. |
| septin-original-validation-cvt_vesicle_membrane | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/adversary-septin/original-checks.json; 20261022T010402Z-cvt-vesicle-membrane-audit actual validate/render plus original-source/current hash comparison | supports | Both native commands exited zero; Markdown matches byte-for-byte and target hashes match original historical source, original frozen input and current record. |
| septin-native-cvt_vesicle_membrane-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cvt_vesicle_membrane-uniprot-verify-receipt.json; Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cvt_vesicle_membrane-uniprot-verify.log | supports | Exit zero. No protein examples or UniProtKB graph xrefs and zero GENE_OR_PROTEIN graph nodes. Execution success verifies only this empty represented inventory; it does not establish narrative Ape1/Ams1/Atg identity, localization, mechanism, complete composition or formation necessity. |
| septin-native-cvt_vesicle_membrane-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cvt_vesicle_membrane-uniprot-causal-receipt.json; Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cvt_vesicle_membrane-uniprot-causal.log | supports | Exit zero. No protein examples or UniProtKB graph xrefs and zero GENE_OR_PROTEIN graph nodes. Execution success verifies only this empty represented inventory; it does not establish narrative Ape1/Ams1/Atg identity, localization, mechanism, complete composition or formation necessity. |
| septin-context-cvt_complex | data/structures/other/cvt_complex.yaml; Boundary fields only: identifier, label, definition, structure_kind, parents, part_of and has_part | supports | Frozen before inspection. Exact GO0034270 denotes a multiprotein cargo complex, distinct from the GO0033107 double-membrane carrier, the surrounding bilayer and the enclosed region. No whole-neighbor scientific review, protein example verification or historical finding disposition is asserted. |
| septin-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0033107,GO:0033110,GO:0034270,GO:0032258,GO:0031410,GO:0060205,GO:0030659,GO:0000324; All eight exact returned terms: identities, definitions, active status, synonyms and relevant direct typed child relations | supports | GO0033107 is the double-membrane Cvt carrier and has exact cytoplasm-to-vacuole-targeting vesicle synonyms; GO0033110 denotes either one of its two bilayers. GO0034270 identifies the preApe1 cargo complex. Parent and part relations, fungal vacuole endpoint and GO0032258 selective Cvt process are consistent with maintained scope. GO0060205 is the broader lumen parent, not an exact Cvt-lumen substitute. |
| septin-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Exact taxId, scientificName, rank and lineage | supports | Taxon4932 is the species Saccharomyces cerevisiae. Taxon identity is verified independently of model strain, experimental condition or quantitative prevalence. |
| septin-SL0080 | https://rest.uniprot.org/locations/SL-0080.json; Native entry id/name/definition, immediate isA/partOf and nested GO mappings | supports | SL0080 maps exactly to GO0033107 and has cytoplasmic vesicle parentage. |
| septin-SL0081 | https://rest.uniprot.org/locations/SL-0081.json; Native entry id/name/definition, immediate isA/partOf and nested GO mappings | supports | SL0081 maps exactly to GO0033110, with cytoplasmic vesicle membrane parentage and Cvt vesicle partOf; it does not identify an individual lipid species. |
| septin-SL0323 | https://rest.uniprot.org/locations/SL-0323.json; Native entry id/name/definition, immediate isA/partOf and nested GO mappings | supports | SL0323 positively identifies the Cvt vesicle lumen, with cytoplasmic vesicle lumen parent and Cvt vesicle partOf. It has no own GO mapping in this returned entry; this does not prove global ontology absence. |
| septin-reggiori2004-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A15004240%20AND%20SRC%3AMED; Complete native primary abstract plus exact title/authors/year/DOI/PMID/PMCID and article type | supports | Reggiori et al.2004 PMID15004240 DOI10.1091/mbc.e03-07-0479 is a primary research article. Its abstract supports cytosolic double-membrane Cvt sequestration and early-secretory contribution while retaining membrane-origin uncertainty. |
| septin-shintani2004-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A15138258%20AND%20SRC%3AMED; Complete native primary abstract plus exact title/authors/year/DOI/PMID/PMCID and article type | supports | Shintani and Klionsky2004 PMID15138258 DOI10.1074/jbc.M404399200 is a primary experiment, not a secondary review. Ape1/Atg19 complex formation, PAS organization and conditional Cvt vesicle formation are distinguished. |
| septin-scott2001-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A11430817%20AND%20SRC%3AMED; Complete native primary abstract plus exact title/authors/year/DOI/PMID/PMCID and article type | supports | Scott et al.2001 PMID11430817 DOI10.1016/s1097-2765(01)00263-5 identifies Cvt19 as a selective hydrolase receptor, with prAPI binding and vacuolar cotransport. Cvt19 requirement for specific cargo is distinct from bulk autophagy and pexophagy requirements. |
| septin-reggiori2004-pmc-prefixed | https://pmc.ncbi.nlm.nih.gov/articles/PMC404015/; Genuine current PMC404015 HTML: complete Introduction sec1; Methods Strains and Media sec3/Table1 and pulse-chase sec6; Results sec13 and sec14 with Figures5–8 text captions; Discussion sec17 only. Other sections and all pixels/raw data not audited. | supports | Yeast BY4742/SEY6210 and listed sec7/sec12 models support double-membrane cargo carriers, outer-membrane fusion and inner-body release. Temperature-shift and pulse-chase experiments show early-secretory effects on PAS/cargo transport. Effects depend on timing and conditions; the authors explicitly cannot distinguish ER from Golgi origin. Broader intro claims are contextual synthesis within a primary paper, not newly performed experiments. |
| septin-shintani2004-pmc-prefixed | https://pmc.ncbi.nlm.nih.gov/articles/PMC1712665/; Genuine current PMC1712665 HTML: complete scientific main body, Introduction S1, Experimental Procedures S2–5/TableI, Results S6–9 and Discussion S10, including Figures1–3 captions as text. No pixels/raw data or independently audited cited references. | supports | The primary study uses SEY6210-derived fluorescent reporters, temperature-sensitive atg1 synchronization, nutrient-rich conditions and rapamycin/starvation controls. Cargo/receptor deletion delays efficient Cvt vesicle delivery and PAS organization; starvation autophagosome formation remains distinct. Atg8-PE reporter delivery is a proxy requiring processing controls. The source supports cargo inclusion and condition-specific assembly contribution, not universal necessity of every actor or an exhaustive lipid/Atg inventory. Atg19/Cvt19 naming is explicit. |
| septin-scott2001-pmc-prefixed | https://pmc.ncbi.nlm.nih.gov/articles/PMC2767243/; Genuine current PMC2767243 HTML: Results S8 including Figure6 caption; Discussion S14; Methods Strains and Media S18/Table1, coimmunoprecipitation S24 and in-vitro binding S25. Complete abstract read separately; remaining article sections and pixels not claimed. | supports | Coimmunoprecipitation distinguishes prAPI precursor association from mature API and a propeptide mutant; heterologous E.coli extract/reticulocyte translation assays support Cvt19 binding without a required yeast bridging protein. This is not a purified-protein-only assay. Discussion distinguishes atypical cargo-bound receptor turnover from classical receptor recycling and the inner cargo compartment from intermembrane space. The bounded receptor claim is supported without importing every downstream membrane-assembly step. |
| septin-lumen-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=Cvt%20vesicle%20lumen&amp;limit=100; Current first100 returned GO candidate ids/names, pageInfo current1 of7 | supports | No exact Cvt vesicle lumen term was identified in this bounded returned set. Exact SL0323 supports retained local identity. No exhaustive ontology absence or forced broader-term mapping is claimed. |
| septin-local-identity-search | rg --no-ignore --hidden -n ^identifier: (cellstructuremech:cvt_vesicle_lumen&#124;GO:0033107&#124;GO:0033110&#124;GO:0034270)$ data/structures; Complete exact anchored-identifier matches in data/structures including hidden/ignored files | supports | Each of the three target ids and the context Cvt-complex id has one matching maintained record; the full matched contents were read only where already frozen. |
| septin-catalogue | https://imodulondb.org/api/datasets; Complete official organism list and every returned organism/dataset key | supports | No Saccharomyces cerevisiae or other yeast-matched organism/dataset is in the returned official catalogue. All three records positively invoke the Cvt/early-secretory pathway; whole and membrane also name molecular cargo/receptor context. A source applicability assessment is required even without expression claims. No unrelated organism query or biological absence inference is justified. |
| septin-historical-adapter-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical actual datasets invocation00:49:00.848907Z–00:49:00.863225Z | context_only | Historical canary invocation exited1 with PermissionError reading pyvenv.cfg. This hash-verified retained receipt is not a fresh invocation or successful current adapter run; current official catalogue fallback was read separately. |
| septin-access-source-receipts | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/adversary-septin/source-receipts.json; Actual URLs, timestamps, response outcomes and successful-response hashes | context_only | Numeric PMC links returned HTTP200 challenge pages, not scientific text; prefixed PMC links returned genuine article bodies. Guessed S3 .1 objects returned404 and EuropePMC fullTextXML returned500. The guessed /organisms.json catalogue path returned an HTML fallback, not catalogue data; the correct /api/datasets response was independently inspected. No failed or stub route is counted as body access. |
| septin-access-source-receipts2 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/adversary-septin/source-receipts2.json; Actual URLs, timestamps, response outcomes and successful-response hashes | context_only | Numeric PMC links returned HTTP200 challenge pages, not scientific text; prefixed PMC links returned genuine article bodies. Guessed S3 .1 objects returned404 and EuropePMC fullTextXML returned500. The guessed /organisms.json catalogue path returned an HTML fallback, not catalogue data; the correct /api/datasets response was independently inspected. No failed or stub route is counted as body access. |
| check-qc | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/qc.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| check-labels | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/labels.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| check-trait-links | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/trait-links.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Native TraitMech link check passed. |
| check-vendored | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/vendored.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Pinned governed files match; native vendored check passed. |
| check-curies | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/curies.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| focused | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/focused-results.json; All twenty actual target schema/strict command outputs | supports | Ten schema and ten strict commands returned exit zero. |
| supplemental-pmid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/pmid-chunks-receipt.json; Complete native-report PMID set checked with unchanged resolver in batches of at most fifty | supports | 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers remain unverified. |
| historical-adapter-runner-availability | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner invocation receipt, cross-checked against exact stdout/stderr hashes; reread during PR2362 synthesis | context_only | Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS PermissionError reading the configured runner pyvenv.cfg. This is a retained historical availability observation, not a fresh attempt or a scientific validation failure. Native policy permits inspected source-catalogue fallback. |

## Limits And Additional Notes

- Cyanelle inner membrane, intermembrane space, membrane and outer membrane independent subreview: Four assigned targets only, all unchanged from original frozen records. No other local scientific record was used as evidence; public native GO/SL sources supply compartment boundaries. Historical record corrections/issues are not recertified or terminally resolved.
- Cyanelle inner membrane, intermembrane space, membrane and outer membrane independent subreview: Fresh Giddings1983 scans409/414/416/417 were independently viewed at text and pixel level. These include culture context, envelope Results and Discussion, and indicated figures. No other page, entire paper, complete bibliography or raw microscopy measurement reanalysis is claimed. Historical presumed PG/LPS chemistry and endosymbiont terminology remain historical.
- Cyanelle inner membrane, intermembrane space, membrane and outer membrane independent subreview: Pfanzagl1996 primary-structure and PMID8955325 comparative evidence are complete primary abstracts plus exact metadata. The comparative PMC HTML is an abstract/PDF landing page, not inspected article body. No chemical numeric data or universal species/strain composition is inferred.
- Cyanelle inner membrane, intermembrane space, membrane and outer membrane independent subreview: Kojima2016 canonical PMC body was read at Abstract/Introduction, Results isolation/sequence/channel subsections, complete Discussion, Methods13–21 and liposome assay32. Figure captions are text only; no figure pixels, full Table1, supplementary data or raw experiment reanalysis. Numeric PMC challenge, S3.1 404 and EuropePMC XML500 are distinct failed routes.
- Cyanelle inner membrane, intermembrane space, membrane and outer membrane independent subreview: Giddings model is UTEX LB555; Kojima model is NIES547 with paper-specific isolation/culture conditions. Reconstituted diffusion assays do not demonstrate in-vivo rates or individual formation necessity. COMMON is qualitative anatomy, not a prevalence estimate.
- Cyanelle inner membrane, intermembrane space, membrane and outer membrane independent subreview: Source locations match exact identities and typed parent/parthood distinctions. SL0083 is broader unresolved localization fallback, not an exact generic envelope membrane match. Collective bilayer constitutional necessity and IMS PG UNKNOWN essentiality remain distinct from requirements for particular molecules.
- Cyanelle inner membrane, intermembrane space, membrane and outer membrane independent subreview: All four records are genuine material/topology exclusions under actual structured-source triggers. Two omissions and two expression-only N/A sentences are not counted as defects absent positive named molecular/pathway/stress/trait assertions. No compulsory protein inventory is invented.
- Cyanelle inner membrane, intermembrane space, membrane and outer membrane independent subreview: Current full catalogue lacks glaucophyte hosts; no matched downstream gene/module query applies and no biological absence follows. The historical00:49Z PermissionError runner receipt is retained at its actual time, not a new invocation or success.
- Cyanelle inner membrane, intermembrane space, membrane and outer membrane independent subreview: All eight native protein commands pass empty inventories and zero typed molecular nodes, without proving biological localization, assembly necessity or source claims. Root owns global gates, issue handling, immutable successor authoring and all repository/GitHub writes.
- Whole cyanelle, envelope and stroma independent subreview: Cyanelle/envelope/stroma source slice: Giddings scans actually viewed are pages409,410,412,414,416,417 only; remaining printed pages were not read in this fresh audit. No whole-paper, quantitative remeasurement or raw-data reanalysis claim.
- Whole cyanelle, envelope and stroma independent subreview: Cyanelle/envelope/stroma source slice: Pfanzagl1996 primary-structure evidence and PMID8955325 comparative study were read as complete primary abstracts/metadata, not full Methods/Results. Their broad material/taxon claims do not establish molecule-specific assembly necessity.
- Whole cyanelle, envelope and stroma independent subreview: Cyanelle/envelope/stroma source slice: Kojima canonical body was independently read only at Abstract, Introduction, Results first isolation subsection and Methods13–19. Price JATS read at Introduction, Methods2.1 and Results3.4/3.5; article figure/supplement references and captions are not fresh pixel inspection. Supplied plaque responses retain their actual11:52Z fetch times.
- Whole cyanelle, envelope and stroma independent subreview: Cyanelle/envelope/stroma source slice: retained historical native adapter failure was00:49Z, not a fresh PR2362 run. Current catalogue scope is its returned dataset listing; no matched glaucophyte dataset and no downstream gene/module result. Absence is not negative biology.
- Whole cyanelle, envelope and stroma independent subreview: Cyanelle/envelope/stroma source slice: six current native protein commands pass on empty declared inventories / zero GENE_OR_PROTEIN nodes. They do not prove complete protein coverage, identity, membership or necessity. Root owns full-corpus gates, issue dedup and CI; this report borrows no future CI success.
- Whole cyanelle, envelope and stroma independent subreview: Cyanelle/envelope/stroma source slice: reviewed-label-only PG grounding is an explicit scientific unknown; bounded GO text search is not universal absence. COMMON is qualitative occurrence, not quantitative prevalence. No prior category/neighbor issue is resolved; three original finding arrays were empty.
- Cvt vesicle, lumen and membrane independent subreview: All three target hashes are unchanged, including comparison with original historical source bytes. Original bundle access times and global gate claims remain historical; no prior source snapshot is recast as a new fetch.
- Cvt vesicle, lumen and membrane independent subreview: Fresh primary bodies were recovered only through PMC-prefixed routes. Shintani2004 scientific main body was read completely including text captions; Reggiori2004 was read only at Introduction, named strain/pulse-chase Methods, early-secretory Results and sec17 Discussion; Scott2001 only at named binding Results, atypical-receptor Discussion and associated Methods. No pixels, raw data, movies or independent audit of cited studies.
- Cvt vesicle, lumen and membrane independent subreview: The initial numeric PMC routes were verification stubs despite HTTP200. Guessed S3 paths returned404 and EuropePMC XML routes500. The guessed catalogue path returned HTML, while the correct official API returned data. These access limitations do not mean the recovered papers or catalogue are unreadable.
- Cvt vesicle, lumen and membrane independent subreview: GO lumen candidate search was first100/page1of7 only; exact SL0323 positively supports the local identity. No exhaustive ontology or chemical-family absence is certified. Generic bilayer constitution does not establish necessity of an individual lipid species.
- Cvt vesicle, lumen and membrane independent subreview: All six current native protein commands returned zero with empty accession inventories and zero typed protein nodes. They do not validate narrative Atg/Ape1/Ams1 identity, localization, complete composition, molecular mechanism or formation necessity.
- Cvt vesicle, lumen and membrane independent subreview: Cvt/cargo and early-secretory pathway assertions trigger source applicability in all three records, including lumen canonical-example context despite its mechanism exclusion. Current official catalogue lacks a matching yeast dataset. No unrelated downstream query or biological absence inference; historical runner PermissionError retains actual00:49Z time and is not rerun.
- Cvt vesicle, lumen and membrane independent subreview: COMMON is qualitative. Selected yeast strains, nutrient-rich Cvt transport and starvation/rapamycin autophagy remain separate; published conditional defects do not establish universal formation requirements or an exclusive ER/Golgi membrane donor.
- Cvt vesicle, lumen and membrane independent subreview: The frozen Cvt-complex neighbor was read only at declared boundary fields, not its complete scientific inventory. No neighbor, group, category, old issue or prior curation decision is terminally resolved. Root owns global gates, issue deduplication/publication, repository/GitHub writes and final CI/queue checks.
- Historical observations remain immutable; their old checks are not represented as current-head execution.
- The adapter runner was not rerun after the canary established OS access failure. Catalogue-based coverage is assessed directly; fresh and reused responses retain actual access timestamps.
- Native label checks include 923 no-adapter skips. Native identifier checks include 909 PMID transport failures and 254 skipped identifiers; bounded supplemental checks independently resolve the 909 PMIDs.
- Scientific record-curation findings stay in separate issues; no record is edited by this review PR.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after saving this immutable observation and are not represented here as already completed.
- All ten original YAML/Markdown pairs remain unchanged. Current main was merged normally and pushed without force.
- This explicit issue-bearing ten-record cohort follows the native persistence policy. Concrete review-bundle defects were observed and filed as #2673 and #2674. One newly observed scientific provenance finding has no invented predecessor or terminal disposition; the original ten reviews contained no findings.
- Issue #2673 tracks the stale cyanelle target: new history and three topology edges connect the intermembrane space and stroma to the cyanelle and locate thylakoids within stroma. The successor reassesses the added relations against current GO and bounded primary microscopy evidence, retaining actual taxon and experimental scope.
- Issue #2674 tracks four unsupported expression-only applicability exclusions: Cvt vesicle, lumen and membrane name pathway or molecular context, and whole cyanelle asserts photosynthesis. The six remaining cyanelle records retain genuine material/topology exclusions because their full claims do not assert named machinery, regulators or physiological-response pathways.
- Source commit ed8281f2fc915349c8ce429e7103e42b256c0533 is retained by tag review-base/pr2362-current-record-followup-20261103.
- CLAUDE.md is an alias of AGENTS.md; canonical regular AGENTS.md bytes are frozen.
- All 48 used local inputs were frozen before assessment, including Cvt complex as a boundary-context neighbor, native configuration, graph/protein policies and verifier source. The neighbor is context only, not an additional target or a disposition of its findings.
- Fresh and reused public-source snapshots retain actual access dates and inspection tiers. Exact authority identity does not independently establish mechanistic action, species-wide generalization or assembly necessity.
- All twenty native protein commands returned zero on empty represented protein inventories and zero typed GENE_OR_PROTEIN graph nodes. They do not validate narrative Atg/Ape1/Ams1 assertions, photosynthetic machinery, protein localization or source scope.
- Named pathway context in the Cvt lumen still triggers applicability assessment even though direct molecular mechanism is withheld. Genuine cyanelle boundary/material exclusions do not become defects merely because their prior applicability row was absent or expressed narrowly.
- A new minor finding concerns the stale cyanelle edge evidence note, which calls the GO intermembrane-space-to-cyanelle relation direct although current authority gives transitive parthood through the envelope. The biological edge remains supported. The note correction stays in a separate record-curation issue #2675; nine other targets retain qualified positive scientific assessments. No record is edited.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T115912Z-pr2362-current-record-followup
kind: batch
repository: CultureBotAI/CellStructureMech
title: 'PR 2362: current-input review of ten records and adversarial follow-up'
started_at: '2026-11-03T11:50:42.116655Z'
finished_at: '2026-11-03T11:59:12Z'
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
summary: Current-input reassessment of all ten records in PR2362. One stale cyanelle
  review is substantively refreshed and four structured-source applicability assessments
  are corrected. Independent source review identifies one minor new cyanelle GO-provenance
  finding for separate curation; no records are edited.
source:
  git_revision: ed8281f2fc915349c8ce429e7103e42b256c0533
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
  - path: data/structures/membrane_organelle/cvt_vesicle.yaml
    sha256: cf6eb5075a057a0b8b104cbacb61cdf895298eb4b018945a08b46bcb939c8b0c
    role: target
  - path: data/structures/membrane_organelle/cvt_vesicle_lumen.yaml
    sha256: 3bb8cb5c3f751ec93619bb4658fb51a2c6e6a94e4e0b16aa0ea8a0833a28c243
    role: target
  - path: data/structures/membrane_organelle/cvt_vesicle_membrane.yaml
    sha256: 679cdeb18f93b2ecf38916c132f8461121e7067f0db52e4b24842559b39dbb67
    role: target
  - path: data/structures/membrane_organelle/cyanelle.yaml
    sha256: 5ebb2c3b4cc2d9364dc08ac335c793409014f30f0ca009ee3b4aeafb860371b6
    role: target
  - path: data/structures/membrane_organelle/cyanelle_envelope.yaml
    sha256: 4a25594b3a26541401976d3ab78f271bc8726951462af9073fafc0eff2389a67
    role: target
  - path: data/structures/membrane_organelle/cyanelle_inner_membrane.yaml
    sha256: f10bb4f3ff44fb6d0b23e67379861768a590eb6d3da75686e296a0a5b3b26970
    role: target
  - path: data/structures/membrane_organelle/cyanelle_intermembrane_space.yaml
    sha256: aba8ad62f544ec82bea2f4767a8c79cc45d3fe117423163fc1ce1211a2527f8c
    role: target
  - path: data/structures/membrane_organelle/cyanelle_membrane.yaml
    sha256: b95c9fcb293bd9f434df3ccf9ecaa7c9bf04e1f83a95a2cd19673441a537a20b
    role: target
  - path: data/structures/membrane_organelle/cyanelle_outer_membrane.yaml
    sha256: 2f058b25ce3bf1b49d52bc03391ee46d6e26376860035469f037d27c52234047
    role: target
  - path: data/structures/membrane_organelle/cyanelle_stroma.yaml
    sha256: 13d83e3dadca9cafaa6550a7bf84cd8066bf1539ccaacd3627ec23aa5b08e118
    role: target
  - path: data/structures/other/cvt_complex.yaml
    sha256: 29ffd90803735e2db2a3869531eae7e439bac79b868049f6d7766c6c9a694902
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
  - path: reviews/structured/20261022T010353Z-cvt-vesicle-audit/review.md
    sha256: 9c9a6a218a8702d2ad829bc7c8e61cf3d3dca836a5f46e88b4b4e00f3f068c50
    role: context
  - path: reviews/structured/20261022T010353Z-cvt-vesicle-audit/review.yaml
    sha256: d59b0197adec346d7446a07ca5bd3d79a8bddfa40046e110081eff58c4b2e8cc
    role: context
  - path: reviews/structured/20261022T010357Z-cvt-vesicle-lumen-audit/review.md
    sha256: f03a3a5cd285bbd5381d84085ab7b657743ee10a6c2d1daeb2b17b0388632793
    role: context
  - path: reviews/structured/20261022T010357Z-cvt-vesicle-lumen-audit/review.yaml
    sha256: c15022bb93f16bda92f89bc7c8124c8014776de3e493c3783bb7b53f25d8caa4
    role: context
  - path: reviews/structured/20261022T010402Z-cvt-vesicle-membrane-audit/review.md
    sha256: 4ecb47906ca9c7d74ec2e7368e5c13cd644c4cabf6d21a17c01e68c3d3625c73
    role: context
  - path: reviews/structured/20261022T010402Z-cvt-vesicle-membrane-audit/review.yaml
    sha256: 4d33933a47cdf13e03b6c884954f32b566df400f8667e0bdd4064b87c30aeaf3
    role: context
  - path: reviews/structured/20261022T010406Z-cyanelle-audit/review.md
    sha256: 3286a2ed589a9404b10714107a537ef42d231c337a6f7402cc9f3fdf13dee537
    role: context
  - path: reviews/structured/20261022T010406Z-cyanelle-audit/review.yaml
    sha256: 2902d5c0cf0ba994861d191c9cb500d54d58a080e2f8bcdfc778aec66e077d4c
    role: context
  - path: reviews/structured/20261022T010409Z-cyanelle-envelope-audit/review.md
    sha256: 85a9f3d6783f4d25846dfdd154a513e14f31de1f9fa2242d2fbfc405486ee415
    role: context
  - path: reviews/structured/20261022T010409Z-cyanelle-envelope-audit/review.yaml
    sha256: b57e357b1140a5b5314c9d64838f9bcc466fc053b94ef9c218bbd72d1446b62b
    role: context
  - path: reviews/structured/20261022T010413Z-cyanelle-inner-membrane-audit/review.md
    sha256: 4c95a1d2a10bdb35602159c27498cf24e55637810e2f9d323275c17beb58cdc4
    role: context
  - path: reviews/structured/20261022T010413Z-cyanelle-inner-membrane-audit/review.yaml
    sha256: 079d9c5875583d0430999da5f358428312d945474c09882f9c47b7248b7147f0
    role: context
  - path: reviews/structured/20261022T010416Z-cyanelle-intermembrane-space-audit/review.md
    sha256: 8025c8b3338e6b2a7380c8d6ac4f03fd6d6f94f4d24aa45b0ecb774ae43d9258
    role: context
  - path: reviews/structured/20261022T010416Z-cyanelle-intermembrane-space-audit/review.yaml
    sha256: b15a205ca0cae3224ef5f0b52570d631a604a0a2a9db6b8fc3abf48687393c5f
    role: context
  - path: reviews/structured/20261022T010419Z-cyanelle-membrane-audit/review.md
    sha256: ab4142b95465695550f915402fbf74d4ffb1b60b2209f93bb23930db75f03cfc
    role: context
  - path: reviews/structured/20261022T010419Z-cyanelle-membrane-audit/review.yaml
    sha256: 7106f9791c22478e91dfea9fbf6c1eed74a5a98f8cd83517cfde7cc2a3fbb508
    role: context
  - path: reviews/structured/20261022T010421Z-cyanelle-outer-membrane-audit/review.md
    sha256: ef4864468b75363b348e2ab125444934e4aea5091324f3df2f6364899c6019e2
    role: context
  - path: reviews/structured/20261022T010421Z-cyanelle-outer-membrane-audit/review.yaml
    sha256: 81e5de805bca9fe7d3731dbad98ec9e831488b80e5304e0ac774ae581ebe450f
    role: context
  - path: reviews/structured/20261022T010425Z-cyanelle-stroma-audit/review.md
    sha256: 99bb176e5b93d1b8bdf930704f9d18b5a20032761154fbf7499b1522cef25cf3
    role: context
  - path: reviews/structured/20261022T010425Z-cyanelle-stroma-audit/review.yaml
    sha256: 66e2866e2593f996c1833f20e12642f5e7f44aa4d011ab48ba762da47207f133
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
- target_id: GO:0033107
  path: data/structures/membrane_organelle/cvt_vesicle.yaml
  label: Cvt vesicle
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cvt_vesicle.yaml
    role: maintained scientific record
- target_id: cellstructuremech:cvt_vesicle_lumen
  path: data/structures/membrane_organelle/cvt_vesicle_lumen.yaml
  label: Cvt vesicle lumen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cvt_vesicle_lumen.yaml
    role: maintained scientific record
- target_id: GO:0033110
  path: data/structures/membrane_organelle/cvt_vesicle_membrane.yaml
  label: Cvt vesicle membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cvt_vesicle_membrane.yaml
    role: maintained scientific record
- target_id: GO:0009842
  path: data/structures/membrane_organelle/cyanelle.yaml
  label: cyanelle
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cyanelle.yaml
    role: maintained scientific record
- target_id: GO:0033112
  path: data/structures/membrane_organelle/cyanelle_envelope.yaml
  label: cyanelle envelope
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cyanelle_envelope.yaml
    role: maintained scientific record
- target_id: GO:0036012
  path: data/structures/membrane_organelle/cyanelle_inner_membrane.yaml
  label: cyanelle inner membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cyanelle_inner_membrane.yaml
    role: maintained scientific record
- target_id: GO:0036014
  path: data/structures/membrane_organelle/cyanelle_intermembrane_space.yaml
  label: cyanelle intermembrane space
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cyanelle_intermembrane_space.yaml
    role: maintained scientific record
- target_id: GO:0033113
  path: data/structures/membrane_organelle/cyanelle_membrane.yaml
  label: cyanelle membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cyanelle_membrane.yaml
    role: maintained scientific record
- target_id: GO:0036013
  path: data/structures/membrane_organelle/cyanelle_outer_membrane.yaml
  label: cyanelle outer membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cyanelle_outer_membrane.yaml
    role: maintained scientific record
- target_id: GO:0034060
  path: data/structures/membrane_organelle/cyanelle_stroma.yaml
  label: cyanelle stroma
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cyanelle_stroma.yaml
    role: maintained scientific record
scope:
  description: Exact ten-record PR cohort reassessed against current main 41d0d30a456e5f1af1417f23afa89bc4fa0674ba.
    Changed inputs are substantively reassessed. Scientific records remain unchanged.
  selection: Complete cohort of ten maintained records reviewed in original PR head
    1d0845adece5711c9a194abadaf80aeec1eb8b50.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - GO:0033107
  - cellstructuremech:cvt_vesicle_lumen
  - GO:0033110
  - GO:0009842
  - GO:0033112
  - GO:0036012
  - GO:0036014
  - GO:0033113
  - GO:0036013
  - GO:0034060
checks:
- check_id: qc
  name: Full native QC
  status: passed
  required: true
  target_ids:
  - GO:0033107
  - cellstructuremech:cvt_vesicle_lumen
  - GO:0033110
  - GO:0009842
  - GO:0033112
  - GO:0036012
  - GO:0036014
  - GO:0033113
  - GO:0036013
  - GO:0034060
  command: just qc
  exit_code: 0
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  scope_note: Actual local execution at main-merge head ed8281f2fc915349c8ce429e7103e42b256c0533.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-qc
- check_id: labels
  name: Native label correspondence
  status: passed
  required: true
  target_ids:
  - GO:0033107
  - cellstructuremech:cvt_vesicle_lumen
  - GO:0033110
  - GO:0009842
  - GO:0033112
  - GO:0036012
  - GO:0036014
  - GO:0033113
  - GO:0036013
  - GO:0034060
  command: just validate-products
  exit_code: 0
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  scope_note: Actual local execution at main-merge head ed8281f2fc915349c8ce429e7103e42b256c0533.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-labels
- check_id: trait-links
  name: TraitMech references
  status: passed
  required: true
  target_ids:
  - GO:0033107
  - cellstructuremech:cvt_vesicle_lumen
  - GO:0033110
  - GO:0009842
  - GO:0033112
  - GO:0036012
  - GO:0036014
  - GO:0033113
  - GO:0036013
  - GO:0034060
  command: just check-trait-links
  exit_code: 0
  summary: Native TraitMech link check passed.
  scope_note: Actual local execution at main-merge head ed8281f2fc915349c8ce429e7103e42b256c0533.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-trait-links
- check_id: vendored
  name: Pinned governed files
  status: passed
  required: true
  target_ids:
  - GO:0033107
  - cellstructuremech:cvt_vesicle_lumen
  - GO:0033110
  - GO:0009842
  - GO:0033112
  - GO:0036012
  - GO:0036014
  - GO:0033113
  - GO:0036013
  - GO:0034060
  command: just vendored-check
  exit_code: 0
  summary: Pinned governed files match; native vendored check passed.
  scope_note: Actual local execution at main-merge head ed8281f2fc915349c8ce429e7103e42b256c0533.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-vendored
- check_id: curies
  name: Native identifier resolver
  status: passed
  required: true
  target_ids:
  - GO:0033107
  - cellstructuremech:cvt_vesicle_lumen
  - GO:0033110
  - GO:0009842
  - GO:0033112
  - GO:0036012
  - GO:0036014
  - GO:0033113
  - GO:0036013
  - GO:0034060
  command: just check-curies
  exit_code: 0
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  scope_note: Actual local execution at main-merge head ed8281f2fc915349c8ce429e7103e42b256c0533.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-curies
- check_id: focused-0
  name: validate GO:0033107
  status: passed
  required: true
  target_ids:
  - GO:0033107
  command: just validate data/structures/membrane_organelle/cvt_vesicle.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-1
  name: validate-strict GO:0033107
  status: passed
  required: true
  target_ids:
  - GO:0033107
  command: just validate-strict data/structures/membrane_organelle/cvt_vesicle.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-2
  name: validate cellstructuremech:cvt_vesicle_lumen
  status: passed
  required: true
  target_ids:
  - cellstructuremech:cvt_vesicle_lumen
  command: just validate data/structures/membrane_organelle/cvt_vesicle_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-3
  name: validate-strict cellstructuremech:cvt_vesicle_lumen
  status: passed
  required: true
  target_ids:
  - cellstructuremech:cvt_vesicle_lumen
  command: just validate-strict data/structures/membrane_organelle/cvt_vesicle_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-4
  name: validate GO:0033110
  status: passed
  required: true
  target_ids:
  - GO:0033110
  command: just validate data/structures/membrane_organelle/cvt_vesicle_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-5
  name: validate-strict GO:0033110
  status: passed
  required: true
  target_ids:
  - GO:0033110
  command: just validate-strict data/structures/membrane_organelle/cvt_vesicle_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-6
  name: validate GO:0009842
  status: passed
  required: true
  target_ids:
  - GO:0009842
  command: just validate data/structures/membrane_organelle/cyanelle.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-7
  name: validate-strict GO:0009842
  status: passed
  required: true
  target_ids:
  - GO:0009842
  command: just validate-strict data/structures/membrane_organelle/cyanelle.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-8
  name: validate GO:0033112
  status: passed
  required: true
  target_ids:
  - GO:0033112
  command: just validate data/structures/membrane_organelle/cyanelle_envelope.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-9
  name: validate-strict GO:0033112
  status: passed
  required: true
  target_ids:
  - GO:0033112
  command: just validate-strict data/structures/membrane_organelle/cyanelle_envelope.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-10
  name: validate GO:0036012
  status: passed
  required: true
  target_ids:
  - GO:0036012
  command: just validate data/structures/membrane_organelle/cyanelle_inner_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-11
  name: validate-strict GO:0036012
  status: passed
  required: true
  target_ids:
  - GO:0036012
  command: just validate-strict data/structures/membrane_organelle/cyanelle_inner_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-12
  name: validate GO:0036014
  status: passed
  required: true
  target_ids:
  - GO:0036014
  command: just validate data/structures/membrane_organelle/cyanelle_intermembrane_space.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-13
  name: validate-strict GO:0036014
  status: passed
  required: true
  target_ids:
  - GO:0036014
  command: just validate-strict data/structures/membrane_organelle/cyanelle_intermembrane_space.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-14
  name: validate GO:0033113
  status: passed
  required: true
  target_ids:
  - GO:0033113
  command: just validate data/structures/membrane_organelle/cyanelle_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-15
  name: validate-strict GO:0033113
  status: passed
  required: true
  target_ids:
  - GO:0033113
  command: just validate-strict data/structures/membrane_organelle/cyanelle_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-16
  name: validate GO:0036013
  status: passed
  required: true
  target_ids:
  - GO:0036013
  command: just validate data/structures/membrane_organelle/cyanelle_outer_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-17
  name: validate-strict GO:0036013
  status: passed
  required: true
  target_ids:
  - GO:0036013
  command: just validate-strict data/structures/membrane_organelle/cyanelle_outer_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-18
  name: validate GO:0034060
  status: passed
  required: true
  target_ids:
  - GO:0034060
  command: just validate data/structures/membrane_organelle/cyanelle_stroma.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-19
  name: validate-strict GO:0034060
  status: passed
  required: true
  target_ids:
  - GO:0034060
  command: just validate-strict data/structures/membrane_organelle/cyanelle_stroma.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: supplemental-pmid
  name: Supplemental bounded PMID authority checks
  status: passed
  required: true
  target_ids:
  - GO:0033107
  - cellstructuremech:cvt_vesicle_lumen
  - GO:0033110
  - GO:0009842
  - GO:0033112
  - GO:0036012
  - GO:0036014
  - GO:0033113
  - GO:0036013
  - GO:0034060
  command: .venv/bin/python /private/tmp/cellstructure-batches-2346-2397-20261103/check_pmid_chunks.py
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362
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
  - GO:0033107
  - cellstructuremech:cvt_vesicle_lumen
  - GO:0033110
  - GO:0009842
  - GO:0033112
  - GO:0036012
  - GO:0036014
  - GO:0033113
  - GO:0036013
  - GO:0034060
  summary: 'Four unsupported expression-only applicability exclusions are corrected:
    the three Cvt carrier/lumen/membrane records name Cvt or early-secretory pathway
    and molecular context, and whole cyanelle asserts photosynthesis. Six cyanelle
    boundary/material records remain genuine exclusions after full-claim inspection.
    Complete official catalogue coverage has no matching relevant yeast or Cyanophora
    dataset; no unrelated organism or downstream module query substitutes for noncoverage.
    Resource noncoverage is not biological absence. The retained historical runner
    failure is not a fresh invocation.'
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
  - GO:0033107
  - cellstructuremech:cvt_vesicle_lumen
  - GO:0033110
  - GO:0009842
  - GO:0033112
  - GO:0036012
  - GO:0036014
  - GO:0033113
  - GO:0036013
  - GO:0034060
  summary: Three read-only reviewers covered the complete ten-record cohort, including
    changed inputs, with explicit scientific findings and source-access limits. Final
    artifact/head acceptance occurs after saving.
  evidence_ids:
  - plaque-policy
  - plaque-rubric
  - plaque-graph-policy
  - plaque-schema-policy
  - plaque-shared-go
  - plaque-cyanelle-boundary-parents
  - plaque-cyanelle-SL-0480
  - plaque-cyanelle-SL-0481
  - plaque-cyanelle-SL-0482
  - plaque-cyanelle-SL-0083
  - plaque-shared-tax2762
  - plaque-shared-tax38254
  - plaque-shared-giddings1983-meta
  - plaque-shared-giddings1983-page409
  - plaque-shared-giddings1983-page414
  - plaque-shared-giddings1983-page416
  - plaque-shared-giddings1983-page417
  - plaque-shared-pfanzagl1996-meta
  - plaque-pfanzagl-comparative-meta
  - plaque-pfanzagl-comparative-body
  - plaque-kojima2016-meta
  - plaque-kojima2016-canonical
  - plaque-kojima2016-body
  - plaque-kojima2016-s3
  - plaque-kojima2016-epmcxml
  - plaque-catalogue
  - micro-policy
  - micro-go
  - micro-ims-go-path
  - micro-SL-0082
  - micro-SL-0479
  - micro-SL-0350
  - micro-cyanelle-SL-0480
  - micro-tax2762
  - micro-tax38254
  - micro-giddings1983-meta
  - micro-giddings1983-page409
  - micro-giddings1983-page410
  - micro-giddings1983-page412
  - micro-giddings1983-page414
  - micro-giddings1983-page416
  - micro-giddings1983-page417
  - micro-pfanzagl1996-meta
  - micro-pfanzagl-comparative-meta
  - micro-kojima2016-canonical
  - micro-price2019-meta
  - micro-price2019-s3
  - septin-review-policy
  - septin-curation-policy
  - septin-graph-policy
  - septin-go
  - septin-tax4932
  - septin-SL0080
  - septin-SL0081
  - septin-SL0323
  - septin-reggiori2004-meta
  - septin-shintani2004-meta
  - septin-scott2001-meta
  - septin-reggiori2004-pmc-prefixed
  - septin-shintani2004-pmc-prefixed
  - septin-scott2001-pmc-prefixed
- check_id: historical-adapter-runner
  name: Retained historical adapter runner availability
  status: unavailable
  required: false
  target_ids:
  - GO:0033107
  - cellstructuremech:cvt_vesicle_lumen
  - GO:0033110
  - GO:0009842
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
- check_id: cvt_vesicle-uniprot-verify
  name: Native cvt vesicle UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0033107
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cvt_vesicle.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero on an empty represented protein
    inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative
    molecules, localization, mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-cvt_vesicle-verify
- check_id: cvt_vesicle-uniprot-causal
  name: Native cvt vesicle UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0033107
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cvt_vesicle.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero on an empty represented protein
    inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative
    molecules, localization, mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-cvt_vesicle-causal
- check_id: cvt_vesicle_lumen-uniprot-verify
  name: Native cvt vesicle lumen UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:cvt_vesicle_lumen
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cvt_vesicle_lumen.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero on an empty represented protein
    inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative
    molecules, localization, mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-cvt_vesicle_lumen-verify
- check_id: cvt_vesicle_lumen-uniprot-causal
  name: Native cvt vesicle lumen UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:cvt_vesicle_lumen
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cvt_vesicle_lumen.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero on an empty represented protein
    inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative
    molecules, localization, mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-cvt_vesicle_lumen-causal
- check_id: cvt_vesicle_membrane-uniprot-verify
  name: Native cvt vesicle membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0033110
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cvt_vesicle_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero on an empty represented protein
    inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative
    molecules, localization, mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-cvt_vesicle_membrane-verify
- check_id: cvt_vesicle_membrane-uniprot-causal
  name: Native cvt vesicle membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0033110
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cvt_vesicle_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero on an empty represented protein
    inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative
    molecules, localization, mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-cvt_vesicle_membrane-causal
- check_id: cyanelle-uniprot-verify
  name: Native cyanelle UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0009842
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero on an empty represented protein
    inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative
    molecules, localization, mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-cyanelle-verify
- check_id: cyanelle-uniprot-causal
  name: Native cyanelle UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0009842
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero on an empty represented protein
    inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative
    molecules, localization, mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-cyanelle-causal
- check_id: cyanelle_envelope-uniprot-verify
  name: Native cyanelle envelope UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0033112
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_envelope.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero on an empty represented protein
    inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative
    molecules, localization, mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-cyanelle_envelope-verify
- check_id: cyanelle_envelope-uniprot-causal
  name: Native cyanelle envelope UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0033112
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_envelope.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero on an empty represented protein
    inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative
    molecules, localization, mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-cyanelle_envelope-causal
- check_id: cyanelle_inner_membrane-uniprot-verify
  name: Native cyanelle inner membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0036012
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_inner_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero on an empty represented protein
    inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative
    molecules, localization, mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-cyanelle_inner_membrane-verify
- check_id: cyanelle_inner_membrane-uniprot-causal
  name: Native cyanelle inner membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0036012
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_inner_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero on an empty represented protein
    inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative
    molecules, localization, mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-cyanelle_inner_membrane-causal
- check_id: cyanelle_intermembrane_space-uniprot-verify
  name: Native cyanelle intermembrane space UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0036014
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_intermembrane_space.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero on an empty represented protein
    inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative
    molecules, localization, mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-cyanelle_intermembrane_space-verify
- check_id: cyanelle_intermembrane_space-uniprot-causal
  name: Native cyanelle intermembrane space UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0036014
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_intermembrane_space.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero on an empty represented protein
    inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative
    molecules, localization, mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-cyanelle_intermembrane_space-causal
- check_id: cyanelle_membrane-uniprot-verify
  name: Native cyanelle membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0033113
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero on an empty represented protein
    inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative
    molecules, localization, mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-cyanelle_membrane-verify
- check_id: cyanelle_membrane-uniprot-causal
  name: Native cyanelle membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0033113
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero on an empty represented protein
    inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative
    molecules, localization, mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-cyanelle_membrane-causal
- check_id: cyanelle_outer_membrane-uniprot-verify
  name: Native cyanelle outer membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0036013
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_outer_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero on an empty represented protein
    inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative
    molecules, localization, mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-cyanelle_outer_membrane-verify
- check_id: cyanelle_outer_membrane-uniprot-causal
  name: Native cyanelle outer membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0036013
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_outer_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero on an empty represented protein
    inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative
    molecules, localization, mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-cyanelle_outer_membrane-causal
- check_id: cyanelle_stroma-uniprot-verify
  name: Native cyanelle stroma UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0034060
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_stroma.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero on an empty represented protein
    inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative
    molecules, localization, mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-cyanelle_stroma-verify
- check_id: cyanelle_stroma-uniprot-causal
  name: Native cyanelle stroma UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0034060
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_stroma.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero on an empty represented protein
    inventory and zero typed GENE_OR_PROTEIN nodes. This does not validate narrative
    molecules, localization, mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-cyanelle_stroma-causal
evidence:
- evidence_id: current-record-0
  kind: record_content
  reference: data/structures/membrane_organelle/cvt_vesicle.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T11:59:12Z'
  support: context_only
  summary: Original frozen SHA256 cf6eb5075a057a0b8b104cbacb61cdf895298eb4b018945a08b46bcb939c8b0c;
    current SHA256 cf6eb5075a057a0b8b104cbacb61cdf895298eb4b018945a08b46bcb939c8b0c.
    Record bytes unchanged since the original review.
  snapshot_sha256: cf6eb5075a057a0b8b104cbacb61cdf895298eb4b018945a08b46bcb939c8b0c
- evidence_id: original-review-0
  kind: prior_review
  reference: reviews/structured/20261022T010353Z-cvt-vesicle-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T11:59:12Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: d59b0197adec346d7446a07ca5bd3d79a8bddfa40046e110081eff58c4b2e8cc
- evidence_id: current-record-1
  kind: record_content
  reference: data/structures/membrane_organelle/cvt_vesicle_lumen.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T11:59:12Z'
  support: context_only
  summary: Original frozen SHA256 3bb8cb5c3f751ec93619bb4658fb51a2c6e6a94e4e0b16aa0ea8a0833a28c243;
    current SHA256 3bb8cb5c3f751ec93619bb4658fb51a2c6e6a94e4e0b16aa0ea8a0833a28c243.
    Record bytes unchanged since the original review.
  snapshot_sha256: 3bb8cb5c3f751ec93619bb4658fb51a2c6e6a94e4e0b16aa0ea8a0833a28c243
- evidence_id: original-review-1
  kind: prior_review
  reference: reviews/structured/20261022T010357Z-cvt-vesicle-lumen-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T11:59:12Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: c15022bb93f16bda92f89bc7c8124c8014776de3e493c3783bb7b53f25d8caa4
- evidence_id: current-record-2
  kind: record_content
  reference: data/structures/membrane_organelle/cvt_vesicle_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T11:59:12Z'
  support: context_only
  summary: Original frozen SHA256 679cdeb18f93b2ecf38916c132f8461121e7067f0db52e4b24842559b39dbb67;
    current SHA256 679cdeb18f93b2ecf38916c132f8461121e7067f0db52e4b24842559b39dbb67.
    Record bytes unchanged since the original review.
  snapshot_sha256: 679cdeb18f93b2ecf38916c132f8461121e7067f0db52e4b24842559b39dbb67
- evidence_id: original-review-2
  kind: prior_review
  reference: reviews/structured/20261022T010402Z-cvt-vesicle-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T11:59:12Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 4d33933a47cdf13e03b6c884954f32b566df400f8667e0bdd4064b87c30aeaf3
- evidence_id: current-record-3
  kind: record_content
  reference: data/structures/membrane_organelle/cyanelle.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T11:59:12Z'
  support: context_only
  summary: Original frozen SHA256 24275c8050ca5d13c66d563c7aa697a4de65766f87499f876fc94c41cd2f0db7;
    current SHA256 5ebb2c3b4cc2d9364dc08ac335c793409014f30f0ca009ee3b4aeafb860371b6.
    Changed record reassessed against current sources.
  snapshot_sha256: 5ebb2c3b4cc2d9364dc08ac335c793409014f30f0ca009ee3b4aeafb860371b6
- evidence_id: original-review-3
  kind: prior_review
  reference: reviews/structured/20261022T010406Z-cyanelle-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T11:59:12Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 2902d5c0cf0ba994861d191c9cb500d54d58a080e2f8bcdfc778aec66e077d4c
- evidence_id: current-record-4
  kind: record_content
  reference: data/structures/membrane_organelle/cyanelle_envelope.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T11:59:12Z'
  support: context_only
  summary: Original frozen SHA256 4a25594b3a26541401976d3ab78f271bc8726951462af9073fafc0eff2389a67;
    current SHA256 4a25594b3a26541401976d3ab78f271bc8726951462af9073fafc0eff2389a67.
    Record bytes unchanged since the original review.
  snapshot_sha256: 4a25594b3a26541401976d3ab78f271bc8726951462af9073fafc0eff2389a67
- evidence_id: original-review-4
  kind: prior_review
  reference: reviews/structured/20261022T010409Z-cyanelle-envelope-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T11:59:12Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: b57e357b1140a5b5314c9d64838f9bcc466fc053b94ef9c218bbd72d1446b62b
- evidence_id: current-record-5
  kind: record_content
  reference: data/structures/membrane_organelle/cyanelle_inner_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T11:59:12Z'
  support: context_only
  summary: Original frozen SHA256 f10bb4f3ff44fb6d0b23e67379861768a590eb6d3da75686e296a0a5b3b26970;
    current SHA256 f10bb4f3ff44fb6d0b23e67379861768a590eb6d3da75686e296a0a5b3b26970.
    Record bytes unchanged since the original review.
  snapshot_sha256: f10bb4f3ff44fb6d0b23e67379861768a590eb6d3da75686e296a0a5b3b26970
- evidence_id: original-review-5
  kind: prior_review
  reference: reviews/structured/20261022T010413Z-cyanelle-inner-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T11:59:12Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 079d9c5875583d0430999da5f358428312d945474c09882f9c47b7248b7147f0
- evidence_id: current-record-6
  kind: record_content
  reference: data/structures/membrane_organelle/cyanelle_intermembrane_space.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T11:59:12Z'
  support: context_only
  summary: Original frozen SHA256 aba8ad62f544ec82bea2f4767a8c79cc45d3fe117423163fc1ce1211a2527f8c;
    current SHA256 aba8ad62f544ec82bea2f4767a8c79cc45d3fe117423163fc1ce1211a2527f8c.
    Record bytes unchanged since the original review.
  snapshot_sha256: aba8ad62f544ec82bea2f4767a8c79cc45d3fe117423163fc1ce1211a2527f8c
- evidence_id: original-review-6
  kind: prior_review
  reference: reviews/structured/20261022T010416Z-cyanelle-intermembrane-space-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T11:59:12Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: b15a205ca0cae3224ef5f0b52570d631a604a0a2a9db6b8fc3abf48687393c5f
- evidence_id: current-record-7
  kind: record_content
  reference: data/structures/membrane_organelle/cyanelle_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T11:59:12Z'
  support: context_only
  summary: Original frozen SHA256 b95c9fcb293bd9f434df3ccf9ecaa7c9bf04e1f83a95a2cd19673441a537a20b;
    current SHA256 b95c9fcb293bd9f434df3ccf9ecaa7c9bf04e1f83a95a2cd19673441a537a20b.
    Record bytes unchanged since the original review.
  snapshot_sha256: b95c9fcb293bd9f434df3ccf9ecaa7c9bf04e1f83a95a2cd19673441a537a20b
- evidence_id: original-review-7
  kind: prior_review
  reference: reviews/structured/20261022T010419Z-cyanelle-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T11:59:12Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 7106f9791c22478e91dfea9fbf6c1eed74a5a98f8cd83517cfde7cc2a3fbb508
- evidence_id: current-record-8
  kind: record_content
  reference: data/structures/membrane_organelle/cyanelle_outer_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T11:59:12Z'
  support: context_only
  summary: Original frozen SHA256 2f058b25ce3bf1b49d52bc03391ee46d6e26376860035469f037d27c52234047;
    current SHA256 2f058b25ce3bf1b49d52bc03391ee46d6e26376860035469f037d27c52234047.
    Record bytes unchanged since the original review.
  snapshot_sha256: 2f058b25ce3bf1b49d52bc03391ee46d6e26376860035469f037d27c52234047
- evidence_id: original-review-8
  kind: prior_review
  reference: reviews/structured/20261022T010421Z-cyanelle-outer-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T11:59:12Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 81e5de805bca9fe7d3731dbad98ec9e831488b80e5304e0ac774ae581ebe450f
- evidence_id: current-record-9
  kind: record_content
  reference: data/structures/membrane_organelle/cyanelle_stroma.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T11:59:12Z'
  support: context_only
  summary: Original frozen SHA256 13d83e3dadca9cafaa6550a7bf84cd8066bf1539ccaacd3627ec23aa5b08e118;
    current SHA256 13d83e3dadca9cafaa6550a7bf84cd8066bf1539ccaacd3627ec23aa5b08e118.
    Record bytes unchanged since the original review.
  snapshot_sha256: 13d83e3dadca9cafaa6550a7bf84cd8066bf1539ccaacd3627ec23aa5b08e118
- evidence_id: original-review-9
  kind: prior_review
  reference: reviews/structured/20261022T010425Z-cyanelle-stroma-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T11:59:12Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 66e2866e2593f996c1833f20e12642f5e7f44aa4d011ab48ba762da47207f133
- evidence_id: plaque-current-5
  kind: record_content
  reference: data/structures/membrane_organelle/cyanelle_inner_membrane.yaml
  locator: Entire maintained record at source ed8281f2fc915349c8ce429e7103e42b256c0533;
    all fields, histories, discussions and graphs
  summary: Entire current target independently read. Hash remains unchanged from original
    frozen target; PROPOSED status unchanged and no record curation performed.
  accessed_at: '2026-11-03T11:55:26.475588Z'
  support: supports
  snapshot_sha256: f10bb4f3ff44fb6d0b23e67379861768a590eb6d3da75686e296a0a5b3b26970
- evidence_id: plaque-original-5
  kind: prior_review
  reference: reviews/structured/20261022T010413Z-cyanelle-inner-membrane-audit/review.yaml
  locator: Original authoritative YAML/Markdown, source inputs, checks, assessments,
    findings/actions and limitations
  summary: Original native validate/render passes and all original historical input
    hashes match. Verdict pass_with_limitations, no findings or actions; no original
    scientific finding exists to terminally dispose of.
  accessed_at: '2026-11-03T11:55:26.475588Z'
  support: supports
  snapshot_sha256: 079d9c5875583d0430999da5f358428312d945474c09882f9c47b7248b7147f0
- evidence_id: plaque-current-6
  kind: record_content
  reference: data/structures/membrane_organelle/cyanelle_intermembrane_space.yaml
  locator: Entire maintained record at source ed8281f2fc915349c8ce429e7103e42b256c0533;
    all fields, histories, discussions and graphs
  summary: Entire current target independently read. Hash remains unchanged from original
    frozen target; PROPOSED status unchanged and no record curation performed.
  accessed_at: '2026-11-03T11:55:26.475588Z'
  support: supports
  snapshot_sha256: aba8ad62f544ec82bea2f4767a8c79cc45d3fe117423163fc1ce1211a2527f8c
- evidence_id: plaque-original-6
  kind: prior_review
  reference: reviews/structured/20261022T010416Z-cyanelle-intermembrane-space-audit/review.yaml
  locator: Original authoritative YAML/Markdown, source inputs, checks, assessments,
    findings/actions and limitations
  summary: Original native validate/render passes and all original historical input
    hashes match. Verdict pass_with_limitations, no findings or actions; no original
    scientific finding exists to terminally dispose of.
  accessed_at: '2026-11-03T11:55:26.475588Z'
  support: supports
  snapshot_sha256: b15a205ca0cae3224ef5f0b52570d631a604a0a2a9db6b8fc3abf48687393c5f
- evidence_id: plaque-current-7
  kind: record_content
  reference: data/structures/membrane_organelle/cyanelle_membrane.yaml
  locator: Entire maintained record at source ed8281f2fc915349c8ce429e7103e42b256c0533;
    all fields, histories, discussions and graphs
  summary: Entire current target independently read. Hash remains unchanged from original
    frozen target; PROPOSED status unchanged and no record curation performed.
  accessed_at: '2026-11-03T11:55:26.475588Z'
  support: supports
  snapshot_sha256: b95c9fcb293bd9f434df3ccf9ecaa7c9bf04e1f83a95a2cd19673441a537a20b
- evidence_id: plaque-original-7
  kind: prior_review
  reference: reviews/structured/20261022T010419Z-cyanelle-membrane-audit/review.yaml
  locator: Original authoritative YAML/Markdown, source inputs, checks, assessments,
    findings/actions and limitations
  summary: Original native validate/render passes and all original historical input
    hashes match. Verdict pass_with_limitations, no findings or actions; no original
    scientific finding exists to terminally dispose of.
  accessed_at: '2026-11-03T11:55:26.475588Z'
  support: supports
  snapshot_sha256: 7106f9791c22478e91dfea9fbf6c1eed74a5a98f8cd83517cfde7cc2a3fbb508
- evidence_id: plaque-current-8
  kind: record_content
  reference: data/structures/membrane_organelle/cyanelle_outer_membrane.yaml
  locator: Entire maintained record at source ed8281f2fc915349c8ce429e7103e42b256c0533;
    all fields, histories, discussions and graphs
  summary: Entire current target independently read. Hash remains unchanged from original
    frozen target; PROPOSED status unchanged and no record curation performed.
  accessed_at: '2026-11-03T11:55:26.475588Z'
  support: supports
  snapshot_sha256: 2f058b25ce3bf1b49d52bc03391ee46d6e26376860035469f037d27c52234047
- evidence_id: plaque-original-8
  kind: prior_review
  reference: reviews/structured/20261022T010421Z-cyanelle-outer-membrane-audit/review.yaml
  locator: Original authoritative YAML/Markdown, source inputs, checks, assessments,
    findings/actions and limitations
  summary: Original native validate/render passes and all original historical input
    hashes match. Verdict pass_with_limitations, no findings or actions; no original
    scientific finding exists to terminally dispose of.
  accessed_at: '2026-11-03T11:55:26.475588Z'
  support: supports
  snapshot_sha256: 81e5de805bca9fe7d3731dbad98ec9e831488b80e5304e0ac774ae581ebe450f
- evidence_id: plaque-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Frozen native review, material identity, component, graph and structured-source
    applicability contract
  summary: Actual named genes/proteins/regulators/pathways/stress responses/traits
    trigger structured-source assessment. Generic material/topology or explicitly
    withheld molecular assignments are genuine exclusions. No missing molecular inventory
    is fabricated merely because a membrane contains proteins.
  accessed_at: '2026-11-03T11:55:26.475588Z'
  support: context_only
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: plaque-rubric
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Frozen native review, material identity, component, graph and structured-source
    applicability contract
  summary: Actual named genes/proteins/regulators/pathways/stress responses/traits
    trigger structured-source assessment. Generic material/topology or explicitly
    withheld molecular assignments are genuine exclusions. No missing molecular inventory
    is fabricated merely because a membrane contains proteins.
  accessed_at: '2026-11-03T11:55:26.475588Z'
  support: context_only
  snapshot_sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
- evidence_id: plaque-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Frozen native review, material identity, component, graph and structured-source
    applicability contract
  summary: Actual named genes/proteins/regulators/pathways/stress responses/traits
    trigger structured-source assessment. Generic material/topology or explicitly
    withheld molecular assignments are genuine exclusions. No missing molecular inventory
    is fabricated merely because a membrane contains proteins.
  accessed_at: '2026-11-03T11:55:26.475588Z'
  support: context_only
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: plaque-schema-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Frozen native review, material identity, component, graph and structured-source
    applicability contract
  summary: Actual named genes/proteins/regulators/pathways/stress responses/traits
    trigger structured-source assessment. Generic material/topology or explicitly
    withheld molecular assignments are genuine exclusions. No missing molecular inventory
    is fabricated merely because a membrane contains proteins.
  accessed_at: '2026-11-03T11:55:26.475588Z'
  support: context_only
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: plaque-shared-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009842,GO:0009536,GO:0033112,GO:0036012,GO:0036013,GO:0036014,GO:0034060,GO:0009843,GO:0033114,GO:0033115,GO:0033113,GO:0042170,GO:0009527,GO:0009532,GO:0005737,GO:0015979,GO:0009526
  locator: Exact identities/active definitions/synonyms of represented cyanelle/plastid/cytoplasm
    terms; typed child relations for0042170,0033113,0033112,0009527 and0034060 context
  summary: Inner0036012 and outer0036013 are is_a children of generic envelope membrane0033113,
    which is part_of envelope0033112. Envelope also has IMS0036014 as part_of. Plastid
    outer0009527 has outer cyanelle membrane as is_a child. Inner/outer direct envelope
    parthood is additionally explicit in UniProt; no missing direct GO relation is
    invented. Envelope membranes, stroma and thylakoids remain distinct. Same-PR public
    snapshot independently read with original fetch timestamp retained.
  accessed_at: '2026-11-03T11:52:36.404418Z'
  support: supports
  snapshot_sha256: b294054ca58e46634347a17541b9c003d339a6230c57b18920cad889fab06532
- evidence_id: plaque-cyanelle-boundary-parents
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009528,GO:0009529
  locator: Complete exact0009528/0009529 definitions, active status and direct typed
    child relations
  summary: Plastid inner membrane0009528 has cyanelle inner0036012 as is_a child;
    plastid IMS0009529 has cyanelle IMS0036014 as is_a child. This verifies exact
    parent types rather than inferring them from mixed ancestry.
  accessed_at: '2026-11-03T11:52:14.167746Z'
  support: supports
  snapshot_sha256: b8d234500ad7a085d60e4fbf0476277292680c7f4ba9db8e653155fbab33a90d
- evidence_id: plaque-cyanelle-SL-0480
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0480.json
  locator: Complete top-level definition, synonyms, direct GO correspondence, immediate
    isA/partOf; nested objects distinguished
  summary: SL0480 defines the stroma/IMS separator, directly maps toGO0036012, has
    generic cyanelle/plastid-inner isA and envelope partOf. Protein-count statistics
    are not structural prevalence or constituent necessity evidence.
  accessed_at: '2026-11-03T11:52:14.167349Z'
  support: supports
  snapshot_sha256: b91c540680ba95ebee76012cbfcb23234f3ef6df3427a70bb85fcadd801933e9
- evidence_id: plaque-cyanelle-SL-0481
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0481.json
  locator: Complete top-level definition, synonyms, direct GO correspondence, immediate
    isA/partOf; nested objects distinguished
  summary: SL0481 defines the region between inner/outer membranes including the vestigial
    PG layer, directly mapsGO0036014, has plastid-IMS parent and envelope partOf.
    Protein-count statistics are not structural prevalence or constituent necessity
    evidence.
  accessed_at: '2026-11-03T11:52:14.167545Z'
  support: supports
  snapshot_sha256: 62b1e54da01decbbb01d4f3b94b8cdeda5f079a6dd8dd7c184984e5f9b20318d
- evidence_id: plaque-cyanelle-SL-0482
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0482.json
  locator: Complete top-level definition, synonyms, direct GO correspondence, immediate
    isA/partOf; nested objects distinguished
  summary: SL0482 defines the cytoplasm-facing cyanelle membrane, mapsGO0036013, has
    generic cyanelle/plastid-outer parents and envelope partOf. Protein-count statistics
    are not structural prevalence or constituent necessity evidence.
  accessed_at: '2026-11-03T11:52:14.167641Z'
  support: supports
  snapshot_sha256: a4b7b6ebfe0a2ef50b64e7fecb7a4a41941b2b230fa4dc68c5e946e62843c5c3
- evidence_id: plaque-cyanelle-SL-0083
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0083.json
  locator: Complete top-level definition, synonyms, direct GO correspondence, immediate
    isA/partOf; nested objects distinguished
  summary: SL0083 mapsGO0033113 but explicitly permits unresolved outer/inner/thylakoid
    protein localization. The maintained generic record correctly treats this as broader
    fallback, not an exact xref or expansion of GO envelope-only scope. Protein-count
    statistics are not structural prevalence or constituent necessity evidence.
  accessed_at: '2026-11-03T11:52:14.167699Z'
  support: supports
  snapshot_sha256: 88194546a200aedf9070c559be5ef3955bd191f495627362f8cc1b7b5deeed86
- evidence_id: plaque-shared-tax2762
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2762
  locator: Complete native taxId/scientificName/rank/lineage/alternative names
  summary: Native ENA verifies Cyanophora paradoxa 2762. Species belongs to Glaucocystophyceae.
    Identity does not establish experimental strain or quantitative prevalence; same-PR
    snapshot independently reread.
  accessed_at: '2026-11-03T11:52:36.404873Z'
  support: supports
  snapshot_sha256: 8384800c0c30321c096fb48117051165d50982c461255fe65d738d523d60ed7a
- evidence_id: plaque-shared-tax38254
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/38254
  locator: Complete native taxId/scientificName/rank/lineage/alternative names
  summary: Native ENA verifies Glaucocystophyceae 38254. Glaucophyta and Glaucophyceae
    are synonyms of class Glaucocystophyceae. Identity does not establish experimental
    strain or quantitative prevalence; same-PR snapshot independently reread.
  accessed_at: '2026-11-03T11:52:36.404908Z'
  support: supports
  snapshot_sha256: 4b487eb0e34bcb4941fbb315aae5214c96ea6f60255d71a2aca172cd35844009
- evidence_id: plaque-shared-giddings1983-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1104%2Fpp.71.2.409
  locator: Complete primary abstract and exact title/authors/year/DOI/PMID metadata
  summary: Giddings/Wasmann/Staehelin1983 distinguishes inner envelope membrane and
    two exterior layers by thin sections/freeze fracture. Presumptive PG/LPS assignment
    and historical symbiont interpretation are not upgraded to current molecular certainty.
    The separate fresh source scans support inspected body scope.
  accessed_at: '2026-11-03T11:52:37.145401Z'
  support: supports
  snapshot_sha256: e9050ae8f4efd4fb2d2362f165fcf9704d181bed10bd5e996a87e7ae85d79c02
- evidence_id: plaque-shared-giddings1983-page409
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/6ed041edd2c7/plntphys00558-0203.png
  locator: 'Complete scanned page409 visually inspected: title/authors, abstract,
    Introduction and culture/initial isolation Methods'
  summary: Source identifies C.paradoxa UTEX LB555,26C,modified CY-II medium and continuous
    illumination. Historical endosymbiont terminology is not imposed on modern GO
    organelle identity. Public scan independently viewed from same-PR shared snapshot
    at actual retained fetch time; not a full-paper claim.
  accessed_at: '2026-11-03T11:52:37.773780Z'
  support: supports
  snapshot_sha256: c0184058c66810b2544be1af57fac9acc2bbbfcdf71ee1186aade8232e5c9f61
- evidence_id: plaque-shared-giddings1983-page414
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/9d4d067999da/plntphys00558-0208.png
  locator: 'Complete scanned page414 visually inspected: Envelope Membranes Results
    opening, Figure11/12 images and captions'
  summary: Envelope Results distinguish inner membrane and wall layer. Figure12 identifies
    inner-membrane P-face and thickened wall at cleavage furrow; Figure11 is thylakoid
    context, not envelope. Public scan independently viewed from same-PR shared snapshot
    at actual retained fetch time; not a full-paper claim.
  accessed_at: '2026-11-03T11:52:38.060694Z'
  support: supports
  snapshot_sha256: 331f5f9fdd4e16e2a8cb67d9b5d45cca5467dc6554051cfa6696e34471e7bb82
- evidence_id: plaque-shared-giddings1983-page416
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/c329334d81e0/plntphys00558-0210.png
  locator: 'Complete scanned page416 visually inspected: Envelope Results continuation,
    Figure15 histogram/caption and Discussion opening'
  summary: Outer-envelope fracture faces occur exterior to presumed PG; isolation
    can produce membrane blisters/peeling, exposing underlying smooth wall. No raw
    histogram or microscopy measurement reanalysis. Public scan independently viewed
    from same-PR shared snapshot at actual retained fetch time; not a full-paper claim.
  accessed_at: '2026-11-03T11:52:38.068083Z'
  support: supports
  snapshot_sha256: 41f820c6bde6abc4318ac32baa45293634543bb4aceb0dc5129c3d25414e91ef
- evidence_id: plaque-shared-giddings1983-page417
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/7694ed6a7a74/plntphys00558-0211.png
  locator: 'Complete scanned page417 visually inspected: envelope Discussion and Figure16–18
    images/captions plus adjacent text'
  summary: Inner membrane is distinct from thylakoids, with no observed continuity.
    Figure17 shows outer-envelope membrane detached from PG; Figure18 shows exposed
    layer after membrane removal. Historical chemical and organelle-status interpretations
    remain qualified. Public scan independently viewed from same-PR shared snapshot
    at actual retained fetch time; not a full-paper claim.
  accessed_at: '2026-11-03T11:52:38.074636Z'
  support: supports
  snapshot_sha256: 276c1cb60d1a909200199f8e24495840d2caa5f5131c8a896d3f97d70e5bcf6f
- evidence_id: plaque-shared-pfanzagl1996-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1128%2Fjb.178.2.332-339.1996
  locator: Complete primary abstract and exact title/authors/year/DOI and PMID8550450
    metadata
  summary: Pfanzagl1996 primary-structure study biochemically characterizes C.paradoxa
    cyanelle PG using separated muropeptides and mass spectrometry. This supports
    material presence, not every reported chemical measurement, all glaucophyte species,
    a complete protein inventory or individual formation necessity. Abstract tier
    only in this reviewer.
  accessed_at: '2026-11-03T11:52:37.151802Z'
  support: supports
  snapshot_sha256: 83885c5efad4f11a564a920fd758d6d4c3d0f303810b056da883f23b995e92b8
- evidence_id: plaque-pfanzagl-comparative-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:8955325%20AND%20SRC:MED
  locator: Complete primary abstract, precise PMID8955325/DOI10.1128/jb.178.23.6994-6997.1996
    and title/authors/year
  summary: Comparative study directly analyzes Glaucocystis nostochinearum and Cyanoptyche
    gloeocystis cyanelle PG with chromatography/mass spectrometry, in comparison with
    prior Cyanophora evidence. The named genera in the IMS taxon note are supported;
    no universal recipe or numerical prevalence follows.
  accessed_at: '2026-11-03T11:52:14.174981Z'
  support: supports
  snapshot_sha256: 703ee4ecc41c108b84a9333646b4cb2357a8fbdb9a0ed2dabed6392f8f2b63a1
- evidence_id: plaque-pfanzagl-comparative-body
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/178604/
  locator: Genuine PMC title/byline/abstract and PDF-only full-text landing surface
  summary: This successful HTML retrieval supplies the same complete abstract and
    a link to PDF, not the article body. No full comparative-body or underlying measurement
    reanalysis is claimed.
  accessed_at: '2026-11-03T11:52:36.877869Z'
  support: context_only
  snapshot_sha256: d2a50900fc3c1a86177069d09a4e09262b5aed7a0dcc42e12fe0293d4ba8697a
- evidence_id: plaque-kojima2016-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI:%2210.1074/jbc.M116.746131%22
  locator: 'Exact DOI query result: title/authors/year/PMID27502278/PMC5025702 and
    complete abstract'
  summary: Kojima/Muramoto/Kusano2016 bibliography and primary abstract verified.
    CppS/F localization and channel assays are described in the genuine primary body
    separately; outer target does not assert a full molecular inventory or measured
    in-vivo transport rate.
  accessed_at: '2026-11-03T11:52:14.169276Z'
  support: supports
  snapshot_sha256: b835645082c5bb585962834b3e53b0e285fecd37ac866ca00e807e49145881b7
- evidence_id: plaque-kojima2016-canonical
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC5025702/
  locator: Genuine primary HTML Abstract/Introduction, complete Results subsections
    Isolation and Sequence Analysis(sec5/6), channel subsection8, complete Discussion9;
    Methods13–21 and32; included captions as text
  summary: C.paradoxa NIES547 cultures at24C supplied isolated cyanelle membranes.
    Co-fractionation, detergent-resistant PG/protein preparations, microscopy, pigments
    and independent outer-membrane isolation support the narrow exterior localization
    context. Channel measurements use reconstituted proteoliposomes; they do not prove
    membrane formation necessity or in-vivo rates. No complete-paper, Table1 audit,
    figure-pixel, supplementary or raw-data reanalysis claim; current target withholds
    named molecular assignments.
  accessed_at: '2026-11-03T11:52:36.877791Z'
  support: supports
  snapshot_sha256: c5018e5b2381b92e94633472e8fd89ceb39747432bd0908051b13b829e7c0739
- evidence_id: plaque-kojima2016-body
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/5025702/
  locator: Actual HTTP response inspected solely for source-access tier
  summary: HTTP200. Numeric PMC returned a challenge, S3 guessed version404, EuropePMC
    XML500. None supplies inspected full text; canonical PMC route separately succeeds.
  accessed_at: '2026-11-03T11:52:14.170882Z'
  support: context_only
  snapshot_sha256: 9097f5c811375ab2c8179e9b9b2a07735376e47fd8341ba151410c5ce7ec6fac
- evidence_id: plaque-kojima2016-s3
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5025702.1/PMC5025702.1.xml
  locator: Actual HTTP response inspected solely for source-access tier
  summary: HTTP404. Numeric PMC returned a challenge, S3 guessed version404, EuropePMC
    XML500. None supplies inspected full text; canonical PMC route separately succeeds.
  accessed_at: '2026-11-03T11:52:36.877494Z'
  support: context_only
  snapshot_sha256: 64e3884ee36142d6b322ca9bd8a9c7adacbab3dafa49f15e4645b62051ccd86c
- evidence_id: plaque-kojima2016-epmcxml
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5025702/fullTextXML
  locator: Actual HTTP response inspected solely for source-access tier
  summary: HTTP500. Numeric PMC returned a challenge, S3 guessed version404, EuropePMC
    XML500. None supplies inspected full text; canonical PMC route separately succeeds.
  accessed_at: '2026-11-03T11:52:36.877707Z'
  support: context_only
  snapshot_sha256: d0e290dfbc01318f9d5c191ea72e4df2d8e22802efd32577dfa62f739f95e158
- evidence_id: plaque-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete fresh /api/datasets response; all20 organism rows and their dataset
    entries inspected, no pagination
  summary: No current organism row covers Cyanophora or another glaucophyte. No downstream
    matched gene/module query applies, and no bacterial/cyanobacterial analogue is
    substituted. Catalogue noncoverage is not evidence of biological absence.
  accessed_at: '2026-11-03T11:52:14.354050Z'
  support: supports
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: plaque-historical-runner
  kind: validation
  reference: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  locator: Original historical00:49Z receipt and exact stdout/stderr independently
    reread/hash-verified
  summary: Historical runner exited1 before datasets due OS PermissionError on pyvenv.cfg;
    not a new invocation or successful execution. Official current catalogue is the
    permitted source fallback.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: plaque-original-checks
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/adversary-plaque/original-checks.json
  locator: Four read-only native original validate/render executions; every frozen
    input at its historical source commit
  summary: All four originals validate/render exactly.19/19/12/12 historical source
    hashes match; all four current target hashes unchanged. Original findings/actions
    empty.
  accessed_at: '2026-11-03T11:53:14.105351Z'
  support: supports
  snapshot_sha256: 6dd7616a88d9960459e30c923336afb312f8281a082fc5664e08f2a694abb553
- evidence_id: plaque-native-cyanelle_inner_membrane-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_inner_membrane.yaml
    --verify
  locator: Actual root-owned native command receipt and exact stdout independently
    read/hash-verified
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  accessed_at: '2026-11-03T11:51:42.893275Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-cyanelle_inner_membrane-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_inner_membrane.yaml
    --causal-graphs
  locator: Actual root-owned native command receipt and exact stdout independently
    read/hash-verified
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
    \  total GENE_OR_PROTEIN causal nodes"
  accessed_at: '2026-11-03T11:51:43.301255Z'
  support: supports
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: plaque-native-cyanelle_intermembrane_space-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_intermembrane_space.yaml
    --verify
  locator: Actual root-owned native command receipt and exact stdout independently
    read/hash-verified
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  accessed_at: '2026-11-03T11:51:43.724880Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-cyanelle_intermembrane_space-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_intermembrane_space.yaml
    --causal-graphs
  locator: Actual root-owned native command receipt and exact stdout independently
    read/hash-verified
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
    \  total GENE_OR_PROTEIN causal nodes"
  accessed_at: '2026-11-03T11:51:44.142157Z'
  support: supports
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: plaque-native-cyanelle_membrane-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_membrane.yaml
    --verify
  locator: Actual root-owned native command receipt and exact stdout independently
    read/hash-verified
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  accessed_at: '2026-11-03T11:51:44.560629Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-cyanelle_membrane-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_membrane.yaml
    --causal-graphs
  locator: Actual root-owned native command receipt and exact stdout independently
    read/hash-verified
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
    \  total GENE_OR_PROTEIN causal nodes"
  accessed_at: '2026-11-03T11:51:44.975412Z'
  support: supports
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: plaque-native-cyanelle_outer_membrane-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_outer_membrane.yaml
    --verify
  locator: Actual root-owned native command receipt and exact stdout independently
    read/hash-verified
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  accessed_at: '2026-11-03T11:51:45.394700Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-cyanelle_outer_membrane-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_outer_membrane.yaml
    --causal-graphs
  locator: Actual root-owned native command receipt and exact stdout independently
    read/hash-verified
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
    \  total GENE_OR_PROTEIN causal nodes"
  accessed_at: '2026-11-03T11:51:45.812995Z'
  support: supports
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: micro-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Evidence Rules; Structured Source Cross-Checks; native checklist; profile
    and shared lineage contract; applicable common inputs frozen by native inspect
    before assessment
  accessed_at: '2026-11-03T11:57:58.866777Z'
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
  summary: Native review requires narrow source scope, actual input hashes and command
    results, bounded searches, explicit applicability for named pathways, and separate
    record curation. All 17 retained common policy/schema/verifier inputs remain byte-identical
    to the previous reviewed common set; route/profile/config/checklist/shared contract
    reread in this audit.
  support: context_only
- evidence_id: micro-record-cyanelle
  kind: record_content
  reference: data/structures/membrane_organelle/cyanelle.yaml
  locator: 'Entire maintained YAML: definition, history, hierarchy, components, distribution/examples,
    functions, evidence, graph and discussions'
  accessed_at: '2026-11-03T11:57:58.866777Z'
  snapshot_sha256: 5ebb2c3b4cc2d9364dc08ac335c793409014f30f0ca009ee3b4aeafb860371b6
  summary: Entire current record independently read at ed8281f2fc915349c8ce429e7103e42b256c0533;
    PROPOSED status retained; current SHA matches native inspect and current main.
    Changed record reassessed substantively; original frozen version retained.
  support: supports
- evidence_id: micro-prior-cyanelle
  kind: prior_review
  reference: reviews/structured/20261022T010406Z-cyanelle-audit/review.yaml
  locator: Entire authoritative original YAML and paired Markdown, especially source.inputs,
    scientific assessments, verdict, checks[id=imodulondb], limitations and empty
    findings/actions
  accessed_at: '2026-11-03T11:57:58.866777Z'
  snapshot_sha256: 2902d5c0cf0ba994861d191c9cb500d54d58a080e2f8bcdfc778aec66e077d4c
  summary: Original qualified pass had no scientific finding or request-curation action.
    Original validation/render and historical input hash independently checked; original
    observation is retained, not rewritten or recertified as current.
  support: context_only
- evidence_id: micro-native-cyanelle-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cyanelle-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle.yaml
    --verify; adjacent stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cyanelle-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T11:51:41.215948Z'
  snapshot_sha256: 9149252b2bb7f7e07a936ec2fd47470989be09fef52cfd2cc05c94c6bae2a2e2
  summary: Root executed at exact reviewed source; exit 0. The declared UniProt protein-example/xref
    inventory is empty, so this is not independent proof of protein identity, membership
    or necessity.
  support: supports
- evidence_id: micro-native-cyanelle-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cyanelle-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle.yaml
    --causal-graphs; adjacent stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cyanelle-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T11:51:41.639120Z'
  snapshot_sha256: 9272acc2878dafbef1073f7d4849c54b7e3e3c1f2f69f640cc350865b8ffa521
  summary: Root executed at exact reviewed source; exit 0. All GENE_OR_PROTEIN categories
    and total are zero; this checks no biochemical gene/protein node and does not
    validate topology or biology.
  support: supports
- evidence_id: micro-record-cyanelle_envelope
  kind: record_content
  reference: data/structures/membrane_organelle/cyanelle_envelope.yaml
  locator: 'Entire maintained YAML: definition, history, hierarchy, components, distribution/examples,
    functions, evidence, graph and discussions'
  accessed_at: '2026-11-03T11:57:58.866777Z'
  snapshot_sha256: 4a25594b3a26541401976d3ab78f271bc8726951462af9073fafc0eff2389a67
  summary: Entire current record independently read at ed8281f2fc915349c8ce429e7103e42b256c0533;
    PROPOSED status retained; current SHA matches native inspect and current main.
    Current bytes match original frozen scientific input.
  support: supports
- evidence_id: micro-prior-cyanelle_envelope
  kind: prior_review
  reference: reviews/structured/20261022T010409Z-cyanelle-envelope-audit/review.yaml
  locator: Entire authoritative original YAML and paired Markdown, especially source.inputs,
    scientific assessments, verdict, checks[id=imodulondb], limitations and empty
    findings/actions
  accessed_at: '2026-11-03T11:57:58.866777Z'
  snapshot_sha256: b57e357b1140a5b5314c9d64838f9bcc466fc053b94ef9c218bbd72d1446b62b
  summary: Original qualified pass had no scientific finding or request-curation action.
    Original validation/render and historical input hash independently checked; original
    observation is retained, not rewritten or recertified as current.
  support: context_only
- evidence_id: micro-native-cyanelle_envelope-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cyanelle_envelope-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_envelope.yaml
    --verify; adjacent stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cyanelle_envelope-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T11:51:42.050736Z'
  snapshot_sha256: 6c1c5b9b64b3187ab559d3ce11b6cfa39f7bfb8ccd0e8d7adb82e2dc627501a1
  summary: Root executed at exact reviewed source; exit 0. The declared UniProt protein-example/xref
    inventory is empty, so this is not independent proof of protein identity, membership
    or necessity.
  support: supports
- evidence_id: micro-native-cyanelle_envelope-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cyanelle_envelope-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_envelope.yaml
    --causal-graphs; adjacent stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cyanelle_envelope-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T11:51:42.473671Z'
  snapshot_sha256: 64f1d2c993bd75984ed1d027b85b94a5ad082bc4c68503e30002b526acb1dd7c
  summary: Root executed at exact reviewed source; exit 0. All GENE_OR_PROTEIN categories
    and total are zero; this checks no biochemical gene/protein node and does not
    validate topology or biology.
  support: supports
- evidence_id: micro-record-cyanelle_stroma
  kind: record_content
  reference: data/structures/membrane_organelle/cyanelle_stroma.yaml
  locator: 'Entire maintained YAML: definition, history, hierarchy, components, distribution/examples,
    functions, evidence, graph and discussions'
  accessed_at: '2026-11-03T11:57:58.866777Z'
  snapshot_sha256: 13d83e3dadca9cafaa6550a7bf84cd8066bf1539ccaacd3627ec23aa5b08e118
  summary: Entire current record independently read at ed8281f2fc915349c8ce429e7103e42b256c0533;
    PROPOSED status retained; current SHA matches native inspect and current main.
    Current bytes match original frozen scientific input.
  support: supports
- evidence_id: micro-prior-cyanelle_stroma
  kind: prior_review
  reference: reviews/structured/20261022T010425Z-cyanelle-stroma-audit/review.yaml
  locator: Entire authoritative original YAML and paired Markdown, especially source.inputs,
    scientific assessments, verdict, checks[id=imodulondb], limitations and empty
    findings/actions
  accessed_at: '2026-11-03T11:57:58.866777Z'
  snapshot_sha256: 66e2866e2593f996c1833f20e12642f5e7f44aa4d011ab48ba762da47207f133
  summary: Original qualified pass had no scientific finding or request-curation action.
    Original validation/render and historical input hash independently checked; original
    observation is retained, not rewritten or recertified as current.
  support: context_only
- evidence_id: micro-native-cyanelle_stroma-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cyanelle_stroma-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_stroma.yaml
    --verify; adjacent stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cyanelle_stroma-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T11:51:46.224159Z'
  snapshot_sha256: 369100b66e4fe001bf3f29ff3104348274e82ac37656fbb97e4e5678e8aa9261
  summary: Root executed at exact reviewed source; exit 0. The declared UniProt protein-example/xref
    inventory is empty, so this is not independent proof of protein identity, membership
    or necessity.
  support: supports
- evidence_id: micro-native-cyanelle_stroma-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cyanelle_stroma-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_stroma.yaml
    --causal-graphs; adjacent stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cyanelle_stroma-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T11:51:46.636178Z'
  snapshot_sha256: d78420d43e1a0e8a1b69bfaf2c92ee09a4d034da458c49a30968cec3de55841b
  summary: Root executed at exact reviewed source; exit 0. All GENE_OR_PROTEIN categories
    and total are zero; this checks no biochemical gene/protein node and does not
    validate topology or biology.
  support: supports
- evidence_id: micro-original-validation-inputs
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/adversary-microtubule/original-validation-inputs.json
  locator: All three original validate + render --content executions and original-source
    versus current-target SHA256 comparisons
  accessed_at: '2026-11-03T11:52:55.330006Z'
  snapshot_sha256: 613a1e74eb08862d116e6deb538d7dca5d9c3d3a8e2a2bcfbcde78de458113bb
  summary: 'Three native original validations exit 0, three deterministic Markdown
    comparisons match. Frozen source revision 9c0446c4c0dd4b458787c43a499e4ceab5e179a6
    verified. Only whole cyanelle changed: old24275c8050ca5d13c66d563c7aa697a4de65766f87499f876fc94c41cd2f0db7
    versus current5ebb2c3b4cc2d9364dc08ac335c793409014f30f0ca009ee3b4aeafb860371b6.'
  support: supports
- evidence_id: micro-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009842,GO:0009536,GO:0033112,GO:0036012,GO:0036013,GO:0036014,GO:0034060,GO:0009843,GO:0033114,GO:0033115,GO:0033113,GO:0042170,GO:0009527,GO:0009532,GO:0005737,GO:0015979,GO:0009526
  locator: 'Exact 17-ID QuickGO term response: definitions, synonyms, native child
    relations for whole cyanelle, envelope, inner/outer membranes, IMS, stroma, thylakoid/lumen/membrane,
    plastid parents and photosynthesis'
  accessed_at: '2026-11-03T11:52:36.404418Z'
  snapshot_sha256: b294054ca58e46634347a17541b9c003d339a6230c57b18920cad889fab06532
  summary: Exact identities and typed parthood/is-a relationships support the retained
    anatomy. Whole cyanelle explicitly has stroma as a part; IMS is a child of envelope,
    itself a part of cyanelle. Definition and synonyms remain compatible with current
    taxonomic terminology.
  support: supports
- evidence_id: micro-ims-go-path
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0036014/paths/GO:0009842
  locator: Complete QuickGO paths response from GO:0036014 to GO:0009842; one returned
    path of two part_of edges
  accessed_at: '2026-11-03T11:55:10.662657Z'
  snapshot_sha256: c38e07d8759bd3a9867a937b7079043709363b09e150db7f5a9cb081b34e55a7
  summary: The only returned path is GO:0036014 → GO:0033112 → GO:0009842. Supports
    transitive IMS parthood in cyanelle while refuting the record note that GO asserts
    this as a direct relationship.
  support: refutes
- evidence_id: micro-SL-0082
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0082.json
  locator: 'Native UniProt Subcellular Location JSON: definition, GO mapping and hierarchy;
    protein-count metadata not treated as inventory'
  accessed_at: '2026-11-03T11:52:36.404680Z'
  snapshot_sha256: ae0660e1e761b28504bbca0b97ea8b0cd6260df50fc514d37e4bcdb4afb2a3de
  summary: Exact Cyanelle entry maps GO0009842, gives cyanoplast/muroplast synonyms
    and describes photosynthetic glaucophyte organelle with double membrane and PG.
  support: supports
- evidence_id: micro-SL-0479
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0479.json
  locator: 'Native UniProt Subcellular Location JSON: definition, GO mapping and hierarchy;
    protein-count metadata not treated as inventory'
  accessed_at: '2026-11-03T11:52:36.404831Z'
  snapshot_sha256: f926a2da38e46b3f002892ab0db2dab5d69d1cbc5d703d2cf0fe3f9d1f3312b6
  summary: Exact envelope entry maps GO0033112 and explicitly includes both membranes,
    IMS and PG; it is not a single bilayer.
  support: supports
- evidence_id: micro-SL-0350
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0350.json
  locator: 'Native UniProt Subcellular Location JSON: definition, GO mapping and hierarchy;
    protein-count metadata not treated as inventory'
  accessed_at: '2026-11-03T11:52:36.404770Z'
  snapshot_sha256: 41732e97d7212549f0c1326e8ed3c0f9038b0d41d28e6b8aa8436206e92032b4
  summary: Exact stroma entry maps GO0034060, excludes thylakoid space, and lists
    DNA/ribosomes/photosynthetic products as contents, not mandatory identities of
    the compartment.
  support: supports
- evidence_id: micro-cyanelle-SL-0480
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0480.json
  locator: Native UniProt definition and hierarchy; independently read supplied response,
    preserving plaque fetch timestamp
  accessed_at: '2026-11-03T11:52:14.167349Z'
  snapshot_sha256: b91c540680ba95ebee76012cbfcb23234f3ef6df3427a70bb85fcadd801933e9
  summary: The inner membrane separates stroma from IMS; this supports the graph boundary
    without treating either compartment as a membrane or protein.
  support: supports
- evidence_id: micro-tax2762
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2762
  locator: 'Exact ENA taxonomy tax-id response: scientific name, rank, lineage and
    other names'
  accessed_at: '2026-11-03T11:52:36.404873Z'
  snapshot_sha256: 8384800c0c30321c096fb48117051165d50982c461255fe65d738d523d60ed7a
  summary: ENA taxon2762 is species Cyanophora paradoxa.
  support: supports
- evidence_id: micro-tax38254
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/38254
  locator: 'Exact ENA taxonomy tax-id response: scientific name, rank, lineage and
    other names'
  accessed_at: '2026-11-03T11:52:36.404908Z'
  snapshot_sha256: 4b487eb0e34bcb4941fbb315aae5214c96ea6f60255d71a2aca172cd35844009
  summary: ENA taxon38254 is class Glaucocystophyceae, with Glaucophyta and Glaucophyceae
    listed as alternative names.
  support: supports
- evidence_id: micro-giddings1983-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1104%2Fpp.71.2.409
  locator: 'Europe PMC exact DOI core result PMID16662839: bibliographic identity
    and complete primary abstract'
  accessed_at: '2026-11-03T11:52:37.145401Z'
  snapshot_sha256: e9050ae8f4efd4fb2d2362f165fcf9704d181bed10bd5e996a87e7ae85d79c02
  summary: Primary microscopy of Cyanophora paradoxa cyanelles and thylakoids; presumptive
    PSII/contact assignments remain qualified. This is abstract metadata, supplemented
    by the separately viewed scanned pages.
  support: supports
- evidence_id: micro-giddings1983-page409
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/6ed041edd2c7/plntphys00558-0203.png
  locator: Giddings et al.1983 DOI10.1104/pp.71.2.409, printed page409; source scan
    visually viewed as pixels, text and stated figures/captions
  accessed_at: '2026-11-03T11:52:37.773780Z'
  snapshot_sha256: c0184058c66810b2544be1af57fac9acc2bbbfcdf71ee1186aade8232e5c9f61
  summary: 'Title, abstract, Introduction and opening Methods inspected in pixels:
    Cyanophora paradoxa UTEX LB555 culture/isolation; photosynthetically active cyanelles,
    phycobilisomes, and qualified historic envelope/PG interpretation.'
  support: supports
- evidence_id: micro-giddings1983-page410
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/8d99de19802c/plntphys00558-0204.png
  locator: Giddings et al.1983 DOI10.1104/pp.71.2.409, printed page410; source scan
    visually viewed as pixels, text and stated figures/captions
  accessed_at: '2026-11-03T11:52:37.785213Z'
  snapshot_sha256: ba0bd01ef58d44879c8f7b2689f79f5066039cef904b15a32330a611681812c0
  summary: 'Figures1–3 pixels and captions inspected: whole-cell cyanelle, isolated
    cyanelle and thylakoid faces; curved lamellae within the organelle, not a numerical
    or universal concentricity measurement. Isolation continuation and thylakoid preparation
    also read.'
  support: supports
- evidence_id: micro-giddings1983-page412
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/392b5bf89308/plntphys00558-0206.png
  locator: Giddings et al.1983 DOI10.1104/pp.71.2.409, printed page412; source scan
    visually viewed as pixels, text and stated figures/captions
  accessed_at: '2026-11-03T11:52:37.796954Z'
  snapshot_sha256: 9c033e4b190ed1cd62006b88fa8961e80608056e79e1ec0fc45040e3bb19f47f
  summary: Results opening states dense cyanelle stroma; thylakoid/phycobilisome results
    and Methods continuation read, Figure6 pixels/caption inspected. Morphology is
    not a universal assembly-necessity test.
  support: supports
- evidence_id: micro-giddings1983-page414
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/9d4d067999da/plntphys00558-0208.png
  locator: Giddings et al.1983 DOI10.1104/pp.71.2.409, printed page414; source scan
    visually viewed as pixels, text and stated figures/captions
  accessed_at: '2026-11-03T11:52:38.060694Z'
  snapshot_sha256: 331f5f9fdd4e16e2a8cb67d9b5d45cca5467dc6554051cfa6696e34471e7bb82
  summary: 'Envelope Membranes Results opening and Figures11–12 pixels/captions read:
    inner membrane, wall layer and isolated cyanelle organization distinguish envelope
    from internal thylakoids.'
  support: supports
- evidence_id: micro-giddings1983-page416
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/c329334d81e0/plntphys00558-0210.png
  locator: Giddings et al.1983 DOI10.1104/pp.71.2.409, printed page416; source scan
    visually viewed as pixels, text and stated figures/captions
  accessed_at: '2026-11-03T11:52:38.068083Z'
  snapshot_sha256: 41f820c6bde6abc4318ac32baa45293634543bb4aceb0dc5129c3d25414e91ef
  summary: 'Envelope Results continuation and Discussion opening read with Figure15
    histogram pixels/caption: outer layer exterior to PG and preparation-associated
    blistering/peeling are explicitly distinguished.'
  support: supports
- evidence_id: micro-giddings1983-page417
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/7694ed6a7a74/plntphys00558-0211.png
  locator: Giddings et al.1983 DOI10.1104/pp.71.2.409, printed page417; source scan
    visually viewed as pixels, text and stated figures/captions
  accessed_at: '2026-11-03T11:52:38.074636Z'
  snapshot_sha256: 276c1cb60d1a909200199f8e24495840d2caa5f5131c8a896d3f97d70e5bcf6f
  summary: 'Complete envelope Discussion and Figures16–18 pixels/captions read: distinct
    inner and outer envelope structure, PG layer and no observed continuity between
    inner envelope and thylakoids; historical endosymbiont terminology is not current
    taxonomy.'
  support: supports
- evidence_id: micro-pfanzagl1996-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1128%2Fjb.178.2.332-339.1996
  locator: 'Europe PMC exact DOI core result PMID8550450: complete primary abstract
    and bibliographic identity; no full-body Methods/Results inspection claimed'
  accessed_at: '2026-11-03T11:52:37.151802Z'
  snapshot_sha256: 83885c5efad4f11a564a920fd758d6d4c3d0f303810b056da883f23b995e92b8
  summary: Primary biochemical characterization of Cyanophora paradoxa cyanelle PG
    by separation and mass spectrometry supports the material claim. Abstract-only
    scope is adequate for the record broad biochemical attribution, not a new claim
    about detailed experimental conditions or necessity.
  support: supports
- evidence_id: micro-pfanzagl-comparative-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:8955325%20AND%20SRC:MED
  locator: Complete Europe PMC primary abstract for PMID8955325 plus metadata; independently
    read supplied response, original fetch time retained
  accessed_at: '2026-11-03T11:52:14.174981Z'
  snapshot_sha256: 703ee4ecc41c108b84a9333646b4cb2357a8fbdb9a0ed2dabed6392f8f2b63a1
  summary: HPLC/mass-spectrometric study identifies cyanelle PG in Glaucocystis nostochinearum
    and Cyanoptyche gloeocystis and compares earlier Cyanophora paradoxa chemistry.
    Supports the envelope note about those three named genera without universal species
    prevalence or full-body inspection.
  support: supports
- evidence_id: micro-kojima2016-canonical
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC5025702/
  locator: 'Genuine PMC5025702 canonical HTML: Abstract, Introduction, Results first
    subsection Isolation of CppS/F (sec5), Experimental Procedures Strains/Culture,
    Cyanelle Isolation, CppS/F Isolation, PG detection/binding, EM and PG preparation
    (sec13–19); text/captions only, not figure-pixel inspection'
  accessed_at: '2026-11-03T11:52:36.877791Z'
  snapshot_sha256: c5018e5b2381b92e94633472e8fd89ceb39747432bd0908051b13b829e7c0739
  summary: Independent bounded body read confirms C.paradoxa NIES547 biochemical fractionation
    and PG-associated proteins/outer membrane preparation; direct localization support
    has appropriate experimental scope. No claim of reading all Results, all Methods,
    sequence analyses or supplementary data; article is not a universal necessity
    experiment.
  support: supports
- evidence_id: micro-price2019-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A31098614%20AND%20SRC%3AMED
  locator: Europe PMC exact PMID31098614 core metadata and complete primary abstract
  accessed_at: '2026-11-03T11:52:37.155148Z'
  snapshot_sha256: eeda9dcb7aa664f416cd916e182898985216663258d085a011da07a19152d528
  summary: Price et al.2019 DOI10.1093/dnares/dsz009 is a Cyanophora genome/ultrastructure
    study, supporting the reference identity and scoped glaucophyte context.
  support: supports
- evidence_id: micro-price2019-s3
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6704402.1/PMC6704402.1.xml
  locator: 'Genuine PMC6704402.1 JATS: Introduction, Methods2.1, Results3.4 including3.4.1–5
    and3.5; Figure2 and referenced supplement captions/prose only, no pixel inspection'
  accessed_at: '2026-11-03T11:52:37.628767Z'
  snapshot_sha256: c471e02995f4d10cb086115d79c6f850c60c822b846551023eabf95d5badb3ac
  summary: Primary QFDE microscopy and C.paradoxa CCMP329 genome context support plastid/thylakoid/PG
    anatomy. Results3.4.3 describes apparent concentric/spiral architecture with occasional
    termini/bifurcations, so the stale thylakoid-in-stroma edge is supported as bounded
    morphology, not a universal closed-onion claim. Introduction and cited historical
    conclusions are secondary context; no reanalysis or exhaustive genome audit claimed.
  support: supports
- evidence_id: micro-pg-search
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=cyanelle%20peptidoglycan&limit=100&page=1
  locator: Complete QuickGO query response with literal query cyanelle peptidoglycan,
    page1, limit100
  accessed_at: '2026-11-03T11:52:37.756203Z'
  snapshot_sha256: 3d8aae3b2ec8cd6a34b229f338851ac92353011aee8804df8e0a35b1cdce8358
  summary: Returned64 results, including broader PG-wall and cyanelle anatomical terms,
    do not establish a unique cyanelle PG-sheet identity. The existing reviewed-label-only
    component and explicit open grounding discussion remain appropriate; no universal
    absence conclusion.
  search_scope: QuickGO GO text search on 2026-11-03, literal query=cyanelle peptidoglycan,
    page=1, limit=100; response reports64 total results and one page. All returned
    IDs/names inspected; only the exact cyanelle anatomy terms separately retrieved
    at authority level. This is not a search of all ontologies or an assertion no
    exact term exists.
  support: supports
- evidence_id: micro-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Complete public iModulonDB /api/datasets response; organism IDs/names and
    dataset arrays inspected
  accessed_at: '2026-11-03T11:52:37.723725Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  summary: No organism/dataset entry matches Cyanophora paradoxa, Glaucocystophyceae/Glaucophyta,
    Cyanoptyche or Glaucocystis. Synechococcus elongatus is a different bacterial
    organism and is not substituted for a glaucophyte plastid. No matched dataset
    means downstream gene/module queries cannot inform this record; absence is not
    biological negative evidence.
  search_scope: iModulonDB public /api/datasets GET on 2026-11-03; unfiltered returned20
    organism rows/28 organism-dataset pairs, no pagination or client result truncation.
    Inspected all names/IDs/dataset arrays for Cyanophora/paradoxa/Glaucocystophyceae/Glaucophyta/Glaucocystis/Cyanoptyche;
    no organism match. Scope is this returned catalogue, not all expression resources.
  support: supports
- evidence_id: micro-historical-adapter-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Retained actual native imodulondb datasets attempt, exit1 / operating-system
    PermissionError reading runner pyvenv.cfg; receipt reviewed as historical evidence
  accessed_at: '2026-11-03T00:49:00.848907Z'
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: This runner failure occurred at00:49:00Z in the earlier canary session,
    not a fresh invocation for PR2362. Current applicability uses the independently
    fetched catalogue fallback. Unavailability does not imply absent biology.
  support: context_only
- evidence_id: septin-review-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Structured Source Cross-Checks and immutable review contract
  summary: Named molecular and pathway assertions trigger applicability assessment,
    including affirmative canonical-example pathway claims. Expression-only non-inference
    is not an exemption. No covered organism is a resource limit, not negative biology.
  accessed_at: '2026-11-03T11:55:50.493869Z'
  support: supports
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: septin-curation-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Identity, components, material constitution, source scope and evidence
  summary: A structure, its constituent bilayer, cargo complex and associated transient
    assembly machinery remain distinct. Molecular identity does not establish localization
    or formation necessity.
  accessed_at: '2026-11-03T11:55:50.493869Z'
  support: supports
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: septin-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: NONMECHANISTIC graphs and scoped molecular evidence
  summary: Descriptive topology and supported delivery endpoints may be nonmechanistic.
    Empty protein-node inventories do not prove narrative molecular assertions.
  accessed_at: '2026-11-03T11:55:50.493869Z'
  support: supports
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: septin-record-cvt_vesicle
  kind: record_content
  reference: data/structures/membrane_organelle/cvt_vesicle.yaml
  locator: Entire current maintained YAML at ed8281f2fc915349c8ce429e7103e42b256c0533
  summary: Read identity/definition, history, hierarchy, components, taxon and canonical
    context, function, every graph edge, evidence and discussion. No target image,
    quantitative property, trait link, verbatim snippet or individual protein accession
    is declared.
  accessed_at: '2026-11-03T11:55:50.493869Z'
  support: supports
  snapshot_sha256: cf6eb5075a057a0b8b104cbacb61cdf895298eb4b018945a08b46bcb939c8b0c
- evidence_id: septin-original-cvt_vesicle
  kind: prior_review
  reference: reviews/structured/20261022T010353Z-cvt-vesicle-audit/review.yaml
  locator: Original YAML plus deterministic Markdown; frozen inputs, checks, source
    tiers, assessments and limitations
  summary: Original qualified pass has no scientific findings or request-curation
    actions. Its target bytes remain current. Its expression-only iModulonDB rationale
    is insufficient; historical source times and global checks remain historical.
  accessed_at: '2026-11-03T11:55:50.493869Z'
  support: supports
  snapshot_sha256: d59b0197adec346d7446a07ca5bd3d79a8bddfa40046e110081eff58c4b2e8cc
- evidence_id: septin-original-validation-cvt_vesicle
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/adversary-septin/original-checks.json
  locator: 20261022T010353Z-cvt-vesicle-audit actual validate/render plus original-source/current
    hash comparison
  summary: Both native commands exited zero; Markdown matches byte-for-byte and target
    hashes match original historical source, original frozen input and current record.
  accessed_at: '2026-11-03T11:52:04.441308Z'
  support: supports
  snapshot_sha256: 6940be2374b1528d7945067617cacdf192064b33f253b7ae046def9f3172f242
- evidence_id: septin-native-cvt_vesicle-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cvt_vesicle-uniprot-verify-receipt.json
  locator: Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cvt_vesicle-uniprot-verify.log
  summary: Exit zero. No protein examples or UniProtKB graph xrefs and zero GENE_OR_PROTEIN
    graph nodes. Execution success verifies only this empty represented inventory;
    it does not establish narrative Ape1/Ams1/Atg identity, localization, mechanism,
    complete composition or formation necessity.
  accessed_at: '2026-11-03T11:51:38.722064Z'
  support: supports
  snapshot_sha256: f527164e64f88e40a3ca9dffc3cf784c15753b0e44ca891cdd74641899ef1953
- evidence_id: septin-native-cvt_vesicle-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cvt_vesicle-uniprot-causal-receipt.json
  locator: Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cvt_vesicle-uniprot-causal.log
  summary: Exit zero. No protein examples or UniProtKB graph xrefs and zero GENE_OR_PROTEIN
    graph nodes. Execution success verifies only this empty represented inventory;
    it does not establish narrative Ape1/Ams1/Atg identity, localization, mechanism,
    complete composition or formation necessity.
  accessed_at: '2026-11-03T11:51:39.133152Z'
  support: supports
  snapshot_sha256: cac0f4c45b3812ae40119882f8a637bd96f8074a3b7b08fe71fc791f76670853
- evidence_id: septin-record-cvt_vesicle_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/cvt_vesicle_lumen.yaml
  locator: Entire current maintained YAML at ed8281f2fc915349c8ce429e7103e42b256c0533
  summary: Read identity/definition, history, hierarchy, components, taxon and canonical
    context, function, every graph edge, evidence and discussion. No target image,
    quantitative property, trait link, verbatim snippet or individual protein accession
    is declared.
  accessed_at: '2026-11-03T11:55:50.493869Z'
  support: supports
  snapshot_sha256: 3bb8cb5c3f751ec93619bb4658fb51a2c6e6a94e4e0b16aa0ea8a0833a28c243
- evidence_id: septin-original-cvt_vesicle_lumen
  kind: prior_review
  reference: reviews/structured/20261022T010357Z-cvt-vesicle-lumen-audit/review.yaml
  locator: Original YAML plus deterministic Markdown; frozen inputs, checks, source
    tiers, assessments and limitations
  summary: Original qualified pass has no scientific findings or request-curation
    actions. Its target bytes remain current. Its expression-only iModulonDB rationale
    is insufficient; historical source times and global checks remain historical.
  accessed_at: '2026-11-03T11:55:50.493869Z'
  support: supports
  snapshot_sha256: c15022bb93f16bda92f89bc7c8124c8014776de3e493c3783bb7b53f25d8caa4
- evidence_id: septin-original-validation-cvt_vesicle_lumen
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/adversary-septin/original-checks.json
  locator: 20261022T010357Z-cvt-vesicle-lumen-audit actual validate/render plus original-source/current
    hash comparison
  summary: Both native commands exited zero; Markdown matches byte-for-byte and target
    hashes match original historical source, original frozen input and current record.
  accessed_at: '2026-11-03T11:52:05.584185Z'
  support: supports
  snapshot_sha256: 6940be2374b1528d7945067617cacdf192064b33f253b7ae046def9f3172f242
- evidence_id: septin-native-cvt_vesicle_lumen-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cvt_vesicle_lumen-uniprot-verify-receipt.json
  locator: Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cvt_vesicle_lumen-uniprot-verify.log
  summary: Exit zero. No protein examples or UniProtKB graph xrefs and zero GENE_OR_PROTEIN
    graph nodes. Execution success verifies only this empty represented inventory;
    it does not establish narrative Ape1/Ams1/Atg identity, localization, mechanism,
    complete composition or formation necessity.
  accessed_at: '2026-11-03T11:51:39.553933Z'
  support: supports
  snapshot_sha256: fccb5a7a1358922a79d2d64695565836ddecfd2fbbab552bd256a52cdc809d61
- evidence_id: septin-native-cvt_vesicle_lumen-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cvt_vesicle_lumen-uniprot-causal-receipt.json
  locator: Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cvt_vesicle_lumen-uniprot-causal.log
  summary: Exit zero. No protein examples or UniProtKB graph xrefs and zero GENE_OR_PROTEIN
    graph nodes. Execution success verifies only this empty represented inventory;
    it does not establish narrative Ape1/Ams1/Atg identity, localization, mechanism,
    complete composition or formation necessity.
  accessed_at: '2026-11-03T11:51:39.966186Z'
  support: supports
  snapshot_sha256: c12ea164a3c97e9cd4204b1d0e351dd81852b45b0bc465ee900f493e9e309be0
- evidence_id: septin-record-cvt_vesicle_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/cvt_vesicle_membrane.yaml
  locator: Entire current maintained YAML at ed8281f2fc915349c8ce429e7103e42b256c0533
  summary: Read identity/definition, history, hierarchy, components, taxon and canonical
    context, function, every graph edge, evidence and discussion. No target image,
    quantitative property, trait link, verbatim snippet or individual protein accession
    is declared.
  accessed_at: '2026-11-03T11:55:50.493869Z'
  support: supports
  snapshot_sha256: 679cdeb18f93b2ecf38916c132f8461121e7067f0db52e4b24842559b39dbb67
- evidence_id: septin-original-cvt_vesicle_membrane
  kind: prior_review
  reference: reviews/structured/20261022T010402Z-cvt-vesicle-membrane-audit/review.yaml
  locator: Original YAML plus deterministic Markdown; frozen inputs, checks, source
    tiers, assessments and limitations
  summary: Original qualified pass has no scientific findings or request-curation
    actions. Its target bytes remain current. Its expression-only iModulonDB rationale
    is insufficient; historical source times and global checks remain historical.
  accessed_at: '2026-11-03T11:55:50.493869Z'
  support: supports
  snapshot_sha256: 4d33933a47cdf13e03b6c884954f32b566df400f8667e0bdd4064b87c30aeaf3
- evidence_id: septin-original-validation-cvt_vesicle_membrane
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/adversary-septin/original-checks.json
  locator: 20261022T010402Z-cvt-vesicle-membrane-audit actual validate/render plus
    original-source/current hash comparison
  summary: Both native commands exited zero; Markdown matches byte-for-byte and target
    hashes match original historical source, original frozen input and current record.
  accessed_at: '2026-11-03T11:52:06.730208Z'
  support: supports
  snapshot_sha256: 6940be2374b1528d7945067617cacdf192064b33f253b7ae046def9f3172f242
- evidence_id: septin-native-cvt_vesicle_membrane-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cvt_vesicle_membrane-uniprot-verify-receipt.json
  locator: Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cvt_vesicle_membrane-uniprot-verify.log
  summary: Exit zero. No protein examples or UniProtKB graph xrefs and zero GENE_OR_PROTEIN
    graph nodes. Execution success verifies only this empty represented inventory;
    it does not establish narrative Ape1/Ams1/Atg identity, localization, mechanism,
    complete composition or formation necessity.
  accessed_at: '2026-11-03T11:51:40.376556Z'
  support: supports
  snapshot_sha256: 371c11548abe722162b5d5969379e4a51418174842433fffa8856917d1d9c629
- evidence_id: septin-native-cvt_vesicle_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cvt_vesicle_membrane-uniprot-causal-receipt.json
  locator: Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/cvt_vesicle_membrane-uniprot-causal.log
  summary: Exit zero. No protein examples or UniProtKB graph xrefs and zero GENE_OR_PROTEIN
    graph nodes. Execution success verifies only this empty represented inventory;
    it does not establish narrative Ape1/Ams1/Atg identity, localization, mechanism,
    complete composition or formation necessity.
  accessed_at: '2026-11-03T11:51:40.796003Z'
  support: supports
  snapshot_sha256: a9579dfaaf5b49ee7f22cf7eef6541637b522301cf31d5abdfbdd8a091f5014d
- evidence_id: septin-context-cvt_complex
  kind: record_content
  reference: data/structures/other/cvt_complex.yaml
  locator: 'Boundary fields only: identifier, label, definition, structure_kind, parents,
    part_of and has_part'
  summary: Frozen before inspection. Exact GO0034270 denotes a multiprotein cargo
    complex, distinct from the GO0033107 double-membrane carrier, the surrounding
    bilayer and the enclosed region. No whole-neighbor scientific review, protein
    example verification or historical finding disposition is asserted.
  accessed_at: '2026-11-03T11:55:50.493869Z'
  support: supports
  snapshot_sha256: 29ffd90803735e2db2a3869531eae7e439bac79b868049f6d7766c6c9a694902
- evidence_id: septin-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0033107,GO:0033110,GO:0034270,GO:0032258,GO:0031410,GO:0060205,GO:0030659,GO:0000324
  locator: 'All eight exact returned terms: identities, definitions, active status,
    synonyms and relevant direct typed child relations'
  summary: GO0033107 is the double-membrane Cvt carrier and has exact cytoplasm-to-vacuole-targeting
    vesicle synonyms; GO0033110 denotes either one of its two bilayers. GO0034270
    identifies the preApe1 cargo complex. Parent and part relations, fungal vacuole
    endpoint and GO0032258 selective Cvt process are consistent with maintained scope.
    GO0060205 is the broader lumen parent, not an exact Cvt-lumen substitute.
  accessed_at: '2026-11-03T11:51:53.292762Z'
  support: supports
  snapshot_sha256: 996f6e9edc4ec2167e0ee08326490b7e55c8f2c135f0edf88023f2475d5efca1
- evidence_id: septin-tax4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Exact taxId, scientificName, rank and lineage
  summary: Taxon4932 is the species Saccharomyces cerevisiae. Taxon identity is verified
    independently of model strain, experimental condition or quantitative prevalence.
  accessed_at: '2026-11-03T11:51:53.293037Z'
  support: supports
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
- evidence_id: septin-SL0080
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0080.json
  locator: Native entry id/name/definition, immediate isA/partOf and nested GO mappings
  summary: SL0080 maps exactly to GO0033107 and has cytoplasmic vesicle parentage.
  accessed_at: '2026-11-03T11:51:53.293119Z'
  support: supports
  snapshot_sha256: 78f6059d78715afb4efd1a3f54296f0e7d1fb0c915b1a8d1d5a18e9721c43e9f
- evidence_id: septin-SL0081
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0081.json
  locator: Native entry id/name/definition, immediate isA/partOf and nested GO mappings
  summary: SL0081 maps exactly to GO0033110, with cytoplasmic vesicle membrane parentage
    and Cvt vesicle partOf; it does not identify an individual lipid species.
  accessed_at: '2026-11-03T11:51:53.293179Z'
  support: supports
  snapshot_sha256: 022dabf54e0c0c7e152f278f29dc194e6fdb7c859afe2a4cf62a090b77cea140
- evidence_id: septin-SL0323
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0323.json
  locator: Native entry id/name/definition, immediate isA/partOf and nested GO mappings
  summary: SL0323 positively identifies the Cvt vesicle lumen, with cytoplasmic vesicle
    lumen parent and Cvt vesicle partOf. It has no own GO mapping in this returned
    entry; this does not prove global ontology absence.
  accessed_at: '2026-11-03T11:51:53.293229Z'
  support: supports
  snapshot_sha256: f7618f53ff5aed9a3a6b46b3bfe06e236d58ec7397b43999f3b8df448b8e7b4a
- evidence_id: septin-reggiori2004-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A15004240%20AND%20SRC%3AMED
  locator: Complete native primary abstract plus exact title/authors/year/DOI/PMID/PMCID
    and article type
  summary: Reggiori et al.2004 PMID15004240 DOI10.1091/mbc.e03-07-0479 is a primary
    research article. Its abstract supports cytosolic double-membrane Cvt sequestration
    and early-secretory contribution while retaining membrane-origin uncertainty.
  accessed_at: '2026-11-03T11:51:54.023844Z'
  support: supports
  snapshot_sha256: 923b0a91aaa2e0a2ecc4153f810d909c42f0129f6a71ea504c25908ef75af1a8
  search_scope: Europe PMC REST exact PMID AND SRC:MED query encoded in reference,
    resultType=core, format=json; one matched result returned and inspected at 2026-11-03T11:51:54.023844Z.
    No date filter or broad literature-absence claim.
- evidence_id: septin-shintani2004-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A15138258%20AND%20SRC%3AMED
  locator: Complete native primary abstract plus exact title/authors/year/DOI/PMID/PMCID
    and article type
  summary: Shintani and Klionsky2004 PMID15138258 DOI10.1074/jbc.M404399200 is a primary
    experiment, not a secondary review. Ape1/Atg19 complex formation, PAS organization
    and conditional Cvt vesicle formation are distinguished.
  accessed_at: '2026-11-03T11:51:54.028774Z'
  support: supports
  snapshot_sha256: eaa7b0da8ee454d86a5c7a75af92bb0d5475ae3a7ec3b93c6a182057cbfb3277
  search_scope: Europe PMC REST exact PMID AND SRC:MED query encoded in reference,
    resultType=core, format=json; one matched result returned and inspected at 2026-11-03T11:51:54.028774Z.
    No date filter or broad literature-absence claim.
- evidence_id: septin-scott2001-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A11430817%20AND%20SRC%3AMED
  locator: Complete native primary abstract plus exact title/authors/year/DOI/PMID/PMCID
    and article type
  summary: Scott et al.2001 PMID11430817 DOI10.1016/s1097-2765(01)00263-5 identifies
    Cvt19 as a selective hydrolase receptor, with prAPI binding and vacuolar cotransport.
    Cvt19 requirement for specific cargo is distinct from bulk autophagy and pexophagy
    requirements.
  accessed_at: '2026-11-03T11:51:55.104817Z'
  support: supports
  snapshot_sha256: 2b0c902c436c14cb6ad4d2a4efc7761459dc73a9853dc9d219202bd582560995
  search_scope: Europe PMC REST exact PMID AND SRC:MED query encoded in reference,
    resultType=core, format=json; one matched result returned and inspected at 2026-11-03T11:51:55.104817Z.
    No date filter or broad literature-absence claim.
- evidence_id: septin-reggiori2004-pmc-prefixed
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC404015/
  locator: 'Genuine current PMC404015 HTML: complete Introduction sec1; Methods Strains
    and Media sec3/Table1 and pulse-chase sec6; Results sec13 and sec14 with Figures5–8
    text captions; Discussion sec17 only. Other sections and all pixels/raw data not
    audited.'
  summary: Yeast BY4742/SEY6210 and listed sec7/sec12 models support double-membrane
    cargo carriers, outer-membrane fusion and inner-body release. Temperature-shift
    and pulse-chase experiments show early-secretory effects on PAS/cargo transport.
    Effects depend on timing and conditions; the authors explicitly cannot distinguish
    ER from Golgi origin. Broader intro claims are contextual synthesis within a primary
    paper, not newly performed experiments.
  accessed_at: '2026-11-03T11:52:44.039650Z'
  support: supports
  snapshot_sha256: c6e920f0e7dc866b10c1bdc179d4cc63604ffd4b349682f6d4243ba131254553
- evidence_id: septin-shintani2004-pmc-prefixed
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1712665/
  locator: 'Genuine current PMC1712665 HTML: complete scientific main body, Introduction
    S1, Experimental Procedures S2–5/TableI, Results S6–9 and Discussion S10, including
    Figures1–3 captions as text. No pixels/raw data or independently audited cited
    references.'
  summary: The primary study uses SEY6210-derived fluorescent reporters, temperature-sensitive
    atg1 synchronization, nutrient-rich conditions and rapamycin/starvation controls.
    Cargo/receptor deletion delays efficient Cvt vesicle delivery and PAS organization;
    starvation autophagosome formation remains distinct. Atg8-PE reporter delivery
    is a proxy requiring processing controls. The source supports cargo inclusion
    and condition-specific assembly contribution, not universal necessity of every
    actor or an exhaustive lipid/Atg inventory. Atg19/Cvt19 naming is explicit.
  accessed_at: '2026-11-03T11:52:44.427793Z'
  support: supports
  snapshot_sha256: 034ed88ed78ea5ce5ac9e3d0a32d92406cb483b159c8326a0131af538d6efe15
- evidence_id: septin-scott2001-pmc-prefixed
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2767243/
  locator: 'Genuine current PMC2767243 HTML: Results S8 including Figure6 caption;
    Discussion S14; Methods Strains and Media S18/Table1, coimmunoprecipitation S24
    and in-vitro binding S25. Complete abstract read separately; remaining article
    sections and pixels not claimed.'
  summary: Coimmunoprecipitation distinguishes prAPI precursor association from mature
    API and a propeptide mutant; heterologous E.coli extract/reticulocyte translation
    assays support Cvt19 binding without a required yeast bridging protein. This is
    not a purified-protein-only assay. Discussion distinguishes atypical cargo-bound
    receptor turnover from classical receptor recycling and the inner cargo compartment
    from intermembrane space. The bounded receptor claim is supported without importing
    every downstream membrane-assembly step.
  accessed_at: '2026-11-03T11:52:44.702094Z'
  support: supports
  snapshot_sha256: a9adfeccab0e78afcae666a34064d14af638feb99cccb8ff591c114ecb03c8f1
- evidence_id: septin-lumen-search
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=Cvt%20vesicle%20lumen&limit=100
  locator: Current first100 returned GO candidate ids/names, pageInfo current1 of7
  summary: No exact Cvt vesicle lumen term was identified in this bounded returned
    set. Exact SL0323 supports retained local identity. No exhaustive ontology absence
    or forced broader-term mapping is claimed.
  accessed_at: '2026-11-03T11:51:55.387712Z'
  support: supports
  snapshot_sha256: 53ddff600f724b5365e6ac945bb7992736857f613acc0288fb6c8187024a459b
  search_scope: QuickGO search query=Cvt vesicle lumen, limit=100, page1 of7, 608
    reported hits, no date filter; returned first100 ids/names inspected at 2026-11-03T11:51:55.387712Z.
    No later pages or global exact-match exclusion claimed.
- evidence_id: septin-local-identity-search
  kind: search
  reference: 'rg --no-ignore --hidden -n ^identifier: (cellstructuremech:cvt_vesicle_lumen|GO:0033107|GO:0033110|GO:0034270)$
    data/structures'
  locator: Complete exact anchored-identifier matches in data/structures including
    hidden/ignored files
  summary: Each of the three target ids and the context Cvt-complex id has one matching
    maintained record; the full matched contents were read only where already frozen.
  accessed_at: '2026-11-03T11:53:52.018015Z'
  support: supports
  snapshot_sha256: dc19b7fb7b78016b813044f0c66cd550844d49a39861ed1e766df48c4a5ad624
  search_scope: Actual rg --no-ignore --hidden search of all data/structures at 2026-11-03T11:53:52.018015Z;
    exact four identifier alternatives in reference. Hidden and gitignored files included;
    other repository paths and semantic synonyms not claimed exhaustively searched.
- evidence_id: septin-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Complete official organism list and every returned organism/dataset key
  summary: No Saccharomyces cerevisiae or other yeast-matched organism/dataset is
    in the returned official catalogue. All three records positively invoke the Cvt/early-secretory
    pathway; whole and membrane also name molecular cargo/receptor context. A source
    applicability assessment is required even without expression claims. No unrelated
    organism query or biological absence inference is justified.
  accessed_at: '2026-11-03T11:52:44.039212Z'
  support: supports
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: Official GET https://imodulondb.org/api/datasets at 2026-11-03T11:52:44.039212Z;
    entire response inspected for Saccharomyces/cerevisiae/yeast names and every organism/dataset
    key; no date filter. No downstream gene/module search because no matched host
    dataset.
- evidence_id: septin-historical-adapter-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical actual datasets invocation00:49:00.848907Z–00:49:00.863225Z
  summary: Historical canary invocation exited1 with PermissionError reading pyvenv.cfg.
    This hash-verified retained receipt is not a fresh invocation or successful current
    adapter run; current official catalogue fallback was read separately.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: septin-access-source-receipts
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/adversary-septin/source-receipts.json
  locator: Actual URLs, timestamps, response outcomes and successful-response hashes
  summary: Numeric PMC links returned HTTP200 challenge pages, not scientific text;
    prefixed PMC links returned genuine article bodies. Guessed S3 .1 objects returned404
    and EuropePMC fullTextXML returned500. The guessed /organisms.json catalogue path
    returned an HTML fallback, not catalogue data; the correct /api/datasets response
    was independently inspected. No failed or stub route is counted as body access.
  accessed_at: '2026-11-03T11:55:50.493869Z'
  support: context_only
  snapshot_sha256: 9448fcd6fc0759a0b52ef00f576f23f7009df1cdf3a339a333252ec94934d984
- evidence_id: septin-access-source-receipts2
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/adversary-septin/source-receipts2.json
  locator: Actual URLs, timestamps, response outcomes and successful-response hashes
  summary: Numeric PMC links returned HTTP200 challenge pages, not scientific text;
    prefixed PMC links returned genuine article bodies. Guessed S3 .1 objects returned404
    and EuropePMC fullTextXML returned500. The guessed /organisms.json catalogue path
    returned an HTML fallback, not catalogue data; the correct /api/datasets response
    was independently inspected. No failed or stub route is counted as body access.
  accessed_at: '2026-11-03T11:55:50.493869Z'
  support: context_only
  snapshot_sha256: 14d38dbd75275214edb0f1356392664c2a9b553fb6b182293821307a66db654c
- evidence_id: check-qc
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/qc.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T11:57:16.421187Z'
  support: supports
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  snapshot_sha256: 2bbbe60a09577b2f2de849c7bfbf52382d0acc4c6ed1156009a5c209a02efa3d
- evidence_id: check-labels
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/labels.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T11:52:59.280793Z'
  support: supports
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  snapshot_sha256: 6cdfb05df9a27194f05a5fd7f851783f817ac1523ca0bbfa54fe0e0d18775905
- evidence_id: check-trait-links
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/trait-links.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T11:52:13.186139Z'
  support: supports
  summary: Native TraitMech link check passed.
  snapshot_sha256: dadd6223e84bf32d1adecaa22e764e318c14e28a1239fa98bf54f0f826668573
- evidence_id: check-vendored
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/vendored.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T11:52:36.664146Z'
  support: supports
  summary: Pinned governed files match; native vendored check passed.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: check-curies
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/curies.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T11:52:14.320190Z'
  support: supports
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  snapshot_sha256: bc12b1285f5747707643f7a98e03dbb3a6c88fb062ad49f99db9cb42ececf3d2
- evidence_id: focused
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/focused-results.json
  locator: All twenty actual target schema/strict command outputs
  accessed_at: '2026-11-03T11:59:12Z'
  support: supports
  summary: Ten schema and ten strict commands returned exit zero.
  snapshot_sha256: f2ee73a88fe11d26327f201104fa55a3d22f5c6fb3aadfda27f983324719d9ae
- evidence_id: supplemental-pmid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/pmid-chunks-receipt.json
  locator: Complete native-report PMID set checked with unchanged resolver in batches
    of at most fifty
  accessed_at: '2026-11-03T11:53:16.693167Z'
  support: supports
  summary: 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers
    remain unverified.
  snapshot_sha256: 21ba8fa5c4d096d6f364db94a38562b8f93470f85dce400ba438baf34731ae7f
- evidence_id: historical-adapter-runner-availability
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner invocation receipt, cross-checked against exact stdout/stderr
    hashes; reread during PR2362 synthesis
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS
    PermissionError reading the configured runner pyvenv.cfg. This is a retained historical
    availability observation, not a fresh attempt or a scientific validation failure.
    Native policy permits inspected source-catalogue fallback.
assessments:
- assessment_id: plaque-t5-native
  area: schema
  topic: Native protein and graph inventories
  outcome: supported
  summary: Both commands pass empty represented protein inventories and zero GENE_OR_PROTEIN
    nodes. These are mechanical checks, not independent certification of paper biology
    or an exhaustive membrane proteome.
  target_ids:
  - GO:0036012
  evidence_ids:
  - plaque-current-5
  - plaque-native-cyanelle_inner_membrane-verify
  - plaque-native-cyanelle_inner_membrane-causal
- assessment_id: plaque-t5-provenance
  area: provenance
  topic: Original lineage and unchanged frozen record
  outcome: supported
  summary: Original validates/renders exactly and all historical input hashes match.
    Current target is unchanged; no stale input requires refresh. Original findings/actions
    are empty. Historical record issues are context only, not reclosed or recertified.
  target_ids:
  - GO:0036012
  evidence_ids:
  - plaque-current-5
  - plaque-original-5
  - plaque-original-checks
- assessment_id: plaque-t5-coverage
  area: completeness
  topic: Entire maintained record and bounded science
  outcome: supported
  summary: All maintained fields, histories, discussions and graph edges read. No
    images, snippets, quantitative properties or named protein examples are represented.
    Optional protein inventories are not fabricated and no scientific curation defect
    established at declared evidence tiers.
  target_ids:
  - GO:0036012
  evidence_ids:
  - plaque-current-5
  - plaque-policy
  - plaque-rubric
- assessment_id: plaque-t5-taxonomy
  area: scope
  topic: Exact organism/class and qualitative occurrence
  outcome: supported
  summary: ENA verifies C.paradoxa2762 and Glaucocystophyceae38254 including Glaucophyta
    synonym. COMMON is qualitative defining organization, not a sampled numerical
    prevalence or identical composition in every life stage. Primary culture observations
    remain strain-specific.
  target_ids:
  - GO:0036012
  evidence_ids:
  - plaque-current-5
  - plaque-shared-go
  - plaque-shared-tax2762
  - plaque-shared-tax38254
  - plaque-shared-giddings1983-page409
- assessment_id: plaque-t5-necessity
  area: evidence
  topic: Collective material versus particular molecule necessity
  outcome: unknown
  summary: Morphology and localization do not establish that an individual lipid species,
    PG modification or protein is necessary for formation. Such claims are not made
    here. ESSENTIAL bilayer entries are constitutional collective material; IMS PG
    essentiality is explicitly UNKNOWN.
  target_ids:
  - GO:0036012
  evidence_ids:
  - plaque-current-5
  - plaque-shared-go
  - plaque-shared-pfanzagl1996-meta
  - plaque-rubric
- assessment_id: plaque-t5-source-tiers
  area: provenance
  topic: Primary scans and limited biochemical evidence
  outcome: supported
  summary: Fresh Giddings scans409/414/416/417 were independently viewed, including
    source text and figures; no full-paper or raw-image reanalysis. Pfanzagl primary-structure
    evidence is complete abstract only. Historical presumed PG/LPS chemistry and endosymbiont
    wording are not generalized into new molecular or evolutionary claims.
  target_ids:
  - GO:0036012
  evidence_ids:
  - plaque-current-5
  - plaque-shared-giddings1983-meta
  - plaque-shared-giddings1983-page409
  - plaque-shared-giddings1983-page414
  - plaque-shared-giddings1983-page416
  - plaque-shared-giddings1983-page417
  - plaque-shared-pfanzagl1996-meta
- assessment_id: plaque-t6-native
  area: schema
  topic: Native protein and graph inventories
  outcome: supported
  summary: Both commands pass empty represented protein inventories and zero GENE_OR_PROTEIN
    nodes. These are mechanical checks, not independent certification of paper biology
    or an exhaustive membrane proteome.
  target_ids:
  - GO:0036014
  evidence_ids:
  - plaque-current-6
  - plaque-native-cyanelle_intermembrane_space-verify
  - plaque-native-cyanelle_intermembrane_space-causal
- assessment_id: plaque-t6-provenance
  area: provenance
  topic: Original lineage and unchanged frozen record
  outcome: supported
  summary: Original validates/renders exactly and all historical input hashes match.
    Current target is unchanged; no stale input requires refresh. Original findings/actions
    are empty. Historical record issues are context only, not reclosed or recertified.
  target_ids:
  - GO:0036014
  evidence_ids:
  - plaque-current-6
  - plaque-original-6
  - plaque-original-checks
- assessment_id: plaque-t6-coverage
  area: completeness
  topic: Entire maintained record and bounded science
  outcome: supported
  summary: All maintained fields, histories, discussions and graph edges read. No
    images, snippets, quantitative properties or named protein examples are represented.
    Optional protein inventories are not fabricated and no scientific curation defect
    established at declared evidence tiers.
  target_ids:
  - GO:0036014
  evidence_ids:
  - plaque-current-6
  - plaque-policy
  - plaque-rubric
- assessment_id: plaque-t6-taxonomy
  area: scope
  topic: Exact organism/class and qualitative occurrence
  outcome: supported
  summary: ENA verifies C.paradoxa2762 and Glaucocystophyceae38254 including Glaucophyta
    synonym. COMMON is qualitative defining organization, not a sampled numerical
    prevalence or identical composition in every life stage. Primary culture observations
    remain strain-specific.
  target_ids:
  - GO:0036014
  evidence_ids:
  - plaque-current-6
  - plaque-shared-go
  - plaque-shared-tax2762
  - plaque-shared-tax38254
  - plaque-shared-giddings1983-page409
- assessment_id: plaque-t6-necessity
  area: evidence
  topic: Collective material versus particular molecule necessity
  outcome: unknown
  summary: Morphology and localization do not establish that an individual lipid species,
    PG modification or protein is necessary for formation. Such claims are not made
    here. ESSENTIAL bilayer entries are constitutional collective material; IMS PG
    essentiality is explicitly UNKNOWN.
  target_ids:
  - GO:0036014
  evidence_ids:
  - plaque-current-6
  - plaque-shared-go
  - plaque-shared-pfanzagl1996-meta
  - plaque-rubric
- assessment_id: plaque-t6-source-tiers
  area: provenance
  topic: Primary scans and limited biochemical evidence
  outcome: supported
  summary: Fresh Giddings scans409/414/416/417 were independently viewed, including
    source text and figures; no full-paper or raw-image reanalysis. Pfanzagl primary-structure
    evidence is complete abstract only. Historical presumed PG/LPS chemistry and endosymbiont
    wording are not generalized into new molecular or evolutionary claims.
  target_ids:
  - GO:0036014
  evidence_ids:
  - plaque-current-6
  - plaque-shared-giddings1983-meta
  - plaque-shared-giddings1983-page409
  - plaque-shared-giddings1983-page414
  - plaque-shared-giddings1983-page416
  - plaque-shared-giddings1983-page417
  - plaque-shared-pfanzagl1996-meta
- assessment_id: plaque-t7-native
  area: schema
  topic: Native protein and graph inventories
  outcome: supported
  summary: Both commands pass empty represented protein inventories and zero GENE_OR_PROTEIN
    nodes. These are mechanical checks, not independent certification of paper biology
    or an exhaustive membrane proteome.
  target_ids:
  - GO:0033113
  evidence_ids:
  - plaque-current-7
  - plaque-native-cyanelle_membrane-verify
  - plaque-native-cyanelle_membrane-causal
- assessment_id: plaque-t7-provenance
  area: provenance
  topic: Original lineage and unchanged frozen record
  outcome: supported
  summary: Original validates/renders exactly and all historical input hashes match.
    Current target is unchanged; no stale input requires refresh. Original findings/actions
    are empty. Historical record issues are context only, not reclosed or recertified.
  target_ids:
  - GO:0033113
  evidence_ids:
  - plaque-current-7
  - plaque-original-7
  - plaque-original-checks
- assessment_id: plaque-t7-coverage
  area: completeness
  topic: Entire maintained record and bounded science
  outcome: supported
  summary: All maintained fields, histories, discussions and graph edges read. No
    images, snippets, quantitative properties or named protein examples are represented.
    Optional protein inventories are not fabricated and no scientific curation defect
    established at declared evidence tiers.
  target_ids:
  - GO:0033113
  evidence_ids:
  - plaque-current-7
  - plaque-policy
  - plaque-rubric
- assessment_id: plaque-t7-taxonomy
  area: scope
  topic: Exact organism/class and qualitative occurrence
  outcome: supported
  summary: ENA verifies C.paradoxa2762 and Glaucocystophyceae38254 including Glaucophyta
    synonym. COMMON is qualitative defining organization, not a sampled numerical
    prevalence or identical composition in every life stage. Primary culture observations
    remain strain-specific.
  target_ids:
  - GO:0033113
  evidence_ids:
  - plaque-current-7
  - plaque-shared-go
  - plaque-shared-tax2762
  - plaque-shared-tax38254
  - plaque-shared-giddings1983-page409
- assessment_id: plaque-t7-necessity
  area: evidence
  topic: Collective material versus particular molecule necessity
  outcome: unknown
  summary: Morphology and localization do not establish that an individual lipid species,
    PG modification or protein is necessary for formation. Such claims are not made
    here. ESSENTIAL bilayer entries are constitutional collective material; IMS PG
    essentiality is explicitly UNKNOWN.
  target_ids:
  - GO:0033113
  evidence_ids:
  - plaque-current-7
  - plaque-shared-go
  - plaque-shared-pfanzagl1996-meta
  - plaque-rubric
- assessment_id: plaque-t7-source-tiers
  area: provenance
  topic: Primary scans and limited biochemical evidence
  outcome: supported
  summary: Fresh Giddings scans409/414/416/417 were independently viewed, including
    source text and figures; no full-paper or raw-image reanalysis. Pfanzagl primary-structure
    evidence is complete abstract only. Historical presumed PG/LPS chemistry and endosymbiont
    wording are not generalized into new molecular or evolutionary claims.
  target_ids:
  - GO:0033113
  evidence_ids:
  - plaque-current-7
  - plaque-shared-giddings1983-meta
  - plaque-shared-giddings1983-page409
  - plaque-shared-giddings1983-page414
  - plaque-shared-giddings1983-page416
  - plaque-shared-giddings1983-page417
  - plaque-shared-pfanzagl1996-meta
- assessment_id: plaque-t8-native
  area: schema
  topic: Native protein and graph inventories
  outcome: supported
  summary: Both commands pass empty represented protein inventories and zero GENE_OR_PROTEIN
    nodes. These are mechanical checks, not independent certification of paper biology
    or an exhaustive membrane proteome.
  target_ids:
  - GO:0036013
  evidence_ids:
  - plaque-current-8
  - plaque-native-cyanelle_outer_membrane-verify
  - plaque-native-cyanelle_outer_membrane-causal
- assessment_id: plaque-t8-provenance
  area: provenance
  topic: Original lineage and unchanged frozen record
  outcome: supported
  summary: Original validates/renders exactly and all historical input hashes match.
    Current target is unchanged; no stale input requires refresh. Original findings/actions
    are empty. Historical record issues are context only, not reclosed or recertified.
  target_ids:
  - GO:0036013
  evidence_ids:
  - plaque-current-8
  - plaque-original-8
  - plaque-original-checks
- assessment_id: plaque-t8-coverage
  area: completeness
  topic: Entire maintained record and bounded science
  outcome: supported
  summary: All maintained fields, histories, discussions and graph edges read. No
    images, snippets, quantitative properties or named protein examples are represented.
    Optional protein inventories are not fabricated and no scientific curation defect
    established at declared evidence tiers.
  target_ids:
  - GO:0036013
  evidence_ids:
  - plaque-current-8
  - plaque-policy
  - plaque-rubric
- assessment_id: plaque-t8-taxonomy
  area: scope
  topic: Exact organism/class and qualitative occurrence
  outcome: supported
  summary: ENA verifies C.paradoxa2762 and Glaucocystophyceae38254 including Glaucophyta
    synonym. COMMON is qualitative defining organization, not a sampled numerical
    prevalence or identical composition in every life stage. Primary culture observations
    remain strain-specific.
  target_ids:
  - GO:0036013
  evidence_ids:
  - plaque-current-8
  - plaque-shared-go
  - plaque-shared-tax2762
  - plaque-shared-tax38254
  - plaque-shared-giddings1983-page409
  - plaque-kojima2016-canonical
- assessment_id: plaque-t8-necessity
  area: evidence
  topic: Collective material versus particular molecule necessity
  outcome: unknown
  summary: Morphology and localization do not establish that an individual lipid species,
    PG modification or protein is necessary for formation. Such claims are not made
    here. ESSENTIAL bilayer entries are constitutional collective material; IMS PG
    essentiality is explicitly UNKNOWN.
  target_ids:
  - GO:0036013
  evidence_ids:
  - plaque-current-8
  - plaque-shared-go
  - plaque-shared-pfanzagl1996-meta
  - plaque-rubric
- assessment_id: plaque-t8-source-tiers
  area: provenance
  topic: Primary scans and limited biochemical evidence
  outcome: supported
  summary: Fresh Giddings scans409/414/416/417 were independently viewed, including
    source text and figures; no full-paper or raw-image reanalysis. Pfanzagl primary-structure
    evidence is complete abstract only. Historical presumed PG/LPS chemistry and endosymbiont
    wording are not generalized into new molecular or evolutionary claims.
  target_ids:
  - GO:0036013
  evidence_ids:
  - plaque-current-8
  - plaque-shared-giddings1983-meta
  - plaque-shared-giddings1983-page409
  - plaque-shared-giddings1983-page414
  - plaque-shared-giddings1983-page416
  - plaque-shared-giddings1983-page417
  - plaque-shared-pfanzagl1996-meta
- assessment_id: plaque-t5-identity
  area: identity
  topic: Exact compartment, parentage and source scope
  outcome: supported
  summary: Exact GO0036012/SL0480 identify the stroma-facing inner envelope membrane,
    exact inner-envelope synonym, plastid-inner and generic cyanelle-membrane parents
    and envelope parthood.
  target_ids:
  - GO:0036012
  evidence_ids:
  - plaque-current-5
  - plaque-shared-go
  - plaque-cyanelle-boundary-parents
  - plaque-cyanelle-SL-0480
- assessment_id: plaque-t6-identity
  area: identity
  topic: Exact compartment, parentage and source scope
  outcome: supported
  summary: Exact GO0036014/SL0481 identify the PG-containing intermembrane region;
    both GO synonyms are exact. Plastid-IMS is is_a and envelope is the containing
    structure; region is distinct from its boundaries and stroma.
  target_ids:
  - GO:0036014
  evidence_ids:
  - plaque-current-6
  - plaque-shared-go
  - plaque-cyanelle-boundary-parents
  - plaque-cyanelle-SL-0481
- assessment_id: plaque-t7-identity
  area: identity
  topic: Exact compartment, parentage and source scope
  outcome: supported
  summary: GO0033113 identifies either envelope bilayer, with plastid-membrane parent
    and envelope parthood. SL0083 has broader unresolved outer/inner/thylakoid localization
    scope; maintained evidence explicitly caveats this and correctly omits an exact
    xref.
  target_ids:
  - GO:0033113
  evidence_ids:
  - plaque-current-7
  - plaque-shared-go
  - plaque-cyanelle-boundary-parents
  - plaque-cyanelle-SL-0083
- assessment_id: plaque-t8-identity
  area: identity
  topic: Exact compartment, parentage and source scope
  outcome: supported
  summary: Exact GO0036013/SL0482 identify the cytoplasm-facing outer membrane; generic
    cyanelle/plastid-outer parents and envelope parthood agree. Native source definitions
    distinguish outer membrane from whole envelope, PG layer and IMS.
  target_ids:
  - GO:0036013
  evidence_ids:
  - plaque-current-8
  - plaque-shared-go
  - plaque-cyanelle-boundary-parents
  - plaque-cyanelle-SL-0482
- assessment_id: plaque-t5-composition
  area: grounding
  topic: Material constituent and honest unresolved grounding
  outcome: supported
  summary: Collective inner lipid bilayer is defining membrane material, not a single
    chemical species. REVIEWED_LABEL_ONLY and the existing grounding TODO retain specificity
    honestly; the whole-membrane GO identifier is not misused as an exact chemical
    ID.
  target_ids:
  - GO:0036012
  evidence_ids:
  - plaque-current-5
  - plaque-shared-go
  - plaque-rubric
- assessment_id: plaque-t6-composition
  area: grounding
  topic: Material constituent and honest unresolved grounding
  outcome: supported
  summary: PG is a structural layer in the IMS, not a single muropeptide or a membrane-bounded
    compartment. Direct GO/SL placement and primary chemistry support its presence.
    UNKNOWN essentiality and explicit material-layer grounding TODO avoid guessed
    IDs or implied biogenesis necessity.
  target_ids:
  - GO:0036014
  evidence_ids:
  - plaque-current-6
  - plaque-shared-go
  - plaque-rubric
  - plaque-cyanelle-SL-0481
  - plaque-shared-pfanzagl1996-meta
- assessment_id: plaque-t7-composition
  area: grounding
  topic: Material constituent and honest unresolved grounding
  outcome: supported
  summary: Generic collective envelope lipid bilayer is constitutional material when
    inner/outer identity is unspecified. GO envelope-only scope excludes thylakoid
    membrane; broader SL fallback is not treated as exact constituent identity.
  target_ids:
  - GO:0033113
  evidence_ids:
  - plaque-current-7
  - plaque-shared-go
  - plaque-rubric
- assessment_id: plaque-t8-composition
  area: grounding
  topic: Material constituent and honest unresolved grounding
  outcome: supported
  summary: The outer lipid bilayer is collective material. Kojima protein localization
    is bounded contextual support for the exterior membrane boundary, not identification
    of a specific lipid or evidence that CppS/F is universally required to form it.
  target_ids:
  - GO:0036013
  evidence_ids:
  - plaque-current-8
  - plaque-shared-go
  - plaque-rubric
  - plaque-kojima2016-canonical
- assessment_id: plaque-t5-graph
  area: graph
  topic: Complete descriptive graph
  outcome: supported
  summary: All three NONMECHANISTIC edges represent envelope parthood and the stroma/IMS
    boundaries. Exact GO/SL and inspected envelope ultrastructure support the geometry;
    no import machinery or photosystem mechanism is asserted.
  target_ids:
  - GO:0036012
  evidence_ids:
  - plaque-current-5
  - plaque-shared-go
  - plaque-graph-policy
  - plaque-cyanelle-SL-0480
- assessment_id: plaque-t6-graph
  area: graph
  topic: Complete descriptive graph
  outcome: supported
  summary: Outer and inner membrane delimit the region; structural PG resides within
    it. component_ref points to the actual PG material, not a gene/protein. All three
    NONMECHANISTIC relations agree with GO/SL and chemistry, without transport or
    PG-remodeling mechanisms.
  target_ids:
  - GO:0036014
  evidence_ids:
  - plaque-current-6
  - plaque-shared-go
  - plaque-graph-policy
  - plaque-cyanelle-SL-0481
  - plaque-cyanelle-SL-0480
- assessment_id: plaque-t7-graph
  area: graph
  topic: Complete descriptive graph
  outcome: supported
  summary: Three descriptive relations state generic membrane partOf envelope and
    inner/outer is_a generic membrane. Direct typed GO children support them; component_ref
    identifies collective material without substituting a protein identity. Thylakoid
    is explicitly excluded.
  target_ids:
  - GO:0033113
  evidence_ids:
  - plaque-current-7
  - plaque-shared-go
  - plaque-graph-policy
  - plaque-cyanelle-SL-0083
- assessment_id: plaque-t8-graph
  area: graph
  topic: Complete descriptive graph
  outcome: supported
  summary: Envelope parthood, cytoplasm-facing orientation and outer boundary of the
    IMS are source-supported. GO/SL geometry plus Kojima exterior localization agree,
    without equating membrane with PG or claiming transport kinetics.
  target_ids:
  - GO:0036013
  evidence_ids:
  - plaque-current-8
  - plaque-shared-go
  - plaque-graph-policy
  - plaque-cyanelle-SL-0482
  - plaque-kojima2016-canonical
- assessment_id: plaque-t6-comparative-scope
  area: evidence
  topic: PG distribution across the named genera
  outcome: supported
  summary: PMID8955325 primary abstract directly reports Glaucocystis nostochinearum
    and Cyanoptyche gloeocystis PG analysis with prior Cyanophora comparison. This
    supports the three named genera in the class-level note, not every glaucophyte
    strain or a universal quantified chemical recipe. C.paradoxa canonical example
    is the separate primary-structure study.
  target_ids:
  - GO:0036014
  evidence_ids:
  - plaque-current-6
  - plaque-pfanzagl-comparative-meta
  - plaque-pfanzagl-comparative-body
  - plaque-shared-pfanzagl1996-meta
- assessment_id: plaque-t8-biochemical-localization
  area: evidence
  topic: Exterior protein localization and distinct experimental assays
  outcome: supported
  summary: Kojima NIES547 fractionation, PG/protein preparations, microscopy/pigment
    support and separate outer-membrane preparation support the record’s narrow localization
    note. Primary proteoliposome channel assays are separate from live-cell rates
    or formation necessity. The record does not assert a complete CppS/F inventory
    or import mechanistic/evolutionary title claims wholesale.
  target_ids:
  - GO:0036013
  evidence_ids:
  - plaque-current-8
  - plaque-kojima2016-canonical
  - plaque-kojima2016-meta
- assessment_id: plaque-t5-adapter
  area: scope
  topic: Genuine material and topology applicability exclusion
  outcome: not_applicable
  summary: Inner membrane describes collective lipid material and stroma/IMS topology;
    no named molecular identity, regulator, pathway, stress response, trait or dataset
    is asserted. Its absent original adapter row does not create a defect when applicability
    is genuinely absent. Fresh complete catalogue also has no Cyanophora/glaucophyte
    host. No unmatched bacterial/cyanobacterial dataset, missing inventory or biological
    absence is inferred; historical runner remains separately dated.
  target_ids:
  - GO:0036012
  evidence_ids:
  - plaque-current-5
  - plaque-original-5
  - plaque-policy
  - plaque-catalogue
  - plaque-historical-runner
- assessment_id: plaque-t6-adapter
  area: scope
  topic: Genuine material and topology applicability exclusion
  outcome: not_applicable
  summary: IMS describes PG as a material layer and comparative structural occurrence,
    not PG biosynthesis/remodeling machinery, a regulator or stress-response trait.
    No positive molecular/pathway trigger is asserted; the absent original row alone
    is not a defect. Fresh complete catalogue also has no Cyanophora/glaucophyte host.
    No unmatched bacterial/cyanobacterial dataset, missing inventory or biological
    absence is inferred; historical runner remains separately dated.
  target_ids:
  - GO:0036014
  evidence_ids:
  - plaque-current-6
  - plaque-original-6
  - plaque-policy
  - plaque-catalogue
  - plaque-historical-runner
- assessment_id: plaque-t7-adapter
  area: scope
  topic: Genuine material and topology applicability exclusion
  outcome: not_applicable
  summary: Generic membrane describes envelope lipid material and localization-class
    boundaries. The broader SL fallback mentions unresolved protein locations but
    asserts no named protein or pathway. Retain genuine N/A with this concrete scope
    rationale; do not count its earlier expression-only wording as a defect when no
    trigger exists. Fresh complete catalogue also has no Cyanophora/glaucophyte host.
    No unmatched bacterial/cyanobacterial dataset, missing inventory or biological
    absence is inferred; historical runner remains separately dated.
  target_ids:
  - GO:0033113
  evidence_ids:
  - plaque-current-7
  - plaque-original-7
  - plaque-policy
  - plaque-catalogue
  - plaque-historical-runner
- assessment_id: plaque-t8-adapter
  area: scope
  topic: Genuine material and topology applicability exclusion
  outcome: not_applicable
  summary: Outer membrane cites generic protein-localization experiments as topology
    context but names no constituent gene/protein, regulator, pathway or stress-response
    mechanism. A paper title mentioning diffusion channels is bibliographic context,
    not a target assertion of channel machinery. Genuine N/A is retained with this
    scope rationale. Fresh complete catalogue also has no Cyanophora/glaucophyte host.
    No unmatched bacterial/cyanobacterial dataset, missing inventory or biological
    absence is inferred; historical runner remains separately dated.
  target_ids:
  - GO:0036013
  evidence_ids:
  - plaque-current-8
  - plaque-original-8
  - plaque-policy
  - plaque-catalogue
  - plaque-historical-runner
- assessment_id: micro-cyanelle-identity
  area: identity
  topic: Exact structure and boundary identity
  outcome: supported
  summary: GO0009842 denotes the whole glaucophyte photosynthetic plastid, with valid
    plastid is-a and envelope/stroma/thylakoid parthood; exact synonyms and native
    status are preserved.
  target_ids:
  - GO:0009842
  evidence_ids:
  - micro-record-cyanelle
  - micro-go
  - micro-SL-0082
  - micro-SL-0479
  - micro-SL-0350
  - micro-cyanelle-SL-0480
- assessment_id: micro-cyanelle-taxa
  area: scope
  topic: Qualitative occurrence versus experimental scope
  outcome: supported
  summary: Species2762 and class38254 are current verified authorities. COMMON is
    characteristic qualitative anatomy, not measured prevalence; canonical C.paradoxa
    is species-level illustration of paper-specific experimental material. Giddings
    used UTEX LB555; Kojima NIES547; Price genome study CCMP329. Native authorities
    support defining glaucophyte anatomy; no claim of every species being experimentally
    tested.
  target_ids:
  - GO:0009842
  evidence_ids:
  - micro-record-cyanelle
  - micro-tax2762
  - micro-tax38254
  - micro-giddings1983-page409
  - micro-giddings1983-page410
  - micro-giddings1983-page412
  - micro-giddings1983-page414
  - micro-giddings1983-page416
  - micro-giddings1983-page417
  - micro-pfanzagl1996-meta
  - micro-pfanzagl-comparative-meta
  - micro-kojima2016-canonical
  - micro-price2019-s3
  - micro-SL-0350
- assessment_id: micro-cyanelle-composition
  area: completeness
  topic: Constituents, optional content and necessity
  outcome: supported
  summary: Three lipid-bilayer rows identify constituent membranes; PG sheet is reviewed-label-only
    with an explicit unresolved exact-grounding discussion. UNKNOWN essentiality is
    not a missing knockout assertion. The record does not promise a complete molecular
    stoichiometry/inventory.
  target_ids:
  - GO:0009842
  evidence_ids:
  - micro-record-cyanelle
  - micro-policy
  - micro-go
  - micro-SL-0082
  - micro-SL-0479
  - micro-SL-0350
  - micro-cyanelle-SL-0480
  - micro-pfanzagl1996-meta
  - micro-kojima2016-canonical
  - micro-pg-search
- assessment_id: micro-cyanelle-native-protein
  area: schema
  topic: Empty native protein checks
  outcome: supported
  summary: Both actual native commands exited0 on the current source. Empty declared
    accession inventories and zero GENE_OR_PROTEIN nodes make this a bounded representation
    check, not an exhaustive protein search, identity verification, biochemical-membership
    or assembly-necessity finding.
  target_ids:
  - GO:0009842
  evidence_ids:
  - micro-record-cyanelle
  - micro-native-cyanelle-verify
  - micro-native-cyanelle-causal
- assessment_id: micro-cyanelle-historical-input
  area: provenance
  topic: Original hashes, native pair integrity and lineage
  outcome: supported
  summary: 'Only this target is stale in my slice: original source hash24275c8050ca5d13c66d563c7aa697a4de65766f87499f876fc94c41cd2f0db7
    changed to5ebb2c3b4cc2d9364dc08ac335c793409014f30f0ca009ee3b4aeafb860371b6. A
    new history event and three topological edges were fully reassessed; original
    five-edge review remains historical. Original native validation/render match;
    all three original scientific findings/actions were empty, so no predecessor finding
    or historical issue is terminally resolved by this review.'
  target_ids:
  - GO:0009842
  evidence_ids:
  - micro-record-cyanelle
  - micro-prior-cyanelle
  - micro-original-validation-inputs
- assessment_id: micro-cyanelle-source-tiers
  area: evidence
  topic: Claim support and source-access limits
  outcome: supported
  summary: Current source review uses native authority definitions, six visually inspected
    Giddings scans, Pfanzagl primary-structure and comparative abstracts, bounded
    genuine Kojima body, and bounded Price JATS. Price and GO support photosynthetic
    function; Giddings morphology alone is not used as the sole proof of physiological
    function. Historical terminology, microscopy preparation effects, literature-cited
    context and actual strain scopes remain qualified; no new molecular necessity
    or universal prevalence claims are made.
  target_ids:
  - GO:0009842
  evidence_ids:
  - micro-record-cyanelle
  - micro-giddings1983-page409
  - micro-giddings1983-page410
  - micro-giddings1983-page412
  - micro-giddings1983-page414
  - micro-giddings1983-page416
  - micro-giddings1983-page417
  - micro-pfanzagl1996-meta
  - micro-pfanzagl-comparative-meta
  - micro-kojima2016-canonical
  - micro-price2019-s3
  - micro-giddings1983-meta
  - micro-price2019-meta
  - micro-go
  - micro-SL-0082
  - micro-SL-0479
  - micro-SL-0350
  - micro-cyanelle-SL-0480
- assessment_id: micro-cyanelle-unpopulated
  area: evidence
  topic: Images, measurements and verbatim snippets
  outcome: not_applicable
  summary: The entire current target has no image entry or measured property needing
    verification and no verbatim snippet asserted. Source scans were nonetheless visually
    inspected where morphology was assessed; no new measurements or image attribution
    are imputed to the record.
  target_ids:
  - GO:0009842
  evidence_ids:
  - micro-record-cyanelle
  - micro-giddings1983-page409
  - micro-giddings1983-page410
  - micro-giddings1983-page412
  - micro-giddings1983-page414
  - micro-giddings1983-page416
  - micro-giddings1983-page417
- assessment_id: micro-cyanelle-status
  area: provenance
  topic: Status and curation ownership
  outcome: supported
  summary: Record remains PROPOSED. History is treated as context, not certification
    of old correctness or automatic closure of another issue/category. This read-only
    review edits no record or history; any scientific correction belongs to a separate
    guarded-writer curation change.
  target_ids:
  - GO:0009842
  evidence_ids:
  - micro-record-cyanelle
  - micro-prior-cyanelle
  - micro-policy
- assessment_id: micro-cyanelle_envelope-identity
  area: identity
  topic: Exact structure and boundary identity
  outcome: supported
  summary: GO0033112 denotes the complete double-membrane envelope including IMS,
    with plastid-envelope is-a and cyanelle parthood; distinct from either single
    bilayer.
  target_ids:
  - GO:0033112
  evidence_ids:
  - micro-record-cyanelle_envelope
  - micro-go
  - micro-SL-0082
  - micro-SL-0479
  - micro-SL-0350
  - micro-cyanelle-SL-0480
- assessment_id: micro-cyanelle_envelope-taxa
  area: scope
  topic: Qualitative occurrence versus experimental scope
  outcome: supported
  summary: Species2762 and class38254 are current verified authorities. COMMON is
    characteristic qualitative anatomy, not measured prevalence; canonical C.paradoxa
    is species-level illustration of paper-specific experimental material. Giddings
    used UTEX LB555; Kojima NIES547; Price genome study CCMP329. The envelope explicitly
    names Glaucocystis/Cyanoptyche/Cyanophora, supported by PMID8955325 abstract,
    not extrapolated from a single species.
  target_ids:
  - GO:0033112
  evidence_ids:
  - micro-record-cyanelle_envelope
  - micro-tax2762
  - micro-tax38254
  - micro-giddings1983-page409
  - micro-giddings1983-page410
  - micro-giddings1983-page412
  - micro-giddings1983-page414
  - micro-giddings1983-page416
  - micro-giddings1983-page417
  - micro-pfanzagl1996-meta
  - micro-pfanzagl-comparative-meta
  - micro-kojima2016-canonical
  - micro-price2019-s3
  - micro-SL-0350
- assessment_id: micro-cyanelle_envelope-composition
  area: completeness
  topic: Constituents, optional content and necessity
  outcome: supported
  summary: Outer/inner bilayers and PG sheet are material components, not proteins;
    broad IMS is not substituted for PG-sheet identity. UNKNOWN essentiality avoids
    inferring assembly necessity from occurrence or biochemical localization. The
    envelope record does not assert an unrecorded named transport mechanism.
  target_ids:
  - GO:0033112
  evidence_ids:
  - micro-record-cyanelle_envelope
  - micro-policy
  - micro-go
  - micro-SL-0082
  - micro-SL-0479
  - micro-SL-0350
  - micro-cyanelle-SL-0480
  - micro-pfanzagl1996-meta
  - micro-kojima2016-canonical
  - micro-pg-search
- assessment_id: micro-cyanelle_envelope-native-protein
  area: schema
  topic: Empty native protein checks
  outcome: supported
  summary: Both actual native commands exited0 on the current source. Empty declared
    accession inventories and zero GENE_OR_PROTEIN nodes make this a bounded representation
    check, not an exhaustive protein search, identity verification, biochemical-membership
    or assembly-necessity finding.
  target_ids:
  - GO:0033112
  evidence_ids:
  - micro-record-cyanelle_envelope
  - micro-native-cyanelle_envelope-verify
  - micro-native-cyanelle_envelope-causal
- assessment_id: micro-cyanelle_envelope-historical-input
  area: provenance
  topic: Original hashes, native pair integrity and lineage
  outcome: supported
  summary: Current target bytes match the original frozen input. Original native validation/render
    match; all three original scientific findings/actions were empty, so no predecessor
    finding or historical issue is terminally resolved by this review.
  target_ids:
  - GO:0033112
  evidence_ids:
  - micro-record-cyanelle_envelope
  - micro-prior-cyanelle_envelope
  - micro-original-validation-inputs
- assessment_id: micro-cyanelle_envelope-source-tiers
  area: evidence
  topic: Claim support and source-access limits
  outcome: supported
  summary: Current source review uses native authority definitions, six visually inspected
    Giddings scans, Pfanzagl primary-structure and comparative abstracts, bounded
    genuine Kojima body, and bounded Price JATS. Historical terminology, microscopy
    preparation effects, literature-cited context and actual strain scopes remain
    qualified; no new molecular necessity or universal prevalence claims are made.
  target_ids:
  - GO:0033112
  evidence_ids:
  - micro-record-cyanelle_envelope
  - micro-giddings1983-page409
  - micro-giddings1983-page410
  - micro-giddings1983-page412
  - micro-giddings1983-page414
  - micro-giddings1983-page416
  - micro-giddings1983-page417
  - micro-pfanzagl1996-meta
  - micro-pfanzagl-comparative-meta
  - micro-kojima2016-canonical
  - micro-price2019-s3
  - micro-giddings1983-meta
  - micro-price2019-meta
  - micro-go
  - micro-SL-0082
  - micro-SL-0479
  - micro-SL-0350
  - micro-cyanelle-SL-0480
- assessment_id: micro-cyanelle_envelope-unpopulated
  area: evidence
  topic: Images, measurements and verbatim snippets
  outcome: not_applicable
  summary: The entire current target has no image entry or measured property needing
    verification and no verbatim snippet asserted. Source scans were nonetheless visually
    inspected where morphology was assessed; no new measurements or image attribution
    are imputed to the record.
  target_ids:
  - GO:0033112
  evidence_ids:
  - micro-record-cyanelle_envelope
  - micro-giddings1983-page409
  - micro-giddings1983-page410
  - micro-giddings1983-page412
  - micro-giddings1983-page414
  - micro-giddings1983-page416
  - micro-giddings1983-page417
- assessment_id: micro-cyanelle_envelope-status
  area: provenance
  topic: Status and curation ownership
  outcome: supported
  summary: Record remains PROPOSED. History is treated as context, not certification
    of old correctness or automatic closure of another issue/category. This read-only
    review edits no record or history; any scientific correction belongs to a separate
    guarded-writer curation change.
  target_ids:
  - GO:0033112
  evidence_ids:
  - micro-record-cyanelle_envelope
  - micro-prior-cyanelle_envelope
  - micro-policy
- assessment_id: micro-cyanelle_stroma-identity
  area: identity
  topic: Exact structure and boundary identity
  outcome: supported
  summary: GO0034060 and SL0350 denote the stromal compartment excluding thylakoid
    lumen, with plastid-stroma is-a and cyanelle parthood. It is a region, not a protein
    or membrane.
  target_ids:
  - GO:0034060
  evidence_ids:
  - micro-record-cyanelle_stroma
  - micro-go
  - micro-SL-0082
  - micro-SL-0479
  - micro-SL-0350
  - micro-cyanelle-SL-0480
- assessment_id: micro-cyanelle_stroma-taxa
  area: scope
  topic: Qualitative occurrence versus experimental scope
  outcome: supported
  summary: Species2762 and class38254 are current verified authorities. COMMON is
    characteristic qualitative anatomy, not measured prevalence; canonical C.paradoxa
    is species-level illustration of paper-specific experimental material. Giddings
    used UTEX LB555; Kojima NIES547; Price genome study CCMP329. Native authorities
    support defining glaucophyte anatomy; no claim of every species being experimentally
    tested.
  target_ids:
  - GO:0034060
  evidence_ids:
  - micro-record-cyanelle_stroma
  - micro-tax2762
  - micro-tax38254
  - micro-giddings1983-page409
  - micro-giddings1983-page410
  - micro-giddings1983-page412
  - micro-giddings1983-page414
  - micro-giddings1983-page416
  - micro-giddings1983-page417
  - micro-pfanzagl1996-meta
  - micro-pfanzagl-comparative-meta
  - micro-kojima2016-canonical
  - micro-price2019-s3
  - micro-SL-0350
- assessment_id: micro-cyanelle_stroma-composition
  area: completeness
  topic: Constituents, optional content and necessity
  outcome: supported
  summary: No component or protein inventory is declared. Its resolved discussion
    explicitly distinguishes DNA/ribosomes/photosynthetic products as possible compartment
    contents and withholds inventory expansion; omission of optional content-level
    slots is not a consequential defect.
  target_ids:
  - GO:0034060
  evidence_ids:
  - micro-record-cyanelle_stroma
  - micro-policy
  - micro-go
  - micro-SL-0082
  - micro-SL-0479
  - micro-SL-0350
  - micro-cyanelle-SL-0480
  - micro-pfanzagl1996-meta
  - micro-kojima2016-canonical
  - micro-pg-search
- assessment_id: micro-cyanelle_stroma-native-protein
  area: schema
  topic: Empty native protein checks
  outcome: supported
  summary: Both actual native commands exited0 on the current source. Empty declared
    accession inventories and zero GENE_OR_PROTEIN nodes make this a bounded representation
    check, not an exhaustive protein search, identity verification, biochemical-membership
    or assembly-necessity finding.
  target_ids:
  - GO:0034060
  evidence_ids:
  - micro-record-cyanelle_stroma
  - micro-native-cyanelle_stroma-verify
  - micro-native-cyanelle_stroma-causal
- assessment_id: micro-cyanelle_stroma-historical-input
  area: provenance
  topic: Original hashes, native pair integrity and lineage
  outcome: supported
  summary: Current target bytes match the original frozen input. Original native validation/render
    match; all three original scientific findings/actions were empty, so no predecessor
    finding or historical issue is terminally resolved by this review.
  target_ids:
  - GO:0034060
  evidence_ids:
  - micro-record-cyanelle_stroma
  - micro-prior-cyanelle_stroma
  - micro-original-validation-inputs
- assessment_id: micro-cyanelle_stroma-source-tiers
  area: evidence
  topic: Claim support and source-access limits
  outcome: supported
  summary: Current source review uses native authority definitions, six visually inspected
    Giddings scans, Pfanzagl primary-structure and comparative abstracts, bounded
    genuine Kojima body, and bounded Price JATS. Historical terminology, microscopy
    preparation effects, literature-cited context and actual strain scopes remain
    qualified; no new molecular necessity or universal prevalence claims are made.
  target_ids:
  - GO:0034060
  evidence_ids:
  - micro-record-cyanelle_stroma
  - micro-giddings1983-page409
  - micro-giddings1983-page410
  - micro-giddings1983-page412
  - micro-giddings1983-page414
  - micro-giddings1983-page416
  - micro-giddings1983-page417
  - micro-pfanzagl1996-meta
  - micro-pfanzagl-comparative-meta
  - micro-kojima2016-canonical
  - micro-price2019-s3
  - micro-giddings1983-meta
  - micro-price2019-meta
  - micro-go
  - micro-SL-0082
  - micro-SL-0479
  - micro-SL-0350
  - micro-cyanelle-SL-0480
- assessment_id: micro-cyanelle_stroma-unpopulated
  area: evidence
  topic: Images, measurements and verbatim snippets
  outcome: not_applicable
  summary: The entire current target has no image entry or measured property needing
    verification and no verbatim snippet asserted. Source scans were nonetheless visually
    inspected where morphology was assessed; no new measurements or image attribution
    are imputed to the record.
  target_ids:
  - GO:0034060
  evidence_ids:
  - micro-record-cyanelle_stroma
  - micro-giddings1983-page409
  - micro-giddings1983-page410
  - micro-giddings1983-page412
  - micro-giddings1983-page414
  - micro-giddings1983-page416
  - micro-giddings1983-page417
- assessment_id: micro-cyanelle_stroma-status
  area: provenance
  topic: Status and curation ownership
  outcome: supported
  summary: Record remains PROPOSED. History is treated as context, not certification
    of old correctness or automatic closure of another issue/category. This read-only
    review edits no record or history; any scientific correction belongs to a separate
    guarded-writer curation change.
  target_ids:
  - GO:0034060
  evidence_ids:
  - micro-record-cyanelle_stroma
  - micro-prior-cyanelle_stroma
  - micro-policy
- assessment_id: micro-cyanelle-graph
  area: graph
  topic: Eight topological edges and stale three-edge refresh
  outcome: concern
  summary: 'The retained outer-facing/inner-stroma boundary, PG-in-IMS, thylakoid-membrane
    parthood and photosynthesis support remain bounded NONMECHANISTIC topology. Newly
    added stroma→cyanelle parthood is a direct GO relation; thylakoid→stroma residency
    is supported by GO context and Giddings/Price morphology. Newly added IMS→cyanelle
    parthood is valid transitively through envelope. Its evidence note wrongly labels
    that GO relationship direct: F1 is a minor attribution correction, not rejection
    of the anatomical edge.'
  target_ids:
  - GO:0009842
  evidence_ids:
  - micro-record-cyanelle
  - micro-go
  - micro-ims-go-path
  - micro-giddings1983-page409
  - micro-giddings1983-page410
  - micro-giddings1983-page412
  - micro-giddings1983-page414
  - micro-giddings1983-page416
  - micro-giddings1983-page417
  - micro-price2019-s3
- assessment_id: micro-envelope-graph
  area: graph
  topic: Six NONMECHANISTIC envelope edges
  outcome: supported
  summary: Whole/envelope parthood, outer/inner subdivision, inner boundary to stroma,
    IMS within envelope and PG within IMS agree with exact authorities and scoped
    primary evidence. No gene/protein necessity, direct molecular interaction or transport
    mechanism is asserted.
  target_ids:
  - GO:0033112
  evidence_ids:
  - micro-record-cyanelle_envelope
  - micro-go
  - micro-SL-0082
  - micro-SL-0479
  - micro-SL-0350
  - micro-cyanelle-SL-0480
  - micro-giddings1983-page409
  - micro-giddings1983-page410
  - micro-giddings1983-page412
  - micro-giddings1983-page414
  - micro-giddings1983-page416
  - micro-giddings1983-page417
  - micro-pfanzagl1996-meta
  - micro-pfanzagl-comparative-meta
  - micro-kojima2016-canonical
  - micro-price2019-s3
- assessment_id: micro-stroma-graph
  area: graph
  topic: Two NONMECHANISTIC stromal edges
  outcome: supported
  summary: Stroma part_of whole cyanelle and inner membrane bounds stroma are supported
    by current GO and SL0480. The inner membrane separates stroma from IMS, and thylakoid
    lumen is excluded. No arbitrary composition or biochemical causal mechanism is
    inferred.
  target_ids:
  - GO:0034060
  evidence_ids:
  - micro-record-cyanelle_stroma
  - micro-go
  - micro-SL-0082
  - micro-SL-0479
  - micro-SL-0350
  - micro-cyanelle-SL-0480
- assessment_id: micro-cyanelle-adapter
  area: evidence
  topic: Named pathway triggers actual structured-source assessment
  outcome: concern
  summary: Whole cyanelle explicitly names photosynthesisGO0015979, so the original
    no-transcriptomic-inference rationale is insufficient. Current real catalogue
    inspection finds no matching glaucophyte organism/dataset; bacterial Synechococcus
    is not a proxy. Native runner historical unavailability and current public-source
    fallback are distinguished. No applicable matched dataset remains to search/summarize;
    no biological inference follows from this catalogue absence.
  target_ids:
  - GO:0009842
  evidence_ids:
  - micro-record-cyanelle
  - micro-prior-cyanelle
  - micro-policy
  - micro-catalogue
  - micro-historical-adapter-runner
- assessment_id: micro-cyanelle_envelope-adapter
  area: evidence
  topic: Genuine structural/material applicability exclusion
  outcome: not_applicable
  summary: The reviewed current content asserts material identity, compartment boundaries
    and qualitative occurrence, not a named gene/locus/accession/regulator/pathway/stress/trait/transcriptomics
    claim requiring a gene-module query. Bibliographic titles, localization evidence
    and expressly deferred stromal contents do not create an asserted molecular mechanism.
    No separate omission finding is warranted merely because the original N/A wording
    mentioned expression. Whole cyanelle pathway applicability is assessed separately.
  target_ids:
  - GO:0033112
  evidence_ids:
  - micro-record-cyanelle_envelope
  - micro-policy
- assessment_id: micro-cyanelle_stroma-adapter
  area: evidence
  topic: Genuine structural/material applicability exclusion
  outcome: not_applicable
  summary: The reviewed current content asserts material identity, compartment boundaries
    and qualitative occurrence, not a named gene/locus/accession/regulator/pathway/stress/trait/transcriptomics
    claim requiring a gene-module query. Bibliographic titles, localization evidence
    and expressly deferred stromal contents do not create an asserted molecular mechanism.
    No separate omission finding is warranted merely because the original N/A wording
    mentioned expression. Whole cyanelle pathway applicability is assessed separately.
  target_ids:
  - GO:0034060
  evidence_ids:
  - micro-record-cyanelle_stroma
  - micro-policy
- assessment_id: septin-cvt_vesicle-schema
  area: schema
  topic: Original schema/render and unchanged frozen targets
  outcome: supported
  summary: Original native validate/render succeeds with deterministic Markdown and
    matching historical/current target hashes. No record change is needed to refresh
    this assessment.
  target_ids:
  - GO:0033107
  evidence_ids:
  - septin-record-cvt_vesicle
  - septin-original-validation-cvt_vesicle
- assessment_id: septin-cvt_vesicle-native-scope
  area: provenance
  topic: Actual empty protein inventory limits
  outcome: supported
  summary: No protein examples or UniProtKB graph xrefs and zero GENE_OR_PROTEIN graph
    nodes. Execution success verifies only this empty represented inventory; it does
    not establish narrative Ape1/Ams1/Atg identity, localization, mechanism, complete
    composition or formation necessity.
  target_ids:
  - GO:0033107
  evidence_ids:
  - septin-record-cvt_vesicle
  - septin-native-cvt_vesicle-verify
  - septin-native-cvt_vesicle-causal
- assessment_id: septin-cvt_vesicle-nonasserted-surfaces
  area: scope
  topic: Images, measurements, traits and snippets
  outcome: not_applicable
  summary: The maintained record asserts none of these optional surfaces. Textual
    primary figure-caption inspection is not pixel inspection or raw-data reanalysis;
    no image-rights attestation is needed for absent target images.
  target_ids:
  - GO:0033107
  evidence_ids:
  - septin-record-cvt_vesicle
- assessment_id: septin-cvt_vesicle_lumen-schema
  area: schema
  topic: Original schema/render and unchanged frozen targets
  outcome: supported
  summary: Original native validate/render succeeds with deterministic Markdown and
    matching historical/current target hashes. No record change is needed to refresh
    this assessment.
  target_ids:
  - cellstructuremech:cvt_vesicle_lumen
  evidence_ids:
  - septin-record-cvt_vesicle_lumen
  - septin-original-validation-cvt_vesicle_lumen
- assessment_id: septin-cvt_vesicle_lumen-native-scope
  area: provenance
  topic: Actual empty protein inventory limits
  outcome: supported
  summary: No protein examples or UniProtKB graph xrefs and zero GENE_OR_PROTEIN graph
    nodes. Execution success verifies only this empty represented inventory; it does
    not establish narrative Ape1/Ams1/Atg identity, localization, mechanism, complete
    composition or formation necessity.
  target_ids:
  - cellstructuremech:cvt_vesicle_lumen
  evidence_ids:
  - septin-record-cvt_vesicle_lumen
  - septin-native-cvt_vesicle_lumen-verify
  - septin-native-cvt_vesicle_lumen-causal
- assessment_id: septin-cvt_vesicle_lumen-nonasserted-surfaces
  area: scope
  topic: Images, measurements, traits and snippets
  outcome: not_applicable
  summary: The maintained record asserts none of these optional surfaces. Textual
    primary figure-caption inspection is not pixel inspection or raw-data reanalysis;
    no image-rights attestation is needed for absent target images.
  target_ids:
  - cellstructuremech:cvt_vesicle_lumen
  evidence_ids:
  - septin-record-cvt_vesicle_lumen
- assessment_id: septin-cvt_vesicle_membrane-schema
  area: schema
  topic: Original schema/render and unchanged frozen targets
  outcome: supported
  summary: Original native validate/render succeeds with deterministic Markdown and
    matching historical/current target hashes. No record change is needed to refresh
    this assessment.
  target_ids:
  - GO:0033110
  evidence_ids:
  - septin-record-cvt_vesicle_membrane
  - septin-original-validation-cvt_vesicle_membrane
- assessment_id: septin-cvt_vesicle_membrane-native-scope
  area: provenance
  topic: Actual empty protein inventory limits
  outcome: supported
  summary: No protein examples or UniProtKB graph xrefs and zero GENE_OR_PROTEIN graph
    nodes. Execution success verifies only this empty represented inventory; it does
    not establish narrative Ape1/Ams1/Atg identity, localization, mechanism, complete
    composition or formation necessity.
  target_ids:
  - GO:0033110
  evidence_ids:
  - septin-record-cvt_vesicle_membrane
  - septin-native-cvt_vesicle_membrane-verify
  - septin-native-cvt_vesicle_membrane-causal
- assessment_id: septin-cvt_vesicle_membrane-nonasserted-surfaces
  area: scope
  topic: Images, measurements, traits and snippets
  outcome: not_applicable
  summary: The maintained record asserts none of these optional surfaces. Textual
    primary figure-caption inspection is not pixel inspection or raw-data reanalysis;
    no image-rights attestation is needed for absent target images.
  target_ids:
  - GO:0033110
  evidence_ids:
  - septin-record-cvt_vesicle_membrane
- assessment_id: septin-cvt_vesicle-taxon
  area: scope
  topic: Yeast model and condition-bounded occurrence
  outcome: supported
  summary: ENA validates S.cerevisiae identity. Reggiori and Shintani establish carrier
    context in named budding-yeast strains; COMMON is qualitative, not a measured
    prevalence or a claim of constant visible vesicles in every cell. Nutrient-rich
    Cvt transport, nitrogen-starvation/rapamycin autophagy and temperature-sensitive
    perturbations remain distinct.
  target_ids:
  - GO:0033107
  evidence_ids:
  - septin-record-cvt_vesicle
  - septin-tax4932
  - septin-reggiori2004-pmc-prefixed
  - septin-shintani2004-pmc-prefixed
- assessment_id: septin-cvt_vesicle-adapter
  area: scope
  topic: Actual structured-source applicability and unmatched host
  outcome: not_applicable
  summary: Affirmative Cvt/early-secretory pathway assertions trigger applicability
    inspection even though a graph is nonmechanistic or omits proteins. The complete
    current catalogue lacks a matching S.cerevisiae dataset, so downstream gene/module
    checks are not applicable. Historical runner failure is separate; catalogue noncoverage
    is not negative biology.
  target_ids:
  - GO:0033107
  evidence_ids:
  - septin-record-cvt_vesicle
  - septin-review-policy
  - septin-catalogue
  - septin-historical-adapter-runner
- assessment_id: septin-cvt_vesicle-history
  area: provenance
  topic: Maintained status and original history
  outcome: supported
  summary: PROPOSED status and all prior curation/history text remain unchanged. A
    fresh qualified review neither retrospectively certifies old execution/authorship
    nor terminally resolves historical issue references or the neighbor cargo record.
  target_ids:
  - GO:0033107
  evidence_ids:
  - septin-record-cvt_vesicle
  - septin-original-cvt_vesicle
  - septin-context-cvt_complex
- assessment_id: septin-cvt_vesicle_lumen-taxon
  area: scope
  topic: Yeast model and condition-bounded occurrence
  outcome: supported
  summary: ENA validates S.cerevisiae identity. Reggiori and Shintani establish carrier
    context in named budding-yeast strains; COMMON is qualitative, not a measured
    prevalence or a claim of constant visible vesicles in every cell. Nutrient-rich
    Cvt transport, nitrogen-starvation/rapamycin autophagy and temperature-sensitive
    perturbations remain distinct.
  target_ids:
  - cellstructuremech:cvt_vesicle_lumen
  evidence_ids:
  - septin-record-cvt_vesicle_lumen
  - septin-tax4932
  - septin-reggiori2004-pmc-prefixed
  - septin-shintani2004-pmc-prefixed
- assessment_id: septin-cvt_vesicle_lumen-adapter
  area: scope
  topic: Actual structured-source applicability and unmatched host
  outcome: not_applicable
  summary: Affirmative Cvt/early-secretory pathway assertions trigger applicability
    inspection even though a graph is nonmechanistic or omits proteins. The complete
    current catalogue lacks a matching S.cerevisiae dataset, so downstream gene/module
    checks are not applicable. Historical runner failure is separate; catalogue noncoverage
    is not negative biology.
  target_ids:
  - cellstructuremech:cvt_vesicle_lumen
  evidence_ids:
  - septin-record-cvt_vesicle_lumen
  - septin-review-policy
  - septin-catalogue
  - septin-historical-adapter-runner
- assessment_id: septin-cvt_vesicle_lumen-history
  area: provenance
  topic: Maintained status and original history
  outcome: supported
  summary: PROPOSED status and all prior curation/history text remain unchanged. A
    fresh qualified review neither retrospectively certifies old execution/authorship
    nor terminally resolves historical issue references or the neighbor cargo record.
  target_ids:
  - cellstructuremech:cvt_vesicle_lumen
  evidence_ids:
  - septin-record-cvt_vesicle_lumen
  - septin-original-cvt_vesicle_lumen
  - septin-context-cvt_complex
- assessment_id: septin-cvt_vesicle_membrane-taxon
  area: scope
  topic: Yeast model and condition-bounded occurrence
  outcome: supported
  summary: ENA validates S.cerevisiae identity. Reggiori and Shintani establish carrier
    context in named budding-yeast strains; COMMON is qualitative, not a measured
    prevalence or a claim of constant visible vesicles in every cell. Nutrient-rich
    Cvt transport, nitrogen-starvation/rapamycin autophagy and temperature-sensitive
    perturbations remain distinct.
  target_ids:
  - GO:0033110
  evidence_ids:
  - septin-record-cvt_vesicle_membrane
  - septin-tax4932
  - septin-reggiori2004-pmc-prefixed
  - septin-shintani2004-pmc-prefixed
- assessment_id: septin-cvt_vesicle_membrane-adapter
  area: scope
  topic: Actual structured-source applicability and unmatched host
  outcome: not_applicable
  summary: Affirmative Cvt/early-secretory pathway assertions trigger applicability
    inspection even though a graph is nonmechanistic or omits proteins. The complete
    current catalogue lacks a matching S.cerevisiae dataset, so downstream gene/module
    checks are not applicable. Historical runner failure is separate; catalogue noncoverage
    is not negative biology.
  target_ids:
  - GO:0033110
  evidence_ids:
  - septin-record-cvt_vesicle_membrane
  - septin-review-policy
  - septin-catalogue
  - septin-historical-adapter-runner
- assessment_id: septin-cvt_vesicle_membrane-history
  area: provenance
  topic: Maintained status and original history
  outcome: supported
  summary: PROPOSED status and all prior curation/history text remain unchanged. A
    fresh qualified review neither retrospectively certifies old execution/authorship
    nor terminally resolves historical issue references or the neighbor cargo record.
  target_ids:
  - GO:0033110
  evidence_ids:
  - septin-record-cvt_vesicle_membrane
  - septin-original-cvt_vesicle_membrane
  - septin-context-cvt_complex
- assessment_id: septin-cvt_vesicle-identity
  area: identity
  topic: Whole double-membrane carrier, cargo and bilayers
  outcome: supported
  summary: Exact GO0033107 definition and synonyms, cytoplasmic-vesicle parent and
    SL0080 mapping denote the complete carrier. GO0033110 is either individual bilayer;
    GO0034270 is the protein cargo complex. Whole enclosure is not attributed to a
    single bilayer.
  target_ids:
  - GO:0033107
  evidence_ids:
  - septin-record-cvt_vesicle
  - septin-go
  - septin-SL0080
  - septin-context-cvt_complex
  - septin-reggiori2004-pmc-prefixed
- assessment_id: septin-cvt_vesicle-components
  area: grounding
  topic: Membrane part and incorporated cargo complex
  outcome: supported
  summary: The membrane row denotes a complete structural bilayer part; its LIPID
    type is collective material, not an asserted single lipid species. The Cvt-complex
    constituent is explicitly sequestered cargo, not a coat or a full assembly-machine
    census. GO exact identities and primary cargo inclusion support these bounded
    rows; species-specific complexes and transient actors are not silently conflated.
  target_ids:
  - GO:0033107
  evidence_ids:
  - septin-record-cvt_vesicle
  - septin-curation-policy
  - septin-go
  - septin-shintani2004-pmc-prefixed
- assessment_id: septin-cvt_vesicle-necessity
  area: grounding
  topic: Constitution versus empirical formation necessity
  outcome: unknown
  summary: ESSENTIAL refers to the defining membrane material of the double-membrane
    carrier, not a named phospholipid removal experiment. Cargo UNKNOWN avoids upgrading
    conditional APE1/ATG19 deletion phenotypes into universal formation necessity.
    Molecular requirements and complete stoichiometry are not established by this
    descriptive record.
  target_ids:
  - GO:0033107
  evidence_ids:
  - septin-record-cvt_vesicle
  - septin-curation-policy
  - septin-shintani2004-pmc-prefixed
  - septin-reggiori2004-pmc-prefixed
- assessment_id: septin-cvt_vesicle-function
  area: evidence
  topic: Selective hydrolase cargo delivery
  outcome: supported
  summary: 'GO0032258 and primary studies support selective cytoplasmic hydrolase
    enclosure and eventual fungal-vacuole delivery. Scott directly supports the Cvt19
    receptor/prAPI binding context; Shintani explicitly supplies Atg19/Cvt19 nomenclature.
    The word review in one maintained Shintani note is treated as a verb, not a source-type
    claim: this is a primary experiment.'
  target_ids:
  - GO:0033107
  evidence_ids:
  - septin-record-cvt_vesicle
  - septin-go
  - septin-reggiori2004-pmc-prefixed
  - septin-shintani2004-pmc-prefixed
  - septin-scott2001-pmc-prefixed
  - septin-scott2001-meta
- assessment_id: septin-cvt_vesicle-graph
  area: graph
  topic: Four descriptive edges at carrier scope
  outcome: supported
  summary: Membrane part_of whole carrier, cargo complex enclosed_by whole carrier,
    carrier supports Cvt pathway, and carrier delivers cargo_to fungal vacuole are
    supported. Bulk-cytoplasm exclusion is source-supported selective enclosure; no
    measured exclusion coefficient, universal size or complete receptor/scaffold/fusion
    mechanism is asserted.
  target_ids:
  - GO:0033107
  evidence_ids:
  - septin-record-cvt_vesicle
  - septin-go
  - septin-reggiori2004-pmc-prefixed
  - septin-shintani2004-pmc-prefixed
  - septin-graph-policy
- assessment_id: septin-cvt_vesicle-machinery
  area: completeness
  topic: Explicitly incomplete Atg inventory
  outcome: supported
  summary: The TODO distinguishes unrepresented Atg19/Atg11/Atg8/Atg9 machinery from
    the already represented membrane and cargo complex. The primary papers establish
    named actors and context; exact family uncertainty is not uncertainty that they
    exist. A descriptive carrier record does not assert exhaustive machinery or mechanism,
    and adding all transient actors as constituents would be unjustified. No consequential
    missing-required-representation defect is established in this review.
  target_ids:
  - GO:0033107
  evidence_ids:
  - septin-record-cvt_vesicle
  - septin-curation-policy
  - septin-shintani2004-pmc-prefixed
  - septin-scott2001-pmc-prefixed
  - septin-context-cvt_complex
- assessment_id: septin-cvt_vesicle_lumen-identity
  area: identity
  topic: Positive SL lumen identity with bounded GO candidates
  outcome: supported
  summary: SL0323 directly supports the local Cvt lumen definition, cytoplasmic-vesicle-lumen
    parent and carrier parthood. Bounded current GO candidates did not establish a
    conflicting exact mapping; no exhaustive absence claim is made. The ignored-inclusive
    exact-id search finds one maintained local record.
  target_ids:
  - cellstructuremech:cvt_vesicle_lumen
  evidence_ids:
  - septin-record-cvt_vesicle_lumen
  - septin-SL0323
  - septin-go
  - septin-lumen-search
  - septin-local-identity-search
- assessment_id: septin-cvt_vesicle_lumen-topology
  area: graph
  topic: Two mature-compartment relations
  outcome: supported
  summary: The mature cargo-containing compartment is part of the whole carrier and
    is bounded by its surrounding membrane at the source location scope. This describes
    the interior rather than asserting that either outer bilayer individually directly
    contacts cargo, or equating it with the intermembrane space/post-fusion Cvt body.
    No fusion, receptor/scaffold mechanism or soluble inventory is asserted.
  target_ids:
  - cellstructuremech:cvt_vesicle_lumen
  evidence_ids:
  - septin-record-cvt_vesicle_lumen
  - septin-SL0323
  - septin-go
  - septin-reggiori2004-pmc-prefixed
  - septin-scott2001-pmc-prefixed
  - septin-graph-policy
- assessment_id: septin-cvt_vesicle_lumen-pathway-scope
  area: scope
  topic: Canonical early-secretory requirement without invented molecular steps
  outcome: supported
  summary: The canonical example positively cites early-secretory requirements; Reggiori
    sec12/sec7 results support this condition-bounded pathway context. The graph expressly
    declines the receptor/scaffold/expansion mechanism. Its geometry-focused content
    does not erase that affirmative pathway assertion for adapter applicability.
  target_ids:
  - cellstructuremech:cvt_vesicle_lumen
  evidence_ids:
  - septin-record-cvt_vesicle_lumen
  - septin-reggiori2004-pmc-prefixed
  - septin-review-policy
- assessment_id: septin-cvt_vesicle_lumen-formation
  area: grounding
  topic: No declared molecular necessity
  outcome: not_applicable
  summary: No molecular component or essentiality row is declared in this region record.
    The primary carrier evidence does not establish an independent lumen-assembly
    molecular inventory. No missing optional component row is treated as a defect.
  target_ids:
  - cellstructuremech:cvt_vesicle_lumen
  evidence_ids:
  - septin-record-cvt_vesicle_lumen
  - septin-curation-policy
  - septin-reggiori2004-pmc-prefixed
- assessment_id: septin-cvt_vesicle_membrane-identity
  area: identity
  topic: Either bilayer of the double-membrane carrier
  outcome: supported
  summary: GO0033110 and SL0081 denote either surrounding bilayer, with cytoplasmic-vesicle-membrane
    parentage and Cvt-carrier parthood. The maintained definition and pair-of-membranes
    graph preserve the double-membrane structure.
  target_ids:
  - GO:0033110
  evidence_ids:
  - septin-record-cvt_vesicle_membrane
  - septin-go
  - septin-SL0081
  - septin-reggiori2004-pmc-prefixed
- assessment_id: septin-cvt_vesicle_membrane-material
  area: grounding
  topic: Collective bilayer and limited chemical specificity
  outcome: supported
  summary: The reviewed-label-only LIPID row describes collective bilayer material.
    Its notes and TODO acknowledge that no separate exact chemical constituent was
    curated; the membrane location is not falsely assigned as a molecular lipid identity.
    This review does not establish exhaustive chemical ontology absence or an exact
    species/abundance inventory.
  target_ids:
  - GO:0033110
  evidence_ids:
  - septin-record-cvt_vesicle_membrane
  - septin-curation-policy
  - septin-go
  - septin-SL0081
- assessment_id: septin-cvt_vesicle_membrane-necessity
  area: grounding
  topic: Unresolved individual lipid requirements
  outcome: unknown
  summary: A bilayer is constitutive of the membrane definition, while empirical necessity
    of individual lipids or composition ratios is unassessed. Neither current primary
    article supplies a species-specific lipid removal/substitution assay; logical
    material constitution is not such an assay.
  target_ids:
  - GO:0033110
  evidence_ids:
  - septin-record-cvt_vesicle_membrane
  - septin-go
  - septin-reggiori2004-pmc-prefixed
  - septin-shintani2004-pmc-prefixed
- assessment_id: septin-cvt_vesicle_membrane-function
  area: evidence
  topic: Membrane contribution to selective carrier function
  outcome: supported
  summary: The membrane surrounds the selective hydrolase carrier; it is not described
    as an enzyme or independent receptor. GO0032258 and primary cargo experiments
    support carrier context. A unique ER/Golgi membrane donor is explicitly not inferred
    from early-secretory perturbations.
  target_ids:
  - GO:0033110
  evidence_ids:
  - septin-record-cvt_vesicle_membrane
  - septin-go
  - septin-reggiori2004-pmc-prefixed
  - septin-shintani2004-pmc-prefixed
- assessment_id: septin-cvt_vesicle_membrane-graph
  area: graph
  topic: Three descriptive carrier-context edges
  outcome: supported
  summary: The graph specifies a pair of membranes and only individual membrane parthood,
    enclosure of Cvt complex by the complete vesicle, and carrier participation in
    targeting. Every edge has relevant authority/primary support; it does not collapse
    two bilayers or invent molecular membrane-expansion steps.
  target_ids:
  - GO:0033110
  evidence_ids:
  - septin-record-cvt_vesicle_membrane
  - septin-go
  - septin-SL0081
  - septin-reggiori2004-pmc-prefixed
  - septin-shintani2004-pmc-prefixed
  - septin-graph-policy
- assessment_id: septin-cvt_vesicle-verdict
  area: evidence
  topic: Qualified positive scientific assessment
  outcome: supported
  summary: No concrete scientific curation finding was established in this complete
    assigned-record scope. Original findings/actions were empty and remain so; qualified
    support retains source-body boundaries, incomplete molecular composition, conditional
    experiments, empty native inventories and dataset noncoverage. The identified
    adapter defect belongs to the original review bundle and is corrected through
    a successor.
  target_ids:
  - GO:0033107
  evidence_ids:
  - septin-record-cvt_vesicle
  - septin-original-cvt_vesicle
  - septin-go
  - septin-reggiori2004-pmc-prefixed
  - septin-shintani2004-pmc-prefixed
- assessment_id: septin-cvt_vesicle_lumen-verdict
  area: evidence
  topic: Qualified positive scientific assessment
  outcome: supported
  summary: No concrete scientific curation finding was established in this complete
    assigned-record scope. Original findings/actions were empty and remain so; qualified
    support retains source-body boundaries, incomplete molecular composition, conditional
    experiments, empty native inventories and dataset noncoverage. The identified
    adapter defect belongs to the original review bundle and is corrected through
    a successor.
  target_ids:
  - cellstructuremech:cvt_vesicle_lumen
  evidence_ids:
  - septin-record-cvt_vesicle_lumen
  - septin-original-cvt_vesicle_lumen
  - septin-go
  - septin-reggiori2004-pmc-prefixed
  - septin-SL0323
- assessment_id: septin-cvt_vesicle_membrane-verdict
  area: evidence
  topic: Qualified positive scientific assessment
  outcome: supported
  summary: No concrete scientific curation finding was established in this complete
    assigned-record scope. Original findings/actions were empty and remain so; qualified
    support retains source-body boundaries, incomplete molecular composition, conditional
    experiments, empty native inventories and dataset noncoverage. The identified
    adapter defect belongs to the original review bundle and is corrected through
    a successor.
  target_ids:
  - GO:0033110
  evidence_ids:
  - septin-record-cvt_vesicle_membrane
  - septin-original-cvt_vesicle_membrane
  - septin-go
  - septin-reggiori2004-pmc-prefixed
  - septin-shintani2004-pmc-prefixed
- assessment_id: current-input-comparison
  area: provenance
  topic: Complete frozen-input comparison and bounded refresh
  outcome: supported
  summary: 1 of ten original target hashes differ from current main. The changed content
    is substantively reassessed in the target-specific assessments; original observations
    remain historical and unchanged. All current target and used context bytes are
    frozen.
  target_ids:
  - GO:0033107
  - cellstructuremech:cvt_vesicle_lumen
  - GO:0033110
  - GO:0009842
  - GO:0033112
  - GO:0036012
  - GO:0036014
  - GO:0033113
  - GO:0036013
  - GO:0034060
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
- finding_id: micro-F1
  issue_key: cyanelle-ims-direct-go-parthood-overstatement
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Cyanelle IMS evidence note overstates direct GO parthood
  description: The newly added edge correctly states cyanelle intermembrane space
    is part of the whole cyanelle. However, its evidence note says GO0036014 places
    it as a direct part of GO0009842. The current authority asserts GO0036014 part_of
    GO0033112 (envelope), and GO0033112 part_of GO0009842; the direct stroma relation
    is a separate case. Correct the note to distinguish transitive parthood through
    envelope while retaining the supported anatomical edge.
  target_ids:
  - GO:0009842
  field_paths:
  - causal_graphs[graph_id=cyanelle_envelope_thylakoid_topology].edges[subject=cyanelle_intermembrane_space,object=cyanelle].evidence[reference=GO:0036014].notes
  evidence_ids:
  - micro-record-cyanelle
  - micro-go
  - micro-ims-go-path
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cyanelle.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    standard and causal graph
  native_severity: minor
  normalization_reason: 'Minor bounded provenance wording error: biological IMS parthood
    and record identity remain valid; source does not supply the claimed direct edge.
    New finding on changed content, so no predecessor finding is fabricated.'
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2675
actions:
- action_id: micro-A1
  finding_ids:
  - micro-F1
  target_ids:
  - GO:0009842
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cyanelle.yaml
    role: maintained scientific record
  description: In a separately authorized curation change, revise only the IMS-to-cyanelle
    edge evidence note to say GO supports parthood transitively through GO0033112,
    retaining the biologically valid edge. Recheck live authority paths before editing.
  acceptance_checks:
  - Evidence note distinguishes GO0036014 part_of GO0033112 part_of GO0009842 from
    a direct asserted ontology relationship.
  - Retained anatomical edge is not deleted merely because ontology parthood is transitive.
  - Use guarded validated writer, curation event and repository history in the separate
    curation change; focused native checks pass.
  - No scientific record changes in this review PR.
limitations:
- 'Cyanelle inner membrane, intermembrane space, membrane and outer membrane independent
  subreview: Four assigned targets only, all unchanged from original frozen records.
  No other local scientific record was used as evidence; public native GO/SL sources
  supply compartment boundaries. Historical record corrections/issues are not recertified
  or terminally resolved.'
- 'Cyanelle inner membrane, intermembrane space, membrane and outer membrane independent
  subreview: Fresh Giddings1983 scans409/414/416/417 were independently viewed at
  text and pixel level. These include culture context, envelope Results and Discussion,
  and indicated figures. No other page, entire paper, complete bibliography or raw
  microscopy measurement reanalysis is claimed. Historical presumed PG/LPS chemistry
  and endosymbiont terminology remain historical.'
- 'Cyanelle inner membrane, intermembrane space, membrane and outer membrane independent
  subreview: Pfanzagl1996 primary-structure and PMID8955325 comparative evidence are
  complete primary abstracts plus exact metadata. The comparative PMC HTML is an abstract/PDF
  landing page, not inspected article body. No chemical numeric data or universal
  species/strain composition is inferred.'
- 'Cyanelle inner membrane, intermembrane space, membrane and outer membrane independent
  subreview: Kojima2016 canonical PMC body was read at Abstract/Introduction, Results
  isolation/sequence/channel subsections, complete Discussion, Methods13–21 and liposome
  assay32. Figure captions are text only; no figure pixels, full Table1, supplementary
  data or raw experiment reanalysis. Numeric PMC challenge, S3.1 404 and EuropePMC
  XML500 are distinct failed routes.'
- 'Cyanelle inner membrane, intermembrane space, membrane and outer membrane independent
  subreview: Giddings model is UTEX LB555; Kojima model is NIES547 with paper-specific
  isolation/culture conditions. Reconstituted diffusion assays do not demonstrate
  in-vivo rates or individual formation necessity. COMMON is qualitative anatomy,
  not a prevalence estimate.'
- 'Cyanelle inner membrane, intermembrane space, membrane and outer membrane independent
  subreview: Source locations match exact identities and typed parent/parthood distinctions.
  SL0083 is broader unresolved localization fallback, not an exact generic envelope
  membrane match. Collective bilayer constitutional necessity and IMS PG UNKNOWN essentiality
  remain distinct from requirements for particular molecules.'
- 'Cyanelle inner membrane, intermembrane space, membrane and outer membrane independent
  subreview: All four records are genuine material/topology exclusions under actual
  structured-source triggers. Two omissions and two expression-only N/A sentences
  are not counted as defects absent positive named molecular/pathway/stress/trait
  assertions. No compulsory protein inventory is invented.'
- 'Cyanelle inner membrane, intermembrane space, membrane and outer membrane independent
  subreview: Current full catalogue lacks glaucophyte hosts; no matched downstream
  gene/module query applies and no biological absence follows. The historical00:49Z
  PermissionError runner receipt is retained at its actual time, not a new invocation
  or success.'
- 'Cyanelle inner membrane, intermembrane space, membrane and outer membrane independent
  subreview: All eight native protein commands pass empty inventories and zero typed
  molecular nodes, without proving biological localization, assembly necessity or
  source claims. Root owns global gates, issue handling, immutable successor authoring
  and all repository/GitHub writes.'
- 'Whole cyanelle, envelope and stroma independent subreview: Cyanelle/envelope/stroma
  source slice: Giddings scans actually viewed are pages409,410,412,414,416,417 only;
  remaining printed pages were not read in this fresh audit. No whole-paper, quantitative
  remeasurement or raw-data reanalysis claim.'
- 'Whole cyanelle, envelope and stroma independent subreview: Cyanelle/envelope/stroma
  source slice: Pfanzagl1996 primary-structure evidence and PMID8955325 comparative
  study were read as complete primary abstracts/metadata, not full Methods/Results.
  Their broad material/taxon claims do not establish molecule-specific assembly necessity.'
- 'Whole cyanelle, envelope and stroma independent subreview: Cyanelle/envelope/stroma
  source slice: Kojima canonical body was independently read only at Abstract, Introduction,
  Results first isolation subsection and Methods13–19. Price JATS read at Introduction,
  Methods2.1 and Results3.4/3.5; article figure/supplement references and captions
  are not fresh pixel inspection. Supplied plaque responses retain their actual11:52Z
  fetch times.'
- 'Whole cyanelle, envelope and stroma independent subreview: Cyanelle/envelope/stroma
  source slice: retained historical native adapter failure was00:49Z, not a fresh
  PR2362 run. Current catalogue scope is its returned dataset listing; no matched
  glaucophyte dataset and no downstream gene/module result. Absence is not negative
  biology.'
- 'Whole cyanelle, envelope and stroma independent subreview: Cyanelle/envelope/stroma
  source slice: six current native protein commands pass on empty declared inventories
  / zero GENE_OR_PROTEIN nodes. They do not prove complete protein coverage, identity,
  membership or necessity. Root owns full-corpus gates, issue dedup and CI; this report
  borrows no future CI success.'
- 'Whole cyanelle, envelope and stroma independent subreview: Cyanelle/envelope/stroma
  source slice: reviewed-label-only PG grounding is an explicit scientific unknown;
  bounded GO text search is not universal absence. COMMON is qualitative occurrence,
  not quantitative prevalence. No prior category/neighbor issue is resolved; three
  original finding arrays were empty.'
- 'Cvt vesicle, lumen and membrane independent subreview: All three target hashes
  are unchanged, including comparison with original historical source bytes. Original
  bundle access times and global gate claims remain historical; no prior source snapshot
  is recast as a new fetch.'
- 'Cvt vesicle, lumen and membrane independent subreview: Fresh primary bodies were
  recovered only through PMC-prefixed routes. Shintani2004 scientific main body was
  read completely including text captions; Reggiori2004 was read only at Introduction,
  named strain/pulse-chase Methods, early-secretory Results and sec17 Discussion;
  Scott2001 only at named binding Results, atypical-receptor Discussion and associated
  Methods. No pixels, raw data, movies or independent audit of cited studies.'
- 'Cvt vesicle, lumen and membrane independent subreview: The initial numeric PMC
  routes were verification stubs despite HTTP200. Guessed S3 paths returned404 and
  EuropePMC XML routes500. The guessed catalogue path returned HTML, while the correct
  official API returned data. These access limitations do not mean the recovered papers
  or catalogue are unreadable.'
- 'Cvt vesicle, lumen and membrane independent subreview: GO lumen candidate search
  was first100/page1of7 only; exact SL0323 positively supports the local identity.
  No exhaustive ontology or chemical-family absence is certified. Generic bilayer
  constitution does not establish necessity of an individual lipid species.'
- 'Cvt vesicle, lumen and membrane independent subreview: All six current native protein
  commands returned zero with empty accession inventories and zero typed protein nodes.
  They do not validate narrative Atg/Ape1/Ams1 identity, localization, complete composition,
  molecular mechanism or formation necessity.'
- 'Cvt vesicle, lumen and membrane independent subreview: Cvt/cargo and early-secretory
  pathway assertions trigger source applicability in all three records, including
  lumen canonical-example context despite its mechanism exclusion. Current official
  catalogue lacks a matching yeast dataset. No unrelated downstream query or biological
  absence inference; historical runner PermissionError retains actual00:49Z time and
  is not rerun.'
- 'Cvt vesicle, lumen and membrane independent subreview: COMMON is qualitative. Selected
  yeast strains, nutrient-rich Cvt transport and starvation/rapamycin autophagy remain
  separate; published conditional defects do not establish universal formation requirements
  or an exclusive ER/Golgi membrane donor.'
- 'Cvt vesicle, lumen and membrane independent subreview: The frozen Cvt-complex neighbor
  was read only at declared boundary fields, not its complete scientific inventory.
  No neighbor, group, category, old issue or prior curation decision is terminally
  resolved. Root owns global gates, issue deduplication/publication, repository/GitHub
  writes and final CI/queue checks.'
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
- 'This explicit issue-bearing ten-record cohort follows the native persistence policy.
  Concrete review-bundle defects were observed and filed as #2673 and #2674. One newly
  observed scientific provenance finding has no invented predecessor or terminal disposition;
  the original ten reviews contained no findings.'
- 'Issue #2673 tracks the stale cyanelle target: new history and three topology edges
  connect the intermembrane space and stroma to the cyanelle and locate thylakoids
  within stroma. The successor reassesses the added relations against current GO and
  bounded primary microscopy evidence, retaining actual taxon and experimental scope.'
- 'Issue #2674 tracks four unsupported expression-only applicability exclusions: Cvt
  vesicle, lumen and membrane name pathway or molecular context, and whole cyanelle
  asserts photosynthesis. The six remaining cyanelle records retain genuine material/topology
  exclusions because their full claims do not assert named machinery, regulators or
  physiological-response pathways.'
- Source commit ed8281f2fc915349c8ce429e7103e42b256c0533 is retained by tag review-base/pr2362-current-record-followup-20261103.
- CLAUDE.md is an alias of AGENTS.md; canonical regular AGENTS.md bytes are frozen.
- All 48 used local inputs were frozen before assessment, including Cvt complex as
  a boundary-context neighbor, native configuration, graph/protein policies and verifier
  source. The neighbor is context only, not an additional target or a disposition
  of its findings.
- Fresh and reused public-source snapshots retain actual access dates and inspection
  tiers. Exact authority identity does not independently establish mechanistic action,
  species-wide generalization or assembly necessity.
- All twenty native protein commands returned zero on empty represented protein inventories
  and zero typed GENE_OR_PROTEIN graph nodes. They do not validate narrative Atg/Ape1/Ams1
  assertions, photosynthetic machinery, protein localization or source scope.
- Named pathway context in the Cvt lumen still triggers applicability assessment even
  though direct molecular mechanism is withheld. Genuine cyanelle boundary/material
  exclusions do not become defects merely because their prior applicability row was
  absent or expressed narrowly.
- 'A new minor finding concerns the stale cyanelle edge evidence note, which calls
  the GO intermembrane-space-to-cyanelle relation direct although current authority
  gives transitive parthood through the envelope. The biological edge remains supported.
  The note correction stays in a separate record-curation issue #2675; nine other
  targets retain qualified positive scientific assessments. No record is edited.'
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T010353Z-cvt-vesicle-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T010357Z-cvt-vesicle-lumen-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T010402Z-cvt-vesicle-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T010406Z-cyanelle-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T010409Z-cyanelle-envelope-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T010413Z-cyanelle-inner-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T010416Z-cyanelle-intermembrane-space-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T010419Z-cyanelle-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T010421Z-cyanelle-outer-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T010425Z-cyanelle-stroma-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
links:
- https://github.com/CultureBotAI/CellStructureMech/pull/2362
- https://github.com/CultureBotAI/CellStructureMech/issues/2514
- https://github.com/CultureBotAI/CellStructureMech/issues/2673
- https://github.com/CultureBotAI/CellStructureMech/issues/2674
- https://github.com/CultureBotAI/CellStructureMech/issues/2675
```
