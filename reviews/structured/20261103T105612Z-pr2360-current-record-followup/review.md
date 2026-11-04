# PR 2360: current-input review of ten records and adversarial follow-up

- Review: 20261103T105612Z-pr2360-current-record-followup
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-11-03T10:48:58.638483Z
- Finished UTC: 2026-11-03T10:56:12Z
- Reviewer: Codex root synthesis with three independent read-only adversarial reviewers (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Current-input reassessment of all ten records in PR2360. All original target hashes remain current. Independent source assessments retain three inherited scientific findings and correct nine structured-source applicability assessments without editing records.

## Scope And Provenance

Exact ten-record PR cohort reassessed against current main 715c37405da56c249de0afa236041f70bdbc399f. Changed inputs are substantively reassessed. Scientific records remain unchanged.

Selection: Complete cohort of ten maintained records reviewed in original PR head 652ff606a49dc8a55b0911b71b875818fceea691.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base cee44c9b340b36e4e103ebd16c4bfcf6745bd41f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0033106 | data/structures/membrane_organelle/cis_golgi_network_membrane.yaml | maintained | cis-Golgi network membrane |
| GO:0045334 | data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle.yaml | maintained | clathrin-coated endocytic vesicle |
| GO:0106176 | data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_lumen.yaml | maintained | clathrin-coated endocytic vesicle lumen |
| GO:0030669 | data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_membrane.yaml | maintained | clathrin-coated endocytic vesicle membrane |
| GO:0030136 | data/structures/membrane_organelle/clathrin_coated_vesicle.yaml | maintained | clathrin-coated vesicle |
| cellstructuremech:clathrin_coated_vesicle_lumen | data/structures/membrane_organelle/clathrin_coated_vesicle_lumen.yaml | maintained | clathrin-coated vesicle lumen |
| GO:0030665 | data/structures/membrane_organelle/clathrin_coated_vesicle_membrane.yaml | maintained | clathrin-coated vesicle membrane |
| GO:0030135 | data/structures/membrane_organelle/coated_vesicle.yaml | maintained | coated vesicle |
| GO:0030662 | data/structures/membrane_organelle/coated_vesicle_membrane.yaml | maintained | coated vesicle membrane |
| cellstructuremech:coccolith_vesicle | data/structures/membrane_organelle/coccolith_vesicle.yaml | maintained | coccolith vesicle |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full native QC | passed | True | GO:0033106, GO:0045334, GO:0106176, GO:0030669, GO:0030136, cellstructuremech:clathrin_coated_vesicle_lumen, GO:0030665, GO:0030135, GO:0030662, cellstructuremech:coccolith_vesicle | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| Native label correspondence | passed | True | GO:0033106, GO:0045334, GO:0106176, GO:0030669, GO:0030136, cellstructuremech:clathrin_coated_vesicle_lumen, GO:0030665, GO:0030135, GO:0030662, cellstructuremech:coccolith_vesicle | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| TraitMech references | passed | True | GO:0033106, GO:0045334, GO:0106176, GO:0030669, GO:0030136, cellstructuremech:clathrin_coated_vesicle_lumen, GO:0030665, GO:0030135, GO:0030662, cellstructuremech:coccolith_vesicle | Native TraitMech link check passed. |
| Pinned governed files | passed | True | GO:0033106, GO:0045334, GO:0106176, GO:0030669, GO:0030136, cellstructuremech:clathrin_coated_vesicle_lumen, GO:0030665, GO:0030135, GO:0030662, cellstructuremech:coccolith_vesicle | Pinned governed files match; native vendored check passed. |
| Native identifier resolver | passed | True | GO:0033106, GO:0045334, GO:0106176, GO:0030669, GO:0030136, cellstructuremech:clathrin_coated_vesicle_lumen, GO:0030665, GO:0030135, GO:0030662, cellstructuremech:coccolith_vesicle | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| validate GO:0033106 | passed | True | GO:0033106 | Documented focused command passed. |
| validate-strict GO:0033106 | passed | True | GO:0033106 | Documented focused command passed. |
| validate GO:0045334 | passed | True | GO:0045334 | Documented focused command passed. |
| validate-strict GO:0045334 | passed | True | GO:0045334 | Documented focused command passed. |
| validate GO:0106176 | passed | True | GO:0106176 | Documented focused command passed. |
| validate-strict GO:0106176 | passed | True | GO:0106176 | Documented focused command passed. |
| validate GO:0030669 | passed | True | GO:0030669 | Documented focused command passed. |
| validate-strict GO:0030669 | passed | True | GO:0030669 | Documented focused command passed. |
| validate GO:0030136 | passed | True | GO:0030136 | Documented focused command passed. |
| validate-strict GO:0030136 | passed | True | GO:0030136 | Documented focused command passed. |
| validate cellstructuremech:clathrin_coated_vesicle_lumen | passed | True | cellstructuremech:clathrin_coated_vesicle_lumen | Documented focused command passed. |
| validate-strict cellstructuremech:clathrin_coated_vesicle_lumen | passed | True | cellstructuremech:clathrin_coated_vesicle_lumen | Documented focused command passed. |
| validate GO:0030665 | passed | True | GO:0030665 | Documented focused command passed. |
| validate-strict GO:0030665 | passed | True | GO:0030665 | Documented focused command passed. |
| validate GO:0030135 | passed | True | GO:0030135 | Documented focused command passed. |
| validate-strict GO:0030135 | passed | True | GO:0030135 | Documented focused command passed. |
| validate GO:0030662 | passed | True | GO:0030662 | Documented focused command passed. |
| validate-strict GO:0030662 | passed | True | GO:0030662 | Documented focused command passed. |
| validate cellstructuremech:coccolith_vesicle | passed | True | cellstructuremech:coccolith_vesicle | Documented focused command passed. |
| validate-strict cellstructuremech:coccolith_vesicle | passed | True | cellstructuremech:coccolith_vesicle | Documented focused command passed. |
| Supplemental bounded PMID authority checks | passed | True | GO:0033106, GO:0045334, GO:0106176, GO:0030669, GO:0030136, cellstructuremech:clathrin_coated_vesicle_lumen, GO:0030665, GO:0030135, GO:0030662, cellstructuremech:coccolith_vesicle | 909 PMIDs all OK in bounded native requests; full-command limitations remain separate. |
| Official structured-source applicability and covered-dataset cross-checks | passed | False | GO:0033106, GO:0045334, GO:0106176, GO:0030669, GO:0030136, cellstructuremech:clathrin_coated_vesicle_lumen, GO:0030665, GO:0030135, GO:0030662, cellstructuremech:coccolith_vesicle | Nine applicability defects are corrected: the omitted assessment for cis-Golgi network membrane and eight unsupported expression-only exclusions across clathrin-coated endocytic vesicle/lumen/membrane, generic clathrin-coated vesicle/lumen/membrane, coated vesicle and coated vesicle membrane. Both clathrin lumens have explicit molecular recruitment narratives. Coccolith vesicle remains a genuine exclusion because its supported claims are morphological and unresolved ATPase/transport identities are explicitly withheld. Actual complete catalogue coverage has no matched relevant yeast or coccolithophore dataset. No unrelated organism dataset or downstream module query substitutes for noncoverage. Resource noncoverage is not biological absence; retained historical runner failure is not a fresh invocation. |
| Independent claim-level source review | passed | True | GO:0033106, GO:0045334, GO:0106176, GO:0030669, GO:0030136, cellstructuremech:clathrin_coated_vesicle_lumen, GO:0030665, GO:0030135, GO:0030662, cellstructuremech:coccolith_vesicle | Three read-only reviewers covered the complete ten-record cohort, including changed inputs, with explicit scientific findings and source-access limits. Final artifact/head acceptance occurs after saving. |
| Retained historical adapter runner availability | unavailable | False | GO:0033106, GO:0045334, GO:0106176, GO:0030669, GO:0030136, cellstructuremech:clathrin_coated_vesicle_lumen, GO:0030665, GO:0030135, GO:0030662 | Historical 00:49Z invocation unavailable due to OS access restriction. Official catalogue source fallback was inspected separately; no current invocation or successful adapter execution is claimed. The actual historical exit code 1 is retained in the evidence receipt, since the native unavailable-check model has no execution exit-code field. |
| Native cis golgi network membrane UniProt verify check | passed | True | GO:0033106 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native cis golgi network membrane UniProt causal check | passed | True | GO:0033106 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native clathrin coated endocytic vesicle UniProt verify check | passed | True | GO:0045334 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native clathrin coated endocytic vesicle UniProt causal check | passed | True | GO:0045334 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native clathrin coated endocytic vesicle lumen UniProt verify check | passed | True | GO:0106176 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native clathrin coated endocytic vesicle lumen UniProt causal check | passed | True | GO:0106176 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native clathrin coated endocytic vesicle membrane UniProt verify check | passed | True | GO:0030669 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native clathrin coated endocytic vesicle membrane UniProt causal check | passed | True | GO:0030669 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native clathrin coated vesicle UniProt verify check | passed | True | GO:0030136 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native clathrin coated vesicle UniProt causal check | passed | True | GO:0030136 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native clathrin coated vesicle lumen UniProt verify check | passed | True | cellstructuremech:clathrin_coated_vesicle_lumen | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native clathrin coated vesicle lumen UniProt causal check | passed | True | cellstructuremech:clathrin_coated_vesicle_lumen | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native clathrin coated vesicle membrane UniProt verify check | passed | True | GO:0030665 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native clathrin coated vesicle membrane UniProt causal check | passed | True | GO:0030665 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native coated vesicle UniProt verify check | passed | True | GO:0030135 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native coated vesicle UniProt causal check | passed | True | GO:0030135 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native coated vesicle membrane UniProt verify check | passed | True | GO:0030662 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native coated vesicle membrane UniProt causal check | passed | True | GO:0030662 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native coccolith vesicle UniProt verify check | passed | True | cellstructuremech:coccolith_vesicle | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native coccolith vesicle UniProt causal check | passed | True | cellstructuremech:coccolith_vesicle | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |

## Scientific And Domain Assessments

### Native protein inventories and exact graph xrefs

schema: supported. Targets: GO:0030136.

Both commands pass with no explicit protein examples or typed protein nodes. This validates represented empty inventories, not narrative molecular claims or mechanistic necessity.

### Immutable original review and current target hashes

provenance: supported. Targets: GO:0030136.

Original validate/render and all historical input hashes pass; current target is byte-identical to the frozen record. No scientific finding exists to terminally resolve. Historical record issue numbers remain context only.

### Complete target with bounded source review

completeness: supported. Targets: GO:0030136.

All maintained fields were read and claim-bearing evidence assessed at declared tiers. Optional inventories, additional figures, detailed quantitative properties and causal mechanisms are not required. No concrete record-curation defect was established; bundle applicability corrections are separate.

### Native protein inventories and exact graph xrefs

schema: supported. Targets: cellstructuremech:clathrin_coated_vesicle_lumen.

Both commands pass with no explicit protein examples or typed protein nodes. This validates represented empty inventories, not narrative molecular claims or mechanistic necessity.

### Immutable original review and current target hashes

provenance: supported. Targets: cellstructuremech:clathrin_coated_vesicle_lumen.

Original validate/render and all historical input hashes pass; current target is byte-identical to the frozen record. No scientific finding exists to terminally resolve. Historical record issue numbers remain context only.

### Complete target with bounded source review

completeness: supported. Targets: cellstructuremech:clathrin_coated_vesicle_lumen.

All maintained fields were read and claim-bearing evidence assessed at declared tiers. Optional inventories, additional figures, detailed quantitative properties and causal mechanisms are not required. No concrete record-curation defect was established; bundle applicability corrections are separate.

### Native protein inventories and exact graph xrefs

schema: supported. Targets: GO:0030665.

Both commands pass with no explicit protein examples or typed protein nodes. This validates represented empty inventories, not narrative molecular claims or mechanistic necessity.

### Immutable original review and current target hashes

provenance: supported. Targets: GO:0030665.

Original validate/render and all historical input hashes pass; current target is byte-identical to the frozen record. No scientific finding exists to terminally resolve. Historical record issue numbers remain context only.

### Complete target with bounded source review

completeness: supported. Targets: GO:0030665.

All maintained fields were read and claim-bearing evidence assessed at declared tiers. Optional inventories, additional figures, detailed quantitative properties and causal mechanisms are not required. No concrete record-curation defect was established; bundle applicability corrections are separate.

### Native protein inventories and exact graph xrefs

schema: supported. Targets: cellstructuremech:coccolith_vesicle.

Both commands pass with no explicit protein examples or typed protein nodes. This validates represented empty inventories, not narrative molecular claims or mechanistic necessity.

### Immutable original review and current target hashes

provenance: supported. Targets: cellstructuremech:coccolith_vesicle.

Original validate/render and all historical input hashes pass; current target is byte-identical to the frozen record. No scientific finding exists to terminally resolve. Historical record issue numbers remain context only.

### Complete target with bounded source review

completeness: supported. Targets: cellstructuremech:coccolith_vesicle.

All maintained fields were read and claim-bearing evidence assessed at declared tiers. Optional inventories, additional figures, detailed quantitative properties and causal mechanisms are not required. No concrete record-curation defect was established; bundle applicability corrections are separate.

### Whole vesicle, lumen and membrane remain distinct

identity: supported. Targets: GO:0030136.

GO0030136 and SL0070 denote the whole coated vesicle, not its coat or bilayer. Coated-vesicle is_a parent and membrane/coat parthood are supported. The exact CCV synonym is verified.

### Yeast occurrence and recruitment context

scope: supported. Targets: GO:0030136.

Current taxonomy verifies S.cerevisiae4932. Fresh Newpher primary body supports heavy/light-chain and adaptor dynamics at cortical yeast endocytic sites under the actual fluorescent-reporter/mutant conditions. COMMON is qualitative context, not a census or universal state assertion. Lumen/bilayer existence combines exact compartment definitions with the established yeast vesicle context; the study does not directly image a sealed lumen.

### Constitution, recruitment and formation necessity

evidence: unknown. Targets: GO:0030136.

No individual protein or lipid species is asserted essential to forming these target structures. The membrane record uses ESSENTIAL for its defining collective bilayer, not a measured dependency on a particular molecule. Newpher recruitment/turnover and Kaksonen deletion effects must not be upgraded to universal vesicle-assembly necessity.

### Actual named-molecule applicability

scope: supported. Targets: GO:0030136.

All three records explicitly name heavy/light chains and adaptor recruitment in their yeast taxon/example narratives, including the sparse lumen target. Lack of expression claims alone was therefore an unsupported original N/A rationale. The fresh complete catalogue has no S.cerevisiae dataset; no unrelated-organism gene/module query applies and no biological absence follows. Historical runner failure remains separately dated.

### Primary body versus abstract and access failures

provenance: supported. Targets: GO:0030136.

Newpher genuine primary PDF pp87–96 was inspected including Methods and its explicit pre-budding uncoating versus coated-vesicle departure uncertainty. Kaksonen is used at complete-primary-abstract tier only; native challenge/metadata responses are not bodies. No clathrin source figure pixels, movies or raw data were analyzed.

### Whole vesicle, lumen and membrane remain distinct

identity: supported. Targets: cellstructuremech:clathrin_coated_vesicle_lumen.

The local identity follows exact SL0319 lumen definition and synonym. Cytoplasmic-vesicle-lumen is the broader parent and whole clathrin vesicle the partOf host. Bounded GO search returns narrower endocytic and transmitter-specific lumina, which cannot replace this broader identity.

### Yeast occurrence and recruitment context

scope: supported. Targets: cellstructuremech:clathrin_coated_vesicle_lumen.

Current taxonomy verifies S.cerevisiae4932. Fresh Newpher primary body supports heavy/light-chain and adaptor dynamics at cortical yeast endocytic sites under the actual fluorescent-reporter/mutant conditions. COMMON is qualitative context, not a census or universal state assertion. Lumen/bilayer existence combines exact compartment definitions with the established yeast vesicle context; the study does not directly image a sealed lumen.

### Constitution, recruitment and formation necessity

evidence: unknown. Targets: cellstructuremech:clathrin_coated_vesicle_lumen.

No individual protein or lipid species is asserted essential to forming these target structures. The membrane record uses ESSENTIAL for its defining collective bilayer, not a measured dependency on a particular molecule. Newpher recruitment/turnover and Kaksonen deletion effects must not be upgraded to universal vesicle-assembly necessity.

### Actual named-molecule applicability

scope: supported. Targets: cellstructuremech:clathrin_coated_vesicle_lumen.

All three records explicitly name heavy/light chains and adaptor recruitment in their yeast taxon/example narratives, including the sparse lumen target. Lack of expression claims alone was therefore an unsupported original N/A rationale. The fresh complete catalogue has no S.cerevisiae dataset; no unrelated-organism gene/module query applies and no biological absence follows. Historical runner failure remains separately dated.

### Primary body versus abstract and access failures

provenance: supported. Targets: cellstructuremech:clathrin_coated_vesicle_lumen.

Newpher genuine primary PDF pp87–96 was inspected including Methods and its explicit pre-budding uncoating versus coated-vesicle departure uncertainty. Kaksonen is used at complete-primary-abstract tier only; native challenge/metadata responses are not bodies. No clathrin source figure pixels, movies or raw data were analyzed.

### Whole vesicle, lumen and membrane remain distinct

identity: supported. Targets: GO:0030665.

Exact GO0030665/SL0071 identify the lipid-bilayer membrane; coated-vesicle/cytoplasmic-vesicle membrane parents are is_a and the whole vesicle is the parthood host. Synonym and active source identity agree.

### Yeast occurrence and recruitment context

scope: supported. Targets: GO:0030665.

Current taxonomy verifies S.cerevisiae4932. Fresh Newpher primary body supports heavy/light-chain and adaptor dynamics at cortical yeast endocytic sites under the actual fluorescent-reporter/mutant conditions. COMMON is qualitative context, not a census or universal state assertion. Lumen/bilayer existence combines exact compartment definitions with the established yeast vesicle context; the study does not directly image a sealed lumen.

### Constitution, recruitment and formation necessity

evidence: unknown. Targets: GO:0030665.

No individual protein or lipid species is asserted essential to forming these target structures. The membrane record uses ESSENTIAL for its defining collective bilayer, not a measured dependency on a particular molecule. Newpher recruitment/turnover and Kaksonen deletion effects must not be upgraded to universal vesicle-assembly necessity.

### Actual named-molecule applicability

scope: supported. Targets: GO:0030665.

All three records explicitly name heavy/light chains and adaptor recruitment in their yeast taxon/example narratives, including the sparse lumen target. Lack of expression claims alone was therefore an unsupported original N/A rationale. The fresh complete catalogue has no S.cerevisiae dataset; no unrelated-organism gene/module query applies and no biological absence follows. Historical runner failure remains separately dated.

### Primary body versus abstract and access failures

provenance: supported. Targets: GO:0030665.

Newpher genuine primary PDF pp87–96 was inspected including Methods and its explicit pre-budding uncoating versus coated-vesicle departure uncertainty. Kaksonen is used at complete-primary-abstract tier only; native challenge/metadata responses are not bodies. No clathrin source figure pixels, movies or raw data were analyzed.

### Coat constituents owned by the coat record

grounding: supported. Targets: GO:0030136.

The whole vesicle represents coat and membrane as structural parts. Frozen coat boundary/component-label context confirms separate heavy/light-chain entries; duplicating them as direct whole-vesicle components is unnecessary. No independent coat protein-accession reassessment is inferred.

### Clathrin-dependent endocytic uptake

evidence: supported. Targets: GO:0030136.

The broad uptake function and participates_in edge are supported by GO0072583 and primary yeast endocytic studies. The function is not exclusive to all clathrin trafficking or a claim that clathrin is necessary for every vesicle. Kaksonen abstract explicitly distinguishes initiation effects from invagination/vesicle-formation necessity.

### Descriptive coat/membrane parthood and uptake

graph: supported. Targets: GO:0030136.

All three edges are descriptive: coat partOf whole, membrane partOf whole and vesicle participation in uptake. NONMECHANISTIC scope appropriately excludes actin scission, adaptor dependency and unsupported cargo mechanism.

### Lumen as enclosed region

grounding: supported. Targets: cellstructuremech:clathrin_coated_vesicle_lumen.

The lumen has no compulsory protein or cargo inventory. It is spatially bounded, not equated with the bounding membrane or external coat. Molecular recruitment remains taxonomic context rather than a lumen constituent assertion.

### Boundary and parthood without mechanism

graph: supported. Targets: cellstructuremech:clathrin_coated_vesicle_lumen.

Two NONMECHANISTIC edges represent lumen partOf whole and membrane bounds lumen, directly supported by SL0319 and exact whole/membrane identities. No scission, sorting or lumen-wide composition is asserted.

### Collective lipid material and coat distinction

grounding: supported. Targets: GO:0030665.

The reviewed-label-only lipid bilayer is a collective material, not an exact single chemical species. The existing grounding TODO does not prove a missing exact chemical CURIE. Ontology coat association/parthood is distinct from claiming clathrin is itself lipid-bilayer material.

### Membrane surrounds and is part of whole vesicle

graph: supported. Targets: GO:0030665.

The two NONMECHANISTIC edges describe membrane parthood and the source-defined surrounding boundary. GO/SL explicitly define this membrane as surrounding a clathrin-coated vesicle; the graph does not assert an origin, closure kinetics or individual budding machinery. The mutual lumen target separately models the bounded internal region.

### Intracellular formation compartment versus mineral products

identity: supported. Targets: cellstructuremech:coccolith_vesicle.

The source-defined local coccolith vesicle encloses developing mineral and is distinct from a coccolith scale, external coccosphere and separate Ca/P store. GO0043231 remains broader parent. Current bounded searches have zero coccolith/coccolithogenesis hits without recertifying historical exhaustive searches.

### Exact species and culture strains

scope: supported. Targets: cellstructuremech:coccolith_vesicle.

Native taxonomy verifies C.leptoporus127549 and E.huxleyi2903, with Gephyrocapsa huxleyi a synonym. Primary culture methods explicitly identify RCC1130 and AWI1516. The maintained observations stay within their experimental species/strains and do not impose population prevalence or universal life-cycle occurrence.

### Observed bounding membrane with unresolved machinery

grounding: supported. Targets: cellstructuremech:coccolith_vesicle.

The OTHER component is a structural membrane grounded to GO0016020, with UNKNOWN assembly essentiality. Direct microscopy supports the boundary; neither observed densities, a716-particle average nor resemblance to ATPase establish an exact protein constituent or molecular formation requirement. Calcite/baseplate remain cargo, not demonstrated vesicle-building proteins.

### Site of crystal formation with mechanistic limits

evidence: supported. Targets: cellstructuremech:coccolith_vesicle.

The primary studies support a membrane-confined environment for intracellular calcite growth. Source-informed caveats retain uncertain local growth inhibition, transport and membrane-shaping mechanisms. Separate storage apposition does not prove continuity/ion transfer. No mechanism graph is needed for this observational record.

### Native pixels, caption, microscopy and licence

provenance: supported. Targets: cellstructuremech:coccolith_vesicle.

The frozen700x418 image was viewed and exactly matches the fresh source bytes. PanelA is schematic, B is high-pressure-freeze/fracture cryo-SEM, C/D and E are cryo-FIB-SEM slices/reconstructions. Five stages are not one time-lapse. RCC1130, selective external decalcification before FIB, author attribution and exact CC-BY4.0 ALI URL agree with the record. No raw volumes or Figure3/4 pixels were reanalyzed.

### Genuine morphology/material applicability exclusion

scope: not_applicable. Targets: cellstructuremech:coccolith_vesicle.

This record asserts observed membrane morphology and mineralization-site function. ATPase identity, transport machinery and cytoskeletal constituents are explicitly withheld, not positive molecular/pathway assignments. No represented accession, regulator or gene supports a matched module query. The original N/A outcome is retained with this concrete scope rationale, not counted as a defect merely because its earlier sentence mentioned no expression inference. Fresh catalogue also has no coccolithophore host. No molecular inventory or downstream query is invented.

### Exact membrane identity and boundary

identity: supported. Targets: GO:0033106.

Exact GO:0033106 defines the lipid bilayer around CGN compartments, with exact synonym. Broader Golgi membrane and parthood in CGN are appropriate boundary relations. Frozen neighbors distinguish whole CGN and Golgi from this membrane.

### Inherited F1: current experimental taxon

scope: concern. Targets: GO:0033106.

Retained Rossanese primary source uses PPY1/isogenic PPY12; actual ATCC reidentification and ENA LC815816 qualifiers identify PPY12 as K. phaffii460519. Current occurrence/example retain K. pastoris4922. Both valid taxon IDs do not make the experimentally assigned one correct. Preserve the exact membrane-specific major finding.

### Inherited F2: stack study versus CGN membrane

evidence: concern. Targets: GO:0033106.

Rossanese identifies coherent Golgi stacks and tER interface, not a distinct CGN membrane. CGN is not the Golgi stack in native GO. Cho Sed5 fraction concerns S. cerevisiae early-Golgi membranes and does not fill this particular species/compartment evidence gap. Species correction alone cannot repair the membrane-specific occurrence/example; absence of CGN is not inferred.

### Collective lipid material and excluded molecular residents

completeness: supported. Targets: GO:0033106.

Generic bilayer material is a valid reviewed-label-only constituent; no exact single lipid or universal protein inventory is asserted. Sed5/COPII are explicitly discussed as trafficking/localization context, not constitutive lipid material. Collective boundary constitution does not prove formation necessity of individual molecular species.

### Three NONMECHANISTIC topology edges

graph: supported. Targets: GO:0033106.

Membrane bounds CGN, CGN part of Golgi and CGN abuts ER are supported as generic authority topology. Here the component-linked node denotes the membrane explicitly defined as lipid bilayer; unlike the neighboring whole-network node, it does not identify the full compartment with a lipid constituent. Rossanese supplies broader adjacency context only.

### Original applicability omission

scope: concern. Targets: GO:0033106.

The original omitted applicability despite its actual Sed5-positive compartment and COPII evidence assessment. Fresh catalogue contains no matching yeast organism/dataset; no downstream query is invented. This corrects review coverage without adding membrane constituents.

### Unchanged inputs and native checks

schema: supported. Targets: GO:0033106.

Original pair validates/renders and target hash remains current. Six current slice protein receipts were inspected; this membrane has empty protein inventory/zero protein nodes, so no molecular completeness or occurrence is certified by their success.

### Exact two-finding lineage and verdict

provenance: concern. Targets: GO:0033106.

Maintain original20261021T111327Z-cis-golgi-network-membrane-audit/F1 and/F2 as open confirmed major findings with exact separate membrane issue keys. Current needs_curation does not resolve or conflate prior whole-network issues or category findings.

### Whole vesicle, membrane and subtype boundaries

identity: supported. Targets: GO:0030135.

Active exact GO definitions preserve the broad coated vesicle and its lipid-bilayer boundary. Clathrin/COPI/COPII are subtype examples rather than whole-class synonyms. Generic coat and subtype coat neighbors were read only for boundary/component-label context.

### Species occurrence and experimental example

scope: supported. Targets: GO:0030135.

Barlowe complete primary abstract supports yeast ER-derived COPII budding. Fresh Matsuoka primary text directly compares native ER-microsome-derived and synthetic-liposome vesicles; RSY445 is explicit. Whole-vesicle native-ER and membrane synthetic-liposome exemplars are both source-supported. COMMON is qualitative model context, not quantified prevalence; S288C protein exemplars are not automatically the experimental strain.

### Constituents, necessary material and heterogeneous coats

completeness: supported. Targets: GO:0030135.

Generic lipid bilayer is constitutional material, not proof that each chemical species is necessary. The parent coat class spans distinct clathrin/COPI/COPII complexes; subtype-specific inventories are intentionally kept separate. No single family should ground the heterogeneous parent cohort. Specific coat-protein essentiality is not inferred from bounded reconstitution.

### Inherited RET1 ambiguity with correct representative

grounding: concern. Targets: GO:0030135.

Fresh reviewed exact RET1/taxon559292 query returns P22276 RNA-polymerase-III RET1 and P53622 coatomer alpha primary COP1/RET1 synonym. COP1 query returns only P53622. The record role already calls it representative, but the attached note still says single reviewed RET1 entry. Preserve minor F1, accession, taxon and representative identity; current search does not reconstruct historical results.

### Six reviewed protein examples and family scope

grounding: supported. Targets: GO:0030135.

Six accessions match the declared yeast symbols and S288C reviewed status; CHC1/CLC1/SEC13/SEC31/SEC26/COP1 queries each return the declared single entry currently. InterPro entries identify distinct constituent families and broad domains, not a universal coat family or proof every subtype has all six proteins.

### Experimental context and protein annotation scopes

evidence: supported. Targets: GO:0030135.

Newpher supports yeast clathrin context but diffraction-limited puncta are not all proven mature vesicles. Yu supplies a mammalian-complex/human-and-yeast-Arf1 recruitment model, not accession-specific yeast experiments. SEC13 nuclear-pore and SEC26 Golgi-membrane citations are accurately labeled annotation provenance, not relabeled direct vesicle-membership evidence.

### Five descriptive coat/membrane/budding/transport edges

graph: supported. Targets: GO:0030135.

Assemble-into, parthood, direction-neutral pinching off and vesicle-mediated transport are supported at explicit NONMECHANISTIC parent scope. No universal adaptor, donor membrane, budding direction or complete scission mechanism is asserted. Coat material and the surrounding bilayer remain distinct.

### Correct unsupported expression-only applicability exclusion

scope: concern. Targets: GO:0030135.

Original N/A rationale rests only on no transcriptomic inference despite explicit Sar1/Sec coat machinery and COPII reconstitution (plus protein examples/transport pathway on the whole record). Current source-policy trigger applies; full catalogue lacks matching yeast datasets. No unrelated organism module search or biological absence claim is introduced.

### Frozen original and native identity/coverage checks

schema: supported. Targets: GO:0030135.

Original pair validates/renders and target remains byte-identical. Whole coated vesicle has six examples and one COVERED protein node; membrane has empty inventory and zero protein nodes. These documented successes do not certify scientific uniqueness wording, localization or formation necessity.

### Current verdict and scoped lineage

provenance: concern. Targets: GO:0030135.

Preserve exact original20261021T111333Z-coated-vesicle-audit/F1 and stable minor key; needs_curation is the query-note defect only.

### Whole vesicle, membrane and subtype boundaries

identity: supported. Targets: GO:0030662.

Active exact GO definitions preserve the broad coated vesicle and its lipid-bilayer boundary. Clathrin/COPI/COPII are subtype examples rather than whole-class synonyms. Generic coat and subtype coat neighbors were read only for boundary/component-label context.

### Species occurrence and experimental example

scope: supported. Targets: GO:0030662.

Barlowe complete primary abstract supports yeast ER-derived COPII budding. Fresh Matsuoka primary text directly compares native ER-microsome-derived and synthetic-liposome vesicles; RSY445 is explicit. Whole-vesicle native-ER and membrane synthetic-liposome exemplars are both source-supported. COMMON is qualitative model context, not quantified prevalence; S288C protein exemplars are not automatically the experimental strain.

### Constituents, necessary material and heterogeneous coats

completeness: supported. Targets: GO:0030662.

Generic lipid bilayer is constitutional material, not proof that each chemical species is necessary. The parent coat class spans distinct clathrin/COPI/COPII complexes; subtype-specific inventories are intentionally kept separate. No single family should ground the heterogeneous parent cohort. Specific coat-protein essentiality is not inferred from bounded reconstitution.

### Three membrane and coat topology relations

graph: supported. Targets: GO:0030662.

Membrane part_of vesicle, coat part_of membrane and membrane bounds vesicle are supported by exact current GO relations/definition. GO:0030662 explicitly lists vesicle coat as part_of; generic coat protein material need not be duplicated as molecular lipid-bilayer components. NONMECHANISTIC scope remains coherent.

### Correct unsupported expression-only applicability exclusion

scope: concern. Targets: GO:0030662.

Original N/A rationale rests only on no transcriptomic inference despite explicit Sar1/Sec coat machinery and COPII reconstitution (plus protein examples/transport pathway on the whole record). Current source-policy trigger applies; full catalogue lacks matching yeast datasets. No unrelated organism module search or biological absence claim is introduced.

### Frozen original and native identity/coverage checks

schema: supported. Targets: GO:0030662.

Original pair validates/renders and target remains byte-identical. Whole coated vesicle has six examples and one COVERED protein node; membrane has empty inventory and zero protein nodes. These documented successes do not certify scientific uniqueness wording, localization or formation necessity.

### Current verdict and scoped lineage

provenance: supported. Targets: GO:0030662.

Original20261021T111334Z-coated-vesicle-membrane-audit had no scientific finding. Current pass_with_limitations retains positive source assessment, access limits and separate adapter bundle repair; no finding is invented to force persistence.

### Native validation, deterministic rendering and frozen record integrity

schema: supported. Targets: GO:0045334.

The original bundle validates and renders exactly, and the full current record hash equals its original frozen input and historical source bytes. Both current native protein commands exit0 at empty inventory scope. Root owns whole-corpus and final integration gates.

### Empty molecular inventory and actual check times

provenance: supported. Targets: GO:0045334.

All represented protein-example/xref and typed protein-node inventories are empty. Command success cannot independently establish the named clathrin/adaptor narrative, localization, mechanism or necessity. Current receipts and historical original checks remain explicitly separate.

### No maintained images or numerical measurements

scope: not_applicable. Targets: GO:0045334.

No target image, measurement or verbatim source snippet is declared. Reading source captions and text is not image-pixel, supplementary movie or raw microscopy analysis.

### Native validation, deterministic rendering and frozen record integrity

schema: supported. Targets: GO:0106176.

The original bundle validates and renders exactly, and the full current record hash equals its original frozen input and historical source bytes. Both current native protein commands exit0 at empty inventory scope. Root owns whole-corpus and final integration gates.

### Empty molecular inventory and actual check times

provenance: supported. Targets: GO:0106176.

All represented protein-example/xref and typed protein-node inventories are empty. Command success cannot independently establish the named clathrin/adaptor narrative, localization, mechanism or necessity. Current receipts and historical original checks remain explicitly separate.

### No maintained images or numerical measurements

scope: not_applicable. Targets: GO:0106176.

No target image, measurement or verbatim source snippet is declared. Reading source captions and text is not image-pixel, supplementary movie or raw microscopy analysis.

### Native validation, deterministic rendering and frozen record integrity

schema: supported. Targets: GO:0030669.

The original bundle validates and renders exactly, and the full current record hash equals its original frozen input and historical source bytes. Both current native protein commands exit0 at empty inventory scope. Root owns whole-corpus and final integration gates.

### Empty molecular inventory and actual check times

provenance: supported. Targets: GO:0030669.

All represented protein-example/xref and typed protein-node inventories are empty. Command success cannot independently establish the named clathrin/adaptor narrative, localization, mechanism or necessity. Current receipts and historical original checks remain explicitly separate.

### No maintained images or numerical measurements

scope: not_applicable. Targets: GO:0030669.

No target image, measurement or verbatim source snippet is declared. Reading source captions and text is not image-pixel, supplementary movie or raw microscopy analysis.

### Species identity and yeast experimental model

scope: supported. Targets: GO:0045334.

Native taxonomy verifies S. cerevisiae. Newpher directly supports recruitment dynamics at cortical endocytic sites, with wild-type and mutant/drug-treated observations distinguished. COMMON remains qualitative occurrence context, not a frequency measured across strains or conditions. Canonical notes name the endocytic-site model, not a strain-general sealed-vesicle assay.

### Direct sealed-lumen and coat-retention endpoint

evidence: unknown. Targets: GO:0045334.

Newpher Discussion explicitly cannot distinguish clathrin disassembly before budding from departure of a clathrin-bearing vesicle or bud out of the TIRF field. It does not directly resolve sealed lumen or coat retention after release. The lumen formation wording is retained as endocytic-site model context, not a claim that fluorescence puncta resolved closure. Generic structural identity/topology has independent native GO support.

### Narrative molecular/pathway applicability and species coverage

scope: not_applicable. Targets: GO:0045334.

All three records mention clathrin and adaptor recruitment in their yeast-model narrative; whole vesicle and membrane additionally name clathrin-dependent endocytosis. Thus absence of transcriptomic assertions is not an exemption, even for the lumen label. The fresh complete catalogue lacks a matching S. cerevisiae dataset, so no downstream gene/module query applies. Historical runner unavailability remains separately dated.

### Actual primary body and abstract access tiers

provenance: supported. Targets: GO:0045334.

Newpher fresh Duke PDF was inspected only at declared body/table/methods sections and text captions; no pixels or movies. Kaksonen, where cited by whole and membrane, was checked at complete primary abstract only after public body routes failed. Original October access dates are historical; current observations are genuinely fetched November3.

### Formation dependence versus structural constitution

scope: unknown. Targets: GO:0045334.

No individual protein, adaptor or lipid is assigned a tested formation requirement by these target records. Generic membrane material can be constitutionally necessary without requiring clathrin for every endocytic vesicle. The source does not turn recruitment/localization into universal assembly necessity.

### Qualified positive scientific assessment

consistency: supported. Targets: GO:0045334.

pass_with_limitations remains supported for identity, hierarchy, bounded yeast-model scope and nonmechanistic topology. The unresolved sealed-vesicle transition and individual formation dependencies remain explicit. There are no original scientific findings/actions and no new concrete record-curation defect established in this scope.

### Target-specific composition and neighboring scope

completeness: supported. Targets: GO:0045334.

Entire target is reviewed. Generic sibling and coat neighbors supply only boundary/component responsibility context. Optional protein inventories, cargo lists, measurements and images are not required for a whole vesicle or spatial/bilayer part. No neighbor, grouped issue or category finding is terminally resolved.

### Species identity and yeast experimental model

scope: supported. Targets: GO:0106176.

Native taxonomy verifies S. cerevisiae. Newpher directly supports recruitment dynamics at cortical endocytic sites, with wild-type and mutant/drug-treated observations distinguished. COMMON remains qualitative occurrence context, not a frequency measured across strains or conditions. Canonical notes name the endocytic-site model, not a strain-general sealed-vesicle assay.

### Direct sealed-lumen and coat-retention endpoint

evidence: unknown. Targets: GO:0106176.

Newpher Discussion explicitly cannot distinguish clathrin disassembly before budding from departure of a clathrin-bearing vesicle or bud out of the TIRF field. It does not directly resolve sealed lumen or coat retention after release. The lumen formation wording is retained as endocytic-site model context, not a claim that fluorescence puncta resolved closure. Generic structural identity/topology has independent native GO support.

### Narrative molecular/pathway applicability and species coverage

scope: not_applicable. Targets: GO:0106176.

All three records mention clathrin and adaptor recruitment in their yeast-model narrative; whole vesicle and membrane additionally name clathrin-dependent endocytosis. Thus absence of transcriptomic assertions is not an exemption, even for the lumen label. The fresh complete catalogue lacks a matching S. cerevisiae dataset, so no downstream gene/module query applies. Historical runner unavailability remains separately dated.

### Actual primary body and abstract access tiers

provenance: supported. Targets: GO:0106176.

Newpher fresh Duke PDF was inspected only at declared body/table/methods sections and text captions; no pixels or movies. Kaksonen, where cited by whole and membrane, was checked at complete primary abstract only after public body routes failed. Original October access dates are historical; current observations are genuinely fetched November3.

### Formation dependence versus structural constitution

scope: unknown. Targets: GO:0106176.

No individual protein, adaptor or lipid is assigned a tested formation requirement by these target records. Generic membrane material can be constitutionally necessary without requiring clathrin for every endocytic vesicle. The source does not turn recruitment/localization into universal assembly necessity.

### Qualified positive scientific assessment

consistency: supported. Targets: GO:0106176.

pass_with_limitations remains supported for identity, hierarchy, bounded yeast-model scope and nonmechanistic topology. The unresolved sealed-vesicle transition and individual formation dependencies remain explicit. There are no original scientific findings/actions and no new concrete record-curation defect established in this scope.

### Target-specific composition and neighboring scope

completeness: supported. Targets: GO:0106176.

Entire target is reviewed. Generic sibling and coat neighbors supply only boundary/component responsibility context. Optional protein inventories, cargo lists, measurements and images are not required for a whole vesicle or spatial/bilayer part. No neighbor, grouped issue or category finding is terminally resolved.

### Species identity and yeast experimental model

scope: supported. Targets: GO:0030669.

Native taxonomy verifies S. cerevisiae. Newpher directly supports recruitment dynamics at cortical endocytic sites, with wild-type and mutant/drug-treated observations distinguished. COMMON remains qualitative occurrence context, not a frequency measured across strains or conditions. Canonical notes name the endocytic-site model, not a strain-general sealed-vesicle assay.

### Direct sealed-lumen and coat-retention endpoint

evidence: unknown. Targets: GO:0030669.

Newpher Discussion explicitly cannot distinguish clathrin disassembly before budding from departure of a clathrin-bearing vesicle or bud out of the TIRF field. It does not directly resolve sealed lumen or coat retention after release. The lumen formation wording is retained as endocytic-site model context, not a claim that fluorescence puncta resolved closure. Generic structural identity/topology has independent native GO support.

### Narrative molecular/pathway applicability and species coverage

scope: not_applicable. Targets: GO:0030669.

All three records mention clathrin and adaptor recruitment in their yeast-model narrative; whole vesicle and membrane additionally name clathrin-dependent endocytosis. Thus absence of transcriptomic assertions is not an exemption, even for the lumen label. The fresh complete catalogue lacks a matching S. cerevisiae dataset, so no downstream gene/module query applies. Historical runner unavailability remains separately dated.

### Actual primary body and abstract access tiers

provenance: supported. Targets: GO:0030669.

Newpher fresh Duke PDF was inspected only at declared body/table/methods sections and text captions; no pixels or movies. Kaksonen, where cited by whole and membrane, was checked at complete primary abstract only after public body routes failed. Original October access dates are historical; current observations are genuinely fetched November3.

### Formation dependence versus structural constitution

scope: unknown. Targets: GO:0030669.

No individual protein, adaptor or lipid is assigned a tested formation requirement by these target records. Generic membrane material can be constitutionally necessary without requiring clathrin for every endocytic vesicle. The source does not turn recruitment/localization into universal assembly necessity.

### Qualified positive scientific assessment

consistency: supported. Targets: GO:0030669.

pass_with_limitations remains supported for identity, hierarchy, bounded yeast-model scope and nonmechanistic topology. The unresolved sealed-vesicle transition and individual formation dependencies remain explicit. There are no original scientific findings/actions and no new concrete record-curation defect established in this scope.

### Target-specific composition and neighboring scope

completeness: supported. Targets: GO:0030669.

Entire target is reviewed. Generic sibling and coat neighbors supply only boundary/component responsibility context. Optional protein inventories, cargo lists, measurements and images are not required for a whole vesicle or spatial/bilayer part. No neighbor, grouped issue or category finding is terminally resolved.

### Whole endocytic-coated vesicle and dual parentage

identity: supported. Targets: GO:0045334.

GO0045334 identifies the whole plasma-membrane-derived clathrin-coated endocytic vesicle, with GO0030136 and GO0030139 as independent is-a parents. Named coat GO0030128 and membrane GO0030669 are parts, not synonyms of the whole. The endocytic class is distinct from clathrin traffic at internal TGN/endosomal sites.

### Parts versus lower-level constituents

grounding: supported. Targets: GO:0045334.

Whole-vesicle has_part names the coat and membrane and intentionally leaves chains, adaptors and lipids to those substructure records. This does not require a duplicate protein inventory or imply every endocytic carrier must depend on clathrin for formation.

### Five nonmechanistic parthood, bounds and participation edges

graph: supported. Targets: GO:0045334.

All five edges are supported at their stated scope: coat part_of membrane and whole, membrane part_of and bounds whole, whole participates in named endocytic process. Official GO source has the membrane bounding_layer_of axiom. No complete adaptor assembly, cargo selection or actin-driven scission mechanism is asserted.

### Endocytic-specific lumen and generic-lumen parent

identity: supported. Targets: GO:0106176.

GO0106176 denotes enclosed volume, not cargo. It is_a GO0071682 and part_of GO0045334. The local generic clathrin-coated-vesicle lumen parent is a broader class, supported by its frozen definition and UniProtSL0319; nested parent GO mappings do not give SL0319 a direct GO0106176 identity.

### Spatial region without invariant cargo composition

grounding: supported. Targets: GO:0106176.

The bounded lumen is intentionally not a fixed cargo or protein complex. Empty components and exclusion of variable internalized cargo are coherent with its native definition; absence of a detailed molecular inventory is not a required correction.

### Two descriptive lumen containment/enclosure edges

graph: supported. Targets: GO:0106176.

The lumen is part of the whole vesicle, and membrane bounds the lumen. The latter follows its explicit enclosed-volume definition; it does not make the membrane identical to cargo or assert how closure/scission occurs. Both graph edges are NONMECHANISTIC.

### Exact bilayer, dual membrane parents and protein-coat part

identity: supported. Targets: GO:0030669.

GO0030669 is the bilayer around the whole endocytic coated vesicle, with clathrin-coated membrane and endocytic membrane parents. GO0030128 is explicitly a part in the native ontology and remains a separately named protein coat, not lipid material.

### Collective constitutional bilayer and label-only grounding

grounding: supported. Targets: GO:0030669.

The single LIPID row is collective bilayer material, not an exact lipid molecule. REVIEWED_LABEL_ONLY avoids using whole-location GO0030669 as a chemical identity. ESSENTIAL is constitutional at that collective scale; the open grounding TODO is uncertainty, not evidence no suitable term exists.

### Four descriptive edges and material component linkage

graph: supported. Targets: GO:0030669.

All four edges retain coat parthood, membrane parthood/bounds and whole-vesicle process participation. GO source directly supports the bounding_layer_of and coat part_of relations. The membrane component_ref links its collective bilayer material rather than assigning a lipid identity to the protein coat or complete multisubstructure vesicle. No molecular necessity mechanism is introduced.

### Complete frozen-input comparison and bounded refresh

provenance: supported. Targets: GO:0033106, GO:0045334, GO:0106176, GO:0030669, GO:0030136, cellstructuremech:clathrin_coated_vesicle_lumen, GO:0030665, GO:0030135, GO:0030662, cellstructuremech:coccolith_vesicle.

0 of ten original target hashes differ from current main. The changed content is substantively reassessed in the target-specific assessments; original observations remain historical and unchanged. All current target and used context bytes are frozen.

## Findings

### micro-F1: The cited PPY1/PPY12 lineage has the wrong current species

major / open / confirmed; issue key: cis-golgi-network-membrane-ppy12-current-taxon.

Rossanese1999 used PPY1 and its isogenic PPY12 derivatives. ATCC identifies PPY12 as K. phaffii after sequence-based reidentification; ENA LC815816.1 independently pairs PPY12 with taxon460519. The maintained occurrence and canonical-example fields instead assign that experiment to K. pastoris4922. Historical Pichia pastoris nomenclature alone does not justify that current species assignment.

### micro-F2: The stack study does not directly establish a CGN-membrane example

major / open / confirmed; issue key: cis-golgi-network-membrane-stack-study-evidence-scope.

The sole source attached to this membrane occurrence and canonical example resolves ordered Golgi stacks near transitional ER. Native GO distinguishes CGN from the Golgi stack; the study assigns its observed Sec13-positive tubulovesicular interface to tER. Stack membranes or early-Golgi marker apposition therefore do not directly identify the particular CGN membrane asserted by these fields. The scope gap persists after correcting the species.

### micro-F3: Qualify the RET1 protein-example uniqueness claim

minor / open / confirmed; issue key: coated-vesicle-ret1-query-uniqueness.

The current reviewed exact-gene/taxon query for RET1 in S288C returns P53622 (primary COP1; RET1 synonym) and P22276 (primary RET1; RNA polymerase III subunit). P53622 is the correct representative alpha-coatomer example, as its role already states, but its evidence note calls it the single reviewed RET1 entry. The finding concerns this present unsupported uniqueness wording; it does not establish what a historical query returned.

## Recommended Actions And Acceptance Checks

### micro-A1

Correct any retained PPY1/PPY12 experimental attribution to K. phaffii460519 using the explicit strain bridge and retain the historical name in notes. Independently resolve the CGN-membrane evidence gap before retaining the study as a confirmed example.

- Any retained experimental attribution uses the verified current taxon and documented strain provenance.
- Retaxonomizing the strain is not treated as proof of CGN-membrane occurrence.
- Focused native validators pass.
- Scientific edits belong to a separate authorized guarded-writer curation PR with event/history and native checks; no record is changed in this review PR.

### micro-A2

Supply direct evidence for the CGN membrane in the asserted organism, or remove/defer the occurrence/example and retain Rossanese as explicitly broader Golgi-stack/tER context. Do not infer absence of CGN from the evidence gap or replace the exact membrane identity with a whole-stack concept.

- Retained occurrence and canonical-example evidence distinguishes CGN membrane from generic stack membranes and tER.
- The example does not rest solely on ordered stacks or early-Golgi marker localization.
- The independent current-taxon mismatch is resolved for retained experimental attributions.
- Focused native validators pass.
- Scientific edits belong to a separate authorized guarded-writer curation PR with event/history and native checks; no record is changed in this review PR.

### micro-A3

Retain P53622/COP1 and explain that legacy RET1 was disambiguated by the coatomer protein identity; remove the unsupported single-entry wording or explicitly use the unique COP1 query with a refreshed retrieval note.

- The current note does not claim RET1 uniquely identifies P53622.
- The correct coatomer accession and taxon remain unchanged.
- The note distinguishes current verification from historical retrieval.
- Focused native validation passes.
- Scientific edits belong to a separate authorized guarded-writer curation PR with event/history and native checks; no record is changed in this review PR.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| current-record-0 | data/structures/membrane_organelle/cis_golgi_network_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 c818f4de1c2fd8c36bc121d4389ce017c59526e083e6aefdf1b2a0041411da9c; current SHA256 c818f4de1c2fd8c36bc121d4389ce017c59526e083e6aefdf1b2a0041411da9c. Record bytes unchanged since the original review. |
| original-review-0 | reviews/structured/20261021T111327Z-cis-golgi-network-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-1 | data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 3193e3f6ea811d515c1545dc4e9179c8122e8718a328ed11261c7b648e94343d; current SHA256 3193e3f6ea811d515c1545dc4e9179c8122e8718a328ed11261c7b648e94343d. Record bytes unchanged since the original review. |
| original-review-1 | reviews/structured/20261021T111328Z-clathrin-coated-endocytic-vesicle-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-2 | data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_lumen.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 d3a53daa5cc28635e48242bfa4d7dab04186a8c7f17b40a1491de51e94a33951; current SHA256 d3a53daa5cc28635e48242bfa4d7dab04186a8c7f17b40a1491de51e94a33951. Record bytes unchanged since the original review. |
| original-review-2 | reviews/structured/20261021T111329Z-clathrin-coated-endocytic-vesicle-lumen-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-3 | data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 70d8d315440e5cc7cc4c8f8c11a9103d74deffa773df25d9051113122d8a189a; current SHA256 70d8d315440e5cc7cc4c8f8c11a9103d74deffa773df25d9051113122d8a189a. Record bytes unchanged since the original review. |
| original-review-3 | reviews/structured/20261021T111329Z-clathrin-coated-endocytic-vesicle-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-4 | data/structures/membrane_organelle/clathrin_coated_vesicle.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 cee241afc73475bcdec9d8c3c4c57bdf9c4cb2f726e4a78615dfb393613be9ad; current SHA256 cee241afc73475bcdec9d8c3c4c57bdf9c4cb2f726e4a78615dfb393613be9ad. Record bytes unchanged since the original review. |
| original-review-4 | reviews/structured/20261021T111330Z-clathrin-coated-vesicle-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-5 | data/structures/membrane_organelle/clathrin_coated_vesicle_lumen.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 2137a192f721232651c140497813cea3f15a73a67e910194d59fadc7837308f9; current SHA256 2137a192f721232651c140497813cea3f15a73a67e910194d59fadc7837308f9. Record bytes unchanged since the original review. |
| original-review-5 | reviews/structured/20261021T111331Z-clathrin-coated-vesicle-lumen-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-6 | data/structures/membrane_organelle/clathrin_coated_vesicle_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 963e3cbe094c98b1279923d8f4ecc6a27343f82aa7240dece427fa09882c25f1; current SHA256 963e3cbe094c98b1279923d8f4ecc6a27343f82aa7240dece427fa09882c25f1. Record bytes unchanged since the original review. |
| original-review-6 | reviews/structured/20261021T111332Z-clathrin-coated-vesicle-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-7 | data/structures/membrane_organelle/coated_vesicle.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 baf2f374fd87cb07f0ae0a31c5962cfa34c345941f872a96759858c88c8218c1; current SHA256 baf2f374fd87cb07f0ae0a31c5962cfa34c345941f872a96759858c88c8218c1. Record bytes unchanged since the original review. |
| original-review-7 | reviews/structured/20261021T111333Z-coated-vesicle-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-8 | data/structures/membrane_organelle/coated_vesicle_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 b74f6c754d374d664267834c903c7bb2aed86f79145de8ce69f6ea9785bbebcc; current SHA256 b74f6c754d374d664267834c903c7bb2aed86f79145de8ce69f6ea9785bbebcc. Record bytes unchanged since the original review. |
| original-review-8 | reviews/structured/20261021T111334Z-coated-vesicle-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-9 | data/structures/membrane_organelle/coccolith_vesicle.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 89b7e793211332507189d1ba872fc1eb901cf8703323853cd10d65b45e971655; current SHA256 89b7e793211332507189d1ba872fc1eb901cf8703323853cd10d65b45e971655. Record bytes unchanged since the original review. |
| original-review-9 | reviews/structured/20261021T111335Z-coccolith-vesicle-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| plaque-current-4 | data/structures/membrane_organelle/clathrin_coated_vesicle.yaml; Entire maintained record at source cee44c9b340b36e4e103ebd16c4bfcf6745bd41f; all fields, histories, discussions and graphs | supports | Complete current target read. Hash is unchanged from the original frozen target; PROPOSED status remains unchanged and no record curation is performed. |
| plaque-original-4 | reviews/structured/20261021T111330Z-clathrin-coated-vesicle-audit/review.yaml; Original authoritative YAML, rendered Markdown, all source inputs, assessments, checks, findings/actions and limitations | supports | Original review validates and renders byte-identically. Every historical frozen input resolves and matches its hash at the original source commit; current target hash also matches. Original verdict is pass_with_limitations, with no scientific findings or curation actions. |
| plaque-current-5 | data/structures/membrane_organelle/clathrin_coated_vesicle_lumen.yaml; Entire maintained record at source cee44c9b340b36e4e103ebd16c4bfcf6745bd41f; all fields, histories, discussions and graphs | supports | Complete current target read. Hash is unchanged from the original frozen target; PROPOSED status remains unchanged and no record curation is performed. |
| plaque-original-5 | reviews/structured/20261021T111331Z-clathrin-coated-vesicle-lumen-audit/review.yaml; Original authoritative YAML, rendered Markdown, all source inputs, assessments, checks, findings/actions and limitations | supports | Original review validates and renders byte-identically. Every historical frozen input resolves and matches its hash at the original source commit; current target hash also matches. Original verdict is pass_with_limitations, with no scientific findings or curation actions. |
| plaque-current-6 | data/structures/membrane_organelle/clathrin_coated_vesicle_membrane.yaml; Entire maintained record at source cee44c9b340b36e4e103ebd16c4bfcf6745bd41f; all fields, histories, discussions and graphs | supports | Complete current target read. Hash is unchanged from the original frozen target; PROPOSED status remains unchanged and no record curation is performed. |
| plaque-original-6 | reviews/structured/20261021T111332Z-clathrin-coated-vesicle-membrane-audit/review.yaml; Original authoritative YAML, rendered Markdown, all source inputs, assessments, checks, findings/actions and limitations | supports | Original review validates and renders byte-identically. Every historical frozen input resolves and matches its hash at the original source commit; current target hash also matches. Original verdict is pass_with_limitations, with no scientific findings or curation actions. |
| plaque-current-9 | data/structures/membrane_organelle/coccolith_vesicle.yaml; Entire maintained record at source cee44c9b340b36e4e103ebd16c4bfcf6745bd41f; all fields, histories, discussions and graphs | supports | Complete current target read. Hash is unchanged from the original frozen target; PROPOSED status remains unchanged and no record curation is performed. |
| plaque-original-9 | reviews/structured/20261021T111335Z-coccolith-vesicle-audit/review.yaml; Original authoritative YAML, rendered Markdown, all source inputs, assessments, checks, findings/actions and limitations | supports | Original review validates and renders byte-identically. Every historical frozen input resolves and matches its hash at the original source commit; current target hash also matches. Original verdict is pass_with_limitations, with no scientific findings or curation actions. |
| plaque-policy | .claude/skills/review-yaml-record/SKILL.md; Frozen native evidence, structure identity, components, graph-scope and applicability contract | context_only | Named molecular narratives trigger actual structured-source applicability; absent expression claims alone do not justify exemption. Localization, molecular function, material constitution and formation necessity are distinct. |
| plaque-rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Frozen native evidence, structure identity, components, graph-scope and applicability contract | context_only | Named molecular narratives trigger actual structured-source applicability; absent expression claims alone do not justify exemption. Localization, molecular function, material constitution and formation necessity are distinct. |
| plaque-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Frozen native evidence, structure identity, components, graph-scope and applicability contract | context_only | Named molecular narratives trigger actual structured-source applicability; absent expression claims alone do not justify exemption. Localization, molecular function, material constitution and formation necessity are distinct. |
| plaque-schema-policy | src/cellstructuremech/schema/cellstructuremech.yaml; Frozen native evidence, structure identity, components, graph-scope and applicability contract | context_only | Named molecular narratives trigger actual structured-source applicability; absent expression claims alone do not justify exemption. Localization, molecular function, material constitution and formation necessity are distinct. |
| plaque-neighbor-coat | data/structures/other/clathrin_vesicle_coat.yaml; Identifier, label, definition, hierarchy/parthood only; coat additionally component IDs/labels/types for heavy and light chain | context_only | Frozen before inspection. Used only to distinguish whole vesicle, coat, mineral product and external covering. Coat contains separate heavy/light-chain components, as the target discussion states. No independent validation of neighbor accession mappings, full neighbor science or historical dispositions is claimed. |
| plaque-neighbor-coccolith | data/structures/envelope/coccolith.yaml; Identifier, label, definition, hierarchy/parthood only; coat additionally component IDs/labels/types for heavy and light chain | context_only | Frozen before inspection. Used only to distinguish whole vesicle, coat, mineral product and external covering. Coat contains separate heavy/light-chain components, as the target discussion states. No independent validation of neighbor accession mappings, full neighbor science or historical dispositions is claimed. |
| plaque-neighbor-coccosphere | data/structures/envelope/coccosphere.yaml; Identifier, label, definition, hierarchy/parthood only; coat additionally component IDs/labels/types for heavy and light chain | context_only | Frozen before inspection. Used only to distinguish whole vesicle, coat, mineral product and external covering. Coat contains separate heavy/light-chain components, as the target discussion states. No independent validation of neighbor accession mappings, full neighbor science or historical dispositions is claimed. |
| plaque-clathrin-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030136,GO:0030135,GO:0030125,GO:0030665,GO:0072583,GO:0060205,GO:0030659,GO:0030662; All eight requested active GO terms, names, definitions, aspects and typed child relations | supports | Exact whole vesicle0030136, coat0030125 and membrane0030665 are distinct. Membrane is a direct part_of child of whole vesicle, coated vesicle0030135 is its is_a parent, and membrane parents0030662/0030659 are connected by is_a. The ontology also represents coat part_of the membrane location; this does not make coat proteins constituents of the separately modeled lipid-bilayer material. GO0072583 supports endocytosis through coated pits/vesicles. |
| plaque-root23-sources-coccolith-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0016020,GO:0043231; Exact GO0016020 and0043231 identities, active status and definitions | supports | GO0016020 denotes the structural membrane; GO0043231 is a broad intracellular membrane-bounded organelle parent, not an exact coccolith-vesicle identity. |
| plaque-clathrin-agent-SL-0070 | https://rest.uniprot.org/locations/SL-0070.json; Native definition, synonyms, direct GO correspondences and immediate isA/partOf objects distinguished from nested ancestors | supports | SL0070 identifies the whole clathrin-coated vesicle and CCV synonym. SL0071 is its membrane and directly partOf SL0070. SL0319 defines the bounded lumen, directly partOf SL0070, with cytoplasmic-vesicle-lumen parent; it does not have an exact direct GO correspondence. |
| plaque-clathrin-agent-SL-0071 | https://rest.uniprot.org/locations/SL-0071.json; Native definition, synonyms, direct GO correspondences and immediate isA/partOf objects distinguished from nested ancestors | supports | SL0070 identifies the whole clathrin-coated vesicle and CCV synonym. SL0071 is its membrane and directly partOf SL0070. SL0319 defines the bounded lumen, directly partOf SL0070, with cytoplasmic-vesicle-lumen parent; it does not have an exact direct GO correspondence. |
| plaque-clathrin-agent-SL-0319 | https://rest.uniprot.org/locations/SL-0319.json; Native definition, synonyms, direct GO correspondences and immediate isA/partOf objects distinguished from nested ancestors | supports | SL0070 identifies the whole clathrin-coated vesicle and CCV synonym. SL0071 is its membrane and directly partOf SL0070. SL0319 defines the bounded lumen, directly partOf SL0070, with cytoplasmic-vesicle-lumen parent; it does not have an exact direct GO correspondence. |
| plaque-clathrin-agent-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Exact taxId, scientificName, rank, lineage and alternative-name list | supports | Current ENA verifies Saccharomyces cerevisiae 4932.  Taxonomy alone does not establish occurrence, strain identity or prevalence. |
| plaque-root23-sources-NCBITaxon-127549 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/127549; Exact taxId, scientificName, rank, lineage and alternative-name list | supports | Current ENA verifies Calcidiscus leptoporus 127549.  Taxonomy alone does not establish occurrence, strain identity or prevalence. |
| plaque-root23-sources-NCBITaxon-2903 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2903; Exact taxId, scientificName, rank, lineage and alternative-name list | supports | Current ENA verifies Emiliania huxleyi 2903. Gephyrocapsa huxleyi is explicitly a synonym of Emiliania huxleyi. Taxonomy alone does not establish occurrence, strain identity or prevalence. |
| plaque-clathrin-agent-doi-10.1016_j.devcel.2005.04.014 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.devcel.2005.04.014; Exact DOI query result: title, authors, publication year, DOI/PMID and complete abstract | supports | Verified bibliography: In vivo dynamics of clathrin and its adaptor-dependent recruitment to the actin-based endocytic machinery in yeast.; Newpher TM, Smith RP, Lemmon V, Lemmon SK.; 2005. Complete abstract inspected; body access is separately declared. |
| plaque-clathrin-agent-kaksonen2005-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.cell.2005.09.024; Exact DOI query result: title, authors, publication year, DOI/PMID and complete abstract | supports | Verified bibliography: A modular design for the clathrin- and actin-mediated endocytosis machinery.; Kaksonen M, Toret CP, Drubin DG.; 2005. Complete abstract inspected; body access is separately declared. |
| plaque-root23-sources-doi-10.1021_jacs.6c02151 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1021/jacs.6c02151; Exact DOI query result: title, authors, publication year, DOI/PMID and complete abstract | supports | Verified bibliography: Spatial Relations between Coccoliths and Their Confining Membrane During Crystal Morphogenesis.; Avrahami EM, Karpov D, Aram L, Elad N, Safadi R, Rosenhek-Goldian I, Sui XM, de Haan D, Varsano N, Cohen SR, Zlotnikov I, Gal A.; 2026. Complete abstract inspected; body access is separately declared. |
| plaque-root23-sources-doi-10.1038_ncomms11228 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038/ncomms11228; Exact DOI query result: title, authors, publication year, DOI/PMID and complete abstract | supports | Verified bibliography: A vacuole-like compartment concentrates a disordered calcium phase in a key coccolithophorid alga.; Sviben S, Gal A, Hood MA, Bertinetti L, Politi Y, Bennet M, Krishnamoorthy P, Schertel A, Wirth R, Sorrentino A, Pereiro E, Faivre D, Scheffel A.; 2016. Complete abstract inspected; body access is separately declared. |
| plaque-clathrin-agent-newpher2005-duke | https://dukespace.lib.duke.edu/server/api/core/bitstreams/e3c70c30-e4a1-4ba0-8ea6-c50af4ba491e/content; Genuine published PDF pp87–96: Summary, Introduction, Results, Discussion and Experimental Procedures including Table1 and Fig1–6 captions; text only | supports | Fresh primary body supports heavy/light-chain localization at cortical yeast sites, adaptor-dependent recruitment and their timing relative to actin. Experiments include live fluorescent reporters, mutants and LAT-A, usually30C, in the named Table1 strains. The paper explicitly cannot distinguish clathrin disassembly before budding from departure of coated vesicles from the evanescent field. Its reporter dynamics are not direct sealed-lumen imaging, universal formation necessity or a population prevalence census. |
| plaque-clathrin-agent-newpher2005-publisher | https://doi.org/10.1016/j.devcel.2005.04.014; Actual native HTTP response; body format/content inspected to establish access tier only | context_only | HTTP200. Redirect/challenge/access response does not supply an inspected complete article body. Kaksonen support remains the exact complete primary abstract; no successful full-body retrieval is claimed here. |
| plaque-clathrin-agent-kaksonen2005-core | https://core.ac.uk/download/pdf/82329151.pdf; Actual native HTTP response; body format/content inspected to establish access tier only | context_only | HTTP403. Redirect/challenge/access response does not supply an inspected complete article body. Kaksonen support remains the exact complete primary abstract; no successful full-body retrieval is claimed here. |
| plaque-clathrin-agent-kaksonen2005-publisher | https://www.sciencedirect.com/science/article/pii/S0092867405009785; Actual native HTTP response; body format/content inspected to establish access tier only | context_only | HTTP403. Redirect/challenge/access response does not supply an inspected complete article body. Kaksonen support remains the exact complete primary abstract; no successful full-body retrieval is claimed here. |
| plaque-clathrin-agent-kaksonen2005-cellpdf | https://www.cell.com/article/S0092867405009785/pdf; Actual native HTTP response; body format/content inspected to establish access tier only | context_only | HTTP403. Redirect/challenge/access response does not supply an inspected complete article body. Kaksonen support remains the exact complete primary abstract; no successful full-body retrieval is claimed here. |
| plaque-clathrin-agent-kaksonen2005-corealternate | https://core.ac.uk/reader/82329151; Actual native HTTP response; body format/content inspected to establish access tier only | context_only | HTTP403. Redirect/challenge/access response does not supply an inspected complete article body. Kaksonen support remains the exact complete primary abstract; no successful full-body retrieval is claimed here. |
| plaque-clathrin-agent-kaksonen2005-api | https://api.elsevier.com/content/article/PII:S0092867405009785?httpAccept=text/xml; Actual native HTTP response; body format/content inspected to establish access tier only | context_only | HTTP200. Elsevier API returns bibliographic metadata, not scientific article body. Kaksonen support remains the exact complete primary abstract; no successful full-body retrieval is claimed here. |
| plaque-root23-sources-jats-PMC13067266 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13067266/fullTextXML; Complete scientific Introduction, Results, Discussion and Conclusions (sec1–4); complete Figure2–6 captions as text. Figure2 pixels inspected separately. | supports | Avrahami2026 directly images intracellular mineral-containing vesicles in C.leptoporus. Membrane–crystal spacing varies by region/stage.716 averaged particles are about half a full ATPase height; identity/function remain unresolved. Luminal calcium is observed; proposed chemical subregions and local growth inhibition are interpretations, not sealed suborganelles or a proven universal molding mechanism. Figures3/4 are cryo-ET; Figure2 is schematic/cryo-SEM/FIB-SEM. |
| plaque-root23-sources-coccolith2026-supplement | https://pmc-oa-opendata.s3.amazonaws.com/PMC13067266.1/ja6c02151_si_001.pdf; Actual PDF, Materials and Methods from Cell cultures through complete FIB-SEM data processing; partial subsequent lamellae section read but not used for stronger claims | supports | RCC1130 is explicitly identified, with18C and16h light/8h dark culture conditions. Figure2B preparation is high-pressure freezing/freeze fracture. External coccolith EDTA removal precedes plunge freezing/FIB slice-and-view, followed by alignment and manual membrane segmentation. No entire-supplement, raw reconstruction or cryo-ET processing audit is claimed. |
| plaque-root23-sources-jats-PMC4834641 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4834641/fullTextXML; Complete Results sec4–6, Discussion sec7 and culture Methods sec9; included Figure3–7 captions as text, not pixel inspection | supports | Sviben2016 distinguishes E.huxleyi AWI1516 coccolith-vesicle/reticular-body system from a separate membrane-bound Ca/P-rich store. Apposition does not prove membrane continuity or a named transporter. Earlier luminal nondetection is not generalized across species or to the later C.leptoporus observation. Methods support AWI1516 and18C culture/induction conditions. |
| plaque-root23-sources-coccolith2026-s3xml | https://pmc-oa-opendata.s3.amazonaws.com/PMC13067266.1/PMC13067266.1.xml; Native archived article title, complete author names, permissions and ALI license_ref | supports | Exact attribution agrees with the maintained figure. ALI supplies https://creativecommons.org/licenses/by/4.0/ and human-readable permission identifies CC-BY4.0. |
| plaque-root23-sources-coccolith-fig2 | https://pmc-oa-opendata.s3.amazonaws.com/PMC13067266.1/ja6c02151_0002.jpg; Fresh native Figure2 file bytes; exact SHA256 compared to frozen image, with complete source Figure2 caption independently read | supports | Native figure bytes exactly match the maintained image. The viewed panels show a schematic; cryo-SEM and cryo-FIB-SEM sections; and five reconstructed stages. Membrane/crystal relationships and scale bars match the caption; stages are different observed coccoliths, not a time-lapse of one cell. |
| plaque-image | data/images/membrane_organelle/coccolith_vesicle/pmc13067266_fig2.jpg; Entire700x418-pixel frozen image displayed with view_image and visually inspected | supports | PanelA schematic is not to scale; panelB cryogenic SEM shows a cut cell; C/D have sections and backscatter insets; E has five left-to-right/top-to-bottom reconstructed stages with membrane on right halves. Pixel inspection and source caption support SEM modality with reconstructed-volume panels, not cryo-ET attribution for this figure. |
| plaque-root23-sources-coccolith-go-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=coccolith&amp;limit=100&amp;page=1; Complete returned first page and exact query URL; result identities inspected | context_only | No returned hits for this exact bounded query. |
| plaque-root23-sources-coccolithogenesis-go-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=coccolithogenesis&amp;limit=100&amp;page=1; Complete returned first page and exact query URL; result identities inspected | context_only | No returned hits for this exact bounded query. |
| plaque-clathrin-lumen-go-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=clathrin%20coated%20vesicle%20lumen&amp;limit=100&amp;page=1; Complete returned first page and exact query URL; result identities inspected | context_only | First100 of651 hits include a narrower clathrin-coated ENDOCYTIC vesicle lumen, not an exact replacement for the broader SL0319 scope. This is not an exhaustive ontology absence claim. |
| plaque-catalogue | https://imodulondb.org/api/datasets; Complete current /api/datasets response, every organism and dataset row; no pagination | supports | No catalogue row matches S.cerevisiae, C.leptoporus or E.huxleyi/Gephyrocapsa. Downstream matched-organism gene/module queries therefore do not apply. Neither unrelated taxa nor catalogue absence establish biological absence. |
| plaque-historical-runner | /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources imodulondb datasets; Historical00:49Z receipt and stdout/stderr independently reread and hash-verified | context_only | Historical runner exited1 before datasets due OS PermissionError reading pyvenv.cfg. This is not a fresh invocation; current official catalogue is the permitted source fallback. |
| plaque-original-checks | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/adversary-plaque/original-checks.json; Four read-only native validate/render executions and every original frozen-source input hash | supports | All four validate; Markdown is exact;15/15/15/17 historical inputs match original source commits; all four target hashes remain current. Original findings/actions are empty. |
| plaque-native-clathrin_coated_vesicle-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/clathrin_coated_vesicle.yaml --verify; Actual root-owned focused command receipt and exact stdout independently read/hash-verified | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| plaque-native-clathrin_coated_vesicle-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/clathrin_coated_vesicle.yaml --causal-graphs; Actual root-owned focused command receipt and exact stdout independently read/hash-verified | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| plaque-native-clathrin_coated_vesicle_lumen-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/clathrin_coated_vesicle_lumen.yaml --verify; Actual root-owned focused command receipt and exact stdout independently read/hash-verified | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| plaque-native-clathrin_coated_vesicle_lumen-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/clathrin_coated_vesicle_lumen.yaml --causal-graphs; Actual root-owned focused command receipt and exact stdout independently read/hash-verified | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| plaque-native-clathrin_coated_vesicle_membrane-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/clathrin_coated_vesicle_membrane.yaml --verify; Actual root-owned focused command receipt and exact stdout independently read/hash-verified | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| plaque-native-clathrin_coated_vesicle_membrane-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/clathrin_coated_vesicle_membrane.yaml --causal-graphs; Actual root-owned focused command receipt and exact stdout independently read/hash-verified | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| plaque-native-coccolith_vesicle-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/coccolith_vesicle.yaml --verify; Actual root-owned focused command receipt and exact stdout independently read/hash-verified | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| plaque-native-coccolith_vesicle-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/coccolith_vesicle.yaml --causal-graphs; Actual root-owned focused command receipt and exact stdout independently read/hash-verified | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| micro-review-policy | .claude/skills/review-yaml-record/SKILL.md; Evidence Rules; Structured Source Cross-Checks; Workflow | supports | Named molecular claims trigger structured-source applicability whether or not expression inference is made. Scope of protein identity, membership and formation necessity must be kept separate. Read-only source review does not authorize record edits. |
| micro-review-config | conf/record_review.yaml; Active routes and rubrics | supports | Current frozen configuration reread; seventeen common policy/schema/verifier inputs are byte-identical to the preceding independently reviewed cohort. Previously inspected contract rules remain applicable; current source and target bytes are independently verified. |
| micro-review-profile | docs/record-review-profile.md; Issue-only persistence and native checks | supports | Issue-bearing successor can include positive assessments alongside preserved unresolved findings. Original observations remain immutable. Root owns global gates and final review publication. |
| micro-graph-contract | .claude/skills/curate-causal-graphs/SKILL.md; Graph scope, node identity and constituent/necessity separation | supports | NONMECHANISTIC boundary/transport graphs are not complete molecular mechanisms. Membrane material, whole network, coat and whole vesicle identities must remain distinct. |
| micro-native-schema | src/cellstructuremech/schema/cellstructuremech.yaml; EssentialityEnum and CausalNode.component_ref | supports | Collective bilayer constitution is distinct from experimental necessity of individual lipids/proteins. component_ref must match the own component denoted; a membrane defined as the bilayer differs from the entire membrane-bounded compartment. |
| micro-review-schema | schema/record_review.yaml; EvidenceKind, Area, FindingReference and proposed action fields | supports | Source scopes and real dates are retained; native assessment area schema and complete predecessor repository/review/finding identity are used. |
| micro-original-validation-inputs | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/adversary-microtubule/original-validation-inputs.json; Three original native validate runs, render --content comparisons and git blob hash checks | supports | All three original pairs validate and render byte-identically. Their frozen target hashes match both original source9c0446c4 and current source; no stale input in this slice. Historical global executions remain historical. |
| micro-record-cis_golgi_network_membrane | data/structures/membrane_organelle/cis_golgi_network_membrane.yaml; Complete current YAML at cee44c9b340b36e4e103ebd16c4bfcf6745bd41f | supports | Whole unchanged target read, including identity, definition, taxon/strain examples, constituents, evidence, graph, scope notes, discussions and history. Original frozen hash remains current. |
| micro-prior-cis_golgi_network_membrane | reviews/structured/20261021T111327Z-cis-golgi-network-membrane-audit/review.yaml; Entire original YAML and deterministic Markdown | supports | Exact immutable 20261021T111327Z-cis-golgi-network-membrane-audit; original verdict needs_curation with 2 scientific findings. Original access dates and checks are not silently renewed. |
| micro-native-cis_golgi_network_membrane-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/cis_golgi_network_membrane-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cis_golgi_network_membrane.yaml --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/cis_golgi_network_membrane-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0 at cee44c9b340b36e4e103ebd16c4bfcf6745bd41f from 2026-11-03T10:50:08.672089+00:00 to 2026-11-03T10:50:09.075758+00:00. Empty protein-example inventory and zero GENE_OR_PROTEIN nodes. Passing empty scope does not verify narrative trafficking proteins or experimental occurrence. |
| micro-native-cis_golgi_network_membrane-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/cis_golgi_network_membrane-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cis_golgi_network_membrane.yaml --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/cis_golgi_network_membrane-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual exit0 at cee44c9b340b36e4e103ebd16c4bfcf6745bd41f from 2026-11-03T10:50:09.111556+00:00 to 2026-11-03T10:50:09.513675+00:00. Empty protein-example inventory and zero GENE_OR_PROTEIN nodes. Passing empty scope does not verify narrative trafficking proteins or experimental occurrence. |
| micro-record-coated_vesicle | data/structures/membrane_organelle/coated_vesicle.yaml; Complete current YAML at cee44c9b340b36e4e103ebd16c4bfcf6745bd41f | supports | Whole unchanged target read, including identity, definition, taxon/strain examples, constituents, evidence, graph, scope notes, discussions and history. Original frozen hash remains current. |
| micro-prior-coated_vesicle | reviews/structured/20261021T111333Z-coated-vesicle-audit/review.yaml; Entire original YAML and deterministic Markdown | supports | Exact immutable 20261021T111333Z-coated-vesicle-audit; original verdict needs_curation with 1 scientific findings. Original access dates and checks are not silently renewed. |
| micro-native-coated_vesicle-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/coated_vesicle-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/coated_vesicle.yaml --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/coated_vesicle-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0 at cee44c9b340b36e4e103ebd16c4bfcf6745bd41f from 2026-11-03T10:50:15.237964+00:00 to 2026-11-03T10:50:16.858845+00:00. Six reviewed S288C examples; one GENE_OR_PROTEIN node COVERED. RET1 ambiguity is a prose/query finding despite valid representative accession and native coverage. |
| micro-native-coated_vesicle-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/coated_vesicle-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/coated_vesicle.yaml --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/coated_vesicle-uniprot-causal.log SHA256 964400df2eca2a7f65a0941ad15132db748cdda186e8562931cbd43bde0d4464 | supports | Actual exit0 at cee44c9b340b36e4e103ebd16c4bfcf6745bd41f from 2026-11-03T10:50:16.889146+00:00 to 2026-11-03T10:50:17.293425+00:00. Six reviewed S288C examples; one GENE_OR_PROTEIN node COVERED. RET1 ambiguity is a prose/query finding despite valid representative accession and native coverage. |
| micro-record-coated_vesicle_membrane | data/structures/membrane_organelle/coated_vesicle_membrane.yaml; Complete current YAML at cee44c9b340b36e4e103ebd16c4bfcf6745bd41f | supports | Whole unchanged target read, including identity, definition, taxon/strain examples, constituents, evidence, graph, scope notes, discussions and history. Original frozen hash remains current. |
| micro-prior-coated_vesicle_membrane | reviews/structured/20261021T111334Z-coated-vesicle-membrane-audit/review.yaml; Entire original YAML and deterministic Markdown | supports | Exact immutable 20261021T111334Z-coated-vesicle-membrane-audit; original verdict pass_with_limitations with 0 scientific findings. Original access dates and checks are not silently renewed. |
| micro-native-coated_vesicle_membrane-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/coated_vesicle_membrane-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/coated_vesicle_membrane.yaml --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/coated_vesicle_membrane-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0 at cee44c9b340b36e4e103ebd16c4bfcf6745bd41f from 2026-11-03T10:50:17.323529+00:00 to 2026-11-03T10:50:17.729675+00:00. Empty protein-example inventory and zero GENE_OR_PROTEIN nodes. Passing empty scope does not verify narrative trafficking proteins or experimental occurrence. |
| micro-native-coated_vesicle_membrane-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/coated_vesicle_membrane-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/coated_vesicle_membrane.yaml --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/coated_vesicle_membrane-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual exit0 at cee44c9b340b36e4e103ebd16c4bfcf6745bd41f from 2026-11-03T10:50:17.760485+00:00 to 2026-11-03T10:50:18.158515+00:00. Empty protein-example inventory and zero GENE_OR_PROTEIN nodes. Passing empty scope does not verify narrative trafficking proteins or experimental occurrence. |
| micro-neighbor-cis_golgi_network | data/structures/membrane_organelle/cis_golgi_network.yaml; Frozen identity, definition, kind, hierarchy/parthood/has_part; coat neighbors additionally component IDs/labels/groundings/gene_symbols | supports | Boundary context only: cis_golgi_network. Supports distinction of whole compartments/membranes and generic versus subtype coats. No full neighboring-record source review or resolution of their findings is claimed. |
| micro-neighbor-golgi_apparatus | data/structures/membrane_organelle/golgi_apparatus.yaml; Frozen identity, definition, kind, hierarchy/parthood/has_part; coat neighbors additionally component IDs/labels/groundings/gene_symbols | supports | Boundary context only: golgi_apparatus. Supports distinction of whole compartments/membranes and generic versus subtype coats. No full neighboring-record source review or resolution of their findings is claimed. |
| micro-neighbor-vesicle_coat | data/structures/other/vesicle_coat.yaml; Frozen identity, definition, kind, hierarchy/parthood/has_part; coat neighbors additionally component IDs/labels/groundings/gene_symbols | supports | Boundary context only: vesicle_coat. Supports distinction of whole compartments/membranes and generic versus subtype coats. No full neighboring-record source review or resolution of their findings is claimed. |
| micro-neighbor-clathrin_vesicle_coat | data/structures/other/clathrin_vesicle_coat.yaml; Frozen identity, definition, kind, hierarchy/parthood/has_part; coat neighbors additionally component IDs/labels/groundings/gene_symbols | supports | Boundary context only: clathrin_vesicle_coat. Supports distinction of whole compartments/membranes and generic versus subtype coats. No full neighboring-record source review or resolution of their findings is claimed. |
| micro-neighbor-copi_vesicle_coat | data/structures/other/copi_vesicle_coat.yaml; Frozen identity, definition, kind, hierarchy/parthood/has_part; coat neighbors additionally component IDs/labels/groundings/gene_symbols | supports | Boundary context only: copi_vesicle_coat. Supports distinction of whole compartments/membranes and generic versus subtype coats. No full neighboring-record source review or resolution of their findings is claimed. |
| micro-neighbor-copii_vesicle_coat | data/structures/other/copii_vesicle_coat.yaml; Frozen identity, definition, kind, hierarchy/parthood/has_part; coat neighbors additionally component IDs/labels/groundings/gene_symbols | supports | Boundary context only: copii_vesicle_coat. Supports distinction of whole compartments/membranes and generic versus subtype coats. No full neighboring-record source review or resolution of their findings is claimed. |
| micro-cis-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005783,GO:0005794,GO:0005801,GO:0033106,GO:0098791; Retained2026-11-03T10:11Z packet, reassessed for the membrane target; QuickGO exact GO:0005801/0033106/0005794/0098791/0005783 active terms, definitions, synonyms, comments and children | supports | Unchanged source snapshot reused with its actual original access time. CGN is an ER-abutting network distinct from its membrane and whole Golgi; current GO explicitly says CGN is not part of the Golgi stack. Broader cis-face synonyms are not exact identities. |
| micro-cis-tax-4922 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4922; Retained2026-11-03T10:11Z packet, reassessed for the membrane target; ENA taxonomy exact taxId/scientificName/rank/lineage/otherNames | supports | Unchanged source snapshot reused with its actual original access time. Current authority identifies 4922 as Komagataella pastoris. Species and strain scope are retained; historical Pichia naming is not used as a current strain identity bridge. |
| micro-cis-tax-460519 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/460519; Retained2026-11-03T10:11Z packet, reassessed for the membrane target; ENA taxonomy exact taxId/scientificName/rank/lineage/otherNames | supports | Unchanged source snapshot reused with its actual original access time. Current authority identifies 460519 as Komagataella phaffii. Species and strain scope are retained; historical Pichia naming is not used as a current strain identity bridge. |
| micro-cis-jats-PMC2148216 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2148216.1/PMC2148216.1.xml; Retained2026-11-03T10:11Z packet, reassessed for the membrane target; DOI10.1083/jcb.145.1.69; Methods Strains and Plasmids, complete Results and complete Discussion; text only | supports | Unchanged source snapshot reused with its actual original access time. PPY1/PPY12 experiments establish coherent Golgi stacks adjacent to transitional ER. Sec13-positive tubulovesicular interface is interpreted as tER; Och1/late-marker apposition does not independently identify a distinct CGN. Whole primary narrative does not establish absence of CGN. No raw micrograph/pixel audit or full supplementary analysis. |
| micro-cis-atcc-204163 | https://www.atcc.org/products/204163; Retained2026-11-03T10:11Z packet, reassessed for the membrane target; ATCC204163 product identity, Strain designation PPY12, Genotype his4 arg4, Characteristics Comments | supports | Unchanged source snapshot reused with its actual original access time. PPY12 is K. phaffii; ATCC explicitly describes the change from K. pastoris based on in-house sequence analysis. This is a strain identity bridge, not evidence of organelle occurrence. |
| micro-cis-ena-LC815816 | https://www.ebi.ac.uk/ena/browser/api/embl/LC815816.1?download=false; Retained2026-11-03T10:11Z packet, reassessed for the membrane target; ENA LC815816.1 EMBL FT source qualifiers organism/strain/db_xref | supports | Unchanged source snapshot reused with its actual original access time. Source qualifiers identify Komagataella phaffii PPY12, taxon460519. Corroborates the strain bridge independently of historical name; ATG14 sequence is not evidence of CGN membership/function. |
| micro-cis-cho2000-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1016/S0014-5793%2800%2901268-0%22; Retained2026-11-03T10:11Z packet, reassessed for the membrane target; DOI10.1016/S0014-5793(00)01268-0; exact metadata and complete primary abstract only | partial | Unchanged source snapshot reused with its actual original access time. S. cerevisiae Sed5 membrane immunoisolation enriches early-Golgi mannosyltransferases and excludes late-Golgi/ER markers. This limited abstract does not establish K. pastoris/phaffii CGN occurrence or universally essential resident proteins; both publisher body/PDF attempts403. |
| micro-cis-go-parent | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000139; QuickGO exact GO:0000139 active name, definition and returned children | supports | Golgi membrane denotes the lipid bilayer surrounding Golgi compartments. This is appropriate broader membrane context; no current direct GO is_a edge absent from this response is invented. |
| micro-coated-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0012507,GO:0016192,GO:0030120,GO:0030125,GO:0030126,GO:0030127,GO:0030134,GO:0030135,GO:0030136,GO:0030137,GO:0030662,GO:0030663,GO:0030665,GO:0031410; All exact returned GO identifiers, active flags, definitions, synonyms and is_a/part_of children | supports | Current authority distinguishes coated vesicle, surrounding membrane, generic coat and clathrin/COPI/COPII subtypes. GO:0030662 explicitly lists GO:0030120 vesicle coat as part_of child; generic lipid-bilayer intuition is not substituted for this maintained ontology relationship. Transport process and cytoplasmic-vesicle parent terms are exact. |
| micro-coat-membrane-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0012507,GO:0030120,GO:0030135,GO:0030659,GO:0030662,GO:0030663,GO:0030665; All exact returned GO identifiers, active flags, definitions, synonyms and is_a/part_of children | supports | Current authority distinguishes coated vesicle, surrounding membrane, generic coat and clathrin/COPI/COPII subtypes. GO:0030662 explicitly lists GO:0030120 vesicle coat as part_of child; generic lipid-bilayer intuition is not substituted for this maintained ontology relationship. Transport process and cytoplasmic-vesicle parent terms are exact. |
| micro-NCBITaxon-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; ENA taxonomy exact taxId, scientificName, rank and lineage | supports | Verified 4932 Saccharomyces cerevisiae. Species-level experimental occurrence and representative S288C protein identity are distinct; this row does not equate experimental stocks to S288C. |
| micro-NCBITaxon-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; ENA taxonomy exact taxId, scientificName, rank and lineage | supports | Verified 559292 Saccharomyces cerevisiae S288C. Species-level experimental occurrence and representative S288C protein identity are distinct; this row does not equate experimental stocks to S288C. |
| micro-PMID-8004676 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A8004676%20AND%20SRC%3AMED; Exact metadata and complete primary abstract; DOI10.1016/0092-8674(94)90138-4; title COPII: a membrane coat formed by Sec proteins that drive vesicle budding from the endoplasmic reticulum. | partial | Complete primary abstract supports ER-derived COPII budding with Sar1/Sec13/Sec23 complexes, distinct from COPI. GTP versus nonhydrolyzable nucleotide changes fusion competence. Four failed publisher routes are not full bodies; no full Barlowe Methods audit. |
| micro-PMID-9568718 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A9568718%20AND%20SRC%3AMED; Exact metadata and complete primary abstract; DOI10.1016/s0092-8674(00)81577-9; title COPII-coated vesicle formation reconstituted with purified coat proteins and chemically defined liposomes. | partial | Complete primary abstract supports sequential coat recruitment to native ER and defined liposomes, coated buds/vesicles and integrity of donor/product membranes. Full selected body passages are separately evidenced below. |
| micro-PMID-10684247 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A10684247%20AND%20SRC%3AMED; Exact metadata and complete primary abstract; DOI10.1083/jcb.148.4.635; title The yeast nuclear pore complex: composition, architecture, and transport mechanism. | partial | Complete primary abstract concerns yeast nuclear-pore inventory/localization. It is consistent with the exact Q04491 nuclear-pore annotation cited by the record, not direct evidence for vesicle membership. |
| micro-PMID-14562095 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A14562095%20AND%20SRC%3AMED; Exact metadata and complete primary abstract; DOI10.1038/nature02026; title Global analysis of protein localization in budding yeast. | partial | Complete primary abstract concerns systematic GFP localization in yeast. The record correctly attributes P41810 Golgi-membrane localization to the UniProt experimental annotation; abstract does not independently expose every protein row. |
| micro-doi-10.1016_j.devcel.2005.04.014 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.devcel.2005.04.014; Exact metadata and complete primary abstract; DOI10.1016/j.devcel.2005.04.014; title In vivo dynamics of clathrin and its adaptor-dependent recruitment to the actin-based endocytic machinery in yeast. | partial | Complete primary abstract reports cortical/internal yeast clathrin and adaptor context. Full selected primary body is separately evidenced, without universal-necessity or single-vesicle resolution claims. |
| micro-doi-10.1016_j.cell.2012.01.015 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.cell.2012.01.015; Exact metadata and complete primary abstract; DOI10.1016/j.cell.2012.01.015; title A structure-based mechanism for Arf1-dependent recruitment of coatomer to membranes. | partial | Complete primary abstract reports Arf1/coatomer structural and biochemical recruitment model. Actual mammalian/yeast construct scopes and model limits are retained in the separately inspected body. |
| micro-matsuoka1998-author | https://bednareklab.biochem.wisc.edu/wp-content/uploads/sites/1623/2022/02/1998_Matsuoka_etal_Cell.pdf; DOI10.1016/S0092-8674(00)81577-9; printed p269 native/synthetic comparison and integrity Results; pp270-271 Discussion Vesicle Morphogenesis Governed by COPII Coat; Figure7 caption; p273 Strain and Materials; p274 stoichiometry Methods | supports | Fresh genuine author-hosted primary PDF text. Native microsome-derived and synthetic liposome-derived COPII vesicles are explicitly compared; RSY445 supplies ER-enriched microsomes. These support whole-vesicle native-ER and membrane synthetic-liposome examples. Reconstitution requirements do not become universal in vivo necessities, and the strain is not assumed identical to S288C. No figure pixels/raw data/full-paper audit. |
| micro-newpher2005-duke | https://dukespace.lib.duke.edu/server/api/core/bitstreams/e3c70c30-e4a1-4ba0-8ea6-c50af4ba491e/content; DOI10.1016/j.devcel.2005.04.014; printed pp87-89 Summary, Introduction, Table1, Results Localization of Clathrin In Vivo and Figure1 caption | supports | Fresh genuine institutional primary PDF. Yeast fluorescent heavy/light chains colocalize in cortical and intracellular structures; larger puncta partly overlap TGN/endosomal markers. Diffraction-limited puncta are not all proven mature vesicles. Broad clathrin-context support does not require one coat subtype or universally essential adaptor. No later body/movie/pixel audit. |
| micro-yu2012-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC3285272.1/PMC3285272.1.xml; DOI10.1016/j.cell.2012.01.015; complete Introduction; Results Experimental Approach and A Model for Arf1-Dependent Recruitment of Coatomer to Membranes | supports | Genuine primary JATS. Mammalian coatomer subcomplexes with defined human/yeast truncated Arf1 constructs support a bounded recruitment model. COPI, COPII and clathrin/AP systems are distinguished; proposed conformational effects remain proposals. Not direct accession-specific evidence for every yeast coat example, nor complete Methods/raw-data audit. |
| micro-UniProtKB-P22137 | https://rest.uniprot.org/uniprotkb/P22137.json; Exact UniProtKB entryType, primaryAccession, organism, genes, proteinDescription; SUBCELLULAR LOCATION and its source annotations | supports | Reviewed S288C accession P22137 primary gene CHC1; identity and native localization-annotation scope checked. Q04491 PMID10684247 specifically annotates nuclear pore; P41810 PMID14562095 specifically annotates Golgi membrane. P53622 is coatomer alpha/COP1 with RET1 synonym; P22276 is RNA-polymerase-III RET1. Identity verification alone does not establish universal coat membership/necessity. |
| micro-UniProtKB-P17891 | https://rest.uniprot.org/uniprotkb/P17891.json; Exact UniProtKB entryType, primaryAccession, organism, genes, proteinDescription; SUBCELLULAR LOCATION and its source annotations | supports | Reviewed S288C accession P17891 primary gene CLC1; identity and native localization-annotation scope checked. Q04491 PMID10684247 specifically annotates nuclear pore; P41810 PMID14562095 specifically annotates Golgi membrane. P53622 is coatomer alpha/COP1 with RET1 synonym; P22276 is RNA-polymerase-III RET1. Identity verification alone does not establish universal coat membership/necessity. |
| micro-UniProtKB-Q04491 | https://rest.uniprot.org/uniprotkb/Q04491.json; Exact UniProtKB entryType, primaryAccession, organism, genes, proteinDescription; SUBCELLULAR LOCATION and its source annotations | supports | Reviewed S288C accession Q04491 primary gene SEC13; identity and native localization-annotation scope checked. Q04491 PMID10684247 specifically annotates nuclear pore; P41810 PMID14562095 specifically annotates Golgi membrane. P53622 is coatomer alpha/COP1 with RET1 synonym; P22276 is RNA-polymerase-III RET1. Identity verification alone does not establish universal coat membership/necessity. |
| micro-UniProtKB-P38968 | https://rest.uniprot.org/uniprotkb/P38968.json; Exact UniProtKB entryType, primaryAccession, organism, genes, proteinDescription; SUBCELLULAR LOCATION and its source annotations | supports | Reviewed S288C accession P38968 primary gene SEC31; identity and native localization-annotation scope checked. Q04491 PMID10684247 specifically annotates nuclear pore; P41810 PMID14562095 specifically annotates Golgi membrane. P53622 is coatomer alpha/COP1 with RET1 synonym; P22276 is RNA-polymerase-III RET1. Identity verification alone does not establish universal coat membership/necessity. |
| micro-UniProtKB-P41810 | https://rest.uniprot.org/uniprotkb/P41810.json; Exact UniProtKB entryType, primaryAccession, organism, genes, proteinDescription; SUBCELLULAR LOCATION and its source annotations | supports | Reviewed S288C accession P41810 primary gene SEC26; identity and native localization-annotation scope checked. Q04491 PMID10684247 specifically annotates nuclear pore; P41810 PMID14562095 specifically annotates Golgi membrane. P53622 is coatomer alpha/COP1 with RET1 synonym; P22276 is RNA-polymerase-III RET1. Identity verification alone does not establish universal coat membership/necessity. |
| micro-UniProtKB-P53622 | https://rest.uniprot.org/uniprotkb/P53622.json; Exact UniProtKB entryType, primaryAccession, organism, genes, proteinDescription; SUBCELLULAR LOCATION and its source annotations | supports | Reviewed S288C accession P53622 primary gene COP1; identity and native localization-annotation scope checked. Q04491 PMID10684247 specifically annotates nuclear pore; P41810 PMID14562095 specifically annotates Golgi membrane. P53622 is coatomer alpha/COP1 with RET1 synonym; P22276 is RNA-polymerase-III RET1. Identity verification alone does not establish universal coat membership/necessity. |
| micro-UniProtKB-P22276 | https://rest.uniprot.org/uniprotkb/P22276.json; Exact UniProtKB entryType, primaryAccession, organism, genes, proteinDescription; SUBCELLULAR LOCATION and its source annotations | supports | Reviewed S288C accession P22276 primary gene RET1; identity and native localization-annotation scope checked. Q04491 PMID10684247 specifically annotates nuclear pore; P41810 PMID14562095 specifically annotates Golgi membrane. P53622 is coatomer alpha/COP1 with RET1 synonym; P22276 is RNA-polymerase-III RET1. Identity verification alone does not establish universal coat membership/necessity. |
| micro-query-CHC1-559292 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3ACHC1%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; Complete current UniProt reviewed exact-gene/taxon query and pagination metadata | supports | Current query returns 1 entries: P22137. RET1 ambiguity is current, not a reconstruction of the historical retrieval. Correct COP1 representative is retained. |
| micro-query-CLC1-559292 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3ACLC1%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; Complete current UniProt reviewed exact-gene/taxon query and pagination metadata | supports | Current query returns 1 entries: P17891. RET1 ambiguity is current, not a reconstruction of the historical retrieval. Correct COP1 representative is retained. |
| micro-query-SEC13-559292 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3ASEC13%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; Complete current UniProt reviewed exact-gene/taxon query and pagination metadata | supports | Current query returns 1 entries: Q04491. RET1 ambiguity is current, not a reconstruction of the historical retrieval. Correct COP1 representative is retained. |
| micro-query-SEC31-559292 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3ASEC31%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; Complete current UniProt reviewed exact-gene/taxon query and pagination metadata | supports | Current query returns 1 entries: P38968. RET1 ambiguity is current, not a reconstruction of the historical retrieval. Correct COP1 representative is retained. |
| micro-query-SEC26-559292 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3ASEC26%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; Complete current UniProt reviewed exact-gene/taxon query and pagination metadata | supports | Current query returns 1 entries: P41810. RET1 ambiguity is current, not a reconstruction of the historical retrieval. Correct COP1 representative is retained. |
| micro-query-COP1-559292 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3ACOP1%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; Complete current UniProt reviewed exact-gene/taxon query and pagination metadata | supports | Current query returns 1 entries: P53622. RET1 ambiguity is current, not a reconstruction of the historical retrieval. Correct COP1 representative is retained. |
| micro-query-RET1-559292 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3ARET1%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; Complete current UniProt reviewed exact-gene/taxon query and pagination metadata | supports | Current query returns 2 entries: P22276, P53622. RET1 ambiguity is current, not a reconstruction of the historical retrieval. Correct COP1 representative is retained. |
| micro-ipr-P22137 | https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/P22137/?page_size=200; InterPro all-entry/member matches for exact UniProt P22137; full returned page, count21, next=None | context_only | Bounded constituent family matches: IPR016341 Clathrin, heavy chain; PIRSF002290 Clathrin heavy chain; PTHR10292 Clathrin heavy chain. Distinct protein families support heterogeneous coat scope; none is promoted to exact identity of the entire clathrin/COPI/COPII parent cohort or proof of residency. |
| micro-ipr-P17891 | https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/P17891/?page_size=200; InterPro all-entry/member matches for exact UniProt P17891; full returned page, count4, next=None | context_only | Bounded constituent family matches: IPR000996 Clathrin light chain; PF01086 Clathrin light chain; PTHR10639 CLATHRIN LIGHT CHAIN. Distinct protein families support heterogeneous coat scope; none is promoted to exact identity of the entire clathrin/COPI/COPII parent cohort or proof of residency. |
| micro-ipr-Q04491 | https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/Q04491/?page_size=200; InterPro all-entry/member matches for exact UniProt Q04491; full returned page, count11, next=None | context_only | Bounded constituent family matches: IPR037363 Sec13/Seh1 family; PTHR11024 NUCLEAR PORE COMPLEX PROTEIN SEC13 / SEH1 FAMILY MEMBER. Distinct protein families support heterogeneous coat scope; none is promoted to exact identity of the entire clathrin/COPI/COPII parent cohort or proof of residency. |
| micro-ipr-P38968 | https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/P38968/?page_size=200; InterPro all-entry/member matches for exact UniProt P38968; full returned page, count23, next=None | context_only | Bounded constituent family matches: IPR040251 Protein transport protein SEC31-like; PF07304 Steroid receptor RNA activator (SRA1); PF11549 Protein transport protein SEC31; PTHR13923 SEC31-RELATED PROTEIN. Distinct protein families support heterogeneous coat scope; none is promoted to exact identity of the entire clathrin/COPI/COPII parent cohort or proof of residency. |
| micro-ipr-P41810 | https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/P41810/?page_size=200; InterPro all-entry/member matches for exact UniProt P41810; full returned page, count15, next=None | context_only | Bounded constituent family matches: IPR016460 Coatomer beta subunit (COPB1); PIRSF005727 Coatomer, beta subunit; PTHR10635 COATOMER SUBUNIT BETA. Distinct protein families support heterogeneous coat scope; none is promoted to exact identity of the entire clathrin/COPI/COPII parent cohort or proof of residency. |
| micro-ipr-P53622 | https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/P53622/?page_size=200; InterPro all-entry/member matches for exact UniProt P53622; full returned page, count29, next=None | context_only | Bounded constituent family matches: IPR016391 Coatomer subunit alpha; IPR050844 Coatomer complex subunit; PIRSF003354 Coatomer, alpha subunit; PTHR19876 Coatomer complex subunit. Distinct protein families support heterogeneous coat scope; none is promoted to exact identity of the entire clathrin/COPI/COPII parent cohort or proof of residency. |
| micro-adapter-catalogue | https://imodulondb.org/api/datasets; Complete official iModulonDB organism/dataset catalogue | supports | No Saccharomyces, Komagataella or Pichia dataset appears in the returned catalogue; thus no matched-organism gene/module query is justified. This coverage limit does not establish biological absence. |
| micro-historical-adapter-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Retained00:49Z kg-microbe-sources imodulondb datasets receipt, actual stderr/exit | context_only | Earlier actual invocation returned1 due to PermissionError opening pyvenv.cfg. This is a historical unavailable runner observation, not a fresh invocation or successful execution. Current official source catalogue was inspected as permitted fallback. |
| septin-review-policy | .claude/skills/review-yaml-record/SKILL.md; Structured Source Cross-Checks and immutable review workflow | supports | Named molecular or pathway assertions trigger applicability even when in narrative context. Absence of transcriptomic claims is not an exemption. An unmatched organism permits bounded downstream non-applicability. |
| septin-curation-policy | docs/CURATION.md; Structure identity, parthood, component grounding and source scope | supports | Whole structures, constituent material and spatial regions are distinct. Optional inventories do not require unsupported constituents. Constitution, association and experimental formation dependency must not be conflated. |
| septin-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; NONMECHANISTIC graph scope and material component_ref | supports | Descriptive identity, parthood and enclosure may be nonmechanistic. Structural-material representation does not establish individual molecular formation necessity. |
| septin-record-clathrin_coated_endocytic_vesicle | data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle.yaml; Entire current maintained record at cee44c9b340b36e4e103ebd16c4bfcf6745bd41f | supports | Full identity, history, definitions, parent/part boundaries, components where present, taxonomic examples, functions, graph, evidence and discussions read. No images, measurements or verbatim snippets are declared. |
| septin-original-clathrin_coated_endocytic_vesicle | reviews/structured/20261021T111328Z-clathrin-coated-endocytic-vesicle-audit/review.yaml; Entire original YAML/Markdown pair, frozen record hash, checks, source tiers, assessments, verdict and empty findings/actions | supports | Original pass_with_limitations has no scientific finding or request-curation action. Its record bytes remain current. Historical source access and checks are not promoted to current execution. |
| septin-original-validation-clathrin_coated_endocytic_vesicle | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/adversary-septin/original-checks.json; 20261021T111328Z-clathrin-coated-endocytic-vesicle-audit native validate/render; original source/current target hashes | supports | Both commands exit0 and rendered Markdown is byte-identical. Current record bytes equal the original frozen hash and bytes at the historical source revision. |
| septin-native-clathrin_coated_endocytic_vesicle-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/clathrin_coated_endocytic_vesicle-uniprot-verify-receipt.json; Actual root command receipt plus /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/clathrin_coated_endocytic_vesicle-uniprot-verify.log | supports | Exit0. No protein_examples, UniProtKB protein xrefs or GENE_OR_PROTEIN graph nodes are declared. Zero typed protein nodes means this success does not independently verify narrative clathrin/adaptor identity, localization, pathway mechanism or formation necessity. |
| septin-native-clathrin_coated_endocytic_vesicle-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/clathrin_coated_endocytic_vesicle-uniprot-causal-receipt.json; Actual root command receipt plus /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/clathrin_coated_endocytic_vesicle-uniprot-causal.log | supports | Exit0. No protein_examples, UniProtKB protein xrefs or GENE_OR_PROTEIN graph nodes are declared. Zero typed protein nodes means this success does not independently verify narrative clathrin/adaptor identity, localization, pathway mechanism or formation necessity. |
| septin-record-clathrin_coated_endocytic_vesicle_lumen | data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_lumen.yaml; Entire current maintained record at cee44c9b340b36e4e103ebd16c4bfcf6745bd41f | supports | Full identity, history, definitions, parent/part boundaries, components where present, taxonomic examples, functions, graph, evidence and discussions read. No images, measurements or verbatim snippets are declared. |
| septin-original-clathrin_coated_endocytic_vesicle_lumen | reviews/structured/20261021T111329Z-clathrin-coated-endocytic-vesicle-lumen-audit/review.yaml; Entire original YAML/Markdown pair, frozen record hash, checks, source tiers, assessments, verdict and empty findings/actions | supports | Original pass_with_limitations has no scientific finding or request-curation action. Its record bytes remain current. Historical source access and checks are not promoted to current execution. |
| septin-original-validation-clathrin_coated_endocytic_vesicle_lumen | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/adversary-septin/original-checks.json; 20261021T111329Z-clathrin-coated-endocytic-vesicle-lumen-audit native validate/render; original source/current target hashes | supports | Both commands exit0 and rendered Markdown is byte-identical. Current record bytes equal the original frozen hash and bytes at the historical source revision. |
| septin-native-clathrin_coated_endocytic_vesicle_lumen-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/clathrin_coated_endocytic_vesicle_lumen-uniprot-verify-receipt.json; Actual root command receipt plus /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/clathrin_coated_endocytic_vesicle_lumen-uniprot-verify.log | supports | Exit0. No protein_examples, UniProtKB protein xrefs or GENE_OR_PROTEIN graph nodes are declared. Zero typed protein nodes means this success does not independently verify narrative clathrin/adaptor identity, localization, pathway mechanism or formation necessity. |
| septin-native-clathrin_coated_endocytic_vesicle_lumen-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/clathrin_coated_endocytic_vesicle_lumen-uniprot-causal-receipt.json; Actual root command receipt plus /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/clathrin_coated_endocytic_vesicle_lumen-uniprot-causal.log | supports | Exit0. No protein_examples, UniProtKB protein xrefs or GENE_OR_PROTEIN graph nodes are declared. Zero typed protein nodes means this success does not independently verify narrative clathrin/adaptor identity, localization, pathway mechanism or formation necessity. |
| septin-record-clathrin_coated_endocytic_vesicle_membrane | data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_membrane.yaml; Entire current maintained record at cee44c9b340b36e4e103ebd16c4bfcf6745bd41f | supports | Full identity, history, definitions, parent/part boundaries, components where present, taxonomic examples, functions, graph, evidence and discussions read. No images, measurements or verbatim snippets are declared. |
| septin-original-clathrin_coated_endocytic_vesicle_membrane | reviews/structured/20261021T111329Z-clathrin-coated-endocytic-vesicle-membrane-audit/review.yaml; Entire original YAML/Markdown pair, frozen record hash, checks, source tiers, assessments, verdict and empty findings/actions | supports | Original pass_with_limitations has no scientific finding or request-curation action. Its record bytes remain current. Historical source access and checks are not promoted to current execution. |
| septin-original-validation-clathrin_coated_endocytic_vesicle_membrane | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/adversary-septin/original-checks.json; 20261021T111329Z-clathrin-coated-endocytic-vesicle-membrane-audit native validate/render; original source/current target hashes | supports | Both commands exit0 and rendered Markdown is byte-identical. Current record bytes equal the original frozen hash and bytes at the historical source revision. |
| septin-native-clathrin_coated_endocytic_vesicle_membrane-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/clathrin_coated_endocytic_vesicle_membrane-uniprot-verify-receipt.json; Actual root command receipt plus /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/clathrin_coated_endocytic_vesicle_membrane-uniprot-verify.log | supports | Exit0. No protein_examples, UniProtKB protein xrefs or GENE_OR_PROTEIN graph nodes are declared. Zero typed protein nodes means this success does not independently verify narrative clathrin/adaptor identity, localization, pathway mechanism or formation necessity. |
| septin-native-clathrin_coated_endocytic_vesicle_membrane-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/clathrin_coated_endocytic_vesicle_membrane-uniprot-causal-receipt.json; Actual root command receipt plus /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/clathrin_coated_endocytic_vesicle_membrane-uniprot-causal.log | supports | Exit0. No protein_examples, UniProtKB protein xrefs or GENE_OR_PROTEIN graph nodes are declared. Zero typed protein nodes means this success does not independently verify narrative clathrin/adaptor identity, localization, pathway mechanism or formation necessity. |
| septin-context-clathrin_coat_of_endocytic_vesicle | data/structures/other/clathrin_coat_of_endocytic_vesicle.yaml; Frozen identity, definition, parent/part and component fields only | supports | Boundary context only: the generic class/lumen/material differs from the endocytic-specific target, while the coat neighbor carries lower-level proteins. No independent verification of neighbor protein accessions or whole-neighbor finding disposition is asserted. |
| septin-context-clathrin_coated_vesicle | data/structures/membrane_organelle/clathrin_coated_vesicle.yaml; Frozen identity, definition, parent/part and component fields only | supports | Boundary context only: the generic class/lumen/material differs from the endocytic-specific target, while the coat neighbor carries lower-level proteins. No independent verification of neighbor protein accessions or whole-neighbor finding disposition is asserted. |
| septin-context-clathrin_coated_vesicle_lumen | data/structures/membrane_organelle/clathrin_coated_vesicle_lumen.yaml; Frozen identity, definition, parent/part and component fields only | supports | Boundary context only: the generic class/lumen/material differs from the endocytic-specific target, while the coat neighbor carries lower-level proteins. No independent verification of neighbor protein accessions or whole-neighbor finding disposition is asserted. |
| septin-context-clathrin_coated_vesicle_membrane | data/structures/membrane_organelle/clathrin_coated_vesicle_membrane.yaml; Frozen identity, definition, parent/part and component fields only | supports | Boundary context only: the generic class/lumen/material differs from the endocytic-specific target, while the coat neighbor carries lower-level proteins. No independent verification of neighbor protein accessions or whole-neighbor finding disposition is asserted. |
| septin-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0045334,GO:0106176,GO:0030669,GO:0030136,GO:0030139,GO:0030128,GO:0072583,GO:0071682,GO:0030665,GO:0030666; All ten exact returned terms: identifiers, active status, namespace, definitions and relevant typed children | supports | GO identifies whole endocytic vesicle GO0045334, membrane GO0030669, lumen GO0106176 and coat GO0030128 separately. The whole is both clathrin-coated and endocytic; membrane has both membrane subtype parents; lumen has endocytic-lumen parent and whole-vesicle parthood. Exact process GO0072583 describes clathrin-coated pit internalization. No cargo identity or universal clathrin necessity follows. |
| septin-ancestors-0045334 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0045334/ancestors?relations=is_a,part_of; Complete exact term ancestors response restricted to is_a and part_of | supports | Requested typed ancestor closure corroborates containment/type hierarchy; it is not itself an experimental mechanism or a formal bounding-layer axiom. |
| septin-ancestors-0106176 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0106176/ancestors?relations=is_a,part_of; Complete exact term ancestors response restricted to is_a and part_of | supports | Requested typed ancestor closure corroborates containment/type hierarchy; it is not itself an experimental mechanism or a formal bounding-layer axiom. |
| septin-ancestors-0030669 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030669/ancestors?relations=is_a,part_of; Complete exact term ancestors response restricted to is_a and part_of | supports | Requested typed ancestor closure corroborates containment/type hierarchy; it is not itself an experimental mechanism or a formal bounding-layer axiom. |
| septin-go-edit | https://raw.githubusercontent.com/geneontology/go-ontology/master/src/ontology/go-edit.obo; Only exact stanzas GO0030669, GO0045334, GO0106176 and GO0030128 from official source ontology; extracted stanzas at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/adversary-septin/go-edit-target-terms.json | supports | The official GO0030669 stanza explicitly has intersection_of membrane and bounding_layer_of GO0045334, plus part_of GO0045334 and both membrane is-a parents. GO0030128 is part_of GO0030669. The lumen stanza has GO0071682 parent and part_of GO0045334. Thus maintained bounds/parthood notes have formal ontology support; no ontology-wide scientific audit is claimed. |
| septin-SL-0319 | https://rest.uniprot.org/locations/SL-0319.json; Native id/name/definition, top-level fields, isA/partOf hierarchy; no protein-list interpretation | supports | SL0319 identifies the generic clathrin-coated vesicle lumen and partOf generic clathrin-coated vesicle. It has no top-level geneOntologies mapping; nested parent mappings do not make it identical to endocytic-specific GO0106176. The maintained local generic-lumen parent remains broader. |
| septin-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete ENA taxId, scientificName, rank, lineage and aliases | supports | NCBITaxon4932 is species Saccharomyces cerevisiae. Taxonomy verifies identity, not strain-specific prevalence or a measured COMMON frequency. |
| septin-newpher-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.devcel.2005.04.014&amp;pageSize=25; Europe PMC exact DOI result: complete abstract and title/authors/DOI/PMID/journal/year | supports | Newpher, Smith, Lemmon and Lemmon2005, PMID15992543, describes cortical clathrin, Abp1/cargo association and adaptor-dependent recruitment in yeast. This is the complete primary abstract and exact bibliography, not independent verification of all figures or released-vesicle ultrastructure. |
| septin-kaksonen-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.cell.2005.09.024&amp;pageSize=25; Europe PMC exact DOI result: complete abstract and title/authors/DOI/PMID/journal/year | supports | Kaksonen, Toret and Drubin2005, PMID16239147, complete primary abstract describes deletion-mutant/live-imaging evidence for coat, invagination, actin and scission modules. It explicitly finds clathrin facilitates initiation but is not necessary for membrane invagination or vesicle formation in that yeast system. This is abstract-only experimental scope, not a Methods/Results body read. |
| septin-newpher-duke | https://dukespace.lib.duke.edu/server/api/core/bitstreams/e3c70c30-e4a1-4ba0-8ea6-c50af4ba491e/content; Fresh readable publisher-format PDF in Duke repository: printed pp87–96 Summary/Introduction, Table1, selected Results Localization of Clathrin In Vivo, cargo/cortical association, Transient Association and Cortical Recruitment; Discussion and Experimental Procedures/Microscopy text. Captions are text only. | supports | Actual primary body supports dynamic cortical clathrin/adaptor recruitment in S. cerevisiae, with wt reporter strains and mutant/LAT-A conditions distinguished. Table1 names laboratory strains; cells generally grown30C, live microscopy uses mid-log synthetic cultures. Cortical events are distinct from internal TGN/endosomal clathrin. Discussion p95 explicitly cannot distinguish clathrin disassembly before budding from a clathrin-bearing vesicle or bud leaving the TIRF field. This source supports model-site dynamics, not resolved sealed lumen, universal retained coat or direct proof every budding event forms a coated carrier. No full image/movie/raw-data audit is claimed. |
| septin-catalogue | https://imodulondb.org/api/datasets; Complete official /api/datasets response: every organism id/name and its dataset keys | supports | No organism/dataset matches Saccharomyces cerevisiae in this complete current response. Named clathrin/adaptor and endocytosis context merits applicability assessment, but uncovered organism scope makes downstream gene/module lookup not applicable. No unrelated species is substituted, and noncoverage is not negative biological evidence. |
| septin-historical-adapter-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Actual canary command00:49:00.848907Z–00:49:00.863225Z | supports | Historical datasets invocation exited1 with OS PermissionError reading runner pyvenv.cfg. This retained receipt is not a fresh attempt or a successful adapter run. Current official catalogue fallback was fetched separately. |
| septin-access-source-receipts | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/adversary-septin/source-receipts.json; Actual request timestamps, outcomes and saved successful-body hashes | supports | Fresh authority/primary/catalogue requests succeeded except Kaksonen publisher PDF HTTP403. Newpher is a genuine PDF; no challenge page is treated as article body. |
| septin-access-extra-receipts | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/adversary-septin/extra-receipts.json; Actual request timestamps, outcomes and saved successful-body hashes | supports | Kaksonen CORE public mirror returned403; attempted detailed OLS term URL returned404. Neither supplied source body or contrary scientific evidence. Exact ontology axioms were subsequently checked at the official GO source. |
| septin-bounded-source-search | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/adversary-septin/browser-search.json; Only first returned result set for two exact queries; source discovery only | supports | Exact publication/ontology search results were used as retrieval leads. Native source responses, complete abstracts and inspected Newpher PDF provide scientific support. Third-party summaries, unrelated records and search-result absence are not used to establish claims. |
| check-qc | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/qc.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| check-labels | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/labels.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| check-trait-links | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/trait-links.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Native TraitMech link check passed. |
| check-vendored | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/vendored.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Pinned governed files match; native vendored check passed. |
| check-curies | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/curies.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| focused | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/focused-results.json; All twenty actual target schema/strict command outputs | supports | Ten schema and ten strict commands returned exit zero. |
| supplemental-pmid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/pmid-chunks-receipt.json; Complete native-report PMID set checked with unchanged resolver in batches of at most fifty | supports | 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers remain unverified. |
| historical-adapter-runner-availability | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner invocation receipt, cross-checked against exact stdout/stderr hashes; reread during PR2360 synthesis | context_only | Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS PermissionError reading the configured runner pyvenv.cfg. This is a retained historical availability observation, not a fresh attempt or a scientific validation failure. Native policy permits inspected source-catalogue fallback. |

## Limits And Additional Notes

- Generic clathrin-coated vesicle, lumen, membrane and coccolith vesicle independent subreview: Assigned four records only; all four frozen target hashes remain unchanged. Three additional neighbors were frozen before boundary/component-label inspection and are not fully reviewed or terminally disposed of.
- Generic clathrin-coated vesicle, lumen, membrane and coccolith vesicle independent subreview: Newpher2005 is a genuine fresh primary PDF, text of pp87–96 including Methods and figure captions. No figure pixels, movies, supplementary experiments or raw quantitative data were reanalyzed. The primary paper cannot distinguish pre-budding clathrin loss from departure of coated vesicles from the surface field.
- Generic clathrin-coated vesicle, lumen, membrane and coccolith vesicle independent subreview: Kaksonen2005 support is the complete primary abstract only; attempted CORE/publisher/PDF routes were403 and the ElsevierAPI is bibliographic metadata. Newpher DOI redirect response is not its body; the separate institutional PDF supplies actual body access.
- Generic clathrin-coated vesicle, lumen, membrane and coccolith vesicle independent subreview: Yeast COMMON scope is qualitative; reporter recruitment does not directly image a sealed lumen or establish individual assembly necessity. Constitutional collective bilayer differs from necessity of each lipid species.
- Generic clathrin-coated vesicle, lumen, membrane and coccolith vesicle independent subreview: Avrahami2026 scientific sec1–4 and source captions were read in full; supplementary Methods were read through FIB-SEM data processing, not audited in entirety. Sviben2016 scope is Results sec4–6, Discussion sec7 and culture Methods sec9.
- Generic clathrin-coated vesicle, lumen, membrane and coccolith vesicle independent subreview: Only the maintained Figure2 pixels were viewed. Figure3–7 captions were text evidence; cryo-ET, XRF maps, raw reconstructions and supplementary microscopy were not reanalyzed. Fresh Figure2 bytes, metadata, authors and ALI CC-BY4.0 match the frozen record.
- Generic clathrin-coated vesicle, lumen, membrane and coccolith vesicle independent subreview: Current authority searches retain exact bounds: two coccolith queries return0; clathrin-lumen query inspected first100 of651 hits and does not certify exhaustive absence. A narrower endocytic-lumen term is not the exact broader target. Historical record searches and issue resolutions are not recertified.
- Generic clathrin-coated vesicle, lumen, membrane and coccolith vesicle independent subreview: Fresh complete structured-source catalogue lacks matched yeast/coccolithophore hosts. No downstream matched-dataset query applies and no biological absence follows. Historical00:49Z OS-access runner failure is retained, not a new invocation or success.
- Generic clathrin-coated vesicle, lumen, membrane and coccolith vesicle independent subreview: Clathrin lumen has explicit molecular recruitment narratives despite sparse geometry, so it belongs among the three applicability corrections. Coccolith is genuinely excluded because candidate molecular identities and mechanisms are expressly unasserted; its N/A outcome remains with a precise rationale.
- Generic clathrin-coated vesicle, lumen, membrane and coccolith vesicle independent subreview: All eight native protein commands pass empty inventories and zero typed protein nodes. They cannot verify narrative molecular identity, localization, function or necessity. Root owns full-corpus gates, issue deduplication/publication and all repository/GitHub writes.
- Cis-Golgi network membrane, coated vesicle and coated vesicle membrane independent subreview: Assigned scope comprises cis-Golgi network membrane, coated vesicle and coated vesicle membrane. All are unchanged. Six frozen neighbors were read only at declared boundary fields; their scientific findings and category/group issues are not resolved or conflated.
- Cis-Golgi network membrane, coated vesicle and coated vesicle membrane independent subreview: Cis-Golgi sources reuse verified unchanged10:11Z public snapshots from the immediately prior review. Rossanese full Results/Discussion and Strains and Plasmids Methods were previously inspected and the strain/interface passages reread here; no new source download, figure-pixel audit or broader full-Methods/supplement scope is claimed. ATCC and ENA identify strain only.
- Cis-Golgi network membrane, coated vesicle and coated vesicle membrane independent subreview: Cho2000 remains complete primary abstract only; historical attempted body/PDF403 remains an access limitation. It concerns S. cerevisiae early-Golgi membranes and does not directly establish K. phaffii CGN membrane occurrence.
- Cis-Golgi network membrane, coated vesicle and coated vesicle membrane independent subreview: Barlowe1994 is current complete primary abstract/bibliography only. Current publisher and ScienceDirect requests returned403. Matsuoka author-hosted PDF is genuinely readable at the exact selected pages/sections declared; neither source is represented as a full-paper/raw-data or image-pixel audit.
- Cis-Golgi network membrane, coated vesicle and coated vesicle membrane independent subreview: Newpher2005 current institutional PDF was read at pp87-89 Summary/Introduction/Table1/Localization subsection/Figure1 caption only; no later experiments, movies or pixels were reanalyzed. Yu2012 current genuine JATS was read at complete Introduction and two declared Results/model subsections, not full Methods/figures/raw data.
- Cis-Golgi network membrane, coated vesicle and coated vesicle membrane independent subreview: Rout2000 and Huh2003 are complete primary abstract only plus exact UniProt source annotations. The record explicitly identifies nuclear-pore and Golgi-membrane annotations; these are not direct vesicle-membership experiments.
- Cis-Golgi network membrane, coated vesicle and coated vesicle membrane independent subreview: S288C protein examples are representative identity anchors, not asserted experimental strain matches for RSY445 or every source. Current query uniqueness is bounded to seven exact symbols/taxon559292/reviewed filters and does not certify historical results. Protein/domain matches do not identify a universal composite coat family.
- Cis-Golgi network membrane, coated vesicle and coated vesicle membrane independent subreview: Current catalogue returned no matching yeast dataset. Historical runner PermissionError occurred00:49Z and was not rerun here; current fallback is separately timestamped. Absence of a matching dataset is not biological absence or a fabricated downstream gene/module check.
- Cis-Golgi network membrane, coated vesicle and coated vesicle membrane independent subreview: Six native protein commands passed; two membrane targets have empty inventories/zero protein nodes and whole coated vesicle has six examples/one COVERED node. Native success does not repair unsupported prose or establish assembly necessity.
- Cis-Golgi network membrane, coated vesicle and coated vesicle membrane independent subreview: No assigned target contains an image or numerical property requiring pixel/measurement inspection. The other cohort coccolith image is outside this subreview. Root owns full local QC, global authority checks, issue deduplication/publication and final integration; no future final-head CI claim is made.
- Clathrin-coated endocytic vesicle, lumen and membrane independent subreview: Assigned three unchanged endocytic clathrin targets only. All original bundles validate/render exactly and target hashes equal original frozen/source bytes. No original scientific findings or request-curation actions exist.
- Clathrin-coated endocytic vesicle, lumen and membrane independent subreview: Fresh Newpher publisher-format Duke PDF was inspected at declared Summary/Introduction, Table1, selected Results, Discussion and Experimental Procedures/Microscopy text on printed pp87–96. Captions are text only; no figure pixels, supplementary movies or raw microscopy were reanalysed.
- Clathrin-coated endocytic vesicle, lumen and membrane independent subreview: Newpher does not resolve clathrin disassembly before budding versus departure of a clathrin-bearing vesicle/bud outside the TIRF field. The yeast example is a recruitment/endocytic-site model, not direct visualization of a sealed lumen or universal retained coat.
- Clathrin-coated endocytic vesicle, lumen and membrane independent subreview: Kaksonen primary support is complete native abstract and bibliography only. Publisher PDF and CORE routes returned403; no full Methods/Results body or figure audit is claimed. Its clathrin-necessity result remains specific to the studied yeast assay.
- Clathrin-coated endocytic vesicle, lumen and membrane independent subreview: Formal GO bounding_layer_of and coat part_of assertions were read directly from four selected official source-ontology stanzas after the OLS route returned404. No whole-ontology audit or inference from failed access is made.
- Clathrin-coated endocytic vesicle, lumen and membrane independent subreview: Species identity and qualitative COMMON scope do not establish prevalence across strains/conditions. Source wt reporter, mutant and drug-treated observations are kept distinct; neighbor protein accessions are context only, not independently audited target claims.
- Clathrin-coated endocytic vesicle, lumen and membrane independent subreview: All three targets contain actual clathrin/adaptor narrative despite zero typed protein nodes; even the lumen merits applicability assessment. The complete current catalogue has no matched S. cerevisiae dataset. No unrelated taxon query or absence-of-biology inference is made. Historical runner failure remains00:49Z, not a fresh execution.
- Clathrin-coated endocytic vesicle, lumen and membrane independent subreview: All six current protein commands pass empty inventories; they do not independently validate narrative molecules, localization, mechanism or formation necessity. Root owns global gates and final CI/queue checks.
- Clathrin-coated endocytic vesicle, lumen and membrane independent subreview: Whole-vesicle constituent responsibility, collective membrane material and spatial lumen/cargo boundaries are distinct. No unsupported invariant protein/cargo inventory, exact lipid grounding or universal individual formation requirement is added.
- Clathrin-coated endocytic vesicle, lumen and membrane independent subreview: Four frozen neighbors were inspected only for declared identity/boundary/component context. No historical grouped/category finding or neighboring record issue is terminally resolved. Repository/GitHub writes and issue deduplication/publication remain root-owned.
- Historical observations remain immutable; their old checks are not represented as current-head execution.
- The adapter runner was not rerun after the canary established OS access failure. Catalogue-based coverage is assessed directly; fresh and reused responses retain actual access timestamps.
- Native label checks include 923 no-adapter skips. Native identifier checks include 909 PMID transport failures and 254 skipped identifiers; bounded supplemental checks independently resolve the 909 PMIDs.
- Scientific record-curation findings stay in separate issues; no record is edited by this review PR.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after saving this immutable observation and are not represented here as already completed.
- All ten original YAML/Markdown pairs remain unchanged. Current main was merged normally and pushed without force.
- This explicit issue-bearing ten-record cohort follows the native persistence policy. Each inherited scientific finding retains exact predecessor identity.
- All ten original target hashes match current main. No stale target review requires a content refresh, but current claim-level source reassessment and bundle corrections are recorded in this immutable successor.
- Issue #2664 tracks one omitted applicability assessment and eight unsupported expression-only exclusions. Clathrin lumen narratives name molecular recruitment and therefore require assessment; coccolith vesicle is a genuine exclusion because molecular identities and transport machinery are explicitly withheld.
- Source commit cee44c9b340b36e4e103ebd16c4bfcf6745bd41f is retained by tag review-base/pr2360-current-record-followup-20261103.
- CLAUDE.md is an alias of AGENTS.md; canonical regular AGENTS.md bytes are frozen.
- All used local context was frozen before assessment, including nine neighbor records, the coccolith image, native configuration, graph/protein policies and verifier source. Neighbors are context only, not additional targets or dispositions of their findings.
- Fresh and reused public-source snapshots retain actual access dates and inspection tiers. Native authority identity does not independently establish localization, mechanistic action or assembly necessity.
- Native checks with empty protein inventories or zero GENE_OR_PROTEIN nodes do not validate molecules appearing only in narrative prose. The coated-vesicle graph has one covered molecular node linked to its represented component examples; that coverage does not establish query uniqueness or assembly necessity.
- The two major cis-Golgi network membrane findings concern current PPY12 species attribution and the distinction between whole-stack evidence and the specific CGN membrane. Related #2661 and #2662 concern the separate whole-network record; neither those issues nor #2663 are resolved here.
- The minor coated-vesicle RET1 finding concerns exact query uniqueness. Valid representative accessions and their supported roles are preserved; primary symbol and synonym matches are distinguished.
- The coccolith source figure supports observed membrane geometry and reconstructed stages, not time-lapse continuity or specified transport machinery. Its attached image, strain context, modality and licence are independently assessed.
- All three inherited scientific findings remain open for separate record curation. Eight targets retain qualified positive scientific assessments. No record is edited.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T105612Z-pr2360-current-record-followup
kind: batch
repository: CultureBotAI/CellStructureMech
title: 'PR 2360: current-input review of ten records and adversarial follow-up'
started_at: '2026-11-03T10:48:58.638483Z'
finished_at: '2026-11-03T10:56:12Z'
reviewer:
  identity: Codex root synthesis with three independent read-only adversarial reviewers
  kind: agent
  independence: self_review
  independence_basis: Root authors this synthesis of three separate read-only reviews.
    Independent reviewers inspected original bundles, current record bytes and primary/authority
    sources, and did not author or modify repository files. They independently re-review
    the final saved head before publication. This is not human scientific sign-off.
skill: .claude/skills/review-yaml-record/SKILL.md; explicit batch route in docs/record-review-profile.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Current-input reassessment of all ten records in PR2360. All original target
  hashes remain current. Independent source assessments retain three inherited scientific
  findings and correct nine structured-source applicability assessments without editing
  records.
source:
  git_revision: cee44c9b340b36e4e103ebd16c4bfcf6745bd41f
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
  - path: data/images/membrane_organelle/coccolith_vesicle/pmc13067266_fig2.jpg
    sha256: f41e31add721c5f01869b2ce9ebe38b8aa7add53acb9a6445f6d2335858d2020
    role: context
  - path: data/structures/envelope/coccolith.yaml
    sha256: 8932b1ad635cf2e272c74fb8d4f00e6036b851ec2baa3daa3b5c3b52cc6979fa
    role: context
  - path: data/structures/envelope/coccosphere.yaml
    sha256: b72167a6093a734226fc2c9458c475f7a05120e8d2077d5f7b7007ee0a5cd299
    role: context
  - path: data/structures/membrane_organelle/cis_golgi_network.yaml
    sha256: 369cae5270aeacd25a94317be3b005167773bd89a5e4c2583061fa24cd79f31d
    role: context
  - path: data/structures/membrane_organelle/cis_golgi_network_membrane.yaml
    sha256: c818f4de1c2fd8c36bc121d4389ce017c59526e083e6aefdf1b2a0041411da9c
    role: target
  - path: data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle.yaml
    sha256: 3193e3f6ea811d515c1545dc4e9179c8122e8718a328ed11261c7b648e94343d
    role: target
  - path: data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_lumen.yaml
    sha256: d3a53daa5cc28635e48242bfa4d7dab04186a8c7f17b40a1491de51e94a33951
    role: target
  - path: data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_membrane.yaml
    sha256: 70d8d315440e5cc7cc4c8f8c11a9103d74deffa773df25d9051113122d8a189a
    role: target
  - path: data/structures/membrane_organelle/clathrin_coated_vesicle.yaml
    sha256: cee241afc73475bcdec9d8c3c4c57bdf9c4cb2f726e4a78615dfb393613be9ad
    role: target
  - path: data/structures/membrane_organelle/clathrin_coated_vesicle_lumen.yaml
    sha256: 2137a192f721232651c140497813cea3f15a73a67e910194d59fadc7837308f9
    role: target
  - path: data/structures/membrane_organelle/clathrin_coated_vesicle_membrane.yaml
    sha256: 963e3cbe094c98b1279923d8f4ecc6a27343f82aa7240dece427fa09882c25f1
    role: target
  - path: data/structures/membrane_organelle/coated_vesicle.yaml
    sha256: baf2f374fd87cb07f0ae0a31c5962cfa34c345941f872a96759858c88c8218c1
    role: target
  - path: data/structures/membrane_organelle/coated_vesicle_membrane.yaml
    sha256: b74f6c754d374d664267834c903c7bb2aed86f79145de8ce69f6ea9785bbebcc
    role: target
  - path: data/structures/membrane_organelle/coccolith_vesicle.yaml
    sha256: 89b7e793211332507189d1ba872fc1eb901cf8703323853cd10d65b45e971655
    role: target
  - path: data/structures/membrane_organelle/golgi_apparatus.yaml
    sha256: e3df76cd9d71ba04df9e5349475bd4191c31f93156acd422ef6b0223b88facca
    role: context
  - path: data/structures/other/clathrin_coat_of_endocytic_vesicle.yaml
    sha256: 04cd29ffe90456d0dc2acbe6dbba20bd061587015653a0bea6d7259c1c7f6220
    role: context
  - path: data/structures/other/clathrin_vesicle_coat.yaml
    sha256: cef674eb9fc2b08323c1780daa340012db00fd43e3f89c7de880ac972594e17d
    role: context
  - path: data/structures/other/copi_vesicle_coat.yaml
    sha256: 1b264ad3800f2c5c8c78d327f63a32bdc73888a003e3be3fcad778bb9f993195
    role: context
  - path: data/structures/other/copii_vesicle_coat.yaml
    sha256: 3b7c89b408581ddfd7f40203a1810eda738e87b1d2457812209b8586abbb0ef2
    role: context
  - path: data/structures/other/vesicle_coat.yaml
    sha256: d8bd367b310d26010f7c909b47b7e5b8676be216b22e81a69eab083d506c3818
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
  - path: reviews/structured/20261021T111327Z-cis-golgi-network-membrane-audit/review.md
    sha256: 4bd894b6f821dac6d3cbde1c056361ab3fd2154e05cd93c618a3ef2074e49672
    role: context
  - path: reviews/structured/20261021T111327Z-cis-golgi-network-membrane-audit/review.yaml
    sha256: c2cb05552b9ddc319f82c78f28c7e7b76b653cf0bfb30fac5fac3babdb7b8562
    role: context
  - path: reviews/structured/20261021T111328Z-clathrin-coated-endocytic-vesicle-audit/review.md
    sha256: 716b3c876839d077133897d4ebd2f8c9e4dd5710b4f6368e2a941105db2de5b0
    role: context
  - path: reviews/structured/20261021T111328Z-clathrin-coated-endocytic-vesicle-audit/review.yaml
    sha256: 6c8294738ce8825502a24e1ac67657062ce41feecca60a846364d259df1bb50e
    role: context
  - path: reviews/structured/20261021T111329Z-clathrin-coated-endocytic-vesicle-lumen-audit/review.md
    sha256: dfc4a09557c2000abafde33d56507326511aed0a993ab3d00bd4a6b2a5f805fd
    role: context
  - path: reviews/structured/20261021T111329Z-clathrin-coated-endocytic-vesicle-lumen-audit/review.yaml
    sha256: 04b141b90eac13e8f9763cb66ba3f35591dfdfca08cff3277995c6951bad78ee
    role: context
  - path: reviews/structured/20261021T111329Z-clathrin-coated-endocytic-vesicle-membrane-audit/review.md
    sha256: 06d59f53eba9d03dede6954cd7325ff08789c40604ff1eddf8e1b7519c1f20be
    role: context
  - path: reviews/structured/20261021T111329Z-clathrin-coated-endocytic-vesicle-membrane-audit/review.yaml
    sha256: ca324107ccb682459d538e6fdfebe6cba513319dcf615e44d2948637347327c4
    role: context
  - path: reviews/structured/20261021T111330Z-clathrin-coated-vesicle-audit/review.md
    sha256: 8269190d43d7708d72c5caa34ca89df814233ccb433431b64bacee7634f6872a
    role: context
  - path: reviews/structured/20261021T111330Z-clathrin-coated-vesicle-audit/review.yaml
    sha256: bd0476ce3500948f612015e0e396f0f40f58261544828f790f21a3fd850d6788
    role: context
  - path: reviews/structured/20261021T111331Z-clathrin-coated-vesicle-lumen-audit/review.md
    sha256: 638a9f35c595c2cb65d52102006cac618eb488182eec962997d3dc936a91453f
    role: context
  - path: reviews/structured/20261021T111331Z-clathrin-coated-vesicle-lumen-audit/review.yaml
    sha256: e937f1b6d79a0d6605221930b32ba918b9a14d5d2717dc8069b172e5b0ac6424
    role: context
  - path: reviews/structured/20261021T111332Z-clathrin-coated-vesicle-membrane-audit/review.md
    sha256: 78809acec87acd4bda16399f6ccfdb1ce559cd59932391e39bff71bd0e1eeaa7
    role: context
  - path: reviews/structured/20261021T111332Z-clathrin-coated-vesicle-membrane-audit/review.yaml
    sha256: 2bdb53c90a03960d886fa43d2d61c2e3f84e702b07dc71427ea6147217fd16d8
    role: context
  - path: reviews/structured/20261021T111333Z-coated-vesicle-audit/review.md
    sha256: 4953aa86b45069e0d7e30f78acf864f58d3f9dd603330b6c240e41ce6dacc53f
    role: context
  - path: reviews/structured/20261021T111333Z-coated-vesicle-audit/review.yaml
    sha256: 2d21b43cbb854d99973d35da5ee51136319c90bdc7fd1aa1f111f15441554b1c
    role: context
  - path: reviews/structured/20261021T111334Z-coated-vesicle-membrane-audit/review.md
    sha256: 33139e398bfb645af1606fbcf0f7cb516625cb8d76a24d6ed9263e82d766a95b
    role: context
  - path: reviews/structured/20261021T111334Z-coated-vesicle-membrane-audit/review.yaml
    sha256: 2232e0751eacf3e99b4e0f79257808634c6c51fe1e973c6947f80f5da7a5376a
    role: context
  - path: reviews/structured/20261021T111335Z-coccolith-vesicle-audit/review.md
    sha256: 13cf54c0c93c8fde4057d112324320345ebb3f1066cd65c7aa6f2bba29db78e8
    role: context
  - path: reviews/structured/20261021T111335Z-coccolith-vesicle-audit/review.yaml
    sha256: f23c52bba81f53d4af37baa17a353ef3c9aafb453a6ff1d857c1ee1622c8f1ff
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
- target_id: GO:0033106
  path: data/structures/membrane_organelle/cis_golgi_network_membrane.yaml
  label: cis-Golgi network membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cis_golgi_network_membrane.yaml
    role: maintained scientific record
- target_id: GO:0045334
  path: data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle.yaml
  label: clathrin-coated endocytic vesicle
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle.yaml
    role: maintained scientific record
- target_id: GO:0106176
  path: data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_lumen.yaml
  label: clathrin-coated endocytic vesicle lumen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_lumen.yaml
    role: maintained scientific record
- target_id: GO:0030669
  path: data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_membrane.yaml
  label: clathrin-coated endocytic vesicle membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_membrane.yaml
    role: maintained scientific record
- target_id: GO:0030136
  path: data/structures/membrane_organelle/clathrin_coated_vesicle.yaml
  label: clathrin-coated vesicle
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/clathrin_coated_vesicle.yaml
    role: maintained scientific record
- target_id: cellstructuremech:clathrin_coated_vesicle_lumen
  path: data/structures/membrane_organelle/clathrin_coated_vesicle_lumen.yaml
  label: clathrin-coated vesicle lumen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/clathrin_coated_vesicle_lumen.yaml
    role: maintained scientific record
- target_id: GO:0030665
  path: data/structures/membrane_organelle/clathrin_coated_vesicle_membrane.yaml
  label: clathrin-coated vesicle membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/clathrin_coated_vesicle_membrane.yaml
    role: maintained scientific record
- target_id: GO:0030135
  path: data/structures/membrane_organelle/coated_vesicle.yaml
  label: coated vesicle
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/coated_vesicle.yaml
    role: maintained scientific record
- target_id: GO:0030662
  path: data/structures/membrane_organelle/coated_vesicle_membrane.yaml
  label: coated vesicle membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/coated_vesicle_membrane.yaml
    role: maintained scientific record
- target_id: cellstructuremech:coccolith_vesicle
  path: data/structures/membrane_organelle/coccolith_vesicle.yaml
  label: coccolith vesicle
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/coccolith_vesicle.yaml
    role: maintained scientific record
scope:
  description: Exact ten-record PR cohort reassessed against current main 715c37405da56c249de0afa236041f70bdbc399f.
    Changed inputs are substantively reassessed. Scientific records remain unchanged.
  selection: Complete cohort of ten maintained records reviewed in original PR head
    652ff606a49dc8a55b0911b71b875818fceea691.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - GO:0033106
  - GO:0045334
  - GO:0106176
  - GO:0030669
  - GO:0030136
  - cellstructuremech:clathrin_coated_vesicle_lumen
  - GO:0030665
  - GO:0030135
  - GO:0030662
  - cellstructuremech:coccolith_vesicle
checks:
- check_id: qc
  name: Full native QC
  status: passed
  required: true
  target_ids:
  - GO:0033106
  - GO:0045334
  - GO:0106176
  - GO:0030669
  - GO:0030136
  - cellstructuremech:clathrin_coated_vesicle_lumen
  - GO:0030665
  - GO:0030135
  - GO:0030662
  - cellstructuremech:coccolith_vesicle
  command: just qc
  exit_code: 0
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  scope_note: Actual local execution at main-merge head cee44c9b340b36e4e103ebd16c4bfcf6745bd41f.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-qc
- check_id: labels
  name: Native label correspondence
  status: passed
  required: true
  target_ids:
  - GO:0033106
  - GO:0045334
  - GO:0106176
  - GO:0030669
  - GO:0030136
  - cellstructuremech:clathrin_coated_vesicle_lumen
  - GO:0030665
  - GO:0030135
  - GO:0030662
  - cellstructuremech:coccolith_vesicle
  command: just validate-products
  exit_code: 0
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  scope_note: Actual local execution at main-merge head cee44c9b340b36e4e103ebd16c4bfcf6745bd41f.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-labels
- check_id: trait-links
  name: TraitMech references
  status: passed
  required: true
  target_ids:
  - GO:0033106
  - GO:0045334
  - GO:0106176
  - GO:0030669
  - GO:0030136
  - cellstructuremech:clathrin_coated_vesicle_lumen
  - GO:0030665
  - GO:0030135
  - GO:0030662
  - cellstructuremech:coccolith_vesicle
  command: just check-trait-links --check
  exit_code: 0
  summary: Native TraitMech link check passed.
  scope_note: Actual local execution at main-merge head cee44c9b340b36e4e103ebd16c4bfcf6745bd41f.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-trait-links
- check_id: vendored
  name: Pinned governed files
  status: passed
  required: true
  target_ids:
  - GO:0033106
  - GO:0045334
  - GO:0106176
  - GO:0030669
  - GO:0030136
  - cellstructuremech:clathrin_coated_vesicle_lumen
  - GO:0030665
  - GO:0030135
  - GO:0030662
  - cellstructuremech:coccolith_vesicle
  command: just vendored-check
  exit_code: 0
  summary: Pinned governed files match; native vendored check passed.
  scope_note: Actual local execution at main-merge head cee44c9b340b36e4e103ebd16c4bfcf6745bd41f.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-vendored
- check_id: curies
  name: Native identifier resolver
  status: passed
  required: true
  target_ids:
  - GO:0033106
  - GO:0045334
  - GO:0106176
  - GO:0030669
  - GO:0030136
  - cellstructuremech:clathrin_coated_vesicle_lumen
  - GO:0030665
  - GO:0030135
  - GO:0030662
  - cellstructuremech:coccolith_vesicle
  command: just check-curies-strict
  exit_code: 0
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  scope_note: Actual local execution at main-merge head cee44c9b340b36e4e103ebd16c4bfcf6745bd41f.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-curies
- check_id: focused-0
  name: validate GO:0033106
  status: passed
  required: true
  target_ids:
  - GO:0033106
  command: just validate data/structures/membrane_organelle/cis_golgi_network_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-1
  name: validate-strict GO:0033106
  status: passed
  required: true
  target_ids:
  - GO:0033106
  command: just validate-strict data/structures/membrane_organelle/cis_golgi_network_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-2
  name: validate GO:0045334
  status: passed
  required: true
  target_ids:
  - GO:0045334
  command: just validate data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-3
  name: validate-strict GO:0045334
  status: passed
  required: true
  target_ids:
  - GO:0045334
  command: just validate-strict data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-4
  name: validate GO:0106176
  status: passed
  required: true
  target_ids:
  - GO:0106176
  command: just validate data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-5
  name: validate-strict GO:0106176
  status: passed
  required: true
  target_ids:
  - GO:0106176
  command: just validate-strict data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-6
  name: validate GO:0030669
  status: passed
  required: true
  target_ids:
  - GO:0030669
  command: just validate data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-7
  name: validate-strict GO:0030669
  status: passed
  required: true
  target_ids:
  - GO:0030669
  command: just validate-strict data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-8
  name: validate GO:0030136
  status: passed
  required: true
  target_ids:
  - GO:0030136
  command: just validate data/structures/membrane_organelle/clathrin_coated_vesicle.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-9
  name: validate-strict GO:0030136
  status: passed
  required: true
  target_ids:
  - GO:0030136
  command: just validate-strict data/structures/membrane_organelle/clathrin_coated_vesicle.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-10
  name: validate cellstructuremech:clathrin_coated_vesicle_lumen
  status: passed
  required: true
  target_ids:
  - cellstructuremech:clathrin_coated_vesicle_lumen
  command: just validate data/structures/membrane_organelle/clathrin_coated_vesicle_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-11
  name: validate-strict cellstructuremech:clathrin_coated_vesicle_lumen
  status: passed
  required: true
  target_ids:
  - cellstructuremech:clathrin_coated_vesicle_lumen
  command: just validate-strict data/structures/membrane_organelle/clathrin_coated_vesicle_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-12
  name: validate GO:0030665
  status: passed
  required: true
  target_ids:
  - GO:0030665
  command: just validate data/structures/membrane_organelle/clathrin_coated_vesicle_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-13
  name: validate-strict GO:0030665
  status: passed
  required: true
  target_ids:
  - GO:0030665
  command: just validate-strict data/structures/membrane_organelle/clathrin_coated_vesicle_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-14
  name: validate GO:0030135
  status: passed
  required: true
  target_ids:
  - GO:0030135
  command: just validate data/structures/membrane_organelle/coated_vesicle.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-15
  name: validate-strict GO:0030135
  status: passed
  required: true
  target_ids:
  - GO:0030135
  command: just validate-strict data/structures/membrane_organelle/coated_vesicle.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-16
  name: validate GO:0030662
  status: passed
  required: true
  target_ids:
  - GO:0030662
  command: just validate data/structures/membrane_organelle/coated_vesicle_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-17
  name: validate-strict GO:0030662
  status: passed
  required: true
  target_ids:
  - GO:0030662
  command: just validate-strict data/structures/membrane_organelle/coated_vesicle_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-18
  name: validate cellstructuremech:coccolith_vesicle
  status: passed
  required: true
  target_ids:
  - cellstructuremech:coccolith_vesicle
  command: just validate data/structures/membrane_organelle/coccolith_vesicle.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-19
  name: validate-strict cellstructuremech:coccolith_vesicle
  status: passed
  required: true
  target_ids:
  - cellstructuremech:coccolith_vesicle
  command: just validate-strict data/structures/membrane_organelle/coccolith_vesicle.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: supplemental-pmid
  name: Supplemental bounded PMID authority checks
  status: passed
  required: true
  target_ids:
  - GO:0033106
  - GO:0045334
  - GO:0106176
  - GO:0030669
  - GO:0030136
  - cellstructuremech:clathrin_coated_vesicle_lumen
  - GO:0030665
  - GO:0030135
  - GO:0030662
  - cellstructuremech:coccolith_vesicle
  command: .venv/bin/python /private/tmp/cellstructure-batches-2346-2397-20261103/check_pmid_chunks.py
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360
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
  - GO:0033106
  - GO:0045334
  - GO:0106176
  - GO:0030669
  - GO:0030136
  - cellstructuremech:clathrin_coated_vesicle_lumen
  - GO:0030665
  - GO:0030135
  - GO:0030662
  - cellstructuremech:coccolith_vesicle
  summary: 'Nine applicability defects are corrected: the omitted assessment for cis-Golgi
    network membrane and eight unsupported expression-only exclusions across clathrin-coated
    endocytic vesicle/lumen/membrane, generic clathrin-coated vesicle/lumen/membrane,
    coated vesicle and coated vesicle membrane. Both clathrin lumens have explicit
    molecular recruitment narratives. Coccolith vesicle remains a genuine exclusion
    because its supported claims are morphological and unresolved ATPase/transport
    identities are explicitly withheld. Actual complete catalogue coverage has no
    matched relevant yeast or coccolithophore dataset. No unrelated organism dataset
    or downstream module query substitutes for noncoverage. Resource noncoverage is
    not biological absence; retained historical runner failure is not a fresh invocation.'
  evidence_ids:
  - plaque-catalogue
  - plaque-historical-runner
  - micro-adapter-catalogue
  - septin-catalogue
- check_id: independent-scientific-review
  name: Independent claim-level source review
  status: passed
  required: true
  target_ids:
  - GO:0033106
  - GO:0045334
  - GO:0106176
  - GO:0030669
  - GO:0030136
  - cellstructuremech:clathrin_coated_vesicle_lumen
  - GO:0030665
  - GO:0030135
  - GO:0030662
  - cellstructuremech:coccolith_vesicle
  summary: Three read-only reviewers covered the complete ten-record cohort, including
    changed inputs, with explicit scientific findings and source-access limits. Final
    artifact/head acceptance occurs after saving.
  evidence_ids:
  - plaque-policy
  - plaque-rubric
  - plaque-graph-policy
  - plaque-schema-policy
  - plaque-clathrin-agent-go
  - plaque-root23-sources-coccolith-go
  - plaque-clathrin-agent-SL-0070
  - plaque-clathrin-agent-SL-0071
  - plaque-clathrin-agent-SL-0319
  - plaque-clathrin-agent-tax4932
  - plaque-root23-sources-NCBITaxon-127549
  - plaque-root23-sources-NCBITaxon-2903
  - plaque-clathrin-agent-doi-10.1016_j.devcel.2005.04.014
  - plaque-clathrin-agent-kaksonen2005-meta
  - plaque-root23-sources-doi-10.1021_jacs.6c02151
  - plaque-root23-sources-doi-10.1038_ncomms11228
  - plaque-clathrin-agent-newpher2005-duke
  - plaque-clathrin-agent-newpher2005-publisher
  - plaque-clathrin-agent-kaksonen2005-core
  - plaque-clathrin-agent-kaksonen2005-publisher
  - plaque-clathrin-agent-kaksonen2005-cellpdf
  - plaque-clathrin-agent-kaksonen2005-corealternate
  - plaque-clathrin-agent-kaksonen2005-api
  - plaque-root23-sources-jats-PMC13067266
  - plaque-root23-sources-coccolith2026-supplement
  - plaque-root23-sources-jats-PMC4834641
  - plaque-root23-sources-coccolith2026-s3xml
  - plaque-root23-sources-coccolith-fig2
  - plaque-catalogue
  - micro-review-policy
  - micro-review-config
  - micro-review-profile
  - micro-graph-contract
  - micro-native-schema
  - micro-review-schema
  - micro-cis-go
  - micro-cis-tax-4922
  - micro-cis-tax-460519
  - micro-cis-jats-PMC2148216
  - micro-cis-atcc-204163
  - micro-cis-ena-LC815816
  - micro-cis-cho2000-meta
  - micro-cis-go-parent
  - micro-coated-go
  - micro-coat-membrane-go
  - micro-NCBITaxon-4932
  - micro-NCBITaxon-559292
  - micro-PMID-8004676
  - micro-PMID-9568718
  - micro-PMID-10684247
  - micro-PMID-14562095
  - micro-doi-10.1016_j.devcel.2005.04.014
  - micro-doi-10.1016_j.cell.2012.01.015
  - micro-matsuoka1998-author
  - micro-newpher2005-duke
  - micro-yu2012-s3
  - micro-UniProtKB-P22137
  - micro-UniProtKB-P17891
  - micro-UniProtKB-Q04491
  - micro-UniProtKB-P38968
  - micro-UniProtKB-P41810
  - micro-UniProtKB-P53622
  - micro-UniProtKB-P22276
  - micro-ipr-P22137
  - micro-ipr-P17891
  - micro-ipr-Q04491
  - micro-ipr-P38968
  - micro-ipr-P41810
  - micro-ipr-P53622
  - septin-review-policy
  - septin-curation-policy
  - septin-graph-policy
  - septin-go
  - septin-ancestors-0045334
  - septin-ancestors-0106176
  - septin-ancestors-0030669
  - septin-go-edit
  - septin-SL-0319
  - septin-tax4932
  - septin-newpher-meta
  - septin-kaksonen-meta
  - septin-newpher-duke
- check_id: historical-adapter-runner
  name: Retained historical adapter runner availability
  status: unavailable
  required: false
  target_ids:
  - GO:0033106
  - GO:0045334
  - GO:0106176
  - GO:0030669
  - GO:0030136
  - cellstructuremech:clathrin_coated_vesicle_lumen
  - GO:0030665
  - GO:0030135
  - GO:0030662
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
- check_id: cis_golgi_network_membrane-uniprot-verify
  name: Native cis golgi network membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0033106
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cis_golgi_network_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-cis_golgi_network_membrane-verify
- check_id: cis_golgi_network_membrane-uniprot-causal
  name: Native cis golgi network membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0033106
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cis_golgi_network_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-cis_golgi_network_membrane-causal
- check_id: clathrin_coated_endocytic_vesicle-uniprot-verify
  name: Native clathrin coated endocytic vesicle UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0045334
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-clathrin_coated_endocytic_vesicle-verify
- check_id: clathrin_coated_endocytic_vesicle-uniprot-causal
  name: Native clathrin coated endocytic vesicle UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0045334
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-clathrin_coated_endocytic_vesicle-causal
- check_id: clathrin_coated_endocytic_vesicle_lumen-uniprot-verify
  name: Native clathrin coated endocytic vesicle lumen UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0106176
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_lumen.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-clathrin_coated_endocytic_vesicle_lumen-verify
- check_id: clathrin_coated_endocytic_vesicle_lumen-uniprot-causal
  name: Native clathrin coated endocytic vesicle lumen UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0106176
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_lumen.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-clathrin_coated_endocytic_vesicle_lumen-causal
- check_id: clathrin_coated_endocytic_vesicle_membrane-uniprot-verify
  name: Native clathrin coated endocytic vesicle membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0030669
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-clathrin_coated_endocytic_vesicle_membrane-verify
- check_id: clathrin_coated_endocytic_vesicle_membrane-uniprot-causal
  name: Native clathrin coated endocytic vesicle membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0030669
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-clathrin_coated_endocytic_vesicle_membrane-causal
- check_id: clathrin_coated_vesicle-uniprot-verify
  name: Native clathrin coated vesicle UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0030136
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/clathrin_coated_vesicle.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-clathrin_coated_vesicle-verify
- check_id: clathrin_coated_vesicle-uniprot-causal
  name: Native clathrin coated vesicle UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0030136
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/clathrin_coated_vesicle.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-clathrin_coated_vesicle-causal
- check_id: clathrin_coated_vesicle_lumen-uniprot-verify
  name: Native clathrin coated vesicle lumen UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:clathrin_coated_vesicle_lumen
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/clathrin_coated_vesicle_lumen.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-clathrin_coated_vesicle_lumen-verify
- check_id: clathrin_coated_vesicle_lumen-uniprot-causal
  name: Native clathrin coated vesicle lumen UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:clathrin_coated_vesicle_lumen
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/clathrin_coated_vesicle_lumen.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-clathrin_coated_vesicle_lumen-causal
- check_id: clathrin_coated_vesicle_membrane-uniprot-verify
  name: Native clathrin coated vesicle membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0030665
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/clathrin_coated_vesicle_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-clathrin_coated_vesicle_membrane-verify
- check_id: clathrin_coated_vesicle_membrane-uniprot-causal
  name: Native clathrin coated vesicle membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0030665
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/clathrin_coated_vesicle_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-clathrin_coated_vesicle_membrane-causal
- check_id: coated_vesicle-uniprot-verify
  name: Native coated vesicle UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0030135
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/coated_vesicle.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-coated_vesicle-verify
- check_id: coated_vesicle-uniprot-causal
  name: Native coated vesicle UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0030135
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/coated_vesicle.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-coated_vesicle-causal
- check_id: coated_vesicle_membrane-uniprot-verify
  name: Native coated vesicle membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0030662
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/coated_vesicle_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-coated_vesicle_membrane-verify
- check_id: coated_vesicle_membrane-uniprot-causal
  name: Native coated vesicle membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0030662
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/coated_vesicle_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-coated_vesicle_membrane-causal
- check_id: coccolith_vesicle-uniprot-verify
  name: Native coccolith vesicle UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:coccolith_vesicle
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/coccolith_vesicle.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-coccolith_vesicle-verify
- check_id: coccolith_vesicle-uniprot-causal
  name: Native coccolith vesicle UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:coccolith_vesicle
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/coccolith_vesicle.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-coccolith_vesicle-causal
evidence:
- evidence_id: current-record-0
  kind: record_content
  reference: data/structures/membrane_organelle/cis_golgi_network_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T10:56:12Z'
  support: context_only
  summary: Original frozen SHA256 c818f4de1c2fd8c36bc121d4389ce017c59526e083e6aefdf1b2a0041411da9c;
    current SHA256 c818f4de1c2fd8c36bc121d4389ce017c59526e083e6aefdf1b2a0041411da9c.
    Record bytes unchanged since the original review.
  snapshot_sha256: c818f4de1c2fd8c36bc121d4389ce017c59526e083e6aefdf1b2a0041411da9c
- evidence_id: original-review-0
  kind: prior_review
  reference: reviews/structured/20261021T111327Z-cis-golgi-network-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T10:56:12Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: c2cb05552b9ddc319f82c78f28c7e7b76b653cf0bfb30fac5fac3babdb7b8562
- evidence_id: current-record-1
  kind: record_content
  reference: data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T10:56:12Z'
  support: context_only
  summary: Original frozen SHA256 3193e3f6ea811d515c1545dc4e9179c8122e8718a328ed11261c7b648e94343d;
    current SHA256 3193e3f6ea811d515c1545dc4e9179c8122e8718a328ed11261c7b648e94343d.
    Record bytes unchanged since the original review.
  snapshot_sha256: 3193e3f6ea811d515c1545dc4e9179c8122e8718a328ed11261c7b648e94343d
- evidence_id: original-review-1
  kind: prior_review
  reference: reviews/structured/20261021T111328Z-clathrin-coated-endocytic-vesicle-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T10:56:12Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 6c8294738ce8825502a24e1ac67657062ce41feecca60a846364d259df1bb50e
- evidence_id: current-record-2
  kind: record_content
  reference: data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_lumen.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T10:56:12Z'
  support: context_only
  summary: Original frozen SHA256 d3a53daa5cc28635e48242bfa4d7dab04186a8c7f17b40a1491de51e94a33951;
    current SHA256 d3a53daa5cc28635e48242bfa4d7dab04186a8c7f17b40a1491de51e94a33951.
    Record bytes unchanged since the original review.
  snapshot_sha256: d3a53daa5cc28635e48242bfa4d7dab04186a8c7f17b40a1491de51e94a33951
- evidence_id: original-review-2
  kind: prior_review
  reference: reviews/structured/20261021T111329Z-clathrin-coated-endocytic-vesicle-lumen-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T10:56:12Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 04b141b90eac13e8f9763cb66ba3f35591dfdfca08cff3277995c6951bad78ee
- evidence_id: current-record-3
  kind: record_content
  reference: data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T10:56:12Z'
  support: context_only
  summary: Original frozen SHA256 70d8d315440e5cc7cc4c8f8c11a9103d74deffa773df25d9051113122d8a189a;
    current SHA256 70d8d315440e5cc7cc4c8f8c11a9103d74deffa773df25d9051113122d8a189a.
    Record bytes unchanged since the original review.
  snapshot_sha256: 70d8d315440e5cc7cc4c8f8c11a9103d74deffa773df25d9051113122d8a189a
- evidence_id: original-review-3
  kind: prior_review
  reference: reviews/structured/20261021T111329Z-clathrin-coated-endocytic-vesicle-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T10:56:12Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: ca324107ccb682459d538e6fdfebe6cba513319dcf615e44d2948637347327c4
- evidence_id: current-record-4
  kind: record_content
  reference: data/structures/membrane_organelle/clathrin_coated_vesicle.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T10:56:12Z'
  support: context_only
  summary: Original frozen SHA256 cee241afc73475bcdec9d8c3c4c57bdf9c4cb2f726e4a78615dfb393613be9ad;
    current SHA256 cee241afc73475bcdec9d8c3c4c57bdf9c4cb2f726e4a78615dfb393613be9ad.
    Record bytes unchanged since the original review.
  snapshot_sha256: cee241afc73475bcdec9d8c3c4c57bdf9c4cb2f726e4a78615dfb393613be9ad
- evidence_id: original-review-4
  kind: prior_review
  reference: reviews/structured/20261021T111330Z-clathrin-coated-vesicle-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T10:56:12Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: bd0476ce3500948f612015e0e396f0f40f58261544828f790f21a3fd850d6788
- evidence_id: current-record-5
  kind: record_content
  reference: data/structures/membrane_organelle/clathrin_coated_vesicle_lumen.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T10:56:12Z'
  support: context_only
  summary: Original frozen SHA256 2137a192f721232651c140497813cea3f15a73a67e910194d59fadc7837308f9;
    current SHA256 2137a192f721232651c140497813cea3f15a73a67e910194d59fadc7837308f9.
    Record bytes unchanged since the original review.
  snapshot_sha256: 2137a192f721232651c140497813cea3f15a73a67e910194d59fadc7837308f9
- evidence_id: original-review-5
  kind: prior_review
  reference: reviews/structured/20261021T111331Z-clathrin-coated-vesicle-lumen-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T10:56:12Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: e937f1b6d79a0d6605221930b32ba918b9a14d5d2717dc8069b172e5b0ac6424
- evidence_id: current-record-6
  kind: record_content
  reference: data/structures/membrane_organelle/clathrin_coated_vesicle_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T10:56:12Z'
  support: context_only
  summary: Original frozen SHA256 963e3cbe094c98b1279923d8f4ecc6a27343f82aa7240dece427fa09882c25f1;
    current SHA256 963e3cbe094c98b1279923d8f4ecc6a27343f82aa7240dece427fa09882c25f1.
    Record bytes unchanged since the original review.
  snapshot_sha256: 963e3cbe094c98b1279923d8f4ecc6a27343f82aa7240dece427fa09882c25f1
- evidence_id: original-review-6
  kind: prior_review
  reference: reviews/structured/20261021T111332Z-clathrin-coated-vesicle-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T10:56:12Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 2bdb53c90a03960d886fa43d2d61c2e3f84e702b07dc71427ea6147217fd16d8
- evidence_id: current-record-7
  kind: record_content
  reference: data/structures/membrane_organelle/coated_vesicle.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T10:56:12Z'
  support: context_only
  summary: Original frozen SHA256 baf2f374fd87cb07f0ae0a31c5962cfa34c345941f872a96759858c88c8218c1;
    current SHA256 baf2f374fd87cb07f0ae0a31c5962cfa34c345941f872a96759858c88c8218c1.
    Record bytes unchanged since the original review.
  snapshot_sha256: baf2f374fd87cb07f0ae0a31c5962cfa34c345941f872a96759858c88c8218c1
- evidence_id: original-review-7
  kind: prior_review
  reference: reviews/structured/20261021T111333Z-coated-vesicle-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T10:56:12Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 2d21b43cbb854d99973d35da5ee51136319c90bdc7fd1aa1f111f15441554b1c
- evidence_id: current-record-8
  kind: record_content
  reference: data/structures/membrane_organelle/coated_vesicle_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T10:56:12Z'
  support: context_only
  summary: Original frozen SHA256 b74f6c754d374d664267834c903c7bb2aed86f79145de8ce69f6ea9785bbebcc;
    current SHA256 b74f6c754d374d664267834c903c7bb2aed86f79145de8ce69f6ea9785bbebcc.
    Record bytes unchanged since the original review.
  snapshot_sha256: b74f6c754d374d664267834c903c7bb2aed86f79145de8ce69f6ea9785bbebcc
- evidence_id: original-review-8
  kind: prior_review
  reference: reviews/structured/20261021T111334Z-coated-vesicle-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T10:56:12Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 2232e0751eacf3e99b4e0f79257808634c6c51fe1e973c6947f80f5da7a5376a
- evidence_id: current-record-9
  kind: record_content
  reference: data/structures/membrane_organelle/coccolith_vesicle.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T10:56:12Z'
  support: context_only
  summary: Original frozen SHA256 89b7e793211332507189d1ba872fc1eb901cf8703323853cd10d65b45e971655;
    current SHA256 89b7e793211332507189d1ba872fc1eb901cf8703323853cd10d65b45e971655.
    Record bytes unchanged since the original review.
  snapshot_sha256: 89b7e793211332507189d1ba872fc1eb901cf8703323853cd10d65b45e971655
- evidence_id: original-review-9
  kind: prior_review
  reference: reviews/structured/20261021T111335Z-coccolith-vesicle-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T10:56:12Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: f23c52bba81f53d4af37baa17a353ef3c9aafb453a6ff1d857c1ee1622c8f1ff
- evidence_id: plaque-current-4
  kind: record_content
  reference: data/structures/membrane_organelle/clathrin_coated_vesicle.yaml
  locator: Entire maintained record at source cee44c9b340b36e4e103ebd16c4bfcf6745bd41f;
    all fields, histories, discussions and graphs
  summary: Complete current target read. Hash is unchanged from the original frozen
    target; PROPOSED status remains unchanged and no record curation is performed.
  accessed_at: '2026-11-03T10:54:43.189907Z'
  support: supports
  snapshot_sha256: cee241afc73475bcdec9d8c3c4c57bdf9c4cb2f726e4a78615dfb393613be9ad
- evidence_id: plaque-original-4
  kind: prior_review
  reference: reviews/structured/20261021T111330Z-clathrin-coated-vesicle-audit/review.yaml
  locator: Original authoritative YAML, rendered Markdown, all source inputs, assessments,
    checks, findings/actions and limitations
  summary: Original review validates and renders byte-identically. Every historical
    frozen input resolves and matches its hash at the original source commit; current
    target hash also matches. Original verdict is pass_with_limitations, with no scientific
    findings or curation actions.
  accessed_at: '2026-11-03T10:54:43.189907Z'
  support: supports
  snapshot_sha256: bd0476ce3500948f612015e0e396f0f40f58261544828f790f21a3fd850d6788
- evidence_id: plaque-current-5
  kind: record_content
  reference: data/structures/membrane_organelle/clathrin_coated_vesicle_lumen.yaml
  locator: Entire maintained record at source cee44c9b340b36e4e103ebd16c4bfcf6745bd41f;
    all fields, histories, discussions and graphs
  summary: Complete current target read. Hash is unchanged from the original frozen
    target; PROPOSED status remains unchanged and no record curation is performed.
  accessed_at: '2026-11-03T10:54:43.189907Z'
  support: supports
  snapshot_sha256: 2137a192f721232651c140497813cea3f15a73a67e910194d59fadc7837308f9
- evidence_id: plaque-original-5
  kind: prior_review
  reference: reviews/structured/20261021T111331Z-clathrin-coated-vesicle-lumen-audit/review.yaml
  locator: Original authoritative YAML, rendered Markdown, all source inputs, assessments,
    checks, findings/actions and limitations
  summary: Original review validates and renders byte-identically. Every historical
    frozen input resolves and matches its hash at the original source commit; current
    target hash also matches. Original verdict is pass_with_limitations, with no scientific
    findings or curation actions.
  accessed_at: '2026-11-03T10:54:43.189907Z'
  support: supports
  snapshot_sha256: e937f1b6d79a0d6605221930b32ba918b9a14d5d2717dc8069b172e5b0ac6424
- evidence_id: plaque-current-6
  kind: record_content
  reference: data/structures/membrane_organelle/clathrin_coated_vesicle_membrane.yaml
  locator: Entire maintained record at source cee44c9b340b36e4e103ebd16c4bfcf6745bd41f;
    all fields, histories, discussions and graphs
  summary: Complete current target read. Hash is unchanged from the original frozen
    target; PROPOSED status remains unchanged and no record curation is performed.
  accessed_at: '2026-11-03T10:54:43.189907Z'
  support: supports
  snapshot_sha256: 963e3cbe094c98b1279923d8f4ecc6a27343f82aa7240dece427fa09882c25f1
- evidence_id: plaque-original-6
  kind: prior_review
  reference: reviews/structured/20261021T111332Z-clathrin-coated-vesicle-membrane-audit/review.yaml
  locator: Original authoritative YAML, rendered Markdown, all source inputs, assessments,
    checks, findings/actions and limitations
  summary: Original review validates and renders byte-identically. Every historical
    frozen input resolves and matches its hash at the original source commit; current
    target hash also matches. Original verdict is pass_with_limitations, with no scientific
    findings or curation actions.
  accessed_at: '2026-11-03T10:54:43.189907Z'
  support: supports
  snapshot_sha256: 2bdb53c90a03960d886fa43d2d61c2e3f84e702b07dc71427ea6147217fd16d8
- evidence_id: plaque-current-9
  kind: record_content
  reference: data/structures/membrane_organelle/coccolith_vesicle.yaml
  locator: Entire maintained record at source cee44c9b340b36e4e103ebd16c4bfcf6745bd41f;
    all fields, histories, discussions and graphs
  summary: Complete current target read. Hash is unchanged from the original frozen
    target; PROPOSED status remains unchanged and no record curation is performed.
  accessed_at: '2026-11-03T10:54:43.189907Z'
  support: supports
  snapshot_sha256: 89b7e793211332507189d1ba872fc1eb901cf8703323853cd10d65b45e971655
- evidence_id: plaque-original-9
  kind: prior_review
  reference: reviews/structured/20261021T111335Z-coccolith-vesicle-audit/review.yaml
  locator: Original authoritative YAML, rendered Markdown, all source inputs, assessments,
    checks, findings/actions and limitations
  summary: Original review validates and renders byte-identically. Every historical
    frozen input resolves and matches its hash at the original source commit; current
    target hash also matches. Original verdict is pass_with_limitations, with no scientific
    findings or curation actions.
  accessed_at: '2026-11-03T10:54:43.189907Z'
  support: supports
  snapshot_sha256: f23c52bba81f53d4af37baa17a353ef3c9aafb453a6ff1d857c1ee1622c8f1ff
- evidence_id: plaque-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Frozen native evidence, structure identity, components, graph-scope and
    applicability contract
  summary: Named molecular narratives trigger actual structured-source applicability;
    absent expression claims alone do not justify exemption. Localization, molecular
    function, material constitution and formation necessity are distinct.
  accessed_at: '2026-11-03T10:54:43.189907Z'
  support: context_only
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: plaque-rubric
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Frozen native evidence, structure identity, components, graph-scope and
    applicability contract
  summary: Named molecular narratives trigger actual structured-source applicability;
    absent expression claims alone do not justify exemption. Localization, molecular
    function, material constitution and formation necessity are distinct.
  accessed_at: '2026-11-03T10:54:43.189907Z'
  support: context_only
  snapshot_sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
- evidence_id: plaque-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Frozen native evidence, structure identity, components, graph-scope and
    applicability contract
  summary: Named molecular narratives trigger actual structured-source applicability;
    absent expression claims alone do not justify exemption. Localization, molecular
    function, material constitution and formation necessity are distinct.
  accessed_at: '2026-11-03T10:54:43.189907Z'
  support: context_only
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: plaque-schema-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Frozen native evidence, structure identity, components, graph-scope and
    applicability contract
  summary: Named molecular narratives trigger actual structured-source applicability;
    absent expression claims alone do not justify exemption. Localization, molecular
    function, material constitution and formation necessity are distinct.
  accessed_at: '2026-11-03T10:54:43.189907Z'
  support: context_only
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: plaque-neighbor-coat
  kind: record_content
  reference: data/structures/other/clathrin_vesicle_coat.yaml
  locator: Identifier, label, definition, hierarchy/parthood only; coat additionally
    component IDs/labels/types for heavy and light chain
  summary: Frozen before inspection. Used only to distinguish whole vesicle, coat,
    mineral product and external covering. Coat contains separate heavy/light-chain
    components, as the target discussion states. No independent validation of neighbor
    accession mappings, full neighbor science or historical dispositions is claimed.
  accessed_at: '2026-11-03T10:54:43.189907Z'
  support: context_only
  snapshot_sha256: cef674eb9fc2b08323c1780daa340012db00fd43e3f89c7de880ac972594e17d
- evidence_id: plaque-neighbor-coccolith
  kind: record_content
  reference: data/structures/envelope/coccolith.yaml
  locator: Identifier, label, definition, hierarchy/parthood only; coat additionally
    component IDs/labels/types for heavy and light chain
  summary: Frozen before inspection. Used only to distinguish whole vesicle, coat,
    mineral product and external covering. Coat contains separate heavy/light-chain
    components, as the target discussion states. No independent validation of neighbor
    accession mappings, full neighbor science or historical dispositions is claimed.
  accessed_at: '2026-11-03T10:54:43.189907Z'
  support: context_only
  snapshot_sha256: 8932b1ad635cf2e272c74fb8d4f00e6036b851ec2baa3daa3b5c3b52cc6979fa
- evidence_id: plaque-neighbor-coccosphere
  kind: record_content
  reference: data/structures/envelope/coccosphere.yaml
  locator: Identifier, label, definition, hierarchy/parthood only; coat additionally
    component IDs/labels/types for heavy and light chain
  summary: Frozen before inspection. Used only to distinguish whole vesicle, coat,
    mineral product and external covering. Coat contains separate heavy/light-chain
    components, as the target discussion states. No independent validation of neighbor
    accession mappings, full neighbor science or historical dispositions is claimed.
  accessed_at: '2026-11-03T10:54:43.189907Z'
  support: context_only
  snapshot_sha256: b72167a6093a734226fc2c9458c475f7a05120e8d2077d5f7b7007ee0a5cd299
- evidence_id: plaque-clathrin-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030136,GO:0030135,GO:0030125,GO:0030665,GO:0072583,GO:0060205,GO:0030659,GO:0030662
  locator: All eight requested active GO terms, names, definitions, aspects and typed
    child relations
  summary: Exact whole vesicle0030136, coat0030125 and membrane0030665 are distinct.
    Membrane is a direct part_of child of whole vesicle, coated vesicle0030135 is
    its is_a parent, and membrane parents0030662/0030659 are connected by is_a. The
    ontology also represents coat part_of the membrane location; this does not make
    coat proteins constituents of the separately modeled lipid-bilayer material. GO0072583
    supports endocytosis through coated pits/vesicles.
  accessed_at: '2026-11-03T10:50:36.954922Z'
  support: supports
  snapshot_sha256: 99bb7c9eae759e77dbeb8efc316337e5593f176de6a769197070419135166ed5
- evidence_id: plaque-root23-sources-coccolith-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0016020,GO:0043231
  locator: Exact GO0016020 and0043231 identities, active status and definitions
  summary: GO0016020 denotes the structural membrane; GO0043231 is a broad intracellular
    membrane-bounded organelle parent, not an exact coccolith-vesicle identity.
  accessed_at: '2026-11-03T10:50:37.899926Z'
  support: supports
  snapshot_sha256: 62ae267eca80e0297bca56833f905cbd02db3e689d5d24ba8e16e10b1c451dc5
- evidence_id: plaque-clathrin-agent-SL-0070
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0070.json
  locator: Native definition, synonyms, direct GO correspondences and immediate isA/partOf
    objects distinguished from nested ancestors
  summary: SL0070 identifies the whole clathrin-coated vesicle and CCV synonym. SL0071
    is its membrane and directly partOf SL0070. SL0319 defines the bounded lumen,
    directly partOf SL0070, with cytoplasmic-vesicle-lumen parent; it does not have
    an exact direct GO correspondence.
  accessed_at: '2026-11-03T10:50:36.955211Z'
  support: supports
  snapshot_sha256: f43fcdaa17e965bb510e8bfbfc25cac322e28c331a29ea44ff71953a61d7840c
- evidence_id: plaque-clathrin-agent-SL-0071
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0071.json
  locator: Native definition, synonyms, direct GO correspondences and immediate isA/partOf
    objects distinguished from nested ancestors
  summary: SL0070 identifies the whole clathrin-coated vesicle and CCV synonym. SL0071
    is its membrane and directly partOf SL0070. SL0319 defines the bounded lumen,
    directly partOf SL0070, with cytoplasmic-vesicle-lumen parent; it does not have
    an exact direct GO correspondence.
  accessed_at: '2026-11-03T10:50:37.559365Z'
  support: supports
  snapshot_sha256: 53b10efd70ad2b9a0be036761855e978313a01dbc7a3eb8985e72cf74142eac0
- evidence_id: plaque-clathrin-agent-SL-0319
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0319.json
  locator: Native definition, synonyms, direct GO correspondences and immediate isA/partOf
    objects distinguished from nested ancestors
  summary: SL0070 identifies the whole clathrin-coated vesicle and CCV synonym. SL0071
    is its membrane and directly partOf SL0070. SL0319 defines the bounded lumen,
    directly partOf SL0070, with cytoplasmic-vesicle-lumen parent; it does not have
    an exact direct GO correspondence.
  accessed_at: '2026-11-03T10:50:37.554329Z'
  support: supports
  snapshot_sha256: 60adcc470cf8170aeb6ca0842437084ca80cb1a3e5fbd7c87e7a4b3a735d0e4e
- evidence_id: plaque-clathrin-agent-tax4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Exact taxId, scientificName, rank, lineage and alternative-name list
  summary: Current ENA verifies Saccharomyces cerevisiae 4932.  Taxonomy alone does
    not establish occurrence, strain identity or prevalence.
  accessed_at: '2026-11-03T10:50:36.955160Z'
  support: supports
  snapshot_sha256: d930c884e1154be4c050977652c0d6baf3666d183a90fa17ead8d01cce2c770f
- evidence_id: plaque-root23-sources-NCBITaxon-127549
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/127549
  locator: Exact taxId, scientificName, rank, lineage and alternative-name list
  summary: Current ENA verifies Calcidiscus leptoporus 127549.  Taxonomy alone does
    not establish occurrence, strain identity or prevalence.
  accessed_at: '2026-11-03T10:50:37.583481Z'
  support: supports
  snapshot_sha256: b40f70d18d46271a012610371904101819726ec1f4fc1054ca41a87a2b88e8c2
- evidence_id: plaque-root23-sources-NCBITaxon-2903
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2903
  locator: Exact taxId, scientificName, rank, lineage and alternative-name list
  summary: Current ENA verifies Emiliania huxleyi 2903. Gephyrocapsa huxleyi is explicitly
    a synonym of Emiliania huxleyi. Taxonomy alone does not establish occurrence,
    strain identity or prevalence.
  accessed_at: '2026-11-03T10:50:37.602680Z'
  support: supports
  snapshot_sha256: dd94de64d5f0b4a22db3c88631c1c29f985b2856636530d16b404e913762054f
- evidence_id: plaque-clathrin-agent-doi-10.1016_j.devcel.2005.04.014
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.devcel.2005.04.014
  locator: 'Exact DOI query result: title, authors, publication year, DOI/PMID and
    complete abstract'
  summary: 'Verified bibliography: In vivo dynamics of clathrin and its adaptor-dependent
    recruitment to the actin-based endocytic machinery in yeast.; Newpher TM, Smith
    RP, Lemmon V, Lemmon SK.; 2005. Complete abstract inspected; body access is separately
    declared.'
  accessed_at: '2026-11-03T10:50:36.955263Z'
  support: supports
  snapshot_sha256: c99ec084fa3f65e3b5107699c30f42b09489dbc49d6be518d71ff9352d5a199c
- evidence_id: plaque-clathrin-agent-kaksonen2005-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.cell.2005.09.024
  locator: 'Exact DOI query result: title, authors, publication year, DOI/PMID and
    complete abstract'
  summary: 'Verified bibliography: A modular design for the clathrin- and actin-mediated
    endocytosis machinery.; Kaksonen M, Toret CP, Drubin DG.; 2005. Complete abstract
    inspected; body access is separately declared.'
  accessed_at: '2026-11-03T10:50:36.955409Z'
  support: supports
  snapshot_sha256: b21f04a2ca620468ebafa02936207fe7e04553d44f862f3f18d72a85b6c4aba2
- evidence_id: plaque-root23-sources-doi-10.1021_jacs.6c02151
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1021/jacs.6c02151
  locator: 'Exact DOI query result: title, authors, publication year, DOI/PMID and
    complete abstract'
  summary: 'Verified bibliography: Spatial Relations between Coccoliths and Their
    Confining Membrane During Crystal Morphogenesis.; Avrahami EM, Karpov D, Aram
    L, Elad N, Safadi R, Rosenhek-Goldian I, Sui XM, de Haan D, Varsano N, Cohen SR,
    Zlotnikov I, Gal A.; 2026. Complete abstract inspected; body access is separately
    declared.'
  accessed_at: '2026-11-03T10:50:37.642797Z'
  support: supports
  snapshot_sha256: ac00ca5a592b21ef9dee0d22139285198b21a3c8f4383a36d7e74574efc90895
- evidence_id: plaque-root23-sources-doi-10.1038_ncomms11228
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/ncomms11228
  locator: 'Exact DOI query result: title, authors, publication year, DOI/PMID and
    complete abstract'
  summary: 'Verified bibliography: A vacuole-like compartment concentrates a disordered
    calcium phase in a key coccolithophorid alga.; Sviben S, Gal A, Hood MA, Bertinetti
    L, Politi Y, Bennet M, Krishnamoorthy P, Schertel A, Wirth R, Sorrentino A, Pereiro
    E, Faivre D, Scheffel A.; 2016. Complete abstract inspected; body access is separately
    declared.'
  accessed_at: '2026-11-03T10:50:37.703103Z'
  support: supports
  snapshot_sha256: 33692828d7c67bfaaf1f13d373edf993110a19ad9b13c868ef39a1b4cfe80eb9
- evidence_id: plaque-clathrin-agent-newpher2005-duke
  kind: primary_source
  reference: https://dukespace.lib.duke.edu/server/api/core/bitstreams/e3c70c30-e4a1-4ba0-8ea6-c50af4ba491e/content
  locator: 'Genuine published PDF pp87–96: Summary, Introduction, Results, Discussion
    and Experimental Procedures including Table1 and Fig1–6 captions; text only'
  summary: Fresh primary body supports heavy/light-chain localization at cortical
    yeast sites, adaptor-dependent recruitment and their timing relative to actin.
    Experiments include live fluorescent reporters, mutants and LAT-A, usually30C,
    in the named Table1 strains. The paper explicitly cannot distinguish clathrin
    disassembly before budding from departure of coated vesicles from the evanescent
    field. Its reporter dynamics are not direct sealed-lumen imaging, universal formation
    necessity or a population prevalence census.
  accessed_at: '2026-11-03T10:50:36.955318Z'
  support: supports
  snapshot_sha256: c848e911372b9afb9902e4a74e3cb3dd66ef90eb5e102024cc95fff648bb6c21
- evidence_id: plaque-clathrin-agent-newpher2005-publisher
  kind: authority
  reference: https://doi.org/10.1016/j.devcel.2005.04.014
  locator: Actual native HTTP response; body format/content inspected to establish
    access tier only
  summary: HTTP200. Redirect/challenge/access response does not supply an inspected
    complete article body. Kaksonen support remains the exact complete primary abstract;
    no successful full-body retrieval is claimed here.
  accessed_at: '2026-11-03T10:50:36.955362Z'
  support: context_only
  snapshot_sha256: 5df941bcc76d6caccdb7f7d86b8fd5365874521f4d3dc8eafc0e5e62b77b6f04
- evidence_id: plaque-clathrin-agent-kaksonen2005-core
  kind: authority
  reference: https://core.ac.uk/download/pdf/82329151.pdf
  locator: Actual native HTTP response; body format/content inspected to establish
    access tier only
  summary: HTTP403. Redirect/challenge/access response does not supply an inspected
    complete article body. Kaksonen support remains the exact complete primary abstract;
    no successful full-body retrieval is claimed here.
  accessed_at: '2026-11-03T10:50:36.955730Z'
  support: context_only
  snapshot_sha256: 555aca8e44621c6427c77775aae75f55a1da52c54af4c342e9a8661f39ddb766
- evidence_id: plaque-clathrin-agent-kaksonen2005-publisher
  kind: authority
  reference: https://www.sciencedirect.com/science/article/pii/S0092867405009785
  locator: Actual native HTTP response; body format/content inspected to establish
    access tier only
  summary: HTTP403. Redirect/challenge/access response does not supply an inspected
    complete article body. Kaksonen support remains the exact complete primary abstract;
    no successful full-body retrieval is claimed here.
  accessed_at: '2026-11-03T10:50:37.010228Z'
  support: context_only
  snapshot_sha256: dae3a27adf4eeb97c13dfe3bff490d7c0a5f65a25e65a6cdc53cb03beeb633e8
- evidence_id: plaque-clathrin-agent-kaksonen2005-cellpdf
  kind: authority
  reference: https://www.cell.com/article/S0092867405009785/pdf
  locator: Actual native HTTP response; body format/content inspected to establish
    access tier only
  summary: HTTP403. Redirect/challenge/access response does not supply an inspected
    complete article body. Kaksonen support remains the exact complete primary abstract;
    no successful full-body retrieval is claimed here.
  accessed_at: '2026-11-03T10:50:37.096854Z'
  support: context_only
  snapshot_sha256: f23ed5e951b10ea3878d222f473b1bf1ae3b49c732ffcc64c43ab5a081ee7232
- evidence_id: plaque-clathrin-agent-kaksonen2005-corealternate
  kind: authority
  reference: https://core.ac.uk/reader/82329151
  locator: Actual native HTTP response; body format/content inspected to establish
    access tier only
  summary: HTTP403. Redirect/challenge/access response does not supply an inspected
    complete article body. Kaksonen support remains the exact complete primary abstract;
    no successful full-body retrieval is claimed here.
  accessed_at: '2026-11-03T10:50:37.137740Z'
  support: context_only
  snapshot_sha256: d695425adbd482da71846e36e2a854c846f99190eb0187e2bc4ce8f9b776a0c4
- evidence_id: plaque-clathrin-agent-kaksonen2005-api
  kind: authority
  reference: https://api.elsevier.com/content/article/PII:S0092867405009785?httpAccept=text/xml
  locator: Actual native HTTP response; body format/content inspected to establish
    access tier only
  summary: HTTP200. Elsevier API returns bibliographic metadata, not scientific article
    body. Kaksonen support remains the exact complete primary abstract; no successful
    full-body retrieval is claimed here.
  accessed_at: '2026-11-03T10:50:37.184883Z'
  support: context_only
  snapshot_sha256: 53993cd92f3bb1d1dcd4f4f4887c8a8acd6f0e64d35250a3fd23d05fc0dd0f51
- evidence_id: plaque-root23-sources-jats-PMC13067266
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13067266/fullTextXML
  locator: Complete scientific Introduction, Results, Discussion and Conclusions (sec1–4);
    complete Figure2–6 captions as text. Figure2 pixels inspected separately.
  summary: Avrahami2026 directly images intracellular mineral-containing vesicles
    in C.leptoporus. Membrane–crystal spacing varies by region/stage.716 averaged
    particles are about half a full ATPase height; identity/function remain unresolved.
    Luminal calcium is observed; proposed chemical subregions and local growth inhibition
    are interpretations, not sealed suborganelles or a proven universal molding mechanism.
    Figures3/4 are cryo-ET; Figure2 is schematic/cryo-SEM/FIB-SEM.
  accessed_at: '2026-11-03T10:50:38.205687Z'
  support: supports
  snapshot_sha256: 394a5731e2fdd83227a7bf515488f6add3b971c53697b6297c1e581f7c6baec9
- evidence_id: plaque-root23-sources-coccolith2026-supplement
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC13067266.1/ja6c02151_si_001.pdf
  locator: Actual PDF, Materials and Methods from Cell cultures through complete FIB-SEM
    data processing; partial subsequent lamellae section read but not used for stronger
    claims
  summary: RCC1130 is explicitly identified, with18C and16h light/8h dark culture
    conditions. Figure2B preparation is high-pressure freezing/freeze fracture. External
    coccolith EDTA removal precedes plunge freezing/FIB slice-and-view, followed by
    alignment and manual membrane segmentation. No entire-supplement, raw reconstruction
    or cryo-ET processing audit is claimed.
  accessed_at: '2026-11-03T10:50:38.341626Z'
  support: supports
  snapshot_sha256: b919d05e8a48887245d56be37a7aa917366f68cdf058e6b742bae29d385a3248
- evidence_id: plaque-root23-sources-jats-PMC4834641
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4834641/fullTextXML
  locator: Complete Results sec4–6, Discussion sec7 and culture Methods sec9; included
    Figure3–7 captions as text, not pixel inspection
  summary: Sviben2016 distinguishes E.huxleyi AWI1516 coccolith-vesicle/reticular-body
    system from a separate membrane-bound Ca/P-rich store. Apposition does not prove
    membrane continuity or a named transporter. Earlier luminal nondetection is not
    generalized across species or to the later C.leptoporus observation. Methods support
    AWI1516 and18C culture/induction conditions.
  accessed_at: '2026-11-03T10:50:38.344858Z'
  support: supports
  snapshot_sha256: cb92f360326ea29a36cd37f6bf417250926d35f9dd2327659475a6bcb26633ab
- evidence_id: plaque-root23-sources-coccolith2026-s3xml
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC13067266.1/PMC13067266.1.xml
  locator: Native archived article title, complete author names, permissions and ALI
    license_ref
  summary: Exact attribution agrees with the maintained figure. ALI supplies https://creativecommons.org/licenses/by/4.0/
    and human-readable permission identifies CC-BY4.0.
  accessed_at: '2026-11-03T10:50:38.348957Z'
  support: supports
  snapshot_sha256: c65411d5c5adb24f2e42120962c24d0fd3ecaffda72f9f485a728a313f2acdef
- evidence_id: plaque-root23-sources-coccolith-fig2
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC13067266.1/ja6c02151_0002.jpg
  locator: Fresh native Figure2 file bytes; exact SHA256 compared to frozen image,
    with complete source Figure2 caption independently read
  summary: Native figure bytes exactly match the maintained image. The viewed panels
    show a schematic; cryo-SEM and cryo-FIB-SEM sections; and five reconstructed stages.
    Membrane/crystal relationships and scale bars match the caption; stages are different
    observed coccoliths, not a time-lapse of one cell.
  accessed_at: '2026-11-03T10:50:38.525347Z'
  support: supports
  snapshot_sha256: f41e31add721c5f01869b2ce9ebe38b8aa7add53acb9a6445f6d2335858d2020
- evidence_id: plaque-image
  kind: record_content
  reference: data/images/membrane_organelle/coccolith_vesicle/pmc13067266_fig2.jpg
  locator: Entire700x418-pixel frozen image displayed with view_image and visually
    inspected
  summary: PanelA schematic is not to scale; panelB cryogenic SEM shows a cut cell;
    C/D have sections and backscatter insets; E has five left-to-right/top-to-bottom
    reconstructed stages with membrane on right halves. Pixel inspection and source
    caption support SEM modality with reconstructed-volume panels, not cryo-ET attribution
    for this figure.
  accessed_at: '2026-11-03T10:54:43.189907Z'
  support: supports
  snapshot_sha256: f41e31add721c5f01869b2ce9ebe38b8aa7add53acb9a6445f6d2335858d2020
- evidence_id: plaque-root23-sources-coccolith-go-search
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=coccolith&limit=100&page=1
  locator: Complete returned first page and exact query URL; result identities inspected
  summary: No returned hits for this exact bounded query.
  accessed_at: '2026-11-03T10:50:38.147627Z'
  support: context_only
  search_scope: QuickGO ontology search; query=coccolith; accessed 2026-11-03T10:50:38.147627Z;
    page1,limit100; total hits=0; no later pages searched.
  snapshot_sha256: f3a7dae9b1e9335291e3940cdf0e5f8dadf9335da7b9547710606b5106c63f86
- evidence_id: plaque-root23-sources-coccolithogenesis-go-search
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=coccolithogenesis&limit=100&page=1
  locator: Complete returned first page and exact query URL; result identities inspected
  summary: No returned hits for this exact bounded query.
  accessed_at: '2026-11-03T10:50:38.161738Z'
  support: context_only
  search_scope: QuickGO ontology search; query=coccolithogenesis; accessed 2026-11-03T10:50:38.161738Z;
    page1,limit100; total hits=0; no later pages searched.
  snapshot_sha256: f3a7dae9b1e9335291e3940cdf0e5f8dadf9335da7b9547710606b5106c63f86
- evidence_id: plaque-clathrin-lumen-go-search
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=clathrin%20coated%20vesicle%20lumen&limit=100&page=1
  locator: Complete returned first page and exact query URL; result identities inspected
  summary: First100 of651 hits include a narrower clathrin-coated ENDOCYTIC vesicle
    lumen, not an exact replacement for the broader SL0319 scope. This is not an exhaustive
    ontology absence claim.
  accessed_at: '2026-11-03T10:52:23.937293Z'
  support: context_only
  search_scope: QuickGO ontology search; query=clathrin coated vesicle lumen; accessed
    2026-11-03T10:52:23.937293Z; page1,limit100; total hits=651; no later pages searched.
  snapshot_sha256: ef2ec127a05d8b98a1b23c6df1b8484214837f5be264640758dda52b22d34798
- evidence_id: plaque-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete current /api/datasets response, every organism and dataset row;
    no pagination
  summary: No catalogue row matches S.cerevisiae, C.leptoporus or E.huxleyi/Gephyrocapsa.
    Downstream matched-organism gene/module queries therefore do not apply. Neither
    unrelated taxa nor catalogue absence establish biological absence.
  accessed_at: '2026-11-03T10:50:38.743723Z'
  support: supports
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: plaque-historical-runner
  kind: validation
  reference: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  locator: Historical00:49Z receipt and stdout/stderr independently reread and hash-verified
  summary: Historical runner exited1 before datasets due OS PermissionError reading
    pyvenv.cfg. This is not a fresh invocation; current official catalogue is the
    permitted source fallback.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: plaque-original-checks
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/adversary-plaque/original-checks.json
  locator: Four read-only native validate/render executions and every original frozen-source
    input hash
  summary: All four validate; Markdown is exact;15/15/15/17 historical inputs match
    original source commits; all four target hashes remain current. Original findings/actions
    are empty.
  accessed_at: '2026-11-03T10:51:57.003427Z'
  support: supports
  snapshot_sha256: 09624c583a03fff7b9c580144e9d55b78c35a2ff3cad8f12b4f5e8ac7d01b5fc
- evidence_id: plaque-native-clathrin_coated_vesicle-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/clathrin_coated_vesicle.yaml
    --verify
  locator: Actual root-owned focused command receipt and exact stdout independently
    read/hash-verified
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  accessed_at: '2026-11-03T10:50:12.864040Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-clathrin_coated_vesicle-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/clathrin_coated_vesicle.yaml
    --causal-graphs
  locator: Actual root-owned focused command receipt and exact stdout independently
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
  accessed_at: '2026-11-03T10:50:13.328357Z'
  support: supports
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: plaque-native-clathrin_coated_vesicle_lumen-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/clathrin_coated_vesicle_lumen.yaml
    --verify
  locator: Actual root-owned focused command receipt and exact stdout independently
    read/hash-verified
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  accessed_at: '2026-11-03T10:50:13.810601Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-clathrin_coated_vesicle_lumen-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/clathrin_coated_vesicle_lumen.yaml
    --causal-graphs
  locator: Actual root-owned focused command receipt and exact stdout independently
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
  accessed_at: '2026-11-03T10:50:14.281135Z'
  support: supports
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: plaque-native-clathrin_coated_vesicle_membrane-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/clathrin_coated_vesicle_membrane.yaml
    --verify
  locator: Actual root-owned focused command receipt and exact stdout independently
    read/hash-verified
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  accessed_at: '2026-11-03T10:50:14.744082Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-clathrin_coated_vesicle_membrane-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/clathrin_coated_vesicle_membrane.yaml
    --causal-graphs
  locator: Actual root-owned focused command receipt and exact stdout independently
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
  accessed_at: '2026-11-03T10:50:15.205820Z'
  support: supports
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: plaque-native-coccolith_vesicle-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/coccolith_vesicle.yaml
    --verify
  locator: Actual root-owned focused command receipt and exact stdout independently
    read/hash-verified
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  accessed_at: '2026-11-03T10:50:18.593866Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-coccolith_vesicle-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/coccolith_vesicle.yaml
    --causal-graphs
  locator: Actual root-owned focused command receipt and exact stdout independently
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
  accessed_at: '2026-11-03T10:50:19.035808Z'
  support: supports
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: micro-review-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Evidence Rules; Structured Source Cross-Checks; Workflow
  accessed_at: '2026-11-03T10:54:57.309459Z'
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
  summary: Named molecular claims trigger structured-source applicability whether
    or not expression inference is made. Scope of protein identity, membership and
    formation necessity must be kept separate. Read-only source review does not authorize
    record edits.
  support: supports
- evidence_id: micro-review-config
  kind: authority
  reference: conf/record_review.yaml
  locator: Active routes and rubrics
  accessed_at: '2026-11-03T10:54:57.309459Z'
  snapshot_sha256: d3334a12b8a616a7638f1195748085d2b543fba7df67ad4ff8fcc0ac18f2d3ee
  summary: Current frozen configuration reread; seventeen common policy/schema/verifier
    inputs are byte-identical to the preceding independently reviewed cohort. Previously
    inspected contract rules remain applicable; current source and target bytes are
    independently verified.
  support: supports
- evidence_id: micro-review-profile
  kind: authority
  reference: docs/record-review-profile.md
  locator: Issue-only persistence and native checks
  accessed_at: '2026-11-03T10:54:57.309459Z'
  snapshot_sha256: 6a49c8d35f0a94082a9ad0b8bd8c6a929d85de8339141955f3779bd7ab0eb7e4
  summary: Issue-bearing successor can include positive assessments alongside preserved
    unresolved findings. Original observations remain immutable. Root owns global
    gates and final review publication.
  support: supports
- evidence_id: micro-graph-contract
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Graph scope, node identity and constituent/necessity separation
  accessed_at: '2026-11-03T10:54:57.309459Z'
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
  summary: NONMECHANISTIC boundary/transport graphs are not complete molecular mechanisms.
    Membrane material, whole network, coat and whole vesicle identities must remain
    distinct.
  support: supports
- evidence_id: micro-native-schema
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: EssentialityEnum and CausalNode.component_ref
  accessed_at: '2026-11-03T10:54:57.309459Z'
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
  summary: Collective bilayer constitution is distinct from experimental necessity
    of individual lipids/proteins. component_ref must match the own component denoted;
    a membrane defined as the bilayer differs from the entire membrane-bounded compartment.
  support: supports
- evidence_id: micro-review-schema
  kind: authority
  reference: schema/record_review.yaml
  locator: EvidenceKind, Area, FindingReference and proposed action fields
  accessed_at: '2026-11-03T10:54:57.309459Z'
  snapshot_sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
  summary: Source scopes and real dates are retained; native assessment area schema
    and complete predecessor repository/review/finding identity are used.
  support: supports
- evidence_id: micro-original-validation-inputs
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/adversary-microtubule/original-validation-inputs.json
  locator: Three original native validate runs, render --content comparisons and git
    blob hash checks
  accessed_at: '2026-11-03T10:50:14.226798Z'
  snapshot_sha256: 812960f1524b688981fdb85a0f8ae3525ad4d186c3a7a7415565407ede1ecce8
  summary: All three original pairs validate and render byte-identically. Their frozen
    target hashes match both original source9c0446c4 and current source; no stale
    input in this slice. Historical global executions remain historical.
  support: supports
- evidence_id: micro-record-cis_golgi_network_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/cis_golgi_network_membrane.yaml
  locator: Complete current YAML at cee44c9b340b36e4e103ebd16c4bfcf6745bd41f
  accessed_at: '2026-11-03T10:54:57.309459Z'
  snapshot_sha256: c818f4de1c2fd8c36bc121d4389ce017c59526e083e6aefdf1b2a0041411da9c
  summary: Whole unchanged target read, including identity, definition, taxon/strain
    examples, constituents, evidence, graph, scope notes, discussions and history.
    Original frozen hash remains current.
  support: supports
- evidence_id: micro-prior-cis_golgi_network_membrane
  kind: prior_review
  reference: reviews/structured/20261021T111327Z-cis-golgi-network-membrane-audit/review.yaml
  locator: Entire original YAML and deterministic Markdown
  accessed_at: '2026-11-03T10:54:57.309459Z'
  snapshot_sha256: c2cb05552b9ddc319f82c78f28c7e7b76b653cf0bfb30fac5fac3babdb7b8562
  summary: Exact immutable 20261021T111327Z-cis-golgi-network-membrane-audit; original
    verdict needs_curation with 2 scientific findings. Original access dates and checks
    are not silently renewed.
  support: supports
- evidence_id: micro-native-cis_golgi_network_membrane-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/cis_golgi_network_membrane-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cis_golgi_network_membrane.yaml
    --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/cis_golgi_network_membrane-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T10:50:09.075758Z'
  snapshot_sha256: f4cd44eca0a643c5fc20bde7e5c6a5a76bf812f38fa33ddd89b9e1b26c8f2969
  summary: Actual exit0 at cee44c9b340b36e4e103ebd16c4bfcf6745bd41f from 2026-11-03T10:50:08.672089+00:00
    to 2026-11-03T10:50:09.075758+00:00. Empty protein-example inventory and zero
    GENE_OR_PROTEIN nodes. Passing empty scope does not verify narrative trafficking
    proteins or experimental occurrence.
  support: supports
- evidence_id: micro-native-cis_golgi_network_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/cis_golgi_network_membrane-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cis_golgi_network_membrane.yaml
    --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/cis_golgi_network_membrane-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T10:50:09.513675Z'
  snapshot_sha256: bf7c06f594913d77b52517604ab9170faaa738b05c83eab24be38d24ae0ddf2d
  summary: Actual exit0 at cee44c9b340b36e4e103ebd16c4bfcf6745bd41f from 2026-11-03T10:50:09.111556+00:00
    to 2026-11-03T10:50:09.513675+00:00. Empty protein-example inventory and zero
    GENE_OR_PROTEIN nodes. Passing empty scope does not verify narrative trafficking
    proteins or experimental occurrence.
  support: supports
- evidence_id: micro-record-coated_vesicle
  kind: record_content
  reference: data/structures/membrane_organelle/coated_vesicle.yaml
  locator: Complete current YAML at cee44c9b340b36e4e103ebd16c4bfcf6745bd41f
  accessed_at: '2026-11-03T10:54:57.309459Z'
  snapshot_sha256: baf2f374fd87cb07f0ae0a31c5962cfa34c345941f872a96759858c88c8218c1
  summary: Whole unchanged target read, including identity, definition, taxon/strain
    examples, constituents, evidence, graph, scope notes, discussions and history.
    Original frozen hash remains current.
  support: supports
- evidence_id: micro-prior-coated_vesicle
  kind: prior_review
  reference: reviews/structured/20261021T111333Z-coated-vesicle-audit/review.yaml
  locator: Entire original YAML and deterministic Markdown
  accessed_at: '2026-11-03T10:54:57.309459Z'
  snapshot_sha256: 2d21b43cbb854d99973d35da5ee51136319c90bdc7fd1aa1f111f15441554b1c
  summary: Exact immutable 20261021T111333Z-coated-vesicle-audit; original verdict
    needs_curation with 1 scientific findings. Original access dates and checks are
    not silently renewed.
  support: supports
- evidence_id: micro-native-coated_vesicle-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/coated_vesicle-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/coated_vesicle.yaml
    --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/coated_vesicle-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T10:50:16.858845Z'
  snapshot_sha256: 521142d9f4a2369b1b5a301070f7ae4c02c7c4033a1dae0bd0dafddb07d881fa
  summary: Actual exit0 at cee44c9b340b36e4e103ebd16c4bfcf6745bd41f from 2026-11-03T10:50:15.237964+00:00
    to 2026-11-03T10:50:16.858845+00:00. Six reviewed S288C examples; one GENE_OR_PROTEIN
    node COVERED. RET1 ambiguity is a prose/query finding despite valid representative
    accession and native coverage.
  support: supports
- evidence_id: micro-native-coated_vesicle-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/coated_vesicle-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/coated_vesicle.yaml
    --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/coated_vesicle-uniprot-causal.log
    SHA256 964400df2eca2a7f65a0941ad15132db748cdda186e8562931cbd43bde0d4464
  accessed_at: '2026-11-03T10:50:17.293425Z'
  snapshot_sha256: 0f532f5a0a332f842d6fb60ba381b93ae73c1c838ccf6e865c39e3825cc23e9d
  summary: Actual exit0 at cee44c9b340b36e4e103ebd16c4bfcf6745bd41f from 2026-11-03T10:50:16.889146+00:00
    to 2026-11-03T10:50:17.293425+00:00. Six reviewed S288C examples; one GENE_OR_PROTEIN
    node COVERED. RET1 ambiguity is a prose/query finding despite valid representative
    accession and native coverage.
  support: supports
- evidence_id: micro-record-coated_vesicle_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/coated_vesicle_membrane.yaml
  locator: Complete current YAML at cee44c9b340b36e4e103ebd16c4bfcf6745bd41f
  accessed_at: '2026-11-03T10:54:57.309459Z'
  snapshot_sha256: b74f6c754d374d664267834c903c7bb2aed86f79145de8ce69f6ea9785bbebcc
  summary: Whole unchanged target read, including identity, definition, taxon/strain
    examples, constituents, evidence, graph, scope notes, discussions and history.
    Original frozen hash remains current.
  support: supports
- evidence_id: micro-prior-coated_vesicle_membrane
  kind: prior_review
  reference: reviews/structured/20261021T111334Z-coated-vesicle-membrane-audit/review.yaml
  locator: Entire original YAML and deterministic Markdown
  accessed_at: '2026-11-03T10:54:57.309459Z'
  snapshot_sha256: 2232e0751eacf3e99b4e0f79257808634c6c51fe1e973c6947f80f5da7a5376a
  summary: Exact immutable 20261021T111334Z-coated-vesicle-membrane-audit; original
    verdict pass_with_limitations with 0 scientific findings. Original access dates
    and checks are not silently renewed.
  support: supports
- evidence_id: micro-native-coated_vesicle_membrane-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/coated_vesicle_membrane-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/coated_vesicle_membrane.yaml
    --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/coated_vesicle_membrane-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T10:50:17.729675Z'
  snapshot_sha256: d7997f0bd8c451e0ff8b4ef83c6829673466c1ca36f82e53d1d38664b1dbb78c
  summary: Actual exit0 at cee44c9b340b36e4e103ebd16c4bfcf6745bd41f from 2026-11-03T10:50:17.323529+00:00
    to 2026-11-03T10:50:17.729675+00:00. Empty protein-example inventory and zero
    GENE_OR_PROTEIN nodes. Passing empty scope does not verify narrative trafficking
    proteins or experimental occurrence.
  support: supports
- evidence_id: micro-native-coated_vesicle_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/coated_vesicle_membrane-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/coated_vesicle_membrane.yaml
    --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/coated_vesicle_membrane-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T10:50:18.158515Z'
  snapshot_sha256: 689cab2f571b7ed3101595b4a786ab3742498b76aa899bb75a0e3fd63804df56
  summary: Actual exit0 at cee44c9b340b36e4e103ebd16c4bfcf6745bd41f from 2026-11-03T10:50:17.760485+00:00
    to 2026-11-03T10:50:18.158515+00:00. Empty protein-example inventory and zero
    GENE_OR_PROTEIN nodes. Passing empty scope does not verify narrative trafficking
    proteins or experimental occurrence.
  support: supports
- evidence_id: micro-neighbor-cis_golgi_network
  kind: record_content
  reference: data/structures/membrane_organelle/cis_golgi_network.yaml
  locator: Frozen identity, definition, kind, hierarchy/parthood/has_part; coat neighbors
    additionally component IDs/labels/groundings/gene_symbols
  accessed_at: '2026-11-03T10:54:57.309459Z'
  snapshot_sha256: 369cae5270aeacd25a94317be3b005167773bd89a5e4c2583061fa24cd79f31d
  summary: 'Boundary context only: cis_golgi_network. Supports distinction of whole
    compartments/membranes and generic versus subtype coats. No full neighboring-record
    source review or resolution of their findings is claimed.'
  support: supports
- evidence_id: micro-neighbor-golgi_apparatus
  kind: record_content
  reference: data/structures/membrane_organelle/golgi_apparatus.yaml
  locator: Frozen identity, definition, kind, hierarchy/parthood/has_part; coat neighbors
    additionally component IDs/labels/groundings/gene_symbols
  accessed_at: '2026-11-03T10:54:57.309459Z'
  snapshot_sha256: e3df76cd9d71ba04df9e5349475bd4191c31f93156acd422ef6b0223b88facca
  summary: 'Boundary context only: golgi_apparatus. Supports distinction of whole
    compartments/membranes and generic versus subtype coats. No full neighboring-record
    source review or resolution of their findings is claimed.'
  support: supports
- evidence_id: micro-neighbor-vesicle_coat
  kind: record_content
  reference: data/structures/other/vesicle_coat.yaml
  locator: Frozen identity, definition, kind, hierarchy/parthood/has_part; coat neighbors
    additionally component IDs/labels/groundings/gene_symbols
  accessed_at: '2026-11-03T10:54:57.309459Z'
  snapshot_sha256: d8bd367b310d26010f7c909b47b7e5b8676be216b22e81a69eab083d506c3818
  summary: 'Boundary context only: vesicle_coat. Supports distinction of whole compartments/membranes
    and generic versus subtype coats. No full neighboring-record source review or
    resolution of their findings is claimed.'
  support: supports
- evidence_id: micro-neighbor-clathrin_vesicle_coat
  kind: record_content
  reference: data/structures/other/clathrin_vesicle_coat.yaml
  locator: Frozen identity, definition, kind, hierarchy/parthood/has_part; coat neighbors
    additionally component IDs/labels/groundings/gene_symbols
  accessed_at: '2026-11-03T10:54:57.309459Z'
  snapshot_sha256: cef674eb9fc2b08323c1780daa340012db00fd43e3f89c7de880ac972594e17d
  summary: 'Boundary context only: clathrin_vesicle_coat. Supports distinction of
    whole compartments/membranes and generic versus subtype coats. No full neighboring-record
    source review or resolution of their findings is claimed.'
  support: supports
- evidence_id: micro-neighbor-copi_vesicle_coat
  kind: record_content
  reference: data/structures/other/copi_vesicle_coat.yaml
  locator: Frozen identity, definition, kind, hierarchy/parthood/has_part; coat neighbors
    additionally component IDs/labels/groundings/gene_symbols
  accessed_at: '2026-11-03T10:54:57.309459Z'
  snapshot_sha256: 1b264ad3800f2c5c8c78d327f63a32bdc73888a003e3be3fcad778bb9f993195
  summary: 'Boundary context only: copi_vesicle_coat. Supports distinction of whole
    compartments/membranes and generic versus subtype coats. No full neighboring-record
    source review or resolution of their findings is claimed.'
  support: supports
- evidence_id: micro-neighbor-copii_vesicle_coat
  kind: record_content
  reference: data/structures/other/copii_vesicle_coat.yaml
  locator: Frozen identity, definition, kind, hierarchy/parthood/has_part; coat neighbors
    additionally component IDs/labels/groundings/gene_symbols
  accessed_at: '2026-11-03T10:54:57.309459Z'
  snapshot_sha256: 3b7c89b408581ddfd7f40203a1810eda738e87b1d2457812209b8586abbb0ef2
  summary: 'Boundary context only: copii_vesicle_coat. Supports distinction of whole
    compartments/membranes and generic versus subtype coats. No full neighboring-record
    source review or resolution of their findings is claimed.'
  support: supports
- evidence_id: micro-cis-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005783,GO:0005794,GO:0005801,GO:0033106,GO:0098791
  locator: Retained2026-11-03T10:11Z packet, reassessed for the membrane target; QuickGO
    exact GO:0005801/0033106/0005794/0098791/0005783 active terms, definitions, synonyms,
    comments and children
  accessed_at: '2026-11-03T10:11:08.059163Z'
  snapshot_sha256: 1f64f46ea3228d75112cc4a7cd62683682181d7f56a4b695efb1f8f03db842e8
  summary: Unchanged source snapshot reused with its actual original access time.
    CGN is an ER-abutting network distinct from its membrane and whole Golgi; current
    GO explicitly says CGN is not part of the Golgi stack. Broader cis-face synonyms
    are not exact identities.
  support: supports
- evidence_id: micro-cis-tax-4922
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4922
  locator: Retained2026-11-03T10:11Z packet, reassessed for the membrane target; ENA
    taxonomy exact taxId/scientificName/rank/lineage/otherNames
  accessed_at: '2026-11-03T10:11:09.052648Z'
  snapshot_sha256: 97a9231814c8f3647963f28cdbbdffca2dc1067a0136592a0f0d37babb846ee3
  summary: Unchanged source snapshot reused with its actual original access time.
    Current authority identifies 4922 as Komagataella pastoris. Species and strain
    scope are retained; historical Pichia naming is not used as a current strain identity
    bridge.
  support: supports
- evidence_id: micro-cis-tax-460519
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/460519
  locator: Retained2026-11-03T10:11Z packet, reassessed for the membrane target; ENA
    taxonomy exact taxId/scientificName/rank/lineage/otherNames
  accessed_at: '2026-11-03T10:11:09.053105Z'
  snapshot_sha256: d7cb478e59011f67e93469d8e1b458585b0e2373435fdad6ffc5962069f62a31
  summary: Unchanged source snapshot reused with its actual original access time.
    Current authority identifies 460519 as Komagataella phaffii. Species and strain
    scope are retained; historical Pichia naming is not used as a current strain identity
    bridge.
  support: supports
- evidence_id: micro-cis-jats-PMC2148216
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2148216.1/PMC2148216.1.xml
  locator: Retained2026-11-03T10:11Z packet, reassessed for the membrane target; DOI10.1083/jcb.145.1.69;
    Methods Strains and Plasmids, complete Results and complete Discussion; text only
  accessed_at: '2026-11-03T10:11:09.799368Z'
  snapshot_sha256: e9eb8235003747a36696a90d27a3fd45f601b1e46dfb3bba5419d779b5fe9590
  summary: Unchanged source snapshot reused with its actual original access time.
    PPY1/PPY12 experiments establish coherent Golgi stacks adjacent to transitional
    ER. Sec13-positive tubulovesicular interface is interpreted as tER; Och1/late-marker
    apposition does not independently identify a distinct CGN. Whole primary narrative
    does not establish absence of CGN. No raw micrograph/pixel audit or full supplementary
    analysis.
  support: supports
- evidence_id: micro-cis-atcc-204163
  kind: authority
  reference: https://www.atcc.org/products/204163
  locator: Retained2026-11-03T10:11Z packet, reassessed for the membrane target; ATCC204163
    product identity, Strain designation PPY12, Genotype his4 arg4, Characteristics
    Comments
  accessed_at: '2026-11-03T10:11:09.799560Z'
  snapshot_sha256: 871a39203ad01dd26935f6aedb49c60d70abce7f7ac74977069748beb44e2ba6
  summary: Unchanged source snapshot reused with its actual original access time.
    PPY12 is K. phaffii; ATCC explicitly describes the change from K. pastoris based
    on in-house sequence analysis. This is a strain identity bridge, not evidence
    of organelle occurrence.
  support: supports
- evidence_id: micro-cis-ena-LC815816
  kind: authority
  reference: https://www.ebi.ac.uk/ena/browser/api/embl/LC815816.1?download=false
  locator: Retained2026-11-03T10:11Z packet, reassessed for the membrane target; ENA
    LC815816.1 EMBL FT source qualifiers organism/strain/db_xref
  accessed_at: '2026-11-03T10:11:09.967152Z'
  snapshot_sha256: f02d748dce33d5c56b830ab9e96ccb14facd65a8a7621bdaa10c7711eb8d63b4
  summary: Unchanged source snapshot reused with its actual original access time.
    Source qualifiers identify Komagataella phaffii PPY12, taxon460519. Corroborates
    the strain bridge independently of historical name; ATG14 sequence is not evidence
    of CGN membership/function.
  support: supports
- evidence_id: micro-cis-cho2000-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1016/S0014-5793%2800%2901268-0%22
  locator: Retained2026-11-03T10:11Z packet, reassessed for the membrane target; DOI10.1016/S0014-5793(00)01268-0;
    exact metadata and complete primary abstract only
  accessed_at: '2026-11-03T10:11:10.006407Z'
  snapshot_sha256: b0960521e38911bcc0523d02dcbc5d953440044fcace3d795af4bf575d3fd67f
  summary: Unchanged source snapshot reused with its actual original access time.
    S. cerevisiae Sed5 membrane immunoisolation enriches early-Golgi mannosyltransferases
    and excludes late-Golgi/ER markers. This limited abstract does not establish K.
    pastoris/phaffii CGN occurrence or universally essential resident proteins; both
    publisher body/PDF attempts403.
  support: partial
- evidence_id: micro-cis-go-parent
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000139
  locator: QuickGO exact GO:0000139 active name, definition and returned children
  accessed_at: '2026-11-03T10:50:15.147824Z'
  snapshot_sha256: c72b414cdeea8f8b7e171c6ba56625fba7b621cbf2eb987f05aa8635300f8f6f
  summary: Golgi membrane denotes the lipid bilayer surrounding Golgi compartments.
    This is appropriate broader membrane context; no current direct GO is_a edge absent
    from this response is invented.
  support: supports
- evidence_id: micro-coated-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0012507,GO:0016192,GO:0030120,GO:0030125,GO:0030126,GO:0030127,GO:0030134,GO:0030135,GO:0030136,GO:0030137,GO:0030662,GO:0030663,GO:0030665,GO:0031410
  locator: All exact returned GO identifiers, active flags, definitions, synonyms
    and is_a/part_of children
  accessed_at: '2026-11-03T10:50:09.031481Z'
  snapshot_sha256: a363327108a025a02c180493d4af6fcdc2c436eb631f447835d0de66dbc5e0a3
  summary: Current authority distinguishes coated vesicle, surrounding membrane, generic
    coat and clathrin/COPI/COPII subtypes. GO:0030662 explicitly lists GO:0030120
    vesicle coat as part_of child; generic lipid-bilayer intuition is not substituted
    for this maintained ontology relationship. Transport process and cytoplasmic-vesicle
    parent terms are exact.
  support: supports
- evidence_id: micro-coat-membrane-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0012507,GO:0030120,GO:0030135,GO:0030659,GO:0030662,GO:0030663,GO:0030665
  locator: All exact returned GO identifiers, active flags, definitions, synonyms
    and is_a/part_of children
  accessed_at: '2026-11-03T10:50:15.094547Z'
  snapshot_sha256: 68c2d00f0838d6ba737cc7ee8c2971cef18217d0e6376faf5ecb4727ff237fb1
  summary: Current authority distinguishes coated vesicle, surrounding membrane, generic
    coat and clathrin/COPI/COPII subtypes. GO:0030662 explicitly lists GO:0030120
    vesicle coat as part_of child; generic lipid-bilayer intuition is not substituted
    for this maintained ontology relationship. Transport process and cytoplasmic-vesicle
    parent terms are exact.
  support: supports
- evidence_id: micro-NCBITaxon-4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: ENA taxonomy exact taxId, scientificName, rank and lineage
  accessed_at: '2026-11-03T10:50:09.031825Z'
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
  summary: Verified 4932 Saccharomyces cerevisiae. Species-level experimental occurrence
    and representative S288C protein identity are distinct; this row does not equate
    experimental stocks to S288C.
  support: supports
- evidence_id: micro-NCBITaxon-559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: ENA taxonomy exact taxId, scientificName, rank and lineage
  accessed_at: '2026-11-03T10:50:09.301739Z'
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
  summary: Verified 559292 Saccharomyces cerevisiae S288C. Species-level experimental
    occurrence and representative S288C protein identity are distinct; this row does
    not equate experimental stocks to S288C.
  support: supports
- evidence_id: micro-PMID-8004676
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A8004676%20AND%20SRC%3AMED
  locator: 'Exact metadata and complete primary abstract; DOI10.1016/0092-8674(94)90138-4;
    title COPII: a membrane coat formed by Sec proteins that drive vesicle budding
    from the endoplasmic reticulum.'
  accessed_at: '2026-11-03T10:50:09.031904Z'
  snapshot_sha256: f3ff438cc130518602efe6aa0252c6d5634fafad949d62cf23e3a6e837819fc7
  summary: Complete primary abstract supports ER-derived COPII budding with Sar1/Sec13/Sec23
    complexes, distinct from COPI. GTP versus nonhydrolyzable nucleotide changes fusion
    competence. Four failed publisher routes are not full bodies; no full Barlowe
    Methods audit.
  support: partial
- evidence_id: micro-PMID-9568718
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A9568718%20AND%20SRC%3AMED
  locator: Exact metadata and complete primary abstract; DOI10.1016/s0092-8674(00)81577-9;
    title COPII-coated vesicle formation reconstituted with purified coat proteins
    and chemically defined liposomes.
  accessed_at: '2026-11-03T10:50:09.031954Z'
  snapshot_sha256: 0cdaf91dc4f4bf9261f55530522a8ed41116b930c39ac656de0d729c318bf1c0
  summary: Complete primary abstract supports sequential coat recruitment to native
    ER and defined liposomes, coated buds/vesicles and integrity of donor/product
    membranes. Full selected body passages are separately evidenced below.
  support: partial
- evidence_id: micro-PMID-10684247
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A10684247%20AND%20SRC%3AMED
  locator: 'Exact metadata and complete primary abstract; DOI10.1083/jcb.148.4.635;
    title The yeast nuclear pore complex: composition, architecture, and transport
    mechanism.'
  accessed_at: '2026-11-03T10:50:10.138597Z'
  snapshot_sha256: 396890291e0e08a1cd3edd1e908a21b784188ee72528b3f59607336b6e1cf750
  summary: Complete primary abstract concerns yeast nuclear-pore inventory/localization.
    It is consistent with the exact Q04491 nuclear-pore annotation cited by the record,
    not direct evidence for vesicle membership.
  support: partial
- evidence_id: micro-PMID-14562095
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A14562095%20AND%20SRC%3AMED
  locator: Exact metadata and complete primary abstract; DOI10.1038/nature02026; title
    Global analysis of protein localization in budding yeast.
  accessed_at: '2026-11-03T10:50:10.149429Z'
  snapshot_sha256: 8bbeed3381c96852db4221aac079da00e1bf5c50630629c24d4d9136e1645c21
  summary: Complete primary abstract concerns systematic GFP localization in yeast.
    The record correctly attributes P41810 Golgi-membrane localization to the UniProt
    experimental annotation; abstract does not independently expose every protein
    row.
  support: partial
- evidence_id: micro-doi-10.1016_j.devcel.2005.04.014
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.devcel.2005.04.014
  locator: Exact metadata and complete primary abstract; DOI10.1016/j.devcel.2005.04.014;
    title In vivo dynamics of clathrin and its adaptor-dependent recruitment to the
    actin-based endocytic machinery in yeast.
  accessed_at: '2026-11-03T10:50:09.375926Z'
  snapshot_sha256: c99ec084fa3f65e3b5107699c30f42b09489dbc49d6be518d71ff9352d5a199c
  summary: Complete primary abstract reports cortical/internal yeast clathrin and
    adaptor context. Full selected primary body is separately evidenced, without universal-necessity
    or single-vesicle resolution claims.
  support: partial
- evidence_id: micro-doi-10.1016_j.cell.2012.01.015
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.cell.2012.01.015
  locator: Exact metadata and complete primary abstract; DOI10.1016/j.cell.2012.01.015;
    title A structure-based mechanism for Arf1-dependent recruitment of coatomer to
    membranes.
  accessed_at: '2026-11-03T10:50:10.136772Z'
  snapshot_sha256: 720deee8d2fa1906684b6741443d65dbcafb8234d7e28b5fb4945db432ec4fe8
  summary: Complete primary abstract reports Arf1/coatomer structural and biochemical
    recruitment model. Actual mammalian/yeast construct scopes and model limits are
    retained in the separately inspected body.
  support: partial
- evidence_id: micro-matsuoka1998-author
  kind: primary_source
  reference: https://bednareklab.biochem.wisc.edu/wp-content/uploads/sites/1623/2022/02/1998_Matsuoka_etal_Cell.pdf
  locator: DOI10.1016/S0092-8674(00)81577-9; printed p269 native/synthetic comparison
    and integrity Results; pp270-271 Discussion Vesicle Morphogenesis Governed by
    COPII Coat; Figure7 caption; p273 Strain and Materials; p274 stoichiometry Methods
  accessed_at: '2026-11-03T10:50:14.504240Z'
  snapshot_sha256: 4c7e8eafea53f213b25b339d684115bd65a1af9e79d86b9e1222050aa52b0efa
  summary: Fresh genuine author-hosted primary PDF text. Native microsome-derived
    and synthetic liposome-derived COPII vesicles are explicitly compared; RSY445
    supplies ER-enriched microsomes. These support whole-vesicle native-ER and membrane
    synthetic-liposome examples. Reconstitution requirements do not become universal
    in vivo necessities, and the strain is not assumed identical to S288C. No figure
    pixels/raw data/full-paper audit.
  support: supports
- evidence_id: micro-newpher2005-duke
  kind: primary_source
  reference: https://dukespace.lib.duke.edu/server/api/core/bitstreams/e3c70c30-e4a1-4ba0-8ea6-c50af4ba491e/content
  locator: DOI10.1016/j.devcel.2005.04.014; printed pp87-89 Summary, Introduction,
    Table1, Results Localization of Clathrin In Vivo and Figure1 caption
  accessed_at: '2026-11-03T10:50:10.151680Z'
  snapshot_sha256: c848e911372b9afb9902e4a74e3cb3dd66ef90eb5e102024cc95fff648bb6c21
  summary: Fresh genuine institutional primary PDF. Yeast fluorescent heavy/light
    chains colocalize in cortical and intracellular structures; larger puncta partly
    overlap TGN/endosomal markers. Diffraction-limited puncta are not all proven mature
    vesicles. Broad clathrin-context support does not require one coat subtype or
    universally essential adaptor. No later body/movie/pixel audit.
  support: supports
- evidence_id: micro-yu2012-s3
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3285272.1/PMC3285272.1.xml
  locator: DOI10.1016/j.cell.2012.01.015; complete Introduction; Results Experimental
    Approach and A Model for Arf1-Dependent Recruitment of Coatomer to Membranes
  accessed_at: '2026-11-03T10:50:10.213884Z'
  snapshot_sha256: a7adecb3e84137dcc05565185633b97cd4c07fc8e2556c98e9922152c7d34ea6
  summary: Genuine primary JATS. Mammalian coatomer subcomplexes with defined human/yeast
    truncated Arf1 constructs support a bounded recruitment model. COPI, COPII and
    clathrin/AP systems are distinguished; proposed conformational effects remain
    proposals. Not direct accession-specific evidence for every yeast coat example,
    nor complete Methods/raw-data audit.
  support: supports
- evidence_id: micro-UniProtKB-P22137
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P22137.json
  locator: Exact UniProtKB entryType, primaryAccession, organism, genes, proteinDescription;
    SUBCELLULAR LOCATION and its source annotations
  accessed_at: '2026-11-03T10:50:10.651153Z'
  snapshot_sha256: 09d51b91c677526fa74c1513304fdd8c51215ce5c9511a6654355fbd16c61648
  summary: Reviewed S288C accession P22137 primary gene CHC1; identity and native
    localization-annotation scope checked. Q04491 PMID10684247 specifically annotates
    nuclear pore; P41810 PMID14562095 specifically annotates Golgi membrane. P53622
    is coatomer alpha/COP1 with RET1 synonym; P22276 is RNA-polymerase-III RET1. Identity
    verification alone does not establish universal coat membership/necessity.
  support: supports
- evidence_id: micro-UniProtKB-P17891
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P17891.json
  locator: Exact UniProtKB entryType, primaryAccession, organism, genes, proteinDescription;
    SUBCELLULAR LOCATION and its source annotations
  accessed_at: '2026-11-03T10:50:10.758719Z'
  snapshot_sha256: 1b6e6853470eea45530073217e5f1abcfbe6fba0fc5568df34d83a73130d25af
  summary: Reviewed S288C accession P17891 primary gene CLC1; identity and native
    localization-annotation scope checked. Q04491 PMID10684247 specifically annotates
    nuclear pore; P41810 PMID14562095 specifically annotates Golgi membrane. P53622
    is coatomer alpha/COP1 with RET1 synonym; P22276 is RNA-polymerase-III RET1. Identity
    verification alone does not establish universal coat membership/necessity.
  support: supports
- evidence_id: micro-UniProtKB-Q04491
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q04491.json
  locator: Exact UniProtKB entryType, primaryAccession, organism, genes, proteinDescription;
    SUBCELLULAR LOCATION and its source annotations
  accessed_at: '2026-11-03T10:50:10.895910Z'
  snapshot_sha256: 5ea1f9385e1989653cc9b1251babdb2a1e325e72d3b3617590028f3fca38207c
  summary: Reviewed S288C accession Q04491 primary gene SEC13; identity and native
    localization-annotation scope checked. Q04491 PMID10684247 specifically annotates
    nuclear pore; P41810 PMID14562095 specifically annotates Golgi membrane. P53622
    is coatomer alpha/COP1 with RET1 synonym; P22276 is RNA-polymerase-III RET1. Identity
    verification alone does not establish universal coat membership/necessity.
  support: supports
- evidence_id: micro-UniProtKB-P38968
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P38968.json
  locator: Exact UniProtKB entryType, primaryAccession, organism, genes, proteinDescription;
    SUBCELLULAR LOCATION and its source annotations
  accessed_at: '2026-11-03T10:50:10.944018Z'
  snapshot_sha256: 3cd679eb515caf22dceb7f5a2b97bb726ea5a88379f3117f90f10ab06364d1fc
  summary: Reviewed S288C accession P38968 primary gene SEC31; identity and native
    localization-annotation scope checked. Q04491 PMID10684247 specifically annotates
    nuclear pore; P41810 PMID14562095 specifically annotates Golgi membrane. P53622
    is coatomer alpha/COP1 with RET1 synonym; P22276 is RNA-polymerase-III RET1. Identity
    verification alone does not establish universal coat membership/necessity.
  support: supports
- evidence_id: micro-UniProtKB-P41810
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P41810.json
  locator: Exact UniProtKB entryType, primaryAccession, organism, genes, proteinDescription;
    SUBCELLULAR LOCATION and its source annotations
  accessed_at: '2026-11-03T10:50:11.102232Z'
  snapshot_sha256: 14db746dd9b7298b293cb31c5f9c75daf9d58bf6702ffb741a3c9678c17d1520
  summary: Reviewed S288C accession P41810 primary gene SEC26; identity and native
    localization-annotation scope checked. Q04491 PMID10684247 specifically annotates
    nuclear pore; P41810 PMID14562095 specifically annotates Golgi membrane. P53622
    is coatomer alpha/COP1 with RET1 synonym; P22276 is RNA-polymerase-III RET1. Identity
    verification alone does not establish universal coat membership/necessity.
  support: supports
- evidence_id: micro-UniProtKB-P53622
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P53622.json
  locator: Exact UniProtKB entryType, primaryAccession, organism, genes, proteinDescription;
    SUBCELLULAR LOCATION and its source annotations
  accessed_at: '2026-11-03T10:50:11.450980Z'
  snapshot_sha256: 3fa8e6ac02935b57b3588e23901528210478283bbb5311fd3d3118999af5ced3
  summary: Reviewed S288C accession P53622 primary gene COP1; identity and native
    localization-annotation scope checked. Q04491 PMID10684247 specifically annotates
    nuclear pore; P41810 PMID14562095 specifically annotates Golgi membrane. P53622
    is coatomer alpha/COP1 with RET1 synonym; P22276 is RNA-polymerase-III RET1. Identity
    verification alone does not establish universal coat membership/necessity.
  support: supports
- evidence_id: micro-UniProtKB-P22276
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P22276.json
  locator: Exact UniProtKB entryType, primaryAccession, organism, genes, proteinDescription;
    SUBCELLULAR LOCATION and its source annotations
  accessed_at: '2026-11-03T10:50:15.397868Z'
  snapshot_sha256: 6350861516db02ef2e6d782e0e1c3f10840ebcc196560e5fa7a2cd8cb4d97c92
  summary: Reviewed S288C accession P22276 primary gene RET1; identity and native
    localization-annotation scope checked. Q04491 PMID10684247 specifically annotates
    nuclear pore; P41810 PMID14562095 specifically annotates Golgi membrane. P53622
    is coatomer alpha/COP1 with RET1 synonym; P22276 is RNA-polymerase-III RET1. Identity
    verification alone does not establish universal coat membership/necessity.
  support: supports
- evidence_id: micro-query-CHC1-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3ACHC1%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete current UniProt reviewed exact-gene/taxon query and pagination
    metadata
  accessed_at: '2026-11-03T10:50:11.519171Z'
  snapshot_sha256: 2a920614f72637e8dca08d8a782c81c920e1e8a01fd1b0b958f6d70602c68b89
  summary: 'Current query returns 1 entries: P22137. RET1 ambiguity is current, not
    a reconstruction of the historical retrieval. Correct COP1 representative is retained.'
  support: supports
  search_scope: UniProtKB literal URL https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3ACHC1%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29;
    accessed 2026-11-03T10:50:11.519171+00:00; gene_exact=CHC1, taxonomy_id559292,
    reviewed:true, size500; complete returned response total_results=1, Link=None.
    Only this query/date/taxon; no universal uniqueness/absence claim.
- evidence_id: micro-query-CLC1-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3ACLC1%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete current UniProt reviewed exact-gene/taxon query and pagination
    metadata
  accessed_at: '2026-11-03T10:50:11.974374Z'
  snapshot_sha256: 263ed77f230c390b1cf03ce642b609d8cff66ef219794d4c6bccab47942bbc69
  summary: 'Current query returns 1 entries: P17891. RET1 ambiguity is current, not
    a reconstruction of the historical retrieval. Correct COP1 representative is retained.'
  support: supports
  search_scope: UniProtKB literal URL https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3ACLC1%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29;
    accessed 2026-11-03T10:50:11.974374+00:00; gene_exact=CLC1, taxonomy_id559292,
    reviewed:true, size500; complete returned response total_results=1, Link=None.
    Only this query/date/taxon; no universal uniqueness/absence claim.
- evidence_id: micro-query-SEC13-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3ASEC13%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete current UniProt reviewed exact-gene/taxon query and pagination
    metadata
  accessed_at: '2026-11-03T10:50:11.989706Z'
  snapshot_sha256: 8967ba9e2ec39d6cb3ef7e6da9e8cd5ceb82f150094d58f932574e30155b6cba
  summary: 'Current query returns 1 entries: Q04491. RET1 ambiguity is current, not
    a reconstruction of the historical retrieval. Correct COP1 representative is retained.'
  support: supports
  search_scope: UniProtKB literal URL https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3ASEC13%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29;
    accessed 2026-11-03T10:50:11.989706+00:00; gene_exact=SEC13, taxonomy_id559292,
    reviewed:true, size500; complete returned response total_results=1, Link=None.
    Only this query/date/taxon; no universal uniqueness/absence claim.
- evidence_id: micro-query-SEC31-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3ASEC31%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete current UniProt reviewed exact-gene/taxon query and pagination
    metadata
  accessed_at: '2026-11-03T10:50:12.795132Z'
  snapshot_sha256: 9860d546b4ea67784200cb6bee02e10605b6e5674b9827ce546fa20eecfaf685
  summary: 'Current query returns 1 entries: P38968. RET1 ambiguity is current, not
    a reconstruction of the historical retrieval. Correct COP1 representative is retained.'
  support: supports
  search_scope: UniProtKB literal URL https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3ASEC31%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29;
    accessed 2026-11-03T10:50:12.795132+00:00; gene_exact=SEC31, taxonomy_id559292,
    reviewed:true, size500; complete returned response total_results=1, Link=None.
    Only this query/date/taxon; no universal uniqueness/absence claim.
- evidence_id: micro-query-SEC26-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3ASEC26%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete current UniProt reviewed exact-gene/taxon query and pagination
    metadata
  accessed_at: '2026-11-03T10:50:12.865779Z'
  snapshot_sha256: 7d2571f17957840503323f13c6caa07bafaac786466d4aae0c7d4755b2e4818a
  summary: 'Current query returns 1 entries: P41810. RET1 ambiguity is current, not
    a reconstruction of the historical retrieval. Correct COP1 representative is retained.'
  support: supports
  search_scope: UniProtKB literal URL https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3ASEC26%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29;
    accessed 2026-11-03T10:50:12.865779+00:00; gene_exact=SEC26, taxonomy_id559292,
    reviewed:true, size500; complete returned response total_results=1, Link=None.
    Only this query/date/taxon; no universal uniqueness/absence claim.
- evidence_id: micro-query-COP1-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3ACOP1%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete current UniProt reviewed exact-gene/taxon query and pagination
    metadata
  accessed_at: '2026-11-03T10:50:13.918775Z'
  snapshot_sha256: 7ae16d897c8db90416843060a4f2e9120b0e3613f4106d9634bcf9dc662bbe3a
  summary: 'Current query returns 1 entries: P53622. RET1 ambiguity is current, not
    a reconstruction of the historical retrieval. Correct COP1 representative is retained.'
  support: supports
  search_scope: UniProtKB literal URL https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3ACOP1%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29;
    accessed 2026-11-03T10:50:13.918775+00:00; gene_exact=COP1, taxonomy_id559292,
    reviewed:true, size500; complete returned response total_results=1, Link=None.
    Only this query/date/taxon; no universal uniqueness/absence claim.
- evidence_id: micro-query-RET1-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3ARET1%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete current UniProt reviewed exact-gene/taxon query and pagination
    metadata
  accessed_at: '2026-11-03T10:50:14.131856Z'
  snapshot_sha256: e08053c7530d77cd89e56c7471167d1ff5c188e01f31390c1a89d329b7b1fe7a
  summary: 'Current query returns 2 entries: P22276, P53622. RET1 ambiguity is current,
    not a reconstruction of the historical retrieval. Correct COP1 representative
    is retained.'
  support: supports
  search_scope: UniProtKB literal URL https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3ARET1%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29;
    accessed 2026-11-03T10:50:14.131856+00:00; gene_exact=RET1, taxonomy_id559292,
    reviewed:true, size500; complete returned response total_results=2, Link=None.
    Only this query/date/taxon; no universal uniqueness/absence claim.
- evidence_id: micro-ipr-P22137
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/P22137/?page_size=200
  locator: InterPro all-entry/member matches for exact UniProt P22137; full returned
    page, count21, next=None
  accessed_at: '2026-11-03T10:50:15.682835Z'
  snapshot_sha256: e39182fe41f5d9e37a897f56b3a830258ca615a6e21dd337255f3a64aab64123
  summary: 'Bounded constituent family matches: IPR016341 Clathrin, heavy chain; PIRSF002290
    Clathrin heavy chain; PTHR10292 Clathrin heavy chain. Distinct protein families
    support heterogeneous coat scope; none is promoted to exact identity of the entire
    clathrin/COPI/COPII parent cohort or proof of residency.'
  support: context_only
- evidence_id: micro-ipr-P17891
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/P17891/?page_size=200
  locator: InterPro all-entry/member matches for exact UniProt P17891; full returned
    page, count4, next=None
  accessed_at: '2026-11-03T10:50:15.809749Z'
  snapshot_sha256: 46421befac88aec55b37b0c08e6d3708eec8ff5db0f71300b56a5af014624ea2
  summary: 'Bounded constituent family matches: IPR000996 Clathrin light chain; PF01086
    Clathrin light chain; PTHR10639 CLATHRIN LIGHT CHAIN. Distinct protein families
    support heterogeneous coat scope; none is promoted to exact identity of the entire
    clathrin/COPI/COPII parent cohort or proof of residency.'
  support: context_only
- evidence_id: micro-ipr-Q04491
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/Q04491/?page_size=200
  locator: InterPro all-entry/member matches for exact UniProt Q04491; full returned
    page, count11, next=None
  accessed_at: '2026-11-03T10:50:16.179798Z'
  snapshot_sha256: 307fd15d80f011edd635d4a24005b5871665080012fb5a5e354a426818f6767a
  summary: 'Bounded constituent family matches: IPR037363 Sec13/Seh1 family; PTHR11024
    NUCLEAR PORE COMPLEX PROTEIN SEC13 / SEH1 FAMILY MEMBER. Distinct protein families
    support heterogeneous coat scope; none is promoted to exact identity of the entire
    clathrin/COPI/COPII parent cohort or proof of residency.'
  support: context_only
- evidence_id: micro-ipr-P38968
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/P38968/?page_size=200
  locator: InterPro all-entry/member matches for exact UniProt P38968; full returned
    page, count23, next=None
  accessed_at: '2026-11-03T10:50:16.185168Z'
  snapshot_sha256: 03913f0833ca510083df7545552ad7e636bf00610ddebceab3448cdf0b1d1d96
  summary: 'Bounded constituent family matches: IPR040251 Protein transport protein
    SEC31-like; PF07304 Steroid receptor RNA activator (SRA1); PF11549 Protein transport
    protein SEC31; PTHR13923 SEC31-RELATED PROTEIN. Distinct protein families support
    heterogeneous coat scope; none is promoted to exact identity of the entire clathrin/COPI/COPII
    parent cohort or proof of residency.'
  support: context_only
- evidence_id: micro-ipr-P41810
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/P41810/?page_size=200
  locator: InterPro all-entry/member matches for exact UniProt P41810; full returned
    page, count15, next=None
  accessed_at: '2026-11-03T10:50:16.823008Z'
  snapshot_sha256: c8db9e49d0c0c160e2d3b8487f9c01f3f8327ad5a215c5c5a3e99ae553e2bd75
  summary: 'Bounded constituent family matches: IPR016460 Coatomer beta subunit (COPB1);
    PIRSF005727 Coatomer, beta subunit; PTHR10635 COATOMER SUBUNIT BETA. Distinct
    protein families support heterogeneous coat scope; none is promoted to exact identity
    of the entire clathrin/COPI/COPII parent cohort or proof of residency.'
  support: context_only
- evidence_id: micro-ipr-P53622
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/P53622/?page_size=200
  locator: InterPro all-entry/member matches for exact UniProt P53622; full returned
    page, count29, next=None
  accessed_at: '2026-11-03T10:50:17.048398Z'
  snapshot_sha256: 910a5af4b79703b8b1de589a632100e4e11a2145a3adea0d91d903b7459c2ab4
  summary: 'Bounded constituent family matches: IPR016391 Coatomer subunit alpha;
    IPR050844 Coatomer complex subunit; PIRSF003354 Coatomer, alpha subunit; PTHR19876
    Coatomer complex subunit. Distinct protein families support heterogeneous coat
    scope; none is promoted to exact identity of the entire clathrin/COPI/COPII parent
    cohort or proof of residency.'
  support: context_only
- evidence_id: micro-adapter-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Complete official iModulonDB organism/dataset catalogue
  accessed_at: '2026-11-03T10:50:15.271955Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  summary: No Saccharomyces, Komagataella or Pichia dataset appears in the returned
    catalogue; thus no matched-organism gene/module query is justified. This coverage
    limit does not establish biological absence.
  support: supports
  search_scope: iModulonDB GET https://imodulondb.org/api/datasets at 2026-11-03T10:50:15.271955+00:00;
    complete returned20 organism rows and28 organism-dataset pairs, no pagination
    advertised. Checked organism names and keys for Saccharomyces cerevisiae/S288C,
    Komagataella pastoris/phaffii and historical Pichia. No query into an unrelated
    organism dataset or universal absence inference.
- evidence_id: micro-historical-adapter-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Retained00:49Z kg-microbe-sources imodulondb datasets receipt, actual stderr/exit
  accessed_at: '2026-11-03T00:49:00.863225Z'
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Earlier actual invocation returned1 due to PermissionError opening pyvenv.cfg.
    This is a historical unavailable runner observation, not a fresh invocation or
    successful execution. Current official source catalogue was inspected as permitted
    fallback.
  support: context_only
- evidence_id: septin-review-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Structured Source Cross-Checks and immutable review workflow
  summary: Named molecular or pathway assertions trigger applicability even when in
    narrative context. Absence of transcriptomic claims is not an exemption. An unmatched
    organism permits bounded downstream non-applicability.
  accessed_at: '2026-11-03T10:54:55.867151Z'
  support: supports
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: septin-curation-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Structure identity, parthood, component grounding and source scope
  summary: Whole structures, constituent material and spatial regions are distinct.
    Optional inventories do not require unsupported constituents. Constitution, association
    and experimental formation dependency must not be conflated.
  accessed_at: '2026-11-03T10:54:55.867151Z'
  support: supports
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: septin-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: NONMECHANISTIC graph scope and material component_ref
  summary: Descriptive identity, parthood and enclosure may be nonmechanistic. Structural-material
    representation does not establish individual molecular formation necessity.
  accessed_at: '2026-11-03T10:54:55.867151Z'
  support: supports
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: septin-record-clathrin_coated_endocytic_vesicle
  kind: record_content
  reference: data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle.yaml
  locator: Entire current maintained record at cee44c9b340b36e4e103ebd16c4bfcf6745bd41f
  summary: Full identity, history, definitions, parent/part boundaries, components
    where present, taxonomic examples, functions, graph, evidence and discussions
    read. No images, measurements or verbatim snippets are declared.
  accessed_at: '2026-11-03T10:54:55.867151Z'
  support: supports
  snapshot_sha256: 3193e3f6ea811d515c1545dc4e9179c8122e8718a328ed11261c7b648e94343d
- evidence_id: septin-original-clathrin_coated_endocytic_vesicle
  kind: prior_review
  reference: reviews/structured/20261021T111328Z-clathrin-coated-endocytic-vesicle-audit/review.yaml
  locator: Entire original YAML/Markdown pair, frozen record hash, checks, source
    tiers, assessments, verdict and empty findings/actions
  summary: Original pass_with_limitations has no scientific finding or request-curation
    action. Its record bytes remain current. Historical source access and checks are
    not promoted to current execution.
  accessed_at: '2026-11-03T10:54:55.867151Z'
  support: supports
  snapshot_sha256: 6c8294738ce8825502a24e1ac67657062ce41feecca60a846364d259df1bb50e
- evidence_id: septin-original-validation-clathrin_coated_endocytic_vesicle
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/adversary-septin/original-checks.json
  locator: 20261021T111328Z-clathrin-coated-endocytic-vesicle-audit native validate/render;
    original source/current target hashes
  summary: Both commands exit0 and rendered Markdown is byte-identical. Current record
    bytes equal the original frozen hash and bytes at the historical source revision.
  accessed_at: '2026-11-03T10:50:39.465857Z'
  support: supports
  snapshot_sha256: 153a53b30853edf76af5d7d8fbf0ea945604fedfb8abc9a24b737cded5090951
- evidence_id: septin-native-clathrin_coated_endocytic_vesicle-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/clathrin_coated_endocytic_vesicle-uniprot-verify-receipt.json
  locator: Actual root command receipt plus /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/clathrin_coated_endocytic_vesicle-uniprot-verify.log
  summary: Exit0. No protein_examples, UniProtKB protein xrefs or GENE_OR_PROTEIN
    graph nodes are declared. Zero typed protein nodes means this success does not
    independently verify narrative clathrin/adaptor identity, localization, pathway
    mechanism or formation necessity.
  accessed_at: '2026-11-03T10:50:09.934733Z'
  support: supports
  snapshot_sha256: 1a57a356fd29ab76da41eda8710a7672c7d43efbbe727fed4d68d415b10e485f
- evidence_id: septin-native-clathrin_coated_endocytic_vesicle-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/clathrin_coated_endocytic_vesicle-uniprot-causal-receipt.json
  locator: Actual root command receipt plus /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/clathrin_coated_endocytic_vesicle-uniprot-causal.log
  summary: Exit0. No protein_examples, UniProtKB protein xrefs or GENE_OR_PROTEIN
    graph nodes are declared. Zero typed protein nodes means this success does not
    independently verify narrative clathrin/adaptor identity, localization, pathway
    mechanism or formation necessity.
  accessed_at: '2026-11-03T10:50:10.423003Z'
  support: supports
  snapshot_sha256: be63c52d3961d8a8b360bf7bd77d18aec36130a52dc1bf6acbd87175a7e7b1d6
- evidence_id: septin-record-clathrin_coated_endocytic_vesicle_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_lumen.yaml
  locator: Entire current maintained record at cee44c9b340b36e4e103ebd16c4bfcf6745bd41f
  summary: Full identity, history, definitions, parent/part boundaries, components
    where present, taxonomic examples, functions, graph, evidence and discussions
    read. No images, measurements or verbatim snippets are declared.
  accessed_at: '2026-11-03T10:54:55.867151Z'
  support: supports
  snapshot_sha256: d3a53daa5cc28635e48242bfa4d7dab04186a8c7f17b40a1491de51e94a33951
- evidence_id: septin-original-clathrin_coated_endocytic_vesicle_lumen
  kind: prior_review
  reference: reviews/structured/20261021T111329Z-clathrin-coated-endocytic-vesicle-lumen-audit/review.yaml
  locator: Entire original YAML/Markdown pair, frozen record hash, checks, source
    tiers, assessments, verdict and empty findings/actions
  summary: Original pass_with_limitations has no scientific finding or request-curation
    action. Its record bytes remain current. Historical source access and checks are
    not promoted to current execution.
  accessed_at: '2026-11-03T10:54:55.867151Z'
  support: supports
  snapshot_sha256: 04b141b90eac13e8f9763cb66ba3f35591dfdfca08cff3277995c6951bad78ee
- evidence_id: septin-original-validation-clathrin_coated_endocytic_vesicle_lumen
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/adversary-septin/original-checks.json
  locator: 20261021T111329Z-clathrin-coated-endocytic-vesicle-lumen-audit native validate/render;
    original source/current target hashes
  summary: Both commands exit0 and rendered Markdown is byte-identical. Current record
    bytes equal the original frozen hash and bytes at the historical source revision.
  accessed_at: '2026-11-03T10:50:40.601763Z'
  support: supports
  snapshot_sha256: 153a53b30853edf76af5d7d8fbf0ea945604fedfb8abc9a24b737cded5090951
- evidence_id: septin-native-clathrin_coated_endocytic_vesicle_lumen-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/clathrin_coated_endocytic_vesicle_lumen-uniprot-verify-receipt.json
  locator: Actual root command receipt plus /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/clathrin_coated_endocytic_vesicle_lumen-uniprot-verify.log
  summary: Exit0. No protein_examples, UniProtKB protein xrefs or GENE_OR_PROTEIN
    graph nodes are declared. Zero typed protein nodes means this success does not
    independently verify narrative clathrin/adaptor identity, localization, pathway
    mechanism or formation necessity.
  accessed_at: '2026-11-03T10:50:10.911411Z'
  support: supports
  snapshot_sha256: c68c2377a2a02734ffff8607f5c31033efa9ea5a739e200db5fc875e36a7e4ad
- evidence_id: septin-native-clathrin_coated_endocytic_vesicle_lumen-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/clathrin_coated_endocytic_vesicle_lumen-uniprot-causal-receipt.json
  locator: Actual root command receipt plus /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/clathrin_coated_endocytic_vesicle_lumen-uniprot-causal.log
  summary: Exit0. No protein_examples, UniProtKB protein xrefs or GENE_OR_PROTEIN
    graph nodes are declared. Zero typed protein nodes means this success does not
    independently verify narrative clathrin/adaptor identity, localization, pathway
    mechanism or formation necessity.
  accessed_at: '2026-11-03T10:50:11.422504Z'
  support: supports
  snapshot_sha256: ea903b9f14608fb90c53ca0e348549899ffdadb7c0886b25a44b3cb8fa1605fb
- evidence_id: septin-record-clathrin_coated_endocytic_vesicle_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_membrane.yaml
  locator: Entire current maintained record at cee44c9b340b36e4e103ebd16c4bfcf6745bd41f
  summary: Full identity, history, definitions, parent/part boundaries, components
    where present, taxonomic examples, functions, graph, evidence and discussions
    read. No images, measurements or verbatim snippets are declared.
  accessed_at: '2026-11-03T10:54:55.867151Z'
  support: supports
  snapshot_sha256: 70d8d315440e5cc7cc4c8f8c11a9103d74deffa773df25d9051113122d8a189a
- evidence_id: septin-original-clathrin_coated_endocytic_vesicle_membrane
  kind: prior_review
  reference: reviews/structured/20261021T111329Z-clathrin-coated-endocytic-vesicle-membrane-audit/review.yaml
  locator: Entire original YAML/Markdown pair, frozen record hash, checks, source
    tiers, assessments, verdict and empty findings/actions
  summary: Original pass_with_limitations has no scientific finding or request-curation
    action. Its record bytes remain current. Historical source access and checks are
    not promoted to current execution.
  accessed_at: '2026-11-03T10:54:55.867151Z'
  support: supports
  snapshot_sha256: ca324107ccb682459d538e6fdfebe6cba513319dcf615e44d2948637347327c4
- evidence_id: septin-original-validation-clathrin_coated_endocytic_vesicle_membrane
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/adversary-septin/original-checks.json
  locator: 20261021T111329Z-clathrin-coated-endocytic-vesicle-membrane-audit native
    validate/render; original source/current target hashes
  summary: Both commands exit0 and rendered Markdown is byte-identical. Current record
    bytes equal the original frozen hash and bytes at the historical source revision.
  accessed_at: '2026-11-03T10:50:41.742181Z'
  support: supports
  snapshot_sha256: 153a53b30853edf76af5d7d8fbf0ea945604fedfb8abc9a24b737cded5090951
- evidence_id: septin-native-clathrin_coated_endocytic_vesicle_membrane-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/clathrin_coated_endocytic_vesicle_membrane-uniprot-verify-receipt.json
  locator: Actual root command receipt plus /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/clathrin_coated_endocytic_vesicle_membrane-uniprot-verify.log
  summary: Exit0. No protein_examples, UniProtKB protein xrefs or GENE_OR_PROTEIN
    graph nodes are declared. Zero typed protein nodes means this success does not
    independently verify narrative clathrin/adaptor identity, localization, pathway
    mechanism or formation necessity.
  accessed_at: '2026-11-03T10:50:11.925027Z'
  support: supports
  snapshot_sha256: 4942c6f1be70fba7b421b4d1c557dcf9b33879834a9c7b850422f032a38ead20
- evidence_id: septin-native-clathrin_coated_endocytic_vesicle_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/clathrin_coated_endocytic_vesicle_membrane-uniprot-causal-receipt.json
  locator: Actual root command receipt plus /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/clathrin_coated_endocytic_vesicle_membrane-uniprot-causal.log
  summary: Exit0. No protein_examples, UniProtKB protein xrefs or GENE_OR_PROTEIN
    graph nodes are declared. Zero typed protein nodes means this success does not
    independently verify narrative clathrin/adaptor identity, localization, pathway
    mechanism or formation necessity.
  accessed_at: '2026-11-03T10:50:12.394110Z'
  support: supports
  snapshot_sha256: e800bc7ad0820a4b65b675c1652dd8cd1163fe63c1f022e8170852cb483a14e7
- evidence_id: septin-context-clathrin_coat_of_endocytic_vesicle
  kind: record_content
  reference: data/structures/other/clathrin_coat_of_endocytic_vesicle.yaml
  locator: Frozen identity, definition, parent/part and component fields only
  summary: 'Boundary context only: the generic class/lumen/material differs from the
    endocytic-specific target, while the coat neighbor carries lower-level proteins.
    No independent verification of neighbor protein accessions or whole-neighbor finding
    disposition is asserted.'
  accessed_at: '2026-11-03T10:54:55.867151Z'
  support: supports
  snapshot_sha256: 04cd29ffe90456d0dc2acbe6dbba20bd061587015653a0bea6d7259c1c7f6220
- evidence_id: septin-context-clathrin_coated_vesicle
  kind: record_content
  reference: data/structures/membrane_organelle/clathrin_coated_vesicle.yaml
  locator: Frozen identity, definition, parent/part and component fields only
  summary: 'Boundary context only: the generic class/lumen/material differs from the
    endocytic-specific target, while the coat neighbor carries lower-level proteins.
    No independent verification of neighbor protein accessions or whole-neighbor finding
    disposition is asserted.'
  accessed_at: '2026-11-03T10:54:55.867151Z'
  support: supports
  snapshot_sha256: cee241afc73475bcdec9d8c3c4c57bdf9c4cb2f726e4a78615dfb393613be9ad
- evidence_id: septin-context-clathrin_coated_vesicle_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/clathrin_coated_vesicle_lumen.yaml
  locator: Frozen identity, definition, parent/part and component fields only
  summary: 'Boundary context only: the generic class/lumen/material differs from the
    endocytic-specific target, while the coat neighbor carries lower-level proteins.
    No independent verification of neighbor protein accessions or whole-neighbor finding
    disposition is asserted.'
  accessed_at: '2026-11-03T10:54:55.867151Z'
  support: supports
  snapshot_sha256: 2137a192f721232651c140497813cea3f15a73a67e910194d59fadc7837308f9
- evidence_id: septin-context-clathrin_coated_vesicle_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/clathrin_coated_vesicle_membrane.yaml
  locator: Frozen identity, definition, parent/part and component fields only
  summary: 'Boundary context only: the generic class/lumen/material differs from the
    endocytic-specific target, while the coat neighbor carries lower-level proteins.
    No independent verification of neighbor protein accessions or whole-neighbor finding
    disposition is asserted.'
  accessed_at: '2026-11-03T10:54:55.867151Z'
  support: supports
  snapshot_sha256: 963e3cbe094c98b1279923d8f4ecc6a27343f82aa7240dece427fa09882c25f1
- evidence_id: septin-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0045334,GO:0106176,GO:0030669,GO:0030136,GO:0030139,GO:0030128,GO:0072583,GO:0071682,GO:0030665,GO:0030666
  locator: 'All ten exact returned terms: identifiers, active status, namespace, definitions
    and relevant typed children'
  summary: GO identifies whole endocytic vesicle GO0045334, membrane GO0030669, lumen
    GO0106176 and coat GO0030128 separately. The whole is both clathrin-coated and
    endocytic; membrane has both membrane subtype parents; lumen has endocytic-lumen
    parent and whole-vesicle parthood. Exact process GO0072583 describes clathrin-coated
    pit internalization. No cargo identity or universal clathrin necessity follows.
  accessed_at: '2026-11-03T10:50:28.060380Z'
  support: supports
  snapshot_sha256: 3e0c3bb0d57477942c2058c1ea14c0ed8c37a64856901ab4ee6c6e204c4bbded
- evidence_id: septin-ancestors-0045334
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0045334/ancestors?relations=is_a,part_of
  locator: Complete exact term ancestors response restricted to is_a and part_of
  summary: Requested typed ancestor closure corroborates containment/type hierarchy;
    it is not itself an experimental mechanism or a formal bounding-layer axiom.
  accessed_at: '2026-11-03T10:50:28.701734Z'
  support: supports
  snapshot_sha256: c2b44cb32ee44ba142ca8f592e9d7a0d0c9d240b3ff9c46c1fd43887b8a18cfe
- evidence_id: septin-ancestors-0106176
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0106176/ancestors?relations=is_a,part_of
  locator: Complete exact term ancestors response restricted to is_a and part_of
  summary: Requested typed ancestor closure corroborates containment/type hierarchy;
    it is not itself an experimental mechanism or a formal bounding-layer axiom.
  accessed_at: '2026-11-03T10:50:28.701961Z'
  support: supports
  snapshot_sha256: 9f9c38be0f0063b0fcb44e1d56c69d34098b189d645830e1985a262a8533452d
- evidence_id: septin-ancestors-0030669
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030669/ancestors?relations=is_a,part_of
  locator: Complete exact term ancestors response restricted to is_a and part_of
  summary: Requested typed ancestor closure corroborates containment/type hierarchy;
    it is not itself an experimental mechanism or a formal bounding-layer axiom.
  accessed_at: '2026-11-03T10:50:28.733080Z'
  support: supports
  snapshot_sha256: 54ff2635dbf02e51579fe91f6e986b70aad68d119d015d86d0edf91e789db488
- evidence_id: septin-go-edit
  kind: authority
  reference: https://raw.githubusercontent.com/geneontology/go-ontology/master/src/ontology/go-edit.obo
  locator: Only exact stanzas GO0030669, GO0045334, GO0106176 and GO0030128 from official
    source ontology; extracted stanzas at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/adversary-septin/go-edit-target-terms.json
  summary: The official GO0030669 stanza explicitly has intersection_of membrane and
    bounding_layer_of GO0045334, plus part_of GO0045334 and both membrane is-a parents.
    GO0030128 is part_of GO0030669. The lumen stanza has GO0071682 parent and part_of
    GO0045334. Thus maintained bounds/parthood notes have formal ontology support;
    no ontology-wide scientific audit is claimed.
  accessed_at: '2026-11-03T10:52:48.490869Z'
  support: supports
  snapshot_sha256: 2df17c2f3cef6fe48af3365822becc4df3728fc4f571151c6ed7a2d9344fdb84
- evidence_id: septin-SL-0319
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0319.json
  locator: Native id/name/definition, top-level fields, isA/partOf hierarchy; no protein-list
    interpretation
  summary: SL0319 identifies the generic clathrin-coated vesicle lumen and partOf
    generic clathrin-coated vesicle. It has no top-level geneOntologies mapping; nested
    parent mappings do not make it identical to endocytic-specific GO0106176. The
    maintained local generic-lumen parent remains broader.
  accessed_at: '2026-11-03T10:50:28.060800Z'
  support: supports
  snapshot_sha256: 60adcc470cf8170aeb6ca0842437084ca80cb1a3e5fbd7c87e7a4b3a735d0e4e
- evidence_id: septin-tax4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete ENA taxId, scientificName, rank, lineage and aliases
  summary: NCBITaxon4932 is species Saccharomyces cerevisiae. Taxonomy verifies identity,
    not strain-specific prevalence or a measured COMMON frequency.
  accessed_at: '2026-11-03T10:50:28.060716Z'
  support: supports
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
- evidence_id: septin-newpher-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.devcel.2005.04.014&pageSize=25
  locator: 'Europe PMC exact DOI result: complete abstract and title/authors/DOI/PMID/journal/year'
  summary: Newpher, Smith, Lemmon and Lemmon2005, PMID15992543, describes cortical
    clathrin, Abp1/cargo association and adaptor-dependent recruitment in yeast. This
    is the complete primary abstract and exact bibliography, not independent verification
    of all figures or released-vesicle ultrastructure.
  accessed_at: '2026-11-03T10:50:28.060854Z'
  support: supports
  snapshot_sha256: c99ec084fa3f65e3b5107699c30f42b09489dbc49d6be518d71ff9352d5a199c
  search_scope: Europe PMC REST search, exact DOI:10.1016/j.devcel.2005.04.014, format=json,
    resultType=core, pageSize=25, first response page only, no date filter. Exact
    matched article inspected at 2026-11-03T10:50:28.060854Z. No general literature-absence
    inference.
- evidence_id: septin-kaksonen-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.cell.2005.09.024&pageSize=25
  locator: 'Europe PMC exact DOI result: complete abstract and title/authors/DOI/PMID/journal/year'
  summary: Kaksonen, Toret and Drubin2005, PMID16239147, complete primary abstract
    describes deletion-mutant/live-imaging evidence for coat, invagination, actin
    and scission modules. It explicitly finds clathrin facilitates initiation but
    is not necessary for membrane invagination or vesicle formation in that yeast
    system. This is abstract-only experimental scope, not a Methods/Results body read.
  accessed_at: '2026-11-03T10:50:28.652552Z'
  support: supports
  snapshot_sha256: ac348282501025b934892bf941d37eb61a9a74e715270f13d12771a551cd95c0
  search_scope: Europe PMC REST search, exact DOI:10.1016/j.cell.2005.09.024, format=json,
    resultType=core, pageSize=25, first response page only, no date filter. Exact
    matched article inspected at 2026-11-03T10:50:28.652552Z. No general literature-absence
    inference.
- evidence_id: septin-newpher-duke
  kind: primary_source
  reference: https://dukespace.lib.duke.edu/server/api/core/bitstreams/e3c70c30-e4a1-4ba0-8ea6-c50af4ba491e/content
  locator: 'Fresh readable publisher-format PDF in Duke repository: printed pp87–96
    Summary/Introduction, Table1, selected Results Localization of Clathrin In Vivo,
    cargo/cortical association, Transient Association and Cortical Recruitment; Discussion
    and Experimental Procedures/Microscopy text. Captions are text only.'
  summary: Actual primary body supports dynamic cortical clathrin/adaptor recruitment
    in S. cerevisiae, with wt reporter strains and mutant/LAT-A conditions distinguished.
    Table1 names laboratory strains; cells generally grown30C, live microscopy uses
    mid-log synthetic cultures. Cortical events are distinct from internal TGN/endosomal
    clathrin. Discussion p95 explicitly cannot distinguish clathrin disassembly before
    budding from a clathrin-bearing vesicle or bud leaving the TIRF field. This source
    supports model-site dynamics, not resolved sealed lumen, universal retained coat
    or direct proof every budding event forms a coated carrier. No full image/movie/raw-data
    audit is claimed.
  accessed_at: '2026-11-03T10:50:28.060899Z'
  support: supports
  snapshot_sha256: c848e911372b9afb9902e4a74e3cb3dd66ef90eb5e102024cc95fff648bb6c21
- evidence_id: septin-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: 'Complete official /api/datasets response: every organism id/name and its
    dataset keys'
  summary: No organism/dataset matches Saccharomyces cerevisiae in this complete current
    response. Named clathrin/adaptor and endocytosis context merits applicability
    assessment, but uncovered organism scope makes downstream gene/module lookup not
    applicable. No unrelated species is substituted, and noncoverage is not negative
    biological evidence.
  accessed_at: '2026-11-03T10:50:28.666781Z'
  support: supports
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: Official iModulonDB GET /api/datasets at 2026-11-03T10:50:28.666781Z;
    inspected the complete returned organism list and all dataset keys for Saccharomyces,
    S. cerevisiae and budding yeast. No date filter or unrelated-taxonomy downstream
    search. This is coverage assessment, not transcriptomic support for mechanism.
- evidence_id: septin-historical-adapter-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Actual canary command00:49:00.848907Z–00:49:00.863225Z
  summary: Historical datasets invocation exited1 with OS PermissionError reading
    runner pyvenv.cfg. This retained receipt is not a fresh attempt or a successful
    adapter run. Current official catalogue fallback was fetched separately.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: supports
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: septin-access-source-receipts
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/adversary-septin/source-receipts.json
  locator: Actual request timestamps, outcomes and saved successful-body hashes
  summary: Fresh authority/primary/catalogue requests succeeded except Kaksonen publisher
    PDF HTTP403. Newpher is a genuine PDF; no challenge page is treated as article
    body.
  accessed_at: '2026-11-03T10:54:55.867151Z'
  support: supports
  snapshot_sha256: c80e3c468861867e582f5bc1f9b7f1b606caffb7ada3d82969dfde8462236a9b
- evidence_id: septin-access-extra-receipts
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/adversary-septin/extra-receipts.json
  locator: Actual request timestamps, outcomes and saved successful-body hashes
  summary: Kaksonen CORE public mirror returned403; attempted detailed OLS term URL
    returned404. Neither supplied source body or contrary scientific evidence. Exact
    ontology axioms were subsequently checked at the official GO source.
  accessed_at: '2026-11-03T10:54:55.867151Z'
  support: supports
  snapshot_sha256: 1549bee69434090c1a64e8e175ac6539579440c526c7da0aa4128d268bd1ee69
- evidence_id: septin-bounded-source-search
  kind: search
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/adversary-septin/browser-search.json
  locator: Only first returned result set for two exact queries; source discovery
    only
  summary: Exact publication/ontology search results were used as retrieval leads.
    Native source responses, complete abstracts and inspected Newpher PDF provide
    scientific support. Third-party summaries, unrelated records and search-result
    absence are not used to establish claims.
  accessed_at: '2026-11-03T10:52:01Z'
  support: supports
  snapshot_sha256: b2b26fbc941f0a4134c7d276a5f888deb61d287a4b59485823bbb257b5ae0a80
  search_scope: Web search at 2026-11-03T10:52:01Z; queries ["\"GO:0030669\" \"bounding\"",
    "\"A modular design for the clathrin\" pdf Kaksonen Toret Drubin"]; first returned
    result set, response_length=long, no date/recency filter or pagination. Only exact
    official ontology and legitimate cited-primary routes pursued; no exhaustive absence
    claim.
- evidence_id: check-qc
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/qc.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T10:55:38.279358Z'
  support: supports
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  snapshot_sha256: 02e1497526fae93b0b3ef5e0a8cfe560dba4030be638fcc1843eb40ac92a9e97
- evidence_id: check-labels
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/labels.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T10:50:38.551401Z'
  support: supports
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  snapshot_sha256: 6cdfb05df9a27194f05a5fd7f851783f817ac1523ca0bbfa54fe0e0d18775905
- evidence_id: check-trait-links
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/trait-links.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T10:50:16.038567Z'
  support: supports
  summary: Native TraitMech link check passed.
  snapshot_sha256: 8b336cdefbbd3daf6da8787990efdbe346c95e2c8361d50b7eb68a18f2d5a44a
- evidence_id: check-vendored
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/vendored.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T10:50:14.263646Z'
  support: supports
  summary: Pinned governed files match; native vendored check passed.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: check-curies
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/curies.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T10:51:33.005809Z'
  support: supports
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  snapshot_sha256: 19f996dd7df0222a54a590355c715c7d2b8ebf9dec91b91a6717d1caa56d3152
- evidence_id: focused
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/focused-results.json
  locator: All twenty actual target schema/strict command outputs
  accessed_at: '2026-11-03T10:56:12Z'
  support: supports
  summary: Ten schema and ten strict commands returned exit zero.
  snapshot_sha256: b02fe9c30cac3a25a59a2988f39cfd9e056781e74c1a9dbb05439134c3b02ec1
- evidence_id: supplemental-pmid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2360/pmid-chunks-receipt.json
  locator: Complete native-report PMID set checked with unchanged resolver in batches
    of at most fifty
  accessed_at: '2026-11-03T10:52:11.691142Z'
  support: supports
  summary: 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers
    remain unverified.
  snapshot_sha256: 6b2d4cf02bfbe02b4b1cd93fcdfa62d0fdc1409103c2f20362827e9af628c23f
- evidence_id: historical-adapter-runner-availability
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner invocation receipt, cross-checked against exact stdout/stderr
    hashes; reread during PR2360 synthesis
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS
    PermissionError reading the configured runner pyvenv.cfg. This is a retained historical
    availability observation, not a fresh attempt or a scientific validation failure.
    Native policy permits inspected source-catalogue fallback.
assessments:
- assessment_id: plaque-t4-native
  area: schema
  topic: Native protein inventories and exact graph xrefs
  outcome: supported
  summary: Both commands pass with no explicit protein examples or typed protein nodes.
    This validates represented empty inventories, not narrative molecular claims or
    mechanistic necessity.
  target_ids:
  - GO:0030136
  evidence_ids:
  - plaque-current-4
  - plaque-native-clathrin_coated_vesicle-verify
  - plaque-native-clathrin_coated_vesicle-causal
- assessment_id: plaque-t4-original-provenance
  area: provenance
  topic: Immutable original review and current target hashes
  outcome: supported
  summary: Original validate/render and all historical input hashes pass; current
    target is byte-identical to the frozen record. No scientific finding exists to
    terminally resolve. Historical record issue numbers remain context only.
  target_ids:
  - GO:0030136
  evidence_ids:
  - plaque-current-4
  - plaque-original-4
  - plaque-original-checks
- assessment_id: plaque-t4-coverage
  area: completeness
  topic: Complete target with bounded source review
  outcome: supported
  summary: All maintained fields were read and claim-bearing evidence assessed at
    declared tiers. Optional inventories, additional figures, detailed quantitative
    properties and causal mechanisms are not required. No concrete record-curation
    defect was established; bundle applicability corrections are separate.
  target_ids:
  - GO:0030136
  evidence_ids:
  - plaque-current-4
  - plaque-policy
  - plaque-rubric
- assessment_id: plaque-t5-native
  area: schema
  topic: Native protein inventories and exact graph xrefs
  outcome: supported
  summary: Both commands pass with no explicit protein examples or typed protein nodes.
    This validates represented empty inventories, not narrative molecular claims or
    mechanistic necessity.
  target_ids:
  - cellstructuremech:clathrin_coated_vesicle_lumen
  evidence_ids:
  - plaque-current-5
  - plaque-native-clathrin_coated_vesicle_lumen-verify
  - plaque-native-clathrin_coated_vesicle_lumen-causal
- assessment_id: plaque-t5-original-provenance
  area: provenance
  topic: Immutable original review and current target hashes
  outcome: supported
  summary: Original validate/render and all historical input hashes pass; current
    target is byte-identical to the frozen record. No scientific finding exists to
    terminally resolve. Historical record issue numbers remain context only.
  target_ids:
  - cellstructuremech:clathrin_coated_vesicle_lumen
  evidence_ids:
  - plaque-current-5
  - plaque-original-5
  - plaque-original-checks
- assessment_id: plaque-t5-coverage
  area: completeness
  topic: Complete target with bounded source review
  outcome: supported
  summary: All maintained fields were read and claim-bearing evidence assessed at
    declared tiers. Optional inventories, additional figures, detailed quantitative
    properties and causal mechanisms are not required. No concrete record-curation
    defect was established; bundle applicability corrections are separate.
  target_ids:
  - cellstructuremech:clathrin_coated_vesicle_lumen
  evidence_ids:
  - plaque-current-5
  - plaque-policy
  - plaque-rubric
- assessment_id: plaque-t6-native
  area: schema
  topic: Native protein inventories and exact graph xrefs
  outcome: supported
  summary: Both commands pass with no explicit protein examples or typed protein nodes.
    This validates represented empty inventories, not narrative molecular claims or
    mechanistic necessity.
  target_ids:
  - GO:0030665
  evidence_ids:
  - plaque-current-6
  - plaque-native-clathrin_coated_vesicle_membrane-verify
  - plaque-native-clathrin_coated_vesicle_membrane-causal
- assessment_id: plaque-t6-original-provenance
  area: provenance
  topic: Immutable original review and current target hashes
  outcome: supported
  summary: Original validate/render and all historical input hashes pass; current
    target is byte-identical to the frozen record. No scientific finding exists to
    terminally resolve. Historical record issue numbers remain context only.
  target_ids:
  - GO:0030665
  evidence_ids:
  - plaque-current-6
  - plaque-original-6
  - plaque-original-checks
- assessment_id: plaque-t6-coverage
  area: completeness
  topic: Complete target with bounded source review
  outcome: supported
  summary: All maintained fields were read and claim-bearing evidence assessed at
    declared tiers. Optional inventories, additional figures, detailed quantitative
    properties and causal mechanisms are not required. No concrete record-curation
    defect was established; bundle applicability corrections are separate.
  target_ids:
  - GO:0030665
  evidence_ids:
  - plaque-current-6
  - plaque-policy
  - plaque-rubric
- assessment_id: plaque-t9-native
  area: schema
  topic: Native protein inventories and exact graph xrefs
  outcome: supported
  summary: Both commands pass with no explicit protein examples or typed protein nodes.
    This validates represented empty inventories, not narrative molecular claims or
    mechanistic necessity.
  target_ids:
  - cellstructuremech:coccolith_vesicle
  evidence_ids:
  - plaque-current-9
  - plaque-native-coccolith_vesicle-verify
  - plaque-native-coccolith_vesicle-causal
- assessment_id: plaque-t9-original-provenance
  area: provenance
  topic: Immutable original review and current target hashes
  outcome: supported
  summary: Original validate/render and all historical input hashes pass; current
    target is byte-identical to the frozen record. No scientific finding exists to
    terminally resolve. Historical record issue numbers remain context only.
  target_ids:
  - cellstructuremech:coccolith_vesicle
  evidence_ids:
  - plaque-current-9
  - plaque-original-9
  - plaque-original-checks
- assessment_id: plaque-t9-coverage
  area: completeness
  topic: Complete target with bounded source review
  outcome: supported
  summary: All maintained fields were read and claim-bearing evidence assessed at
    declared tiers. Optional inventories, additional figures, detailed quantitative
    properties and causal mechanisms are not required. No concrete record-curation
    defect was established; bundle applicability corrections are separate.
  target_ids:
  - cellstructuremech:coccolith_vesicle
  evidence_ids:
  - plaque-current-9
  - plaque-policy
  - plaque-rubric
- assessment_id: plaque-t4-identity
  area: identity
  topic: Whole vesicle, lumen and membrane remain distinct
  outcome: supported
  summary: GO0030136 and SL0070 denote the whole coated vesicle, not its coat or bilayer.
    Coated-vesicle is_a parent and membrane/coat parthood are supported. The exact
    CCV synonym is verified.
  target_ids:
  - GO:0030136
  evidence_ids:
  - plaque-current-4
  - plaque-clathrin-agent-go
  - plaque-clathrin-agent-SL-0070
- assessment_id: plaque-t4-scope
  area: scope
  topic: Yeast occurrence and recruitment context
  outcome: supported
  summary: Current taxonomy verifies S.cerevisiae4932. Fresh Newpher primary body
    supports heavy/light-chain and adaptor dynamics at cortical yeast endocytic sites
    under the actual fluorescent-reporter/mutant conditions. COMMON is qualitative
    context, not a census or universal state assertion. Lumen/bilayer existence combines
    exact compartment definitions with the established yeast vesicle context; the
    study does not directly image a sealed lumen.
  target_ids:
  - GO:0030136
  evidence_ids:
  - plaque-current-4
  - plaque-clathrin-agent-go
  - plaque-clathrin-agent-SL-0070
  - plaque-clathrin-agent-tax4932
  - plaque-clathrin-agent-newpher2005-duke
  - plaque-clathrin-agent-doi-10.1016_j.devcel.2005.04.014
- assessment_id: plaque-t4-necessity
  area: evidence
  topic: Constitution, recruitment and formation necessity
  outcome: unknown
  summary: No individual protein or lipid species is asserted essential to forming
    these target structures. The membrane record uses ESSENTIAL for its defining collective
    bilayer, not a measured dependency on a particular molecule. Newpher recruitment/turnover
    and Kaksonen deletion effects must not be upgraded to universal vesicle-assembly
    necessity.
  target_ids:
  - GO:0030136
  evidence_ids:
  - plaque-current-4
  - plaque-clathrin-agent-go
  - plaque-clathrin-agent-SL-0070
  - plaque-clathrin-agent-newpher2005-duke
  - plaque-clathrin-agent-kaksonen2005-meta
- assessment_id: plaque-t4-adapter
  area: scope
  topic: Actual named-molecule applicability
  outcome: supported
  summary: All three records explicitly name heavy/light chains and adaptor recruitment
    in their yeast taxon/example narratives, including the sparse lumen target. Lack
    of expression claims alone was therefore an unsupported original N/A rationale.
    The fresh complete catalogue has no S.cerevisiae dataset; no unrelated-organism
    gene/module query applies and no biological absence follows. Historical runner
    failure remains separately dated.
  target_ids:
  - GO:0030136
  evidence_ids:
  - plaque-current-4
  - plaque-original-4
  - plaque-policy
  - plaque-catalogue
  - plaque-historical-runner
- assessment_id: plaque-t4-source-tiers
  area: provenance
  topic: Primary body versus abstract and access failures
  outcome: supported
  summary: Newpher genuine primary PDF pp87–96 was inspected including Methods and
    its explicit pre-budding uncoating versus coated-vesicle departure uncertainty.
    Kaksonen is used at complete-primary-abstract tier only; native challenge/metadata
    responses are not bodies. No clathrin source figure pixels, movies or raw data
    were analyzed.
  target_ids:
  - GO:0030136
  evidence_ids:
  - plaque-current-4
  - plaque-clathrin-agent-newpher2005-duke
  - plaque-clathrin-agent-kaksonen2005-meta
  - plaque-clathrin-agent-kaksonen2005-api
- assessment_id: plaque-t5-identity
  area: identity
  topic: Whole vesicle, lumen and membrane remain distinct
  outcome: supported
  summary: The local identity follows exact SL0319 lumen definition and synonym. Cytoplasmic-vesicle-lumen
    is the broader parent and whole clathrin vesicle the partOf host. Bounded GO search
    returns narrower endocytic and transmitter-specific lumina, which cannot replace
    this broader identity.
  target_ids:
  - cellstructuremech:clathrin_coated_vesicle_lumen
  evidence_ids:
  - plaque-current-5
  - plaque-clathrin-agent-go
  - plaque-clathrin-agent-SL-0319
  - plaque-clathrin-lumen-go-search
- assessment_id: plaque-t5-scope
  area: scope
  topic: Yeast occurrence and recruitment context
  outcome: supported
  summary: Current taxonomy verifies S.cerevisiae4932. Fresh Newpher primary body
    supports heavy/light-chain and adaptor dynamics at cortical yeast endocytic sites
    under the actual fluorescent-reporter/mutant conditions. COMMON is qualitative
    context, not a census or universal state assertion. Lumen/bilayer existence combines
    exact compartment definitions with the established yeast vesicle context; the
    study does not directly image a sealed lumen.
  target_ids:
  - cellstructuremech:clathrin_coated_vesicle_lumen
  evidence_ids:
  - plaque-current-5
  - plaque-clathrin-agent-go
  - plaque-clathrin-agent-SL-0319
  - plaque-clathrin-agent-tax4932
  - plaque-clathrin-agent-newpher2005-duke
  - plaque-clathrin-agent-doi-10.1016_j.devcel.2005.04.014
- assessment_id: plaque-t5-necessity
  area: evidence
  topic: Constitution, recruitment and formation necessity
  outcome: unknown
  summary: No individual protein or lipid species is asserted essential to forming
    these target structures. The membrane record uses ESSENTIAL for its defining collective
    bilayer, not a measured dependency on a particular molecule. Newpher recruitment/turnover
    and Kaksonen deletion effects must not be upgraded to universal vesicle-assembly
    necessity.
  target_ids:
  - cellstructuremech:clathrin_coated_vesicle_lumen
  evidence_ids:
  - plaque-current-5
  - plaque-clathrin-agent-go
  - plaque-clathrin-agent-SL-0319
  - plaque-clathrin-agent-newpher2005-duke
  - plaque-clathrin-agent-kaksonen2005-meta
- assessment_id: plaque-t5-adapter
  area: scope
  topic: Actual named-molecule applicability
  outcome: supported
  summary: All three records explicitly name heavy/light chains and adaptor recruitment
    in their yeast taxon/example narratives, including the sparse lumen target. Lack
    of expression claims alone was therefore an unsupported original N/A rationale.
    The fresh complete catalogue has no S.cerevisiae dataset; no unrelated-organism
    gene/module query applies and no biological absence follows. Historical runner
    failure remains separately dated.
  target_ids:
  - cellstructuremech:clathrin_coated_vesicle_lumen
  evidence_ids:
  - plaque-current-5
  - plaque-original-5
  - plaque-policy
  - plaque-catalogue
  - plaque-historical-runner
- assessment_id: plaque-t5-source-tiers
  area: provenance
  topic: Primary body versus abstract and access failures
  outcome: supported
  summary: Newpher genuine primary PDF pp87–96 was inspected including Methods and
    its explicit pre-budding uncoating versus coated-vesicle departure uncertainty.
    Kaksonen is used at complete-primary-abstract tier only; native challenge/metadata
    responses are not bodies. No clathrin source figure pixels, movies or raw data
    were analyzed.
  target_ids:
  - cellstructuremech:clathrin_coated_vesicle_lumen
  evidence_ids:
  - plaque-current-5
  - plaque-clathrin-agent-newpher2005-duke
  - plaque-clathrin-agent-kaksonen2005-meta
  - plaque-clathrin-agent-kaksonen2005-api
- assessment_id: plaque-t6-identity
  area: identity
  topic: Whole vesicle, lumen and membrane remain distinct
  outcome: supported
  summary: Exact GO0030665/SL0071 identify the lipid-bilayer membrane; coated-vesicle/cytoplasmic-vesicle
    membrane parents are is_a and the whole vesicle is the parthood host. Synonym
    and active source identity agree.
  target_ids:
  - GO:0030665
  evidence_ids:
  - plaque-current-6
  - plaque-clathrin-agent-go
  - plaque-clathrin-agent-SL-0071
- assessment_id: plaque-t6-scope
  area: scope
  topic: Yeast occurrence and recruitment context
  outcome: supported
  summary: Current taxonomy verifies S.cerevisiae4932. Fresh Newpher primary body
    supports heavy/light-chain and adaptor dynamics at cortical yeast endocytic sites
    under the actual fluorescent-reporter/mutant conditions. COMMON is qualitative
    context, not a census or universal state assertion. Lumen/bilayer existence combines
    exact compartment definitions with the established yeast vesicle context; the
    study does not directly image a sealed lumen.
  target_ids:
  - GO:0030665
  evidence_ids:
  - plaque-current-6
  - plaque-clathrin-agent-go
  - plaque-clathrin-agent-SL-0071
  - plaque-clathrin-agent-tax4932
  - plaque-clathrin-agent-newpher2005-duke
  - plaque-clathrin-agent-doi-10.1016_j.devcel.2005.04.014
- assessment_id: plaque-t6-necessity
  area: evidence
  topic: Constitution, recruitment and formation necessity
  outcome: unknown
  summary: No individual protein or lipid species is asserted essential to forming
    these target structures. The membrane record uses ESSENTIAL for its defining collective
    bilayer, not a measured dependency on a particular molecule. Newpher recruitment/turnover
    and Kaksonen deletion effects must not be upgraded to universal vesicle-assembly
    necessity.
  target_ids:
  - GO:0030665
  evidence_ids:
  - plaque-current-6
  - plaque-clathrin-agent-go
  - plaque-clathrin-agent-SL-0071
  - plaque-clathrin-agent-newpher2005-duke
  - plaque-clathrin-agent-kaksonen2005-meta
- assessment_id: plaque-t6-adapter
  area: scope
  topic: Actual named-molecule applicability
  outcome: supported
  summary: All three records explicitly name heavy/light chains and adaptor recruitment
    in their yeast taxon/example narratives, including the sparse lumen target. Lack
    of expression claims alone was therefore an unsupported original N/A rationale.
    The fresh complete catalogue has no S.cerevisiae dataset; no unrelated-organism
    gene/module query applies and no biological absence follows. Historical runner
    failure remains separately dated.
  target_ids:
  - GO:0030665
  evidence_ids:
  - plaque-current-6
  - plaque-original-6
  - plaque-policy
  - plaque-catalogue
  - plaque-historical-runner
- assessment_id: plaque-t6-source-tiers
  area: provenance
  topic: Primary body versus abstract and access failures
  outcome: supported
  summary: Newpher genuine primary PDF pp87–96 was inspected including Methods and
    its explicit pre-budding uncoating versus coated-vesicle departure uncertainty.
    Kaksonen is used at complete-primary-abstract tier only; native challenge/metadata
    responses are not bodies. No clathrin source figure pixels, movies or raw data
    were analyzed.
  target_ids:
  - GO:0030665
  evidence_ids:
  - plaque-current-6
  - plaque-clathrin-agent-newpher2005-duke
  - plaque-clathrin-agent-kaksonen2005-meta
  - plaque-clathrin-agent-kaksonen2005-api
- assessment_id: plaque-t4-composition
  area: grounding
  topic: Coat constituents owned by the coat record
  outcome: supported
  summary: The whole vesicle represents coat and membrane as structural parts. Frozen
    coat boundary/component-label context confirms separate heavy/light-chain entries;
    duplicating them as direct whole-vesicle components is unnecessary. No independent
    coat protein-accession reassessment is inferred.
  target_ids:
  - GO:0030136
  evidence_ids:
  - plaque-current-4
  - plaque-neighbor-coat
  - plaque-current-6
  - plaque-clathrin-agent-go
- assessment_id: plaque-t4-function
  area: evidence
  topic: Clathrin-dependent endocytic uptake
  outcome: supported
  summary: The broad uptake function and participates_in edge are supported by GO0072583
    and primary yeast endocytic studies. The function is not exclusive to all clathrin
    trafficking or a claim that clathrin is necessary for every vesicle. Kaksonen
    abstract explicitly distinguishes initiation effects from invagination/vesicle-formation
    necessity.
  target_ids:
  - GO:0030136
  evidence_ids:
  - plaque-current-4
  - plaque-clathrin-agent-go
  - plaque-clathrin-agent-kaksonen2005-meta
  - plaque-clathrin-agent-newpher2005-duke
- assessment_id: plaque-t4-graph
  area: graph
  topic: Descriptive coat/membrane parthood and uptake
  outcome: supported
  summary: 'All three edges are descriptive: coat partOf whole, membrane partOf whole
    and vesicle participation in uptake. NONMECHANISTIC scope appropriately excludes
    actin scission, adaptor dependency and unsupported cargo mechanism.'
  target_ids:
  - GO:0030136
  evidence_ids:
  - plaque-current-4
  - plaque-clathrin-agent-go
  - plaque-clathrin-agent-SL-0070
- assessment_id: plaque-t5-composition
  area: grounding
  topic: Lumen as enclosed region
  outcome: supported
  summary: The lumen has no compulsory protein or cargo inventory. It is spatially
    bounded, not equated with the bounding membrane or external coat. Molecular recruitment
    remains taxonomic context rather than a lumen constituent assertion.
  target_ids:
  - cellstructuremech:clathrin_coated_vesicle_lumen
  evidence_ids:
  - plaque-current-5
  - plaque-clathrin-agent-SL-0319
  - plaque-current-4
  - plaque-current-6
- assessment_id: plaque-t5-graph
  area: graph
  topic: Boundary and parthood without mechanism
  outcome: supported
  summary: Two NONMECHANISTIC edges represent lumen partOf whole and membrane bounds
    lumen, directly supported by SL0319 and exact whole/membrane identities. No scission,
    sorting or lumen-wide composition is asserted.
  target_ids:
  - cellstructuremech:clathrin_coated_vesicle_lumen
  evidence_ids:
  - plaque-current-5
  - plaque-clathrin-agent-SL-0319
  - plaque-clathrin-agent-go
- assessment_id: plaque-t6-composition
  area: grounding
  topic: Collective lipid material and coat distinction
  outcome: supported
  summary: The reviewed-label-only lipid bilayer is a collective material, not an
    exact single chemical species. The existing grounding TODO does not prove a missing
    exact chemical CURIE. Ontology coat association/parthood is distinct from claiming
    clathrin is itself lipid-bilayer material.
  target_ids:
  - GO:0030665
  evidence_ids:
  - plaque-current-6
  - plaque-neighbor-coat
  - plaque-clathrin-agent-go
  - plaque-clathrin-agent-SL-0071
- assessment_id: plaque-t6-graph
  area: graph
  topic: Membrane surrounds and is part of whole vesicle
  outcome: supported
  summary: The two NONMECHANISTIC edges describe membrane parthood and the source-defined
    surrounding boundary. GO/SL explicitly define this membrane as surrounding a clathrin-coated
    vesicle; the graph does not assert an origin, closure kinetics or individual budding
    machinery. The mutual lumen target separately models the bounded internal region.
  target_ids:
  - GO:0030665
  evidence_ids:
  - plaque-current-6
  - plaque-current-5
  - plaque-clathrin-agent-go
  - plaque-clathrin-agent-SL-0071
- assessment_id: plaque-t9-identity
  area: identity
  topic: Intracellular formation compartment versus mineral products
  outcome: supported
  summary: The source-defined local coccolith vesicle encloses developing mineral
    and is distinct from a coccolith scale, external coccosphere and separate Ca/P
    store. GO0043231 remains broader parent. Current bounded searches have zero coccolith/coccolithogenesis
    hits without recertifying historical exhaustive searches.
  target_ids:
  - cellstructuremech:coccolith_vesicle
  evidence_ids:
  - plaque-current-9
  - plaque-root23-sources-jats-PMC13067266
  - plaque-root23-sources-jats-PMC4834641
  - plaque-root23-sources-coccolith-go
  - plaque-root23-sources-coccolith-go-search
  - plaque-root23-sources-coccolithogenesis-go-search
  - plaque-neighbor-coccolith
  - plaque-neighbor-coccosphere
- assessment_id: plaque-t9-scope
  area: scope
  topic: Exact species and culture strains
  outcome: supported
  summary: Native taxonomy verifies C.leptoporus127549 and E.huxleyi2903, with Gephyrocapsa
    huxleyi a synonym. Primary culture methods explicitly identify RCC1130 and AWI1516.
    The maintained observations stay within their experimental species/strains and
    do not impose population prevalence or universal life-cycle occurrence.
  target_ids:
  - cellstructuremech:coccolith_vesicle
  evidence_ids:
  - plaque-current-9
  - plaque-root23-sources-jats-PMC13067266
  - plaque-root23-sources-jats-PMC4834641
  - plaque-root23-sources-NCBITaxon-127549
  - plaque-root23-sources-NCBITaxon-2903
  - plaque-root23-sources-coccolith2026-supplement
- assessment_id: plaque-t9-composition
  area: grounding
  topic: Observed bounding membrane with unresolved machinery
  outcome: supported
  summary: The OTHER component is a structural membrane grounded to GO0016020, with
    UNKNOWN assembly essentiality. Direct microscopy supports the boundary; neither
    observed densities, a716-particle average nor resemblance to ATPase establish
    an exact protein constituent or molecular formation requirement. Calcite/baseplate
    remain cargo, not demonstrated vesicle-building proteins.
  target_ids:
  - cellstructuremech:coccolith_vesicle
  evidence_ids:
  - plaque-current-9
  - plaque-root23-sources-jats-PMC13067266
  - plaque-root23-sources-jats-PMC4834641
  - plaque-root23-sources-coccolith-go
- assessment_id: plaque-t9-function
  area: evidence
  topic: Site of crystal formation with mechanistic limits
  outcome: supported
  summary: The primary studies support a membrane-confined environment for intracellular
    calcite growth. Source-informed caveats retain uncertain local growth inhibition,
    transport and membrane-shaping mechanisms. Separate storage apposition does not
    prove continuity/ion transfer. No mechanism graph is needed for this observational
    record.
  target_ids:
  - cellstructuremech:coccolith_vesicle
  evidence_ids:
  - plaque-current-9
  - plaque-root23-sources-jats-PMC13067266
  - plaque-root23-sources-jats-PMC4834641
- assessment_id: plaque-t9-image
  area: provenance
  topic: Native pixels, caption, microscopy and licence
  outcome: supported
  summary: The frozen700x418 image was viewed and exactly matches the fresh source
    bytes. PanelA is schematic, B is high-pressure-freeze/fracture cryo-SEM, C/D and
    E are cryo-FIB-SEM slices/reconstructions. Five stages are not one time-lapse.
    RCC1130, selective external decalcification before FIB, author attribution and
    exact CC-BY4.0 ALI URL agree with the record. No raw volumes or Figure3/4 pixels
    were reanalyzed.
  target_ids:
  - cellstructuremech:coccolith_vesicle
  evidence_ids:
  - plaque-current-9
  - plaque-root23-sources-jats-PMC13067266
  - plaque-root23-sources-jats-PMC4834641
  - plaque-image
  - plaque-root23-sources-coccolith-fig2
  - plaque-root23-sources-coccolith2026-supplement
  - plaque-root23-sources-coccolith2026-s3xml
- assessment_id: plaque-t9-adapter
  area: scope
  topic: Genuine morphology/material applicability exclusion
  outcome: not_applicable
  summary: This record asserts observed membrane morphology and mineralization-site
    function. ATPase identity, transport machinery and cytoskeletal constituents are
    explicitly withheld, not positive molecular/pathway assignments. No represented
    accession, regulator or gene supports a matched module query. The original N/A
    outcome is retained with this concrete scope rationale, not counted as a defect
    merely because its earlier sentence mentioned no expression inference. Fresh catalogue
    also has no coccolithophore host. No molecular inventory or downstream query is
    invented.
  target_ids:
  - cellstructuremech:coccolith_vesicle
  evidence_ids:
  - plaque-current-9
  - plaque-original-9
  - plaque-policy
  - plaque-catalogue
- assessment_id: micro-cis_golgi_network_membrane-a1
  area: identity
  topic: Exact membrane identity and boundary
  outcome: supported
  summary: Exact GO:0033106 defines the lipid bilayer around CGN compartments, with
    exact synonym. Broader Golgi membrane and parthood in CGN are appropriate boundary
    relations. Frozen neighbors distinguish whole CGN and Golgi from this membrane.
  target_ids:
  - GO:0033106
  evidence_ids:
  - micro-record-cis_golgi_network_membrane
  - micro-cis-go
  - micro-cis-go-parent
  - micro-neighbor-cis_golgi_network
  - micro-neighbor-golgi_apparatus
- assessment_id: micro-cis_golgi_network_membrane-a2
  area: scope
  topic: 'Inherited F1: current experimental taxon'
  outcome: concern
  summary: Retained Rossanese primary source uses PPY1/isogenic PPY12; actual ATCC
    reidentification and ENA LC815816 qualifiers identify PPY12 as K. phaffii460519.
    Current occurrence/example retain K. pastoris4922. Both valid taxon IDs do not
    make the experimentally assigned one correct. Preserve the exact membrane-specific
    major finding.
  target_ids:
  - GO:0033106
  evidence_ids:
  - micro-record-cis_golgi_network_membrane
  - micro-cis-jats-PMC2148216
  - micro-cis-atcc-204163
  - micro-cis-ena-LC815816
  - micro-cis-tax-4922
  - micro-cis-tax-460519
- assessment_id: micro-cis_golgi_network_membrane-a3
  area: evidence
  topic: 'Inherited F2: stack study versus CGN membrane'
  outcome: concern
  summary: Rossanese identifies coherent Golgi stacks and tER interface, not a distinct
    CGN membrane. CGN is not the Golgi stack in native GO. Cho Sed5 fraction concerns
    S. cerevisiae early-Golgi membranes and does not fill this particular species/compartment
    evidence gap. Species correction alone cannot repair the membrane-specific occurrence/example;
    absence of CGN is not inferred.
  target_ids:
  - GO:0033106
  evidence_ids:
  - micro-record-cis_golgi_network_membrane
  - micro-cis-go
  - micro-cis-jats-PMC2148216
  - micro-cis-cho2000-meta
- assessment_id: micro-cis_golgi_network_membrane-a4
  area: completeness
  topic: Collective lipid material and excluded molecular residents
  outcome: supported
  summary: Generic bilayer material is a valid reviewed-label-only constituent; no
    exact single lipid or universal protein inventory is asserted. Sed5/COPII are
    explicitly discussed as trafficking/localization context, not constitutive lipid
    material. Collective boundary constitution does not prove formation necessity
    of individual molecular species.
  target_ids:
  - GO:0033106
  evidence_ids:
  - micro-record-cis_golgi_network_membrane
  - micro-cis-go
  - micro-cis-cho2000-meta
  - micro-cis-jats-PMC2148216
  - micro-native-schema
- assessment_id: micro-cis_golgi_network_membrane-a5
  area: graph
  topic: Three NONMECHANISTIC topology edges
  outcome: supported
  summary: Membrane bounds CGN, CGN part of Golgi and CGN abuts ER are supported as
    generic authority topology. Here the component-linked node denotes the membrane
    explicitly defined as lipid bilayer; unlike the neighboring whole-network node,
    it does not identify the full compartment with a lipid constituent. Rossanese
    supplies broader adjacency context only.
  target_ids:
  - GO:0033106
  evidence_ids:
  - micro-record-cis_golgi_network_membrane
  - micro-cis-go
  - micro-cis-go-parent
  - micro-native-schema
  - micro-graph-contract
  - micro-neighbor-cis_golgi_network
- assessment_id: micro-cis_golgi_network_membrane-a6
  area: scope
  topic: Original applicability omission
  outcome: concern
  summary: The original omitted applicability despite its actual Sed5-positive compartment
    and COPII evidence assessment. Fresh catalogue contains no matching yeast organism/dataset;
    no downstream query is invented. This corrects review coverage without adding
    membrane constituents.
  target_ids:
  - GO:0033106
  evidence_ids:
  - micro-record-cis_golgi_network_membrane
  - micro-prior-cis_golgi_network_membrane
  - micro-review-policy
  - micro-review-config
  - micro-adapter-catalogue
  - micro-historical-adapter-runner
- assessment_id: micro-cis_golgi_network_membrane-a7
  area: schema
  topic: Unchanged inputs and native checks
  outcome: supported
  summary: Original pair validates/renders and target hash remains current. Six current
    slice protein receipts were inspected; this membrane has empty protein inventory/zero
    protein nodes, so no molecular completeness or occurrence is certified by their
    success.
  target_ids:
  - GO:0033106
  evidence_ids:
  - micro-record-cis_golgi_network_membrane
  - micro-original-validation-inputs
  - micro-native-cis_golgi_network_membrane-verify
  - micro-native-cis_golgi_network_membrane-causal
- assessment_id: micro-cis_golgi_network_membrane-a8
  area: provenance
  topic: Exact two-finding lineage and verdict
  outcome: concern
  summary: Maintain original20261021T111327Z-cis-golgi-network-membrane-audit/F1 and/F2
    as open confirmed major findings with exact separate membrane issue keys. Current
    needs_curation does not resolve or conflate prior whole-network issues or category
    findings.
  target_ids:
  - GO:0033106
  evidence_ids:
  - micro-record-cis_golgi_network_membrane
  - micro-prior-cis_golgi_network_membrane
  - micro-cis-jats-PMC2148216
  - micro-cis-atcc-204163
- assessment_id: micro-coated_vesicle-a1
  area: identity
  topic: Whole vesicle, membrane and subtype boundaries
  outcome: supported
  summary: Active exact GO definitions preserve the broad coated vesicle and its lipid-bilayer
    boundary. Clathrin/COPI/COPII are subtype examples rather than whole-class synonyms.
    Generic coat and subtype coat neighbors were read only for boundary/component-label
    context.
  target_ids:
  - GO:0030135
  evidence_ids:
  - micro-record-coated_vesicle
  - micro-coated-go
  - micro-coat-membrane-go
  - micro-neighbor-vesicle_coat
  - micro-neighbor-clathrin_vesicle_coat
  - micro-neighbor-copi_vesicle_coat
  - micro-neighbor-copii_vesicle_coat
- assessment_id: micro-coated_vesicle-a2
  area: scope
  topic: Species occurrence and experimental example
  outcome: supported
  summary: Barlowe complete primary abstract supports yeast ER-derived COPII budding.
    Fresh Matsuoka primary text directly compares native ER-microsome-derived and
    synthetic-liposome vesicles; RSY445 is explicit. Whole-vesicle native-ER and membrane
    synthetic-liposome exemplars are both source-supported. COMMON is qualitative
    model context, not quantified prevalence; S288C protein exemplars are not automatically
    the experimental strain.
  target_ids:
  - GO:0030135
  evidence_ids:
  - micro-record-coated_vesicle
  - micro-NCBITaxon-4932
  - micro-NCBITaxon-559292
  - micro-PMID-8004676
  - micro-PMID-9568718
  - micro-matsuoka1998-author
- assessment_id: micro-coated_vesicle-a3
  area: completeness
  topic: Constituents, necessary material and heterogeneous coats
  outcome: supported
  summary: Generic lipid bilayer is constitutional material, not proof that each chemical
    species is necessary. The parent coat class spans distinct clathrin/COPI/COPII
    complexes; subtype-specific inventories are intentionally kept separate. No single
    family should ground the heterogeneous parent cohort. Specific coat-protein essentiality
    is not inferred from bounded reconstitution.
  target_ids:
  - GO:0030135
  evidence_ids:
  - micro-record-coated_vesicle
  - micro-coated-go
  - micro-coat-membrane-go
  - micro-matsuoka1998-author
  - micro-native-schema
  - micro-neighbor-vesicle_coat
- assessment_id: micro-coated_vesicle-a4
  area: grounding
  topic: Inherited RET1 ambiguity with correct representative
  outcome: concern
  summary: Fresh reviewed exact RET1/taxon559292 query returns P22276 RNA-polymerase-III
    RET1 and P53622 coatomer alpha primary COP1/RET1 synonym. COP1 query returns only
    P53622. The record role already calls it representative, but the attached note
    still says single reviewed RET1 entry. Preserve minor F1, accession, taxon and
    representative identity; current search does not reconstruct historical results.
  target_ids:
  - GO:0030135
  evidence_ids:
  - micro-record-coated_vesicle
  - micro-UniProtKB-P53622
  - micro-UniProtKB-P22276
  - micro-query-RET1-559292
  - micro-query-COP1-559292
- assessment_id: micro-coated_vesicle-a5
  area: grounding
  topic: Six reviewed protein examples and family scope
  outcome: supported
  summary: Six accessions match the declared yeast symbols and S288C reviewed status;
    CHC1/CLC1/SEC13/SEC31/SEC26/COP1 queries each return the declared single entry
    currently. InterPro entries identify distinct constituent families and broad domains,
    not a universal coat family or proof every subtype has all six proteins.
  target_ids:
  - GO:0030135
  evidence_ids:
  - micro-record-coated_vesicle
  - micro-UniProtKB-P22137
  - micro-UniProtKB-P17891
  - micro-UniProtKB-Q04491
  - micro-UniProtKB-P38968
  - micro-UniProtKB-P41810
  - micro-UniProtKB-P53622
  - micro-query-CHC1-559292
  - micro-query-CLC1-559292
  - micro-query-SEC13-559292
  - micro-query-SEC31-559292
  - micro-query-SEC26-559292
  - micro-query-COP1-559292
  - micro-ipr-P22137
  - micro-ipr-P17891
  - micro-ipr-Q04491
  - micro-ipr-P38968
  - micro-ipr-P41810
  - micro-ipr-P53622
- assessment_id: micro-coated_vesicle-a6
  area: evidence
  topic: Experimental context and protein annotation scopes
  outcome: supported
  summary: Newpher supports yeast clathrin context but diffraction-limited puncta
    are not all proven mature vesicles. Yu supplies a mammalian-complex/human-and-yeast-Arf1
    recruitment model, not accession-specific yeast experiments. SEC13 nuclear-pore
    and SEC26 Golgi-membrane citations are accurately labeled annotation provenance,
    not relabeled direct vesicle-membership evidence.
  target_ids:
  - GO:0030135
  evidence_ids:
  - micro-record-coated_vesicle
  - micro-newpher2005-duke
  - micro-yu2012-s3
  - micro-UniProtKB-Q04491
  - micro-UniProtKB-P41810
  - micro-PMID-10684247
  - micro-PMID-14562095
- assessment_id: micro-coated_vesicle-a7
  area: graph
  topic: Five descriptive coat/membrane/budding/transport edges
  outcome: supported
  summary: Assemble-into, parthood, direction-neutral pinching off and vesicle-mediated
    transport are supported at explicit NONMECHANISTIC parent scope. No universal
    adaptor, donor membrane, budding direction or complete scission mechanism is asserted.
    Coat material and the surrounding bilayer remain distinct.
  target_ids:
  - GO:0030135
  evidence_ids:
  - micro-record-coated_vesicle
  - micro-coated-go
  - micro-coat-membrane-go
  - micro-graph-contract
  - micro-matsuoka1998-author
  - micro-yu2012-s3
- assessment_id: micro-coated_vesicle-a8
  area: scope
  topic: Correct unsupported expression-only applicability exclusion
  outcome: concern
  summary: Original N/A rationale rests only on no transcriptomic inference despite
    explicit Sar1/Sec coat machinery and COPII reconstitution (plus protein examples/transport
    pathway on the whole record). Current source-policy trigger applies; full catalogue
    lacks matching yeast datasets. No unrelated organism module search or biological
    absence claim is introduced.
  target_ids:
  - GO:0030135
  evidence_ids:
  - micro-record-coated_vesicle
  - micro-prior-coated_vesicle
  - micro-review-policy
  - micro-review-config
  - micro-adapter-catalogue
  - micro-historical-adapter-runner
- assessment_id: micro-coated_vesicle-a9
  area: schema
  topic: Frozen original and native identity/coverage checks
  outcome: supported
  summary: Original pair validates/renders and target remains byte-identical. Whole
    coated vesicle has six examples and one COVERED protein node; membrane has empty
    inventory and zero protein nodes. These documented successes do not certify scientific
    uniqueness wording, localization or formation necessity.
  target_ids:
  - GO:0030135
  evidence_ids:
  - micro-record-coated_vesicle
  - micro-original-validation-inputs
  - micro-native-coated_vesicle-verify
  - micro-native-coated_vesicle-causal
- assessment_id: micro-coated_vesicle-a10
  area: provenance
  topic: Current verdict and scoped lineage
  outcome: concern
  summary: Preserve exact original20261021T111333Z-coated-vesicle-audit/F1 and stable
    minor key; needs_curation is the query-note defect only.
  target_ids:
  - GO:0030135
  evidence_ids:
  - micro-record-coated_vesicle
  - micro-prior-coated_vesicle
  - micro-original-validation-inputs
  - micro-matsuoka1998-author
- assessment_id: micro-coated_vesicle_membrane-a1
  area: identity
  topic: Whole vesicle, membrane and subtype boundaries
  outcome: supported
  summary: Active exact GO definitions preserve the broad coated vesicle and its lipid-bilayer
    boundary. Clathrin/COPI/COPII are subtype examples rather than whole-class synonyms.
    Generic coat and subtype coat neighbors were read only for boundary/component-label
    context.
  target_ids:
  - GO:0030662
  evidence_ids:
  - micro-record-coated_vesicle_membrane
  - micro-coated-go
  - micro-coat-membrane-go
  - micro-neighbor-vesicle_coat
  - micro-neighbor-clathrin_vesicle_coat
  - micro-neighbor-copi_vesicle_coat
  - micro-neighbor-copii_vesicle_coat
- assessment_id: micro-coated_vesicle_membrane-a2
  area: scope
  topic: Species occurrence and experimental example
  outcome: supported
  summary: Barlowe complete primary abstract supports yeast ER-derived COPII budding.
    Fresh Matsuoka primary text directly compares native ER-microsome-derived and
    synthetic-liposome vesicles; RSY445 is explicit. Whole-vesicle native-ER and membrane
    synthetic-liposome exemplars are both source-supported. COMMON is qualitative
    model context, not quantified prevalence; S288C protein exemplars are not automatically
    the experimental strain.
  target_ids:
  - GO:0030662
  evidence_ids:
  - micro-record-coated_vesicle_membrane
  - micro-NCBITaxon-4932
  - micro-NCBITaxon-559292
  - micro-PMID-8004676
  - micro-PMID-9568718
  - micro-matsuoka1998-author
- assessment_id: micro-coated_vesicle_membrane-a3
  area: completeness
  topic: Constituents, necessary material and heterogeneous coats
  outcome: supported
  summary: Generic lipid bilayer is constitutional material, not proof that each chemical
    species is necessary. The parent coat class spans distinct clathrin/COPI/COPII
    complexes; subtype-specific inventories are intentionally kept separate. No single
    family should ground the heterogeneous parent cohort. Specific coat-protein essentiality
    is not inferred from bounded reconstitution.
  target_ids:
  - GO:0030662
  evidence_ids:
  - micro-record-coated_vesicle_membrane
  - micro-coated-go
  - micro-coat-membrane-go
  - micro-matsuoka1998-author
  - micro-native-schema
  - micro-neighbor-vesicle_coat
- assessment_id: micro-coated_vesicle_membrane-a4
  area: graph
  topic: Three membrane and coat topology relations
  outcome: supported
  summary: Membrane part_of vesicle, coat part_of membrane and membrane bounds vesicle
    are supported by exact current GO relations/definition. GO:0030662 explicitly
    lists vesicle coat as part_of; generic coat protein material need not be duplicated
    as molecular lipid-bilayer components. NONMECHANISTIC scope remains coherent.
  target_ids:
  - GO:0030662
  evidence_ids:
  - micro-record-coated_vesicle_membrane
  - micro-coat-membrane-go
  - micro-coated-go
  - micro-graph-contract
  - micro-native-schema
- assessment_id: micro-coated_vesicle_membrane-a5
  area: scope
  topic: Correct unsupported expression-only applicability exclusion
  outcome: concern
  summary: Original N/A rationale rests only on no transcriptomic inference despite
    explicit Sar1/Sec coat machinery and COPII reconstitution (plus protein examples/transport
    pathway on the whole record). Current source-policy trigger applies; full catalogue
    lacks matching yeast datasets. No unrelated organism module search or biological
    absence claim is introduced.
  target_ids:
  - GO:0030662
  evidence_ids:
  - micro-record-coated_vesicle_membrane
  - micro-prior-coated_vesicle_membrane
  - micro-review-policy
  - micro-review-config
  - micro-adapter-catalogue
  - micro-historical-adapter-runner
- assessment_id: micro-coated_vesicle_membrane-a6
  area: schema
  topic: Frozen original and native identity/coverage checks
  outcome: supported
  summary: Original pair validates/renders and target remains byte-identical. Whole
    coated vesicle has six examples and one COVERED protein node; membrane has empty
    inventory and zero protein nodes. These documented successes do not certify scientific
    uniqueness wording, localization or formation necessity.
  target_ids:
  - GO:0030662
  evidence_ids:
  - micro-record-coated_vesicle_membrane
  - micro-original-validation-inputs
  - micro-native-coated_vesicle_membrane-verify
  - micro-native-coated_vesicle_membrane-causal
- assessment_id: micro-coated_vesicle_membrane-a7
  area: provenance
  topic: Current verdict and scoped lineage
  outcome: supported
  summary: Original20261021T111334Z-coated-vesicle-membrane-audit had no scientific
    finding. Current pass_with_limitations retains positive source assessment, access
    limits and separate adapter bundle repair; no finding is invented to force persistence.
  target_ids:
  - GO:0030662
  evidence_ids:
  - micro-record-coated_vesicle_membrane
  - micro-prior-coated_vesicle_membrane
  - micro-original-validation-inputs
  - micro-matsuoka1998-author
- assessment_id: septin-clathrin_coated_endocytic_vesicle-schema
  area: schema
  topic: Native validation, deterministic rendering and frozen record integrity
  outcome: supported
  summary: The original bundle validates and renders exactly, and the full current
    record hash equals its original frozen input and historical source bytes. Both
    current native protein commands exit0 at empty inventory scope. Root owns whole-corpus
    and final integration gates.
  target_ids:
  - GO:0045334
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle
  - septin-original-validation-clathrin_coated_endocytic_vesicle
  - septin-native-clathrin_coated_endocytic_vesicle-verify
  - septin-native-clathrin_coated_endocytic_vesicle-causal
- assessment_id: septin-clathrin_coated_endocytic_vesicle-native-limits
  area: provenance
  topic: Empty molecular inventory and actual check times
  outcome: supported
  summary: All represented protein-example/xref and typed protein-node inventories
    are empty. Command success cannot independently establish the named clathrin/adaptor
    narrative, localization, mechanism or necessity. Current receipts and historical
    original checks remain explicitly separate.
  target_ids:
  - GO:0045334
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle
  - septin-original-clathrin_coated_endocytic_vesicle
  - septin-native-clathrin_coated_endocytic_vesicle-verify
  - septin-native-clathrin_coated_endocytic_vesicle-causal
- assessment_id: septin-clathrin_coated_endocytic_vesicle-images
  area: scope
  topic: No maintained images or numerical measurements
  outcome: not_applicable
  summary: No target image, measurement or verbatim source snippet is declared. Reading
    source captions and text is not image-pixel, supplementary movie or raw microscopy
    analysis.
  target_ids:
  - GO:0045334
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle
- assessment_id: septin-clathrin_coated_endocytic_vesicle_lumen-schema
  area: schema
  topic: Native validation, deterministic rendering and frozen record integrity
  outcome: supported
  summary: The original bundle validates and renders exactly, and the full current
    record hash equals its original frozen input and historical source bytes. Both
    current native protein commands exit0 at empty inventory scope. Root owns whole-corpus
    and final integration gates.
  target_ids:
  - GO:0106176
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle_lumen
  - septin-original-validation-clathrin_coated_endocytic_vesicle_lumen
  - septin-native-clathrin_coated_endocytic_vesicle_lumen-verify
  - septin-native-clathrin_coated_endocytic_vesicle_lumen-causal
- assessment_id: septin-clathrin_coated_endocytic_vesicle_lumen-native-limits
  area: provenance
  topic: Empty molecular inventory and actual check times
  outcome: supported
  summary: All represented protein-example/xref and typed protein-node inventories
    are empty. Command success cannot independently establish the named clathrin/adaptor
    narrative, localization, mechanism or necessity. Current receipts and historical
    original checks remain explicitly separate.
  target_ids:
  - GO:0106176
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle_lumen
  - septin-original-clathrin_coated_endocytic_vesicle_lumen
  - septin-native-clathrin_coated_endocytic_vesicle_lumen-verify
  - septin-native-clathrin_coated_endocytic_vesicle_lumen-causal
- assessment_id: septin-clathrin_coated_endocytic_vesicle_lumen-images
  area: scope
  topic: No maintained images or numerical measurements
  outcome: not_applicable
  summary: No target image, measurement or verbatim source snippet is declared. Reading
    source captions and text is not image-pixel, supplementary movie or raw microscopy
    analysis.
  target_ids:
  - GO:0106176
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle_lumen
- assessment_id: septin-clathrin_coated_endocytic_vesicle_membrane-schema
  area: schema
  topic: Native validation, deterministic rendering and frozen record integrity
  outcome: supported
  summary: The original bundle validates and renders exactly, and the full current
    record hash equals its original frozen input and historical source bytes. Both
    current native protein commands exit0 at empty inventory scope. Root owns whole-corpus
    and final integration gates.
  target_ids:
  - GO:0030669
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle_membrane
  - septin-original-validation-clathrin_coated_endocytic_vesicle_membrane
  - septin-native-clathrin_coated_endocytic_vesicle_membrane-verify
  - septin-native-clathrin_coated_endocytic_vesicle_membrane-causal
- assessment_id: septin-clathrin_coated_endocytic_vesicle_membrane-native-limits
  area: provenance
  topic: Empty molecular inventory and actual check times
  outcome: supported
  summary: All represented protein-example/xref and typed protein-node inventories
    are empty. Command success cannot independently establish the named clathrin/adaptor
    narrative, localization, mechanism or necessity. Current receipts and historical
    original checks remain explicitly separate.
  target_ids:
  - GO:0030669
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle_membrane
  - septin-original-clathrin_coated_endocytic_vesicle_membrane
  - septin-native-clathrin_coated_endocytic_vesicle_membrane-verify
  - septin-native-clathrin_coated_endocytic_vesicle_membrane-causal
- assessment_id: septin-clathrin_coated_endocytic_vesicle_membrane-images
  area: scope
  topic: No maintained images or numerical measurements
  outcome: not_applicable
  summary: No target image, measurement or verbatim source snippet is declared. Reading
    source captions and text is not image-pixel, supplementary movie or raw microscopy
    analysis.
  target_ids:
  - GO:0030669
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle_membrane
- assessment_id: septin-clathrin_coated_endocytic_vesicle-taxon
  area: scope
  topic: Species identity and yeast experimental model
  outcome: supported
  summary: Native taxonomy verifies S. cerevisiae. Newpher directly supports recruitment
    dynamics at cortical endocytic sites, with wild-type and mutant/drug-treated observations
    distinguished. COMMON remains qualitative occurrence context, not a frequency
    measured across strains or conditions. Canonical notes name the endocytic-site
    model, not a strain-general sealed-vesicle assay.
  target_ids:
  - GO:0045334
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle
  - septin-go
  - septin-newpher-meta
  - septin-newpher-duke
  - septin-tax4932
- assessment_id: septin-clathrin_coated_endocytic_vesicle-sealed-transition
  area: evidence
  topic: Direct sealed-lumen and coat-retention endpoint
  outcome: unknown
  summary: Newpher Discussion explicitly cannot distinguish clathrin disassembly before
    budding from departure of a clathrin-bearing vesicle or bud out of the TIRF field.
    It does not directly resolve sealed lumen or coat retention after release. The
    lumen formation wording is retained as endocytic-site model context, not a claim
    that fluorescence puncta resolved closure. Generic structural identity/topology
    has independent native GO support.
  target_ids:
  - GO:0045334
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle
  - septin-go
  - septin-newpher-meta
  - septin-newpher-duke
- assessment_id: septin-clathrin_coated_endocytic_vesicle-adapter
  area: scope
  topic: Narrative molecular/pathway applicability and species coverage
  outcome: not_applicable
  summary: All three records mention clathrin and adaptor recruitment in their yeast-model
    narrative; whole vesicle and membrane additionally name clathrin-dependent endocytosis.
    Thus absence of transcriptomic assertions is not an exemption, even for the lumen
    label. The fresh complete catalogue lacks a matching S. cerevisiae dataset, so
    no downstream gene/module query applies. Historical runner unavailability remains
    separately dated.
  target_ids:
  - GO:0045334
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle
  - septin-go
  - septin-newpher-meta
  - septin-newpher-duke
  - septin-review-policy
  - septin-catalogue
  - septin-historical-adapter-runner
- assessment_id: septin-clathrin_coated_endocytic_vesicle-provenance
  area: provenance
  topic: Actual primary body and abstract access tiers
  outcome: supported
  summary: Newpher fresh Duke PDF was inspected only at declared body/table/methods
    sections and text captions; no pixels or movies. Kaksonen, where cited by whole
    and membrane, was checked at complete primary abstract only after public body
    routes failed. Original October access dates are historical; current observations
    are genuinely fetched November3.
  target_ids:
  - GO:0045334
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle
  - septin-go
  - septin-newpher-meta
  - septin-newpher-duke
  - septin-kaksonen-meta
  - septin-access-extra-receipts
- assessment_id: septin-clathrin_coated_endocytic_vesicle-necessity
  area: scope
  topic: Formation dependence versus structural constitution
  outcome: unknown
  summary: No individual protein, adaptor or lipid is assigned a tested formation
    requirement by these target records. Generic membrane material can be constitutionally
    necessary without requiring clathrin for every endocytic vesicle. The source does
    not turn recruitment/localization into universal assembly necessity.
  target_ids:
  - GO:0045334
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle
  - septin-go
  - septin-newpher-meta
  - septin-newpher-duke
  - septin-curation-policy
  - septin-kaksonen-meta
- assessment_id: septin-clathrin_coated_endocytic_vesicle-verdict
  area: consistency
  topic: Qualified positive scientific assessment
  outcome: supported
  summary: pass_with_limitations remains supported for identity, hierarchy, bounded
    yeast-model scope and nonmechanistic topology. The unresolved sealed-vesicle transition
    and individual formation dependencies remain explicit. There are no original scientific
    findings/actions and no new concrete record-curation defect established in this
    scope.
  target_ids:
  - GO:0045334
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle
  - septin-go
  - septin-newpher-meta
  - septin-newpher-duke
  - septin-original-clathrin_coated_endocytic_vesicle
- assessment_id: septin-clathrin_coated_endocytic_vesicle-completeness
  area: completeness
  topic: Target-specific composition and neighboring scope
  outcome: supported
  summary: Entire target is reviewed. Generic sibling and coat neighbors supply only
    boundary/component responsibility context. Optional protein inventories, cargo
    lists, measurements and images are not required for a whole vesicle or spatial/bilayer
    part. No neighbor, grouped issue or category finding is terminally resolved.
  target_ids:
  - GO:0045334
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle
  - septin-go
  - septin-newpher-meta
  - septin-newpher-duke
  - septin-context-clathrin_coated_vesicle
  - septin-context-clathrin_coated_vesicle_lumen
  - septin-context-clathrin_coated_vesicle_membrane
  - septin-context-clathrin_coat_of_endocytic_vesicle
- assessment_id: septin-clathrin_coated_endocytic_vesicle_lumen-taxon
  area: scope
  topic: Species identity and yeast experimental model
  outcome: supported
  summary: Native taxonomy verifies S. cerevisiae. Newpher directly supports recruitment
    dynamics at cortical endocytic sites, with wild-type and mutant/drug-treated observations
    distinguished. COMMON remains qualitative occurrence context, not a frequency
    measured across strains or conditions. Canonical notes name the endocytic-site
    model, not a strain-general sealed-vesicle assay.
  target_ids:
  - GO:0106176
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle_lumen
  - septin-go
  - septin-newpher-meta
  - septin-newpher-duke
  - septin-tax4932
- assessment_id: septin-clathrin_coated_endocytic_vesicle_lumen-sealed-transition
  area: evidence
  topic: Direct sealed-lumen and coat-retention endpoint
  outcome: unknown
  summary: Newpher Discussion explicitly cannot distinguish clathrin disassembly before
    budding from departure of a clathrin-bearing vesicle or bud out of the TIRF field.
    It does not directly resolve sealed lumen or coat retention after release. The
    lumen formation wording is retained as endocytic-site model context, not a claim
    that fluorescence puncta resolved closure. Generic structural identity/topology
    has independent native GO support.
  target_ids:
  - GO:0106176
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle_lumen
  - septin-go
  - septin-newpher-meta
  - septin-newpher-duke
- assessment_id: septin-clathrin_coated_endocytic_vesicle_lumen-adapter
  area: scope
  topic: Narrative molecular/pathway applicability and species coverage
  outcome: not_applicable
  summary: All three records mention clathrin and adaptor recruitment in their yeast-model
    narrative; whole vesicle and membrane additionally name clathrin-dependent endocytosis.
    Thus absence of transcriptomic assertions is not an exemption, even for the lumen
    label. The fresh complete catalogue lacks a matching S. cerevisiae dataset, so
    no downstream gene/module query applies. Historical runner unavailability remains
    separately dated.
  target_ids:
  - GO:0106176
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle_lumen
  - septin-go
  - septin-newpher-meta
  - septin-newpher-duke
  - septin-review-policy
  - septin-catalogue
  - septin-historical-adapter-runner
- assessment_id: septin-clathrin_coated_endocytic_vesicle_lumen-provenance
  area: provenance
  topic: Actual primary body and abstract access tiers
  outcome: supported
  summary: Newpher fresh Duke PDF was inspected only at declared body/table/methods
    sections and text captions; no pixels or movies. Kaksonen, where cited by whole
    and membrane, was checked at complete primary abstract only after public body
    routes failed. Original October access dates are historical; current observations
    are genuinely fetched November3.
  target_ids:
  - GO:0106176
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle_lumen
  - septin-go
  - septin-newpher-meta
  - septin-newpher-duke
- assessment_id: septin-clathrin_coated_endocytic_vesicle_lumen-necessity
  area: scope
  topic: Formation dependence versus structural constitution
  outcome: unknown
  summary: No individual protein, adaptor or lipid is assigned a tested formation
    requirement by these target records. Generic membrane material can be constitutionally
    necessary without requiring clathrin for every endocytic vesicle. The source does
    not turn recruitment/localization into universal assembly necessity.
  target_ids:
  - GO:0106176
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle_lumen
  - septin-go
  - septin-newpher-meta
  - septin-newpher-duke
  - septin-curation-policy
- assessment_id: septin-clathrin_coated_endocytic_vesicle_lumen-verdict
  area: consistency
  topic: Qualified positive scientific assessment
  outcome: supported
  summary: pass_with_limitations remains supported for identity, hierarchy, bounded
    yeast-model scope and nonmechanistic topology. The unresolved sealed-vesicle transition
    and individual formation dependencies remain explicit. There are no original scientific
    findings/actions and no new concrete record-curation defect established in this
    scope.
  target_ids:
  - GO:0106176
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle_lumen
  - septin-go
  - septin-newpher-meta
  - septin-newpher-duke
  - septin-original-clathrin_coated_endocytic_vesicle_lumen
- assessment_id: septin-clathrin_coated_endocytic_vesicle_lumen-completeness
  area: completeness
  topic: Target-specific composition and neighboring scope
  outcome: supported
  summary: Entire target is reviewed. Generic sibling and coat neighbors supply only
    boundary/component responsibility context. Optional protein inventories, cargo
    lists, measurements and images are not required for a whole vesicle or spatial/bilayer
    part. No neighbor, grouped issue or category finding is terminally resolved.
  target_ids:
  - GO:0106176
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle_lumen
  - septin-go
  - septin-newpher-meta
  - septin-newpher-duke
  - septin-context-clathrin_coated_vesicle
  - septin-context-clathrin_coated_vesicle_lumen
  - septin-context-clathrin_coated_vesicle_membrane
  - septin-context-clathrin_coat_of_endocytic_vesicle
- assessment_id: septin-clathrin_coated_endocytic_vesicle_membrane-taxon
  area: scope
  topic: Species identity and yeast experimental model
  outcome: supported
  summary: Native taxonomy verifies S. cerevisiae. Newpher directly supports recruitment
    dynamics at cortical endocytic sites, with wild-type and mutant/drug-treated observations
    distinguished. COMMON remains qualitative occurrence context, not a frequency
    measured across strains or conditions. Canonical notes name the endocytic-site
    model, not a strain-general sealed-vesicle assay.
  target_ids:
  - GO:0030669
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle_membrane
  - septin-go
  - septin-newpher-meta
  - septin-newpher-duke
  - septin-tax4932
- assessment_id: septin-clathrin_coated_endocytic_vesicle_membrane-sealed-transition
  area: evidence
  topic: Direct sealed-lumen and coat-retention endpoint
  outcome: unknown
  summary: Newpher Discussion explicitly cannot distinguish clathrin disassembly before
    budding from departure of a clathrin-bearing vesicle or bud out of the TIRF field.
    It does not directly resolve sealed lumen or coat retention after release. The
    lumen formation wording is retained as endocytic-site model context, not a claim
    that fluorescence puncta resolved closure. Generic structural identity/topology
    has independent native GO support.
  target_ids:
  - GO:0030669
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle_membrane
  - septin-go
  - septin-newpher-meta
  - septin-newpher-duke
- assessment_id: septin-clathrin_coated_endocytic_vesicle_membrane-adapter
  area: scope
  topic: Narrative molecular/pathway applicability and species coverage
  outcome: not_applicable
  summary: All three records mention clathrin and adaptor recruitment in their yeast-model
    narrative; whole vesicle and membrane additionally name clathrin-dependent endocytosis.
    Thus absence of transcriptomic assertions is not an exemption, even for the lumen
    label. The fresh complete catalogue lacks a matching S. cerevisiae dataset, so
    no downstream gene/module query applies. Historical runner unavailability remains
    separately dated.
  target_ids:
  - GO:0030669
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle_membrane
  - septin-go
  - septin-newpher-meta
  - septin-newpher-duke
  - septin-review-policy
  - septin-catalogue
  - septin-historical-adapter-runner
- assessment_id: septin-clathrin_coated_endocytic_vesicle_membrane-provenance
  area: provenance
  topic: Actual primary body and abstract access tiers
  outcome: supported
  summary: Newpher fresh Duke PDF was inspected only at declared body/table/methods
    sections and text captions; no pixels or movies. Kaksonen, where cited by whole
    and membrane, was checked at complete primary abstract only after public body
    routes failed. Original October access dates are historical; current observations
    are genuinely fetched November3.
  target_ids:
  - GO:0030669
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle_membrane
  - septin-go
  - septin-newpher-meta
  - septin-newpher-duke
  - septin-kaksonen-meta
  - septin-access-extra-receipts
- assessment_id: septin-clathrin_coated_endocytic_vesicle_membrane-necessity
  area: scope
  topic: Formation dependence versus structural constitution
  outcome: unknown
  summary: No individual protein, adaptor or lipid is assigned a tested formation
    requirement by these target records. Generic membrane material can be constitutionally
    necessary without requiring clathrin for every endocytic vesicle. The source does
    not turn recruitment/localization into universal assembly necessity.
  target_ids:
  - GO:0030669
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle_membrane
  - septin-go
  - septin-newpher-meta
  - septin-newpher-duke
  - septin-curation-policy
  - septin-kaksonen-meta
- assessment_id: septin-clathrin_coated_endocytic_vesicle_membrane-verdict
  area: consistency
  topic: Qualified positive scientific assessment
  outcome: supported
  summary: pass_with_limitations remains supported for identity, hierarchy, bounded
    yeast-model scope and nonmechanistic topology. The unresolved sealed-vesicle transition
    and individual formation dependencies remain explicit. There are no original scientific
    findings/actions and no new concrete record-curation defect established in this
    scope.
  target_ids:
  - GO:0030669
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle_membrane
  - septin-go
  - septin-newpher-meta
  - septin-newpher-duke
  - septin-original-clathrin_coated_endocytic_vesicle_membrane
- assessment_id: septin-clathrin_coated_endocytic_vesicle_membrane-completeness
  area: completeness
  topic: Target-specific composition and neighboring scope
  outcome: supported
  summary: Entire target is reviewed. Generic sibling and coat neighbors supply only
    boundary/component responsibility context. Optional protein inventories, cargo
    lists, measurements and images are not required for a whole vesicle or spatial/bilayer
    part. No neighbor, grouped issue or category finding is terminally resolved.
  target_ids:
  - GO:0030669
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle_membrane
  - septin-go
  - septin-newpher-meta
  - septin-newpher-duke
  - septin-context-clathrin_coated_vesicle
  - septin-context-clathrin_coated_vesicle_lumen
  - septin-context-clathrin_coated_vesicle_membrane
  - septin-context-clathrin_coat_of_endocytic_vesicle
- assessment_id: septin-clathrin_coated_endocytic_vesicle-identity
  area: identity
  topic: Whole endocytic-coated vesicle and dual parentage
  outcome: supported
  summary: GO0045334 identifies the whole plasma-membrane-derived clathrin-coated
    endocytic vesicle, with GO0030136 and GO0030139 as independent is-a parents. Named
    coat GO0030128 and membrane GO0030669 are parts, not synonyms of the whole. The
    endocytic class is distinct from clathrin traffic at internal TGN/endosomal sites.
  target_ids:
  - GO:0045334
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle
  - septin-go
  - septin-go-edit
  - septin-ancestors-0045334
  - septin-newpher-duke
- assessment_id: septin-clathrin_coated_endocytic_vesicle-components
  area: grounding
  topic: Parts versus lower-level constituents
  outcome: supported
  summary: Whole-vesicle has_part names the coat and membrane and intentionally leaves
    chains, adaptors and lipids to those substructure records. This does not require
    a duplicate protein inventory or imply every endocytic carrier must depend on
    clathrin for formation.
  target_ids:
  - GO:0045334
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle
  - septin-go
  - septin-curation-policy
  - septin-context-clathrin_coat_of_endocytic_vesicle
  - septin-context-clathrin_coated_vesicle_membrane
- assessment_id: septin-clathrin_coated_endocytic_vesicle-graph
  area: graph
  topic: Five nonmechanistic parthood, bounds and participation edges
  outcome: supported
  summary: 'All five edges are supported at their stated scope: coat part_of membrane
    and whole, membrane part_of and bounds whole, whole participates in named endocytic
    process. Official GO source has the membrane bounding_layer_of axiom. No complete
    adaptor assembly, cargo selection or actin-driven scission mechanism is asserted.'
  target_ids:
  - GO:0045334
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle
  - septin-go
  - septin-go-edit
  - septin-graph-policy
  - septin-newpher-duke
  - septin-kaksonen-meta
- assessment_id: septin-clathrin_coated_endocytic_vesicle_lumen-identity
  area: identity
  topic: Endocytic-specific lumen and generic-lumen parent
  outcome: supported
  summary: GO0106176 denotes enclosed volume, not cargo. It is_a GO0071682 and part_of
    GO0045334. The local generic clathrin-coated-vesicle lumen parent is a broader
    class, supported by its frozen definition and UniProtSL0319; nested parent GO
    mappings do not give SL0319 a direct GO0106176 identity.
  target_ids:
  - GO:0106176
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle_lumen
  - septin-go
  - septin-go-edit
  - septin-ancestors-0106176
  - septin-SL-0319
  - septin-context-clathrin_coated_vesicle_lumen
- assessment_id: septin-clathrin_coated_endocytic_vesicle_lumen-composition
  area: grounding
  topic: Spatial region without invariant cargo composition
  outcome: supported
  summary: The bounded lumen is intentionally not a fixed cargo or protein complex.
    Empty components and exclusion of variable internalized cargo are coherent with
    its native definition; absence of a detailed molecular inventory is not a required
    correction.
  target_ids:
  - GO:0106176
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle_lumen
  - septin-go
  - septin-curation-policy
- assessment_id: septin-clathrin_coated_endocytic_vesicle_lumen-graph
  area: graph
  topic: Two descriptive lumen containment/enclosure edges
  outcome: supported
  summary: The lumen is part of the whole vesicle, and membrane bounds the lumen.
    The latter follows its explicit enclosed-volume definition; it does not make the
    membrane identical to cargo or assert how closure/scission occurs. Both graph
    edges are NONMECHANISTIC.
  target_ids:
  - GO:0106176
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle_lumen
  - septin-go
  - septin-go-edit
  - septin-graph-policy
- assessment_id: septin-clathrin_coated_endocytic_vesicle_membrane-identity
  area: identity
  topic: Exact bilayer, dual membrane parents and protein-coat part
  outcome: supported
  summary: GO0030669 is the bilayer around the whole endocytic coated vesicle, with
    clathrin-coated membrane and endocytic membrane parents. GO0030128 is explicitly
    a part in the native ontology and remains a separately named protein coat, not
    lipid material.
  target_ids:
  - GO:0030669
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle_membrane
  - septin-go
  - septin-go-edit
  - septin-ancestors-0030669
  - septin-context-clathrin_coat_of_endocytic_vesicle
- assessment_id: septin-clathrin_coated_endocytic_vesicle_membrane-material
  area: grounding
  topic: Collective constitutional bilayer and label-only grounding
  outcome: supported
  summary: The single LIPID row is collective bilayer material, not an exact lipid
    molecule. REVIEWED_LABEL_ONLY avoids using whole-location GO0030669 as a chemical
    identity. ESSENTIAL is constitutional at that collective scale; the open grounding
    TODO is uncertainty, not evidence no suitable term exists.
  target_ids:
  - GO:0030669
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle_membrane
  - septin-go
  - septin-curation-policy
- assessment_id: septin-clathrin_coated_endocytic_vesicle_membrane-graph
  area: graph
  topic: Four descriptive edges and material component linkage
  outcome: supported
  summary: All four edges retain coat parthood, membrane parthood/bounds and whole-vesicle
    process participation. GO source directly supports the bounding_layer_of and coat
    part_of relations. The membrane component_ref links its collective bilayer material
    rather than assigning a lipid identity to the protein coat or complete multisubstructure
    vesicle. No molecular necessity mechanism is introduced.
  target_ids:
  - GO:0030669
  evidence_ids:
  - septin-record-clathrin_coated_endocytic_vesicle_membrane
  - septin-go
  - septin-go-edit
  - septin-graph-policy
  - septin-kaksonen-meta
- assessment_id: current-input-comparison
  area: provenance
  topic: Complete frozen-input comparison and bounded refresh
  outcome: supported
  summary: 0 of ten original target hashes differ from current main. The changed content
    is substantively reassessed in the target-specific assessments; original observations
    remain historical and unchanged. All current target and used context bytes are
    frozen.
  target_ids:
  - GO:0033106
  - GO:0045334
  - GO:0106176
  - GO:0030669
  - GO:0030136
  - cellstructuremech:clathrin_coated_vesicle_lumen
  - GO:0030665
  - GO:0030135
  - GO:0030662
  - cellstructuremech:coccolith_vesicle
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
  issue_key: cis-golgi-network-membrane-ppy12-current-taxon
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: The cited PPY1/PPY12 lineage has the wrong current species
  description: Rossanese1999 used PPY1 and its isogenic PPY12 derivatives. ATCC identifies
    PPY12 as K. phaffii after sequence-based reidentification; ENA LC815816.1 independently
    pairs PPY12 with taxon460519. The maintained occurrence and canonical-example
    fields instead assign that experiment to K. pastoris4922. Historical Pichia pastoris
    nomenclature alone does not justify that current species assignment.
  target_ids:
  - GO:0033106
  field_paths:
  - taxonomic_distribution[0].taxon_id
  - taxonomic_distribution[0].taxon_label
  - canonical_examples[0].taxon_id
  - canonical_examples[0].taxon_label
  evidence_ids:
  - micro-record-cis_golgi_network_membrane
  - micro-cis-jats-PMC2148216
  - micro-cis-atcc-204163
  - micro-cis-ena-LC815816
  - micro-cis-tax-4922
  - micro-cis-tax-460519
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cis_golgi_network_membrane.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: major
  normalization_reason: Major because the source-based occurrence and canonical example
    have a materially incorrect experimental taxon, while generic membrane identity
    is valid.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T111327Z-cis-golgi-network-membrane-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2665
- finding_id: micro-F2
  issue_key: cis-golgi-network-membrane-stack-study-evidence-scope
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: The stack study does not directly establish a CGN-membrane example
  description: The sole source attached to this membrane occurrence and canonical
    example resolves ordered Golgi stacks near transitional ER. Native GO distinguishes
    CGN from the Golgi stack; the study assigns its observed Sec13-positive tubulovesicular
    interface to tER. Stack membranes or early-Golgi marker apposition therefore do
    not directly identify the particular CGN membrane asserted by these fields. The
    scope gap persists after correcting the species.
  target_ids:
  - GO:0033106
  field_paths:
  - taxonomic_distribution[0]
  - canonical_examples[0]
  evidence_ids:
  - micro-record-cis_golgi_network_membrane
  - micro-cis-go
  - micro-cis-jats-PMC2148216
  - micro-cis-cho2000-meta
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cis_golgi_network_membrane.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: major
  normalization_reason: Major because the only asserted occurrence and canonical example
    overextend the cited study to a distinct compartment membrane; generic GO identity
    and topology remain sound.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T111327Z-cis-golgi-network-membrane-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2666
- finding_id: micro-F3
  issue_key: coated-vesicle-ret1-query-uniqueness
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Qualify the RET1 protein-example uniqueness claim
  description: The current reviewed exact-gene/taxon query for RET1 in S288C returns
    P53622 (primary COP1; RET1 synonym) and P22276 (primary RET1; RNA polymerase III
    subunit). P53622 is the correct representative alpha-coatomer example, as its
    role already states, but its evidence note calls it the single reviewed RET1 entry.
    The finding concerns this present unsupported uniqueness wording; it does not
    establish what a historical query returned.
  target_ids:
  - GO:0030135
  field_paths:
  - components#coat_proteins.protein_examples[5].evidence[0].notes
  evidence_ids:
  - micro-record-coated_vesicle
  - micro-UniProtKB-P53622
  - micro-UniProtKB-P22276
  - micro-query-RET1-559292
  - micro-query-COP1-559292
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/coated_vesicle.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: minor
  normalization_reason: Minor because the accession, taxon, primary gene and representative
    identity are correct; one evidence note overstates uniqueness.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T111333Z-coated-vesicle-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2667
actions:
- action_id: micro-A1
  finding_ids:
  - micro-F1
  target_ids:
  - GO:0033106
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cis_golgi_network_membrane.yaml
    role: maintained scientific record
  description: Correct any retained PPY1/PPY12 experimental attribution to K. phaffii460519
    using the explicit strain bridge and retain the historical name in notes. Independently
    resolve the CGN-membrane evidence gap before retaining the study as a confirmed
    example.
  acceptance_checks:
  - Any retained experimental attribution uses the verified current taxon and documented
    strain provenance.
  - Retaxonomizing the strain is not treated as proof of CGN-membrane occurrence.
  - Focused native validators pass.
  - Scientific edits belong to a separate authorized guarded-writer curation PR with
    event/history and native checks; no record is changed in this review PR.
- action_id: micro-A2
  finding_ids:
  - micro-F2
  target_ids:
  - GO:0033106
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cis_golgi_network_membrane.yaml
    role: maintained scientific record
  description: Supply direct evidence for the CGN membrane in the asserted organism,
    or remove/defer the occurrence/example and retain Rossanese as explicitly broader
    Golgi-stack/tER context. Do not infer absence of CGN from the evidence gap or
    replace the exact membrane identity with a whole-stack concept.
  acceptance_checks:
  - Retained occurrence and canonical-example evidence distinguishes CGN membrane
    from generic stack membranes and tER.
  - The example does not rest solely on ordered stacks or early-Golgi marker localization.
  - The independent current-taxon mismatch is resolved for retained experimental attributions.
  - Focused native validators pass.
  - Scientific edits belong to a separate authorized guarded-writer curation PR with
    event/history and native checks; no record is changed in this review PR.
- action_id: micro-A3
  finding_ids:
  - micro-F3
  target_ids:
  - GO:0030135
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/coated_vesicle.yaml
    role: maintained scientific record
  description: Retain P53622/COP1 and explain that legacy RET1 was disambiguated by
    the coatomer protein identity; remove the unsupported single-entry wording or
    explicitly use the unique COP1 query with a refreshed retrieval note.
  acceptance_checks:
  - The current note does not claim RET1 uniquely identifies P53622.
  - The correct coatomer accession and taxon remain unchanged.
  - The note distinguishes current verification from historical retrieval.
  - Focused native validation passes.
  - Scientific edits belong to a separate authorized guarded-writer curation PR with
    event/history and native checks; no record is changed in this review PR.
limitations:
- 'Generic clathrin-coated vesicle, lumen, membrane and coccolith vesicle independent
  subreview: Assigned four records only; all four frozen target hashes remain unchanged.
  Three additional neighbors were frozen before boundary/component-label inspection
  and are not fully reviewed or terminally disposed of.'
- 'Generic clathrin-coated vesicle, lumen, membrane and coccolith vesicle independent
  subreview: Newpher2005 is a genuine fresh primary PDF, text of pp87–96 including
  Methods and figure captions. No figure pixels, movies, supplementary experiments
  or raw quantitative data were reanalyzed. The primary paper cannot distinguish pre-budding
  clathrin loss from departure of coated vesicles from the surface field.'
- 'Generic clathrin-coated vesicle, lumen, membrane and coccolith vesicle independent
  subreview: Kaksonen2005 support is the complete primary abstract only; attempted
  CORE/publisher/PDF routes were403 and the ElsevierAPI is bibliographic metadata.
  Newpher DOI redirect response is not its body; the separate institutional PDF supplies
  actual body access.'
- 'Generic clathrin-coated vesicle, lumen, membrane and coccolith vesicle independent
  subreview: Yeast COMMON scope is qualitative; reporter recruitment does not directly
  image a sealed lumen or establish individual assembly necessity. Constitutional
  collective bilayer differs from necessity of each lipid species.'
- 'Generic clathrin-coated vesicle, lumen, membrane and coccolith vesicle independent
  subreview: Avrahami2026 scientific sec1–4 and source captions were read in full;
  supplementary Methods were read through FIB-SEM data processing, not audited in
  entirety. Sviben2016 scope is Results sec4–6, Discussion sec7 and culture Methods
  sec9.'
- 'Generic clathrin-coated vesicle, lumen, membrane and coccolith vesicle independent
  subreview: Only the maintained Figure2 pixels were viewed. Figure3–7 captions were
  text evidence; cryo-ET, XRF maps, raw reconstructions and supplementary microscopy
  were not reanalyzed. Fresh Figure2 bytes, metadata, authors and ALI CC-BY4.0 match
  the frozen record.'
- 'Generic clathrin-coated vesicle, lumen, membrane and coccolith vesicle independent
  subreview: Current authority searches retain exact bounds: two coccolith queries
  return0; clathrin-lumen query inspected first100 of651 hits and does not certify
  exhaustive absence. A narrower endocytic-lumen term is not the exact broader target.
  Historical record searches and issue resolutions are not recertified.'
- 'Generic clathrin-coated vesicle, lumen, membrane and coccolith vesicle independent
  subreview: Fresh complete structured-source catalogue lacks matched yeast/coccolithophore
  hosts. No downstream matched-dataset query applies and no biological absence follows.
  Historical00:49Z OS-access runner failure is retained, not a new invocation or success.'
- 'Generic clathrin-coated vesicle, lumen, membrane and coccolith vesicle independent
  subreview: Clathrin lumen has explicit molecular recruitment narratives despite
  sparse geometry, so it belongs among the three applicability corrections. Coccolith
  is genuinely excluded because candidate molecular identities and mechanisms are
  expressly unasserted; its N/A outcome remains with a precise rationale.'
- 'Generic clathrin-coated vesicle, lumen, membrane and coccolith vesicle independent
  subreview: All eight native protein commands pass empty inventories and zero typed
  protein nodes. They cannot verify narrative molecular identity, localization, function
  or necessity. Root owns full-corpus gates, issue deduplication/publication and all
  repository/GitHub writes.'
- 'Cis-Golgi network membrane, coated vesicle and coated vesicle membrane independent
  subreview: Assigned scope comprises cis-Golgi network membrane, coated vesicle and
  coated vesicle membrane. All are unchanged. Six frozen neighbors were read only
  at declared boundary fields; their scientific findings and category/group issues
  are not resolved or conflated.'
- 'Cis-Golgi network membrane, coated vesicle and coated vesicle membrane independent
  subreview: Cis-Golgi sources reuse verified unchanged10:11Z public snapshots from
  the immediately prior review. Rossanese full Results/Discussion and Strains and
  Plasmids Methods were previously inspected and the strain/interface passages reread
  here; no new source download, figure-pixel audit or broader full-Methods/supplement
  scope is claimed. ATCC and ENA identify strain only.'
- 'Cis-Golgi network membrane, coated vesicle and coated vesicle membrane independent
  subreview: Cho2000 remains complete primary abstract only; historical attempted
  body/PDF403 remains an access limitation. It concerns S. cerevisiae early-Golgi
  membranes and does not directly establish K. phaffii CGN membrane occurrence.'
- 'Cis-Golgi network membrane, coated vesicle and coated vesicle membrane independent
  subreview: Barlowe1994 is current complete primary abstract/bibliography only. Current
  publisher and ScienceDirect requests returned403. Matsuoka author-hosted PDF is
  genuinely readable at the exact selected pages/sections declared; neither source
  is represented as a full-paper/raw-data or image-pixel audit.'
- 'Cis-Golgi network membrane, coated vesicle and coated vesicle membrane independent
  subreview: Newpher2005 current institutional PDF was read at pp87-89 Summary/Introduction/Table1/Localization
  subsection/Figure1 caption only; no later experiments, movies or pixels were reanalyzed.
  Yu2012 current genuine JATS was read at complete Introduction and two declared Results/model
  subsections, not full Methods/figures/raw data.'
- 'Cis-Golgi network membrane, coated vesicle and coated vesicle membrane independent
  subreview: Rout2000 and Huh2003 are complete primary abstract only plus exact UniProt
  source annotations. The record explicitly identifies nuclear-pore and Golgi-membrane
  annotations; these are not direct vesicle-membership experiments.'
- 'Cis-Golgi network membrane, coated vesicle and coated vesicle membrane independent
  subreview: S288C protein examples are representative identity anchors, not asserted
  experimental strain matches for RSY445 or every source. Current query uniqueness
  is bounded to seven exact symbols/taxon559292/reviewed filters and does not certify
  historical results. Protein/domain matches do not identify a universal composite
  coat family.'
- 'Cis-Golgi network membrane, coated vesicle and coated vesicle membrane independent
  subreview: Current catalogue returned no matching yeast dataset. Historical runner
  PermissionError occurred00:49Z and was not rerun here; current fallback is separately
  timestamped. Absence of a matching dataset is not biological absence or a fabricated
  downstream gene/module check.'
- 'Cis-Golgi network membrane, coated vesicle and coated vesicle membrane independent
  subreview: Six native protein commands passed; two membrane targets have empty inventories/zero
  protein nodes and whole coated vesicle has six examples/one COVERED node. Native
  success does not repair unsupported prose or establish assembly necessity.'
- 'Cis-Golgi network membrane, coated vesicle and coated vesicle membrane independent
  subreview: No assigned target contains an image or numerical property requiring
  pixel/measurement inspection. The other cohort coccolith image is outside this subreview.
  Root owns full local QC, global authority checks, issue deduplication/publication
  and final integration; no future final-head CI claim is made.'
- 'Clathrin-coated endocytic vesicle, lumen and membrane independent subreview: Assigned
  three unchanged endocytic clathrin targets only. All original bundles validate/render
  exactly and target hashes equal original frozen/source bytes. No original scientific
  findings or request-curation actions exist.'
- 'Clathrin-coated endocytic vesicle, lumen and membrane independent subreview: Fresh
  Newpher publisher-format Duke PDF was inspected at declared Summary/Introduction,
  Table1, selected Results, Discussion and Experimental Procedures/Microscopy text
  on printed pp87–96. Captions are text only; no figure pixels, supplementary movies
  or raw microscopy were reanalysed.'
- 'Clathrin-coated endocytic vesicle, lumen and membrane independent subreview: Newpher
  does not resolve clathrin disassembly before budding versus departure of a clathrin-bearing
  vesicle/bud outside the TIRF field. The yeast example is a recruitment/endocytic-site
  model, not direct visualization of a sealed lumen or universal retained coat.'
- 'Clathrin-coated endocytic vesicle, lumen and membrane independent subreview: Kaksonen
  primary support is complete native abstract and bibliography only. Publisher PDF
  and CORE routes returned403; no full Methods/Results body or figure audit is claimed.
  Its clathrin-necessity result remains specific to the studied yeast assay.'
- 'Clathrin-coated endocytic vesicle, lumen and membrane independent subreview: Formal
  GO bounding_layer_of and coat part_of assertions were read directly from four selected
  official source-ontology stanzas after the OLS route returned404. No whole-ontology
  audit or inference from failed access is made.'
- 'Clathrin-coated endocytic vesicle, lumen and membrane independent subreview: Species
  identity and qualitative COMMON scope do not establish prevalence across strains/conditions.
  Source wt reporter, mutant and drug-treated observations are kept distinct; neighbor
  protein accessions are context only, not independently audited target claims.'
- 'Clathrin-coated endocytic vesicle, lumen and membrane independent subreview: All
  three targets contain actual clathrin/adaptor narrative despite zero typed protein
  nodes; even the lumen merits applicability assessment. The complete current catalogue
  has no matched S. cerevisiae dataset. No unrelated taxon query or absence-of-biology
  inference is made. Historical runner failure remains00:49Z, not a fresh execution.'
- 'Clathrin-coated endocytic vesicle, lumen and membrane independent subreview: All
  six current protein commands pass empty inventories; they do not independently validate
  narrative molecules, localization, mechanism or formation necessity. Root owns global
  gates and final CI/queue checks.'
- 'Clathrin-coated endocytic vesicle, lumen and membrane independent subreview: Whole-vesicle
  constituent responsibility, collective membrane material and spatial lumen/cargo
  boundaries are distinct. No unsupported invariant protein/cargo inventory, exact
  lipid grounding or universal individual formation requirement is added.'
- 'Clathrin-coated endocytic vesicle, lumen and membrane independent subreview: Four
  frozen neighbors were inspected only for declared identity/boundary/component context.
  No historical grouped/category finding or neighboring record issue is terminally
  resolved. Repository/GitHub writes and issue deduplication/publication remain root-owned.'
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
  Each inherited scientific finding retains exact predecessor identity.
- All ten original target hashes match current main. No stale target review requires
  a content refresh, but current claim-level source reassessment and bundle corrections
  are recorded in this immutable successor.
- 'Issue #2664 tracks one omitted applicability assessment and eight unsupported expression-only
  exclusions. Clathrin lumen narratives name molecular recruitment and therefore require
  assessment; coccolith vesicle is a genuine exclusion because molecular identities
  and transport machinery are explicitly withheld.'
- Source commit cee44c9b340b36e4e103ebd16c4bfcf6745bd41f is retained by tag review-base/pr2360-current-record-followup-20261103.
- CLAUDE.md is an alias of AGENTS.md; canonical regular AGENTS.md bytes are frozen.
- All used local context was frozen before assessment, including nine neighbor records,
  the coccolith image, native configuration, graph/protein policies and verifier source.
  Neighbors are context only, not additional targets or dispositions of their findings.
- Fresh and reused public-source snapshots retain actual access dates and inspection
  tiers. Native authority identity does not independently establish localization,
  mechanistic action or assembly necessity.
- Native checks with empty protein inventories or zero GENE_OR_PROTEIN nodes do not
  validate molecules appearing only in narrative prose. The coated-vesicle graph has
  one covered molecular node linked to its represented component examples; that coverage
  does not establish query uniqueness or assembly necessity.
- 'The two major cis-Golgi network membrane findings concern current PPY12 species
  attribution and the distinction between whole-stack evidence and the specific CGN
  membrane. Related #2661 and #2662 concern the separate whole-network record; neither
  those issues nor #2663 are resolved here.'
- The minor coated-vesicle RET1 finding concerns exact query uniqueness. Valid representative
  accessions and their supported roles are preserved; primary symbol and synonym matches
  are distinguished.
- The coccolith source figure supports observed membrane geometry and reconstructed
  stages, not time-lapse continuity or specified transport machinery. Its attached
  image, strain context, modality and licence are independently assessed.
- All three inherited scientific findings remain open for separate record curation.
  Eight targets retain qualified positive scientific assessments. No record is edited.
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T111327Z-cis-golgi-network-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T111328Z-clathrin-coated-endocytic-vesicle-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T111329Z-clathrin-coated-endocytic-vesicle-lumen-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T111329Z-clathrin-coated-endocytic-vesicle-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T111330Z-clathrin-coated-vesicle-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T111331Z-clathrin-coated-vesicle-lumen-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T111332Z-clathrin-coated-vesicle-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T111333Z-coated-vesicle-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T111334Z-coated-vesicle-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T111335Z-coccolith-vesicle-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
links:
- https://github.com/CultureBotAI/CellStructureMech/pull/2360
- https://github.com/CultureBotAI/CellStructureMech/issues/2514
- https://github.com/CultureBotAI/CellStructureMech/issues/2664
- https://github.com/CultureBotAI/CellStructureMech/issues/2665
- https://github.com/CultureBotAI/CellStructureMech/issues/2666
- https://github.com/CultureBotAI/CellStructureMech/issues/2667
```
